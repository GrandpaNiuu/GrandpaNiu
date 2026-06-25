# 变更影响报告

- 生成时间：2026-06-26 02:36:09 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Release/Android/branches.json`
- `Release/checksums.json`
- `Scripts/generated/fusion-script-bundle.js`
- `Scripts/generated/fusion-script-bundle.manifest.json`
- `reports/android_rules_report.md`
- `reports/app_cleaner_active_report.md`
- `reports/app_source_validation_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/mitm_scope_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/rule_overlap_report.md`
- `reports/script_aggregation_report.md`
- `reports/script_aggregation_validation_report.md`
- `reports/script_bundle_sandbox_report.md`
- `reports/upstream_app_module_sync_report.md`
- `reports/upstream_risk_gate_report.md`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `Release/Android/branches.json`
- `Release/checksums.json`
- `Scripts/generated/fusion-script-bundle.js`
- `Scripts/generated/fusion-script-bundle.manifest.json`
- `reports/android_rules_report.md`
- `reports/app_cleaner_active_report.md`
- `reports/app_source_validation_report.md`
- `reports/build_summary.json`
- `reports/build_summary.md`
- `reports/mitm_scope_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/remote_rule_syntax_report.md`
- `reports/rule_overlap_report.md`
- `reports/script_aggregation_report.md`
- `reports/script_aggregation_validation_report.md`
- `reports/script_bundle_sandbox_report.md`
- `reports/upstream_app_module_sync_report.md`
- `reports/upstream_risk_gate_report.md`

## 影响的模块层

- Other
- README/docs
- Scripts

## 可能影响的 App

- 待人工确认

## 风险判断

- 是否涉及脚本：是
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：否
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：是

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
