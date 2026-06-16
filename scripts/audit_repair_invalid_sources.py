#!/usr/bin/env python3
"""Source-first invalid remote source audit and conservative repair.

Daily source of truth is Rules/, Scripts/, Rewrite/Sources/ and Rewrite/Remotes/.
This tool audits those source files first, repairs them after two confirmed
failures, then the workflow rebuilds Release and syncs the root module.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / "reports"
REPORT_PATH = REPORT_DIR / "invalid_sources_report.md"
HISTORY_PATH = REPORT_DIR / "invalid_sources_history.json"
SOURCES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
CANDIDATES_JSON = ROOT / "Rewrite" / "Remotes" / "candidates.json"
SOURCE_GLOBS = [
    "Rules/*.list",
    "Scripts/*.conf",
    "Rewrite/Sources/*.conf",
]
EXPECTED_UPDATE_URL = "https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"
USER_AGENT = "GrandpaNiu-InvalidSourceRepair/2.0 (+https://github.com/GrandpaNiuu/GrandpaNiu)"
TIMEOUT_SECONDS = 25
FAIL_THRESHOLD = 2
MAX_AUTO_COMMENTS = 20
MAX_AUTO_DELETES = 5
TRANSIENT_STATUS = {429, 500, 502, 503, 504}
URL_RE = re.compile(r"https?://[^\s\"'<>)\],]+")
SCRIPT_PATH_RE = re.compile(r"script-path=(https?://[^,\s]+)")
UPDATE_URL_RE = re.compile(r"^#!update-url=(https?://\S+)\s*$")
GITHUB_RAW_RE = re.compile(r"^https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.+)$")
GITHUB_BLOB_RE = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)$")
DOMAIN_SET_VALUE_RE = re.compile(r"^(?:\+\.)?(?:\*\.)?\.?[A-Za-z0-9_][A-Za-z0-9_.-]*[A-Za-z0-9_]$|^localhost$", re.I)
PROTECTED_PATTERNS = (
    "spotify-upstream",
    "Spotify_remove_ads.js",
    "youtube.response",
    "kelee.one/Tool/Loon/Lpx/Spotify_remove_ads.lpx",
    "kelee.one/Resource/JavaScript/Spotify/Spotify_remove_ads.js",
    "Maasea/sgmodule",
    "Ronghemokuai.sgmodule",
    EXPECTED_UPDATE_URL,
    "README.md",
    "redirect.html",
    "import.html",
)
DISALLOWED_REPLACEMENT_HOSTS = ("ghproxy", "mirror", "tinyurl.com", "bit.ly", "t.co", "shorturl")
HTML_ERROR_TOKENS = ("404 not found", "repository not found", "file not found", "there isn't a github pages site here")
RULE_FEATURES = ("DOMAIN", "DOMAIN-SUFFIX", "URL-REGEX", "RULE-SET", "DOMAIN-SET", "payload", "host-suffix")
RISK_PATTERNS = (
    "premium",
    "vip",
    "unlock",
    "crack",
    "bypass payment",
    "payment bypass",
    "login bypass",
    "cookie",
    "token",
    "authorization",
    "boxjs",
    "adult",
    "casino",
    "gambling",
    "ghproxy",
    "mirror",
    "tinyurl",
    "bit.ly",
    "t.co/",
    "shorturl",
    "会员",
    "破解",
    "解锁",
    "支付绕过",
    "登录绕过",
)


@dataclass(frozen=True)
class Source:
    url: str
    path: str
    line_number: int
    kind: str
    line: str
    json_group: str = ""
    json_index: int = -1


@dataclass
class Check:
    ok: bool
    confirmed_invalid: bool
    status: int | None = None
    final_url: str = ""
    error_type: str = ""
    content_type: str = ""
    content_length: int | None = None
    sample: str = ""

    @property
    def last_error(self) -> str:
        if self.status:
            return f"HTTP {self.status}" if not self.error_type else f"HTTP {self.status} {self.error_type}"
        return self.error_type or "UNKNOWN_ERROR"


def stop(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        stop(f"invalid json {path}: {exc}")


def write_json(path: Path, data: dict) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def clean_url(url: str) -> str:
    return url.rstrip(".,;")


def classify(line: str, url: str) -> str:
    stripped = line.strip()
    if SCRIPT_PATH_RE.search(line):
        return "script"
    if stripped.startswith("RULE-SET,"):
        return "rule-set"
    if stripped.startswith("DOMAIN-SET,"):
        return "domain-set"
    if UPDATE_URL_RE.match(stripped):
        return "update-url"
    if GITHUB_BLOB_RE.match(url):
        return "github-blob"
    if "raw.githubusercontent.com" in url or "githubusercontent.com" in url:
        return "raw"
    if "github.io" in urllib.parse.urlparse(url).netloc:
        return "github-pages"
    return "external"


def scan_text_file(path: Path) -> list[Source]:
    sources: list[Source] = []
    rel = path.relative_to(ROOT).as_posix()
    for idx, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        urls: list[str] = []
        match = SCRIPT_PATH_RE.search(line)
        if match:
            urls.append(match.group(1))
        update_match = UPDATE_URL_RE.match(line.strip())
        if update_match:
            urls.append(update_match.group(1))
        parts = [part.strip() for part in line.split(",")]
        if len(parts) >= 2 and parts[0] in {"RULE-SET", "DOMAIN-SET"} and parts[1].startswith("http"):
            urls.append(parts[1])
        urls.extend(URL_RE.findall(line))
        for raw in dict.fromkeys(urls):
            url = clean_url(raw)
            if "$" in url:
                continue
            sources.append(Source(url=url, path=rel, line_number=idx, kind=classify(line, url), line=line))
    return sources


def scan_json_registry(path: Path, group: str) -> list[Source]:
    data = read_json(path)
    sources: list[Source] = []
    for idx, item in enumerate(data.get(group, [])):
        url = str(item.get("url", "")).strip()
        if not url:
            continue
        kind = "rule-set" if item.get("type") == "RULE-SET" else "domain-set" if item.get("type") == "DOMAIN-SET" else str(item.get("kind", "external"))
        line = json.dumps(item, ensure_ascii=False)
        sources.append(Source(url=url, path=path.relative_to(ROOT).as_posix(), line_number=idx + 1, kind=kind, line=line, json_group=group, json_index=idx))
    return sources


def scan_sources() -> list[Source]:
    sources: list[Source] = []
    for pattern in SOURCE_GLOBS:
        for path in ROOT.glob(pattern):
            if path.is_file():
                sources.extend(scan_text_file(path))
    sources.extend(scan_json_registry(SOURCES_JSON, "rule_sets"))
    sources.extend(scan_json_registry(CANDIDATES_JSON, "candidates"))
    unique: dict[tuple[str, str, int], Source] = {}
    for source in sources:
        unique.setdefault((source.url, source.path, source.line_number), source)
    return list(unique.values())


def request_once(url: str, method: str) -> Check:
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if method == "GET":
        headers["Range"] = "bytes=0-4096"
    request = urllib.request.Request(url, headers=headers, method=method)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            body = response.read(4097) if method == "GET" else b""
            length_header = response.headers.get("Content-Length")
            content_length = int(length_header) if length_header and length_header.isdigit() else len(body) or None
            return Check(True, False, response.status, response.geturl(), "", response.headers.get("Content-Type", ""), content_length, body.decode("utf-8", errors="ignore")[:4096])
    except urllib.error.HTTPError as exc:
        body = exc.read(4097) if method == "GET" else b""
        return Check(False, exc.code in {404, 410}, exc.code, exc.geturl(), f"HTTP {exc.code}", exc.headers.get("Content-Type", "") if exc.headers else "", len(body) or None, body.decode("utf-8", errors="ignore")[:4096])
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        text = str(exc).lower()
        error_type = "TIMEOUT" if "timed out" in text else "DNS_ERROR" if "getaddrinfo" in text else type(exc).__name__
        return Check(False, False, None, url, error_type)


def is_html_error(check: Check) -> bool:
    sample = check.sample.lower()
    return "text/html" in check.content_type.lower() and any(token in sample for token in HTML_ERROR_TOKENS)


def check_source(source: Source) -> Check:
    head = request_once(source.url, "HEAD")
    needs_get = not head.ok or head.status is None or head.status >= 400 or head.content_length == 0 or "text/html" in head.content_type.lower()
    check = request_once(source.url, "GET") if needs_get else head
    if check.ok and check.status and 200 <= check.status < 400:
        if check.content_length == 0 and source.kind in {"script", "rule-set", "domain-set", "raw", "update-url"}:
            check.ok = False
            check.confirmed_invalid = True
            check.error_type = "EMPTY_CONTENT"
        elif is_html_error(check):
            check.ok = False
            check.confirmed_invalid = True
            check.error_type = "HTML_ERROR_PAGE"
    if check.status in TRANSIENT_STATUS:
        check.confirmed_invalid = False
    return check


def is_protected(source: Source) -> bool:
    haystack = f"{source.url}\n{source.line}"
    return any(token in haystack for token in PROTECTED_PATTERNS)


def load_history() -> dict[str, dict[str, object]]:
    if not HISTORY_PATH.exists():
        return {}
    return read_json(HISTORY_PATH)


def save_history(history: dict[str, dict[str, object]]) -> None:
    write_json(HISTORY_PATH, history)


def history_key(source: Source) -> str:
    return f"{source.path}::{source.url}"


def update_history(history: dict[str, dict[str, object]], sources: Iterable[Source], checks: dict[str, Check], today: str) -> dict[str, dict[str, object]]:
    current = {history_key(source): source for source in sources}
    updated = {key: value for key, value in history.items() if key in current}
    for key, source in current.items():
        check = checks[key]
        if check.ok or not check.confirmed_invalid:
            updated.pop(key, None)
            continue
        old = updated.get(key, {})
        updated[key] = {
            "url": source.url,
            "path": source.path,
            "first_failed_date": old.get("first_failed_date", today),
            "last_failed_date": today,
            "fail_count": int(old.get("fail_count", 0)) + 1,
            "last_error": check.last_error,
            "line_number": source.line_number,
            "line_preview": source.line.strip()[:240],
        }
    return updated


def valid_replacement_host(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    return not any(blocked in host for blocked in DISALLOWED_REPLACEMENT_HOSTS)


def github_repo_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    if parsed.netloc == "raw.githubusercontent.com" and len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    if parsed.netloc == "github.com" and len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    return ""


def trusted_repo_ok(url: str, trusted_repositories: set[str]) -> bool:
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme != "https" or not valid_replacement_host(url):
        return False
    repo = github_repo_from_url(url)
    return bool(repo and repo in trusted_repositories)


def has_risk_text(text: str) -> bool:
    lowered = text.lower()
    return any(token.lower() in lowered for token in RISK_PATTERNS)


def github_parts(url: str) -> tuple[str, str, str, str] | None:
    match = GITHUB_RAW_RE.match(url) or GITHUB_BLOB_RE.match(url)
    if not match:
        return None
    return match.groups()


def raw_url(owner: str, repo: str, branch: str, path: str) -> str:
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"


def source_type_policy(source: Source) -> tuple[str, str]:
    if source.json_group:
        try:
            item = json.loads(source.line)
        except json.JSONDecodeError:
            item = {}
        return str(item.get("type", "")).upper(), str(item.get("policy", "REJECT")).upper()
    parts = [part.strip() for part in source.line.split(",")]
    if len(parts) >= 3 and parts[0] in {"RULE-SET", "DOMAIN-SET"}:
        return parts[0].upper(), parts[2].upper()
    if source.kind == "rule-set":
        return "RULE-SET", "REJECT"
    if source.kind == "domain-set":
        return "DOMAIN-SET", "REJECT"
    return "", ""


def active_remote_urls(skip_url: str) -> set[str]:
    data = read_json(SOURCES_JSON)
    urls: set[str] = set()
    for item in data.get("rule_sets", []):
        url = str(item.get("url", "")).strip()
        if url and url != skip_url and item.get("enabled", False):
            urls.add(url)
    return urls


def candidate_pool_replacements(source: Source) -> list[str]:
    if source.kind not in {"rule-set", "domain-set"} and not source.json_group:
        return []
    data = read_json(CANDIDATES_JSON)
    trusted_repositories = set(data.get("trusted_repositories", []))
    source_type, source_policy = source_type_policy(source)
    existing_active = active_remote_urls(source.url)
    urls: list[str] = []
    for candidate in data.get("candidates", []):
        if candidate.get("kind") != "remote_rule":
            continue
        if not candidate.get("enabled", False) or not candidate.get("activate", False):
            continue
        if candidate.get("protected", False):
            continue
        if str(candidate.get("type", "")).upper() != source_type:
            continue
        if str(candidate.get("policy", "REJECT")).upper() != source_policy:
            continue
        url = str(candidate.get("url", "")).strip()
        if not url or url == source.url or url in existing_active:
            continue
        metadata = "\n".join(str(candidate.get(key, "")) for key in ("name", "url", "purpose"))
        if has_risk_text(metadata) or not trusted_repo_ok(url, trusted_repositories):
            continue
        urls.append(url)
    return urls


def replacement_candidates(source: Source) -> list[str]:
    candidates: list[str] = []
    parts = github_parts(source.url)
    if parts:
        owner, repo, branch, path = parts
        candidates.extend(raw_url(owner, repo, other, path) for other in ("main", "master") if other != branch)
    candidates.extend(candidate_pool_replacements(source))
    return [url for url in dict.fromkeys(candidates) if valid_replacement_host(url)]


def verify_replacement(source: Source, url: str) -> bool:
    check = check_source(Source(url, source.path, source.line_number, source.kind, source.line))
    if not check.ok or check.status not in {200, 206} or is_html_error(check):
        return False
    sample = check.sample
    source_type, _ = source_type_policy(source)
    if source.kind == "script":
        return any(token in sample for token in ("$done", "function", "=>", "const ", "let ", "var "))
    if source_type == "DOMAIN-SET":
        values = [
            line.strip()
            for line in sample.splitlines()
            if line.strip() and not line.lstrip().startswith(("#", "//"))
        ]
        return bool(values) and sum(1 for line in values[:50] if DOMAIN_SET_VALUE_RE.match(line)) >= min(3, len(values))
    if source_type == "RULE-SET" or source.kind in {"rule-set", "raw"}:
        return any(token in sample for token in RULE_FEATURES)
    return "<html" not in sample.lower()


def find_replacement(source: Source) -> str | None:
    for candidate in replacement_candidates(source):
        if verify_replacement(source, candidate):
            return candidate
    return None


def repair_text_source(source: Source, replacement: str | None, today: str, last_error: str) -> str:
    path = ROOT / source.path
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    idx = source.line_number - 1
    if idx < 0 or idx >= len(lines):
        return "manual"
    original = lines[idx]
    if original.lstrip().startswith("#"):
        return "manual"
    if replacement:
        lines[idx] = f"# AUTO-UPDATED {today}: replaced invalid source after 2 confirmed failures\n" + original.replace(source.url, replacement)
        action = "updated"
    elif source.kind in {"rule-set", "domain-set"} and last_error.startswith("HTTP 404"):
        lines[idx] = f"# AUTO-DELETED {today}: source-first removed standalone invalid remote rule, last_error={last_error}"
        action = "deleted"
    else:
        lines[idx] = f"# AUTO-DISABLED {today}: source failed for 2 confirmed checks, last_error={last_error}\n# original line:\n# {original}"
        action = "commented"
    write_text(path, "\n".join(lines) + "\n")
    return action


def repair_json_source(source: Source, replacement: str | None, today: str, last_error: str) -> str:
    path = ROOT / source.path
    data = read_json(path)
    items = data.get(source.json_group, [])
    if source.json_index < 0 or source.json_index >= len(items):
        return "manual"
    item = items[source.json_index]
    if item.get("protected"):
        return "protected"
    if replacement:
        item["url"] = replacement
        item["last_auto_repair"] = f"{today}: replaced invalid source"
        action = "updated"
    else:
        item["enabled"] = False
        if "activate" in item:
            item["activate"] = False
        item["disabled_reason"] = f"{today}: source failed for 2 confirmed checks, last_error={last_error}"
        action = "disabled_json"
    write_json(path, data)
    return action


def apply_repairs(sources: list[Source], checks: dict[str, Check], history: dict[str, dict[str, object]], today: str) -> dict[str, list[str]]:
    actions = {"updated": [], "commented": [], "deleted": [], "disabled_json": [], "protected": [], "manual": []}
    for source in sources:
        key = history_key(source)
        record = history.get(key, {})
        check = checks[key]
        fail_count = int(record.get("fail_count", 0))
        if check.ok or not check.confirmed_invalid or fail_count < FAIL_THRESHOLD:
            continue
        if is_protected(source):
            actions["protected"].append(source.url)
            actions["manual"].append(source.url)
            continue
        replacement = find_replacement(source)
        if source.json_group:
            action = repair_json_source(source, replacement, today, check.last_error)
        else:
            action = repair_text_source(source, replacement, today, check.last_error)
        actions.setdefault(action, []).append(source.url if not replacement else f"{source.url} -> {replacement}")
    if len(actions["commented"]) > MAX_AUTO_COMMENTS:
        stop("automatic comments exceed safety limit")
    if len(actions["deleted"]) > MAX_AUTO_DELETES:
        stop("automatic deletes exceed safety limit")
    return actions


def md_list(items: Iterable[str], empty: str = "无") -> str:
    values = list(dict.fromkeys(items))
    return f"- {empty}\n" if not values else "".join(f"- `{item}`\n" for item in values)


def generate_report(today: str, sources: list[Source], checks: dict[str, Check], history: dict[str, dict[str, object]], actions: dict[str, list[str]]) -> str:
    failed = [source.url for source in sources if not checks[history_key(source)].ok]
    first_failed = [history[key]["url"] for key in history if int(history[key].get("fail_count", 0)) == 1]
    two_day = [history[key]["url"] for key in history if int(history[key].get("fail_count", 0)) >= FAIL_THRESHOLD]
    changed = any(actions.get(key) for key in ("updated", "commented", "deleted", "disabled_json"))
    return "\n".join([
        "# Invalid Sources Audit and Repair Report",
        "",
        f"- 日期：{today}",
        "- 维护模式：source-first",
        f"- 扫描源文件链接总数：{len(sources)}",
        f"- 正常链接数量：{len(sources) - len(failed)}",
        f"- 本次是否修改源头文件：{'yes' if changed else 'no'}",
        "",
        "本系统优先修复 `Rewrite/Remotes/`、`Rules/`、`Scripts/`、`Rewrite/Sources/`，随后由工作流重新构建 Release 并同步根目录主模块。不会因单日失败删除规则。",
        "",
        "## 今日首次失败链接", md_list(first_failed).rstrip(),
        "", "## 连续失败 2 天链接", md_list(two_day).rstrip(),
        "", "## 已自动替换链接", md_list(actions.get("updated", [])).rstrip(),
        "", "## 已自动注释链接", md_list(actions.get("commented", [])).rstrip(),
        "", "## 已自动删除链接", md_list(actions.get("deleted", [])).rstrip(),
        "", "## 已自动禁用 JSON 源", md_list(actions.get("disabled_json", [])).rstrip(),
        "", "## 受保护但失败链接", md_list(actions.get("protected", [])).rstrip(),
        "", "## 需要人工确认链接", md_list(actions.get("manual", [])).rstrip(),
        "", "## 今日失败明细", md_list([f"{source.url} ({checks[history_key(source)].last_error})" for source in sources if not checks[history_key(source)].ok]).rstrip(),
        "",
    ])


def guard_github_outage(sources: list[Source], checks: dict[str, Check]) -> None:
    github = [source for source in sources if "github" in urllib.parse.urlparse(source.url).netloc]
    if not github:
        return
    failed = [source for source in github if not checks[history_key(source)].ok]
    transient = [source for source in failed if checks[history_key(source)].status in TRANSIENT_STATUS or checks[history_key(source)].error_type in {"TIMEOUT", "DNS_ERROR"}]
    if len(github) and len(failed) / len(github) > 0.30 and len(transient) >= len(failed) // 2:
        stop("more than 30% of GitHub links failed with transient errors; likely network outage")


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    sources = scan_sources()
    checks = {history_key(source): check_source(source) for source in sources}
    guard_github_outage(sources, checks)
    history = update_history(load_history(), sources, checks, today)
    actions = apply_repairs(sources, checks, history, today)
    save_history(history)
    write_text(REPORT_PATH, generate_report(today, sources, checks, history, actions))
    failed_count = sum(1 for check in checks.values() if not check.ok)
    changed = any(actions.get(key) for key in ("updated", "commented", "deleted", "disabled_json"))
    print(f"Source-first audited {len(sources)} links, failed today: {failed_count}, source_changed={changed}")


if __name__ == "__main__":
    main()
