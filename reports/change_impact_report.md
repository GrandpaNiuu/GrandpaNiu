# 变更影响报告

- 生成时间：2026-06-19 00:24:11 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/branches.json`
- `Release/Android/branches.json`
- `Release/Module.sgmodule`
- `Release/Modules/README.md`
- `Release/Modules/bilibili.sgmodule`
- `Release/Modules/ithome.sgmodule`
- `Release/Modules/netease-music.sgmodule`
- `Release/Modules/tieba.sgmodule`
- `Release/Modules/youtube.sgmodule`
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
- `Rewrite/Sources/Apps/youtube.conf`
- `Rewrite/Sources/Meta.conf`
- `Ronghemokuai.sgmodule`
- `Scripts/youtube.conf`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
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
- `scripts/build_release_modules.py`
- `scripts/sync_upstream_app_modules.py`
- `scripts/validate_repository.py`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `Android/branches.json`
- `Release/Android/branches.json`
- `Release/Module.sgmodule`
- `Release/Modules/README.md`
- `Release/Modules/bilibili.sgmodule`
- `Release/Modules/ithome.sgmodule`
- `Release/Modules/netease-music.sgmodule`
- `Release/Modules/tieba.sgmodule`
- `Release/Modules/youtube.sgmodule`
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
- `Rewrite/Sources/Apps/youtube.conf`
- `Rewrite/Sources/Meta.conf`
- `Ronghemokuai.sgmodule`
- `Scripts/youtube.conf`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/app_status_matrix.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
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
- `scripts/build_release_modules.py`
- `scripts/sync_upstream_app_modules.py`
- `scripts/validate_repository.py`

## 影响的模块层

- Other
- README/docs
- Rewrite/Sources
- Scripts
- Scripts/maintenance

## 可能影响的 App

- Spotify
- YouTube
- 知乎
- Bilibili
- 微博
- 百度贴吧
- 京东
- 拼多多
- 12306
- 高德地图
- 网易云音乐
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
