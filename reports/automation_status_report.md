# Automation Status Report

- Generated at: 2026-11-13 09:17:48 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `0d7e1d2b`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [43319774270](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319774270) / completed | [43319774270](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319774270) / success | [43319774270](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319774270) / 2026-11-13 06:26:43 +0800 | 2.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [43319868210](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319868210) / completed | [43319868210](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319868210) / success | [43319868210](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43319868210) / 2026-11-13 06:27:00 +0800 | 2.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [43320031068](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43320031068) / completed | [43320031068](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43320031068) / success | [43320031068](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43320031068) / 2026-11-13 06:27:53 +0800 | 2.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [43320059171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43320059171) / completed | [43320059171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43320059171) / success | [43320059171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43320059171) / 2026-11-13 06:28:14 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [43321930404](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43321930404) / completed | [43321930404](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43321930404) / success | [43321930404](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43321930404) / 2026-11-13 06:40:23 +0800 | 2.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [43322828984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43322828984) / completed | [43322828984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43322828984) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 315.7h | last success is stale (315.7h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [43343788179](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43343788179) / in_progress | [43137972889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43137972889) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / completed | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / success | [42524647818](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/42524647818) / 2026-11-09 05:21:23 +0800 | 99.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 603.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [43138051802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138051802) / completed | [43138051802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138051802) / success | [43138051802](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43138051802) / 2026-11-12 09:57:50 +0800 | 23.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [43323028474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43323028474) / completed | [43323028474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43323028474) / success | [43323028474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43323028474) / 2026-11-13 06:46:55 +0800 | 2.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
