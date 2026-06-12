#!/usr/bin/env python3
"""Generate compact Release build summary reports."""

from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
MODULES_INDEX = ROOT / "Release" / "Modules" / "README.md"
CHECKSUMS = ROOT / "Release" / "checksums.json"
OUT_JSON = ROOT / "reports" / "build_summary.json"
OUT_MD = ROOT / "reports" / "build_summary.md"
SECTION_RE = re.compile(r"^\[(.+)]$")
MODULE_ROW_RE = re.compile(r"^\| .+? \| `[^`]+\.sgmodule` \| `[^`]+` \| .+? \|$")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def count_sections(text: str) -> dict[str, int]:
    current = "Meta"
    counts: Counter[str] = Counter()
    for raw in text.splitlines():
        line = raw.strip()
        match = SECTION_RE.match(line)
        if match:
            current = match.group(1)
            continue
        if not line or line.startswith("#"):
            continue
        counts[current] += 1
    return dict(sorted(counts.items()))


def count_modules() -> int:
    return sum(1 for line in read(MODULES_INDEX).splitlines() if MODULE_ROW_RE.match(line.strip()))


def checksum_count() -> int:
    if not CHECKSUMS.exists():
        return 0
    try:
        data = json.loads(read(CHECKSUMS))
    except json.JSONDecodeError:
        return 0
    return int(data.get("count", 0))


def build_payload() -> dict[str, object]:
    text = read(MODULE)
    sections = count_sections(text)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "module": rel(MODULE),
        "module_exists": MODULE.exists(),
        "module_size": MODULE.stat().st_size if MODULE.exists() else 0,
        "section_counts": sections,
        "release_modules": count_modules(),
        "checksum_files": checksum_count(),
    }


def build_markdown(payload: dict[str, object]) -> str:
    lines = [
        "# Build Summary",
        "",
        f"- Generated at: `{payload['generated_at']}`",
        f"- Main module: `{payload['module']}`",
        f"- Main module size: `{payload['module_size']}` bytes",
        f"- Release modules: `{payload['release_modules']}`",
        f"- Checksum entries: `{payload['checksum_files']}`",
        "",
        "## Section counts",
        "",
        "| Section | Active lines |",
        "|---|---:|",
    ]
    for section, count in dict(payload["section_counts"]).items():
        lines.append(f"| `{section}` | {count} |")
    lines.append("")
    return "\n".join(lines)


def main() -> None:
    payload = build_payload()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8", newline="\n")
    print(f"wrote {rel(OUT_JSON)} and {rel(OUT_MD)}")


if __name__ == "__main__":
    main()
