# Automation Status Report

- Generated at: 2026-08-24 04:45:51 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `e9baec31`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32653216506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653216506) / completed | [32653216506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653216506) / success | [32653216506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653216506) / 2026-08-24 00:57:16 +0800 | 3.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32653326482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653326482) / completed | [32653326482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653326482) / success | [32653326482](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653326482) / 2026-08-24 00:58:50 +0800 | 3.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32653597813](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653597813) / completed | [32653597813](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653597813) / success | [32653597813](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653597813) / 2026-08-24 01:03:52 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32653824922](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653824922) / completed | [32653824922](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653824922) / success | [32653824922](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653824922) / 2026-08-24 01:08:00 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32654841799](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32654841799) / completed | [32654841799](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32654841799) / success | [32654841799](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32654841799) / 2026-08-24 01:27:12 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32655505806](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32655505806) / completed | [32655505806](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32655505806) / success | [32655505806](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32655505806) / 2026-08-24 01:40:49 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32665398424](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32665398424) / in_progress | [32597636934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597636934) / success | [32597636934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597636934) / 2026-08-23 04:46:39 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / completed | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 2.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 385.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32597668075](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597668075) / completed | [32597668075](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597668075) / success | [32597668075](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597668075) / 2026-08-23 04:47:12 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32656217843](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656217843) / completed | [32656217843](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656217843) / success | [32656217843](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656217843) / 2026-08-24 01:52:20 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
