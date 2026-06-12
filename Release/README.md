# Release

This directory stores generated release files. Do not maintain `Release/` as the source of truth.

Regenerate release outputs with:

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
```

## Current generated entries

- `Release/Ronghemokuai.sgmodule`
- `Release/Module.sgmodule` compatibility alias copied from `Release/Ronghemokuai.sgmodule`
- root `Ronghemokuai.sgmodule`
- `Release/Rules.conf`
- `Release/RulesGroup.conf`
- `Release/Modules/`
- `Release/Android/`

## Public release entry points

- Fusion module: <https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule>
- Release module alias: <https://grandpaniuu.github.io/GrandpaNiu/Release/Module.sgmodule>
- Release catalog: <https://grandpaniuu.github.io/GrandpaNiu/Web/catalog.md>
- Release JSON: <https://grandpaniuu.github.io/GrandpaNiu/Web/release-links.json>
- App modules: <https://grandpaniuu.github.io/GrandpaNiu/Release/Modules/>
- Android release: <https://grandpaniuu.github.io/GrandpaNiu/Release/Android/>

The stable tag can be created after local build validation and a green `Module Factory Build` run. Do not edit generated files here directly.

## Legacy entries

The old full/lite/stable files are compatibility placeholders only:

- `Release/Ronghemokuai-full.sgmodule`
- `Release/Ronghemokuai-lite.sgmodule`
- `Release/Ronghemokuai-stable-plus.sgmodule`
- `Release/Ronghemokuai-stable.sgmodule`

They are deprecated legacy files and are not public catalog entries. See `Release/Legacy/README.md`.

## Source of truth

- Main source files: `Rewrite/Sources/`
- App source files: `Rewrite/Sources/Apps/`
- Misc source files: `Rewrite/Sources/Misc/`
- Remote governance: `Rewrite/Remotes/`
- Android source files: `Android/`
- Generation plan: `Rewrite/Generate.conf`
