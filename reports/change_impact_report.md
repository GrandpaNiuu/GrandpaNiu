# 变更影响报告

- 生成时间：2026-06-14 08:30:19 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/branches.json`
- `Release/Android/branches.json`
- `Release/Module.sgmodule`
- `Release/Modules/bilibili.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Sources/Apps/bilibili.conf`
- `Rewrite/Sources/Map-Local-legacy-reviewed.conf`
- `Rewrite/Sources/Map-Local.conf`
- `Ronghemokuai.sgmodule`
- `reports/android_rules_report.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/module_factory_report.md`
- `reports/multi_release_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/repository_health_report.md`
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
- `Release/Modules/bilibili.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Release/Stable/Module.sgmodule`
- `Release/Stable/Ronghemokuai.sgmodule`
- `Release/checksums.json`
- `Release/checksums.txt`
- `Rewrite/Sources/Apps/bilibili.conf`
- `Rewrite/Sources/Map-Local-legacy-reviewed.conf`
- `Rewrite/Sources/Map-Local.conf`
- `Ronghemokuai.sgmodule`
- `reports/android_rules_report.md`
- `reports/automated_quality_evidence.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/module_factory_report.md`
- `reports/multi_release_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/repository_health_report.md`
- `scripts/sync_upstream_app_modules.py`
- `scripts/validate_repository.py`

## 影响的模块层

- Other
- README/docs
- Rewrite/Sources
- Scripts/maintenance

## 可能影响的 App

- Bilibili
- 百度贴吧
- 美团
- 12306
- 喜马拉雅

## 风险判断

- 是否涉及脚本：是
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：是
- 是否需要测试 Spotify：按需
- 是否需要测试 YouTube：按需
- 是否需要测试知乎：按需
- 是否需要测试登录/支付/验证码：是

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
