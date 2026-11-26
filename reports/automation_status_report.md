# Automation Status Report

- Generated at: 2026-11-26 10:57:33 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `0c785f7a`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [45730099328](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730099328) / completed | [45730099328](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730099328) / success | [45730099328](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730099328) / 2026-11-26 08:38:50 +0800 | 2.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [45730213707](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730213707) / completed | [45730213707](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730213707) / success | [45730213707](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730213707) / 2026-11-26 08:39:23 +0800 | 2.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [45730585965](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730585965) / completed | [45730585965](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730585965) / success | [45730585965](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730585965) / 2026-11-26 08:42:44 +0800 | 2.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [45730615833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730615833) / completed | [45730615833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730615833) / success | [45730615833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45730615833) / 2026-11-26 08:43:01 +0800 | 2.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [45732002817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45732002817) / completed | [45732002817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45732002817) / success | [45732002817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45732002817) / 2026-11-26 08:54:40 +0800 | 2.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [45732824711](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45732824711) / completed | [45732824711](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45732824711) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [45745768983](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45745768983) / in_progress | [45541219724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45541219724) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / completed | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / success | [45079342334](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45079342334) / 2026-11-23 06:45:10 +0800 | 76.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 917.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [45541317053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45541317053) / completed | [45541317053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45541317053) / success | [45541317053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45541317053) / 2026-11-25 11:38:09 +0800 | 23.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [45732975700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45732975700) / completed | [45732975700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45732975700) / success | [45732975700](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/45732975700) / 2026-11-26 09:02:37 +0800 | 1.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
