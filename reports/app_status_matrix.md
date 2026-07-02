# App 状态矩阵

生成时间：2026-07-03 04:39:05 +0800

本矩阵是自动化质量总览。状态只表达仓库源头是否被自动扫描覆盖，以及是否满足可回滚、可审计的发布边界。

| App 名称 | 所属类别 | 覆盖来源 | 所属入口 | 自动状态 | 风险等级 | 证据来源 | 发布策略 | 回滚路径 | 备注 |
|---|---|---|---|---|---|---|---|---|---|
| Spotify | 音乐 | MITM, Remote, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| YouTube | 视频 | MITM, Remote, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 知乎 | 内容社区 | MITM, Remote, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| Bilibili | 视频 | MITM, Remote, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 微博 | 社交 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 百度贴吧 | 社交 | MITM, Remote, Rewrite, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 小红书 | 社交电商 | MITM, Remote, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 酷安 | 工具社区 | MITM, Rewrite, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 淘宝 | 电商 | MITM, Remote, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 闲鱼 | 电商 | MITM, Rewrite, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 京东 | 电商 | MITM, Remote, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 拼多多 | 电商 | MITM, Remote, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 美团 | 本地生活 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 大众点评 | 本地生活 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 饿了么 | 本地生活 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 滴滴 | 出行 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 12306 | 出行 | Rewrite, Rule, Script | 未确认 | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 高德地图 | 地图 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 百度地图 | 地图 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 网易云音乐 | 音乐 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 喜马拉雅 | 音频 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 小宇宙 | 音频 | MITM, Rewrite, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 斗鱼 | 直播 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 中 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| Reddit | 社交 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 低 | automated_quality_evidence.md / 静态扫描 | 随 Fusion 自动门禁发布 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 微信 | 社交 / 支付 / 小程序 / 图片 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 支付宝 | 支付 | Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 银行 / 验证码 | 安全敏感 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 图片 CDN | 资源加载 | MITM, Rewrite, Rule, Script | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |
| 小程序资源 | 微信生态 | Rule | fusion | 自动门禁覆盖 | 高 | automated_quality_evidence.md / 静态扫描 | 保留保护优先、需可回滚源头 | 回滚 Rules 中对应源头后重建 | 覆盖不等于效果承诺；用户反馈只进入 Issue 或后续修复输入 |

## 发布边界

- 静态覆盖不得写成效果承诺。
- 用户反馈不是发布阻断门禁；它只作为 Issue、回滚或修复输入。
- 高风险 App 保持保护规则优先、回滚路径明确、自动门禁通过。
- Fusion 是唯一公开入口；兼容目录只由构建器同步。
