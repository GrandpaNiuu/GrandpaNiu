# GrandpaNiu Android 使用教程

## 这个 Android 版本是什么

这是 Android 规则版本，主要用于广告域名拦截和规则分流。

它不是代理节点订阅，也不提供节点。

第一版不包含 iOS 的 Script、MITM、Rewrite 功能。Android 版本主要迁移域名、关键词和部分 IP 规则。

## 推荐客户端

普通用户优先使用：

- FlClash
- Clash Meta For Android
- 其他 Mihomo 兼容客户端

## 没有节点的用户怎么用

没有节点、只想做广告拦截的用户，导入完整配置：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Android-Full.yaml
```

步骤：

1. 安装 FlClash 或 Clash Meta For Android。
2. 打开导入页：`https://grandpaniuu.github.io/GrandpaNiu/android.html`。
3. 点击一键尝试导入。
4. 如果跳转失败，复制完整配置链接，在客户端里手动导入。
5. 启动 VPN。
6. 更新规则。

## 已有节点用户怎么用

已有节点订阅用户不要导入 `GrandpaNiu-Android-Full.yaml`。

`GrandpaNiu-Android-Full.yaml` 只适合没节点、只想做广告拦截的用户。已有节点用户直接导入它，可能覆盖原来的节点、策略组和规则。

已有节点用户应把 `GrandpaNiu-Ads.yaml` 加到原 Clash / Mihomo 配置里：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/mihomo/GrandpaNiu-Ads.yaml
```

加入：

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
  - MATCH,🚀 节点选择
```

`RULE-SET,grandpaniu_ads,REJECT` 必须放在 `MATCH`、`GEOIP`、代理分流规则之前。

保留原来的节点、策略组和 `MATCH`；广告请求拦截，其他流量继续走原节点。

## 常见问题

### 为什么直接导入 GrandpaNiu-Ads.yaml 报错？

因为 `GrandpaNiu-Ads.yaml` 是规则集，不是完整配置。普通无节点用户请导入 `GrandpaNiu-Android-Full.yaml`；已有节点用户请把规则集挂到原配置里。

### Android 版本有没有代理节点？

没有。它是规则配置，不提供代理节点。

### 为什么 iOS 的脚本功能 Android 没有？

因为 Surge / Shadowrocket 的 Script、MITM、Rewrite 是 iOS / Surge 生态能力，不能直接等价迁移到 Android。

### 启动后没效果怎么办？

1. 确认导入的是正确文件。
2. 确认客户端 VPN 已启动。
3. 确认规则已更新。
4. 确认日志里没有配置报错。
5. 已有节点用户确认 `RULE-SET,grandpaniu_ads,REJECT` 放在 `rules` 最前面。

### 会影响正常上网吗？

可能会误拦截。如果某个 App 或网站异常，可以先关闭 GrandpaNiu 规则测试，再反馈具体域名或 App。