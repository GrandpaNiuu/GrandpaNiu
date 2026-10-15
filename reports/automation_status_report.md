# Automation Status Report

- Generated at: 2026-10-16 07:09:14 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `5d919f4d`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [38798439517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798439517) / completed | [38798439517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798439517) / success | [38798439517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798439517) / 2026-10-16 04:01:51 +0800 | 3.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [38798528579](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798528579) / completed | [38798528579](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798528579) / success | [38798528579](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798528579) / 2026-10-16 04:02:03 +0800 | 3.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [38798856017](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798856017) / completed | [38798856017](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798856017) / success | [38798856017](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798856017) / 2026-10-16 04:04:04 +0800 | 3.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [38798938339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798938339) / completed | [38798938339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798938339) / success | [38798938339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38798938339) / 2026-10-16 04:04:28 +0800 | 3.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [38800377827](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38800377827) / completed | [38800377827](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38800377827) / success | [38800377827](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38800377827) / 2026-10-16 04:15:47 +0800 | 2.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [38801467746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38801467746) / completed | [38801467746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38801467746) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 337.3h | last success is stale (337.3h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [38821779717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38821779717) / in_progress | [38653403801](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38653403801) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 335.1h | last success is stale (335.1h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / completed | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / success | [38174715037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38174715037) / 2026-10-12 05:03:52 +0800 | 98.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1660.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [38653491251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38653491251) / completed | [38653491251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38653491251) / success | [38653491251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38653491251) / 2026-10-15 07:20:55 +0800 | 23.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [38801744853](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38801744853) / completed | [38801744853](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38801744853) / success | [38801744853](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/38801744853) / 2026-10-16 04:25:06 +0800 | 2.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
