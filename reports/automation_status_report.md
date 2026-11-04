# Automation Status Report

- Generated at: 2026-11-04 08:44:14 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `95d9a632`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [41726303561](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41726303561) / completed | [41726303561](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41726303561) / success | [41726303561](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41726303561) / 2026-11-04 05:58:05 +0800 | 2.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [41726588472](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41726588472) / completed | [41726588472](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41726588472) / success | [41726588472](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41726588472) / 2026-11-04 05:59:17 +0800 | 2.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [41727326343](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41727326343) / completed | [41727326343](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41727326343) / success | [41727326343](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41727326343) / 2026-11-04 06:04:09 +0800 | 2.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [41727388697](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41727388697) / completed | [41727388697](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41727388697) / success | [41727388697](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41727388697) / 2026-11-04 06:04:34 +0800 | 2.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [41729155605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41729155605) / completed | [41729155605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41729155605) / success | [41729155605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41729155605) / 2026-11-04 06:16:18 +0800 | 2.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [41730039295](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41730039295) / completed | [41730039295](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41730039295) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 99.1h | last success is stale (99.1h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [41748989472](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41748989472) / in_progress | [41566462099](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566462099) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / completed | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / success | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / 2026-11-02 05:22:24 +0800 | 51.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 387.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [41566544355](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566544355) / completed | [41566544355](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566544355) / success | [41566544355](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41566544355) / 2026-11-03 10:30:50 +0800 | 22.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [41730273788](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41730273788) / completed | [41730273788](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41730273788) / success | [41730273788](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41730273788) / 2026-11-04 06:23:00 +0800 | 2.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
