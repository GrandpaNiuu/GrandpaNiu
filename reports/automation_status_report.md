# Automation Status Report

- Generated at: 2026-08-19 04:46:52 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `cad7780c`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32163314052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32163314052) / completed | [32163314052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32163314052) / success | [32163314052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32163314052) / 2026-08-19 01:01:41 +0800 | 3.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32163429269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32163429269) / completed | [32163429269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32163429269) / success | [32163429269](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32163429269) / 2026-08-19 01:02:22 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32164248175](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32164248175) / completed | [32164248175](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32164248175) / success | [32164248175](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32164248175) / 2026-08-19 01:11:42 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32164391923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32164391923) / completed | [32164391923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32164391923) / success | [32164391923](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32164391923) / 2026-08-19 01:13:08 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32166297423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32166297423) / completed | [32166297423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32166297423) / success | [32166297423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32166297423) / 2026-08-19 01:35:08 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32167447107](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32167447107) / completed | [32167447107](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32167447107) / success | [32167447107](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32167447107) / 2026-08-19 01:49:31 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32184144321](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32184144321) / in_progress | [32067988333](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32067988333) / success | [32067988333](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32067988333) / 2026-08-18 04:51:38 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / completed | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / success | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / 2026-08-17 01:51:36 +0800 | 50.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 265.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32068048310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068048310) / completed | [32068048310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068048310) / success | [32068048310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068048310) / 2026-08-18 04:52:13 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32167663657](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32167663657) / completed | [32167663657](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32167663657) / success | [32167663657](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32167663657) / 2026-08-19 01:49:42 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
