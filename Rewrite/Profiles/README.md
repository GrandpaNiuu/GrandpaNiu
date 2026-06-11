# Profiles

This directory stores source-first build profiles for the module factory.

## Active Profile

- `fusion.conf`: the only active public build profile. It combines the maintained rule, script, rewrite, remote source, and MITM layers into `Ronghemokuai.sgmodule`.

## Legacy Profiles

The old `stable.conf`, `stable-plus.conf`, `lite.conf`, and `full.conf` files may remain for history, compatibility review, or rollback reference only. They must not be used by README, import pages, default workflows, health checks, validation, or release reports as public entries.

## Maintenance Rule

New module work should update source files first:

```text
Rules/
Scripts/
Rewrite/Sources/
Rewrite/Remotes/
Rewrite/Profiles/fusion.conf
```

Then rebuild with:

```bash
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_module_integrity.py
python3 scripts/validate_repository.py
```
