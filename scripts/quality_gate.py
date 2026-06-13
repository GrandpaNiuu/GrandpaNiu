#!/usr/bin/env python3
"""Run the complete reproducible quality gate for GrandpaNiu."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def node_executable() -> str:
    found = shutil.which("node")
    if found:
        return found
    bundled = Path.home() / ".cache" / "codex-runtimes" / "codex-primary-runtime" / "dependencies" / "node" / "bin"
    for candidate in (bundled / "node.exe", bundled / "node"):
        if candidate.exists():
            return str(candidate)
    raise SystemExit("ERROR: node executable not found")


def compile_targets() -> list[str]:
    scripts = [str(path.relative_to(ROOT)) for path in sorted((ROOT / "scripts").glob("*.py"))]
    tools = [str(path.relative_to(ROOT)) for path in sorted((ROOT / "tools").glob("*.py"))]
    return scripts + tools + ["Rewrite/Generator/Builder.py"]


def run(command: list[str]) -> None:
    print("$ " + " ".join(command), flush=True)
    subprocess.run(command, cwd=ROOT, check=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail if tracked files are dirty after the gate")
    args = parser.parse_args()

    node = node_executable()
    commands: list[list[str]] = [
        [sys.executable, "-m", "py_compile", *compile_targets()],
        [node, "--check", "Scripts/app-cleaner.js"],
        [sys.executable, "-m", "unittest", "discover", "-s", "tests"],
        [sys.executable, "scripts/build_android_rules.py"],
        [sys.executable, "scripts/build_windows_v2rayn.py"],
        [sys.executable, "scripts/build_release_android.py"],
        [sys.executable, "scripts/android_format_check.py"],
        [sys.executable, "scripts/convert_quanx_rules.py"],
        [sys.executable, "scripts/build_module.py", "--build", "--profile", "fusion"],
        [sys.executable, "scripts/factory_finalize.py", "--sync-root"],
        [sys.executable, "scripts/build_release_variants.py"],
        [sys.executable, "scripts/build_checksums.py"],
        [sys.executable, "scripts/validate_generator_config.py"],
        [sys.executable, "scripts/validate_manifest.py"],
        [sys.executable, "scripts/validate_remote_rule_syntax.py"],
        [sys.executable, "tools/generate_automated_quality_evidence.py"],
        [sys.executable, "scripts/validate_governance_extensions.py"],
        [sys.executable, "scripts/validate_profiles.py"],
        [sys.executable, "scripts/validate_module_integrity.py"],
        [sys.executable, "scripts/generate_app_coverage_matrix.py"],
        [sys.executable, "scripts/generate_app_status_matrix.py"],
        [sys.executable, "scripts/generate_script_inventory_report.py"],
        [sys.executable, "scripts/score_candidates.py"],
        [sys.executable, "scripts/audit_reject_risk.py"],
        [sys.executable, "scripts/audit_domestic_app_connectivity.py"],
        [sys.executable, "scripts/generate_change_impact_report.py"],
        [sys.executable, "scripts/generate_workflow_health_report.py"],
        [sys.executable, "scripts/check_report_freshness.py"],
        [sys.executable, "tools/generate_automated_quality_evidence.py"],
        [sys.executable, "scripts/repository_health_check.py"],
        [sys.executable, "tools/generate_automated_quality_evidence.py"],
        [sys.executable, "scripts/validate_repository.py"],
    ]
    for command in commands:
        run(command)

    if args.check:
        run(["git", "diff", "--exit-code"])
    print("Quality gate passed.")


if __name__ == "__main__":
    main()
