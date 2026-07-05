# Automation Status Report

- Generated at: 2026-07-06 05:57:30 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `8768cb71`
- Overall status: `unknown`
- Blocking findings: 0
- Warnings: 11

## API Status

GitHub Actions status could not be fetched in this environment.

```text
URLError: <urlopen error _ssl.c:999: The handshake operation timed out>
```

Existing workflow syntax checks still run locally; this report will refresh with real run data in GitHub Actions.

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `module-factory-build.yml` | push/manual | observe | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |
| `workflow-failure-issue.yml` | workflow_run | observe | unknown | n/a / n/a | n/a / n/a | n/a / n/a | n/a | GitHub API unavailable |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
