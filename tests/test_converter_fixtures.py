from __future__ import annotations

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "sync_upstream_app_modules",
    ROOT / "scripts" / "sync_upstream_app_modules.py",
)
assert SPEC and SPEC.loader
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class ConverterFixtureTests(unittest.TestCase):
    def record(self) -> dict[str, object]:
        return {
            "id": "fixture",
            "name": "Fixture",
            "source_url": "https://raw.githubusercontent.com/example/rules/main/fixture.sgmodule",
            "target": "Rewrite/Sources/Apps/fixture.conf",
            "enabled": True,
            "direct_commit": True,
            "risk": "low",
            "backup": False,
            "upstream_project": "example/rules",
            "last_sync_mode": "test",
        }

    def test_preserves_arguments_and_drops_display_metadata(self) -> None:
        upstream = "\n".join(
            [
                "#!name=Upstream Fixture",
                "#!arguments=mode:auto,level:1",
                "#!arguments-desc=mode controls cleanup",
                "#!icon=https://example.com/icon.png",
                "#!category=Ads",
                "[Rule]",
                "DOMAIN,ads.example.com,REJECT",
            ]
        )
        converted, upstream_name = sync.converted_source(self.record(), upstream)
        self.assertEqual("Upstream Fixture", upstream_name)
        self.assertIn("#!arguments=mode:auto,level:1", converted)
        self.assertIn("#!arguments-desc=mode controls cleanup", converted)
        self.assertNotIn("#!icon=", converted)
        self.assertNotIn("#!category=", converted)

    def test_loon_script_fixture_keeps_argument_binary_body_and_timeout(self) -> None:
        line = (
            "http-response ^https://api.example.com/v1 "
            "requires-body=1,binary-body-mode=1,max-size=-1,tag=fixture response,"
            "script-path=https://example.com/fixture.js,timeout=12"
        )
        converted = sync.convert_loon_script_line(line, "fixture", 1)
        self.assertIn("fixture-response = type=http-response", converted)
        self.assertIn("requires-body=1", converted)
        self.assertIn("binary-body-mode=1", converted)
        self.assertIn("max-size=-1", converted)
        self.assertIn("timeout=12", converted)
        self.assertIn("script-path=https://example.com/fixture.js", converted)

    def test_qx_loose_fixture_routes_rules_scripts_and_mitm(self) -> None:
        sections = sync.convert_loose_qx_lines(
            [
                "host-suffix,ads.fixtureads.net,reject",
                "^https://api.fixtureads.net/ad script-response-body https://cdn.fixtureads.net/ad.js",
                "hostname = api.fixtureads.net,cdn.fixtureads.net",
            ],
            "fixture",
        )
        self.assertEqual(["DOMAIN-SUFFIX,ads.fixtureads.net,REJECT"], sections["Rule"])
        self.assertEqual(1, len(sections["Script"]))
        self.assertIn("fixture.response.2 = type=http-response", sections["Script"][0])
        self.assertIn("requires-body=1", sections["Script"][0])
        self.assertEqual(["hostname = %APPEND% api.fixtureads.net,cdn.fixtureads.net"], sections["MITM"])

    def test_jq_map_local_and_header_rewrite_fixtures(self) -> None:
        body_section, body_line = sync.convert_loon_rewrite_line(
            "^https://api.example.com/feed response-body-json-jq '.data.ads=[]'"
        )
        self.assertEqual("Body Rewrite", body_section)
        self.assertEqual("http-response-jq ^https://api.example.com/feed '.data.ads=[]'", body_line)

        map_section, map_line = sync.convert_loon_rewrite_line(
            '^https://api.example.com/empty mock-response-body data-type=json data="{"code":0}"'
        )
        self.assertEqual("Map Local", map_section)
        self.assertIn("data-type=json", map_line)
        self.assertIn("status-code=200", map_line)

        header_section, header_line = sync.convert_loon_rewrite_line(
            "^https://api.example.com header-del X-Ads"
        )
        self.assertEqual("Header Rewrite", header_section)
        self.assertEqual("http-request ^https://api.example.com header-del X-Ads", header_line)


if __name__ == "__main__":
    unittest.main()
