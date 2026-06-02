#!/usr/bin/env python3
"""Run the GrandpaNiu quality gate in a fixed order."""

from __future__ import annotations

import subprocess
import sys

COMMANDS = [
    ["python3", "scripts/build_android_rules.py"],
    ["python3", "scripts/validate_android_rules.py"],
    ["python3", "scripts/build_module.py", "--build", "--profile", "stable"],
    ["python3", "scripts/factory_finalize.py", "--sync-root"],
    ["python3", "scripts/build_release_variants.py"],
    ["python3", "scripts/validate_repository.py"],
    ["python3", "scripts/validate_profiles.py"],
    ["python3", "scripts/audit_reject_risk.py"],
    ["python3", "scripts/generate_app_status_matrix.py"],
    ["python3", "scripts/check_report_freshness.py"],
]


def run(command: list[str]) -> None:
    print("$ " + " ".join(command), flush=True)
    completed = subprocess.run(command, text=True)
    if completed.returncode != 0:
        raise SystemExit(f"Quality gate failed: {' '.join(command)}")


def main() -> None:
    for command in COMMANDS:
        run(command)
    print("Quality gate passed.")


if __name__ == "__main__":
    main()
