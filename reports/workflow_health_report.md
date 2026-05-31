# Workflow 健康报告

生成时间：2026-06-01 03:04:28 +0800

本报告默认不调用 GitHub API。workflow 最新运行状态无法确认，需要在 GitHub Actions 页面确认 completed / success。

| Workflow | 用途 | 触发方式 | 最近状态 | 失败时优先排查 |
|---|---|---|---|---|
| Module Factory Build | 构建 Release 并同步 Root | 手动 / push | 存在；最新状态无法确认 | build_module.py、factory_finalize.py、profile、sources、Root/Release diff |
| Daily Module Update | 每日日期、结构、链接和验证检查 | 手动 / 定时 / push | 存在；最新状态无法确认 | 必要标记、远程链接、validate_repository.py 输出 |
| Daily invalid source audit and repair | 连续失效源审计和安全处理 | 手动 / 定时 | 存在；最新状态无法确认 | GitHub 网络、history 计数、误判 404 |
| Upstream candidate collect | 每周可信候选源收集 | 手动 / 定时 | 存在；最新状态无法确认 | candidates.json、风险词、重复源、trusted_repositories |
| Repository Health Check | 仓库治理健康检查 | 手动 / 定时 / push | 存在；最新状态无法确认 | 治理文件、README 链接、重复脚本、重复 MITM、报告新鲜度 |
| Stable Plus Promotion PR | 单项 App 晋级审查 PR 入口 | 手动 | 存在；最新状态无法确认 | manual_test_log.md、单项 App 范围、PR 是否为 draft |

## 说明

- 如果需要真实最近状态，请打开仓库 Actions 页面确认。
- 所有会写仓库的 workflow 应使用 `permissions: contents: write` 和共享并发组 `module-maintenance`。
- Promotion PR 只允许单项 App 审查，不自动合并，不整体合并 Stable Plus。
