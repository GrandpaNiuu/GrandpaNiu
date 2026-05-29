# Module Factory Diff Report

Root lines: 2825
Release lines: 2840
Diff lines: 964
Diff clipped: yes

```diff
--- Ronghemokuai.sgmodule
+++ Release/Ronghemokuai.sgmodule
@@ -12,113 +12,47 @@
 # changelog: 修复 IPv6 CIDR 与拼多多 IPv6 正则；移除 Dreame ZIP 注入、粉笔第三方图片注入、Bilibili 伪会员改写；新增 cmp_ 脚本层。
 # arguments: YouTube Enhance 参数沿用上游，字幕/歌词翻译默认关闭以降低兼容风险。
 [Rule]
-# Spotify playback protection rules
-# Keep these rules before remote advertising sources.
+# Direct rules
+DOMAIN,dorangesource.alicdn.com,DIRECT
+DOMAIN,push.m.youku.com,DIRECT
+DOMAIN,un-acs.youku.com,DIRECT
+DOMAIN-SUFFIX,soulapp.cn,DIRECT
+IP-CIDR,8.210.3.170/32,DIRECT,no-resolve
+IP-CIDR,47.75.72.47/32,DIRECT,no-resolve
+# Spotify rules
 DOMAIN-SUFFIX,spotify.com,DIRECT
 DOMAIN-SUFFIX,scdn.co,DIRECT
 DOMAIN-SUFFIX,spotifycdn.com,DIRECT
 DOMAIN-SUFFIX,pscdn.co,DIRECT
 DOMAIN,spclient.wg.spotify.com,DIRECT
 DOMAIN-SUFFIX,spclient.spotify.com,DIRECT
-# YouTube playback protection placeholder
-# Keep this file available for future precise DIRECT rules.
-# Do not add broad googlevideo or google domains unless a specific conflict is confirmed.
+DOMAIN,ads-img-qc.xhscdn.com,REJECT,pre-matching
+DOMAIN,ads-video-al.xhscdn.com,REJECT,pre-matching
+DOMAIN,ads-video-qc.xhscdn.com,REJECT,pre-matching
+# YouTube rules
+AND,((DOMAIN-SUFFIX,googlevideo.com), (PROTOCOL,UDP)),REJECT
+AND,((DOMAIN,youtubei.googleapis.com), (PROTOCOL,UDP)),REJECT
 # Reject rules
-# remote: blackmatrix7 Advertising
-RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list,REJECT
-# remote: Cats-Team AdRules
-DOMAIN-SET,https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt,REJECT
-# remote: anti-AD Surge
-RULE-SET,https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt,REJECT
-# remote: ACL4SSR BanAD
-RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list,REJECT
-# remote: Loyalsoldier reject
-RULE-SET,https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt,REJECT
-# remote: 217heidai adblockfilters
-RULE-SET,https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list,REJECT
-# Spotify 白名单：放在远程广告规则前，避免广告规则误杀播放链路导致跳歌
-# === 新框架 Layer 1：基础拦截层 ===
-# 顺序原则：必要 DIRECT 白名单优先，其后远程广告规则、本地域名/IP、URL-REGEX/AND 逻辑。
-# 安全边界：不主动拦截支付、登录、验证码、银行证券、微信/支付宝安全、证书校验接口。
-# GitHub 去广告规则补充（Surge 端按远程资源自动更新）
-# === Remote AdBlock Hub：远程广告规则增强层 ===
-# 只添加可信远程规则，不覆盖本地规则；用于补充国内外网页、App 通用广告域名。
-DOMAIN,dorangesource.alicdn.com,DIRECT
-DOMAIN,push.m.youku.com,DIRECT
-DOMAIN,un-acs.youku.com,DIRECT
-DOMAIN-SUFFIX,soulapp.cn,DIRECT
-IP-CIDR,8.210.3.170/32,DIRECT,no-resolve
-IP-CIDR,47.75.72.47/32,DIRECT,no-resolve
-DOMAIN,access.if.iqiyi.com,REJECT,pre-matching
 DOMAIN,ad-analysis.pconline.com.cn,REJECT,pre-matching
 DOMAIN,ad-cdn.qingting.fm,REJECT,pre-matching
-DOMAIN,ad-h5-cdn.soulapp.cn,REJECT,pre-matching
-DOMAIN,ad-h5-station-cdn.soulapp.cn,REJECT,pre-matching
-DOMAIN,ad-r.soulapp.cn,REJECT,pre-matching
 DOMAIN,ad-stat.ksosoft.com,REJECT,pre-matching
-DOMAIN,ad.21cn.com,REJECT,pre-matching
-DOMAIN,ad.api.moji.com,REJECT,pre-matching
-DOMAIN,ad.chelaile.net.cn,REJECT,pre-matching
-DOMAIN,ad.cyapi.cn,REJECT,pre-matching
-DOMAIN,ad.iot.360.cn,REJECT,pre-matching
-DOMAIN,ad.jia.360.cn,REJECT,pre-matching
-DOMAIN,ad.k.21cn.com,REJECT,pre-matching
-DOMAIN,ad.mcloud.139.com,REJECT,pre-matching
-DOMAIN,ad.qingting.fm,REJECT,pre-matching
-DOMAIN,ad.seeyouyima.com,REJECT,pre-matching
-DOMAIN,ad.tencentmusic.com,REJECT,pre-matching
-DOMAIN,adashx.m.taobao.com,REJECT,pre-matching
-DOMAIN,adbehavior.wsa.ximalaya.com,REJECT,pre-matching
-DOMAIN,adbehavior.ximalaya.com,REJECT,pre-matching
-DOMAIN,adlaunch.moji.com,REJECT,pre-matching
 DOMAIN,adlaunch.qingting.fm,REJECT,pre-matching
 DOMAIN,admarket.21cn.com,REJECT,pre-matching
 DOMAIN,admarketing.yahoo.net,REJECT,pre-matching
 DOMAIN,admusicpic.music.126.net,REJECT,pre-matching
-DOMAIN,ads-img-qc.xhscdn.com,REJECT,pre-matching
-DOMAIN,ads-shopping.shouqianba.com,REJECT,pre-matching
-DOMAIN,ads-video-al.xhscdn.com,REJECT,pre-matching
-DOMAIN,ads-video-qc.xhscdn.com,REJECT,pre-matching
-DOMAIN,ads.auctions.yahoo.com,REJECT,pre-matching
-DOMAIN,ads.finance.yahoo.com,REJECT,pre-matching
-DOMAIN,ads.mojicdn.com,REJECT,pre-matching
-DOMAIN,ads.reader.yueyouxs.com,REJECT,pre-matching
-DOMAIN,ads.service.kugou.com,REJECT,pre-matching
-DOMAIN,ads.ysepay.com,REJECT,pre-matching
-DOMAIN,adse.wsa.ximalaya.com,REJECT,pre-matching
-DOMAIN,adse.ximalaya.com,REJECT,pre-matching
-DOMAIN,adsehera.ximalaya.com,REJECT,pre-matching
-DOMAIN,adservice.kugou.com,REJECT,pre-matching
-DOMAIN,adserviceretry.kglink.cn,REJECT,pre-matching
-DOMAIN,adserviceretry.kugou.com,REJECT,pre-matching
-DOMAIN,adshows.21cn.com,REJECT,pre-matching
-DOMAIN,adsmind.gdtimg.com,REJECT,pre-matching
-DOMAIN,adsmind.ugdtimg.com,REJECT,pre-matching
-DOMAIN,adsp.xunlei.com,REJECT,pre-matching
-DOMAIN,adstats.tencentmusic.com,REJECT,pre-matching
 DOMAIN,adui.tg.meitu.com,REJECT,pre-matching
 DOMAIN,adv-adlog.variflight.com,REJECT,pre-matching
-DOMAIN,adv-ads.variflight.com,REJECT,pre-matching
-DOMAIN,advert.mafengwo.cn,REJECT,pre-matching
-DOMAIN,advertise.baicizhan.com,REJECT,pre-matching
-DOMAIN,advertise.baicizhan.org,REJECT,pre-matching
 DOMAIN,adx-api.zdmimg.com,REJECT,pre-matching
-DOMAIN,adx-core.youku.com,REJECT,pre-matching
-DOMAIN,adx-open-service.youku.com,REJECT,pre-matching
 DOMAIN,adx-os.bridgeturbo.com,REJECT,pre-matching
 DOMAIN,adx.yiche.com,REJECT,pre-matching
 DOMAIN,adx.zuoyebang.com,REJECT,pre-matching
 DOMAIN,afdconf.baidu.com,REJECT,pre-matching
 DOMAIN,amap-aos-info-nogw.amap.com,REJECT,pre-matching
-DOMAIN,amdc.m.youku.com,REJECT,pre-matching
-DOMAIN,analytics.umetrip.com,REJECT,pre-matching
 DOMAIN,api.biliapi.com,REJECT,pre-matching
 DOMAIN,api.biliapi.net,REJECT,pre-matching
-DOMAIN,api.iqiyi.com,REJECT,pre-matching
 DOMAIN,apm-native.xiaohongshu.com,REJECT,pre-matching
 DOMAIN,apm.gotokeep.com,REJECT,pre-matching
 DOMAIN,apmplus.volces.com,REJECT,pre-matching
-DOMAIN,app-ad.variflight.com,REJECT,pre-matching
 DOMAIN,app.biliapi.com,REJECT,pre-matching
 DOMAIN,app.biliapi.net,REJECT,pre-matching
 DOMAIN,appcloud.zhihu.com,REJECT,pre-matching
@@ -129,12 +63,9 @@
 DOMAIN,atrace.chelaile.net.cn,REJECT,pre-matching
 DOMAIN,axxd.xmseeyouyima.com,REJECT,pre-matching
 DOMAIN,badjs.weixinbridge.com,REJECT,pre-matching
-DOMAIN,cad.youku.com,REJECT,pre-matching
 DOMAIN,cd-1.pddpic.com,REJECT,pre-matching
 DOMAIN,cdl-1.pddpic.com,REJECT,pre-matching
 DOMAIN,cdl-p2.pddpic.com,REJECT,pre-matching
-DOMAIN,cdn-ad.wtzw.com,REJECT,pre-matching
-DOMAIN,cdn-new-ad.wtzw.com,REJECT,pre-matching
 DOMAIN,collect.xiaopeng.com,REJECT,pre-matching
 DOMAIN,counter.kingsoft.com,REJECT,pre-matching
 DOMAIN,counter.ksosoft.com,REJECT,pre-matching
@@ -149,22 +80,14 @@
 DOMAIN,dflow.bz.mgtv.com,REJECT,pre-matching
 DOMAIN,dns.weixin.qq.com.cn,REJECT,pre-matching
 DOMAIN,dpmtpush.dianping.com,REJECT,pre-matching
-DOMAIN,dr-danmu.youku.com,REJECT,pre-matching
-DOMAIN,dsp-ad.yy.com,REJECT,pre-matching
-DOMAIN,dwtracking.jk.cn,REJECT,pre-matching
 DOMAIN,dynamicf.sankuai.com,REJECT,pre-matching
-DOMAIN,emdcadvertise.eastmoney.com,REJECT,pre-matching
-DOMAIN,emdcadvertisepj.eastmoney.com,REJECT,pre-matching
-DOMAIN,ems.youku.com,REJECT,pre-matching
 DOMAIN,encounter.bz.mgtv.com,REJECT,pre-matching
 DOMAIN,et.ykccn.com,REJECT,pre-matching
 DOMAIN,etl.xlmc.sandai.net,REJECT,pre-matching
 DOMAIN,floor.bz.mgtv.com,REJECT,pre-matching
 DOMAIN,free-aos-cdn-image.amap.com,REJECT,pre-matching
 DOMAIN,gather.colorfulclouds.net,REJECT,pre-matching
-DOMAIN,group-ssl-danmu-ori.youku.com,REJECT,pre-matching
 DOMAIN,gwp.xiaojukeji.com,REJECT,pre-matching
-DOMAIN,h-adashx.ut.taobao.com,REJECT,pre-matching
 DOMAIN,hc-ssp.sm.cn,REJECT,pre-matching
 DOMAIN,hlx.meituan.com,REJECT,pre-matching
 DOMAIN,httpdns-sdk.n.netease.com,REJECT,pre-matching
@@ -185,13 +108,11 @@
 DOMAIN,iadmusicmatvideo.music.126.net,REJECT,pre-matching
 DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching
 DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching
-DOMAIN,img.auction-ads.wpscdn.cn,REJECT,pre-matching
 DOMAIN,imgad0.pcauto.com.cn,REJECT,pre-matching
 DOMAIN,imgad0.pconline.com.cn,REJECT,pre-matching
 DOMAIN,ipv4.music.163.com,REJECT,pre-matching
 DOMAIN,ipv6.music.163.com,REJECT,pre-matching
 DOMAIN,ivy.pchouse.com.cn,REJECT,pre-matching
-DOMAIN,kad.gotokeep.com,REJECT,pre-matching
 DOMAIN,layer.bz.mgtv.com,REJECT,pre-matching
 DOMAIN,layout.meituan.net,REJECT,pre-matching
 DOMAIN,lc.map.baidu.com,REJECT,pre-matching
@@ -203,25 +124,19 @@
 DOMAIN,log.ycapp.yiche.com,REJECT,pre-matching
 DOMAIN,logs.chelaile.net.cn,REJECT,pre-matching
 DOMAIN,lx0.meituan.com,REJECT,pre-matching
-DOMAIN,m.atm.youku.com,REJECT,pre-matching
 DOMAIN,mall-dsp2.qinlinkeji.com,REJECT,pre-matching
 DOMAIN,mallapi2.qinlinkeji.com,REJECT,pre-matching
-DOMAIN,mbads.paas.cmbchina.com,REJECT,pre-matching
-DOMAIN,mc.atm.youku.com,REJECT,pre-matching
 DOMAIN,mdap.mpaas.cn-hangzhou.aliyuncs.com,REJECT,pre-matching
 DOMAIN,meta.pinduoduo.com,REJECT,pre-matching
 DOMAIN,minfo.wps.cn,REJECT,pre-matching
 DOMAIN,mob.bz.mgtv.com,REJECT,pre-matching
-DOMAIN,mobad.ijinshan.com,REJECT,pre-matching
 DOMAIN,mqtt.zhihu.com,REJECT,pre-matching
 DOMAIN,msmp.abchina.com.cn,REJECT,pre-matching
 DOMAIN,music.httpdns.c.163.com,REJECT,pre-matching
 DOMAIN,nbsdk-baichuan.alicdn.com,REJECT,pre-matching
-DOMAIN,open-pixon.ads-pixiv.net,REJECT,pre-matching
 DOMAIN,ossgw.alicdn.com,REJECT,pre-matching
 DOMAIN,popup.dushu365.com,REJECT,pre-matching
 DOMAIN,pp-cdnfile2pcdn.msstatic.com,REJECT,pre-matching
-DOMAIN,pre-acs.youku.com,REJECT,pre-matching
 DOMAIN,r.dianping.com,REJECT,pre-matching
 DOMAIN,rc-topic-api.bz.mgtv.com,REJECT,pre-matching
 DOMAIN,richmanapi.jxedt.com,REJECT,pre-matching
@@ -229,25 +144,17 @@
 DOMAIN,richmanrules.jxedt.com,REJECT,pre-matching
 DOMAIN,rprain.bz.mgtv.com,REJECT,pre-matching
 DOMAIN,rprain.log.mgtv.com,REJECT,pre-matching
-DOMAIN,rttrack.ddxq.mobi,REJECT,pre-matching
-DOMAIN,saad.ms.zhangyue.net,REJECT,pre-matching
 DOMAIN,sax.sina.com.cn,REJECT,pre-matching
 DOMAIN,saxn.sina.com.cn,REJECT,pre-matching
 DOMAIN,saxs.sina.com.cn,REJECT,pre-matching
-DOMAIN,sdk.ad.sfys365.com,REJECT,pre-matching
-DOMAIN,sdkconfig.ad.xiaomi.com,REJECT,pre-matching
 DOMAIN,sensors.umetrip.com.cn,REJECT,pre-matching
-DOMAIN,smad.ms.zhangyue.net,REJECT,pre-matching
 DOMAIN,smartop-sdkapi-ipv6.jiguang.cn,REJECT,pre-matching
 DOMAIN,smartop-sdkapi.jiguang.cn,REJECT,pre-matching
-DOMAIN,soul-ad.soulapp.cn,REJECT,pre-matching
 DOMAIN,splash.yy.com,REJECT,pre-matching
-DOMAIN,splashimgretrybssdl.cloud.kugou.com,REJECT,pre-matching
 DOMAIN,stat.youpin.mi.com,REJECT,pre-matching
 DOMAIN,stun1.douyucdn.cn,REJECT,pre-matching
 DOMAIN,stun1.qvb.qcloud.com,REJECT,pre-matching
 DOMAIN,sugar.zhihu.com,REJECT,pre-matching
-DOMAIN,t-ads.xiaohongshu.com,REJECT,pre-matching
 DOMAIN,ta-a.pinduoduo.com,REJECT,pre-matching
 DOMAIN,ta.pinduoduo.com,REJECT,pre-matching
 DOMAIN,th-a.pinduoduo.com,REJECT,pre-matching
@@ -256,15 +163,11 @@
 DOMAIN,titan.babytree.com,REJECT,pre-matching
 DOMAIN,titan.pinduoduo.com,REJECT,pre-matching
 DOMAIN,titan01.babytree.com,REJECT,pre-matching
-DOMAIN,track.58.com,REJECT,pre-matching
-DOMAIN,trackercollect.ddxq.mobi,REJECT,pre-matching
-DOMAIN,tracklog.58.com,REJECT,pre-matching
 DOMAIN,tte.meituan.com,REJECT,pre-matching
 DOMAIN,u1.img.mobile.sina.cn,REJECT,pre-matching
 DOMAIN,ucdc.upaas.quark.cn,REJECT,pre-matching
 DOMAIN,union.chinalifeonline.com.cn,REJECT,pre-matching
 DOMAIN,ups.ksmobile.net,REJECT,pre-matching
-DOMAIN,ut.taobao.com,REJECT,pre-matching
 DOMAIN,vali-g1.cp31.ott.cibntv.net,REJECT,pre-matching
 DOMAIN,vali-ugc.cp31.ott.cibntv.net,REJECT,pre-matching
 DOMAIN,vip.bz.mgtv.com,REJECT,pre-matching
@@ -272,34 +175,17 @@
 DOMAIN,wgo.mmstat.com,REJECT,pre-matching
 DOMAIN,ws.ksmobile.net,REJECT,pre-matching
 DOMAIN,xg.pinduoduo.com,REJECT,pre-matching
-DOMAIN,yk-ssp.ad.youku.com,REJECT,pre-matching
-DOMAIN,ykad-data.youku.com,REJECT,pre-matching
 DOMAIN,yl.zh.cmbchina.com,REJECT,pre-matching
 DOMAIN,ymg-api.terabox.com,REJECT,pre-matching
-DOMAIN,youku-acs.m.taobao.com,REJECT,pre-matching
-DOMAIN,youku-crm-product.youku.com,REJECT,pre-matching
-DOMAIN,ysad.yy.com,REJECT,pre-matching
 DOMAIN,yuyin-httpdns.gslb.yy.com,REJECT,pre-matching
 DOMAIN,zxid-m.mobileservice.cn,REJECT,pre-matching
 DOMAIN-SUFFIX,3rd.t.sohu.com,REJECT,pre-matching
 DOMAIN-SUFFIX,888.tv.sohu.com,REJECT,pre-matching
-DOMAIN-SUFFIX,ad.10010.com,REJECT,pre-matching
-DOMAIN-SUFFIX,ad.csdn.net,REJECT,pre-matching
-DOMAIN-SUFFIX,ad.e.waimai.sankuai.com,REJECT,pre-matching
-DOMAIN-SUFFIX,ad.hpplay.cn,REJECT,pre-matching
-DOMAIN-SUFFIX,ad.mail.sohu.com,REJECT,pre-matching
-DOMAIN-SUFFIX,ad.sohu.com,REJECT,pre-matching
 DOMAIN-SUFFIX,adcanvas.com,REJECT,pre-matching
 DOMAIN-SUFFIX,adeng.hpplay.cn,REJECT,pre-matching
 DOMAIN-SUFFIX,adjust.com,REJECT,pre-matching
 DOMAIN-SUFFIX,adnet.sohu.com,REJECT,pre-matching
-DOMAIN-SUFFIX,ads.linkedin.com,REJECT,pre-matching
-DOMAIN-SUFFIX,ads.sohu.com,REJECT,pre-matching
-DOMAIN-SUFFIX,adserver.yahoo.com,REJECT,pre-matching
-DOMAIN-SUFFIX,adsmoloco.com,REJECT,pre-matching
-DOMAIN-SUFFIX,adspecs.yahoo.com,REJECT,pre-matching
 DOMAIN-SUFFIX,adv.ccb.com,REJECT,pre-matching
-DOMAIN-SUFFIX,advertising.yahoo.com,REJECT,pre-matching
 DOMAIN-SUFFIX,adx-api.hupu.com,REJECT,pre-matching
 DOMAIN-SUFFIX,adx.hupu.com,REJECT,pre-matching
 DOMAIN-SUFFIX,afp.zol-img.com.cn,REJECT,pre-matching
@@ -323,7 +209,6 @@
 DOMAIN-SUFFIX,dc2.csdn.net,REJECT,pre-matching
 DOMAIN-SUFFIX,dynamic.zol.com.cn,REJECT,pre-matching
 DOMAIN-SUFFIX,ehaier.com,REJECT,pre-matching
-DOMAIN-SUFFIX,fds.api.moji.com,REJECT,pre-matching
 DOMAIN-SUFFIX,gdt.qq.com,REJECT,pre-matching
 DOMAIN-SUFFIX,gemini.yahoo.com,REJECT,pre-matching
 DOMAIN-SUFFIX,go.sohu.com,REJECT,pre-matching
@@ -331,14 +216,9 @@
 DOMAIN-SUFFIX,httpdns.meituan.com,REJECT,pre-matching
 DOMAIN-SUFFIX,hui.sohu.com,REJECT,pre-matching
 DOMAIN-SUFFIX,imp.zol.com.cn,REJECT,pre-matching
-DOMAIN-SUFFIX,iyes.youku.com,REJECT,pre-matching
 DOMAIN-SUFFIX,js.zol.com.cn,REJECT,pre-matching
-DOMAIN-SUFFIX,log.moji.com,REJECT,pre-matching
 DOMAIN-SUFFIX,lx.meituan.net,REJECT,pre-matching
-DOMAIN-SUFFIX,mads.meituan.com,REJECT,pre-matching
-DOMAIN-SUFFIX,me.api.moji.com,REJECT,pre-matching
 DOMAIN-SUFFIX,medal.blog.csdn.net,REJECT,pre-matching
-DOMAIN-SUFFIX,medproad.com,REJECT,pre-matching
 DOMAIN-SUFFIX,meituan.xn,REJECT,pre-matching
 DOMAIN-SUFFIX,meituan.yoga,REJECT,pre-matching
 DOMAIN-SUFFIX,meituangov.cn,REJECT,pre-matching
@@ -357,25 +237,17 @@
 DOMAIN-SUFFIX,pvtest.zol.com.cn,REJECT,pre-matching
 DOMAIN-SUFFIX,suvset.sohu.com,REJECT,pre-matching
 DOMAIN-SUFFIX,tappx.com,REJECT,pre-matching
-DOMAIN-SUFFIX,track.bankcomm.com,REJECT,pre-matching
-DOMAIN-SUFFIX,track.mm.taou.com,REJECT,pre-matching
-DOMAIN-SUFFIX,track.sohu.com,REJECT,pre-matching
-DOMAIN-SUFFIX,tracker.yhd.com,REJECT,pre-matching
 DOMAIN-SUFFIX,v.smtcdns.com,REJECT,pre-matching
 DOMAIN-SUFFIX,v1d.szbdyd.com,REJECT,pre-matching
 DOMAIN-SUFFIX,wappv.zol.com.cn,REJECT,pre-matching
 DOMAIN-SUFFIX,wmlog.meituan.com,REJECT,pre-matching
 DOMAIN-SUFFIX,wxs.qq.com,REJECT,pre-matching
 DOMAIN-SUFFIX,ydjs.zol.com.cn,REJECT,pre-matching
-DOMAIN-KEYWORD,ads.yahoo,REJECT,pre-matching
 DOMAIN-KEYWORD,apimg.qunliao.info,REJECT,pre-matching
-DOMAIN-KEYWORD,bj.imp.voiceads.cn,REJECT,pre-matching
 DOMAIN-KEYWORD,c-hzgt2.getui.com,REJECT,pre-matching
 DOMAIN-KEYWORD,cm-10-134.getui.com,REJECT,pre-matching
 DOMAIN-KEYWORD,cm-10-35.getui.com,REJECT,pre-matching
 DOMAIN-KEYWORD,dnspod.meituan.httpdns,REJECT,pre-matching
-DOMAIN-KEYWORD,iflyad.bj.openstorage.cn,REJECT,pre-matching
-DOMAIN-KEYWORD,m.panda.voiceads.cn,REJECT,pre-matching
 DOMAIN-KEYWORD,medicine.lanjiyin.com.cn,REJECT,pre-matching
 DOMAIN-KEYWORD,ossp.voicecloud.cn,REJECT,pre-matching
 DOMAIN-KEYWORD,report.meituan,REJECT,pre-matching
@@ -406,9 +278,7 @@
 IP-CIDR,180.76.76.200/32,REJECT,no-resolve
 IP-CIDR,182.61.194.7/32,REJECT,no-resolve
 IP-CIDR6,2402:4e00:1200:ed00:0:9089:6dac:96b6/128,REJECT,no-resolve
-AND,((DOMAIN-SUFFIX,chat.bilibili.com),(OR,((DOMAIN-KEYWORD,stun),(DOMAIN-KEYWORD,tracker)))),REJECT
 AND,((PROTOCOL,QUIC),(DOMAIN,api.pinduoduo.com)),REJECT-NO-DROP
-AND,((PROTOCOL,QUIC),(DOMAIN,soulapp.cn)),REJECT-NO-DROP
 AND,((PROTOCOL,QUIC),(DOMAIN-SUFFIX,xiaohongshu.com)),REJECT-NO-DROP
 AND,((PROTOCOL,TCP),(DST-PORT,25641),(IP-ASN,45090,no-resolve)),REJECT
 AND,((PROTOCOL,TCP),(DST-PORT,25641),(IP-ASN,55990,no-resolve)),REJECT
@@ -419,73 +289,105 @@
 URL-REGEX,^https?:\/\/.+\/amdc\/mobileDispatch,REJECT
 URL-REGEX,^https?:\/\/a\.line\.me\/cs\/v\d\/oa$,REJECT-DROP
 URL-REGEX,^https?:\/\/a\.line\.me\/er\/l.*\/v\d\/event\/image,REJECT-TINYGIF
-URL-REGEX,^https?:\/\/a\.line\.me\/er\/lads\/v\d\/ei\?,REJECT-TINYGIF
-URL-REGEX,^https?:\/\/a\.line\.me\/lass\/api\/v\d\/ads$,REJECT-DROP
 URL-REGEX,^https?:\/\/a\.line\.me\/oa\/v\d\/e$,REJECT-DROP
 URL-REGEX,^https?:\/\/crs-event\.line\.me\/v\d\/imp,REJECT-DROP
 URL-REGEX,^https?:\/\/d\.line-scdn\.net\/lcp-prod-photo\/20.+\.(jpg|jpeg|png),REJECT-TINYGIF
 URL-REGEX,^https?:\/\/ec-bot-obs\.line-scdn\.net\/0h[0-9a-zA-Z_-]{50}[0-9a-zA-Z_-]*,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/file-share\.izuiyou\.com\/octopus\/media\/templates\/search_home_page_(nv|nv_v2)\/search_home_page_nv,REJECT
-URL-REGEX,^https?:\/\/log\.stat\.kugou\.com\/mobile\/ad\.html,REJECT
 URL-REGEX,^https?:\/\/mercury-gateway\.ixiaochuan\.cn\/mercury\/v1\/ad\/,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/obs\.line-scdn\.net\/0h.+\/(o|m)\d+x\d+$,REJECT-DROP
 URL-REGEX,^https?:\/\/obs\.line-scdn\.net\/0h.+\/\d+p\.mp4$,REJECT-DROP
 URL-REGEX,^https?:\/\/obs\.line-scdn\.net\/0hGH\d,REJECT-DROP
 URL-REGEX,^https?:\/\/obs\.line-scdn\.net\/0h[a-zA-Z0-9_-]{50}[a-zA-Z0-9_-]*,REJECT-DROP
 URL-REGEX,^https?:\/\/obs\.line-scdn\.net\/r\/linecrs\/.+\/m180x180$,REJECT-TINYGIF
-URL-REGEX,^https?:\/\/rich\.kuwo\.cn\/AdService\/,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/rich\.kuwo\.cn\/EcomResourceServer\/,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/scdn\.line-apps\.com\/lan\/document\/pageEvent\/line\/ios\/,REJECT-DROP
 URL-REGEX,^https?:\/\/scdn\.line-apps\.com\/lan\/image\/line\/bannerImageEvent\/,REJECT-DROP
-URL-REGEX,^https?:\/\/sch\.line\.me\/api\/v\d\/ads$,REJECT-DROP
 URL-REGEX,^https?:\/\/searchrecterm\.kuwo\.cn\/recterm\.s,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/uts-front\.line-apps\.com\/event$,REJECT-DROP
 URL-REGEX,^https?:\/\/uts-front\.line-apps\.com\/settings$,REJECT-DROP
 URL-REGEX,^https?:\/\/vip\d\.kuwo\.cn\/vip\/v\d\/sysinfo\?op=getRePayAndDoPayBox,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/album\/adBar\/,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/app\/newMenuList\/menuListInfo,REJECT-TINYGIF
-URL-REGEX,^https?:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/app\/pasterAdvert\/,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/app\/startup\/config,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/user\/freeMode\/,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/web-mmap-pay\.line-apps\.com\/tw\/liff\/campaign\/v1\/aggregate\/ad\/banner\/,REJECT-TINYGIF
 URL-REGEX,^https?:\/\/w\.line\.me\/adp\/api\/ad\/v\d\/,REJECT-DROP
 URL-REGEX,^https?:\/\/w{32}\.jddebug\.com\/diagnose\?,REJECT
-
-# YouTube Enhance（Maasea 必要规则，2026-05-25 上游检查）
-# 风险提示：阻断 YouTube QUIC/UDP 可提升 HTTPS MITM 与脚本命中率；若视频长期转圈，可临时注释以下两行测试。
-AND,((DOMAIN-SUFFIX,googlevideo.com), (PROTOCOL,UDP)),REJECT
-AND,((DOMAIN,youtubei.googleapis.com), (PROTOCOL,UDP)),REJECT
-
-# === Legacy 26.1.27 Selected Migration: Rule START ===
-# 从旧版融合模块逐条筛选迁移；仅加入缺失、低风险、非重复、非高风险去广告规则。
-DOMAIN,ad.thsi.cn,REJECT,pre-matching
-DOMAIN,ad.video.51togic.com,REJECT,pre-matching
-DOMAIN,ad.xiangji.qq.com,REJECT,pre-matching
-DOMAIN,ad.ximalaya.com,REJECT,pre-matching
 DOMAIN,adapi.izuiyou.com,REJECT,pre-matching
-DOMAIN,adbs.ximalaya.com,REJECT,pre-matching
 DOMAIN,adcdn.tencentmusic.com,REJECT,pre-matching
 DOMAIN,adcdn6.tencentmusic.com,REJECT,pre-matching
 DOMAIN,adexpo.tencentmusic.com,REJECT,pre-matching
 DOMAIN,adproxy.autohome.com.cn,REJECT,pre-matching
-DOMAIN,ads.zhinengxiyifang.cn,REJECT,pre-matching
+DOMAIN,api-ad-product.huxiu.com,REJECT,pre-matching
+DOMAIN,cdn.adapi.fotoable.com,REJECT,pre-matching
+DOMAIN,ssp-adx.myzaker.com,REJECT,pre-matching
+DOMAIN,video.market.xiaomi.com,REJECT,pre-matching
```
