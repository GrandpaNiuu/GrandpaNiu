# Automation Status Report

- Generated at: 2026-11-01 07:31:16 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `585637cb`
- Overall status: `fail`
- Blocking findings: 3
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [41238036559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238036559) / completed | [41238036559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238036559) / success | [41238036559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238036559) / 2026-11-01 04:16:36 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [41238161883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238161883) / completed | [41238161883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238161883) / success | [41238161883](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238161883) / 2026-11-01 04:17:24 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [41238311614](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238311614) / completed | [41238311614](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238311614) / success | [41238311614](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238311614) / 2026-11-01 04:19:22 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [41238348866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238348866) / completed | [41238348866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238348866) / success | [41238348866](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238348866) / 2026-11-01 04:19:38 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [41238826261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238826261) / completed | [41238826261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238826261) / success | [41238826261](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41238826261) / 2026-11-01 04:26:05 +0800 | 3.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [41239081260](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41239081260) / completed | [41239081260](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41239081260) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 25.9h | latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [41252846521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41252846521) / in_progress | [41147286206](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41147286206) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 147.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 314.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [41147359804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41147359804) / completed | [41147359804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41147359804) / success | [41147359804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41147359804) / 2026-10-31 07:56:23 +0800 | 23.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [41239181203](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41239181203) / completed | [41239181203](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41239181203) / success | [41239181203](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41239181203) / 2026-11-01 04:30:17 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
