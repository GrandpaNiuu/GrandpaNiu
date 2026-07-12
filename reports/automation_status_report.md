# Automation Status Report

- Generated at: 2026-07-13 01:39:31 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `9c431ccc`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [29202375935](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29202375935) / in_progress | [29161901292](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29161901292) / success | [29161901292](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29161901292) / 2026-07-12 01:37:21 +0800 | 24.0h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29161978793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29161978793) / completed | [29161978793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29161978793) / success | [29161978793](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29161978793) / 2026-07-12 01:38:54 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29162077227](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162077227) / completed | [29162077227](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162077227) / success | [29162077227](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162077227) / 2026-07-12 01:42:28 +0800 | 24.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29162074721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162074721) / completed | [29162074721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162074721) / success | [29162074721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162074721) / 2026-07-12 01:41:55 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29162608775](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162608775) / completed | [29162608775](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162608775) / success | [29162608775](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162608775) / 2026-07-12 01:59:48 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29162955905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162955905) / completed | [29162955905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162955905) / success | [29162955905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29162955905) / 2026-07-12 02:11:54 +0800 | 23.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29168396768](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168396768) / completed | [29168396768](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168396768) / success | [29168396768](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168396768) / 2026-07-12 05:13:03 +0800 | 20.4h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 167.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 70.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29168411983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411983) / completed | [29168411983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411983) / success | [29168411983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411983) / 2026-07-12 05:13:42 +0800 | 20.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29168411981](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411981) / completed | [29168411981](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411981) / success | [29168411981](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29168411981) / 2026-07-12 05:13:12 +0800 | 20.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
