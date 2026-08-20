# Automation Status Report

- Generated at: 2026-08-21 04:54:19 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `e119dc48`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32395476457](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32395476457) / completed | [32395476457](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32395476457) / success | [32395476457](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32395476457) / 2026-08-21 01:04:39 +0800 | 3.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32395544573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32395544573) / completed | [32395544573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32395544573) / success | [32395544573](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32395544573) / 2026-08-21 01:05:09 +0800 | 3.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32396351780](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32396351780) / completed | [32396351780](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32396351780) / success | [32396351780](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32396351780) / 2026-08-21 01:13:28 +0800 | 3.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32396460117](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32396460117) / completed | [32396460117](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32396460117) / success | [32396460117](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32396460117) / 2026-08-21 01:14:25 +0800 | 3.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32398548011](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32398548011) / completed | [32398548011](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32398548011) / success | [32398548011](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32398548011) / 2026-08-21 01:37:17 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32399719114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32399719114) / completed | [32399719114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32399719114) / success | [32399719114](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32399719114) / 2026-08-21 01:50:30 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32416576653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32416576653) / in_progress | [32300840392](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32300840392) / success | [32300840392](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32300840392) / 2026-08-20 04:53:04 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / completed | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / success | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / 2026-08-17 01:51:36 +0800 | 99.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 313.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32300956908](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32300956908) / completed | [32300956908](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32300956908) / success | [32300956908](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32300956908) / 2026-08-20 04:53:36 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32399843066](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32399843066) / completed | [32399843066](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32399843066) / success | [32399843066](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32399843066) / 2026-08-21 01:50:41 +0800 | 3.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
