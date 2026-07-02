# Profiles

This directory stores source-first build profiles for the module factory.

## Active Profile

- `fusion.conf` is the only build profile and the only public iOS module path.
- It combines maintained rules, scripts, rewrite fragments, remote sources, and MITM layers into `Ronghemokuai.sgmodule`.

There are no Stable, Stable Plus, Lite, or Full profile files in the active repository. Historical rollout records belong in Git history, not in the build tree.

## Maintenance Rule

New module work must update source files first:

```text
Rules/
Scripts/
Rewrite/Sources/
Rewrite/Remotes/
Rewrite/Profiles/fusion.conf
```

Then rebuild and validate:

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
python3 scripts/validate_profiles.py
python3 scripts/validate_repository.py
```
