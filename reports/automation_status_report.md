# Automation Status Report

- Generated at: 2026-08-17 04:44:47 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `318a124a`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31960050705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960050705) / completed | [31960050705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960050705) / success | [31960050705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960050705) / 2026-08-17 00:57:09 +0800 | 3.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31960138600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960138600) / completed | [31960138600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960138600) / success | [31960138600](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960138600) / 2026-08-17 00:57:49 +0800 | 3.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31960401195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960401195) / completed | [31960401195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960401195) / success | [31960401195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960401195) / 2026-08-17 01:02:59 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31960510812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960510812) / completed | [31960510812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960510812) / success | [31960510812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31960510812) / 2026-08-17 01:05:00 +0800 | 3.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31961573521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31961573521) / completed | [31961573521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31961573521) / success | [31961573521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31961573521) / 2026-08-17 01:26:37 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31962194371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962194371) / completed | [31962194371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962194371) / success | [31962194371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962194371) / 2026-08-17 01:39:31 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31971433560](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31971433560) / in_progress | [31907537476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907537476) / success | [31907537476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907537476) / 2026-08-16 04:45:39 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / completed | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / success | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / 2026-08-17 01:51:36 +0800 | 2.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 217.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / completed | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / success | [31907568122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31907568122) / 2026-08-16 04:46:15 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31962862785](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962862785) / completed | [31962862785](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962862785) / success | [31962862785](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962862785) / 2026-08-17 01:51:47 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
