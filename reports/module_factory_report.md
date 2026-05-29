# Module Factory Report

日期：2026-05-29
构建 profile：stable
是否从根目录主模块拆分：yes
Release 是否与根目录主模块一致：yes
Release 行数：2833

## Sources 统计
- Rule: 523 lines
- URL Rewrite: 1598 lines
- Header Rewrite: 5 lines
- Body Rewrite: 456 lines
- Map Local: 16 lines
- Script: 213 lines
- MITM: 2 lines

## 参与构建的源头
- Rewrite/Sources/: rewrite、body、map local、MITM 与过渡兼容片段
- Rules/: DIRECT、Spotify、YouTube、本地规则片段
- Scripts/: Spotify、YouTube、App 脚本片段
- Rewrite/Remotes/sources.json: 远程 RULE-SET / DOMAIN-SET 清单
- Rewrite/Profiles/: 构建 profile

## 重复检查
- 重复脚本名：无
- 重复 MITM hostname：无

## 说明
- 根目录 Ronghemokuai.sgmodule 仍是正式导入入口。
- Release/Ronghemokuai.sgmodule 是工厂源文件生成的发布副本。
- 当前构建不会自动覆盖根目录主模块。

## Finalize 后状态
- Release 已同步回根目录主模块：yes
- 同步后 diff lines：0
- Scripts/spotify.conf 仅保留 Spotify 核心脚本。
- 其他 app2smile 脚本归入 Scripts/app-clean.conf。
