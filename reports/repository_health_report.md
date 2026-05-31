# 仓库健康检查报告

生成时间：2026-06-01 02:37:23 +0800

## 总体状态

- 阻断问题：0
- Root 与 Release 一致：是
- GrandpaNiu = 默认 Stable：是
- validate_repository.py：通过
- node --check Scripts/app-cleaner.js：通过
- workflow 最新状态：无法确认，需要在 GitHub Actions 页面确认 completed / success
- 微信广告仅 Stable Plus：是
- 脚本总数：33
- MITM hostname 数量：120

## 区块检查

- [Rule]：570 行
- [URL Rewrite]：1597 行
- [Header Rewrite]：5 行
- [Body Rewrite]：455 行
- [Map Local]：15 行
- [Script]：152 行
- [MITM]：4 行

## 报告生成器运行结果

- `scripts/audit_reject_risk.py`：通过
- `scripts/generate_app_status_matrix.py`：通过
- `scripts/create_promotion_pr.py`：通过
- `scripts/score_candidates.py`：通过
- `scripts/audit_domestic_app_connectivity.py`：通过
- `scripts/generate_workflow_health_report.py`：通过
- `scripts/check_report_freshness.py`：通过

## 阻断问题

- 无

## 缺少文件

- 无

## 缺少 workflow

- 无

## 缺少报告

- 无

## 主模块缺少标记

- 无

## 重复脚本名

- 无

## 重复 MITM hostname

- 无

## README 失效本地链接

- 无

## Blocking stale reports

- 无

## Workflow 配置摘要

- `.github/workflows/module-factory-build.yml`：contents: write；concurrency；node --check；默认 stable
- `.github/workflows/daily-module-update.yml`：contents: write；concurrency；默认 stable
- `.github/workflows/daily-invalid-source-repair.yml`：contents: write；concurrency；默认 stable
- `.github/workflows/upstream-collect.yml`：contents: write；concurrency；默认 stable
- `.github/workflows/repository-health.yml`：contents: write；concurrency；node --check；默认 stable
- `.github/workflows/stable-plus-promotion-pr.yml`：contents: write；concurrency；默认 stable

## validate_repository.py 输出

```text
Repository validation passed.
```

## node --check 输出

```text
无输出
```

## 维护边界

- 所有修改应 source-first，先改 Rules / Scripts / Rewrite/Sources / Rewrite/Remotes / Rewrite/Profiles，再构建 Release 和 Root。
- Stable 目标是稳定、低误伤、可长期使用，不追求最大覆盖。
- Stable Plus 只做增强测试，不整体合并进 Stable。
- 没有真实手测记录时，报告必须写未测或 manual-review。
- 本报告无法确认远端 workflow 最新运行状态，需在 GitHub Actions 页面查看。
