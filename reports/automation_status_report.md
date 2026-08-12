# Automation Status Report

- Generated at: 2026-08-13 01:36:07 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `70b555bc`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31623358631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31623358631) / in_progress | [31518168516](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518168516) / success | [31518168516](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518168516) / 2026-08-12 01:34:49 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31518439235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518439235) / completed | [31518439235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518439235) / success | [31518439235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518439235) / 2026-08-12 01:37:07 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31519014658](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519014658) / completed | [31519014658](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519014658) / success | [31519014658](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519014658) / 2026-08-12 01:43:57 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31519063710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519063710) / completed | [31519063710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519063710) / success | [31519063710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519063710) / 2026-08-12 01:44:20 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31520479722](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31520479722) / completed | [31520479722](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31520479722) / success | [31520479722](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31520479722) / 2026-08-12 02:01:07 +0800 | 23.6h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31521254986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521254986) / completed | [31521254986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521254986) / success | [31521254986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521254986) / 2026-08-12 02:10:52 +0800 | 23.4h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31536747702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536747702) / completed | [31536747702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536747702) / success | [31536747702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536747702) / 2026-08-12 05:12:46 +0800 | 20.4h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 71.6h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 118.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31536807139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536807139) / completed | [31536807139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536807139) / success | [31536807139](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536807139) / 2026-08-12 05:13:24 +0800 | 20.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31536855812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536855812) / completed | [31536855812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536855812) / success | [31536855812](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536855812) / 2026-08-12 05:13:38 +0800 | 20.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
