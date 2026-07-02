# 本地维护环境

GrandpaNiu 当前只维护 Fusion 单一模块。

日常修改应发生在 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Remotes/` 和 `Rewrite/Profiles/fusion.conf`。

`Release/`、`Web/`、`reports/`、根目录模块文件都是构建结果，不应长期手工修改。

推荐在本地准备 Git、Python 3.10+ 和 Node.js LTS，并使用 Fusion 构建器和质量门完成验证。

旧的 Stable、Stable Plus、Lite 与 Full 配置和发布文件已经移除；历史状态通过 Git 记录追溯。
