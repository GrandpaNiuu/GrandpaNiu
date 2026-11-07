# Automation Status Report

- Generated at: 2026-11-07 08:10:44 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `d915d570`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [42299151082](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299151082) / completed | [42299151082](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299151082) / success | [42299151082](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299151082) / 2026-11-07 05:45:45 +0800 | 2.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [42299190437](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299190437) / completed | [42299190437](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299190437) / success | [42299190437](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299190437) / 2026-11-07 05:46:10 +0800 | 2.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [42299406025](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299406025) / completed | [42299406025](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299406025) / success | [42299406025](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299406025) / 2026-11-07 05:46:33 +0800 | 2.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [42299488699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299488699) / completed | [42299488699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299488699) / success | [42299488699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42299488699) / 2026-11-07 05:47:06 +0800 | 2.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [42301160319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42301160319) / completed | [42301160319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42301160319) / success | [42301160319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42301160319) / 2026-11-07 06:00:16 +0800 | 2.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [42302510073](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42302510073) / completed | [42302510073](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42302510073) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 170.6h | last success is stale (170.6h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [42316585068](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42316585068) / in_progress | [42140796028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140796028) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / completed | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / success | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / 2026-11-02 05:22:24 +0800 | 122.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 458.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [42140901367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140901367) / completed | [42140901367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140901367) / success | [42140901367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42140901367) / 2026-11-06 09:01:04 +0800 | 23.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [42302715223](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42302715223) / completed | [42302715223](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42302715223) / success | [42302715223](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42302715223) / 2026-11-07 06:11:17 +0800 | 2.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
