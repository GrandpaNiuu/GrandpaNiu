# 变更影响报告

- 生成时间：2026-06-13 22:38:38 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Android/branches.json`
- `Release/Android/README.md`
- `Release/Android/branches.json`
- `Release/checksums.json`
- `android.html`
- `reports/android_rules_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_android_report.md`
- `reports/remote_rule_syntax_report.md`
- `scripts/android_format_check.py`
- `scripts/build_android_rules.py`
- `scripts/build_release_android.py`

## 新增文件

- `Android/branches.json`
- `Release/Android/branches.json`

## 删除文件

- 无

## 修改文件

- `Release/Android/README.md`
- `Release/checksums.json`
- `android.html`
- `reports/android_rules_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/release_android_report.md`
- `reports/remote_rule_syntax_report.md`
- `scripts/android_format_check.py`
- `scripts/build_android_rules.py`
- `scripts/build_release_android.py`

## 影响的模块层

- Other
- README/docs
- Scripts/maintenance

## 可能影响的 App

- 待人工确认

## 风险判断

- 是否涉及脚本：是
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：是
- 是否需要测试 Spotify：按需
- 是否需要测试 YouTube：按需
- 是否需要测试知乎：按需
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
