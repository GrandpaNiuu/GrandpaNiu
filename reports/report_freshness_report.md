# 报告新鲜度检查报告

生成时间：2026-06-03 08:51:04 +0800

本报告检查治理报告是否落后于对应源文件。关键报告 stale 时应视为阻断项；`manual_test_log.md` 只作为 manual-review，不自动失败。

## 总览

- 检查项：8
- fresh：5
- stale / missing：2
- blocking stale / missing：0
- manual-review：1

## 明细

| 报告 | 状态 | 是否阻断 | 报告时间 | 输入最新时间 | 原因 |
|---|---|---|---|---|---|
| `reports/profile_validation_report.md` | fresh | 是 | 2026-06-03 08:51:01 +0800 | 2026-06-03 08:51:00 +0800 | Profile、规则、脚本或构建逻辑变更后必须重新验证四版本构建。 |
| `reports/repository_health_report.md` | stale | 自刷新报告，Repository Health 运行后复查 | 2026-06-03 08:51:00 +0800 | 2026-06-03 08:51:01 +0800 | 仓库治理、工作流或模块源头变更后必须刷新健康报告。 |
| `reports/candidate_security_score_report.md` | fresh | 是 | 2026-06-03 08:51:04 +0800 | 2026-06-03 08:51:00 +0800 | 候选源或评分脚本变更后必须刷新安全评分。 |
| `reports/domestic_app_connectivity_audit.md` | fresh | 是 | 2026-06-03 08:51:04 +0800 | 2026-06-03 08:51:00 +0800 | 国内 App 联网风险相关源头变更后必须刷新审计报告。 |
| `reports/reject_risk_report.md` | fresh | 是 | 2026-06-03 08:51:03 +0800 | 2026-06-03 08:51:00 +0800 | REJECT 或 DIRECT 变更后必须刷新误伤风险分类。 |
| `reports/app_status_matrix.md` | fresh | 是 | 2026-06-03 08:51:03 +0800 | 2026-06-03 08:51:01 +0800 | 覆盖源头或人工测试记录变更后必须刷新 App 状态矩阵。 |
| `reports/manual_test_log.md` | manual-review | 否 | 2026-06-03 08:51:00 +0800 | 2026-06-03 08:51:01 +0800 | 人工测试记录落后时只进入 manual-review，不自动写成通过。 |
| `reports/app_cleaner_active_report.md` | stale | 否 | 2026-06-03 08:51:00 +0800 | 2026-06-03 08:51:00 +0800 | app-cleaner active 入口或融合逻辑变更后建议刷新说明。 |

## 处理规则

- `fresh`：报告不早于输入文件。
- `stale`：报告落后于输入文件，应重新运行对应生成脚本。
- `missing`：报告缺失，应补齐。
- `manual-review`：人工测试记录落后于模块变更，应确认仍为未测或更新真实测试结果。
- `repository_health_report.md` 属于自刷新报告，健康检查运行后应再次刷新本报告。
