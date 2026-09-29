# Automation Status Report

- Generated at: 2026-09-30 07:51:02 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `60e6b04f`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36630274790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630274790) / completed | [36630274790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630274790) / success | [36630274790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630274790) / 2026-09-30 05:01:29 +0800 | 2.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36630411165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630411165) / completed | [36630411165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630411165) / success | [36630411165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630411165) / 2026-09-30 05:01:54 +0800 | 2.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36630783609](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630783609) / completed | [36630783609](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630783609) / success | [36630783609](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630783609) / 2026-09-30 05:04:52 +0800 | 2.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36630838481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630838481) / completed | [36630838481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630838481) / success | [36630838481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36630838481) / 2026-09-30 05:05:21 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36632522405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36632522405) / completed | [36632522405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36632522405) / success | [36632522405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36632522405) / 2026-09-30 05:20:50 +0800 | 2.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36633271127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633271127) / completed | [36633271127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633271127) / success | [36633271127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633271127) / 2026-09-30 05:28:18 +0800 | 2.4h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36647320881](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647320881) / in_progress | [36503173687](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36503173687) / success | [36503173687](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36503173687) / 2026-09-29 08:28:06 +0800 | 23.4h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / completed | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / success | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / 2026-09-28 04:21:38 +0800 | 51.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1276.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36503238360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36503238360) / completed | [36503238360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36503238360) / success | [36503238360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36503238360) / 2026-09-29 08:28:38 +0800 | 23.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36633483358](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633483358) / completed | [36633483358](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633483358) / success | [36633483358](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36633483358) / 2026-09-30 05:28:28 +0800 | 2.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
