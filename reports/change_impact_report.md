# 变更影响报告

- 生成时间：2026-06-14 23:55:15 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/branches.json`
- `Release/Android/branches.json`
- `Release/Module.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Ronghemokuai.sgmodule`
- `Scripts/qingrex-miniapp-app-ad.conf`
- `reports/android_rules_report.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/qingrex_miniapp_import_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/repository_health_report.md`
- `scripts/import_qingrex_official_module.py`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `Android/branches.json`
- `Release/Android/branches.json`
- `Release/Module.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Ronghemokuai.sgmodule`
- `Scripts/qingrex-miniapp-app-ad.conf`
- `reports/android_rules_report.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/module_integrity_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/qingrex_miniapp_import_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/repository_health_report.md`
- `scripts/import_qingrex_official_module.py`

## 影响的模块层

- Other
- README/docs
- Scripts
- Scripts/maintenance

## 可能影响的 App

- 知乎
- 百度贴吧
- 酷安
- 淘宝
- 闲鱼
- 京东
- 拼多多
- 美团
- 滴滴
- 12306
- 高德地图
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
