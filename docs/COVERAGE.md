# 功能覆盖清单

本清单记录 `Ronghemokuai.sgmodule` 当前重点覆盖对象、覆盖强度和维护状态。实际生效范围由 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Remotes/sources.json` 和 `Rewrite/Profiles/stable.conf` 共同决定。

## 覆盖强度说明

| 状态 | 含义 |
|---|---|
| 重点专项 | 有白名单、脚本、MITM 或专门保护逻辑 |
| 明确覆盖 | 有脚本、Body Rewrite、Map Local 或明确本地规则 |
| 部分覆盖 | 有规则或局部接口处理，但不是完整独立模块 |
| 不建议加入 | 容易影响登录、支付、验证码或账户安全 |

## 重点专项

| App / 服务 | 状态 | 说明 |
|---|---|---|
| Spotify | 重点专项 | DIRECT 白名单、Header Rewrite、`spotify-json`、`spotify-proto`、必要 MITM |
| YouTube | 重点专项 | `youtube.response`，保留 YouTube Enhance 逻辑 |
| 知乎 | 重点专项 | `zhihu-enhance` 与既有问题页清理，处理广告卡片、推荐广告、商业字段 |
| Bilibili | 部分覆盖 | 当前为规则和 Map Local 局部净化，不是完整独立脚本模块 |

## 明确覆盖对象

| 分类 | App / 服务 |
|---|---|
| 社区内容 | 微博、百度贴吧、小红书、酷安、小黑盒、脉脉、Reddit、飞客茶馆、盖得排行、Soul、皮皮虾 |
| 新闻资讯 | QQ 新闻 / 腾讯新闻、网易新闻、财新、IT之家、什么值得买、51CTO |
| 视频音乐 | 芒果 TV、人人视频、网易云音乐、咪咕视频、斗鱼、喜马拉雅、小宇宙 FM、快看漫画 |
| 电商生活 | 淘宝、闲鱼、京东、拼多多、盒马、菜鸟、美团、美团外卖、大众点评、饿了么、瑞幸、Cotti、Manner、朴朴、Lawson、途虎养车 |
| 出行地图 | 滴滴、12306、航旅纵横、高德地图、百度地图、飞猪、国航、吉祥航空、深圳通类 App |
| 阅读教育 | 起点、网易有道词典、问卷星、宝宝树、薄荷、Gaoding、51CTO |
| 工具其他 | 迅雷、转转、海尔、配音秀、360 摄像机、萤石云、搜狗输入法、韵达、Usmile、QBB6 |

## 远程规则覆盖

当前远程规则源以 `Rewrite/Remotes/sources.json` 为准，主要包括：

```text
blackmatrix7 Advertising
blackmatrix7 Advertising Lite
blackmatrix7 Hijacking
blackmatrix7 Privacy
Cats-Team AdRules
privacy-protection-tools anti-AD
ACL4SSR BanAD
ACL4SSR BanProgramAD
ACL4SSR BanEasyListChina
Loyalsoldier reject
217heidai adblockfilters
```

远程规则源主要用于通用广告域名、隐私追踪、劫持域名、网页广告和常见广告 SDK。不要把远程规则源理解为每个 App 都有完整脚本模块。

## 本地规则与重写覆盖

| 区块 | 作用 |
|---|---|
| `[Rule]` | DIRECT 白名单、本地 REJECT、远程 RULE-SET / DOMAIN-SET |
| `[URL Rewrite]` | URL 层广告接口清理 |
| `[Header Rewrite]` | Header 层处理，例如 Spotify 缓存头处理 |
| `[Body Rewrite]` | JSON 字段清理，处理广告卡片、弹窗、活动字段 |
| `[Map Local]` | 本地空响应，例如 Bilibili、喜马拉雅、瑞幸、转转、美团等局部接口 |
| `[Script]` | Spotify、YouTube、知乎和普通 App 去广告脚本 |
| `[MITM]` | 使用 `%APPEND%` 追加必要 hostname |

## Bilibili 当前状态

Bilibili 目前是局部净化：

```text
规则层：biliapi 相关域名拦截
Map Local：活动、搜索、广告素材、PGC 活动物料等接口
```

不加入权益类、账号类、付费类改写。

## 知乎当前状态

知乎已经加入增强净化层：

```text
Scripts/zhihu-enhance.conf
Scripts/zhihu-enhance.js
```

处理范围：

```text
信息流广告
回答页广告
推荐广告
商业卡片
推广字段
赞助字段
```

不处理：

```text
会员
盐选 / 付费内容
支付状态
登录状态
账号身份
Cookie / Token
```

## 不建议加入拦截的对象

```text
微信 / 支付宝 / 银行 App 登录与支付接口
验证码接口
证书校验接口
账号安全接口
会员权益接口
Cookie / Token / 账户状态接口
```

上述对象如果出现广告，只能做极小范围、可回滚的局部处理，不允许大面积 MITM 或脚本覆盖。
