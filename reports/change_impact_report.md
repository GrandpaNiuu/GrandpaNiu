# 变更影响报告

- 生成时间：2026-06-20 08:11:53 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/branches.json`
- `Release/Android/branches.json`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Generate.conf`
- `Rewrite/Generator/Generate.conf`
- `Rewrite/Registry.md`
- `Scripts/README.md`
- `Scripts/generated/fusion-script-bundle.js`
- `Scripts/generated/fusion-script-bundle.manifest.json`
- `Web/registry.md`
- `reports/android_rules_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
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
- `reports/script_aggregation_report.md`
- `reports/script_aggregation_validation_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`
- `scripts/build_module.py`
- `scripts/build_release_variants.py`
- `scripts/quality_gate.py`
- `tools/validate_script_aggregation.py`

## 新增文件

- `Scripts/generated/fusion-script-bundle.manifest.json`
- `reports/script_aggregation_validation_report.md`
- `tools/validate_script_aggregation.py`

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
- `Scripts/README.md`
- `Scripts/generated/fusion-script-bundle.js`
- `Web/registry.md`
- `reports/android_rules_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
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
- `reports/script_aggregation_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`
- `scripts/build_module.py`
- `scripts/build_release_variants.py`
- `scripts/quality_gate.py`

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
- 京东
- 美团
- 滴滴
- 12306
- 高德地图
- 网易云音乐
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
