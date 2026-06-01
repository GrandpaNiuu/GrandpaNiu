# App 状态矩阵

生成时间：2026-06-02 00:29:06 +0800

本矩阵是质量总览，不把静态覆盖写成已经验证。真实测试来源只允许来自 `reports/manual_test_log.md`；没有记录时一律标记为“未测”。

| App 名称 | 所属类别 | 覆盖来源 | 所属版本 | 测试状态 | 风险等级 | 最近测试日期 | 测试来源 | 是否允许进入 Stable | 回滚路径 | 备注 |
|---|---|---|---|---|---|---|---|---|---|---|
| Spotify | 音乐 | MITM, Remote, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 中 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| YouTube | 视频 | MITM, Remote, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 中 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 知乎 | 内容社区 | MITM, Remote, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 中 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| Bilibili | 视频 | MITM, Remote, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 中 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 微博 | 社交 | MITM, Rewrite, Script | stable, stable-plus, full | 未测 | 中 | 未记录 | 无真实记录 | 未测，不允许晋级 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 百度贴吧 | 社交 | MITM, Remote, Rewrite, Script | stable, stable-plus, full | 未测 | 中 | 未记录 | 无真实记录 | 未测，不允许晋级 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 小红书 | 社交电商 | MITM, Remote, Rewrite, Rule, Script | stable, stable-plus, lite, full | 未测 | 中 | 未记录 | 无真实记录 | 未测，不允许晋级 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 酷安 | 工具社区 | MITM, Rewrite, Script | stable, stable-plus, full | 未测 | 中 | 未记录 | 无真实记录 | 未测，不允许晋级 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 淘宝 | 电商 | MITM, Remote, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 闲鱼 | 电商 | MITM, Rewrite, Script | stable, stable-plus, full | 通过 | 中 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过 | 回滚 Rewrite、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 京东 | 电商 | MITM, Remote, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 拼多多 | 电商 | MITM, Remote, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 美团 | 本地生活 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 大众点评 | 本地生活 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 饿了么 | 本地生活 | MITM, Rewrite, Script | stable, stable-plus, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 滴滴 | 出行 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 12306 | 出行 | Rewrite, Rule, Script | stable, stable-plus, full | 未测 | 高 | 未记录 | 无真实记录 | 未测或高风险，需人工复核 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 高德地图 | 地图 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 未测 | 高 | 未记录 | 无真实记录 | 未测或高风险，需人工复核 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 百度地图 | 地图 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 未测 | 高 | 未记录 | 无真实记录 | 未测或高风险，需人工复核 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 网易云音乐 | 音乐 | MITM, Rewrite, Rule | stable, stable-plus, lite, full | 未测 | 中 | 未记录 | 无真实记录 | 未测，不允许晋级 | 回滚 Rewrite、Rules 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 喜马拉雅 | 音频 | MITM, Rewrite, Rule, Script | stable, stable-plus, full | 通过 | 中 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 小宇宙 | 音频 | MITM, Rewrite, Script | stable, stable-plus, full | 未测 | 中 | 未记录 | 无真实记录 | 未测，不允许晋级 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 斗鱼 | 直播 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 中 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| Reddit | 社交 | MITM, Rewrite, Script | stable, stable-plus, full | 未测 | 低 | 未记录 | 无真实记录 | 未测，不允许晋级 | 回滚 Rewrite、Scripts 中对应源头后重建 | 覆盖存在不等于测试通过；未测必须保持未测 |
| 微信 | 社交 / 支付 / 小程序 / 图片 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 支付宝 | 支付 | Rewrite | 未确认 | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 银行 / 验证码 | 安全敏感 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 图片 CDN | 资源加载 | MITM, Rewrite, Rule, Script | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rewrite、Rules、Scripts 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |
| 小程序资源 | 微信生态 | Rule | stable, stable-plus, lite, full | 通过 | 高 | 2026-06-01 | manual_test_log.md / 用户确认 | Stable 第一轮通过；后续敏感链路变更仍需复测 | 回滚 Rules 中对应源头后重建 | 用户确认，不是助手亲测；大改后仍需复测 |

## 晋级边界

- 未测试不得写通过。
- 本次 Stable 第一轮通过来源为 `manual_test_log.md / 用户确认`，不是助手亲测。
- 微信、支付宝、银行、验证码、支付、图片 CDN、小程序默认高风险；即使本轮通过，后续涉及这些链路的规则变更仍需重新测试。
- Stable Plus 中的内容只有真实测试通过后，才能进入单项晋级流程。
- 不允许把 Stable Plus 整体合并进 Stable，只能单项 App 晋级。
