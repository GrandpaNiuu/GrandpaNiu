# Automation Status Report

- Generated at: 2026-10-21 07:16:15 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `05cc95f2`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39489100804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489100804) / completed | [39489100804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489100804) / success | [39489100804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489100804) / 2026-10-21 04:07:30 +0800 | 3.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [39489261378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489261378) / completed | [39489261378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489261378) / success | [39489261378](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489261378) / 2026-10-21 04:07:47 +0800 | 3.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39489508467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489508467) / completed | [39489508467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489508467) / success | [39489508467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489508467) / 2026-10-21 04:09:40 +0800 | 3.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39489551312](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489551312) / completed | [39489551312](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489551312) / success | [39489551312](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489551312) / 2026-10-21 04:09:58 +0800 | 3.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39491828615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39491828615) / completed | [39491828615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39491828615) / success | [39491828615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39491828615) / 2026-10-21 04:26:10 +0800 | 2.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39493984580](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39493984580) / completed | [39493984580](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39493984580) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 457.4h | last success is stale (457.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39513857099](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39513857099) / in_progress | [39343947631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39343947631) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 51.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 49.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39344028717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344028717) / completed | [39344028717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344028717) / success | [39344028717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344028717) / 2026-10-20 07:50:33 +0800 | 23.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39494224200](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39494224200) / completed | [39494224200](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39494224200) / success | [39494224200](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39494224200) / 2026-10-21 04:42:19 +0800 | 2.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
