# 变更影响报告

- 生成时间：2026-06-12 03:06:34 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `.github/workflows/daily-module-update.yml`
- `.github/workflows/module-factory-build.yml`
- `.github/workflows/repository-health.yml`
- `Release/Modules/README.md`
- `Release/Modules/amap.sgmodule`
- `Release/Modules/baidu.sgmodule`
- `Release/Modules/meituan.sgmodule`
- `Release/Modules/quark.sgmodule`
- `Release/Modules/soul.sgmodule`
- `Release/Modules/wps.sgmodule`
- `Release/Modules/youku.sgmodule`
- `Release/Modules/zdm.sgmodule`
- `Release/Modules/zuoyebang.sgmodule`
- `Release/README.md`
- `Release/Ronghemokuai.sgmodule`
- `Release/Rules.conf`
- `Release/RulesGroup.conf`
- `Rewrite/Generate.conf`
- `Rewrite/Registry.md`
- `Rewrite/Sources/Apps/README.md`
- `Rewrite/Sources/Apps/amap.conf`
- `Rewrite/Sources/Apps/baidu.conf`
- `Rewrite/Sources/Apps/meituan.conf`
- `Rewrite/Sources/Apps/soul.conf`
- `Rewrite/Sources/Apps/wps.conf`
- `Rewrite/Sources/Apps/zdm.conf`
- `Rewrite/Sources/Apps/zuoyebang.conf`
- `Rewrite/Sources/Misc/README.md`
- `Rewrite/Sources/Misc/analytics.conf`
- `Rewrite/Sources/Misc/cdn-direct.conf`
- `Rewrite/Sources/Misc/finance-protect.conf`
- `Rewrite/Sources/Misc/generic-ads.conf`
- `Rewrite/Sources/Misc/httpdns.conf`
- `Rewrite/Sources/Misc/video-protect.conf`
- `Ronghemokuai.sgmodule`
- `Web/catalog.md`
- `Web/index.html`
- `Web/registry.md`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_modules_report.md`
- `reports/release_rules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/repository_health_report.md`
- `scripts/build_module.py`
- `scripts/build_release_modules.py`
- `scripts/repository_health_check.py`

## 新增文件

- `Release/Modules/amap.sgmodule`
- `Release/Modules/baidu.sgmodule`
- `Release/Modules/meituan.sgmodule`
- `Release/Modules/quark.sgmodule`
- `Release/Modules/soul.sgmodule`
- `Release/Modules/wps.sgmodule`
- `Release/Modules/youku.sgmodule`
- `Release/Modules/zdm.sgmodule`
- `Release/Modules/zuoyebang.sgmodule`
- `Rewrite/Sources/Apps/amap.conf`
- `Rewrite/Sources/Apps/baidu.conf`
- `Rewrite/Sources/Apps/meituan.conf`
- `Rewrite/Sources/Apps/soul.conf`
- `Rewrite/Sources/Apps/wps.conf`
- `Rewrite/Sources/Apps/zdm.conf`
- `Rewrite/Sources/Apps/zuoyebang.conf`
- `Rewrite/Sources/Misc/analytics.conf`
- `Rewrite/Sources/Misc/cdn-direct.conf`
- `Rewrite/Sources/Misc/finance-protect.conf`
- `Rewrite/Sources/Misc/generic-ads.conf`
- `Rewrite/Sources/Misc/httpdns.conf`
- `Rewrite/Sources/Misc/video-protect.conf`

## 删除文件

- 无

## 修改文件

- `.github/workflows/daily-module-update.yml`
- `.github/workflows/module-factory-build.yml`
- `.github/workflows/repository-health.yml`
- `Release/Modules/README.md`
- `Release/README.md`
- `Release/Ronghemokuai.sgmodule`
- `Release/Rules.conf`
- `Release/RulesGroup.conf`
- `Rewrite/Generate.conf`
- `Rewrite/Registry.md`
- `Rewrite/Sources/Apps/README.md`
- `Rewrite/Sources/Misc/README.md`
- `Ronghemokuai.sgmodule`
- `Web/catalog.md`
- `Web/index.html`
- `Web/registry.md`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_modules_report.md`
- `reports/release_rules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/repository_health_report.md`
- `scripts/build_module.py`
- `scripts/build_release_modules.py`
- `scripts/repository_health_check.py`

## 影响的模块层

- Other
- README/docs
- Rewrite/Sources
- Scripts/maintenance
- Workflows

## 可能影响的 App

- Spotify
- YouTube
- 知乎
- Bilibili
- 微博
- 淘宝
- 京东
- 拼多多
- 美团
- 大众点评
- 高德地图
- 网易云音乐

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
