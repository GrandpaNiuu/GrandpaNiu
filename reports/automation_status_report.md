# Automation Status Report

- Generated at: 2026-08-17 00:56:47 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `3ff9926e`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31960050705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960050705) / in_progress | [31896829550](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31896829550) / success | [31896829550](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31896829550) / 2026-08-16 00:55:58 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31896932146](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31896932146) / completed | [31896932146](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31896932146) / success | [31896932146](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31896932146) / 2026-08-16 00:57:34 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31897179711](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31897179711) / completed | [31897179711](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31897179711) / success | [31897179711](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31897179711) / 2026-08-16 01:02:49 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31897301281](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31897301281) / completed | [31897301281](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31897301281) / success | [31897301281](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31897301281) / 2026-08-16 01:05:18 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31898309417](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31898309417) / completed | [31898309417](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31898309417) / success | [31898309417](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31898309417) / 2026-08-16 01:27:18 +0800 | 23.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31898928360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31898928360) / completed | [31898928360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31898928360) / success | [31898928360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31898928360) / 2026-08-16 01:41:24 +0800 | 23.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31907537476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907537476) / completed | [31907537476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907537476) / success | [31907537476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907537476) / 2026-08-16 04:45:39 +0800 | 20.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 166.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 213.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / completed | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / success | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / 2026-08-16 04:46:15 +0800 | 20.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31907591513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907591513) / completed | [31907591513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907591513) / success | [31907591513](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907591513) / 2026-08-16 04:46:24 +0800 | 20.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
