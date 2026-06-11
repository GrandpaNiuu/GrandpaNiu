# 功能覆盖清单

本清单记录 Fusion 模块当前覆盖对象、覆盖方式和维护边界。实际生效范围由 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Remotes/sources.json` 与 `Rewrite/Profiles/fusion.conf` 共同决定。

## 覆盖强度

| 状态 | 含义 |
|---|---|
| 重点专项 | 有专门脚本、MITM、白名单或保护逻辑 |
| 明确覆盖 | 有 Script、Body Rewrite、Map Local 或明确本地规则 |
| 局部覆盖 | 只有部分接口、域名或远程规则命中 |
| 高风险保守 | 涉及登录、支付、验证码、图片/CDN 或核心 API，只允许小范围处理 |

## 重点专项

| App / 服务 | 覆盖方式 | 作用 | 备注 |
|---|---|---|---|
| Spotify | DIRECT、Header Rewrite、Script、MITM | 减少广告响应与异常缓存影响 | 不改账号、订阅、权限状态 |
| YouTube | DIRECT、Script、Map Local、MITM | 响应清理和局部广告接口处理 | 需复测播放、搜索、评论、Shorts |
| 知乎 | Script、Body Rewrite、URL Rewrite、MITM | 清理信息流、回答页、推广字段 | 不处理会员、付费、登录状态 |
| Bilibili | Rule、URL Rewrite、Body Rewrite、Map Local、MITM | 搜索、活动、广告素材等局部净化 | 不引入会员破解或支付绕过 |

## App 类别覆盖

| 类别 | 代表对象 | 覆盖说明 |
|---|---|---|
| 视频音乐 | Bilibili、YouTube、Spotify、芒果 TV、网易云音乐、喜马拉雅、小宇宙、斗鱼、虎牙 | 主要处理广告接口、开屏、活动入口、推荐位和部分响应字段 |
| 内容社区 | 知乎、微博、小红书、贴吧、酷安、Reddit、小黑盒、脉脉 | 主要处理信息流广告、详情页推广、弹窗和商业字段 |
| 电商消费 | 淘宝、闲鱼、京东、拼多多、什么值得买、转转、盒马、菜鸟 | 只处理广告和活动入口，商品图、购物车、订单页保持保守 |
| 本地生活 | 美团、大众点评、饿了么、瑞幸、麦当劳、星巴克、便利店类 App | 只处理广告、活动卡片和弹窗，下单前置和支付链路不做绕过 |
| 地图出行 | 高德地图、百度地图、滴滴、航旅纵横、12306、航空类 App | 只处理广告入口和活动位，定位、路线、票务、订单链路需保守 |
| 工具办公 | WPS、有道、360 摄像机、萤石、配音秀、输入法类 App | 主要处理首页推广、配置广告字段和弹窗 |
| 微信相关 | 微信广告域、广点通广告域 | 不覆盖微信图片、小程序、支付、登录、公众号核心资源 |

## 远程规则源

远程规则源由 `Rewrite/Remotes/sources.json` 管理，构建时写入 `[Rule]`。当前规则源主要用于：

- 通用广告域名。
- 常见广告 SDK。
- 隐私追踪。
- 劫持域名。
- 网页广告与程序化广告。

远程源必须满足：

- 使用 `https://`。
- 不使用短链、代理镜像或不可信中转。
- 语法通过 `scripts/validate_remote_rule_syntax.py`。
- 失效源由 `scripts/audit_repair_invalid_sources.py` 记录、禁用或等待替换。

## 重复项策略

| 重复类型 | 处理方式 |
|---|---|
| 最终 Fusion 模块重复 active line | 阻断验证 |
| 重复 script name | 阻断验证 |
| 重复 MITM hostname | 阻断验证 |
| 同一规则文件内部重复 entry | 阻断验证 |
| 不同规则包之间存在交集 | 允许保留，最终 Fusion 构建时自动去重 |

跨文件交集不直接删除，因为 Android 输出、单 App 规则包和兼容包可能需要独立保留相同规则。

## 不建议加入

以下对象默认不加入拦截或脚本处理：

```text
银行 App
支付接口
验证码接口
证书校验接口
登录态接口
Cookie / Token / Authorization
会员权益与付费内容
微信图片 / 小程序 / 支付 / 登录核心域
地图定位与路线核心接口
订单、票务、下单前置核心接口
```

## 报告入口

| 报告 | 用途 |
|---|---|
| `reports/module_integrity_report.md` | Fusion 输出结构、重复项和规则源完整性 |
| `reports/profile_validation_report.md` | Fusion profile 构建状态、脚本数、MITM 数 |
| `reports/remote_rule_syntax_report.md` | 远程规则源语法与可用性 |
| `reports/invalid_sources_report.md` | 失效源审核与自动修复结果 |
| `reports/app_coverage_matrix.md` | App 覆盖矩阵 |
| `reports/rule_traceability_matrix.md` | 高风险规则来源、风险和回滚路径 |

## 结论口径

- “已纳入覆盖”：仓库存在对应规则、脚本、Rewrite 或 MITM。
- “语法通过”：本地构建和静态验证通过。
- “远程源可用”：远程源在本次 `validate_remote_rule_syntax.py` 检查中可拉取并解析。
- “真机通过”：必须有人工测试记录或明确用户反馈，不能由静态扫描自动推断。
