# Automation Status Report

- Generated at: 2026-09-26 07:22:55 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `f2a96cb0`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36183746371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36183746371) / completed | [36183746371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36183746371) / success | [36183746371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36183746371) / 2026-09-26 04:07:58 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36183799055](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36183799055) / completed | [36183799055](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36183799055) / success | [36183799055](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36183799055) / 2026-09-26 04:08:20 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36184000468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36184000468) / completed | [36184000468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36184000468) / success | [36184000468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36184000468) / 2026-09-26 04:09:31 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36184016786](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36184016786) / completed | [36184016786](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36184016786) / success | [36184016786](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36184016786) / 2026-09-26 04:09:41 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36185281776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36185281776) / completed | [36185281776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36185281776) / success | [36185281776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36185281776) / 2026-09-26 04:22:16 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36186316524](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36186316524) / completed | [36186316524](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36186316524) / success | [36186316524](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36186316524) / 2026-09-26 04:33:39 +0800 | 2.8h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36200764364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36200764364) / in_progress | [36071896003](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071896003) / success | [36071896003](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071896003) / 2026-09-25 07:17:24 +0800 | 24.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / completed | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 123.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1180.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36071970028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071970028) / completed | [36071970028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071970028) / success | [36071970028](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36071970028) / 2026-09-25 07:18:00 +0800 | 24.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36186505931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36186505931) / completed | [36186505931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36186505931) / success | [36186505931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36186505931) / 2026-09-26 04:33:49 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
