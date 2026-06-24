# 单一融合版发布报告

生成时间：2026-06-25 02:21:24 +0800

本仓库现在只发布一个融合模块，不再拆分 Stable / Stable Plus / Lite / Full 给用户选择。

| Profile | 文件 | 脚本数 | MITM 数量 | 默认发布 | 用途 | Pages 地址 | Raw 地址 |
|---|---|---:|---:|---|---|---|---|
| fusion | `Ronghemokuai.sgmodule` | 44 | 1235 | yes | 单一融合模块入口 | https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule | https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule |
| fusion | `Release/Ronghemokuai.sgmodule` | 44 | 1235 | yes | Release 同步入口 | https://grandpaniuu.github.io/GrandpaNiu/Release/Ronghemokuai.sgmodule | https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Release/Ronghemokuai.sgmodule |

## 使用规则

- Shadowrocket / Surge 只导入 `Ronghemokuai.sgmodule`。
- 不再要求用户判断 Stable、Stable Plus、Lite、Full。
- 规则、脚本、Rewrite、MITM 的维护仍然通过源头文件完成。
- 若某个 App 误伤，直接在 fusion 源头层回滚对应规则或 hostname。

## 构建状态

- 构建 profile：fusion
- Release 与 Root 当前是否一致：是
- 旧多版本文件不再作为公开入口。
