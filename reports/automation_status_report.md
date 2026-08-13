# Automation Status Report

- Generated at: 2026-08-14 05:11:56 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `22760f42`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [31726411442](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31726411442) / completed | [31726411442](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31726411442) / success | [31726411442](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31726411442) / 2026-08-14 01:36:13 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [31726660232](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31726660232) / completed | [31726660232](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31726660232) / success | [31726660232](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31726660232) / 2026-08-14 01:38:12 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [31727187186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31727187186) / completed | [31727187186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31727187186) / success | [31727187186](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31727187186) / 2026-08-14 01:44:43 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [31727256455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31727256455) / completed | [31727256455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31727256455) / success | [31727256455](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31727256455) / 2026-08-14 01:45:26 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [31728573249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31728573249) / completed | [31728573249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31728573249) / success | [31728573249](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31728573249) / 2026-08-14 02:01:26 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [31729393743](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31729393743) / completed | [31729393743](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31729393743) / success | [31729393743](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31729393743) / 2026-08-14 02:11:34 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [31744516125](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31744516125) / in_progress | [31641317575](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31641317575) / success | [31641317575](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31641317575) / 2026-08-13 05:11:48 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / completed | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / success | [31327952865](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31327952865) / 2026-08-10 02:02:48 +0800 | 99.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 146.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [31641380217](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31641380217) / completed | [31641380217](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31641380217) / success | [31641380217](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31641380217) / 2026-08-13 05:12:27 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [31729501733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31729501733) / completed | [31729501733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31729501733) / success | [31729501733](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31729501733) / 2026-08-14 02:11:45 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
