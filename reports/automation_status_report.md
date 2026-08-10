# Automation Status Report

- Generated at: 2026-08-11 05:10:18 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `564ade48`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31414377580](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414377580) / completed | [31414377580](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414377580) / success | [31414377580](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414377580) / 2026-08-11 01:31:47 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31414569645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414569645) / completed | [31414569645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414569645) / success | [31414569645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414569645) / 2026-08-11 01:33:28 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31415049511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415049511) / completed | [31415049511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415049511) / success | [31415049511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415049511) / 2026-08-11 01:39:12 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31415085810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415085810) / completed | [31415085810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415085810) / success | [31415085810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415085810) / 2026-08-11 01:39:30 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31416391970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31416391970) / completed | [31416391970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31416391970) / success | [31416391970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31416391970) / 2026-08-11 01:55:17 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31417385897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417385897) / completed | [31417385897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417385897) / success | [31417385897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417385897) / 2026-08-11 02:07:38 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31432549341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432549341) / in_progress | [31335718929](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31335718929) / success | [31335718929](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31335718929) / 2026-08-10 05:01:34 +0800 | 24.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 27.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 74.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31335756416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31335756416) / completed | [31335756416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31335756416) / success | [31335756416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31335756416) / 2026-08-10 05:02:11 +0800 | 24.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31417506037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417506037) / completed | [31417506037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417506037) / success | [31417506037](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417506037) / 2026-08-11 02:07:59 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
