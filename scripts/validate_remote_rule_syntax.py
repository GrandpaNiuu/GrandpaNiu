#!/usr/bin/env python3
"""Validate published remote RULE-SET and DOMAIN-SET syntax before release.

This guard prevents Shadowrocket red-cross failures caused by mixing formats,
such as putting a pure domain list or Quantumult X rules into a Shadowrocket
RULE-SET.

The validator is intentionally strict for repository-owned outputs. It also
normalizes known upstreams whose files are pure domain sets before validation,
so stale generated outputs cannot keep reintroducing the same red-cross issue.
"""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "remote_rule_syntax_report.md"
REMOTES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
USER_AGENT = "GrandpaNiu-Remote-Rule-Syntax-Validator/1.2"

SCAN_FILES = [
    ROOT / "Ronghemokuai.sgmodule",
    ROOT / "Release" / "Ronghemokuai.sgmodule",
    ROOT / "Rules" / "aggressive-ad-sources.list",
]

NORMALIZE_TEXT_FILES = [
    *SCAN_FILES,
    ROOT / "Rewrite" / "Sources" / "Rule.conf",
    ROOT / "Rules" / "original-remote-rule-sets.list",
]

PAGES_PREFIX = "https://grandpaniuu.github.io/GrandpaNiu/"
RAW_PREFIX = "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/"

KNOWN_DOMAIN_SET_URLS = {
    "https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list",
    "https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt",
}

RULE_LINE_RE = re.compile(r"^(RULE-SET|DOMAIN-SET),([^,\s]+),([^,\s]+)(?:,.*)?$", re.I)
HTML_RE = re.compile(r"^\s*(?:<!doctype\s+html|<html|<head|<body)\b", re.I)
DOMAIN_SET_VALUE_RE = re.compile(
    r"^(?:\+\.)?(?:\*\.)?\.?[A-Za-z0-9_][A-Za-z0-9_.-]*[A-Za-z0-9_]$|^localhost$",
    re.I,
)

ALLOWED_RULE_TYPES = {
    "AND",
    "OR",
    "NOT",
    "DOMAIN",
    "DOMAIN-SUFFIX",
    "DOMAIN-KEYWORD",
    "DOMAIN-WILDCARD",
    "DOMAIN-REGEX",
    "IP-CIDR",
    "IP-CIDR6",
    "IP-ASN",
    "GEOIP",
    "PROCESS-NAME",
    "USER-AGENT",
    "URL-REGEX",
    "DST-PORT",
    "SRC-PORT",
    "SRC-IP",
    "SRC-IP-CIDR",
    "PROTOCOL",
    "RULE-SET",
    "SCRIPT",
}

INCOMPATIBLE_QUANX_TYPES = {
    "HOST",
    "HOST-SUFFIX",
    "HOST-KEYWORD",
    "IP6-CIDR",
    "GEOIP6",
}

SECTION_HEADERS = {
    "[RULE]",
    "[RULES]",
    "[URL REWRITE]",
    "[HEADER REWRITE]",
    "[BODY REWRITE]",
    "[MAP LOCAL]",
    "[SCRIPT]",
    "[MITM]",
    "[GENERAL]",
}


@dataclass
class RemoteRef:
    rule_type: str
    url: str
    policy: str
    sources: set[str] = field(default_factory=set)


@dataclass
class CheckResult:
    rule_type: str
    url: str
    sources: list[str]
    status: str
    checked_from: str
    rule_count: int
    errors: list[str]


def stop(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def is_repo_owned_url(url: str) -> bool:
    return url.startswith(PAGES_PREFIX) or url.startswith(RAW_PREFIX)


def normalize_known_remote_types() -> list[str]:
    """Rewrite known pure-domain upstreams from RULE-SET to DOMAIN-SET.

    This intentionally edits generated module outputs before validation. The
    workflow commits generated outputs after validation, so stale red-cross
    lines are repaired rather than repeatedly failing the same run.
    """
    changes: list[str] = []
    for path in NORMALIZE_TEXT_FILES:
        if not path.exists():
            continue
        text = read(path)
        original = text
        for url in KNOWN_DOMAIN_SET_URLS:
            text = text.replace(f"RULE-SET,{url},", f"DOMAIN-SET,{url},")
        if text != original:
            write(path, text)
            changes.append(path.relative_to(ROOT).as_posix())

    if REMOTES_JSON.exists():
        try:
            data = json.loads(read(REMOTES_JSON))
        except json.JSONDecodeError as exc:
            stop(f"invalid JSON in {REMOTES_JSON.relative_to(ROOT)}: {exc}")
        changed_json = False
        for item in data.get("rule_sets", []):
            url = str(item.get("url", "")).strip()
            if url in KNOWN_DOMAIN_SET_URLS and item.get("type") != "DOMAIN-SET":
                item["type"] = "DOMAIN-SET"
                item["purpose"] = str(item.get("purpose", "domain-set remote rule source"))
                changed_json = True
        if changed_json:
            write(REMOTES_JSON, json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            changes.append(REMOTES_JSON.relative_to(ROOT).as_posix())
    return changes


def write_report(results: list[CheckResult], normalizations: list[str]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    failed = [result for result in results if result.status == "fail"]
    warned = [result for result in results if result.status == "warn"]
    lines = [
        "# 远程规则语法校验报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告用于阻断 Shadowrocket / Surge 远程规则集红叉问题。校验目标包括：",
        "",
        "- `RULE-SET` 远程内容必须是 Shadowrocket/Surge 可识别的规则类型。",
        "- `DOMAIN-SET` 远程内容必须是纯域名集合，不允许混入带逗号的规则行。",
        "- 不允许把 Quantumult X 的 `host`、`host-suffix`、`host-keyword`、`ip6-cidr` 直接作为 Shadowrocket `RULE-SET`。",
        "- 已知纯域名上游会在验证前自动规范成 `DOMAIN-SET`，防止旧生成文件反复导致红叉。",
        "- 仓库自有 Pages / raw 链接严格阻断；外部源下载失败记录为 warn，避免网络抖动阻断仓库构建。",
        "",
        "## 汇总",
        "",
        f"- 检查远程规则数：{len(results)}",
        f"- 通过：{len(results) - len(failed) - len(warned)}",
        f"- 警告：{len(warned)}",
        f"- 失败：{len(failed)}",
        f"- 自动规范化文件数：{len(normalizations)}",
        "",
        "## 自动规范化文件",
        "",
    ]
    if normalizations:
        lines.extend(f"- `{path}`" for path in normalizations)
    else:
        lines.append("- 无")
    lines += [
        "",
        "## 明细",
        "",
        "| 状态 | 类型 | 规则数 | 检查来源 | 引用位置 | URL | 错误 / 警告 |",
        "|---|---|---:|---|---|---|---|",
    ]
    for result in results:
        source_text = "<br>".join(sorted(result.sources))
        error_text = "<br>".join(result.errors) if result.errors else "-"
        lines.append(
            f"| {result.status} | {result.rule_type} | {result.rule_count} | {result.checked_from} | {source_text} | `{result.url}` | {error_text} |"
        )
    lines += [
        "",
        "## 发布规则",
        "",
        "- 本报告出现 `fail` 时，不允许发布模块。",
        "- `warn` 表示外部源下载失败或临时不可读，需要人工观察，但不阻断仓库自有构建。",
        "- 新增远程源前，必须先确认源格式属于 `RULE-SET` 或 `DOMAIN-SET` 的真实兼容格式。",
        "- 如果上游是 Quantumult X 格式，必须先转换到 `Rules/converted/` 后再引用。",
        "- 如果上游是纯域名列表，必须用 `DOMAIN-SET`，不能用 `RULE-SET`。",
        "",
    ]
    write(REPORT, "\n".join(lines))


def collect_refs_from_text(path: Path, refs: dict[tuple[str, str], RemoteRef]) -> None:
    text = read(path)
    if not text:
        return
    for lineno, raw in enumerate(text.splitlines(), 1):
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            continue
        match = RULE_LINE_RE.match(stripped)
        if not match:
            continue
        rule_type, url, policy = match.groups()
        key = (rule_type.upper(), url)
        refs.setdefault(key, RemoteRef(rule_type.upper(), url, policy)).sources.add(f"{path.relative_to(ROOT)}:{lineno}")


def collect_refs_from_json(refs: dict[tuple[str, str], RemoteRef]) -> None:
    if not REMOTES_JSON.exists():
        return
    try:
        data = json.loads(read(REMOTES_JSON))
    except json.JSONDecodeError as exc:
        stop(f"invalid JSON in {REMOTES_JSON.relative_to(ROOT)}: {exc}")
    for index, item in enumerate(data.get("rule_sets", []), 1):
        if not item.get("enabled", False):
            continue
        rule_type = str(item.get("type", "")).strip().upper()
        url = str(item.get("url", "")).strip()
        policy = str(item.get("policy", "REJECT")).strip()
        if not rule_type or not url:
            continue
        key = (rule_type, url)
        name = str(item.get("name", f"rule_sets[{index}]")).strip()
        refs.setdefault(key, RemoteRef(rule_type, url, policy)).sources.add(f"Rewrite/Remotes/sources.json:{name}")


def local_path_for_url(url: str) -> Path | None:
    if url.startswith(PAGES_PREFIX):
        candidate = ROOT / url[len(PAGES_PREFIX):]
        return candidate if candidate.exists() else None
    if url.startswith(RAW_PREFIX):
        candidate = ROOT / url[len(RAW_PREFIX):]
        return candidate if candidate.exists() else None
    return None


def fetch_remote(url: str) -> tuple[str, str]:
    local = local_path_for_url(url)
    if local is not None:
        return read(local), f"local:{local.relative_to(ROOT)}"
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=45) as response:
            status = getattr(response, "status", 200)
            body = response.read().decode("utf-8", errors="replace")
            return body, f"http:{status}"
    except urllib.error.HTTPError as exc:
        return "", f"HTTP {exc.code}"
    except urllib.error.URLError as exc:
        return "", f"URL error: {exc}"


def normalize_rule_line(line: str) -> str:
    line = line.strip()
    if line.startswith("- "):
        line = line[2:].strip()
    return line


def active_rule_lines(text: str) -> list[tuple[int, str]]:
    lines: list[tuple[int, str]] = []
    for lineno, raw in enumerate(text.splitlines(), 1):
        stripped = normalize_rule_line(raw)
        if not stripped:
            continue
        if stripped.startswith(("#", ";", "//")):
            continue
        upper = stripped.upper()
        if upper in SECTION_HEADERS or stripped.lower() == "payload:":
            continue
        lines.append((lineno, stripped))
    return lines


def basic_content_errors(text: str, checked_from: str) -> list[str]:
    if not text.strip():
        return [f"empty or unreadable content ({checked_from})"]
    head = text.lstrip()[:200]
    if HTML_RE.match(head):
        return ["downloaded HTML instead of a rule file"]
    if head.startswith("404:") or "404 Not Found" in head[:500]:
        return ["downloaded 404 content instead of a rule file"]
    return []


def looks_like_domain_set(lines: list[tuple[int, str]]) -> bool:
    if not lines:
        return False
    sample = [line for _, line in lines[:30]]
    if any("," in line for line in sample):
        return False
    return sum(1 for line in sample if DOMAIN_SET_VALUE_RE.match(line)) >= max(3, len(sample) // 2)


def validate_rule_set(text: str) -> tuple[int, list[str]]:
    errors: list[str] = []
    lines = active_rule_lines(text)
    if looks_like_domain_set(lines):
        return len(lines), ["remote content looks like a pure DOMAIN-SET; change the reference type from RULE-SET to DOMAIN-SET"]
    for lineno, line in lines:
        first = line.split(",", 1)[0].strip()
        token = first.upper()
        if token in INCOMPATIBLE_QUANX_TYPES:
            errors.append(f"line {lineno}: incompatible QuanX rule type `{first}`")
            continue
        if token not in ALLOWED_RULE_TYPES:
            errors.append(f"line {lineno}: unsupported RULE-SET rule type `{first}`")
            continue
        if token in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "DOMAIN-WILDCARD", "DOMAIN-REGEX"}:
            parts = [part.strip() for part in line.split(",")]
            if len(parts) < 2 or not parts[1]:
                errors.append(f"line {lineno}: missing domain value")
        elif token in {"IP-CIDR", "IP-CIDR6", "SRC-IP-CIDR"}:
            parts = [part.strip() for part in line.split(",")]
            if len(parts) < 2 or "/" not in parts[1]:
                errors.append(f"line {lineno}: missing CIDR value")
        if len(errors) >= 30:
            errors.append("too many errors; output truncated")
            break
    return len(lines), errors


def validate_domain_set(text: str) -> tuple[int, list[str]]:
    errors: list[str] = []
    lines = active_rule_lines(text)
    for lineno, line in lines:
        if "," in line:
            errors.append(f"line {lineno}: DOMAIN-SET must not contain comma rule syntax")
            continue
        if line.startswith(("http://", "https://")):
            errors.append(f"line {lineno}: DOMAIN-SET contains URL instead of domain")
            continue
        if "/" in line:
            errors.append(f"line {lineno}: DOMAIN-SET contains slash path or CIDR-like value")
            continue
        if not DOMAIN_SET_VALUE_RE.match(line):
            errors.append(f"line {lineno}: invalid DOMAIN-SET value `{line}`")
        if len(errors) >= 30:
            errors.append("too many errors; output truncated")
            break
    return len(lines), errors


def classify_status(ref: RemoteRef, checked_from: str, errors: list[str]) -> str:
    if not errors:
        return "pass"
    if is_repo_owned_url(ref.url):
        return "fail"
    if checked_from.startswith(("HTTP ", "URL error:")):
        return "warn"
    if any("downloaded HTML" in error or "downloaded 404" in error or "empty or unreadable" in error for error in errors):
        return "warn"
    return "fail"


def check_ref(ref: RemoteRef) -> CheckResult:
    text, checked_from = fetch_remote(ref.url)
    errors = basic_content_errors(text, checked_from)
    rule_count = 0
    if not errors:
        if ref.rule_type == "RULE-SET":
            rule_count, errors = validate_rule_set(text)
        elif ref.rule_type == "DOMAIN-SET":
            rule_count, errors = validate_domain_set(text)
        else:
            errors = [f"unsupported remote reference type `{ref.rule_type}`"]
    status = classify_status(ref, checked_from, errors)
    return CheckResult(
        rule_type=ref.rule_type,
        url=ref.url,
        sources=sorted(ref.sources),
        status=status,
        checked_from=checked_from,
        rule_count=rule_count,
        errors=errors,
    )


def main() -> None:
    normalizations = normalize_known_remote_types()
    refs: dict[tuple[str, str], RemoteRef] = {}
    for path in SCAN_FILES:
        collect_refs_from_text(path, refs)
    collect_refs_from_json(refs)

    results = [check_ref(ref) for ref in sorted(refs.values(), key=lambda item: (item.rule_type, item.url))]
    write_report(results, normalizations)

    failed = [result for result in results if result.status == "fail"]
    if failed:
        for result in failed:
            print(f"FAIL {result.rule_type} {result.url}: {'; '.join(result.errors)}", file=sys.stderr)
        raise SystemExit(f"remote rule syntax validation failed: {len(failed)} source(s)")

    warned = [result for result in results if result.status == "warn"]
    if warned:
        for result in warned:
            print(f"WARN {result.rule_type} {result.url}: {'; '.join(result.errors)}", file=sys.stderr)
    print(
        f"Remote rule syntax validation completed: {len(results)} source(s), "
        f"{len(warned)} warning(s), {len(normalizations)} normalization file(s); "
        f"report={REPORT.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
