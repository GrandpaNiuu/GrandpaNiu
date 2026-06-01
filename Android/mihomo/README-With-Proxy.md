# 已有节点用户使用 GrandpaNiu Android 规则

本文件给已经有机场订阅、节点配置、Clash / Mihomo 配置的安卓用户使用。

## 先看结论

已有节点订阅用户不要导入 `GrandpaNiu-Android-Full.yaml`。

`GrandpaNiu-Android-Full.yaml` 只适合没有节点、只想做广告拦截的用户。它是完整 Mihomo 配置，直接导入可能覆盖你原来的节点、策略组和规则。

已有节点用户应该使用：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

这个文件不是节点订阅，也不是完整配置。它只是广告规则集，需要加到你原来的 Clash / Mihomo 配置里。

## 加入 rule-providers

在原配置中加入：

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

## 在 rules 最前面加入

```yaml
rules:
  - RULE-SET,grandpaniu_ads,REJECT
  - MATCH,🚀 节点选择
```

`RULE-SET,grandpaniu_ads,REJECT` 必须放在 `MATCH`、`GEOIP`、代理分流规则之前。否则广告请求可能先被原来的代理规则命中，导致去广告规则不生效。

## 最终效果

保留原来的节点、策略组和 `MATCH`。

广告请求命中 GrandpaNiu 规则后会被 `REJECT`。

其他流量继续走你原来的节点、策略组或直连规则。

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

## 常见问题

### 为什么不能直接导入 GrandpaNiu-Ads.yaml？

因为它是规则集，不是完整配置。已有节点用户要把它挂到原配置中；没有节点的用户请导入 `GrandpaNiu-Android-Full.yaml`。

### 为什么不要导入 Full？

因为 Full 是完整配置，里面没有你的机场节点。已有节点用户导入后，可能会覆盖原来的节点、策略组和分流规则。

### 如果 App 或网站异常怎么办？

先关闭 GrandpaNiu 规则测试。如果关闭后恢复正常，说明可能误拦截，需要反馈具体域名或 App。