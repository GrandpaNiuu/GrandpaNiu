#!/usr/bin/env python3
"""Generate SHA256 checksums for public Release artifacts."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_JSON = ROOT / "Release" / "checksums.json"
OUTPUT_TXT = ROOT / "Release" / "checksums.txt"
INCLUDE_PATTERNS = [
    "Release/*.sgmodule",
    "Release/*.conf",
    "Release/Modules/*.sgmodule",
    "Release/Stable/*",
    "Release/Beta/*",
    "Release/Canary/*",
    "Web/*.html",
    "Web/*.md",
    "Web/*.json",
]
EXCLUDE_NAMES = {"checksums.json", "checksums.txt"}


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def collect_files() -> list[Path]:
    files: dict[str, Path] = {}
    for pattern in INCLUDE_PATTERNS:
        for path in ROOT.glob(pattern):
            if not path.is_file():
                continue
            if path.name in EXCLUDE_NAMES:
                continue
            files[rel(path)] = path
    return [files[key] for key in sorted(files)]


def main() -> None:
    files = collect_files()
    entries = [
        {"path": rel(path), "size": path.stat().st_size, "sha256": sha256(path)}
        for path in files
    ]
    payload = {
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "algorithm": "sha256",
        "count": len(entries),
        "files": entries,
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    OUTPUT_TXT.write_text("".join(f"{item['sha256']}  {item['path']}\n" for item in entries), encoding="utf-8", newline="\n")
    print(f"wrote {rel(OUTPUT_JSON)} and {rel(OUTPUT_TXT)} for {len(entries)} files")


if __name__ == "__main__":
    main()
