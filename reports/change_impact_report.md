# 变更影响报告

- 生成时间：2026-06-14 03:02:46 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Release/Android/branches.json`
- `Release/Modules/README.md`
- `Release/Modules/soul.sgmodule`
- `Release/Modules/zhihu.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Remotes/app-modules.json`
- `Rewrite/Sources/Apps/caiyun-weather.conf`
- `Rewrite/Sources/Apps/hupu.conf`
- `Rewrite/Sources/Apps/ithome.conf`
- `Rewrite/Sources/Apps/soul.conf`
- `Rewrite/Sources/Apps/zhihu.conf`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `backup/upstream-app-modules/zhihu/20260613-175043.conf`
- `reports/android_rules_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_modules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/upstream_app_module_sync_report.md`

## 新增文件

- `backup/upstream-app-modules/zhihu/20260613-175043.conf`

## 删除文件

- 无

## 修改文件

- `Release/Android/branches.json`
- `Release/Modules/README.md`
- `Release/Modules/soul.sgmodule`
- `Release/Modules/zhihu.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Remotes/app-modules.json`
- `Rewrite/Sources/Apps/caiyun-weather.conf`
- `Rewrite/Sources/Apps/hupu.conf`
- `Rewrite/Sources/Apps/ithome.conf`
- `Rewrite/Sources/Apps/soul.conf`
- `Rewrite/Sources/Apps/zhihu.conf`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_modules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/upstream_app_module_sync_report.md`

## 影响的模块层

- Other
- README/docs
- Remotes
- Rewrite/Sources

## 可能影响的 App

- Spotify
- YouTube
- 知乎
- 淘宝
- 京东

## 风险判断

- 是否涉及脚本：否
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
