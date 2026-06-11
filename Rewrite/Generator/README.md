# Rewrite Generator

This directory provides the generator layer used by the module factory layout.

The current repository keeps the implementation in `scripts/`. This directory adds a stable entry point instead of moving existing scripts.

Recommended command:

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

## Pipeline

1. Build module from source files.
2. Sync the generated Release module back to the root entry file.
3. Write release reports.
4. Run available repository validation scripts.

## Current implementation

`Builder.py` calls existing scripts when they exist:

- `scripts/build_module.py`
- `scripts/factory_finalize.py`
- `scripts/build_release_variants.py`
- `scripts/validate_repository.py`
- `scripts/validate_profiles.py`
- `scripts/validate_governance_extensions.py`

## Next targets

- Read `Rewrite/Generate.conf` as the top-level build plan.
- Generate `Release/Rules.conf`.
- Generate `Release/RulesGroup.conf`.
- Generate per-app modules under `Release/Modules/`.
