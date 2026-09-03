# Automation Status Report

- Generated at: 2026-09-04 06:41:29 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `d03f0288`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33796243212](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796243212) / completed | [33796243212](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796243212) / success | [33796243212](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796243212) / 2026-09-04 03:25:50 +0800 | 3.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33796336572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796336572) / completed | [33796336572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796336572) / success | [33796336572](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796336572) / 2026-09-04 03:26:08 +0800 | 3.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33796582540](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796582540) / completed | [33796582540](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796582540) / success | [33796582540](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796582540) / 2026-09-04 03:28:34 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33796620954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796620954) / completed | [33796620954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796620954) / success | [33796620954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33796620954) / 2026-09-04 03:28:46 +0800 | 3.2h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33798005033](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33798005033) / completed | [33798005033](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33798005033) / success | [33798005033](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33798005033) / 2026-09-04 03:43:35 +0800 | 3.0h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33799241571](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33799241571) / completed | [33799241571](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33799241571) / success | [33799241571](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33799241571) / 2026-09-04 03:57:46 +0800 | 2.7h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33814214450](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33814214450) / in_progress | [33691813363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33691813363) / success | [33691813363](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33691813363) / 2026-09-03 06:44:47 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / completed | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / success | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / 2026-08-31 04:00:57 +0800 | 98.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 651.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33691863121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33691863121) / completed | [33691863121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33691863121) / success | [33691863121](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33691863121) / 2026-09-03 06:45:21 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33799468320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33799468320) / completed | [33799468320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33799468320) / success | [33799468320](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33799468320) / 2026-09-04 03:57:56 +0800 | 2.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
