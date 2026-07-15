#!/usr/bin/env python3
"""Generate compact Release build summary reports."""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
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
VOLATILE_META_PREFIXES = ("#!desc=", "# update-date:")


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


def semantic_snapshot(text: str) -> dict[str, object]:
    current = "Meta"
    stable_metadata: list[str] = []
    sections: dict[str, list[str]] = {}
    for raw in text.splitlines():
        line = raw.strip()
        match = SECTION_RE.match(line)
        if match:
            current = match.group(1)
            sections.setdefault(current, [])
            continue
        if not line:
            continue
        if current == "Meta":
            if line.startswith("#!") and not line.startswith(VOLATILE_META_PREFIXES):
                stable_metadata.append(line)
            continue
        if line.startswith("#"):
            continue
        sections.setdefault(current, []).append(line)

    section_sha256 = {
        section: hashlib.sha256("\n".join(lines).encode("utf-8")).hexdigest()
        for section, lines in sections.items()
    }
    stable_metadata_sha256 = hashlib.sha256("\n".join(stable_metadata).encode("utf-8")).hexdigest()
    semantic_payload = {
        "stable_metadata": stable_metadata,
        "sections": sections,
    }
    semantic_sha256 = hashlib.sha256(
        json.dumps(semantic_payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    return {
        "sha256": semantic_sha256,
        "stable_metadata_sha256": stable_metadata_sha256,
        "section_sha256": section_sha256,
    }


def classify_module_change(current_text: str, previous_text: str | None) -> dict[str, object]:
    current = semantic_snapshot(current_text)
    if previous_text is None:
        return {
            "classification": "baseline-unavailable",
            "changed_sections": [],
            "stable_metadata_changed": False,
        }

    previous = semantic_snapshot(previous_text)
    current_raw = hashlib.sha256(current_text.encode("utf-8")).hexdigest()
    previous_raw = hashlib.sha256(previous_text.encode("utf-8")).hexdigest()
    if current_raw == previous_raw:
        classification = "unchanged"
    elif current["sha256"] == previous["sha256"]:
        classification = "metadata-only"
    else:
        classification = "module-semantic-changed"

    current_sections = dict(current["section_sha256"])
    previous_sections = dict(previous["section_sha256"])
    changed_sections = sorted(
        section
        for section in set(current_sections) | set(previous_sections)
        if current_sections.get(section) != previous_sections.get(section)
    )
    return {
        "classification": classification,
        "changed_sections": changed_sections,
        "stable_metadata_changed": current["stable_metadata_sha256"] != previous["stable_metadata_sha256"],
    }


def git_output(*args: str) -> str | None:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    return result.stdout.strip() if result.returncode == 0 else None


def head_module_baseline() -> tuple[dict[str, str], str | None]:
    commit = git_output("rev-parse", "HEAD")
    module_blob = git_output("rev-parse", "HEAD:Release/Ronghemokuai.sgmodule")
    module_text = git_output("show", "HEAD:Release/Ronghemokuai.sgmodule")
    return (
        {
            "ref": "HEAD",
            "commit": commit or "unavailable",
            "module_blob": module_blob or "unavailable",
        },
        (module_text + "\n") if module_text is not None else None,
    )


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
    semantic = semantic_snapshot(text)
    comparison_baseline, previous_text = head_module_baseline()
    change = classify_module_change(text, previous_text)
    return {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "module": rel(MODULE),
        "module_exists": MODULE.exists(),
        "module_size": MODULE.stat().st_size if MODULE.exists() else 0,
        "section_counts": sections,
        "semantic_sha256": semantic["sha256"],
        "stable_metadata_sha256": semantic["stable_metadata_sha256"],
        "section_sha256": semantic["section_sha256"],
        "change": change,
        "comparison_baseline": comparison_baseline,
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
        f"- Semantic SHA-256: `{payload['semantic_sha256']}`",
        f"- Change classification: `{dict(payload['change'])['classification']}`",
        f"- Comparison baseline: `{dict(payload['comparison_baseline'])['ref']}` "
        f"commit `{dict(payload['comparison_baseline'])['commit']}` / "
        f"module blob `{dict(payload['comparison_baseline'])['module_blob']}`",
        "",
        "## Section counts",
        "",
        "| Section | Active lines |",
        "|---|---:|",
    ]
    for section, count in dict(payload["section_counts"]).items():
        lines.append(f"| `{section}` | {count} |")
    change = dict(payload["change"])
    lines.extend(
        [
            "",
            "## Semantic change",
            "",
            f"- Classification: `{change['classification']}`",
            f"- Changed sections: `{', '.join(change['changed_sections']) or 'none'}`",
            f"- Stable metadata changed: `{change['stable_metadata_changed']}`",
            "- Volatile date text in `#!desc` is excluded from the semantic fingerprint.",
            "- Boundary: this fingerprint covers module configuration text, not runtime behavior or remote content changing behind an unchanged URL.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    payload = build_payload()
    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    OUT_MD.write_text(build_markdown(payload), encoding="utf-8", newline="\n")
    print(f"wrote {rel(OUT_JSON)} and {rel(OUT_MD)}")


if __name__ == "__main__":
    main()
