# 手动测试记录

本文件用于记录真实人工测试结果。测试来源必须写清楚；没有真实测试时，不得填写“通过”。

## 记录原则

- 只有真实打开客户端、完成指定页面检查后，才能写“通过”。
- “用户确认”必须来自真实使用反馈，不得由维护脚本或助手推断。
- 涉及登录、支付、验证码、银行、微信媒体、图片 CDN、小程序的变更，即使已有通过记录，后续大改后仍需复测。
- Stable Plus / Full 的测试记录不能自动代表 Stable 通过。
- Full 只作为排查版；Full 结果不能整体晋级 Stable。

## 标准测试记录模板

复制以下模板新增记录：

```text
### YYYY-MM-DD / App 或服务 / 模块版本

- 测试人或来源：
- 设备与系统：
- 客户端与版本：Shadowrocket / Surge / 其他
- 使用模块：Stable / Stable Plus / Lite / Full
- 模块链接或 commit：
- App 版本：
- 测试页面：
- 测试动作：
- 是否更新模块、脚本、全部资源：
- 是否与 Lite 对照：是 / 否
- Lite 对照结果：
- 是否关闭模块对照：是 / 否
- 关闭模块对照结果：
- Shadowrocket 日志关键命中：
- 结果：通过 / 失败 / 部分异常 / 待复测
- 误伤表现：
- 回滚路径：
- 证据：截图 / 录屏 / 日志 / 用户确认
- 备注：
```

## Stable 第一轮测试确认

| 日期 | 模块版本 | 测试来源 | 测试范围 | 结果 | 是否通过 |
|---|---|---|---|---|---|
| 2026-06-01 | Stable / GrandpaNiu | 用户确认 | 国内 App 图片 / 联网 / 微信发图 | 已恢复正常 | 是 |
| 2026-06-01 | Stable / GrandpaNiu | 用户确认 | Stable 第一轮真实测试 | 通过 | 是 |

### Stable 第一轮涉及 App / 服务

本轮记录来自用户确认。涉及范围：

- Spotify
- YouTube
- 知乎
- Bilibili
- 淘宝
- 京东
- 拼多多
- 美团
- 大众点评
- 饿了么
- 微信
- 支付宝
- 银行 / 验证码
- 图片 CDN
- 小程序资源
- 闲鱼
- 喜马拉雅
- 滴滴
- 斗鱼

## 2026-06-11 Actions 核验记录

本节只记录可核验的 GitHub Actions 运行状态，不代表 App 真机测试通过。

| Workflow | Run ID | 核验来源 | Status | Conclusion | 处理结论 |
|---|---:|---|---|---|---|
| Module Factory Build | 27029906505 | GitHub Actions job 明细 | completed | success | 通过 |
| Daily Module Update | 27303422092 | GitHub Actions job 明细 | completed | success | 通过 |
| Daily invalid source audit and repair | 27235955379 | GitHub Actions job 明细 | completed | success | 通过 |
| Daily invalid rule audit and safe repair | 27307325073 | GitHub Actions job 明细 | completed | success | 通过 |
| Upstream candidate collect | 27236314334 | GitHub Actions job 明细 | completed | success | 通过 |
| Repository Health Check | 27105193304 | GitHub Actions job 明细 | completed | success | 通过 |
| Stable Plus Promotion PR | 27026755128 | GitHub Actions job 明细 | completed | success / draft PR step skipped | 通过；未创建晋级 PR，保持人工审查 |

补充说明：GitHub Pages deployment 属于页面部署，不作为 Stable / Stable Plus 晋级依据。若 Actions 页面出现新的 in_progress 运行，需等待完成后重新记录。

## Stable Plus 单项测试记录

Stable Plus 仍需逐个 App 单项测试。Stable 第一轮通过不代表 Stable Plus 可以整体合并进 Stable。

| 日期 | 模块版本 | 测试来源 | App / 服务 | 测试项目 | 结果 | 是否通过 | 是否允许晋级 Stable |
|---|---|---|---|---|---|---|---|
| 未测试 | Stable Plus | 未测试 | 微信广告规则 | 插入广告减少、发图、收图、朋友圈、公众号图片、小程序、支付前置页、登录状态 | 未测试 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 微博 | 首页、信息流、热搜、评论、私信、登录状态 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 百度贴吧 | 首页、帖子页、楼中楼、图片加载、登录状态 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 小红书 | 首页、搜索、笔记详情、评论、图片/视频加载、登录状态 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 酷安 | 首页、动态、应用详情、评论、登录状态 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 12306 | 首页、车票查询、登录、验证码、订单前置 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 高德地图 | 首页、搜索、定位、路线规划、导航前置 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 百度地图 | 首页、搜索、定位、路线规划、导航前置 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 网易云音乐 | 首页、搜索、播放、歌单、评论 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | 小宇宙 | 首页、搜索、播放、节目详情、评论 | 待复测 | 否 | 否 |
| 待测试 | Stable Plus | 待人工真机测试 | Reddit | 首页、帖子详情、评论、登录状态 | 待复测 | 否 | 否 |

### 单项晋级准入规则

1. 每次只允许一个 App 或一组明确 hostname / script 入口进入晋级审查。
2. 必须有 Stable Plus 真机测试记录，且至少覆盖：首页、搜索/详情页、登录状态、媒体资源加载、核心交互。
3. 高风险 App 必须额外覆盖：登录、验证码、支付前置、订单前置、图片 CDN、小程序或地图定位。
4. 必须完成 Lite 对照和关闭模块对照，确认异常不是 App 服务端、缓存或网络本身导致。
5. 必须记录可回滚路径，优先回滚源头文件，而不是直接改 Release 成品。
6. 没有日志、截图、录屏或用户确认时，不允许写“通过”。
7. 不允许 Stable Plus 整体合并进 Stable；不允许 Full 整体合并进 Stable。

## Release / Tag 发布核验记录

| 日期 | 操作项 | 当前状态 | 结论 |
|---|---|---|---|
| 2026-06-11 | Release 文件生成 | `Release/Ronghemokuai-stable.sgmodule`、`Release/Ronghemokuai-stable-plus.sgmodule`、`Release/Ronghemokuai-lite.sgmodule`、`Release/Ronghemokuai-full.sgmodule` 已存在 | 可作为发布资产候选 |
| 2026-06-11 | GitHub Release / tag 创建 | 当前维护连接器未提供创建 GitHub Release 或 tag 的写入接口 | 未执行；需在 GitHub 页面或本地 git/gh 执行 |
| 2026-06-11 | 发布前条件 | Profile 全量验证显示 stable 可发布；stable-plus/lite/full 不默认发布 | 只允许 Stable 作为正式发布入口 |

建议发布标签命名：`v2026.06.11-stable`。

发布前必须确认：

```bash
git fetch origin
git checkout main
git pull --ff-only origin main
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
git tag -a v2026.06.11-stable -m "Stable release 2026-06-11"
git push origin v2026.06.11-stable
```

GitHub Release 资产建议只附 Stable 文件，Stable Plus / Lite / Full 放在说明中作为测试或排查版本，不作为默认推荐。

## Full 排查记录

Full 只用于定位问题和查漏拦，不作为 Stable 候选池。任何从 Full 到 Stable 的迁移必须拆成单项 App、单类规则或单组 hostname，并补充真实测试记录。

| 日期 | 模块版本 | 测试来源 | 排查对象 | 发现问题 | 后续动作 | 是否允许批量晋级 Stable |
|---|---|---|---|---|---|---|
| 未测试 | Full | 未测试 | 全量排查 | 未记录 | 无 | 否 |

## 失败 / 误伤记录

所有误伤必须可复现，并尽量附 Shadowrocket 日志。没有日志时，至少需要 Lite 对照和关闭模块对照。

| 日期 | 模块版本 | App / 服务 | 现象 | Lite 是否正常 | 关闭模块是否正常 | 初步定位 | 回滚路径 | 状态 |
|---|---|---|---|---|---|---|---|---|
| 未记录 | 未记录 | 未记录 | 未记录 | 未记录 | 未记录 | 未记录 | 未记录 | 未记录 |

## 最低测试清单

大改后至少覆盖：

- Shadowrocket 更新模块、脚本、全部资源。
- Stable 与 Lite 对照。
- Spotify 连续播放。
- YouTube 首页、搜索、播放、Shorts。
- 知乎首页、回答页、搜索页。
- Bilibili 首页、搜索、播放页。
- 淘宝 / 京东 / 拼多多首页、搜索、商品图、订单前置。
- 微信发图、收图、朋友圈、公众号图片、小程序、支付前置页。
- 支付宝 / 银行 App 登录、验证码、支付前置流程。
- 高德 / 百度地图搜索、定位、路线规划。

## 记录规则

- “用户确认”表示由用户反馈真实使用结果。
- Stable Plus 内容只有在单项 App 真实测试通过后，才能进入晋级流程。
- 不允许 Stable Plus 整体合并进 Stable。
- 不允许 Full 整体合并进 Stable。
- 涉及登录、支付、验证码、银行、微信媒体、图片 CDN、小程序的变更，即使已有通过记录，后续大改后仍需复测。
