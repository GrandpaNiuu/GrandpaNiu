# Codex 执行标准

本文件定义 Codex 修改 GrandpaNiu 仓库时的强制边界。目标是让仓库保持可构建、可验证、可回滚，而不是盲目扩大规则、脚本或 MITM 覆盖。

## 总原则

1. **source-first**：先改 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Profiles/`、`Rewrite/Remotes/`，再构建 `Release/` 和根目录模块。
2. **Stable 保守**：默认正式版只保留低误伤、可长期使用、可回滚内容。
3. **Stable Plus 测试**：增强内容先进入 Stable Plus，不得整体合并进 Stable。
4. **Lite 排查省电**：Lite 用于低 MITM、低脚本、低风险定位。
5. **Full 只做全量排查**：Full 不适合长期启用，不得作为默认发布目标。
6. **敏感链路默认保护**：登录、支付、验证码、银行、微信、支付宝、Cookie、Token、会员权益、账号状态默认不拦截、不改写。
7. **一个 PR 只处理一个风险单元**：一个 App、一类 CDN、一组 HTTPDNS、一个低风险脚本融合项，或一批同源低风险广告域。

## 任务分级

| 级别 | 任务类型 | 允许修改 | 禁止修改 | 验收重点 |
|---|---|---|---|---|
| P0 | 构建失败、验证失败、报告阻断、Root/Release 不一致 | 构建脚本、验证脚本、报告生成脚本、对应源头文件 | 扩大 Stable MITM、批量删除 REJECT、启用未知脚本 | `validate_repository.py` 通过，blocking stale 为 0 |
| P1 | 治理文档、报告闭环、workflow 状态、人工测试计划 | `docs/`、`reports/`、报告生成脚本、README 入口 | 修改广告规则语义、扩大 hostname、伪造人工测试 | 文档一致，报告可追溯 |
| P2 | 单项 App 修复、Stable Plus 测试、候选源评估 | 单个 App 对应源头、Stable Plus 或 pending 配置、审计报告 | 整体合并 Stable Plus/Full，批量迁移 MITM | 单项可回滚，有测试计划 |
| P3 | 脚本瘦身、低风险规则优化、性能优化 | 单个低风险 JSON cleaner、单条规则、单个候选源 | request-body/protobuf/binary-body 脚本硬合并 | `node --check` 通过，回滚路径明确 |

## 文件修改边界

### 可以直接修改

- `docs/*.md`
- `reports/*.md`
- `scripts/*report*.py`
- `scripts/validate_repository.py`
- `scripts/repository_health_check.py`
- `scripts/check_report_freshness.py`
- `scripts/generate_workflow_health_report.py`
- `README.md`

### 需要特别谨慎

- `Rules/reject.list`
- `Rules/direct.list`
- `Rules/wechat-ad.list`
- `Scripts/app-cleaner.js`
- `Scripts/app-cleaner-active.conf`
- `Rewrite/Sources/MITM-*.conf`
- `Rewrite/Profiles/*.conf`
- `Rewrite/Remotes/sources.json`
- `Rewrite/Remotes/candidates.json`

### 默认禁止

- 批量删除 REJECT。
- 批量扩大 Stable MITM。
- 把 Full 或 Stable Plus 整体合并进 Stable。
- 启用未知、混淆、request-body、Cookie、Token、会员权益脚本。
- 手改 `Ronghemokuai.sgmodule` 但不改源头。
- 没有真实测试却把 `manual_test_log.md` 或 `app_status_matrix.md` 写成通过。
- 在一个 PR 中同时处理多个无关风险单元。

## Stable 准入标准

任何规则、脚本或 MITM 进入 Stable，必须同时满足：

1. 来源明确。
2. 风险分类明确。
3. 不涉及登录、支付、验证码、银行、Cookie、Token、会员权益。
4. 不影响图片 CDN、核心 API、HTTPDNS。
5. 已在 Stable Plus 或真实本地环境确认关键流程正常。
6. `reports/rule_traceability_matrix.md` 中存在对应记录或风险说明。
7. 每条高风险规则有明确 `rollback_path`。
8. `validate_repository.py` 通过。
9. `repository_health_check.py` 阻断问题为 0。

不满足以上条件时，只能进入 Stable Plus、Full、pending 或 manual-review，不能进入 Stable。

## 高风险 rollback_path 要求

每条高风险规则必须能回答：

| 字段 | 要求 |
|---|---|
| 修改文件 | 指出具体源头文件，例如 `Rules/reject.list` 或 `Rewrite/Sources/MITM-stable-plus.conf` |
| 影响版本 | stable / stable-plus / lite / full |
| 影响 App / 服务 | 指出可能受影响的 App 或服务 |
| 回滚动作 | 删除、恢复、移出 profile、补 DIRECT 或恢复旧脚本入口 |
| 重建命令 | 至少包含 build stable、sync root、build release variants、validate_repository |
| 复测范围 | 首页、图片、登录、支付前置、验证码、小程序、评论、搜索等 |

没有 rollback_path 的高风险项不得合并。

## 必跑命令

每次治理或源头变更后至少运行：

```bash
python3 -m py_compile \
  scripts/build_module.py \
  scripts/build_release_variants.py \
  scripts/factory_finalize.py \
  scripts/validate_repository.py \
  scripts/repository_health_check.py \
  scripts/validate_profiles.py \
  scripts/check_report_freshness.py \
  scripts/generate_workflow_health_report.py \
  scripts/audit_reject_risk.py \
  scripts/audit_domestic_app_connectivity.py \
  scripts/generate_app_status_matrix.py \
  scripts/score_candidates.py

node --check Scripts/app-cleaner.js

python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_profiles.py
python3 scripts/validate_repository.py
python3 scripts/check_report_freshness.py
python3 scripts/repository_health_check.py
```

## 报告要求

每次改动必须明确是否需要刷新：

- `reports/repository_health_report.md`
- `reports/report_freshness_report.md`
- `reports/workflow_health_report.md`
- `reports/profile_validation_report.md`
- `reports/app_status_matrix.md`
- `reports/reject_risk_report.md`
- `reports/domestic_app_connectivity_audit.md`
- `reports/candidate_security_score_report.md`
- `reports/rule_traceability_matrix.md`

新增或修改规则、脚本、MITM 前，应先生成或更新相应审计报告；无法确认真实 App 行为时，只能写 `manual-review` 或 `未测`。

## 回滚要求

每次变更必须说明：

1. 回滚哪些源头文件。
2. 是否需要重新构建 stable。
3. 是否需要同步 Root。
4. 是否影响 Stable Plus、Lite、Full。
5. 是否需要用户重新测试登录、支付、验证码、图片加载或播放链路。

## PR / commit 描述模板

```markdown
## 修改范围
- 源头文件：
- 生成文件：
- 风险单元：
- 是否影响 Stable：
- 是否影响 Stable Plus / Lite / Full：

## 风险判断
- 登录：是/否
- 支付：是/否
- 验证码：是/否
- 银行：是/否
- 微信/支付宝：是/否
- 图片/CDN：是/否
- HTTPDNS：是/否
- Cookie/Token/会员权益：是/否
- MITM 扩大：是/否

## 验证结果
- py_compile：通过/失败
- node --check：通过/失败
- build stable：通过/失败
- build release variants：通过/失败
- validate_profiles：通过/失败
- validate_repository：通过/失败
- check_report_freshness：通过/失败
- repository_health_check：通过/失败

## 回滚路径
- 回滚文件：
- 回滚动作：
- 重新构建：是/否
- 重新同步 Root：是/否
- 复测范围：
```

## 判断标准

- 能报告的问题，不直接猜测修复。
- 能单项处理的问题，不批量处理。
- 能进入 Stable Plus 测试的问题，不直接进 Stable。
- 能等待日志确认的问题，不用关键词硬判。
- 能保持未测的问题，不写成通过。
- 能用 Lite 对照定位的问题，不直接扩大 Stable。
