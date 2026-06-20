# Fusion 单模块策略与旧四版本归档说明

本文替代旧的四版本治理说明。当前 GrandpaNiu 的公开 iOS 策略是 **Fusion 单一融合模块**，不再把 Stable / Stable Plus / Lite / Full 作为公开版本路线维护。

## 当前公开策略

| 类型 | 文件 | 状态 |
|---|---|---|
| 主公开入口 | `Ronghemokuai.sgmodule` | active |
| Release 主模块 | `Release/Ronghemokuai.sgmodule` | active |
| Release 兼容别名 | `Release/Module.sgmodule` | active |
| App 独立模块 | `Release/Modules/*.sgmodule` | diagnostic / convenience |

普通用户只应导入 Fusion 主模块：

```text
https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule
```

## Deprecated / Legacy Reference

以下旧文件只作为历史兼容、审计或回滚参考：

```text
Release/Ronghemokuai-stable.sgmodule
Release/Ronghemokuai-stable-plus.sgmodule
Release/Ronghemokuai-lite.sgmodule
Release/Ronghemokuai-full.sgmodule
Rewrite/Profiles/stable.conf
Rewrite/Profiles/stable-plus.conf
Rewrite/Profiles/lite.conf
Rewrite/Profiles/full.conf
```

这些文件不得作为 README、导入页、默认 workflow、健康检查、发布报告或 Web catalog 的正式入口。

## 构建链路

当前标准构建入口：

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
```

Builder 负责调用底层脚本，并生成：

```text
Release/Ronghemokuai.sgmodule
Release/Module.sgmodule
Ronghemokuai.sgmodule
Release/Rules.conf
Release/RulesGroup.conf
Release/Modules/
Release/Android/
Web/
reports/
```

## 维护边界

- 不再做 Stable Plus 整体晋级 Stable。
- 不再以 Lite / Full 作为公开排查入口。
- 如需回滚或对照，可查看 legacy profile 和 legacy Release 占位文件。
- 新规则、新脚本、新 MITM 覆盖应进入 Fusion 源层，并通过风险门禁、沙盒、仓库验证和人工实测逐步确认。
- 登录、支付、银行、验证码、视频播放、图片/CDN 相关链路优先保护，不用扩大版本线解决误伤。

## 后续文档修正标准

旧文档中如果仍出现“四版本正式路线”“Stable Plus 晋级 Stable”“Full 长期启用”等说法，应改为：

```text
Fusion 为唯一公开主模块；旧四版本仅为 deprecated / legacy reference。
```
