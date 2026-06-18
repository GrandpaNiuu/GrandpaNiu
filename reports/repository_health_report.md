# Repository Health Report

- Generated at: 2026-06-19 04:37:19 +0800
- Blocking issues: 0
- Root and Release identical: yes
- Fusion profile finalized: yes
- validate_repository.py: passed
- automated quality evidence: passed
- node --check Scripts/app-cleaner.js: passed
- Script entries: 26
- MITM hostnames: 1189

## Section Counts

- [Rule]: 946
- [URL Rewrite]: 2490
- [Header Rewrite]: 1
- [Body Rewrite]: 1652
- [Map Local]: 351
- [Script]: 86
- [MITM]: 1

## Blocking Issues

- none

## Missing Files

- none

## Missing Workflows

- none

## Missing Fusion Markers

- none

## Duplicate Script Names

- none

## Duplicate MITM Hostnames

- none

## Workflow Summary

- `.github/workflows/module-factory-build.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/daily-module-update.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/daily-audit-and-repair.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/daily-invalid-source-repair.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/scheduled-module-update.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/upstream-app-module-sync.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/upstream-collect.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/daily-schedule-watchdog.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/repository-health.yml`: contents: write; concurrency; fusion; rebase retry

## validate_repository.py Output

```text
Repository validation passed.
```

## automated quality evidence Output

```text
Automated quality evidence written to ./reports/automated_quality_evidence.md
```

## node --check Output

```text
no output
```
