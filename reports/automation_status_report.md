# Automation Status Report

- Generated at: 2026-10-19 06:30:11 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `7c1654de`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [39156151388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156151388) / completed | [39156151388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156151388) / success | [39156151388](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156151388) / 2026-10-19 02:53:30 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [39156272947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156272947) / completed | [39156272947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156272947) / success | [39156272947](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156272947) / 2026-10-19 02:54:30 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [39156630091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156630091) / completed | [39156630091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156630091) / success | [39156630091](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156630091) / 2026-10-19 02:59:18 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [39156705265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156705265) / completed | [39156705265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156705265) / success | [39156705265](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39156705265) / 2026-10-19 03:00:18 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [39158418720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158418720) / completed | [39158418720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158418720) / success | [39158418720](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158418720) / 2026-10-19 03:22:50 +0800 | 3.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [39158870897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158870897) / completed | [39158870897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39158870897) / failure | [36931408752](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36931408752) / 2026-10-02 05:53:15 +0800 | 408.6h | last success is stale (408.6h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [39172478135](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39172478135) / in_progress | [39168088912](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168088912) / failure | [36943708934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36943708934) / 2026-10-02 08:00:29 +0800 | 406.5h | last success is stale (406.5h > 48h)<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / completed | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / success | [39159468517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39159468517) / 2026-10-19 03:37:05 +0800 | 2.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 58m | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [39168383048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168383048) / completed | [39168383048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168383048) / success | [39168383048](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168383048) / 2026-10-19 05:34:16 +0800 | 56m | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [39168425963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168425963) / completed | [39168425963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168425963) / success | [39168425963](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168425963) / 2026-10-19 05:34:25 +0800 | 56m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
