# 模块工厂流程

本文是当前仓库唯一权威的模块工厂说明。

## 完整流程

```text
Profiles + Remotes + Rules + Scripts + Rewrite/Sources
        ↓
scripts/build_module.py
        ↓
Release/Ronghemokuai.sgmodule
        ↓
scripts/factory_finalize.py
        ↓
Ronghemokuai.sgmodule
```

根目录 `Ronghemokuai.sgmodule` 始终是 Shadowrocket / Surge 正式导入入口，必须保留：

```text
#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

## 目录职责

| 路径 | 职责 |
|---|---|
| `Rewrite/Profiles/stable.conf` | 当前唯一稳定构建 profile。 |
| `Rewrite/Remotes/sources.json` | 机器可读远程 `RULE-SET` / `DOMAIN-SET` 清单。 |
| `Rules/*.list` | 本地规则源，参与 `[Rule]` 构建。 |
| `Scripts/*.conf` | 脚本源，参与 `[Script]` 构建。 |
| `Rewrite/Sources/*.conf` | 从主模块拆分出的过渡兼容片段，保留 Meta、Rule、Rewrite、Script、MITM 等区块。 |
| `scripts/build_module.py` | 读取 profile、remotes、rules、scripts、sources，生成 `Release/Ronghemokuai.sgmodule` 和工厂报告。 |
| `scripts/factory_finalize.py` | 拆分 Rules / Scripts，并把 Release 同步回根目录主模块。 |
| `Release/Ronghemokuai.sgmodule` | 工厂生成的发布副本。 |
| `reports/` | 构建、差异、最终同步、每日检查和失效源审计报告。 |

## 工作流顺序

主工作流是 `.github/workflows/module-factory-build.yml`，执行顺序为：

```text
python3 scripts/build_module.py --extract-from-root --build --profile stable
python3 scripts/factory_finalize.py
```

工作流会验证：

```text
[Rule]
[Script]
[MITM]
spotify-json
spotify-proto
youtube.response
#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

验证失败时工作流应直接失败，不提交损坏模块。

## 报告输出

| 报告 | 内容 |
|---|---|
| `reports/module_factory_report.md` | 构建 profile、来源、行数、重复项检查。 |
| `reports/module_factory_diff_report.md` | Root 与 Release 的 diff，finalize 后应为 0。 |
| `reports/factory_finalize_report.md` | Rules / Scripts 拆分数量和 Root / Release 同步结果。 |
| `reports/repository_cleanup_report.md` | 仓库结构、清理结果和仍需人工测试的风险项。 |

## Root 与 Release 同步

`build_module.py` 只生成 `Release/Ronghemokuai.sgmodule`。

`factory_finalize.py` 负责：

1. 从 `Rewrite/Sources/Rule.conf` 拆分 `Rules/*.list`。
2. 从 `Rewrite/Sources/Script.conf` 拆分 `Scripts/*.conf`。
3. 校验 Release 中的核心区块和核心脚本。
4. 将 `Release/Ronghemokuai.sgmodule` 同步到根目录 `Ronghemokuai.sgmodule`。
5. 生成 `reports/factory_finalize_report.md`。
6. 重新生成同步后的 `reports/module_factory_diff_report.md`。

正常状态下 Root 与 Release 应完全一致；如存在差异，必须在报告中说明原因。

## Spotify / YouTube 分类

- `Scripts/spotify.conf` 只保留 `spotify-json`、`spotify-proto` 或明确 Spotify / spclient 相关脚本。
- `Scripts/youtube.conf` 只保留 `youtube.response` 或明确 YouTube / Maasea 相关脚本。
- Tieba、QQ News、VGTime、普通 app2smile、fmz200 / wool_scripts、zirawell / R-Store 脚本进入 `Scripts/app-clean.conf`。
- Spotify 播放链路保护规则进入 `Rules/spotify-direct.list`，不得放进 REJECT。
- YouTube 精准保护规则进入 `Rules/youtube-direct.list`，不得无脑 DIRECT 所有 Google / YouTube 域名。

## 自动维护边界

- `daily-module-update.yml` 只更新日期、检查关键结构和生成每日报告。
- `daily-invalid-source-repair.yml` 连续 2 天确认失效后才处理，优先同源替换，其次注释，最后才低风险删除。
- Spotify、YouTube、主模块地址、安装页、导入页和核心远程规则源只报告，不自动破坏。

## 不加入工具痕迹文件

仓库不加入 `.claude`、`CLAUDE.md` 等特定工具配置文件。它们不参与模块工厂流程，也会让公开仓库混入无关工具痕迹。

## 后续维护方式

1. 修改规则或脚本时，优先改 `Rules/`、`Scripts/`、`Rewrite/Remotes/sources.json`。
2. 保留 `Rewrite/Sources/` 作为过渡兼容层，不随意删除。
3. 修改后运行工厂命令并检查 Root / Release 是否一致。
4. 检查 Spotify、YouTube、登录、支付、验证码和常用 App 基础功能。
5. 所有自动修复必须可回滚，无法确认安全时只写报告。
