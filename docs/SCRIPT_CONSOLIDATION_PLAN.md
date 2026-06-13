# 脚本瘦身计划

本计划的目标是减少脚本入口数量，但不减少功能覆盖。当前阶段只做分析和规划，不删除、不合并、不禁用任何脚本。

## 核心原则

1. 少脚本不等于少功能。
2. 先分析，再灰度，再合并，最后才移除旧入口。
3. Spotify、YouTube、知乎等复杂专项脚本不参与第一阶段合并。
4. 登录、支付、验证码、会员、权益相关逻辑不允许进入通用清理器。
5. 能用 Rule / URL Rewrite 解决的静态广告接口，优先从脚本迁移到规则层。
6. 每次瘦身后必须重新生成四个 Release 版本，并更新测试记录。

## 不删除脚本的当前阶段

当前阶段只新增：

- `scripts/generate_script_inventory_report.py`
- `reports/script_inventory_report.md`
- `docs/SCRIPT_CONSOLIDATION_PLAN.md`

不做以下操作：

- 不删除任何 `Scripts/*.conf` 入口。
- 不删除任何远程 `script-path`。
- 不修改默认 `stable` 功能。
- 不自动合并脚本。
- 不把测试版内容自动晋级到正式版。

## 分析分类

脚本清单报告会把脚本分为四类：

| 分类 | 含义 | 当前策略 |
|---|---|---|
| 必须独立保留 | Spotify、YouTube、知乎、protobuf、复杂业务或安全边界相关 | 不合并 |
| 可合并候选 | 普通 App JSON 去广告、弹窗、信息流、推荐位清理 | 先进入灰度计划 |
| 可改规则候选 | 不依赖 body 的广告接口、开屏素材、统计接口 | 评估迁移到 Rule / URL Rewrite |
| 需要人工复核 | 静态分析无法判断的脚本 | 人工看脚本内容和自动化验证 |

## 第一阶段：清单和重复分析

目标：只建立可视化清单，不动功能。

动作：

1. 生成 `reports/script_inventory_report.md`。
2. 统计脚本总数、来源、匹配 App、是否 requires-body、是否 binary-body。
3. 找出重复脚本名。
4. 找出多个入口共用同一个 `script-path` 的情况。
5. 标记可合并候选和可规则化候选。

验收标准：

- `validate_repository.py` 通过。
- `Repository Health Check` 成功。
- 不产生 Root / Release diff。
- 四个 Release 版本仍存在。

## 第二阶段：设计统一 app-cleaner

目标：先设计，不替换。

建议新增：

```text
Scripts/app-cleaner.js
Scripts/app-cleaner.config.json
```

设计方向：

```text
URL pattern -> App key -> cleaner function -> safe field removal -> output body
```

要求：

- 所有 cleaner 必须是白名单逻辑。
- 默认不处理未知接口。
- 出错时返回原 body，不强行写空。
- 记录命中 App、处理函数、删除字段数量。
- 禁止处理登录、支付、验证码、会员权益字段。

## 第三阶段：Stable Plus 灰度

目标：只在 `stable-plus` 中试运行统一清理器。

做法：

1. 在 `stable-plus` profile 中增加新统一脚本入口。
2. 保留旧脚本入口，不立即删除。
3. 用报告对比旧入口和新入口覆盖范围。
4. 自动化验证 Stable Plus。

不得直接改：

- `stable` 默认正式版。
- Spotify / YouTube / 知乎核心脚本。
- 支付、登录、验证码、银行相关逻辑。

## 第四阶段：逐项替换旧入口

目标：一类 App 一类 App 替换，不整体替换。

替换路径：

```text
旧单脚本入口
-> stable-plus 新 app-cleaner 并行测试
-> 自动化验证通过
-> 删除 stable-plus 旧入口
-> 观察一段时间
-> 单项进入 stable
```

每次最多处理一个 App 组，例如：

- 贴吧 / QQ 新闻 / VGTime
- 普通 R-Store AntiAd JSON 清理类
- 电商弹窗类
- 内容资讯推荐位类
- 出行首页广告类

## 第五阶段：规则化迁移

适合迁移到规则层的类型：

- 纯广告域名。
- 纯开屏素材域名。
- 统计和埋点接口。
- 不需要读取 body 的 request/response 入口。

迁移目标：

```text
Rules/reject.list
Rules/app-clean.list
Rules/web-ads.list
Rewrite/Sources/URL-Rewrite.conf
```

规则化后必须确认：

- 不误杀登录。
- 不误杀验证码。
- 不误杀支付前置。
- 不误杀订单页。

## 禁止合并范围

以下脚本和逻辑不得进入通用清理器：

- Spotify 播放链路。
- YouTube Enhance。
- 知乎增强安全边界。
- protobuf / binary body 处理。
- 会员权益、登录、支付、验证码、银行相关接口。
- 任何无法解释用途的混淆脚本。

## 推荐目标

不追求一步降到极低数量。建议分阶段目标：

| 阶段 | 目标 |
|---|---:|
| 当前 | 建立脚本清单，不删除 |
| 第一轮灰度 | 104 -> 80 左右 |
| 第二轮灰度 | 80 -> 60 左右 |
| 长期目标 | 50-70 个稳定入口 |

Lite 继续保持低数量；Full 可以保留更多入口用于排查，不强制压缩。

## 每次瘦身后的验证命令

```bash
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/validate_profiles.py
python3 scripts/repository_health_check.py
```

## 测试要求

每次减少脚本后，至少测试：

- Spotify：播放、切歌、搜索。
- YouTube：首页、播放、Shorts、评论。
- 知乎：首页、回答页、评论。
- Bilibili：首页、播放、评论。
- 淘宝 / 京东 / 拼多多：详情、购物车、订单页。
- 微信 / 支付宝 / 银行 App：登录、验证码、支付前置。

没有真实测试，不得写“功能不减少”。
