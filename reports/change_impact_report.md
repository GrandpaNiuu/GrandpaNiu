# 变更影响报告

- 生成时间：2026-06-20 01:40:10 +0800
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
- `Release/Module.sgmodule`
- `Release/Modules/README.md`
- `Release/Modules/bilibili.sgmodule`
- `Release/Modules/dragon-read.sgmodule`
- `Release/Modules/i-qi-yi-video.sgmodule`
- `Release/Modules/netease-music.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Rules.conf`
- `Release/RulesGroup.conf`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/Stable/Rules.conf`
- `Release/Stable/RulesGroup.conf`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Sources/Apps/bilibili.conf`
- `Rewrite/Sources/Apps/dragon-read.conf`
- `Rewrite/Sources/Apps/i-qi-yi-video.conf`
- `Rewrite/Sources/Apps/netease-music.conf`
- `Rewrite/Sources/Meta.conf`
- `Rewrite/Sources/Misc/android-compatible-ads.conf`
- `Rewrite/Sources/Misc/httpdns.conf`
- `Rewrite/Sources/Rule.conf`
- `Rewrite/Sources/URL-Rewrite.conf`
- `Ronghemokuai.sgmodule`
- `Rules/aggressive-ads.list`
- `Rules/app-clean.list`
- `Rules/converted/zirawell-allAdBlock-shadowrocket.list`
- `Rules/converted/zirawell-appAdBlock-shadowrocket.list`
- `Rules/direct.list`
- `Rules/protect-login.list`
- `Rules/protect-video.list`
- `Rules/qingrex-miniapp-app-ad.list`
- `Rules/reject.list`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`
- `reports/android_rules_report.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/daily_update_report.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_modules_report.md`
- `reports/release_rules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `scripts/build_module.py`
- `scripts/convert_quanx_rules.py`
- `scripts/sync_upstream_app_modules.py`
- `scripts/validate_repository.py`

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
- `Release/Module.sgmodule`
- `Release/Modules/README.md`
- `Release/Modules/bilibili.sgmodule`
- `Release/Modules/dragon-read.sgmodule`
- `Release/Modules/i-qi-yi-video.sgmodule`
- `Release/Modules/netease-music.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Rules.conf`
- `Release/RulesGroup.conf`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/Stable/Rules.conf`
- `Release/Stable/RulesGroup.conf`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Sources/Apps/bilibili.conf`
- `Rewrite/Sources/Apps/dragon-read.conf`
- `Rewrite/Sources/Apps/i-qi-yi-video.conf`
- `Rewrite/Sources/Apps/netease-music.conf`
- `Rewrite/Sources/Meta.conf`
- `Rewrite/Sources/Misc/android-compatible-ads.conf`
- `Rewrite/Sources/Misc/httpdns.conf`
- `Rewrite/Sources/Rule.conf`
- `Rewrite/Sources/URL-Rewrite.conf`
- `Ronghemokuai.sgmodule`
- `Rules/aggressive-ads.list`
- `Rules/app-clean.list`
- `Rules/converted/zirawell-allAdBlock-shadowrocket.list`
- `Rules/converted/zirawell-appAdBlock-shadowrocket.list`
- `Rules/direct.list`
- `Rules/protect-login.list`
- `Rules/protect-video.list`
- `Rules/qingrex-miniapp-app-ad.list`
- `Rules/reject.list`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json`
- `reports/android_rules_report.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/daily_update_report.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_modules_report.md`
- `reports/release_rules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `scripts/build_module.py`
- `scripts/convert_quanx_rules.py`
- `scripts/sync_upstream_app_modules.py`
- `scripts/validate_repository.py`

## 影响的模块层

- Other
- README/docs
- Rewrite/Sources
- Rules
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
