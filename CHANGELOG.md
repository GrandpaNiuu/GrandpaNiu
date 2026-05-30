# Changelog

## v1.3 governance and health reports - 2026-05-30

- Strengthened daily module validation.
- Added compatibility source migration audit.
- Added security policy, contribution rules, script review checklist, MITM policy, and versioning policy.
- Added `full.conf` as a non-default full coverage testing profile.
- Added App coverage matrix, change impact report, and workflow health report generators.
- Added backup manifest.
- Clarified profile release-sync semantics by removing the unused `write_release_only` field.
- Kept PrivacyLite 404 under observation because it has only one recorded failed day.

## v1.2 source-first governance - 2026-05-30

- Added Zhihu enhancement.
- Added `lite.conf`.
- Added repository validation and health check scripts.
- Added repository health workflow.
- Expanded trusted low-risk remote rule candidates while keeping scripts pending.

## v1.1 source-driven factory - 2026-05-29

- Refactored the module factory into a source-driven build.
- Default build reads `Rules/`, `Scripts/`, `Rewrite/Sources/`, `Rewrite/Remotes/`, and `Rewrite/Profiles/`.
- Finalize syncs Release back to the root module.
- Added stable backups and factory reports.

## v1.0 initial maintenance system - 2026-05-25

- Added one-click import, fallback import page, and module update URL.
- Added daily update workflow.
- Added maintenance and troubleshooting documentation.
- Added trusted remote source registry and basic reports.
