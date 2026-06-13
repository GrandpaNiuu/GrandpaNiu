#!/usr/bin/env python3
"""Validate generated Android rule outputs."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ANDROID = ROOT / "Android"
RELEASE_ANDROID = ROOT / "Release" / "Android"
REQUIRED_SOURCE_FILES = [
    ANDROID / "mihomo" / "GrandpaNiu-Ads.yaml",
    ANDROID / "mihomo" / "GrandpaNiu-Android-Full.yaml",
    ANDROID / "mihomo" / "apps" / "iOS-Compatible-Reject.yaml",
    ANDROID / "mihomo" / "apps" / "iOS-App-Compatible-Reject.yaml",
    ANDROID / "sing-box" / "GrandpaNiu-Ads.json",
    ANDROID / "adguard" / "GrandpaNiu-DNS.txt",
    ANDROID / "v2rayng" / "GrandpaNiu-v2rayng-routing.json",
]
REQUIRED_RELEASE_DIRS = [
    RELEASE_ANDROID / "mihomo",
    RELEASE_ANDROID / "sing-box",
    RELEASE_ANDROID / "adguard",
    RELEASE_ANDROID / "v2rayng",
]


def fail(message: str) -> None:
    raise SystemExit(message)


def active_mihomo_rules(path: Path) -> list[str]:
    rules: list[str] = []
    for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw.strip()
        if not line or line == "payload:" or line.startswith("#"):
            continue
        if line.startswith("-"):
            line = line[1:].strip()
        if line:
            rules.append(line)
    return rules


def check_duplicates(name: str, values: list[str]) -> None:
    seen: set[str] = set()
    duplicates: list[str] = []
    for value in values:
        key = value.lower()
        if key in seen and value not in duplicates:
            duplicates.append(value)
        seen.add(key)
    if duplicates:
        fail(f"{name} has duplicate rules: {', '.join(duplicates[:10])}")


def validate_mihomo(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    if "payload:" not in text:
        fail(f"missing payload: {path.relative_to(ROOT)}")
    rules = active_mihomo_rules(path)
    if not rules:
        fail(f"empty mihomo rules: {path.relative_to(ROOT)}")
    check_duplicates(path.relative_to(ROOT).as_posix(), rules)
    for rule in rules:
        if "," not in rule:
            fail(f"invalid mihomo rule `{rule}` in {path.relative_to(ROOT)}")
    return len(rules)


def validate_json(path: Path) -> int:
    data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    if not isinstance(data, dict):
        fail(f"json root must be object: {path.relative_to(ROOT)}")
    text = json.dumps(data, ensure_ascii=False)
    if "rules" not in data and "routing" not in data:
        fail(f"json rules missing: {path.relative_to(ROOT)}")
    if len(text) < 20:
        fail(f"json too small: {path.relative_to(ROOT)}")
    return len(text)


def validate_text(path: Path) -> int:
    lines = [line.strip() for line in path.read_text(encoding="utf-8", errors="replace").splitlines() if line.strip() and not line.startswith("!")]
    if not lines:
        fail(f"empty text rules: {path.relative_to(ROOT)}")
    check_duplicates(path.relative_to(ROOT).as_posix(), lines)
    return len(lines)


def main() -> None:
    for directory in [
        ANDROID / "mihomo" / "apps",
        ANDROID / "sing-box" / "apps",
        ANDROID / "adguard" / "apps",
        ANDROID / "v2rayng" / "apps",
    ]:
        if not directory.exists():
            fail(f"missing directory: {directory.relative_to(ROOT)}")
    for path in REQUIRED_SOURCE_FILES:
        if not path.exists():
            fail(f"missing required Android output: {path.relative_to(ROOT)}")
    for directory in REQUIRED_RELEASE_DIRS:
        if not directory.exists():
            fail(f"missing release Android directory: {directory.relative_to(ROOT)}")

    main_count = validate_mihomo(ANDROID / "mihomo" / "GrandpaNiu-Ads.yaml")
    validate_mihomo(ANDROID / "mihomo" / "apps" / "iOS-App-Compatible-Reject.yaml")
    for path in (ANDROID / "sing-box").rglob("*.json"):
        validate_json(path)
    for path in (ANDROID / "v2rayng").rglob("*.json"):
        validate_json(path)
    for path in (ANDROID / "adguard").rglob("*.txt"):
        validate_text(path)
    if main_count < 300:
        fail(f"Android main rules unexpectedly low: {main_count}")
    print(f"Android format check passed: main_rules={main_count}")


if __name__ == "__main__":
    main()
