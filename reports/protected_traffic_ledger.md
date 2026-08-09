# 保护链路台账

- 生成时间：2026-08-10 01:52:30 +0800
- 扫描源文件：9
- 保护/候选条目：179
- DIRECT 条目：150
- 非 DIRECT 条目：29

## 使用边界

- 本报告只记录登录、支付、银行、验证码、视频、图片/CDN、HTTPDNS 等保护链路来源。
- 它不是自动放行清单，也不会修改规则。
- 出现 App 无网络、无法登录、无法播放或图片空白时，先查本台账和 MITM/REJECT 风险台账，再做单点源文件调整。

## 分类统计

| category | entries |
| --- | --- |
| 其他保护 / 需人工归类 | 48 |
| 图片 / 静态 CDN | 39 |
| 验证码 / HTTPDNS / 核心 API | 34 |
| 支付 / 银行 / 订单 | 28 |
| 登录 / 账号 | 20 |
| 视频 / 音乐播放 | 16 |

## 源文件统计

| source_file | entries | exists |
| --- | --- | --- |
| Rules/direct.list | 74 | True |
| Rules/protect-login.list | 26 | True |
| Rewrite/Sources/Misc/finance-protect.conf | 15 | True |
| Rewrite/Sources/Misc/cdn-direct.conf | 15 | True |
| Rewrite/Sources/Misc/httpdns.conf | 15 | True |
| Rules/protect-payment.list | 12 | True |
| Rules/protect-video.list | 12 | True |
| Rules/protect-cdn.list | 6 | True |
| Rewrite/Sources/Misc/video-protect.conf | 4 | True |

## 非 DIRECT 条目提示

这些条目位于保护相关源文件中，但策略不是 DIRECT。它们可能是 App 特定广告例外，不应自动删除；未来如发生误伤需单点复核。

| source | policy | line |
| --- | --- | --- |
| Rules/protect-login.list:14 | OTHER | DOMAIN-SUFFIX,accounts.google.com,PROXY |
| Rules/protect-login.list:15 | OTHER | DOMAIN-SUFFIX,google.com,PROXY |
| Rules/protect-login.list:16 | OTHER | DOMAIN-SUFFIX,gstatic.com,PROXY |
| Rules/protect-login.list:17 | OTHER | DOMAIN-SUFFIX,googleapis.com,PROXY |
| Rules/protect-login.list:19 | OTHER | DOMAIN-SUFFIX,facebook.com,PROXY |
| Rules/protect-login.list:20 | OTHER | DOMAIN-SUFFIX,fbcdn.net,PROXY |
| Rules/protect-login.list:21 | OTHER | DOMAIN-SUFFIX,instagram.com,PROXY |
| Rules/protect-login.list:22 | OTHER | DOMAIN-SUFFIX,cdninstagram.com,PROXY |
| Rules/protect-login.list:23 | OTHER | DOMAIN-SUFFIX,whatsapp.com,PROXY |
| Rules/protect-login.list:24 | OTHER | DOMAIN-SUFFIX,whatsapp.net,PROXY |
| Rules/protect-login.list:25 | OTHER | DOMAIN-SUFFIX,telegram.org,PROXY |
| Rules/protect-login.list:26 | OTHER | DOMAIN-SUFFIX,t.me,PROXY |
| Rules/protect-login.list:27 | OTHER | DOMAIN-SUFFIX,discord.com,PROXY |
| Rules/protect-login.list:28 | OTHER | DOMAIN-SUFFIX,discordapp.com,PROXY |
| Rules/protect-login.list:29 | OTHER | DOMAIN-SUFFIX,discordapp.net,PROXY |
| Rules/protect-login.list:30 | OTHER | DOMAIN-SUFFIX,reddit.com,PROXY |
| Rules/protect-login.list:31 | OTHER | DOMAIN-SUFFIX,redditmedia.com,PROXY |
| Rules/protect-video.list:10 | OTHER | DOMAIN-SUFFIX,googlevideo.com,PROXY,pre-matching |
| Rules/protect-video.list:11 | OTHER | DOMAIN,youtubei.googleapis.com,PROXY,pre-matching |
| Rules/protect-video.list:12 | OTHER | DOMAIN-SUFFIX,ytimg.com,PROXY,pre-matching |
| Rules/protect-video.list:13 | OTHER | DOMAIN-SUFFIX,ggpht.com,PROXY,pre-matching |
| Rules/protect-video.list:14 | OTHER | DOMAIN-SUFFIX,netflix.com,PROXY,pre-matching |
| Rules/protect-video.list:15 | OTHER | DOMAIN-SUFFIX,nflxvideo.net,PROXY,pre-matching |
| Rules/protect-video.list:16 | OTHER | DOMAIN-SUFFIX,nflximg.net,PROXY,pre-matching |
| Rewrite/Sources/Misc/cdn-direct.conf:5 | REJECT | AND,((DOMAIN-SUFFIX,pddpic.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching |
| Rewrite/Sources/Misc/cdn-direct.conf:6 | REJECT | AND,((DOMAIN-SUFFIX,pddcdn.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching |
| Rewrite/Sources/Misc/cdn-direct.conf:7 | REJECT | AND,((DOMAIN-SUFFIX,jdimg.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching |
| Rewrite/Sources/Misc/cdn-direct.conf:8 | REJECT | AND,((DOMAIN-SUFFIX,360buyimg.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching |
| Rewrite/Sources/Misc/cdn-direct.conf:9 | REJECT | URL-REGEX,"^https?:\/\/m\.360buyimg\.com\/(?:mobilecms\|babel)\/.*",REJECT-IMG,extended-matching |

## 分类样例

### 图片 / 静态 CDN

| source | policy | line |
| --- | --- | --- |
| Rules/direct.list:2 | DIRECT | DOMAIN,dorangesource.alicdn.com,DIRECT |
| Rules/direct.list:30 | DIRECT | DOMAIN,mmsns.qpic.cn,DIRECT,pre-matching |
| Rules/direct.list:31 | DIRECT | DOMAIN,shmmsns.qpic.cn,DIRECT,pre-matching |
| Rules/direct.list:33 | DIRECT | DOMAIN-SUFFIX,qpic.cn,DIRECT,pre-matching |
| Rules/direct.list:34 | DIRECT | DOMAIN-SUFFIX,gtimg.cn,DIRECT,pre-matching |
| Rules/direct.list:39 | DIRECT | DOMAIN-SUFFIX,alicdn.com,DIRECT,pre-matching |
| Rules/direct.list:40 | DIRECT | DOMAIN-SUFFIX,alicdn.net,DIRECT,pre-matching |
| Rules/direct.list:41 | DIRECT | DOMAIN-SUFFIX,tbcdn.cn,DIRECT,pre-matching |
| Rules/direct.list:42 | DIRECT | DOMAIN-SUFFIX,taobaocdn.com,DIRECT,pre-matching |
| Rules/direct.list:43 | DIRECT | DOMAIN-SUFFIX,360buyimg.com,DIRECT,pre-matching |
| Rules/direct.list:44 | DIRECT | DOMAIN-SUFFIX,jdimg.com,DIRECT,pre-matching |
| Rules/direct.list:45 | DIRECT | DOMAIN-SUFFIX,bdimg.com,DIRECT,pre-matching |
| Rules/direct.list:47 | DIRECT | DOMAIN-SUFFIX,biliimg.com,DIRECT,pre-matching |
| Rules/direct.list:51 | DIRECT | DOMAIN-SUFFIX,msstatic.com,DIRECT,pre-matching |
| Rules/direct.list:52 | DIRECT | DOMAIN-SUFFIX,zdmimg.com,DIRECT,pre-matching |
| Rules/direct.list:58 | DIRECT | DOMAIN,free-aos-cdn-image.amap.com,DIRECT,pre-matching |
| Rules/direct.list:84 | DIRECT | DOMAIN-SUFFIX,zijiecdn.com,DIRECT,pre-matching |
| Rules/protect-login.list:20 | OTHER | DOMAIN-SUFFIX,fbcdn.net,PROXY |
| Rules/protect-login.list:22 | OTHER | DOMAIN-SUFFIX,cdninstagram.com,PROXY |
| Rules/protect-video.list:12 | OTHER | DOMAIN-SUFFIX,ytimg.com,PROXY,pre-matching |

### 视频 / 音乐播放

| source | policy | line |
| --- | --- | --- |
| Rules/direct.list:3 | DIRECT | DOMAIN,push.m.youku.com,DIRECT |
| Rules/direct.list:4 | DIRECT | DOMAIN,un-acs.youku.com,DIRECT |
| Rules/direct.list:46 | DIRECT | DOMAIN-SUFFIX,hdslb.com,DIRECT,pre-matching |
| Rules/direct.list:48 | DIRECT | DOMAIN-SUFFIX,bilivideo.com,DIRECT,pre-matching |
| Rules/direct.list:74 | DIRECT | DOMAIN,httpdns.music.163.com,DIRECT,pre-matching |
| Rules/protect-video.list:5 | DIRECT | DOMAIN-SUFFIX,bilivideo.com,DIRECT |
| Rules/protect-video.list:6 | DIRECT | DOMAIN-SUFFIX,hdslb.com,DIRECT |
| Rules/protect-video.list:10 | OTHER | DOMAIN-SUFFIX,googlevideo.com,PROXY,pre-matching |
| Rules/protect-video.list:15 | OTHER | DOMAIN-SUFFIX,nflxvideo.net,PROXY,pre-matching |
| Rewrite/Sources/Misc/video-protect.conf:5 | DIRECT | DOMAIN-SUFFIX,bilivideo.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/video-protect.conf:6 | DIRECT | DOMAIN-SUFFIX,hdslb.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/video-protect.conf:7 | DIRECT | DOMAIN-SUFFIX,mgtv.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/video-protect.conf:8 | DIRECT | DOMAIN-SUFFIX,youku.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/cdn-direct.conf:15 | DIRECT | DOMAIN-SUFFIX,hdslb.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/cdn-direct.conf:17 | DIRECT | DOMAIN-SUFFIX,bilivideo.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/httpdns.conf:9 | DIRECT | DOMAIN,httpdns.music.163.com,DIRECT,pre-matching |

### 其他保护 / 需人工归类

| source | policy | line |
| --- | --- | --- |
| Rules/direct.list:5 | DIRECT | DOMAIN-SUFFIX,soulapp.cn,DIRECT |
| Rules/direct.list:6 | DIRECT | IP-CIDR,8.210.3.170/32,DIRECT,no-resolve |
| Rules/direct.list:7 | DIRECT | IP-CIDR,47.75.72.47/32,DIRECT,no-resolve |
| Rules/direct.list:22 | DIRECT | DOMAIN-SUFFIX,wx.qq.com,DIRECT,pre-matching |
| Rules/direct.list:27 | DIRECT | DOMAIN,wxs.qq.com,DIRECT,pre-matching |
| Rules/direct.list:28 | DIRECT | DOMAIN,res.wx.qq.com,DIRECT,pre-matching |
| Rules/direct.list:29 | DIRECT | DOMAIN,wxapp.tc.qq.com,DIRECT,pre-matching |
| Rules/direct.list:49 | DIRECT | DOMAIN-SUFFIX,meituan.net,DIRECT,pre-matching |
| Rules/direct.list:50 | DIRECT | DOMAIN-SUFFIX,dpfile.com,DIRECT,pre-matching |
| Rules/direct.list:53 | DIRECT | DOMAIN-SUFFIX,amap.com,DIRECT,pre-matching |
| Rules/direct.list:59 | DIRECT | DOMAIN,amap-aos-info-nogw.amap.com,DIRECT,pre-matching |
| Rules/direct.list:60 | DIRECT | DOMAIN,layout.meituan.net,DIRECT,pre-matching |
| Rules/direct.list:61 | DIRECT | DOMAIN,lc.map.baidu.com,DIRECT,pre-matching |
| Rules/direct.list:65 | DIRECT | DOMAIN,api.iqiyi.com,DIRECT,pre-matching |
| Rules/direct.list:66 | DIRECT | DOMAIN,api.bilibili.com,DIRECT,pre-matching |
| Rules/direct.list:67 | DIRECT | DOMAIN,app.bilibili.com,DIRECT,pre-matching |
| Rules/direct.list:86 | DIRECT | DOMAIN-SUFFIX,amemv.com,DIRECT,pre-matching |
| Rules/direct.list:87 | DIRECT | DOMAIN-SUFFIX,douyin.com,DIRECT,pre-matching |
| Rules/direct.list:88 | DIRECT | DOMAIN-SUFFIX,ixigua.com,DIRECT,pre-matching |
| Rules/direct.list:89 | DIRECT | DOMAIN-SUFFIX,toutiao.com,DIRECT,pre-matching |

### 支付 / 银行 / 订单

| source | policy | line |
| --- | --- | --- |
| Rules/direct.list:11 | DIRECT | DOMAIN-SUFFIX,ccb.com,DIRECT,pre-matching |
| Rules/direct.list:12 | DIRECT | DOMAIN-SUFFIX,abchina.com.cn,DIRECT,pre-matching |
| Rules/direct.list:13 | DIRECT | DOMAIN-SUFFIX,psbc.com,DIRECT,pre-matching |
| Rules/direct.list:14 | DIRECT | DOMAIN-SUFFIX,boc.cn,DIRECT,pre-matching |
| Rules/direct.list:15 | DIRECT | DOMAIN-SUFFIX,bankcomm.com,DIRECT,pre-matching |
| Rules/direct.list:16 | DIRECT | DOMAIN-SUFFIX,icbc.com.cn,DIRECT,pre-matching |
| Rules/direct.list:17 | DIRECT | DOMAIN-SUFFIX,cmbchina.com,DIRECT,pre-matching |
| Rules/direct.list:25 | DIRECT | DOMAIN-SUFFIX,wechatpay.cn,DIRECT,pre-matching |
| Rules/protect-payment.list:5 | DIRECT | DOMAIN-SUFFIX,alipay.com,DIRECT |
| Rules/protect-payment.list:6 | DIRECT | DOMAIN-SUFFIX,alipayobjects.com,DIRECT |
| Rules/protect-payment.list:8 | DIRECT | DOMAIN-SUFFIX,tenpay.com,DIRECT |
| Rules/protect-payment.list:9 | DIRECT | DOMAIN-SUFFIX,wechatpay.com,DIRECT |
| Rules/protect-payment.list:11 | DIRECT | DOMAIN-SUFFIX,unionpay.com,DIRECT |
| Rules/protect-payment.list:13 | DIRECT | DOMAIN-SUFFIX,paypal.com,DIRECT |
| Rules/protect-payment.list:14 | DIRECT | DOMAIN-SUFFIX,paypalobjects.com,DIRECT |
| Rewrite/Sources/Misc/finance-protect.conf:7 | DIRECT | DOMAIN-SUFFIX,wechatpay.cn,DIRECT,pre-matching |
| Rewrite/Sources/Misc/finance-protect.conf:8 | DIRECT | DOMAIN-SUFFIX,tenpay.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/finance-protect.conf:9 | DIRECT | DOMAIN-SUFFIX,alipay.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/finance-protect.conf:10 | DIRECT | DOMAIN-SUFFIX,alipayobjects.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/finance-protect.conf:11 | DIRECT | DOMAIN-SUFFIX,icbc.com.cn,DIRECT,pre-matching |

### 登录 / 账号

| source | policy | line |
| --- | --- | --- |
| Rules/direct.list:21 | DIRECT | DOMAIN-SUFFIX,weixin.qq.com,DIRECT,pre-matching |
| Rules/direct.list:23 | DIRECT | DOMAIN-SUFFIX,wechat.com,DIRECT,pre-matching |
| Rules/direct.list:24 | DIRECT | DOMAIN-SUFFIX,servicewechat.com,DIRECT,pre-matching |
| Rules/direct.list:25 | DIRECT | DOMAIN-SUFFIX,wechatpay.cn,DIRECT,pre-matching |
| Rules/direct.list:26 | DIRECT | DOMAIN,dns.weixin.qq.com.cn,DIRECT,pre-matching |
| Rules/direct.list:32 | DIRECT | DOMAIN,wx.qlogo.cn,DIRECT,pre-matching |
| Rules/direct.list:35 | DIRECT | DOMAIN-SUFFIX,weixinbridge.com,DIRECT,pre-matching |
| Rules/direct.list:36 | DIRECT | DOMAIN-SUFFIX,qlogo.cn,DIRECT,pre-matching |
| Rules/protect-login.list:6 | DIRECT | DOMAIN-SUFFIX,passport.jd.com,DIRECT |
| Rules/protect-login.list:7 | DIRECT | DOMAIN-SUFFIX,login.taobao.com,DIRECT |
| Rules/protect-login.list:8 | DIRECT | DOMAIN-SUFFIX,login.tmall.com,DIRECT |
| Rules/protect-login.list:9 | DIRECT | DOMAIN-SUFFIX,account.xiaomi.com,DIRECT |
| Rules/protect-login.list:10 | DIRECT | DOMAIN-SUFFIX,passport.baidu.com,DIRECT |
| Rules/protect-login.list:12 | DIRECT | DOMAIN-SUFFIX,open.weixin.qq.com,DIRECT |
| Rules/protect-login.list:14 | OTHER | DOMAIN-SUFFIX,accounts.google.com,PROXY |
| Rules/protect-login.list:18 | DIRECT | DOMAIN-SUFFIX,login.live.com,DIRECT |
| Rules/protect-payment.list:9 | DIRECT | DOMAIN-SUFFIX,wechatpay.com,DIRECT |
| Rules/protect-payment.list:10 | DIRECT | DOMAIN-SUFFIX,mch.weixin.qq.com,DIRECT |
| Rewrite/Sources/Misc/finance-protect.conf:5 | DIRECT | DOMAIN-SUFFIX,weixin.qq.com,DIRECT,pre-matching |
| Rewrite/Sources/Misc/finance-protect.conf:7 | DIRECT | DOMAIN-SUFFIX,wechatpay.cn,DIRECT,pre-matching |

### 验证码 / HTTPDNS / 核心 API

| source | policy | line |
| --- | --- | --- |
| Rules/direct.list:26 | DIRECT | DOMAIN,dns.weixin.qq.com.cn,DIRECT,pre-matching |
| Rules/direct.list:68 | DIRECT | DOMAIN,grpc.biliapi.net,DIRECT,pre-matching |
| Rules/direct.list:69 | DIRECT | DOMAIN-SUFFIX,biliapi.com,DIRECT,pre-matching |
| Rules/direct.list:70 | DIRECT | DOMAIN-SUFFIX,biliapi.net,DIRECT,pre-matching |
| Rules/direct.list:71 | DIRECT | DOMAIN,httpdns-sdk.n.netease.com,DIRECT,pre-matching |
| Rules/direct.list:72 | DIRECT | DOMAIN,httpdns.baidubce.com,DIRECT,pre-matching |
| Rules/direct.list:73 | DIRECT | DOMAIN,httpdns.calorietech.com,DIRECT,pre-matching |
| Rules/direct.list:74 | DIRECT | DOMAIN,httpdns.music.163.com,DIRECT,pre-matching |
| Rules/direct.list:75 | DIRECT | DOMAIN,httpdns.n.netease.com,DIRECT,pre-matching |
| Rules/direct.list:76 | DIRECT | DOMAIN,httpdns.yunxindns.com,DIRECT,pre-matching |
| Rules/direct.list:77 | DIRECT | DOMAIN,httpdnsmultiapi.meituan.com,DIRECT,pre-matching |
| Rules/direct.list:78 | DIRECT | DOMAIN,httpdnsmultiapivip.meituan.com,DIRECT,pre-matching |
| Rules/direct.list:79 | DIRECT | DOMAIN,hdns.ksyun.com,DIRECT,pre-matching |
| Rules/direct.list:80 | DIRECT | DOMAIN,lofter.httpdns.c.163.com,DIRECT,pre-matching |
| Rules/direct.list:81 | DIRECT | DOMAIN,music.httpdns.c.163.com,DIRECT,pre-matching |
| Rules/direct.list:82 | DIRECT | DOMAIN-SUFFIX,zijieapi.com,DIRECT,pre-matching |
| Rules/direct.list:83 | DIRECT | DOMAIN-SUFFIX,zijieapi.net,DIRECT,pre-matching |
| Rules/direct.list:85 | DIRECT | DOMAIN-SUFFIX,snssdk.com,DIRECT,pre-matching |
| Rules/protect-video.list:9 | DIRECT | DOMAIN-SUFFIX,akadns.net,DIRECT |
| Rewrite/Sources/Misc/httpdns.conf:5 | DIRECT | DOMAIN-KEYWORD,httpdns,DIRECT,pre-matching |
