# GrandpaNiu 源头驱动维护标准

本仓库已经不是单文件手工维护模式，而是源头驱动的 Shadowrocket / Surge 模块工厂。

正式导入入口仍然是：

```text
Ronghemokuai.sgmodule
```

但它是生成结果，不是长期手工维护源头。日常维护应优先修改：

```text
Rules/*.list
Scripts/*.conf
Rewrite/Sources/*.conf
Rewrite/Remotes/sources.json
Rewrite/Remotes/candidates.json
Rewrite/Profiles/stable.conf
Rewrite/Profiles/lite.conf
```

完整流程：

```text
Rules + Scripts + Rewrite/Sources + Remotes + Profiles
        -> scripts/build_module.py --build --profile stable
        -> Release/Ronghemokuai.sgmodule
        -> scripts/factory_finalize.py --sync-root
        -> Ronghemokuai.sgmodule
```

## 核心维护原则

1. 不直接长期手写 `Ronghemokuai.sgmodule`。
2. 不直接手写 `Release/Ronghemokuai.sgmodule`。
3. 规则优先改 `Rules/` 或 `Rewrite/Remotes/sources.json`。
4. 脚本优先改 `Scripts/`，脚本新增必须人工确认。
5. Rewrite、Header、Body、Map Local、MITM 优先改 `Rewrite/Sources/`。
6. 修改后必须重新构建并验证 Root 与 Release 一致。
7. Spotify / YouTube / 知乎增强是硬保护项。
8. 登录、支付、验证码、银行、微信、支付宝相关接口优先避免误伤。
9. 性能异常时先看脚本、MITM、Body Rewrite，不要先删除远程规则源。

## 每日维护

每天通常只需要观察，不需要手工改仓库。

检查项目：

1. 查看 `Daily Module Update` 是否成功。
2. 查看 `Daily invalid source audit and repair` 是否成功。
3. 查看 `reports/daily_update_report.md`。
4. 查看 `reports/invalid_sources_report.md`。
5. 确认 `reports/module_factory_diff_report.md` 中 diff lines 为 `0`。
6. 在 Shadowrocket 中更新模块、更新脚本、更新全部。
7. 测试 Spotify 连续播放是否跳歌。
8. 测试 YouTube 首页、搜索、播放、Shorts。
9. 测试知乎首页、回答页、搜索页是否正常。
10. 测试登录、支付、验证码、银行、微信、支付宝。
11. 如果电量异常，查看 iPhone 设置中的 Shadowrocket 电池占比。

若没有异常，不要临时手动改主模块。

## 每周维护

每周检查一次自动收集和源头状态：

1. 查看 `reports/upstream_collect_report.md`。
2. 查看新增了哪些远程规则源。
3. 查看哪些候选源被跳过以及原因。
4. 检查 `Rewrite/Remotes/candidates.json` 是否需要补充低风险候选。
5. 检查 `Rewrite/Remotes/sources.json` 是否有重复或无意义来源。
6. 运行或确认 `Module Factory Build` 后 Root 与 Release 是否一致。
7. 查看 `docs/PERFORMANCE.md`，判断近期是否需要启用或测试 lite profile。

候选源规则：

- `remote_rule` 可以低风险自动化。
- `script` 默认保持 `pending`。
- Spotify / YouTube 核心来源只报告，不自动替换。
- 不开启全网搜索，只使用可信候选池。

## 每月维护

每月做一次低风险整理：

1. 检查重复脚本名。
2. 检查重复 MITM hostname。
3. 检查 `Rules/spotify-direct.list` 是否仍然不含 REJECT。
4. 检查 `Scripts/spotify.conf` 是否只包含 Spotify 脚本。
5. 检查 `Scripts/youtube.conf` 是否只包含 YouTube 脚本。
6. 检查 `Scripts/app-clean.conf` 是否承载普通 App 净化脚本。
7. 检查 `Scripts/zhihu-enhance.conf` 与 `Scripts/zhihu-enhance.js` 是否仍然存在。
8. 检查 `Rewrite/Sources/MITM.conf` 是否过度扩大。
9. 用 `lite.conf` 测试一次低耗电构建是否可用。
10. 更新稳定备份。

推荐验证命令：

```text
python3 -m py_compile scripts/build_module.py scripts/factory_finalize.py scripts/audit_repair_invalid_sources.py scripts/collect_upstreams.py scripts/validate_repository.py
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
```

低耗电参考构建命令：

```text
python3 scripts/build_module.py --build --profile lite
```

注意：`lite.conf` 是低耗电参考配置，不是默认正式配置。正式发布仍以 `stable.conf` 为准，除非经过 24 小时手动测试。

## 性能与耗电维护

性能说明见：

```text
docs/PERFORMANCE.md
```

常见耗电来源：

```text
MITM HTTPS 解密
Body Rewrite
http-response 脚本
YouTube / 知乎 / 信息流 App 的大型 JSON
视频类和信息流类 App 高频请求
```

判断标准：

```text
Shadowrocket 电池占比 3% - 8%：通常正常
Shadowrocket 电池占比 8% - 10%：偏重但可观察
Shadowrocket 电池占比 10% - 15%：建议排查高频脚本
Shadowrocket 电池占比 15% 以上：建议测试 lite profile
```

## Lite Profile 维护标准

`Rewrite/Profiles/lite.conf` 用于低耗电测试，不默认替代 stable。

Lite 版原则：

1. 保留 Spotify 核心保护。
2. 保留 YouTube 核心脚本。
3. 保留知乎增强净化。
4. 减少普通 App 脚本。
5. 减少兼容层批量导入。
6. 不启用未知脚本。
7. 构建后必须手动测试 24 小时。

如果要把 lite 构建结果用于正式主模块，需要执行完整验证并确认：

```text
Spotify 不跳歌
YouTube 不转圈
知乎不空白
登录 / 支付 / 验证码正常
Root 与 Release diff lines = 0
```

## 新增远程规则标准

优先新增到：

```text
Rewrite/Remotes/candidates.json
```

通过收集器验证后进入：

```text
Rewrite/Remotes/sources.json
```

允许类型：

```text
RULE-SET
DOMAIN-SET
```

要求：

1. 必须是 `https://`。
2. 必须来自可信公开仓库。
3. 必须是 Shadowrocket / Surge 可识别规则格式。
4. 必须用途明确，只做广告、开屏、弹窗、横幅、信息流、网页广告、统计追踪。
5. 不使用短链、代理、镜像、ghproxy。
6. 不添加破解、解锁、支付绕过、登录绕过、Cookie、BoxJS、成人、博彩内容。

## 新增脚本标准

脚本风险高，不能完全自动化。

要求：

1. 默认进入 `enabled=false` 或 `status=pending`。
2. 必须人工阅读脚本内容。
3. 必须确认没有破解、会员解锁、支付绕过、登录绕过、Cookie、BoxJS、未知混淆逻辑。
4. 必须确认 pattern 不会覆盖登录、支付、验证码接口。
5. 必须确认需要的 MITM hostname 是最小范围。
6. 通过后才允许加入 `Scripts/app-clean.conf`、`Scripts/spotify.conf`、`Scripts/youtube.conf` 或独立专项脚本配置。

分类要求：

```text
Scripts/spotify.conf        只放 spotify-json / spotify-proto / 明确 Spotify 脚本
Scripts/youtube.conf        只放 youtube.response / 明确 YouTube 脚本
Scripts/zhihu-enhance.conf  只放知乎增强净化脚本入口
Scripts/app-clean.conf      普通 App 净化脚本
```

## 失效源处理标准

失效源修复采用 source-first 策略。

优先处理：

```text
Rewrite/Remotes/sources.json
Rewrite/Remotes/candidates.json
Rules/*.list
Scripts/*.conf
Rewrite/Sources/*.conf
```

处理顺序：

1. 连续 2 天确认失败才处理。
2. 优先寻找同仓库、同来源的可信替代链接。
3. 找不到替代时，JSON 源优先禁用并写明原因。
4. 文本源优先注释原行，保留回滚线索。
5. 只有低风险独立远程规则才允许删除。
6. Spotify、YouTube、知乎增强、update-url、安装页、导入页只报告，不自动破坏。

修复后必须重新构建：

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
```

## 禁止加入内容

```text
会员解锁
Premium 破解
支付绕过
登录绕过
账户权益伪造
证书绕过
Cookie 签到任务
BoxJS 账号任务
成人内容
博彩内容
灰产内容
短链跳转脚本
未知混淆脚本
ghproxy / mirror 正式源
来源不可验证脚本
```

## 出现问题时的排查顺序

Spotify 跳歌：

```text
Rules/spotify-direct.list
Scripts/spotify.conf
Rewrite/Sources/Header-Rewrite.conf
Rewrite/Sources/MITM.conf
最近新增 remote rule
```

YouTube 转圈：

```text
Scripts/youtube.conf
Rewrite/Sources/Map-Local.conf
Rewrite/Sources/MITM.conf
最近新增 URL Rewrite / Body Rewrite
```

知乎广告仍出现或知乎空白：

```text
Scripts/zhihu-enhance.conf
Scripts/zhihu-enhance.js
Rewrite/Profiles/stable.conf
Rewrite/Sources/MITM.conf
HTTPS 解密和证书信任状态
```

登录、支付、验证码异常：

```text
最近新增 Rules
最近新增 Scripts
Rewrite/Sources/URL-Rewrite.conf
Rewrite/Sources/Body-Rewrite.conf
Rewrite/Sources/MITM.conf
```

耗电异常：

```text
docs/PERFORMANCE.md
Scripts/*.conf
Rewrite/Sources/Body-Rewrite.conf
Rewrite/Sources/MITM.conf
Rewrite/Profiles/lite.conf
```

## 回滚标准

优先使用：

```text
backup/Ronghemokuai.stable.sgmodule
backup/Ronghemokuai.before-factory-refactor.sgmodule
Git 提交历史
```

回滚后必须运行：

```text
python3 scripts/validate_repository.py
```

## 推荐提交说明

```text
Build and sync module factory output
Collect trusted upstream candidates
Daily source-first invalid source audit and repair
Update source-driven maintenance guide
Add low-power lite profile
Update performance guide
Fix Spotify playback protection
Fix YouTube enhance compatibility
Update trusted remote candidates
```

不要使用过于模糊的提交说明，例如 `update`、`fix`、`改一下`。
