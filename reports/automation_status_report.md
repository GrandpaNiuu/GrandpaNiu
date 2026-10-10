# Automation Status Report

- Generated at: 2026-10-11 04:18:49 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `53572917`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [38083183703](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083183703) / in_progress | [37992003387](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992003387) / success | [37992003387](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992003387) / 2026-10-10 05:13:59 +0800 | 23.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38083247699](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38083247699) / queued | [37992208889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992208889) / success | [37992208889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992208889) / 2026-10-10 05:14:55 +0800 | 23.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37992785411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992785411) / completed | [37992785411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992785411) / success | [37992785411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992785411) / 2026-10-10 05:20:21 +0800 | 23.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37992834374](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992834374) / completed | [37992834374](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992834374) / success | [37992834374](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37992834374) / 2026-10-10 05:20:54 +0800 | 23.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37994179037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37994179037) / completed | [37994179037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37994179037) / success | [37994179037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37994179037) / 2026-10-10 05:34:25 +0800 | 22.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37995324444](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37995324444) / completed | [37995324444](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37995324444) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 214.4h | last success is stale (214.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38007790807](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007790807) / completed | [38007790807](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007790807) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 212.3h | last success is stale (212.3h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 143.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1537.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38007850330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007850330) / completed | [38007850330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007850330) / success | [38007850330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007850330) / 2026-10-10 08:10:11 +0800 | 20.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38007863612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007863612) / completed | [38007863612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007863612) / success | [38007863612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38007863612) / 2026-10-10 08:10:19 +0800 | 20.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
