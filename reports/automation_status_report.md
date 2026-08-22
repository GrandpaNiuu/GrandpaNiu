# Automation Status Report

- Generated at: 2026-08-23 00:56:33 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `d2bf0492`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32586169703](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32586169703) / in_progress | [32506136036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506136036) / success | [32506136036](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506136036) / 2026-08-22 01:04:38 +0800 | 23.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32506220352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506220352) / completed | [32506220352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506220352) / success | [32506220352](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32506220352) / 2026-08-22 01:05:04 +0800 | 23.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32507017059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507017059) / completed | [32507017059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507017059) / success | [32507017059](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507017059) / 2026-08-22 01:13:47 +0800 | 23.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32507088407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507088407) / completed | [32507088407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507088407) / success | [32507088407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32507088407) / 2026-08-22 01:14:30 +0800 | 23.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32508997423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32508997423) / completed | [32508997423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32508997423) / success | [32508997423](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32508997423) / 2026-08-22 01:36:45 +0800 | 23.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32510132484](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510132484) / completed | [32510132484](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510132484) / success | [32510132484](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32510132484) / 2026-08-22 01:50:57 +0800 | 23.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32525308927](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525308927) / completed | [32525308927](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525308927) / success | [32525308927](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525308927) / 2026-08-22 04:47:49 +0800 | 20.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / completed | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / success | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / 2026-08-17 01:51:36 +0800 | 143.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 357.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32525371979](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525371979) / completed | [32525371979](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525371979) / success | [32525371979](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525371979) / 2026-08-22 04:48:25 +0800 | 20.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32525421110](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525421110) / completed | [32525421110](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525421110) / success | [32525421110](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32525421110) / 2026-08-22 04:48:34 +0800 | 20.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
