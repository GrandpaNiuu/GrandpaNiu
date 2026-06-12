# Rules

本目录是仓库的**纯规则源目录**，用于保存域名、IP、白名单、拦截规则和应用补充规则。

`Rules/` 是源材料之一，不是最终发布目录。最终对外使用的规则文件由生成器统一输出到 `Release/`。

## 当前定位

```text
Rules/                         # 规则源材料
Rewrite/Generator/Builder.py   # 统一构建入口
Release/Rules.conf             # 生成后的规则输出
Release/RulesGroup.conf        # 生成后的规则组输出
```

不要直接把 `Release/Rules.conf` 或 `Release/RulesGroup.conf` 当作源文件维护；它们应由构建流程生成。

## 当前规则文件

```text
direct.list           # 白名单 / 直连保护规则
reject.list           # 本地广告拦截规则
spotify-direct.list   # Spotify 播放链路保护
youtube-direct.list   # YouTube 播放链路保护
app-clean.list        # 常用 App 净化补充
web-ads.list          # 网页广告补充
```

## 维护原则

- 白名单和播放、登录、支付、验证码、CDN 保护规则优先。
- 本地拦截规则只加入确认有效、低误杀风险的内容。
- 远程规则源登记在 `Rewrite/Remotes/Index.md`、`Rewrite/Remotes/Catalog.md` 或 `Rewrite/Remotes/sources.json`。
- 候选规则先进入 `Rewrite/Sources/Candidates/`，确认稳定后再进入正式源文件。
- 不在本目录保存破解、支付绕过、登录绕过或高风险规则。

## 构建方式

修改本目录后，使用统一生成入口重建输出：

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
```

构建完成后检查：

```text
Release/Rules.conf
Release/RulesGroup.conf
Release/Module.sgmodule
Ronghemokuai.sgmodule
```
