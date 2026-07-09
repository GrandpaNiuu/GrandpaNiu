#!/usr/bin/env python3
"""Build a static MITM optimization baseline report from the generated module."""

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
    text = module.read_text(encoding="utf-8", errors="replace")
    sections = build_module.split_source_fragment(text)
    mitm = sections.get("MITM", "")
    entries = build_module.parse_mitm_host_entries(mitm, module.relative_to(ROOT).as_posix())
    features = build_module.build_effective_deep_features(sections)
    hosts, evidence = build_module.compile_mitm_hosts(
        entries,
        features,
        build_module.ShadowrocketMITMMatcher(wildcard_semantics_verified=False, allow_reduction=False),
        build_module.force_keep_mitm_hosts(entries),
    )
    if not hosts:
        raise SystemExit("ERROR: MITM baseline produced no hostnames")
    build_module.write_mitm_optimization_reports(evidence)
    print(
        "MITM optimization baseline written: "
        f"{build_module.MITM_OPTIMIZATION_REPORT_MD.relative_to(ROOT)}, "
        f"{build_module.MITM_OPTIMIZATION_REPORT_JSON.relative_to(ROOT)}"
    )


if __name__ == "__main__":
    main()
