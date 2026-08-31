# Automation Status Report

- Generated at: 2026-09-01 07:57:45 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `0314e52e`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33442160122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442160122) / completed | [33442160122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442160122) / success | [33442160122](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442160122) / 2026-09-01 05:37:08 +0800 | 2.3h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33442227882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442227882) / completed | [33442227882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442227882) / success | [33442227882](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442227882) / 2026-09-01 05:37:33 +0800 | 2.3h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33442411721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442411721) / completed | [33442411721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442411721) / success | [33442411721](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442411721) / 2026-09-01 05:39:29 +0800 | 2.3h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33442450133](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442450133) / completed | [33442450133](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442450133) / success | [33442450133](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33442450133) / 2026-09-01 05:39:42 +0800 | 2.3h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33443421662](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443421662) / completed | [33443421662](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443421662) / success | [33443421662](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443421662) / 2026-09-01 05:52:12 +0800 | 2.1h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33443737617](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443737617) / completed | [33443737617](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443737617) / success | [33443737617](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443737617) / 2026-09-01 05:57:00 +0800 | 2.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33452817649](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33452817649) / in_progress | [33340288462](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33340288462) / success | [33340288462](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33340288462) / 2026-08-31 06:52:47 +0800 | 25.1h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / completed | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / success | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / 2026-08-31 04:00:57 +0800 | 27.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 580.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33340317433](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33340317433) / completed | [33340317433](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33340317433) / success | [33340317433](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33340317433) / 2026-08-31 06:53:21 +0800 | 25.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33443872688](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443872688) / completed | [33443872688](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443872688) / success | [33443872688](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33443872688) / 2026-09-01 05:57:10 +0800 | 2.0h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
