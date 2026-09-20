# Automation Status Report

- Generated at: 2026-09-21 03:01:50 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ea2d2213`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35530895441](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35530895441) / in_progress | [35462438135](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462438135) / success | [35462438135](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462438135) / 2026-09-20 02:50:58 +0800 | 24.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35462594553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462594553) / completed | [35462594553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462594553) / success | [35462594553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462594553) / 2026-09-20 02:53:19 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35462849274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462849274) / completed | [35462849274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462849274) / success | [35462849274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462849274) / 2026-09-20 02:58:30 +0800 | 24.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35462902445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462902445) / completed | [35462902445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462902445) / success | [35462902445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35462902445) / 2026-09-20 02:59:29 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35463815189](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35463815189) / completed | [35463815189](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35463815189) / success | [35463815189](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35463815189) / 2026-09-20 03:16:59 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35464122001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464122001) / completed | [35464122001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464122001) / success | [35464122001](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35464122001) / 2026-09-20 03:23:16 +0800 | 23.6h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35473135337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473135337) / completed | [35473135337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473135337) / success | [35473135337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473135337) / 2026-09-20 06:22:53 +0800 | 20.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / completed | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / success | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / 2026-09-14 03:43:57 +0800 | 167.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1055.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35473168301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473168301) / completed | [35473168301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473168301) / success | [35473168301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473168301) / 2026-09-20 06:23:22 +0800 | 20.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35473190860](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473190860) / completed | [35473190860](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473190860) / success | [35473190860](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473190860) / 2026-09-20 06:23:30 +0800 | 20.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
