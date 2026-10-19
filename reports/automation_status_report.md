# Automation Status Report

- Generated at: 2026-10-20 07:50:01 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `f13d0767`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39325710998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325710998) / completed | [39325710998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325710998) / success | [39325710998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325710998) / 2026-10-20 05:14:21 +0800 | 2.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [39325843121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325843121) / completed | [39325843121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325843121) / success | [39325843121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39325843121) / 2026-10-20 05:14:47 +0800 | 2.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39326074481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326074481) / completed | [39326074481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326074481) / success | [39326074481](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326074481) / 2026-10-20 05:16:09 +0800 | 2.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39326136031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326136031) / completed | [39326136031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326136031) / success | [39326136031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39326136031) / 2026-10-20 05:16:35 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39327178186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39327178186) / completed | [39327178186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39327178186) / success | [39327178186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39327178186) / 2026-10-20 05:24:59 +0800 | 2.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39328611521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39328611521) / completed | [39328611521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39328611521) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 433.9h | last success is stale (433.9h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39343947631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39343947631) / in_progress | [39172478135](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39172478135) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 431.8h | last success is stale (431.8h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 28.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 26.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39172527389](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39172527389) / completed | [39172527389](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39172527389) / success | [39172527389](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39172527389) / 2026-10-19 06:30:41 +0800 | 25.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39328867673](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39328867673) / completed | [39328867673](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39328867673) / success | [39328867673](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39328867673) / 2026-10-20 05:37:03 +0800 | 2.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
