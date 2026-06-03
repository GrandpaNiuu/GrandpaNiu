# Stable Plus 晋级 PR 报告

生成时间：2026-06-03 11:18:37 +0800

本报告只准备单项 App 晋级审查材料，不会自动合并 PR，也不允许把 Stable Plus 整体合并进 Stable。

## 当前结论

- App 名称：未指定
- Stable Plus 状态：允许单项晋级流程
- 晋级判定：允许单项晋级流程
- 测试记录链接：`reports/manual_test_log.md`
- 测试证据：Stable 第一轮已由用户确认通过；Stable Plus 仍需按 App 单项测试和 PR 审查
- 微信广告规则仍仅 Stable Plus：是
- 整体合并限制：不允许 Stable Plus 整体合并进 Stable
- 单项要求：每个 App 仍需单项测试记录、风险说明和 PR 审查

## PR 必填信息

- App 名称：未指定
- 从哪个 profile 晋级：stable-plus -> stable
- 新增 / 移动的 hostname：未自动识别，需人工填写
- 新增 / 移动的 rule：需人工确认
- 新增 / 移动的 script：无自动移动，脚本必须单独审查
- 新增 / 移动的 Rewrite：需人工确认具体源文件
- 影响范围：未自动发现敏感关键词，仍需人工确认登录 / 支付 / 验证码 / 图片 / 小程序
- 是否涉及登录 / 支付 / 验证码 / 银行 / 图片 / 小程序：未自动发现敏感关键词，仍需人工确认登录 / 支付 / 验证码 / 图片 / 小程序
- 回滚步骤：回滚对应 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Profiles/` 源头文件后重新运行构建与校验

## 门禁

- 没有 `manual_test_log.md` 真实通过记录时，不允许生成 `stable-ready`。
- 没有真实测试记录时，只能写 `manual-review`。
- Stable 第一轮通过只代表默认 Stable 本轮可用，不代表 Stable Plus 可以整体进入 Stable。
- 不允许 Stable Plus 整体合并进 Stable。
- 只能单项 App 晋级。
- 每个 App 都需要单项测试记录和 PR 审查。
- PR 默认不自动 merge。

## 自动识别信息

- Profile 命中：未识别
- Stable Plus hostname 命中数：0
