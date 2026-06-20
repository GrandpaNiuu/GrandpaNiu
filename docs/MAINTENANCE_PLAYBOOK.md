# 维护 Playbook

本 playbook 用于日常小步维护。目标是让仓库保持可构建、可审计、可回滚，不通过一次性大改扩大风险。

## 日常维护顺序

1. 先读 AI 维护记录：
   - `AGENTS.md`
   - `PROJECT_STATE.md`
   - `AI_HANDOFF.md`
   - `docs/ai/TASKS.md`
   - `docs/ai/DECISIONS.md`
   - `docs/ai/RISK_LOG.md`
   - `docs/ai/WORKLOG.md`
2. 再读最近报告：
   - `reports/repository_health_report.md`
   - `reports/report_freshness_report.md`
   - `reports/profile_validation_report.md`
   - `reports/reject_risk_report.md`
   - `reports/domestic_app_connectivity_audit.md`
   - `reports/app_status_matrix.md`
3. 确认修改入口：
   - 规则：`Rules/*.list` 或 `Rewrite/Remotes/*.json`
   - 脚本：`Scripts/*.conf` 和对应 JS 文件
   - Rewrite / Header / Body / Map Local / MITM：`Rewrite/Sources/*.conf`
   - App 源：`Rewrite/Sources/Apps/*.conf`
   - 通用层：`Rewrite/Sources/Misc/*.conf`
4. 小步修改源头文件，不直接改生成结果。
5. 运行相关检查。
6. 只提交本次相关文件，并说明影响范围和回滚方式。

## Fusion 单模块边界

- 公开 iOS 入口是 Fusion 主模块。
- `Ronghemokuai.sgmodule`、`Release/Ronghemokuai.sgmodule`、`Release/Module.sgmodule` 必须保持同源。
- `Release/Modules/` 是 App 独立诊断和便利用模块，不是新的公开版本路线。
- 旧 Stable / Stable Plus / Lite / Full 只作为 deprecated / legacy reference，不作为日常维护目标。

## 规则修改边界

- 只接受低误伤、可解释、可回滚的规则。
- 不批量删除或批量新增高风险规则。
- 图片 CDN、HTTPDNS、登录、支付、验证码、银行、微信媒体、小程序资源默认高风险。
- 遇到误伤时优先做精确 `DIRECT` 保护或单条回滚，不加过宽白名单。
- 没有真实日志和手测记录时，保持 manual-review。

## 脚本修改边界

- 未知脚本、混淆脚本、来源不清脚本保持 pending 或 manual-review。
- 请求体、二进制、protobuf、账号状态、登录、支付、验证码、会员权益相关脚本不得自动进入 Fusion。
- 低风险 JSON cleaner 可以在明确回滚路径和测试范围后逐步合并到 `Scripts/app-cleaner.js`。
- 修改 `Scripts/app-cleaner.js` 后至少运行：

```bash
node --check Scripts/app-cleaner.js
```

## MITM 修改边界

- MITM hostname 必须最小化。
- 不允许无脑追加 `*` 通配。
- 不覆盖银行、支付、验证码、登录安全域。
- broad wildcard 必须有来源、用途和回滚路径。

## 必跑命令

标准构建：

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
```

完整质量门：

```bash
python3 scripts/quality_gate.py
```

常用轻量检查：

```bash
python3 -m py_compile scripts/*.py Rewrite/Generator/Builder.py
node --check Scripts/app-cleaner.js
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

## 自动化验证流程

1. Shadowrocket / Surge 中只启用 Fusion 主模块。
2. 更新模块、脚本和资源。
3. 先测常用链路。
4. 重点测试：
   - 首页加载
   - 图片加载
   - 登录状态
   - 支付前置页
   - 验证码
   - 小程序 / 媒体资源
   - 广告减少效果
5. 没有真实测试记录时，只能写“未测”或 `manual-review`。

## 回滚流程

1. 根据报告定位改动层：
   - `Rules/`
   - `Scripts/`
   - `Rewrite/Sources/`
   - `Rewrite/Remotes/`
2. 回滚对应源头文件。
3. 重新运行构建和验证。
4. 确认 Root / Release 一致。
5. 更新相关报告，写清回滚原因和影响范围。

不要通过手工改 `Ronghemokuai.sgmodule` 回滚长期状态；根模块只是生成结果。

## 禁止事项

- 不加入会员破解、Premium 解锁、权益伪造。
- 不加入支付绕过、登录绕过、验证码绕过。
- 不加入 Cookie、Token、BoxJS 或账号依赖。
- 不加入成人、博彩、灰产、短链、镜像站或 ghproxy 正式源。
- 不加入未知混淆脚本。
- 不伪造测试通过。
- 不恢复旧四版本作为公开路线。
- 不直接扩大 Fusion 规则、MITM 或脚本覆盖来解决未经验证的需求。
