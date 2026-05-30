<div align="center">

# GrandpaNiu

Shadowrocket / Surge 自用融合净化模块工厂。

[![安装模块](https://img.shields.io/static/v1?label=Install&message=Shadowrocket&color=0A84FF&labelColor=111827&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule)
[![备用页面](https://img.shields.io/static/v1?label=Fallback&message=Import%20Page&color=34C759&labelColor=111827&style=for-the-badge)](https://grandpaniuu.github.io/GrandpaNiu/import.html)

</div>

## 导入入口

| 入口 | 链接 |
|---|---|
| 一键导入 | [Shadowrocket 安装入口](https://grandpaniuu.github.io/GrandpaNiu/redirect.html?url=shadowrocket%3A%2F%2Finstall%3Fmodule%3Dhttps%3A%2F%2Fraw.githubusercontent.com%2FGrandpaNiuu%2FGrandpaNiu%2Fmain%2FRonghemokuai.sgmodule) |
| 备用页面 | [import.html](https://grandpaniuu.github.io/GrandpaNiu/import.html) |
| Raw 地址 | [Ronghemokuai.sgmodule](https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Ronghemokuai.sgmodule) |
| Pages 地址 | [Ronghemokuai.sgmodule](https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule) |

导入后建议在 Shadowrocket 中更新模块、更新脚本、更新全部资源。

## 项目定位

正式导入入口是 `Ronghemokuai.sgmodule`，但它是工厂生成结果，不是长期手工维护源头。

```text
Rules + Scripts + Rewrite/Sources + Rewrite/Remotes + Rewrite/Profiles
        -> scripts/build_module.py --build --profile stable
        -> Release/Ronghemokuai.sgmodule
        -> scripts/factory_finalize.py --sync-root
        -> Ronghemokuai.sgmodule
```

## 当前状态

| 项目 | 状态 |
|---|---|
| 默认 profile | `stable` |
| 低耗电 profile | `lite`，不默认发布 |
| 全覆盖测试 profile | `full`，不默认发布 |
| Root / Release | 通过 `reports/repository_health_report.md` 与 diff 报告确认 |
| 质量门禁 | `scripts/validate_repository.py` |
| 健康报告 | `reports/repository_health_report.md` |
| Profile 验证 | `reports/profile_validation_report.md` |
| MITM 状态 | 数量较大，已进入分层治理；查看 `reports/mitm_split_report.md` |
| 规则收集策略 | 可信候选源，不做全网大规模自动收集 |
| 脚本策略 | 默认 pending，不直接进入 stable |
| 手动测试 | 记录在 `reports/manual_test_log.md`，未测不得写通过 |

## Profile

| Profile | 定位 |
|---|---|
| `stable.conf` | 默认正式版 |
| `lite.conf` | 低耗电参考版，不默认发布 |
| `full.conf` | 全覆盖测试版，不默认发布 |

默认 GitHub Actions 仍使用 `stable`。

## 核心能力

- 通用广告、开屏、弹窗、横幅、信息流、推荐位和活动卡片清理。
- Spotify 播放链路保护。
- YouTube Enhance 保留。
- 知乎增强净化。
- 常用 App 和网页广告净化。
- 可信远程规则源维护。
- 失效源审计、安全候选源收集、健康报告和回滚备份。

## 安全边界

本仓库不加入会员解锁、Premium 破解、支付绕过、登录绕过、账户权益伪造、Cookie / Token / BoxJS、成人、博彩、短链、镜像源、`ghproxy` 或未知混淆脚本。

Spotify、YouTube、知乎、登录、支付、验证码、银行、微信、支付宝优先保护。

## 维护入口

| 类型 | 链接 | 用途 |
|---|---|---|
| 工厂流程 | [docs/FACTORY_FLOW.md](docs/FACTORY_FLOW.md) | 源头驱动构建说明 |
| 维护标准 | [docs/MAINTENANCE.md](docs/MAINTENANCE.md) | 日常维护规则 |
| 发布回滚 | [docs/RELEASE.md](docs/RELEASE.md) | 发布、测试、回滚流程 |
| 测试标准 | [docs/TESTING.md](docs/TESTING.md) | 手动测试流程和记录要求 |
| 性能说明 | [docs/PERFORMANCE.md](docs/PERFORMANCE.md) | profile 和耗电策略 |
| 安全政策 | [SECURITY.md](SECURITY.md) | 安全边界和报告方式 |
| 个人自用声明 | [LICENSE](LICENSE) | 使用限制和风险声明 |
| 贡献规则 | [CONTRIBUTING.md](CONTRIBUTING.md) | 后续维护者规则 |
| 脚本审核 | [docs/SCRIPT_REVIEW.md](docs/SCRIPT_REVIEW.md) | 脚本进入 stable 前检查 |
| MITM 策略 | [docs/MITM_POLICY.md](docs/MITM_POLICY.md) | hostname 分级和增长控制 |
| 版本策略 | [docs/VERSIONING.md](docs/VERSIONING.md) | 日期和语义版本规则 |
| 覆盖清单 | [docs/COVERAGE.md](docs/COVERAGE.md) | 功能覆盖方向 |
| 项目范围 | [docs/SCOPE.md](docs/SCOPE.md) | 允许和禁止内容 |
| 问题排查 | [docs/TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | 常见异常定位 |
| 质量门禁 | [docs/QUALITY_GATE.md](docs/QUALITY_GATE.md) | 阻断项和发布前检查 |
| 变更记录 | [CHANGELOG.md](CHANGELOG.md) | 版本和维护记录 |
| 备份说明 | [backup/README.md](backup/README.md) | 回滚方式 |
| 备份清单 | [backup/manifest.json](backup/manifest.json) | 可用备份文件 |
| 工厂工作流 | [.github/workflows/module-factory-build.yml](.github/workflows/module-factory-build.yml) | stable 构建与同步 |
| 每日检查工作流 | [.github/workflows/daily-module-update.yml](.github/workflows/daily-module-update.yml) | 日期、结构和核心远程检查 |
| 失效源修复工作流 | [.github/workflows/daily-invalid-source-repair.yml](.github/workflows/daily-invalid-source-repair.yml) | 连续失效后的保守修复 |
| 候选源收集工作流 | [.github/workflows/upstream-collect.yml](.github/workflows/upstream-collect.yml) | 可信候选规则源周检查 |
| 健康检查工作流 | [.github/workflows/repository-health.yml](.github/workflows/repository-health.yml) | 仓库治理报告 |

## 报告入口

| 报告 | 用途 |
|---|---|
| [reports/module_factory_report.md](reports/module_factory_report.md) | 模块工厂构建报告 |
| [reports/module_factory_diff_report.md](reports/module_factory_diff_report.md) | Root / Release 差异 |
| [reports/factory_finalize_report.md](reports/factory_finalize_report.md) | finalize 同步报告 |
| [reports/daily_update_report.md](reports/daily_update_report.md) | 每日检查报告 |
| [reports/invalid_sources_report.md](reports/invalid_sources_report.md) | 失效源审计 |
| [reports/invalid_sources_history.json](reports/invalid_sources_history.json) | 失效源历史 |
| [reports/upstream_collect_report.md](reports/upstream_collect_report.md) | 候选源收集 |
| [reports/repository_health_report.md](reports/repository_health_report.md) | 仓库健康检查 |
| [reports/compat_migration_report.md](reports/compat_migration_report.md) | 兼容层迁移审计 |
| [reports/mitm_split_report.md](reports/mitm_split_report.md) | MITM 分层报告 |
| [reports/profile_validation_report.md](reports/profile_validation_report.md) | stable / lite / full 构建验证 |
| [reports/app_coverage_matrix.md](reports/app_coverage_matrix.md) | App 覆盖矩阵 |
| [reports/change_impact_report.md](reports/change_impact_report.md) | 变更影响报告 |
| [reports/workflow_health_report.md](reports/workflow_health_report.md) | workflow 健康报告 |
| [reports/manual_test_log.md](reports/manual_test_log.md) | 手动测试记录 |

## 常用验证

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```