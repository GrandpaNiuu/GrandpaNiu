# 变更影响报告

- 生成时间：2026-05-31 13:10:57 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `Release/Ronghemokuai-full.sgmodule`
- `Release/Ronghemokuai-lite.sgmodule`
- `Release/Ronghemokuai-stable-plus.sgmodule`
- `Release/Ronghemokuai-stable.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Ronghemokuai.sgmodule`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/multi_release_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `Release/Ronghemokuai-full.sgmodule`
- `Release/Ronghemokuai-lite.sgmodule`
- `Release/Ronghemokuai-stable-plus.sgmodule`
- `Release/Ronghemokuai-stable.sgmodule`
- `Release/Ronghemokuai.sgmodule`
- `Ronghemokuai.sgmodule`
- `reports/module_factory_diff_report.md`
- `reports/module_factory_report.md`
- `reports/multi_release_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`

## 影响的模块层

- Other
- README/docs

## 可能影响的 App

- 待人工确认

## 风险判断

- 是否涉及脚本：否
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：否
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：按需
- 是否需要测试 YouTube：按需
- 是否需要测试知乎：按需
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。
- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
