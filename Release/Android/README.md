# Release Android

Generated Android rule outputs mirrored from `Android/`.

## Published formats

| Format | Directory | Files |
|---|---|---:|
| mihomo | `Release/Android/mihomo` | 23 |
| sing-box | `Release/Android/sing-box` | 20 |
| adguard | `Release/Android/adguard` | 20 |
| v2rayng | `Release/Android/v2rayng` | 20 |

## Source of truth

- Editable Android sources remain under `Android/`.
- Published Android release files are generated into `Release/Android/`.
- Do not edit this directory first; regenerate it through `Rewrite/Generator/Builder.py --release`.
