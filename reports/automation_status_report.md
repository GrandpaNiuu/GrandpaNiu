# Automation Status Report

- Generated at: 2026-09-16 03:49:00 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `01505183`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35015769901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35015769901) / in_progress | [34893227429](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893227429) / success | [34893227429](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893227429) / 2026-09-15 04:31:01 +0800 | 23.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35015837165](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35015837165) / in_progress | [34893497476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893497476) / success | [34893497476](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34893497476) / 2026-09-15 04:32:33 +0800 | 23.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34894111087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894111087) / completed | [34894111087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894111087) / success | [34894111087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894111087) / 2026-09-15 04:38:45 +0800 | 23.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34894138950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894138950) / completed | [34894138950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894138950) / success | [34894138950](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34894138950) / 2026-09-15 04:39:04 +0800 | 23.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34895434196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34895434196) / completed | [34895434196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34895434196) / success | [34895434196](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34895434196) / 2026-09-15 04:52:31 +0800 | 22.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34896025523](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896025523) / completed | [34896025523](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896025523) / success | [34896025523](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34896025523) / 2026-09-15 04:59:22 +0800 | 22.8h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34907954139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34907954139) / completed | [34907954139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34907954139) / success | [34907954139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34907954139) / 2026-09-15 07:15:35 +0800 | 20.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / completed | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / success | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / 2026-09-14 03:43:57 +0800 | 48.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 936.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34908024660](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34908024660) / completed | [34908024660](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34908024660) / success | [34908024660](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34908024660) / 2026-09-15 07:16:10 +0800 | 20.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34908072360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34908072360) / completed | [34908072360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34908072360) / success | [34908072360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34908072360) / 2026-09-15 07:16:22 +0800 | 20.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
