# 变更影响报告

- 生成时间：2026-06-13 08:21:44 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `.github/workflows/daily-module-update.yml`
- `.github/workflows/module-factory-build.yml`
- `.github/workflows/repository-health.yml`
- `Release/Module.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Ronghemokuai.sgmodule`
- `Scripts/youtube.conf`
- `docs/ARCHITECTURE.md`
- `docs/AUTOMATION_POLICY.md`
- `docs/CODEX_EXECUTION_STANDARD.md`
- `docs/COVERAGE.md`
- `docs/FOUR_PROFILE_GOVERNANCE.md`
- `docs/LOCAL_ENV_SETUP.md`
- `docs/MAINTENANCE_PLAYBOOK.md`
- `docs/MITM_POLICY.md`
- `docs/MODULE_FEATURES.md`
- `docs/PROFILE_POLICY.md`
- `docs/QUALITY_GATE.md`
- `docs/ROADMAP.md`
- `docs/SCRIPT_CONSOLIDATION_PLAN.md`
- `docs/SCRIPT_REVIEW.md`
- `docs/TESTING.md`
- `reports/android_rules_report.md`
- `reports/app_coverage_matrix.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/reject_risk_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`
- `scripts/audit_compat_sources.py`
- `scripts/check_report_freshness.py`
- `scripts/collect_upstreams.py`
- `scripts/create_promotion_pr.py`
- `scripts/generate_app_coverage_matrix.py`
- `scripts/generate_app_status_matrix.py`
- `scripts/generate_script_inventory_report.py`
- `scripts/generate_stable_plus_promotion_report.py`
- `scripts/quality_gate.py`
- `scripts/repository_health_check.py`
- `scripts/safe_refine_module.py`
- `scripts/validate_governance_extensions.py`
- `scripts/validate_repository.py`
- `tests/test_automated_quality_gate.py`
- `tools/generate_automated_quality_evidence.py`

## 新增文件

- `reports/automated_quality_evidence.md`
- `tests/test_automated_quality_gate.py`
- `tools/generate_automated_quality_evidence.py`

## 删除文件

- 无

## 修改文件

- `.github/workflows/daily-module-update.yml`
- `.github/workflows/module-factory-build.yml`
- `.github/workflows/repository-health.yml`
- `Release/Module.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Ronghemokuai.sgmodule`
- `Scripts/youtube.conf`
- `docs/ARCHITECTURE.md`
- `docs/AUTOMATION_POLICY.md`
- `docs/CODEX_EXECUTION_STANDARD.md`
- `docs/COVERAGE.md`
- `docs/FOUR_PROFILE_GOVERNANCE.md`
- `docs/LOCAL_ENV_SETUP.md`
- `docs/MAINTENANCE_PLAYBOOK.md`
- `docs/MITM_POLICY.md`
- `docs/MODULE_FEATURES.md`
- `docs/PROFILE_POLICY.md`
- `docs/QUALITY_GATE.md`
- `docs/ROADMAP.md`
- `docs/SCRIPT_CONSOLIDATION_PLAN.md`
- `docs/SCRIPT_REVIEW.md`
- `docs/TESTING.md`
- `reports/android_rules_report.md`
- `reports/app_coverage_matrix.md`
- `reports/app_status_matrix.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/reject_risk_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`
- `scripts/audit_compat_sources.py`
- `scripts/check_report_freshness.py`
- `scripts/collect_upstreams.py`
- `scripts/create_promotion_pr.py`
- `scripts/generate_app_coverage_matrix.py`
- `scripts/generate_app_status_matrix.py`
- `scripts/generate_script_inventory_report.py`
- `scripts/generate_stable_plus_promotion_report.py`
- `scripts/quality_gate.py`
- `scripts/repository_health_check.py`
- `scripts/safe_refine_module.py`
- `scripts/validate_governance_extensions.py`
- `scripts/validate_repository.py`

## 影响的模块层

- Other
- README/docs
- Scripts
- Scripts/maintenance
- Workflows

## 可能影响的 App

- Spotify
- YouTube
- 知乎
- Bilibili
- 微博
- 百度贴吧
- 美团
- 滴滴
- 12306
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
