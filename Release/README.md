# Release

本目录存放**生成后的发布文件**。`Release/` 不是源目录，不应直接作为规则或模块的维护入口。

统一生成命令：

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
```

## 标准发布结构

当前仓库对齐图片里的标准输出结构：

```text
Release/
  Rules.conf
  RulesGroup.conf
  Module.sgmodule
  Modules/
```

对应说明：

```text
Release/Rules.conf       # 生成后的规则输出
Release/RulesGroup.conf  # 生成后的规则组输出
Release/Module.sgmodule  # Release 目录内的模块兼容别名
Release/Modules/         # 按应用拆分的独立诊断 / 便利用模块
```

## 当前主要发布入口

```text
Ronghemokuai.sgmodule              # 根目录公开主入口
Release/Ronghemokuai.sgmodule      # Release 内主模块文件
Release/Module.sgmodule            # 兼容别名，复制自 Release/Ronghemokuai.sgmodule
Release/Rules.conf                 # 规则输出
Release/RulesGroup.conf            # 规则组输出
Release/Modules/                   # App 独立模块
Release/Android/                   # Android 输出
```

公开目录：

```text
https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
https://grandpaniuu.github.io/GrandpaNiu/Release/Module.sgmodule
https://grandpaniuu.github.io/GrandpaNiu/Web/catalog.md
https://grandpaniuu.github.io/GrandpaNiu/Web/release-links.json
```

## Legacy 旧入口策略

以下旧文件只作为历史链接兼容占位，不再作为公开版本体系维护：

```text
Release/Ronghemokuai-full.sgmodule
Release/Ronghemokuai-lite.sgmodule
Release/Ronghemokuai-stable-plus.sgmodule
Release/Ronghemokuai-stable.sgmodule
```

处理原则：

- 不加入 `Web/release-links.json` 的公开 catalog。
- 不作为 Stable / Lite / Full 多版本路线继续扩展。
- 如仍保留在根 `Release/` 下，只用于避免旧链接失效。
- 旧入口说明集中放在 `Release/Legacy/README.md`。

## Source of truth

```text
Rules/                    # 纯规则源
Scripts/                  # 本地脚本资产与脚本说明
Rewrite/Sources/          # 模块正式源片段
Rewrite/Sources/Apps/     # 按应用拆分源片段
Rewrite/Sources/Misc/     # 通用补充源片段
Rewrite/Remotes/          # 上游来源治理
Rewrite/Registry.md       # 来源归属、风险和回滚索引
Rewrite/Profiles/         # Profile 配置
Rewrite/Generator/        # 构建器
Android/                  # Android 源文件
```

## 维护规则

- 改源文件，不直接改 Release 输出。
- 生成后再检查 `Release/Module.sgmodule`、`Release/Ronghemokuai.sgmodule`、`Release/Rules.conf`、`Release/RulesGroup.conf`。
- 公开入口以 Fusion 单一融合模块为主。
- `Release/Modules/` 是诊断和便利用途，不代表新版本线。
