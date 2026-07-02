# Fusion 构建与发布边界

GrandpaNiu 采用单一 `fusion` profile。公开 iOS 构建、验证、报告和 workflow 都围绕 `Rewrite/Profiles/fusion.conf`。

## 当前策略

| 项目 | 规则 |
|---|---|
| 默认 profile | `fusion` |
| 标准构建 | `python3 Rewrite/Generator/Builder.py --profile fusion --release` |
| Root 同步 | 由 Builder / `factory_finalize.py --sync-root` 完成 |
| 公开入口 | `Ronghemokuai.sgmodule`、`Release/Ronghemokuai.sgmodule`、`Release/Module.sgmodule` |
| App 独立模块 | `Release/Modules/*.sgmodule`，仅用于诊断或按需导入，不构成版本线 |

仓库不再保留 Stable、Stable Plus、Lite 或 Full profile、Release 产物、晋级流程或对应人工测试清单。历史变更仅通过 Git 历史追溯。

## Fusion 分层

Fusion 仍按 source-first 分层维护，而不是无条件叠加所有规则：

| 层 | 用途 |
|---|---|
| core | Spotify、YouTube、知乎等基础专项 |
| app-clean | 通用低风险 JSON 清理 |
| legacy-reviewed | 已审阅的兼容内容 |
| qingrex | 小程序 / App 广告层 |
| selected extensions | 已审阅的扩展覆盖；必须保留风险说明和回滚路径 |

## 安全边界

不得进入 Fusion 的内容：

- 会员破解、付费绕过、登录绕过。
- 支付、银行、验证码、证书校验、账号安全改写。
- Cookie、Token 或 Authorization 的读写、伪造或泄露。
- 未知、混淆、短链、代理镜像来源脚本。
- request-body、binary、protobuf、加密 body 脚本；除非已完成明确人工审查并具备回滚方案。

## 自动维护边界

自动化可以拉取可信候选源、执行语法与风险校验、构建 Fusion、同步 Root / Release、生成报告和检查重复项。

自动化不能声称任意 App 已完成真机验证，也不能把外部脚本未经审核直接纳入 Fusion。

## 必跑验证

```bash
python3 -m py_compile scripts/*.py Rewrite/Generator/Builder.py
node --check Scripts/app-cleaner.js
python3 Rewrite/Generator/Builder.py --profile fusion --release
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
- Fusion 出现误伤时，从 `Rewrite/Profiles/fusion.conf` 移除对应源头引用并重建。
- 远程规则源失效时，优先禁用或替换源，不使用短链、代理或镜像绕过。
- 高风险 App 只做单项回滚，不批量删规则。
- 回滚后重新生成模块完整性、远程规则语法与仓库健康报告。
