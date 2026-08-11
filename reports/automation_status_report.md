# Automation Status Report

- Generated at: 2026-08-12 05:12:20 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `160fc384`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31518168516](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518168516) / completed | [31518168516](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518168516) / success | [31518168516](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518168516) / 2026-08-12 01:34:49 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31518439235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518439235) / completed | [31518439235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518439235) / success | [31518439235](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518439235) / 2026-08-12 01:37:07 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31519014658](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519014658) / completed | [31519014658](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519014658) / success | [31519014658](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519014658) / 2026-08-12 01:43:57 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31519063710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519063710) / completed | [31519063710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519063710) / success | [31519063710](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31519063710) / 2026-08-12 01:44:20 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31520479722](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31520479722) / completed | [31520479722](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31520479722) / success | [31520479722](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31520479722) / 2026-08-12 02:01:07 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31521254986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521254986) / completed | [31521254986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521254986) / success | [31521254986](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521254986) / 2026-08-12 02:10:52 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31536747702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31536747702) / in_progress | [31432549341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432549341) / success | [31432549341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432549341) / 2026-08-11 05:10:45 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 51.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 98.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31432624363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432624363) / completed | [31432624363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432624363) / success | [31432624363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432624363) / 2026-08-11 05:11:16 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31521382474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521382474) / completed | [31521382474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521382474) / success | [31521382474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31521382474) / 2026-08-12 02:11:06 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
