#!/usr/bin/env python3
"""Create rule release files from the built fusion module."""

from __future__ import annotations

from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RELEASE_MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
RULES_OUT = ROOT / "Release" / "Rules.conf"
GROUPS_OUT = ROOT / "Release" / "RulesGroup.conf"
REPORT = ROOT / "reports" / "release_rules_report.md"
SECTIONS = ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]
POLICIES = ["DIRECT", "REJECT", "PROXY", "OTHER"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def split_sections(text: str) -> dict[str, list[str]]:
    data = {name: [] for name in SECTIONS}
    current = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if line.startswith("[") and line.endswith("]"):
            name = line[1:-1]
            current = name if name in data else None
            continue
        if current:
            data[current].append(line)
    return data


def active_rules(lines: list[str]) -> list[str]:
    result = []
    seen = set()
    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or line in seen:
            continue
        seen.add(line)
        result.append(line)
    return result


def policy_of(line: str) -> str:
    parts = [part.strip().upper() for part in line.split(",") if part.strip()]
    for part in reversed(parts):
        if part in POLICIES:
            return part
    return "OTHER"


def grouped(rules: list[str]) -> OrderedDict[str, list[str]]:
    result = OrderedDict((name, []) for name in POLICIES)
    for line in rules:
        result.setdefault(policy_of(line), []).append(line)
    return result


def rules_conf(rules: list[str]) -> str:
    return "\n".join([
        "#!name=GrandpaNiu Rules",
        "#!desc=Rule-only output generated from Release/Ronghemokuai.sgmodule",
        "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Release/Rules.conf",
        "",
        "[Rule]",
        *rules,
        "",
    ])


def groups_conf(rules: list[str]) -> str:
    lines = [
        "#!name=GrandpaNiu Rule Groups",
        "#!desc=Grouped rule output generated from Release/Ronghemokuai.sgmodule",
        "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Release/RulesGroup.conf",
        "",
        "[Rule]",
    ]
    for name, items in grouped(rules).items():
        if items:
            lines.append(f"# group: {name}")
            lines.extend(items)
            lines.append("")
    return "\n".join(lines)


def report(rules: list[str]) -> str:
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
    for name, items in grouped(rules).items():
        lines.append(f"- {name}: {len(items)}")
    return "\n".join(lines) + "\n"


def main() -> None:
    module = read(RELEASE_MODULE)
    if not module:
        raise SystemExit(f"missing release module: {RELEASE_MODULE}")
    rules = active_rules(split_sections(module)["Rule"])
    if not rules:
        raise SystemExit("release module has no active rules")
    write(RULES_OUT, rules_conf(rules))
    write(GROUPS_OUT, groups_conf(rules))
    write(REPORT, report(rules))
    print(f"Built {RULES_OUT} and {GROUPS_OUT} with {len(rules)} rules")


if __name__ == "__main__":
    main()
