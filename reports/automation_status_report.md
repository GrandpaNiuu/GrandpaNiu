# Automation Status Report

- Generated at: 2026-11-13 06:26:26 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `761a6ed0`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [43319774270](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319774270) / in_progress | [43116242805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43116242805) / success | [43116242805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43116242805) / 2026-11-12 07:00:39 +0800 | 23.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [43319868210](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319868210) / in_progress | [43116552544](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43116552544) / success | [43116552544](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43116552544) / 2026-11-12 07:02:13 +0800 | 23.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [43117208448](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43117208448) / completed | [43117208448](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43117208448) / success | [43117208448](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43117208448) / 2026-11-12 07:07:00 +0800 | 23.3h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [43117318577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43117318577) / completed | [43117318577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43117318577) / success | [43117318577](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43117318577) / 2026-11-12 07:07:36 +0800 | 23.3h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [43119502219](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43119502219) / completed | [43119502219](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43119502219) / success | [43119502219](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43119502219) / 2026-11-12 07:24:42 +0800 | 23.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [43120253256](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43120253256) / completed | [43120253256](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43120253256) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 312.8h | last success is stale (312.8h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [43137972889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43137972889) / completed | [43137972889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43137972889) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / completed | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / success | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / 2026-11-09 05:21:23 +0800 | 97.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 600.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [43138051802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138051802) / completed | [43138051802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138051802) / success | [43138051802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138051802) / 2026-11-12 09:57:50 +0800 | 20.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [43138071896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138071896) / completed | [43138071896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138071896) / success | [43138071896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138071896) / 2026-11-12 09:58:01 +0800 | 20.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
