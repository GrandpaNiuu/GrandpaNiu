# Automation Status Report

- Generated at: 2026-07-10 02:22:26 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `1b8308ed`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [29040380502](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29040380502) / in_progress | [28964745710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28964745710) / success | [28964745710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28964745710) / 2026-07-09 02:05:01 +0800 | 24.3h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28964786852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28964786852) / completed | [28964786852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28964786852) / success | [28964786852](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28964786852) / 2026-07-09 02:05:33 +0800 | 24.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28965009554](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965009554) / completed | [28965009554](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965009554) / success | [28965009554](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965009554) / 2026-07-09 02:09:00 +0800 | 24.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28965037244](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965037244) / completed | [28965037244](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965037244) / success | [28965037244](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965037244) / 2026-07-09 02:09:18 +0800 | 24.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28965903905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965903905) / completed | [28965903905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965903905) / success | [28965903905](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28965903905) / 2026-07-09 02:24:03 +0800 | 24.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28967559474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28967559474) / completed | [28967559474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28967559474) / success | [28967559474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28967559474) / 2026-07-09 02:51:39 +0800 | 23.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28977562121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) / completed | [28977562121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) / success | [28977562121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977562121) / 2026-07-09 05:39:06 +0800 | 20.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / completed | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / success | [28750952237](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28750952237) / 2026-07-06 02:41:30 +0800 | 95.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / completed | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / success | [28897414070](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28897414070) / 2026-07-08 04:47:11 +0800 | 45.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [28977602081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602081) / completed | [28977602081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602081) / success | [28977602081](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602081) / 2026-07-09 05:39:40 +0800 | 20.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28977602053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602053) / completed | [28977602053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602053) / success | [28977602053](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28977602053) / 2026-07-09 05:39:17 +0800 | 20.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
