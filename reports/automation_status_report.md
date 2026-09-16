# Automation Status Report

- Generated at: 2026-09-17 03:41:41 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `6d047665`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35141958145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35141958145) / in_progress | [35015769901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35015769901) / success | [35015769901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35015769901) / 2026-09-16 03:49:17 +0800 | 23.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35142010548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142010548) / in_progress | [35015837165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35015837165) / success | [35015837165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35015837165) / 2026-09-16 03:49:39 +0800 | 23.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35016052882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35016052882) / completed | [35016052882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35016052882) / success | [35016052882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35016052882) / 2026-09-16 03:51:20 +0800 | 23.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35016119553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35016119553) / completed | [35016119553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35016119553) / success | [35016119553](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35016119553) / 2026-09-16 03:51:57 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35017673886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35017673886) / completed | [35017673886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35017673886) / success | [35017673886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35017673886) / 2026-09-16 04:08:01 +0800 | 23.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35018626815](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35018626815) / completed | [35018626815](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35018626815) / success | [35018626815](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35018626815) / 2026-09-16 04:18:41 +0800 | 23.4h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35033635473](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033635473) / completed | [35033635473](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033635473) / success | [35033635473](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033635473) / 2026-09-16 07:00:46 +0800 | 20.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / completed | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / success | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / 2026-09-14 03:43:57 +0800 | 72.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 960.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35033714038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033714038) / completed | [35033714038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033714038) / success | [35033714038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033714038) / 2026-09-16 07:01:28 +0800 | 20.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35033765334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033765334) / completed | [35033765334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033765334) / success | [35033765334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35033765334) / 2026-09-16 07:01:38 +0800 | 20.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
