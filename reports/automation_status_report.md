# Automation Status Report

- Generated at: 2026-08-19 01:01:22 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `efea94b1`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32163314052](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32163314052) / in_progress | [32048173262](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32048173262) / success | [32048173262](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32048173262) / 2026-08-18 00:59:39 +0800 | 24.0h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32048273031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32048273031) / completed | [32048273031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32048273031) / success | [32048273031](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32048273031) / 2026-08-18 01:00:23 +0800 | 24.0h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32049197110](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32049197110) / completed | [32049197110](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32049197110) / success | [32049197110](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32049197110) / 2026-08-18 01:11:47 +0800 | 23.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32049288171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32049288171) / completed | [32049288171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32049288171) / success | [32049288171](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32049288171) / 2026-08-18 01:12:54 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [32050938927](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32050938927) / completed | [32050938927](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32050938927) / success | [32050938927](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32050938927) / 2026-08-18 01:35:21 +0800 | 23.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [32051971595](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32051971595) / completed | [32051971595](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32051971595) / success | [32051971595](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32051971595) / 2026-08-18 01:49:49 +0800 | 23.2h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [32067988333](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32067988333) / completed | [32067988333](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32067988333) / success | [32067988333](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32067988333) / 2026-08-18 04:51:38 +0800 | 20.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / completed | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / success | [31962783416](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31962783416) / 2026-08-17 01:51:36 +0800 | 47.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 261.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32068048310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068048310) / completed | [32068048310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068048310) / success | [32068048310](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068048310) / 2026-08-18 04:52:13 +0800 | 20.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [32068103567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068103567) / completed | [32068103567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068103567) / success | [32068103567](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32068103567) / 2026-08-18 04:52:25 +0800 | 20.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
