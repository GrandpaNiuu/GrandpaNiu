# Workflow 健康报告

- 生成时间：2026-05-31 03:43:11 +0800
- 状态模式：静态清单模式：无法自动获取最近状态（GITHUB_TOKEN not available）

| Workflow | 用途 | 触发方式 | 最近运行时间 | 最近状态 | 结论 | 失败 Job | 失败 Step | 对应 commit | 失败时优先排查 |
|---|---|---|---|---|---|---|---|---|---|
| Module Factory Build | 构建 Release 并同步 Root | 手动 / push | 需要在 GitHub Actions 页面确认 | 存在 | 待人工确认 | 待确认 | 待确认 | 待确认 | build_module.py、factory_finalize.py、profile、sources、Root/Release diff |
| Daily Module Update | 每日日期、结构、链接和验证检查 | 手动 / 定时 / push | 需要在 GitHub Actions 页面确认 | 存在 | 待人工确认 | 待确认 | 待确认 | 待确认 | 核心标记、远程链接、validate_repository.py 输出 |
| Daily invalid source audit and repair | 连续失效源审计和安全处理 | 手动 / 定时 | 需要在 GitHub Actions 页面确认 | 存在 | 待人工确认 | 待确认 | 待确认 | 待确认 | GitHub 网络、history 计数、保护项、误判 404 |
| Upstream candidate collect | 每周可信候选源收集 | 手动 / 定时 | 需要在 GitHub Actions 页面确认 | 存在 | 待人工确认 | 待确认 | 待确认 | 待确认 | candidates.json、风险词、重复源、trusted_repositories |
| Repository Health Check | 仓库治理健康检查 | 手动 / 定时 / push | 需要在 GitHub Actions 页面确认 | 存在 | 待人工确认 | 待确认 | 待确认 | 待确认 | 缺失治理文件、README 链接、重复脚本、重复 MITM |

## 说明

- 有 `GITHUB_TOKEN` 时，本报告尝试读取 GitHub Actions 最近运行状态。
- 无法读取 API 时，报告会退回静态清单模式，并要求人工到 Actions 页面确认。
- 所有会写仓库的 workflow 应使用 `permissions: contents: write` 和共享并发组 `module-maintenance`。
