# Automation Status Report

- Generated at: 2026-08-27 02:22:08 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `5fd8f3e4`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32999170743](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999170743) / in_progress | [32876068348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876068348) / success | [32876068348](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876068348) / 2026-08-26 01:09:19 +0800 | 25.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32999149240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999149240) / completed | [32999149240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999149240) / success | [32999149240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999149240) / 2026-08-27 02:21:12 +0800 | 1m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32876951074](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876951074) / completed | [32876951074](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876951074) / success | [32876951074](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32876951074) / 2026-08-26 01:17:32 +0800 | 25.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32877044467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32877044467) / completed | [32877044467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32877044467) / success | [32877044467](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32877044467) / 2026-08-26 01:18:17 +0800 | 25.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32878968670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32878968670) / completed | [32878968670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32878968670) / success | [32878968670](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32878968670) / 2026-08-26 01:38:12 +0800 | 24.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32880041578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880041578) / completed | [32880041578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880041578) / success | [32880041578](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32880041578) / 2026-08-26 01:50:49 +0800 | 24.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32897907188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897907188) / completed | [32897907188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897907188) / success | [32897907188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897907188) / 2026-08-26 04:53:49 +0800 | 21.5h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / completed | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 72.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 455.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32897983050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897983050) / completed | [32897983050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897983050) / success | [32897983050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897983050) / 2026-08-26 04:54:25 +0800 | 21.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32999230928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999230928) / completed | [32999230928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999230928) / success | [32999230928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999230928) / 2026-08-27 02:21:41 +0800 | 0m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
