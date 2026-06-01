# GrandpaNiu sing-box 版

这是面向高级 Android 用户的 sing-box source rule-set。它不是普通用户主推方案，也不是完整 sing-box 配置。

规则地址：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/sing-box/GrandpaNiu-Ads.json
```

## 使用方式

在自己的 sing-box 配置里通过 remote rule_set 引用，并把命中的规则设置为 `reject`。

```json
{
  "route": {
    "rule_set": [
      {
        "tag": "grandpaniu_ads",
        "type": "remote",
        "format": "source",
        "url": "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/sing-box/GrandpaNiu-Ads.json",
        "download_detour": "direct"
      }
    ],
    "rules": [
      {
        "rule_set": "grandpaniu_ads",
        "action": "reject"
      }
    ],
    "final": "direct"
  }
}
```

## 限制

Android 版只迁移域名、关键词和 IP 规则，不包含 iOS 的 Script、MITM、Rewrite 能力。它可以拦截常见广告域名和追踪域名，但不保证去除 YouTube、TikTok、Instagram、Facebook 等平台内嵌广告。
