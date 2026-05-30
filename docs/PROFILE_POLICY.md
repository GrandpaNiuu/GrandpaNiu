# Profile 策略与发布边界

本文件定义 GrandpaNiu 模块工厂的 profile 边界。任何 workflow、脚本或人工修改都应遵守本策略。

## Profile 定义

| Profile | MITM 来源 | 用途 | 是否默认发布 |
|---|---|---|---|
| `lite` | `MITM-core.conf` | 低耗电、低风险参考 | 否 |
| `stable` | `MITM-core.conf` + `MITM-app-clean.conf` | 默认正式版 | 是 |
| `stable-plus` | stable + `MITM-stable-plus.conf` | 常用 App 增强测试版 | 否 |
| `full` | stable-plus + `MITM-extended.conf` 或 core/app/extended | 全量排查测试版 | 否 |

## 默认发布规则

- 默认 workflow 必须使用 `--profile stable`。
- 默认 workflow 不允许使用 `--profile stable-plus`。
- 默认 workflow 不允许使用 `--profile full`。
- 根目录 `Ronghemokuai.sgmodule` 只允许由 stable 构建后同步生成。

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
2. 进入 `MITM-stable-plus.conf` 的 hostname 必须说明对应 App 或服务类别。
3. 进入 `MITM-app-clean.conf` 前，必须在 `reports/manual_test_log.md` 有真实测试记录。
4. 银行、支付、登录、验证码、token、cookie、passport、security 相关 hostname 不得进入 stable。

## Script 晋级规则

脚本候选必须先进入 pending：

```text
candidates.json pending
-> 人工审查
-> stable-plus 或 app-clean 测试
-> stable
```

不允许新脚本直接进入 stable，除非它是已有核心脚本的安全修复，并且通过人工验证。

## 回滚规则

每次重大变更都必须可回滚：

- Root 与 Release 不一致时，先运行 `factory_finalize.py --sync-root`。
- stable 出现严重误杀时，优先回滚最近一次 profile 或 MITM 分层变更。
- 新增的 MITM 层应先从 `stable-plus` 移除，不要先删除源文件。
- full 只用于排查，不作为回滚目标发布。

## 验证命令

每次大改后运行：

```bash
python3 -m py_compile scripts/*.py
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/validate_profiles.py
python3 scripts/repository_health_check.py
```

## 人工测试要求

没有真实测试时，不得写“通过”。测试最少覆盖：

- Spotify
- YouTube
- 知乎
- Bilibili
- 淘宝 / 京东 / 拼多多
- 微信 / 支付宝 / 银行 App 登录、验证码、支付前置流程
