# GrandpaNiu Android Mihomo 使用说明

Android 版本面向 Mihomo / Clash Meta / FlClash 等兼容客户端。

## 导入页

打开：

```text
https://grandpaniuu.github.io/GrandpaNiu/android.html
```

## 没有节点，只想做广告拦截

导入完整配置：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Android-Full.yaml
```

`GrandpaNiu-Android-Full.yaml` 是完整 Mihomo 配置，适合没有节点、只想做广告拦截的用户。

## 已有节点订阅用户

已有节点订阅用户不要导入 `GrandpaNiu-Android-Full.yaml`。

已有节点用户应把 `GrandpaNiu-Ads.yaml` 加到原 Clash / Mihomo 配置里：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

参考：

```text
Android/mihomo/README-With-Proxy.md
```

核心规则：

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
  - MATCH,🚀 节点选择
```

`RULE-SET,grandpaniu_ads,REJECT` 必须放在 `MATCH`、`GEOIP`、代理分流规则之前。

保留原来的节点、策略组和 `MATCH`；广告请求拦截，其他流量继续走原节点。