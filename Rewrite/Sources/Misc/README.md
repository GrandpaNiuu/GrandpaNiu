# Rewrite Sources / Misc

This directory is reserved for reviewed upstream module fragments and miscellaneous source material.

Target layout:

```text
Rewrite/Sources/Misc/
├─ reviewed-upstream.conf
├─ experimental.conf
└─ legacy.conf
```

Current policy:

- Raw upstream files should be recorded under `Rewrite/Remotes/` first.
- Only reviewed and normalized fragments should enter this directory.
- Experimental fragments must not be included in Release output unless listed in `Rewrite/Generate.conf`.
