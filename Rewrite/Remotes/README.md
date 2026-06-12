# Rewrite/Remotes

本目录用于管理**上游来源治理**，包括远程规则源、远程脚本源、候选源、来源索引和风险说明。

它不是最终发布目录，也不是必须完整镜像所有上游 JavaScript 的目录。当前设计是：优先保存来源索引和审计信息；只有在需要固定版本、避免上游失效或做风险审查时，才保存上游原始脚本副本。

## 当前定位

```text
Rewrite/Remotes/Index.md       # 上游来源总索引
Rewrite/Remotes/Catalog.md     # 上游来源目录说明
Rewrite/Remotes/sources.json   # 已采用来源清单
Rewrite/Remotes/candidates.json# 候选来源清单
Rewrite/Remotes/Scripts/       # 可选：下载并固化的上游 JavaScript 原文件
```

## 与图片框架的对应关系

图片中的 `Remotes/` 标注为“下载的上游 JavaScript 原文件”。本仓库当前采用更安全的做法：

```text
默认：记录上游来源、用途、风险、回滚路径
必要时：再把上游 JS 固化到 Rewrite/Remotes/Scripts/
```

这样可以避免盲目搬运未知脚本，同时保留后续固定版本和离线审计能力。

## 收录原则

- 已采用来源写入 `sources.json`。
- 待观察来源写入 `candidates.json`。
- 来源说明同步维护到 `Index.md` 或 `Catalog.md`。
- 高风险、失效、误杀明显或来源不明的内容不得直接进入正式源。
- 若保存上游 JS 原文件，必须记录原始 URL、来源项目、更新时间、用途、风险和回滚方式。

## 与生成流程的关系

```text
Rewrite/Remotes/       # 来源治理与候选来源
Rewrite/Sources/       # 正式源片段
Rewrite/Registry.md    # 脚本 / 规则来源归属登记
Rewrite/Generator/     # 构建器
Release/               # 生成输出
```

`Release/` 不应直接依赖未登记的远程脚本或规则源。
