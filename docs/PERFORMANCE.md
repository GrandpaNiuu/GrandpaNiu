# 性能与耗电说明

本项目是融合模块，不是单一规则列表。性能和耗电主要受以下因素影响：

- MITM hostname 数量。
- Body Rewrite。
- http-response 脚本。
- 大型 JSON 响应处理。
- 高频 App 请求。
- 远程规则数量。

## Profile

| Profile | 定位 |
|---|---|
| `stable.conf` | 默认正式版，功能和稳定性平衡。 |
| `lite.conf` | 低耗电参考版，减少普通 App 脚本和兼容层。 |
| `full.conf` | 全覆盖测试版，不默认发布，适合人工验证更广覆盖。 |

## 观察方式

建议在 iPhone 设置中观察 Shadowrocket 的 24 小时电池占比：

- 1% - 3%：很轻。
- 3% - 8%：正常。
- 8% - 10%：偏重但可观察。
- 10% - 15%：需要排查高频脚本和 MITM。
- 15% 以上：建议测试 lite profile 或减少脚本。

## 调整原则

- 新脚本默认 pending。
- 高风险脚本不要直接进 stable。
- MITM hostname 必须最小化。
- 不常用 App 优先放到 full 测试，不默认进入 stable。
- Spotify、YouTube、知乎核心能力不因性能调整直接删除。

## 测试命令

```text
python3 scripts/build_module.py --build --profile fusion
python3 scripts/build_module.py --build --profile fusion
```

注意：构建 lite 或 full 会更新 `Release/Ronghemokuai.sgmodule`。正式发布前必须重新用 stable 构建并同步。
