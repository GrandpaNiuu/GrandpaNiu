#!/usr/bin/env python3
"""Generate a source-level rule overlap report without mutating sources."""

from __future__ import annotations

from collections import defaultdict
import datetime as dt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RULES_DIR = ROOT / "Rules"
REPORT = ROOT / "reports" / "rule_overlap_report.md"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def active_rules(path: Path) -> list[str]:
    lines: list[str] = []
    for raw in read(path).splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        lines.append(line)
    return lines


def main() -> None:
    by_rule: dict[str, set[str]] = defaultdict(set)
    per_file: dict[str, int] = {}
    for path in sorted(RULES_DIR.rglob("*.list")):
        rel = path.relative_to(ROOT).as_posix()
        rules = active_rules(path)
        per_file[rel] = len(rules)
        for rule in rules:
            by_rule[rule].add(rel)
    overlaps = {rule: files for rule, files in by_rule.items() if len(files) > 1}
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# Rule Overlap Report",
        "",
        f"- Generated at: {now}",
        f"- Rule files: {len(per_file)}",
        f"- Active source rules: {sum(per_file.values())}",
        f"- Unique source rules: {len(by_rule)}",
        f"- Cross-file overlaps: {len(overlaps)}",
        "",
        "## Largest Rule Files",
        "",
    ]
    for path, count in sorted(per_file.items(), key=lambda item: item[1], reverse=True)[:30]:
        lines.append(f"- `{path}`: {count}")
    lines.extend([
        "",
        "## Cross-file Overlap Samples",
        "",
    ])
    for rule, files in sorted(overlaps.items(), key=lambda item: (-len(item[1]), item[0]))[:120]:
        lines.append(f"- `{rule}` -> {', '.join(f'`{item}`' for item in sorted(files))}")
    if len(overlaps) > 120:
        lines.append(f"- ... {len(overlaps) - 120} more")
    lines.extend([
        "",
        "## Maintenance Notes",
        "",
        "- Cross-file overlap is not automatically wrong because Android, app modules and compatibility outputs can share rules.",
        "- Same-file duplicate active rules remain a validation error in `scripts/validate_module_integrity.py`.",
        "- Use this report when deciding whether a rule belongs in `Rules/`, `Rewrite/Sources/Misc/`, or an app source file.",
        "",
    ])
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Rule overlap report written to {REPORT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
