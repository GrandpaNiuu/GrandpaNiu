# Workflow 健康报告

- 生成时间：2026-05-31 03:07:19 +0800
- 最近状态：需要在 GitHub Actions 页面确认

| Workflow | 用途 | 触发方式 | 最近状态 | 失败时优先排查 |
|---|---|---|---|---|
| Module Factory Build | 构建 Release 并同步 Root | 手动 / push | 存在，最近状态需在 GitHub Actions 页面确认 | build_module.py、factory_finalize.py、profile、sources、Root/Release diff |
| Daily Module Update | 每日日期、结构、链接和验证检查 | 手动 / 定时 / push | 存在，最近状态需在 GitHub Actions 页面确认 | 核心标记、远程链接、validate_repository.py 输出 |
| Daily invalid source audit and repair | 连续失效源审计和安全处理 | 手动 / 定时 | 存在，最近状态需在 GitHub Actions 页面确认 | GitHub 网络、history 计数、保护项、误判 404 |
| Upstream candidate collect | 每周可信候选源收集 | 手动 / 定时 | 存在，最近状态需在 GitHub Actions 页面确认 | candidates.json、风险词、重复源、trusted_repositories |
| Repository Health Check | 仓库治理健康检查 | 手动 / 定时 / push | 存在，最近状态需在 GitHub Actions 页面确认 | 缺失治理文件、README 链接、重复脚本、重复 MITM |

## 说明

- 本报告不调用 GitHub API；如果需要最近运行状态，请打开仓库 Actions 页面确认。
- 所有会写仓库的 workflow 应使用 `permissions: contents: write` 和共享并发组 `module-maintenance`。
