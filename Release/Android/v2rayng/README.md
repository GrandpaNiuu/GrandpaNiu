# GrandpaNiu v2rayNG / V2Ray / Xray 规则片段

这是面向高级 Android 用户的 V2Ray / Xray routing JSON 片段，不作为普通用户主推方案。普通用户优先使用 FlClash / Mihomo，并导入 `Android/mihomo/GrandpaNiu-Android-Full.yaml` 或按已有节点教程加入 `GrandpaNiu-Ads.yaml`。

规则片段地址：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/v2rayng/GrandpaNiu-v2rayng-routing.json
```

## 重要提醒

v2rayNG 不能直接导入 `GrandpaNiu-Ads.yaml`。

`GrandpaNiu-Ads.yaml` 是 Mihomo / Clash 规则集，不是 V2Ray 配置，也不是 v2rayNG 节点订阅。

v2rayNG 用户应使用 `GrandpaNiu-v2rayng-routing.json`，并把里面的 `routing.rules` 和 `block` outbound 手动合并进自己原来的配置。

已有节点用户不要导入完整配置覆盖原节点。正确做法是保留原来的 outbounds，把 `block` outbound 和广告 `routing.rules` 合并进原配置。

广告 `routing.rules` 必须放在普通 proxy/direct 规则之前。广告命中 `block`，其他流量继续走原节点。

## 这个文件包含什么

`GrandpaNiu-v2rayng-routing.json` 包含两部分：

```json
{
  "routing": {
    "rules": [
      {
        "type": "field",
        "domain": [
          "full:example.org",
          "domain:example.com",
          "keyword:ads"
        ],
        "outboundTag": "block"
      },
      {
        "type": "field",
        "ip": [
          "1.2.3.0/24",
          "2400:3200::/32"
        ],
        "outboundTag": "block"
      }
    ]
  },
  "outbounds": [
    {
      "tag": "block",
      "protocol": "blackhole",
      "settings": {
        "response": {
          "type": "none"
        }
      }
    }
  ]
}
```

## 合并方法

1. 打开你原来的 V2Ray / Xray 配置。
2. 保留原来的节点和 `outbounds`。
3. 把 `GrandpaNiu-v2rayng-routing.json` 里的 `block` outbound 加到原配置的 `outbounds` 数组里。
4. 把 `GrandpaNiu-v2rayng-routing.json` 里的广告 `routing.rules` 加到原配置的 `routing.rules` 最前面。
5. 确认这些广告规则位于普通 proxy/direct 规则之前。

合并后的效果是：广告请求命中 GrandpaNiu 规则后走 `block`，其他流量继续走你原来的节点、分流和直连规则。

## 限制

Android v2rayNG 版本只迁移域名、关键词和 IP 规则，不迁移 iOS / Surge / Shadowrocket 的 Script、MITM、Rewrite、Header Rewrite、Body Rewrite 功能。

它可以拦截常见广告域名、追踪域名和部分 App 广告请求，但不保证去除所有广告，尤其是 YouTube、TikTok、Instagram、Facebook 等平台内嵌广告，因为这些广告可能和正常内容共用同一域名。
