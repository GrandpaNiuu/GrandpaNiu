#!/usr/bin/env python3
"""Generate rule-only release files from the built fusion module."""

from __future__ import annotations

import datetime as dt
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE_MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
RULES_OUT = ROOT / "Release" / "Rules.conf"
GROUPS_OUT = ROOT / "Release" / "RulesGroup.conf"
REPORT = ROOT / "reports" / "release_rules_report.md"

SECTION_ORDER = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]
POLICY_ORDER = ["DIRECT", "REJECT", "PROXY", "REJECT-TINYGIF", "REJECT-DROP", "OTHER"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def split_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {name: [] for name in SECTION_ORDER}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("[") and line.endswith("]"):
            name = line[1:-1]
            current = name if name in sections else None
            continue
        if current:
            sections[current].append(line)
    return sections


def active_rule_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line in seen:
            continue
        seen.add(line)
        out.append(line)
    return out


def rule_policy(line: str) -> str:
    parts = [part.strip() for part in line.split(",") if part.strip()]
    for part in reversed(parts):
        upper = part.upper()
        if upper in POLICY_ORDER:
            return upper
    return "OTHER"


def grouped_rules(rules: list[str]) -> OrderedDict[str, list[str]]:
    groups: OrderedDict[str, list[str]] = OrderedDict((policy, []) for policy in POLICY_ORDER)
    for line in rules:
        groups.setdefault(rule_policy(line), []).append(line)
    return groups


def build_rules_conf(rules: list[str]) -> str:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "#!name=GrandpaNiu Rules",
        "#!desc=Rule-only output generated from Release/Ronghemokuai.sgmodule",
        "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Release/Rules.conf",
        f"# generated-at: {today}",
        "",
        "[Rule]",
        *rules,
        "",
    ]
    return "\n".join(lines)


def build_groups_conf(rules: list[str]) -> str:
    today = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "#!name=GrandpaNiu Rule Groups",
        "#!desc=Grouped rule output generated from Release/Ronghemokuai.sgmodule",
        "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Release/RulesGroup.conf",
        f"# generated-at: {today}",
        "",
        "[Rule]",
    ]
    for policy, items in grouped_rules(rules).items():
        if not items:
            continue
        lines.append(f"# group: {policy}")
        lines.extend(items)
        lines.append("")
    return "\n".join(lines)


def make_report(rules: list[str]) -> str:
    groups = grouped_rules(rules)
    lines = [
        "# Release rule output report",
        "",
        f"- Source: `{RELEASE_MODULE.relative_to(ROOT).as_posix()}`",
        f"- Rules output: `{RULES_OUT.relative_to(ROOT).as_posix()}`",
        f"- Rule groups output: `{GROUPS_OUT.relative_to(ROOT).as_posix()}`",
        f"- Total active rules: {len(rules)}",
        "",
        "## Groups",
    ]
    for policy, items in groups.items():
        lines.append(f"- {policy}: {len(items)}")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    module_text = read(RELEASE_MODULE)
    if not module_text:
        raise SystemExit(f"missing release module: {RELEASE_MODULE}")
    sections = split_sections(module_text)
    rules = active_rule_lines(sections["Rule"])
    if not rules:
        raise SystemExit("release module has no active rules")
    write(RULES_OUT, build_rules_conf(rules))
    write(GROUPS_OUT, build_groups_conf(rules))
    write(REPORT, make_report(rules))
    print(f"Built {RULES_OUT} and {GROUPS_OUT} with {len(rules)} rules")


if __name__ == "__main__":
    main()
