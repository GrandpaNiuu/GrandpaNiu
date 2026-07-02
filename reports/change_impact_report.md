# 变更影响报告

- 生成时间：2026-07-02 10:08:38 +0800
- 变更识别模式：git diff 精准模式

## 本次修改文件

- `PROJECT_STATE.md`
- `Release/Legacy/README.md`
- `Release/README.md`
- `Release/Ronghemokuai-full.sgmodule`
- `Release/Ronghemokuai-lite.sgmodule`
- `Release/Ronghemokuai-stable-plus.sgmodule`
- `Release/Ronghemokuai-stable.sgmodule`
- `Rewrite/Profiles/README.md`
- `Rewrite/Profiles/full.conf`
- `Rewrite/Profiles/lite.conf`
- `Rewrite/Profiles/stable-plus.conf`
- `Rewrite/Profiles/stable.conf`
- `docs/BUILD_FLOW.md`
- `docs/FOUR_PROFILE_GOVERNANCE.md`
- `docs/LOCAL_ENV_SETUP.md`
- `docs/PERFORMANCE.md`
- `docs/PROFILE_POLICY.md`
- `docs/RELEASE.md`
- `docs/VERSIONING.md`
- `reports/app2smile_qqnews_stable_plus_report.md`
- `reports/manual_test_log.md`
- `reports/mitm_split_report.md`
- `reports/promotion_pr_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`
- `reports/stable_plus_manual_test_plan.md`
- `reports/stable_plus_promotion_report.md`
- `reports/wechat_ad_test_report.md`
- `scripts/create_promotion_pr.py`
- `scripts/dedupe_qq_news_script_path.py`
- `scripts/generate_stable_plus_promotion_report.py`
- `scripts/split_mitm_sources.py`

## 新增文件

- 无

## 删除文件

- `Release/Legacy/README.md`
- `Release/Ronghemokuai-full.sgmodule`
- `Release/Ronghemokuai-lite.sgmodule`
- `Release/Ronghemokuai-stable-plus.sgmodule`
- `Release/Ronghemokuai-stable.sgmodule`
- `Rewrite/Profiles/full.conf`
- `Rewrite/Profiles/lite.conf`
- `Rewrite/Profiles/stable-plus.conf`
- `Rewrite/Profiles/stable.conf`
- `reports/app2smile_qqnews_stable_plus_report.md`
- `reports/manual_test_log.md`
- `reports/mitm_split_report.md`
- `reports/promotion_pr_report.md`
- `reports/script_consolidation_rollback_report.md`
- `reports/script_dedupe_report.md`
- `reports/stable_plus_manual_test_plan.md`
- `reports/stable_plus_promotion_report.md`
- `scripts/create_promotion_pr.py`
- `scripts/generate_stable_plus_promotion_report.py`
- `scripts/split_mitm_sources.py`

## 修改文件

- `PROJECT_STATE.md`
- `Release/README.md`
- `Rewrite/Profiles/README.md`
- `docs/BUILD_FLOW.md`
- `docs/FOUR_PROFILE_GOVERNANCE.md`
- `docs/LOCAL_ENV_SETUP.md`
- `docs/PERFORMANCE.md`
- `docs/PROFILE_POLICY.md`
- `docs/RELEASE.md`
- `docs/VERSIONING.md`
- `reports/wechat_ad_test_report.md`
- `scripts/dedupe_qq_news_script_path.py`

## 影响的模块层

- Other
- Profiles
- README/docs
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
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，优先回滚最近一次 Fusion 输出提交。
- 回滚后运行 `build_module.py --build --profile fusion`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
