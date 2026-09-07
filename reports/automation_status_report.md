# Automation Status Report

- Generated at: 2026-09-08 04:08:10 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ad425bed`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34158174104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158174104) / in_progress | [34052254702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052254702) / success | [34052254702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052254702) / 2026-09-07 02:37:38 +0800 | 25.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34158221733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158221733) / in_progress | [34052294366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052294366) / success | [34052294366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052294366) / 2026-09-07 02:37:59 +0800 | 25.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34052416269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052416269) / completed | [34052416269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052416269) / success | [34052416269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052416269) / 2026-09-07 02:39:58 +0800 | 25.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34052436605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052436605) / completed | [34052436605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052436605) / success | [34052436605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052436605) / 2026-09-07 02:40:15 +0800 | 25.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34053520770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34053520770) / completed | [34053520770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34053520770) / success | [34053520770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34053520770) / 2026-09-07 03:01:48 +0800 | 25.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34054370271](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054370271) / completed | [34054370271](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054370271) / success | [34054370271](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054370271) / 2026-09-07 03:18:13 +0800 | 24.8h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34063299179](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063299179) / completed | [34063299179](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063299179) / success | [34063299179](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063299179) / 2026-09-07 06:12:24 +0800 | 21.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / completed | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 24.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 745.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34063334251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063334251) / completed | [34063334251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063334251) / success | [34063334251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063334251) / 2026-09-07 06:13:02 +0800 | 21.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34063367535](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063367535) / completed | [34063367535](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063367535) / success | [34063367535](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063367535) / 2026-09-07 06:13:11 +0800 | 21.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
