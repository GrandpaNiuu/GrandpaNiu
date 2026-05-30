# 仓库健康检查报告

生成时间：2026-05-31 05:13:37 +0800

## 总体状态

- 阻断问题：0
- 提醒事项：1
- 统一验证：通过
- Root 与 Release 一致：是
- 启用远程规则源：11
- 启用候选源：6
- pending 脚本候选：1
- 脚本总数：104
- MITM hostname 数量：120

## 模块区块行数

- Rule: 531
- URL Rewrite: 1597
- Header Rewrite: 5
- Body Rewrite: 455
- Map Local: 15
- Script: 214
- MITM: 4

## 阻断问题

- 无

## 提醒事项

- PrivacyLite 已连续失败 2 天及以上，应保守禁用候选或验证同源替代

## 缺少必要文件

- 无

## 缺少工作流

- 无

## 未生成的可选报告

- 无

## 主模块缺少关键标记

- 无

## 重复脚本名

- 无

## 重复 MITM hostname

- 无

## README 失效本地链接

- 无

## Workflow 摘要

- .github/workflows/module-factory-build.yml: contents:write, concurrency, uses-stable
- .github/workflows/daily-module-update.yml: contents:write, concurrency, uses-stable
- .github/workflows/daily-invalid-source-repair.yml: contents:write, concurrency, uses-stable
- .github/workflows/upstream-collect.yml: contents:write, concurrency, uses-stable
- .github/workflows/repository-health.yml: contents:write, concurrency, uses-stable

## Pending 脚本候选

- app2smile Tieba script

## 统一验证输出

```text
Repository validation passed.
```

## 后续维护建议

1. 日常修改应优先编辑 Rules、Scripts、Rewrite/Sources、Rewrite/Remotes 和 Rewrite/Profiles。
2. Root 模块只作为生成结果，必须通过 build_module.py 与 factory_finalize.py 同步。
3. 新脚本默认 pending，不直接进入 stable。
4. 出现登录、支付、验证码异常时，优先回查 MITM、Body Rewrite 和 Map Local。
5. 远程源连续失败 2 天后才进入处理流程，单日网络失败只报告观察。
