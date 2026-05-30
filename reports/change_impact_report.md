# 变更影响报告

- 生成时间：2026-05-31 02:29:25 +0800
- 说明：无 git 工作树时，本报告基于最近修改文件时间生成；如需精确变更，请结合提交 diff 人工确认。

## 本次修改文件

- `docs/QUALITY_GATE.md`
- `docs/PERFORMANCE.md`
- `docs/TROUBLESHOOTING.md`
- `docs/SCRIPT_REVIEW.md`
- `docs/VERSIONING.md`
- `docs/RELEASE.md`
- `docs/SCOPE.md`
- `docs/TESTING.md`
- `docs/FACTORY_FLOW.md`
- `docs/MITM_POLICY.md`
- `docs/MAINTENANCE.md`
- `docs/COVERAGE.md`
- `Scripts/zhihu-enhance.js`
- `Scripts/youtube.conf`
- `Scripts/spotify.conf`
- `Scripts/app-clean.conf`
- `Scripts/zhihu-enhance.conf`
- `SECURITY.md`
- `Rules/youtube-direct.list`
- `Rules/spotify-direct.list`
- `Rules/web-ads.list`
- `Rules/direct.list`
- `Rules/app-clean.list`
- `Rules/reject.list`
- `Rewrite/Sources/URL-Rewrite.conf`
- `Rewrite/Sources/MITM.conf`
- `Rewrite/Sources/Map-Local.conf`
- `Rewrite/Sources/Rule.conf`
- `Rewrite/Sources/Header-Rewrite.conf`
- `Rewrite/Sources/Body-Rewrite.conf`

## 影响的模块层

- MITM
- README/docs
- Rewrite/Sources
- Rules
- Scripts

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

- 是否涉及脚本：是
- 是否涉及 MITM：是
- 是否涉及 Body Rewrite：是
- 是否涉及远程规则源：否
- 是否需要测试 Spotify：是
- 是否需要测试 YouTube：是
- 是否需要测试知乎：是
- 是否需要测试登录/支付/验证码：是

## 回滚建议

- 优先回滚最近一次提交。
- 若主模块导入异常，可用 `backup/Ronghemokuai.stable.sgmodule` 人工恢复。
- 回滚后运行 `build_module.py --build --profile stable`、`factory_finalize.py --sync-root`、`validate_repository.py` 和 `repository_health_check.py`。
