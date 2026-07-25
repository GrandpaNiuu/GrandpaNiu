# Automation Status Report

- Generated at: 2026-07-26 05:23:09 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `6ca1ef79`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30167946853](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30167946853) / completed | [30167946853](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30167946853) / success | [30167946853](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30167946853) / 2026-07-26 01:37:08 +0800 | 3.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30168025710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168025710) / completed | [30168025710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168025710) / success | [30168025710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168025710) / 2026-07-26 01:38:37 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30168207249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168207249) / completed | [30168207249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168207249) / success | [30168207249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168207249) / 2026-07-26 01:44:02 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30168225805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168225805) / completed | [30168225805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168225805) / success | [30168225805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168225805) / 2026-07-26 01:44:34 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30168798593](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168798593) / completed | [30168798593](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168798593) / success | [30168798593](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30168798593) / 2026-07-26 02:01:58 +0800 | 3.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30169128643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30169128643) / completed | [30169128643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30169128643) / success | [30169128643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30169128643) / 2026-07-26 02:12:29 +0800 | 3.2h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30175523980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30175523980) / in_progress | [30128205171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30128205171) / success | [30128205171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30128205171) / 2026-07-25 05:35:15 +0800 | 23.8h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / completed | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / success | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / 2026-07-20 02:33:21 +0800 | 146.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 241.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30128239256](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30128239256) / completed | [30128239256](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30128239256) / success | [30128239256](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30128239256) / 2026-07-25 05:35:57 +0800 | 23.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30169166375](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30169166375) / completed | [30169166375](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30169166375) / success | [30169166375](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30169166375) / 2026-07-26 02:12:41 +0800 | 3.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
