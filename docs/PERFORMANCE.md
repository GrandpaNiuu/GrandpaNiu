# 性能与耗电说明

本文件用于说明 `Ronghemokuai.sgmodule` 在 Shadowrocket / Surge 中可能产生的性能和电量影响，以及后续如何维护低耗电版本。

## 基本判断

当前模块属于融合型模块，不是轻量单规则模块。它同时包含：

```text
远程规则
本地规则
URL Rewrite
Header Rewrite
Body Rewrite
Map Local
http-response 脚本
MITM hostname
```

因此它的耗电水平通常高于纯规则模块，但低于同时叠加多个大型模块、重复 MITM、重复脚本的混乱配置。

## 主要耗电来源

| 来源 | 说明 | 影响 |
|---|---|---|
| MITM HTTPS 解密 | 需要解密指定 hostname 的 HTTPS 流量 | 中等到偏高 |
| Body Rewrite | 对响应体进行字段改写 | 中等 |
| http-response 脚本 | 命中接口后执行 JavaScript | 中等到偏高 |
| 大型 JSON 处理 | YouTube、知乎、信息流类接口返回内容大 | 偏高 |
| 视频 / 信息流 App 高频请求 | YouTube、知乎、小红书、微博、Bilibili 等 | 偏高 |
| 远程规则集 | 规则匹配本身一般比脚本轻 | 低到中等 |

## 实际使用判断标准

在 iPhone 中查看：

```text
设置 -> 电池 -> App 电池用量 -> Shadowrocket
```

建议观察 24 小时：

| Shadowrocket 电池占比 | 判断 |
|---|---|
| 1% - 3% | 很轻 |
| 3% - 8% | 正常 |
| 8% - 10% | 偏重但可接受 |
| 10% - 15% | 需要观察高频 App 和脚本命中 |
| 15% 以上 | 建议切换低耗电配置或减少脚本 |

## 高频场景

更容易增加耗电的使用方式：

```text
长时间刷知乎信息流 / 回答页
长时间看 YouTube
长时间刷小红书 / 微博 / 淘宝 / 京东 / 拼多多
长时间看 Bilibili / 直播 / 短视频
开启 HTTPS 解密并同时使用多个脚本模块
```

不太容易明显增加耗电的使用方式：

```text
只保持 Shadowrocket 开启
轻度网页浏览
只使用远程规则拦截广告域名
只播放 Spotify，且没有频繁跳歌或重连
```

## 低耗电维护原则

1. 脚本优先精简，规则其次精简。
2. MITM hostname 只保留必要域名，不无脑扩大。
3. 高频 App 的 pattern 必须精准，避免匹配过宽。
4. 不常用 App 的脚本不要默认加入核心 profile。
5. 新脚本默认 pending，确认稳定后再加入 stable。
6. 视频类、信息流类、购物类 App 的响应体脚本要优先观察耗电。

## Lite Profile

仓库提供 `Rewrite/Profiles/lite.conf` 作为低耗电参考 profile。

特点：

```text
保留 Spotify 核心保护
保留 YouTube 核心脚本
保留知乎增强净化
减少普通 App 脚本
减少远程规则源参与
关闭 source_rule_compat
关闭 source_script_compat
```

构建命令：

```text
python3 scripts/build_module.py --build --profile lite
```

注意：

```text
lite profile 是低耗电参考配置，不是默认正式配置。
默认正式配置仍然是 stable profile。
如果要把 lite 作为正式主模块，需要先手动测试 24 小时。
```

## 测试建议

切换或调整模块后，至少测试：

```text
Spotify 连续播放 10 首歌
YouTube 首页、搜索、播放、Shorts
知乎首页、回答页、搜索页
微信、支付宝、银行 App 登录/验证码/支付
淘宝、京东、拼多多、外卖类 App 常用流程
```

若出现空白、加载失败、登录异常或支付异常，优先回看最近新增的：

```text
Scripts/*.conf
Rewrite/Sources/Body-Rewrite.conf
Rewrite/Sources/URL-Rewrite.conf
Rewrite/Sources/MITM.conf
Rewrite/Remotes/sources.json
```
