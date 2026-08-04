# Automation Status Report

- Generated at: 2026-08-05 05:46:11 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `377134c2`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30937700344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937700344) / completed | [30937700344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937700344) / success | [30937700344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937700344) / 2026-08-05 02:16:03 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30937818964](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937818964) / completed | [30937818964](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937818964) / success | [30937818964](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937818964) / 2026-08-05 02:16:47 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30937975615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937975615) / completed | [30937975615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937975615) / success | [30937975615](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30937975615) / 2026-08-05 02:18:37 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30938071063](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30938071063) / completed | [30938071063](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30938071063) / success | [30938071063](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30938071063) / 2026-08-05 02:19:53 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30939917306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30939917306) / completed | [30939917306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30939917306) / success | [30939917306](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30939917306) / 2026-08-05 02:43:37 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30941052093](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30941052093) / completed | [30941052093](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30941052093) / success | [30941052093](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30941052093) / 2026-08-05 02:59:29 +0800 | 2.8h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30953709032](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30953709032) / in_progress | [30855392320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855392320) / success | [30855392320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855392320) / 2026-08-04 05:38:02 +0800 | 24.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / completed | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / success | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / 2026-08-03 02:35:38 +0800 | 51.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 481.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30855448884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855448884) / completed | [30855448884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855448884) / success | [30855448884](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30855448884) / 2026-08-04 05:38:43 +0800 | 24.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30941193531](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30941193531) / completed | [30941193531](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30941193531) / success | [30941193531](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30941193531) / 2026-08-05 02:59:45 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
