# 模块工厂报告

- 日期：2026-05-31
- 构建 profile：stable
- 是否从 root 反拆：否
- 构建阶段 Root/Release 是否一致：否
- Release 行数：2848
- Release MITM hostname 数量：120

## 源文件统计
- Rule: 523 行
- URL Rewrite: 1598 行
- Header Rewrite: 5 行
- Body Rewrite: 456 行
- Map Local: 16 行
- Script: 204 行
- MITM: 2 行

## 构建输入
- Rewrite/Profiles/stable.conf
- Rewrite/Remotes/sources.json
- Rules/: DIRECT、Spotify、YouTube、本地 App、网页和 Reject 规则片段
- Scripts/: Spotify、YouTube、知乎和 App-clean 脚本片段
- Rewrite/Sources/: Meta、Rewrite、Body Rewrite、Map Local、MITM 和兼容片段
- [mitm] profile 可选择 MITM-core / MITM-app-clean / MITM-extended 分层输入；stable 默认不直接吃 extended 层。

## 重复检查
- 重复脚本名：无
- 重复 MITM hostname：无

## 说明
- 日常维护应优先修改 Rules、Scripts、Rewrite/Sources、Rewrite/Remotes 和 Rewrite/Profiles。
- Release/Ronghemokuai.sgmodule 由工厂源头生成。
- 根目录 Ronghemokuai.sgmodule 由 factory_finalize.py 同步生成。
- 候选源收集保持保守：来源可信、改动可回滚、报告可验证。
- --extract-from-root 只用于初始化或恢复源头，不是日常构建路径。

## Finalize 后状态
- Release 已同步回根目录主模块：yes
- 同步后 diff lines：0
- Scripts/spotify.conf 仅保留 Spotify 核心脚本。
- 其他 app2smile 脚本归入 Scripts/app-clean.conf。
