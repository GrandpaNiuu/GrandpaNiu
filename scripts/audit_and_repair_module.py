#!/usr/bin/env python3
"""Audit external links in the generated Fusion module without editing it.

Source repairs are delegated to ``audit_repair_invalid_sources.py`` before the
Builder runs. This final-output audit is intentionally report-only:
- it reports all detected external links;
- it never deletes rules automatically;
- protected Spotify, YouTube, and core upstream sources are report-only.
"""

from __future__ import annotations

import argparse
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
REPORT_PATH = REPORT_DIR / "daily_audit_report.md"
HISTORY_PATH = REPORT_DIR / "invalid_history.json"
EXPECTED_UPDATE_URL = "https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"
USER_AGENT = "GrandpaNiu-DailyAudit/1.0 (+https://github.com/GrandpaNiuu/GrandpaNiu)"
TIMEOUT_SECONDS = 25
REQUIRED_SECTIONS = {"Rule", "Script", "MITM"}
KNOWN_SECTIONS = {"Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"}
CORE_TOKENS = ("spotify-json", "spotify-proto", "youtube.response")

PROTECTED_PATTERNS = (
    "spotify-json",
    "spotify-proto",
    "youtube.response",
    "spclient.wg.spotify.com",
    "raw.githubusercontent.com/app2smile/rules/master/js/spotify-json.js",
    "raw.githubusercontent.com/app2smile/rules/master/js/spotify-proto.js",
    "raw.githubusercontent.com/app2smile/rules/master/module/spotify.module",
    "Maasea/sgmodule",
    "blackmatrix7/ios_rule_script",
    "Cats-Team/AdRules",
    "Remote AdBlock Hub",
    "zirawell/R-Store",
    "fmz200/wool_scripts",
    "app2smile",
    EXPECTED_UPDATE_URL,
    "https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule",
)

URL_RE = re.compile(r"https?://[^\s\"'<>)\],]+")
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")
SCRIPT_PATH_RE = re.compile(r"script-path=(https?://[^,\s]+)")
UPDATE_URL_RE = re.compile(r"^#!update-url=(https?://\S+)\s*$")
HTML_ERROR_TOKENS = (
    "404 not found",
    "not found",
    "repository not found",
    "file not found",
    "there isn't a github pages site here",
)
TRANSIENT_ERRORS = {"TIMEOUT", "DNS_ERROR", "HTTP 429", "HTTP 500", "HTTP 502", "HTTP 503", "HTTP 504"}
CI_BLOCKED_SCRIPT_HOSTS = {"kelee.one"}


@dataclass(frozen=True)
class LinkItem:
    url: str
    line_no: int
    section: str
    kind: str
    line: str


@dataclass
class CheckResult:
    ok: bool
    status: int | None = None
    error_type: str = ""
    final_url: str = ""
    content_length: int | None = None
    content_type: str = ""
    sample: str = ""

    @property
    def last_error(self) -> str:
        if self.status:
            return f"HTTP {self.status}" if not self.error_type else f"HTTP {self.status} {self.error_type}"
        return self.error_type or "UNKNOWN_ERROR"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_module() -> list[str]:
    try:
        return MODULE_PATH.read_text(encoding="utf-8").splitlines()
    except UnicodeError as exc:
        fail(f"encoding error while reading {MODULE_PATH}: {exc}")
    except OSError as exc:
        fail(f"cannot read {MODULE_PATH}: {exc}")


def section_map(lines: list[str]) -> dict[str, int]:
    sections: dict[str, int] = {}
    for idx, line in enumerate(lines, 1):
        match = SECTION_RE.match(line.strip())
        if match:
            sections[match.group(1)] = idx
    missing = sorted(REQUIRED_SECTIONS - set(sections))
    if missing:
        fail(f"required sections missing: {', '.join(missing)}")
    return sections


def current_section(line: str, active: str) -> str:
    match = SECTION_RE.match(line.strip())
    if match:
        return match.group(1)
    return active


def clean_url(url: str) -> str:
    return url.rstrip(".,;")


def is_auditable_url(url: str) -> bool:
    """Return true only for literal external source URLs.

    Rewrite and body-rewrite sections often contain URL regex patterns such as
    https://example\.com:\d+/. Those are valid module matchers, but they are not
    network resources and must not be HEAD/GET checked.
    """
    parsed = urllib.parse.urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        return False
    regex_netloc_tokens = ("\\", "^", "$", "*", "+", "?", "(", ")", "[", "]", "{", "}", "|")
    return not any(token in parsed.netloc for token in regex_netloc_tokens)


def classify_line(line: str, url: str) -> str:
    stripped = line.strip()
    if SCRIPT_PATH_RE.search(line):
        return "script"
    if stripped.startswith("RULE-SET,"):
        return "rule-set"
    if stripped.startswith("DOMAIN-SET,"):
        return "domain-set"
    if UPDATE_URL_RE.match(stripped):
        return "update-url"
    if "raw.githubusercontent.com" in url or "githubusercontent" in url:
        return "raw"
    if "github.com" in url and "/blob/" in url:
        return "github-blob"
    if "github.io" in url:
        return "github-pages"
    return "external"


def scan_links(lines: list[str]) -> list[LinkItem]:
    links: list[LinkItem] = []
    seen: set[tuple[str, int]] = set()
    section = ""
    for idx, line in enumerate(lines, 1):
        section = current_section(line, section)
        explicit: list[str] = []
        script_match = SCRIPT_PATH_RE.search(line)
        if script_match:
            explicit.append(script_match.group(1))
        update_match = UPDATE_URL_RE.match(line.strip())
        if update_match:
            explicit.append(update_match.group(1))
        parts = [part.strip() for part in line.split(",")]
        if len(parts) >= 2 and parts[0].strip() in {"RULE-SET", "DOMAIN-SET"} and parts[1].startswith("http"):
            explicit.append(parts[1])
        if not section or line.lstrip().startswith("#"):
            explicit.extend(URL_RE.findall(line))
        for raw_url in explicit:
            url = clean_url(raw_url)
            if "$" in url or not is_auditable_url(url):
                continue
            key = (url, idx)
            if key in seen:
                continue
            seen.add(key)
            links.append(LinkItem(url=url, line_no=idx, section=section or "GLOBAL", kind=classify_line(line, url), line=line))
    return links


def request_url(url: str, method: str) -> CheckResult:
    headers = {"User-Agent": USER_AGENT, "Accept": "*/*"}
    if method == "GET":
        headers["Range"] = "bytes=0-2048"
    req = urllib.request.Request(url, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT_SECONDS) as resp:
            body = resp.read(2049) if method == "GET" else b""
            length_header = resp.headers.get("Content-Length") or resp.headers.get("Content-Range")
            content_length = int(length_header) if length_header and length_header.isdigit() else len(body) or None
            return CheckResult(
                ok=True,
                status=resp.status,
                final_url=resp.geturl(),
                content_length=content_length,
                content_type=resp.headers.get("Content-Type", ""),
                sample=body.decode("utf-8", errors="ignore")[:2048],
            )
    except urllib.error.HTTPError as exc:
        body = exc.read(2049) if method == "GET" else b""
        return CheckResult(
            ok=False,
            status=exc.code,
            error_type=classify_http_error(exc.code),
            final_url=exc.geturl(),
            content_length=len(body) or None,
            content_type=exc.headers.get("Content-Type", "") if exc.headers else "",
            sample=body.decode("utf-8", errors="ignore")[:2048],
        )
    except urllib.error.URLError as exc:
        reason = str(exc.reason)
        if "timed out" in reason.lower():
            return CheckResult(ok=False, error_type="TIMEOUT")
        if "name or service not known" in reason.lower() or "getaddrinfo failed" in reason.lower():
            return CheckResult(ok=False, error_type="DNS_ERROR")
        return CheckResult(ok=False, error_type=f"URL_ERROR: {reason[:120]}")
    except TimeoutError:
        return CheckResult(ok=False, error_type="TIMEOUT")
    except OSError as exc:
        return CheckResult(ok=False, error_type=f"NETWORK_ERROR: {str(exc)[:120]}")


def classify_http_error(status: int) -> str:
    if status == 404:
        return "NOT_FOUND"
    if status == 410:
        return "GONE"
    if status == 429:
        return "HTTP 429"
    if status >= 500:
        return f"HTTP {status}"
    return f"HTTP {status}"


def is_html_error(result: CheckResult, item: LinkItem) -> bool:
    if item.kind not in {"script", "rule-set", "domain-set", "raw", "update-url"}:
        return False
    sample = result.sample.lower()
    content_type = result.content_type.lower()
    if "text/html" not in content_type:
        return False
    if item.kind == "github-blob" and result.status and 200 <= result.status < 400:
        return False
    parsed_original = urllib.parse.urlparse(item.url)
    parsed_final = urllib.parse.urlparse(result.final_url or item.url)
    if parsed_original.netloc and parsed_final.netloc and parsed_original.netloc != parsed_final.netloc:
        return True
    return any(token in sample for token in HTML_ERROR_TOKENS)


def check_link(item: LinkItem) -> CheckResult:
    parsed = urllib.parse.urlparse(item.url)
    if item.kind == "script" and parsed.netloc.lower() in CI_BLOCKED_SCRIPT_HOSTS:
        return CheckResult(ok=True, error_type="SKIPPED_CI_BLOCKED_HOST")
    head = request_url(item.url, "HEAD")
    needs_get = (
        not head.ok
        or head.status is None
        or head.status >= 400
        or head.content_length == 0
        or "text/html" in head.content_type.lower()
    )
    result = request_url(item.url, "GET") if needs_get else head
    if result.ok and result.status and 200 <= result.status < 400:
        if result.content_length == 0 and item.kind in {"script", "rule-set", "domain-set", "raw", "update-url"}:
            result.ok = False
            result.error_type = "EMPTY_CONTENT"
        elif is_html_error(result, item):
            result.ok = False
            result.error_type = "UNRELATED_HTML"
    return result


def is_transient(result: CheckResult) -> bool:
    if result.status in {429, 500, 502, 503, 504}:
        return True
    return result.error_type in TRANSIENT_ERRORS or result.error_type.startswith("URL_ERROR")


def is_protected(item: LinkItem) -> bool:
    haystack = f"{item.url}\n{item.line}"
    return any(pattern in haystack for pattern in PROTECTED_PATTERNS)


def load_history() -> dict[str, dict[str, object]]:
    if not HISTORY_PATH.exists():
        return {}
    try:
        return json.loads(HISTORY_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, UnicodeError) as exc:
        fail(f"invalid history file {HISTORY_PATH}: {exc}")


def save_history(history: dict[str, dict[str, object]]) -> None:
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    write_text_lf(HISTORY_PATH, json.dumps(history, ensure_ascii=False, indent=2, sort_keys=True) + "\n")


def update_history(
    history: dict[str, dict[str, object]],
    links: Iterable[LinkItem],
    results: dict[str, CheckResult],
    today: str,
) -> dict[str, dict[str, object]]:
    by_url = {item.url: item for item in links}
    updated = {url: record for url, record in history.items() if url in by_url}
    for url, item in by_url.items():
        result = results[url]
        if result.ok:
            updated.pop(url, None)
            continue
        old = updated.get(url, {})
        updated[url] = {
            "first_seen": old.get("first_seen", today),
            "last_seen": today,
            "fail_count": int(old.get("fail_count", 0)) + 1,
            "last_error": result.last_error,
            "section": item.section,
            "line_preview": item.line.strip()[:240],
        }
    return updated


def validate_module(lines: list[str]) -> None:
    text = "\n".join(lines)
    sections = section_map(lines)
    for token in CORE_TOKENS:
        if token not in text:
            fail(f"required core token missing: {token}")
    update_url = ""
    for line in lines:
        update_match = UPDATE_URL_RE.match(line.strip())
        if update_match:
            update_url = update_match.group(1)
            break
    if update_url != EXPECTED_UPDATE_URL:
        fail(f"update-url must point to {EXPECTED_UPDATE_URL}")
    if not any(line.strip() and not line.lstrip().startswith("#") for line in lines[sections["Script"] : sections["MITM"] - 1]):
        fail("[Script] section would become empty")
    if not any(line.strip().startswith("hostname = ") for line in lines[sections["MITM"] :]):
        fail("[MITM] section would become empty")


def write_text_lf(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


def markdown_list(items: Iterable[str], empty: str = "无") -> str:
    unique = list(dict.fromkeys(items))
    if not unique:
        return f"- {empty}\n"
    return "".join(f"- `{item}`\n" for item in unique)


def generate_report(
    today: str,
    lines: list[str],
    links: list[LinkItem],
    results: dict[str, CheckResult],
    history: dict[str, dict[str, object]],
    sections: dict[str, int],
    auto_disabled: list[str],
    auto_replaced: list[tuple[str, str]],
    protected_failed: list[str],
    manual: list[str],
) -> str:
    failed_today = [url for url, result in results.items() if not result.ok]
    ok_count = len(results) - len(failed_today)
    two_days = [url for url, record in history.items() if int(record.get("fail_count", 0)) == 2]
    three_days = [url for url, record in history.items() if int(record.get("fail_count", 0)) >= 3]
    spotify_ok = all(token in "\n".join(lines) for token in ("spotify-json", "spotify-proto"))
    youtube_ok = "youtube.response" in "\n".join(lines)
    update_ok = EXPECTED_UPDATE_URL in "\n".join(lines)

    replacement_lines = [f"`{old}` -> `{new}`" for old, new in auto_replaced]
    protected_marked = [f"{url} - PROTECTED_FAILED_NEEDS_MANUAL_CONFIRMATION" for url in protected_failed]

    return "\n".join(
        [
            "# Daily Invalid Rule Audit Report",
            "",
            f"- 日期：{today}",
            f"- 模块总行数：{len(lines)}",
            f"- 扫描到的外部链接数量：{len(results)}",
            f"- 正常链接数量：{ok_count}",
            f"- 当天失败链接数量：{len(failed_today)}",
            f"- [Rule] 存在：{'yes' if 'Rule' in sections else 'no'}",
            f"- [Script] 存在：{'yes' if 'Script' in sections else 'no'}",
            f"- [MITM] 存在：{'yes' if 'MITM' in sections else 'no'}",
            f"- update-url 是否正确：{'yes' if update_ok else 'no'}",
            f"- Spotify 核心检查结果：{'pass' if spotify_ok else 'fail'}",
            f"- YouTube 核心检查结果：{'pass' if youtube_ok else 'fail'}",
            "",
            "本阶段只审计生成产物，不直接修改模块；源文件修复由 audit_repair_invalid_sources.py 在构建前完成。",
            "",
            "## 连续失败 2 天的链接",
            markdown_list(two_days).rstrip(),
            "",
            "## 连续失败 3 天及以上的链接",
            markdown_list(three_days).rstrip(),
            "",
            "## 本阶段直接注释的链接（应始终为空）",
            markdown_list(auto_disabled).rstrip(),
            "",
            "## 本阶段直接替换的链接（应始终为空）",
            markdown_list(replacement_lines).rstrip(),
            "",
            "## 受保护但失败的链接",
            markdown_list(protected_marked).rstrip(),
            "",
            "## 需要人工确认的链接",
            markdown_list(manual).rstrip(),
            "",
            "## 当天失败明细",
            markdown_list([f"{url} ({results[url].last_error})" for url in failed_today]).rstrip(),
            "",
            "## 不执行删除的说明",
            "- 最终模块是生成产物，本脚本不会直接注释、替换或删除其中的行。",
            "- 自动修复必须先修改 Rules、Rewrite、Scripts 或远程源登记，再由 Builder 重新生成产物。",
            "- 自动删除被禁用；低风险、确认无替代且连续多日失效的内容也需要人工确认后再处理。",
            "- Spotify、YouTube、核心远程规则源和主模块地址即使失败也只报告，不自动注释或删除。",
            "",
        ]
    )


def guard_github_outage(links: list[LinkItem], results: dict[str, CheckResult]) -> None:
    github_urls = [item.url for item in links if "github" in urllib.parse.urlparse(item.url).netloc]
    transient = [url for url in github_urls if not results[url].ok and is_transient(results[url])]
    if len(github_urls) >= 10 and len(transient) >= max(5, len(github_urls) // 3):
        fail("large number of GitHub links failed with transient errors; likely network or GitHub outage")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--report-only",
        action="store_true",
        help="explicitly document that generated module output will not be edited",
    )
    return parser.parse_args()


def main() -> None:
    parse_args()
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).date().isoformat()
    REPORT_DIR.mkdir(parents=True, exist_ok=True)

    lines = read_module()
    sections = section_map(lines)
    validate_module(lines)

    links = scan_links(lines)
    unique_links: dict[str, LinkItem] = {}
    for item in links:
        unique_links.setdefault(item.url, item)

    results = {url: check_link(item) for url, item in unique_links.items()}
    guard_github_outage(list(unique_links.values()), results)

    old_history = load_history()
    history = update_history(old_history, unique_links.values(), results, today)
    protected_failed = [
        item.url for item in unique_links.values() if not results[item.url].ok and is_protected(item)
    ]
    manual = [
        url
        for url, record in history.items()
        if int(record.get("fail_count", 0)) >= 3
    ]
    save_history(history)

    report = generate_report(
        today,
        lines,
        list(unique_links.values()),
        results,
        history,
        sections,
        [],
        [],
        protected_failed,
        manual,
    )
    write_text_lf(REPORT_PATH, report)
    print(f"Audited {len(unique_links)} links, failed today: {sum(1 for r in results.values() if not r.ok)}")


if __name__ == "__main__":
    main()
