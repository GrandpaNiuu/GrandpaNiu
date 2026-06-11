# GrandpaNiu Mihomo / Clash Meta 版

这是 Android 可用的 GrandpaNiu 规则版本，适合 FlClash、Clash Meta For Android、Mihomo 兼容客户端。

## 普通用户推荐

普通用户请导入完整配置：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Android-Full.yaml
```

它不包含代理节点，只会使用 GrandpaNiu 广告规则进行 `REJECT` 拦截，最后默认 `MATCH,DIRECT`。

## 已有节点用户怎么使用

已有节点订阅用户不要导入 GrandpaNiu-Android-Full.yaml。

GrandpaNiu-Android-Full.yaml 是完整 Mihomo 配置，只适合没有节点、只想做广告拦截的用户。如果用户已经有机场节点订阅，直接导入 GrandpaNiu-Android-Full.yaml 可能会覆盖原来的节点、策略组和规则。

GrandpaNiu-Ads.yaml 不是节点订阅，也不是完整配置。它只是广告规则集。已有节点用户应该把它加入自己原来的 Clash / Mihomo 配置里。

规则集地址：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

如果你已经有节点订阅，不要导入 `GrandpaNiu-Android-Full.yaml`，否则可能覆盖你原来的节点、策略组和分流规则。

`GrandpaNiu-Android-Full.yaml` 适合没有节点、只想使用广告规则拦截的普通用户。

已有节点用户请把 `GrandpaNiu-Ads.yaml` 加到你原来的 Clash / Mihomo 配置里：

1. 添加 `rule-providers`。
2. 在 `rules` 最前面添加 `RULE-SET,grandpaniu_ads,REJECT`。
3. 保留你原来的节点、策略组和 `MATCH` 规则。

这样就是：广告请求拦截，其他流量继续走你的节点。

在已有配置中加入：

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

然后在 `rules` 最前面加入：

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

更详细说明见 [README-With-Proxy.md](README-With-Proxy.md)。

## 高级用户规则集

`GrandpaNiu-Ads.yaml` 是规则集，不是完整配置。只有会自己写 Mihomo 配置的用户才需要它：

GrandpaNiu-Ads.yaml 是规则集，不是完整订阅；普通安卓用户请导入 GrandpaNiu-Android-Full.yaml。

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

## 能做什么

- 通过域名、域名后缀、关键词和 IP 规则拦截常见广告域名、追踪域名和部分 App 广告请求。
- 不提供代理节点。
- 不包含 iOS 的 Script、MITM、Rewrite、Header Rewrite、Body Rewrite。

## 做不到什么

它不保证去除所有广告。YouTube、TikTok、Instagram、Facebook 等平台内嵌广告可能和正常内容共用同一域名，单靠 Android 规则集通常无法稳定拦截。

遇到 App 或网站异常时，可以先暂停配置，或反馈具体域名和客户端日志。
