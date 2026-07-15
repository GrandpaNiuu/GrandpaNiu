from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_module  # noqa: E402


class ProtectedRuleCompilerTests(unittest.TestCase):
    def test_protected_exact_domain_blocks_conflicting_exact_reject(self) -> None:
        protected = build_module.parse_protected_route_patterns(
            "DOMAIN,free-aos-cdn-image.amap.com,DIRECT,pre-matching\n"
        )
        rules = (
            "DOMAIN,free-aos-cdn-image.amap.com,REJECT,pre-matching\n"
            "DOMAIN,ads.example.com,REJECT,pre-matching\n"
        )

        compiled = build_module.strip_protected_reject_conflicts(rules, protected)

        self.assertNotIn("free-aos-cdn-image.amap.com", compiled)
        self.assertIn("DOMAIN,ads.example.com,REJECT,pre-matching", compiled)

    def test_broad_protection_suffix_does_not_guess_about_exact_ad_endpoint(self) -> None:
        protected = build_module.parse_protected_route_patterns(
            "DOMAIN-SUFFIX,amap.com,DIRECT,pre-matching\n"
        )
        rule = "DOMAIN,ads.amap.com,REJECT,pre-matching\n"

        compiled = build_module.strip_protected_reject_conflicts(rule, protected)

        self.assertEqual(rule, compiled)

    def test_protected_exact_domain_blocks_broader_suffix_reject(self) -> None:
        protected = build_module.parse_protected_route_patterns(
            "DOMAIN,open.weixin.qq.com,DIRECT,pre-matching\n"
        )
        rules = "DOMAIN-SUFFIX,weixin.qq.com,REJECT,pre-matching\n"

        compiled = build_module.strip_protected_reject_conflicts(rules, protected)

        self.assertEqual("", compiled)

    def test_contextual_compound_reject_is_not_guessed_or_removed(self) -> None:
        protected = build_module.parse_protected_route_patterns(
            "DOMAIN-SUFFIX,pddpic.com,DIRECT,pre-matching\n"
        )
        contextual = (
            'AND,((DOMAIN-SUFFIX,pddpic.com,extended-matching),'
            '(USER-AGENT,"*bili*")),REJECT,pre-matching\n'
        )

        compiled = build_module.strip_protected_reject_conflicts(contextual, protected)

        self.assertEqual(contextual, compiled)

    def test_repository_protection_sources_cover_final_rule_conflicts(self) -> None:
        profile = build_module.load_profile("fusion")
        protected = build_module.build_protected_route_patterns(profile)
        compiled = build_module.build_rules(profile)

        conflicts = build_module.find_protected_reject_conflicts(compiled, protected)

        self.assertEqual([], conflicts)
        self.assertTrue(any(item.host == "free-aos-cdn-image.amap.com" for item in protected))


if __name__ == "__main__":
    unittest.main()
