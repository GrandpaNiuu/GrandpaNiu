# Automation Status Report

- Generated at: 2026-11-02 05:22:06 +0800
- Repository: `GrandpaNiuu/GrandpaNiu`
- Current commit: `e2cf2fe7`
- Overall status: `fail`
- Blocking findings: 4
- Warnings: 0

## Workflow Status

| Workflow | Cadence | Required | State | Latest run | Latest completed | Last success | Success age | Notes |
|---|---|---:|---|---|---|---|---:|---|
| `daily-module-update.yml` | daily, Beijing 00:37 | yes | ok | [41348665234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348665234) / completed | [41348665234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348665234) / success | [41348665234](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348665234) / 2026-11-02 04:48:59 +0800 | 33m | ok |
| `daily-audit-and-repair.yml` | daily, Beijing 00:43 | yes | ok | [41348737585](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348737585) / completed | [41348737585](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348737585) / success | [41348737585](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348737585) / 2026-11-02 04:49:13 +0800 | 33m | ok |
| `daily-invalid-source-repair.yml` | daily, Beijing 00:49 | yes | ok | [41348991876](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348991876) / completed | [41348991876](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348991876) / success | [41348991876](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41348991876) / 2026-11-02 04:52:09 +0800 | 30m | ok |
| `upstream-collect.yml` | daily, Beijing 00:55 | yes | ok | [41349030432](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41349030432) / completed | [41349030432](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41349030432) / success | [41349030432](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41349030432) / 2026-11-02 04:52:29 +0800 | 30m | ok |
| `scheduled-module-update.yml` | daily, Beijing 01:07 | yes | ok | [41350002405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41350002405) / completed | [41350002405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41350002405) / success | [41350002405](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41350002405) / 2026-11-02 05:04:19 +0800 | 18m | ok |
| `upstream-app-module-sync.yml` | daily, Beijing 01:19 | yes | fail | [41351010077](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351010077) / completed | [41351010077](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351010077) / failure | [41132060349](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41132060349) / 2026-10-31 05:35:28 +0800 | 47.8h | last success is stale (47.8h > 40h)<br>latest completed run is failure |
| `daily-schedule-watchdog.yml` | daily, Beijing 04:30 | yes | fail | [41252846521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41252846521) / completed | [41252846521](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41252846521) / failure | n/a / n/a | n/a | no successful completed run found<br>latest completed run is failure |
| `repository-health.yml` | weekly, Sunday Beijing 01:37 | yes | ok | [41351542002](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351542002) / in_progress | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / success | [40228240054](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/40228240054) / 2026-10-26 03:56:06 +0800 | 169.4h | ok |
| `module-factory-build.yml` | push/manual | observe | ok | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / completed | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / success | [39168147194](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/39168147194) / 2026-10-19 05:32:01 +0800 | 335.8h | ok |
| `pages-deploy.yml` | Module Factory / watchdog / manual | observe | ok | [41252903356](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41252903356) / completed | [41252903356](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41252903356) / success | [41252903356](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41252903356) / 2026-11-01 07:31:49 +0800 | 21.8h | ok |
| `workflow-failure-issue.yml` | workflow_run | observe | ok | [41351278809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351278809) / completed | [41351278809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351278809) / success | [41351278809](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/41351278809) / 2026-11-02 05:18:01 +0800 | 4m | ok |

## Policy

- Daily maintenance workflows should have a successful completed run within 40 hours.
- The watchdog itself is allowed 48 hours because it validates the previous run while the current run is still in progress.
- Repository health is weekly and should have a successful completed run within 9 days.
- Push-triggered and workflow-run issue workflows are observed but do not block on age.
- A latest failure on an older commit is a warning, not a blocker, when a fresh successful run still exists and the current commit is newer.
- Local API/network failures do not block local development; strict mode in the watchdog blocks real stale or failed scheduled automation.
