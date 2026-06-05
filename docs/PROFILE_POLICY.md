# Profile 策略与发布边界

本文件定义 GrandpaNiu 模块工厂的 profile 边界。任何 workflow、脚本或人工修改都应遵守本策略。

## Profile 定义

| Profile | MITM 来源 | 用途 | 是否默认发布 | 晋级权限 |
|---|---|---|---|---|
| `lite` | `MITM-core.conf` | 低耗电、低风险参考 | 否 | 不作为晋级来源，只用于对照排查 |
| `stable` | `MITM-core.conf` + `MITM-app-clean.conf` | 默认正式版 | 是 | 只接收已测试、可回滚的单项变更 |
| `stable-plus` | stable + `MITM-stable-plus.conf` | 常用 App 增强测试版 | 否 | 可作为单项 App 晋级候选来源 |
| `full` | stable-plus + `MITM-extended.conf` 或 core/app/extended | 全量排查测试版 | 否 | 冻结为排查版，不允许批量晋级 Stable |

## 默认发布规则

- 默认 workflow 必须使用 `--profile stable`。
- 默认 workflow 不允许使用 `--profile stable-plus`。
- 默认 workflow 不允许使用 `--profile full`。
- 根目录 `Ronghemokuai.sgmodule` 只允许由 stable 构建后同步生成。
- 任何 workflow 不得把 Full 或 Stable Plus 当成默认入口。

## MITM 晋级规则

MITM hostname 的晋级路径：

```text
MITM-extended.conf
-> MITM-stable-plus.conf
-> 人工测试
-> MITM-app-clean.conf
```

要求：

1. 不允许从 extended 批量直接进入 stable。
2. 不允许从 full 批量直接进入 stable。
3. 进入 `MITM-stable-plus.conf` 的 hostname 必须说明对应 App 或服务类别。
4. 进入 `MITM-app-clean.conf` 前，必须在 `reports/manual_test_log.md` 有真实测试记录。
5. 银行、支付、登录、验证码、token、cookie、passport、security 相关 hostname 不得进入 stable。
6. 涉及微信媒体、小程序、图片 CDN、地图、订单前置的 hostname，即使测试通过，也必须单项晋级。

## Full 冻结规则

Full 的定位是排查和查漏拦，不是默认发布池，也不是 Stable 候选池。

禁止：

- 将 Full 整体合并进 Stable。
- 将 Full 的 MITM、Rule、Rewrite、Script 批量迁移到 Stable。
- 用 Full 的“能用”替代 Stable 的真实测试记录。
- 把 Full 的排查结果写成“Stable 通过”。

允许：

- 使用 Full 定位缺失的 hostname、规则或脚本覆盖。
- 将 Full 中的单个 App、单类规则、单组 hostname 拆出来进入 Stable Plus 测试。
- Stable Plus 单项测试通过后，再按晋级流程进入 Stable。

Full 到 Stable 的任何变更必须包含：

```text
影响范围
具体文件和规则差异
manual_test_log.md 测试记录
Lite 对照结果
关闭模块对照结果
回滚路径
误伤风险说明
```

## Script 晋级规则

脚本候选必须先进入 pending：

```text
candidates.json pending
-> 人工审查
-> stable-plus 或 app-clean 测试
-> stable
```

不允许新脚本直接进入 stable，除非它是已有脚本的安全修复，并且通过人工验证。

脚本风险排序：

```text
request-body / binary / protobuf / Cookie / Token / 登录 / 支付 / 验证码
> response-body JSON cleaner
> requires-body=0 的请求清理
> 可替换为 Rule / URL Rewrite 的轻量逻辑
```

高风险脚本默认不得进入 Stable。

## 远程规则晋级规则

- `RULE-SET` 必须通过 `scripts/validate_remote_rule_syntax.py`。
- `DOMAIN-SET` 必须是纯域名集合。
- Quantumult X 规则必须先由 `scripts/convert_quanx_rules.py` 转换后再引用。
- 不允许把 `host`、`host-suffix`、`host-keyword`、`ip6-cidr` 直接作为 Shadowrocket `RULE-SET`。
- 远程规则源失败时，优先移入 pending 或替换为仓库内转换文件，不允许用短链、代理、镜像绕过。

## 回滚规则

每次重大变更都必须可回滚：

- Root 与 Release 不一致时，先运行 `factory_finalize.py --sync-root`。
- stable 出现严重误杀时，优先回滚最近一次 profile 或 MITM 分层变更。
- 新增的 MITM 层应先从 `stable-plus` 移除，不要先删除源文件。
- full 只用于排查，不作为回滚目标发布。
- 远程规则语法失败时，先移除或转换对应源，再重建四个 Release 版本。

## 验证命令

每次大改后运行：

```bash
python3 -m py_compile scripts/*.py
python3 scripts/convert_quanx_rules.py
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_remote_rule_syntax.py
python3 scripts/validate_repository.py
python3 scripts/validate_profiles.py
python3 scripts/repository_health_check.py
```

## 人工测试要求

没有真实测试时，不得写“通过”。测试最少覆盖：

- Stable 与 Lite 对照。
- Spotify。
- YouTube。
- 知乎。
- Bilibili。
- 淘宝 / 京东 / 拼多多。
- 微信 / 支付宝 / 银行 App 登录、验证码、支付前置流程。
- 图片 CDN、小程序资源、地图搜索和定位。

测试必须记录到 `reports/manual_test_log.md`。Issue 反馈必须优先要求用户提供 Lite 对照、关闭模块对照和日志。