# 变更影响报告

- 生成时间：2026-06-01 05:13:48 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `reports/app_status_matrix.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/mitm_split_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/promotion_pr_report.md`
- `reports/reject_risk_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`
- `reports/script_inventory_report.md`
- `reports/stable_plus_promotion_report.md`
- `reports/workflow_health_report.md`

## 新增文件

- 无

## 删除文件

- 无

## 修改文件

- `reports/app_status_matrix.md`
- `reports/candidate_security_score_report.md`
- `reports/change_impact_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/mitm_split_report.md`
- `reports/multi_release_report.md`
- `reports/profile_validation_report.md`
- `reports/promotion_pr_report.md`
- `reports/reject_risk_report.md`
- `reports/report_freshness_report.md`
- `reports/repository_health_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`
- `reports/script_inventory_report.md`
- `reports/stable_plus_promotion_report.md`
- `reports/workflow_health_report.md`

## 影响的模块层

- README/docs

## 可能影响的 App

- Spotify
- YouTube
- Bilibili
- 12306
- Reddit

## 风险判断

- 是否涉及脚本：否
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：按需
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。
- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
