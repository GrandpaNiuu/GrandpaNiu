# 发布与回滚

本仓库只发布 Fusion 模块。

公开入口为 `Ronghemokuai.sgmodule`，生成副本为 `Release/Ronghemokuai.sgmodule`，`Release/Module.sgmodule` 仅是兼容别名。三者必须保持一致。

发布前使用 Fusion 构建器生成产物，并完成仓库验证、质量门和健康检查。

不再发布或回滚到 Stable、Stable Plus、Lite 或 Full 文件。出现问题时，应回滚对应源规则、脚本或 MITM 片段，再重新构建 Fusion。
