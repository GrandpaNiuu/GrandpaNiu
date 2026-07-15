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


def current_release_sections() -> dict[str, str]:
    if not RELEASE.exists():
        fail("Release/Ronghemokuai.sgmodule is missing")
    return build_module.split_source_fragment(RELEASE.read_text(encoding="utf-8", errors="replace"))


def release_hosts_from_sections(sections: dict[str, str]) -> list[str]:
    return [build_module.normalize_mitm_host_token(host) for host in build_module.parse_mitm_hosts(sections.get("MITM", ""))]


def source_baseline() -> tuple[list[str], set[str]]:
    profile = build_module.load_profile(build_module.DEFAULT_PROFILE)
    entries, _ = build_module.collect_mitm_entries(profile)
    unique = build_module.ordered_unique_host_entries(entries)
    return [entry.normalized for entry in unique], build_module.force_keep_mitm_hosts(entries)


def mark_reports_validated() -> None:
    reference_time = max(
        (path.stat().st_mtime for path in (RELEASE, REPORT_JSON, REPORT_MD) if path.exists()),
        default=0.0,
    )
    validated_time = reference_time + 1.0
    for path in (REPORT_JSON, REPORT_MD):
        os.utime(path, (validated_time, validated_time))


def deep_features_from_report(data: dict[str, object]) -> list[build_module.DeepFeature]:
    features: list[build_module.DeepFeature] = []
    for raw in data.get("deep_features", []):
        if not isinstance(raw, dict):
            fail("MITM optimization report has an invalid deep feature")
        features.append(
            build_module.DeepFeature(
                order=int(raw.get("order", 0)),
                section=str(raw.get("section", "")),
                expression=str(raw.get("expression", "")),
                action=str(raw.get("action", "")),
                name=str(raw.get("name", "")),
                source=str(raw.get("source", "")),
                host_constraints=tuple(str(host) for host in raw.get("host_constraints", [])),
                opaque=bool(raw.get("opaque", False)),
                requires_mitm=bool(raw.get("requires_mitm", True)),
                source_hosts=tuple(str(host) for host in raw.get("source_hosts", [])),
            )
        )
    return features


def validate_equivalent_mode(data: dict[str, object], optimized_hosts: list[str]) -> None:
    baseline_hosts = [
        build_module.normalize_mitm_host_token(str(host))
        for host in data.get("baseline_unique_hosts", [])
    ]
    baseline_set = set(baseline_hosts)
    optimized_set = set(optimized_hosts)
    if not optimized_set < baseline_set:
        fail("equivalent mode did not produce a strict baseline subset")

    contract = data.get("matcher_contract", {})
    if not isinstance(contract, dict):
        fail("equivalent mode matcher contract is missing")
    if contract.get("name") != build_module.ShadowrocketMITMMatcher.CONTRACT_NAME:
        fail("equivalent mode matcher contract name is unsupported")
    if not contract.get("wildcard_semantics_verified") or not contract.get("allow_equivalent_compaction"):
        fail("equivalent mode matcher contract is not enabled and verified")
    if contract.get("allow_range_reduction"):
        fail("equivalent mode must not enable wildcard range reduction")

    baseline_patterns = {host for host in baseline_set if "*" in host or "?" in host}
    optimized_patterns = {host for host in optimized_set if "*" in host or "?" in host}
    if optimized_patterns != baseline_patterns:
        fail("equivalent mode changed wildcard or pattern tokens")

    removals = data.get("semantic_equivalent_removals", [])
    if not isinstance(removals, list):
        fail("equivalent mode removal evidence is invalid")
    removal_by_token = {
        build_module.normalize_mitm_host_token(str(item.get("token", ""))): item
        for item in removals
        if isinstance(item, dict) and item.get("token")
    }
    removed_hosts = baseline_set - optimized_set
    if len(removal_by_token) != len(removals):
        fail("equivalent mode removal evidence contains duplicates or invalid entries")
    if set(removal_by_token) != removed_hosts:
        fail("equivalent mode removal evidence does not match removed hosts")
    if int(data.get("semantic_equivalent_removed_count", -1)) != len(removed_hosts):
        fail("equivalent mode removal count is inconsistent")

    force_keep = {
        build_module.normalize_mitm_host_token(str(host))
        for host in data.get("force_keep_hosts", [])
    }
    matcher = build_module.ShadowrocketMITMMatcher(
        wildcard_semantics_verified=True,
        allow_reduction=False,
        allow_equivalent_compaction=True,
    )
    negative_patterns = [host[1:] for host in baseline_hosts if host.startswith("-") and len(host) > 1]
    for host in sorted(removed_hosts):
        item = removal_by_token[host]
        wildcard = build_module.normalize_mitm_host_token(str(item.get("covering_wildcard", "")))
        if not build_module.MITM_EXACT_HOST_RE.fullmatch(host):
            fail(f"equivalent mode removed a non-exact hostname token: {host}")
        if not wildcard.startswith("*.") or not build_module.MITM_EXACT_HOST_RE.fullmatch(wildcard[2:]):
            fail(f"equivalent mode used a non-canonical wildcard: {wildcard}")
        if host in force_keep:
            fail(f"equivalent mode removed force-keep hostname: {host}")
        if any(matcher.covers(pattern, host) for pattern in negative_patterns):
            fail(f"equivalent mode removed a hostname with negative-token overlap: {host}")
        if wildcard not in optimized_set or not matcher.covers(wildcard, host):
            fail(f"equivalent mode has invalid wildcard evidence for: {host}")
        if not item.get("source") or not item.get("covering_wildcard_source"):
            fail(f"equivalent mode source trace is incomplete for: {host}")

    valid, reasons = build_module.validate_compiled_mitm_contract(
        optimized_hosts,
        baseline_hosts,
        deep_features_from_report(data),
        matcher,
        force_keep,
        "equivalent",
    )
    if not valid:
        fail("equivalent mode coverage contract failed: " + ";".join(reasons))
    if not data.get("same_mitm_coverage_under_matcher_contract"):
        fail("equivalent mode did not record matcher-contract coverage equivalence")

    expected_order = [host for host in baseline_hosts if host not in removed_hosts]
    if optimized_hosts != expected_order:
        fail("equivalent mode changed retained hostname order")


def validate_fallback_mode(data: dict[str, object], optimized_hosts: list[str]) -> None:
    baseline_hosts = [
        build_module.normalize_mitm_host_token(str(host))
        for host in data.get("baseline_unique_hosts", [])
    ]
    if data.get("mode") != "fallback" or not data.get("fallback"):
        fail("fallback state is inconsistent")
    if not data.get("fallback_reason"):
        fail("fallback reason is missing")
    if optimized_hosts != baseline_hosts:
        fail("fallback did not restore the complete ordered baseline")
    if int(data.get("semantic_equivalent_removed_count", -1)) != 0:
        fail("fallback retained a non-zero equivalent removal count")
    if int(data.get("proved_reduction_count", -1)) != 0:
        fail("fallback retained a non-zero range reduction count")
    baseline_wildcards = [host for host in baseline_hosts if host.startswith("*.")]
    optimized_wildcards = [host for host in optimized_hosts if host.startswith("*.")]
    if optimized_wildcards != baseline_wildcards:
        fail("fallback changed the wildcard set or order")


def main() -> None:
    if not REPORT_JSON.exists() or not REPORT_MD.exists():
        fail("MITM optimization reports are missing")
    data = json.loads(REPORT_JSON.read_text(encoding="utf-8"))
    release_sections = current_release_sections()
    release_hosts = release_hosts_from_sections(release_sections)
    optimized_hosts = [build_module.normalize_mitm_host_token(str(host)) for host in data.get("optimized_hosts", [])]
    if not optimized_hosts:
        fail("MITM optimization report has no optimized_hosts")
    if release_hosts != optimized_hosts:
        fail("Release MITM hostnames differ from mitm_optimization_report.json")
    expected_baseline, expected_force_keep = source_baseline()
    reported_baseline = [
        build_module.normalize_mitm_host_token(str(host))
        for host in data.get("baseline_unique_hosts", [])
    ]
    if reported_baseline != expected_baseline:
        fail("MITM report baseline differs from current Fusion source declarations")
    reported_force_keep = {
        build_module.normalize_mitm_host_token(str(host))
        for host in data.get("force_keep_hosts", [])
    }
    if reported_force_keep != expected_force_keep:
        fail("MITM report force-keep set differs from current Fusion sources")
    expected_features = [
        build_module.deep_feature_dict(feature)
        for feature in build_module.build_effective_deep_features(release_sections)
    ]
    if data.get("deep_features") != expected_features:
        fail("MITM report deep-feature fingerprints differ from generated Release")
    expected_non_mitm = build_module.non_mitm_fingerprint_summary(release_sections)
    if data.get("non_mitm_fingerprint") != expected_non_mitm:
        fail("non-MITM semantic fingerprint differs from generated Release")
    mode = data.get("mode")
    if mode == "normalize" and reported_baseline != optimized_hosts:
        fail("normalize mode changed the baseline hostname token set")
    if mode == "equivalent":
        validate_equivalent_mode(data, optimized_hosts)
    if mode == "fallback":
        validate_fallback_mode(data, optimized_hosts)
    if mode == "reduce":
        fail("wildcard range reduction is not enabled by the independent validator")
    if mode not in {"normalize", "equivalent", "fallback"}:
        fail(f"unsupported MITM optimization mode: {mode}")
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
