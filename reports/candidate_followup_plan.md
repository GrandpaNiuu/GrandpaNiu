# 候选源后续处理计划

本计划基于 `Rewrite/Remotes/candidates.json` 和 `reports/candidate_security_score_report.md`，用于约束候选源后续处理。候选源不得无审核进入默认 Stable。

## 分类处理规则

| 分类 | 允许动作 | 禁止动作 | 后续要求 |
|---|---|---|---|
| safe-rule-candidate | 进入 pending 或 Stable Plus 测试流程 | 直接进入 Stable | 构建验证、误伤审计、人工复核 |
| stable-plus-only | 只进入 Stable Plus 测试 | 整体合并 Stable | 单项测试通过后再考虑晋级 |
| manual-review | 保持 disabled / pending | 自动启用 | 人工阅读用途、风险和许可 |
| blocked | 不启用 | 进入任何模块 | 记录阻断原因 |
| reference-only | 只作参考 | 拉取远程模块进默认模块 | 只提取可解释、可回滚的局部思路 |
| failed / 404 | 连续确认后处理 | 单日失败即删除 | 优先同源替换，其次注释，最后删除 |

## 当前候选方向

| 候选类型 | 代表项 | 当前建议 | 说明 |
|---|---|---|---|
| 可信规则源 | blackmatrix7 Advertising Lite / Hijacking / Privacy | 可进入候选或测试流程 | 仍需误伤审计，不得无审核进入 Stable |
| 可信规则源 | ACL4SSR BanProgramAD / BanEasyListChina | 可进入候选或测试流程 | 先做规则格式、重复和误伤检查 |
| 暂停或失败规则源 | blackmatrix7 Privacy Lite | manual-review | 已出现失败记录时，不自动恢复启用 |
| 参考规则源 | Loyalsoldier reject domain set / Cats-Team AdRules DNS list | manual-review | 域名集风险较高，需分批复核 |
| 脚本候选 | app2smile Tieba script | 保持 pending | 脚本默认风险高，需人工审查源码和行为 |
| 参考模块 | Maasea YouTube Enhance reference | reference-only | 只作参考，不直接接入远程模块 |

## 候选进入流程

```text
候选登记
-> 安全评分
-> 规则 / 脚本 / reference 分类
-> 重复检查
-> 误伤风险审计
-> Stable Plus 或 pending
-> 人工测试
-> 单项晋级审查
-> Stable
```

## 审查标准

候选必须满足：

- 来源清楚。
- URL 可读、非短链、非镜像、非 ghproxy。
- 不涉及登录、支付、验证码、银行、Cookie、Token、会员权益。
- 有回滚路径。
- 通过构建和验证。
- 不扩大 Stable 的高风险 MITM。

## 脚本候选额外要求

脚本候选默认 disabled / pending。只有满足以下条件才允许进一步测试：

1. 源码可读，未混淆。
2. 不改 request body。
3. 不访问或写入 Cookie / Token / 账号状态。
4. 不涉及会员权益、支付、登录、验证码。
5. 有单项 App 测试计划。
6. 有回滚路径。

## 失败源处理策略

- 单日失败：只记录。
- 连续失败：复核是否临时网络问题。
- 确认 404 / 410 / 文件不存在：优先同源替换。
- 无替代源：注释并记录原因。
- 低风险独立远程规则才允许最终删除。

## 禁止事项

- 不使用全网随机搜索结果直接进候选。
- 不拉取未知远程模块作为默认模块。
- 不把脚本候选直接写入 Stable。
- 不把 reference-only 当成启用源。
