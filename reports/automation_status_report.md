# Automation Status Report

- Generated at: 2026-07-06 06:03:10 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `5f5badf9`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28749304568](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749304568) / completed | [28749304568](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749304568) / success | [28749304568](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749304568) / 2026-07-06 01:41:35 +0800 | 4.4h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28749362792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749362792) / completed | [28749362792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749362792) / success | [28749362792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749362792) / 2026-07-06 01:43:07 +0800 | 4.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28749498119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749498119) / completed | [28749498119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749498119) / success | [28749498119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749498119) / 2026-07-06 01:48:24 +0800 | 4.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28749548087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749548087) / completed | [28749548087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749548087) / success | [28749548087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749548087) / 2026-07-06 01:50:03 +0800 | 4.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28750142010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750142010) / completed | [28750142010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750142010) / success | [28750142010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750142010) / 2026-07-06 02:11:19 +0800 | 3.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28750712613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750712613) / completed | [28750712613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750712613) / success | [28750712613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750712613) / 2026-07-06 02:32:30 +0800 | 3.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28755580529](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28755580529) / completed | [28755580529](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28755580529) / success | [28755580529](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28755580529) / 2026-07-06 05:32:27 +0800 | 31m | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 3.4h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [28756366178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28756366178) / in_progress | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / success | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / 2026-07-04 10:43:05 +0800 | 43.3h | latest run is in_progress |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [28755590928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28755590928) / completed | [28755590928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28755590928) / failure | [28720153795](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153795) / 2026-07-05 05:27:03 +0800 | 24.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28755590931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28755590931) / completed | [28755590931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28755590931) / success | [28755590931](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28755590931) / 2026-07-06 05:32:34 +0800 | 31m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
