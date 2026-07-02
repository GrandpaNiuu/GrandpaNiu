# Automation Status Report

- Generated at: 2026-07-02 12:26:11 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Overall status: `warn`
- Blocking findings: 0
- Warnings: 1

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [28539092511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539092511) / completed | [28539092511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539092511) / success | [28539092511](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539092511) / 2026-07-02 02:29:29 +0800 | 9.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [28539136602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539136602) / completed | [28539136602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539136602) / success | [28539136602](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539136602) / 2026-07-02 02:30:09 +0800 | 9.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [28539292954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539292954) / completed | [28539292954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539292954) / success | [28539292954](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28539292954) / 2026-07-02 02:32:35 +0800 | 9.9h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [28540371201](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28540371201) / completed | [28540371201](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28540371201) / success | [28540371201](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28540371201) / 2026-07-02 02:52:01 +0800 | 9.6h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [28541038955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541038955) / completed | [28541038955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541038955) / success | [28541038955](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541038955) / 2026-07-02 03:04:02 +0800 | 9.4h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [28541625184](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) / completed | [28541625184](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) / success | [28541625184](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28541625184) / 2026-07-02 03:15:05 +0800 | 9.2h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / completed | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / success | [28550399745](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28550399745) / 2026-07-02 05:57:38 +0800 | 6.5h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / completed | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / success | [28332332245](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28332332245) / 2026-06-29 02:48:00 +0800 | 81.6h | ok |
| `module-factory-build.yml` | push/manual | observe | warn | [28565310634](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28565310634) / in_progress | [28561960172](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28561960172) / success | [28561960172](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28561960172) / 2026-07-02 10:53:28 +0800 | 1.5h | latest run is in_progress |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [28561997109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28561997109) / completed | [28561997109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28561997109) / success | [28561997109](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/28561997109) / 2026-07-02 10:53:40 +0800 | 1.5h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
