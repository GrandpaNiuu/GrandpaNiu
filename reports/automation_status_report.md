# Automation Status Report

- Generated at: 2026-08-13 05:11:21 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `03fe45fb`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31623358631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31623358631) / completed | [31623358631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31623358631) / success | [31623358631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31623358631) / 2026-08-13 01:36:28 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31623577188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31623577188) / completed | [31623577188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31623577188) / success | [31623577188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31623577188) / 2026-08-13 01:38:18 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31624091559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31624091559) / completed | [31624091559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31624091559) / success | [31624091559](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31624091559) / 2026-08-13 01:44:22 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31624144223](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31624144223) / completed | [31624144223](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31624144223) / success | [31624144223](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31624144223) / 2026-08-13 01:44:57 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31625442645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31625442645) / completed | [31625442645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31625442645) / success | [31625442645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31625442645) / 2026-08-13 02:00:57 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31626250236](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31626250236) / completed | [31626250236](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31626250236) / success | [31626250236](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31626250236) / 2026-08-13 02:11:25 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31641317575](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31641317575) / in_progress | [31536747702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536747702) / success | [31536747702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536747702) / 2026-08-12 05:12:46 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 75.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 122.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31536807139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536807139) / completed | [31536807139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536807139) / success | [31536807139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536807139) / 2026-08-12 05:13:24 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31626399630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31626399630) / completed | [31626399630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31626399630) / success | [31626399630](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31626399630) / 2026-08-13 02:11:35 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
