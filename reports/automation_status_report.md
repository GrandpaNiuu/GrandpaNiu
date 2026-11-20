# Automation Status Report

- Generated at: 2026-11-20 09:49:34 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `a53e932c`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [44635436043](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44635436043) / completed | [44635436043](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44635436043) / success | [44635436043](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44635436043) / 2026-11-20 07:12:32 +0800 | 2.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [44635658746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44635658746) / completed | [44635658746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44635658746) / success | [44635658746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44635658746) / 2026-11-20 07:13:09 +0800 | 2.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [44636027233](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44636027233) / completed | [44636027233](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44636027233) / success | [44636027233](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44636027233) / 2026-11-20 07:15:43 +0800 | 2.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [44636141044](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44636141044) / completed | [44636141044](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44636141044) / success | [44636141044](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44636141044) / 2026-11-20 07:16:21 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [44637910018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44637910018) / completed | [44637910018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44637910018) / success | [44637910018](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44637910018) / 2026-11-20 07:28:54 +0800 | 2.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [44639181635](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44639181635) / completed | [44639181635](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44639181635) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [44656369165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44656369165) / in_progress | [44440542422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44440542422) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / completed | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / success | [43766878447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/43766878447) / 2026-11-16 06:02:31 +0800 | 99.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / completed | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / success | [39168147515](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147515) / 2026-10-19 05:33:42 +0800 | 772.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [44440638318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44440638318) / completed | [44440638318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44440638318) / success | [44440638318](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44440638318) / 2026-11-19 09:56:40 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [44639413253](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44639413253) / completed | [44639413253](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44639413253) / success | [44639413253](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/44639413253) / 2026-11-20 07:39:08 +0800 | 2.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
