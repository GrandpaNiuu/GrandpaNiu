# Automation Status Report

- Generated at: 2026-10-27 07:57:55 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `e18511e6`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [40401997239](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40401997239) / completed | [40401997239](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40401997239) / success | [40401997239](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40401997239) / 2026-10-27 05:11:09 +0800 | 2.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [40402110800](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402110800) / completed | [40402110800](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402110800) / success | [40402110800](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402110800) / 2026-10-27 05:11:28 +0800 | 2.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [40402440938](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402440938) / completed | [40402440938](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402440938) / success | [40402440938](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402440938) / 2026-10-27 05:13:28 +0800 | 2.7h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [40402474611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402474611) / completed | [40402474611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402474611) / success | [40402474611](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40402474611) / 2026-10-27 05:13:52 +0800 | 2.7h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [40405144330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40405144330) / completed | [40405144330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40405144330) / success | [40405144330](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40405144330) / 2026-10-27 05:32:48 +0800 | 2.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [40406203405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40406203405) / completed | [40406203405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40406203405) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [40423236259](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40423236259) / in_progress | [40241456202](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241456202) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / completed | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 28.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 194.4h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [40241501612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241501612) / completed | [40241501612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241501612) / success | [40241501612](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40241501612) / 2026-10-26 06:43:14 +0800 | 25.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [40406415928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40406415928) / completed | [40406415928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40406415928) / success | [40406415928](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40406415928) / 2026-10-27 05:41:18 +0800 | 2.3h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
