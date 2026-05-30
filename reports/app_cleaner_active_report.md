# App Cleaner Active 批量融合报告

## 当前状态

- 统一承接脚本：`Scripts/app-cleaner.js`
- 统一 active 入口：`Scripts/app-cleaner-active.conf`
- 已废弃 shadow 入口：`Scripts/app-cleaner-shadow.conf`
- 当前模式：active
- 承接方式：一个 active 入口按 URL 分发到不同 App 清理函数

## 已融合批次

### Batch 1

- QQ News
- VGTime

### Batch 2

- SQKB / 省钱快报
- 163News / 网易新闻
- XiaoHeiHe / 小黑盒
- Manner
- Chaoge / 超格教育

### Batch 3

- SMZDM / 什么值得买
- Taobao / 淘宝
- JuneYaoAir / 吉祥航空
- DDXQ / 叮咚买菜
- ZSGJ / 掌上公交

## 设计原则

- 未匹配 URL 原样返回。
- body 为空原样返回。
- JSON 解析失败原样返回。
- 每个 App 单独函数处理，避免相互污染。
- 不处理登录、支付、验证码、银行、会员权益、protobuf、binary-body、加密 body。
- 旧入口由 `scripts/dedupe_qq_news_script_path.py` 在构建前从 `Scripts/app-clean.conf` 与 `Rewrite/Sources/Script.conf` 同步移除。

## 预期效果

- 多个旧脚本入口由一个 `app-cleaner-active-json-clean` 承接。
- 脚本入口数量下降。
- 功能由 App 内部分发函数保留。
- 回滚路径保留在 `reports/script_consolidation_rollback_report.md`。

## 必测 App

- QQ News
- VGTime
- 省钱快报
- 网易新闻
- 小黑盒
- Manner
- 超格教育
- 什么值得买
- 淘宝
- 吉祥航空
- 叮咚买菜
- 掌上公交

## 回滚条件

若出现页面空白、加载失败、广告残留明显变多、JSON 解析异常、核心页面无法打开，应按 `reports/script_consolidation_rollback_report.md` 回滚。
