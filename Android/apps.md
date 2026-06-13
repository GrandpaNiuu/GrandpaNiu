# Android App 增强规则索引

Android 版现在由 `scripts/build_android_rules.py` 自动生成四类输出：

- Mihomo / FlClash: `Android/mihomo/`
- sing-box: `Android/sing-box/`
- AdGuard: `Android/adguard/`
- v2rayNG: `Android/v2rayng/`

## 分层

| 层级 | 路径 | 作用 | 默认进入主规则 |
|---|---|---|---|
| 主规则 | `Android/mihomo/GrandpaNiu-Ads.yaml` | 聚合低风险 Android 源、iOS 通用 reject、iOS App 兼容 reject | 是 |
| App 增强 | `Android/*/apps/` | 按 App 或组合包输出，便于单独引用 | 已聚合进主规则，也可单独引用 |
| iOS 通用兼容 | `iOS-Compatible-Reject` | 从 `Rules/reject.list` 提取 Android 可表达规则 | 是 |
| iOS App 兼容 | `iOS-App-Compatible-Reject` | 从 `Rewrite/Sources/Apps/*.conf` 的 `[Rule]` REJECT 规则提取 | 是 |
| 高风险测试 | `Android/*/risky/` | HTTPDNS、宽泛 CDN、宽泛关键词等排查规则 | 否 |

## iOS 转 Android 的边界

Android 规则只能稳定承载域名、关键词和 IP 类拦截能力。构建器会自动跳过：

- `[Script]`
- `[MITM]`
- `[URL Rewrite]`
- `[Header Rewrite]`
- `[Body Rewrite]`
- `[Map Local]`
- `DIRECT` / `PROXY` / 播放保护类规则
- 登录、支付、银行、验证码、媒体播放、图片 CDN 等保护域

这意味着 Android 会继承 iOS/Fusion 里能安全转成规则集的部分，但不会承诺具备 iOS 模块级脚本净化能力。

## 推荐入口

普通用户优先使用完整 Mihomo 配置：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Android-Full.yaml
```

已有节点订阅或已有 Mihomo 配置的用户，请只加入规则集：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

示例：

```yaml
rule-providers:
  grandpaniu_ads:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml"
    path: ./ruleset/GrandpaNiu-Ads.yaml
    interval: 86400

rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - MATCH,DIRECT
```

`RULE-SET,grandpaniu_ads,REJECT` 应放在 `MATCH`、`GEOIP` 和普通代理分流规则之前。

## 单独增强包

| 名称 | Mihomo / FlClash | sing-box | AdGuard | v2rayNG |
|---|---|---|---|---|
| iOS App 兼容层 | `Android/mihomo/apps/iOS-App-Compatible-Reject.yaml` | `Android/sing-box/apps/iOS-App-Compatible-Reject.json` | `Android/adguard/apps/iOS-App-Compatible-Reject.txt` | `Android/v2rayng/apps/iOS-App-Compatible-Reject-routing.json` |
| iOS 通用兼容层 | `Android/mihomo/apps/iOS-Compatible-Reject.yaml` | `Android/sing-box/apps/iOS-Compatible-Reject.json` | `Android/adguard/apps/iOS-Compatible-Reject.txt` | `Android/v2rayng/apps/iOS-Compatible-Reject-routing.json` |
| 国内 App 组合包 | `Android/mihomo/apps/Domestic-Apps.yaml` | `Android/sing-box/apps/Domestic-Apps.json` | `Android/adguard/apps/Domestic-Apps.txt` | `Android/v2rayng/apps/Domestic-Apps-routing.json` |
| YouTube | `Android/mihomo/apps/YouTube.yaml` | `Android/sing-box/apps/YouTube.json` | `Android/adguard/apps/YouTube.txt` | `Android/v2rayng/apps/YouTube-routing.json` |
| Spotify | `Android/mihomo/apps/Spotify.yaml` | `Android/sing-box/apps/Spotify.json` | `Android/adguard/apps/Spotify.txt` | `Android/v2rayng/apps/Spotify-routing.json` |
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

## 维护要求

1. Android 源优先维护在 `Android/mihomo/apps/`，脚本会同步生成其他三种格式。
2. iOS/Fusion 源里的可迁移 REJECT 规则会自动进入 `iOS-App-Compatible-Reject`。
3. 不要把会员解锁、支付绕过、登录绕过、视频播放链路、图片 CDN 保护规则转成 Android REJECT。
4. 出现图片不加载、登录异常、白屏、播放异常时，先暂停对应单 App 增强包或主规则集并反馈具体域名。
5. `Android/*/risky/` 只用于排查，不进入主规则。
