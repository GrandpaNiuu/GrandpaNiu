# Automation Status Report

- Generated at: 2026-07-16 04:03:06 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `47e38b10`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29438118649](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438118649) / completed | [29438118649](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438118649) / success | [29438118649](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438118649) / 2026-07-16 01:51:35 +0800 | 2.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29438212834](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438212834) / completed | [29438212834](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438212834) / success | [29438212834](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438212834) / 2026-07-16 01:52:14 +0800 | 2.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29438599956](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438599956) / completed | [29438599956](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438599956) / success | [29438599956](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438599956) / 2026-07-16 01:57:48 +0800 | 2.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29438669170](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438669170) / completed | [29438669170](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438669170) / success | [29438669170](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29438669170) / 2026-07-16 01:59:06 +0800 | 2.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29439705803](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29439705803) / completed | [29439705803](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29439705803) / success | [29439705803](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29439705803) / 2026-07-16 02:14:40 +0800 | 1.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29441039684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29441039684) / completed | [29441039684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29441039684) / success | [29441039684](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29441039684) / 2026-07-16 02:35:10 +0800 | 1.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29369660755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369660755) / completed | [29369660755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369660755) / success | [29369660755](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29369660755) / 2026-07-15 05:29:09 +0800 | 22.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / completed | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / success | [29203998652](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29203998652) / 2026-07-13 02:31:34 +0800 | 73.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / in_progress | [29442515323](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29442515323) / success | [29442515323](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29442515323) / 2026-07-16 02:56:55 +0800 | 1.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29442610625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29442610625) / completed | [29442610625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29442610625) / success | [29442610625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29442610625) / 2026-07-16 02:57:29 +0800 | 1.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29442645332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29442645332) / completed | [29442645332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29442645332) / success | [29442645332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29442645332) / 2026-07-16 02:57:41 +0800 | 1.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
