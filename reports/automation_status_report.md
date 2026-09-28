# Automation Status Report

- Generated at: 2026-09-29 06:16:21 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `aa32a1da`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36491268454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491268454) / in_progress | [36345854694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345854694) / success | [36345854694](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345854694) / 2026-09-28 03:52:21 +0800 | 26.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36491332112](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491332112) / in_progress | [36345882365](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345882365) / success | [36345882365](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345882365) / 2026-09-28 03:52:45 +0800 | 26.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36345961216](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345961216) / completed | [36345961216](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345961216) / success | [36345961216](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345961216) / 2026-09-28 03:53:21 +0800 | 26.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36345976936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345976936) / completed | [36345976936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345976936) / success | [36345976936](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36345976936) / 2026-09-28 03:53:31 +0800 | 26.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36346492402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36346492402) / completed | [36346492402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36346492402) / success | [36346492402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36346492402) / 2026-09-28 04:02:28 +0800 | 26.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36347188447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347188447) / completed | [36347188447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347188447) / success | [36347188447](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347188447) / 2026-09-28 04:14:00 +0800 | 26.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36357877811](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357877811) / completed | [36357877811](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357877811) / success | [36357877811](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357877811) / 2026-09-28 07:12:40 +0800 | 23.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / completed | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / success | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / 2026-09-28 04:21:38 +0800 | 25.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1251.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36357918809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357918809) / completed | [36357918809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357918809) / success | [36357918809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357918809) / 2026-09-28 07:13:12 +0800 | 23.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36357948798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357948798) / completed | [36357948798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357948798) / success | [36357948798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357948798) / 2026-09-28 07:13:22 +0800 | 23.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
