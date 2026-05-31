# 变更影响报告

- 生成时间：2026-06-01 05:27:54 +0800
- 变更识别模式：fallback 最近修改时间模式

## 本次修改文件

- `Rewrite/Sources/MITM-app-clean.conf`
- `Rewrite/Sources/MITM-core.conf`
- `Rewrite/Sources/MITM-extended.conf`
- `reports/app_coverage_matrix.md`
- `reports/app_status_matrix.md`
- `reports/candidate_security_score_report.md`
- `reports/compat_migration_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/factory_finalize_report.md`
- `reports/mitm_split_report.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/promotion_pr_report.md`
- `reports/reject_risk_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`
- `reports/script_inventory_report.md`
- `reports/stable_plus_promotion_report.md`
- `scripts/generate_app_coverage_matrix.py`
- `scripts/generate_app_status_matrix.py`
- `scripts/generate_change_impact_report.py`
- `scripts/generate_stable_plus_promotion_report.py`
- `scripts/generate_workflow_health_report.py`
- `scripts/migrate_legacy_selected_rules.py`
- `scripts/score_candidates.py`
- `scripts/split_mitm_sources.py`
- `scripts/validate_profiles.py`
- `scripts/validate_repository.py`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `reports/app_status_matrix.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/reject_risk_report.md`
- `reports/candidate_security_score_report.md`
- `reports/script_inventory_report.md`
- `reports/promotion_pr_report.md`
- `reports/stable_plus_promotion_report.md`
- `reports/app_coverage_matrix.md`
- `reports/profile_validation_report.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/multi_release_report.md`
- `reports/mitm_split_report.md`
- `Rewrite/Sources/MITM-extended.conf`
- `Rewrite/Sources/MITM-app-clean.conf`
- `Rewrite/Sources/MITM-core.conf`
- `reports/compat_migration_report.md`
- `reports/factory_finalize_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`
- `scripts/validate_profiles.py`
- `scripts/validate_repository.py`
- `scripts/split_mitm_sources.py`
- `scripts/score_candidates.py`
- `scripts/generate_app_coverage_matrix.py`
- `scripts/migrate_legacy_selected_rules.py`
- `scripts/generate_app_status_matrix.py`
- `scripts/generate_change_impact_report.py`
- `scripts/generate_workflow_health_report.py`
- `scripts/generate_stable_plus_promotion_report.py`

## 影响的模块层

- MITM
- README/docs
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
- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。
- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
