# Automation Status Report

- Generated at: 2026-08-31 04:00:39 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `c23b614e`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33330791741](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330791741) / completed | [33330791741](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330791741) / success | [33330791741](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330791741) / 2026-08-31 03:26:00 +0800 | 35m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33330835812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330835812) / completed | [33330835812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330835812) / success | [33330835812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330835812) / 2026-08-31 03:26:25 +0800 | 34m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33330989806](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330989806) / completed | [33330989806](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330989806) / success | [33330989806](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33330989806) / 2026-08-31 03:29:36 +0800 | 31m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33331022710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33331022710) / completed | [33331022710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33331022710) / success | [33331022710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33331022710) / 2026-08-31 03:30:20 +0800 | 30m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33331632871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33331632871) / completed | [33331632871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33331632871) / success | [33331632871](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33331632871) / 2026-08-31 03:43:39 +0800 | 17m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33332036664](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332036664) / completed | [33332036664](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332036664) / success | [33332036664](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332036664) / 2026-08-31 03:53:22 +0800 | 7m | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33279246810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279246810) / completed | [33279246810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279246810) / success | [33279246810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279246810) / 2026-08-30 06:43:05 +0800 | 21.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / in_progress | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 170.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 552.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33279267497](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279267497) / completed | [33279267497](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279267497) / success | [33279267497](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33279267497) / 2026-08-30 06:43:43 +0800 | 21.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33332110612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332110612) / completed | [33332110612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332110612) / success | [33332110612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332110612) / 2026-08-31 03:53:30 +0800 | 7m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
