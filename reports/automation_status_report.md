# Automation Status Report

- Generated at: 2026-07-23 05:35:04 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `720f7ae3`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29944067764](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944067764) / completed | [29944067764](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944067764) / success | [29944067764](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944067764) / 2026-07-23 01:52:17 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29944165452](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944165452) / completed | [29944165452](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944165452) / success | [29944165452](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944165452) / 2026-07-23 01:52:18 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29944463632](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944463632) / completed | [29944463632](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944463632) / success | [29944463632](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944463632) / 2026-07-23 01:56:23 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29944540859](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944540859) / completed | [29944540859](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944540859) / success | [29944540859](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29944540859) / 2026-07-23 01:57:11 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29945841154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29945841154) / completed | [29945841154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29945841154) / success | [29945841154](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29945841154) / 2026-07-23 02:15:30 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29947383833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29947383833) / completed | [29947383833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29947383833) / success | [29947383833](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29947383833) / 2026-07-23 02:38:11 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29959742562](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29959742562) / in_progress | [29870703999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870703999) / success | [29870703999](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870703999) / 2026-07-22 05:38:08 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / completed | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / success | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / 2026-07-20 02:33:21 +0800 | 75.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 169.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29870741955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870741955) / completed | [29870741955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870741955) / success | [29870741955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29870741955) / 2026-07-22 05:38:41 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29947530304](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29947530304) / completed | [29947530304](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29947530304) / success | [29947530304](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29947530304) / 2026-07-23 02:38:23 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
