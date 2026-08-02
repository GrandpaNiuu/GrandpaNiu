# Automation Status Report

- Generated at: 2026-08-03 05:23:05 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `38f1dc96`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30759327798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759327798) / completed | [30759327798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759327798) / success | [30759327798](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759327798) / 2026-08-03 01:39:41 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30759431639](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759431639) / completed | [30759431639](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759431639) / success | [30759431639](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759431639) / 2026-08-03 01:42:08 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30759597815](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759597815) / completed | [30759597815](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759597815) / success | [30759597815](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759597815) / 2026-08-03 01:46:30 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30759594069](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759594069) / completed | [30759594069](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759594069) / success | [30759594069](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30759594069) / 2026-08-03 01:46:12 +0800 | 3.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30760301145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30760301145) / completed | [30760301145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30760301145) / success | [30760301145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30760301145) / 2026-08-03 02:05:28 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30760648882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30760648882) / completed | [30760648882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30760648882) / success | [30760648882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30760648882) / 2026-08-03 02:15:31 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30767751181](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30767751181) / in_progress | [30718995980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30718995980) / success | [30718995980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30718995980) / 2026-08-02 05:22:58 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / completed | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / success | [30761407385](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761407385) / 2026-08-03 02:35:38 +0800 | 2.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 433.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30719015521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30719015521) / completed | [30719015521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30719015521) / success | [30719015521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30719015521) / 2026-08-02 05:23:37 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30761469030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761469030) / completed | [30761469030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761469030) / success | [30761469030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30761469030) / 2026-08-03 02:35:48 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
