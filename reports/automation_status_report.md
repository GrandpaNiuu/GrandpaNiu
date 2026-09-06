# Automation Status Report

- Generated at: 2026-09-07 06:12:01 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ec14b188`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34052254702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052254702) / completed | [34052254702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052254702) / success | [34052254702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052254702) / 2026-09-07 02:37:38 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34052294366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052294366) / completed | [34052294366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052294366) / success | [34052294366](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052294366) / 2026-09-07 02:37:59 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34052416269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052416269) / completed | [34052416269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052416269) / success | [34052416269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052416269) / 2026-09-07 02:39:58 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34052436605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052436605) / completed | [34052436605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052436605) / success | [34052436605](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34052436605) / 2026-09-07 02:40:15 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34053520770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34053520770) / completed | [34053520770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34053520770) / success | [34053520770](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34053520770) / 2026-09-07 03:01:48 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34054370271](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054370271) / completed | [34054370271](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054370271) / success | [34054370271](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054370271) / 2026-09-07 03:18:13 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34063299179](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34063299179) / in_progress | [33995021545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995021545) / success | [33995021545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995021545) / 2026-09-06 06:08:32 +0800 | 24.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / completed | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 2.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 723.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33995048597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995048597) / completed | [33995048597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995048597) / success | [33995048597](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33995048597) / 2026-09-06 06:09:04 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34054997036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054997036) / completed | [34054997036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054997036) / success | [34054997036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054997036) / 2026-09-07 03:28:33 +0800 | 2.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
