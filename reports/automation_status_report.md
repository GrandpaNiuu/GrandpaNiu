# Automation Status Report

- Generated at: 2026-08-22 04:47:21 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `d3b96dde`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32506136036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506136036) / completed | [32506136036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506136036) / success | [32506136036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506136036) / 2026-08-22 01:04:38 +0800 | 3.7h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32506220352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506220352) / completed | [32506220352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506220352) / success | [32506220352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506220352) / 2026-08-22 01:05:04 +0800 | 3.7h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32507017059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507017059) / completed | [32507017059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507017059) / success | [32507017059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507017059) / 2026-08-22 01:13:47 +0800 | 3.6h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32507088407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507088407) / completed | [32507088407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507088407) / success | [32507088407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507088407) / 2026-08-22 01:14:30 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32508997423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32508997423) / completed | [32508997423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32508997423) / success | [32508997423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32508997423) / 2026-08-22 01:36:45 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32510132484](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510132484) / completed | [32510132484](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510132484) / success | [32510132484](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510132484) / 2026-08-22 01:50:57 +0800 | 2.9h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32525308927](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525308927) / in_progress | [32416576653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32416576653) / success | [32416576653](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32416576653) / 2026-08-21 04:54:38 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / completed | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / success | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / 2026-08-17 01:51:36 +0800 | 122.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 337.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32416629613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32416629613) / completed | [32416629613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32416629613) / success | [32416629613](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32416629613) / 2026-08-21 04:55:11 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32510285896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510285896) / completed | [32510285896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510285896) / success | [32510285896](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510285896) / 2026-08-22 01:51:08 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
