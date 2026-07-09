import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_module  # noqa: E402


def feature(host: str, opaque: bool = False) -> build_module.DeepFeature:
    escaped_host = host.replace(".", r"\.")
    return build_module.DeepFeature(
        order=0,
        section="URL Rewrite",
        expression=rf"^https?:\/\/{escaped_host}\/ad",
        action="- reject",
        name="",
        source="test",
        host_constraints=(host,),
        opaque=opaque,
        source_hosts=(host,),
    )


class MITMOptimizerTests(unittest.TestCase):
    def test_duplicate_hosts_from_multiple_sources_keep_first_token(self) -> None:
        entries = [
            build_module.MITMHostEntry(0, "API.Example.COM", "api.example.com", "a.conf", "hostname = API.Example.COM"),
            build_module.MITMHostEntry(1, "api.example.com", "api.example.com", "b.conf", "hostname = api.example.com"),
        ]

        hosts, evidence = build_module.compile_mitm_hosts(entries, [], build_module.ShadowrocketMITMMatcher())

        self.assertEqual(["api.example.com"], hosts)
        self.assertEqual(1, evidence["deduplicated_exact_duplicate_count"])
        self.assertTrue(evidence["same_hostname_token_set"])

    def test_duplicate_hosts_across_hostname_lines_are_deduplicated(self) -> None:
        entries = build_module.parse_mitm_host_entries(
            "hostname = %APPEND% a.example.com,b.example.com\nhostname = %APPEND% a.example.com",
            "test.conf",
        )

        hosts, evidence = build_module.compile_mitm_hosts(entries, [], build_module.ShadowrocketMITMMatcher())

        self.assertEqual(["a.example.com", "b.example.com"], hosts)
        self.assertEqual(1, evidence["deduplicated_exact_duplicate_count"])

    def test_normalize_preserves_hostname_set(self) -> None:
        hosts, evidence = build_module.compile_mitm_hosts(
            ["A.Example.COM", "b.example.com"],
            [],
            build_module.ShadowrocketMITMMatcher(),
        )

        self.assertEqual({"a.example.com", "b.example.com"}, set(hosts))
        self.assertTrue(evidence["same_hostname_token_set"])
        self.assertEqual("normalize", evidence["mode"])

    def test_non_mitm_fingerprint_is_independent_of_mitm(self) -> None:
        before = {
            "Rule": "DOMAIN,ads.example.com,REJECT\n",
            "URL Rewrite": r"^https?:\/\/a\.example\.com\/ad - reject",
            "MITM": "hostname = a.example.com",
        }
        after = dict(before)
        after["MITM"] = "hostname = a.example.com,b.example.com"

        self.assertEqual(
            build_module.fingerprint_non_mitm_sections(before),
            build_module.fingerprint_non_mitm_sections(after),
        )

    def test_wildcard_without_matcher_proof_keeps_exact_subdomain(self) -> None:
        hosts, evidence = build_module.compile_mitm_hosts(
            ["*.example.com", "api.example.com"],
            [feature("api.example.com")],
            build_module.ShadowrocketMITMMatcher(wildcard_semantics_verified=False, allow_reduction=False),
        )

        self.assertEqual(["*.example.com", "api.example.com"], hosts)
        self.assertEqual(1, evidence["proof_reduce_disabled_due_to_missing_matcher_evidence"])

    def test_wildcard_with_opaque_feature_does_not_reduce(self) -> None:
        hosts, evidence = build_module.compile_mitm_hosts(
            ["*.example.com", "api.example.com"],
            [feature("api.example.com", opaque=True)],
            build_module.ShadowrocketMITMMatcher(wildcard_semantics_verified=True, allow_reduction=True),
        )

        self.assertEqual(["*.example.com", "api.example.com"], hosts)
        self.assertEqual("normalize", evidence["mode"])
        self.assertGreaterEqual(evidence["opaque_retained_count"], 1)

    def test_verified_finite_wildcard_dependency_can_reduce(self) -> None:
        hosts, evidence = build_module.compile_mitm_hosts(
            ["*.example.com", "api.example.com", "static.example.com"],
            [feature("api.example.com"), feature("static.example.com")],
            build_module.ShadowrocketMITMMatcher(wildcard_semantics_verified=True, allow_reduction=True),
        )

        self.assertEqual(["api.example.com", "static.example.com"], hosts)
        self.assertEqual("reduce", evidence["mode"])
        self.assertEqual(1, evidence["proved_reduction_count"])

    def test_lost_deep_feature_coverage_is_rejected(self) -> None:
        valid, reasons = build_module.validate_compiled_mitm_contract(
            ["api.example.com"],
            ["*.example.com", "api.example.com"],
            [feature("missing.example.com")],
            build_module.ShadowrocketMITMMatcher(wildcard_semantics_verified=True, allow_reduction=False),
            (),
            "reduce",
        )

        self.assertFalse(valid)
        self.assertTrue(any("deep_feature_mitm_coverage_missing" in reason for reason in reasons))

    def test_same_input_is_stable_across_builds(self) -> None:
        args = (
            ["*.example.com", "api.example.com", "api.example.com"],
            [feature("api.example.com")],
            build_module.ShadowrocketMITMMatcher(),
        )

        first, _ = build_module.compile_mitm_hosts(*args)
        second, _ = build_module.compile_mitm_hosts(*args)

        self.assertEqual(first, second)

    def test_matcher_semantics_are_documented_by_tests(self) -> None:
        matcher = build_module.ShadowrocketMITMMatcher(wildcard_semantics_verified=True)

        self.assertTrue(matcher.covers("api.example.com", "api.example.com"))
        self.assertTrue(matcher.covers("API.Example.COM", "api.example.com"))
        self.assertTrue(matcher.covers("*.example.com", "api.example.com"))
        self.assertFalse(matcher.covers("*.example.com", "example.com"))
        self.assertTrue(matcher.covers("*.example.com", "deep.api.example.com"))
        self.assertEqual(
            {"api.example.com", "*.example.com"},
            {build_module.normalize_mitm_host_token(host) for host in ["api.example.com", "API.Example.COM", "*.example.com"]},
        )


if __name__ == "__main__":
    unittest.main()
