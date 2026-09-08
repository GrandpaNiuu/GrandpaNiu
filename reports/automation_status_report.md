# Automation Status Report

- Generated at: 2026-09-09 06:50:06 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `b6b0110e`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34269602332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269602332) / completed | [34269602332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269602332) / success | [34269602332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269602332) / 2026-09-09 03:34:18 +0800 | 3.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34269705606](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269705606) / completed | [34269705606](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269705606) / success | [34269705606](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269705606) / 2026-09-09 03:34:49 +0800 | 3.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34269980689](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269980689) / completed | [34269980689](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269980689) / success | [34269980689](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269980689) / 2026-09-09 03:37:27 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34269997007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269997007) / completed | [34269997007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269997007) / success | [34269997007](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269997007) / 2026-09-09 03:37:40 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34271233912](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34271233912) / completed | [34271233912](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34271233912) / success | [34271233912](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34271233912) / 2026-09-09 03:50:43 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34271850808](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34271850808) / completed | [34271850808](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34271850808) / success | [34271850808](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34271850808) / 2026-09-09 03:58:14 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34287812368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287812368) / in_progress | [34168302025](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168302025) / success | [34168302025](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168302025) / 2026-09-08 06:56:10 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / completed | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 51.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 771.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34168342504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168342504) / completed | [34168342504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168342504) / success | [34168342504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168342504) / 2026-09-08 06:56:42 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34272044192](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34272044192) / completed | [34272044192](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34272044192) / success | [34272044192](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34272044192) / 2026-09-09 03:58:25 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
