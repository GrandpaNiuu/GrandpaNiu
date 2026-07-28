# Automation Status Report

- Generated at: 2026-07-29 05:36:23 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `ba369106`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30385455438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385455438) / completed | [30385455438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385455438) / success | [30385455438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385455438) / 2026-07-29 02:01:39 +0800 | 3.6h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30385548729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385548729) / completed | [30385548729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385548729) / success | [30385548729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385548729) / 2026-07-29 02:01:54 +0800 | 3.6h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30385744627](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385744627) / completed | [30385744627](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385744627) / success | [30385744627](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385744627) / 2026-07-29 02:05:00 +0800 | 3.5h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30385761949](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385761949) / completed | [30385761949](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385761949) / success | [30385761949](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385761949) / 2026-07-29 02:05:14 +0800 | 3.5h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30386952953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30386952953) / completed | [30386952953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30386952953) / success | [30386952953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30386952953) / 2026-07-29 02:20:47 +0800 | 3.3h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30389240875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389240875) / completed | [30389240875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389240875) / success | [30389240875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389240875) / 2026-07-29 02:51:48 +0800 | 2.7h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30401333776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401333776) / in_progress | [30307518208](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307518208) / success | [30307518208](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307518208) / 2026-07-28 05:36:30 +0800 | 24.0h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 51.0h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 313.5h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30307567631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307567631) / completed | [30307567631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307567631) / success | [30307567631](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30307567631) / 2026-07-28 05:37:09 +0800 | 24.0h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30389368474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389368474) / completed | [30389368474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389368474) / success | [30389368474](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389368474) / 2026-07-29 02:52:00 +0800 | 2.7h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
