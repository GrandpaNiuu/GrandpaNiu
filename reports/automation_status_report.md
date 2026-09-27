# Automation Status Report

- Generated at: 2026-09-28 04:21:23 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `3c46a727`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36345854694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345854694) / completed | [36345854694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345854694) / success | [36345854694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345854694) / 2026-09-28 03:52:21 +0800 | 29m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36345882365](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345882365) / completed | [36345882365](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345882365) / success | [36345882365](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345882365) / 2026-09-28 03:52:45 +0800 | 29m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36345961216](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345961216) / completed | [36345961216](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345961216) / success | [36345961216](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345961216) / 2026-09-28 03:53:21 +0800 | 28m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36345976936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345976936) / completed | [36345976936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345976936) / success | [36345976936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345976936) / 2026-09-28 03:53:31 +0800 | 28m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36346492402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36346492402) / completed | [36346492402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36346492402) / success | [36346492402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36346492402) / 2026-09-28 04:02:28 +0800 | 19m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36347188447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347188447) / completed | [36347188447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347188447) / success | [36347188447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347188447) / 2026-09-28 04:14:00 +0800 | 7m | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36278197269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36278197269) / completed | [36278197269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36278197269) / success | [36278197269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36278197269) / 2026-09-27 07:03:31 +0800 | 21.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / in_progress | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 168.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1225.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36278243364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36278243364) / completed | [36278243364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36278243364) / success | [36278243364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36278243364) / 2026-09-27 07:04:02 +0800 | 21.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36347265294](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347265294) / completed | [36347265294](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347265294) / success | [36347265294](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347265294) / 2026-09-28 04:14:11 +0800 | 7m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
