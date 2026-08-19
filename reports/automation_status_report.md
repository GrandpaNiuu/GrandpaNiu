# Automation Status Report

- Generated at: 2026-08-20 04:52:44 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `0fa59e09`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32278972078](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32278972078) / completed | [32278972078](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32278972078) / success | [32278972078](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32278972078) / 2026-08-20 01:00:02 +0800 | 3.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32279095298](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32279095298) / completed | [32279095298](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32279095298) / success | [32279095298](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32279095298) / 2026-08-20 01:00:37 +0800 | 3.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32280069901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32280069901) / completed | [32280069901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32280069901) / success | [32280069901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32280069901) / 2026-08-20 01:10:56 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32280207807](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32280207807) / completed | [32280207807](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32280207807) / success | [32280207807](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32280207807) / 2026-08-20 01:12:17 +0800 | 3.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32282218666](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32282218666) / completed | [32282218666](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32282218666) / success | [32282218666](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32282218666) / 2026-08-20 01:33:39 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32283345821](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32283345821) / completed | [32283345821](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32283345821) / success | [32283345821](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32283345821) / 2026-08-20 01:46:03 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32300840392](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32300840392) / in_progress | [32184144321](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32184144321) / success | [32184144321](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32184144321) / 2026-08-19 04:47:12 +0800 | 24.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / completed | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / success | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / 2026-08-17 01:51:36 +0800 | 75.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 289.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32184211817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32184211817) / completed | [32184211817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32184211817) / success | [32184211817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32184211817) / 2026-08-19 04:47:51 +0800 | 24.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32283501555](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32283501555) / completed | [32283501555](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32283501555) / success | [32283501555](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32283501555) / 2026-08-20 01:46:15 +0800 | 3.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
