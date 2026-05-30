# 变更影响报告

- 生成时间：2026-05-30 09:10:47 +0800
- 说明：无 git 工作树时，本报告基于最近修改文件时间生成；如需精确变更，请结合提交 diff 人工确认。

## 本次修改文件

- `CONTRIBUTING.md`
- `README.md`
- `Rewrite/Remotes/candidates.json`
- `.github/workflows/repository-health.yml`
- `CHANGELOG.md`
- `docs/RELEASE.md`
- `docs/PERFORMANCE.md`
- `docs/MAINTENANCE.md`
- `docs/FACTORY_FLOW.md`
- `docs/VERSIONING.md`
- `docs/MITM_POLICY.md`
- `docs/SCRIPT_REVIEW.md`
- `SECURITY.md`
- `Rewrite/Profiles/full.conf`
- `Rewrite/Profiles/lite.conf`
- `Rewrite/Profiles/stable.conf`
- `.github/workflows/daily-module-update.yml`
- `docs/TROUBLESHOOTING.md`
- `docs/SCOPE.md`
- `docs/QUALITY_GATE.md`
- `docs/COVERAGE.md`
- `scripts/zhihu-enhance.js`
- `scripts/zhihu-enhance.conf`
- `scripts/youtube.conf`
- `scripts/spotify.conf`
- `scripts/app-clean.conf`
- `Rules/youtube-direct.list`
- `Rules/web-ads.list`
- `Rules/spotify-direct.list`
- `Rules/reject.list`

## 影响的模块层

- Other
- Profiles
- README/docs
- Remotes
- Rules
- Workflows

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

- 是否涉及脚本：否
- 是否涉及 MITM：否
- 是否涉及 Body Rewrite：否
- 是否涉及远程规则源：是
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：按需

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。
- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
