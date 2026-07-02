# 质量门禁标准

本文件定义 GrandpaNiu 仓库的阻断检查、提醒检查和 Fusion 发布标准。发布判断统一依赖自动化质量证据，不依赖旧版多 profile 的人工晋级记录。

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
8. `Scripts/spotify.conf` 或 `Scripts/youtube.conf` 混入不相关 App 脚本。
9. 存在重复脚本名或重复 MITM hostname。
10. `sources.json` 或 `candidates.json` JSON 格式错误。
11. 启用的远程源使用短链、代理、镜像或非 HTTPS。
12. README 本地链接失效。
13. 出现 `.claude`、`CLAUDE.md` 等工具痕迹文件。
14. `RULE-SET` 远程内容下载失败、下载到 HTML/404、空文件或混入不兼容规则语法。
15. `DOMAIN-SET` 远程内容不是纯域名集合，或混入带逗号规则行。
16. 发现 Quantumult X 的 `host`、`host-suffix`、`host-keyword`、`ip6-cidr` 被直接作为 Shadowrocket `RULE-SET` 引用。
17. 未经单项审查、自动化质量证据和可回滚源头，将候选或高风险扩展批量并入 Fusion。
18. 任一跟踪文本文件包含 UTF-8 BOM。
19. 缺少或未刷新 `reports/automated_quality_evidence.md`。

## 提醒项

提醒项不一定阻断发布，但需要观察：

1. 某个远程源首次失败。
2. 候选源连续被跳过。
3. `Script` 行数快速增加。
4. `MITM hostname` 数量快速增加。
5. 知乎、YouTube、Bilibili 等高频接口新增 Body Rewrite。
6. 用户反馈登录、支付、验证码异常。
7. `reports/automated_quality_evidence.md` 长期未刷新。

## 必跑命令

修改源头文件后运行统一质量门禁：

```bash
python scripts/quality_gate.py
```

质量门禁内部会运行核心命令，包括：

```text
python -m py_compile scripts/*.py Rewrite/Generator/Builder.py tools/*.py
node --check Scripts/app-cleaner.js
python -m unittest discover -s tests
python scripts/validate_app_sources.py
python scripts/convert_quanx_rules.py
python Rewrite/Generator/Builder.py --profile fusion --release
python scripts/validate_remote_rule_syntax.py
python scripts/validate_governance_extensions.py
python scripts/validate_repository.py
python scripts/repository_health_check.py
tools/generate_automated_quality_evidence.py
```

## 远程规则语法门禁

`validate_remote_rule_syntax.py` 是阻断检查，不是提醒检查。

检查范围：

- 根目录模块。
- Release 主模块。
- 兼容 Release 文件。
- `Rules/aggressive-ad-sources.list`。
- `Rules/original-remote-rule-sets.list`。
- `Rewrite/Remotes/sources.json` 中启用的远程规则。

处理规则：

- 上游是 QuanX 格式时，必须先用 `scripts/convert_quanx_rules.py` 转换到 `Rules/converted/` 后再引用。
- 不允许把 QuanX 原始 `host` / `host-suffix` / `host-keyword` 直接放入 Shadowrocket `RULE-SET`。
- 仓库自己的 Pages / raw 链接由校验器优先映射到本地文件，避免 workflow 读到旧缓存。
- 出现失败时，优先修源头，不要只修改 Release 成品。

## Fusion 变更边界

Fusion 是唯一公开模块，不存在 Stable、Stable Plus、Lite 或 Full 的并行发布线。

- 候选、扩展或高风险规则不能批量进入 Fusion。
- 每次接入必须限定到单项 App、单类规则或单组 hostname，并保留源头、风险说明和回滚路径。
- 自动化质量证据只证明构建与静态治理通过，不等同于效果承诺或真实设备结论。
- App 独立模块可用于诊断或按需导入，但不构成新的公开版本线。

## 自动化对应关系

| 检查 | 文件 / 工作流 |
|---|---|
| 构建主模块 | `.github/workflows/module-factory-build.yml` |
| 统一质量门禁 | `scripts/quality_gate.py` |
| QuanX 规则转换 | `scripts/convert_quanx_rules.py` |
| 远程规则语法阻断校验 | `scripts/validate_remote_rule_syntax.py` |
| 治理扩展阻断校验 | `scripts/validate_governance_extensions.py` |
| 每日基础检查 | `.github/workflows/daily-module-update.yml` |
| 失效源审计 | `.github/workflows/daily-invalid-source-repair.yml` |
| 候选源收集 | `.github/workflows/upstream-collect.yml` |
| 仓库健康检查 | `.github/workflows/repository-health.yml` |
| 阻断校验 | `scripts/validate_repository.py` |
| 健康报告 | `scripts/repository_health_check.py` |
| 自动化验证记录 | `reports/automated_quality_evidence.md` |
| 远程规则语法报告 | `reports/remote_rule_syntax_report.md` |

## 处理原则

```text
先报告，再修复。
先源头，再主模块。
先替换，再注释，最后删除。
先小步提交，再观察。
脚本比规则风险高，脚本默认 pending。
远程规则先校验语法，再谈覆盖效果。
候选或扩展层不批量进入 Fusion。
播放、登录、支付、验证码优先保护。
```
