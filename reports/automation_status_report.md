# Automation Status Report

- Generated at: 2026-09-20 06:22:31 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `070c7433`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35462438135](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462438135) / completed | [35462438135](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462438135) / success | [35462438135](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462438135) / 2026-09-20 02:50:58 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35462594553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462594553) / completed | [35462594553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462594553) / success | [35462594553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462594553) / 2026-09-20 02:53:19 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35462849274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462849274) / completed | [35462849274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462849274) / success | [35462849274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462849274) / 2026-09-20 02:58:30 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35462902445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462902445) / completed | [35462902445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462902445) / success | [35462902445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462902445) / 2026-09-20 02:59:29 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35463815189](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35463815189) / completed | [35463815189](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35463815189) / success | [35463815189](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35463815189) / 2026-09-20 03:16:59 +0800 | 3.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35464122001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464122001) / completed | [35464122001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464122001) / success | [35464122001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464122001) / 2026-09-20 03:23:16 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35473135337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473135337) / in_progress | [35402727925](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402727925) / success | [35402727925](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402727925) / 2026-09-19 06:43:18 +0800 | 23.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / completed | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / success | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / 2026-09-14 03:43:57 +0800 | 146.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1035.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35402785466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402785466) / completed | [35402785466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402785466) / success | [35402785466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402785466) / 2026-09-19 06:43:57 +0800 | 23.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35464193878](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464193878) / completed | [35464193878](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464193878) / success | [35464193878](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464193878) / 2026-09-20 03:23:27 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
