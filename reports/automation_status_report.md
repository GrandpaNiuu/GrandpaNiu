# Automation Status Report

- Generated at: 2026-10-30 08:01:27 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `8001d8e5`
- Overall status: `fail`
- Blocking findings: 2
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40957324434](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957324434) / completed | [40957324434](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957324434) / success | [40957324434](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957324434) / 2026-10-30 05:24:20 +0800 | 2.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40957548686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957548686) / completed | [40957548686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957548686) / success | [40957548686](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957548686) / 2026-10-30 05:25:12 +0800 | 2.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40957890243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957890243) / completed | [40957890243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957890243) / success | [40957890243](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957890243) / 2026-10-30 05:27:30 +0800 | 2.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40957921584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957921584) / completed | [40957921584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957921584) / success | [40957921584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40957921584) / 2026-10-30 05:27:40 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40960112625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40960112625) / completed | [40960112625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40960112625) / success | [40960112625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40960112625) / 2026-10-30 05:43:43 +0800 | 2.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [40961208645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961208645) / completed | [40961208645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961208645) / success | [40961208645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961208645) / 2026-10-30 05:52:58 +0800 | 2.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40976956919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40976956919) / in_progress | [40791959388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40791959388) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 100.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 266.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40792040889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792040889) / completed | [40792040889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792040889) / success | [40792040889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40792040889) / 2026-10-29 08:08:19 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40961453788](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961453788) / completed | [40961453788](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961453788) / success | [40961453788](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40961453788) / 2026-10-30 05:53:09 +0800 | 2.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
