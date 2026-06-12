# GrandpaNiu 融合模块规则与脚本完整审计报告

生成依据：仓库现有构建报告、规则报告、脚本清单、远程规则语法报告、模块完整性报告、App 覆盖矩阵、App 状态矩阵和手动测试记录。

## 1. 总结结论

当前 `Ronghemokuai.sgmodule` 可以判定为：

- 静态结构正常。
- Root / Release 内容一致。
- 没有重复 section。
- 没有重复 active rule / rewrite / script / MITM line。
- 没有重复脚本名。
- 没有多个入口共用同一个 script-path。
- 远程规则源语法全部通过。
- 单一融合 profile `fusion` 可发布。
- App 覆盖已经形成完整矩阵，但部分 App 仍是“静态覆盖未真机测试”，不能写成真实通过。

真实边界：本报告确认的是静态结构、生成链路、语法和覆盖面；不等于所有 App 的真实客户端行为都已经人工验证。涉及登录、支付、验证码、银行、微信媒体、图片 CDN、小程序、视频播放的变更仍必须复测。

## 2. 构建产物总览

| 项目 | 当前结果 |
|---|---:|
| 主模块 | `Release/Ronghemokuai.sgmodule` |
| 主模块大小 | 350483 bytes |
| Release 独立 App 模块 | 27 |
| checksum 条目 | 49 |
| 构建时间 | 2026-06-12T14:38:04Z |

## 3. 主融合模块 Section 覆盖

| Section | Active lines |
|---|---:|
| Rule | 713 |
| URL Rewrite | 1644 |
| Header Rewrite | 1 |
| Body Rewrite | 455 |
| Map Local | 148 |
| Script | 46 |
| MITM | 1 |

解释：`MITM` section 只有 1 行是正常的，因为它通常是一行 `hostname = %APPEND% ...`，实际 hostname 数量见完整性检查。

## 4. 完整性检查

| 检查项 | 结果 |
|---|---|
| Root / Release 内容一致 | 通过 |
| 重复 section | 无 |
| 重复 active rule / rewrite / script / MITM line | 无 |
| Script 入口数 | 46 |
| MITM hostname 数 | 1072 |
| 本地规则 active entries | 3638 |
| 跨文件交集 entries | 1405 |
| 远程规则源总数 | 16 |
| 已启用远程规则源 | 14 |

说明：跨文件交集不是故障。最终融合模块构建时会按 active line 去重；单独规则包、Android 包和兼容包保留交集是允许的。

## 5. Release 规则输出

| 分类 | 数量 |
|---|---:|
| Total active rules | 713 |
| DIRECT | 102 |
| REJECT | 566 |
| PROXY | 10 |
| OTHER | 35 |

注意：REJECT 风险审计中的“活跃 REJECT 规则数 302”是针对源规则审计口径；Release grouped rules 中的 566 是最终发布规则分组口径。二者口径不同，不是冲突。

## 6. 远程规则语法状态

| 项目 | 数量 |
|---|---:|
| 检查远程规则数 | 16 |
| 通过 | 16 |
| 警告 | 0 |
| 失败 | 0 |
| 自动规范化文件数 | 0 |

结论：当前远程规则没有 Shadowrocket / Surge 红叉级别的语法故障。新增远程源前仍必须确认是真实兼容的 `RULE-SET` 或 `DOMAIN-SET` 格式。

## 7. 脚本状态

| 项目 | 数量 |
|---|---:|
| 脚本入口总数 | 46 |
| 识别到的 App / 服务方向 | 16 |
| 重复脚本名 | 0 |
| 多入口共用同一 script-path | 0 |
| 必须独立保留 | 9 |
| 可合并候选 | 8 |
| 可改规则候选 | 5 |
| 需要人工复核 | 24 |

### 脚本来源分布

| 来源 | 数量 |
|---|---:|
| zirawell R-Store | 21 |
| raw.perzikkop.com | 12 |
| app2smile | 5 |
| fmz200 wool_scripts | 4 |
| local | 2 |
| raw.githubusercontent.com | 1 |
| Maasea | 1 |

### 脚本文件分布

| 文件 | 脚本数 |
|---|---:|
| `Scripts/app-clean.conf` | 28 |
| `Scripts/qingrex-miniapp-app-ad.conf` | 12 |
| `Scripts/spotify.conf` | 2 |
| `Scripts/app-cleaner-active.conf` | 1 |
| `Scripts/app2smile-qqnews-stable-plus.conf` | 1 |
| `Scripts/youtube.conf` | 1 |
| `Scripts/zhihu-enhance.conf` | 1 |

结论：脚本层没有命名重复和路径复用冲突。主要风险不是语法，而是 24 个入口需要人工复核；这些通常涉及大型 JSON、Body Rewrite、请求体或深层结构处理。

## 8. 独立 App 模块输出

| 项目 | 数量 |
|---|---:|
| 手动配置模块 | 18 |
| 自动发现模块 | 10 |
| 自动发现且成功生成 | 9 |
| 总模块规格 | 28 |
| 实际生成模块 | 27 |
| 跳过空模块 | 1 |

跳过项：`_TEMPLATE`，这是模板源，不是实际 App 模块，跳过正常。

### 27 个已生成模块

| 模块 | 来源 | 主要覆盖 |
|---|---|---|
| Spotify | manual | Rule, Header Rewrite, Script, MITM |
| YouTube | manual | Map Local, Script, MITM |
| Zhihu | manual | Rule, URL Rewrite, Body Rewrite, Script, MITM |
| Bilibili | manual | Rule, URL Rewrite, Body Rewrite, Map Local, MITM |
| RedNote / 小红书 | manual | Rule, URL Rewrite, Script, MITM |
| WeChat | manual | Rule, URL Rewrite, Map Local, MITM |
| QQ News | manual | URL Rewrite, Body Rewrite, Script, MITM |
| Weibo | manual | URL Rewrite, Body Rewrite, Script, MITM |
| Pinduoduo | manual | Rule, MITM |
| JD | manual | Rule, MITM |
| Taobao | manual | Rule, MITM |
| Netease Music | manual | Rule, MITM |
| MGTV | manual | Rule, MITM |
| Huya | manual | Rule, MITM |
| Yiche | manual | Rule, MITM |
| PCAuto | manual | Rule, MITM |
| Umetrip | manual | Rule, MITM |
| Xiaopeng | manual | Rule, MITM |
| Amap | auto | Rule, URL Rewrite, MITM |
| Baidu | auto | Rule, URL Rewrite, MITM |
| Meituan | auto | Rule, URL Rewrite, MITM |
| Quark | auto | Rule, MITM |
| Soul | auto | Rule, URL Rewrite, MITM |
| WPS | auto | Rule, URL Rewrite, MITM |
| Youku | auto | Rule, MITM |
| ZDM | auto | Rule, URL Rewrite, MITM |
| Zuoyebang | auto | Rule, URL Rewrite, MITM |

说明：`Release/Modules/` 是诊断和便利用途，不是多版本路线。公开入口仍是单一融合模块 `Ronghemokuai.sgmodule`。

## 9. App 覆盖范围

### 重点专项覆盖

- Spotify：Header Rewrite, MITM, Remote Rule, Rule, Script。
- YouTube：MITM, Remote Rule, Rule, Script。
- 知乎：Body Rewrite, MITM, Remote Rule, Rule, Script, URL Rewrite。

### 明确覆盖

- Bilibili
- 微博
- 百度贴吧
- 小红书
- 酷安
- 淘宝
- 闲鱼
- 拼多多
- 美团
- 饿了么
- 滴滴
- 12306
- 高德地图
- 喜马拉雅
- 小宇宙
- 斗鱼
- Reddit

### 局部覆盖

- 京东
- 大众点评
- 百度地图
- 网易云音乐

### App 状态矩阵中已有“用户确认通过”的项目

以下来自 `reports/manual_test_log.md / 用户确认`，不是助手亲测：

- Spotify
- YouTube
- 知乎
- Bilibili
- 淘宝
- 京东
- 拼多多
- 美团
- 大众点评
- 饿了么
- 微信
- 支付宝
- 银行 / 验证码
- 图片 CDN
- 小程序资源
- 闲鱼
- 喜马拉雅
- 滴滴
- 斗鱼

### 覆盖存在但仍标记未测 / 待复测的项目

- 微博
- 百度贴吧
- 小红书
- 酷安
- 12306
- 高德地图
- 百度地图
- 网易云音乐
- 小宇宙
- Reddit

这些不能写成“真实通过”。后续必须做真机测试并记录到 `reports/manual_test_log.md`。

## 10. REJECT 风险审计

| 风险项 | 数量 |
|---|---:|
| 源侧活跃 REJECT 规则数 | 302 |
| 明确广告域 | 72 |
| 图片 / CDN 风险 | 9 |
| HTTPDNS 风险 | 14 |
| 微信 / 支付 / 银行风险 | 4 |
| 国内核心 API 风险 | 27 |
| 不确定规则 | 184 |
| 需要人工复核总数 | 238 |

结论：当前没有静态阻断级故障，但 REJECT 层仍有大量需要人工复核的风险项。尤其是 CDN、HTTPDNS、微信、支付、银行和国内核心 API，不建议继续扩大 REJECT，应该优先走保护规则和真机验证。

## 11. 当前保护层

当前融合 profile 已优先加载：

- `Rules/protect-login.list`
- `Rules/protect-payment.list`
- `Rules/protect-video.list`
- `Rules/protect-cdn.list`

作用：在融合模块内先保护登录、支付、视频播放和静态资源链路，再执行清理和拦截规则。

## 12. 当前风险结论

| 类型 | 结论 |
|---|---|
| 语法错误 | 未发现 |
| 远程规则红叉风险 | 未发现 |
| 重复脚本名 | 未发现 |
| 重复 MITM hostname | 未发现 |
| 构建结构问题 | 未发现 |
| 高风险脚本 | 存在，需要人工复核 |
| 高风险 REJECT | 存在，需要人工复核 |
| App 真机覆盖 | 部分已由用户确认，部分仍未测 |

## 13. 建议处理顺序

1. 保持当前单一融合模块策略，不拆多版本。
2. 不要继续盲目增加 REJECT 源。
3. 先处理 `REJECT 风险审计报告` 中的 HTTPDNS、CDN、支付、银行、核心 API 风险项。
4. 对 24 个需要人工复核的脚本逐项建立测试记录。
5. 对未测 App 按优先级复测：微博、小红书、百度贴吧、12306、高德、百度地图、网易云音乐、小宇宙、Reddit。
6. 每次规则变更后运行：

```bash
python Rewrite/Generator/Builder.py --profile fusion --release --check
```

7. 每次真实测试后更新：

```text
reports/manual_test_log.md
```

## 14. 最终判定

当前仓库模块可以判定为“静态检查正常、构建正常、覆盖完整度较高、但仍有高风险项需要人工验证”。

可以继续正常使用和维护；不要把“覆盖存在”误写成“真机通过”。
