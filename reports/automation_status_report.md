# Automation Status Report

- Generated at: 2026-11-28 10:51:43 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `072f8324`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [46086626248](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086626248) / completed | [46086626248](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086626248) / success | [46086626248](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086626248) / 2026-11-28 08:13:34 +0800 | 2.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [46086754577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086754577) / completed | [46086754577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086754577) / success | [46086754577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086754577) / 2026-11-28 08:14:20 +0800 | 2.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [46086931002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086931002) / completed | [46086931002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086931002) / success | [46086931002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086931002) / 2026-11-28 08:16:20 +0800 | 2.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [46086941858](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086941858) / completed | [46086941858](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086941858) / success | [46086941858](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46086941858) / 2026-11-28 08:16:35 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [46087863495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46087863495) / completed | [46087863495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46087863495) / success | [46087863495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46087863495) / 2026-11-28 08:26:51 +0800 | 2.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [46088589048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46088589048) / completed | [46088589048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46088589048) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [46100072116](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46100072116) / in_progress | [45931548892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45931548892) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / completed | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / success | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / 2026-11-23 06:45:10 +0800 | 124.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 965.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [45931624292](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45931624292) / completed | [45931624292](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45931624292) / success | [45931624292](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45931624292) / 2026-11-27 11:00:43 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [46088696954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46088696954) / completed | [46088696954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46088696954) / success | [46088696954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/46088696954) / 2026-11-28 08:35:36 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
