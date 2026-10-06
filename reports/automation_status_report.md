# Automation Status Report

- Generated at: 2026-10-07 05:12:44 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `1bdfcfe5`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37532096335](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37532096335) / in_progress | [37385241919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385241919) / success | [37385241919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385241919) / 2026-10-06 06:54:28 +0800 | 22.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37385317341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385317341) / completed | [37385317341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385317341) / success | [37385317341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385317341) / 2026-10-06 06:54:52 +0800 | 22.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37385510015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385510015) / completed | [37385510015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385510015) / success | [37385510015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385510015) / 2026-10-06 06:56:26 +0800 | 22.3h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37385543051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385543051) / completed | [37385543051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385543051) / success | [37385543051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385543051) / 2026-10-06 06:56:45 +0800 | 22.3h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37386546527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37386546527) / completed | [37386546527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37386546527) / success | [37386546527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37386546527) / 2026-10-06 07:07:14 +0800 | 22.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37387103694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37387103694) / completed | [37387103694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37387103694) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 119.3h | last success is stale (119.3h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [37398717919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398717919) / completed | [37398717919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398717919) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 117.2h | last success is stale (117.2h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 48.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1442.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [37398775306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398775306) / completed | [37398775306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398775306) / success | [37398775306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398775306) / 2026-10-06 09:21:58 +0800 | 19.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37398788963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398788963) / completed | [37398788963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398788963) / success | [37398788963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398788963) / 2026-10-06 09:22:11 +0800 | 19.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
