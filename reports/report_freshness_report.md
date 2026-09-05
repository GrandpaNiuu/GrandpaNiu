# 报告新鲜度检查报告

生成时间：2026-09-06 02:33:45 +0800

本报告检查治理报告是否落后于对应源文件。关键报告 stale 时应视为阻断项；自刷新报告会在质量门禁末尾再生成一次。

## 总览

- 检查项：23
- fresh：23
- stale / missing：0
- blocking stale / missing：0

## 明细

| 报告 | 状态 | 是否阻断 | 报告时间 | 输入最新时间 | 原因 |
|---|---|---|---|---|---|
| `reports/app_source_validation_report.md` | fresh | 是 | 2026-09-06 02:33:22 +0800 | 2026-09-06 02:33:01 +0800 | App 源或上游转换逻辑变更后必须重新验证每个独立模块的语法。 |
| `reports/profile_validation_report.md` | fresh | 是 | 2026-09-06 02:33:27 +0800 | 2026-09-06 02:33:25 +0800 | Profile、规则、脚本或构建逻辑变更后必须重新验证 Fusion 构建。 |
| `reports/module_budget_report.md` | fresh | 是 | 2026-09-06 02:33:30 +0800 | 2026-09-06 02:33:27 +0800 | Fusion 体积、超长行、Section、Script 和 MITM 预算必须反映当前生成模块。 |
| `reports/repository_health_report.md` | fresh | 是 | 2026-09-06 02:33:45 +0800 | 2026-09-06 02:33:25 +0800 | 仓库治理、工作流或模块源头变更后必须刷新健康报告。 |
| `reports/automated_quality_evidence.md` | fresh | 是 | 2026-09-06 02:33:44 +0800 | 2026-09-06 02:33:25 +0800 | 自动化证据报告必须反映当前构建、校验和质量门禁。 |
| `reports/automation_status_report.md` | fresh | 是 | 2026-09-06 02:33:44 +0800 | 2026-09-06 02:33:01 +0800 | Automation status report must reflect the current workflow set and watchdog policy. |
| `reports/automation_gap_report.md` | fresh | 是 | 2026-09-06 02:33:44 +0800 | 2026-09-06 02:33:25 +0800 | Automation gap report must reflect current workflow wiring, platform parity, app module coverage, and script aggregation cache state. |
| `reports/candidate_security_score_report.md` | fresh | 是 | 2026-09-06 02:33:34 +0800 | 2026-09-06 02:33:01 +0800 | 候选源或评分脚本变更后必须刷新安全评分。 |
| `reports/domestic_app_connectivity_audit.md` | fresh | 是 | 2026-09-06 02:33:34 +0800 | 2026-09-06 02:33:01 +0800 | 国内 App 联网风险相关源头变更后必须刷新审计报告。 |
| `reports/reject_risk_report.md` | fresh | 是 | 2026-09-06 02:33:34 +0800 | 2026-09-06 02:33:01 +0800 | REJECT 或 DIRECT 变更后必须刷新误伤风险分类。 |
| `reports/app_status_matrix.md` | fresh | 是 | 2026-09-06 02:33:34 +0800 | 2026-09-06 02:33:25 +0800 | 覆盖源头或状态矩阵生成逻辑变更后必须刷新 App 状态矩阵。 |
| `reports/script_aggregation_validation_report.md` | fresh | 是 | 2026-09-06 02:33:27 +0800 | 2026-09-06 02:33:25 +0800 | Script aggregation manifest and bundle changes must be validated. |
| `reports/script_bundle_sandbox_report.md` | fresh | 是 | 2026-09-06 02:33:29 +0800 | 2026-09-06 02:33:25 +0800 | Script bundle runtime sandbox coverage must match the generated bundle. |
| `reports/upstream_risk_gate_report.md` | fresh | 是 | 2026-09-06 02:33:22 +0800 | 2026-09-06 02:33:01 +0800 | Enabled direct-commit upstream app modules must pass the risk gate. |
| `reports/mitm_scope_report.md` | fresh | 是 | 2026-09-06 02:33:30 +0800 | 2026-09-06 02:33:27 +0800 | MITM scope report must reflect the current generated module. |
| `reports/mitm_optimization_report.md` | fresh | 是 | 2026-09-06 02:33:28 +0800 | 2026-09-06 02:33:28 +0800 | MITM optimization report must reflect the current generated Fusion MITM output and compiler contract. |
| `reports/mitm_reject_risk_ledger.md` | fresh | 是 | 2026-09-06 02:33:30 +0800 | 2026-09-06 02:33:25 +0800 | MITM / REJECT 风险台账必须反映当前源文件范围，并且只能标记风险、不直接改规则。 |
| `reports/upstream_provenance_report.md` | fresh | 是 | 2026-09-06 02:33:30 +0800 | 2026-09-06 02:33:01 +0800 | 上游来源、可信分层和许可台账必须反映当前直接同步配置。 |
| `reports/platform_compatibility_matrix.md` | fresh | 是 | 2026-09-06 02:33:30 +0800 | 2026-09-06 02:33:27 +0800 | 平台兼容矩阵必须反映当前 iOS、Android、Windows 输出边界。 |
| `reports/protected_traffic_ledger.md` | fresh | 是 | 2026-09-06 02:33:30 +0800 | 2026-09-06 02:33:01 +0800 | 登录、支付、银行、视频、CDN 和 HTTPDNS 保护链路台账必须保持新鲜。 |
| `reports/false_positive_review_report.md` | fresh | 是 | 2026-09-06 02:33:34 +0800 | 2026-09-06 02:33:34 +0800 | 误伤复核队列必须基于最新风险台账和保护链路台账。 |
| `reports/rule_overlap_report.md` | fresh | 否 | 2026-09-06 02:33:30 +0800 | 2026-09-06 02:33:16 +0800 | Source-level rule overlap report should reflect current rule files. |
| `reports/app_cleaner_active_report.md` | fresh | 否 | 2026-09-06 02:33:30 +0800 | 2026-09-06 02:33:01 +0800 | app-cleaner active 入口或融合逻辑变更后建议刷新说明。 |

## 处理规则

- `fresh`：报告不早于输入文件。
- `stale`：报告落后于输入文件，应重新运行对应生成脚本。
- `missing`：报告缺失，应补齐。
- `repository_health_report.md` 与 `automated_quality_evidence.md` 属于自刷新报告，质量门禁运行后应再次刷新。
