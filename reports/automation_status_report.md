# Automation Status Report

- Generated at: 2026-10-08 08:17:22 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `31be9e43`
- Overall status: `fail`
- Blocking findings: 3
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37690010487](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690010487) / completed | [37690010487](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690010487) / success | [37690010487](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690010487) / 2026-10-08 05:32:55 +0800 | 2.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37690140010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690140010) / completed | [37690140010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690140010) / success | [37690140010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690140010) / 2026-10-08 05:33:16 +0800 | 2.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37690764735](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690764735) / completed | [37690764735](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690764735) / success | [37690764735](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690764735) / 2026-10-08 05:38:31 +0800 | 2.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37690788533](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690788533) / completed | [37690788533](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690788533) / success | [37690788533](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690788533) / 2026-10-08 05:39:10 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37692621725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37692621725) / completed | [37692621725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37692621725) / success | [37692621725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37692621725) / 2026-10-08 05:55:13 +0800 | 2.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37693674855](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37693674855) / completed | [37693674855](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37693674855) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 146.4h | last success is stale (146.4h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [34287812368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287812368) / completed | [34287812368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287812368) / success | [34287812368](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34287812368) / 2026-09-09 06:50:31 +0800 | 697.4h | last success is stale (697.4h > 48h) |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 75.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1469.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [37549305906](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37549305906) / completed | [37549305906](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37549305906) / success | [37549305906](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37549305906) / 2026-10-07 07:57:28 +0800 | 24.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37693825200](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37693825200) / completed | [37693825200](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37693825200) / success | [37693825200](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37693825200) / 2026-10-08 06:05:07 +0800 | 2.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
