# Automation Status Report

- Generated at: 2026-07-08 04:46:50 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `4834b9ed`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28889621052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889621052) / completed | [28889621052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889621052) / success | [28889621052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889621052) / 2026-07-08 02:34:38 +0800 | 2.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28889662670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889662670) / completed | [28889662670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889662670) / success | [28889662670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889662670) / 2026-07-08 02:34:57 +0800 | 2.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28890652643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890652643) / completed | [28890652643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890652643) / success | [28890652643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890652643) / 2026-07-08 02:51:29 +0800 | 1.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28890676445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890676445) / completed | [28890676445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890676445) / success | [28890676445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890676445) / 2026-07-08 02:51:45 +0800 | 1.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28891630197](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28891630197) / completed | [28891630197](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28891630197) / success | [28891630197](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28891630197) / 2026-07-08 03:07:45 +0800 | 1.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28892111422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892111422) / completed | [28892111422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892111422) / success | [28892111422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892111422) / 2026-07-08 03:17:34 +0800 | 1.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28825832207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825832207) / completed | [28825832207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825832207) / success | [28825832207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825832207) / 2026-07-07 05:53:49 +0800 | 22.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 50.1h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / in_progress | [28756366178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28756366178) / success | [28756366178](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28756366178) / 2026-07-06 06:03:23 +0800 | 46.7h | latest run is in_progress |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [28825852901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825852901) / completed | [28825852901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825852901) / success | [28825852901](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825852901) / 2026-07-07 05:54:19 +0800 | 22.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28892238403](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892238403) / completed | [28892238403](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892238403) / success | [28892238403](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892238403) / 2026-07-08 03:17:45 +0800 | 1.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
