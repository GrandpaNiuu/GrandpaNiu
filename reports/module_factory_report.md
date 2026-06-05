# 模块工厂报告

- 日期：2026-06-05
- 构建 profile：stable
- 是否从 root 反拆：否
- 构建阶段 Root/Release 是否一致：是
- Release 行数：2916
- Release MITM hostname 数量：264

## 源文件统计
- Rule: 525 行
- URL Rewrite: 1598 行
- Header Rewrite: 5 行
- Body Rewrite: 456 行
- Map Local: 16 行
- Script: 141 行
- MITM: 2 行

## 构建输入
- Rewrite/Profiles/stable.conf
- Rewrite/Remotes/sources.json
- Rules/: DIRECT、Spotify、YouTube、本地 App、网页、Reject 和 legacy stable import 规则片段
- Scripts/: Spotify、YouTube、知乎、App-clean 和 legacy reviewed 脚本片段
- Rewrite/Sources/: Meta、Rewrite、Body Rewrite、Map Local、MITM、legacy reviewed 和兼容片段
- [mitm] profile 可选择 MITM-core / MITM-app-clean / MITM-extended / MITM-legacy-reviewed 分层输入；stable 默认只吃 reviewed legacy 层。

## 重复检查
- 重复脚本名：无
- 重复 MITM hostname：无

## 模块输出清理
- 生成模块会自动删除空行和普通 # 注释说明。
- 保留 #!update-url、#!name、#!desc 和 # update-date: 等必要元数据。

## 说明
- 日常维护应优先修改 Rules、Scripts、Rewrite/Sources、Rewrite/Remotes 和 Rewrite/Profiles。
- Release/Ronghemokuai.sgmodule 由工厂源头生成。
- 根目录 Ronghemokuai.sgmodule 由 factory_finalize.py 同步生成。
- legacy Script / MITM / Rewrite 必须进入 reviewed 源头后才会被 stable profile 读取。
- --extract-from-root 只用于初始化或恢复源头，不是日常构建路径。

## Finalize 后状态
- Release 已同步回根目录主模块：yes
- 同步后 diff lines：0
- Scripts/spotify.conf 仅保留 Spotify 核心脚本。
- 其他 app2smile 脚本归入 Scripts/app-clean.conf。
