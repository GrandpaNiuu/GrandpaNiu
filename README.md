<div align="center">

# GrandpaNiu

### Shadowrocket / Surge compatible personal cleanup module factory

One import entry for App cleanup, web ad filtering, Spotify playback protection, YouTube Enhance, remote source maintenance, source-driven builds, and rollback reports.

<br>

[![Install Module](https://img.shields.io/static/v1?label=Install%20Module&message=Shadowrocket&color=0A84FF&labelColor=111827&logo=rocket&logoColor=white&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule)
[![Fallback Page](https://img.shields.io/static/v1?label=Fallback%20Page&message=Copy%20URL&color=34C759&labelColor=111827&logo=safari&logoColor=white&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/import.html)

<br>

![Shadowrocket](https://img.shields.io/badge/Shadowrocket-supported-0A84FF?style=flat-square)
![Surge](https://img.shields.io/badge/Surge-compatible-5856D6?style=flat-square)
![Spotify](https://img.shields.io/badge/Spotify-protected-1DB954?style=flat-square)
![YouTube](https://img.shields.io/badge/YouTube%20Enhance-kept-FF3B30?style=flat-square)
![Factory](https://img.shields.io/badge/source--driven-factory-F59E0B?style=flat-square)
![Safe](https://img.shields.io/badge/no%20premium%20bypass-safe-6B7280?style=flat-square)

</div>

---

## Quick Import

| Entry | Description |
|---|---|
| [Install Module](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule) | Recommended Shadowrocket import entry. |
| [Fallback Import Page](https://grandpaniuu.github.io/GrandpaNiu/import.html) | Use this page if automatic redirect is blocked. |
| [Raw Module URL](https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule) | GitHub raw module file. |
| [GitHub Pages Module URL](https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule) | Stable Pages URL and the module `update-url`. |

After importing, update the module, scripts, and remote resources in Shadowrocket.

## Project Positioning

GrandpaNiu is a personal Shadowrocket / Surge compatible cleanup module. It combines local rules, remote rule sets, rewrites, scripts, map-local responses, and MITM hostnames into one generated module.

The root `Ronghemokuai.sgmodule` is the import output, not the long-term source of truth. Daily maintenance should edit source files first, then let the factory regenerate the module.

## Module Factory Flow

```text
Profiles + Remotes + Rules + Scripts + Rewrite/Sources
        -> scripts/build_module.py --build --profile stable
        -> Release/Ronghemokuai.sgmodule
        -> scripts/factory_finalize.py --sync-root
        -> Ronghemokuai.sgmodule
```

| Layer | Role |
|---|---|
| `Rewrite/Profiles/stable.conf` | Active stable build profile. |
| `Rewrite/Remotes/sources.json` | Machine-readable trusted remote `RULE-SET` / `DOMAIN-SET` registry. |
| `Rules/*.list` | Local rule sources for `[Rule]`. |
| `Scripts/*.conf` | Script sources for `[Script]`. |
| `Rewrite/Sources/*.conf` | Meta, rewrite, body rewrite, map-local, and MITM source fragments. |
| `Release/Ronghemokuai.sgmodule` | Generated release copy. |
| `Ronghemokuai.sgmodule` | Official import output synced from Release. |

Full flow documentation: [docs/FACTORY_FLOW.md](docs/FACTORY_FLOW.md).

## Core Features

- General ad domain, SDK, tracker, activity card, splash, popup, banner, and feed cleanup.
- App cleanup rules for common domestic apps and selected trusted upstream scripts.
- Web ad, tracker, and statistics cleanup.
- Spotify playback protection through early DIRECT rules, header rewrite, `spotify-json`, `spotify-proto`, and required MITM hostnames.
- YouTube Enhance preservation through `youtube.response` and required YouTube hostnames.
- Trusted remote rule registry with validation and protected core sources.
- Daily reports, invalid-source history, safe repair workflow, and stable backups.

## Maintenance Links

| Type | Link | Purpose |
|---|---|---|
| Factory flow | [docs/FACTORY_FLOW.md](docs/FACTORY_FLOW.md) | Source-driven build reference. |
| Factory workflow | [.github/workflows/module-factory-build.yml](.github/workflows/module-factory-build.yml) | Build Release and sync root output. |
| Factory report | [reports/module_factory_report.md](reports/module_factory_report.md) | Build profile, inputs, counts, and duplicate checks. |
| Factory diff report | [reports/module_factory_diff_report.md](reports/module_factory_diff_report.md) | Root versus Release diff. |
| Finalize report | [reports/factory_finalize_report.md](reports/factory_finalize_report.md) | Release-to-root sync result. |
| Factory refactor report | [reports/factory_refactor_report.md](reports/factory_refactor_report.md) | Source-driven refactor summary and validation. |
| Cleanup report | [reports/repository_cleanup_report.md](reports/repository_cleanup_report.md) | Repository cleanup and verification notes. |
| Daily update report | [reports/daily_update_report.md](reports/daily_update_report.md) | Daily structure and link check report. |
| Invalid-source report | [reports/invalid_sources_report.md](reports/invalid_sources_report.md) | Invalid link audit and safe repair results. |
| Invalid-source history | [reports/invalid_sources_history.json](reports/invalid_sources_history.json) | Consecutive failure history. |
| Daily update workflow | [.github/workflows/daily-module-update.yml](.github/workflows/daily-module-update.yml) | Lightweight daily date and report update. |
| Invalid-source workflow | [.github/workflows/daily-invalid-source-repair.yml](.github/workflows/daily-invalid-source-repair.yml) | Safe repair after 2 confirmed failed days. |
| Refine report | [reports/module_refine_report.md](reports/module_refine_report.md) | Safe refine and duplicate validation notes. |
| Maintenance guide | [docs/MAINTENANCE.md](docs/MAINTENANCE.md) | Daily maintenance rules. |
| Troubleshooting | [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | Spotify, YouTube, login, payment, and verification troubleshooting. |
| Coverage | [docs/COVERAGE.md](docs/COVERAGE.md) | Feature coverage status. |
| Scope | [docs/SCOPE.md](docs/SCOPE.md) | Allowed and forbidden project scope. |
| Changelog | [CHANGELOG.md](CHANGELOG.md) | Main repository changes. |
| Stable backup | [backup/README.md](backup/README.md) | Backup and rollback instructions. |

## Automatic Maintenance

### Module Factory Build

Workflow: [.github/workflows/module-factory-build.yml](.github/workflows/module-factory-build.yml)

It compiles the Python scripts, builds from source inputs, syncs Release back to the root module, validates all required sections and core markers, and commits generated outputs only when changed.

`--extract-from-root` is reserved for initialization or disaster recovery. It is not the normal daily build path.

### Daily Module Update

Workflow: [.github/workflows/daily-module-update.yml](.github/workflows/daily-module-update.yml)

It updates the date, checks key structure and main remote links, and writes the daily report. It does not perform large module rewrites.

### Daily Invalid-Source Repair

Workflow: [.github/workflows/daily-invalid-source-repair.yml](.github/workflows/daily-invalid-source-repair.yml)

It scans remote scripts, `RULE-SET`, `DOMAIN-SET`, `update-url`, GitHub raw links, GitHub Pages links, and other external URLs. A source is handled only after 2 consecutive confirmed failed checks. The repair priority is:

1. Replace with a verified same-origin upstream URL.
2. Comment the original line if no reliable replacement exists.
3. Delete only low-risk independent remote rule references.

Protected Spotify, YouTube, install, import, update, and core upstream entries are reported for manual confirmation instead of being modified automatically.

## Safety Boundary

This repository is for:

- Ad blocking.
- Splash ad cleanup.
- Popup, banner, feed, recommendation, and activity-card cleanup.
- Web ad and tracker cleanup.
- Spotify playback protection.
- YouTube Enhance preservation.
- Domestic App cleanup.
- Remote rule and script source maintenance.
- Source-driven module factory builds.

This repository does not add:

- Membership or Premium unlocks.
- Payment bypass.
- Login bypass.
- Account entitlement spoofing.
- Certificate bypass.
- Cookie or BoxJS account tasks.
- Adult, gambling, or gray-market content.
- Short-link scripts.
- Unknown obfuscated scripts.
- Unverified third-party script sources.
- `ghproxy` or mirror sites as official sources.

## Troubleshooting

| Issue | First checks |
|---|---|
| Spotify skips tracks | Check Spotify DIRECT rules, `spotify-json`, `spotify-proto`, header rewrite, `spclient.wg.spotify.com`, `*.spclient.spotify.com`, and other Spotify modules. |
| YouTube spins or loses Enhance behavior | Check `youtube.response`, YouTube MITM hostnames, Map Local entries, and recent rewrite changes. |
| Login fails | Temporarily disable the module, then inspect recent rules, rewrite entries, and MITM changes. |
| Payment or verification code fails | Check MITM, URL Rewrite, Body Rewrite, and Map Local entries first. |
| Remote source fails | Read the reports and confirm whether the failure is consecutive; single-day GitHub network failures should not trigger deletion. |

More detail: [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md).

## Maintenance Principles

- Edit source files first: `Rules/`, `Scripts/`, `Rewrite/Sources/`, `Rewrite/Remotes/`, and `Rewrite/Profiles/`.
- Let the factory generate `Release/Ronghemokuai.sgmodule`.
- Let finalize sync `Release/Ronghemokuai.sgmodule` back to `Ronghemokuai.sgmodule`.
- Keep Root and Release identical after finalize.
- Keep Spotify and YouTube core entries protected.
- Prefer replacement, then comments, and only delete low-risk independent invalid remote rules.
- Keep reports readable and rollback paths available.
