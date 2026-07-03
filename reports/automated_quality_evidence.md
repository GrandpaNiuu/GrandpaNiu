# 自动化质量证据报告

生成时间：2026-07-03 08:15:26 +0800
Git 分支：`repair/upstream-app-sync`
Git 提交：`81db9891`

本仓库发布门禁以可重复执行的自动化证据为准：构建、语法检查、远程规则校验、模块完整性、报告新鲜度和仓库健康检查。

## 核心结论

- Root / Release 一致：是
- UTF-8 BOM 命中：0
- 证据报告数量：25

## 必跑自动化命令

- `python -m py_compile scripts/*.py Rewrite/Generator/Builder.py tools/*.py`
- `node --check Scripts/app-cleaner.js`
- `python -m unittest discover -s tests`
- `python scripts/convert_quanx_rules.py`
- `python Rewrite/Generator/Builder.py --profile fusion --release`
- `python scripts/validate_app_sources.py`
- `python scripts/android_format_check.py`
- `node --check Scripts/generated/fusion-script-bundle.js`
- `python tools/validate_script_aggregation.py`
- `python tools/test_script_bundle_sandbox.py`
- `python tools/validate_upstream_risk_gate.py`
- `python scripts/validate_generator_config.py`
- `python scripts/validate_manifest.py`
- `python scripts/validate_remote_rule_syntax.py`
- `python scripts/validate_governance_extensions.py`
- `python scripts/validate_profiles.py`
- `python scripts/validate_module_integrity.py`
- `python tools/generate_mitm_scope_report.py`
- `python tools/generate_mitm_reject_risk_ledger.py`
- `python tools/generate_rule_overlap_report.py`
- `python tools/generate_app_cleaner_active_report.py`
- `python scripts/repository_health_check.py`
- `python scripts/check_automation_status.py`
- `python tools/generate_automation_gap_report.py`
- `python tools/check_report_encoding.py`
- `python tools/generate_automated_quality_evidence.py`
- `python scripts/validate_repository.py`

## 证据文件状态

| 文件 | 状态 |
|---|---|
| `reports/android_rules_report.md` | present |
| `reports/module_integrity_report.md` | present |
| `reports/app_source_validation_report.md` | present |
| `reports/multi_release_report.md` | present |
| `reports/profile_validation_report.md` | present |
| `reports/remote_rule_syntax_report.md` | present |
| `reports/repository_health_report.md` | present |
| `reports/report_freshness_report.md` | present |
| `reports/app_coverage_matrix.md` | present |
| `reports/app_status_matrix.md` | present |
| `reports/script_inventory_report.md` | present |
| `reports/script_aggregation_report.md` | present |
| `reports/script_aggregation_validation_report.md` | present |
| `reports/script_bundle_sandbox_report.md` | present |
| `reports/upstream_risk_gate_report.md` | present |
| `reports/mitm_scope_report.md` | present |
| `reports/mitm_reject_risk_ledger.md` | present |
| `reports/rule_overlap_report.md` | present |
| `reports/app_cleaner_active_report.md` | present |
| `reports/candidate_security_score_report.md` | present |
| `reports/reject_risk_report.md` | present |
| `reports/domestic_app_connectivity_audit.md` | present |
| `reports/automation_status_report.md` | present |
| `reports/automation_gap_report.md` | present |
| `reports/report_encoding_report.md` | present |

## BOM 扫描

- 未发现 UTF-8 BOM。

## 发布策略

- 自动化门禁失败时不得发布主模块。
- 静态覆盖不写成已验证通过；它只表示规则、脚本或 MITM 层存在命中。
- 用户反馈可以作为 Issue 输入，但不是发布阻断门禁。
- 高风险改动必须保留来源、风险、回滚路径，并通过自动化质量门禁。
