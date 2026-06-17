# 报告新鲜度检查报告

生成时间：2026-06-17 22:29:51 +0800

本报告检查治理报告是否落后于对应源文件。关键报告 stale 时应视为阻断项；自刷新报告会在质量门禁末尾再生成一次。

## 总览

- 检查项：8
- fresh：5
- stale / missing：3
- blocking stale / missing：0

## 明细

| 报告 | 状态 | 是否阻断 | 报告时间 | 输入最新时间 | 原因 |
|---|---|---|---|---|---|
| `reports/profile_validation_report.md` | fresh | 是 | 2026-06-17 22:29:49 +0800 | 2026-06-17 22:29:46 +0800 | Profile、规则、脚本或构建逻辑变更后必须重新验证 Fusion 构建。 |
| `reports/repository_health_report.md` | stale | 自刷新报告，质量门禁末尾复查 | 2026-06-17 22:29:42 +0800 | 2026-06-17 22:29:49 +0800 | 仓库治理、工作流或模块源头变更后必须刷新健康报告。 |
| `reports/automated_quality_evidence.md` | stale | 自刷新报告，质量门禁末尾复查 | 2026-06-17 22:29:49 +0800 | 2026-06-17 22:29:49 +0800 | 自动化证据报告必须反映当前构建、校验和质量门禁。 |
| `reports/candidate_security_score_report.md` | fresh | 是 | 2026-06-17 22:29:50 +0800 | 2026-06-17 22:29:30 +0800 | 候选源或评分脚本变更后必须刷新安全评分。 |
| `reports/domestic_app_connectivity_audit.md` | fresh | 是 | 2026-06-17 22:29:50 +0800 | 2026-06-17 22:29:30 +0800 | 国内 App 联网风险相关源头变更后必须刷新审计报告。 |
| `reports/reject_risk_report.md` | fresh | 是 | 2026-06-17 22:29:50 +0800 | 2026-06-17 22:29:30 +0800 | REJECT 或 DIRECT 变更后必须刷新误伤风险分类。 |
| `reports/app_status_matrix.md` | fresh | 是 | 2026-06-17 22:29:50 +0800 | 2026-06-17 22:29:49 +0800 | 覆盖源头或状态矩阵生成逻辑变更后必须刷新 App 状态矩阵。 |
| `reports/app_cleaner_active_report.md` | stale | 否 | 2026-06-17 22:29:30 +0800 | 2026-06-17 22:29:30 +0800 | app-cleaner active 入口或融合逻辑变更后建议刷新说明。 |

## 处理规则

- `fresh`：报告不早于输入文件。
- `stale`：报告落后于输入文件，应重新运行对应生成脚本。
- `missing`：报告缺失，应补齐。
- `repository_health_report.md` 与 `automated_quality_evidence.md` 属于自刷新报告，质量门禁运行后应再次刷新。
