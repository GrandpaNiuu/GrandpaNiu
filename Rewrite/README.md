# Rewrite

This directory is the module factory processing layer.

## Layout

- `Generator/`: unified build entry point.
- `Profiles/`: build profiles. Main profile: `fusion.conf`.
- `Remotes/`: remote source records.
- `Sources/`: local source fragments.
- `Generate.conf`: top-level build plan.
- `Manifest.conf`: section mapping.
- `Registry.md`: source and risk registry.

## Command

Run:

`python Rewrite/Generator/Builder.py --profile fusion --release --check`

Dry run:

`python Rewrite/Generator/Builder.py --profile fusion --release --check --dry-run`

## Rule

Edit source files first. Treat `Release/` as generated output.
