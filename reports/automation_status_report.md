# Automation Status Report

- Generated at: 2026-09-18 06:57:38 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `4f6f57aa`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35267138751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267138751) / completed | [35267138751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267138751) / success | [35267138751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267138751) / 2026-09-18 03:50:39 +0800 | 3.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35267212957](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267212957) / completed | [35267212957](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267212957) / success | [35267212957](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267212957) / 2026-09-18 03:51:04 +0800 | 3.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35267465172](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267465172) / completed | [35267465172](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267465172) / success | [35267465172](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267465172) / 2026-09-18 03:53:17 +0800 | 3.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35267555035](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267555035) / completed | [35267555035](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267555035) / success | [35267555035](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267555035) / 2026-09-18 03:53:59 +0800 | 3.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35269099856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35269099856) / completed | [35269099856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35269099856) / success | [35269099856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35269099856) / 2026-09-18 04:10:09 +0800 | 2.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35270444332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35270444332) / completed | [35270444332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35270444332) / success | [35270444332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35270444332) / 2026-09-18 04:24:22 +0800 | 2.6h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35284558433](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35284558433) / in_progress | [35160752453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160752453) / success | [35160752453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160752453) / 2026-09-17 07:06:35 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / completed | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / success | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / 2026-09-14 03:43:57 +0800 | 99.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 987.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35160814955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160814955) / completed | [35160814955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160814955) / success | [35160814955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160814955) / 2026-09-17 07:07:06 +0800 | 23.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35270611109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35270611109) / completed | [35270611109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35270611109) / success | [35270611109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35270611109) / 2026-09-18 04:24:33 +0800 | 2.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
