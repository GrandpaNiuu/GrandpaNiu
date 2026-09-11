# Automation Status Report

- Generated at: 2026-09-12 06:41:50 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ee0a9ae8`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34637808394](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34637808394) / completed | [34637808394](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34637808394) / success | [34637808394](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34637808394) / 2026-09-12 03:16:18 +0800 | 3.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34637912705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34637912705) / completed | [34637912705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34637912705) / success | [34637912705](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34637912705) / 2026-09-12 03:16:43 +0800 | 3.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34638136534](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34638136534) / completed | [34638136534](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34638136534) / success | [34638136534](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34638136534) / 2026-09-12 03:19:21 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34638154041](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34638154041) / completed | [34638154041](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34638154041) / success | [34638154041](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34638154041) / 2026-09-12 03:19:34 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34639337418](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34639337418) / completed | [34639337418](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34639337418) / success | [34639337418](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34639337418) / 2026-09-12 03:32:45 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34640804924](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34640804924) / completed | [34640804924](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34640804924) / success | [34640804924](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34640804924) / 2026-09-12 03:50:09 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34655097856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34655097856) / in_progress | [34538684127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538684127) / success | [34538684127](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538684127) / 2026-09-11 06:42:17 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / completed | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 123.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 843.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34538747611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538747611) / completed | [34538747611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538747611) / success | [34538747611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34538747611) / 2026-09-11 06:42:49 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34640973162](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34640973162) / completed | [34640973162](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34640973162) / success | [34640973162](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34640973162) / 2026-09-12 03:50:18 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
