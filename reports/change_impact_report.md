# 变更影响报告

- 生成时间：2026-05-31 03:37:23 +0800
- 变更识别模式：fallback 最近修改时间模式

## 本次修改文件

- `reports/app_coverage_matrix.md`
- `reports/compat_migration_report.md`
- `reports/daily_audit_report.md`
- `reports/daily_update_report.md`
- `reports/factory_finalize_report.md`
- `reports/factory_refactor_report.md`
- `reports/legacy_selected_migration_report.md`
- `reports/manual_test_log.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/repository_cleanup_report.md`
- `reports/repository_health_report.md`
- `reports/upstream_collect_report.md`
- `reports/workflow_health_report.md`
- `reports/zhihu_enhance_report.md`
- `scripts/audit_and_repair_module.py`
- `scripts/audit_compat_sources.py`
- `scripts/audit_repair_invalid_sources.py`
- `scripts/build_module.py`
- `scripts/collect_upstreams.py`
- `scripts/factory_finalize.py`
- `scripts/generate_app_coverage_matrix.py`
- `scripts/generate_change_impact_report.py`
- `scripts/generate_workflow_health_report.py`
- `scripts/migrate_legacy_selected_rules.py`
- `scripts/repository_health_check.py`
- `scripts/safe_refine_module.py`
- `scripts/split_mitm_sources.py`
- `scripts/validate_profiles.py`
- `scripts/validate_repository.py`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `reports/app_coverage_matrix.md`
- `reports/compat_migration_report.md`
- `reports/factory_finalize_report.md`
- `reports/module_factory_report.md`
- `reports/module_factory_diff_report.md`
- `scripts/audit_compat_sources.py`
- `scripts/validate_repository.py`
- `scripts/split_mitm_sources.py`
- `scripts/safe_refine_module.py`
- `scripts/generate_app_coverage_matrix.py`
- `scripts/audit_repair_invalid_sources.py`
- `scripts/build_module.py`
- `scripts/generate_workflow_health_report.py`
- `scripts/migrate_legacy_selected_rules.py`
- `scripts/generate_change_impact_report.py`
- `scripts/collect_upstreams.py`
- `scripts/factory_finalize.py`
- `scripts/validate_profiles.py`
- `scripts/repository_health_check.py`
- `reports/workflow_health_report.md`
- `reports/zhihu_enhance_report.md`
- `reports/manual_test_log.md`
- `reports/daily_audit_report.md`
- `reports/factory_refactor_report.md`
- `scripts/audit_and_repair_module.py`
- `reports/repository_health_report.md`
- `reports/upstream_collect_report.md`
- `reports/repository_cleanup_report.md`
- `reports/daily_update_report.md`
- `reports/legacy_selected_migration_report.md`

## 影响的模块层

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
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。
- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
