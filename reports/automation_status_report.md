# Automation Status Report

- Generated at: 2026-07-11 02:10:37 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `68deda53`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 2

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [29113562589](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113562589) / in_progress | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / success | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / 2026-07-10 02:22:43 +0800 | 23.8h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | warn | [29113596453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29113596453) / in_progress | [29040504976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) / success | [29040504976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) / 2026-07-10 02:24:35 +0800 | 23.8h | latest run is in_progress |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / completed | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / success | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / 2026-07-10 02:30:05 +0800 | 23.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / completed | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / success | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / 2026-07-10 02:31:44 +0800 | 23.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / completed | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / success | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / 2026-07-10 02:54:48 +0800 | 23.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / completed | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / success | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / 2026-07-10 03:02:59 +0800 | 23.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [29052878712](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052878712) / completed | [29052878712](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052878712) / success | [29052878712](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052878712) / 2026-07-10 05:54:28 +0800 | 20.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 119.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 22.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29052905918](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052905918) / completed | [29052905918](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052905918) / success | [29052905918](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052905918) / 2026-07-10 05:55:01 +0800 | 20.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29052906093](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052906093) / completed | [29052906093](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052906093) / success | [29052906093](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052906093) / 2026-07-10 05:54:39 +0800 | 20.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
