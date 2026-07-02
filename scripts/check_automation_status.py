#!/usr/bin/env python3
"""Check whether unattended GitHub Actions maintenance is still healthy."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "automation_status_report.md"
DEFAULT_REPOSITORY = "GrandpaNiuu/GrandpaNiu"
BEIJING = dt.timezone(dt.timedelta(hours=8))
API_TIMEOUT_SECONDS = 12
BAD_CONCLUSIONS = {"action_required", "failure", "startup_failure", "timed_out"}


@dataclass(frozen=True)
class WorkflowExpectation:
    file: str
    name: str
    cadence: str
    max_success_age_hours: int | None
    required: bool = True


WORKFLOWS: tuple[WorkflowExpectation, ...] = (
    WorkflowExpectation("daily-module-update.yml", "Daily Module Update", "daily, Beijing 00:37", 40),
    WorkflowExpectation("daily-audit-and-repair.yml", "Daily invalid rule audit and safe repair", "daily, Beijing 00:43", 40),
    WorkflowExpectation("daily-invalid-source-repair.yml", "Daily invalid source audit and repair", "daily, Beijing 00:49", 40),
    WorkflowExpectation("upstream-collect.yml", "Upstream candidate collect", "daily, Beijing 00:55", 40),
    WorkflowExpectation("scheduled-module-update.yml", "Scheduled Module Factory Update", "daily, Beijing 01:07", 40),
    WorkflowExpectation("upstream-app-module-sync.yml", "Upstream app module sync", "daily, Beijing 01:19", 40),
    WorkflowExpectation("daily-schedule-watchdog.yml", "Daily schedule watchdog", "daily, Beijing 04:30", 48),
    WorkflowExpectation("repository-health.yml", "Repository Health Check", "weekly, Sunday Beijing 01:37", 9 * 24),
    WorkflowExpectation("module-factory-build.yml", "Module Factory Build", "push/manual", None, required=False),
    WorkflowExpectation("pages-deploy.yml", "Deploy GitHub Pages", "workflow_run / manual / public-path push", None, required=False),
    WorkflowExpectation("workflow-failure-issue.yml", "Workflow failure issue", "workflow_run", None, required=False),
)


def now_utc() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def parse_time(value: str | None) -> dt.datetime | None:
    if not value:
        return None
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def fmt_time(value: dt.datetime | None) -> str:
    if not value:
        return "n/a"
    return value.astimezone(BEIJING).strftime("%Y-%m-%d %H:%M:%S %z")


def age_hours(value: dt.datetime | None, reference: dt.datetime) -> float | None:
    if not value:
        return None
    return max((reference - value.astimezone(dt.timezone.utc)).total_seconds() / 3600, 0.0)


def fmt_age(value: float | None) -> str:
    if value is None:
        return "n/a"
    if value < 1:
        return f"{value * 60:.0f}m"
    return f"{value:.1f}h"


def repository_name() -> str:
    value = os.environ.get("GITHUB_REPOSITORY", "").strip()
    if value and "/" in value:
        return value
    return DEFAULT_REPOSITORY


def github_api_json(url: str) -> dict[str, Any]:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "GrandpaNiu-automation-status",
    }
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=API_TIMEOUT_SECONDS) as response:
        payload = response.read().decode("utf-8", errors="replace")
    return json.loads(payload)


def fetch_runs(repo: str, workflow_file: str) -> list[dict[str, Any]]:
    quoted = urllib.parse.quote(workflow_file, safe="")
    url = f"https://api.github.com/repos/{repo}/actions/workflows/{quoted}/runs?per_page=20&branch=main"
    payload = github_api_json(url)
    runs = payload.get("workflow_runs", [])
    return runs if isinstance(runs, list) else []


def run_url(run: dict[str, Any] | None) -> str:
    if not run:
        return ""
    value = str(run.get("html_url") or "")
    return value


def run_label(run: dict[str, Any] | None) -> str:
    if not run:
        return "n/a"
    run_id = run.get("id") or run.get("databaseId") or "run"
    url = run_url(run)
    return f"[{run_id}]({url})" if url else str(run_id)


def evaluate_workflow(expectation: WorkflowExpectation, runs: list[dict[str, Any]], reference: dt.datetime) -> dict[str, Any]:
    latest = runs[0] if runs else None
    completed = [run for run in runs if run.get("status") == "completed"]
    latest_completed = completed[0] if completed else None
    last_success = next((run for run in completed if run.get("conclusion") == "success"), None)
    latest_completed_conclusion = str(latest_completed.get("conclusion") or "") if latest_completed else ""
    last_success_time = parse_time(str(last_success.get("updated_at") or last_success.get("created_at") or "")) if last_success else None
    success_age = age_hours(last_success_time, reference)

    blockers: list[str] = []
    warnings: list[str] = []
    if expectation.required and not runs:
        blockers.append("no runs found")
    if expectation.required and latest_completed_conclusion in BAD_CONCLUSIONS:
        blockers.append(f"latest completed run is {latest_completed_conclusion}")
    if expectation.required and expectation.max_success_age_hours is not None:
        if last_success is None:
            blockers.append("no successful completed run found")
        elif success_age is not None and success_age > expectation.max_success_age_hours:
            blockers.append(
                f"last success is stale ({fmt_age(success_age)} > {expectation.max_success_age_hours}h)"
            )
    if latest and latest.get("status") != "completed":
        warnings.append(f"latest run is {latest.get('status')}")
    if latest_completed_conclusion in {"cancelled", "skipped"}:
        warnings.append(f"latest completed run is {latest_completed_conclusion}")

    if blockers:
        state = "fail"
    elif warnings:
        state = "warn"
    else:
        state = "ok"

    return {
        "file": expectation.file,
        "name": expectation.name,
        "cadence": expectation.cadence,
        "required": expectation.required,
        "state": state,
        "latest": latest,
        "latest_completed": latest_completed,
        "latest_completed_conclusion": latest_completed_conclusion or "n/a",
        "last_success": last_success,
        "last_success_time": last_success_time,
        "success_age": success_age,
        "blockers": blockers,
        "warnings": warnings,
    }


def markdown_report(repo: str, rows: list[dict[str, Any]], api_error: str | None, reference: dt.datetime) -> str:
    blockers = [item for row in rows for item in row["blockers"]]
    warnings = [item for row in rows for item in row["warnings"]]
    status = "unknown" if api_error else "fail" if blockers else "warn" if warnings else "ok"
    lines = [
        "# Automation Status Report",
        "",
        f"- Generated at: {fmt_time(reference)}",
        f"- Repository: `{repo}`",
        f"- Overall status: `{status}`",
        f"- Blocking findings: {len(blockers)}",
        f"- Warnings: {len(warnings)}",
        "",
    ]
    if api_error:
        lines += [
            "## API Status",
            "",
            "GitHub Actions status could not be fetched in this environment.",
            "",
            "```text",
            api_error,
            "```",
            "",
            "Existing workflow syntax checks still run locally; this report will refresh with real run data in GitHub Actions.",
            "",
        ]
    lines += [
        "## Workflow Status",
        "",
        "| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |",
        "|---|---|---:|---|---|---|---|---:|---|",
    ]
    for row in rows:
        latest = row["latest"]
        latest_completed = row["latest_completed"]
        last_success = row["last_success"]
        notes = row["blockers"] or row["warnings"] or ["ok"]
        lines.append(
            "| "
            + " | ".join(
                [
                    f"`{row['file']}`",
                    row["cadence"],
                    "yes" if row["required"] else "observe",
                    row["state"],
                    f"{run_label(latest)} / {latest.get('status') if latest else 'n/a'}",
                    f"{run_label(latest_completed)} / {row['latest_completed_conclusion']}",
                    f"{run_label(last_success)} / {fmt_time(row['last_success_time'])}",
                    fmt_age(row["success_age"]),
                    "<br>".join(notes),
                ]
            )
            + " |"
        )
    lines += [
        "",
        "## Policy",
        "",
        "- Daily maintenance workflows should have a successful completed run within 40 hours.",
        "- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.",
        "- Repository health is weekly and should have a successful completed run within 9 days.",
        "- Push-triggered and workflow-run issue workflows are observed but do not block on age.",
        "- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.",
        "",
    ]
    return "\n".join(lines)


def write_report(text: str) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    parser = argparse.ArgumentParser(description="Check scheduled GitHub Actions maintenance status.")
    parser.add_argument("--strict", action="store_true", help="fail if required workflows are stale or failed")
    parser.add_argument("--no-write", action="store_true", help="evaluate without writing reports/automation_status_report.md")
    args = parser.parse_args()

    repo = repository_name()
    reference = now_utc()
    rows: list[dict[str, Any]] = []
    api_error: str | None = None

    try:
        for expectation in WORKFLOWS:
            rows.append(evaluate_workflow(expectation, fetch_runs(repo, expectation.file), reference))
    except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        api_error = f"{type(exc).__name__}: {exc}"
        rows = [
            {
                "file": expectation.file,
                "name": expectation.name,
                "cadence": expectation.cadence,
                "required": expectation.required,
                "state": "unknown",
                "latest": None,
                "latest_completed": None,
                "latest_completed_conclusion": "n/a",
                "last_success": None,
                "last_success_time": None,
                "success_age": None,
                "blockers": [],
                "warnings": ["GitHub API unavailable"],
            }
            for expectation in WORKFLOWS
        ]

    report = markdown_report(repo, rows, api_error, reference)
    if not args.no_write:
        write_report(report)
        print(f"Automation status report written to {REPORT}")
    elif api_error:
        print(f"WARNING: GitHub Actions status unavailable: {api_error}", file=sys.stderr)

    blockers = [item for row in rows for item in row["blockers"]]
    if args.strict and blockers:
        raise SystemExit("Automation status check failed: " + "; ".join(blockers))
    if args.strict and api_error:
        print("WARNING: strict automation status skipped because GitHub API was unavailable.", file=sys.stderr)


if __name__ == "__main__":
    main()
