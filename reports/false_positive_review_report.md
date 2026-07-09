# 误伤复核队列报告

- 生成时间：2026-07-10 03:02:53 +0800
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

| type | risk | category | source | entry | reason |
| --- | --- | --- | --- | --- | --- |
| MITM | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/appso.conf:12 | sso.ifanr.com | 命中敏感链路关键词 |
| MITM | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/mobile-clouds.conf:14 | jzts.cmpassport.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | pay.kkmh.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | ccmsupport-sz.tenpay.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | creditcardapp.bankcomm.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | mbmodule-openapi.paas.cmbchina.com | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | cdn-pay.kkmh.com | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/51-job.conf:12 | ^https://cupid\.51jobapp\.com/open/noauth/jobs/detail/sesame-competitive/ - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/51-job.conf:13 | ^https://cupid\.51jobapp\.com/open/noauth/jobs/job-detail/user-rights\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/51-job.conf:15 | ^https://cupid\.51jobapp\.com/launch-hub/open/noauth/popUp/ - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/51-job.conf:16 | ^https://cupid\.51jobapp\.com/launch-hub/open/noauth/popUp/getHomePagePopUp\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/appso.conf:9 | ^https?://sso\.ifanr\.com/jiong/IOS/appso/splash/ - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/blued.conf:10 | ^https?://social\.blued\.cn/users/no_auth/benefit - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/dao-meng-kong-jian.conf:10 | ^https?://appdmkj\.5idream\.net/v2/login/message/tip - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/etouch-ecalendar.conf:12 | ^https://client-lz\.rili\.cn/lizhi/api/auth/voice_room_entrance/list\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/huo-mao.conf:9 | ^https?://api\.huomao\.com/channels/loginAd - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/pu-pu-mall.conf:9 | ^https://j1\.pupuapi\.com/client/account/discount/order - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/wechat-mini-programs.conf:101 | ^https://gw-passenger-wap\.01zhuanche\.com/gw-passenger-wap/zhuanche-passenger-token/commonSkipToken/common/getAdList - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/wechat-mini-programs.conf:104 | ^https://passenger\.t3go\.cn/passenger-activity-api/notoken/api/v1/resource/getSource - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/wechat-mini-programs.conf:126 | ^https://api\.szbgcx\.cn/account/adv/ - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/xia-chu-fang.conf:10 | ^https://api\.xiachufang\.com/v2/account/feeds_v7\.json - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/Apps/xiao-hei-he.conf:9 | ^https://api\.xiaoheihe\.cn/account/get_ads_info_v2 - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:55 | ^https:\/\/api\.szbgcx\.cn\/account\/adv\/ - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:1332 | ^https?:\/\/social\.blued\.cn\/users\/no_auth\/benefit - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:1342 | ^https?:\/\/sso\.ifanr\.com\/jiong\/IOS\/appso\/splash\/ - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:1489 | ^https?:\/\/www\.onstar\.com\.cn\/mssos\/sos\/social\/v1\/community\/article\/page - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:346 | ^https?:\/\/api\.m\.jd\.com\/\?loginType=11 - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:415 | ^https?:\/\/api\.ulife\.group\/auth\/account\/entrance - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:416 | ^https?:\/\/api\.ulife\.group\/auth\/account\/getUpgradeStrategy - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:429 | ^https?:\/\/api\.xiachufang\.com\/v2\/account\/feeds_v7\.json - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:434 | ^https?:\/\/api\.xiaoheihe\.cn\/account\/get_ads_info - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:502 | ^https?:\/\/app\.ceair\.com\/customize\/security\/update - reject-200 | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:558 | ^https?:\/\/appdmkj\.5idream\.net\/v2\/login\/message\/tip - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:654 | ^https?:\/\/client-api-v\d\.oray\.com\/materials\/(?:SLCC_IOS_STARTUP\ | SLCC_IOS_DEVICE\ |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:656 | ^https?:\/\/client-lz\.rili\.cn\/lizhi\/api\/auth\/voice_room_entrance\/list\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:687 | ^https?:\/\/cupid\.51jobapp\.com\/launch-hub\/open\/noauth\/popUp\/ - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:688 | ^https?:\/\/cupid\.51jobapp\.com\/launch-hub\/open\/noauth\/popUp\/getHomePagePopUp\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:690 | ^https?:\/\/cupid\.51jobapp\.com\/open\/noauth\/jobs\/detail\/sesame-competitive\/ - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:691 | ^https?:\/\/cupid\.51jobapp\.com\/open\/noauth\/jobs\/job-detail\/user-rights\? - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:815 | ^https?:\/\/gateway\.cotticoffee\.com\/cotti-capi\/person\/homeLoginPrompt - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:844 | ^https?:\/\/gw-passenger\.01zhuanche\.com\/gw-passenger\/zhuanche-passenger-token\/leachtoken\/webservice\/homepage\/queryADs - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:933 | ^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(side-bar\/mini-program\/music-service\/account\ | delivery\/(?:batch-deliver\ |
| REJECT | high | 登录 / 账号 / 鉴权 | Rewrite/Sources/URL-Rewrite.conf:934 | ^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(vipcenter\/tspopup\/get\ | vipauth\/app\/auth\ |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | Rewrite/Sources/Apps/aiinquiry.conf:15 | ^https://aiqicha\.baidu\.com/m/getLoginWordsAjax - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | Rewrite/Sources/URL-Rewrite.conf:220 | ^https?:\/\/aiqicha\.baidu\.com\/m\/getLoginWordsAjax - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | Rewrite/Sources/URL-Rewrite.conf:354 | ^https?:\/\/api\.map\.baidu\.com\/\?qt=verify - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | Rewrite/Sources/Apps/seasun-jx3.conf:12 | ^https://jx3comm\.xoyocdn\.com/jx3gc/zhcn/login_ad/WebCareer/WebCareerTab\.txt - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite.conf:1014 | ^https?:\/\/m\.client\.10010\.com\/mobileService\/(activity\ | customer)\/(accountListData\ |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite.conf:1462 | ^https?:\/\/www\.dpfile\.com\/picasso\/picasso-qa\/src\/AnswerList\/AnswerList-bundle - reject | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite.conf:958 | ^https?:\/\/jx3comm\.xoyocdn\.com\/jx3gc\/zhcn\/login_ad\/WebCareer\/WebCareerTab\.txt - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:23 | ^https://creditcardapp\.bankcomm\.com/cnsvPmpaMdbcardWeb/page/getGuidePageAds - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:24 | ^https://mbmodule-openapi\.paas\.cmbchina\.com/graphic/v2/module/graphic - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Apps/wechat-mini-programs.conf:82 | ^https://ccmsupport-sz\.tenpay\.com/cgi-bin/common/ccm_page_element.cgi - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Rule.conf:101 | DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/Rule.conf:102 | DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:10 | ^https:\/\/creditcardapp\.bankcomm\.com\/cnsvPmpaMdbcardWeb\/page\/getGuidePageAds - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:13 | ^https:\/\/mbmodule-openapi\.paas\.cmbchina\.com\/graphic\/v2\/module\/graphic - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:52 | ^https:\/\/ccmsupport-sz\.tenpay\.com\/cgi-bin\/common\/ccm_page_element.cgi - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite.conf:1023 | ^https?:\/\/m\.qianbao\.qq\.com\/pages\/walletHome\?invisible - reject | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite.conf:1024 | ^https?:\/\/m\.qianbao\.qq\.com\/services\/walletHome\/get(QQshop\ | Game\ |
| REJECT | high | 银行 / 支付 / 钱包 | Rewrite/Sources/URL-Rewrite.conf:320 | ^https?:\/\/api\.hellobike\.com\/api\?homepage\.newWelfare\.alipay - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/qingrex-miniapp-app-ad.list:30 | DOMAIN-KEYWORD,adv.ccb.com,REJECT,extended-matching,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/reject.list:73 | DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/reject.list:74 | DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/reject.list:98 | DOMAIN,msmp.abchina.com.cn,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/web-ads.list:16 | DOMAIN,ads.ysepay.com,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/web-ads.list:37 | DOMAIN,mbads.paas.cmbchina.com,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | Rules/web-ads.list:64 | DOMAIN-SUFFIX,track.bankcomm.com,REJECT,pre-matching | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 国内 App 核心 API | Rewrite/Sources/URL-Rewrite.conf:1159 | ^https?:\/\/npay\.meituan\.com\/conch\/flow\/mypage-wallet-info - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 国内 App 核心 API | Rewrite/Sources/URL-Rewrite.conf:1160 | ^https?:\/\/npay\.meituan\.com\/conch\/walletv\d\/wechat-pop-window - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:27 | ^https://(cdn-)?pay\.kkmh\.com/v\d/kb/wallet - reject-dict | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:111 | ^http:\/\/image1\.ccb\.com\/newsinfo\/eBranch\/check\/(?:nf\/newfin\/activity\ | po\/poortheme\/activity)\/\w+\.png - reject |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | Rewrite/Sources/URL-Rewrite.conf:40 | ^https?:\/\/(cdn-)?pay\.kkmh\.com\/v\d\/kb\/(?:wallet\ | comic_page_banner) - reject-dict |

## medium 抽样复核队列

| type | risk | category | source | entry | reason |
| --- | --- | --- | --- | --- | --- |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/aiinquiry.conf:22 | aiqicha.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-input-method.conf:20 | imeres.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-input-method.conf:20 | mbd.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-input-method.conf:20 | mime.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-map.conf:25 | afd.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-map.conf:25 | ecom.map.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-map.conf:25 | newclient.map.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-map.conf:25 | yongche.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-net-disk.conf:21 | pan.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-photo.conf:16 | mbd.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-photo.conf:16 | pan.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-translation.conf:13 | mime.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-wenku.conf:34 | appwk.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu-wenku.conf:34 | tanbi.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu.conf:12 | m.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidu.conf:12 | www.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/baidupan.conf:27 | pan.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/damai.conf:18 | acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/i-mai-cai.conf:21 | mall.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/i-mai-cai.conf:21 | portal-portm.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/jd.conf:23 | api.m.jd.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/jdwaimai.conf:19 | api.m.jd.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | apimobile.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | cdb.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | mall.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | rms.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | web.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/meituan.conf:30 | wmapi.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/pinduoduo.conf:85 | api.pinduoduo.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/robo-taxi.conf:14 | idgdata.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/taobao-travel.conf:16 | acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/taobao.conf:44 | acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/taobao.conf:44 | guide-acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/taopiaopiao.conf:19 | acs.m.taobao.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/tieba.conf:18 | tiebac.baidu.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | api.pinduoduo.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | rms.meituan.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/wechat-official-accounts.conf:16 | mp.weixin.qq.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | Rewrite/Sources/Apps/wechat.conf:17 | mp.weixin.qq.com | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API / 通配 MITM | Rewrite/Sources/Apps/amap.conf:81 | *.amap.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 国内 App 核心 API / 通配 MITM | Rewrite/Sources/Apps/meituan.conf:30 | *.dianping.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/baby-tree-parenting.conf:16 | aimg.babytreeimg.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/caiyun-weather.conf:22 | cdn-w.caiyunapp.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/che-lai-le.conf:23 | pic1.chelaile.net.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/clicli.conf:12 | js-ad.ayximgs.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/di-duan-ying-shi.conf:15 | img.ddrk.me | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/dian-shi-jia.conf:13 | cdn.dianshihome.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/dlabel-cloud-tag.conf:13 | imagepc.ctaiot.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/douyu.conf:27 | apiv2.douyucdn.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/douyu.conf:27 | rtbapi.douyucdn.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/douyu.conf:27 | venus.douyucdn.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/jie-mian-news.conf:12 | img.jiemian.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kingsoft-power-word.conf:26 | mobile-pic.cache.iciba.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | cdn-api.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | cdn-h5.kuaikanmanhua.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | cdn-shop.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | cdn-social.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | cdn-topic.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/kuai-kan-comic.conf:43 | topic.kkmh.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/lenovo-print.conf:12 | abcapi.lenovoimage.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | ad.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | d.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | ec-bot-obs.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | obs.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | scdn.line-apps.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/line.conf:51 | static.line-scdn.net | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/lofter.conf:14 | images.pinduoduo.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/ma-ka-long-wan-tu.conf:13 | static01.versa-ai.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/ma-ma-wang-yun-yu.conf:12 | qimg.cdnmama.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/mai-dui-dui.conf:19 | conf-darwin.xycdn.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/mai-dui-dui.conf:19 | mobads-pre-config.cdn.bcebos.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/mkz.conf:18 | base.mkzcdn.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/picc-insurance.conf:19 | zgrb.epicc.com.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/qi-shui-music.conf:16 | lf-cdn-tos.bytescm.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/qi-xin-bao.conf:21 | qxb-minicode-pic-osscache.qixin.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/quan-min-ge-ge.conf:12 | y.gtimg.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/seasun-jx3.conf:15 | jx3comm.xoyocdn.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/seven-cat.conf:32 | cdn.wtzw.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/sf-express.conf:19 | ucmp-static.sf-express.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/sogou-input.conf:16 | business-cdn.shouji.sogou.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/taobao.conf:44 | heic.alicdn.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/tencent-games-community.conf:12 | static.gameplus.qq.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/tencent-sports.conf:13 | sports3.gtimg.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/ttvoice.conf:12 | ga-album-cdnqn.52tt.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | appuser-static.huolala.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | fscdn.zto.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/wechat-mini-programs.conf:167 | images.qmai.cn | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/xfuse.conf:12 | img.mofyi.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/xiaojukeji-charge.conf:20 | am.didistatic.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | Rewrite/Sources/Apps/zdm.conf:57 | haojia-cdn.smzdm.com | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | Rewrite/Sources/Apps/58-tong-cheng.conf:34 | *.58cdn.com.cn | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | Rewrite/Sources/Apps/che-lai-le.conf:23 | cdn.*.chelaileapp.cn | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | Rewrite/Sources/Apps/huya.conf:14 | *.msstatic.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | Rewrite/Sources/Apps/qqksong.conf:52 | amsweb-cdn-*-1258344696.file.myqcloud.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/bilibili.conf:87 | grpc.biliapi.net | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/i-qi-yi-video.conf:44 | -i.vip.iqiyi.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | damang.api.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | dc?.bz.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | hb-boom.api.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | me.bz.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | mobile-thor.api.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | mobile.api.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/mgtv.conf:64 | mobileso.bz.mgtv.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-music.conf:53 | interface.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-music.conf:53 | interface3.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-music.conf:53 | interface9.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-music.conf:53 | ipv4.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-news.conf:29 | interface.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/netease-news.conf:29 | interface3?.music.163.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/spotify.conf:17 | spclient.wg.spotify.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/tencent-video.conf:33 | vv.video.qq.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/youku.conf:40 | push.m.youku.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/youku.conf:40 | un-acs.youku.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | Rewrite/Sources/Apps/youtube.conf:26 | youtubei.googleapis.com | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | Rewrite/Sources/Apps/i-qi-yi-video.conf:44 | *.iqiyi.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | Rewrite/Sources/Apps/spotify.conf:17 | *spclient.spotify.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | Rewrite/Sources/Apps/youtube.conf:26 | *.googlevideo.com | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | Rewrite/Sources/Apps/caixin-media.conf:28 | e*.caixin.com | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | Rewrite/Sources/Apps/caixin-media.conf:28 | g*.caixin.com | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | Rewrite/Sources/Apps/caixin-media.conf:28 | m*.caixin.com | 包含通配 MITM 范围 |

## 建议处理流程

1. 用户反馈具体 App 和现象后，先搜索本报告的 `entry` 或 `source`。
2. 同时查看 `reports/protected_traffic_ledger.md` 是否已有保护链路。
3. 如果是误伤，优先在最小源文件里注释、缩窄或添加精确保护。
4. 运行 `python scripts/quality_gate.py`。
5. 在 `docs/ai/RISK_LOG.md` 记录证据、处理结论和回滚路径。
