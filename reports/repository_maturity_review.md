# 仓库专业度复盘与加强方向

## 结论

当前仓库已经从普通自用模块进入“专业化模块工厂”阶段，但还不能称为完美仓库。

当前判断：

```text
专业化自动构建能力：已具备
多版本发布能力：已具备
脚本融合与回滚治理：已具备
MITM 分层治理：已具备
健康报告与覆盖矩阵：已具备
完全无人值守真机验证：不具备，也不应伪造
默认 Stable 无审核自动吸收外部脚本：不应该
```

综合成熟度：约 80-85%。

## 当前框架理解

仓库当前框架是源头驱动模块工厂：

```text
Rules
Scripts
Rewrite/Sources
Rewrite/Remotes
Rewrite/Profiles
scripts/*.py
        ↓
build_module.py
        ↓
factory_finalize.py
        ↓
build_release_variants.py
        ↓
Root + Release 四版本模块
```

四个版本分工：

| 版本 | 定位 | 是否默认发布 | 风险 |
|---|---|---|---|
| stable | 默认正式版 | 是 | 低 |
| stable-plus | 增强测试版 | 否 | 中 |
| lite | 低耗电排查版 | 否 | 最低 |
| full | 全量排查版 | 否 | 高 |

## 当前已经做得好的地方

### 1. 多版本发布结构清晰

- `stable` 保持默认发布。
- `stable-plus` 用于测试更多覆盖。
- `lite` 用于低风险排查。
- `full` 用于查漏拦，不默认发布。

这是专业仓库的必要基础。

### 2. Root / Release 闭环已建立

仓库已有 Root 与 Release 一致性检查，并在健康报告中展示。

### 3. app-cleaner 已进入专业融合架构

`Scripts/app-cleaner.js` 已改成 registry / dispatcher 架构：

- `RAW_CLEANERS` 处理 raw body。
- `JSON_CLEANERS` 处理标准 JSON response。
- Batch 5 通用 cleaner 放最后，避免抢先误伤专项 cleaner。
- workflow 执行 `node --check Scripts/app-cleaner.js`。

### 4. MITM 分层治理已经有基础

当前 MITM 被拆成：

- `MITM-core.conf`
- `MITM-app-clean.conf`
- `MITM-stable-plus.conf`
- `MITM-extended.conf`
- `MITM.conf` 原始回滚源

这比单一大 MITM 更专业。

### 5. 自动化边界已经写清楚

`docs/AUTOMATION_POLICY.md` 已明确：

- 自动化负责收集、筛选、构建、验证、报告和告警。
- 默认 Stable 不接受未知内容无审核直入。
- 所有 App 一视同仁维护，不设置核心保护对象。

## 本次检查中已修正的问题

### 1. 修正旧“核心”表达

发现部分生成脚本和测试模板仍会生成：

- 核心标记
- 核心专项
- 核心流程

这与当前“一视同仁维护”原则冲突。

已修正：

- `scripts/validate_profiles.py`
- `scripts/generate_script_inventory_report.py`
- `reports/manual_test_log.md`

### 2. 修正脚本清单分类逻辑

旧逻辑会因为名称包含 `zhihu` 就标记为“核心专项脚本”。

已改为：

- 不再按 App 名称设置核心地位。
- request-body、binary、protobuf、登录、支付、验证码、Cookie、Token、权益类才按高风险处理。
- 微博、知乎 R-Store、MGTV、Soul 等复杂脚本进入人工复核，而不是简单归类为可合并。

## 当前不足和加强方向

### P0：必须补齐最新 Actions 结果

最新报告显示部分 workflow 在生成时仍为 running / in_progress。需要重新跑：

```text
Module Factory Build
Repository Health Check
```

跑完后必须确认：

- 全部 completed / success。
- Root / Release 一致。
- validate_repository.py 通过。
- node --check 通过。
- profile_validation_report 更新到最新提交。

### P1：测试治理仍是最大短板

当前手动测试记录仍是未测试状态，这是正确的，没有伪造通过。

但这也是仓库距离“非常专业”的最大短板。

需要做：

1. Stable 第一轮真实测试。
2. app-cleaner 已融合 App 批量测试。
3. Stable Plus 分批测试。
4. 只把真实通过项加入晋级候选。
5. 异常必须绑定 commit、模块版本、App、页面、复现步骤。

### P1：候选源安全评分还不够

当前已有候选源收集，但还需要加强：

- 来源可信评分。
- 脚本风险词评分。
- 是否混淆评分。
- 是否包含 Cookie / Token / BoxJS。
- 是否改 request body。
- 是否触碰支付 / 登录 / 验证码。
- 是否有回滚路径。

建议新增：

```text
scripts/score_candidates.py
reports/candidate_security_score_report.md
```

### P1：Stable Plus 晋级机制应做成 PR 化

现在是生成晋级候选报告。更专业的做法是：

```text
Stable Plus 测试通过
-> 生成单项晋级候选
-> 自动开 PR
-> PR 内包含影响范围、MITM 增量、回滚方式、测试记录
-> 人工合并
```

### P2：脚本数量还可以继续降，但不能以破坏功能为代价

当前脚本入口已经显著下降。继续向 20 左右推进时，不能继续盲目硬合。

正确方向：

1. 继续合并低风险 JSON response cleaner。
2. requires-body=0 的脚本评估改成 Rule / URL Rewrite。
3. request-body 保持独立。
4. protobuf / binary-body 保持独立。
5. 复杂脚本先拆功能再决定是否合并。

### P2：健康报告应加入“报告新鲜度”检查

当前健康报告会展示生成时间，但还没有强制判断报告是否落后于最新提交。

建议新增：

```text
reports freshness check
```

检查内容：

- profile_validation_report 是否晚于最新构建提交。
- script_inventory_report 是否晚于 Scripts 变更。
- repository_health_report 是否晚于 workflows / scripts 变更。
- manual_test_log 是否明确未测试或已测试。

### P2：README 与 docs 应继续保持生成一致性

README、MODULE_FEATURES、AUTOMATION_POLICY 已经比较清楚，但后续建议加入：

- 单项 App 状态页。
- App 覆盖状态表：覆盖 / 未测 / 通过 / 异常 / 回滚。
- 每个版本的 MITM 差异摘要。

建议新增：

```text
reports/app_status_matrix.md
```

## 对“是否完美”的判断

不是完美。

原因：

- Actions 最新完成状态需要重新确认。
- 真机测试仍大面积未完成。
- 候选源安全评分还不够细。
- Stable Plus 晋级还不是 PR 流程。
- 报告新鲜度没有强门禁。
- 复杂脚本仍需要逐个拆解评估。

但它已经是比较专业的模块工厂：

- 有分层。
- 有构建。
- 有验证。
- 有报告。
- 有回滚。
- 有自动化边界。
- 有多版本导入。
- 有脚本融合架构。

## 下一步建议顺序

1. 重新运行 `Module Factory Build`。
2. 重新运行 `Repository Health Check`。
3. 确认 workflow 全部 success。
4. 开始 Stable 第一轮真实测试。
5. 新增候选源安全评分报告。
6. 新增报告新鲜度检查。
7. 将 Stable Plus 晋级候选改成自动 PR。
8. 继续低风险 JSON cleaner 融合，目标向 20-30 个脚本入口靠近。

## 最终指正

追求“全自动”没有问题，但不能把“全自动拉取外部规则脚本”理解为“自动塞进默认模块”。

专业做法是：

```text
自动收集
自动评分
自动构建
自动报告
自动开 Issue / PR
人工确认测试结果
单项晋级 Stable
```

这才是长期稳定仓库，而不是短期堆规则仓库。
