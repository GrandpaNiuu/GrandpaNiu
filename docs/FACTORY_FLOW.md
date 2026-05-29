# Module Factory Flow

This is the authoritative factory-flow document for the repository.

## Core Principle

`Ronghemokuai.sgmodule` is the official import output, but it is not the long-term hand-maintained source of truth.

Daily maintenance should update:

- `Rules/*.list`
- `Scripts/*.conf`
- `Rewrite/Sources/*.conf`
- `Rewrite/Remotes/sources.json`
- `Rewrite/Profiles/stable.conf`

The factory then generates the release module and syncs it back to the root import module.

## Complete Flow

```text
Rules + Scripts + Rewrite/Sources + Remotes + Profiles
        -> scripts/build_module.py --build --profile stable
        -> Release/Ronghemokuai.sgmodule
        -> scripts/factory_finalize.py --sync-root
        -> Ronghemokuai.sgmodule
```

`--extract-from-root` is only for initialization or disaster recovery. It is not the default daily build path.

## Directory Responsibilities

| Path | Responsibility |
|---|---|
| `Rewrite/Profiles/stable.conf` | Current stable build profile. |
| `Rewrite/Remotes/sources.json` | Trusted remote `RULE-SET` / `DOMAIN-SET` registry. |
| `Rewrite/Remotes/candidates.json` | Trusted upstream candidate registry; no web-wide search. |
| `Rules/direct.list` | General DIRECT allowlist. |
| `Rules/spotify-direct.list` | Spotify playback-path protection; must stay before remote ad rules. |
| `Rules/youtube-direct.list` | Narrow YouTube protection rules. |
| `Rules/reject.list` | General reject rules. |
| `Rules/app-clean.list` | App cleanup rules. |
| `Rules/web-ads.list` | Web ad, statistics, and tracker rules. |
| `Scripts/spotify.conf` | Only `spotify-json`, `spotify-proto`, or clearly Spotify / spclient scripts. |
| `Scripts/youtube.conf` | Only `youtube.response` or clearly YouTube / Maasea scripts. |
| `Scripts/app-clean.conf` | Other ordinary App cleanup scripts. |
| `Rewrite/Sources/Meta.conf` | Module metadata and `update-url`. |
| `Rewrite/Sources/URL-Rewrite.conf` | URL rewrite source fragment. |
| `Rewrite/Sources/Header-Rewrite.conf` | Header rewrite source fragment, including Spotify header handling. |
| `Rewrite/Sources/Body-Rewrite.conf` | Body rewrite source fragment. |
| `Rewrite/Sources/Map-Local.conf` | Local response mapping source fragment. |
| `Rewrite/Sources/MITM.conf` | MITM hostname source fragment, using `%APPEND%`. |
| `Release/Ronghemokuai.sgmodule` | Generated release copy. |
| `Ronghemokuai.sgmodule` | Root import module synced from Release. |

## Workflow Order

`.github/workflows/module-factory-build.yml` runs:

```text
python3 -m py_compile scripts/build_module.py scripts/factory_finalize.py scripts/audit_repair_invalid_sources.py
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
```

The workflow validates:

```text
[Rule]
[URL Rewrite]
[Header Rewrite]
[Body Rewrite]
[Map Local]
[Script]
[MITM]
spotify-json
spotify-proto
youtube.response
#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
Root and Release equality
```

If any required marker is missing, the workflow fails instead of committing a broken module.

## Build Script

`scripts/build_module.py`:

- Reads `Rewrite/Profiles/stable.conf`.
- Reads `Rewrite/Remotes/sources.json`.
- Reads `Rules/*.list`.
- Reads `Scripts/*.conf`.
- Reads `Rewrite/Sources/*.conf`.
- Generates `Release/Ronghemokuai.sgmodule`.
- Generates `reports/module_factory_report.md`.
- Generates `reports/module_factory_diff_report.md`.
- Validates section presence, core markers, duplicate script names, and duplicate MITM hostnames.

Enabled remote sources must be trusted, public, HTTPS, and schema-valid. The builder rejects short links, mirror sites, `ghproxy`, and unknown remote source formats.

## Finalize Script

Default command:

```text
python3 scripts/factory_finalize.py --sync-root
```

Default finalize mode:

- Validates `Release/Ronghemokuai.sgmodule`.
- Syncs Release to root `Ronghemokuai.sgmodule`.
- Validates the root module.
- Generates `reports/factory_finalize_report.md`.
- Confirms Root and Release are identical.

Migration or recovery command:

```text
python3 scripts/factory_finalize.py --split-from-sources --sync-root
```

Default finalize mode does not rewrite `Rules/` or `Scripts/`. Splitting is explicit so daily builds do not keep reverse-extracting the root module.

## Reports

| Report | Purpose |
|---|---|
| `reports/module_factory_report.md` | Build profile, inputs, section counts, and duplicate checks. |
| `reports/module_factory_diff_report.md` | Root versus Release diff; should be zero after finalize. |
| `reports/factory_finalize_report.md` | Final sync mode and Root/Release equality. |
| `reports/factory_refactor_report.md` | Source-driven refactor summary, backup, core checks, and manual tests. |
| `reports/repository_cleanup_report.md` | Repository cleanup and workflow validation notes. |

## Spotify and YouTube Protection

The following entries are hard-protected:

- `spotify-json`
- `spotify-proto`
- `youtube.response`
- `spclient.wg.spotify.com`
- `*.spclient.spotify.com`
- Spotify DIRECT allowlist
- Spotify header rewrite
- YouTube Enhance script and required YouTube hostnames

If Spotify skipping appears, first check remote ad-rule conflicts and add narrow DIRECT protection. Do not remove Spotify scripts as the first response.

## Automatic Maintenance Boundary

- `daily-module-update.yml` updates dates and reports only.
- `daily-invalid-source-repair.yml` handles invalid sources only after 2 consecutive confirmed failed checks.
- `upstream-collect.yml` runs weekly and reads only `Rewrite/Remotes/candidates.json`.
- The repair order is: verified same-origin replacement, comment, then low-risk independent remote-rule deletion.
- Spotify, YouTube, the module `update-url`, install pages, import pages, and protected upstream sources are report-only when they fail.

## Upstream Candidate Collection

`scripts/collect_upstreams.py` is a conservative collector:

- It does not search the web.
- It only accepts candidates registered in `Rewrite/Remotes/candidates.json`.
- It only allows trusted GitHub repositories listed in that file.
- It rejects short links, proxy hosts, mirror hosts, risky keywords, unknown scripts, and duplicate URLs.
- It validates rule-like or JavaScript-like content before adding anything.
- It keeps script candidates pending unless they are explicitly approved.
- It reports Spotify and YouTube core references instead of replacing them.

The weekly workflow runs:

```text
python3 -m py_compile scripts/collect_upstreams.py scripts/build_module.py scripts/factory_finalize.py
python3 scripts/collect_upstreams.py
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
```

The report is written to `reports/upstream_collect_report.md`.

## Tool-Specific Config Files

Do not add `.claude`, `CLAUDE.md`, or similar tool-specific traces. They do not participate in the module factory and add noise to the public repository.

## Maintenance Method

1. Edit source files first.
2. Change rules in `Rules/` or `Rewrite/Remotes/sources.json`.
3. Change scripts in `Scripts/`.
4. Change rewrite, body rewrite, map local, or MITM fragments in `Rewrite/Sources/`.
5. Run the build and finalize commands.
6. Confirm Root and Release diff lines are `0`.
7. Manually test Spotify, YouTube, login, payment, verification code, WeChat, Alipay, banking, and the most-used Apps.
