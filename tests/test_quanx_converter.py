from __future__ import annotations

import contextlib
import importlib.util
import io
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "convert_quanx_rules",
    ROOT / "scripts" / "convert_quanx_rules.py",
)
assert SPEC and SPEC.loader
converter = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = converter
SPEC.loader.exec_module(converter)


class QuanXConverterTests(unittest.TestCase):
    def test_fetch_failure_keeps_existing_converted_output(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            output = root / "Rules" / "converted" / "example.list"
            output.parent.mkdir(parents=True)
            output.write_text("DOMAIN,ad.example.com\n", encoding="utf-8")
            source = converter.Source("Example", "https://example.com/list", output)
            with patch.object(converter, "ROOT", root), patch.object(
                converter,
                "fetch_text",
                side_effect=converter.FetchError("network down"),
            ):
                message = converter.convert_source(source)
            self.assertIn("keeping existing", message)
            self.assertEqual("DOMAIN,ad.example.com\n", output.read_text(encoding="utf-8"))

    def test_fetch_failure_without_existing_output_still_fails(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = converter.Source("Example", "https://example.com/list", root / "missing.list")
            with patch.object(converter, "ROOT", root), patch.object(
                converter,
                "fetch_text",
                side_effect=converter.FetchError("network down"),
            ):
                with contextlib.redirect_stderr(io.StringIO()):
                    with self.assertRaises(SystemExit):
                        converter.convert_source(source)


if __name__ == "__main__":
    unittest.main()
