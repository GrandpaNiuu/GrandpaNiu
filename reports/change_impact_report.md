# 变更影响报告

- 生成时间：2026-06-13 03:03:21 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Release/Module.sgmodule`
- `Release/Modules/README.md`
- `Release/Modules/youtube.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Remotes/app-modules.json`
- `Rewrite/Sources/Apps/youtube.conf`
- `Rewrite/Sources/MITM-core.conf`
- `Rewrite/Sources/MITM.conf`
- `Ronghemokuai.sgmodule`
- `Scripts/youtube.conf`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_modules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/upstream_app_module_sync_report.md`
- `scripts/sync_upstream_app_modules.py`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `Release/Module.sgmodule`
- `Release/Modules/README.md`
- `Release/Modules/youtube.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Remotes/app-modules.json`
- `Rewrite/Sources/Apps/youtube.conf`
- `Rewrite/Sources/MITM-core.conf`
- `Rewrite/Sources/MITM.conf`
- `Ronghemokuai.sgmodule`
- `Scripts/youtube.conf`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_modules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/upstream_app_module_sync_report.md`
- `scripts/sync_upstream_app_modules.py`

## 影响的模块层

- MITM
- Other
- README/docs
- Remotes
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
