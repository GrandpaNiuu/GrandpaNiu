# Automation Status Report

- Generated at: 2026-07-12 01:37:00 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `416c8042`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [29161901292](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29161901292) / in_progress | [29113562589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113562589) / success | [29113562589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113562589) / 2026-07-11 02:11:00 +0800 | 23.4h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29113596453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113596453) / completed | [29113596453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113596453) / success | [29113596453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113596453) / 2026-07-11 02:11:32 +0800 | 23.4h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29113722037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113722037) / completed | [29113722037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113722037) / success | [29113722037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113722037) / 2026-07-11 02:13:22 +0800 | 23.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29113749888](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113749888) / completed | [29113749888](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113749888) / success | [29113749888](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113749888) / 2026-07-11 02:13:51 +0800 | 23.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29114516220](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29114516220) / completed | [29114516220](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29114516220) / success | [29114516220](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29114516220) / 2026-07-11 02:26:30 +0800 | 23.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29115955791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29115955791) / completed | [29115955791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29115955791) / success | [29115955791](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29115955791) / 2026-07-11 02:52:00 +0800 | 22.8h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29125025294](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125025294) / completed | [29125025294](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125025294) / success | [29125025294](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125025294) / 2026-07-11 05:33:05 +0800 | 20.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 142.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 46.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29125050156](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125050156) / completed | [29125050156](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125050156) / success | [29125050156](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125050156) / 2026-07-11 05:33:43 +0800 | 20.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29125049828](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125049828) / completed | [29125049828](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125049828) / success | [29125049828](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29125049828) / 2026-07-11 05:33:15 +0800 | 20.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
