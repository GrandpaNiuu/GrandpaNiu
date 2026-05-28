# 旧版 26.1.27 精选规则迁移报告

生成时间：2026-05-29 01:02:53 +0800

## 迁移原则

- 保留当前新框架，不整包覆盖。
- 只从旧版中迁移当前缺失的低风险去广告规则。
- 不迁移会员、支付、登录、验证码、证书、安全绕过、成人、博彩相关内容。
- 不迁移无法确认来源安全的脚本。
- 不删除现有 Spotify、YouTube、远程规则源、已有脚本。

## 新增统计

- [Rule] 新增：71 条
- [URL Rewrite] 新增：17 条
- [Body Rewrite] 新增：1 条
- [Map Local] 新增：0 条
- [Script] 新增：1 条

## 新增明细

### [Rule]

- `DOMAIN,ad.thsi.cn,REJECT,pre-matching`
- `DOMAIN,ad.video.51togic.com,REJECT,pre-matching`
- `DOMAIN,ad.xiangji.qq.com,REJECT,pre-matching`
- `DOMAIN,ad.ximalaya.com,REJECT,pre-matching`
- `DOMAIN,adapi.izuiyou.com,REJECT,pre-matching`
- `DOMAIN,adbs.ximalaya.com,REJECT,pre-matching`
- `DOMAIN,adcdn.tencentmusic.com,REJECT,pre-matching`
- `DOMAIN,adcdn6.tencentmusic.com,REJECT,pre-matching`
- `DOMAIN,adexpo.tencentmusic.com,REJECT,pre-matching`
- `DOMAIN,adproxy.autohome.com.cn,REJECT,pre-matching`
- `DOMAIN,ads.zhinengxiyifang.cn,REJECT,pre-matching`
- `DOMAIN,adsebs.ximalaya.com,REJECT,pre-matching`
- `DOMAIN,adsebs.wsa.ximalaya.com,REJECT,pre-matching`
- `DOMAIN,adweb.ximalaya.com,REJECT,pre-matching`
- `DOMAIN,adweb.wsa.ximalaya.com,REJECT,pre-matching`
- `DOMAIN,adwx.ximalaya.com,REJECT,pre-matching`
- `DOMAIN,adwx.wsa.ximalaya.com,REJECT,pre-matching`
- `DOMAIN,api-ad-product.huxiu.com,REJECT,pre-matching`
- `DOMAIN,cdn.adapi.fotoable.com,REJECT,pre-matching`
- `DOMAIN,cmad.video.51togic.com,REJECT,pre-matching`
- `DOMAIN,dyads.stg.ixigua.com,REJECT,pre-matching`
- `DOMAIN,iad.g.163.com,REJECT,pre-matching`
- `DOMAIN,market.m.taobao.com,REJECT,pre-matching`
- `DOMAIN,mobads.baidu.com,REJECT,pre-matching`
- `DOMAIN,ssp-adx.myzaker.com,REJECT,pre-matching`
- `DOMAIN,sspapi.youxiaoad.com,REJECT,pre-matching`
- `DOMAIN,video.market.xiaomi.com,REJECT,pre-matching`
- `DOMAIN,xadsdk.shellapp.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,ad.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adse.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adsebs.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adbehavior.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adweb.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adwx.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,ads.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adse.wsa.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adsebs.wsa.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adweb.wsa.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adwx.wsa.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adbehavior.wsa.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,ad.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adse.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adsebs.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adbehavior.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adweb.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adwx.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,ads.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adse.wsa.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adsebs.wsa.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adweb.wsa.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adwx.wsa.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adbehavior.wsa.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,admaster.com.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adsafeprotected.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adsrvr.org,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adview.cn,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adxs.ximalaya.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,adxs.xmcdn.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,api-ad-product.huxiu.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,googleadservices.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,iad.apple.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,scorecardresearch.com,REJECT,pre-matching`
- `DOMAIN-SUFFIX,voiceads.cn,REJECT,pre-matching`
- `DOMAIN-KEYWORD,admarvel,REJECT,pre-matching`
- `DOMAIN-KEYWORD,adsage,REJECT,pre-matching`
- `DOMAIN-KEYWORD,adsmogo,REJECT,pre-matching`
- `DOMAIN-KEYWORD,adsrvmedia,REJECT,pre-matching`
- `DOMAIN-KEYWORD,adtrack,REJECT,pre-matching`
- `DOMAIN-KEYWORD,adwo,REJECT,pre-matching`
- `DOMAIN-KEYWORD,madmini,REJECT,pre-matching`
- `DOMAIN-KEYWORD,mobads,REJECT,pre-matching`

### [URL Rewrite]

- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/api3\.do - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/gf\.m\.aplus - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/gwr - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/log - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/abtest - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/aplus - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/ad - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/aplusCrash - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/adlog - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/analytics - reject`
- `^https?:\/\/adashx\.ut\.taobao\.com\/rest\/utm - reject`
- `^https?:\/\/adx\.alibaba\.com\/.* - reject`
- `^https?:\/\/ad\.alicdn\.com\/.* - reject`
- `^https?:\/\/adash\.man\.taobao\.com\/.* - reject`
- `^https?:\/\/g\.alicdn\.com\/.*\/ad\/.* - reject`
- `^https?:\/\/gw\.alicdn\.com\/.*\/ad\/.* - reject`
- `^https?:\/\/img\.alicdn\.com\/.*\/ad\/.* - reject`

### [Body Rewrite]

- `http-response-jq ^https?:\/\/api\.zhihu\.com\/search\/recommend_query\/v2\? 'del(.recommend_queries)'`

### [Map Local]

- 无

### [Script]

- `legacy_safe_qqnews = type=http-response,pattern=^https?:\/\/(news\.ssp\.qq\.com\/app|r\.inews\.qq\.com\/(get(QQNewsUnreadList|TagFeedList)|news_feed\/hot_module_list)),script-path=https://raw.githubusercontent.com/app2smile/rules/master/js/`

## 跳过说明（节选）

### [Rule]

- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,api.ssp.xcsc.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,appgift.sinaapp.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,appgiftwall.oss-cn-beijing.aliyuncs.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,apppv.zol.com.cn,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,assets.giocdn.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,bdcdn*.seafood.qq.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,cdnfile1.msstatic.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,disp.titan.mgtv.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,ggs.myzaker.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,gorgon.youdao.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,hs.qhupdate.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,impservice.dictapp.youdao.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,log.51cto.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,logsdk.qq.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,nex.163.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,nexac.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,nexage.163.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,pglstatp-toutiao.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,pgdt.gtimg.cn,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,pic.rmb.bdstatic.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,pstatp.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,qchannel04.cn,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,rumt-zh.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,sdk.51.la,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,slardar.ixigua.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,sm.domobcdn.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,static-cn.plista.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,tnc3-alisc1.bytedance.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,tnc3-aliec2.snssdk.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,tracking.intl.miui.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,union-click.jd.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,vs19.gzcu.u3.ucweb.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,webcast5-normal-hl-lf.ixigua.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN,x.da.hunantv.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN-SUFFIX,analysis.pconline.com.cn,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN-SUFFIX,biddingx.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN-SUFFIX,cpro.baidu.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN-SUFFIX,crashlytics.com,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN-SUFFIX,doubleclick.net,REJECT,pre-matching
- 关键词不符合去广告安全筛选或包含高风险词：DOMAIN-SUFFIX,duapps.com,REJECT,pre-matching

### [URL Rewrite]

- 关键词不符合去广告安全筛选或包含高风险词：^https?:\/\/umengjmacs\.m\.taobao\.com\/.* - reject
- 关键词不符合去广告安全筛选或包含高风险词：^https?:\/\/g\.alicdn\.com\/.*\/TB1.*\.jpg - reject
- 关键词不符合去广告安全筛选或包含高风险词：^https?:\/\/gw\.alicdn\.com\/.*\/TB1.* - reject
- 关键词不符合去广告安全筛选或包含高风险词：^https?:\/\/img\.alicdn\.com\/.*\/TB1.* - reject

### [Body Rewrite]

- 无

### [Map Local]

- 无

### [Script]

- 无

## 关键项验证

- [Rule]：存在
- [Script]：存在
- [MITM]：存在
- spotify-json：存在
- spotify-proto：存在
- youtube.response：存在

## 后续测试

1. Shadowrocket 更新模块和脚本。
2. 测试 Spotify 是否播放稳定、是否跳歌。
3. 测试 YouTube 是否播放正常。
4. 测试常用国内 App 登录、支付、验证码是否正常。