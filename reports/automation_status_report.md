# Automation Status Report

- Generated at: 2026-10-11 07:41:52 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `680cdb88`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [38083183703](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083183703) / completed | [38083183703](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083183703) / success | [38083183703](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083183703) / 2026-10-11 04:19:10 +0800 | 3.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38083247699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083247699) / completed | [38083247699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083247699) / success | [38083247699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083247699) / 2026-10-11 04:19:31 +0800 | 3.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [38083328559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083328559) / completed | [38083328559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083328559) / success | [38083328559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083328559) / 2026-10-11 04:20:31 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [38083340376](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083340376) / completed | [38083340376](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083340376) / success | [38083340376](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083340376) / 2026-10-11 04:20:48 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [38084128731](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38084128731) / completed | [38084128731](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38084128731) / success | [38084128731](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38084128731) / 2026-10-11 04:32:54 +0800 | 3.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [38084322779](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38084322779) / completed | [38084322779](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38084322779) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 217.8h | last success is stale (217.8h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38095897558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38095897558) / in_progress | [38007790807](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007790807) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 215.7h | last success is stale (215.7h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 147.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1540.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38007850330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007850330) / completed | [38007850330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007850330) / success | [38007850330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007850330) / 2026-10-10 08:10:11 +0800 | 23.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38084394229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38084394229) / completed | [38084394229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38084394229) / success | [38084394229](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38084394229) / 2026-10-11 04:36:24 +0800 | 3.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
