# Rewrite Generator

This directory is the stable generator layer for the module factory layout.

`Rewrite/Generator/Generate.conf` is now the preferred build plan. `Rewrite/Generate.conf` remains as a legacy mirror for older commands and fallback behavior.

Recommended command:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

Dry-run the pipeline without writing files:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check --dry-run
```

## Pipeline

1. Build the fusion module from source files.
2. Sync the generated Release module back to the root entry file.
3. Generate release variants and reports.
4. Generate pure rules and grouped rules.
5. Generate per-app modules under `Release/Modules/`.
6. Generate release aliases and channel directories.
7. Mirror Android outputs into `Release/Android/`.
8. Generate Web module pages and release catalogs.
9. Generate checksums and build summaries.
10. Run repository validation scripts when `--check` is used.

## Current implementation

`Builder.py` calls configured scripts when they exist:

- `scripts/build_module.py`
- `scripts/factory_finalize.py`
- `scripts/build_release_variants.py`
- `scripts/build_release_rules.py`
- `scripts/build_release_modules.py`
- `scripts/build_release_aliases.py`
- `scripts/build_channels.py`
- `scripts/build_release_android.py`
- `scripts/build_web_modules.py`
- `scripts/build_web_catalog.py`
- `scripts/build_checksums.py`
- `scripts/build_release_summary.py`
- `scripts/validate_generator_config.py`
- `scripts/validate_manifest.py`
- `scripts/validate_remote_rule_syntax.py`
- `scripts/validate_repository.py`
- `scripts/validate_profiles.py`
- `scripts/validate_governance_extensions.py`

## Maintenance rule

Do not add a new release artifact manually without wiring it into both:

1. `Rewrite/Generator/Generate.conf`
2. `Rewrite/Generator/Builder.py`

The config consistency check prevents the preferred config and legacy mirror from drifting silently.
