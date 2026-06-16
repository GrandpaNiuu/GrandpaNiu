#!/usr/bin/env python3
"""Conservative upstream candidate collector.

The collector is intentionally candidate-list driven. It never searches the
web, never accepts unknown repositories, and keeps scripts pending unless a
candidate is explicitly approved from a trusted upstream.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CANDIDATES_PATH = ROOT / "Rewrite" / "Remotes" / "candidates.json"
SOURCES_PATH = ROOT / "Rewrite" / "Remotes" / "sources.json"
REPORT_PATH = ROOT / "reports" / "upstream_collect_report.md"
MODULE_PATH = ROOT / "Ronghemokuai.sgmodule"
RELEASE_PATH = ROOT / "Release" / "Ronghemokuai.sgmodule"
RULES_DIR = ROOT / "Rules"
SCRIPTS_DIR = ROOT / "Scripts"
USER_AGENT = "GrandpaNiu-UpstreamCollector/1.0 (+https://github.com/GrandpaNiuu/GrandpaNiu)"
TIMEOUT_SECONDS = 25
MAX_READ_BYTES = 1024 * 1024

ALLOWED_KINDS = {"remote_rule", "local_rule", "script", "reference_module"}
ALLOWED_REMOTE_TYPES = {"RULE-SET", "DOMAIN-SET"}
ALLOWED_LOCAL_TARGETS = {
    "Rules/direct.list",
    "Rules/spotify-direct.list",
    "Rules/youtube-direct.list",
    "Rules/reject.list",
    "Rules/app-clean.list",
    "Rules/web-ads.list",
}
ALLOWED_SCRIPT_TARGETS = {
    "Scripts/spotify.conf",
    "Scripts/youtube.conf",
    "Scripts/app-clean.conf",
}

RISK_PATTERNS = (
    "破解",
    "会员",
    "解锁",
    "付费",
    "支付绕过",
    "登录绕过",
    "证书绕过",
    "成人",
    "博彩",
    "premium unlock",
    "premium",
    "vip unlock",
    "unlock",
    "crack",
    "bypass payment",
    "payment bypass",
    "login bypass",
    "cookie",
    "boxjs",
    "porn",
    "adult",
    "casino",
    "gambling",
    "ghproxy",
    "mirror",
    "tinyurl",
    "bit.ly",
    "t.co/",
    "shorturl",
)
RULE_FEATURES = (
    "DOMAIN,",
    "DOMAIN-SUFFIX,",
    "DOMAIN-KEYWORD,",
    "DOMAIN-SET,",
    "RULE-SET,",
    "URL-REGEX,",
    "IP-CIDR,",
    "payload:",
    "host-suffix",
)
SCRIPT_FEATURES = ("$done", "$request", "$response", "function ", "const ", "let ", "var ", "JSON.parse")
PROTECTED_PATTERNS = (
    "spotify-json",
    "spotify-proto",
    "youtube.response",
    "spclient.wg.spotify.com",
    "*.spclient.spotify.com",
    "raw.githubusercontent.com/app2smile/rules/master/js/spotify-json.js",
    "raw.githubusercontent.com/app2smile/rules/master/js/spotify-proto.js",
    "raw.githubusercontent.com/app2smile/rules/master/module/spotify.module",
    "Maasea/sgmodule",
)


@dataclass
class FetchResult:
    ok: bool
    status: int | None = None
    final_url: str = ""
    content_type: str = ""
    content_length: int | None = None
    text: str = ""
    error: str = ""


@dataclass
class CandidateResult:
    name: str
    kind: str
    url: str
    action: str
    reason: str
    target: str = ""
    status: int | None = None
    notes: list[str] = field(default_factory=list)


def stop(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        stop(f"missing file: {path}")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        stop(f"invalid json: {path}: {exc}")
    except UnicodeError as exc:
        stop(f"encoding error: {path}: {exc}")


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def candidate_text(candidate: dict[str, Any]) -> str:
    return "\n".join(str(candidate.get(key, "")) for key in ("name", "url", "purpose", "script_entry"))


def has_risk_text(text: str, patterns: tuple[str, ...] = RISK_PATTERNS) -> str:
    lowered = text.lower()
    for token in patterns:
        if token.lower() in lowered:
            return token
    return ""


def is_protected(candidate: dict[str, Any]) -> bool:
    text = candidate_text(candidate)
    return bool(candidate.get("protected")) or any(token in text for token in PROTECTED_PATTERNS)


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
    if parsed.scheme != "https":
        return False
    if any(token in url.lower() for token in ("ghproxy", "mirror", "tinyurl", "bit.ly", "t.co/", "shorturl")):
        return False
    repo = github_repo_from_url(url)
    return bool(repo and repo in trusted_repositories)


def request_url(url: str, method: str, range_header: bool = False) -> FetchResult:
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if range_header:
        headers["Range"] = f"bytes=0-{MAX_READ_BYTES - 1}"
    request = urllib.request.Request(url, method=method, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=TIMEOUT_SECONDS) as response:
            raw = response.read(MAX_READ_BYTES + 1) if method == "GET" else b""
            return FetchResult(
                ok=200 <= response.status < 300,
                status=response.status,
                final_url=response.geturl(),
                content_type=response.headers.get("Content-Type", ""),
                content_length=response.headers.get("Content-Length"),
                text=raw[:MAX_READ_BYTES].decode("utf-8", errors="replace"),
            )
    except urllib.error.HTTPError as exc:
        raw = exc.read(4096) if method == "GET" else b""
        return FetchResult(
            ok=False,
            status=exc.code,
            final_url=exc.geturl() if hasattr(exc, "geturl") else url,
            content_type=exc.headers.get("Content-Type", "") if exc.headers else "",
            content_length=exc.headers.get("Content-Length") if exc.headers else None,
            text=raw.decode("utf-8", errors="replace"),
            error=f"HTTP {exc.code}",
        )
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return FetchResult(ok=False, final_url=url, error=type(exc).__name__)


def fetch_candidate(url: str) -> FetchResult:
    head = request_url(url, "HEAD")
    if head.ok:
        get = request_url(url, "GET", range_header=True)
        if get.ok:
            return get
        return FetchResult(
            ok=True,
            status=head.status,
            final_url=head.final_url,
            content_type=head.content_type,
            content_length=head.content_length,
            text="",
        )
    return request_url(url, "GET", range_header=True)


def looks_like_html_error(result: FetchResult) -> bool:
    lowered = result.text[:4096].lower()
    if "text/html" in result.content_type.lower() and not any(feature.lower() in lowered for feature in RULE_FEATURES + SCRIPT_FEATURES):
        return True
    return any(token in lowered for token in ("404 not found", "repository not found", "file not found"))


def looks_like_rule(text: str) -> bool:
    sample = text[:65536]
    return any(feature in sample for feature in RULE_FEATURES)


def looks_like_script(text: str) -> bool:
    sample = text[:65536]
    return any(feature in sample for feature in SCRIPT_FEATURES)


def existing_urls() -> set[str]:
    urls: set[str] = set()
    pattern = re.compile(r"https?://[^\s\"'<>)\],]+")
    for path in [SOURCES_PATH, *RULES_DIR.glob("*.list"), *SCRIPTS_DIR.glob("*.conf"), *(ROOT / "Rewrite" / "Sources").glob("*.conf")]:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        urls.update(match.group(0).rstrip(",") for match in pattern.finditer(text))
    return urls


def existing_script_names() -> set[str]:
    names: set[str] = set()
    for path in SCRIPTS_DIR.glob("*.conf"):
        for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
            stripped = line.strip()
            if stripped and not stripped.startswith("#") and "=" in stripped:
                names.add(stripped.split("=", 1)[0].strip())
    return names


def append_unique_lines(path: Path, header: str, lines: list[str]) -> int:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    existing_active = {line.strip() for line in existing.splitlines() if line.strip() and not line.strip().startswith("#")}
    new_lines = [line.strip() for line in lines if line.strip() and not line.strip().startswith("#") and line.strip() not in existing_active]
    if not new_lines:
        return 0
    suffix = "" if existing.endswith("\n") or not existing else "\n"
    block = suffix + header.rstrip() + "\n" + "\n".join(new_lines) + "\n"
    write_text(path, existing + block)
    return len(new_lines)


def add_remote_source(sources: dict[str, Any], candidate: dict[str, Any]) -> bool:
    existing = {item.get("url") for item in sources.get("rule_sets", [])}
    if candidate["url"] in existing:
        return False
    item = {
        "name": str(candidate["name"]).strip(),
        "type": str(candidate["type"]).strip(),
        "url": str(candidate["url"]).strip(),
        "policy": str(candidate.get("policy", "REJECT")).strip(),
        "enabled": bool(candidate.get("activate", False)),
        "protected": bool(candidate.get("protected", False)),
        "purpose": str(candidate.get("purpose", "collected trusted upstream candidate")).strip(),
    }
    sources.setdefault("rule_sets", []).append(item)
    write_json(SOURCES_PATH, sources)
    return True


def validate_candidate_schema(candidate: dict[str, Any]) -> str:
    for field_name in ("name", "kind", "url", "purpose"):
        if not str(candidate.get(field_name, "")).strip():
            return f"missing {field_name}"
    if candidate["kind"] not in ALLOWED_KINDS:
        return f"unsupported kind {candidate['kind']}"
    if candidate["kind"] == "remote_rule":
        if candidate.get("type") not in ALLOWED_REMOTE_TYPES:
            return "remote_rule requires type RULE-SET or DOMAIN-SET"
        if not str(candidate.get("policy", "")).strip():
            return "remote_rule requires policy"
    return ""


def process_candidate(
    candidate: dict[str, Any],
    sources: dict[str, Any],
    trusted_repositories: set[str],
    known_urls: set[str],
    known_script_names: set[str],
) -> CandidateResult:
    name = str(candidate.get("name", "")).strip() or "(unnamed)"
    kind = str(candidate.get("kind", "")).strip()
    url = str(candidate.get("url", "")).strip()
    result = CandidateResult(name=name, kind=kind, url=url, action="skipped", reason="")

    schema_error = validate_candidate_schema(candidate)
    if schema_error:
        result.reason = schema_error
        return result

    if not candidate.get("enabled", False):
        result.reason = "candidate disabled"
        return result

    if is_protected(candidate):
        result.reason = "PROTECTED_FAILED_NEEDS_MANUAL_CONFIRMATION: protected core/reference candidate"
        return result

    risk = has_risk_text(candidate_text(candidate))
    if risk:
        result.reason = f"risk keyword in candidate metadata: {risk}"
        return result

    if not trusted_repo_ok(url, trusted_repositories):
        result.reason = "URL is not an allowed trusted GitHub repository or uses a forbidden host"
        return result

    if url in known_urls:
        result.reason = "duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources"
        return result

    fetched = fetch_candidate(url)
    result.status = fetched.status
    if not fetched.ok:
        result.reason = fetched.error or f"HTTP {fetched.status}"
        return result
    if looks_like_html_error(fetched):
        result.reason = "candidate returned an HTML/error page"
        return result
    if kind == "script":
        risk = has_risk_text(fetched.text)
        if risk:
            result.reason = f"risk keyword in script content: {risk}"
            return result

    if kind == "reference_module":
        result.reason = "reference module is report-only"
        return result

    if kind == "remote_rule":
        if not looks_like_rule(fetched.text):
            result.reason = "content does not look like a Surge/Shadowrocket rule source"
            return result
        added = add_remote_source(sources, candidate)
        if not added:
            result.reason = "duplicate URL already present in sources.json"
            return result
        result.action = "added_remote_source"
        result.target = "Rewrite/Remotes/sources.json"
        result.reason = "passed checks and was registered"
        if not candidate.get("activate", False):
            result.notes.append("registered with enabled=false because activate is not true")
        return result

    if kind == "local_rule":
        if not looks_like_rule(fetched.text):
            result.reason = "content does not look like a rule list"
            return result
        target = str(candidate.get("target", "Rules/app-clean.list"))
        if target not in ALLOWED_LOCAL_TARGETS:
            result.reason = f"local_rule target is not allowed: {target}"
            return result
        if not candidate.get("approved", False):
            result.reason = "local_rule candidates require approved=true before appending"
            return result
        rule_lines = [line for line in fetched.text.splitlines() if line.strip() and not line.strip().startswith("#")]
        count = append_unique_lines(ROOT / target, f"# collected: {name}", rule_lines)
        result.action = "added_local_rules" if count else "skipped"
        result.target = target
        result.reason = f"added {count} unique rules" if count else "all rules were duplicates"
        return result

    if kind == "script":
        if not looks_like_script(fetched.text):
            result.reason = "content does not look like JavaScript"
            return result
        status = str(candidate.get("status", "pending")).strip().lower()
        if status != "approved" and not candidate.get("trusted_upstream", False):
            result.reason = "script candidate is pending; scripts are not auto-added without approval"
            return result
        target = str(candidate.get("target", "Scripts/app-clean.conf"))
        if target not in ALLOWED_SCRIPT_TARGETS:
            result.reason = f"script target is not allowed: {target}"
            return result
        entry = str(candidate.get("script_entry", "")).strip()
        if not entry or "script-path=" not in entry:
            result.reason = "script candidate requires a script_entry with script-path"
            return result
        script_name = entry.split("=", 1)[0].strip()
        if script_name in known_script_names:
            result.reason = f"duplicate script name: {script_name}"
            return result
        entry_risk = has_risk_text(entry)
        if entry_risk:
            result.reason = f"risk keyword in script entry: {entry_risk}"
            return result
        count = append_unique_lines(ROOT / target, f"# collected script: {name}", [entry])
        result.action = "added_script" if count else "skipped"
        result.target = target
        result.reason = "added approved script entry" if count else "script entry already exists"
        return result

    result.reason = "unhandled candidate kind"
    return result


def root_release_equal() -> bool:
    if not MODULE_PATH.exists() or not RELEASE_PATH.exists():
        return False
    return MODULE_PATH.read_text(encoding="utf-8", errors="replace") == RELEASE_PATH.read_text(encoding="utf-8", errors="replace")


def make_report(results: list[CandidateResult], before_equal: bool, after_equal: bool, module_changed: bool) -> str:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    added = [item for item in results if item.action.startswith("added")]
    skipped = [item for item in results if item.action == "skipped"]
    added_remote = [item for item in results if item.action == "added_remote_source"]
    added_rules = [item for item in results if item.action == "added_local_rules"]
    added_scripts = [item for item in results if item.action == "added_script"]
    lines = [
        "# 候选源收集报告",
        "",
        f"- 日期：{today}",
        f"- 候选总数：{len(results)}",
        f"- 新增远程规则源：{len(added_remote)}",
        f"- 新增本地规则组：{len(added_rules)}",
        f"- 新增脚本入口：{len(added_scripts)}",
        f"- 跳过候选源：{len(skipped)}",
        f"- 收集器是否修改主模块：{'是' if module_changed else '否'}",
        f"- 收集前 Root/Release 是否一致：{'是' if before_equal else '否'}",
        f"- 收集后 Root/Release 是否一致：{'是' if after_equal else '否'}",
        "",
        "本收集器保持保守：不搜索全网，只读取 `Rewrite/Remotes/candidates.json`，拒绝风险词和不可信仓库，pending 脚本不会进入模块，也不会自动替换 Spotify / YouTube / 知乎核心项。",
        "",
        "## 新增远程规则源",
    ]
    if added_remote:
        lines.extend(f"- {item.name}: {item.url} -> {item.target}; {item.reason}" for item in added_remote)
    else:
        lines.append("- 无")
    lines.append("")
    lines.append("## 新增本地规则")
    if added_rules:
        lines.extend(f"- {item.name}: {item.target}; {item.reason}" for item in added_rules)
    else:
        lines.append("- 无")
    lines.append("")
    lines.append("## 新增脚本")
    if added_scripts:
        lines.extend(f"- {item.name}: {item.target}; {item.reason}" for item in added_scripts)
    else:
        lines.append("- 无")
    lines.append("")
    lines.append("## 跳过候选源")
    if skipped:
        for item in skipped:
            status = f", status={item.status}" if item.status is not None else ""
            lines.append(f"- {item.name}: {item.reason}{status}")
    else:
        lines.append("- 无")
    lines.append("")
    lines.append("## 是否需要自动化验证")
    if added:
        lines.append("- 是。请更新模块并测试受影响 App，同时检查 Spotify、YouTube 和知乎核心流程。")
    else:
        lines.append("- 本次没有新增源，自动化验证可按需执行。")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    before_module = MODULE_PATH.read_text(encoding="utf-8", errors="replace") if MODULE_PATH.exists() else ""
    before_equal = root_release_equal()
    candidates_data = read_json(CANDIDATES_PATH)
    sources = read_json(SOURCES_PATH)
    trusted_repositories = set(candidates_data.get("trusted_repositories", []))
    candidates = candidates_data.get("candidates", [])
    if not isinstance(candidates, list):
        stop("candidates.json field 'candidates' must be a list")
    known_urls = existing_urls()
    known_script_names = existing_script_names()
    results = [
        process_candidate(candidate, sources, trusted_repositories, known_urls, known_script_names)
        for candidate in candidates
    ]
    after_module = MODULE_PATH.read_text(encoding="utf-8", errors="replace") if MODULE_PATH.exists() else ""
    after_equal = root_release_equal()
    write_text(REPORT_PATH, make_report(results, before_equal, after_equal, before_module != after_module))


if __name__ == "__main__":
    main()
