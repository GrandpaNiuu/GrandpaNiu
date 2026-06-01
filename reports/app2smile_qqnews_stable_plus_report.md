# app2smile QQ News Stable Plus 接入报告

生成日期：2026-06-01

## 结论

本次选择 QQ News / 腾讯新闻作为单个 App 的 Stable Plus 测试接入对象。仓库当前已经按 source-first 方式完成接入，未全量合并 app2smile/rules，也未把完整 sgmodule 粘贴进 `Ronghemokuai.sgmodule`。

## 来源

- 上游模块：`https://raw.githubusercontent.com/app2smile/rules/master/module/qqnews.sgmodule`
- 上游脚本：`https://raw.githubusercontent.com/app2smile/rules/master/js/qq-news.js`
- 上游仓库：`https://github.com/app2smile/rules`
- `Rewrite/Remotes/sources.json` 中的 reference module：`app2smile QQ News module`
- reference module 状态：`enabled=false`，`protected=true`

## 上游模块拆分结果

| 上游区块 | 提取结果 | 本仓库源头位置 | 说明 |
|---|---|---|---|
| `[Rule]` | 无 | `Rules/app2smile-qqnews-stable-plus.list` | 上游模块没有规则区块，本仓库保留显式占位文件记录 App 边界 |
| `[MITM]` | `news.ssp.qq.com`, `r.inews.qq.com` | `Rewrite/Sources/MITM-stable-plus.conf` | 仅用于 Stable Plus；不新增到 Stable |
| `[Script]` | `qq-news.js` response cleaner | `Scripts/app2smile-qqnews-stable-plus.conf` | 仅用于 QQ News 广告清理测试 |

## Profile 接入

- `Rewrite/Profiles/stable-plus.conf`
  - `[rules]` 已接入 `Rules/app2smile-qqnews-stable-plus.list`
  - `[scripts]` 已接入 `Scripts/app2smile-qqnews-stable-plus.conf`
  - `[mitm]` 使用 `Rewrite/Sources/MITM-stable-plus.conf`
  - `[safety]` 标记 `app2smile_qqnews = stable_plus_only_manual_testing`

- `Rewrite/Profiles/stable.conf`
  - 未接入 `Rules/app2smile-qqnews-stable-plus.list`
  - 未接入 `Scripts/app2smile-qqnews-stable-plus.conf`
  - 未引入 `MITM-stable-plus.conf`

## 影响 App

- 影响 App：QQ News / 腾讯新闻
- 处理范围：开屏、新闻列表、专题广告、广告列表等上游脚本声明的广告清理场景
- 不涉及：Spotify、YouTube、Zhihu 现有入口
- 不涉及：会员解锁、付费绕过、登录绕过、支付绕过、Cookie / Token / BoxJS

## 是否影响 Stable

不影响默认 Stable。

说明：

- 本次 app2smile 单项接入只挂到 Stable Plus。
- 根目录 `Ronghemokuai.sgmodule` 仍由 Stable 生成。
- `Release/Ronghemokuai-stable.sgmodule` 不应包含 `app2smile_qqnews_json`。
- `Release/Ronghemokuai-stable-plus.sgmodule` 应包含 `app2smile_qqnews_json`。

## 需要真机测试

需要。当前状态只能视为 Stable Plus 测试接入，不能写成已通过。

建议测试项：

| 测试项 | 状态 | 说明 |
|---|---|---|
| 首页加载 | 未测试 | 确认信息流正常加载 |
| 图片加载 | 未测试 | 确认新闻封面图、正文图、头像不受影响 |
| 登录状态 | 未测试 | 确认已登录状态不丢失 |
| 验证码 | 未测试 | 如触发登录或安全验证，确认不被拦截 |
| 视频 / 媒体资源 | 未测试 | 确认视频新闻、专题媒体资源正常 |
| 广告减少效果 | 未测试 | 对比 Stable 与 Stable Plus，不得通过破坏页面实现去广告 |
| Shadowrocket 日志 | 未测试 | 确认没有误伤登录、图片、媒体资源请求 |

## 回滚路径

如 QQ News 出现异常，按 source-first 回滚：

1. 从 `Rewrite/Profiles/stable-plus.conf` 移除：
   - `app2smile_qqnews = Rules/app2smile-qqnews-stable-plus.list`
   - `app2smile_qqnews = Scripts/app2smile-qqnews-stable-plus.conf`
   - `[safety]` 中的 `app2smile_qqnews = stable_plus_only_manual_testing`
2. 如需进一步收窄，确认 `Rewrite/Sources/MITM-stable-plus.conf` 中的 `news.ssp.qq.com`、`r.inews.qq.com` 是否仍由其他 Stable Plus 测试项需要。
3. 保留 `Rules/app2smile-qqnews-stable-plus.list` 和 `Scripts/app2smile-qqnews-stable-plus.conf` 作为可回滚源头，或在后续独立提交中注释。
4. 重新运行：

```bash
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/check_report_freshness.py
python3 scripts/repository_health_check.py
```

## 边界

- 不全量合并 app2smile/rules。
- 不修改 Stable。
- 不修改 Spotify / YouTube / Zhihu 现有入口。
- 不把完整上游 sgmodule 复制进主模块。
- 没有真实测试记录前，不得晋级 Stable。
