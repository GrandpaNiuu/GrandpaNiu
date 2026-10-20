# Automation Status Report

- Generated at: 2026-10-21 04:07:09 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `7ca8ebba`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39489100804](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39489100804) / in_progress | [39325710998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325710998) / success | [39325710998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325710998) / 2026-10-20 05:14:21 +0800 | 22.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [39325843121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325843121) / completed | [39325843121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325843121) / success | [39325843121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325843121) / 2026-10-20 05:14:47 +0800 | 22.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39326074481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326074481) / completed | [39326074481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326074481) / success | [39326074481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326074481) / 2026-10-20 05:16:09 +0800 | 22.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39326136031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326136031) / completed | [39326136031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326136031) / success | [39326136031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326136031) / 2026-10-20 05:16:35 +0800 | 22.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39327178186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39327178186) / completed | [39327178186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39327178186) / success | [39327178186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39327178186) / 2026-10-20 05:24:59 +0800 | 22.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39328611521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39328611521) / completed | [39328611521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39328611521) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 454.2h | last success is stale (454.2h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39343947631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39343947631) / completed | [39343947631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39343947631) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 452.1h | last success is stale (452.1h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 48.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 46.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39344028717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344028717) / completed | [39344028717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344028717) / success | [39344028717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344028717) / 2026-10-20 07:50:33 +0800 | 20.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39344045805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344045805) / completed | [39344045805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344045805) / success | [39344045805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39344045805) / 2026-10-20 07:50:43 +0800 | 20.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
