# Automation Status Report

- Generated at: 2026-07-08 05:51:14 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `1dff2aa6`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28889621052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889621052) / completed | [28889621052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889621052) / success | [28889621052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889621052) / 2026-07-08 02:34:38 +0800 | 3.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28889662670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889662670) / completed | [28889662670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889662670) / success | [28889662670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28889662670) / 2026-07-08 02:34:57 +0800 | 3.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28890652643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890652643) / completed | [28890652643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890652643) / success | [28890652643](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890652643) / 2026-07-08 02:51:29 +0800 | 3.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28890676445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890676445) / completed | [28890676445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890676445) / success | [28890676445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28890676445) / 2026-07-08 02:51:45 +0800 | 3.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28891630197](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28891630197) / completed | [28891630197](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28891630197) / success | [28891630197](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28891630197) / 2026-07-08 03:07:45 +0800 | 2.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28892111422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892111422) / completed | [28892111422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892111422) / success | [28892111422](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28892111422) / 2026-07-08 03:17:34 +0800 | 2.6h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [28901158371](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28901158371) / in_progress | [28825832207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825832207) / success | [28825832207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28825832207) / 2026-07-07 05:53:49 +0800 | 24.0h | latest run is in_progress |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 51.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / completed | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / success | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / 2026-07-08 04:47:11 +0800 | 1.1h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [28897569296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897569296) / completed | [28897569296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897569296) / success | [28897569296](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897569296) / 2026-07-08 04:47:43 +0800 | 1.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28897569258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897569258) / completed | [28897569258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897569258) / success | [28897569258](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897569258) / 2026-07-08 04:47:20 +0800 | 1.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
