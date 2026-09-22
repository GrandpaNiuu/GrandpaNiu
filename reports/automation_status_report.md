# Automation Status Report

- Generated at: 2026-09-23 07:06:58 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `c43c225d`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35776473623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776473623) / completed | [35776473623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776473623) / success | [35776473623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776473623) / 2026-09-23 03:53:18 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35776550591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776550591) / completed | [35776550591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776550591) / success | [35776550591](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776550591) / 2026-09-23 03:53:45 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35776768482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776768482) / completed | [35776768482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776768482) / success | [35776768482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776768482) / 2026-09-23 03:54:56 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35776801183](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776801183) / completed | [35776801183](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776801183) / success | [35776801183](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35776801183) / 2026-09-23 03:55:18 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35777977039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35777977039) / completed | [35777977039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35777977039) / success | [35777977039](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35777977039) / 2026-09-23 04:06:48 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35778893512](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35778893512) / completed | [35778893512](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35778893512) / success | [35778893512](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35778893512) / 2026-09-23 04:15:20 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35795790495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795790495) / in_progress | [35667570590](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35667570590) / success | [35667570590](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35667570590) / 2026-09-22 07:27:25 +0800 | 23.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / completed | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 51.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1108.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35667641532](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35667641532) / completed | [35667641532](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35667641532) / success | [35667641532](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35667641532) / 2026-09-22 07:28:04 +0800 | 23.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35779080119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35779080119) / completed | [35779080119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35779080119) / success | [35779080119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35779080119) / 2026-09-23 04:15:32 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
