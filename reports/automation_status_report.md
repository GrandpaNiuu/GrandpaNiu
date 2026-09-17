# Automation Status Report

- Generated at: 2026-09-18 03:50:17 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `17be6ac4`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [35267138751](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267138751) / in_progress | [35141958145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35141958145) / success | [35141958145](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35141958145) / 2026-09-17 03:42:09 +0800 | 24.1h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [35267212957](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35267212957) / in_progress | [35142010548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142010548) / success | [35142010548](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142010548) / 2026-09-17 03:42:39 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [35142357985](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142357985) / completed | [35142357985](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142357985) / success | [35142357985](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142357985) / 2026-09-17 03:45:00 +0800 | 24.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [35142459005](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142459005) / completed | [35142459005](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142459005) / success | [35142459005](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35142459005) / 2026-09-17 03:45:48 +0800 | 24.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [35143677724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35143677724) / completed | [35143677724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35143677724) / success | [35143677724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35143677724) / 2026-09-17 03:58:32 +0800 | 23.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [35145266887](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35145266887) / completed | [35145266887](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35145266887) / success | [35145266887](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35145266887) / 2026-09-17 04:15:37 +0800 | 23.6h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [35160752453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160752453) / completed | [35160752453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160752453) / success | [35160752453](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160752453) / 2026-09-17 07:06:35 +0800 | 20.7h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / completed | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / success | [34778500468](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/34778500468) / 2026-09-14 03:43:57 +0800 | 96.1h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 984.7h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [35160814955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160814955) / completed | [35160814955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160814955) / success | [35160814955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160814955) / 2026-09-17 07:07:06 +0800 | 20.7h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [35160853717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160853717) / completed | [35160853717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160853717) / success | [35160853717](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/35160853717) / 2026-09-17 07:07:15 +0800 | 20.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
