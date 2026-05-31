# App Cleaner Active 批量融合报告

## 当前状态

- 统一承接脚本：`Scripts/app-cleaner.js`
- 统一 active 入口：`Scripts/app-cleaner-active.conf`
- 当前模式：active
- 承接方式：一个 active 入口按 URL 分发到不同 App 清理函数
- 架构：registry / dispatcher
- 语法门禁：GitHub Actions 中执行 `node --check Scripts/app-cleaner.js`

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

### Batch 4

- KKMH / 快看漫画
- Goofish / 闲鱼
- XMly / 喜马拉雅
- Didi / 滴滴

### Batch 5

通用低风险 JSON 广告字段清理器，覆盖一批广告字段、banner、popup、splash、promotion、feed ad、commercial 字段清理。该批次只在 `app-cleaner-active.conf` 白名单域名命中时生效，未匹配 URL 原样返回。

### Batch 6

- Douyu / 斗鱼
- SPTCC / 上海交通卡
- Youdao Dict / 有道词典
- Maimai / 脉脉

## Batch 5 当前白名单方向

- CoolApk
- 大众点评 / 美团相关
- 高德地图
- 宝宝树
- 马蜂窝
- 稿定设计
- 拼多多
- 起点
- 快手广告接口
- 盒马 / 菜鸟 / 转转 / 百度地图 / 海尔
- 小宇宙 / 配音秀 / 京东 / Reddit / 薄荷健康
- 360 摄像机 / 飞猪 / 1314之旅 / 阿里广告 / 皮皮虾
- 趣达 / 复游会 / 途虎 / 萤石 / 飞客
- 盖得排行 / 小米商城 / 亲宝宝 / 51CTO / 饿了么 / 堆糖 / 51job / usmile
- 财新 / 罗森 / 美柚 / 咪咕视频 / 朴朴 / 企迈

## 设计原则

- 未匹配 URL 原样返回。
- body 为空原样返回。
- JSON 解析失败原样返回。
- `RAW_CLEANERS` 只处理需要 raw body 的低风险替换。
- `JSON_CLEANERS` 只处理标准 JSON response body。
- 专项 App 使用独立函数处理，避免相互污染。
- Batch 5 使用递归广告字段清理器，只清理常见广告字段和明显广告数组项。
- 不处理登录、支付、验证码、银行、会员权益、protobuf、binary-body、加密 body。
- 旧入口由 `scripts/dedupe_qq_news_script_path.py` 在构建前从 `Scripts/app-clean.conf` 与 `Rewrite/Sources/Script.conf` 同步移除。

## 本轮未融合内容

以下继续保持独立，不硬合：

- Weibo / 微博：逻辑大，包含多页面深层结构和非标准开屏返回。
- Zhihu R-Store：结构复杂，已另有知乎增强入口，不在本轮合并。
- MGTV / CNTV：体量大，覆盖爱奇艺、芒果、优酷等多服务，暂不合并。
- Soul：包含限制修改、状态逻辑，不作为低风险 JSON 清理。
- Keep、Cotti、RRTV、网易云音乐、12306、航旅纵横、搜狗输入法、韵达：保留独立评估。
- protobuf / binary-body / request-body / 登录支付验证码相关脚本：禁止硬合。

## 预期效果

- 多个旧脚本入口由一个 `app-cleaner-active-json-clean` 承接。
- 脚本入口数量继续下降，目标向 20-50 区间靠近。
- 功能由 App 内部分发函数和通用字段清理器保留。
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
- 快看漫画
- 闲鱼
- 喜马拉雅
- 滴滴
- 斗鱼
- 上海交通卡
- 有道词典
- 脉脉
- Batch 5 白名单 App 中实际常用的 App

## 回滚条件

若出现页面空白、加载失败、广告残留明显变多、JSON 解析异常、核心页面无法打开，应按 `reports/script_consolidation_rollback_report.md` 回滚。
