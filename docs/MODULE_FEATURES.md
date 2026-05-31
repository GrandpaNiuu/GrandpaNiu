# 模块版本功能与 App 覆盖说明

本文件说明 `Stable`、`Stable Plus`、`Lite`、`Full` 四个 Shadowrocket 独立模块分别包含什么能力、覆盖哪些 App 方向，以及哪些内容只是测试覆盖。

## 使用原则

- 日常只启用一个版本，不要同时启用多个版本。
- 默认长期使用 `Stable`。
- 想测试更多 App 覆盖时使用 `Stable Plus`。
- 手机发热、耗电或 App 异常时使用 `Lite`。
- `Full` 只用于查漏拦和排查问题，不建议长期启用。
- 覆盖说明来自当前规则、脚本、Rewrite、MITM 和静态扫描结果，不等于所有广告场景都已人工测试通过。
- 实际脚本数、MITM 数和构建状态以 `reports/profile_validation_report.md` 为准。

## 版本总览

| 版本 | 文件 | 定位 | 是否默认发布 | 覆盖策略 | 建议用途 |
|---|---|---|---|---|---|
| Stable | `Release/Ronghemokuai-stable.sgmodule` | 默认正式版 | 是 | 核心专项 + 常用 App 净化 + 低风险融合脚本 | 日常长期使用 |
| Stable Plus | `Release/Ronghemokuai-stable-plus.sgmodule` | 常用 App 增强测试版 | 否 | Stable + 常用 App 增强 MITM 覆盖 | 测试更多常用 App 去广告 |
| Lite | `Release/Ronghemokuai-lite.sgmodule` | 低耗电参考版 | 否 | 只保留核心链路 | 低风险、省电、异常排查 |
| Full | `Release/Ronghemokuai-full.sgmodule` | 全量排查测试版 | 否 | Stable + Stable Plus + extended MITM | 查漏拦、定位缺失 hostname |

## Stable：默认正式版

Stable 是默认发布版本，目标是长期稳定，而不是最大覆盖。

### 功能方向

- 通用广告拦截。
- 开屏广告、弹窗、横幅、信息流、推荐位、活动卡片清理。
- Spotify 播放链路保护。
- YouTube Enhance 保留。
- 知乎增强净化。
- 常用 App 和网页广告净化。
- 低风险 JSON 清理脚本融合：通过 `Scripts/app-cleaner.js` 承接多个普通广告字段清理入口，减少重复脚本入口。
- 可信远程规则源维护。

### 重点覆盖 App / 服务

| 类别 | App / 服务方向 | 覆盖说明 |
|---|---|---|
| 核心专项 | Spotify | 播放链路、脚本、直连保护、相关 MITM |
| 核心专项 | YouTube | YouTube Enhance、播放相关 MITM、Map Local、规则保护 |
| 核心专项 | 知乎 | 首页、回答页、推荐流、广告接口、增强净化脚本 |
| 视频社区 | Bilibili、斗鱼、咪咕视频、VGTime、快看漫画 | App 广告、接口净化、部分 Rewrite / MITM |
| 电商购物 | 淘宝、闲鱼、京东、拼多多、什么值得买、转转、飞猪、菜鸟 | 首页、搜索、商品详情、推荐位、弹窗、活动卡片清理方向 |
| 本地生活 | 美团、大众点评、饿了么、叮咚买菜、朴朴、罗森、Manner、企迈 | 首页、搜索、店铺页、活动卡片、下单前置页相关清理方向 |
| 内容社区 | 小红书、微博、贴吧、Reddit、酷安、小黑盒、皮皮虾、脉脉 | 信息流、推荐位、广告接口清理方向 |
| 音频内容 | 网易云音乐、喜马拉雅、小宇宙 | 首页、详情页、推荐位、广告接口清理方向 |
| 地图出行 | 高德地图、百度地图、滴滴、吉祥航空、掌上公交 | 首页、地图广告、活动入口、推荐位清理方向 |
| 工具办公 | 有道、51CTO、稿定设计、配音秀、usmile、萤石、360 摄像机 | 首页、推广、配置、广告字段清理方向 |
| 资讯阅读 | 网易新闻、财新、IT之家、起点、宝宝树、马蜂窝、飞客 | 热词、banner、弹窗、信息流广告字段清理方向 |

### 脚本融合边界

`Stable` 当前采用 `app-cleaner-active-json-clean` 统一入口承接低风险 JSON 清理类脚本。该入口遵循：

- 未匹配 URL 原样返回。
- body 为空原样返回。
- JSON 解析失败原样返回。
- 专项 App 使用独立函数处理。
- 通用批次只清理常见广告字段和明显广告数组项。
- 不处理登录、支付、验证码、银行、会员权益、protobuf、binary-body、加密 body。

## Stable Plus：常用 App 增强测试版

Stable Plus 在 Stable 基础上增加 `MITM-stable-plus.conf`。它不是默认发布版本，用于测试更多常用 App 覆盖。

### 额外覆盖 App / 服务

| 类别 | App / 服务方向 | 覆盖说明 |
|---|---|---|
| 视频娱乐 | 爱奇艺、AcFun、芒果 TV、咪咕视频、虎牙、快手 | 开屏、视频广告、推荐位、接口广告清理方向 |
| 电商消费 | 得物、唯品会、当当、转转、什么值得买、永辉 | 首页、搜索、商品页、推荐位、活动卡片清理方向 |
| 餐饮消费 | 瑞幸、麦当劳、星巴克 | 首页、活动卡片、弹窗、推荐位清理方向 |
| 出行旅游 | 携程、去哪儿、途家、途牛、航旅纵横、飞常准、南航、东航 | 首页、推荐位、活动卡片、广告接口清理方向 |
| 内容资讯 | 豆瓣、LOFTER、虎嗅、澎湃、华尔街见闻、人民 App、ZAKER | 信息流、广告接口、推荐位清理方向 |
| 招聘职场 | 猎聘、BOSS 直聘、51job、猪八戒 | 首页、推荐位、广告接口清理方向 |
| 学习办公 | 有道、WPS、金山文档、超星、粉笔 | 首页、弹窗、推荐位、广告接口清理方向 |
| 云盘工具 | 阿里云盘、天翼云盘、迅雷、向日葵 | 首页、弹窗、活动卡片、广告接口清理方向 |
| 汽车硬件 | 汽车之家、易车、比亚迪、小鹏、小牛、米家、Zepp、萤石、Petkit | 首页、设备页、推荐位、广告接口清理方向 |

### 晋级规则

Stable Plus 里的内容不会自动进入 Stable。正确路径是：

```text
Stable Plus 中测试
-> 确认登录 / 验证码 / 支付前置 / 核心流程正常
-> 单项 App 进入晋级候选
-> 人工确认后再进入 Stable
```

## Lite：低耗电参考版

Lite 只保留最核心的能力，适合省电、排查异常或低风险使用。

### 包含内容

- Spotify 核心脚本。
- YouTube 核心脚本。
- 知乎增强净化。
- 核心 MITM：Spotify / YouTube / 知乎相关 hostname。
- 基础规则和必要远程规则。

### 适合场景

- 手机发热。
- 电量消耗明显增加。
- 某些 App 登录或页面异常。
- 想先确认是不是 MITM 覆盖过大导致问题。

## Full：全量排查测试版

Full 包含完整 MITM 扩展层，不适合长期启用。

### 包含内容

- Stable 的全部内容。
- Stable Plus 的增强测试覆盖方向。
- 扩展 MITM 层 `MITM-extended.conf`。
- 完整 extended hostname。

### 适合场景

- 某个 App 在 Stable / Stable Plus 中仍有广告残留。
- 需要从 Full 中定位可能缺失的 hostname。
- 临时查漏拦。

### 不适合场景

- 日常长期使用。
- 登录、支付、验证码、银行 App 场景。
- 对耗电和稳定性敏感的设备。

## 覆盖状态说明

| 状态 | 含义 |
|---|---|
| 明确覆盖 | 仓库中存在对应 Rule / Rewrite / Script / MITM 关键词，具备清理方向 |
| 局部覆盖 | 只覆盖部分 hostname 或部分接口，不能保证完整净化 |
| 重点专项 | 作为核心功能重点维护 |
| 未测 | 没有真实人工测试记录，不得宣传为已验证通过 |

当前多数 App 仍属于“规则覆盖存在，但真机测试未完成”。真实测试结果应记录到 `reports/manual_test_log.md`。

## 自动化边界

仓库可以自动做：

- 构建 Stable / Stable Plus / Lite / Full 四个独立模块。
- 检查 Root 与 Release 是否一致。
- 检查 profile 是否能构建。
- 检查 `Scripts/app-cleaner.js` JavaScript 语法。
- 检查关键脚本、MITM、远程源和 README 链接。
- 生成覆盖矩阵、脚本清单、健康报告和回滚报告。

仓库不会自动做：

- 自动真机测试 App。
- 自动确认 YouTube / Spotify / 知乎实际可用。
- 自动确认淘宝 / 拼多多 / 京东订单页无异常。
- 自动确认微信 / 支付宝 / 银行 / 验证码流程无异常。
- 自动把 Stable Plus 或 Full 的内容晋级到 Stable。

## 单项加入或晋级表达模板

### 加入 Stable Plus 测试

```text
请把【App 名称】单项加入 Stable Plus 测试版，不要进入默认 Stable。优先从 MITM-extended.conf 查找相关 hostname，只加入广告、弹窗、信息流、推荐位相关域名，避开登录、支付、验证码、passport、token、cookie、security 相关域名。修改后重新生成四个 Release 版本并运行验证。
```

### 从 Stable Plus 晋级 Stable

```text
我已经测试【App 名称】在 Stable Plus 中正常，核心流程、登录、验证码、支付前置没有异常。请把该 App 相关 hostname 单项晋级到 Stable，不要合并整个 Stable Plus。修改后重新生成四个 Release 版本并运行验证。
```
