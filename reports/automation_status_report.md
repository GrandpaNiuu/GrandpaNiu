# Automation Status Report

- Generated at: 2026-10-01 04:59:03 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `c48da481`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36776293251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776293251) / in_progress | [36630274790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630274790) / success | [36630274790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630274790) / 2026-09-30 05:01:29 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36630411165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630411165) / completed | [36630411165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630411165) / success | [36630411165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630411165) / 2026-09-30 05:01:54 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36630783609](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630783609) / completed | [36630783609](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630783609) / success | [36630783609](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630783609) / 2026-09-30 05:04:52 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36630838481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630838481) / completed | [36630838481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630838481) / success | [36630838481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630838481) / 2026-09-30 05:05:21 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36632522405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36632522405) / completed | [36632522405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36632522405) / success | [36632522405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36632522405) / 2026-09-30 05:20:50 +0800 | 23.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36633271127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633271127) / completed | [36633271127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633271127) / success | [36633271127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633271127) / 2026-09-30 05:28:18 +0800 | 23.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36647320881](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647320881) / completed | [36647320881](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647320881) / success | [36647320881](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647320881) / 2026-09-30 07:51:33 +0800 | 21.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / completed | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / success | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / 2026-09-28 04:21:38 +0800 | 72.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1297.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36647391730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647391730) / completed | [36647391730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647391730) / success | [36647391730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647391730) / 2026-09-30 07:52:10 +0800 | 21.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36647442937](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647442937) / completed | [36647442937](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647442937) / success | [36647442937](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647442937) / 2026-09-30 07:52:19 +0800 | 21.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
