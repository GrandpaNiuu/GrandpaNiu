# Release

本目录用于保存生成后的发布成品。

当前主发布入口仍然是仓库根目录的：

```text
Ronghemokuai.sgmodule
```

后续如果启用生成器流程，可以把生成结果输出到：

```text
Release/Ronghemokuai.sgmodule
```

维护原则：

- `Release/` 只放发布成品，不放原始规则片段。
- 不直接在 `Release/` 中手写复杂规则。
- 如生成结果异常，应回到 `Rewrite/Sources/`、`Rules/`、`Scripts/` 或主模块源文件排查。
