# Automation Status Report

- Generated at: 2026-07-06 02:41:13 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `c1cdc145`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28749304568](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749304568) / completed | [28749304568](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749304568) / success | [28749304568](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749304568) / 2026-07-06 01:41:35 +0800 | 60m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28749362792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749362792) / completed | [28749362792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749362792) / success | [28749362792](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749362792) / 2026-07-06 01:43:07 +0800 | 58m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28749498119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749498119) / completed | [28749498119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749498119) / success | [28749498119](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749498119) / 2026-07-06 01:48:24 +0800 | 53m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28749548087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749548087) / completed | [28749548087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749548087) / success | [28749548087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28749548087) / 2026-07-06 01:50:03 +0800 | 51m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28750142010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750142010) / completed | [28750142010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750142010) / success | [28750142010](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750142010) / 2026-07-06 02:11:19 +0800 | 30m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28750712613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750712613) / completed | [28750712613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750712613) / success | [28750712613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750712613) / 2026-07-06 02:32:30 +0800 | 9m | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28720143746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720143746) / completed | [28720143746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720143746) / success | [28720143746](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720143746) / 2026-07-05 05:26:27 +0800 | 21.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | warn | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / in_progress | [28695947613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) / success | [28695947613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28695947613) / 2026-07-04 13:16:27 +0800 | 37.4h | latest run is in_progress |
| `module-factory-build.yml` | push/manual | observe | ok | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / completed | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / success | [28692446521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28692446521) / 2026-07-04 10:43:05 +0800 | 40.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual / public-path push | observe | ok | [28720153795](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153795) / completed | [28720153795](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153795) / success | [28720153795](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28720153795) / 2026-07-05 05:27:03 +0800 | 21.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28750741191](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750741191) / completed | [28750741191](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750741191) / success | [28750741191](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750741191) / 2026-07-06 02:32:39 +0800 | 9m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
