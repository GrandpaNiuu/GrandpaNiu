# 变更影响报告

- 生成时间：2026-06-13 00:54:27 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Release/Modules/README.md`
- `Release/Modules/ithome.sgmodule`
- `Release/Modules/qqmusic.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/qingrex_miniapp_import_report.md`
- `reports/release_modules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`

## 新增文件

- `Release/Modules/ithome.sgmodule`
- `Release/Modules/qqmusic.sgmodule`

## 删除文件

- 无

## 修改文件

- `Release/Modules/README.md`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Web/catalog.md`
- `Web/modules.html`
- `Web/release-links.json`
- `reports/android_rules_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/qingrex_miniapp_import_report.md`
- `reports/release_modules_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`

## 影响的模块层

- Other
- README/docs

## 可能影响的 App

- Spotify
- Bilibili
- 百度贴吧
- 京东
- 拼多多
- 美团
- 高德地图
- 网易云音乐

## 风险判断

- 是否涉及脚本：否
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：否
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：按需
- 是否需要测试知乎：按需
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
