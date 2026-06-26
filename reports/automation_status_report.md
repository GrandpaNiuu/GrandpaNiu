# Automation Status Report

- Generated at: 2026-06-27 05:46:18 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28256762246](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256762246) / completed | [28256762246](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256762246) / success | [28256762246](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256762246) / 2026-06-27 02:14:35 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28256836282](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256836282) / completed | [28256836282](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256836282) / success | [28256836282](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256836282) / 2026-06-27 02:15:39 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28256962905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256962905) / completed | [28256962905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256962905) / success | [28256962905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256962905) / 2026-06-27 02:18:06 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28256979577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256979577) / completed | [28256979577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256979577) / success | [28256979577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28256979577) / 2026-06-27 02:18:22 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28258976440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28258976440) / completed | [28258976440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28258976440) / success | [28258976440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28258976440) / 2026-06-27 02:57:36 +0800 | 2.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28259626176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259626176) / completed | [28259626176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259626176) / success | [28259626176](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259626176) / 2026-06-27 03:11:00 +0800 | 2.6h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [28267082545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267082545) / in_progress | [28203104967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) / success | [28203104967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28203104967) / 2026-06-26 05:58:37 +0800 | 23.8h | latest run is in_progress |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / completed | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / success | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / 2026-06-22 03:04:56 +0800 | 122.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / completed | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / success | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / 2026-06-26 22:24:31 +0800 | 7.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28259679321](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259679321) / completed | [28259679321](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259679321) / success | [28259679321](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28259679321) / 2026-06-27 03:11:14 +0800 | 2.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
