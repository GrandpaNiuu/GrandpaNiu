# Automation Status Report

- Generated at: 2026-10-01 08:00:57 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `87f310f0`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36776293251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776293251) / completed | [36776293251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776293251) / success | [36776293251](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776293251) / 2026-10-01 04:59:23 +0800 | 3.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36776392984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776392984) / completed | [36776392984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776392984) / success | [36776392984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776392984) / 2026-10-01 04:59:34 +0800 | 3.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36776733762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776733762) / completed | [36776733762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776733762) / success | [36776733762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776733762) / 2026-10-01 05:02:35 +0800 | 3.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36776757356](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776757356) / completed | [36776757356](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776757356) / success | [36776757356](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36776757356) / 2026-10-01 05:03:01 +0800 | 3.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36778916984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36778916984) / completed | [36778916984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36778916984) / success | [36778916984](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36778916984) / 2026-10-01 05:22:31 +0800 | 2.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36779476980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36779476980) / completed | [36779476980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36779476980) / success | [36779476980](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36779476980) / 2026-10-01 05:28:19 +0800 | 2.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36793978555](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36793978555) / in_progress | [36647320881](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647320881) / success | [36647320881](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647320881) / 2026-09-30 07:51:33 +0800 | 24.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / completed | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / success | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / 2026-09-28 04:21:38 +0800 | 75.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1300.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36647391730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647391730) / completed | [36647391730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647391730) / success | [36647391730](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36647391730) / 2026-09-30 07:52:10 +0800 | 24.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36779635190](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36779635190) / completed | [36779635190](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36779635190) / success | [36779635190](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36779635190) / 2026-10-01 05:28:31 +0800 | 2.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
