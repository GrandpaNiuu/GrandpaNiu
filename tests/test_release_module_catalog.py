from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load_module(name: str, relative: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


release_modules = load_module("build_release_modules_test", "scripts/build_release_modules.py")
web_catalog = load_module("build_web_catalog_test", "scripts/build_web_catalog.py")
web_modules = load_module("build_web_modules_test", "scripts/build_web_modules.py")
release_channels = load_module("build_channels_test", "scripts/build_channels.py")


class ReleaseModuleCatalogTests(unittest.TestCase):
    def test_capability_tiers_are_derived_from_effective_sections(self) -> None:
        self.assertEqual("empty", release_modules.capability_tier({}))
        self.assertEqual("deep", release_modules.capability_tier({"Script": 1, "MITM": 1}))
        self.assertEqual("deep", release_modules.capability_tier({"Body Rewrite": 1}))
        self.assertEqual("rewrite", release_modules.capability_tier({"URL Rewrite": 2, "MITM": 1}))
        self.assertEqual("rule", release_modules.capability_tier({"Rule": 4}))

    def test_release_index_exposes_capability_without_claiming_runtime_success(self) -> None:
        spec = release_modules.ModuleSpec("demo", "GrandpaNiu Demo", ("demo",))
        item = release_modules.ModuleBuild(spec, {"Rule": 1, "Script": 1}, "Rewrite/Sources/Apps/demo.conf")
        index = release_modules.make_index([item])

        self.assertIn("| Module | File | Source | Capability | Sections |", index)
        self.assertIn("| deep |", index)
        self.assertIn("does not certify runtime effectiveness", index)

    def test_web_catalog_parses_capability_column(self) -> None:
        row = (
            "| GrandpaNiu Demo | `demo.sgmodule` | "
            "`Rewrite/Sources/Apps/demo.conf` | deep | Rule:1, Script:1 |"
        )
        parsed = web_catalog.parse_module_row(row)

        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertEqual("deep", parsed["capability"])
        self.assertEqual("Rule:1, Script:1", parsed["sections"])

    def test_web_catalog_keeps_backward_compatibility_with_old_rows(self) -> None:
        row = (
            "| GrandpaNiu Demo | `demo.sgmodule` | "
            "`Rewrite/Sources/Apps/demo.conf` | Rule:1 |"
        )
        parsed = web_catalog.parse_module_row(row)

        self.assertIsNotNone(parsed)
        assert parsed is not None
        self.assertEqual("unclassified", parsed["capability"])
        self.assertEqual("Rule:1", parsed["sections"])

    def test_stable_channel_is_labeled_legacy_compatibility(self) -> None:
        stable = release_channels.default_channels()[0]
        self.assertIn("Deprecated compatibility mirror", stable.description)
        self.assertNotIn("Production channel", stable.description)

    def test_web_outputs_explain_capability_evidence_boundary(self) -> None:
        modules = [
            {
                "name": "GrandpaNiu Demo",
                "file": "Release/Modules/demo.sgmodule",
                "source": "Rewrite/Sources/Apps/demo.conf",
                "capability": "deep",
                "sections": "Script:1",
                "raw_url": "https://example.invalid/demo.sgmodule",
            }
        ]
        remotes = {"rule_sets": [], "reference_modules": []}

        self.assertIn("does not certify runtime effectiveness", web_catalog.build_md(modules))
        self.assertIn("capability_contract", web_catalog.build_json(modules, remotes))
        self.assertIn("不代表运行时去广告效果或实机兼容性", web_modules.build_html(modules))


if __name__ == "__main__":
    unittest.main()
