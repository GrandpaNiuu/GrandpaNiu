#!/usr/bin/env python3
"""Validate the single Fusion profile without leaving generated output changed."""

from __future__ import annotations

import datetime as dt
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "profile_validation_report.md"
FACTORY_REPORT = ROOT / "reports" / "module_factory_report.md"
FACTORY_DIFF = ROOT / "reports" / "module_factory_diff_report.md"
PROFILES = {
    "fusion": ("single Fusion release", "yes"),
}
REQUIRED_MARKERS = (
    "[Rule]",
    "[URL Rewrite]",
    "[Header Rewrite]",
    "[Body Rewrite]",
    "[Map Local]",
    "[Script]",
    "[MITM]",
    "spotify-upstream",
    "Spotify_remove_ads.js",
    "youtube.response",
    "zhihu-enhance",
    "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule",
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def count_scripts(text: str) -> int:
    start = text.find("[Script]")
    end = text.find("[MITM]")
    if start < 0 or end < 0 or end <= start:
        return 0
    return len(
        [
            line
            for line in text[start:end].splitlines()
            if line.strip() and not line.lstrip().startswith("#") and not line.startswith("[")
        ]
    )


def count_mitm(text: str) -> int:
    start = text.find("[MITM]")
    if start < 0:
        return 0
    total = 0
    for line in text[start:].splitlines():
        if line.strip().startswith("hostname ="):
            total += len(
                [
                    host.strip()
                    for host in line.split("=", 1)[1].split(",")
                    if host.strip() and host.strip() != "%APPEND%"
                ]
            )
    return total


def validate_profile(profile: str) -> dict[str, Any]:
    proc = subprocess.run(
        [sys.executable, "scripts/build_module.py", "--build", "--profile", profile],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    text = read(RELEASE)
    missing = [marker for marker in REQUIRED_MARKERS if marker not in text]
    passed = proc.returncode == 0 and not missing
    return {
        "profile": profile,
        "passed": passed,
        "ok": "yes" if passed else "no",
        "markers": "passed" if not missing else "missing: " + ", ".join(missing),
        "scripts": str(count_scripts(text)),
        "mitm": str(count_mitm(text)),
        "stdout": (proc.stdout + proc.stderr).strip() or "no output",
    }


def main() -> None:
    release_backup = read(RELEASE)
    report_backup = read(FACTORY_REPORT)
    diff_backup = read(FACTORY_DIFF)
    rows: list[dict[str, Any]] = []
    try:
        for profile in PROFILES:
            rows.append(validate_profile(profile))
    finally:
        if release_backup:
            write(RELEASE, release_backup)
        if report_backup:
            write(FACTORY_REPORT, report_backup)
        if diff_backup:
            write(FACTORY_DIFF, diff_backup)

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# Profile Validation Report",
        "",
        f"Generated: {now}",
        "",
        "This script validates the single public Fusion profile only.",
        "",
        "| Profile | Build | Required markers | Scripts | MITM | Usage | Publishable |",
        "|---|---|---|---:|---:|---|---|",
    ]
    for row in rows:
        usage, publishable = PROFILES[row["profile"]]
        lines.append(
            f"| {row['profile']} | {row['ok']} | {row['markers']} | {row['scripts']} | {row['mitm']} | {usage} | {publishable} |"
        )
    lines += [
        "",
        "## Rules",
        "",
        "- fusion is the only public build profile.",
        "- Default workflows must build with fusion.",
        "- Legacy stable/stable-plus/lite/full files are not public entry points.",
        "- Required markers confirm module structure and core script entries.",
        "",
    ]
    write(REPORT, "\n".join(lines))
    failed = [row["profile"] for row in rows if not row["passed"]]
    if failed:
        raise SystemExit("Profile validation failed: " + ", ".join(failed))
    print(f"Profile validation report written to {REPORT}")


if __name__ == "__main__":
    main()
