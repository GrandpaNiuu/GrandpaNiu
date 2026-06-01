# Workflow 健康报告

生成时间：2026-06-02 00:27:34 +0800

本报告用于确认 workflow 文件是否存在，并尽量读取 GitHub Actions 最近运行状态。若 API 不可用，则只报告配置存在性，不伪造成功状态。

- Repository：`GrandpaNiuu/GrandpaNiu`

| Workflow | 文件 | 用途 | 触发方式 | 最近运行时间 | Status | Conclusion | Run URL | 处理建议 |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | 构建 Release 并同步 Root | 手动 / push | 2026-06-01T16:27:25Z | pending | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/26767773852) | 运行中或未完成，等待完成后复查 |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | 每日日期、结构、链接和验证检查 | 手动 / 定时 / push | 2026-06-01T14:59:15Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/26763010813) | 通过 |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | 连续失效源审计和安全处理 | 手动 / 定时 | 2026-05-31T20:20:23Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/26723426024) | 通过 |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | 每周可信候选源收集 | 手动 / 定时 | 2026-06-01T15:05:47Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/26763383010) | 通过 |
| Repository Health Check | `.github/workflows/repository-health.yml` | 仓库治理健康检查 | 手动 / 定时 / push | 2026-06-01T16:27:24Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/26767773484) | 运行中或未完成，等待完成后复查 |
| Stable Plus Promotion PR | `.github/workflows/stable-plus-promotion-pr.yml` | 单项 App 晋级审查 PR 入口 | 手动 | 2026-05-31T19:16:55Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/26721985115) | 通过 |

## 说明

- `success` 才能视为 workflow 最近一次运行通过。
- `failure`、`cancelled`、`timed_out`、`action_required` 必须打开对应 run 日志排查。
- API 不可用时，本报告只确认配置存在，不确认真实运行状态。
- Promotion PR 只允许单项 App 审查，不自动合并，不整体合并 Stable Plus。
