# 质量门禁标准

本文件定义 GrandpaNiu 仓库的阻断检查、提醒检查和上线标准。

## 质量门禁目标

仓库的目标不是单纯堆规则，而是保持：

```text
可导入
可构建
可验证
可回滚
可长期维护
低误杀
安全边界清楚
远程规则语法兼容
```

## 阻断项

出现以下任一问题时，不应发布主模块：

1. `Ronghemokuai.sgmodule` 与 `Release/Ronghemokuai.sgmodule` 不一致。
2. 主模块缺少 `[Rule]`、`[Script]`、`[MITM]`。
3. 主模块缺少 `[URL Rewrite]`、`[Header Rewrite]`、`[Body Rewrite]`、`[Map Local]`。
4. 缺少 `spotify-json` 或 `spotify-proto`。
5. 缺少 `youtube.response`。
6. 缺少 `zhihu-enhance`。
7. `update-url` 不正确。
8. `Scripts/spotify.conf` 混入普通 App 脚本。
9. `Scripts/youtube.conf` 混入普通 App 脚本。
10. `Rules/spotify-direct.list` 出现 `REJECT`。
11. 存在重复脚本名。
12. 存在重复 MITM hostname。
13. `sources.json` 或 `candidates.json` JSON 格式错误。
14. 启用的远程源使用短链、代理、镜像或非 HTTPS。
15. README 本地链接失效。
16. 出现 `.claude`、`CLAUDE.md` 等工具痕迹文件。
17. `RULE-SET` 远程内容下载失败、下载到 HTML/404、空文件或混入不兼容规则语法。
18. `DOMAIN-SET` 远程内容不是纯域名集合，或混入带逗号规则行。
19. 发现 Quantumult X 的 `host`、`host-suffix`、`host-keyword`、`ip6-cidr` 被直接作为 Shadowrocket `RULE-SET` 引用。
20. 未经单项测试和人工审查，将 Full 或 Stable Plus 内容批量晋级 Stable。

## 提醒项

提醒项不一定阻断发布，但需要观察：

1. 某个远程源首次失败。
2. 候选源连续被跳过。
3. `Script` 行数快速增加。
4. `MITM hostname` 数量快速增加。
5. 知乎、YouTube、Bilibili 等高频接口新增 Body Rewrite。
6. Shadowrocket 电池占比超过 10%。
7. 用户反馈登录、支付、验证码异常。
8. `lite.conf` 长期未测试。
9. `reports/manual_test_log.md` 长期没有新增真实测试记录。

## 必跑命令

修改源头文件后至少运行：

```text
python3 -m py_compile scripts/build_module.py scripts/build_release_variants.py scripts/factory_finalize.py scripts/audit_repair_invalid_sources.py scripts/collect_upstreams.py scripts/validate_repository.py scripts/validate_remote_rule_syntax.py scripts/repository_health_check.py
python3 scripts/convert_quanx_rules.py
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_remote_rule_syntax.py
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

## 发布前人工测试

每次大改后测试：

```text
Shadowrocket 更新模块
Shadowrocket 更新脚本
Shadowrocket 更新全部资源
Stable 与 Lite 对照测试
Spotify 连续播放 10 首歌
YouTube 首页 / 搜索 / 播放 / Shorts
知乎首页 / 回答页 / 搜索页
Bilibili 首页 / 搜索 / 播放页
淘宝 / 京东 / 拼多多基础浏览、商品图、搜索、订单前置
微信发图 / 收图 / 朋友圈 / 公众号图片 / 小程序 / 支付前置页
支付宝 / 银行 App 登录、验证码、支付前置流程
高德 / 百度地图搜索、定位、路线规划
```

测试结果必须进入 `reports/manual_test_log.md`。没有真实测试记录时，不得在报告中写“通过”。

## 远程规则语法门禁

`validate_remote_rule_syntax.py` 是阻断检查，不是提醒检查。

检查范围：

- 根目录模块。
- Release 主模块。
- Stable / Stable Plus / Lite / Full 四个独立发布文件。
- `Rules/aggressive-ad-sources.list`。
- `Rules/original-remote-rule-sets.list`。
- `Rewrite/Remotes/sources.json` 中启用的远程规则。

处理规则：

- 上游是 QuanX 格式时，必须先用 `scripts/convert_quanx_rules.py` 转换到 `Rules/converted/` 后再引用。
- 不允许把 QuanX 原始 `host` / `host-suffix` / `host-keyword` 直接放入 Shadowrocket `RULE-SET`。
- 仓库自己的 Pages / raw 链接由校验器优先映射到本地文件，避免 workflow 读到旧缓存。
- 出现失败时，优先修源头，不要只手动修改 Release 成品。

## Full 冻结边界

Full 是排查版，不是候选发布池。

- Full 不允许作为默认发布。
- Full 不允许整体合并进 Stable。
- Full 中任何规则、脚本、MITM 要进入 Stable，必须按单项 App / 单类规则 / 单组 hostname 提交晋级。
- 晋级必须带：影响范围、测试记录、回滚路径、误伤风险说明。
- 未经测试的 Full 内容只能保持排查用途。

## 自动化对应关系

| 检查 | 文件 / 工作流 |
|---|---|
| 构建主模块 | `.github/workflows/module-factory-build.yml` |
| QuanX 规则转换 | `scripts/convert_quanx_rules.py` |
| 远程规则语法阻断校验 | `scripts/validate_remote_rule_syntax.py` |
| 每日基础检查 | `.github/workflows/daily-module-update.yml` |
| 失效源审计 | `.github/workflows/daily-invalid-source-repair.yml` |
| 候选源收集 | `.github/workflows/upstream-collect.yml` |
| 仓库健康检查 | `.github/workflows/repository-health.yml` |
| 阻断校验 | `scripts/validate_repository.py` |
| 健康报告 | `scripts/repository_health_check.py` |
| 真机测试记录 | `reports/manual_test_log.md` |
| 远程规则语法报告 | `reports/remote_rule_syntax_report.md` |

## 处理原则

```text
先报告，再修复。
先源头，再主模块。
先替换，再注释，最后删除。
先小步提交，再观察。
脚本比规则风险高，脚本默认 pending。
远程规则先校验语法，再谈覆盖效果。
Full 只用于排查，不用于批量晋级。
播放、登录、支付、验证码优先保护。
```
