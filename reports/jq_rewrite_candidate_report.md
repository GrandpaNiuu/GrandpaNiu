# JQ 改写候选与国内 App 加强报告

- 生成时间：2026-06-13 08:38:17 +0800
- 范围：仅检查仓库内 Surge / Shadowrocket 模块源头；不把静态覆盖写成客户端效果承诺。
- 安全边界：只把可用 `http-response-jq` 表达的 JSON Body 处理纳入改写；二进制、protobuf、HTML/JS 注入、请求头判定、支付/登录/订单链路不改。

## 结论

当前国内 App 去广不是整体缺失，但局部偏弱：

1. **京东**：app 子模块仍引用远程 `JD_remove_ads.js`，且命中 `myOrderInfo` / `orderTrackBusiness` 这类订单相关接口；适合拆出非敏感、JSON 型广告字段改为本地 JQ，同时把订单相关接口排除，降低误伤。
2. **美团 / 大众点评**：融合源头已有多条 URL reject，但 app 子模块缺少对应 Body Rewrite；其中 `adshopping`、`operating`、`growth` 这类广告/运营位 JSON 接口适合改成 JQ 空数据/删字段，比整段 reject 更可回滚。
3. **高德地图 / 百度地图 / 饿了么 / 滴滴 / 夸克 / B 站漫画等**：已有较多 JQ 或 Map Local，继续保守维护，不做跨域泛化。
4. **Spotify / YouTube / Bilibili protobuf**：不适合 JQ；这些链路涉及 protobuf、二进制 body、播放链路或复杂脚本，改成 JQ 会增加风险。

## 已改写候选

| App | 原始形态 | 判断 | 本次动作 | 防误伤边界 |
|---|---|---|---|---|
| 京东 | `JD_remove_ads.js` 远程脚本，命中 `deliverLayer/getTabHomeInfo/myOrderInfo/orderTrackBusiness/personinfoBusiness/start/welcomeHome` | 部分适合 JQ | 已改为 JQ：仅覆盖 `deliverLayer/getTabHomeInfo/personinfoBusiness/start/welcomeHome`；删除广告、弹窗、开屏类字段 | host 固定 `api.m.jd.com`；排除 `myOrderInfo`、`orderTrackBusiness` 订单链路 |
| 大众点评 | `m.dianping.com/mapi/mgw/growth/queryhaima`、`mapi.dianping.com/mapi/mgw/growth/clipboardquery` 旧规则为 `reject-dict` | 适合 JQ | reject 改为 JQ：删除 `data/result/moduleList/modules` | host 固定 `m.dianping.com` / `mapi.dianping.com`；仅 mgw growth 路径 |
| 大众点评 | `mapi.dianping.com/adshopping`、`mapi.dianping.com/mapi/operating/(indexopsmodules|loadsplashconfig)` 旧规则为 reject | 适合 JQ | reject 改为 JQ：返回空 `data` 或删除广告数据字段 | host 固定 `mapi.dianping.com`；仅 adshopping / operating 路径 |
| 美团小程序 | `rms.meituan.com/queryPortalInfo`、`web.meituan.com/miniprogram` 已有融合 JQ | 已适合 JQ | 同步到 `Rewrite/Sources/Apps/meituan.conf`，补齐 per-app 模块 Body Rewrite | host 固定 `rms.meituan.com` / `web.meituan.com`；仅模块广告/浮窗/底栏入口 |

## 不改写候选

| App / 类型 | 原因 | 处理 |
|---|---|---|
| Spotify / YouTube / Bilibili protobuf | 播放、protobuf、二进制或脚本逻辑，JQ 不能等价表达 | 不适合 JQ，保留现有脚本/保护链路 |
| 京东 `myOrderInfo` / `orderTrackBusiness` | 订单状态、物流或交易相关链路，误伤成本高 | 从新增 JQ 批次排除 |
| 支付 / 登录 / 会员 / 验证码 / 银行 | 敏感链路，不应做 Body 改写 | 继续由 protect 规则直连或绕过 |
| 纯图片资源、请求头判定、HTML/JS 文本替换 | JQ 只适合 JSON body，不能安全表达这些操作 | 保留 URL Rewrite / Map Local / Script 或不纳入 |

## 变更源头

- `Rewrite/Sources/Body-Rewrite.conf`：新增 `Domestic App Safe JQ Reinforcement` 批次。
- `Rewrite/Sources/Apps/jd.conf`：移除远程 `JD_remove_ads.js` app 子模块引用，改为端点级 JQ；保留 `api.m.jd.com` MITM。
- `Rewrite/Sources/Apps/meituan.conf`：补齐美团 / 大众点评 Body Rewrite；把适合 JQ 的点评 reject 移到 JQ。
- `Rewrite/Sources/URL-Rewrite.conf`：移除已被 JQ 接管的点评 reject，避免重复处理。

## 回滚方式

如某个 App 反馈异常，只回滚对应 host 的新增 JQ 行后重建，不影响其他 App：

- 京东：回滚 `api.m.jd.com/client.action?functionId=...` 两条新增 JQ。
- 大众点评：回滚 `mapi.dianping.com/adshopping`、`mapi.dianping.com/mapi/operating/...`、`m(?:api)?.dianping.com/.../mgw/growth/...` 三条新增 JQ。
- 美团小程序：回滚 `rms.meituan.com` / `web.meituan.com` app 子模块 Body Rewrite 同步行。
