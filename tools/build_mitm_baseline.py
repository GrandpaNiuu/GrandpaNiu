#!/usr/bin/env python3
"""Build a static MITM optimization baseline report from Fusion sources."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_module  # noqa: E402


def main() -> None:
    module = ROOT / "Release" / "Ronghemokuai.sgmodule"
    if not module.exists():
        module = ROOT / "Ronghemokuai.sgmodule"
    if not module.exists():
        raise SystemExit("ERROR: generated Fusion module is missing")
    sections = build_module.split_source_fragment(module.read_text(encoding="utf-8", errors="replace"))
    profile = build_module.load_profile(build_module.DEFAULT_PROFILE)
    entries, _ = build_module.collect_mitm_entries(profile)
    if not entries:
        raise SystemExit("ERROR: Fusion sources produced no MITM hostnames")
    matcher = build_module.ShadowrocketMITMMatcher(
        wildcard_semantics_verified=True,
        allow_reduction=False,
        allow_equivalent_compaction=True,
    )
    hosts, evidence = build_module.compile_mitm_hosts(
        entries,
        build_module.build_effective_deep_features(sections),
        matcher,
        build_module.force_keep_mitm_hosts(entries),
    )
    if not hosts:
        raise SystemExit("ERROR: MITM optimizer produced no hostnames")
    evidence["non_mitm_fingerprint"] = build_module.non_mitm_fingerprint_summary(sections)
    build_module.write_mitm_optimization_reports(evidence)
    print(
        "MITM source baseline and optimization evidence written: "
        f"{build_module.MITM_OPTIMIZATION_REPORT_MD.relative_to(ROOT)}, "
        f"{build_module.MITM_OPTIMIZATION_REPORT_JSON.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
