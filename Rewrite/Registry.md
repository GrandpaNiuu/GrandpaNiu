# Rewrite Registry

This file records source ownership, status, risk level, test status, and fallback path for the module factory.

| ID | Name | Type | Local file | Source | Enabled | Risk | Test status | Fallback |
|---|---|---|---|---|---|---|---|---|
| core.meta | Module metadata | Meta | `Rewrite/Sources/Meta.conf` | Root module split | yes | low | pending | Rebuild from previous root module |
| core.rule | Main rules | Rule | `Rewrite/Sources/Rule.conf` | Root module split and `Rules/` | yes | high | partial | Revert recent rule change |
| core.url_rewrite | URL rewrite | Rewrite | `Rewrite/Sources/URL-Rewrite.conf` | Local source fragment | yes | medium | pending | Revert recent fragment change |
| core.header_rewrite | Header rewrite | Rewrite | `Rewrite/Sources/Header-Rewrite.conf` | Local source fragment | yes | high | pending | Revert recent fragment change |
| core.body_rewrite | Body rewrite | Rewrite | `Rewrite/Sources/Body-Rewrite.conf` | Local source fragment | yes | high | pending | Revert recent fragment change |
| core.map_local | Map local | Rewrite | `Rewrite/Sources/Map-Local.conf` | Local source fragment | yes | high | pending | Revert recent fragment change |
| core.script | Scripts | Script | `Rewrite/Sources/Script.conf` | `Scripts/` and local fragment | yes | high | partial | Revert recent script entry |
| core.mitm | MITM hosts | MITM | `Rewrite/Sources/MITM.conf` | Profile layers | yes | high | partial | Revert recent hostname layer |
| remote.index | Remote index | Remote | `Rewrite/Remotes/Index.md` | Manual record | yes | medium | pending | Disable related remote item |
| remote.sources | Remote sources | Remote | `Rewrite/Remotes/sources.json` | Manual record | yes | medium | pending | Set item enabled to false |
| build.plan | Generation plan | Config | `Rewrite/Generate.conf` | Local plan | yes | low | pending | Revert plan change |
| build.manifest | Manifest | Config | `Rewrite/Manifest.conf` | Local plan | yes | low | pending | Revert manifest change |
| build.generator | Generator entry | Script | `Rewrite/Generator/Builder.py` | Local wrapper | yes | medium | pending | Run scripts directly |

## Rules

- New active sources must have a clear purpose.
- High-risk changes must include a fallback path.
- Spotify and YouTube entries need manual review before changes.
- Stale sources should be recorded in reports before replacement.
