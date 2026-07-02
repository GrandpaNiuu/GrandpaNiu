#!/usr/bin/env python3
"""Validate every app-scoped source fragment before release generation."""

from __future__ import annotations

from collections import Counter
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
APPS_DIR = ROOT / "Rewrite" / "Sources" / "Apps"
REPORT = ROOT / "reports" / "app_source_validation_report.md"
RELEASE_MODULES_DIR = ROOT / "Release" / "Modules"

OUTPUT_SECTIONS = (
    "Rule",
    "URL Rewrite",
    "Header Rewrite",
    "Body Rewrite",
    "Map Local",
    "Script",
    "MITM",
)
ALLOWED_SECTIONS = {"General", *OUTPUT_SECTIONS}
SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
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


def active(lines: list[str]) -> list[tuple[int, str]]:
    return [(number, line.strip()) for number, line in lines if line.strip() and not line.lstrip().startswith("#")]


def duplicates(values: list[str]) -> list[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def split_sections(text: str) -> tuple[dict[str, list[tuple[int, str]]], list[tuple[int, str]]]:
    sections: dict[str, list[tuple[int, str]]] = {"META": []}
    headers: list[tuple[int, str]] = []
    current = "META"
    for number, line in enumerate(text.splitlines(), 1):
        match = SECTION_RE.match(line)
        if match:
            current = match.group(1).strip()
            headers.append((number, current))
            sections.setdefault(current, [])
        else:
            sections.setdefault(current, []).append((number, line.rstrip()))
    return sections, headers


def line_error(path: Path, number: int, message: str) -> str:
    return f"{path.relative_to(ROOT).as_posix()}:{number}: {message}"


def validate_rule(path: Path, number: int, line: str, errors: list[str]) -> None:
    prefix = line.split(",", 1)[0]
    if prefix not in RULE_PREFIXES:
        errors.append(line_error(path, number, f"unsupported Rule prefix: {line}"))
        return
    if prefix in {"RULE-SET", "DOMAIN-SET"} and ",https://" not in line:
        errors.append(line_error(path, number, f"remote rule must use HTTPS: {line}"))
    if prefix in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "IP-CIDR", "IP-CIDR6"} and line.count(",") < 2:
        errors.append(line_error(path, number, f"rule is missing a policy: {line}"))


def validate_rewrite(path: Path, section: str, number: int, line: str, errors: list[str]) -> None:
    if section == "Header Rewrite":
        if not line.startswith(("http-request ", "http-response ")):
            errors.append(line_error(path, number, f"Header Rewrite is missing a request/response verb: {line}"))
        if " header-del " not in line and " header-replace " not in line:
            errors.append(line_error(path, number, f"unsupported Header Rewrite action: {line}"))
        return
    if section == "Body Rewrite":
        if not line.startswith(("http-request ", "http-response ", "http-response-jq ")):
            errors.append(line_error(path, number, f"unsupported Body Rewrite verb: {line}"))
        if len(line.split()) < 3:
            errors.append(line_error(path, number, f"incomplete Body Rewrite: {line}"))
        return
    if section == "Map Local":
        if " data-type=" not in line:
            errors.append(line_error(path, number, f"Map Local is missing data-type: {line}"))
        if " data=" not in line and "data-type=tiny-gif" not in line:
            errors.append(line_error(path, number, f"Map Local is missing embedded data: {line}"))
        if " data-path=" in line:
            errors.append(line_error(path, number, f"remote data-path must be embedded as data: {line}"))
        if line.count("status-code=") > 1:
            errors.append(line_error(path, number, f"Map Local has duplicate status-code: {line}"))
        data_start = line.find('data="{')
        if data_start >= 0 and len(line) > data_start + 7 and line[data_start + 7] == '"':
            errors.append(line_error(path, number, f"Map Local JSON quotes are not escaped: {line}"))
        array_start = line.find('data="[')
        if array_start >= 0 and len(line) > array_start + 7 and line[array_start + 7] == '"':
            errors.append(line_error(path, number, f"Map Local JSON quotes are not escaped: {line}"))
        return
    if not any(action in line for action in REWRITE_ACTIONS):
        errors.append(line_error(path, number, f"unsupported URL Rewrite action: {line}"))


def validate_script(path: Path, number: int, line: str, errors: list[str]) -> str:
    match = SCRIPT_NAME_RE.match(line)
    if not match:
        errors.append(line_error(path, number, f"script is missing a name: {line}"))
        return ""
    name = match.group(1).strip()
    body = line.split("=", 1)[1]
    if "type=http-request" not in body and "type=http-response" not in body:
        errors.append(line_error(path, number, f"script has an unsupported type: {line}"))
    if "script-path=" not in body:
        errors.append(line_error(path, number, f"script is missing script-path: {line}"))
    if "pattern=" not in body:
        errors.append(line_error(path, number, f"script is missing pattern: {line}"))
    return name


def validate_file(path: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8", errors="strict")
    except UnicodeDecodeError as exc:
        return [f"{path.relative_to(ROOT).as_posix()}: invalid UTF-8: {exc}"], 0
    if "\ufffd" in text:
        errors.append(f"{path.relative_to(ROOT).as_posix()}: contains Unicode replacement characters")
    sections, headers = split_sections(text)
    header_names = [name for _, name in headers]
    for name in duplicates(header_names):
        number = next(number for number, header in headers if header == name)
        errors.append(line_error(path, number, f"duplicate section [{name}]"))
    for number, name in headers:
        if name not in ALLOWED_SECTIONS:
            errors.append(line_error(path, number, f"unsupported section [{name}]"))
    if not any(line.startswith("#!name=") for _, line in sections.get("META", [])):
        errors.append(f"{path.relative_to(ROOT).as_posix()}: missing #!name metadata")

    active_count = 0
    script_names: list[str] = []
    mitm_hosts: list[str] = []
    for section in OUTPUT_SECTIONS:
        section_lines = active(sections.get(section, []))
        active_count += len(section_lines)
        for value in duplicates([line for _, line in section_lines]):
            number = next(number for number, line in section_lines if line == value)
            errors.append(line_error(path, number, f"duplicate active line in [{section}]: {value}"))
        for number, line in section_lines:
            if section == "Rule":
                validate_rule(path, number, line, errors)
            elif section in {"URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local"}:
                validate_rewrite(path, section, number, line, errors)
            elif section == "Script":
                script_names.append(validate_script(path, number, line, errors))
            elif section == "MITM":
                match = HOSTNAME_RE.match(line)
                if not match:
                    errors.append(line_error(path, number, f"invalid MITM hostname line: {line}"))
                    continue
                value = match.group(1).replace("%APPEND%", "")
                mitm_hosts.extend(host.strip() for host in value.split(",") if host.strip())
    for name in duplicates([name for name in script_names if name]):
        errors.append(f"{path.relative_to(ROOT).as_posix()}: duplicate script name: {name}")
    for host in duplicates(mitm_hosts):
        errors.append(f"{path.relative_to(ROOT).as_posix()}: duplicate MITM hostname: {host}")
    if active_count == 0:
        errors.append(f"{path.relative_to(ROOT).as_posix()}: no active output entries")
    return errors, active_count


def write_report(
    source_files: list[Path],
    release_files: list[Path],
    errors: list[str],
    source_entries: int,
    release_entries: int,
) -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8)))
    lines = [
        "# App 源语法验证报告",
        "",
        f"- 生成时间：{now.strftime('%Y-%m-%d %H:%M:%S %z')}",
        f"- App 源文件：{len(source_files)}",
        f"- Release App 模块：{len(release_files)}",
        f"- 源文件活跃输出项：{source_entries}",
        f"- Release 活跃输出项：{release_entries}",
        f"- 语法错误：{len(errors)}",
        f"- 结果：{'通过' if not errors else '失败'}",
        "",
        "## 错误明细",
        "",
    ]
    lines.extend(f"- `{error}`" for error in errors)
    if not errors:
        lines.append("- 无。")
    lines += [
        "",
        "## 验证边界",
        "",
        "- 本检查验证源文件结构、规则/重写/脚本/MITM 基础语法和重复项。",
        "- 本检查不能代替 Shadowrocket 真机网络、登录、支付和视频播放测试。",
        "",
    ]
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def main() -> int:
    source_files = sorted(path for path in APPS_DIR.glob("*.conf") if not path.stem.startswith("_"))
    release_files = sorted(RELEASE_MODULES_DIR.glob("*.sgmodule")) if RELEASE_MODULES_DIR.exists() else []
    errors: list[str] = []
    source_entries = 0
    release_entries = 0
    for path in source_files:
        file_errors, count = validate_file(path)
        errors.extend(file_errors)
        source_entries += count
    for path in release_files:
        file_errors, count = validate_file(path)
        errors.extend(file_errors)
        release_entries += count
    if release_files and len(release_files) != len(source_files):
        errors.append(
            f"Release/Modules count mismatch: sources={len(source_files)}, release={len(release_files)}"
        )
    write_report(source_files, release_files, errors, source_entries, release_entries)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print(f"App source validation failed: {len(errors)} error(s).", file=sys.stderr)
        return 1
    print(
        "App source validation passed: "
        f"{len(source_files)} source file(s), {len(release_files)} release module(s), "
        f"{source_entries} source entries."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
