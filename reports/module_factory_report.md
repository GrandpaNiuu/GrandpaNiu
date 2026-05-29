# Module Factory Report

Date: 2026-05-30
Profile: stable
Extracted from root module: no
构建阶段 Root/Release 是否一致: yes
Release line count: 2847

## Source Counts
- Rule: 523 lines
- URL Rewrite: 1598 lines
- Header Rewrite: 5 lines
- Body Rewrite: 456 lines
- Map Local: 16 lines
- Script: 213 lines
- MITM: 2 lines

## Build Inputs
- Rewrite/Profiles/stable.conf
- Rewrite/Remotes/sources.json
- Rules/: DIRECT, Spotify, YouTube, local App, Web, and Reject rule fragments
- Scripts/: Spotify, YouTube, Zhihu, and App-clean script fragments
- Rewrite/Sources/: Meta, rewrite, body rewrite, map local, MITM, and compatibility fragments

## Duplicate Checks
- Duplicate script names: none
- Duplicate MITM hostnames: none

## Notes
- Daily maintenance should edit Rules, Scripts, Rewrite/Sources, Rewrite/Remotes, and Rewrite/Profiles.
- Release/Ronghemokuai.sgmodule is generated from the factory sources.
- Root Ronghemokuai.sgmodule is synchronized by factory_finalize.py.
- Upstream collection stays conservative: trusted sources, reversible changes, verifiable reports.
- --extract-from-root is reserved for initialization or source recovery, not the normal daily build path.

## Finalize 后状态
- Release 已同步回根目录主模块：yes
- 同步后 diff lines：0
- Scripts/spotify.conf 仅保留 Spotify 核心脚本。
- 其他 app2smile 脚本归入 Scripts/app-clean.conf。
