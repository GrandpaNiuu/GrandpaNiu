# Automation Status Report

- Generated at: 2026-09-24 07:01:45 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `646bbe74`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35911604603](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35911604603) / completed | [35911604603](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35911604603) / success | [35911604603](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35911604603) / 2026-09-24 03:48:22 +0800 | 3.2h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35911679076](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35911679076) / completed | [35911679076](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35911679076) / success | [35911679076](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35911679076) / 2026-09-24 03:48:52 +0800 | 3.2h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35912025978](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35912025978) / completed | [35912025978](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35912025978) / success | [35912025978](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35912025978) / 2026-09-24 03:51:26 +0800 | 3.2h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35912189989](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35912189989) / completed | [35912189989](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35912189989) / success | [35912189989](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35912189989) / 2026-09-24 03:52:47 +0800 | 3.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35913992698](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35913992698) / completed | [35913992698](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35913992698) / success | [35913992698](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35913992698) / 2026-09-24 04:09:42 +0800 | 2.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35916180880](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35916180880) / completed | [35916180880](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35916180880) / success | [35916180880](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35916180880) / 2026-09-24 04:30:08 +0800 | 2.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35931454506](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35931454506) / in_progress | [35795790495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795790495) / success | [35795790495](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795790495) / 2026-09-23 07:07:16 +0800 | 23.9h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / completed | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 75.3h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1131.9h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35795842679](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795842679) / completed | [35795842679](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795842679) / success | [35795842679](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35795842679) / 2026-09-23 07:07:51 +0800 | 23.9h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35916372889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35916372889) / completed | [35916372889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35916372889) / success | [35916372889](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35916372889) / 2026-09-24 04:30:18 +0800 | 2.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
