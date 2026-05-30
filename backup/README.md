# Stable Backups

This directory stores manually controlled rollback points. Automated maintenance scripts must not overwrite backup files unless a maintainer explicitly does it.

## Manifest

See [manifest.json](manifest.json) for the current backup list.

## Backup Files

- `Ronghemokuai.stable.sgmodule`: stable module rollback point.
- `Ronghemokuai.before-factory-refactor.sgmodule`: rollback point before the source-driven factory refactor.

## Restore

1. Confirm the generated root module is broken.
2. Copy the selected backup file over `Ronghemokuai.sgmodule`.
3. Run:

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

4. Commit the rollback with a clear reason.

## Notes

- Do not store temporary test modules as stable backups.
- Keep rollback reasons in commit messages or reports.
- Prefer commit revert when possible; use backups when generated output is unusable.
