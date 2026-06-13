# 维护 Playbook

本 playbook 用于日常小步维护。目标是让仓库保持可构建、可审计、可回滚，不通过一次性大改扩大 Stable 覆盖。

## 日常维护顺序

1. 先阅读最近报告：
   - `reports/repository_health_report.md`
   - `reports/report_freshness_report.md`
   - `reports/profile_validation_report.md`
   - `reports/reject_risk_report.md`
   - `reports/domestic_app_connectivity_audit.md`
   - `reports/app_status_matrix.md`
2. 确认修改入口：
   - 规则：`Rules/*.list` 或 `Rewrite/Remotes/*.json`
   - 脚本：`Scripts/*.conf` 和对应脚本文件
   - Rewrite / MITM：`Rewrite/Sources/*.conf`
   - 版本差异：`Rewrite/Profiles/*.conf`
3. 小步修改源头文件，不直接改生成结果。
4. 运行语法检查、构建、四版本生成和验证。
5. 只提交本次相关文件，报告中说明影响范围和回滚方式。
6. 在 Shadowrocket 里只启用一个版本做自动化验证。

## 规则修改边界

- Stable 只接受低误伤、可解释、可回滚的规则。
- 不直接把 Stable Plus 或 Full 的规则整体合并进 Stable。
- 图片 CDN、HTTPDNS、登录、支付、验证码、银行、微信媒体、小程序资源默认高风险。
- 高风险规则先进入人工复核计划或 Stable Plus 测试，不批量删除，也不批量加入 `REJECT`。
- 遇到误伤时优先加精确 `DIRECT` 保护，不加过宽白名单。

## 脚本修改边界

- 未知脚本、混淆脚本、来源不清脚本保持 pending。
- 请求体、二进制、protobuf、账号状态、登录、支付、验证码、会员权益相关脚本不得自动进入 Stable。
- 低风险 JSON cleaner 可以在明确回滚路径和测试范围后逐步合并到 `Scripts/app-cleaner.js`。
- 每次修改 `Scripts/app-cleaner.js` 后必须运行：

```bash
node --check Scripts/app-cleaner.js
```

## MITM 修改边界

- MITM hostname 必须最小化。
- 不允许无脑追加 `*` 通配。
- 不覆盖银行、支付、验证码、登录安全域。
- Stable 的 MITM 以低误伤为优先。
- Stable Plus 可用于增强测试，但仍需单项 App 测试记录。
- Full 只用于排查缺失 hostname，不适合长期启用。

## 四版本使用边界

- `GrandpaNiu / Ronghemokuai.sgmodule` = 默认 Stable。
- `Release/Ronghemokuai-stable.sgmodule` = Stable 独立发布文件。
- `Stable Plus` = 增强测试版，不默认发布，不整体合并进 Stable。
- `Lite` = 低耗电 / 异常定位版。
- `Full` = 全量查漏版，不建议长期启用。

同一设备同一时间只启用一个版本。

## 必跑命令

```bash
python3 -m py_compile \
  scripts/build_module.py \
  scripts/build_release_variants.py \
  scripts/factory_finalize.py \
  scripts/validate_repository.py \
  scripts/repository_health_check.py \
  scripts/validate_profiles.py \
  scripts/check_report_freshness.py

node --check Scripts/app-cleaner.js

python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/check_report_freshness.py
python3 scripts/repository_health_check.py
```

## 自动化验证流程

1. Shadowrocket 中只启用一个版本。
2. 更新模块、更新脚本、更新全部资源。
3. 先测 Stable 的常用链路。
4. Stable 无异常后，再按单个 App 测 Stable Plus。
5. 测试项目至少包括：
   - 首页加载
   - 图片加载
   - 登录状态
   - 支付前置页
   - 验证码
   - 小程序 / 媒体资源
   - 广告减少效果
6. 测试结果写入 `reports/automated_quality_evidence.md`。
7. 没有真实测试记录时，只能写“未测”或 `manual-review`。

## 回滚流程

1. 根据报告定位改动层：
   - `Rules/`
   - `Scripts/`
   - `Rewrite/Sources/`
   - `Rewrite/Profiles/`
   - `Rewrite/Remotes/`
2. 回滚对应源头文件。
3. 重新运行构建和验证。
4. 确认 Root 与 Release 一致。
5. 更新相关报告，写清楚回滚原因和影响范围。

不要通过手工改 `Ronghemokuai.sgmodule` 来回滚长期状态；根模块只是生成结果。

## 禁止事项

- 不加入会员破解、Premium 解锁、权益伪造。
- 不加入支付绕过、登录绕过、验证码绕过。
- 不加入 Cookie、Token、BoxJS 或账号任务依赖。
- 不加入成人、博彩、灰产、短链、镜像站或 ghproxy 正式源。
- 不加入未知混淆脚本。
- 不伪造测试通过。
- 不把“规则覆盖存在”写成“已经验证通过”。
- 不把 Stable Plus 整体合并进 Stable。
- 不直接扩大 Stable 规则、MITM 或脚本覆盖来解决未验证需求。
