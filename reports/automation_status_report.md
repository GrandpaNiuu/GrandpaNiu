# Automation Status Report

- Generated at: 2026-07-31 02:00:34 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `02c49a94`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30568452790](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30568452790) / in_progress | [30477198407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477198407) / success | [30477198407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477198407) / 2026-07-30 01:52:28 +0800 | 24.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30477311875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477311875) / completed | [30477311875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477311875) / success | [30477311875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477311875) / 2026-07-30 01:53:07 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30477763466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477763466) / completed | [30477763466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477763466) / success | [30477763466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477763466) / 2026-07-30 01:59:09 +0800 | 24.0h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30477823941](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477823941) / completed | [30477823941](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477823941) / success | [30477823941](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477823941) / 2026-07-30 01:59:26 +0800 | 24.0h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30478785030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30478785030) / completed | [30478785030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30478785030) / success | [30478785030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30478785030) / 2026-07-30 02:12:08 +0800 | 23.8h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30479129411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479129411) / completed | [30479129411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479129411) / success | [30479129411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479129411) / 2026-07-30 02:17:33 +0800 | 23.7h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30492292817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492292817) / completed | [30492292817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492292817) / success | [30492292817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492292817) / 2026-07-30 05:25:48 +0800 | 20.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 95.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 358.0h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30492338623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492338623) / completed | [30492338623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492338623) / success | [30492338623](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492338623) / 2026-07-30 05:26:24 +0800 | 20.6h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30492376420](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492376420) / completed | [30492376420](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492376420) / success | [30492376420](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492376420) / 2026-07-30 05:26:33 +0800 | 20.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
