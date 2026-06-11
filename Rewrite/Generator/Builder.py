#!/usr/bin/env python3
"""Unified entry point for the GrandpaNiu module factory.

This wrapper keeps the implementation in scripts/ while exposing the
Rewrite/Generator/Builder.py entry point used by the module factory layout.
"""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PYTHON = sys.executable


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def command(script: str, *args: str) -> list[str]:
    return [PYTHON, str(ROOT / script), *args]


def existing_command(script: str, *args: str) -> list[str] | None:
    path = ROOT / script
    if not path.exists():
        return None
    return command(script, *args)


def print_command(cmd: list[str]) -> None:
    printable = [cmd[0], rel(Path(cmd[1])), *cmd[2:]]
    print("$ " + " ".join(printable))


def run(cmd: list[str], dry_run: bool) -> None:
    print_command(cmd)
    if dry_run:
        return
    subprocess.run(cmd, cwd=ROOT, check=True)


def build_plan(profile: str, release: bool, check: bool) -> list[list[str]]:
    steps: list[list[str]] = [
        command("scripts/build_module.py", "--build", "--profile", profile),
    ]

    if release:
        steps.extend([
            command("scripts/factory_finalize.py", "--sync-root"),
            command("scripts/build_release_variants.py"),
            command("scripts/build_release_rules.py"),
            command("scripts/build_release_modules.py"),
        ])

    if check:
        optional_steps = [
            existing_command("scripts/validate_remote_rule_syntax.py"),
            existing_command("scripts/validate_repository.py"),
            existing_command("scripts/validate_profiles.py"),
            existing_command("scripts/validate_governance_extensions.py"),
        ]
        steps.extend(step for step in optional_steps if step is not None)

    return steps


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the GrandpaNiu module factory pipeline.")
    parser.add_argument("--profile", default="fusion", help="Profile name under Rewrite/Profiles. Default: fusion")
    parser.add_argument("--release", action="store_true", help="Finalize Release output and generate release artifacts")
    parser.add_argument("--check", action="store_true", help="Run available validation scripts after build")
    parser.add_argument("--dry-run", action="store_true", help="Print commands without executing them")
    args = parser.parse_args()

    for step in build_plan(args.profile, args.release, args.check):
        run(step, args.dry_run)


if __name__ == "__main__":
    main()
