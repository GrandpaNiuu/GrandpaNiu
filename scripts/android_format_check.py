#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    required_dirs = [
        ROOT / "Android" / "mihomo" / "apps",
        ROOT / "Android" / "sing-box" / "apps",
        ROOT / "Android" / "adguard" / "apps",
        ROOT / "Android" / "v2rayng" / "apps",
    ]
    for directory in required_dirs:
        if not directory.exists():
            raise SystemExit(f"missing directory: {directory.relative_to(ROOT)}")
    print("Android format check passed.")


if __name__ == "__main__":
    main()
