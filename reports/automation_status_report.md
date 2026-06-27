# Automation Status Report

- Generated at: 2026-06-28 01:42:17 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [28296843049](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296843049) / in_progress | [28256762246](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256762246) / success | [28256762246](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256762246) / 2026-06-27 02:14:35 +0800 | 23.5h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28256836282](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256836282) / completed | [28256836282](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256836282) / success | [28256836282](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256836282) / 2026-06-27 02:15:39 +0800 | 23.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28256962905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256962905) / completed | [28256962905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256962905) / success | [28256962905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256962905) / 2026-06-27 02:18:06 +0800 | 23.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28256979577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256979577) / completed | [28256979577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256979577) / success | [28256979577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256979577) / 2026-06-27 02:18:22 +0800 | 23.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28258976440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28258976440) / completed | [28258976440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28258976440) / success | [28258976440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28258976440) / 2026-06-27 02:57:36 +0800 | 22.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28259626176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259626176) / completed | [28259626176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259626176) / success | [28259626176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259626176) / 2026-06-27 03:11:00 +0800 | 22.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28267082545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267082545) / completed | [28267082545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267082545) / success | [28267082545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267082545) / 2026-06-27 05:46:30 +0800 | 19.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / completed | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / success | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / 2026-06-22 03:04:56 +0800 | 142.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / completed | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / success | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / 2026-06-26 22:24:31 +0800 | 27.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28267097789](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267097789) / completed | [28267097789](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267097789) / success | [28267097789](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267097789) / 2026-06-27 05:46:43 +0800 | 19.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
