# Automation Status Report

- Generated at: 2026-07-30 01:52:03 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `5c34d622`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [30477198407](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30477198407) / in_progress | [30385455438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385455438) / success | [30385455438](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385455438) / 2026-07-29 02:01:39 +0800 | 23.8h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [30385548729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385548729) / completed | [30385548729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385548729) / success | [30385548729](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385548729) / 2026-07-29 02:01:54 +0800 | 23.8h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [30385744627](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385744627) / completed | [30385744627](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385744627) / success | [30385744627](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385744627) / 2026-07-29 02:05:00 +0800 | 23.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [30385761949](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385761949) / completed | [30385761949](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385761949) / success | [30385761949](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30385761949) / 2026-07-29 02:05:14 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [30386952953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30386952953) / completed | [30386952953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30386952953) / success | [30386952953](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30386952953) / 2026-07-29 02:20:47 +0800 | 23.5h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [30389240875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389240875) / completed | [30389240875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389240875) / success | [30389240875](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30389240875) / 2026-07-29 02:51:48 +0800 | 23.0h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [30401333776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401333776) / completed | [30401333776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401333776) / success | [30401333776](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401333776) / 2026-07-29 05:36:55 +0800 | 20.3h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / completed | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / success | [30215092898](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30215092898) / 2026-07-27 02:38:20 +0800 | 71.2h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / completed | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / success | [29446746558](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/29446746558) / 2026-07-16 04:03:26 +0800 | 333.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [30401388805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401388805) / completed | [30401388805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401388805) / success | [30401388805](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401388805) / 2026-07-29 05:37:34 +0800 | 20.2h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [30401431207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401431207) / completed | [30401431207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401431207) / success | [30401431207](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/30401431207) / 2026-07-29 05:37:52 +0800 | 20.2h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
