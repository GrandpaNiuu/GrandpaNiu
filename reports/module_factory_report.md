# 模块工厂报告

- 日期：2026-06-18
- 构建 profile：fusion
- 默认公开入口：单一融合版
- 是否从 root 反拆：否
- 构建阶段 Root/Release 是否一致：否
- Release 行数：5550
- Release MITM hostname 数量：1189

## 源文件统计
- Rule: 120 行
- URL Rewrite: 1598 行
- Header Rewrite: 5 行
- Body Rewrite: 445 行
- Map Local: 11 行
- Script: 132 行
- MITM: 2 行

## 构建输入
- Rewrite/Profiles/fusion.conf
- Rewrite/Remotes/sources.json
- Rules/: DIRECT、Spotify、YouTube、本地 App、网页、Reject、legacy、Stable Plus 与 Full 规则片段
- Scripts/: Spotify、YouTube、知乎、App-clean、legacy reviewed、QingRex 与 Stable Plus 脚本片段
- Rewrite/Sources/: Meta、Rewrite、Body Rewrite、Map Local、MITM、legacy reviewed、stable-plus、extended 和兼容片段
- [mitm] fusion profile 同时读取 core / app-clean / legacy-reviewed / qingrex / stable-plus / extended 层。

## 重复检查
- 重复脚本名：无
- 重复 MITM hostname：无

## 模块输出清理
- 生成模块会自动删除空行和普通 # 注释说明。
- 保留 #!update-url、#!name、#!desc 和 # update-date: 等必要元数据。
- 已知纯域名远程源会自动规范为 DOMAIN-SET，避免 Shadowrocket 红叉。

## 说明
- 日常维护应优先修改 Rules、Scripts、Rewrite/Sources、Rewrite/Remotes 和 Rewrite/Profiles/fusion.conf。
- Release/Ronghemokuai.sgmodule 由工厂源头生成。
- 根目录 Ronghemokuai.sgmodule 由 factory_finalize.py 同步生成。
- 本仓库默认不再拆分 Stable / Stable Plus / Lite / Full 作为用户入口。
- --extract-from-root 只用于初始化或恢复源头，不是日常构建路径。

## Finalize 后状态
- Release 已同步回根目录主模块：yes
- 同步后 diff lines：0
- Scripts/spotify.conf 仅保留 Spotify 核心脚本。
- 其他 app2smile 脚本归入 Scripts/app-clean.conf。
