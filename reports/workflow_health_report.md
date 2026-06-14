# Workflow 健康报告

生成时间：2026-06-14 13:11:11 +0800

本报告用于确认 workflow 文件是否存在，并尽量读取 GitHub Actions 最近运行状态。若 API 不可用，则只报告配置存在性，不伪造成功状态。

- Repository：`GrandpaNiuu/GrandpaNiu`

| Workflow | 文件 | 用途 | 触发方式 | 最近运行时间 | Status | Conclusion | Run URL | 处理建议 |
|---|---|---|---|---|---|---|---|---|
| Module Factory Build | `.github/workflows/module-factory-build.yml` | 构建 Release 并同步 Root | 手动 / push | 2026-06-14T05:10:25Z | in_progress | pending | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27489109049) | 运行中或未完成，等待完成后复查 |
| Daily Module Update | `.github/workflows/daily-module-update.yml` | 每日日期、结构、链接和验证检查 | 手动 / 定时 / push | 2026-06-14T05:10:25Z | completed | cancelled | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27489109069) | 已取消；通常是 module-maintenance 并发组被更新运行替代，连续取消时再人工复核 |
| Daily invalid source audit and repair | `.github/workflows/daily-invalid-source-repair.yml` | 连续失效源审计和安全处理 | 手动 / 定时 / push | 2026-06-14T00:12:50Z | completed | cancelled | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27483184246) | 已取消；通常是 module-maintenance 并发组被更新运行替代，连续取消时再人工复核 |
| Upstream candidate collect | `.github/workflows/upstream-collect.yml` | 每周可信候选源收集 | 手动 / 定时 / push | 2026-06-14T00:12:50Z | completed | cancelled | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27483184252) | 已取消；通常是 module-maintenance 并发组被更新运行替代，连续取消时再人工复核 |
| Repository Health Check | `.github/workflows/repository-health.yml` | 仓库治理健康检查 | 手动 / 定时 / push | 2026-06-14T05:10:25Z | completed | success | [open](https://github.com/GrandpaNiuu/GrandpaNiu/actions/runs/27489109059) | 通过 |

## 说明

- `success` 才能视为 workflow 最近一次运行通过。
- `failure`、`timed_out`、`action_required` 必须打开对应 run 日志排查；`cancelled` 通常由并发组替代旧运行导致。
- API 不可用时，本报告只确认配置存在，不确认真实运行状态。
- iOS 公开入口只保留 Fusion；旧 Stable / Stable Plus / Lite / Full 不再作为正式 workflow 入口。
