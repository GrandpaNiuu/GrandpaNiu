# App 覆盖矩阵

- 日期：2026-06-27
- 说明：本报告由静态关键词扫描生成，覆盖强度用于维护参考，不代表完整功能承诺。
- 质量来源：发布门禁只依赖 `reports/automated_quality_evidence.md` 和可重复运行的自动化校验。

| App / 服务 | 覆盖方式 | 覆盖强度 | 风险等级 | 来源文件 | 自动证据状态 | 观察项目 | 备注 |
|---|---|---|---|---|---|---|---|
| Spotify | Header Rewrite, MITM, Remote Rule, Rule, Script | 重点覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/Header-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rules/qingrex-miniapp-app-ad.list<br>Rules/spotify-direct.list<br>Scripts/spotify.conf | 自动扫描已覆盖 | 播放、切歌、搜索、歌单加载由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| YouTube | MITM, Remote Rule, Rule, Script | 重点覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/MITM.conf<br>Rules/protect-video.list<br>Rules/youtube-direct.list<br>Scripts/youtube.conf | 自动扫描已覆盖 | 首页、搜索、播放、Shorts、评论区由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 知乎 | Body Rewrite, MITM, Remote Rule, Rule, Script, URL Rewrite | 重点覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/zhihu-enhance.conf | 自动扫描已覆盖 | 首页、回答页、搜索、评论、点赞、收藏由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| Bilibili | MITM, Remote Rule, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/direct.list<br>Rules/web-ads.list | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 微博 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 百度贴吧 | MITM, Remote Rule, Script | 明确覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/MITM.conf<br>Scripts/app-clean.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 小红书 | MITM, Remote Rule, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/app-clean.list<br>Rules/reject.list<br>Rules/web-ads.list<br>Scripts/app-clean.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 酷安 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 淘宝 | Body Rewrite, MITM, Remote Rule, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/aggressive-ads.list<br>Rules/app-clean.list<br>Rules/direct.list<br>Rules/protect-login.list<br>Scripts/app-clean.conf<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、商品详情、购物车、订单页由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 闲鱼 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 京东 | MITM, Remote Rule, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/protect-login.list | 自动扫描已覆盖 | 首页、搜索、商品详情、购物车、订单页由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 拼多多 | Body Rewrite, MITM, Remote Rule, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、商品详情、订单页由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 美团 | Body Rewrite, MITM, Map Local, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/direct.list<br>Rules/qingrex-miniapp-app-ad.list<br>Rules/reject.list<br>Rules/web-ads.list<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 大众点评 | MITM, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 饿了么 | Body Rewrite, MITM, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 滴滴 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 12306 | Rule | 局部覆盖 | 低 | Rules/aggressive-ads.list | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 按自动门禁维护 |
| 高德地图 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/direct.list<br>Rules/reject.list<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 百度地图 | MITM, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/protect-login.list<br>Rules/qingrex-miniapp-app-ad.list<br>Rules/reject.list<br>Rules/web-ads.list | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 网易云音乐 | MITM, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/direct.list<br>Rules/reject.list | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 喜马拉雅 | Body Rewrite, MITM, Map Local, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/app-clean.list<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 小宇宙 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| 斗鱼 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |
| Reddit | Body Rewrite, MITM, Rule, Script | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rules/protect-login.list<br>Scripts/app-cleaner-active.conf | 自动扫描已覆盖 | 首页、搜索、详情页、核心流程由用户反馈或 Issue 观察，不作为自动门禁。 | 高风险项必须保留保护规则和回滚路径 |

## 风险等级规则

- 低：只涉及 Rule / Remote Rule，不涉及 MITM、Script 或 Body Rewrite。
- 中：涉及 URL Rewrite / Map Local / Script，但不直接命中敏感风险域。
- 高：涉及 MITM、Body Rewrite、大型 JSON、视频播放链路、账号相关接口，或属于 Spotify / YouTube / 知乎等核心链路。

## 处理原则

- 覆盖存在不等于效果承诺。
- 用户反馈进入 Issue 或变更记录，但不作为发布阻断门禁。
- 发布前以自动化质量证据和可回滚源头为准。
