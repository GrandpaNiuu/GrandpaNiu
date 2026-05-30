# App Cleaner Shadow 灰度报告

## 当前状态

- 新增统一清理器：`Scripts/app-cleaner.js`
- 新增配置文件：`Scripts/app-cleaner.config.json`
- 新增 stable-plus 专用入口：`Scripts/app-cleaner-shadow.conf`
- 当前模式：shadow / no-op
- 是否修改响应体：否
- 是否替换旧脚本：否
- 是否进入 stable：否

## 灰度范围

当前只灰度 QQ News URL 范围：

- `news.ssp.qq.com/app`
- `r.inews.qq.com/getQQNewsUnreadList`
- `r.inews.qq.com/getTagFeedList`
- `r.inews.qq.com/gw/page/event_detail`
- `r.inews.qq.com/news_feed/hot_module_list`

## 目的

本阶段只验证统一 runner 是否能够：

1. 在 Stable Plus 中正确加载。
2. 匹配指定 URL。
3. 遇到异常时安全回退。
4. 不修改响应 body。
5. 不影响现有旧脚本功能。

## 安全边界

`app-cleaner.js` 当前不会启用 active cleaner。未来如需开启，必须满足：

1. 先在 Stable Plus 中手动测试通过。
2. 不处理登录、支付、验证码、token、cookie、会员权益、银行相关接口。
3. 使用白名单清理逻辑。
4. 出错时返回原 body。
5. 每次只替换一个 App 组。
6. 不直接进入 Stable。

## 下一步

1. 跑 `Repository Health Check`，让 QQ News 去重和脚本清单自动刷新。
2. 在 Shadowrocket 中启用 Stable Plus。
3. 测试 QQ News 对应页面是否正常。
4. 如果无异常，再考虑把 QQ News 旧入口逐步替换为统一 app-cleaner active 模式。

当前结论：只完成灰度框架，不等于功能替换完成。
