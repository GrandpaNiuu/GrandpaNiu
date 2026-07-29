# Automation Status Report

- Generated at: 2026-07-30 05:25:25 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `83956f33`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30477198407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477198407) / completed | [30477198407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477198407) / success | [30477198407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477198407) / 2026-07-30 01:52:28 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30477311875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477311875) / completed | [30477311875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477311875) / success | [30477311875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477311875) / 2026-07-30 01:53:07 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30477763466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477763466) / completed | [30477763466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477763466) / success | [30477763466](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477763466) / 2026-07-30 01:59:09 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30477823941](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477823941) / completed | [30477823941](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477823941) / success | [30477823941](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477823941) / 2026-07-30 01:59:26 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30478785030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30478785030) / completed | [30478785030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30478785030) / success | [30478785030](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30478785030) / 2026-07-30 02:12:08 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30479129411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479129411) / completed | [30479129411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479129411) / success | [30479129411](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479129411) / 2026-07-30 02:17:33 +0800 | 3.1h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30492292817](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30492292817) / in_progress | [30401333776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401333776) / success | [30401333776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401333776) / 2026-07-29 05:36:55 +0800 | 23.8h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 74.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 337.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30401388805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401388805) / completed | [30401388805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401388805) / success | [30401388805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401388805) / 2026-07-29 05:37:34 +0800 | 23.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30479246300](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479246300) / completed | [30479246300](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479246300) / success | [30479246300](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30479246300) / 2026-07-30 02:17:47 +0800 | 3.1h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
