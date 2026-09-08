# Automation Status Report

- Generated at: 2026-09-09 03:33:59 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `5af7b98d`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34269602332](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269602332) / in_progress | [34158174104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158174104) / success | [34158174104](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158174104) / 2026-09-08 04:08:31 +0800 | 23.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34269705606](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34269705606) / queued | [34158221733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158221733) / success | [34158221733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158221733) / 2026-09-08 04:08:47 +0800 | 23.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34158395861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158395861) / completed | [34158395861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158395861) / success | [34158395861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158395861) / 2026-09-08 04:11:09 +0800 | 23.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34158414004](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158414004) / completed | [34158414004](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158414004) / success | [34158414004](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34158414004) / 2026-09-08 04:11:21 +0800 | 23.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34159439274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34159439274) / completed | [34159439274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34159439274) / success | [34159439274](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34159439274) / 2026-09-08 04:27:29 +0800 | 23.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34160161589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34160161589) / completed | [34160161589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34160161589) / success | [34160161589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34160161589) / 2026-09-08 04:39:40 +0800 | 22.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34168302025](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168302025) / completed | [34168302025](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168302025) / success | [34168302025](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168302025) / 2026-09-08 06:56:10 +0800 | 20.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / completed | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 48.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 768.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34168342504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168342504) / completed | [34168342504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168342504) / success | [34168342504](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168342504) / 2026-09-08 06:56:42 +0800 | 20.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34168368563](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168368563) / completed | [34168368563](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168368563) / success | [34168368563](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34168368563) / 2026-09-08 06:56:53 +0800 | 20.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
