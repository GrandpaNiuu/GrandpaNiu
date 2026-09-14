# Automation Status Report

- Generated at: 2026-09-15 07:15:09 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `79ea906b`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34893227429](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893227429) / completed | [34893227429](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893227429) / success | [34893227429](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893227429) / 2026-09-15 04:31:01 +0800 | 2.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34893497476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893497476) / completed | [34893497476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893497476) / success | [34893497476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893497476) / 2026-09-15 04:32:33 +0800 | 2.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34894111087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894111087) / completed | [34894111087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894111087) / success | [34894111087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894111087) / 2026-09-15 04:38:45 +0800 | 2.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34894138950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894138950) / completed | [34894138950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894138950) / success | [34894138950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894138950) / 2026-09-15 04:39:04 +0800 | 2.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34895434196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34895434196) / completed | [34895434196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34895434196) / success | [34895434196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34895434196) / 2026-09-15 04:52:31 +0800 | 2.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34896025523](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896025523) / completed | [34896025523](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896025523) / success | [34896025523](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896025523) / 2026-09-15 04:59:22 +0800 | 2.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34907954139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34907954139) / in_progress | [34786969392](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34786969392) / success | [34786969392](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34786969392) / 2026-09-14 06:30:31 +0800 | 24.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / completed | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / success | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / 2026-09-14 03:43:57 +0800 | 27.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 916.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34787006531](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34787006531) / completed | [34787006531](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34787006531) / success | [34787006531](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34787006531) / 2026-09-14 06:31:05 +0800 | 24.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34896174113](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896174113) / completed | [34896174113](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896174113) / success | [34896174113](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896174113) / 2026-09-15 04:59:31 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
