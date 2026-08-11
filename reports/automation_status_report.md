# Automation Status Report

- Generated at: 2026-08-12 01:34:27 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `1c320522`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31518168516](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31518168516) / in_progress | [31414377580](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414377580) / success | [31414377580](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414377580) / 2026-08-11 01:31:47 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31414569645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414569645) / completed | [31414569645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414569645) / success | [31414569645](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31414569645) / 2026-08-11 01:33:28 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31415049511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415049511) / completed | [31415049511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415049511) / success | [31415049511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415049511) / 2026-08-11 01:39:12 +0800 | 23.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31415085810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415085810) / completed | [31415085810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415085810) / success | [31415085810](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31415085810) / 2026-08-11 01:39:30 +0800 | 23.9h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31416391970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31416391970) / completed | [31416391970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31416391970) / success | [31416391970](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31416391970) / 2026-08-11 01:55:17 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31417385897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417385897) / completed | [31417385897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417385897) / success | [31417385897](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31417385897) / 2026-08-11 02:07:38 +0800 | 23.4h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31432549341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432549341) / completed | [31432549341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432549341) / success | [31432549341](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432549341) / 2026-08-11 05:10:45 +0800 | 20.4h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 47.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 94.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31432624363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432624363) / completed | [31432624363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432624363) / success | [31432624363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432624363) / 2026-08-11 05:11:16 +0800 | 20.4h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31432661725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432661725) / completed | [31432661725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432661725) / success | [31432661725](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31432661725) / 2026-08-11 05:11:24 +0800 | 20.4h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
