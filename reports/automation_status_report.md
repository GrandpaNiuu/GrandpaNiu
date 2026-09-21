# Automation Status Report

- Generated at: 2026-09-22 07:26:54 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `54ccf60a`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35651652645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35651652645) / completed | [35651652645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35651652645) / success | [35651652645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35651652645) / 2026-09-22 04:33:18 +0800 | 2.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35651871965](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35651871965) / completed | [35651871965](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35651871965) / success | [35651871965](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35651871965) / 2026-09-22 04:34:42 +0800 | 2.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35652369326](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35652369326) / completed | [35652369326](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35652369326) / success | [35652369326](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35652369326) / 2026-09-22 04:39:25 +0800 | 2.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35652472525](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35652472525) / completed | [35652472525](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35652472525) / success | [35652472525](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35652472525) / 2026-09-22 04:40:17 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35654184100](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35654184100) / completed | [35654184100](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35654184100) / success | [35654184100](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35654184100) / 2026-09-22 04:57:13 +0800 | 2.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35655295469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35655295469) / completed | [35655295469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35655295469) / success | [35655295469](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35655295469) / 2026-09-22 05:09:12 +0800 | 2.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35667570590](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35667570590) / in_progress | [35542119116](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35542119116) / success | [35542119116](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35542119116) / 2026-09-21 06:35:36 +0800 | 24.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / completed | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 27.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1084.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35542164410](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35542164410) / completed | [35542164410](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35542164410) / success | [35542164410](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35542164410) / 2026-09-21 06:36:06 +0800 | 24.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35655475975](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35655475975) / completed | [35655475975](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35655475975) / success | [35655475975](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35655475975) / 2026-09-22 05:09:22 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
