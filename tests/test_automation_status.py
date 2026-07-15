from __future__ import annotations

import datetime as dt
import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "check_automation_status",
    ROOT / "scripts" / "check_automation_status.py",
)
assert SPEC and SPEC.loader
status = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = status
SPEC.loader.exec_module(status)


class AutomationStatusTests(unittest.TestCase):
    def test_quality_gate_workflows_provide_authenticated_actions_status(self) -> None:
        for relative in (
            "module-factory-build.yml",
            "daily-module-update.yml",
            "daily-schedule-watchdog.yml",
            "repository-health.yml",
        ):
            text = (ROOT / ".github" / "workflows" / relative).read_text(encoding="utf-8")
            self.assertIn("GITHUB_TOKEN:", text, relative)
            self.assertRegex(text, r"GITHUB_TOKEN:\s*\$\{\{\s*(?:github\.token|secrets\.GITHUB_TOKEN)\s*\}\}")

    def test_in_progress_run_with_fresh_success_is_not_a_warning(self) -> None:
        reference = dt.datetime(2026, 7, 16, 4, 0, tzinfo=dt.timezone.utc)
        expectation = status.WorkflowExpectation("sync.yml", "Sync", "daily", 40)
        row = status.evaluate_workflow(
            expectation,
            [
                {
                    "status": "in_progress",
                    "conclusion": None,
                    "head_sha": "currentsha0000000000000000000000000000000",
                    "updated_at": "2026-07-16T03:55:00Z",
                },
                {
                    "status": "completed",
                    "conclusion": "success",
                    "head_sha": "previoussha000000000000000000000000000000",
                    "updated_at": "2026-07-16T01:00:00Z",
                },
            ],
            reference,
            current_sha="currentsha0000000000000000000000000000000",
        )

        self.assertEqual([], row["blockers"])
        self.assertEqual([], row["warnings"])
        self.assertEqual("ok", row["state"])

    def test_old_commit_failure_with_fresh_success_is_warning(self) -> None:
        reference = dt.datetime(2026, 7, 3, 4, 0, tzinfo=dt.timezone.utc)
        expectation = status.WorkflowExpectation("sync.yml", "Sync", "daily", 40)
        rows = status.evaluate_workflow(
            expectation,
            [
                {
                    "status": "completed",
                    "conclusion": "failure",
                    "head_sha": "oldsha0000000000000000000000000000000000",
                    "updated_at": "2026-07-03T02:00:00Z",
                },
                {
                    "status": "completed",
                    "conclusion": "success",
                    "head_sha": "oldersuccess0000000000000000000000000000",
                    "updated_at": "2026-07-03T01:00:00Z",
                },
            ],
            reference,
            current_sha="newsha0000000000000000000000000000000000",
        )
        self.assertEqual([], rows["blockers"])
        self.assertEqual("warn", rows["state"])
        self.assertIn("older commit", rows["warnings"][0])

    def test_current_commit_failure_is_blocking(self) -> None:
        reference = dt.datetime(2026, 7, 3, 4, 0, tzinfo=dt.timezone.utc)
        expectation = status.WorkflowExpectation("sync.yml", "Sync", "daily", 40)
        rows = status.evaluate_workflow(
            expectation,
            [
                {
                    "status": "completed",
                    "conclusion": "failure",
                    "head_sha": "currentsha0000000000000000000000000000000",
                    "updated_at": "2026-07-03T02:00:00Z",
                },
                {
                    "status": "completed",
                    "conclusion": "success",
                    "head_sha": "oldersuccess0000000000000000000000000000",
                    "updated_at": "2026-07-03T01:00:00Z",
                },
            ],
            reference,
            current_sha="currentsha0000000000000000000000000000000",
        )
        self.assertEqual(["latest completed run is failure"], rows["blockers"])
        self.assertEqual("fail", rows["state"])


if __name__ == "__main__":
    unittest.main()
