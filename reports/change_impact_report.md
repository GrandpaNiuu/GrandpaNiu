# 变更影响报告

- 生成时间：2026-06-20 08:58:10 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/branches.json`
- `Release/Android/branches.json`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Generate.conf`
- `Rewrite/Generator/Generate.conf`
- `Rewrite/Registry.md`
- `Rewrite/Remotes/app-modules.json`
- `Scripts/README.md`
- `Scripts/generated/fusion-script-bundle.js`
- `Scripts/generated/fusion-script-bundle.manifest.json`
- `Web/registry.md`
- `reports/android_rules_report.md`
- `reports/app_cleaner_active_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/mitm_scope_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/reject_risk_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/rule_overlap_report.md`
- `reports/script_aggregation_report.md`
- `reports/script_aggregation_validation_report.md`
- `reports/script_bundle_sandbox_report.md`
- `reports/script_inventory_report.md`
- `reports/upstream_risk_gate_report.md`
- `reports/workflow_health_report.md`
- `scripts/build_module.py`
- `scripts/check_report_freshness.py`
- `scripts/quality_gate.py`
- `scripts/repository_health_check.py`
- `tools/generate_app_cleaner_active_report.py`
- `tools/generate_automated_quality_evidence.py`
- `tools/generate_mitm_scope_report.py`
- `tools/generate_rule_overlap_report.py`
- `tools/test_script_bundle_sandbox.py`
- `tools/validate_upstream_risk_gate.py`

## 新增文件

- `reports/mitm_scope_report.md`
- `reports/rule_overlap_report.md`
- `reports/script_bundle_sandbox_report.md`
- `reports/upstream_risk_gate_report.md`
- `tools/generate_app_cleaner_active_report.py`
- `tools/generate_mitm_scope_report.py`
- `tools/generate_rule_overlap_report.py`
- `tools/test_script_bundle_sandbox.py`
- `tools/validate_upstream_risk_gate.py`

## 删除文件

- 无

## 修改文件

- `Android/branches.json`
- `Release/Android/branches.json`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Generate.conf`
- `Rewrite/Generator/Generate.conf`
- `Rewrite/Registry.md`
- `Rewrite/Remotes/app-modules.json`
- `Scripts/README.md`
- `Scripts/generated/fusion-script-bundle.js`
- `Scripts/generated/fusion-script-bundle.manifest.json`
- `Web/registry.md`
- `reports/android_rules_report.md`
- `reports/app_cleaner_active_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/reject_risk_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_aggregation_report.md`
- `reports/script_aggregation_validation_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`
- `scripts/build_module.py`
- `scripts/check_report_freshness.py`
- `scripts/quality_gate.py`
- `scripts/repository_health_check.py`
- `tools/generate_automated_quality_evidence.py`

## 影响的模块层

- Other
- README/docs
- Remotes
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
- 网易云音乐
- 喜马拉雅
- 斗鱼
- Reddit

## 风险判断

- 是否涉及脚本：是
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：否
- 是否涉及远程规则源：是
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：是

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
