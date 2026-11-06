# Automation Status Report

- Generated at: 2026-11-07 05:45:24 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `469076ee`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [42299151082](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299151082) / in_progress | [42119691370](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42119691370) / success | [42119691370](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42119691370) / 2026-11-06 06:15:05 +0800 | 23.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [42299190437](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299190437) / in_progress | [42120097425](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42120097425) / success | [42120097425](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42120097425) / 2026-11-06 06:17:21 +0800 | 23.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [42120927830](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42120927830) / completed | [42120927830](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42120927830) / success | [42120927830](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42120927830) / 2026-11-06 06:23:01 +0800 | 23.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [42121081342](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42121081342) / completed | [42121081342](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42121081342) / success | [42121081342](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42121081342) / 2026-11-06 06:23:59 +0800 | 23.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [42123150231](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42123150231) / completed | [42123150231](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42123150231) / success | [42123150231](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42123150231) / 2026-11-06 06:39:05 +0800 | 23.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [42123692055](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42123692055) / completed | [42123692055](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42123692055) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 168.2h | last success is stale (168.2h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [42140796028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140796028) / completed | [42140796028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140796028) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / completed | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / success | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / 2026-11-02 05:22:24 +0800 | 120.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 456.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [42140901367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140901367) / completed | [42140901367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140901367) / success | [42140901367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140901367) / 2026-11-06 09:01:04 +0800 | 20.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [42140923751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140923751) / completed | [42140923751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140923751) / success | [42140923751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140923751) / 2026-11-06 09:01:17 +0800 | 20.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
