# Automation Status Report

- Generated at: 2026-08-27 07:54:29 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `29f92a5d`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [32999170743](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999170743) / completed | [32999170743](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999170743) / success | [32999170743](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999170743) / 2026-08-27 02:22:27 +0800 | 5.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [32999149240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999149240) / completed | [32999149240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999149240) / success | [32999149240](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999149240) / 2026-08-27 02:21:12 +0800 | 5.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [32999751661](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999751661) / completed | [32999751661](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999751661) / success | [32999751661](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999751661) / 2026-08-27 02:27:55 +0800 | 5.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [32999797344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999797344) / completed | [32999797344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999797344) / success | [32999797344](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32999797344) / 2026-08-27 02:28:11 +0800 | 5.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33003814856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33003814856) / completed | [33003814856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33003814856) / success | [33003814856](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33003814856) / 2026-08-27 03:12:10 +0800 | 4.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33004808445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33004808445) / completed | [33004808445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33004808445) / success | [33004808445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33004808445) / 2026-08-27 03:23:57 +0800 | 4.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33024913095](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33024913095) / in_progress | [32897907188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897907188) / success | [32897907188](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897907188) / 2026-08-26 04:53:49 +0800 | 27.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / completed | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / success | [32656139329](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32656139329) / 2026-08-24 01:52:11 +0800 | 78.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 460.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [32897983050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897983050) / completed | [32897983050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897983050) / success | [32897983050](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/32897983050) / 2026-08-26 04:54:25 +0800 | 27.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33004936134](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33004936134) / completed | [33004936134](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33004936134) / success | [33004936134](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33004936134) / 2026-08-27 03:24:06 +0800 | 4.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
