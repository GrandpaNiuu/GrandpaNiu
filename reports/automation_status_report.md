# Automation Status Report

- Generated at: 2026-07-24 05:33:22 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `f16fb421`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30031622897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031622897) / completed | [30031622897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031622897) / success | [30031622897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031622897) / 2026-07-24 01:59:06 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30031720451](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031720451) / completed | [30031720451](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031720451) / success | [30031720451](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031720451) / 2026-07-24 01:59:37 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30031956728](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031956728) / completed | [30031956728](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031956728) / success | [30031956728](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30031956728) / 2026-07-24 02:02:29 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30032003608](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30032003608) / completed | [30032003608](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30032003608) / success | [30032003608](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30032003608) / 2026-07-24 02:02:51 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30033080448](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30033080448) / completed | [30033080448](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30033080448) / success | [30033080448](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30033080448) / 2026-07-24 02:18:21 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30034704840](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30034704840) / completed | [30034704840](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30034704840) / success | [30034704840](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30034704840) / 2026-07-24 02:42:18 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30046630536](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30046630536) / in_progress | [29959742562](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29959742562) / success | [29959742562](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29959742562) / 2026-07-23 05:36:04 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / completed | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / success | [29698885994](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29698885994) / 2026-07-20 02:33:21 +0800 | 99.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 193.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29959824038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29959824038) / completed | [29959824038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29959824038) / success | [29959824038](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29959824038) / 2026-07-23 05:36:44 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30034862791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30034862791) / completed | [30034862791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30034862791) / success | [30034862791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30034862791) / 2026-07-24 02:42:30 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
