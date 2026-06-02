# Android App 增强规则索引

Android 端规则分为三层：

| 层级 | 路径 | 作用 | 是否默认启用 |
|---|---|---|---|
| 主规则 | `Android/mihomo/GrandpaNiu-Ads.yaml` | 低风险通用广告、统计、追踪域名 | 是，供主 Android 配置引用 |
| App 可选增强 | `Android/*/apps/` | 按 App 或组合包手动增强覆盖 | 否，用户手动引用 |
| 高风险测试层 | `Android/*/risky/` | HTTPDNS、宽泛 CDN、宽泛关键词等可能误伤规则 | 否，仅排查或测试使用 |

> 不要把 `apps/` 和 `risky/` 直接当作 Android Stable。它们是可选增强层。

## 使用原则

- 普通用户优先使用主规则。
- 想加强某个 App 时，只添加对应 App 文件。
- 想一次覆盖国内常见 App，可以使用 `Domestic-Apps` 组合包。
- 不建议同时启用 `Domestic-Apps` 和大量单 App 文件，规则会重复。
- 出现图片不加载、登录异常、页面空白、播放异常时，先关闭对应 App 增强规则。
- `risky/` 目录只用于测试和排查，不建议长期启用。

## 组合包

| 名称 | 说明 | Mihomo / FlClash | sing-box | AdGuard | v2rayNG |
|---|---|---|---|---|---|
| 国内 App 组合包 | 国内常见 App 广告、统计、追踪域名增强覆盖 | `Android/mihomo/apps/Domestic-Apps.yaml` | `Android/sing-box/apps/Domestic-Apps.json` | `Android/adguard/apps/Domestic-Apps.txt` | `Android/v2rayng/apps/Domestic-Apps-routing.json` |

## 单 App 规则

| App | Mihomo / FlClash | sing-box | AdGuard | v2rayNG |
|---|---|---|---|---|
| YouTube | `Android/mihomo/apps/YouTube.yaml` | `Android/sing-box/apps/YouTube.json` | `Android/adguard/apps/YouTube.txt` | `Android/v2rayng/apps/YouTube-routing.json` |
| Spotify | `Android/mihomo/apps/Spotify.yaml` | `Android/sing-box/apps/Spotify.json` | `Android/adguard/apps/Spotify.txt` | `Android/v2rayng/apps/Spotify-routing.json` |
| 抖音 / 字节系 | `Android/mihomo/apps/Douyin.yaml` | `Android/sing-box/apps/Douyin.json` | `Android/adguard/apps/Douyin.txt` | `Android/v2rayng/apps/Douyin-routing.json` |
| Bilibili | `Android/mihomo/apps/Bilibili.yaml` | `Android/sing-box/apps/Bilibili.json` | `Android/adguard/apps/Bilibili.txt` | `Android/v2rayng/apps/Bilibili-routing.json` |
| 小红书 | `Android/mihomo/apps/Xiaohongshu.yaml` | `Android/sing-box/apps/Xiaohongshu.json` | `Android/adguard/apps/Xiaohongshu.txt` | `Android/v2rayng/apps/Xiaohongshu-routing.json` |
| 微博 | `Android/mihomo/apps/Weibo.yaml` | `Android/sing-box/apps/Weibo.json` | `Android/adguard/apps/Weibo.txt` | `Android/v2rayng/apps/Weibo-routing.json` |
| 优酷 | `Android/mihomo/apps/Youku.yaml` | `Android/sing-box/apps/Youku.json` | `Android/adguard/apps/Youku.txt` | `Android/v2rayng/apps/Youku-routing.json` |
| 爱奇艺 | `Android/mihomo/apps/iQiyi.yaml` | `Android/sing-box/apps/iQiyi.json` | `Android/adguard/apps/iQiyi.txt` | `Android/v2rayng/apps/iQiyi-routing.json` |
| 芒果 TV | `Android/mihomo/apps/MangoTV.yaml` | `Android/sing-box/apps/MangoTV.json` | `Android/adguard/apps/MangoTV.txt` | `Android/v2rayng/apps/MangoTV-routing.json` |
| 网易云音乐 | `Android/mihomo/apps/NeteaseMusic.yaml` | `Android/sing-box/apps/NeteaseMusic.json` | `Android/adguard/apps/NeteaseMusic.txt` | `Android/v2rayng/apps/NeteaseMusic-routing.json` |
| 腾讯音乐 | `Android/mihomo/apps/TencentMusic.yaml` | `Android/sing-box/apps/TencentMusic.json` | `Android/adguard/apps/TencentMusic.txt` | `Android/v2rayng/apps/TencentMusic-routing.json` |
| 酷狗 | `Android/mihomo/apps/Kugou.yaml` | `Android/sing-box/apps/Kugou.json` | `Android/adguard/apps/Kugou.txt` | `Android/v2rayng/apps/Kugou-routing.json` |
| 喜马拉雅 | `Android/mihomo/apps/Ximalaya.yaml` | `Android/sing-box/apps/Ximalaya.json` | `Android/adguard/apps/Ximalaya.txt` | `Android/v2rayng/apps/Ximalaya-routing.json` |
| 淘宝 / 天猫 | `Android/mihomo/apps/Taobao.yaml` | `Android/sing-box/apps/Taobao.json` | `Android/adguard/apps/Taobao.txt` | `Android/v2rayng/apps/Taobao-routing.json` |
| 拼多多 | `Android/mihomo/apps/Pinduoduo.yaml` | `Android/sing-box/apps/Pinduoduo.json` | `Android/adguard/apps/Pinduoduo.txt` | `Android/v2rayng/apps/Pinduoduo-routing.json` |
| 美团 / 大众点评 | `Android/mihomo/apps/Meituan-Dianping.yaml` | `Android/sing-box/apps/Meituan-Dianping.json` | `Android/adguard/apps/Meituan-Dianping.txt` | `Android/v2rayng/apps/Meituan-Dianping-routing.json` |

## 高风险测试层

| 文件 | 说明 |
|---|---|
| `Android/mihomo/risky/Domestic-Risky.yaml` | HTTPDNS、宽泛 CDN、宽泛关键词等测试规则 |

`risky/` 层不是常规去广告规则。它可能导致 App 启动慢、图片不加载、播放异常、定位异常或接口连接失败。只有在你明确知道自己要测试什么时才启用。

## Mihomo / FlClash 引用示例

```yaml
rule-providers:
  grandpaniu_domestic_apps:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/apps/Domestic-Apps.yaml"
    path: ./ruleset/GrandpaNiu-Domestic-Apps.yaml
    interval: 86400

rules:
  - RULE-SET,grandpaniu_domestic_apps,REJECT
  - RULE-SET,grandpaniu_ads,REJECT
  - MATCH,🚀 节点选择
```

App 增强规则应放在 `MATCH`、`GEOIP`、普通代理分流规则之前。

## 维护要求

新增 Android App 规则时，应遵守：

1. 先放入 `apps/`，不要直接进入主规则。
2. 高风险规则放入 `risky/`，不要混入普通 App 文件。
3. 同一 App 尽量保持四种格式同步：Mihomo、sing-box、AdGuard、v2rayNG。
4. 不要承诺完整去广告、会员权益、权限解锁或接口改写能力。
5. 规则覆盖存在不等于真机测试通过。
