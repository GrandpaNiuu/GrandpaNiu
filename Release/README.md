# Release

本目录存放生成后的发布文件，不是规则维护入口。

统一生成命令：

`python3 Rewrite/Generator/Builder.py --profile fusion --release`

## 当前发布入口

```text
Ronghemokuai.sgmodule
Release/Ronghemokuai.sgmodule
Release/Module.sgmodule
Release/Rules.conf
Release/RulesGroup.conf
Release/Modules/
Release/Android/
```

只维护 Fusion 主模块。旧版多 profile 的 Release 文件已经移除；不再提供兼容占位或独立测试版本。

## Source of truth

```text
Rules/
Scripts/
Rewrite/Sources/
Rewrite/Remotes/
Rewrite/Profiles/fusion.conf
Android/
```

改源文件，不直接改 Release 输出。重新生成后检查主模块、兼容别名、规则文件和 App 独立模块。
