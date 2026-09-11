# Automation Status Report

- Generated at: 2026-09-12 03:15:59 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `65f5f7d4`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34637808394](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34637808394) / in_progress | [34519132405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519132405) / success | [34519132405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519132405) / 2026-09-11 03:15:04 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34519233307](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519233307) / completed | [34519233307](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519233307) / success | [34519233307](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519233307) / 2026-09-11 03:15:36 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34519535900](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519535900) / completed | [34519535900](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519535900) / success | [34519535900](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519535900) / 2026-09-11 03:18:18 +0800 | 24.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34519599615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519599615) / completed | [34519599615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519599615) / success | [34519599615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34519599615) / 2026-09-11 03:18:41 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34520868551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34520868551) / completed | [34520868551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34520868551) / success | [34520868551](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34520868551) / 2026-09-11 03:31:55 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34522468661](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34522468661) / completed | [34522468661](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34522468661) / success | [34522468661](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34522468661) / 2026-09-11 03:49:06 +0800 | 23.4h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34538684127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538684127) / completed | [34538684127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538684127) / success | [34538684127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538684127) / 2026-09-11 06:42:17 +0800 | 20.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / completed | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 119.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 840.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34538747611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538747611) / completed | [34538747611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538747611) / success | [34538747611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538747611) / 2026-09-11 06:42:49 +0800 | 20.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34538790689](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538790689) / completed | [34538790689](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538790689) / success | [34538790689](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538790689) / 2026-09-11 06:43:02 +0800 | 20.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
