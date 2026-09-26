# Automation Status Report

- Generated at: 2026-09-27 07:03:02 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `bad86856`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36265700690](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36265700690) / completed | [36265700690](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36265700690) / success | [36265700690](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36265700690) / 2026-09-27 03:21:36 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36265798648](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36265798648) / completed | [36265798648](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36265798648) / success | [36265798648](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36265798648) / 2026-09-27 03:22:27 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36266067992](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266067992) / completed | [36266067992](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266067992) / success | [36266067992](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266067992) / 2026-09-27 03:27:03 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36266103708](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266103708) / completed | [36266103708](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266103708) / success | [36266103708](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266103708) / 2026-09-27 03:27:38 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36266854548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266854548) / completed | [36266854548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266854548) / success | [36266854548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36266854548) / 2026-09-27 03:41:03 +0800 | 3.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36267728957](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36267728957) / completed | [36267728957](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36267728957) / success | [36267728957](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36267728957) / 2026-09-27 03:56:56 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36278197269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36278197269) / in_progress | [36200764364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36200764364) / success | [36200764364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36200764364) / 2026-09-26 07:23:19 +0800 | 23.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / completed | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 147.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1203.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36200817016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36200817016) / completed | [36200817016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36200817016) / success | [36200817016](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36200817016) / 2026-09-26 07:23:51 +0800 | 23.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36267802911](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36267802911) / completed | [36267802911](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36267802911) / success | [36267802911](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36267802911) / 2026-09-27 03:57:07 +0800 | 3.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
