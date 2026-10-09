# Automation Status Report

- Generated at: 2026-10-09 08:31:16 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `a47af8ea`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37846975775](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37846975775) / completed | [37846975775](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37846975775) / success | [37846975775](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37846975775) / 2026-10-09 05:29:28 +0800 | 3.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37847097727](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847097727) / completed | [37847097727](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847097727) / success | [37847097727](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847097727) / 2026-10-09 05:29:53 +0800 | 3.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37847562936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847562936) / completed | [37847562936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847562936) / success | [37847562936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847562936) / 2026-10-09 05:33:32 +0800 | 3.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37847656608](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847656608) / completed | [37847656608](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847656608) / success | [37847656608](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37847656608) / 2026-10-09 05:34:18 +0800 | 2.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37850394890](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37850394890) / completed | [37850394890](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37850394890) / success | [37850394890](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37850394890) / 2026-10-09 05:58:56 +0800 | 2.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37851787746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37851787746) / completed | [37851787746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37851787746) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 170.6h | last success is stale (170.6h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [37865174275](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37865174275) / in_progress | [37706949812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37706949812) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 168.5h | last success is stale (168.5h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 100.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1493.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [37707014129](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707014129) / completed | [37707014129](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707014129) / success | [37707014129](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37707014129) / 2026-10-08 08:18:00 +0800 | 24.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37851974142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37851974142) / completed | [37851974142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37851974142) / success | [37851974142](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37851974142) / 2026-10-09 06:12:35 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
