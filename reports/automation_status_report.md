# Automation Status Report

- Generated at: 2026-10-09 05:29:05 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `7f818832`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37846975775](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37846975775) / in_progress | [37690010487](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690010487) / success | [37690010487](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690010487) / 2026-10-08 05:32:55 +0800 | 23.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37690140010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690140010) / completed | [37690140010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690140010) / success | [37690140010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690140010) / 2026-10-08 05:33:16 +0800 | 23.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37690764735](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690764735) / completed | [37690764735](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690764735) / success | [37690764735](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690764735) / 2026-10-08 05:38:31 +0800 | 23.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37690788533](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690788533) / completed | [37690788533](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690788533) / success | [37690788533](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37690788533) / 2026-10-08 05:39:10 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37692621725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37692621725) / completed | [37692621725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37692621725) / success | [37692621725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37692621725) / 2026-10-08 05:55:13 +0800 | 23.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37693674855](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37693674855) / completed | [37693674855](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37693674855) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 167.6h | last success is stale (167.6h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [37706949812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37706949812) / completed | [37706949812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37706949812) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 165.5h | last success is stale (165.5h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 97.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1490.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [37707014129](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707014129) / completed | [37707014129](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707014129) / success | [37707014129](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707014129) / 2026-10-08 08:18:00 +0800 | 21.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37707027319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707027319) / completed | [37707027319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707027319) / success | [37707027319](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707027319) / 2026-10-08 08:18:10 +0800 | 21.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
