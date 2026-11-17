# Automation Status Report

- Generated at: 2026-11-17 11:01:06 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `f25ebdbf`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [43987709154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43987709154) / completed | [43987709154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43987709154) / success | [43987709154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43987709154) / 2026-11-17 08:28:27 +0800 | 2.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [43987809117](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43987809117) / completed | [43987809117](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43987809117) / success | [43987809117](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43987809117) / 2026-11-17 08:28:50 +0800 | 2.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [43988124420](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43988124420) / completed | [43988124420](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43988124420) / success | [43988124420](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43988124420) / 2026-11-17 08:30:41 +0800 | 2.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [43988158154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43988158154) / completed | [43988158154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43988158154) / success | [43988158154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43988158154) / 2026-11-17 08:31:04 +0800 | 2.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [43989865464](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43989865464) / completed | [43989865464](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43989865464) / success | [43989865464](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43989865464) / 2026-11-17 08:43:47 +0800 | 2.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [43990958104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43990958104) / completed | [43990958104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43990958104) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 413.4h | last success is stale (413.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [44007086022](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44007086022) / in_progress | [43778357363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778357363) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / completed | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / success | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / 2026-11-16 06:02:31 +0800 | 29.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 701.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [43778437861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778437861) / completed | [43778437861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778437861) / success | [43778437861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43778437861) / 2026-11-16 08:07:06 +0800 | 26.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [43991196298](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43991196298) / completed | [43991196298](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43991196298) / success | [43991196298](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43991196298) / 2026-11-17 08:53:05 +0800 | 2.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
