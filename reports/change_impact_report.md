# 变更影响报告

- 生成时间：2026-06-13 08:10:34 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `.github/workflows/daily-module-update.yml`
- `.github/workflows/module-factory-build.yml`
- `.github/workflows/repository-health.yml`
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

- `tests/test_automated_quality_gate.py`
- `tools/generate_automated_quality_evidence.py`

## 删除文件

- 无

## 修改文件

- `.github/workflows/daily-module-update.yml`
- `.github/workflows/module-factory-build.yml`
- `.github/workflows/repository-health.yml`
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
- Scripts/maintenance
- Workflows

## 可能影响的 App

- Spotify
- YouTube
- 知乎
- Bilibili
- 12306

## 风险判断

- 是否涉及脚本：是
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：是
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
