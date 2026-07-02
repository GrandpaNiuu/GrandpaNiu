#!/usr/bin/env python3
"""Run the complete reproducible quality gate for GrandpaNiu."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def node_executable() -> str:
    configured = os.environ.get("NODE_BINARY")
    if configured and Path(configured).exists():
        return configured
    found = shutil.which("node")
    if found:
        return found
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
        [sys.executable, "scripts/refresh_module_date.py"],
        [sys.executable, "scripts/convert_quanx_rules.py"],
        [sys.executable, "Rewrite/Generator/Builder.py", "--profile", "fusion", "--release"],
        [sys.executable, "scripts/validate_app_sources.py"],
        [sys.executable, "scripts/android_format_check.py"],
        [sys.executable, "tools/validate_upstream_risk_gate.py"],
        [sys.executable, "scripts/validate_generator_config.py"],
        [sys.executable, "scripts/validate_manifest.py"],
        [sys.executable, "scripts/validate_remote_rule_syntax.py"],
        [sys.executable, "tools/generate_automated_quality_evidence.py"],
        [sys.executable, "scripts/validate_governance_extensions.py"],
        [sys.executable, "scripts/validate_profiles.py"],
        [node, "--check", "Scripts/generated/fusion-script-bundle.js"],
        [sys.executable, "tools/validate_script_aggregation.py"],
        [sys.executable, "tools/test_script_bundle_sandbox.py"],
        [sys.executable, "scripts/validate_module_integrity.py"],
        [sys.executable, "tools/generate_mitm_scope_report.py"],
        [sys.executable, "tools/generate_rule_overlap_report.py"],
        [sys.executable, "tools/generate_app_cleaner_active_report.py"],
        [sys.executable, "scripts/generate_app_coverage_matrix.py"],
        [sys.executable, "scripts/generate_app_status_matrix.py"],
        [sys.executable, "scripts/generate_script_inventory_report.py"],
        [sys.executable, "scripts/score_candidates.py"],
        [sys.executable, "scripts/audit_reject_risk.py"],
        [sys.executable, "scripts/audit_domestic_app_connectivity.py"],
        [sys.executable, "scripts/generate_change_impact_report.py"],
        [sys.executable, "scripts/generate_workflow_health_report.py"],
        [sys.executable, "scripts/check_automation_status.py"],
        [sys.executable, "tools/generate_automation_gap_report.py"],
        [sys.executable, "scripts/repository_health_check.py"],
        [sys.executable, "scripts/check_report_freshness.py", "--strict"],
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
