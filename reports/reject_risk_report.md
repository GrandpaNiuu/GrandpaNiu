# REJECT 风险审计报告

生成时间：2026-06-14 04:25:14 +0800

本报告只做分类审计，不会自动删除、注释或替换任何规则。高风险项需要先确认 Shadowrocket 日志和真实 App 行为，再做 source-first 修复。

## 总览

- 活跃 REJECT 规则数：302
- 明确广告域：72
- 图片 / CDN 风险：9
- HTTPDNS 风险：14
- 微信 / 支付 / 银行风险：4
- 国内核心 API 风险：27
- 不确定规则：184
- 需要人工复核总数：238

## 重点风险域检查

| 域名 / 关键词 | direct.list 状态 | reject.list 命中 | 建议 |
|---|---|---:|---|
| `qpic.cn` | 已精确保护或覆盖 | 0 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `gtimg.cn` | 已精确保护或覆盖 | 0 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `qlogo.cn` | 已精确保护或覆盖 | 0 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `wxs.qq.com` | 已精确保护或覆盖 | 0 | 默认保护，不直接 REJECT |
| `wx.qq.com` | 已精确保护或覆盖 | 0 | 默认保护，不直接 REJECT |
| `weixin.qq.com` | 已精确保护或覆盖 | 0 | 默认保护，不直接 REJECT |
| `servicewechat.com` | 已精确保护或覆盖 | 0 | 默认保护，不直接 REJECT |
| `wxapp.tc.qq.com` | 已精确保护或覆盖 | 0 | 人工复核 |
| `wechatpay.cn` | 已精确保护或覆盖 | 0 | 默认保护，不直接 REJECT |
| `alicdn.com` | 已精确保护或覆盖 | 3 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `pddpic.com` | 已精确保护或覆盖 | 3 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `360buyimg.com` | 已精确保护或覆盖 | 0 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `jdimg.com` | 已精确保护或覆盖 | 0 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `biliimg.com` | 已精确保护或覆盖 | 0 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `hdslb.com` | 已精确保护或覆盖 | 0 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `meituan.net` | 已精确保护或覆盖 | 3 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `dpfile.com` | 已精确保护或覆盖 | 0 | 默认 DIRECT 或人工复核，不建议 REJECT |
| `httpdns` | 未发现 | 14 | 人工复核，不建议 pre-matching REJECT |
| `dns.weixin` | 已精确保护或覆盖 | 0 | 人工复核，不建议 pre-matching REJECT |

## 明确广告域：可保留 REJECT

- `DOMAIN,ad-analysis.pconline.com.cn,REJECT,pre-matching`
- `DOMAIN,ad-cdn.qingting.fm,REJECT,pre-matching`
- `DOMAIN,ad-stat.ksosoft.com,REJECT,pre-matching`
- `DOMAIN,adlaunch.qingting.fm,REJECT,pre-matching`
- `DOMAIN,admarket.21cn.com,REJECT,pre-matching`
- `DOMAIN,admarketing.yahoo.net,REJECT,pre-matching`
- `DOMAIN,admusicpic.music.126.net,REJECT,pre-matching`
- `DOMAIN,adui.tg.meitu.com,REJECT,pre-matching`
- `DOMAIN,adv-adlog.variflight.com,REJECT,pre-matching`
- `DOMAIN,adx-api.zdmimg.com,REJECT,pre-matching`
- `DOMAIN,adx-os.bridgeturbo.com,REJECT,pre-matching`
- `DOMAIN,adx.yiche.com,REJECT,pre-matching`
- `DOMAIN,adx.zuoyebang.com,REJECT,pre-matching`
- `DOMAIN,badjs.weixinbridge.com,REJECT,pre-matching`
- `DOMAIN,huyafile.msstatic.com,REJECT,pre-matching`
- `DOMAIN,iad0ssl.pcauto.com.cn,REJECT,pre-matching`
- `DOMAIN,iad0ssl.pconline.com.cn,REJECT,pre-matching`
- `DOMAIN,iadmat.nosdn.127.net,REJECT,pre-matching`
- `DOMAIN,iadmatapk.nosdn.127.net,REJECT,pre-matching`
- `DOMAIN,iadmusicmat.music.126.net,REJECT,pre-matching`
- `DOMAIN,iadmusicmatvideo.music.126.net,REJECT,pre-matching`
- `DOMAIN,imgad0.pcauto.com.cn,REJECT,pre-matching`
- `DOMAIN,imgad0.pconline.com.cn,REJECT,pre-matching`
- `DOMAIN,livewebbs2.msstatic.com,REJECT,pre-matching`
- `DOMAIN,livewebbs2pcdn.msstatic.com,REJECT,pre-matching`
- `DOMAIN,log.17gwx.com,REJECT,pre-matching`
- `DOMAIN,log.ycapp.yiche.com,REJECT,pre-matching`
- `DOMAIN,logs.chelaile.net.cn,REJECT,pre-matching`
- `DOMAIN,pp-cdnfile2pcdn.msstatic.com,REJECT,pre-matching`
- `DOMAIN,rprain.log.mgtv.com,REJECT,pre-matching`
- `DOMAIN,splash.yy.com,REJECT,pre-matching`
- `DOMAIN,stat.youpin.mi.com,REJECT,pre-matching`
- `DOMAIN,vstlog.17usoft.com,REJECT,pre-matching`
- `DOMAIN,wgo.mmstat.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adcanvas.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adeng.hpplay.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adjust.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adnet.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adx-api.hupu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adx.hupu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,apilog.qbb6.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,beacon.sina.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,gdt.qq.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,medal.blog.csdn.net,REJECT,pre-matching`
- `DOMAIN-SUFFIX,mistat.xiaomi.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,ms.vipstatic.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,mstat.zol.com.cn,REJECT,pre-matching`
- `URL-REGEX,^https?:\/\/mercury-gateway\.ixiaochuan\.cn\/mercury\/v1\/ad\/,REJECT-TINYGIF`
- `URL-REGEX,^https?:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/album\/adBar\/,REJECT-TINYGIF`
- `URL-REGEX,^https?:\/\/web-mmap-pay\.line-apps\.com\/tw\/liff\/campaign\/v1\/aggregate\/ad\/banner\/,REJECT-TINYGIF`
- `URL-REGEX,^https?:\/\/w\.line\.me\/adp\/api\/ad\/v\d\/,REJECT-DROP`
- `DOMAIN,adapi.izuiyou.com,REJECT,pre-matching`
- `DOMAIN,adcdn.tencentmusic.com,REJECT,pre-matching`
- `DOMAIN,adcdn6.tencentmusic.com,REJECT,pre-matching`
- `DOMAIN,adexpo.tencentmusic.com,REJECT,pre-matching`
- `DOMAIN,adproxy.autohome.com.cn,REJECT,pre-matching`
- `DOMAIN,api-ad-product.huxiu.com,REJECT,pre-matching`
- `DOMAIN,cdn.adapi.fotoable.com,REJECT,pre-matching`
- `DOMAIN,ssp-adx.myzaker.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adbehavior.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adweb.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adwx.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adweb.wsa.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adwx.wsa.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adbehavior.wsa.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,admaster.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adview.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adxs.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,api-ad-product.huxiu.com,REJECT,pre-matching`
- `DOMAIN-KEYWORD,admarvel,REJECT,pre-matching`
- `DOMAIN-KEYWORD,adwo,REJECT,pre-matching`
- `DOMAIN-KEYWORD,madmini,REJECT,pre-matching`

## 图片 / CDN：默认 DIRECT 或人工复核，不建议 REJECT

- `DOMAIN,cd-1.pddpic.com,REJECT,pre-matching`
- `DOMAIN,cdl-1.pddpic.com,REJECT,pre-matching`
- `DOMAIN,cdl-p2.pddpic.com,REJECT,pre-matching`
- `DOMAIN,hudong.alicdn.com,REJECT,pre-matching`
- `DOMAIN,layout.meituan.net,REJECT,pre-matching`
- `DOMAIN,nbsdk-baichuan.alicdn.com,REJECT,pre-matching`
- `DOMAIN,ossgw.alicdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,d.meituan.net,REJECT,pre-matching`
- `DOMAIN-SUFFIX,lx.meituan.net,REJECT,pre-matching`

## HTTPDNS：人工复核，不建议 pre-matching REJECT

- `DOMAIN,httpdns-sdk.n.netease.com,REJECT,pre-matching`
- `DOMAIN,httpdns.baidubce.com,REJECT,pre-matching`
- `DOMAIN,httpdns.calorietech.com,REJECT,pre-matching`
- `DOMAIN,httpdns.music.163.com,REJECT,pre-matching`
- `DOMAIN,httpdns.n.netease.com,REJECT,pre-matching`
- `DOMAIN,httpdns.yunxindns.com,REJECT,pre-matching`
- `DOMAIN,httpdnsmultiapi.meituan.com,REJECT,pre-matching`
- `DOMAIN,httpdnsmultiapivip.meituan.com,REJECT,pre-matching`
- `DOMAIN,lofter.httpdns.c.163.com,REJECT,pre-matching`
- `DOMAIN,music.httpdns.c.163.com,REJECT,pre-matching`
- `DOMAIN,yuyin-httpdns.gslb.yy.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,httpdns.bilivideo.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,httpdns.meituan.com,REJECT,pre-matching`
- `DOMAIN-KEYWORD,dnspod.meituan.httpdns,REJECT,pre-matching`

## 微信 / 支付 / 银行：默认保护，不直接 REJECT

- `DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching`
- `DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching`
- `DOMAIN,yl.zh.cmbchina.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adv.ccb.com,REJECT,pre-matching`

## 国内核心 API：不建议 REJECT

- `DOMAIN,afdconf.baidu.com,REJECT,pre-matching`
- `DOMAIN,amap-aos-info-nogw.amap.com,REJECT,pre-matching`
- `DOMAIN,api.biliapi.com,REJECT,pre-matching`
- `DOMAIN,api.biliapi.net,REJECT,pre-matching`
- `DOMAIN,app.biliapi.com,REJECT,pre-matching`
- `DOMAIN,app.biliapi.net,REJECT,pre-matching`
- `DOMAIN,dpmtpush.dianping.com,REJECT,pre-matching`
- `DOMAIN,free-aos-cdn-image.amap.com,REJECT,pre-matching`
- `DOMAIN,hlx.meituan.com,REJECT,pre-matching`
- `DOMAIN,httpdns.baidubce.com,REJECT,pre-matching`
- `DOMAIN,httpdnsmultiapi.meituan.com,REJECT,pre-matching`
- `DOMAIN,httpdnsmultiapivip.meituan.com,REJECT,pre-matching`
- `DOMAIN,layout.meituan.net,REJECT,pre-matching`
- `DOMAIN,lc.map.baidu.com,REJECT,pre-matching`
- `DOMAIN,lx0.meituan.com,REJECT,pre-matching`
- `DOMAIN,r.dianping.com,REJECT,pre-matching`
- `DOMAIN,tte.meituan.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,d.meituan.net,REJECT,pre-matching`
- `DOMAIN-SUFFIX,httpdns.meituan.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,lx.meituan.net,REJECT,pre-matching`
- `DOMAIN-SUFFIX,meituan.xn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,meituan.yoga,REJECT,pre-matching`
- `DOMAIN-SUFFIX,meituangov.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,wmlog.meituan.com,REJECT,pre-matching`
- `DOMAIN-KEYWORD,dnspod.meituan.httpdns,REJECT,pre-matching`
- `DOMAIN-KEYWORD,report.meituan,REJECT,pre-matching`
- `AND,((PROTOCOL,QUIC),(DOMAIN,api.pinduoduo.com)),REJECT-NO-DROP`

## 不确定规则：pending / manual-review

- `DOMAIN,apm-native.xiaohongshu.com,REJECT,pre-matching`
- `DOMAIN,apm.gotokeep.com,REJECT,pre-matching`
- `DOMAIN,apmplus.volces.com,REJECT,pre-matching`
- `DOMAIN,appcloud.zhihu.com,REJECT,pre-matching`
- `DOMAIN,appcloud2.in.zhihu.com,REJECT,pre-matching`
- `DOMAIN,appgo.189.cn,REJECT,pre-matching`
- `DOMAIN,apps-booster.xiaopeng.com,REJECT,pre-matching`
- `DOMAIN,appupdates.189.cn,REJECT,pre-matching`
- `DOMAIN,atrace.chelaile.net.cn,REJECT,pre-matching`
- `DOMAIN,axxd.xmseeyouyima.com,REJECT,pre-matching`
- `DOMAIN,collect.xiaopeng.com,REJECT,pre-matching`
- `DOMAIN,counter.kingsoft.com,REJECT,pre-matching`
- `DOMAIN,counter.ksosoft.com,REJECT,pre-matching`
- `DOMAIN,crash2.zhihu.com,REJECT,pre-matching`
- `DOMAIN,credits.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,credits2.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,credits3.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,csc-apm.sgcc.com.cn,REJECT,pre-matching`
- `DOMAIN,cube.weixinbridge.com,REJECT,pre-matching`
- `DOMAIN,da.bridgeturbo.com,REJECT,pre-matching`
- `DOMAIN,ddfs-public.ddimg.mobi,REJECT,pre-matching`
- `DOMAIN,dflow.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,dynamicf.sankuai.com,REJECT,pre-matching`
- `DOMAIN,encounter.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,et.ykccn.com,REJECT,pre-matching`
- `DOMAIN,etl.xlmc.sandai.net,REJECT,pre-matching`
- `DOMAIN,floor.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,gather.colorfulclouds.net,REJECT,pre-matching`
- `DOMAIN,gwp.xiaojukeji.com,REJECT,pre-matching`
- `DOMAIN,hc-ssp.sm.cn,REJECT,pre-matching`
- `DOMAIN,ipv4.music.163.com,REJECT,pre-matching`
- `DOMAIN,ipv6.music.163.com,REJECT,pre-matching`
- `DOMAIN,ivy.pchouse.com.cn,REJECT,pre-matching`
- `DOMAIN,layer.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,live-monitor-broker.sankuai.com,REJECT,pre-matching`
- `DOMAIN,mall-dsp2.qinlinkeji.com,REJECT,pre-matching`
- `DOMAIN,mallapi2.qinlinkeji.com,REJECT,pre-matching`
- `DOMAIN,mdap.mpaas.cn-hangzhou.aliyuncs.com,REJECT,pre-matching`
- `DOMAIN,meta.pinduoduo.com,REJECT,pre-matching`
- `DOMAIN,minfo.wps.cn,REJECT,pre-matching`
- `DOMAIN,mob.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,mqtt.zhihu.com,REJECT,pre-matching`
- `DOMAIN,msmp.abchina.com.cn,REJECT,pre-matching`
- `DOMAIN,popup.dushu365.com,REJECT,pre-matching`
- `DOMAIN,rc-topic-api.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,richmanapi.jxedt.com,REJECT,pre-matching`
- `DOMAIN,richmanmain.jxedt.com,REJECT,pre-matching`
- `DOMAIN,richmanrules.jxedt.com,REJECT,pre-matching`
- `DOMAIN,rprain.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,sax.sina.com.cn,REJECT,pre-matching`
- `DOMAIN,saxn.sina.com.cn,REJECT,pre-matching`
- `DOMAIN,saxs.sina.com.cn,REJECT,pre-matching`
- `DOMAIN,sensors.umetrip.com.cn,REJECT,pre-matching`
- `DOMAIN,smartop-sdkapi-ipv6.jiguang.cn,REJECT,pre-matching`
- `DOMAIN,smartop-sdkapi.jiguang.cn,REJECT,pre-matching`
- `DOMAIN,stun1.douyucdn.cn,REJECT,pre-matching`
- `DOMAIN,stun1.qvb.qcloud.com,REJECT,pre-matching`
- `DOMAIN,sugar.zhihu.com,REJECT,pre-matching`
- `DOMAIN,ta-a.pinduoduo.com,REJECT,pre-matching`
- `DOMAIN,ta.pinduoduo.com,REJECT,pre-matching`
- `DOMAIN,th-a.pinduoduo.com,REJECT,pre-matching`
- `DOMAIN,th-b.pinduoduo.com,REJECT,pre-matching`
- `DOMAIN,th.pinduoduo.com,REJECT,pre-matching`
- `DOMAIN,titan.babytree.com,REJECT,pre-matching`
- `DOMAIN,titan.pinduoduo.com,REJECT,pre-matching`
- `DOMAIN,titan01.babytree.com,REJECT,pre-matching`
- `DOMAIN,u1.img.mobile.sina.cn,REJECT,pre-matching`
- `DOMAIN,ucdc.upaas.quark.cn,REJECT,pre-matching`
- `DOMAIN,union.chinalifeonline.com.cn,REJECT,pre-matching`
- `DOMAIN,ups.ksmobile.net,REJECT,pre-matching`
- `DOMAIN,vali-g1.cp31.ott.cibntv.net,REJECT,pre-matching`
- `DOMAIN,vali-ugc.cp31.ott.cibntv.net,REJECT,pre-matching`
- `DOMAIN,vip.bz.mgtv.com,REJECT,pre-matching`
- `DOMAIN,ws.ksmobile.net,REJECT,pre-matching`
- `DOMAIN,xg.pinduoduo.com,REJECT,pre-matching`
- `DOMAIN,ymg-api.terabox.com,REJECT,pre-matching`
- `DOMAIN,zxid-m.mobileservice.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,3rd.t.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,888.tv.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,afp.zol-img.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,api.dsp.yhd.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,api.union.vip.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,app-measurement.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,appier.net,REJECT,pre-matching`
- `DOMAIN-SUFFIX,applovin.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,applvn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,apppv.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,aty.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,corp.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,counter.csdn.net,REJECT,pre-matching`
- `DOMAIN-SUFFIX,cpc.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,cpro.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,da.mgtv.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,dc.csdn.net,REJECT,pre-matching`
- `DOMAIN-SUFFIX,dc2.csdn.net,REJECT,pre-matching`
- `DOMAIN-SUFFIX,dynamic.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,ehaier.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,gemini.yahoo.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,go.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,hui.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,imp.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,js.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,n-st.vip.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pangle.io,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pic.zol-img.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pv.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pvc.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pvm.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pvmsite.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pvnapp.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pvsite.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,pvtest.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,suvset.sohu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,tappx.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,v.smtcdns.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,v1d.szbdyd.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,wappv.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,ydjs.zol.com.cn,REJECT,pre-matching`
- `DOMAIN-KEYWORD,apimg.qunliao.info,REJECT,pre-matching`
- `DOMAIN-KEYWORD,c-hzgt2.getui.com,REJECT,pre-matching`
- 其余 64 条已省略

## 处理边界

- 不批量删除规则。
- 不新增 `DOMAIN-SUFFIX,qq.com,DIRECT` 这类过宽保护。
- 微信、支付、银行、图片 CDN 只能做精确保护。
- 如果需要修复，优先修改 `Rules/direct.list` 的精确 `DIRECT,pre-matching` 或单条注释高风险 REJECT，并重新构建。
- 没有真实日志和手测记录时，保持 manual-review。
