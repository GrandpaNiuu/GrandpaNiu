# Automation Status Report

- Generated at: 2026-09-29 08:27:39 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `4db44a89`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [36491268454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491268454) / completed | [36491268454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491268454) / success | [36491268454](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491268454) / 2026-09-29 06:16:42 +0800 | 2.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [36491332112](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491332112) / completed | [36491332112](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491332112) / success | [36491332112](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491332112) / 2026-09-29 06:17:06 +0800 | 2.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [36491455918](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491455918) / completed | [36491455918](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491455918) / success | [36491455918](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491455918) / 2026-09-29 06:17:39 +0800 | 2.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [36491485726](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491485726) / completed | [36491485726](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491485726) / success | [36491485726](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36491485726) / 2026-09-29 06:17:47 +0800 | 2.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [36492641895](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36492641895) / completed | [36492641895](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36492641895) / success | [36492641895](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36492641895) / 2026-09-29 06:29:43 +0800 | 2.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [36493135301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36493135301) / completed | [36493135301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36493135301) / success | [36493135301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36493135301) / 2026-09-29 06:35:39 +0800 | 1.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [36503173687](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36503173687) / in_progress | [36357877811](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357877811) / success | [36357877811](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357877811) / 2026-09-28 07:12:40 +0800 | 25.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / completed | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / success | [36347669685](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36347669685) / 2026-09-28 04:21:38 +0800 | 28.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1253.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [36357918809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357918809) / completed | [36357918809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357918809) / success | [36357918809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36357918809) / 2026-09-28 07:13:12 +0800 | 25.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [36493309829](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36493309829) / completed | [36493309829](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36493309829) / success | [36493309829](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/36493309829) / 2026-09-29 06:35:50 +0800 | 1.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
