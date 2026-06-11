# Profile 策略与发布边界

GrandpaNiu 当前采用单一 Fusion profile。所有公开 iOS 构建、验证、报告和 workflow 都应围绕 `Rewrite/Profiles/fusion.conf`。

## 当前策略

| 项目 | 规则 |
|---|---|
| 默认 profile | `fusion` |
| 默认构建命令 | `python3 scripts/build_module.py --build --profile fusion` |
| Root 同步 | `python3 scripts/factory_finalize.py --sync-root` |
| 公开入口 | `Ronghemokuai.sgmodule`、`Release/Ronghemokuai.sgmodule` |
| 旧四版本 | 历史兼容或废弃文件，不作为 README、导入页、workflow、报告的正式入口 |

## 旧 profile 处理

`stable.conf`、`stable-plus.conf`、`lite.conf`、`full.conf` 如果仍保留，只能用于历史审计、对照或回滚参考。不得再新增用户入口，也不得作为默认 workflow 参数。

允许出现的旧名称场景：

- 文件名、历史报告、迁移记录。
- 说明“deprecated / legacy only”。
- 源文件名里保留上游来源，例如 `MITM-stable-plus.conf` 或 `app2smile-qqnews-stable-plus.conf`。

不允许出现的旧逻辑：

- workflow 使用 `--profile stable`、`--profile stable-plus`、`--profile lite`、`--profile full`。
- README 或导入页引导用户选择四版本。
- 验证脚本强制要求四版本同时存在或同时发布。
- 报告把旧四版本当成当前正式发布入口。

## Fusion 分层

Fusion 并不是把所有内容无条件混在一起。它仍按 source-first 分层维护：

| 层 | 文件 | 用途 |
|---|---|---|
| core | `MITM-core.conf`、核心 Script / Rule | Spotify、YouTube、知乎等基础专项 |
| app-clean | `MITM-app-clean.conf`、`Scripts/app-cleaner.js` | 通用低风险 JSON 清理 |
| legacy-reviewed | `*-legacy-reviewed.conf` | 已审阅历史兼容内容 |
| qingrex | `*-qingrex-miniapp-app-ad.conf`、`Rules/qingrex-miniapp-app-ad.list` | 小程序 / App 广告层 |
| selected extensions | `MITM-stable-plus.conf`、`MITM-extended.conf` 中被 Fusion 引用的部分 | 扩展覆盖，必须保留风险说明和回滚路径 |

## 安全边界

不得进入 Fusion 的内容：

- 会员破解、付费绕过、登录绕过。
- 支付、银行、验证码、证书校验、账号安全改写。
- Cookie / Token / Authorization 读写或伪造。
- 未知、混淆、短链、代理镜像来源脚本。
- request-body、binary、protobuf、加密 body 脚本，除非有明确人工审查和回滚方案。

## Full 冻结规则

旧 `full` 只能作为历史排查概念保留，不再作为公开入口或默认构建入口。

- 不允许从 full 批量直接进入 stable。
- 不允许 Full 整体合并进 Fusion。
- 不允许把 `host`、`host-suffix`、`host-keyword`、`ip6-cidr` 直接作为 Shadowrocket `RULE-SET`。
- 任何高风险迁移必须先有 `reports/manual_test_log.md` 记录。
- 高风险规则复核必须包含 Lite 对照结果、关闭模块对照结果和可回滚源头。

## 自动维护边界

自动化可以做：

- 拉取可信候选规则源。
- 运行远程规则语法检查。
- 失效源审核、禁用或替换候选。
- 构建 Fusion。
- 同步 Root / Release。
- 生成报告。
- 检查重复项和必要 section。

自动化不能宣称：

- 任意 App 真机已通过。
- 支付、登录、验证码、订单链路已安全。
- 外部脚本可以无审核进入 Fusion。

## 必跑验证

```bash
python3 -m py_compile scripts/*.py
node --check Scripts/app-cleaner.js
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_module_integrity.py
python3 scripts/validate_remote_rule_syntax.py
python3 scripts/validate_profiles.py
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

Android 改动还必须运行：

```bash
python3 scripts/build_android_rules.py
python3 scripts/android_format_check.py
```

## 回滚原则

- Root / Release 不一致时，先运行 `factory_finalize.py --sync-root`。
- Fusion 出现严重误伤时，先从 `Rewrite/Profiles/fusion.conf` 移除对应源头引用并重建。
- 远程规则源失效时，优先禁用或替换源，不使用短链、代理或镜像绕过。
- 高风险 App 只做单项回滚，不批量删规则。
- 回滚后必须重新生成 `reports/module_integrity_report.md`、`reports/remote_rule_syntax_report.md` 和仓库健康报告。
