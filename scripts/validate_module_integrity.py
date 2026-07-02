#!/usr/bin/env python3
"""Validate generated Fusion module integrity and duplicate safety."""

from __future__ import annotations

from collections import Counter, defaultdict
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
SOURCES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
REPORT = ROOT / "reports" / "module_integrity_report.md"

SECTION_ORDER = (
    "Rule",
    "URL Rewrite",
    "Header Rewrite",
    "Body Rewrite",
    "Map Local",
    "Script",
    "MITM",
)
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")
RULE_PREFIXES = {
    "AND",
    "DOMAIN",
    "DOMAIN-KEYWORD",
    "DOMAIN-SET",
    "DOMAIN-SUFFIX",
    "GEOIP",
    "IP-CIDR",
    "IP-CIDR6",
    "FINAL",
    "RULE-SET",
    "URL-REGEX",
}
SCRIPT_TYPES = {"http-request", "http-response"}
REWRITE_ACTIONS = (
    "reject",
    "reject-200",
    "reject-array",
    "reject-dict",
    "reject-img",
    "reject-ttl",
    "echo-response",
    "script-path=",
    "header-del ",
    "header-replace ",
    "302 ",
    " 302",
    "307 ",
    " 307",
    "308 ",
    " 308",
    " header",
)


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8", errors="replace")


def active_lines(lines: list[str]) -> list[str]:
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


def split_sections(text: str) -> tuple[dict[str, list[str]], list[str]]:
    sections: dict[str, list[str]] = {}
    seen_headers: list[str] = []
    current = "META"
    sections[current] = []
    for line in text.splitlines():
        match = SECTION_RE.match(line.strip())
        if match:
            current = match.group(1)
            seen_headers.append(current)
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(line.rstrip())
    return sections, seen_headers


def duplicate_values(values: list[str]) -> list[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def validate_rule_line(line: str) -> None:
    prefix = line.split(",", 1)[0]
    if prefix not in RULE_PREFIXES:
        fail(f"unsupported Rule prefix: {line}")
    if prefix in {"RULE-SET", "DOMAIN-SET"} and ",https://" not in line:
        fail(f"remote rule must use https URL: {line}")
    if prefix in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD"} and line.count(",") < 2:
        fail(f"domain rule missing policy: {line}")
    if prefix in {"IP-CIDR", "IP-CIDR6"} and line.count(",") < 2:
        fail(f"IP rule missing policy: {line}")
    if prefix == "GEOIP" and line.count(",") < 2:
        fail(f"GEOIP rule missing country and policy: {line}")
    if prefix == "FINAL" and line.count(",") < 1:
        fail(f"FINAL rule missing policy: {line}")


def validate_script_line(line: str) -> str:
    match = SCRIPT_NAME_RE.match(line)
    if not match:
        fail(f"script line missing name: {line}")
    name = match.group(1).strip()
    body = line.split("=", 1)[1]
    if not any(f"type={script_type}" in body for script_type in SCRIPT_TYPES):
        fail(f"script line missing supported type: {line}")
    if "script-path=" not in body:
        fail(f"script line missing script-path: {line}")
    if "pattern=" not in body:
        fail(f"script line missing pattern: {line}")
    return name


def validate_rewrite_line(section: str, line: str) -> None:
    if section == "Header Rewrite":
        if " header-del " not in line and " header-replace " not in line:
            fail(f"Header Rewrite line has unsupported action: {line}")
        return
    if section == "Body Rewrite":
        if not line.startswith(("http-request ", "http-response ", "http-response-jq ")):
            fail(f"Body Rewrite line has unsupported verb: {line}")
        if len(line.split()) < 3:
            fail(f"Body Rewrite line is incomplete: {line}")
        return
    if section == "Map Local":
        if " data-type=" not in line:
            fail(f"Map Local line must include data-type: {line}")
        if " data=" not in line and "data-type=tiny-gif" not in line:
            fail(f"Map Local line must include data unless it uses tiny-gif: {line}")
        return
    if not any(action in line for action in REWRITE_ACTIONS):
        fail(f"{section} line has unsupported action: {line}")


def parse_hosts(lines: list[str]) -> list[str]:
    hosts: list[str] = []
    for line in lines:
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        hosts.extend(host.strip() for host in value.split(",") if host.strip())
    return hosts


def validate_sources_json() -> tuple[int, int]:
    data = json.loads(read_text(SOURCES_JSON))
    urls = [str(item.get("url", "")).strip() for item in data.get("rule_sets", [])]
    dupes = duplicate_values([url for url in urls if url])
    if dupes:
        fail("duplicate remote source URLs: " + ", ".join(dupes[:10]))
    enabled = sum(1 for item in data.get("rule_sets", []) if item.get("enabled"))
    return len(urls), enabled


def validate_local_rule_files() -> tuple[int, int]:
    total = 0
    cross_file: dict[str, set[str]] = defaultdict(set)
    for path in sorted((ROOT / "Rules").rglob("*.list")):
        lines = active_lines(read_text(path).splitlines())
        total += len(lines)
        dupes = duplicate_values(lines)
        if dupes:
            fail(f"{path.relative_to(ROOT)} has duplicate active rule entries: {', '.join(dupes[:10])}")
        for line in lines:
            cross_file[line].add(path.relative_to(ROOT).as_posix())
    overlap_count = sum(1 for files in cross_file.values() if len(files) > 1)
    return total, overlap_count


def validate_all(write_report: bool = True) -> dict[str, object]:
    root_text = read_text(MODULE)
    if root_text != read_text(RELEASE):
        fail("Ronghemokuai.sgmodule and Release/Ronghemokuai.sgmodule differ")

    sections, headers = split_sections(root_text)
    header_dupes = duplicate_values(headers)
    if header_dupes:
        fail("duplicate module sections: " + ", ".join(header_dupes))
    missing = [section for section in SECTION_ORDER if not active_lines(sections.get(section, []))]
    if missing:
        fail("missing or empty module sections: " + ", ".join(missing))

    section_counts: dict[str, int] = {}
    for section in SECTION_ORDER:
        lines = active_lines(sections.get(section, []))
        section_counts[section] = len(lines)
        dupes = duplicate_values(lines)
        if dupes:
            fail(f"[{section}] has duplicate active lines: " + ", ".join(dupes[:10]))
        if section == "Rule":
            for line in lines:
                validate_rule_line(line)
        elif section in {"URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local"}:
            for line in lines:
                validate_rewrite_line(section, line)

    script_names = [validate_script_line(line) for line in active_lines(sections["Script"])]
    script_dupes = duplicate_values(script_names)
    if script_dupes:
        fail("duplicate script names: " + ", ".join(script_dupes[:20]))

    hosts = parse_hosts(sections["MITM"])
    host_dupes = duplicate_values(hosts)
    if host_dupes:
        fail("duplicate MITM hostnames: " + ", ".join(host_dupes[:20]))

    remote_total, remote_enabled = validate_sources_json()
    local_rule_total, cross_file_overlap = validate_local_rule_files()

    result: dict[str, object] = {
        "date": dt.date.today().isoformat(),
        "sections": section_counts,
        "scripts": len(script_names),
        "mitm_hosts": len(hosts),
        "remote_total": remote_total,
        "remote_enabled": remote_enabled,
        "local_rule_total": local_rule_total,
        "cross_file_overlap": cross_file_overlap,
    }
    if write_report:
        write_integrity_report(result)
    return result


def write_integrity_report(result: dict[str, object]) -> None:
    lines = [
        "# Fusion 模块完整性报告",
        "",
        f"- 日期：{result['date']}",
        "- 结论：Fusion 输出语法结构、重复项、脚本入口、MITM hostname 和远程规则源索引均通过本地静态检查。",
        "- 说明：跨规则包重复只作为信息记录；最终 `Ronghemokuai.sgmodule` 构建时会按 active line 去重，单独规则包仍保留各自可独立使用的交集。",
        "",
        "## 输出模块",
        "",
        "| 检查项 | 结果 |",
        "|---|---|",
        "| Root / Release 内容一致 | 通过 |",
        "| 重复 section | 无 |",
        "| 重复 active rule / rewrite / script / MITM line | 无 |",
        f"| Script 入口数 | {result['scripts']} |",
        f"| MITM hostname 数 | {result['mitm_hosts']} |",
        "",
        "## Section 规模",
        "",
        "| Section | Active line 数 |",
        "|---|---:|",
    ]
    for section, count in (result["sections"] or {}).items():
        lines.append(f"| `{section}` | {count} |")
    lines.extend(
        [
            "",
            "## 规则源",
            "",
            "| 检查项 | 结果 |",
            "|---|---:|",
            f"| 本地规则 active entries | {result['local_rule_total']} |",
            f"| 跨文件交集 entries | {result['cross_file_overlap']} |",
            f"| 远程规则源总数 | {result['remote_total']} |",
            f"| 已启用远程规则源 | {result['remote_enabled']} |",
            "",
            "## 维护边界",
            "",
            "- 同一文件内部的重复 active rule 会阻断验证。",
            "- 最终 Fusion 模块中的重复 active line、重复 script name、重复 MITM hostname 会阻断验证。",
            "- 跨文件重复不直接删除，因为 Android 包、单 App 包和兼容包可能需要独立保留相同规则。",
            "- 远程 URL 可用性以 `scripts/validate_remote_rule_syntax.py` 和 `scripts/audit_repair_invalid_sources.py` 的结果为准。",
            "",
        ]
    )
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> None:
    validate_all(write_report=True)
    print(f"Module integrity validation passed; report={REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
