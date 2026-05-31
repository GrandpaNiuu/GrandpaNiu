# Workflow 健康报告

生成时间：2026-06-01 03:04:28 +0800

本报告默认不调用 GitHub API。workflow 最新运行状态无法确认，需要在 GitHub Actions 页面确认 completed / success。

## Workflow failure issue 说明

`Workflow failure issue` 是失败监听器，不是普通构建任务。它监听其他 workflow 的完成事件。

正常情况：

- 上游 workflow 成功：`Workflow failure issue` 会显示 `skipped`，这是正常现象。
- 上游 workflow 被正常跳过：`Workflow failure issue` 也可能显示 `skipped`，不代表失败。
- 只有上游 workflow 的 conclusion 为 `failure`、`timed_out`、`action_required`、`cancelled` 时，才会自动创建或更新 Issue。
- 不把正常 `skipped` 当作失败，避免误报。

## Workflow 列表

| Workflow | 用途 | 触发方式 | 最近状态 | 失败时优先排查 |
|---|---|---|---|---|
| Module Factory Build | 构建 Release 并同步 Root | 手动 / push | 存在；最新状态无法确认 | build_module.py、factory_finalize.py、profile、sources、Root/Release diff |
| Daily Module Update | 每日日期、结构、链接和验证检查 | 手动 / 定时 / push | 存在；最新状态无法确认 | 必要标记、远程链接、validate_repository.py 输出 |
| Daily invalid source audit and repair | 连续失效源审计和安全处理 | 手动 / 定时 | 存在；最新状态无法确认 | GitHub 网络、history 计数、误判 404 |
| Upstream candidate collect | 每周可信候选源收集 | 手动 / 定时 | 存在；最新状态无法确认 | candidates.json、风险词、重复源、trusted_repositories |
| Repository Health Check | 仓库治理健康检查 | 手动 / 定时 / push | 存在；最新状态无法确认 | 治理文件、README 链接、重复脚本、重复 MITM、报告新鲜度 |
| Stable Plus Promotion PR | 单项 App 晋级审查 PR 入口 | 手动 | 存在；最新状态无法确认 | manual_test_log.md、单项 App 范围、PR 是否为 draft |
| Workflow failure issue | 监听 workflow 非正常结束并自动开 Issue | workflow_run | skipped 通常正常；最新状态无法确认 | 监听列表、conclusion 条件、issues 权限 |

## Workflow failure issue 监听范围

当前应监听：

- Module Factory Build
- Daily Module Update
- Daily invalid source audit and repair
- Upstream candidate collect
- Repository Health Check
- Stable Plus Promotion PR

## Workflow failure issue 开 Issue 条件

只在以下 conclusion 时开 Issue：

- failure
- timed_out
- action_required
- cancelled

不会因为以下正常状态开 Issue：

- success
- skipped

## 说明

- 如果需要真实最近状态，请打开仓库 Actions 页面确认。
- 所有会写仓库的 workflow 应使用 `permissions: contents: write` 和共享并发组 `module-maintenance`。
- Promotion PR 只允许单项 App 审查，不自动合并，不整体合并 Stable Plus。
- `Workflow failure issue` 显示 skipped 时，先检查被监听的上游 workflow 是否成功；如果上游成功，则 skipped 是预期行为。
