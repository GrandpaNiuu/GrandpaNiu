# Automation Status Report

- Generated at: 2026-10-27 05:10:50 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `1cd03e17`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40401997239](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40401997239) / in_progress | [40224972488](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40224972488) / success | [40224972488](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40224972488) / 2026-10-26 03:14:36 +0800 | 25.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40402110800](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402110800) / in_progress | [40225061156](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225061156) / success | [40225061156](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225061156) / 2026-10-26 03:14:59 +0800 | 25.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40225318892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225318892) / completed | [40225318892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225318892) / success | [40225318892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225318892) / 2026-10-26 03:17:51 +0800 | 25.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40225481276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225481276) / completed | [40225481276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225481276) / success | [40225481276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225481276) / 2026-10-26 03:19:58 +0800 | 25.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40226303724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40226303724) / completed | [40226303724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40226303724) / success | [40226303724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40226303724) / 2026-10-26 03:30:41 +0800 | 25.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40227433445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40227433445) / completed | [40227433445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40227433445) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40241456202](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241456202) / completed | [40241456202](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241456202) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 25.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 191.6h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40241501612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241501612) / completed | [40241501612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241501612) / success | [40241501612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241501612) / 2026-10-26 06:43:14 +0800 | 22.5h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40241512934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241512934) / completed | [40241512934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241512934) / success | [40241512934](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241512934) / 2026-10-26 06:43:23 +0800 | 22.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
