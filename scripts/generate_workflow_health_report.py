#!/usr/bin/env python3
"""Generate a workflow health report with optional GitHub Actions status."""

from __future__ import annotations

import datetime as dt
import json
import os
import re
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "workflow_health_report.md"
DEFAULT_REPOSITORY = "GrandpaNiuu/GrandpaNiu"
API_ROOT = "https://api.github.com"

WORKFLOWS = [
    ("Module Factory Build", ".github/workflows/module-factory-build.yml", "Build Release and sync Root"),
    ("Daily Module Update", ".github/workflows/daily-module-update.yml", "Daily module date, build, report and validation"),
    ("Daily invalid rule audit and safe repair", ".github/workflows/daily-audit-and-repair.yml", "Daily invalid rule audit and safe repair"),
    ("Daily invalid source audit and repair", ".github/workflows/daily-invalid-source-repair.yml", "Daily invalid source audit and repair"),
    ("Scheduled Module Factory Update", ".github/workflows/scheduled-module-update.yml", "Scheduled module factory build and publish"),
    ("Upstream app module sync", ".github/workflows/upstream-app-module-sync.yml", "Sync upstream app modules and validate build"),
    ("Upstream candidate collect", ".github/workflows/upstream-collect.yml", "Collect trusted upstream candidates"),
    ("Daily schedule watchdog", ".github/workflows/daily-schedule-watchdog.yml", "Recover the daily module refresh if GitHub drops a scheduled run"),
    ("Repository Health Check", ".github/workflows/repository-health.yml", "Repository governance health check"),
    ("Deploy GitHub Pages", ".github/workflows/pages-deploy.yml", "Publish the static Pages artifact with serialized deploy retries"),
    ("Workflow failure issue", ".github/workflows/workflow-failure-issue.yml", "Create or update issues for failed Actions"),
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def triggers(text: str) -> str:
    items: list[str] = []
    if "workflow_dispatch" in text:
        items.append("manual")
    if "schedule:" in text:
        items.append("schedule")
    if re.search(r"(?m)^\s*push:", text):
        items.append("push")
    if "workflow_run" in text:
        items.append("workflow_run")
    return " / ".join(items) if items else "unconfirmed"


def priority(path: str) -> str:
    if "module-factory" in path:
        return "Builder, profile, source merge, Root/Release sync"
    if "daily-module" in path:
        return "date refresh, Builder, validation, rebase retry"
    if "daily-audit" in path:
        return "audit_and_repair_module.py, Fusion build, rebase retry"
    if "invalid-source" in path:
        return "network fetch, invalid history, conservative source repair"
    if "scheduled-module" in path:
        return "Builder.py --profile fusion --release, commit, rebase retry"
    if "upstream-app" in path:
        return "app-modules.json, upstream fetch, rollback on failed build"
    if "upstream" in path:
        return "candidates.json, risk filters, trusted repositories"
    if "schedule-watchdog" in path:
        return "module update-date, recovery build, rebase retry"
    if "repository-health" in path:
        return "governance files, duplicate scripts, duplicate MITM, report freshness"
    if "pages-deploy" in path:
        return "Pages artifact scope, deploy-pages timeout, deployment retry guard"
    if "workflow-failure" in path:
        return "workflow_run permissions, issue creation/update"
    return "manual review"


def github_json(path: str) -> tuple[dict[str, Any] | None, str]:
    request = urllib.request.Request(
        f"{API_ROOT}{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "GrandpaNiu-workflow-health",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=20) as response:
            return json.loads(response.read().decode("utf-8")), ""
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:200]
        return None, f"HTTP {exc.code}: {detail}"
    except OSError as exc:
        return None, f"{type(exc).__name__}: {exc}"


def latest_run(workflow_path: str, repository: str) -> tuple[dict[str, str], str]:
    workflow_file = workflow_path.rsplit("/", 1)[-1]
    data, error = github_json(f"/repos/{repository}/actions/workflows/{workflow_file}/runs?per_page=1")
    if error:
        return {}, error
    runs = data.get("workflow_runs", []) if isinstance(data, dict) else []
    if not runs:
        return {}, "no runs found"
    run = runs[0]
    return {
        "created_at": str(run.get("created_at") or ""),
        "status": str(run.get("status") or "unknown"),
        "conclusion": str(run.get("conclusion") or "pending"),
        "url": str(run.get("html_url") or ""),
    }, ""


def conclusion_advice(status: str, conclusion: str, fallback: str) -> str:
    if fallback:
        return f"Unable to confirm: {fallback}"
    if status != "completed":
        return "Run is not completed; check again after it finishes"
    if conclusion == "success":
        return "passed"
    if conclusion == "cancelled":
        return "cancelled, usually superseded by a newer concurrency run"
    if conclusion in {"failure", "timed_out", "action_required"}:
        return "open the run log and fix the failed step"
    return "unknown status; manual review required"


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    repository = os.environ.get("GITHUB_REPOSITORY", DEFAULT_REPOSITORY).strip() or DEFAULT_REPOSITORY

    lines = [
        "# Workflow Health Report",
        "",
        f"- Generated at: {now}",
        f"- Repository: `{repository}`",
        f"- Workflows checked: {len(WORKFLOWS)}",
        "",
        "| Workflow | File | Purpose | Triggers | Latest run | Status | Conclusion | Run URL | Advice |",
        "|---|---|---|---|---|---|---|---|---|",
    ]

    for name, rel, purpose in WORKFLOWS:
        text = read(ROOT / rel)
        if not text:
            lines.append(f"| {name} | `{rel}` | {purpose} | missing | missing | missing | missing | - | add workflow file |")
            continue
        run_info, error = latest_run(rel, repository)
        status = run_info.get("status", "unconfirmed")
        conclusion = run_info.get("conclusion", "unconfirmed")
        created_at = run_info.get("created_at", "unconfirmed")
        url = run_info.get("url", "-")
        url_cell = f"[open]({url})" if url.startswith("https://") else "-"
        advice = conclusion_advice(status, conclusion, error) if run_info else f"config exists; check {priority(rel)}"
        lines.append(f"| {name} | `{rel}` | {purpose} | {triggers(text)} | {created_at} | {status} | {conclusion} | {url_cell} | {advice} |")

    lines += [
        "",
        "## Notes",
        "",
        "- Only `success` is treated as a fully passing latest run.",
        "- `cancelled` is usually harmless when a newer Pages or maintenance run superseded an older one.",
        "- If GitHub API access fails, this report still confirms local workflow configuration exists but cannot prove latest run state.",
        "- iOS public entry remains the single Fusion module; legacy Stable / Stable Plus / Lite / Full outputs are not public workflow entries.",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Workflow health report written to {REPORT}")


if __name__ == "__main__":
    main()
