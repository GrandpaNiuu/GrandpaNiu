# Automation Status Report

- Generated at: 2026-10-31 05:01:05 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `d84b3a03`
- Overall status: `fail`
- Blocking findings: 2
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [41127594080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41127594080) / in_progress | [40957324434](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957324434) / success | [40957324434](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957324434) / 2026-10-30 05:24:20 +0800 | 23.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40957548686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957548686) / completed | [40957548686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957548686) / success | [40957548686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957548686) / 2026-10-30 05:25:12 +0800 | 23.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40957890243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957890243) / completed | [40957890243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957890243) / success | [40957890243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957890243) / 2026-10-30 05:27:30 +0800 | 23.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40957921584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957921584) / completed | [40957921584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957921584) / success | [40957921584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957921584) / 2026-10-30 05:27:40 +0800 | 23.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40960112625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40960112625) / completed | [40960112625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40960112625) / success | [40960112625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40960112625) / 2026-10-30 05:43:43 +0800 | 23.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [40961208645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961208645) / completed | [40961208645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961208645) / success | [40961208645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961208645) / 2026-10-30 05:52:58 +0800 | 23.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40976956919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40976956919) / completed | [40976956919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40976956919) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 121.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 287.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40977046261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977046261) / completed | [40977046261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977046261) / success | [40977046261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977046261) / 2026-10-30 08:02:04 +0800 | 21.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40977065361](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977065361) / completed | [40977065361](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977065361) / success | [40977065361](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40977065361) / 2026-10-30 08:02:13 +0800 | 21.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
