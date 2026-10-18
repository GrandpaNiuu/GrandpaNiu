# Automation Status Report

- Generated at: 2026-10-19 05:30:15 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `328d6e23`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39156151388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156151388) / completed | [39156151388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156151388) / success | [39156151388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156151388) / 2026-10-19 02:53:30 +0800 | 2.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [39156272947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156272947) / completed | [39156272947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156272947) / success | [39156272947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156272947) / 2026-10-19 02:54:30 +0800 | 2.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39156630091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156630091) / completed | [39156630091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156630091) / success | [39156630091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156630091) / 2026-10-19 02:59:18 +0800 | 2.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39156705265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156705265) / completed | [39156705265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156705265) / success | [39156705265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156705265) / 2026-10-19 03:00:18 +0800 | 2.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39158418720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158418720) / completed | [39158418720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158418720) / success | [39158418720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158418720) / 2026-10-19 03:22:50 +0800 | 2.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39158870897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158870897) / completed | [39158870897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158870897) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 407.6h | last success is stale (407.6h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39168088912](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168088912) / in_progress | [39075269715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075269715) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 405.5h | last success is stale (405.5h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 1.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1730.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39075314998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075314998) / completed | [39075314998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075314998) / success | [39075314998](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39075314998) / 2026-10-18 06:30:07 +0800 | 23.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39159585059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159585059) / completed | [39159585059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159585059) / success | [39159585059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159585059) / 2026-10-19 03:37:14 +0800 | 1.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
