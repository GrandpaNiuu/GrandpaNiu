# 已有节点用户使用 GrandpaNiu Android 规则

这个文件面向已经有机场节点订阅、已经能正常使用 Clash / Mihomo 配置的用户。

这个文件不是节点订阅。它不会提供代理节点，也不会替换你的机场订阅。它只是给已有节点配置增加广告拦截能力。

已有节点订阅用户不要导入 GrandpaNiu-Android-Full.yaml。

GrandpaNiu-Android-Full.yaml 是完整 Mihomo 配置，只适合没有节点、只想做广告拦截的用户。如果用户已经有机场节点订阅，直接导入 GrandpaNiu-Android-Full.yaml 可能会覆盖原来的节点、策略组和规则。

GrandpaNiu-Ads.yaml 不是节点订阅，也不是完整配置。它只是广告规则集。已有节点用户应该把它加入自己原来的 Clash / Mihomo 配置里。

规则集地址：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

如果你已经有节点订阅，不要导入 `GrandpaNiu-Android-Full.yaml`，否则可能覆盖你原来的节点、策略组和分流规则。请把 `GrandpaNiu-Ads.yaml` 加到你原来的 Clash / Mihomo 配置里。

## 推荐方式

如果客户端支持覆写 / Override / Mixin，优先用覆写方式加入 GrandpaNiu 规则。这样机场订阅更新时，不容易覆盖你的广告拦截配置。

如果客户端不支持覆写，需要手动编辑 YAML。注意：如果机场订阅更新，手动修改可能会被覆盖，需要重新添加。

## 加入 rule-providers

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

## 把广告规则放在最前面

在 `rules` 最前面加入：

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
```

RULE-SET,grandpaniu_ads,REJECT 必须放在 MATCH、GEOIP、代理分流规则之前。如果放在 MATCH 后面，广告请求可能会先被原来的代理规则命中，导致去广告规则不生效。

最终效果：保留原来的节点、策略组和 MATCH。广告请求命中 GrandpaNiu 规则后会被 REJECT。其他流量继续走用户原来的节点、策略组或直连规则。

## 示例一：广告拦截 + 其他全部走节点

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - MATCH,🚀 节点选择
```

## 示例二：广告拦截 + 国内直连 + 国外走节点

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - GEOIP,CN,DIRECT
  - MATCH,🚀 节点选择
```

## 示例三：广告拦截 + 默认直连 + 指定网站走节点

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - DOMAIN-SUFFIX,google.com,🚀 节点选择
  - DOMAIN-SUFFIX,youtube.com,🚀 节点选择
  - DOMAIN-SUFFIX,twitter.com,🚀 节点选择
  - MATCH,DIRECT
```

## 出现异常怎么办

如果遇到某个网站或 App 异常，可以先关闭 GrandpaNiu 规则，测试是否由广告拦截误拦截导致。

如果关闭后恢复正常，可以反馈具体 App、页面、时间、客户端日志和可疑域名，后续再逐项清理。
