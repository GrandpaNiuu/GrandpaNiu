# Profiles

This directory stores build profiles for the module factory.

## Active Profile

- `stable.conf`: the only active profile. It keeps the current module behavior while allowing `Rules/`, `Scripts/`, `Rewrite/Remotes/sources.json`, and `Rewrite/Sources/` to participate in the release build.

## Maintenance Rule

Do not re-add `full.conf` or `test.conf` unless they implement real, distinct build behavior and are wired into `scripts/build_module.py` and the factory workflow.
