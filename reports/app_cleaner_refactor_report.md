# App Cleaner 语法重构报告

## 本次重构目标

将 `Scripts/app-cleaner.js` 从连续 `if / return` 分发结构，改为 registry / dispatcher 架构。

本次重构只改写脚本组织方式，不新增风险脚本，不删除未承接旧功能，不改变已融合批次的功能边界。

## 当前架构

`app-cleaner.js` 现在分为：

- 通用工具函数。
- URL matcher 函数。
- App 专项 cleaner 函数。
- `RAW_CLEANERS` 注册表。
- `JSON_CLEANERS` 注册表。
- `findCleaner()` dispatcher。
- `main()` 统一入口。

## RAW_CLEANERS

用于不一定是标准 JSON 结构、需要直接处理 response body 字符串的场景。

当前包含：

| key | batch | 说明 |
|---|---|---|
| `zsgj` | batch-3 | 掌上公交 raw body 文本替换 |

## JSON_CLEANERS

用于标准 JSON response body 的清理。

当前包含：

| key | batch | 说明 |
|---|---|---|
| `qq-news` | batch-1 | QQ News |
| `vgtime` | batch-1 | VGTime |
| `sqkb` | batch-2 | 省钱快报 |
| `163news` | batch-2 | 网易新闻 |
| `xiaoheihe` | batch-2 | 小黑盒 |
| `manner` | batch-2 | Manner |
| `chaoge` | batch-2 | 超格教育 |
| `smzdm` | batch-3 | 什么值得买 |
| `taobao` | batch-3 | 淘宝 poplayer |
| `juneyaoair` | batch-3 | 吉祥航空 |
| `ddxq` | batch-3 | 叮咚买菜 |
| `kkmh` | batch-4 | 快看漫画 |
| `goofish` | batch-4 | 闲鱼 |
| `xmly` | batch-4 | 喜马拉雅 |
| `didi` | batch-4 | 滴滴 |
| `generic-json-ad-fields` | batch-5 | 通用低风险 JSON 广告字段清理 |

## 调度顺序

1. 读取 URL 和 body。
2. 先匹配 `RAW_CLEANERS`。
3. raw cleaner 命中后直接处理 body 字符串。
4. 未命中 raw cleaner 时尝试 JSON parse。
5. JSON parse 失败则原样返回。
6. JSON parse 成功后匹配 `JSON_CLEANERS`。
7. 专项 cleaner 优先，Batch 5 通用 cleaner 放最后。
8. 未命中任何 cleaner 时原样返回。

## 安全边界

本次重构保持以下边界：

- 未匹配 URL 原样返回。
- body 为空原样返回。
- JSON 解析失败原样返回。
- cleaner 执行异常时原样返回。
- Batch 5 通用清理器仍放在最后，避免覆盖专项 cleaner。
- 不处理登录、支付、验证码、银行、会员权益、Cookie、Token、protobuf、binary-body、加密 body。

## 对脚本数量的影响

本次重构本身不会直接把脚本数量降到 20。它的作用是让后续继续融合时不再靠堆叠 `if` 语句，而是通过注册表增加或移除 cleaner。

向 20 左右推进的正确路径：

```text
registry / dispatcher 架构
-> 继续识别低风险 JSON cleaner
-> 扩展注册表
-> 迁移旧入口
-> node --check
-> build / validate / profile validation
-> 真机测试
```

## 20 左右目标判断

脚本数量降到 20 左右是长期目标，不应通过删除未承接功能实现。合理方式是：

- 普通 JSON 字段清理类继续进入 `app-cleaner.js`。
- 纯域名或静态广告迁移到规则层。
- 复杂脚本保持独立。
- 复杂脚本如果要融合，必须先拆分功能、写清 matcher、建立回滚。

不建议合并到 `app-cleaner.js` 的类型：

- 登录、支付、验证码、银行相关。
- 会员权益、破解、绕过类。
- Cookie / Token / BoxJS 依赖。
- request body 改写。
- protobuf / binary-body。
- 混淆、加密、强状态缓存脚本。

## 验证要求

GitHub Actions 必须继续执行：

```bash
node --check Scripts/app-cleaner.js
```

并继续执行：

```bash
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/validate_profiles.py
```

## 当前结论

本次完成的是结构性重构，不是新一轮功能扩张。下一步可以在此架构上继续大批量融合，但必须遵守功能承接、语法检查、构建验证和回滚报告四个条件。
