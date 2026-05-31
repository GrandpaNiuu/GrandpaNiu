# 仓库健康检查报告

生成时间：2026-05-31 08:53:06 +0800

## 总体状态

- 阻断问题：0
- 提醒事项：2
- 统一验证：通过
- Root 与 Release 一致：是
- 启用远程规则源：12
- 启用候选源：6
- pending 脚本候选：1
- 脚本总数：37
- stable 当前 MITM hostname 数量：120
- 默认发布策略：stable only；stable-plus / full 不默认发布

## 模块区块行数

- Rule: 533
- URL Rewrite: 1597
- Header Rewrite: 5
- Body Rewrite: 455
- Map Local: 15
- Script: 154
- MITM: 4

## Profile 策略摘要

| Profile | MITM 输入 | 用途 |
|---|---|---|
| lite | Rewrite/Sources/MITM-core.conf | 低耗电参考版，不默认发布 |
| stable | Rewrite/Sources/MITM-core.conf, Rewrite/Sources/MITM-app-clean.conf | 默认正式版，可以发布 |
| stable-plus | Rewrite/Sources/MITM-core.conf, Rewrite/Sources/MITM-app-clean.conf, Rewrite/Sources/MITM-stable-plus.conf | 常用 App 增强测试版，不默认发布 |
| full | Rewrite/Sources/MITM-core.conf, Rewrite/Sources/MITM-app-clean.conf, Rewrite/Sources/MITM-extended.conf | 全量排查测试版，不默认发布 |

## MITM 分层数量

| 文件 | hostname 数量 |
|---|---:|
| `Rewrite/Sources/MITM-core.conf` | 11 |
| `Rewrite/Sources/MITM-app-clean.conf` | 109 |
| `Rewrite/Sources/MITM-stable-plus.conf` | 95 |
| `Rewrite/Sources/MITM-extended.conf` | 889 |
| `Rewrite/Sources/MITM.conf` | 1009 |

## 阻断问题

- 无

## 提醒事项

- 当前存在失效源历史记录：1 条
- 存在连续失败 2 天及以上的源：1 条，应确认是否已禁用或替代

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

## 失效源历史记录

- `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PrivacyLite/PrivacyLite.list`

## 统一验证输出

```text
Repository validation passed.
```

## 后续维护建议

1. 日常修改应优先编辑 Rules、Scripts、Rewrite/Sources、Rewrite/Remotes 和 Rewrite/Profiles。
2. Root 模块只作为生成结果，必须通过 build_module.py 与 factory_finalize.py 同步。
3. 新脚本默认 pending，不直接进入 stable。
4. MITM 从 extended 进入 stable 前，应先进入 stable-plus 并完成真实测试。
5. 出现登录、支付、验证码异常时，优先回查 MITM、Body Rewrite 和 Map Local。
6. 远程源连续失败 2 天后才进入处理流程，单日网络失败只报告观察。
