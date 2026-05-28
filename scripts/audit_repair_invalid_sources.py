#!/usr/bin/env python3
"""Audit invalid remote sources and repair them after 2 failed checks.

This is a conservative maintenance tool for Ronghemokuai.sgmodule.
It never reacts to a single-day failure. After 2 consecutive confirmed
failures it tries trusted same-upstream replacements, then low-risk
removal for standalone remote rule references, otherwise comments the
original line for easy rollback.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "Ronghemokuai.sgmodule"
REPORT_DIR = ROOT / "reports"
REPORT_PATH = REPORT_DIR / "invalid_sources_report.md"
HISTORY_PATH = REPORT_DIR / "invalid_sources_history.json"
EXPECTED_UPDATE_URL = "https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"
USER_AGENT = "GrandpaNiu-InvalidSourceRepair/1.0 (+https://github.com/GrandpaNiuu/GrandpaNiu)"
TIMEOUT_SECONDS = 25
REQUIRED_SECTIONS = {"Rule", "Script", "MITM"}
KNOWN_SECTIONS = {"Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"}
CORE_TOKENS = ("spotify-json", "spotify-proto", "youtube.response")
FAIL_THRESHOLD = 2
MAX_AUTO_COMMENTS = 20
MAX_AUTO_DELETES = 5

PROTECTED_PATTERNS = (
    "spotify-json",
    "spotify-proto",
    "youtube.response",
    "app2smile/rules/master/js/spotify-json.js",
    "app2smile/rules/master/js/spotify-proto.js",
    "app2smile/rules/master/module/spotify.module",
    "Maasea/sgmodule",
    "blackmatrix7/ios_rule_script",
    "Cats-Team/AdRules",
    "Ronghemokuai.sgmodule",
    EXPECTED_UPDATE_URL,
    "https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule",
    "README.md",
    "redirect.html",
    "import.html",
)
DISALLOWED_REPLACEMENT_HOSTS = ("ghproxy", "mirror", "tinyurl.com", "bit.ly", "t.co", "shorturl")

URL_RE = re.compile(r"https?://[^\s\"'<>)\],]+")
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")
SCRIPT_PATH_RE = re.compile(r"script-path=(https?://[^,\s]+)")
UPDATE_URL_RE = re.compile(r"^#!update-url=(https?://\S+)\s*$")
GITHUB_RAW_RE = re.compile(r"^https://raw\.githubusercontent\.com/([^/]+)/([^/]+)/([^/]+)/(.+)$")
GITHUB_BLOB_RE = re.compile(r"^https://github\.com/([^/]+)/([^/]+)/blob/([^/]+)/(.+)$")
HTML_ERROR_TOKENS = (
    "404 not found",
    "not found",
    "repository not found",
    "file not found",
    "there isn't a github pages site here",
    "this repository is empty",
)
RULE_FEATURES = ("DOMAIN", "DOMAIN-SUFFIX", "URL-REGEX", "RULE-SET", "DOMAIN-SET", "payload", "host-suffix")
TRANSIENT_STATUS = {429, 500, 502, 503, 504}


@dataclass(frozen=True)
class Source:
    url: str
    line_number: int
    section: str
    kind: str
    line: str


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
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def write_text_lf(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def read_module() -> list[str]:
    try:
        return MODULE_PATH.read_text(encoding="utf-8").splitlines()
    except UnicodeError as exc:
        stop(f"encoding error while reading {MODULE_PATH}: {exc}")
    except OSError as exc:
        stop(f"cannot read {MODULE_PATH}: {exc}")


def find_sections(lines: list[str]) -> dict[str, int]:
    sections: dict[str, int] = {}
    for idx, line in enumerate(lines, 1):
        match = SECTION_RE.match(line.strip())
        if match:
            sections[match.group(1)] = idx
    missing = sorted(REQUIRED_SECTIONS - set(sections))
    if missing:
        stop(f"required sections missing: {', '.join(missing)}")
    return sections


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


def clean_url(url: str) -> str:
    return url.rstrip(".,;")


def scan_sources(lines: list[str]) -> list[Source]:
    sources: list[Source] = []
    seen: set[tuple[str, int]] = set()
    section = ""
    for idx, line in enumerate(lines, 1):
        match = SECTION_RE.match(line.strip())
        if match:
            section = match.group(1)
        urls: list[str] = []
        script_match = SCRIPT_PATH_RE.search(line)
        if script_match:
            urls.append(script_match.group(1))
        update_match = UPDATE_URL_RE.match(line.strip())
        if update_match:
            urls.append(update_match.group(1))
        parts = [part.strip() for part in line.split(",")]
        if len(parts) >= 2 and parts[0] in {"RULE-SET", "DOMAIN-SET"} and parts[1].startswith("http"):
            urls.append(parts[1])
        urls.extend(URL_RE.findall(line))
        for raw in urls:
            url = clean_url(raw)
            if "$" in url:
                continue
            key = (url, idx)
            if key in seen:
                continue
            seen.add(key)
            sources.append(Source(url=url, line_number=idx, section=section or "GLOBAL", kind=classify(line, url), line=line))
    return sources


def request_once(url: str, method: str) -> Check:
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if method == "GET":
        headers["Range"] = "bytes=0-4096"
    req = urllib.request.Request(url, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as response:
            body = response.read(4097) if method == "GET" else b""
            length_header = response.headers.get("Content-Length")
            content_length = int(length_header) if length_header and length_header.isdigit() else len(body) or None
            return Check(
                ok=True,
                confirmed_invalid=False,
                status=response.status,
                final_url=response.geturl(),
                content_type=response.headers.get("Content-Type", ""),
                content_length=content_length,
                sample=body.decode("utf-8", errors="ignore")[:4096],
            )
    except urllib.error.HTTPError as exc:
        body = exc.read(4097) if method == "GET" else b""
        return Check(
            ok=False,
            confirmed_invalid=exc.code in {404, 410},
            status=exc.code,
            final_url=exc.geturl(),
            error_type=classify_http_error(exc.code),
            content_type=exc.headers.get("Content-Type", "") if exc.headers else "",
            content_length=len(body) or None,
            sample=body.decode("utf-8", errors="ignore")[:4096],
        )
    except urllib.error.URLError as exc:
        reason = str(exc.reason)
        if "timed out" in reason.lower():
            return Check(ok=False, confirmed_invalid=False, error_type="TIMEOUT")
        if "getaddrinfo failed" in reason.lower() or "name or service not known" in reason.lower():
            return Check(ok=False, confirmed_invalid=False, error_type="DNS_ERROR")
        return Check(ok=False, confirmed_invalid=False, error_type=f"URL_ERROR: {reason[:120]}")
    except TimeoutError:
        return Check(ok=False, confirmed_invalid=False, error_type="TIMEOUT")
    except OSError as exc:
        return Check(ok=False, confirmed_invalid=False, error_type=f"NETWORK_ERROR: {str(exc)[:120]}")


def classify_http_error(status: int) -> str:
    if status == 404:
        return "NOT_FOUND"
    if status == 410:
        return "GONE"
    if status in TRANSIENT_STATUS:
        return f"HTTP {status}"
    return f"HTTP {status}"


def is_html_error(check: Check, source: Source) -> bool:
    if source.kind not in {"script", "rule-set", "domain-set", "raw", "update-url", "github-pages"}:
        return False
    if source.kind == "github-blob" and check.status and 200 <= check.status < 400:
        return False
    content_type = check.content_type.lower()
    sample = check.sample.lower()
    if "text/html" not in content_type:
        return False
    return any(token in sample for token in HTML_ERROR_TOKENS)


def check_source(source: Source) -> Check:
    head = request_once(source.url, "HEAD")
    needs_get = (
        not head.ok
        or head.status is None
        or head.status >= 400
        or head.content_length == 0
        or "text/html" in head.content_type.lower()
    )
    check = request_once(source.url, "GET") if needs_get else head
    if check.ok and check.status and 200 <= check.status < 400:
        if check.content_length == 0 and source.kind in {"script", "rule-set", "domain-set", "raw", "update-url"}:
            check.ok = False
            check.confirmed_invalid = True
            check.error_type = "EMPTY_CONTENT"
        elif is_html_error(check, source):
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
    try:
        return json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeError) as exc:
        stop(f"invalid history file {HISTORY_PATH}: {exc}")


def save_history(history: dict[str, dict[str, object]]) -> None:
    write_text_lf(HISTORY_PATH, json.dumps(history, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def update_history(
    history: dict[str, dict[str, object]],
    sources: Iterable[Source],
    checks: dict[str, Check],
    today: str,
) -> dict[str, dict[str, object]]:
    by_url = {source.url: source for source in sources}
    updated = {url: record for url, record in history.items() if url in by_url}
    for url, source in by_url.items():
        check = checks[url]
        if check.ok:
            updated.pop(url, None)
            continue
        if not check.confirmed_invalid:
            updated.pop(url, None)
            continue
        old = updated.get(url, {})
        updated[url] = {
            "first_failed_date": old.get("first_failed_date", today),
            "last_failed_date": today,
            "fail_count": int(old.get("fail_count", 0)) + 1,
            "last_error": check.last_error,
            "section": source.section,
            "line_number": source.line_number,
            "line_preview": source.line.strip()[:240],
        }
    return updated


def has_js_features(text: str) -> bool:
    lowered = text.lower()
    return "<html" not in lowered and any(token in text for token in ("$done", "function", "=>", "const ", "let ", "var "))


def has_rule_features(text: str) -> bool:
    lowered = text.lower()
    return "<html" not in lowered and any(token in text for token in RULE_FEATURES)


def valid_replacement_host(url: str) -> bool:
    host = urllib.parse.urlparse(url).netloc.lower()
    return not any(blocked in host for blocked in DISALLOWED_REPLACEMENT_HOSTS)


def github_api_json(url: str) -> object | None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as response:
            return json.loads(response.read().decode("utf-8"))
    except Exception:
        return None


def github_parts(url: str) -> tuple[str, str, str, str] | None:
    match = GITHUB_RAW_RE.match(url) or GITHUB_BLOB_RE.match(url)
    if not match:
        return None
    owner, repo, branch, path = match.groups()
    return owner, repo, branch, path


def raw_url(owner: str, repo: str, branch: str, path: str) -> str:
    return f"https://raw.githubusercontent.com/{owner}/{repo}/{branch}/{path}"


def replacement_candidates(source: Source) -> list[str]:
    candidates: list[str] = []
    blob = GITHUB_BLOB_RE.match(source.url)
    if blob:
        owner, repo, branch, path = blob.groups()
        candidates.append(raw_url(owner, repo, branch, path))

    parts = github_parts(source.url)
    if parts:
        owner, repo, branch, path = parts
        for new_branch in ("main", "master"):
            if new_branch != branch:
                candidates.append(raw_url(owner, repo, new_branch, path))

        basename = path.rsplit("/", 1)[-1]
        for tree_branch in dict.fromkeys([branch, "main", "master"]):
            tree = github_api_json(f"https://api.github.com/repos/{owner}/{repo}/git/trees/{tree_branch}?recursive=1")
            if not isinstance(tree, dict):
                continue
            entries = tree.get("tree", [])
            if not isinstance(entries, list):
                continue
            for entry in entries:
                if entry.get("type") != "blob":
                    continue
                entry_path = entry.get("path", "")
                if entry_path.endswith("/" + basename) or entry_path == basename:
                    candidates.append(raw_url(owner, repo, tree_branch, entry_path))

        readme = request_once(raw_url(owner, repo, branch, "README.md"), "GET")
        if readme.ok:
            for url in URL_RE.findall(readme.sample):
                if basename in url and (GITHUB_RAW_RE.match(url) or GITHUB_BLOB_RE.match(url)):
                    candidate_parts = github_parts(clean_url(url))
                    if candidate_parts and candidate_parts[0] == owner and candidate_parts[1] == repo:
                        c_owner, c_repo, c_branch, c_path = candidate_parts
                        candidates.append(raw_url(c_owner, c_repo, c_branch, c_path))

    cleaned: list[str] = []
    for candidate in candidates:
        candidate = clean_url(candidate)
        if candidate == source.url or candidate in cleaned or not valid_replacement_host(candidate):
            continue
        cleaned.append(candidate)
    return cleaned


def verify_replacement(source: Source, candidate: str) -> bool:
    check = check_source(Source(url=candidate, line_number=source.line_number, section=source.section, kind=source.kind, line=source.line))
    if not check.ok or check.status not in {200, 206}:
        return False
    if is_html_error(check, source):
        return False
    if source.kind == "script":
        return has_js_features(check.sample)
    if source.kind in {"rule-set", "domain-set", "raw"}:
        return has_rule_features(check.sample) or has_js_features(check.sample)
    return "<html" not in check.sample.lower()


def find_replacement(source: Source) -> str | None:
    for candidate in replacement_candidates(source):
        if verify_replacement(source, candidate):
            return candidate
    return None


def eligible_for_delete(source: Source, check: Check) -> bool:
    if source.kind not in {"rule-set", "domain-set"}:
        return False
    if is_protected(source):
        return False
    if check.status not in {404, 410}:
        return False
    stripped = source.line.strip()
    return stripped.startswith(("RULE-SET,", "DOMAIN-SET,")) and stripped.count(",") <= 2


def comment_source(lines: list[str], source: Source, today: str, last_error: str) -> None:
    original = lines[source.line_number - 1]
    lines[source.line_number - 1] = (
        f"# AUTO-DISABLED {today}: source failed for 2 consecutive checks, last_error={last_error}\n"
        "# original line:\n"
        f"# {original}"
    )


def replace_source(lines: list[str], source: Source, replacement: str, today: str) -> None:
    original = lines[source.line_number - 1]
    lines[source.line_number - 1] = (
        f"# AUTO-UPDATED {today}: replaced invalid source after 2 consecutive failed checks\n"
        f"{original.replace(source.url, replacement)}"
    )


def delete_source(lines: list[str], source: Source, today: str, last_error: str) -> None:
    lines[source.line_number - 1] = f"# AUTO-DELETED {today}: removed standalone invalid remote rule, last_error={last_error}"


def apply_repairs(
    lines: list[str],
    sources: list[Source],
    checks: dict[str, Check],
    history: dict[str, dict[str, object]],
    today: str,
) -> tuple[list[str], list[tuple[str, str]], list[str], list[str], list[str], list[str]]:
    edited = list(lines)
    updated: list[tuple[str, str]] = []
    commented: list[str] = []
    deleted: list[str] = []
    protected_failed: list[str] = []
    manual: list[str] = []
    touched_lines: set[int] = set()

    for source in sources:
        record = history.get(source.url, {})
        fail_count = int(record.get("fail_count", 0))
        check = checks[source.url]
        if check.ok or not check.confirmed_invalid or fail_count < FAIL_THRESHOLD:
            continue
        if is_protected(source):
            protected_failed.append(source.url)
            manual.append(source.url)
            continue
        if source.line.lstrip().startswith("#") or source.line_number in touched_lines:
            manual.append(source.url)
            continue

        replacement = find_replacement(source)
        if replacement:
            replace_source(edited, source, replacement, today)
            updated.append((source.url, replacement))
            touched_lines.add(source.line_number)
            continue

        if eligible_for_delete(source, check):
            delete_source(edited, source, today, check.last_error)
            deleted.append(source.url)
            touched_lines.add(source.line_number)
            continue

        comment_source(edited, source, today, check.last_error)
        commented.append(source.url)
        touched_lines.add(source.line_number)

    if len(commented) > MAX_AUTO_COMMENTS:
        stop(f"automatic comments exceed safety limit: {len(commented)}")
    if len(deleted) > MAX_AUTO_DELETES:
        stop(f"automatic deletes exceed safety limit: {len(deleted)}")
    return edited, updated, commented, deleted, protected_failed, manual


def update_url_ok(lines: list[str]) -> bool:
    for line in lines:
        match = UPDATE_URL_RE.match(line.strip())
        if match:
            return match.group(1) == EXPECTED_UPDATE_URL
    return False


def validate_module(lines: list[str], original_line_count: int, comments: int, deletes: int) -> None:
    text = "\n".join(lines)
    sections = find_sections(lines)
    for token in CORE_TOKENS:
        if token not in text:
            stop(f"required core token missing: {token}")
    if not update_url_ok(lines):
        stop(f"update-url must point to {EXPECTED_UPDATE_URL}")
    if comments > MAX_AUTO_COMMENTS:
        stop("automatic comments exceed safety limit")
    if deletes > MAX_AUTO_DELETES:
        stop("automatic deletes exceed safety limit")
    if len(lines) < original_line_count * 0.97:
        stop("module line count reduced by more than 3%")
    script_start = sections["Script"]
    mitm_start = sections["MITM"]
    if not any(line.strip() and not line.lstrip().startswith("#") for line in lines[script_start:mitm_start - 1]):
        stop("[Script] section would become empty")
    if not any(line.strip().startswith("hostname = ") for line in lines[mitm_start:]):
        stop("[MITM] section would become empty")


def guard_github_outage(sources: list[Source], checks: dict[str, Check]) -> None:
    github_sources = [source for source in sources if "github" in urllib.parse.urlparse(source.url).netloc]
    if not github_sources:
        return
    failed = [source for source in github_sources if not checks[source.url].ok]
    transient = [source for source in failed if checks[source.url].status in TRANSIENT_STATUS or checks[source.url].error_type in {"TIMEOUT", "DNS_ERROR"}]
    if len(failed) / len(github_sources) > 0.30 and len(transient) >= len(failed) // 2:
        stop("more than 30% of GitHub links failed with transient errors; likely network outage")


def write_module(lines: list[str]) -> None:
    try:
        write_text_lf(MODULE_PATH, "\n".join(lines) + "\n")
        MODULE_PATH.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        stop(f"generated {MODULE_PATH} cannot be read as UTF-8: {exc}")


def md_list(items: Iterable[str], empty: str = "无") -> str:
    values = list(dict.fromkeys(items))
    if not values:
        return f"- {empty}\n"
    return "".join(f"- `{value}`\n" for value in values)


def generate_report(
    today: str,
    sources: list[Source],
    checks: dict[str, Check],
    history: dict[str, dict[str, object]],
    updated: list[tuple[str, str]],
    commented: list[str],
    deleted: list[str],
    protected_failed: list[str],
    manual: list[str],
    module_changed: bool,
    safety_triggered: str,
    lines: list[str],
) -> str:
    failed_today = [source.url for source in sources if not checks[source.url].ok]
    first_failed = [url for url in failed_today if int(history.get(url, {}).get("fail_count", 0)) == 1]
    two_day_failed = [url for url, record in history.items() if int(record.get("fail_count", 0)) >= FAIL_THRESHOLD]
    protected_marked = [f"{url} - PROTECTED_FAILED_NEEDS_MANUAL_CONFIRMATION" for url in protected_failed]
    replacements = [f"{old} -> {new}" for old, new in updated]
    text = "\n".join(lines)
    spotify_ok = all(token in text for token in ("spotify-json", "spotify-proto"))
    youtube_ok = "youtube.response" in text

    return "\n".join(
        [
            "# Invalid Sources Audit and Repair Report",
            "",
            f"- 日期：{today}",
            f"- 扫描链接总数：{len(sources)}",
            f"- 正常链接数量：{len(sources) - len(failed_today)}",
            f"- Spotify 核心检查：{'pass' if spotify_ok else 'fail'}",
            f"- YouTube 核心检查：{'pass' if youtube_ok else 'fail'}",
            f"- update-url 检查：{'pass' if update_url_ok(lines) else 'fail'}",
            f"- 安全停止条件是否触发：{safety_triggered or 'no'}",
            f"- 本次提交是否修改 Ronghemokuai.sgmodule：{'yes' if module_changed else 'no'}",
            "",
            "本系统为安全维护工具，不会因单日失败删除规则；连续 2 天失败后优先替换，其次注释，最后才低风险删除。",
            "",
            "## 今日首次失败链接",
            md_list(first_failed).rstrip(),
            "",
            "## 连续失败 2 天链接",
            md_list(two_day_failed).rstrip(),
            "",
            "## 已自动替换链接",
            md_list(replacements).rstrip(),
            "",
            "## 已自动注释链接",
            md_list(commented).rstrip(),
            "",
            "## 已自动删除链接",
            md_list(deleted).rstrip(),
            "",
            "## 受保护但失败链接",
            md_list(protected_marked).rstrip(),
            "",
            "## 需要人工确认链接",
            md_list(manual).rstrip(),
            "",
            "## 今日失败明细",
            md_list([f"{url} ({checks[url].last_error})" for url in failed_today]).rstrip(),
            "",
        ]
    )


def main() -> None:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    lines = read_module()
    original_line_count = len(lines)
    validate_module(lines, original_line_count, 0, 0)

    scanned = scan_sources(lines)
    unique: dict[str, Source] = {}
    for source in scanned:
        unique.setdefault(source.url, source)
    sources = list(unique.values())
    checks = {source.url: check_source(source) for source in sources}
    guard_github_outage(sources, checks)

    history = update_history(load_history(), sources, checks, today)
    edited, updated, commented, deleted, protected_failed, manual = apply_repairs(lines, sources, checks, history, today)
    validate_module(edited, original_line_count, len(commented), len(deleted))
    module_changed = edited != lines
    write_module(edited)
    save_history(history)

    report = generate_report(
        today=today,
        sources=sources,
        checks=checks,
        history=history,
        updated=updated,
        commented=commented,
        deleted=deleted,
        protected_failed=protected_failed,
        manual=manual,
        module_changed=module_changed,
        safety_triggered="no",
        lines=edited,
    )
    write_text_lf(REPORT_PATH, report)
    print(f"Audited {len(sources)} sources, failed today: {sum(1 for c in checks.values() if not c.ok)}, module_changed={module_changed}")


if __name__ == "__main__":
    main()
