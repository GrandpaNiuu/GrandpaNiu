# Automation Status Report

- Generated at: 2026-07-03 00:59:04 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28539092511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539092511) / completed | [28539092511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539092511) / success | [28539092511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539092511) / 2026-07-02 02:29:29 +0800 | 22.5h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28539136602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539136602) / completed | [28539136602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539136602) / success | [28539136602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539136602) / 2026-07-02 02:30:09 +0800 | 22.5h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28539292954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539292954) / completed | [28539292954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539292954) / success | [28539292954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539292954) / 2026-07-02 02:32:35 +0800 | 22.4h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28540371201](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28540371201) / completed | [28540371201](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28540371201) / success | [28540371201](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28540371201) / 2026-07-02 02:52:01 +0800 | 22.1h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28541038955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541038955) / completed | [28541038955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541038955) / success | [28541038955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541038955) / 2026-07-02 03:04:02 +0800 | 21.9h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28541625184](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) / completed | [28541625184](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) / success | [28541625184](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) / 2026-07-02 03:15:05 +0800 | 21.7h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / completed | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / success | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / 2026-07-02 05:57:38 +0800 | 19.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 94.2h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [28607412434](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28607412434) / in_progress | [28600035533](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28600035533) / success | [28600035533](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28600035533) / 2026-07-02 23:02:18 +0800 | 1.9h | latest run is in_progress |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28600129191](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28600129191) / completed | [28600129191](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28600129191) / success | [28600129191](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28600129191) / 2026-07-02 23:02:28 +0800 | 1.9h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
