from __future__ import annotations

import os
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
        self.assertIn("check_automation_status.py", text)
        self.assertIn("validate_repository.py", text)

    def test_quality_gate_uses_unified_builder_for_release_outputs(self) -> None:
        text = (ROOT / "scripts" / "quality_gate.py").read_text(encoding="utf-8")
        self.assertIn('"Rewrite/Generator/Builder.py", "--profile", "fusion", "--release"', text)
        self.assertNotIn('"scripts/build_module.py", "--build"', text)
        self.assertNotIn('"scripts/factory_finalize.py"', text)
        self.assertNotIn('"scripts/build_release_variants.py"', text)

    def test_script_aggregation_cache_is_validated(self) -> None:
        text = (ROOT / "tools" / "validate_script_aggregation.py").read_text(encoding="utf-8")
        self.assertIn("fusion-script-bundle.cache.json", text)
        self.assertIn("cache sha256 mismatch", text)

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

    def test_auto_commit_workflows_use_cross_workflow_lock_and_safe_commit_helper(self) -> None:
        offenders: list[str] = []
        for path in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
            text = path.read_text(encoding="utf-8")
            if "git push origin HEAD:main" not in text and "commit_generated_changes.sh" not in text:
                continue
            expected_group = "group: module-maintenance-${{ github.workflow }}-${{ github.ref }}"
            if expected_group not in text:
                offenders.append(f"{path.name}: missing isolated maintenance concurrency group")
            if "scripts/commit_generated_changes.sh" not in text:
                offenders.append(f"{path.name}: missing commit helper")
            if "tools/acquire_automation_lock.sh" not in text:
                offenders.append(f"{path.name}: missing cross-workflow lock acquisition")
            if "tools/release_automation_lock.sh" not in text:
                offenders.append(f"{path.name}: missing cross-workflow lock release")
            if "if: always()" not in text:
                offenders.append(f"{path.name}: lock release is not unconditional")
            if "git reset --hard" in text:
                offenders.append(f"{path.name}: destructive reset")
            if "git add -A" in text:
                offenders.append(f"{path.name}: broad staging")
        self.assertEqual([], offenders)

    def test_full_builder_workflows_commit_android_and_windows_outputs(self) -> None:
        offenders: list[str] = []
        for path in sorted((ROOT / ".github" / "workflows").glob("*.yml")):
            text = path.read_text(encoding="utf-8")
            if "Rewrite/Generator/Builder.py --profile fusion --release" not in text:
                continue
            if "scripts/commit_generated_changes.sh" not in text:
                continue
            for generated_path in ("Android", "Windows"):
                if f"\n            {generated_path} \\" not in text and f"\n            {generated_path}\n" not in text:
                    offenders.append(f"{path.name}: missing {generated_path} in generated commit paths")
        self.assertEqual([], offenders)

    def test_push_validation_has_one_factory_entrypoint(self) -> None:
        factory = (ROOT / ".github" / "workflows" / "module-factory-build.yml").read_text(encoding="utf-8")
        self.assertIn("\n  push:\n", factory)
        for name in ("daily-audit-and-repair.yml", "scheduled-module-update.yml"):
            text = (ROOT / ".github" / "workflows" / name).read_text(encoding="utf-8")
            self.assertNotIn("\n  push:\n", text, name)

    def test_failure_issue_body_does_not_use_expanding_shell_heredoc(self) -> None:
        text = (ROOT / ".github" / "workflows" / "workflow-failure-issue.yml").read_text(encoding="utf-8")
        self.assertNotIn("<<EOF", text)
        self.assertIn("python3 - <<'PY'", text)

    def test_failure_issue_watcher_observes_pages_deploy(self) -> None:
        text = (ROOT / ".github" / "workflows" / "workflow-failure-issue.yml").read_text(encoding="utf-8")
        self.assertIn("      - Deploy GitHub Pages\n", text)

    def test_invalid_rule_workflow_is_report_only_and_does_not_duplicate_source_repair(self) -> None:
        text = (ROOT / ".github" / "workflows" / "daily-audit-and-repair.yml").read_text(encoding="utf-8")
        self.assertIn("scripts/audit_and_repair_module.py --report-only", text)
        self.assertNotIn("scripts/audit_repair_invalid_sources.py", text)
        self.assertNotIn("Rewrite/Generator/Builder.py --profile fusion --release", text)

    def test_source_repair_and_candidate_collection_have_distinct_ownership(self) -> None:
        source_repair = (ROOT / ".github" / "workflows" / "daily-invalid-source-repair.yml").read_text(encoding="utf-8")
        candidate_collect = (ROOT / ".github" / "workflows" / "upstream-collect.yml").read_text(encoding="utf-8")

        self.assertIn("scripts/audit_repair_invalid_sources.py", source_repair)
        self.assertNotIn("scripts/collect_upstreams.py", source_repair)
        self.assertIn("git status --porcelain", source_repair)
        self.assertIn("if: steps.repair.outputs.source_changed == 'true'", source_repair)
        self.assertIn("scripts/collect_upstreams.py", candidate_collect)
        self.assertIn("source_changed", candidate_collect)
        self.assertIn("git status --porcelain", candidate_collect)
        self.assertIn("if: steps.collect.outputs.source_changed == 'true'", candidate_collect)
        for target in (
            "Rules/direct.list",
            "Rules/spotify-direct.list",
            "Rules/youtube-direct.list",
            "Rules/reject.list",
            "Rules/app-clean.list",
            "Rules/web-ads.list",
            "Scripts/spotify.conf",
            "Scripts/youtube.conf",
            "Scripts/app-clean.conf",
        ):
            self.assertIn(target, candidate_collect)

    def test_change_impact_report_names_its_committed_diff_range(self) -> None:
        text = (ROOT / "scripts" / "generate_change_impact_report.py").read_text(encoding="utf-8")
        self.assertIn("HEAD~1..HEAD (committed-change mode)", text)

    def test_daily_watchdog_checks_scheduled_workflow_status_even_when_module_is_fresh(self) -> None:
        text = (ROOT / ".github" / "workflows" / "daily-schedule-watchdog.yml").read_text(encoding="utf-8")
        self.assertIn("actions: read", text)
        self.assertIn("scripts/check_automation_status.py", text)
        self.assertIn("scripts/check_automation_status.py --strict --no-write", text)
        self.assertNotIn("Daily module date is already fresh; no watchdog recovery needed.\"\n            exit 0", text)

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

    def test_automation_lock_serializes_writers_and_fast_forwards_waiter(self) -> None:
        bash = shutil.which("bash")
        if not bash:
            self.skipTest("bash is required for the workflow automation lock")

        with tempfile.TemporaryDirectory() as temp:
            base = Path(temp)
            remote = base / "remote.git"
            holder = base / "holder"
            waiter = base / "waiter"
            subprocess.run(["git", "init", "--bare", str(remote)], check=True, capture_output=True)
            subprocess.run(["git", "clone", str(remote), str(holder)], check=True, capture_output=True)
            subprocess.run(["git", "config", "user.name", "test"], cwd=holder, check=True)
            subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=holder, check=True)

            tools_dir = holder / "tools"
            tools_dir.mkdir()
            for name in ("acquire_automation_lock.sh", "release_automation_lock.sh"):
                shutil.copy2(ROOT / "tools" / name, tools_dir / name)
            (holder / "artifact.txt").write_text("initial\n", encoding="utf-8")
            subprocess.run(["git", "add", "artifact.txt", "tools"], cwd=holder, check=True)
            subprocess.run(["git", "commit", "-m", "initial"], cwd=holder, check=True, capture_output=True)
            subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=holder, check=True, capture_output=True)
            subprocess.run(
                ["git", f"--git-dir={remote}", "symbolic-ref", "HEAD", "refs/heads/main"], check=True
            )
            subprocess.run(["git", "clone", str(remote), str(waiter)], check=True, capture_output=True)

            env = {
                **os.environ,
                "AUTOMATION_LOCK_ATTEMPTS": "1",
                "AUTOMATION_LOCK_SLEEP_SECONDS": "1",
                "AUTOMATION_LOCK_STALE_SECONDS": "60",
            }
            subprocess.run(
                [bash, "tools/acquire_automation_lock.sh"],
                cwd=holder,
                env=env,
                check=True,
                capture_output=True,
            )

            (holder / "artifact.txt").write_text("holder update\n", encoding="utf-8")
            subprocess.run(["git", "add", "artifact.txt"], cwd=holder, check=True)
            subprocess.run(["git", "commit", "-m", "holder update"], cwd=holder, check=True, capture_output=True)
            subprocess.run(["git", "push", "origin", "HEAD:main"], cwd=holder, check=True, capture_output=True)

            blocked = subprocess.run(
                [bash, "tools/acquire_automation_lock.sh"],
                cwd=waiter,
                env=env,
                capture_output=True,
                text=True,
            )
            self.assertNotEqual(0, blocked.returncode)
            self.assertIn("Timed out waiting", blocked.stderr)

            subprocess.run(
                [bash, "tools/release_automation_lock.sh"],
                cwd=holder,
                check=True,
                capture_output=True,
            )
            subprocess.run(
                [bash, "tools/acquire_automation_lock.sh"],
                cwd=waiter,
                env=env,
                check=True,
                capture_output=True,
            )
            waiter_head = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=waiter, text=True).strip()
            remote_head = subprocess.check_output(
                ["git", f"--git-dir={remote}", "rev-parse", "main"], text=True
            ).strip()
            self.assertEqual(remote_head, waiter_head)
            subprocess.run(
                [bash, "tools/release_automation_lock.sh"],
                cwd=waiter,
                check=True,
                capture_output=True,
            )


if __name__ == "__main__":
    unittest.main()
