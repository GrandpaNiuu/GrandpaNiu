# GrandpaNiu Android 使用教程

## 1. 这个 Android 版本是什么

- 这是 Android 规则版本。
- 它不是代理节点订阅。
- 它主要用于广告域名拦截和规则分流。
- 第一版不包含 iOS 的 Script、MITM、Rewrite 功能。

Android 版本主要通过域名、关键词、IP 规则进行广告拦截，可拦截常见广告域名、追踪域名和部分 App 广告请求。但它不保证去除所有广告，尤其是 YouTube、TikTok、Instagram、Facebook 等平台内嵌广告，因为这些广告可能和正常内容共用同一域名。

## 2. 推荐使用方式

推荐使用：

- FlClash
- Clash Meta For Android
- Mihomo 兼容客户端

普通用户优先使用：

```text
Android/mihomo/GrandpaNiu-Android-Full.yaml
```

## 3. 普通用户导入方法

第一步：下载安装 FlClash 或 Clash Meta For Android。

第二步：复制完整配置链接。

第三步：打开客户端。

第四步：导入配置。

第五步：启动 VPN。

第六步：更新规则。

完整配置链接：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Android-Full.yaml
```

## 4. 会配置的用户使用规则集

下面这个链接是规则集，不是完整订阅：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

示例配置：

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

## 5. 已有节点用户怎么使用

已有节点订阅用户不要导入 GrandpaNiu-Android-Full.yaml。

GrandpaNiu-Android-Full.yaml 是完整 Mihomo 配置，只适合没有节点、只想做广告拦截的用户。如果用户已经有机场节点订阅，直接导入 GrandpaNiu-Android-Full.yaml 可能会覆盖原来的节点、策略组和规则。

GrandpaNiu-Ads.yaml 不是节点订阅，也不是完整配置。它只是广告规则集。已有节点用户应该把它加入自己原来的 Clash / Mihomo 配置里。

规则集地址：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

如果你已经有机场节点订阅，不要直接导入 `GrandpaNiu-Android-Full.yaml` 覆盖原配置。`GrandpaNiu-Android-Full.yaml` 适合没有节点、只想使用广告规则拦截的普通用户。

已有节点用户应该使用 `Android/mihomo/GrandpaNiu-Ads.yaml` 作为 rule-provider，把它加到原来的 Clash / Mihomo 配置里：

1. 添加 `rule-providers`。
2. 在 `rules` 最前面添加 `RULE-SET,grandpaniu_ads,REJECT`。
3. 保留你原来的节点、策略组和 `MATCH` 规则。

这样就是：广告请求拦截，其他流量继续走你的节点。

```yaml
rule-providers:
  grandpaniu_ads:
    type: http
    behavior: classical
    format: yaml
    url: "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml"
    path: ./ruleset/GrandpaNiu-Ads.yaml
    interval: 86400
```

在 `rules` 最前面加入：

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
```

RULE-SET,grandpaniu_ads,REJECT 必须放在 MATCH、GEOIP、代理分流规则之前。如果放在 MATCH 后面，广告请求可能会先被原来的代理规则命中，导致去广告规则不生效。

最终效果：保留原来的节点、策略组和 MATCH。广告请求命中 GrandpaNiu 规则后会被 REJECT。其他流量继续走用户原来的节点、策略组或直连规则。

示例一：广告拦截 + 其他全部走节点

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - MATCH,🚀 节点选择
```

示例二：广告拦截 + 国内直连 + 国外走节点

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - GEOIP,CN,DIRECT
  - MATCH,🚀 节点选择
```

示例三：广告拦截 + 默认直连 + 指定网站走节点

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - DOMAIN-SUFFIX,google.com,🚀 节点选择
  - DOMAIN-SUFFIX,youtube.com,🚀 节点选择
  - DOMAIN-SUFFIX,twitter.com,🚀 节点选择
  - MATCH,DIRECT
```

更多说明见：

```text
Android/mihomo/README-With-Proxy.md
```

## 6. AdGuard 用户怎么用

- 使用 Android 系统自带“私人 DNS”不能直接导入 txt 规则。
- 如果要用 `GrandpaNiu-DNS.txt`，需要使用 AdGuard Android App、AdGuard DNS 用户规则、AdGuard Home 等支持自定义过滤规则的方式。
- 规则地址：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/adguard/GrandpaNiu-DNS.txt
```

## 7. sing-box 用户怎么用

这是高级用户方案。使用 remote rule_set 引用：

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

## 8. 常见问题

Q：为什么我直接导入 GrandpaNiu-Ads.yaml 报错？

A：因为 GrandpaNiu-Ads.yaml 是规则集，不是完整配置。普通用户请导入 GrandpaNiu-Android-Full.yaml。

Q：这个 Android 版本有没有代理节点？

A：没有。它是规则配置，不提供代理节点。

Q：为什么 iOS 的脚本功能安卓没有？

A：因为 Surge/Shadowrocket 的 Script、MITM、Rewrite 是 iOS/Surge 生态能力，不能直接等价迁移到安卓。Android 第一版只迁移域名、关键词、IP 规则。

Q：启动后没效果怎么办？

A：

1. 确认导入的是 GrandpaNiu-Android-Full.yaml。
2. 确认客户端 VPN 已启动。
3. 确认规则已更新。
4. 确认日志里没有配置报错。
5. 如果使用自己的配置，确认 rules 里有 `RULE-SET,grandpaniu_ads,REJECT`。

Q：这个会影响正常上网吗？

A：可能会误拦截。如果遇到某个 App 或网站异常，可以暂时关闭配置，或反馈具体域名和客户端日志。

## 9. 开发者构建方法

```text
python scripts/build_android.py
```

生成文件：

```text
Android/mihomo/GrandpaNiu-Ads.yaml
Android/mihomo/GrandpaNiu-Android-Full.yaml
Android/sing-box/GrandpaNiu-Ads.json
Android/adguard/GrandpaNiu-DNS.txt
```
