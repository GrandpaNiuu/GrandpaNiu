# 变更影响报告

- 生成时间：2026-06-14 07:39:23 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/adguard/GrandpaNiu-DNS.txt`
- `Android/adguard/apps/iOS-App-Compatible-Reject.txt`
- `Android/branches.json`
- `Android/mihomo/GrandpaNiu-Ads.yaml`
- `Android/mihomo/apps/iOS-App-Compatible-Reject.yaml`
- `Android/sing-box/GrandpaNiu-Ads.json`
- `Android/sing-box/apps/iOS-App-Compatible-Reject.json`
- `Android/v2rayng/GrandpaNiu-v2rayng-routing.json`
- `Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json`
- `Release/Android/adguard/GrandpaNiu-DNS.txt`
- `Release/Android/adguard/apps/iOS-App-Compatible-Reject.txt`
- `Release/Android/branches.json`
- `Release/Android/mihomo/GrandpaNiu-Ads.yaml`
- `Release/Android/mihomo/apps/iOS-App-Compatible-Reject.yaml`
- `Release/Android/sing-box/GrandpaNiu-Ads.json`
- `Release/Android/sing-box/apps/iOS-App-Compatible-Reject.json`
- `Release/Android/v2rayng/GrandpaNiu-v2rayng-routing.json`
- `Release/Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json`
- `Release/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Ronghemokuai.sgmodule`
- `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`
- `reports/android_rules_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/reject_risk_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `Android/adguard/GrandpaNiu-DNS.txt`
- `Android/adguard/apps/iOS-App-Compatible-Reject.txt`
- `Android/branches.json`
- `Android/mihomo/GrandpaNiu-Ads.yaml`
- `Android/mihomo/apps/iOS-App-Compatible-Reject.yaml`
- `Android/sing-box/GrandpaNiu-Ads.json`
- `Android/sing-box/apps/iOS-App-Compatible-Reject.json`
- `Android/v2rayng/GrandpaNiu-v2rayng-routing.json`
- `Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json`
- `Release/Android/adguard/GrandpaNiu-DNS.txt`
- `Release/Android/adguard/apps/iOS-App-Compatible-Reject.txt`
- `Release/Android/branches.json`
- `Release/Android/mihomo/GrandpaNiu-Ads.yaml`
- `Release/Android/mihomo/apps/iOS-App-Compatible-Reject.yaml`
- `Release/Android/sing-box/GrandpaNiu-Ads.json`
- `Release/Android/sing-box/apps/iOS-App-Compatible-Reject.json`
- `Release/Android/v2rayng/GrandpaNiu-v2rayng-routing.json`
- `Release/Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json`
- `Release/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Ronghemokuai.sgmodule`
- `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`
- `reports/android_rules_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/reject_risk_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_inventory_report.md`
- `reports/workflow_health_report.md`

## 影响的模块层

- Other
- README/docs

## 可能影响的 App

- Spotify
- YouTube
- Bilibili
- 百度贴吧
- 淘宝
- 拼多多
- 美团
- 饿了么
- 滴滴
- 12306
- 高德地图
- 喜马拉雅
- Reddit

## 风险判断

- 是否涉及脚本：否
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：是
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：按需
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
