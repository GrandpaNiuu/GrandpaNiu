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

## 必跑命令

修改源头文件后至少运行：

```text
python3 -m py_compile scripts/build_module.py scripts/factory_finalize.py scripts/audit_repair_invalid_sources.py scripts/collect_upstreams.py scripts/validate_repository.py scripts/repository_health_check.py
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

## 发布前人工测试

每次大改后测试：

```text
Shadowrocket 更新模块
Shadowrocket 更新脚本
Spotify 连续播放 10 首歌
YouTube 首页 / 搜索 / 播放 / Shorts
知乎首页 / 回答页 / 搜索页
Bilibili 首页 / 搜索 / 播放页
淘宝 / 京东 / 拼多多基础浏览
微信 / 支付宝 / 银行 App 登录、支付、验证码
```

## 自动化对应关系

| 检查 | 文件 / 工作流 |
|---|---|
| 构建主模块 | `.github/workflows/module-factory-build.yml` |
| 每日基础检查 | `.github/workflows/daily-module-update.yml` |
| 失效源审计 | `.github/workflows/daily-invalid-source-repair.yml` |
| 候选源收集 | `.github/workflows/upstream-collect.yml` |
| 仓库健康检查 | `.github/workflows/repository-health.yml` |
| 阻断校验 | `scripts/validate_repository.py` |
| 健康报告 | `scripts/repository_health_check.py` |

## 处理原则

```text
先报告，再修复。
先源头，再主模块。
先替换，再注释，最后删除。
先小步提交，再观察。
脚本比规则风险高，脚本默认 pending。
播放、登录、支付、验证码优先保护。
```
