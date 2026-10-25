# Automation Status Report

- Generated at: 2026-10-26 06:42:46 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `810c6488`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40224972488](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40224972488) / completed | [40224972488](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40224972488) / success | [40224972488](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40224972488) / 2026-10-26 03:14:36 +0800 | 3.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40225061156](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225061156) / completed | [40225061156](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225061156) / success | [40225061156](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225061156) / 2026-10-26 03:14:59 +0800 | 3.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40225318892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225318892) / completed | [40225318892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225318892) / success | [40225318892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225318892) / 2026-10-26 03:17:51 +0800 | 3.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40225481276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225481276) / completed | [40225481276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225481276) / success | [40225481276](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40225481276) / 2026-10-26 03:19:58 +0800 | 3.4h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40226303724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40226303724) / completed | [40226303724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40226303724) / success | [40226303724](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40226303724) / 2026-10-26 03:30:41 +0800 | 3.2h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40227433445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40227433445) / completed | [40227433445](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40227433445) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40241456202](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241456202) / in_progress | [40139268459](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40139268459) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 2.8h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 169.2h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40139327080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40139327080) / completed | [40139327080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40139327080) / success | [40139327080](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40139327080) / 2026-10-25 06:37:13 +0800 | 24.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40228372564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228372564) / completed | [40228372564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228372564) / success | [40228372564](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228372564) / 2026-10-26 03:56:15 +0800 | 2.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
