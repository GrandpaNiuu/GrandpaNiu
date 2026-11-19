# Automation Status Report

- Generated at: 2026-11-19 09:56:04 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `c7ed78d5`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [44417527780](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44417527780) / completed | [44417527780](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44417527780) / success | [44417527780](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44417527780) / 2026-11-19 07:05:54 +0800 | 2.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [44417757685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44417757685) / completed | [44417757685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44417757685) / success | [44417757685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44417757685) / 2026-11-19 07:06:40 +0800 | 2.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [44418191114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44418191114) / completed | [44418191114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44418191114) / success | [44418191114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44418191114) / 2026-11-19 07:09:42 +0800 | 2.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [44418243597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44418243597) / completed | [44418243597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44418243597) / success | [44418243597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44418243597) / 2026-11-19 07:10:00 +0800 | 2.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [44419841527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44419841527) / completed | [44419841527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44419841527) / success | [44419841527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44419841527) / 2026-11-19 07:20:55 +0800 | 2.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [44420563811](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44420563811) / completed | [44420563811](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44420563811) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 460.3h | last success is stale (460.3h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [44440542422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44440542422) / in_progress | [44223601486](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223601486) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / completed | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / success | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / 2026-11-16 06:02:31 +0800 | 75.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 748.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [44223690124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223690124) / completed | [44223690124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223690124) / success | [44223690124](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44223690124) / 2026-11-18 10:30:04 +0800 | 23.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [44420720931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44420720931) / completed | [44420720931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44420720931) / success | [44420720931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44420720931) / 2026-11-19 07:26:17 +0800 | 2.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
