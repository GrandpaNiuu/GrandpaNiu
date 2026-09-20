# Automation Status Report

- Generated at: 2026-09-21 06:35:07 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ec2c84ad`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35530895441](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35530895441) / completed | [35530895441](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35530895441) / success | [35530895441](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35530895441) / 2026-09-21 03:02:08 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35530958463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35530958463) / completed | [35530958463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35530958463) / success | [35530958463](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35530958463) / 2026-09-21 03:02:33 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35531100412](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531100412) / completed | [35531100412](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531100412) / success | [35531100412](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531100412) / 2026-09-21 03:05:01 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35531113399](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531113399) / completed | [35531113399](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531113399) / success | [35531113399](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531113399) / 2026-09-21 03:05:09 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35531968619](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531968619) / completed | [35531968619](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531968619) / success | [35531968619](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35531968619) / 2026-09-21 03:21:02 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35532569268](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35532569268) / completed | [35532569268](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35532569268) / success | [35532569268](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35532569268) / 2026-09-21 03:32:48 +0800 | 3.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35542119116](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35542119116) / in_progress | [35473135337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473135337) / success | [35473135337](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473135337) / 2026-09-20 06:22:53 +0800 | 24.2h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / completed | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / success | [35533124919](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533124919) / 2026-09-21 03:42:36 +0800 | 2.9h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 1059.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35473168301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473168301) / completed | [35473168301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473168301) / success | [35473168301](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35473168301) / 2026-09-20 06:23:22 +0800 | 24.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35533188367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533188367) / completed | [35533188367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533188367) / success | [35533188367](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35533188367) / 2026-09-21 03:42:43 +0800 | 2.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
