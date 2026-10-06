# Automation Status Report

- Generated at: 2026-10-06 09:21:24 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `0b9a0b0f`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [37385241919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385241919) / completed | [37385241919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385241919) / success | [37385241919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385241919) / 2026-10-06 06:54:28 +0800 | 2.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [37385317341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385317341) / completed | [37385317341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385317341) / success | [37385317341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385317341) / 2026-10-06 06:54:52 +0800 | 2.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [37385510015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385510015) / completed | [37385510015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385510015) / success | [37385510015](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385510015) / 2026-10-06 06:56:26 +0800 | 2.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [37385543051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385543051) / completed | [37385543051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385543051) / success | [37385543051](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37385543051) / 2026-10-06 06:56:45 +0800 | 2.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [37386546527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37386546527) / completed | [37386546527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37386546527) / success | [37386546527](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37386546527) / 2026-10-06 07:07:14 +0800 | 2.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [37387103694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37387103694) / completed | [37387103694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37387103694) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 99.5h | last success is stale (99.5h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [37398717919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37398717919) / in_progress | [37243530161](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37243530161) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 97.3h | last success is stale (97.3h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / completed | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / success | [37231857038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37231857038) / 2026-10-05 04:24:24 +0800 | 29.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1422.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [37243577863](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37243577863) / completed | [37243577863](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37243577863) / success | [37243577863](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37243577863) / 2026-10-05 07:23:34 +0800 | 26.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [37387245741](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37387245741) / completed | [37387245741](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37387245741) / success | [37387245741](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/37387245741) / 2026-10-06 07:13:38 +0800 | 2.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
