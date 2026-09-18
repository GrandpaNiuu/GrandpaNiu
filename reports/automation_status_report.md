# Automation Status Report

- Generated at: 2026-09-19 06:42:49 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `40338530`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35384337672](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384337672) / completed | [35384337672](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384337672) / success | [35384337672](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384337672) / 2026-09-19 03:10:42 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35384451890](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384451890) / completed | [35384451890](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384451890) / success | [35384451890](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384451890) / 2026-09-19 03:11:05 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35384759702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384759702) / completed | [35384759702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384759702) / success | [35384759702](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384759702) / 2026-09-19 03:14:23 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35384786329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384786329) / completed | [35384786329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384786329) / success | [35384786329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35384786329) / 2026-09-19 03:14:32 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35386284503](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35386284503) / completed | [35386284503](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35386284503) / success | [35386284503](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35386284503) / 2026-09-19 03:30:59 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35387451425](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35387451425) / completed | [35387451425](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35387451425) / success | [35387451425](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35387451425) / 2026-09-19 03:44:20 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35402727925](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35402727925) / in_progress | [35284558433](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35284558433) / success | [35284558433](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35284558433) / 2026-09-18 06:57:56 +0800 | 23.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / completed | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / success | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / 2026-09-14 03:43:57 +0800 | 123.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1011.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35284605103](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35284605103) / completed | [35284605103](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35284605103) / success | [35284605103](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35284605103) / 2026-09-18 06:58:33 +0800 | 23.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35387608715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35387608715) / completed | [35387608715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35387608715) / success | [35387608715](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35387608715) / 2026-09-19 03:44:30 +0800 | 3.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
