# Stable Plus 晋级 PR 报告

生成时间：2026-06-01 03:17:03 +0800

本报告只准备单项 App 晋级审查材料，不会自动合并 PR，不会把 Stable Plus 整体合并进 Stable。

## 当前结论

- App 名称：未指定
- 晋级判定：manual-review
- 测试记录链接：`reports/manual_test_log.md`
- 测试证据：没有 `manual_test_log.md` 真实通过记录
- 微信广告规则仍仅 Stable Plus：是

## PR 必填信息

- App 名称：未指定
- 从哪个 profile 晋级：stable-plus -> stable
- 新增 / 移动的 hostname：未自动识别，需人工填写
- 新增 / 移动的 rule：需人工确认
- 新增 / 移动的 script：无自动移动，脚本必须单独审查
- 新增 / 移动的 Rewrite：需人工确认具体源文件
- 影响范围：未发现敏感关键词，仍需人工确认登录 / 支付 / 验证码 / 图片 / 小程序
- 是否涉及登录 / 支付 / 验证码 / 银行 / 图片 / 小程序：未发现敏感关键词，仍需人工确认登录 / 支付 / 验证码 / 图片 / 小程序
- 回滚步骤：回滚对应 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Profiles/` 源头文件后重新运行构建与校验

## 门禁

- 没有 `manual_test_log.md` 真实通过记录，不允许生成 `stable-ready`。
- 没有真实测试记录，只能写 `manual-review`。
- 不允许 Stable Plus 整体合并进 Stable。
- 只能单项 App 晋级。
- PR 默认不自动 merge。

## 自动识别信息

- Profile 命中：未识别
- Stable Plus hostname 命中数：0
