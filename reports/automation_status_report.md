# Automation Status Report

- Generated at: 2026-08-04 05:37:34 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `1bd4ee65`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30840916697](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30840916697) / completed | [30840916697](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30840916697) / success | [30840916697](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30840916697) / 2026-08-04 02:22:49 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30841064463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841064463) / completed | [30841064463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841064463) / success | [30841064463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841064463) / 2026-08-04 02:24:16 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30841434545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841434545) / completed | [30841434545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841434545) / success | [30841434545](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841434545) / 2026-08-04 02:29:06 +0800 | 3.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30841457449](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841457449) / completed | [30841457449](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841457449) / success | [30841457449](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30841457449) / 2026-08-04 02:29:15 +0800 | 3.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30843311923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843311923) / completed | [30843311923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843311923) / success | [30843311923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843311923) / 2026-08-04 02:54:21 +0800 | 2.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30843740958](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843740958) / completed | [30843740958](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843740958) / success | [30843740958](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843740958) / 2026-08-04 03:00:39 +0800 | 2.6h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30855392320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855392320) / in_progress | [30767751181](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30767751181) / success | [30767751181](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30767751181) / 2026-08-03 05:23:28 +0800 | 24.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / completed | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / success | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / 2026-08-03 02:35:38 +0800 | 27.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 457.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30767775967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30767775967) / completed | [30767775967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30767775967) / success | [30767775967](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30767775967) / 2026-08-03 05:24:20 +0800 | 24.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30843848247](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843848247) / completed | [30843848247](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843848247) / success | [30843848247](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30843848247) / 2026-08-04 03:00:51 +0800 | 2.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
