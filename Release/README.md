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

只维护 Fusion 主模块。用户不需要选择 Stable、Stable Plus、Lite 或 Full。

`Release/Stable/` 仅由构建器生成，用于旧链接兼容；它与当前 Fusion 内容同步，不是第二个公开版本。`Release/Beta/` 和 `Release/Canary/` 只是保留目录，不发布模块产物。

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
