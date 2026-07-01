# Automation Status Report

- Generated at: 2026-07-02 02:29:10 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | warn | [28539092511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539092511) / in_progress | [28466573892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466573892) / success | [28466573892](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466573892) / 2026-07-01 02:22:04 +0800 | 24.1h | latest run is in_progress |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28466648339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466648339) / completed | [28466648339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466648339) / success | [28466648339](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466648339) / 2026-07-01 02:22:41 +0800 | 24.1h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28466821509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466821509) / completed | [28466821509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466821509) / success | [28466821509](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466821509) / 2026-07-01 02:25:46 +0800 | 24.1h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28466830220](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466830220) / completed | [28466830220](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466830220) / success | [28466830220](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28466830220) / 2026-07-01 02:26:09 +0800 | 24.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28468892997](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28468892997) / completed | [28468892997](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28468892997) / success | [28468892997](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28468892997) / 2026-07-01 03:01:26 +0800 | 23.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28469457522](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28469457522) / completed | [28469457522](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28469457522) / success | [28469457522](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28469457522) / 2026-07-01 03:12:20 +0800 | 23.3h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28478298525](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28478298525) / completed | [28478298525](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28478298525) / success | [28478298525](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28478298525) / 2026-07-01 05:53:42 +0800 | 20.6h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 71.7h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / completed | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / success | [28244167364](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28244167364) / 2026-06-26 22:24:31 +0800 | 124.1h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28478316032](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28478316032) / completed | [28478316032](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28478316032) / success | [28478316032](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28478316032) / 2026-07-01 05:53:54 +0800 | 20.6h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
