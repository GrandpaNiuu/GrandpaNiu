# Sources

本目录用于存放从主模块拆分出来的原始模块片段。

建议拆分目标：

```text
Rule.conf
URL-Rewrite.conf
Header-Rewrite.conf
Body-Rewrite.conf
Map-Local.conf
Script.conf
MITM.conf
```

当前阶段先建立目录，不直接拆分主模块内容。

后续迁移原则：

- 先复制拆分，不删除根目录主模块内容。
- 拆分后通过生成器生成 `Release/Ronghemokuai.sgmodule`。
- 对比生成结果与主模块一致后，再考虑正式启用生成流程。
