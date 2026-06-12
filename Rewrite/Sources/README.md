# Rewrite/Sources

本目录是融合模块的**正式源材料目录**，用于保存 Shadowrocket / Surge 模块生成所需的规则、重写、脚本、MITM 和应用片段。

`Rewrite/Sources/` 是生成链路的上游源目录；`Release/` 是下游输出目录。不要把 `Release/` 当作源文件维护。

## 标准源片段

```text
Rule.conf            # 规则段
URL-Rewrite.conf     # URL 重写段
Header-Rewrite.conf  # Header Rewrite 段
Body-Rewrite.conf    # Body Rewrite 段
Map-Local.conf       # Map Local 段
Script.conf          # Script 段
MITM.conf            # MITM hostname 段
```

## 子目录职责

```text
Apps/        # 按应用拆分的正式源片段
Misc/        # 通用补充源，例如 CDN、视频、金融、广告等保护或净化片段
Candidates/  # 候选规则，进入正式源前的观察区
Rejected/    # 已拒绝或暂不采用的高风险 / 无效规则
```

## 生成链路

```text
Rewrite/Sources/ + Rules/ + Rewrite/Profiles/
        ↓
Rewrite/Generator/Builder.py
        ↓
Release/Ronghemokuai.sgmodule
Release/Module.sgmodule
Release/Rules.conf
Release/RulesGroup.conf
Release/Modules/
```

## 维护原则

- 先改源文件，再通过生成器输出 Release 文件。
- 不直接手工维护 `Release/*.sgmodule`、`Release/Rules.conf` 或 `Release/RulesGroup.conf`。
- 播放、登录、支付、验证码、CDN、图片加载等稳定性保护规则优先。
- 新规则先进入 `Candidates/`，确认低误杀后再移动到正式源文件。
- 高风险、失效、误杀明显或来源不清的规则进入 `Rejected/`，不要直接删除历史判断依据。
- 上游来源、风险、回滚信息登记到 `Rewrite/Registry.md` 或 `Rewrite/Remotes/`。

## 构建方式

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
```

构建后应重点检查：

```text
Release/Module.sgmodule
Release/Ronghemokuai.sgmodule
Release/Modules/
Web/release-links.json
```
