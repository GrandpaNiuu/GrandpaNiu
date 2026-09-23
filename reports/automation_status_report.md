# Automation Status Report

- Generated at: 2026-09-24 03:47:58 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `678864c3`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35911604603](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35911604603) / in_progress | [35776473623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776473623) / success | [35776473623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776473623) / 2026-09-23 03:53:18 +0800 | 23.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35911679076](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35911679076) / in_progress | [35776550591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776550591) / success | [35776550591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776550591) / 2026-09-23 03:53:45 +0800 | 23.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35776768482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776768482) / completed | [35776768482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776768482) / success | [35776768482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776768482) / 2026-09-23 03:54:56 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35776801183](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776801183) / completed | [35776801183](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776801183) / success | [35776801183](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776801183) / 2026-09-23 03:55:18 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35777977039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35777977039) / completed | [35777977039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35777977039) / success | [35777977039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35777977039) / 2026-09-23 04:06:48 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35778893512](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35778893512) / completed | [35778893512](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35778893512) / success | [35778893512](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35778893512) / 2026-09-23 04:15:20 +0800 | 23.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35795790495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795790495) / completed | [35795790495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795790495) / success | [35795790495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795790495) / 2026-09-23 07:07:16 +0800 | 20.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / completed | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 72.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1128.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35795842679](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795842679) / completed | [35795842679](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795842679) / success | [35795842679](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795842679) / 2026-09-23 07:07:51 +0800 | 20.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35795892685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795892685) / completed | [35795892685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795892685) / success | [35795892685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795892685) / 2026-09-23 07:08:03 +0800 | 20.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
