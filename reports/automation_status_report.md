# Automation Status Report

- Generated at: 2026-09-05 06:26:09 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `940fc4a4`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33909358330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909358330) / completed | [33909358330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909358330) / success | [33909358330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909358330) / 2026-09-05 03:07:26 +0800 | 3.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33909474959](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909474959) / completed | [33909474959](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909474959) / success | [33909474959](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909474959) / 2026-09-05 03:07:41 +0800 | 3.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33909711263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909711263) / completed | [33909711263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909711263) / success | [33909711263](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909711263) / 2026-09-05 03:10:21 +0800 | 3.3h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33909742112](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909742112) / completed | [33909742112](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909742112) / success | [33909742112](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33909742112) / 2026-09-05 03:10:33 +0800 | 3.3h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33910893360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33910893360) / completed | [33910893360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33910893360) / success | [33910893360](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33910893360) / 2026-09-05 03:23:55 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33912372402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33912372402) / completed | [33912372402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33912372402) / success | [33912372402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33912372402) / 2026-09-05 03:42:22 +0800 | 2.7h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33925474986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33925474986) / in_progress | [33814214450](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814214450) / success | [33814214450](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814214450) / 2026-09-04 06:41:56 +0800 | 23.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / completed | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / success | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / 2026-08-31 04:00:57 +0800 | 122.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 675.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33814272087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814272087) / completed | [33814272087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814272087) / success | [33814272087](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814272087) / 2026-09-04 06:42:31 +0800 | 23.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33912529636](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33912529636) / completed | [33912529636](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33912529636) / success | [33912529636](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33912529636) / 2026-09-05 03:42:30 +0800 | 2.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
