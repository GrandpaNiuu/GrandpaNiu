# Automation Status Report

- Generated at: 2026-08-24 00:56:59 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `93e32731`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32653216506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32653216506) / in_progress | [32586169703](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586169703) / success | [32586169703](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586169703) / 2026-08-23 00:56:53 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32586249257](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586249257) / completed | [32586249257](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586249257) / success | [32586249257](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586249257) / 2026-08-23 00:57:24 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32586506442](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586506442) / completed | [32586506442](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586506442) / success | [32586506442](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586506442) / 2026-08-23 01:02:22 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32586581721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586581721) / completed | [32586581721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586581721) / success | [32586581721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586581721) / 2026-08-23 01:03:52 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32587776990](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32587776990) / completed | [32587776990](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32587776990) / success | [32587776990](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32587776990) / 2026-08-23 01:28:05 +0800 | 23.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32588414370](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32588414370) / completed | [32588414370](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32588414370) / success | [32588414370](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32588414370) / 2026-08-23 01:41:11 +0800 | 23.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32597636934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597636934) / completed | [32597636934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597636934) / success | [32597636934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597636934) / 2026-08-23 04:46:39 +0800 | 20.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / completed | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / success | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / 2026-08-17 01:51:36 +0800 | 167.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 381.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32597668075](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597668075) / completed | [32597668075](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597668075) / success | [32597668075](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597668075) / 2026-08-23 04:47:12 +0800 | 20.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32597692680](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597692680) / completed | [32597692680](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597692680) / success | [32597692680](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32597692680) / 2026-08-23 04:47:24 +0800 | 20.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
