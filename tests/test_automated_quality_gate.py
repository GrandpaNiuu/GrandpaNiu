from __future__ import annotations

import shutil
import subprocess
import tempfile
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
    "tools/",
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
        self.assertIn("validate_app_sources.py", text)
        self.assertIn("generate_automated_quality_evidence.py", text)
        self.assertIn("validate_repository.py", text)

    def test_quality_gate_strictly_checks_freshness_after_final_bundle_validation(self) -> None:
        text = (ROOT / "scripts" / "quality_gate.py").read_text(encoding="utf-8")
        freshness = text.rfind('"scripts/check_report_freshness.py", "--strict"')
        profile_rebuild = text.rfind('"scripts/validate_profiles.py"')
        aggregation = text.rfind('"tools/validate_script_aggregation.py"')
        sandbox = text.rfind('"tools/test_script_bundle_sandbox.py"')

        self.assertGreater(freshness, profile_rebuild)
        self.assertGreater(freshness, aggregation)
        self.assertGreater(freshness, sandbox)

    def test_status_generators_do_not_read_legacy_manual_log(self) -> None:
        for rel in ("scripts/generate_app_status_matrix.py", "scripts/generate_app_coverage_matrix.py"):
            text = (ROOT / rel).read_text(encoding="utf-8")
            self.assertNotIn("manual_test_log", text)
            self.assertNotIn("MANUAL_LOG", text)

    def test_invalid_source_audit_includes_app_sources(self) -> None:
        text = (ROOT / "scripts" / "audit_repair_invalid_sources.py").read_text(encoding="utf-8")
        self.assertIn('"Rewrite/Sources/Apps/*.conf"', text)

    def test_workflows_use_automated_quality_evidence_not_legacy_log(self) -> None:
        workflow_text = "\n".join(
            path.read_text(encoding="utf-8") for path in (ROOT / ".github" / "workflows").glob("*.yml")
        )
        self.assertNotIn("manual_test_log", workflow_text)
        self.assertIn("automated_quality_evidence.md", workflow_text)
        self.assertIn("scripts/quality_gate.py", workflow_text)

    def test_auto_commit_workflows_share_lock_and_use_safe_commit_helper(self) -> None:
        offenders: list[str] = []
        for path in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
            text = path.read_text(encoding="utf-8")
            if "git push origin HEAD:main" not in text and "commit_generated_changes.sh" not in text:
                continue
            if "group: module-maintenance" not in text:
                offenders.append(f"{path.name}: missing shared concurrency group")
            if "scripts/commit_generated_changes.sh" not in text:
                offenders.append(f"{path.name}: missing commit helper")
            if "git reset --hard" in text:
                offenders.append(f"{path.name}: destructive reset")
            if "git add -A" in text:
                offenders.append(f"{path.name}: broad staging")
        self.assertEqual([], offenders)

    def test_commit_helper_requires_explicit_paths_and_safe_rebase(self) -> None:
        text = (ROOT / "scripts" / "commit_generated_changes.sh").read_text(encoding="utf-8")
        self.assertIn('git add -- "$@"', text)
        self.assertIn("git rebase origin/main", text)
        self.assertNotIn("git add -A", text)
        self.assertNotIn("git reset --hard", text)

    def test_commit_helper_pushes_only_explicit_paths(self) -> None:
        bash = shutil.which("bash")
        if not bash:
            self.skipTest("bash is required for the workflow commit helper")

        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            remote = base / "remote.git"
            work = base / "work"
            subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
            subprocess.run(["git", "clone", str(remote), str(work)], check=True, capture_output=True)
            subprocess.run(["git", "config", "user.name", "test"], cwd=work, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=work, check=True)

            artifact = work / "artifact.txt"
            unstaged = work / "unstaged.txt"
            artifact.write_text("initial\n", encoding="utf-8")
            unstaged.write_text("initial\n", encoding="utf-8")
            subprocess.run(["git", "add", "artifact.txt", "unstaged.txt"], cwd=work, check=True)
            subprocess.run(["git", "commit", "-m", "initial"], cwd=work, check=True, capture_output=True)
            subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=work, check=True, capture_output=True)

            helper_dir = work / "scripts"
            helper_dir.mkdir()
            shutil.copy2(ROOT / "scripts" / "commit_generated_changes.sh", helper_dir)
            artifact.write_text("published\n", encoding="utf-8")
            unstaged.write_text("local-only\n", encoding="utf-8")

            subprocess.run(
                [bash, "scripts/commit_generated_changes.sh", "generated update", "artifact.txt"],
                cwd=work,
                check=True,
                capture_output=True,
            )
            published = subprocess.check_output(
                ["git", f"--git-dir={remote}", "show", "main:artifact.txt"], text=True
            )
            remote_unstaged = subprocess.check_output(
                ["git", f"--git-dir={remote}", "show", "main:unstaged.txt"], text=True
            )
            self.assertEqual("published\n", published)
            self.assertEqual("initial\n", remote_unstaged)


if __name__ == "__main__":
    unittest.main()
