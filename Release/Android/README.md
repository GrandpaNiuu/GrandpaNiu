# Release Android

Generated Android rule outputs mirrored from `Android/`.

## Published formats

| Format | Directory | Files |
|---|---|---:|
| mihomo | `Release/Android/mihomo` | 27 |
| sing-box | `Release/Android/sing-box` | 24 |
| adguard | `Release/Android/adguard` | 24 |
| v2rayng | `Release/Android/v2rayng` | 24 |

## Synced rule branches

- `mihomo`, `sing-box`, `adguard`, and `v2rayng` are generated from the same Android source layer.
- `branches.json` records the synchronized public targets and rule counts.
- AdGuard is the DNS-compatible projection of the same source because AdGuard text filters cannot represent every IP/routing rule.

## Source of truth

- Editable Android sources remain under `Android/`.
- Published Android release files are generated into `Release/Android/`.
- Do not edit this directory first; regenerate it through `Rewrite/Generator/Builder.py --release`.
