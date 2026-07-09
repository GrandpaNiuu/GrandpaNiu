# Automation Status Report

- Generated at: 2026-07-10 05:54:10 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `37c75778`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / completed | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / success | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / 2026-07-10 02:22:43 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29040504976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) / completed | [29040504976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) / success | [29040504976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) / 2026-07-10 02:24:35 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / completed | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / success | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / 2026-07-10 02:30:05 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / completed | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / success | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / 2026-07-10 02:31:44 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / completed | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / success | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / 2026-07-10 02:54:48 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / completed | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / success | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / 2026-07-10 03:02:59 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | warn | [29052878712](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29052878712) / in_progress | [28977562121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) / success | [28977562121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) / 2026-07-09 05:39:06 +0800 | 24.3h | latest run is in_progress |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 99.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / completed | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / success | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / 2026-07-10 03:16:51 +0800 | 2.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [29043759578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043759578) / completed | [29043759578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043759578) / success | [29043759578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043759578) / 2026-07-10 03:17:26 +0800 | 2.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29043759517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043759517) / completed | [29043759517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043759517) / success | [29043759517](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043759517) / 2026-07-10 03:17:05 +0800 | 2.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
