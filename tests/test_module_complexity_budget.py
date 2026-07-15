from __future__ import annotations

import json
import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT / "tools"))

import build_release_summary
import validate_module_budget

BUILDER_SPEC = importlib.util.spec_from_file_location(
    "grandpaniu_builder", ROOT / "Rewrite" / "Generator" / "Builder.py"
)
assert BUILDER_SPEC and BUILDER_SPEC.loader
grandpaniu_builder = importlib.util.module_from_spec(BUILDER_SPEC)
BUILDER_SPEC.loader.exec_module(grandpaniu_builder)


def budget_config(*, max_line_chars: int = 200) -> dict[str, object]:
    return {
        "schema": 1,
        "module": {
            "max_bytes": 10_000,
            "max_lines": 100,
            "max_default_line_chars": max_line_chars,
        },
        "sections": {
            "Rule": {"max_active_lines": 10},
            "Script": {"max_active_lines": 10},
            "MITM": {"max_active_lines": 2},
        },
        "mitm": {"max_tokens": 10, "max_wildcards": 5},
        "large_line_exceptions": [],
    }


class ModuleComplexityBudgetTests(unittest.TestCase):
    def test_unified_builder_enforces_committed_budget(self) -> None:
        preferred = (ROOT / "Rewrite" / "Generator" / "Generate.conf").read_text(encoding="utf-8")
        legacy = (ROOT / "Rewrite" / "Generate.conf").read_text(encoding="utf-8")
        config_path = ROOT / "Rewrite" / "Generator" / "Generate.conf"
        config = grandpaniu_builder.load_config(config_path)
        plan = grandpaniu_builder.build_plan(config, "fusion", True, False, config_path)
        budget_commands = [command for command in plan if command[1].endswith("validate_module_budget.py")]

        self.assertIn("module_budget_script = tools/validate_module_budget.py", preferred)
        self.assertIn("module_budget_script = tools/validate_module_budget.py", legacy)
        self.assertEqual(1, len(budget_commands))
        self.assertIn("--config", budget_commands[0])
        self.assertIn("Rewrite/Generator/module-budgets.json", budget_commands[0])
        self.assertIn("--json-report", budget_commands[0])
        self.assertIn("reports/module_budget_report.json", budget_commands[0])
        self.assertIn("--markdown-report", budget_commands[0])
        self.assertIn("reports/module_budget_report.md", budget_commands[0])

    def test_quality_gate_refreshes_budget_after_final_module_validation(self) -> None:
        quality_gate = (ROOT / "scripts" / "quality_gate.py").read_text(encoding="utf-8")

        budget = quality_gate.rfind('"tools/validate_module_budget.py"')
        profiles = quality_gate.rfind('"scripts/validate_profiles.py"')
        integrity = quality_gate.rfind('"scripts/validate_module_integrity.py"')
        freshness = quality_gate.rfind('"scripts/check_report_freshness.py", "--strict"')

        self.assertGreater(budget, profiles)
        self.assertGreater(budget, integrity)
        self.assertLess(budget, freshness)

    def test_small_module_passes_budget(self) -> None:
        module = """#!name=Fixture
#!desc=2026-07-16 / fusion
[Rule]
DOMAIN,ads.example,REJECT
[Script]
clean = type=http-response,pattern=^https://api\\.example/,script-path=https://example/clean.js
[MITM]
hostname = %APPEND% api.example,*.static.example
"""

        payload = validate_module_budget.analyze_module_text(module, budget_config())

        self.assertEqual("passed", payload["status"])
        self.assertEqual([], payload["errors"])
        self.assertEqual(2, payload["mitm"]["tokens"])
        self.assertEqual(1, payload["mitm"]["wildcards"])

    def test_unregistered_oversized_line_fails_closed(self) -> None:
        module = "[Map Local]\n^https://example data-type=text data=\"" + ("x" * 90) + "\"\n"

        payload = validate_module_budget.analyze_module_text(module, budget_config(max_line_chars=60))

        self.assertEqual("failed", payload["status"])
        self.assertTrue(any("unregistered oversized line" in error for error in payload["errors"]))

    def test_registered_large_line_is_bounded_and_reported(self) -> None:
        module = "[Map Local]\n^https://assets.example/known.js data-type=base64 data=\"" + ("x" * 90) + "\"\n"
        config = budget_config(max_line_chars=80)
        config["large_line_exceptions"] = [
            {
                "id": "known-map-local",
                "section": "Map Local",
                "contains": "assets.example/known.js",
                "max_chars": 160,
                "expected_matches": 1,
                "reason": "fixture",
            }
        ]

        payload = validate_module_budget.analyze_module_text(module, config)

        self.assertEqual("passed", payload["status"])
        self.assertEqual("known-map-local", payload["longest_lines"][0]["exception_id"])
        self.assertEqual(1, payload["exception_matches"]["known-map-local"])

    def test_registered_large_line_still_fails_above_its_own_cap(self) -> None:
        module = "[Map Local]\n^https://assets.example/known.js data-type=base64 data=\"" + ("x" * 130) + "\"\n"
        config = budget_config(max_line_chars=60)
        config["large_line_exceptions"] = [
            {
                "id": "known-map-local",
                "section": "Map Local",
                "contains": "assets.example/known.js",
                "max_chars": 100,
                "expected_matches": 1,
                "reason": "fixture",
            }
        ]

        payload = validate_module_budget.analyze_module_text(module, config)

        self.assertEqual("failed", payload["status"])
        self.assertTrue(any("known-map-local" in error for error in payload["errors"]))

    def test_large_line_exception_cannot_match_multiple_payloads(self) -> None:
        line = '^https://assets.example/known.js data-type=base64 data="' + ("x" * 90) + '"'
        module = f"[Map Local]\n{line}\n{line}#second\n"
        config = budget_config(max_line_chars=60)
        config["large_line_exceptions"] = [
            {
                "id": "known-map-local",
                "section": "Map Local",
                "contains": "assets.example/known.js",
                "max_chars": 180,
                "expected_matches": 1,
                "reason": "fixture",
            }
        ]

        payload = validate_module_budget.analyze_module_text(module, config)

        self.assertEqual("failed", payload["status"])
        self.assertTrue(any("expected 1 oversized line" in error for error in payload["errors"]))

    def test_short_marker_line_does_not_consume_large_line_exception(self) -> None:
        short = '^https://assets.example/known.js data-type=text data="ok"'
        large = '^https://assets.example/known.js data-type=base64 data="' + ("x" * 90) + '"'
        module = f"[Map Local]\n{short}\n{large}\n"
        config = budget_config(max_line_chars=60)
        config["large_line_exceptions"] = [
            {
                "id": "known-map-local",
                "section": "Map Local",
                "contains": "assets.example/known.js",
                "max_chars": 180,
                "expected_matches": 1,
                "reason": "fixture",
            }
        ]

        payload = validate_module_budget.analyze_module_text(module, config)

        self.assertEqual("passed", payload["status"])
        self.assertEqual(1, payload["exception_matches"]["known-map-local"])

    def test_missing_expected_large_line_exception_fails(self) -> None:
        config = budget_config(max_line_chars=60)
        config["large_line_exceptions"] = [
            {
                "id": "known-map-local",
                "section": "Map Local",
                "contains": "assets.example/known.js",
                "max_chars": 180,
                "expected_matches": 1,
                "reason": "fixture",
            }
        ]

        payload = validate_module_budget.analyze_module_text("[Map Local]\n", config)

        self.assertEqual("failed", payload["status"])
        self.assertTrue(any("expected 1 oversized line" in error for error in payload["errors"]))

    def test_each_primary_budget_dimension_blocks_when_exceeded(self) -> None:
        module = "[Rule]\nDOMAIN,ads.example,REJECT\n[MITM]\nhostname = %APPEND% *.api.example,exact.example\n"
        mutations = {
            "module bytes exceeded": lambda config: config["module"].update(max_bytes=1),
            "module lines exceeded": lambda config: config["module"].update(max_lines=1),
            "[Rule] active lines exceeded": lambda config: config["sections"]["Rule"].update(max_active_lines=0),
            "MITM tokens exceeded": lambda config: config["mitm"].update(max_tokens=1),
            "MITM wildcards exceeded": lambda config: config["mitm"].update(max_wildcards=0),
        }

        for expected, mutate in mutations.items():
            with self.subTest(expected=expected):
                config = budget_config()
                mutate(config)
                payload = validate_module_budget.analyze_module_text(module, config)
                self.assertTrue(any(expected in error for error in payload["errors"]), payload["errors"])

    def test_unknown_budget_schema_is_rejected(self) -> None:
        config = budget_config()
        config["schema"] = 2

        with self.assertRaisesRegex(ValueError, "unsupported module budget schema"):
            validate_module_budget.analyze_module_text("[Rule]\nDOMAIN,ads.example,REJECT\n", config)

    def test_repository_fusion_output_fits_committed_budget(self) -> None:
        config = json.loads((ROOT / "Rewrite" / "Generator" / "module-budgets.json").read_text(encoding="utf-8"))
        module = (ROOT / "Release" / "Ronghemokuai.sgmodule").read_text(encoding="utf-8")

        payload = validate_module_budget.analyze_module_text(module, config)

        self.assertEqual([], payload["errors"])


class BuildSummarySemanticTests(unittest.TestCase):
    def test_build_payload_records_head_baseline_identity(self) -> None:
        payload = build_release_summary.build_payload()

        self.assertEqual("HEAD", payload["comparison_baseline"]["ref"])
        self.assertRegex(payload["comparison_baseline"]["commit"], r"^[0-9a-f]{40}$")
        self.assertRegex(payload["comparison_baseline"]["module_blob"], r"^[0-9a-f]{40}$")

    def test_date_only_description_change_is_metadata_only(self) -> None:
        previous = "#!name=Fixture\n#!desc=2026-07-15 / fusion\n[Rule]\nDOMAIN,ads.example,REJECT\n"
        current = "#!name=Fixture\n#!desc=2026-07-16 / fusion\n[Rule]\nDOMAIN,ads.example,REJECT\n"

        change = build_release_summary.classify_module_change(current, previous)

        self.assertEqual("metadata-only", change["classification"])
        self.assertEqual([], change["changed_sections"])

    def test_rule_change_is_behavior_change_with_section_trace(self) -> None:
        previous = "#!name=Fixture\n[Rule]\nDOMAIN,one.example,REJECT\n"
        current = "#!name=Fixture\n[Rule]\nDOMAIN,two.example,REJECT\n"

        change = build_release_summary.classify_module_change(current, previous)

        self.assertEqual("module-semantic-changed", change["classification"])
        self.assertEqual(["Rule"], change["changed_sections"])

    def test_identical_module_is_unchanged(self) -> None:
        module = "#!name=Fixture\n[MITM]\nhostname = %APPEND% api.example\n"

        change = build_release_summary.classify_module_change(module, module)

        self.assertEqual("unchanged", change["classification"])
        self.assertEqual([], change["changed_sections"])


if __name__ == "__main__":
    unittest.main()
