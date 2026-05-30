# 脚本清单与瘦身分析报告

生成时间：待 Repository Health Check 自动刷新

本报告只做静态分析，不删除、不合并、不禁用任何脚本。减少脚本前必须先完成真机测试和回滚准备。

## 总体统计

- 脚本入口总数：当前稳定版约 104 个，待自动脚本刷新精确统计。
- 识别到的 App / 服务方向数量：待自动脚本刷新。
- 重复脚本名：待自动脚本刷新。
- 多入口共用同一 script-path：待自动脚本刷新。

## 分类统计

- 必须独立保留：Spotify、YouTube、知乎、protobuf / binary body、核心专项和安全边界相关脚本。
- 可合并候选：普通 App JSON 清理、弹窗、信息流、推荐位清理脚本。
- 可改规则候选：不依赖 body 的广告接口、开屏素材、统计接口。
- 需要人工复核：静态分析无法判断的脚本。

## 当前保守结论

1. 先不要删除任何脚本。
2. Spotify、YouTube、知乎不参与第一轮合并。
3. 普通 App JSON 去广告脚本可以作为第一批合并候选。
4. 不依赖 body 的请求或广告素材接口可以评估迁移到 Rule / URL Rewrite。
5. 所有合并必须先在 Stable Plus 灰度，不直接进入 Stable。

## 待自动刷新项目

Repository Health Check 接入后，会由 `scripts/generate_script_inventory_report.py` 自动生成以下内容：

- 来源统计。
- 文件分布。
- 重复脚本名。
- 多入口共用同一 script-path。
- 可合并候选摘要。
- 可改规则候选摘要。
- 全量脚本清单。

## 下一步建议

1. 第一阶段只处理重复 script-path 和明显普通 JSON 清理脚本。
2. 设计统一 `app-cleaner.js` 和配置表，不直接删除旧入口。
3. 通过 `stable-plus` 做灰度验证，确认无异常后再减少入口。
4. 能用 Rule / URL Rewrite 解决的静态广告接口，应从脚本迁移到规则层。
5. 每次减少脚本后都要重新生成四个 Release 版本，并更新测试记录。
