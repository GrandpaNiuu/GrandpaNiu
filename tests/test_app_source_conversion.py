from __future__ import annotations

import base64
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "sync_upstream_app_modules",
    ROOT / "scripts" / "sync_upstream_app_modules.py",
)
assert SPEC and SPEC.loader
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class AppSourceConversionTests(unittest.TestCase):
    def test_loon_redirect_is_reordered_for_shadowrocket(self) -> None:
        section, line = sync.convert_loon_rewrite_line(r"^http://example\.com/(.*) 307 https://cdn.example.com/$1")
        self.assertEqual("URL Rewrite", section)
        self.assertEqual(r"^http://example\.com/(.*) https://cdn.example.com/$1 307", line)

    def test_header_replace_regex_uses_supported_shadowrocket_action(self) -> None:
        section, line = sync.convert_loon_rewrite_line(
            r"^https://api\.example\.com header-replace-regex methodname .*Banner null"
        )
        self.assertEqual("Header Rewrite", section)
        self.assertEqual(
            r"http-request ^https://api\.example\.com header-replace methodname .*Banner null",
            line,
        )

    def test_map_local_json_is_escaped_and_status_is_unique(self) -> None:
        line = sync.normalize_map_local_line(
            r'^https://api\.example\.com/ad data-type=json data="{"code":0}" status-code=200 status-code=200 header="content-type: application/json"'
        )
        self.assertIn(r'data="{\"code\":0}"', line)
        self.assertEqual(1, line.count("status-code="))

    def test_mixed_rule_section_routes_rewrite_and_bare_domain(self) -> None:
        sections = sync.convert_rule_section(
            [
                "ad.example.com",
                r"^http://1\.2\.3\.4/(.*) 307 https://cdn.testcdn.net/$1",
            ],
            "example",
        )
        self.assertEqual(["DOMAIN,ad.example.com,REJECT"], sections["Rule"])
        self.assertEqual(
            [r"^http://1\.2\.3\.4/(.*) https://cdn.testcdn.net/$1 307"],
            sections["URL Rewrite"],
        )

    def test_remote_map_local_data_is_embedded_as_base64(self) -> None:
        source = "\n".join(
            [
                "#!name=Example",
                "[Map Local]",
                'https://example.com/a.js data-type=text data-path="https://cdn.example.com/a.js" status-code=200',
            ]
        )
        with patch.object(sync, "fetch_text", return_value="const ok = true;"):
            converted = sync.inline_remote_map_local_data(source)
        expected = base64.b64encode(b"const ok = true;").decode("ascii")
        self.assertIn(f'data-type=base64 data="{expected}"', converted)
        self.assertNotIn("data-path=", converted)

    def test_duplicate_script_names_receive_stable_suffixes(self) -> None:
        lines = [
            "cleanup = type=http-response,pattern=one,script-path=https://example.com/a.js",
            "cleanup = type=http-response,pattern=two,script-path=https://example.com/a.js",
        ]
        converted = sync.dedupe_script_names(lines)
        self.assertTrue(converted[0].startswith("cleanup ="))
        self.assertTrue(converted[1].startswith("cleanup-2 ="))


if __name__ == "__main__":
    unittest.main()
