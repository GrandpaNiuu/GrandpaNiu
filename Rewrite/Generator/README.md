# Generator

本目录用于放置模块生成器相关说明和脚本。

推荐后续生成流程：

```text
Rewrite/Sources/*
Rules/*
Scripts/*
Rewrite/Manifest.conf
        ↓
scripts/build_module.py
        ↓
Release/Ronghemokuai.sgmodule
```

当前阶段只建立框架，不直接替换根目录 `Ronghemokuai.sgmodule`。

生成器设计原则：

- 只负责拼接和校验，不主动改写规则语义。
- 生成前检查 `[Rule]`、`[Script]`、`[MITM]` 是否存在。
- 生成后检查 Spotify / YouTube 核心项是否保留。
- 生成结果先输出到 `Release/`，确认无误后再考虑同步到根目录主模块。
