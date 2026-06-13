# Repository Health Report

- Generated at: 2026-06-14 07:31:00 +0800
- Blocking issues: 0
- Root and Release identical: yes
- Fusion profile finalized: yes
- validate_repository.py: passed
- automated quality evidence: passed
- node --check Scripts/app-cleaner.js: passed
- Script entries: 46
- MITM hostnames: 1189

## Section Counts

- [Rule]: 1112
- [URL Rewrite]: 2492
- [Header Rewrite]: 1
- [Body Rewrite]: 1651
- [Map Local]: 350
- [Script]: 203
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
- `.github/workflows/upstream-collect.yml`: contents: write; concurrency; fusion; rebase retry
- `.github/workflows/repository-health.yml`: contents: write; concurrency; fusion; rebase retry

## validate_repository.py Output

```text
Repository validation passed.
```

## automated quality evidence Output

```text
Automated quality evidence written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/automated_quality_evidence.md
```

## node --check Output

```text
no output
```

## Maintenance Boundaries

- Source-first maintenance: edit `Rules/`, `Scripts/`, `Rewrite/Sources/`, `Rewrite/Remotes/`, and `Rewrite/Profiles/fusion.conf` first.
- Fusion is the only public iOS entry; legacy Stable/Lite/Full files are compatibility placeholders only.
- `Release/` and generated `Web/` catalogs must be rebuilt, not manually patched as source files.
