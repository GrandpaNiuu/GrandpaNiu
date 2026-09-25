# Automation Status Report

- Generated at: 2026-09-26 04:07:38 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `5838ce8f`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36183746371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36183746371) / in_progress | [36052521195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36052521195) / success | [36052521195](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36052521195) / 2026-09-25 04:07:08 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36183799055](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36183799055) / in_progress | [36052660289](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36052660289) / success | [36052660289](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36052660289) / 2026-09-25 04:07:32 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36053044056](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36053044056) / completed | [36053044056](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36053044056) / success | [36053044056](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36053044056) / 2026-09-25 04:10:49 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36053106209](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36053106209) / completed | [36053106209](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36053106209) / success | [36053106209](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36053106209) / 2026-09-25 04:11:17 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36054246628](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36054246628) / completed | [36054246628](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36054246628) / success | [36054246628](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36054246628) / 2026-09-25 04:21:48 +0800 | 23.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36055536567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36055536567) / completed | [36055536567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36055536567) / success | [36055536567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36055536567) / 2026-09-25 04:34:21 +0800 | 23.6h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36071896003](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071896003) / completed | [36071896003](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071896003) / success | [36071896003](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071896003) / 2026-09-25 07:17:24 +0800 | 20.8h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / completed | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 120.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1177.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36071970028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071970028) / completed | [36071970028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071970028) / success | [36071970028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071970028) / 2026-09-25 07:18:00 +0800 | 20.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36072018886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36072018886) / completed | [36072018886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36072018886) / success | [36072018886](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36072018886) / 2026-09-25 07:18:14 +0800 | 20.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
