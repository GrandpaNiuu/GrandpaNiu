from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "audit_repair_invalid_sources",
    ROOT / "scripts" / "audit_repair_invalid_sources.py",
)
assert SPEC and SPEC.loader
audit = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = audit
SPEC.loader.exec_module(audit)


class InvalidSourceAuditTests(unittest.TestCase):
    def test_duplicate_url_and_kind_are_checked_once(self) -> None:
        sources = [
            audit.Source("https://source.test/a", "one.conf", 1, "raw", "a"),
            audit.Source("https://source.test/a", "two.conf", 2, "raw", "b"),
            audit.Source("https://source.test/a", "three.conf", 3, "script", "c"),
        ]
        result = audit.Check(True, False, 200)
        with patch.object(audit, "check_source", return_value=result) as check:
            checks = audit.check_sources(sources)
        self.assertEqual(2, check.call_count)
        self.assertEqual(3, len(checks))
        self.assertTrue(all(item.ok for item in checks.values()))

    def test_app_source_scan_ignores_endpoint_regex_but_keeps_source_and_script_urls(self) -> None:
        path = ROOT / "Rewrite" / "Sources" / "Apps" / "_audit-test.conf"
        content = "\n".join(
            [
                "# source-url: https://source.test/module.lpx",
                "[URL Rewrite]",
                "^https://api.example.test/ad - reject",
                "[Script]",
                "test = type=http-response,pattern=^https://api.example.test/,script-path=https://source.test/script.js",
            ]
        )
        with patch.object(Path, "read_text", return_value=content):
            sources = audit.scan_text_file(path)
        self.assertEqual(
            {"https://source.test/module.lpx", "https://source.test/script.js"},
            {source.url for source in sources},
        )


if __name__ == "__main__":
    unittest.main()
