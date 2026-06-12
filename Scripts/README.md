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
