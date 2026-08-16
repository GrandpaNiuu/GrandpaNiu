# Automation Status Report

- Generated at: 2026-08-17 01:51:14 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `c21df48e`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31960050705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960050705) / completed | [31960050705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960050705) / success | [31960050705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960050705) / 2026-08-17 00:57:09 +0800 | 54m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31960138600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960138600) / completed | [31960138600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960138600) / success | [31960138600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960138600) / 2026-08-17 00:57:49 +0800 | 53m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31960401195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960401195) / completed | [31960401195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960401195) / success | [31960401195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960401195) / 2026-08-17 01:02:59 +0800 | 48m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31960510812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960510812) / completed | [31960510812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960510812) / success | [31960510812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960510812) / 2026-08-17 01:05:00 +0800 | 46m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31961573521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31961573521) / completed | [31961573521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31961573521) / success | [31961573521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31961573521) / 2026-08-17 01:26:37 +0800 | 25m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31962194371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962194371) / completed | [31962194371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962194371) / success | [31962194371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962194371) / 2026-08-17 01:39:31 +0800 | 12m | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31907537476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907537476) / completed | [31907537476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907537476) / success | [31907537476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907537476) / 2026-08-16 04:45:39 +0800 | 21.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / in_progress | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 167.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 214.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / completed | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / success | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / 2026-08-16 04:46:15 +0800 | 21.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31962259950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962259950) / completed | [31962259950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962259950) / success | [31962259950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962259950) / 2026-08-17 01:39:42 +0800 | 12m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
