# Scripts

本目录用于保存**可部署的 JavaScript 脚本文件**、脚本配置片段和脚本来源说明。

注意区分两个目录：

```text
Scripts/   # 大写：模块运行时使用的 JS 脚本与脚本说明
scripts/   # 小写：仓库构建、审计、报告、校验用 Python / Shell 工具
```

## 当前定位

`Scripts/` 对应仓库结构图里的“已部署 JavaScript 文件”目录，但当前仓库仍允许两类内容并存：

```text
*.js      # 本地保存、可被模块引用的 JavaScript 脚本
*.conf    # 脚本相关配置或来源整理片段
*.md      # 脚本来源、用途、风险和维护说明
```

远程脚本可以继续通过模块里的 `script-path=` 引用上游地址，但必须在 `Rewrite/Remotes/` 或 `Rewrite/Registry.md` 中登记来源、用途和风险。

## 与生成流程的关系

```text
Scripts/                       # 本地脚本资产与脚本说明
Rewrite/Sources/Script.conf     # 模块 Script 段源片段
Rewrite/Generator/Builder.py    # 统一构建入口
Release/Module.sgmodule         # 生成后的模块别名
Ronghemokuai.sgmodule           # 公开主入口
```

## 维护原则

- 不保存未知来源、无法审计的混淆脚本。
- 不加入破解、解锁、支付绕过、登录绕过脚本。
- Spotify、YouTube、知乎等核心脚本必须保留来源说明和回滚路径。
- 新脚本先进入候选或说明文件，确认稳定后再接入正式模块。
- 远程脚本失效时先进入报告，再人工确认替换，不自动替换成未知源。
- 修改脚本引用后，需要重新生成 Release 输出并检查 MITM hostname 是否同步。

## 建议的后续整理方向

如脚本继续增加，可以再拆分为：

```text
Scripts/JS/       # 本地 JS 文件
Scripts/Config/   # 脚本配置片段
Scripts/Docs/     # 来源说明与风险记录
```

当前阶段先保持现有文件兼容，不强制移动已有脚本文件，避免破坏历史引用路径。

## 脚本聚合器

`Scripts/generated/fusion-script-bundle.js` 由 `scripts/build_module.py` 自动生成，不要手工修改。

聚合器只打包低风险的 `http-response` 清理脚本：必须依赖响应 body，且不能带 `binary-body-mode` 或自定义 `argument`。Spotify、YouTube、Bilibili protobuf、知乎、登录、支付、银行、钱包、航旅和账号相关脚本会继续保持独立入口。

聚合器同时生成 `Scripts/generated/fusion-script-bundle.manifest.json`，记录每个被聚合脚本的名称、上游 URL、来源哈希、所在 bundle chunk 和保护策略。`tools/validate_script_aggregation.py` 会校验 manifest、bundle、Release 脚本入口是否一致，`tools/test_script_bundle_sandbox.py` 会用 Shadowrocket 风格的 `$request` / `$response` / `$done` 沙箱逐路由验证 bundle。若上游脚本命中后没有调用 `$done`，bundle 会自动 pass-through，避免客户端等待。验证报告位于 `reports/script_aggregation_validation_report.md` 和 `reports/script_bundle_sandbox_report.md`，聚合摘要位于 `reports/script_aggregation_report.md`。

如果某个 App 在聚合后出现异常，应在 `scripts/build_module.py` 中收窄 allowlist 或加入 preserve token，然后重新构建：

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release --check
```
