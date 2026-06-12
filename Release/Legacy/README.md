# Release Legacy Entries

本目录用于说明旧 Release 入口的兼容策略。

旧入口不是当前公开版本体系，只用于兼容历史链接，避免老用户导入地址突然失效。

## 旧入口文件

```text
Release/Ronghemokuai-full.sgmodule
Release/Ronghemokuai-lite.sgmodule
Release/Ronghemokuai-stable-plus.sgmodule
Release/Ronghemokuai-stable.sgmodule
```

## 当前正式入口

```text
Ronghemokuai.sgmodule
Release/Ronghemokuai.sgmodule
Release/Module.sgmodule
Release/Rules.conf
Release/RulesGroup.conf
Release/Modules/
Release/Android/
```

## 维护原则

- 旧 full / lite / stable / stable-plus 文件不再作为公开 catalog 条目。
- 不继续扩展多版本路线；当前策略是 Fusion 单一融合模块。
- 旧文件如保留在根 `Release/` 下，只作为兼容占位。
- 不在旧文件里加入新功能；新功能必须从 `Rewrite/Sources/`、`Rules/`、`Scripts/` 等源目录进入生成流程。
- `Web/release-links.json` 只登记当前正式入口和 App 独立模块，不登记 deprecated legacy 文件。
