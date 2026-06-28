# Automation Status Report

- Generated at: 2026-06-29 05:36:06 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28330749125](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330749125) / completed | [28330749125](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330749125) / success | [28330749125](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330749125) / 2026-06-29 01:48:32 +0800 | 3.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28330770006](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330770006) / completed | [28330770006](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330770006) / success | [28330770006](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330770006) / 2026-06-29 01:49:01 +0800 | 3.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28330872759](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330872759) / completed | [28330872759](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330872759) / success | [28330872759](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330872759) / 2026-06-29 01:52:50 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28330906454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330906454) / completed | [28330906454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330906454) / success | [28330906454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28330906454) / 2026-06-29 01:53:56 +0800 | 3.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28331399161](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28331399161) / completed | [28331399161](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28331399161) / success | [28331399161](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28331399161) / 2026-06-29 02:12:15 +0800 | 3.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28332082716](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332082716) / completed | [28332082716](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332082716) / success | [28332082716](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332082716) / 2026-06-29 02:38:40 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [28336775405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28336775405) / in_progress | [28302500730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28302500730) / success | [28302500730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28302500730) / 2026-06-28 05:36:34 +0800 | 24.0h | latest run is in_progress |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 2.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / completed | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / success | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / 2026-06-26 22:24:31 +0800 | 55.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28332361626](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332361626) / completed | [28332361626](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332361626) / success | [28332361626](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332361626) / 2026-06-29 02:48:13 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
