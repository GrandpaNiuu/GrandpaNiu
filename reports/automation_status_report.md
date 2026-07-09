# Automation Status Report

- Generated at: 2026-07-10 03:16:28 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `87b62e3b`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / completed | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / success | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / 2026-07-10 02:22:43 +0800 | 54m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [29040504976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) / completed | [29040504976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) / success | [29040504976](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040504976) / 2026-07-10 02:24:35 +0800 | 52m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / completed | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / success | [29040858733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040858733) / 2026-07-10 02:30:05 +0800 | 46m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / completed | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / success | [29040964440](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040964440) / 2026-07-10 02:31:44 +0800 | 45m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / completed | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / success | [29042372852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042372852) / 2026-07-10 02:54:48 +0800 | 22m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / completed | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / success | [29042810749](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042810749) / 2026-07-10 03:02:59 +0800 | 13m | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28977562121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) / completed | [28977562121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) / success | [28977562121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) / 2026-07-09 05:39:06 +0800 | 21.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 96.6h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [29043671576](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29043671576) / in_progress | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / success | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / 2026-07-08 04:47:11 +0800 | 46.5h | latest run is in_progress |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [28977602081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602081) / completed | [28977602081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602081) / success | [28977602081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602081) / 2026-07-09 05:39:40 +0800 | 21.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [29042918933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042918933) / completed | [29042918933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042918933) / success | [29042918933](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29042918933) / 2026-07-10 03:03:13 +0800 | 13m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
