# GrandpaNiu Project State

Last updated: 2026-07-02

GrandpaNiu 是一个 source-first 规则构建仓库，输出 iOS Fusion 模块、Android 规则格式、Windows v2rayN 路由、Web catalog 与治理报告。

当前唯一公开 iOS 路径是 Fusion：`Ronghemokuai.sgmodule`、`Release/Ronghemokuai.sgmodule` 与 `Release/Module.sgmodule`。

Stable、Stable Plus、Lite 和 Full 的 profile、Release 文件、晋级脚本及旧测试报告已被移除。历史状态仅通过 Git 提交追溯。

日常维护源头是 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Remotes/` 与 `Rewrite/Profiles/fusion.conf`。`Release/`、`Web/`、`reports/` 与根目录模块均为生成物。

标准维护路径：Fusion 构建器、仓库验证、质量门、健康检查。任何规则、脚本、MITM 或路由变更都应缩小范围并保留可回滚源头。
