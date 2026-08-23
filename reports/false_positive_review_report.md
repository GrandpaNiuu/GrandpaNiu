# 误伤复核队列报告

- 生成时间：2026-08-24 01:51:51 +0800
- 风险台账条目：2989
- high：73
- medium：2916
- MITM：172
- REJECT：2817
- 保护链路台账：存在

## 复核原则

- 本报告只生成复核队列，不自动修改规则。
- 只有出现真实 App 异常、Shadowrocket 日志、抓包证据或可复现失败时，才做 source-first 单点调整。
- 先定位具体源文件，再优先缩小规则；不要批量删除，也不要用宽泛白名单掩盖问题。
- 修改后必须运行完整质量门禁。

## 风险分类统计

| category | count |
| --- | --- |
| 未分类 REJECT | 1897 |
| 图片 / 静态 CDN | 522 |
| 国内 App 核心 API | 215 |
| 视频 / 音乐播放链路 | 165 |
| 通配 MITM | 48 |
| 登录 / 账号 / 鉴权 | 38 |
| 图片 / 静态 CDN / 国内 App 核心 API | 29 |
| 银行 / 支付 / 钱包 | 22 |
| 视频 / 音乐播放链路 / 图片 / 静态 CDN | 18 |
| HTTPDNS / DNS | 7 |
| 银行 / 支付 / 钱包 / 图片 / 静态 CDN | 4 |
| 图片 / 静态 CDN / 通配 MITM | 4 |
| 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | 4 |
| 视频 / 音乐播放链路 / 国内 App 核心 API | 4 |
| 视频 / 音乐播放链路 / 通配 MITM | 3 |
| 登录 / 账号 / 鉴权 / 国内 App 核心 API | 3 |
| 国内 App 核心 API / 通配 MITM | 2 |
| 银行 / 支付 / 钱包 / 国内 App 核心 API | 2 |
| 图片 / 静态 CDN / HTTPDNS / DNS | 2 |

## reject_risk_report 待复核摘要

- 银行 / 支付：0
- 图片 / CDN：0
- 国内核心 API：0

## high 优先复核队列

| type | risk | category | source | output_status | entry | reason |
| --- | --- | --- | --- | --- | --- | --- |
| MITM | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/appso.conf:12 | final-exact | sso.ifanr.com | 命中敏感链路关键词 |
| MITM | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/mobile-clouds.conf:14 | final-exact | jzts.cmpassport.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | final-exact | pay.kkmh.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | final-exact | ccmsupport-sz.tenpay.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | final-exact | creditcardapp.bankcomm.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | final-exact | mbmodule-openapi.paas.cmbchina.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | final-exact | cdn-pay.kkmh.com | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/51-job.conf:12 | source-only-or-compiled | ^https://cupid\.51jobapp\.com/open/noauth/jobs/detail/sesame-competitive/ - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/51-job.conf:13 | source-only-or-compiled | ^https://cupid\.51jobapp\.com/open/noauth/jobs/job-detail/user-rights\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/51-job.conf:15 | source-only-or-compiled | ^https://cupid\.51jobapp\.com/launch-hub/open/noauth/popUp/ - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/51-job.conf:16 | source-only-or-compiled | ^https://cupid\.51jobapp\.com/launch-hub/open/noauth/popUp/getHomePagePopUp\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/appso.conf:9 | source-only-or-compiled | ^https?://sso\.ifanr\.com/jiong/IOS/appso/splash/ - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/blued.conf:10 | source-only-or-compiled | ^https?://social\.blued\.cn/users/no_auth/benefit - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/dao-meng-kong-jian.conf:10 | source-only-or-compiled | ^https?://appdmkj\.5idream\.net/v2/login/message/tip - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/etouch-ecalendar.conf:12 | source-only-or-compiled | ^https://client-lz\.rili\.cn/lizhi/api/auth/voice_room_entrance/list\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/huo-mao.conf:9 | source-only-or-compiled | ^https?://api\.huomao\.com/channels/loginAd - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/pu-pu-mall.conf:9 | source-only-or-compiled | ^https://j1\.pupuapi\.com/client/account/discount/order - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/wechat-mini-programs.conf:101 | source-only-or-compiled | ^https://gw-passenger-wap\.01zhuanche\.com/gw-passenger-wap/zhuanche-passenger-token/commonSkipToken/common/getAdList - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/wechat-mini-programs.conf:104 | source-only-or-compiled | ^https://passenger\.t3go\.cn/passenger-activity-api/notoken/api/v1/resource/getSource - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/wechat-mini-programs.conf:126 | source-only-or-compiled | ^https://api\.szbgcx\.cn/account/adv/ - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/xia-chu-fang.conf:10 | source-only-or-compiled | ^https://api\.xiachufang\.com/v2/account/feeds_v7\.json - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/xiao-hei-he.conf:9 | source-only-or-compiled | ^https://api\.xiaoheihe\.cn/account/get_ads_info_v2 - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:55 | source-only-or-compiled | ^https:\/\/api\.szbgcx\.cn\/account\/adv\/ - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:1332 | source-only-or-compiled | ^https?:\/\/social\.blued\.cn\/users\/no_auth\/benefit - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:1342 | source-only-or-compiled | ^https?:\/\/sso\.ifanr\.com\/jiong\/IOS\/appso\/splash\/ - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:1489 | source-only-or-compiled | ^https?:\/\/www\.onstar\.com\.cn\/mssos\/sos\/social\/v1\/community\/article\/page - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:346 | source-only-or-compiled | ^https?:\/\/api\.m\.jd\.com\/\?loginType=11 - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:415 | source-only-or-compiled | ^https?:\/\/api\.ulife\.group\/auth\/account\/entrance - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:416 | source-only-or-compiled | ^https?:\/\/api\.ulife\.group\/auth\/account\/getUpgradeStrategy - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:429 | source-only-or-compiled | ^https?:\/\/api\.xiachufang\.com\/v2\/account\/feeds_v7\.json - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:434 | source-only-or-compiled | ^https?:\/\/api\.xiaoheihe\.cn\/account\/get_ads_info - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:502 | source-only-or-compiled | ^https?:\/\/app\.ceair\.com\/customize\/security\/update - reject-200 | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:558 | source-only-or-compiled | ^https?:\/\/appdmkj\.5idream\.net\/v2\/login\/message\/tip - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:654 | source-only-or-compiled | ^https?:\/\/client-api-v\d\.oray\.com\/materials\/(?:SLCC_IOS_STARTUP\|SLCC_IOS_DEVICE\|SUNLOGIN_CLIENT_IOS_PROMOTION) - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:656 | source-only-or-compiled | ^https?:\/\/client-lz\.rili\.cn\/lizhi\/api\/auth\/voice_room_entrance\/list\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:687 | source-only-or-compiled | ^https?:\/\/cupid\.51jobapp\.com\/launch-hub\/open\/noauth\/popUp\/ - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:688 | source-only-or-compiled | ^https?:\/\/cupid\.51jobapp\.com\/launch-hub\/open\/noauth\/popUp\/getHomePagePopUp\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:690 | source-only-or-compiled | ^https?:\/\/cupid\.51jobapp\.com\/open\/noauth\/jobs\/detail\/sesame-competitive\/ - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:691 | source-only-or-compiled | ^https?:\/\/cupid\.51jobapp\.com\/open\/noauth\/jobs\/job-detail\/user-rights\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:815 | source-only-or-compiled | ^https?:\/\/gateway\.cotticoffee\.com\/cotti-capi\/person\/homeLoginPrompt - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:844 | source-only-or-compiled | ^https?:\/\/gw-passenger\.01zhuanche\.com\/gw-passenger\/zhuanche-passenger-token\/leachtoken\/webservice\/homepage\/queryADs - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:933 | source-only-or-compiled | ^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(side-bar\/mini-program\/music-service\/account\|delivery\/(?:batch-deliver\|deliver)\|moment\/tab\/info\/get\|yunbei\/account\/entrance\/get) - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:934 | source-only-or-compiled | ^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(vipcenter\/tspopup\/get\|vipauth\/app\/auth\|music-vip-membership\/client\/vip\/info\|zone\/songplay\/entry\/get) - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | Rewrite/Sources/Apps/aiinquiry.conf:15 | source-only-or-compiled | ^https://aiqicha\.baidu\.com/m/getLoginWordsAjax - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | Rewrite/Sources/URL-Rewrite.conf:220 | source-only-or-compiled | ^https?:\/\/aiqicha\.baidu\.com\/m\/getLoginWordsAjax - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | Rewrite/Sources/URL-Rewrite.conf:354 | source-only-or-compiled | ^https?:\/\/api\.map\.baidu\.com\/\?qt=verify - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | Rewrite/Sources/Apps/seasun-jx3.conf:12 | source-only-or-compiled | ^https://jx3comm\.xoyocdn\.com/jx3gc/zhcn/login_ad/WebCareer/WebCareerTab\.txt - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite.conf:1014 | source-only-or-compiled | ^https?:\/\/m\.client\.10010\.com\/mobileService\/(activity\|customer)\/(accountListData\|get_client_adv\|get_startadv) - reject-img | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite.conf:1462 | source-only-or-compiled | ^https?:\/\/www\.dpfile\.com\/picasso\/picasso-qa\/src\/AnswerList\/AnswerList-bundle - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite.conf:958 | source-only-or-compiled | ^https?:\/\/jx3comm\.xoyocdn\.com\/jx3gc\/zhcn\/login_ad\/WebCareer\/WebCareerTab\.txt - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:23 | source-only-or-compiled | ^https://creditcardapp\.bankcomm\.com/cnsvPmpaMdbcardWeb/page/getGuidePageAds - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:24 | source-only-or-compiled | ^https://mbmodule-openapi\.paas\.cmbchina\.com/graphic/v2/module/graphic - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:82 | source-only-or-compiled | ^https://ccmsupport-sz\.tenpay\.com/cgi-bin/common/ccm_page_element.cgi - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Rule.conf:101 | source-only-or-compiled | DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Rule.conf:102 | source-only-or-compiled | DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:10 | source-only-or-compiled | ^https:\/\/creditcardapp\.bankcomm\.com\/cnsvPmpaMdbcardWeb\/page\/getGuidePageAds - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:13 | source-only-or-compiled | ^https:\/\/mbmodule-openapi\.paas\.cmbchina\.com\/graphic\/v2\/module\/graphic - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:52 | source-only-or-compiled | ^https:\/\/ccmsupport-sz\.tenpay\.com\/cgi-bin\/common\/ccm_page_element.cgi - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite.conf:1023 | source-only-or-compiled | ^https?:\/\/m\.qianbao\.qq\.com\/pages\/walletHome\?invisible - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite.conf:1024 | source-only-or-compiled | ^https?:\/\/m\.qianbao\.qq\.com\/services\/walletHome\/get(QQshop\|Game\|Foot)Data - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite.conf:320 | source-only-or-compiled | ^https?:\/\/api\.hellobike\.com\/api\?homepage\.newWelfare\.alipay - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/qingrex-miniapp-app-ad.list:30 | source-only-or-compiled | DOMAIN-KEYWORD,adv.ccb.com,REJECT,extended-matching,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/reject.list:73 | source-only-or-compiled | DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/reject.list:74 | source-only-or-compiled | DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/reject.list:98 | source-only-or-compiled | DOMAIN,msmp.abchina.com.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/web-ads.list:16 | final-exact | DOMAIN,ads.ysepay.com,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/web-ads.list:37 | source-only-or-compiled | DOMAIN,mbads.paas.cmbchina.com,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/web-ads.list:64 | source-only-or-compiled | DOMAIN-SUFFIX,track.bankcomm.com,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 国内 App 核心 API | Rewrite/Sources/URL-Rewrite.conf:1159 | source-only-or-compiled | ^https?:\/\/npay\.meituan\.com\/conch\/flow\/mypage-wallet-info - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 国内 App 核心 API | Rewrite/Sources/URL-Rewrite.conf:1160 | source-only-or-compiled | ^https?:\/\/npay\.meituan\.com\/conch\/walletv\d\/wechat-pop-window - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:27 | source-only-or-compiled | ^https://(cdn-)?pay\.kkmh\.com/v\d/kb/wallet - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:111 | source-only-or-compiled | ^http:\/\/image1\.ccb\.com\/newsinfo\/eBranch\/check\/(?:nf\/newfin\/activity\|po\/poortheme\/activity)\/\w+\.png - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite.conf:40 | source-only-or-compiled | ^https?:\/\/(cdn-)?pay\.kkmh\.com\/v\d\/kb\/(?:wallet\|comic_page_banner) - reject-dict | 命中敏感链路关键词 |

## medium 抽样复核队列

| type | risk | category | source | output_status | entry | reason |
| --- | --- | --- | --- | --- | --- | --- |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/aiinquiry.conf:22 | final-exact | aiqicha.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-input-method.conf:20 | final-exact | imeres.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-input-method.conf:20 | final-exact | mbd.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-input-method.conf:20 | final-exact | mime.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-map.conf:25 | final-exact | afd.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-map.conf:25 | final-exact | ecom.map.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-map.conf:25 | final-exact | newclient.map.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-map.conf:25 | final-exact | yongche.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-net-disk.conf:21 | final-exact | pan.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-photo.conf:16 | final-exact | mbd.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-photo.conf:16 | final-exact | pan.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-translation.conf:13 | final-exact | mime.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-wenku.conf:34 | final-exact | appwk.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-wenku.conf:34 | final-exact | tanbi.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu.conf:12 | final-exact | m.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu.conf:12 | final-exact | www.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidupan.conf:27 | final-exact | pan.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/damai.conf:18 | final-exact | acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/i-mai-cai.conf:21 | final-exact | mall.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/i-mai-cai.conf:21 | final-exact | portal-portm.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/jd.conf:23 | final-exact | api.m.jd.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/jdwaimai.conf:19 | final-exact | api.m.jd.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | final-exact | apimobile.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | final-exact | cdb.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | final-exact | mall.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | final-exact | rms.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | final-exact | web.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | final-exact | wmapi.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/pinduoduo.conf:85 | final-exact | api.pinduoduo.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/robo-taxi.conf:14 | final-exact | idgdata.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/taobao-travel.conf:16 | final-exact | acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/taobao.conf:44 | final-exact | acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/taobao.conf:44 | final-exact | guide-acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/taopiaopiao.conf:19 | final-exact | acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/tieba.conf:18 | final-exact | tiebac.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | final-exact | api.pinduoduo.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | final-exact | rms.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/wechat-official-accounts.conf:16 | final-exact | mp.weixin.qq.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/wechat.conf:17 | final-exact | mp.weixin.qq.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API / 通配 MITM | Rewrite/Sources/Apps/amap.conf:81 | final-exact | *.amap.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 国内 App 核心 API / 通配 MITM | Rewrite/Sources/Apps/meituan.conf:30 | final-exact | *.dianping.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/baby-tree-parenting.conf:16 | final-exact | aimg.babytreeimg.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/caiyun-weather.conf:22 | final-exact | cdn-w.caiyunapp.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/che-lai-le.conf:23 | final-exact | pic1.chelaile.net.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/clicli.conf:12 | final-exact | js-ad.ayximgs.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/di-duan-ying-shi.conf:15 | final-exact | img.ddrk.me | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/dian-shi-jia.conf:13 | final-exact | cdn.dianshihome.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/dlabel-cloud-tag.conf:13 | final-exact | imagepc.ctaiot.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/douyu.conf:27 | final-exact | apiv2.douyucdn.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/douyu.conf:27 | final-exact | rtbapi.douyucdn.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/douyu.conf:27 | final-exact | venus.douyucdn.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/jie-mian-news.conf:12 | final-exact | img.jiemian.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kingsoft-power-word.conf:26 | final-exact | mobile-pic.cache.iciba.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | final-exact | cdn-api.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | final-exact | cdn-h5.kuaikanmanhua.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | final-exact | cdn-shop.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | final-exact | cdn-social.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | final-exact | cdn-topic.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | final-exact | topic.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/lenovo-print.conf:12 | final-exact | abcapi.lenovoimage.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | final-exact | ad.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | final-exact | d.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | final-exact | ec-bot-obs.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | final-exact | obs.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | final-exact | scdn.line-apps.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | final-exact | static.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/lofter.conf:14 | final-exact | images.pinduoduo.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/ma-ka-long-wan-tu.conf:13 | final-exact | static01.versa-ai.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/ma-ma-wang-yun-yu.conf:12 | final-exact | qimg.cdnmama.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/mai-dui-dui.conf:19 | final-exact | conf-darwin.xycdn.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/mai-dui-dui.conf:19 | final-exact | mobads-pre-config.cdn.bcebos.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/mkz.conf:18 | final-exact | base.mkzcdn.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/picc-insurance.conf:19 | final-exact | zgrb.epicc.com.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/qi-shui-music.conf:16 | final-exact | lf-cdn-tos.bytescm.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/qi-xin-bao.conf:21 | final-exact | qxb-minicode-pic-osscache.qixin.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/quan-min-ge-ge.conf:12 | final-exact | y.gtimg.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/seasun-jx3.conf:15 | final-exact | jx3comm.xoyocdn.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/seven-cat.conf:32 | final-exact | cdn.wtzw.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/sf-express.conf:19 | final-exact | ucmp-static.sf-express.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/sogou-input.conf:16 | final-exact | business-cdn.shouji.sogou.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/taobao.conf:44 | final-exact | heic.alicdn.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/tencent-games-community.conf:12 | final-exact | static.gameplus.qq.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/tencent-sports.conf:13 | final-exact | sports3.gtimg.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/ttvoice.conf:12 | final-exact | ga-album-cdnqn.52tt.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | final-exact | appuser-static.huolala.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | final-exact | fscdn.zto.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | final-exact | images.qmai.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/xfuse.conf:12 | final-exact | img.mofyi.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/xiaojukeji-charge.conf:20 | final-exact | am.didistatic.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/zdm.conf:57 | final-exact | haojia-cdn.smzdm.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | Rewrite/Sources/Apps/58-tong-cheng.conf:34 | final-exact | *.58cdn.com.cn | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | Rewrite/Sources/Apps/che-lai-le.conf:23 | final-exact | cdn.*.chelaileapp.cn | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | Rewrite/Sources/Apps/huya.conf:14 | final-exact | *.msstatic.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | Rewrite/Sources/Apps/qqksong.conf:52 | final-exact | amsweb-cdn-*-1258344696.file.myqcloud.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/bilibili.conf:87 | final-exact | grpc.biliapi.net | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/i-qi-yi-video.conf:44 | final-exact | -i.vip.iqiyi.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | final-exact | damang.api.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | final-exact | dc?.bz.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | final-exact | hb-boom.api.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | final-exact | me.bz.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | final-exact | mobile-thor.api.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | final-exact | mobile.api.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | final-exact | mobileso.bz.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-music.conf:53 | final-exact | interface.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-music.conf:53 | final-exact | interface3.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-music.conf:53 | final-exact | interface9.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-music.conf:53 | final-exact | ipv4.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-news.conf:29 | final-exact | interface.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-news.conf:29 | final-exact | interface3?.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/spotify.conf:17 | final-exact | spclient.wg.spotify.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/tencent-video.conf:33 | final-exact | vv.video.qq.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/youku.conf:40 | final-exact | push.m.youku.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/youku.conf:40 | final-exact | un-acs.youku.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/youtube.conf:26 | final-exact | youtubei.googleapis.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | Rewrite/Sources/Apps/i-qi-yi-video.conf:44 | final-exact | *.iqiyi.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | Rewrite/Sources/Apps/spotify.conf:17 | final-exact | *spclient.spotify.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | Rewrite/Sources/Apps/youtube.conf:26 | final-exact | *.googlevideo.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | Rewrite/Sources/Apps/caixin-media.conf:28 | final-exact | e*.caixin.com | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | Rewrite/Sources/Apps/caixin-media.conf:28 | final-exact | g*.caixin.com | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | Rewrite/Sources/Apps/caixin-media.conf:28 | final-exact | m*.caixin.com | 包含通配 MITM 范围 |

## 建议处理流程

1. 用户反馈具体 App 和现象后，先搜索本报告的 `entry` 或 `source`。
2. 同时查看 `reports/protected_traffic_ledger.md` 是否已有保护链路。
3. 如果是误伤，优先在最小源文件里注释、缩窄或添加精确保护。
4. 运行 `python scripts/quality_gate.py`。
5. 在 `docs/ai/RISK_LOG.md` 记录证据、处理结论和回滚路径。
