# Rewrite Registry

本文件用于登记模块片段来源、用途、状态和风险级别。

| 分类 | 文件 | 用途 | 状态 | 备注 |
|---|---|---|---|---|
| Rule | Rewrite/Sources/Rule.conf | 主规则区块拆分片段 | 待拆分 | 来源为 Ronghemokuai.sgmodule |
| URL Rewrite | Rewrite/Sources/URL-Rewrite.conf | URL 重写片段 | 待拆分 | 后续从主模块迁移 |
| Header Rewrite | Rewrite/Sources/Header-Rewrite.conf | Header 重写片段 | 待拆分 | Spotify 相关内容需重点保护 |
| Body Rewrite | Rewrite/Sources/Body-Rewrite.conf | Body 重写片段 | 待拆分 | 仅保留广告净化用途 |
| Map Local | Rewrite/Sources/Map-Local.conf | 本地映射片段 | 待拆分 | 避免误伤播放、登录、支付 |
| Script | Rewrite/Sources/Script.conf | 脚本片段 | 待拆分 | Spotify / YouTube 不自动删除 |
| MITM | Rewrite/Sources/MITM.conf | MITM hostname 片段 | 待拆分 | 使用 %APPEND% 保持兼容 |
| Remote | Rewrite/Remotes/Index.md | 远程规则源索引 | 已建立 | 只登记可信来源 |

维护要求：

- 新增来源必须能访问、能验证、用途明确。
- 不登记未知混淆脚本、短链、镜像站、破解类来源。
- Spotify / YouTube 相关内容只允许人工确认后调整。
- 失效来源先写入报告，再决定替换、注释或删除。
