from __future__ import annotations

import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEXT_SUFFIXES = {
    ".conf",
    ".sgmodule",
    ".module",
    ".list",
    ".py",
    ".js",
    ".json",
    ".md",
    ".yml",
    ".yaml",
    ".html",
    ".txt",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
}
ACTIVE_PREFIXES = (
    ".github/",
    "docs/",
    "scripts/",
    "tests/",
)
ACTIVE_FILES = {
    "README.md",
    "SECURITY.md",
    "CONTRIBUTING.md",
}
LEGACY_TEST_GATE_TOKENS = (
    "manual_test_log",
    "人工测试",
    "真机测试",
    "手动测试",
    "待人工真机测试",
    "用户确认",
)


def tracked_files() -> list[Path]:
    output = subprocess.check_output(
        ["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True
    )
    return [ROOT / line for line in output.splitlines() if line]


def is_text_file(path: Path) -> bool:
    return path.suffix.lower() in TEXT_SUFFIXES or path.name in {"LICENSE", "README.md", "CONTRIBUTING.md"}


def active_policy_file(path: Path) -> bool:
    rel = path.relative_to(ROOT).as_posix()
    return rel in ACTIVE_FILES or rel.startswith(ACTIVE_PREFIXES)


class AutomatedQualityGateTests(unittest.TestCase):
    def test_tracked_text_files_do_not_contain_utf8_bom(self) -> None:
        offenders = []
        for path in tracked_files():
            if is_text_file(path) and b"\xef\xbb\xbf" in path.read_bytes():
                offenders.append(path.relative_to(ROOT).as_posix())
        self.assertEqual([], offenders)

    def test_active_policy_and_scripts_no_longer_reference_legacy_manual_test_gate(self) -> None:
        offenders: list[str] = []
        for path in tracked_files():
            rel = path.relative_to(ROOT).as_posix()
            if rel.startswith("backup/") or not is_text_file(path) or not active_policy_file(path):
                continue
            text = path.read_text(encoding="utf-8", errors="replace")
            for token in LEGACY_TEST_GATE_TOKENS:
                if token in text:
                    offenders.append(f"{rel}: {token}")
        self.assertEqual([], offenders)

    def test_quality_gate_runs_unit_tests_and_writes_automated_evidence(self) -> None:
        text = (ROOT / "scripts" / "quality_gate.py").read_text(encoding="utf-8")
        self.assertIn("unittest", text)
        self.assertIn("generate_automated_quality_evidence.py", text)
        self.assertIn("validate_repository.py", text)

    def test_status_generators_do_not_read_legacy_manual_log(self) -> None:
        for rel in ("scripts/generate_app_status_matrix.py", "scripts/generate_app_coverage_matrix.py"):
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn("manual_test_log", text)
            self.assertNotIn("MANUAL_LOG", text)

    def test_workflows_use_automated_quality_evidence_not_legacy_log(self) -> None:
        workflow_text = "\n".join(
            path.read_text(encoding="utf-8") for path in (ROOT / ".github" / "workflows").glob("*.yml")
        )
        self.assertNotIn("manual_test_log", workflow_text)
        self.assertIn("generate_automated_quality_evidence.py", workflow_text)
        self.assertIn("scripts/quality_gate.py", workflow_text)


if __name__ == "__main__":
    unittest.main()
