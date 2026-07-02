# Fusion 模块与发布边界

GrandpaNiu 当前采用单一 `fusion` profile。所有 iOS 主模块构建、验证、报告和自动化发布，都围绕 `Rewrite/Profiles/fusion.conf` 维护。

## 当前策略

| 项目 | 内容 |
|---|---|
| 默认 profile | `fusion` |
| 标准构建 | `python3 Rewrite/Generator/Builder.py --profile fusion --release` |
| Root 同步 | 由 Builder / `factory_finalize.py --sync-root` 完成 |
| 公开入口 | `Ronghemokuai.sgmodule`、`Release/Ronghemokuai.sgmodule`、`Release/Module.sgmodule` |
| App 独立模块 | `Release/Modules/*.sgmodule`，用于按 App 选择导入，不是多版本路线 |

仓库不再保留 Stable、Stable Plus、Lite 和 Full 作为活跃 profile、Release 产物或发布路线。旧四版本仅作为 Git 历史中的 legacy reference 追溯，不应重新出现在 README、导入页、默认 workflow、健康检查或发布报告中。

## Fusion 分层

Fusion 以 source-first 分层维护，主要来源包括：

| 层 | 用途 |
|---|---|
| core | Spotify、YouTube、知乎等核心专项 |
| app-clean | 通用低风险 JSON 净化 |
| legacy-reviewed | 已审查的兼容规则 |
| qingrex | 小程序 / App 净化规则 |
| selected extensions | 有说明和回滚路径的扩展覆盖 |
| app sources | `Rewrite/Sources/Apps/*.conf` |
| misc sources | `Rewrite/Sources/Misc/*.conf` |
| remote sources | `Rewrite/Remotes/*.json` 管理的低风险远程规则 |

## 安全边界

Fusion 不应包含这些内容：

- 会员解锁、付费功能绕过、登录绕过、支付绕过。
- 银行、支付、验证码、证书校验、账号安全链路的激进改写。
- Cookie、Token、Authorization 的读取、伪造或泄露。
- 未知来源、不可回滚或不可审计的脚本。
- 未经专项审查的 request-body、binary、protobuf 类 body 脚本。

登录、支付、银行、验证码、视频播放、图片/CDN 和核心 API 属于高风险保护链路。相关调整必须先记录风险，再做 source-first 单点修改，并运行完整质量门禁。

## 自动维护边界

自动化可以执行：

- 拉取低风险远程规则和已登记 App 源。
- 运行语法、生成、治理、风险和健康校验。
- 构建 Fusion、Root、Release、Android、Windows、Web 和 reports。
- 使用明确路径提交生成产物，并通过 fetch + rebase + retry 推送。

自动化不应执行：

- 未经风险门禁的高风险 App 整包替换。
- 自动导入会员、登录、支付、账号绕过类模块。
- 未经证据的批量删除、批量放行或大范围 MITM 变更。

## 必须验证

常规发布前至少运行：

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release --check
python3 scripts/quality_gate.py
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

Android 相关变更还应运行：

```bash
python3 scripts/build_android_rules.py
python3 scripts/android_format_check.py
```

## 回滚原则

- Root / Release 不一致时，重新运行 Builder 和 `factory_finalize.py --sync-root`。
- Fusion 某层出现问题时，优先在源文件或 profile 中禁用对应来源，再重建。
- 远程规则源失效时，优先禁用或替换该源，不通过删除整层规避。
- 高风险 App 应保留备份和回滚路径。
- 回滚后仍需运行模块构建、仓库验证、远程规则语法和健康检查。
