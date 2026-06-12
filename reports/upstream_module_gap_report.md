# Upstream Module Gap Report

生成时间：2026-06-13

对比对象：

```text
https://surge.qingr.moe/
https://ddgksf2013.top/
```

当前仓库基准：`Web/release-links.json` 中登记的 `Release/Modules/` App 独立模块。

## 1. 当前仓库已有模块

当前仓库已经有以下 App 独立模块：

```text
spotify
youtube
zhihu
bilibili
rednote
wechat
qqnews
weibo
pinduoduo
jd
taobao
netease-music
mgtv
huya
yiche
pcauto
umetrip
xiaopeng
amap
baidu
meituan
quark
soul
wps
youku
zdm
zuoyebang
```

这些模块已经覆盖主流视频、社区、电商、新闻、地图、音乐、汽车、出行和办公场景，但覆盖范围仍明显小于 QingRex / DDGKSF 的上游资源池。

## 2. QingRex / LoonKissSurge 资源差距

### 2.1 当前缺少的基础前置模块

这些属于优先级最高的缺口。QingRex 页面明确提示其中部分是去广告方案的前置依赖。

```text
广告平台拦截器
HTTPDNS 拦截器
DNS 防泄露
BoxJs
Script Hub
Sub-Store
通用模块
DNS 分流
拦截 HTTPDNS
```

建议处理方式：

```text
Rewrite/Sources/Misc/ad-platform-blocker.conf
Rewrite/Sources/Misc/httpdns-blocker.conf
Rewrite/Sources/Misc/dns-protect.conf
Rewrite/Sources/Misc/boxjs-support.conf
Rewrite/Sources/Misc/script-hub-support.conf
Rewrite/Sources/Misc/sub-store-support.conf
```

其中 `广告平台拦截器` 和 `HTTPDNS 拦截器` 应优先进入候选源，不应直接合并到主模块。先做语法校验、MITM hostname 校验和误杀测试。

### 2.2 当前缺少的系统 / Apple / Surge 工具模块

```text
Apple News 解锁
Apple TestFlight
Apple TV 增强
Apple 地图优化
Apple 天气增强
Apple 定位修改
1.1.1.1 配置管理
Surge 启动时长
流量统计
VPS 流量信息
机场流量信息面板
网络信息 X
网络连通性测试
流媒体解锁检测
流媒体解锁检测 Lite
GPT 可用检测
GPT 可用检测-无 WARP
自动加入 TF
```

建议处理方式：

- `Apple 地图优化`、`Apple 天气增强`、`网络连通性测试`、`流量统计` 可进入候选。
- `Apple News 解锁`、`Apple 定位修改`、`自动加入 TF`、`GPT 可用检测` 需要单独风险审查，不建议直接并入主模块。
- 面板类工具建议放入独立模块，不并入 Fusion 主模块。

### 2.3 当前缺少的视频 / 字幕 / 多媒体增强模块

```text
DualSubsNetflix
DualSubsSpotify
DualSubsUniversal
DualSubsYouTube
YouTube 翻译
Youtube (Music) Enhance
Youtube 去广告（不去贴片）
YouTube 去广告 Maasea
Bilibili Helper
BiliADBlock
BiliEnhanced
BiliGlobal
BiliRedirect
B站 CC 繁体字幕转简体
UposRedirect
各种流媒体字幕翻译
Spotify 歌词增强
Spotify 歌词翻译
VVebo 时间线修复
```

当前仓库已有 `youtube`、`bilibili`、`spotify`、`netease-music`，但缺少字幕、翻译、区域、播放链路增强类资源。

建议处理方式：

```text
Rewrite/Sources/Apps/youtube-enhance.conf
Rewrite/Sources/Apps/dualsubs.conf
Rewrite/Sources/Apps/bilibili-enhance.conf
Rewrite/Sources/Apps/spotify-lyrics.conf
Rewrite/Sources/Apps/vvebo.conf
```

### 2.4 当前缺少的常见 App 去广告模块

优先建议补齐的 App：

```text
Keep
Reddit
小红书
百度贴吧
百度网盘
喜马拉雅
Pixiv
酷安
12306
菜鸟裹裹
随手记
Bing 首页简化
微信阅读
滴滴出行
彩云天气
网易邮箱大师
闲鱼
汽水音乐
小宇宙 FM
车来了
墨迹天气
淘票票
中国联通
QQ 音乐
IT之家
Line
TeraBox
TikTok
Roborock
DREAME
ECOVACS HOME
Fileball
京东比价
京东外卖
七猫小说
下厨房
中华万年历
中国移动云盘
丰巢
乐播投屏
书旗小说
云闪付
一刻相册
一甜相机
```

其中与仓库现有生态最接近、优先级最高：

```text
小红书
百度贴吧
百度网盘
喜马拉雅
Keep
Reddit
菜鸟裹裹
滴滴出行
彩云天气
闲鱼
汽水音乐
小宇宙 FM
墨迹天气
中国联通
QQ 音乐
IT之家
TeraBox
```

建议新增路径：

```text
Rewrite/Sources/Apps/xiaohongshu.conf
Rewrite/Sources/Apps/tieba.conf
Rewrite/Sources/Apps/baidupan.conf
Rewrite/Sources/Apps/ximalaya.conf
Rewrite/Sources/Apps/keep.conf
Rewrite/Sources/Apps/reddit.conf
Rewrite/Sources/Apps/cainiao.conf
Rewrite/Sources/Apps/didi.conf
Rewrite/Sources/Apps/caiyun-weather.conf
Rewrite/Sources/Apps/goofish.conf
Rewrite/Sources/Apps/qishui-music.conf
Rewrite/Sources/Apps/xiaoyuzhou.conf
Rewrite/Sources/Apps/moji-weather.conf
Rewrite/Sources/Apps/china-unicom.conf
Rewrite/Sources/Apps/qqmusic.conf
Rewrite/Sources/Apps/ithome.conf
Rewrite/Sources/Apps/terabox.conf
```

## 3. DDGKSF 资源差距

DDGKSF 页面主要是 Quantumult X 配置、分流、复写、脚本任务和图标库集合，不完全等同于 Surge `.sgmodule`。不能直接全部复制，应先转换和审查。

### 3.1 可转为规则源的分流资源

```text
NeteaseMusic.list
OpenAi.list
Emby.list
AppleIntelligence.list
```

建议处理方式：

```text
Rules/netease-music.list      # 已有相关模块，可对照补强
Rules/openai.list             # 当前缺少
Rules/emby.list               # 当前缺少
Rules/apple-intelligence.list # 当前缺少
```

`Anti-ip.list` 页面自身标注“不建议使用”，不建议收录。

### 3.2 可转为候选复写 / App 净化资源

DDGKSF 中可考虑进入候选的资源：

```text
StartUpAds.conf       # 墨鱼去开屏 2.0
Applet.conf           # 微信小程序去广告
YoutubeAds.conf       # 油管广告屏蔽 / PIP / 背景播放
Zhihu_Plus.conf       # 知乎去广告
Tieba_Ads.conf        # 百度贴吧去广告
XmlyAdBlock.conf      # 喜马拉雅去广告
XiaoHongShu.conf      # 小红书去水印 / 净化
KeepAds.conf          # Keep 净化
WeiboAds.conf         # 微博轻享版
AmapAds.conf          # 高德地图
Netease.conf          # 网易云
CainiaoAds.conf       # 菜鸟裹裹
SuiShouJi.conf        # 随手记
BingSimplify.conf     # Bing 首页简化
CaiYunAds.conf        # 彩云天气
RedditAds.conf        # Reddit 去广告
MailAds.conf          # 网易邮箱大师
GoofishAds.conf       # 闲鱼
QiShuiMusicAds.conf   # 汽水音乐
XiaoYuZhouAds.conf    # 小宇宙
CheLaiLeAds.conf      # 车来了
MoJiWeatherAds.conf   # 墨迹天气
TaoPiaoPiaoAds.conf   # 淘票票
ChinaUnicomAds.conf   # 中国联通
```

建议全部先进入：

```text
Rewrite/Sources/Candidates/ddgksf-*.conf
```

审查通过后，再拆到对应 `Rewrite/Sources/Apps/*.conf`。

### 3.3 可作为独立工具模块候选

```text
Bilibili_CC.conf
Youtube_CC.conf
Dualsub.conf
WeChat110.conf
Location.conf
UposRedirect.conf
spotify-lyric.js
vvebo.js
WeatherKit.snippet
jd_price.js
EndlessGoogle.conf
Q-Search.conf
Douban.conf
Adblock4limbo.conf
CAPTCHA.snippet
```

处理建议：

- `Dualsub`、`Youtube_CC`、`Bilibili_CC` 可作为字幕增强候选。
- `jd_price` 可与 `jd` 模块拆成独立增强，不建议混入纯去广告模块。
- `CAPTCHA`、`Location`、`WeChat110` 风险较高，先登记不导入。
- `Q-Search`、`Douban` 更适合作为独立网页优化模块。

## 4. 不建议收录 / 应拒绝的资源类型

以下类型不建议进入仓库正式源，也不建议进入 Release：

```text
会员解锁
VIP / Pro / SVIP 解锁
支付、订阅、购买校验绕过
区域限制绕过
账号共享
已标注失效、停止维护、未适配新版的资源
来源不清或高度混淆脚本
```

DDGKSF 页面中以下条目应直接归入 `Rewrite/Sources/Rejected/` 或只做来源记录：

```text
Spotify会员
墨鱼专属VIP
酷我SVIP+净化
财新周刊VIP
Nicegram高级版
RevenueCat多合一
BuyiTunes多合一
Emby解锁
端传媒VIP
Goodbility会员
B站自动换区
Testflight共享+解锁区域限制
阿里云盘倍速
解锁NewBing搜索
```

## 5. 建议执行顺序

### 第一批：基础保护与前置依赖

```text
广告平台拦截器
HTTPDNS 拦截器
DNS 防泄露
通用模块
BoxJs
Script Hub
Sub-Store
```

### 第二批：与你仓库现有模块强相关

```text
小红书
百度贴吧
百度网盘
喜马拉雅
Keep
Reddit
菜鸟裹裹
滴滴出行
彩云天气
闲鱼
汽水音乐
小宇宙 FM
墨迹天气
中国联通
QQ 音乐
IT之家
TeraBox
```

### 第三批：增强类独立模块

```text
DualSubsUniversal
DualSubsYouTube
Bilibili_CC
Youtube_CC
Spotify 歌词翻译
VVebo 时间线修复
JD 比价
Q-Search
Douban
```

### 第四批：只登记不导入

```text
VIP / 解锁 / 账号共享 / 支付校验绕过类
已失效 / 未适配新版 / 停止维护类
定位修改 / CAPTCHA / 高风险网页注入类
```

## 6. 建议给 Codex 的下一步任务

```text
请基于 reports/upstream_module_gap_report.md 执行第一批候选导入：
1. 不直接改 Release/。
2. 新增 Rewrite/Sources/Candidates/qingrex-foundation/。
3. 为广告平台拦截器、HTTPDNS 拦截器、DNS 防泄露、通用模块、BoxJs、Script Hub、Sub-Store 建立来源登记文件。
4. 只登记来源和风险，不直接合并到 Fusion 主模块。
5. 更新 Rewrite/Registry.md，记录 source、upstream、risk、fallback、status。
6. 生成 reports/upstream_candidate_import_plan.md。
7. 不导入任何 VIP、解锁、支付绕过、账号共享、破解类资源。
```

## 7. 结论

当前仓库不是缺少少量模块，而是相比 QingRex / DDGKSF 的资源池仍处在“精选融合”阶段。建议不要一次性全量搬运。正确路线是：

```text
来源登记 → 候选目录 → 风险审查 → 语法校验 → 小批量合并 → 生成 Release → 回归测试
```

优先补齐基础前置模块和与你现有 App 模块强相关的缺口，拒绝 VIP / 解锁 / 绕过类资源。
