# 变更影响报告

- 生成时间：2026-07-10 03:16:25 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `AI_HANDOFF.md`
- `Android/branches.json`
- `PROJECT_STATE.md`
- `Release/Android/branches.json`
- `Release/checksums.json`
- `Scripts/generated/fusion-script-bundle.js`
- `Scripts/generated/fusion-script-bundle.manifest.json`
- `docs/ai/DECISIONS.md`
- `docs/ai/RISK_LOG.md`
- `docs/ai/TASKS.md`
- `docs/ai/WORKLOG.md`
- `reports/android_rules_report.md`
- `reports/app_cleaner_active_report.md`
- `reports/app_source_validation_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/automation_gap_report.md`
- `reports/automation_status_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/false_positive_review_report.md`
- `reports/mitm_optimization_report.json`
- `reports/mitm_optimization_report.md`
- `reports/mitm_reject_risk_ledger.md`
- `reports/mitm_scope_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/platform_compatibility_matrix.md`
- `reports/profile_validation_report.md`
- `reports/protected_traffic_ledger.md`
- `reports/reject_risk_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_encoding_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/rule_overlap_report.md`
- `reports/script_aggregation_report.md`
- `reports/script_aggregation_validation_report.md`
- `reports/script_bundle_sandbox_report.md`
- `reports/script_inventory_report.md`
- `reports/upstream_provenance_report.md`
- `reports/upstream_risk_gate_report.md`
- `reports/workflow_health_report.md`
- `scripts/build_module.py`
- `scripts/check_report_freshness.py`
- `scripts/quality_gate.py`
- `scripts/repository_health_check.py`
- `scripts/validate_repository.py`
- `tests/test_mitm_optimizer.py`
- `tools/build_mitm_baseline.py`
- `tools/generate_automated_quality_evidence.py`
- `tools/generate_automation_gap_report.py`
- `tools/validate_mitm_coverage.py`

## 新增文件

- `reports/mitm_optimization_report.json`
- `reports/mitm_optimization_report.md`
- `tests/test_mitm_optimizer.py`
- `tools/build_mitm_baseline.py`
- `tools/validate_mitm_coverage.py`

## 删除文件

- 无

## 修改文件

- `AI_HANDOFF.md`
- `Android/branches.json`
- `PROJECT_STATE.md`
- `Release/Android/branches.json`
- `Release/checksums.json`
- `Scripts/generated/fusion-script-bundle.js`
- `Scripts/generated/fusion-script-bundle.manifest.json`
- `docs/ai/DECISIONS.md`
- `docs/ai/RISK_LOG.md`
- `docs/ai/TASKS.md`
- `docs/ai/WORKLOG.md`
- `reports/android_rules_report.md`
- `reports/app_cleaner_active_report.md`
- `reports/app_source_validation_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/automation_gap_report.md`
- `reports/automation_status_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/false_positive_review_report.md`
- `reports/mitm_reject_risk_ledger.md`
- `reports/mitm_scope_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/platform_compatibility_matrix.md`
- `reports/profile_validation_report.md`
- `reports/protected_traffic_ledger.md`
- `reports/reject_risk_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_encoding_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/rule_overlap_report.md`
- `reports/script_aggregation_report.md`
- `reports/script_aggregation_validation_report.md`
- `reports/script_bundle_sandbox_report.md`
- `reports/script_inventory_report.md`
- `reports/upstream_provenance_report.md`
- `reports/upstream_risk_gate_report.md`
- `reports/workflow_health_report.md`
- `scripts/build_module.py`
- `scripts/check_report_freshness.py`
- `scripts/quality_gate.py`
- `scripts/repository_health_check.py`
- `scripts/validate_repository.py`
- `tools/generate_automated_quality_evidence.py`
- `tools/generate_automation_gap_report.py`

## 影响的模块层

- Other
- README/docs
- Scripts
- Scripts/maintenance

## 可能影响的 App

- Spotify
- YouTube
- 知乎
- Bilibili
- 微博
- 百度贴吧
- 小红书
- 酷安
- 淘宝
- 闲鱼
- 京东
- 拼多多
- 美团
- 大众点评
- 饿了么
- 滴滴
- 12306
- 高德地图
- 百度地图
- 网易云音乐
- 喜马拉雅
- 小宇宙
- 斗鱼
- Reddit

## 风险判断

- 是否涉及脚本：是
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：是
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：是

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
