# Automation Status Report

- Generated at: 2026-07-19 05:11:55 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `9465a4a7`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29654251361](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654251361) / completed | [29654251361](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654251361) / success | [29654251361](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654251361) / 2026-07-19 01:37:48 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29654307584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654307584) / completed | [29654307584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654307584) / success | [29654307584](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654307584) / 2026-07-19 01:39:09 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29654426998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654426998) / completed | [29654426998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654426998) / success | [29654426998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654426998) / 2026-07-19 01:42:42 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29654440630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654440630) / completed | [29654440630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654440630) / success | [29654440630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29654440630) / 2026-07-19 01:42:53 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29655009605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655009605) / completed | [29655009605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655009605) / success | [29655009605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655009605) / 2026-07-19 02:00:59 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29655361504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655361504) / completed | [29655361504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655361504) / success | [29655361504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655361504) / 2026-07-19 02:12:46 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29661146939](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29661146939) / in_progress | [29613941120](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29613941120) / success | [29613941120](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29613941120) / 2026-07-18 05:13:21 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / completed | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 146.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 73.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29613975527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29613975527) / completed | [29613975527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29613975527) / success | [29613975527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29613975527) / 2026-07-18 05:13:59 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29655422158](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655422158) / completed | [29655422158](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655422158) / success | [29655422158](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29655422158) / 2026-07-19 02:12:59 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
