# 变更影响报告

- 生成时间：2026-06-14 05:22:33 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/adguard/apps/iOS-App-Compatible-Reject.txt`
- `Android/branches.json`
- `Android/mihomo/apps/iOS-App-Compatible-Reject.yaml`
- `Android/sing-box/apps/iOS-App-Compatible-Reject.json`
- `Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json`
- `Release/Android/adguard/apps/iOS-App-Compatible-Reject.txt`
- `Release/Android/branches.json`
- `Release/Android/mihomo/apps/iOS-App-Compatible-Reject.yaml`
- `Release/Android/sing-box/apps/iOS-App-Compatible-Reject.json`
- `Release/Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json`
- `Release/Modules/README.md`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/qingrex_miniapp_import_report.md`
- `reports/reject_risk_report.md`
- `reports/release_modules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `Android/adguard/apps/iOS-App-Compatible-Reject.txt`
- `Android/branches.json`
- `Android/mihomo/apps/iOS-App-Compatible-Reject.yaml`
- `Android/sing-box/apps/iOS-App-Compatible-Reject.json`
- `Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json`
- `Release/Android/adguard/apps/iOS-App-Compatible-Reject.txt`
- `Release/Android/branches.json`
- `Release/Android/mihomo/apps/iOS-App-Compatible-Reject.yaml`
- `Release/Android/sing-box/apps/iOS-App-Compatible-Reject.json`
- `Release/Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json`
- `Release/Modules/README.md`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/qingrex_miniapp_import_report.md`
- `reports/reject_risk_report.md`
- `reports/release_modules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`

## 影响的模块层

- Other
- README/docs

## 可能影响的 App

- Spotify
- YouTube
- 知乎
- Bilibili
- 美团
- 滴滴
- 12306
- 高德地图
- Reddit

## 风险判断

- 是否涉及脚本：否
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
