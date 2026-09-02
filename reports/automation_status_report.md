# Automation Status Report

- Generated at: 2026-09-03 03:29:33 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `182bb3d6`
- Overall status: `ok`
- Blocking findings: 0
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [33673504402](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673504402) / in_progress | [33550052861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550052861) / success | [33550052861](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550052861) / 2026-09-02 03:33:57 +0800 | 23.9h | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [33673594494](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33673594494) / in_progress | [33550235740](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550235740) / success | [33550235740](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550235740) / 2026-09-02 03:34:24 +0800 | 23.9h | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [33550647937](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550647937) / completed | [33550647937](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550647937) / success | [33550647937](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550647937) / 2026-09-02 03:38:54 +0800 | 23.8h | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [33550689543](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550689543) / completed | [33550689543](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550689543) / success | [33550689543](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33550689543) / 2026-09-02 03:39:20 +0800 | 23.8h | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [33551760657](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33551760657) / completed | [33551760657](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33551760657) / success | [33551760657](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33551760657) / 2026-09-02 03:50:31 +0800 | 23.7h | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | ok | [33552564354](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33552564354) / completed | [33552564354](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33552564354) / success | [33552564354](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33552564354) / 2026-09-02 04:01:01 +0800 | 23.5h | ok |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | ok | [33567558651](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567558651) / completed | [33567558651](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567558651) / success | [33567558651](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567558651) / 2026-09-02 06:42:33 +0800 | 20.8h | ok |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / completed | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / success | [33332376762](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33332376762) / 2026-08-31 04:00:57 +0800 | 71.5h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / completed | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / success | [31210062620](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/31210062620) / 2026-08-08 03:09:25 +0800 | 624.3h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [33567610108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567610108) / completed | [33567610108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567610108) / success | [33567610108](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567610108) / 2026-09-02 06:43:06 +0800 | 20.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [33567649459](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567649459) / completed | [33567649459](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567649459) / success | [33567649459](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/33567649459) / 2026-09-02 06:43:17 +0800 | 20.8h | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
