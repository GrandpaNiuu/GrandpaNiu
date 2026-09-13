# Automation Status Report

- Generated at: 2026-09-14 03:43:37 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `8ba3a782`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [34776100546](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776100546) / completed | [34776100546](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776100546) / success | [34776100546](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776100546) / 2026-09-14 02:56:34 +0800 | 47m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [34776141719](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776141719) / completed | [34776141719](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776141719) / success | [34776141719](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776141719) / 2026-09-14 02:57:04 +0800 | 47m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [34776287059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776287059) / completed | [34776287059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776287059) / success | [34776287059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776287059) / 2026-09-14 02:59:44 +0800 | 44m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [34776313105](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776313105) / completed | [34776313105](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776313105) / success | [34776313105](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34776313105) / 2026-09-14 03:00:17 +0800 | 43m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [34777252739](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34777252739) / completed | [34777252739](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34777252739) / success | [34777252739](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34777252739) / 2026-09-14 03:18:29 +0800 | 25m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [34777954061](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34777954061) / completed | [34777954061](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34777954061) / success | [34777954061](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34777954061) / 2026-09-14 03:33:18 +0800 | 10m | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [34722738932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34722738932) / completed | [34722738932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34722738932) / success | [34722738932](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34722738932) / 2026-09-13 06:26:40 +0800 | 21.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / in_progress | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / success | [34054933625](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34054933625) / 2026-09-07 03:28:25 +0800 | 168.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 888.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [34722771471](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34722771471) / completed | [34722771471](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34722771471) / success | [34722771471](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34722771471) / 2026-09-13 06:27:15 +0800 | 21.3h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [34778044231](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778044231) / completed | [34778044231](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778044231) / success | [34778044231](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778044231) / 2026-09-14 03:33:28 +0800 | 10m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
