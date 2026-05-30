# App 覆盖矩阵

- 日期：2026-05-31
- 说明：本报告由静态关键词扫描生成，覆盖强度用于维护参考，不代表完整功能承诺。
- 测试状态来自 `reports/manual_test_log.md`；没有真实记录时默认未测。

| App / 服务 | 覆盖方式 | 覆盖强度 | 风险等级 | 来源文件 | 测试状态 | 最近测试日期 | 需要测试项目 | 备注 |
|---|---|---|---|---|---|---|---|---|
| Spotify | Header Rewrite, MITM, Remote Rule, Rule, Script | 重点专项 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/Header-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rules/spotify-direct.list<br>Scripts/spotify.conf | 未测 | 未测试 | 连续播放、切歌、搜索、歌单加载 | 高风险项需手动复测 |
| YouTube | MITM, Map Local, Remote Rule, Rule, Script | 重点专项 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rules/youtube-direct.list<br>Scripts/youtube.conf | 未测 | 未测试 | 首页、搜索、播放、Shorts、评论区 | 高风险项需手动复测 |
| 知乎 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 重点专项 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf<br>Scripts/zhihu-enhance.conf | 未测 | 未测试 | 首页、回答页、搜索、评论、点赞、收藏 | 高风险项需手动复测 |
| Bilibili | Body Rewrite, MITM, Map Local, Rule, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Rules/web-ads.list | 未测 | 未测试 | 首页、搜索、播放页、评论区 | 高风险项需手动复测 |
| 微博 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |
| 百度贴吧 | MITM, Script | 明确覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |
| 小红书 | MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/app-clean.list<br>Rules/reject.list<br>Rules/web-ads.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |
| 酷安 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |
| 淘宝 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/app-clean.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、商品详情、购物车、订单页 | 高风险项需手动复测 |
| 闲鱼 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、商品详情、聊天入口 | 高风险项需手动复测 |
| 京东 | MITM, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf | 未测 | 未测试 | 首页、搜索、商品详情、购物车、订单页 | 高风险项需手动复测 |
| 拼多多 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、商品详情、订单页 | 高风险项需手动复测 |
| 美团 | Body Rewrite, MITM, Map Local, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Rules/web-ads.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、店铺页、下单前置页面 | 高风险项需手动复测 |
| 大众点评 | MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、店铺页、评价页 | 高风险项需手动复测 |
| 饿了么 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、店铺页、下单前置页面 | 高风险项需手动复测 |
| 滴滴 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、定位、路线、订单查询 | 高风险项需手动复测 |
| 12306 | Script | 明确覆盖 | 中 | Scripts/app-clean.conf | 未测 | 未测试 | 首页、车票查询、订单查询 | 按需复测 |
| 高德地图 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、路线规划 | 高风险项需手动复测 |
| 百度地图 | MITM, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Rules/web-ads.list | 未测 | 未测试 | 首页、搜索、路线规划 | 高风险项需手动复测 |
| 网易云音乐 | MITM, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |
| 喜马拉雅 | Body Rewrite, MITM, Map Local, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/app-clean.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |
| 小宇宙 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |
| 斗鱼 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |
| Reddit | Body Rewrite, MITM, Script | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Scripts/app-clean.conf | 未测 | 未测试 | 首页、搜索、详情页、核心流程 | 高风险项需手动复测 |

## 风险等级规则

- 低：只涉及 Rule / Remote Rule，不涉及 MITM、Script 或 Body Rewrite。
- 中：涉及 URL Rewrite / Map Local / Script，但不直接命中敏感风险域。
- 高：涉及 MITM、Body Rewrite、大型 JSON、视频播放链路、账号相关接口，或属于 Spotify / YouTube / 知乎等核心链路。

## 后续改进

- 新增 App 规则或脚本后，应补充关键词映射。
- 高风险项需要在 Shadowrocket 中手动验证登录、支付、验证码和核心播放链路。
