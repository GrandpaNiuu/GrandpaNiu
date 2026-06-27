# Automation Status Report

- Generated at: 2026-06-28 05:36:14 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28296843049](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296843049) / completed | [28296843049](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296843049) / success | [28296843049](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296843049) / 2026-06-28 01:42:31 +0800 | 3.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28296878558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296878558) / completed | [28296878558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296878558) / success | [28296878558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296878558) / 2026-06-28 01:43:29 +0800 | 3.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28296980944](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296980944) / completed | [28296980944](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296980944) / success | [28296980944](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28296980944) / 2026-06-28 01:48:05 +0800 | 3.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28297012381](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28297012381) / completed | [28297012381](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28297012381) / success | [28297012381](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28297012381) / 2026-06-28 01:49:14 +0800 | 3.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28297565779](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28297565779) / completed | [28297565779](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28297565779) / success | [28297565779](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28297565779) / 2026-06-28 02:12:12 +0800 | 3.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28298185774](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28298185774) / completed | [28298185774](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28298185774) / success | [28298185774](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28298185774) / 2026-06-28 02:38:12 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [28302500730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28302500730) / in_progress | [28267082545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267082545) / success | [28267082545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28267082545) / 2026-06-27 05:46:30 +0800 | 23.8h | latest run is in_progress |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / completed | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / success | [27914441205](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27914441205) / 2026-06-22 03:04:56 +0800 | 146.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / completed | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / success | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / 2026-06-26 22:24:31 +0800 | 31.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28298208318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28298208318) / completed | [28298208318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28298208318) / success | [28298208318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28298208318) / 2026-06-28 02:38:22 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
