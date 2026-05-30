# App 覆盖矩阵

- 日期：2026-05-30
- 说明：本报告由静态关键词扫描生成，覆盖强度用于维护参考，不代表完整功能承诺。

| App / 服务 | 覆盖方式 | 覆盖强度 | 风险等级 | 来源文件 | 是否需要手动测试 |
|---|---|---|---|---|---|
| Spotify | Header Rewrite, MITM, Remote Rule, Rule, Script | 重点专项 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/Header-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rules/spotify-direct.list<br>Scripts/spotify.conf | 是 |
| YouTube | MITM, Map Local, Remote Rule, Rule, Script | 重点专项 | 高 | Rewrite/Remotes/sources.json<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rules/youtube-direct.list<br>Scripts/youtube.conf | 是 |
| 知乎 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 重点专项 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf<br>Scripts/zhihu-enhance.conf | 是 |
| Bilibili | Body Rewrite, MITM, Map Local, Rule, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Rules/web-ads.list | 是 |
| 微博 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 是 |
| 百度贴吧 | MITM, Script | 明确覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Scripts/app-clean.conf | 是 |
| 小红书 | MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/app-clean.list<br>Rules/reject.list<br>Rules/web-ads.list<br>Scripts/app-clean.conf | 是 |
| 酷安 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 是 |
| 淘宝 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/app-clean.list<br>Scripts/app-clean.conf | 是 |
| 闲鱼 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 是 |
| 京东 | MITM, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf | 是 |
| 拼多多 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 是 |
| 美团 | Body Rewrite, MITM, Map Local, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Rules/web-ads.list<br>Scripts/app-clean.conf | 是 |
| 大众点评 | MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 是 |
| 饿了么 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 是 |
| 滴滴 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 是 |
| 12306 | Script | 明确覆盖 | 高 | Scripts/app-clean.conf | 是 |
| 高德地图 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 是 |
| 百度地图 | MITM, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Rules/web-ads.list | 是 |
| 网易云音乐 | MITM, Rule, URL Rewrite | 局部覆盖 | 高 | Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list | 是 |
| 喜马拉雅 | Body Rewrite, MITM, Map Local, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/Map-Local.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/app-clean.list<br>Scripts/app-clean.conf | 是 |
| 小宇宙 | Body Rewrite, MITM, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Scripts/app-clean.conf | 是 |
| 斗鱼 | Body Rewrite, MITM, Rule, Script, URL Rewrite | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Rewrite/Sources/URL-Rewrite.conf<br>Rules/reject.list<br>Scripts/app-clean.conf | 是 |
| Reddit | Body Rewrite, MITM, Script | 明确覆盖 | 高 | Rewrite/Sources/Body-Rewrite.conf<br>Rewrite/Sources/MITM.conf<br>Scripts/app-clean.conf | 是 |

## 后续改进

- 新增 App 规则或脚本后，应补充关键词映射。
- 高风险项需要在 Shadowrocket 中手动验证登录、支付、验证码和核心播放链路。
