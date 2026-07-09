#!/usr/bin/env python3
"""Validate the generated MITM optimization report against Release output."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_module  # noqa: E402

REPORT_JSON = ROOT / "reports" / "mitm_optimization_report.json"
REPORT_MD = ROOT / "reports" / "mitm_optimization_report.md"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def current_release_hosts() -> list[str]:
    if not RELEASE.exists():
        fail("Release/Ronghemokuai.sgmodule is missing")
    sections = build_module.split_source_fragment(RELEASE.read_text(encoding="utf-8", errors="replace"))
    return [build_module.normalize_mitm_host_token(host) for host in build_module.parse_mitm_hosts(sections.get("MITM", ""))]


def mark_reports_validated() -> None:
    reference_time = max(
        (path.stat().st_mtime for path in (RELEASE, REPORT_JSON, REPORT_MD) if path.exists()),
        default=0.0,
    )
    validated_time = reference_time + 1.0
    for path in (REPORT_JSON, REPORT_MD):
        os.utime(path, (validated_time, validated_time))


def main() -> None:
    if not REPORT_JSON.exists() or not REPORT_MD.exists():
        fail("MITM optimization reports are missing")
    data = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    release_hosts = current_release_hosts()
    optimized_hosts = [build_module.normalize_mitm_host_token(str(host)) for host in data.get("optimized_hosts", [])]
    if not optimized_hosts:
        fail("MITM optimization report has no optimized_hosts")
    if release_hosts != optimized_hosts:
        fail("Release MITM hostnames differ from mitm_optimization_report.json")
    if data.get("mode") == "normalize" and set(data.get("baseline_unique_hosts", [])) != set(optimized_hosts):
        fail("normalize mode changed the baseline hostname token set")
    coverage = data.get("coverage_validation", {})
    if data.get("fallback"):
        reason = data.get("fallback_reason") or "unknown"
        print(f"MITM optimization used fail-closed fallback: {reason}")
    elif not coverage.get("passed"):
        fail("MITM coverage validation did not pass and no fallback was recorded")
    mark_reports_validated()
    print("MITM coverage validation passed.")


if __name__ == "__main__":
    main()
