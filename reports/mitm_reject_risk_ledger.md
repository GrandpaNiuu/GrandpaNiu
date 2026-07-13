# MITM / REJECT 风险台账

- 生成时间：2026-07-14 02:20:00 +0800
- 扫描 MITM hostname：806
- 标记 MITM 风险项：172
- 扫描 REJECT / rewrite reject 条目：4219
- 标记 REJECT 风险项：2817
- 高风险项：73
- 中风险项：2916

## 使用边界

- 本台账只标来源和风险，不删除、不注释、不替换任何规则。
- 登录、支付、银行、验证码、视频播放、图片/CDN、核心 API 只能在有真实异常或日志证据时单点复核。
- `high` 代表不应随意扩大 MITM / REJECT 范围；`medium` 代表需要人工复核来源和 App 行为。

## MITM 风险项

| 类型 | 风险 | 分类 | 来源 | 条目 | 标记原因 |
|---|---|---|---|---|---|
| MITM | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/appso.conf:12` | `sso.ifanr.com` | 命中敏感链路关键词 |
| MITM | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/mobile-clouds.conf:14` | `jzts.cmpassport.com` | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Apps/kuai-kan-comic.conf:43` | `pay.kkmh.com` | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `ccmsupport-sz.tenpay.com` | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `creditcardapp.bankcomm.com` | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `mbmodule-openapi.paas.cmbchina.com` | 命中敏感链路关键词 |
| MITM | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:43` | `cdn-pay.kkmh.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:22` | `aiqicha.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:20` | `imeres.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:20` | `mbd.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:20` | `mime.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:25` | `afd.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:25` | `ecom.map.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:25` | `newclient.map.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:25` | `yongche.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-net-disk.conf:21` | `pan.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-photo.conf:16` | `mbd.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-photo.conf:16` | `pan.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-translation.conf:13` | `mime.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-wenku.conf:34` | `appwk.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-wenku.conf:34` | `tanbi.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu.conf:12` | `m.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu.conf:12` | `www.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidupan.conf:27` | `pan.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/damai.conf:18` | `acs.m.taobao.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/i-mai-cai.conf:21` | `mall.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/i-mai-cai.conf:21` | `portal-portm.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/jd.conf:23` | `api.m.jd.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/jdwaimai.conf:19` | `api.m.jd.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:30` | `apimobile.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:30` | `cdb.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:30` | `mall.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:30` | `rms.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:30` | `web.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:30` | `wmapi.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/pinduoduo.conf:85` | `api.pinduoduo.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/robo-taxi.conf:14` | `idgdata.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/taobao-travel.conf:16` | `acs.m.taobao.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/taobao.conf:44` | `acs.m.taobao.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/taobao.conf:44` | `guide-acs.m.taobao.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/taopiaopiao.conf:19` | `acs.m.taobao.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/tieba.conf:18` | `tiebac.baidu.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `api.pinduoduo.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `rms.meituan.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/wechat-official-accounts.conf:16` | `mp.weixin.qq.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/wechat.conf:17` | `mp.weixin.qq.com` | 命中敏感链路关键词 |
| MITM | medium | 国内 App 核心 API / 通配 MITM | `Rewrite/Sources/Apps/amap.conf:81` | `*.amap.com` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 国内 App 核心 API / 通配 MITM | `Rewrite/Sources/Apps/meituan.conf:30` | `*.dianping.com` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/baby-tree-parenting.conf:16` | `aimg.babytreeimg.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/caiyun-weather.conf:22` | `cdn-w.caiyunapp.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/che-lai-le.conf:23` | `pic1.chelaile.net.cn` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/clicli.conf:12` | `js-ad.ayximgs.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/di-duan-ying-shi.conf:15` | `img.ddrk.me` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/dian-shi-jia.conf:13` | `cdn.dianshihome.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/dlabel-cloud-tag.conf:13` | `imagepc.ctaiot.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/douyu.conf:27` | `apiv2.douyucdn.cn` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/douyu.conf:27` | `rtbapi.douyucdn.cn` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/douyu.conf:27` | `venus.douyucdn.cn` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/jie-mian-news.conf:12` | `img.jiemian.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kingsoft-power-word.conf:26` | `mobile-pic.cache.iciba.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:43` | `cdn-api.kkmh.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:43` | `cdn-h5.kuaikanmanhua.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:43` | `cdn-shop.kkmh.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:43` | `cdn-social.kkmh.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:43` | `cdn-topic.kkmh.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:43` | `topic.kkmh.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/lenovo-print.conf:12` | `abcapi.lenovoimage.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:51` | `ad.line-scdn.net` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:51` | `d.line-scdn.net` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:51` | `ec-bot-obs.line-scdn.net` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:51` | `obs.line-scdn.net` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:51` | `scdn.line-apps.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:51` | `static.line-scdn.net` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/lofter.conf:14` | `images.pinduoduo.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ma-ka-long-wan-tu.conf:13` | `static01.versa-ai.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ma-ma-wang-yun-yu.conf:12` | `qimg.cdnmama.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mai-dui-dui.conf:19` | `conf-darwin.xycdn.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mai-dui-dui.conf:19` | `mobads-pre-config.cdn.bcebos.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mkz.conf:18` | `base.mkzcdn.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/picc-insurance.conf:19` | `zgrb.epicc.com.cn` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qi-shui-music.conf:16` | `lf-cdn-tos.bytescm.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qi-xin-bao.conf:21` | `qxb-minicode-pic-osscache.qixin.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/quan-min-ge-ge.conf:12` | `y.gtimg.cn` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/seasun-jx3.conf:15` | `jx3comm.xoyocdn.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/seven-cat.conf:32` | `cdn.wtzw.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/sf-express.conf:19` | `ucmp-static.sf-express.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/sogou-input.conf:16` | `business-cdn.shouji.sogou.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/taobao.conf:44` | `heic.alicdn.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/tencent-games-community.conf:12` | `static.gameplus.qq.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/tencent-sports.conf:13` | `sports3.gtimg.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ttvoice.conf:12` | `ga-album-cdnqn.52tt.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `appuser-static.huolala.cn` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `fscdn.zto.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `images.qmai.cn` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/xfuse.conf:12` | `img.mofyi.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/xiaojukeji-charge.conf:20` | `am.didistatic.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/zdm.conf:57` | `haojia-cdn.smzdm.com` | 命中敏感链路关键词 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | `Rewrite/Sources/Apps/58-tong-cheng.conf:34` | `*.58cdn.com.cn` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | `Rewrite/Sources/Apps/che-lai-le.conf:23` | `cdn.*.chelaileapp.cn` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | `Rewrite/Sources/Apps/huya.conf:14` | `*.msstatic.com` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 图片 / 静态 CDN / 通配 MITM | `Rewrite/Sources/Apps/qqksong.conf:52` | `amsweb-cdn-*-1258344696.file.myqcloud.com` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/bilibili.conf:87` | `grpc.biliapi.net` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/i-qi-yi-video.conf:44` | `-i.vip.iqiyi.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:64` | `damang.api.mgtv.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:64` | `dc?.bz.mgtv.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:64` | `hb-boom.api.mgtv.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:64` | `me.bz.mgtv.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:64` | `mobile-thor.api.mgtv.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:64` | `mobile.api.mgtv.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:64` | `mobileso.bz.mgtv.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/netease-music.conf:53` | `interface.music.163.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/netease-music.conf:53` | `interface3.music.163.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/netease-music.conf:53` | `interface9.music.163.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/netease-music.conf:53` | `ipv4.music.163.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/netease-news.conf:29` | `interface.music.163.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/netease-news.conf:29` | `interface3?.music.163.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/spotify.conf:17` | `spclient.wg.spotify.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/tencent-video.conf:33` | `vv.video.qq.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:40` | `push.m.youku.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:40` | `un-acs.youku.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youtube.conf:26` | `youtubei.googleapis.com` | 命中敏感链路关键词 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | `Rewrite/Sources/Apps/i-qi-yi-video.conf:44` | `*.iqiyi.com` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | `Rewrite/Sources/Apps/spotify.conf:17` | `*spclient.spotify.com` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 视频 / 音乐播放链路 / 通配 MITM | `Rewrite/Sources/Apps/youtube.conf:26` | `*.googlevideo.com` | 命中敏感链路关键词；包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/caixin-media.conf:28` | `e*.caixin.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/caixin-media.conf:28` | `g*.caixin.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/caixin-media.conf:28` | `m*.caixin.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/di-di.conf:36` | `113.46.225.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/di-di.conf:36` | `116.85.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/di-di.conf:36` | `120.241.142.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/di-di.conf:36` | `120.241.143.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/di-di.conf:36` | `123.207.209.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/di-di.conf:36` | `162.14.157.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/didi.conf:48` | `113.46.225.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/didi.conf:48` | `116.85.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/didi.conf:48` | `120.241.142.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/didi.conf:48` | `120.241.143.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/didi.conf:48` | `123.207.209.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/didi.conf:48` | `162.14.157.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/dingdong-maicai.conf:37` | `119.29.29.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `*.pangolin-sdk-toutiao.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `*.pangolin-sdk-toutiao.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `*.pglstatp-toutiao.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `*.pglstatp-toutiao.com.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `*.pstatp.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `*.pstatp.com.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `*default.ixigua.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `gurd.snssdk.com.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/fan-qie-novel.conf:39` | `i-lq.snssdk.com.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/huya.conf:14` | `*.huya.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/kebida-dushu.conf:31` | `g*.dushu365.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/kingsoft-power-word.conf:26` | `*.kingsoft-office-service.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/kuai-shou.conf:23` | `az*-api-idc.ksapisrv.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/kuai-shou.conf:23` | `az*-api-js.gifshow.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/kuai-shou.conf:23` | `az*-api.ksapisrv.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/kuai-shou.conf:23` | `az*-live.ksapisrv.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/kuwo.conf:33` | `vip*.kuwo.cn` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/mai-dui-dui.conf:19` | `*.ubixioe.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/man-hua-ren.conf:14` | `*mangaapi.manhuaren.*` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/pcauto.conf:14` | `*.pcauto.com.cn` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/pcauto.conf:14` | `*.pconline.com.cn` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/qi-shui-music.conf:16` | `sf*-fe-tos.pglstatp-toutiao.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/soda-music.conf:33` | `tnc*-*.zijieapi.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/soul.conf:36` | `api*.soulapp.cn` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/tube-max.conf:23` | `*.i18n-pglstatp.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/wechat-mini-programs.conf:167` | `capis*.didapinche.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/weibo.conf:90` | `*.weibo.cn` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/weibo.conf:90` | `*.weibo.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/weimai.conf:13` | `confssl*.iweimai.cn` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/xiaopeng.conf:10` | `*.xiaopeng.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/yiche.conf:10` | `*.yiche.com` | 包含通配 MITM 范围 |
| MITM | medium | 通配 MITM | `Rewrite/Sources/Apps/zhihu.conf:99` | `*.zhihu.com` | 包含通配 MITM 范围 |

## REJECT 风险项

| 类型 | 风险 | 分类 | 来源 | 条目 | 标记原因 |
|---|---|---|---|---|---|
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/51-job.conf:12` | `^https://cupid\.51jobapp\.com/open/noauth/jobs/detail/sesame-competitive/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/51-job.conf:13` | `^https://cupid\.51jobapp\.com/open/noauth/jobs/job-detail/user-rights\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/51-job.conf:15` | `^https://cupid\.51jobapp\.com/launch-hub/open/noauth/popUp/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/51-job.conf:16` | `^https://cupid\.51jobapp\.com/launch-hub/open/noauth/popUp/getHomePagePopUp\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/appso.conf:9` | `^https?://sso\.ifanr\.com/jiong/IOS/appso/splash/ - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/blued.conf:10` | `^https?://social\.blued\.cn/users/no_auth/benefit - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/dao-meng-kong-jian.conf:10` | `^https?://appdmkj\.5idream\.net/v2/login/message/tip - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/etouch-ecalendar.conf:12` | `^https://client-lz\.rili\.cn/lizhi/api/auth/voice_room_entrance/list\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/huo-mao.conf:9` | `^https?://api\.huomao\.com/channels/loginAd - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/pu-pu-mall.conf:9` | `^https://j1\.pupuapi\.com/client/account/discount/order - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:101` | `^https://gw-passenger-wap\.01zhuanche\.com/gw-passenger-wap/zhuanche-passenger-token/commonSkipToken/common/getAdList - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:104` | `^https://passenger\.t3go\.cn/passenger-activity-api/notoken/api/v1/resource/getSource - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:126` | `^https://api\.szbgcx\.cn/account/adv/ - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/xia-chu-fang.conf:10` | `^https://api\.xiachufang\.com/v2/account/feeds_v7\.json - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/Apps/xiao-hei-he.conf:9` | `^https://api\.xiaoheihe\.cn/account/get_ads_info_v2 - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:55` | `^https:\/\/api\.szbgcx\.cn\/account\/adv\/ - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:1332` | `^https?:\/\/social\.blued\.cn\/users\/no_auth\/benefit - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:1342` | `^https?:\/\/sso\.ifanr\.com\/jiong\/IOS\/appso\/splash\/ - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:1489` | `^https?:\/\/www\.onstar\.com\.cn\/mssos\/sos\/social\/v1\/community\/article\/page - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:346` | `^https?:\/\/api\.m\.jd\.com\/\?loginType=11 - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:415` | `^https?:\/\/api\.ulife\.group\/auth\/account\/entrance - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:416` | `^https?:\/\/api\.ulife\.group\/auth\/account\/getUpgradeStrategy - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:429` | `^https?:\/\/api\.xiachufang\.com\/v2\/account\/feeds_v7\.json - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:434` | `^https?:\/\/api\.xiaoheihe\.cn\/account\/get_ads_info - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:502` | `^https?:\/\/app\.ceair\.com\/customize\/security\/update - reject-200` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:558` | `^https?:\/\/appdmkj\.5idream\.net\/v2\/login\/message\/tip - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:654` | `^https?:\/\/client-api-v\d\.oray\.com\/materials\/(?:SLCC_IOS_STARTUP\|SLCC_IOS_DEVICE\|SUNLOGIN_CLIENT_IOS_PROMOTION) - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:656` | `^https?:\/\/client-lz\.rili\.cn\/lizhi\/api\/auth\/voice_room_entrance\/list\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:687` | `^https?:\/\/cupid\.51jobapp\.com\/launch-hub\/open\/noauth\/popUp\/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:688` | `^https?:\/\/cupid\.51jobapp\.com\/launch-hub\/open\/noauth\/popUp\/getHomePagePopUp\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:690` | `^https?:\/\/cupid\.51jobapp\.com\/open\/noauth\/jobs\/detail\/sesame-competitive\/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:691` | `^https?:\/\/cupid\.51jobapp\.com\/open\/noauth\/jobs\/job-detail\/user-rights\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:815` | `^https?:\/\/gateway\.cotticoffee\.com\/cotti-capi\/person\/homeLoginPrompt - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:844` | `^https?:\/\/gw-passenger\.01zhuanche\.com\/gw-passenger\/zhuanche-passenger-token\/leachtoken\/webservice\/homepage\/queryADs - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:933` | `^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(side-bar\/mini-program\/music-service\/account\|delivery\/(?:batch-deliver\|deliver)\|moment\/tab\/info\/get\|yunbei\/account\/entrance\/get) - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 | `Rewrite/Sources/URL-Rewrite.conf:934` | `^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(vipcenter\/tspopup\/get\|vipauth\/app\/auth\|music-vip-membership\/client\/vip\/info\|zone\/songplay\/entry\/get) - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:15` | `^https://aiqicha\.baidu\.com/m/getLoginWordsAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:220` | `^https?:\/\/aiqicha\.baidu\.com\/m\/getLoginWordsAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:354` | `^https?:\/\/api\.map\.baidu\.com\/\?qt=verify - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/seasun-jx3.conf:12` | `^https://jx3comm\.xoyocdn\.com/jx3gc/zhcn/login_ad/WebCareer/WebCareerTab\.txt - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1014` | `^https?:\/\/m\.client\.10010\.com\/mobileService\/(activity\|customer)\/(accountListData\|get_client_adv\|get_startadv) - reject-img` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1462` | `^https?:\/\/www\.dpfile\.com\/picasso\/picasso-qa\/src\/AnswerList\/AnswerList-bundle - reject` | 命中敏感链路关键词 |
| REJECT | high | 登录 / 账号 / 鉴权 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:958` | `^https?:\/\/jx3comm\.xoyocdn\.com\/jx3gc\/zhcn\/login_ad\/WebCareer\/WebCareerTab\.txt - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:23` | `^https://creditcardapp\.bankcomm\.com/cnsvPmpaMdbcardWeb/page/getGuidePageAds - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:24` | `^https://mbmodule-openapi\.paas\.cmbchina\.com/graphic/v2/module/graphic - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:82` | `^https://ccmsupport-sz\.tenpay\.com/cgi-bin/common/ccm_page_element.cgi - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Rule.conf:101` | `DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/Rule.conf:102` | `DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:10` | `^https:\/\/creditcardapp\.bankcomm\.com\/cnsvPmpaMdbcardWeb\/page\/getGuidePageAds - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:13` | `^https:\/\/mbmodule-openapi\.paas\.cmbchina\.com\/graphic\/v2\/module\/graphic - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:52` | `^https:\/\/ccmsupport-sz\.tenpay\.com\/cgi-bin\/common\/ccm_page_element.cgi - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/URL-Rewrite.conf:1023` | `^https?:\/\/m\.qianbao\.qq\.com\/pages\/walletHome\?invisible - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/URL-Rewrite.conf:1024` | `^https?:\/\/m\.qianbao\.qq\.com\/services\/walletHome\/get(QQshop\|Game\|Foot)Data - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rewrite/Sources/URL-Rewrite.conf:320` | `^https?:\/\/api\.hellobike\.com\/api\?homepage\.newWelfare\.alipay - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rules/qingrex-miniapp-app-ad.list:30` | `DOMAIN-KEYWORD,adv.ccb.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rules/reject.list:73` | `DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rules/reject.list:74` | `DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rules/reject.list:98` | `DOMAIN,msmp.abchina.com.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rules/web-ads.list:16` | `DOMAIN,ads.ysepay.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rules/web-ads.list:37` | `DOMAIN,mbads.paas.cmbchina.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 | `Rules/web-ads.list:64` | `DOMAIN-SUFFIX,track.bankcomm.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1159` | `^https?:\/\/npay\.meituan\.com\/conch\/flow\/mypage-wallet-info - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1160` | `^https?:\/\/npay\.meituan\.com\/conch\/walletv\d\/wechat-pop-window - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:27` | `^https://(cdn-)?pay\.kkmh\.com/v\d/kb/wallet - reject-dict` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:111` | `^http:\/\/image1\.ccb\.com\/newsinfo\/eBranch\/check\/(?:nf\/newfin\/activity\|po\/poortheme\/activity)\/\w+\.png - reject` | 命中敏感链路关键词 |
| REJECT | high | 银行 / 支付 / 钱包 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:40` | `^https?:\/\/(cdn-)?pay\.kkmh\.com\/v\d\/kb\/(?:wallet\|comic_page_banner) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | HTTPDNS / DNS | `Rewrite/Sources/URL-Rewrite.conf:118` | `^https?:\/\/101\.42\.130\.147\/httpdns\/resolve\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | HTTPDNS / DNS | `Rewrite/Sources/URL-Rewrite.conf:121` | `^https?:\/\/106\.55\.220\.18:8053\/httpdns\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | HTTPDNS / DNS | `Rewrite/Sources/URL-Rewrite.conf:123` | `^https?:\/\/139\.196\.12\.179:8053\/httpdns\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | HTTPDNS / DNS | `Rewrite/Sources/URL-Rewrite.conf:146` | `^https?:\/\/54\.222\.159\.138:8053\/httpdns\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | HTTPDNS / DNS | `Rules/qingrex-miniapp-app-ad.list:25` | `DOMAIN,hdns.ksyun.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | HTTPDNS / DNS | `Rules/qingrex-miniapp-app-ad.list:26` | `DOMAIN-KEYWORD,httpdns.,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | HTTPDNS / DNS | `Rules/qingrex-miniapp-app-ad.list:27` | `DOMAIN-KEYWORD,httpdns-,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:10` | `^https://aiqicha\.baidu\.com/app/getPopConfigAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:12` | `^https://aiqicha\.baidu\.com/app/getNewsReportAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:14` | `^https://aiqicha\.baidu\.com/apps/getHotRecommendV2Ajax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:16` | `^https://aiqicha\.baidu\.com/app/getAppPopSettingAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:17` | `^https://aiqicha\.baidu\.com/app/commonstatusAjax - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:18` | `^https://aiqicha\.baidu\.com/apps/getHomeMonitorDataAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:19` | `^https://aiqicha\.baidu\.com/apps/searchRecommendAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/amap.conf:9` | `DOMAIN,amap-aos-info-nogw.amap.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:10` | `^https?://mime\.baidu\.com/sapi/v1/lccorpus/(applist\|pannellist) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:11` | `^https?://mime\.baidu\.com/sapi/v1/(circle/joinedlist\|lccorpus/usercorpussync\|aihelpactivity/aihelpresource) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:12` | `^https?://mime\.baidu\.com/commer/pocket_api/enterprise_list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:13` | `^https?://mbd\.baidu\.com/ccs/v1/start/confsync\?appname=baidu_input - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:14` | `^https://mime\.baidu\.com/v5/(fb/st\?logtype\|(notiv3\|cellloc_noti\|noti_cloudswitch_noti)/info) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-input-method.conf:9` | `^https?://mime\.baidu\.com/v5/start_screen_ads/list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:10` | `^https://yongche\.baidu\.com/gomarketing/api/popup/getentrancecordovaurl$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:11` | `^https://yongche\.baidu\.com/goorder/passenger/cobuild/pull\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:12` | `^https://yongche\.baidu\.com/goorder/passenger/operationgirdle$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:13` | `^https://yongche\.baidu\.com/goorder/passenger/baseinfo$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:14` | `^https://ecom\.map\.baidu\.com/ad-ops/afd/popup\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:15` | `^https://maphotel\.baidu\.com/hotel/goextranet/activity/detail\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-map.conf:9` | `^https://afd\.baidu\.com/afd/entry\?action=(update\|query) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-net-disk.conf:10` | `^https://pan\.baidu\.com/api/getsyscfg\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-net-disk.conf:11` | `^https://pan\.baidu\.com/api/taskscore/tasklist\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-net-disk.conf:12` | `^https://pan\.baidu\.com/act/api/activityentry\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-net-disk.conf:13` | `^https://pan\.baidu\.com/rest/\d\.\d/pcs/adv\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-net-disk.conf:14` | `^https://pan\.baidu\.com/api/plugin/get\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-net-disk.conf:15` | `^https://pan\.baidu\.com/recommend/query/list\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-net-disk.conf:9` | `^https://pan\.baidu\.com/api/getconfig\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-photo.conf:10` | `^https://pan\.baidu\.com/youai/material/v1/getbynavid\?.*nav_id=1 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-photo.conf:9` | `^https://pan\.baidu\.com/act/api/conf\?.*conf_key=youa_core_config_ios - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-translation.conf:10` | `^https?://mime\.baidu\.com/v\d/activity/advertisement - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/baidu-translation.conf:9` | `^https?://mime\.baidu\.com/v\d/IosStart/getStartInfo - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/i-mai-cai.conf:10` | `^https://mall\.meituan\.com/api/c/homepage/bubble/operate/info - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/i-mai-cai.conf:11` | `^https://mall\.meituan\.com/api/c/jigsaw/code/category-banner-\d+/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/i-mai-cai.conf:12` | `^https://mall\.meituan\.com/api/c/poi/\d+/order/recommend/v\d - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/i-mai-cai.conf:13` | `^https://mall\.meituan\.com/api/c/banner/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/i-mai-cai.conf:14` | `^https://mall\.meituan\.com/api/c/poi/\d+/personal/recommend - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/i-mai-cai.conf:9` | `^https://mall\.meituan\.com/api/c/homepage/splash - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/jump.conf:11` | `DOMAIN,s3plus.meituan.net,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:10` | `DOMAIN,lx0.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:11` | `DOMAIN,r.dianping.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:12` | `DOMAIN,tte.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:13` | `DOMAIN-SUFFIX,wmlog.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:15` | `DOMAIN-SUFFIX,mads.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:16` | `DOMAIN-KEYWORD,report.meituan,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:19` | `^https?:\/\/apimobile\.meituan\.com\/appupdate - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:20` | `^https?:\/\/apimobile\.meituan\.com\/group\/v\d\/recommend\/unity\/recommends - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:21` | `^https?:\/\/cdb\.meituan\.com\/marketing\/source\/getPageSlotList - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:22` | `^https?:\/\/mall\.meituan\.com\/api\/c\/homepage\/splash - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:23` | `^https?:\/\/mapi\.dianping\.com\/adshopping - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:24` | `^https?:\/\/mapi\.dianping\.com\/mapi\/operating\/(?:indexopsmodules\|loadsplashconfig) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:25` | `^https?:\/\/rms\.meituan\.com\/api\/v\d\/rmsmina\/c\/queryWechatAdvertisement - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:26` | `^https?:\/\/web\.meituan\.com\/newUser\/returnMoney\/popWindow - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:6` | `DOMAIN,dpmtpush.dianping.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:8` | `DOMAIN,layout.meituan.net,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/pinduoduo.conf:11` | `AND,((DOMAIN,api.pinduoduo.com,extended-matching),(PROTOCOL,QUIC)),REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/robo-taxi.conf:11` | `^https://idgdata\.baidu\.com/idgactivity/api/newuser/info\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Apps/robo-taxi.conf:9` | `^https://idgdata\.baidu\.com/mc/app/api/listterminal\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Misc/android-compatible-ads.conf:36` | `DOMAIN,report.meituan,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Misc/android-compatible-ads.conf:44` | `DOMAIN,umengacs.m.taobao.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Misc/android-compatible-ads.conf:48` | `DOMAIN,wmlog.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Rule.conf:109` | `DOMAIN,layout.meituan.net,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Rule.conf:110` | `DOMAIN,lc.map.baidu.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Rule.conf:43` | `DOMAIN,afdconf.baidu.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Rule.conf:44` | `DOMAIN,amap-aos-info-nogw.amap.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Rule.conf:73` | `DOMAIN,dpmtpush.dianping.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/Rule.conf:83` | `DOMAIN,hlx.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1002` | `^https?:\/\/m5-zb\.amap\.com\/ws\/boss\/(?:order\/car\/(?:feedback\/get_card_questions\|feedback\/viptips\|king_toolbox_car_bubble\|remark\/satisfactionConf\|rights_information)\|tips\/onscene_visual_optimization) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1003` | `^https?:\/\/m5-zb\.amap\.com\/ws\/boss\/(?:pay\/web\/paySuccess\/info\/request\|transportation\/diversion\/resource\/driving) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1004` | `^https?:\/\/m5\.amap\.com\/ws\/(?:mapapi\/hint_text\/offline_data\|message\/notice\/list\|shield\/search\/new_hotword) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1005` | `^https?:\/\/m5\.amap\.com\/ws\/aos\/main\/page\/product\/list\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1006` | `^https?:\/\/m5\.amap\.com\/ws\/faas\/amap-navigation\/(?:main-page-assets\|main-page-location\|ridewalk-end-fc\|usr-profile-fc\/homeV2) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1007` | `^https?:\/\/m5\.amap\.com\/ws\/faas\/amap-navigation\/card-service-(?:car-end\|route-plan) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1008` | `^https?:\/\/m5\.amap\.com\/ws\/shield\/scene\/recommend\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1009` | `^https?:\/\/m5\.amap\.com\/ws\/shield\/search\/new_hotword\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1010` | `^https?:\/\/m5\.amap\.com\/ws\/shield\/search_poi\/tips_adv\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1011` | `^https?:\/\/m5\.amap\.com\/ws\/valueadded\/weather\/v2\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1017` | `^https?:\/\/m\.dianping\.com\/an\/gear\/dpmapp\/api\/readLionConfig\/config - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1018` | `^https?:\/\/m\.dianping\.com\/mapi\/mgw\/growth\/queryhaima - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1019` | `^https?:\/\/m\.dianping\.com\/wxmapi\/shop\/friendslike - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1050` | `^https?:\/\/mall\.meituan\.com\/api\/c\/homepage\/splash - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1062` | `^https?:\/\/maphotel\.baidu\.com\/hotel\/goextranet\/activity\/detail\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1068` | `^https?:\/\/mapi\.dianping\.com\/adshopping - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1069` | `^https?:\/\/mapi\.dianping\.com\/mapi\/intelliindex - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1070` | `^https?:\/\/mapi\.dianping\.com\/mapi\/mgw\/growth\/clipboardquery - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1071` | `^https?:\/\/mapi\.dianping\.com\/mapi\/operating\/(?:indexopsmodules\|loadsplashconfig) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1072` | `^https?:\/\/mapi\.dianping\.com\/wdrpreload\/userprediction - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1079` | `^https?:\/\/mbd\.baidu\.com\/ccs\/v1\/start\/confsync\?appname=baidu_input - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1097` | `^https?:\/\/mime\.baidu\.com\/commer\/pocket_api\/enterprise_list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1098` | `^https?:\/\/mime\.baidu\.com\/sapi\/v1\/circle\/joinedlist - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1099` | `^https?:\/\/mime\.baidu\.com\/sapi\/v1\/lccorpus\/(?:applist\|pannellist) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1100` | `^https?:\/\/mime\.baidu\.com\/v5\/activity\/advertisementnonrealtime - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1101` | `^https?:\/\/mime\.baidu\.com\/v5\/hotpatch\/check\?hotpatch - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1102` | `^https?:\/\/mime\.baidu\.com\/v5\/start_screen_ads/list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1103` | `^https?:\/\/mime\.baidu\.com\/v\d\/IosStart\/getStartInfo - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1104` | `^https?:\/\/mime\.baidu\.com\/v\d\/activity\/advertisement - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1180` | `^https?:\/\/oss\.amap\.com\/ws\/banner\/lists\/\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1196` | `^https?:\/\/p\.meituan\.com\/api\/privacy\/config - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1198` | `^https?:\/\/p\d\.meituan\.net\/(display\|mmc)\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1199` | `^https?:\/\/p\d\.meituan\.net\/cell - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1207` | `^https?:\/\/pan\.baidu\.com\/act\/api\/activityentry\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1208` | `^https?:\/\/pan\.baidu\.com\/act\/api\/conf\?.*conf_key=youa_core_config_ios - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1209` | `^https?:\/\/pan\.baidu\.com\/api\/getconfig\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1210` | `^https?:\/\/pan\.baidu\.com\/api\/getsyscfg\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1211` | `^https?:\/\/pan\.baidu\.com\/api\/plugin\/get\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1212` | `^https?:\/\/pan\.baidu\.com\/api\/taskscore\/tasklist\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1213` | `^https?:\/\/pan\.baidu\.com\/buy\/ad\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1214` | `^https?:\/\/pan\.baidu\.com\/recommend\/query\/list\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1215` | `^https?:\/\/pan\.baidu\.com\/rest\/\d\.\d\/pcs\/adv\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1216` | `^https?:\/\/pan\.baidu\.com\/youai\/material\/v1\/getbynavid\?.*nav_id=1 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1232` | `^https?:\/\/portal-portm\.meituan\.com\/horn_ios - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1252` | `^https?:\/\/r6\.mo\.baidu\.com\/res\/file/advertisement\/files\/.+\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1267` | `^https?:\/\/res\.mi\.baidu\.com\/imeres\/ime-res\/advertisement\/files\/.+\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1278` | `^https?:\/\/rms\.meituan\.com\/api\/v\d\/rmsmina\/c\/queryWechatAdvertisement - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1285` | `^https?:\/\/s3plus\.meituan\.net\/ocean-blk-index\/index\/blk_conf - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1286` | `^https?:\/\/s3plus\.meituan\.net\/v\d\/mss_\w+\/brandcpt - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1288` | `^https?:\/\/s3plus\.meituan\.net\/v\d\/mss_\w+\/waimai-alita\/\w+\.zip$ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1326` | `^https?:\/\/sns\.amap\.com\/ws\/msgbox\/pull_mp\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1340` | `^https?:\/\/sqt\.meituan\.com\/s\/gateway\/mweb\/api\/marketingResource\/show - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1408` | `^https?:\/\/update\.pan\.baidu\.com\/statistics - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1431` | `^https?:\/\/w\.meituan\.net\/v\d\/mss_\w+\/waimai-mach\/\d+\/\d+\/pt-im-(?:guider\|coupon-card-stateful) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1441` | `^https?:\/\/web\.meituan\.com\/api\/miniprogram\/my\/(?:novelZone\|resources) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1442` | `^https?:\/\/web\.meituan\.com\/newUser\/returnMoney\/popWindow - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1484` | `^https?:\/\/www\.meituan\.com\/api\/v\d\/appstatus\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1544` | `^https?:\/\/yongche\.baidu\.com\/gomarketing\/api\/popup\/getentrancecordovaurl$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1545` | `^https?:\/\/yongche\.baidu\.com\/goorder\/passenger\/baseinfo$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1546` | `^https?:\/\/yongche\.baidu\.com\/goorder\/passenger\/cobuild\/pull\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1547` | `^https?:\/\/yongche\.baidu\.com\/goorder\/passenger\/operationgirdle$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:206` | `^https?:\/\/afd\.baidu\.com\/afd\/entry\?action=(update\|query) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:209` | `^https?:\/\/ai\.amap\.com\/v1\/ai_rec\/home_qs\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:211` | `^https?:\/\/aiqicha\.baidu\.com\/app\/commonstatusAjax - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:212` | `^https?:\/\/aiqicha\.baidu\.com\/app\/getAppPopSettingAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:215` | `^https?:\/\/aiqicha\.baidu\.com\/app\/getNewsReportAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:216` | `^https?:\/\/aiqicha\.baidu\.com\/app\/getPopConfigAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:217` | `^https?:\/\/aiqicha\.baidu\.com\/apps\/getHomeMonitorDataAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:218` | `^https?:\/\/aiqicha\.baidu\.com\/apps\/getHotRecommendV2Ajax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:219` | `^https?:\/\/aiqicha\.baidu\.com\/apps\/searchRecommendAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:475` | `^https?:\/\/apimobile\.meituan\.com\/appupdate - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:476` | `^https?:\/\/apimobile\.meituan\.com\/group\/v\d\/recommend\/unity\/recommends - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:568` | `^https?:\/\/appwk\.baidu\.com\/activity\/interface\/wkapppopup\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:569` | `^https?:\/\/appwk\.baidu\.com\/appapi\/abg\/index\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:570` | `^https?:\/\/appwk\.baidu\.com\/appapi\/search\/hot\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:571` | `^https?:\/\/appwk\.baidu\.com\/appapi\/task\/viptasklist\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:572` | `^https?:\/\/appwk\.baidu\.com\/naapi\/recommend\/recommenddoc\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:573` | `^https?:\/\/appwk\.baidu\.com\/naapi\/recommend\/vipdoccard\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:574` | `^https?:\/\/appwk\.baidu\.com\/naapi\/search\/wkhotwords\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:575` | `^https?:\/\/appwk\.baidu\.com\/xpage\/interface\/wknaad\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:582` | `^https?:\/\/awp-assets\.meituan\.net\/hfe\/fep\/\w+\.json - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:621` | `^https?:\/\/catdot\.dianping\.com\/broker-service\/hijack - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:622` | `^https?:\/\/catfront\.dianping\.com\/api\/metric\?v=\d&p=rn_gcbu_mrn-joy-poidetail - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:627` | `^https?:\/\/cdb\.meituan\.com\/marketing\/source\/getPageSlotList - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:680` | `^https?:\/\/cover\.baidu\.com\/cover\/page\/dspSwitchAds\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:705` | `^https?:\/\/ddplus\.meituan\.net\/v\d\/mss_\w+\/(?:ehc\|titansx\|ddblue\|edfu)\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:747` | `^https?:\/\/ecom\.map\.baidu\.com\/ad-ops\/afd\/popup\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:771` | `^https?:\/\/fcvbjbcebos\.baidu\.com\/.+.mp4 - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:888` | `^https?:\/\/idgdata\.baidu\.com\/idgactivity\/api\/newuser\/info\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:889` | `^https?:\/\/idgdata\.baidu\.com\/mc\/app\/api\/listterminal\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:990` | `^https?:\/\/log.+?baidu\.com - reject` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/aggressive-ads.list:95` | `DOMAIN,openjmacs.m.taobao.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/aggressive-ads.list:98` | `DOMAIN,umengacs.m.taobao.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/qingrex-miniapp-app-ad.list:11` | `DOMAIN,mobads.baidu.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/qingrex-miniapp-app-ad.list:12` | `DOMAIN-SUFFIX,pos.baidu.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/qingrex-miniapp-app-ad.list:17` | `DOMAIN,afd.baidu.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/qingrex-miniapp-app-ad.list:18` | `DOMAIN,afdconf.baidu.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/qingrex-miniapp-app-ad.list:19` | `DOMAIN,lc.map.baidu.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/qingrex-miniapp-app-ad.list:48` | `DOMAIN,maplocatesdksnapshot.d.meituan.net,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/reject.list:104` | `DOMAIN,r.dianping.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/reject.list:15` | `DOMAIN,afdconf.baidu.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/reject.list:16` | `DOMAIN,amap-aos-info-nogw.amap.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/reject.list:45` | `DOMAIN,dpmtpush.dianping.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/reject.list:55` | `DOMAIN,hlx.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/reject.list:81` | `DOMAIN,layout.meituan.net,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/reject.list:82` | `DOMAIN,lc.map.baidu.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/reject.list:90` | `DOMAIN,lx0.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/web-ads.list:62` | `DOMAIN-SUFFIX,mads.meituan.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 国内 App 核心 API | `Rules/web-ads.list:85` | `DOMAIN,mobads.baidu.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/17173-game.conf:13` | `DOMAIN-SUFFIX,s.17173cdn.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/18183-game.conf:9` | `DOMAIN-SUFFIX,img1.18183.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/36-kr.conf:16` | `^https://gateway\.36kr\.com/api/mis/nav/search/topicListV2\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/58-tong-cheng.conf:14` | `DOMAIN-SUFFIX,t1.58cdn.com.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/58-tong-cheng.conf:15` | `DOMAIN-SUFFIX,t2.58cdn.com.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/58-tong-cheng.conf:16` | `DOMAIN-SUFFIX,t3.58cdn.com.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/58-tong-cheng.conf:28` | `^https?://.+?\.58cdn\.com\.cn/brandads/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/all-football.conf:9` | `DOMAIN-KEYWORD,apimg.qunliao.info,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/amap.conf:11` | `DOMAIN-SUFFIX,v.smtcdns.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/aol.conf:13` | `DOMAIN-SUFFIX,cdn.komentary.aol.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/baby-tree-parenting.conf:9` | `^https?://aimg\.babytreeimg\.com/group1/M00/*/*/.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/baby-tree.conf:11` | `URL-REGEX,"^http:\/\/m\.meitun\.com\/newapi\/router\/topic\/hometptf\/feedRecommend",REJECT-DICT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/baby-tree.conf:12` | `URL-REGEX,"^http:\/\/pic08\.babytreeimg\.com\/knowledge\/2022\/0923\/\w+",REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:14` | `DOMAIN,promotion.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:15` | `DOMAIN,promotion-1.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:16` | `DOMAIN,promotion-2.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:17` | `DOMAIN,promotion-3.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:21` | `DOMAIN,img-x.jd.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:27` | `AND,((DOMAIN-SUFFIX,pddpic.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:28` | `AND,((DOMAIN-SUFFIX,pddcdn.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:29` | `AND,((DOMAIN-SUFFIX,jdimg.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:30` | `AND,((DOMAIN-SUFFIX,360buyimg.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:33` | `URL-REGEX,"^https?:\/\/m\.360buyimg\.com\/(?:mobilecms\|babel)\/.*",REJECT-IMG,extended-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/che-lai-le.conf:14` | `^https?://pic1\.chelaile\.net\.cn/adv/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/che-lai-le.conf:17` | `^https?://atrace\.chelaile\.net\.cn/adpub/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/che-lai-le.conf:18` | `^https?://atrace\.chelaile\.net\.cn/exhibit\?&adv_image - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/che-lai-le.conf:20` | `^https?://cdn\.\w{3}\.chelaileapp\.cn/(api/)?adpub - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/clicli.conf:9` | `^https?://js-ad\.ayximgs\.com\.ad-universe-cdn\.hzhcbkj\.cn/xgapp\.php/v2/top_notice - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/dao-meng-kong-jian.conf:9` | `^https?://appdmkj\.5idream\.net/appPic/homepage - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/di-duan-ying-shi.conf:10` | `^https?://img\.ddrk\.me/cover\.png - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/di-duan-ying-shi.conf:11` | `^https?://ddrk\.me/image/logo_footer\.png - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/di-duan-ying-shi.conf:12` | `^https?://ddrk\.me/wp-content/plugins/advanced-floating-content-lite/public/images/close\.png - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/di-duan-ying-shi.conf:9` | `^https?://img\.ddrk\.me/ad190824 - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/dian-shi-jia.conf:10` | `^https?://cdn\.dianshihome\.com/static/ad/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/dingdong-maicai.conf:10` | `DOMAIN,ddfs-public.ddimg.mobi,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/dlabel-cloud-tag.conf:9` | `^https://imagepc\.ctaiot\.com/dlabel/0/startpage - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/douyu.conf:12` | `DOMAIN,stun1.douyucdn.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/douyu.conf:17` | `^https://rtbapi\.douyucdn\.cn/japi/sign/app/getinfo - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/douyu.conf:9` | `URL-REGEX,"^http:\/\/linkmicschedule\.douyucdn\.cn\/im_schedule\/im_gate_list",REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/eastday.conf:14` | `DOMAIN-SUFFIX,afpimages.eastday,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/eastday.conf:9` | `DOMAIN-SUFFIX,afpimages.eastday.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/facebook.conf:11` | `DOMAIN-SUFFIX,staticxx.facebook.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/fan-qie-novel.conf:27` | `^https?://.+\.(pglstatp-toutiao\|pstatp)\.com/(obj\|img)/(ad-app-package\|ad)/.+ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/fan-qie-novel.conf:28` | `^https?://.+\.(pglstatp-toutiao\|pstatp)\.com/(obj\|img)/web\.business\.image/.+ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/fan-qie-novel.conf:31` | `^https?://.+\.byteimg.com/tos-cn-i-1yzifmftcy/(.+)-jpeg\.jpeg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/fan-qie-novel.conf:35` | `^https?://.+\.byteimg\.com/ad-app-package - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/fan-qie-novel.conf:36` | `^https?://.+\.byteimg\.com/web\.business\.image - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/fen-bi.conf:14` | `^https://hera-webapp\.fenbi\.com/(iphone\|ipad)/topic/hotquery/list\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/feng-huang-xiu.conf:10` | `^https?://api\.fengshows\.com/api/launchAD - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/flyer-tea.conf:11` | `^https://ptf\.flyertrip\.com/static/img/common/ic_plate_mine_button\.png - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/go-com.conf:10` | `DOMAIN-SUFFIX,adimages.go.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/hua-sheng-di-tie.conf:10` | `^https?://cmsfile\.wifi8\.com/uploads/png/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/huya.conf:10` | `DOMAIN,livewebbs2pcdn.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/huya.conf:11` | `DOMAIN,pp-cdnfile2pcdn.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/huya.conf:8` | `DOMAIN,huyafile.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/huya.conf:9` | `DOMAIN,livewebbs2.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/jia-xiao-yi-dian-tong.conf:17` | `^https?://api\.jxedt\.com/jump/EMiCcDNp - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/jia-xiao-yi-dian-tong.conf:18` | `^https?://richmanmain\.jxedt\.com/advertisement/fallback - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/jian-xun.conf:9` | `^https?://api\.tipsoon\.com/api/v1/top/ad - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/jie-mian-news.conf:9` | `^https?://img\.jiemian\.com/ads/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/jump.conf:12` | `DOMAIN,images.pinduoduo.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kingsoft-power-word.conf:10` | `DOMAIN,img.auction-ads.wpscdn.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kingsoft-power-word.conf:20` | `^https?://mobile-pic\.cache\.iciba\.com/feeds_ad/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou-music.conf:16` | `DOMAIN,pgdt.gtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou-music.conf:17` | `DOMAIN,adsmind.gdtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou-music.conf:23` | `DOMAIN-KEYWORD,c1img.ali.kugou.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou-music.conf:24` | `DOMAIN-KEYWORD,kgstaticdlbssdlbig.tx.kugou.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou-music.conf:26` | `DOMAIN-KEYWORD,splashimgbssdl.yun.kugou.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou-music.conf:32` | `DOMAIN-KEYWORD,trackercdnbj.kugou.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou-youth.conf:10` | `^https://gateway\.kugou\.com/youth/v1/start_img/last\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou.conf:11` | `DOMAIN,adsmind.gdtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou.conf:16` | `DOMAIN,splashimgretrybssdl.cloud.kugou.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou.conf:31` | `^https://gzacshow\.kugou\.com/mfanxing-home/cdn/room/index/list_v2 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku-gou.conf:32` | `^https://gzacshow\.kugou\.com/mfx-rt-show/cdn/mo/show/headline - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku6.conf:12` | `DOMAIN-SUFFIX,static.ku6.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku6.conf:13` | `DOMAIN-SUFFIX,gug.ku6cdn.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku6.conf:14` | `DOMAIN-SUFFIX,vi1.ku6img.net,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ku6.conf:15` | `DOMAIN-SUFFIX,vi2.ku6img.net,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-di100.conf:11` | `^https?://p\.kuaidi100\.com/apicenter/card\.dox - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:14` | `^https://(cdn-)?api\.kkmh\.com/v\d/ad/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:15` | `^https://(cdn-)?h5\.kuaikanmanhua\.com/user/scene/api/new_user/sign_in/list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:16` | `^https://(cdn-)?api\.kkmh\.com/v\d/business/activities/get - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:17` | `^https://(cdn-)?api\.kkmh\.com/v\d/business/mine/business_config - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:18` | `^https://(cdn-)?topic\.kkmh\.com/gamecard/v\d/activityModule/userSignInInfo\?activitySignInConfigId - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:19` | `^https://(cdn-)?topic\.kkmh\.com/gamecard/v\d/activityModule/fetchButtonInfo\?buttonConfigId - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:20` | `^https://(cdn-)?topic\.kkmh\.com/gamecard/v\d/activityText/getUserActivityTextInfo\?activityTextConfigId - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:21` | `^https://(cdn-)?pay\.kkmh\.com/v\d/kb/comic_page_banner/detail - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:22` | `^https://(cdn-)?api\.kkmh\.com/v\d/business/fake_push/info - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:23` | `^https://(cdn-)?shop\.kkmh\.com/mbff/popup_administration/page_management_popup_administration$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:24` | `^https://(cdn-)?pay\.kkmh\.com/v\d/vip/banner_tip_list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:25` | `^https://(cdn-)?pay\.kkmh\.com/v\d/vip/charge_tip_list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:28` | `^https://(cdn-)?api\.kkmh\.com/v\d/checkin/api/new_user/tab_info$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:30` | `^https://(cdn-)?pay\.kkmh\.com/v\d/vip/platform_base/popups_display$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-kan-comic.conf:31` | `^https://(cdn-)?api\.kkmh\.com/v\d/checkin/task_center/get_by_task_type - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuai-le-guang-bo.conf:11` | `DOMAIN,adcdn.hpplay.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/kuro-bbs.conf:12` | `^https://api\.kurobbs\.com/forum/app/topic/hotlist\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/lan-ren-ting-shu.conf:10` | `^https?://dapis\.mting\.info/yyting/advertclient/ClientAdvertList\.action - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/lan-ren-ting-shu.conf:9` | `^https?://118\.178\.214\.118/yyting/advertclient/ClientAdvertList\.action - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/le-eco.conf:20` | `DOMAIN-SUFFIX,static.app.m.letv.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/leju.conf:11` | `DOMAIN-SUFFIX,staticadm.leju.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/lenovo-print.conf:9` | `^https://abcapi\.lenovoimage\.com/v1/promote/startup - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:10` | `URL-REGEX,"^https:\/\/a\.line\.me\/er\/l.*\/v\d\/event\/image",REJECT-IMG` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:21` | `URL-REGEX,"^https:\/\/obs\.line-scdn\.net\/0h[a-zA-Z0-9_-]{50}[a-zA-Z0-9_-]*",REJECT-DROP` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:22` | `URL-REGEX,"^https:\/\/obs\.line-scdn\.net\/0h.+\/(o\|m)\d+x\d+$",REJECT-DROP` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:23` | `URL-REGEX,"^https:\/\/obs\.line-scdn\.net\/0hGH\d",REJECT-DROP` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:24` | `URL-REGEX,"^https:\/\/obs\.line-scdn\.net\/0h.+\/\d+p\.mp4$",REJECT-DROP` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:25` | `URL-REGEX,"^https:\/\/obs\.line-scdn\.net\/r\/linecrs\/.+\/m180x180$",REJECT-IMG` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:27` | `URL-REGEX,"^https:\/\/ec-bot-obs\.line-scdn\.net\/0h[0-9a-zA-Z_-]{50}[0-9a-zA-Z_-]*",REJECT-IMG` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:28` | `URL-REGEX,"^https:\/\/d\.line-scdn\.net\/lcp-prod-photo\/20.+\.(jpg\|jpeg\|png)",REJECT-IMG` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:30` | `URL-REGEX,"^https:\/\/web-mmap-pay\.line-apps\.com\/tw\/liff\/campaign\/v\d\/aggregate\/ad\/banner\/",REJECT-IMG` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:31` | `URL-REGEX,"^https:\/\/scdn\.line-apps\.com\/lan\/image\/line\/bannerImageEvent\/",REJECT-DROP` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:32` | `URL-REGEX,"^https:\/\/scdn\.line-apps\.com\/lan\/document\/pageEvent\/line\/ios\/",REJECT-DROP` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:46` | `^https://ad\.line-scdn\.net/0h - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:47` | `^https://static\.line-scdn\.net/ad-sdk/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:48` | `^https://scdn\.line-apps\.com/appresources/moretab/list\.json - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/line.conf:9` | `URL-REGEX,"^https:\/\/a\.line\.me\/er\/lads\/v\d\/ei\?",REJECT-IMG` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/lofter.conf:10` | `^https?://images\.pinduoduo\.com/marketing\_api - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ma-ka-long-wan-tu.conf:10` | `^https?://static01\.versa-ai\.com/upload/ec0ba51d68f9/.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ma-ma-wang-yun-yu.conf:9` | `^https?://qimg\.cdnmama\.com/rd - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mai-dui-dui.conf:11` | `^https?://mobads-pre-config\.cdn\.bcebos\.com/preload\.php - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mai-dui-dui.conf:15` | `^https?://conf-darwin\.xycdn\.com - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mi-ho-yo-bbs.conf:11` | `^https://bbs-api-static\.miyoushe\.com/search/api/search/pre_keyword\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mkz.conf:10` | `^https://base\.mkzcdn\.com/advert/app/story/read/v\d - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mkz.conf:11` | `^https://base\.mkzcdn\.com/advert/app/task/motivate/v\d - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mkz.conf:12` | `^https://base\.mkzcdn\.com/advert/app/user/slide\d/v\d/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/mkz.conf:9` | `^https://base\.mkzcdn\.com/advert/app/read/v\d - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/nai-fei-ying-shi.conf:10` | `^https?://www\.nfmovies\.com/templets/default/images/logos - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/nai-fei-ying-shi.conf:11` | `^https?://www\.nfmovies\.com/uploads/images/play\.jpg - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/nai-fei-ying-shi.conf:9` | `^https?://www\.nfmovies\.com/pic/tu/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/naver.conf:12` | `DOMAIN-SUFFIX,adimg3.search.naver.net,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ntplay.conf:9` | `^https?://blog\.nilbt\.com/static/api/update - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/oschina.conf:9` | `^https?://www\.oschina\.net/action/apiv2/get_launcher - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/oupeng.conf:10` | `DOMAIN-SUFFIX,img-ad.oupeng.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/outfit7.conf:11` | `DOMAIN-SUFFIX,cdn.outfit7.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/outfit7.conf:12` | `DOMAIN-SUFFIX,cdn-gcs.outfit7.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/outlook.conf:9` | `DOMAIN,acdn.adnxs.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/pcauto.conf:10` | `DOMAIN,imgad0.pcauto.com.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/pcauto.conf:11` | `DOMAIN,imgad0.pconline.com.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/phoenix-new-media.conf:24` | `DOMAIN-SUFFIX,c0.ifengimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/phoenix-new-media.conf:25` | `DOMAIN-SUFFIX,c1.ifengimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/photoable.conf:10` | `DOMAIN,cdn.adapi.fotoable.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/picc-insurance.conf:10` | `^https://zgrb\.epicc\.com\.cn/G-HAPP/a/update/startupPage/v1 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/picc-insurance.conf:11` | `^https://zgrb\.epicc\.com\.cn/G-HAPP/a/config/guessYouLike/v3 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/picc-insurance.conf:9` | `^https://zgrb\.epicc\.com\.cn/G-HAPP/h/headlines/queryHeadlines - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/pinduoduo.conf:14` | `DOMAIN,cdl-1.pddpic.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/pinduoduo.conf:16` | `DOMAIN,cdl-p2.pddpic.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/pinduoduo.conf:17` | `DOMAIN,cd-1.pddpic.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/pptv.conf:11` | `DOMAIN,asimgs.pplive.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/pptv.conf:22` | `DOMAIN-SUFFIX,static.g.pptv.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qi-shui-music.conf:13` | `^https://lf-cdn-tos\.bytescm\.com/obj/static/ad/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qi-xin-bao.conf:18` | `^https://qxb-minicode-pic-osscache\.qixin\.com/web/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqksong.conf:10` | `DOMAIN,adsmind.ugdtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqksong.conf:19` | `DOMAIN,pgdt.gtimg.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqksong.conf:20` | `DOMAIN,pgdt.ugdtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqksong.conf:21` | `DOMAIN,qzs.gdtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqksong.conf:40` | `DOMAIN-SUFFIX,ugdtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqksong.conf:42` | `URL-REGEX,"^http:\/\/y\.gtimg\.cn\/music\/common\/upload\/t_k_main_page_banner\/",REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqksong.conf:9` | `DOMAIN,adsmind.gdtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqmusic.conf:11` | `DOMAIN,adcdn.tencentmusic.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqmusic.conf:12` | `DOMAIN,adcdn6.tencentmusic.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqnews.conf:9` | `^https?:\/\/r\.inews\.qq\.com\/(?:adsBlacklist\|getFullScreenPic\|getQQNewsRemoteConfig) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/quan-min-ge-ge.conf:9` | `^https?://y\.gtimg\.cn/music/common//upload/kg_ad/.+?\d{3,4}x\d{4} - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/rqrun.conf:9` | `^https://api\.rq\.run/Api/Spreadimg/spreadimg_type_list$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/sape.conf:10` | `DOMAIN-SUFFIX,cdn-rtb.sape.ru,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/seven-cat.conf:10` | `DOMAIN,cdn-new-ad.wtzw.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/seven-cat.conf:21` | `^https://cdn\.wtzw\.com/bookimg/free/api/v\d/reader/reader-copy-paragraph-all\.json - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/seven-cat.conf:9` | `DOMAIN,cdn-ad.wtzw.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/soul.conf:12` | `DOMAIN,ad-h5-cdn.soulapp.cn,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/soul.conf:13` | `DOMAIN,ad-h5-station-cdn.soulapp.cn,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/taobao.conf:11` | `DOMAIN,hudong.alicdn.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/tencent-games-community.conf:9` | `^https?://static\.gameplus\.qq\.com/img/\d{10}-\d{4}$ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/tencent-sports.conf:10` | `^https?://sports3\.gtimg\.com/community/20cf93884470434eaf38b2e77ab7796a\.png - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/tencent-video.conf:14` | `DOMAIN,pgdt.gtimg.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/tencent-video.conf:9` | `DOMAIN,adsmind.gdtimg.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/the-paper-news.conf:11` | `DOMAIN,imgadpai.thepaper.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/the-paper-news.conf:13` | `DOMAIN-SUFFIX,imgad.thepaper.cn,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/tian-shan-yun-tv.conf:9` | `^https?://www\.tsytv\.com\.cn/api/app/ios/ads - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/ttvoice.conf:9` | `^https?://ga-album-cdnqn\.52tt\.com/prod-yunying/.+.jpg - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:22` | `^https://images\.qmai\.cn/s214925/2023 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:61` | `^https://appuser-static\.huolala\.cn/imgs - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:66` | `^https://sto-customer-app\.oss-cn-shanghai\.aliyuncs\.com/images - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:72` | `^https://fscdn\.zto\.com/fs1 - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:98` | `^https://cbd-gateway-service-applets\.hualala\.com/arch/api/banner/QueryBannerImgList - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/wechat-mini-programs.conf:99` | `^https://alittle-tea\.oss-cn-shanghai\.aliyuncs\.com/images/platform/alittle - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/youku.conf:19` | `DOMAIN,nbsdk-baichuan.alicdn.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/youku.conf:28` | `DOMAIN,adsmind.ugdtimg.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Apps/zdm.conf:9` | `DOMAIN,adx-api.zdmimg.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Misc/android-compatible-ads.conf:19` | `DOMAIN,ads-partner.cdn.bcebos.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Misc/android-compatible-ads.conf:39` | `DOMAIN,static.doubleclick.net,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Misc/cdn-direct.conf:5` | `AND,((DOMAIN-SUFFIX,pddpic.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Misc/cdn-direct.conf:6` | `AND,((DOMAIN-SUFFIX,pddcdn.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Misc/cdn-direct.conf:7` | `AND,((DOMAIN-SUFFIX,jdimg.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Misc/cdn-direct.conf:8` | `AND,((DOMAIN-SUFFIX,360buyimg.com,extended-matching),(USER-AGENT,"*bili*")),REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Misc/cdn-direct.conf:9` | `URL-REGEX,"^https?:\/\/m\.360buyimg\.com\/(?:mobilecms\|babel)\/.*",REJECT-IMG,extended-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:103` | `DOMAIN,imgad0.pcauto.com.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:104` | `DOMAIN,imgad0.pconline.com.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:112` | `DOMAIN,livewebbs2.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:113` | `DOMAIN,livewebbs2pcdn.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:31` | `DOMAIN,ad-cdn.qingting.fm,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:36` | `DOMAIN,admusicpic.music.126.net,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:39` | `DOMAIN,adx-api.zdmimg.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:56` | `DOMAIN,cd-1.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:57` | `DOMAIN,cdl-1.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:58` | `DOMAIN,cdl-p2.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:69` | `DOMAIN,ddfs-public.ddimg.mobi,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:93` | `DOMAIN,hudong.alicdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:94` | `DOMAIN,huyafile.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:40` | `^https:\/\/fscdn\.zto\.com\/fs1 - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:64` | `^https:\/\/cdn\.web\.chelaile\.net\.cn\/info-flow\/index\.html - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:80` | `^http:\/\/img\.dailmo\.com\/img\/61\/23c7125bfe6166d69f3bff5b0ca4d31e\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:81` | `^http:\/\/img\.dailmo\.com\/img\/50\/edb40c6392f848df37f9c31d8a6f90f6\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:82` | `^http:\/\/img\.dailmo\.com\/img\/6\/90585d9e96c73dd49644af57d8501624\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:83` | `^http:\/\/img\.dailmo\.com\/img\/5\/6cb2aa237ce1f65944aa1ecb29fbdeef\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:84` | `^http:\/\/img\.allahall\.com\/img\/61\/23c7125bfe6166d69f3bff5b0ca4d31e\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:85` | `^http:\/\/img\.allahall\.com\/img\/50\/edb40c6392f848df37f9c31d8a6f90f6\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:86` | `^http:\/\/img\.allahall\.com\/img\/6\/90585d9e96c73dd49644af57d8501624\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:87` | `^http:\/\/img\.allahall\.com\/img\/5\/6cb2aa237ce1f65944aa1ecb29fbdeef\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:88` | `^http:\/\/img\.allahall\.com\/img\/59\/6a13a75dfe46ebfdac96bd27ef098885\.jpg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:94` | `^https:\/\/gw\.alicdn\.com\/mt\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:95` | `^https:\/\/gw\.alicdn\.com\/tfs\/.+\d{3,4}-\d{4} - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:96` | `^https:\/\/gw\.alicdn\.com\/tps\/.+\d{3,4}-\d{4} - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1000` | `^https?:\/\/m1\.ad\.10010\.com\/noticeMag\/images\/imageUpload\/2\d{3} - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:101` | `^https?:\/\/.+\.(pglstatp-toutiao\|pstatp)\.com\/(obj\|img)\/(ad-app-package\|ad)\/.+ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1012` | `^https?:\/\/m\.360buyimg\.com\/babel\/jfs\/t1\/[0-9]{6}\/[0-9]{2}\/[0-9]{5}\/[0-9]{6}\/.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1013` | `^https?:\/\/m\.aty\.sohu\.com\/openload? - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1016` | `^https?:\/\/m\.client\.10010\.com\/uniAdmsInterface\/(getHomePageAd\|getWelcomeAd) - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:102` | `^https?:\/\/.+\.(pglstatp-toutiao\|pstatp)\.com\/(obj\|img)\/web\.business\.image\/.+ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1029` | `^https?:\/\/m\.trip\.com\/restapi\/.*\/(queryAdsDisplayData\|queryBadge\|isPopUp\|(?:G\|g)etAppConfig\|getRecommendResource\|appWelcomeImage\|uploadConfigContent\|appData\|appAttributionLog\|heartBeat\|GetUserUpgradeNoticeInfo\|incrQueryTrans\|getTopPic\|getABTestData) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:104` | `^https?:\/\/.+\.byteimg.com/tos-cn-i-1yzifmftcy\/(.+)-jpeg\.jpeg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:105` | `^https?:\/\/.+\.byteimg\.com\/ad-app-package - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:106` | `^https?:\/\/.+\.byteimg\.com\/web\.business\.image - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1080` | `^https?:\/\/mbs\.boc\.cn\/ubas-mgateway-static\/images\/advertType\/.+.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1081` | `^https?:\/\/mbs\.boc\.cn\/ubas-mgateway-static\/images\/theme\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1115` | `^https?:\/\/mmg\.aty\.sohu\.com\/(?:pvlog\|mqs)? - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1116` | `^https?:\/\/mmgr\.gtimg\.com\/gjsmall\/qiantu\/upload\/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1117` | `^https?:\/\/mmgr\.gtimg\.com\/gjsmall\/qqpim\/public\/ios\/splash\/.+?\/\d{4}_\d{4} - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1119` | `^https?:\/\/mobads-pre-config\.cdn\.bcebos\.com\/preload\.php - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1124` | `^https?:\/\/mobile-pic\.cache\.iciba\.com\/feeds_ad\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1139` | `^https?:\/\/mps\.95508\.com\/mps\/club\/cardPortals\/adv\/\d{25}\.(?:png\|jpg) - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1144` | `^https?:\/\/ms\.jr\.jd\.com\/gw\/generic\/aladdin\/(new)?na\/m\/(?:getLoadingPicture\|getPageMutilDataForHomePage\|getTopCard\|getBottomNavigation) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1145` | `^https?:\/\/ms\.jr\.jd\.com\/gw\/generic\/app\/(new)?na\/m\/getLaunchImageList - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1181` | `^https?:\/\/oss\.jegotrip\.com\.cn\/\/appSyncimage - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1187` | `^https?:\/\/p0\.pipi\.cn\/(?:adAdmin\|mediaplus\/maoyantong_ads_fe)\/\w+\.(?:jpg\|png)\?imageMogr2\/thumbnail\/(?:860x0\|!165x165\|!1049x1169) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1189` | `^https?:\/\/p0\.pipi\.cn\/(?:adAdmin\|mediaplus\/maoyantong_ads_fe)\/\w+\.jpg\?imageMogr2\/quality\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1190` | `^https?:\/\/p[^4](c)?\.music\.126\.net\/\w+==\/10995\d{13}\.jpg$ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1194` | `^https?:\/\/p\.kuaidi100\.com\/apicenter\/card\.dox - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:122` | `^https?:\/\/118\.178\.214\.118\/yyting\/advertclient\/ClientAdvertList\.action - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1223` | `^https?:\/\/photocdn\.sohu\.com\/tvmobilemvms - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1224` | `^https?:\/\/pic\.edaijia\.cn\/adsplash\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1225` | `^https?:\/\/pic\.k\.sohu\.com\/img8\/wb\/tj\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1226` | `^https?:\/\/pic\.k\.sohu\.com\/img\d\/wb\/tj\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1227` | `^https?:\/\/pic\d\.chelaile\.net\.cn\/adv\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1233` | `^https?:\/\/portal-xunyou\.qingcdn\.com\/api\/v\d\/ios\/ads\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1234` | `^https?:\/\/portal-xunyou\.qingcdn\.com\/api\/v\d\/ios\/configs\/(?:splash_ad\|ad_urls) - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1238` | `^https?:\/\/pss\.txffp\.com\/piaogen\/images\/launchScreen/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1239` | `^https?:\/\/pt-starimg\.didistatic\.com\/static\/starimg\/node\/.*.(jpg\|png\|gif) - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1240` | `^https?:\/\/ptmpcap\.caocaokeji\.cn\/advert-bss\/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1247` | `^https?:\/\/qimg\.cdnmama\.com\/rd - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1250` | `^https?:\/\/qxb-minicode-pic-osscache\.qixin\.com\/web\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1251` | `^https?:\/\/qzonestyle\.gtimg\.cn\/qzone\/biz\/gdt\/mob\/sdk\/ios\/v\d\/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1253` | `^https?:\/\/r\.inews\.qq\.com\/(?:adsBlacklist\|getFullScreenPic\|getQQNewsRemoteConfig) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1266` | `^https?:\/\/res\.mall\.10010\.cn\/mall\/common\/js\/fa\.js\?referer= - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1280` | `^https?:\/\/rtbapi\.douyucdn\.cn\/japi\/sign\/app\/getinfo - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1289` | `^https?:\/\/s\.go\.sohu\.com\/adgtr\/\?gbcode= - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1298` | `^https?:\/\/scdn\.line-apps\.com\/appresources\/moretab\/list\.json - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1307` | `^https?:\/\/sf3-be-pack\.pglstatp-toutiao\.com\/img\/ad\.union\.api - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1312` | `^https?:\/\/shcss\.suning\.com\/shcss-web\/api\/appImage\/queryAppImage\.do - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1322` | `^https?:\/\/smart\.789\.image\.mucang\.cn\/advert - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1336` | `^https?:\/\/splashqqlive\.gtimg\.com\/website\/\d{6} - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1337` | `^https?:\/\/sports3\.gtimg\.com\/community\/20cf93884470434eaf38b2e77ab7796a\.png - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1350` | `^https?:\/\/static.xyzq.cn\/image\/splash\/opera3.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1351` | `^https?:\/\/static01\.versa-ai\.com\/upload\/ec0ba51d68f9\/.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1352` | `^https?:\/\/static\.95508\.com\/icppweb\/images\/modelMaterial\/(?:advertising\|accurate)\/202\d{5}\/.*.(?:png\|jpg) - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1353` | `^https?:\/\/static\.95508\.com\/mmg\/ciop\/202402\/button\/.*\.gif$ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1354` | `^https?:\/\/static\.95508\.com\/mmg\/ciop\/sysabbr\/cmep\/images\/(app)?popupads - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1355` | `^https?:\/\/static\.95508\.com\/mmg\/images\/ads\/(?!(2024031\|20241205)) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1356` | `^https?:\/\/static\.gameplus\.qq\.com\/img\/\d{10}-\d{4}$ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1357` | `^https?:\/\/static\.line-scdn\.net\/ad-sdk\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1358` | `^https?:\/\/static\.shihuocdn\.cn\/admin\/imgs/202[0-9]{5}\/[a-z0-9]{32}_513x777\.png - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1359` | `^https?:\/\/static\.shihuocdn\.cn\/admin\/imgs/202[0-9]{5}\/[a-z0-9]{32}_750x1624\.png - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1360` | `^https?:\/\/staticlive\.douyucdn\.cn\/.+?\/getStartSend - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1361` | `^https?:\/\/staticlive\.douyucdn\.cn\/upload\/signs\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1363` | `^https?:\/\/stlib\.qbb6\.com\/content\/\w+\.webp - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1368` | `^https?:\/\/swdlcdn\.eastmoney\.com\/app\/adimg\/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1380` | `^https?:\/\/tcmobileapi\.17usoft\.com\/appindexnew\/index\/(?:openscreen\|getpopupimages\|getindexlayoutcelllist\|newmemberzone\|getsearchboxtext\|gethotrecommend) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:140` | `^https?:\/\/3gimg\.qq\.com\/tencentMapTouch\/app\/activity\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1400` | `^https?:\/\/ucmp-static\.sf-express\.com\/proxy\/wxbase\/wxTicket\/wxLiveStreamInfo\?pageNo - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:141` | `^https?:\/\/3gimg\.qq\.com\/tencentMapTouch\/splash\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:144` | `^https?:\/\/4gimg\.map\.qq\.com\/mwaSplash\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1445` | `^https?:\/\/webcdn\.m\.qq\.com\/qiantu\/upload\/202[0-9]{5}\/.*.(jpg\|png) - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1453` | `^https?:\/\/www.icourse163.org\/.*?(Advertisement) - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:147` | `^https?:\/\/7n\.bczcdn\.com\/launchad\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1486` | `^https?:\/\/www\.myusmile\.online\/user\/plaqueTopic\/selectByType - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:149` | `^https?:\/\/[^(apple\|10010)]+\.(com\|cn)\/(a\|A)d(s\|v)?(\/\|\.js) - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1490` | `^https?:\/\/www\.oschina\.net\/action\/apiv2\/get_launcher - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1508` | `^https?:\/\/wx\.17u\.cn\/crapi\/query\/(?:ad\|getAdImgUrlByCode) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1539` | `^https?:\/\/y\.gtimg\.cn\/music\/.*?_Ad/\d+\.png - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1540` | `^https?:\/\/y\.gtimg\.cn\/music\/common\/upload\/kg_ad/.*?\d{4}\.jpg - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1541` | `^https?:\/\/y\.gtimg\.cn\/music\/common\/upload\/targeted_ads - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1543` | `^https?:\/\/yixiu-abtest\.alicdn\.com\/ut-abtest\/config - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1576` | `^https?:\/\/zt-app\.go189\.cn\/zt-app\/welcome\/.*?Animation - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:158` | `^https?:\/\/abcapi\.lenovoimage\.com\/v1\/promote\/startup - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1595` | `^https?:\/\/ad\.alicdn\.com\/.* - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1597` | `^https?:\/\/g\.alicdn\.com\/.*\/ad\/.* - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1598` | `^https?:\/\/gw\.alicdn\.com\/.*\/ad\/.* - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:1599` | `^https?:\/\/img\.alicdn\.com\/.*\/ad\/.* - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:190` | `^https?:\/\/ad\.line-scdn\.net\/0h - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:202` | `^https?:\/\/adstatic\.peopleapp\.com\/upload\/AppLoad\/.*.(?:jpg\|png) - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:208` | `^https?:\/\/agn\.aty\.sohu\.com\/m? - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:223` | `^https?:\/\/ams-cdn\.cdtft\.cn\/prod\/tft-ams\/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:261` | `^https?:\/\/api2\.helper\.qq\.com\/game\/buttons - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:294` | `^https?:\/\/api\.cloud\.189\.cn\/guns\/(img\/recommendedPosition\|getOpenscreenBanners) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:301` | `^https?:\/\/api\.fengshows\.com\/api\/launchAD - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:31` | `^https?:\/\/(cdn-)?api\.kkmh\.com\/v\d\/ad - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:32` | `^https?:\/\/(cdn-)?api\.kkmh\.com\/v\d\/business\/activities\/get - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:327` | `^https?:\/\/api\.intsig\.net\/user\/cs\/operating\/app\/get_startpic\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:33` | `^https?:\/\/(cdn-)?api\.kkmh\.com\/v\d\/business\/fake_push\/info - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:334` | `^https?:\/\/api\.k\.sohu\.com\/api\/channel\/ad\/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:34` | `^https?:\/\/(cdn-)?api\.kkmh\.com\/v\d\/business\/mine\/business_config - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:343` | `^https?:\/\/api\.kurobbs\.com\/forum\/app\/topic\/hotlist\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:35` | `^https?:\/\/(cdn-)?api\.kkmh\.com\/v\d\/checkin\/api\/new_user\/tab_info - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:36` | `^https?:\/\/(cdn-)?api\.kkmh\.com\/v\d\/checkin\/task_center\/get_by_task_type - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:37` | `^https?:\/\/(cdn-)?h5\.kuaikanmanhua\.com\/game-h5\/new-user-welfare\/index\.html - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:38` | `^https?:\/\/(cdn-)?h5\.kuaikanmanhua\.com\/user\/scene\/api\/new_user\/sign_in\/list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:39` | `^https?:\/\/(cdn-)?h5\.kuaikanmanhua\.com\/v\d\/kb\/recharge_good\/list_h5 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:399` | `^https?:\/\/api\.rq\.run\/Api\/Spreadimg\/spreadimg_type_list$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:41` | `^https?:\/\/(cdn-)?pay\.kkmh\.com\/v\d\/vip\/(?:banner\|charge)_tip_list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:413` | `^https?:\/\/api\.tipsoon\.com\/api\/v1\/top\/ad - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:42` | `^https?:\/\/(cdn-)?pay\.kkmh\.com\/v\d\/vip\/platform_base\/popups_display - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:43` | `^https?:\/\/(cdn-)?shop\.kkmh\.com\/mbff\/popup_administration - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:439` | `^https?:\/\/api\.ycapp\.yiche\.com\/appnews\/getadlist - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:44` | `^https?:\/\/(cdn-)?topic\.kkmh\.com\/gamecard\/v\d\/activityModule\/fetchButtonInfo\?buttonConfigId - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:440` | `^https?:\/\/api\.ycapp\.yiche\.com\/yicheapp\/getadlist - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:45` | `^https?:\/\/(cdn-)?topic\.kkmh\.com\/gamecard\/v\d\/activityModule\/userSignInInfo\?activitySignInConfigId - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:46` | `^https?:\/\/(cdn-)?topic\.kkmh\.com\/gamecard\/v\d\/activityText\/getUserActivityTextInfo\?activityTextConfigId - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:465` | `^https?:\/\/api\.zhihu\.com\/v5\.1\/topics\/answer\/\d+\/relation - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:469` | `^https?:\/\/api\.zuihuimai\.com\/static\/.*\/hongbao - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:473` | `^https?:\/\/apicloud\.zol\.com\.cn\/Article\/WapLaunchLogo - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:474` | `^https?:\/\/apicommunity\.qbb6\.com\/community\/category\/list\/get - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:488` | `^https?:\/\/app-cdn\.2q10\.com\/app\/ical\/honored\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:5` | `^https?:\/\/(?:gw\|heic)\.alicdn\.com\/imgextra\/i\d\/\d*\/?[\w!]+-\d-(?:octopus\|tps)-(?:1080\|1125)-\d{4}\.(?:jpg\|png)_(?:1\d{3}\|9\d{2})x(?:\d\|1\d{3}\|9\d{2})q[59]0 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:52` | `^https?:\/\/(gw\|heic)\.alicdn\.com\/imgextra\/\w{2}\/\w+!+(?!600000000(5412\|6148\|4021\|5802))\d*-\d-tps-(?!1035)\d{3,4}-(?!570)\d{3,4}\.(?:jpg\|png)_(1\d{3}\|9\d{2})x(1\d{3}\|9\d{2})q\d0\.jpg_\.(?:heic\|webp) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:525` | `^https?:\/\/app\.peopleapp\.com\/Api\/\d+/HomeApi\/(?:adv\|getAdvertImage) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:53` | `^https?:\/\/(gw\|heic)\.alicdn\.com\/mt\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:54` | `^https?:\/\/(gw\|heic)\.alicdn\.com\/t(?:f\|p)s\/.+\d{3,4}-\d{4} - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:540` | `^https?:\/\/appactive\.1234567\.com\.cn\/AppoperationApi\/OperationService\/GetAppStartImg - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:557` | `^https?:\/\/appdmkj\.5idream\.net\/appPic\/homepage - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:563` | `^https?:\/\/appmedia\.springairlines\.com\/cmsstatic\/.*\.gif - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:567` | `^https?:\/\/appuser-static\.huolala\.cn\/imgs - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:578` | `^https?:\/\/atrace\.chelaile\.net\.cn\/exhibit\?&adv_image - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:58` | `^https?:\/\/(img\|hwimg)\.beingfine\.cn\/(?:float_button\|card) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:584` | `^https?:\/\/b\.appsimg\.com\/upload\/momin - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:588` | `^https?:\/\/bbs-api-static\.miyoushe\.com\/search\/api\/search\/pre_keyword\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:603` | `^https?:\/\/bla\.gtimg\.com\/qqlive\/\d{6}.+?\.png - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:604` | `^https?:\/\/blog\.nilbt\.com\/static\/api\/update - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:608` | `^https?:\/\/business\.msstatic\.com\/advertiser - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:611` | `^https?:\/\/c\.zhangle\.com\/pic\/mktg\/diversity\/.+\.jpg$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:614` | `^https?:\/\/capi\.douyucdn\.cn\/api\/ios_app\/check_update - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:615` | `^https?:\/\/capi\.douyucdn\.cn\/api\/v1\/getStartSend?client_sys=ios - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:616` | `^https?:\/\/capi\.douyucdn\.cn\/lapi\/sign\/app(api)?\/getinfo\?client_sys=ios - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:628` | `^https?:\/\/cdn-evone-ceph\.echargenet\.com\/gw-emas-cdn\/63c4e3b558bb610008969f89 - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:629` | `^https?:\/\/cdn1\.mbs\.boc\.cn\/ubas-mgateway-static\/images\/advertType\/\.+\.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:630` | `^https?:\/\/cdn1\.mbs\.boc\.cn\/ubas-mgateway-static\/images\/theme\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:631` | `^https?:\/\/cdn\.133\.cn\/md\/gtgj\/.+\/.+720x1280 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:632` | `^https?:\/\/cdn\.\w{3}\.chelaileapp\.cn\/(api\/)?adpub - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:633` | `^https?:\/\/cdn\.api\.fotoable\.com\/Advertise\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:634` | `^https?:\/\/cdn\.cmgadx\.com\/sdk\/pool\/\w+\.json - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:635` | `^https?:\/\/cdn\.cmgadx\.com\/sdk\/pool\/m8uTS50pt3DC0Xd6\.json - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:636` | `^https?:\/\/cdn\.sdb\.com\.cn\/app_com\/adversdk - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:637` | `^https?:\/\/cdn\.sdb\.com\.cn\/widget\/magic-module-sprite\/dialog-normal - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:638` | `^https?:\/\/cdn\.sdb\.com\.cn\/widget\/magic-module-sprite\/general-banner - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:639` | `^https?:\/\/cdn\.sdb\.com\.cn\/widget\/nps\/feedback\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:640` | `^https?:\/\/cdn\.sdb\.com\.cn\/widget\/pb\/pb-plugins-rec-content-list - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:642` | `^https?:\/\/cdn\.sdb\.com\.cn\/widget\/pb\/pb-plugins-recomend-content - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:643` | `^https?:\/\/cdn\.wtzw\.com\/bookimg\/free\/api\/v\d\/reader\/reader-copy-paragraph-all\.json - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:645` | `^https?:\/\/cdnfile1\.msstatic\.com\/cdnfile\/appad\/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:648` | `^https?:\/\/cheyouapi\.ycapp\.yiche\.com\/appforum\/getusermessagecount - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:651` | `^https?:\/\/ci\.xiaohongshu\.com\/system_config\/watermark - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:677` | `^https?:\/\/conf-darwin\.xycdn\.com - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:683` | `^https?:\/\/cube\.elemecdn\.com\/[\w\/]+\.jpeg\?x-oss-process=image\/resize,m_fill,w_1\d{3},h_2\d{3}\/format,webp\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:684` | `^https?:\/\/cube\.elemecdn\.com\/[\w\/]+\.jpeg\?x-oss-process=image\/resize,m_fill,w_6\d{2},h_8\d{2}\/format,webp\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:685` | `^https?:\/\/cube\.elemecdn\.com\/[\w\/]+\.jpeg\?x-oss-process=image\/resize,m_fill,w_\d{3},h_\d{4}\/format,webp\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:686` | `^https?:\/\/cube\.elemecdn\.com\/\w\/\w{2}\/\w+mp4\.mp4\? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:698` | `^https?:\/\/dapis\.mting\.info\/yyting\/advertclient\/ClientAdvertList\.action - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:715` | `^https?:\/\/discuz\.gtimg\.cn\/cloud\/scripts\/discuz_tips - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:725` | `^https?:\/\/douyucdn\.cn\/.+\/appapi\/getinfo - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:731` | `^https?:\/\/du\.hupucdn\.com\/\w+h\d{4} - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:735` | `^https?:\/\/e-static\.aia\.com\.cn\/kyh\/resourcefolder\/ads - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:753` | `^https?:\/\/editor\.sm\.cn\/launch_picture - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:755` | `^https?:\/\/elemecdn\.com\/.+\/sitemap - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:763` | `^https?:\/\/ext-svc\.xiaopeng\.com\/api\/log\/open\/get\/image - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:775` | `^https?:\/\/fm\.fenqile\.com\/routev2\/other\/getfloatAd\.json - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:776` | `^https?:\/\/fm\.fenqile\.com\/routev2\/other\/startImg\.json - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:782` | `^https?:\/\/fscdn\.zto\.com\/fs1 - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:783` | `^https?:\/\/fuss10\.elemecdn\.com\/.+?\.mp4 - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:784` | `^https?:\/\/fuss10\.elemecdn\.com\/.+\/w\/(640\|750)\/h\/\d{3,4} - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:79` | `^https?:\/\/(nr-op\|cube)\.elemecdn\.com\/.+\.jpeg\?x-oss-process=image\/resize,m_fill,w_\d{4,},h_\d{4,}\/($\|format,webp\/$) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:795` | `^https?:\/\/g\.alicdn\.com\/(?:alilog\|trace) - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:796` | `^https?:\/\/ga-album-cdnqn\.52tt\.com\/prod-yunying\/.+.jpg - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:817` | `^https?:\/\/gateway\.shouqiev\.com(:\d+)?\/fsda\/app\/(?:bootImage\|loadPic\|appBannerList) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:824` | `^https?:\/\/go\.babytree\.com\/go_pregnancy\/api\/cms_second_tab\/topic_tab_list - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:857` | `^https?:\/\/gzacshow\.kugou\.com\/mfanxing-home\/cdn\/room\/index\/list_v2 - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:858` | `^https?:\/\/gzacshow\.kugou\.com\/mfx-rt-show\/cdn\/mo\/show\/headline - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:867` | `^https?:\/\/hera-webapp\.fenbi\.com\/(iphone\|ipad)\/topic\/hotquery\/list\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:877` | `^https?:\/\/hui\.sohu\.com\/predownload2\/? - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:883` | `^https?:\/\/hwimg\.beingfine\.cn\/(?:card\|Channel) - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:886` | `^https?:\/\/i\d\.hoopchina\.com\.cn\/blogfile\/.+_\d{3}x\d{4} - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:895` | `^https?:\/\/image\.suning\.cn\/uimg\/ma\/ad\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:896` | `^https?:\/\/imagepc\.ctaiot\.com\/dlabel\/0\/startpage - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:897` | `^https?:\/\/images\.cib\.com\.cn\/commons\/uploads\/commons\/[a-zA-Z0-9]{32}\.jpg\?ver=20221[1-2]{1} - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:898` | `^https?:\/\/images\.cib\.com\.cn\/commons\/uploads\/commons\/[a-zA-Z0-9]{32}\.jpg\?ver=20230[1-9]{1} - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:908` | `^https?:\/\/img-tailor\.11222\.cn\/cms\/upload\/img\/.+ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:909` | `^https?:\/\/img-tailor\.11222\.cn\/pm\/app\/.+\.gif - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:910` | `^https?:\/\/img0[1-9]{1}\.benlailife\.com\/AppHomePageImage\/upload\/files\/.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:911` | `^https?:\/\/img0[1-9]{1}\.luckincoffeecdn\.com\/group\d/M00/[A-Z0-9]{2}/[A-Z0-9]{2}/[a-zA-Z0-9]{29}\.(?:jpg\|jpeg)_\.webp - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:912` | `^https?:\/\/img1.126.net\/.+dpi=\w{7,8} - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:913` | `^https?:\/\/img1.126.net\/channel14\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:914` | `^https?:\/\/img\.admobile\.top\/admobile-adRequest\/.*.(?:jpg\|png) - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:915` | `^https?:\/\/img\.jiemian\.com\/ads\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:920` | `^https?:\/\/img\.wukongtv\.com\/wkremote\/AD\/iOS\/.*.(jpg\|png\|jpeg) - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:921` | `^https?:\/\/img\.yun\.01zhuanche\.com\/statics\/app\/advertisement\/.+?-750-1334 - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:922` | `^https?:\/\/img\d+\.10101111cdn\.com\/adpos\/ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:923` | `^https?:\/\/imgcache\.qq\.com\/qqlive\/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:924` | `^https?:\/\/imgx\.jampp\.com\/imgsrv\/tn - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:926` | `^https?:\/\/interface3?\.music\.163\.com/eapi/(ad\|abtest\|sp\|hot\|store\|mlog\|search/(specialkeyword\|defaultkeyword\|hot)) - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:962` | `^https?:\/\/kano\.guahao\.cn\/.+?\?resize=\d{3}-\d{4} - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:969` | `^https?:\/\/l[0-9]{1}\.51fanli\.net\/app\/images\/splash\/2022\/0[4-9]{1}\/.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:970` | `^https?:\/\/l[0-9]{1}\.51fanli\.net\/app\/images\/splash\/2022\/1[0-2]{1}\/.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:971` | `^https?:\/\/l[0-9]{1}\.51fanli\.net\/app\/images\/splash\/202\d{1}\/\d{2}\/.*.jpg - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:974` | `^https?:\/\/lchttpapi\.xczim\.com\/1\.1\/functions\/getLaunchImageForIOS - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:99` | `^https?:\/\/.+?\.58cdn\.com\.cn\/brandads\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:999` | `^https?:\/\/m.360buyimg\.com\/mobilecms\/s1125x2436_jfs\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/aggressive-ads.list:92` | `DOMAIN,baichuan-sdk.alicdn.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/aggressive-ads.list:94` | `DOMAIN,nbsdk-baichuan.alicdn.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/app-clean.list:11` | `DOMAIN,ads.mojicdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/app-clean.list:3` | `DOMAIN,ad-h5-cdn.soulapp.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/app-clean.list:30` | `DOMAIN,splashimgretrybssdl.cloud.kugou.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/app-clean.list:4` | `DOMAIN,ad-h5-station-cdn.soulapp.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/qingrex-miniapp-app-ad.list:126` | `DOMAIN,business.msstatic.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/qingrex-miniapp-app-ad.list:57` | `DOMAIN,acdn.adnxs.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/qingrex-miniapp-app-ad.list:73` | `DOMAIN,a.cpic.com.cn,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/qingrex-miniapp-app-ad.list:76` | `DOMAIN,adsmind.gdtimg.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/qingrex-miniapp-app-ad.list:81` | `DOMAIN,pgdt.gtimg.cn,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:100` | `DOMAIN,nbsdk-baichuan.alicdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:101` | `DOMAIN,ossgw.alicdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:103` | `DOMAIN,pp-cdnfile2pcdn.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:11` | `DOMAIN,adx-api.zdmimg.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:28` | `DOMAIN,cd-1.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:29` | `DOMAIN,cdl-1.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:3` | `DOMAIN,ad-cdn.qingting.fm,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:30` | `DOMAIN,cdl-p2.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:41` | `DOMAIN,ddfs-public.ddimg.mobi,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:65` | `DOMAIN,hudong.alicdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:66` | `DOMAIN,huyafile.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:75` | `DOMAIN,imgad0.pcauto.com.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:76` | `DOMAIN,imgad0.pconline.com.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:8` | `DOMAIN,admusicpic.music.126.net,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:84` | `DOMAIN,livewebbs2.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/reject.list:85` | `DOMAIN,livewebbs2pcdn.msstatic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:19` | `DOMAIN,adsmind.gdtimg.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:20` | `DOMAIN,adsmind.ugdtimg.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:29` | `DOMAIN,cdn-ad.wtzw.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:30` | `DOMAIN,cdn-new-ad.wtzw.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:35` | `DOMAIN,img.auction-ads.wpscdn.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:88` | `DOMAIN-SUFFIX,ad.xmcdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:89` | `DOMAIN-SUFFIX,adse.xmcdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:90` | `DOMAIN-SUFFIX,adsebs.xmcdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:91` | `DOMAIN-SUFFIX,ads.xmcdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:92` | `DOMAIN-SUFFIX,adse.wsa.xmcdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/web-ads.list:93` | `DOMAIN-SUFFIX,adsebs.wsa.xmcdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/wechat-ad.list:16` | `DOMAIN-SUFFIX,adsmind.gdtimg.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/wechat-ad.list:29` | `DOMAIN-SUFFIX,adsmind.apdcdn.tc.qq.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN | `Rules/wechat-ad.list:9` | `DOMAIN-SUFFIX,pgdt.gtimg.cn,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / HTTPDNS / DNS | `Rewrite/Sources/URL-Rewrite.conf:644` | `^https?:\/\/cdn\.wup\.huya\.com\/launch\/queryHttpDns$ - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / HTTPDNS / DNS | `Rules/qingrex-miniapp-app-ad.list:128` | `URL-REGEX,"^http:\/\/cdn\.wup\.huya\.com\/launch\/queryHttpDns$",REJECT,extended-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:11` | `^https://aiqicha\.baidu\.com/app/getHotTopicAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:9` | `^https://aiqicha\.baidu\.com/app/bannerPicAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/Apps/amap.conf:10` | `DOMAIN,free-aos-cdn-image.amap.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/Apps/meituan.conf:27` | `^https?:\/\/wmapi\.meituan\.com\/api\/v\d+\/(?:loadInfo\|openscreen\|startpicture) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/Apps/robo-taxi.conf:10` | `^https://idgdata\.baidu\.com/operation/api/announce/screen/image_manage\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/Rule.conf:79` | `DOMAIN,free-aos-cdn-image.amap.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1197` | `^https?:\/\/p\d\.meituan\.net\/(\d+\.\d+\.\d+\/)?wmbanner\/(?!fb51b9d\|4e9d3c4).+\.gif - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1200` | `^https?:\/\/p\d\.meituan\.net\/movie\/.+?\.jpg\?may_covertWebp - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1201` | `^https?:\/\/p\d\.meituan\.net\/nrpresourcevenus\/\w+\.gif - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1202` | `^https?:\/\/p\d\.meituan\.net\/travelcube\/(?!1d4a663\|52e9bfc\|29a6227\|412c4ac\|6ee35c4\|13bf0bf\|ab8692e\|6858b1d).+@100w_100h - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1203` | `^https?:\/\/p\d\.meituan\.net\/travelcube\/(?!c129a661)\w+\.gif - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1222` | `^https?:\/\/peisongapi\.meituan\.com\/client\/getInitiateImage - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1287` | `^https?:\/\/s3plus\.meituan\.net\/v\d\/mss_\w+\/goku\/(?:lottie\|lucency) - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1377` | `^https?:\/\/t\d{2}\.baidu\.com - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1450` | `^https?:\/\/wmapi\.meituan\.com\/api\/v\d+\/(?:loadInfo\|openscreen\|startpicture) - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:1452` | `^https?:\/\/www.baidu.com\/?action=static&ms=1&version=css_page_2@0.*? - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:148` | `^https?:\/\/[\s\S]*\.baidu\.com/.*?ad[xs]\.php - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:205` | `^https?:\/\/afd\.baidu\.com\/afd\/entry - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:210` | `^https?:\/\/aiqicha\.baidu\.com\/app\/bannerPicAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:214` | `^https?:\/\/aiqicha\.baidu\.com\/app\/getHotTopicAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:80` | `^https?:\/\/(s3plus\|flowplus)\.meituan\.net\/v\d\/\w+\/linglong\/.+\.(?:gif\|jpg\|mp4) - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:890` | `^https?:\/\/idgdata\.baidu\.com\/operation\/api\/announce\/screen\/image_manage\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:916` | `^https?:\/\/img\.meituan\.net\/(adunion\|display\|midas)\/.+\.(gif\|jpg)\.webp$ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:917` | `^https?:\/\/img\.meituan\.net\/bizad - reject` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:918` | `^https?:\/\/img\.meituan\.net\/groceryimages\/\w+\.gif - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:919` | `^https?:\/\/img\.meituan\.net\/groceryimages\/\w+\.png@220w_220h_1e_1l - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:942` | `^https?:\/\/issuecdn\.baidupcs\.com\/issue\/netdisk\/guanggao\/ - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rules/qingrex-miniapp-app-ad.list:49` | `DOMAIN,metrics-picture.d.meituan.net,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 图片 / 静态 CDN / 国内 App 核心 API | `Rules/reject.list:51` | `DOMAIN,free-aos-cdn-image.amap.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/123-net-work-disk.conf:9` | `^https://www\.123pan\.com/api/config/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/17173-game.conf:10` | `DOMAIN-SUFFIX,cvda.17173.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/17173-game.conf:12` | `DOMAIN-SUFFIX,vda.17173.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/178-game.conf:10` | `DOMAIN-SUFFIX,tuiguang.178.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/178-game.conf:9` | `DOMAIN-SUFFIX,market.178.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/18183-game.conf:10` | `DOMAIN-SUFFIX,eezdx.erc.18183.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/18183-game.conf:11` | `DOMAIN-SUFFIX,zpe.klre.18183.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/1905-movie-network.conf:11` | `DOMAIN-SUFFIX,afp.m1905.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/1905-movie-network.conf:12` | `DOMAIN-SUFFIX,counter.m1905.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-weather-king.conf:9` | `^http?://tianqi\.2345\.com/api/content/getContentFeeds\.php - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:11` | `DOMAIN-SUFFIX,ggcode.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:12` | `DOMAIN-SUFFIX,houtai.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:13` | `DOMAIN-SUFFIX,jifen.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:14` | `DOMAIN-SUFFIX,minipage.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:15` | `DOMAIN-SUFFIX,wan.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:16` | `DOMAIN-SUFFIX,zhushou.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:17` | `DOMAIN-SUFFIX,tg.jifen.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:18` | `DOMAIN-SUFFIX,update.minipage.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:19` | `DOMAIN-SUFFIX,g.wan.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2345-web-navigation.conf:9` | `DOMAIN-SUFFIX,dl.2345.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2bulu.conf:10` | `^https://helper\.2bulu\.com/promote/getAppUserModule\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2bulu.conf:11` | `^https://helper\.2bulu\.com/proSpecial/allData\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/2bulu.conf:9` | `^https://helper\.2bulu\.com/search/searchHotKeyList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/36-kr.conf:14` | `^https://gateway\.36kr\.com/api/mis/nav/me/recom\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/36-kr.conf:15` | `^https://gateway\.36kr\.com/api/mis/nav/search/hotword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/36-kr.conf:18` | `^https://gateway\.36kr\.com/api/mis/page/article/recom\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/36-kr.conf:19` | `^https://gateway\.36kr\.com/api/mis/page/newsflash/recom\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/36-kr.conf:20` | `^https://gateway\.36kr\.com/api/mis/sys/skin/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/39-health.conf:10` | `DOMAIN-SUFFIX,d.39.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/39-health.conf:11` | `DOMAIN-SUFFIX,dpvc.39.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/39-health.conf:12` | `DOMAIN-SUFFIX,thetestpage.39.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/39-health.conf:9` | `DOMAIN-SUFFIX,app-g.39.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/51-cto.conf:10` | `DOMAIN-SUFFIX,gg2.51cto.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/51-cto.conf:11` | `DOMAIN-SUFFIX,gg3.51cto.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/51-cto.conf:9` | `DOMAIN-SUFFIX,gg.51cto.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/51-job.conf:10` | `^https://cupid\.51jobapp\.com/open/operation/get/latest/banner-list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/51-job.conf:11` | `^https://cupid\.51jobapp\.com/open/51job-activities/secJob/queryHomeSecondConfigV2\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/51-job.conf:14` | `^https://cupid\.51jobapp\.com/open/resume/strategy/resume-build\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/51-job.conf:9` | `^https://appapi\.51jobapp\.com/api/market/get_launch\.php\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-auto.conf:10` | `DOMAIN-SUFFIX,imp.xgo.com.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-auto.conf:9` | `DOMAIN-SUFFIX,58.xgo.com.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:11` | `DOMAIN-SUFFIX,58mingri.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:12` | `DOMAIN-SUFFIX,58mingtian.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:13` | `DOMAIN-SUFFIX,sc.58mingtian.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:18` | `DOMAIN-SUFFIX,brandshow.58.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:19` | `DOMAIN-SUFFIX,jing.58.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:20` | `DOMAIN-SUFFIX,jumpluna.58.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:21` | `DOMAIN-SUFFIX,news.58.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:24` | `DOMAIN-SUFFIX,zzpush.58.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/58-tong-cheng.conf:25` | `DOMAIN-SUFFIX,jump.luna.58.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/91160.conf:11` | `^https://snsapi\.91160\.com/vipmemberapi/mbCombo/mbComboWords\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/91160.conf:12` | `^https://patientgate\.91160\.com/rec/homepage/open/getUserGoodsList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/91160.conf:13` | `^https://snsapi\.91160\.com/hotword/open/v1/getSearchExplore\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/91160.conf:14` | `^https://snsapi\.91160\.com/hotword/open/v1/getHotWordPlate\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/91160.conf:15` | `^https://snsapi\.91160\.com/engine/backgroundWord/queryForFrontend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/91160.conf:9` | `^https://msglb\.91160\.com/msg/outer/broker/get$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/acfun.conf:10` | `^https?://api-new\.app\.acfun\.cn/rest/app/flash/screen/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ai-mei-ju.conf:10` | `^https?://api\.bjxkhc\.com/index\.php/app/ios/pay/ok$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ai-mei-ju.conf:9` | `^https?://api\.bjxkhc\.com/index\.php/app/ios/ver/index_ios$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ai-pai.conf:10` | `DOMAIN-SUFFIX,atiws.aipai.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ai-pai.conf:9` | `DOMAIN-SUFFIX,apas.aipai.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ai-yue-shu-xiang.conf:9` | `^https?://icc\.one/iFreeTime/xid32uxaoecnfv2/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ali-yun-drive.conf:12` | `^https://member\.alipan\.com/v2/activity/sign_in_luckyBottle - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ali-yun-drive.conf:9` | `IP-CIDR,203.107.1.1/24,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/all-football.conf:12` | `^https?://ap\.dongqiudi\.com/plat/v - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/aol.conf:10` | `DOMAIN-SUFFIX,dynamic.aol.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/aol.conf:11` | `DOMAIN-SUFFIX,free.aol.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:10` | `^https://(a\.athm\.cn/)?mobile\.app\.autohome\.com\.cn/platform/carserver/carcard/mycardv6 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:11` | `^https://(a\.athm\.cn/)?mobile\.app\.autohome\.com\.cn/platform/carserver/usercenter/chat/gse/recquery - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:12` | `^https://autoapi\.autohome\.com\.cn/ypttd/yjc/web/mkgt/act/seckillInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:13` | `^https://(a\.athm\.cn/)?mobile\.app\.autohome\.com\.cn/platform/carserver/usercenter/gethotactcards - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:14` | `^https://(a\.athm\.cn/)?mobile\.app\.autohome\.com\.cn/platform/carserver/carcard/extendedcards - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:15` | `^https://(a\.athm\.cn/)?mobile\.app\.autohome\.com\.cn/platform/carserver/usercenter/getwashcarlist - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:16` | `^https://(a\.athm\.cn/)?mobile\.app\.autohome\.com\.cn/platform/carserver/usercenter/getdealertab - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:17` | `^https://(a\.athm\.cn/)?mobile\.app\.autohome\.com\.cn/platform/carserver/usercenter/getoillist - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:18` | `^https://pcmx\.autohome\.com\.cn/queryCreativeList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:19` | `^https://maam\.pingan\.com\.cn/maam/buoy/getBuoyList\.do - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:20` | `^https://news\.app\.autohome\.com\.cn/cont_v\d+(?:\.\d+){2}/api/article/extenddata - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:23` | `^https://dealer\.m\.autohome\.com\.cn/handler/other/getdata\?__action=super\.list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:24` | `^https://autoapi\.autohome\.com\.cn/arvr-dealercloud-api/online/aggregation/exhibitionList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:25` | `^https://dealer\.m\.autohome\.com\.cn/handler/other/getdata\?__action=vrcore\.list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:26` | `^https://dealer\.m\.autohome\.com\.cn/handler/other/getdata\?__action=platform\.search - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:27` | `^https://a\.athm\.cn/clientlive\.api\.autohome\.com\.cn/api/live/getserieswindowsinfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/auto-home.conf:9` | `^https://(a\.athm\.cn/)?mobile\.app\.autohome\.com\.cn/platform/carserver/carcard/findEquitysV5 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baby-tree-parenting.conf:10` | `^https?://plough\.babytree\.com/plough\.do - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baby-tree-parenting.conf:11` | `^https?://mapiweb\.babytree\.com/newapi/luban/behavior/receive - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baby-tree-parenting.conf:12` | `^https?://go\.babytree\.com/go_pregnancy/api/index_activity/get_app_index_activity - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baby-tree-parenting.conf:13` | `^https?://go\.babytree\.com/go_tool/api/feeding_record/get_home_banner_info - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baby-tree.conf:10` | `URL-REGEX,"^http:\/\/go\.babytree\.com\/go_search\/api\/mobile_search_new\/get_multi_search_default_keywords\?",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baby-tree.conf:13` | `URL-REGEX,"^http:\/\/plough\.babytree\.com\/plough\.do",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baby-tree.conf:9` | `URL-REGEX,"^http:\/\/go\.babytree\.com\/go_pregnancy\/api\/(index_activity\/get_app_index_activity\|sign\/sign_h_5)\?",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baixing.conf:10` | `DOMAIN-SUFFIX,tu.baixing.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baixing.conf:12` | `DOMAIN-SUFFIX,bd-js.baixing.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baixing.conf:13` | `DOMAIN-SUFFIX,bd-s.baixing.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baixing.conf:14` | `DOMAIN-SUFFIX,script-bd.baixing.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bao-mi-hua.conf:10` | `DOMAIN-SUFFIX,djs.baomihua.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bao-mi-hua.conf:11` | `DOMAIN-SUFFIX,resource.baomihua.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bao-mi-hua.conf:9` | `DOMAIN-SUFFIX,a.baomihua.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:11` | `DOMAIN-SUFFIX,midinfo.baofeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:12` | `DOMAIN-SUFFIX,p2pmid.baofeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:13` | `DOMAIN-SUFFIX,data.danmu.baofeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:14` | `DOMAIN-SUFFIX,co.dtech.baofeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:26` | `DOMAIN-SUFFIX,breeze.olclient.baofeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:27` | `DOMAIN-SUFFIX,coop.pop.baofeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:32` | `DOMAIN-SUFFIX,config.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:33` | `DOMAIN-SUFFIX,houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:36` | `DOMAIN-SUFFIX,onlinetips.baofeng5.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:37` | `DOMAIN-SUFFIX,app.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:38` | `DOMAIN-SUFFIX,ck.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:39` | `DOMAIN-SUFFIX,corner.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:40` | `DOMAIN-SUFFIX,d3f.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:41` | `DOMAIN-SUFFIX,mid.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:42` | `DOMAIN-SUFFIX,parser.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:43` | `DOMAIN-SUFFIX,wbwl.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:44` | `DOMAIN-SUFFIX,web.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:45` | `DOMAIN-SUFFIX,wl.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:46` | `DOMAIN-SUFFIX,wx.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:47` | `DOMAIN-SUFFIX,xs.houyi.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:51` | `DOMAIN-SUFFIX,rec.moviebox.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:53` | `DOMAIN-SUFFIX,jfm4.pop.baofeng.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/baofeng-player.conf:9` | `DOMAIN-SUFFIX,active.baofeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bbc.conf:9` | `DOMAIN-SUFFIX,visualscience.external.bbc.co.uk,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/beike.conf:10` | `^https://apps\.api\.ke\.com/platform/shellapp/userCenter/feed\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/beike.conf:11` | `^https://apps\.api\.ke\.com/config/config/getactivityconfig\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/beike.conf:9` | `^https://apps\.api\.ke\.com/config/config/bootpage\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/betty-kitchen.conf:9` | `^https?://channel\.beitaichufang\.com/channel/api/v\d/promote/ios/start/page - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:10` | `^https://manga\.bilibili\.com/twirp/comic\.v\d\.Comic/GetBubbles - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:11` | `^https://manga\.bilibili\.com/twirp/comic\.v\d\.Comic/GetCommonBanner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:12` | `^https://manga\.bilibili\.com/twirp/comic\.v\d\.Comic/SearchBanner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:13` | `^https://manga\.bilibili\.com/twirp/user\.v\d\.SeasonV\d/GetSeasonInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:14` | `^https://manga\.bilibili\.com/twirp/bookshelf\.v\d\.Bookshelf/ListEmptyRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:15` | `^https://manga\.bilibili\.com/twirp/bookshelf\.v\d\.Bookshelf/NovelRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:16` | `^https://manga\.bilibili\.com/twirp/novel\.v\d\.Novel/MoreRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:17` | `^https://manga\.bilibili\.com/twirp/comic\.v\d\.Comic/AppInit - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:18` | `^https://manga\.bilibili\.com/twirp/comic\.v\d\.Comic/ListFlash - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili-comic.conf:9` | `^https://manga\.bilibili\.com/twirp/comic\.v\d\.Comic/GetActivityTab - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili.conf:12` | `DOMAIN,t-dsp.pinduoduo.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili.conf:20` | `DOMAIN,dsp-x.jd.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili.conf:22` | `DOMAIN,jzt.jd.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili.conf:23` | `DOMAIN,kepler.jd.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili.conf:24` | `DOMAIN,keplerapi.jd.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili.conf:34` | `DOMAIN,cm.bilibili.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili.conf:35` | `DOMAIN,cm.bilibili.net,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bilibili.conf:38` | `DOMAIN,impression.biligame.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bing.conf:10` | `DOMAIN-SUFFIX,c.bing.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bing.conf:9` | `DOMAIN-SUFFIX,bat.bing.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/biquge.conf:10` | `DOMAIN-SUFFIX,m.biquge5200.cc,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/biquge.conf:11` | `DOMAIN-SUFFIX,tt.biquge.la,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/biquge.conf:9` | `DOMAIN-SUFFIX,j.biquge520.cc,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bitqiu-pan.conf:10` | `^http://pan-api\.bitqiu\.com/activity/getUrlList$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bitqiu-pan.conf:11` | `^https://pan-api\.bitqiu\.com/activity/guides$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bitqiu-pan.conf:9` | `^https://pan-api\.bitqiu\.com/activity/getPromoteGuide$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/blued.conf:9` | `^https?://social\.blued\.cn/users/recommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bo-luo-bao-light-novel.conf:9` | `^https?://api\.sfacg\.com/ioscfg - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:10` | `^https://bd-api\.kuwo\.cn/api/service/banner/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:11` | `^https://bd-api\.kuwo\.cn/api/ucenter/vip/give/config\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:12` | `^https://bd-api\.kuwo\.cn/api/service/home/module\?.*&moduleId=6 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:13` | `^https://bd-api\.kuwo\.cn/api/pay/vip/lowPriceText\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:14` | `^https://bd-api\.kuwo\.cn/api/service/global/config/vipEnter\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:15` | `^https://bd-api\.kuwo\.cn/api/popup/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:16` | `^https://bd-api\.kuwo\.cn/api/pay/vip/invitation/swell/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:17` | `^https://bd-api\.kuwo\.cn/api/service/version/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:18` | `^https://bd-api\.kuwo\.cn/api/pay/vip/invitation/assist/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/bodian-music.conf:19` | `^https://bd-api\.kuwo\.cn/api/pay/h5/common/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/boo-hee.conf:10` | `^https://api\.boohee\.com/meta-interface/v1/index/tool_buttons\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/boo-hee.conf:11` | `^https://api\.boohee\.com/app-interface/v1/search/search\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/boo-hee.conf:13` | `^https://bohe\.sfo-tx-shanghai-01\.saas\.sensorsdata\.cn/api/v2/sfo/user_popup_configs\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/boo-hee.conf:14` | `^https://api\.boohee\.com/meta-interface/v1/index/sensor-banners\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/boo-hee.conf:9` | `^https://api\.boohee\.com/meta-interface/v1/index/page_float_bubbles\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cainiao.conf:9` | `^https:\/\/nbcps-mtop\.cainiao\.com\/gw\/mtop\.cainiao\.nbcps\.presentation\.fetch\.cn - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/caixin-media.conf:12` | `^https://gg\.caixin\.com/s\?z=caixin&slot=\d+ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/caixin-media.conf:13` | `^https://msgapi\.caixin\.com/msg_api/annmsg/annlist - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/caixin-media.conf:9` | `^https://entities\.caixin\.com/api/(dataplus/promotionHints\|public/push/appIndex\|public/recommendNews) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/caiyun-weather.conf:11` | `DOMAIN,gather.colorfulclouds.net,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/caiyun-weather.conf:9` | `DOMAIN,abyss.cyapi.cn,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/camera360.conf:11` | `DOMAIN,exp.360in.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/camera360.conf:9` | `DOMAIN,dispatcher.360in.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cat-ear-fm.conf:10` | `^https://app\.missevan\.com/x/recommend/get-popup$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cat-ear-fm.conf:11` | `^https://fm\.missevan\.com/api/v2/meta/banner$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cat-ear-fm.conf:12` | `^https://fm\.missevan\.com/api/v2/recommended/top\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cat-ear-fm.conf:13` | `^https://fm\.missevan\.com/api/v2/chatroom/sound/recommend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cclive.conf:11` | `^https://appapi\.cc\.163\.com/v\d/mixfloatingwindow/floating_windows\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cclive.conf:12` | `^http://api\.cc\.163\.com/v1/mpopuprecommend/exit_room_conf$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:10` | `^https://api\.cece\.com/ask/ai_chat/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:11` | `^https://api\.cece\.com/user/popup/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:12` | `^https://api\.cece\.com/chart/easter_egg/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:13` | `^https://api\.cece\.com/user/register_task/notice_task\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:14` | `^https://api\.cece\.com/ask/ask/alert_minus\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:16` | `^https://api\.cece\.com/user/user/myPageBanner\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:17` | `^https://api\.cece\.com/live/recommend/new_user\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:18` | `^https://api\.cece\.com/chart/tools/get_search_recommend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:19` | `^https://api\.cece\.com/user/rank/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:20` | `^https://api\.cece\.com/chart/config/chart_activity\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cece.conf:9` | `^https://api\.cece\.com/user/index/banners\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/chao-ji-ke-cheng-biao.conf:9` | `^https?://182\.92\.244\.70/d/json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/chao-xing-xue-xi-tong.conf:9` | `^https?://learn\.chaoxing\.com/apis/service/appConfig\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/che-lai-le.conf:9` | `DOMAIN-SUFFIX,atrace.chelaile.net.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cheng-fen-miao.conf:10` | `^https://app\.chengfenmiao\.com/helper/VersionCheck\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cheng-fen-miao.conf:11` | `^https://app\.chengfenmiao\.com/item/closet\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cheng-fen-miao.conf:12` | `^https://app\.chengfenmiao\.com/Helper/HotWords\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cheng-fen-miao.conf:9` | `^https://app\.chengfenmiao\.com/Listing/LiveHots\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/chuzhan.conf:10` | `^https://app\.huashi6\.com/app/works/relative$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/chuzhan.conf:11` | `^https://app\.huashi6\.com/app/index/follow/all_random/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/chuzhan.conf:12` | `^https://app\.huashi6\.com/app/index/csyxh/icon$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ci-wei-mao-yue-du.conf:9` | `^https?://app\.hbooker\.com/setting/get_startpage_url_list - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cnn.conf:10` | `DOMAIN-SUFFIX,gdyn.cnn.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cnn.conf:11` | `DOMAIN-SUFFIX,metrics.cnn.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cnn.conf:12` | `DOMAIN-SUFFIX,cnn.dyn.cnn.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cnn.conf:13` | `DOMAIN-SUFFIX,i.l.cnn.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/cool-apk.conf:9` | `^https://api\.coolapk\.com/v6/search\?.*type=hotSearch - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/csdn.conf:10` | `DOMAIN-SUFFIX,counter.csdn.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/csdn.conf:11` | `DOMAIN-SUFFIX,dc.csdn.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/csdn.conf:12` | `DOMAIN-SUFFIX,dc2.csdn.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/csdn.conf:17` | `^https?://app-gw\.csdn\.net/abtesting/v2/getList? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/csg.conf:10` | `^https://95598\.csg\.cn/mp/mpaas/rubik/openapi/rubik/mobile/getRubikScene$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/csg.conf:9` | `^https://95598\.csg\.cn/mp/ucs/ma/zt/content/queryHotInformations$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/da-shi-xiong.conf:11` | `^https?://sdk\.alibaba\.com\.ailbaba\.me/xgapp\.php/v\d/top_notice\? - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/da-shi-xiong.conf:9` | `^https?://sdk\.alibaba\.com\.ailbaba\.me/xgapp\.php/v\d/version - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/damai.conf:10` | `^https://acs\.m\.taobao\.com/gw/mtop\.damai\.mec\.popup\.get/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/damai.conf:9` | `^https://acs\.m\.taobao\.com/gw/mtop\.damai\.wireless\.home\.welcome/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dang-dang-reading.conf:10` | `^https?://e\.dangdang\.com/.+?getDeviceStartPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dang-dang-reading.conf:11` | `^https?://api\.dangdang\.com/mapi\d/mobile/init - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dang-dang-reading.conf:12` | `^https?://mapi\.dangdang\.com/index\.php\?action=init - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dang-dang-reading.conf:9` | `^https?://e\.dangdang\.com/media/api.+\?action=getDeviceStartPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dang-dang.conf:10` | `DOMAIN-SUFFIX,schprompt.dangdang.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dang-dang.conf:11` | `DOMAIN-SUFFIX,t.dangdang.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dang-dang.conf:9` | `DOMAIN-SUFFIX,a.dangdang.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dewu.conf:10` | `^https://app\.dewu\.com/hacking-newbie/v1/app/coupon/module\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dewu.conf:11` | `^https://app\.dewu\.com/api/v1/app/search/lexicon/v3/background_words\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dewu.conf:12` | `^https://app\.dewu\.com/api/v1/app/search/lexicon/v1/rank_words\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dewu.conf:13` | `^https://app\.dewu\.com/sns-rec/v1/attention/feed\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dewu.conf:14` | `^https://app\.dewu\.com/sns-rec/v1/search/word-skip/new-list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dewu.conf:15` | `^https://app\.dewu\.com/sns-rec/v1/search/hotword-list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:10` | `AND,((IP-ASN,45090,no-resolve),(DEST-PORT,25641),(PROTOCOL,TCP)),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:11` | `AND,((IP-ASN,55990,no-resolve),(DEST-PORT,25641),(PROTOCOL,TCP)),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:12` | `AND,((IP-ASN,63646,no-resolve),(DEST-PORT,25641),(PROTOCOL,TCP)),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:15` | `^https://res\.xiaojukeji\.com/resapi/activity/mget - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:16` | `^https://lion\.didialift\.com/broker/\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:17` | `^https://conf\.diditaxi\.com\.cn/homepage/v1/other/slow\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:18` | `^https://ct\.xiaojukeji\.com/agent/v3/feeds\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:19` | `^https://conf\.diditaxi\.com\.cn/dynamic/conf - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:20` | `^https://poi\.map\.xiaojukeji\.com/mapapi/recommend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/di-di.conf:9` | `DOMAIN,gwp.xiaojukeji.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/didi.conf:10` | `AND,((IP-ASN,45090,no-resolve),(DEST-PORT,25641),(PROTOCOL,TCP)),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/didi.conf:11` | `AND,((IP-ASN,55990,no-resolve),(DEST-PORT,25641),(PROTOCOL,TCP)),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/didi.conf:12` | `AND,((IP-ASN,63646,no-resolve),(DEST-PORT,25641),(PROTOCOL,TCP)),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/didi.conf:9` | `DOMAIN,gwp.xiaojukeji.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/digital-heartbeat.conf:10` | `^https://api-changzheng\.chinaath\.com/changzheng-content-center-api/api/global/search/hotSearch/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/digital-heartbeat.conf:9` | `^https://api-changzheng\.chinaath\.com/changzheng-basic-center-api/api/appConfigBanner/listBannerRelease\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ding-xiang-doctor.conf:9` | `^https?://dxy\.com/app/i/ask/biz/feed/launch - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ding-xiang-yuan.conf:9` | `^https?://dq\.dxy\.cn/api\.php\?action=getpostbanners - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:14` | `^https?://119\.29\.29\.\d+/d - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:18` | `^https://maicai\.api\.ddxq\.mobi/homeApi/marketingNotice\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:19` | `^https://maicai\.api\.ddxq\.mobi/search/rollHotKeyword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:20` | `^https://maicai\.api\.ddxq\.mobi/search/rankingList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:21` | `^https://maicai\.api\.ddxq\.mobi/search/hotKeyword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:22` | `^https://maicai\.api\.ddxq\.mobi/order/getRecommend$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:23` | `^https://maicai\.api\.ddxq\.mobi/homeApi/userLike\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:24` | `^https://user\.api\.ddxq\.mobi/userportal-service/api/v1/user/queryMyPage/\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dingdong-maicai.conf:25` | `^https://maicai\.api\.ddxq\.mobi/guide-service/userLike/flowData$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dlabel-cloud-tag.conf:10` | `^https://dudian-oss\.oss-cn-shenzhen\.aliyuncs\.com/dlabel/1/startpage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dong-hua-feng.conf:9` | `^https?://api\.gamer\.com\.tw/mobile_app/anime/v\d/anime_get_question\.php - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dou-ban.conf:11` | `^https://m\.douban\.com/rexxar/api/v\d/market/products/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dou-ban.conf:13` | `^https://frodo\.douban\.com/api/v\d/home_banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dou-ban.conf:14` | `^https://frodo\.douban\.com/api/v\d/search/found_words - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/douyin.conf:11` | `DOMAIN,grandpaniu-douyin-disabled.invalid,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/douyu.conf:11` | `AND,((DEST-PORT,18000),(PROTOCOL,STUN)),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/douyu.conf:13` | `DOMAIN,stun1.qvb.qcloud.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dragon-read.conf:10` | `DOMAIN,zlink.ugsdk.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dragon-read.conf:11` | `DOMAIN,mon.toutiaocloud.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dragon-read.conf:14` | `DOMAIN,mon11-misc-lq.fqnovel.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dragon-read.conf:15` | `DOMAIN,mon11-misc.fqnovel.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dragon-read.conf:16` | `DOMAIN,mon3-misc.fqnovel.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dragon-read.conf:19` | `DOMAIN,mon.toutiaocloud.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dreame.conf:10` | `^https://cn-mall\.dreame\.tech/dreame-mall/api/v1/tag/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dreame.conf:11` | `^https://cn-wxmall\.dreame\.tech/main/goods/get-topgoods$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dui-tang.conf:10` | `^https://api-2\.duitang\.com/napi/vienna/daren/daren/recommend/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/dui-tang.conf:11` | `^https://www\.duitang\.com/napi/hot/search/list/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/eastday.conf:10` | `DOMAIN-SUFFIX,jiaoben.eastday.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/eastday.conf:11` | `DOMAIN-SUFFIX,mini.eastday.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/eastday.conf:12` | `DOMAIN-SUFFIX,tt123.eastday.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/eastday.conf:13` | `DOMAIN-SUFFIX,tt321.eastday.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ecovacs-home.conf:10` | `^https://gl-cn-api\.ecovacs\.cn/v1/private/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/etouch-ecalendar.conf:13` | `^https://client-lz\.rili\.cn/lizhi/api/fortune/question_spots/panel\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/etouch-ecalendar.conf:14` | `^https://client-lz\.rili\.cn/lizhi/api/jujia/flow\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/etouch-ecalendar.conf:15` | `^https://client-lz\.rili\.cn/lizhi/api/album/hl_card\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/etouch-ecalendar.conf:16` | `^https://client-lz\.rili\.cn/lizhi/api/fortune/overview\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/facebook.conf:10` | `DOMAIN-SUFFIX,atdmt.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/facebook.conf:9` | `DOMAIN-SUFFIX,facebookma.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-deng-reading.conf:9` | `^https?://gateway-api\.dushu365\.com/chief-orch/config/config/v100/appConfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:10` | `DOMAIN,dig.bdurl.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:11` | `DOMAIN,activity-ag.awemeughun.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:12` | `DOMAIN,v6-novelapp.ixigua.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:13` | `DOMAIN-SUFFIX,novelapp.ixigua.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:14` | `DOMAIN-SUFFIX,default.ixigua.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:16` | `DOMAIN-SUFFIX,byteorge.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:17` | `IP-CIDR,49.71.37.101/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:18` | `IP-CIDR,117.71.105.23/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:19` | `IP-CIDR,218.94.207.205/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:20` | `IP-CIDR,117.92.229.188/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:21` | `IP-CIDR,101.36.166.16/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:22` | `IP-CIDR,180.96.2.114/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:30` | `^https?://gurd\.snssdk\.com/src/server/v3/package - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fan-qie-novel.conf:9` | `DOMAIN,ug-sinfonlinea.bytedance.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fc-box.conf:10` | `^https://consumer\.fcbox\.com/fcboxactivityweb/api/v\d/clientPage/jinGangFirst\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fc-box.conf:11` | `^https://consumer\.fcbox\.com/v2/home/mallInfo$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fc-box.conf:13` | `^https://consumer\.fcbox\.com/hs-portal/app/config/page/home/v2\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fc-box.conf:14` | `^https://consumer\.fcbox\.com/post/suggestion/query$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fc-box.conf:15` | `^https://consumer\.fcbox\.com/fcboxactivityweb/marketingEntrance/retentionPopup$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fc-box.conf:16` | `^https://consumer\.fcbox\.com/fcboxactivityweb/api/clientPopup/v\d/queryPopupWithPriority$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fc-box.conf:17` | `^https://consumer\.fcbox\.com/fcboxactivityweb/api/guidePopup/popup$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fc-box.conf:9` | `^https://consumer\.fcbox\.com/fcboxactivityweb/api/v\d/clientPage/modulesAggregated\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fei-ke-cha-guan.conf:9` | `^https?://ptf\.flyertrip\.com/common/cf/.*.jpg - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/fen-bi.conf:12` | `^https://keapi\.fenbi\.com/app/iphone/\w+/reddot\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ferris-wheel.conf:10` | `^https://appapi\.motianlun\.cn/showapi/pub/site/\d+/banner/app\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ferris-wheel.conf:11` | `^https://appapi\.motianlun\.cn/userdataapi/pub/v\d/top/keywords\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ferris-wheel.conf:12` | `^https://appapi\.motianlun\.cn/buyerapi/buyer/v\d/search/index\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ferris-wheel.conf:13` | `^https://appapi\.motianlun\.cn/showapi/site/\d+/transfer/recentShows\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/finance-news.conf:10` | `^https://api-one-wscn\.awtmt\.com/apiv1/kvconfig/items/search_keywords_wscnvip$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/finance-news.conf:11` | `^https://api-one-wscn\.awtmt\.com/apiv1/search/hotsearch\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/finance-news.conf:12` | `^https://api-one-wscn\.awtmt\.com/apiv1/content/articles/hot\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/finance-news.conf:13` | `^https://wallstreetcn\.com/app-faas/coupon/user/search/popup$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/finance-news.conf:14` | `^https://api-one-wscn\.awtmt\.com/apiv1/content/lives/relateddata/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/finance-news.conf:15` | `^https://api-one-wscn\.awtmt\.com/apiv1/content/articles/relateddata/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/finance-news.conf:16` | `^https://api-one-wscn\.awtmt\.com/apiv1/content/carousel/information-flow\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/flea-market.conf:10` | `^https://acs\.m\.goofish\.com/gw/mtop\.taobao\.idle\.user\.strategy\.list/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/flea-market.conf:11` | `^https://acs\.m\.goofish\.com/gw/mtop\.taobao\.idle\.item\.recommend\.list/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/flea-market.conf:12` | `^https://acs\.m\.goofish\.com/gw/mtop\.taobao\.idle\.local\.near\.by\.corner\.info/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/flea-market.conf:13` | `^https://acs\.m\.goofish\.com/gw/mtop\.taobao\.idle\.item\.buy\.feeds/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/flea-market.conf:15` | `^https://acs\.m\.goofish\.com/gw/mtop\.taobao\.idle\.playboy\.recommend/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/flyer-tea.conf:10` | `^https://www\.flyert\.com\.cn/api/mobile/index\.php\?module=vip_coupon - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/flyer-tea.conf:12` | `^https://www\.flyert\.com\.cn/api/mobile/index\.php\?module=getdata - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/foodie.conf:11` | `DOMAIN,popup-api.b612kaji.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/funshion.conf:13` | `DOMAIN-SUFFIX,conf.funshion.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/funshion.conf:14` | `DOMAIN-SUFFIX,pub.funshion.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/funshion.conf:15` | `DOMAIN-SUFFIX,vas.funshion.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/funshion.conf:16` | `DOMAIN-SUFFIX,vs.funshion.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/funshion.conf:17` | `DOMAIN-SUFFIX,aa0.pub.funshion.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/funshion.conf:18` | `DOMAIN-SUFFIX,aa1.pub.funshion.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/funshion.conf:19` | `DOMAIN-SUFFIX,rt.funshion.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/funshion.conf:9` | `DOMAIN-SUFFIX,pb.funshion.net.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ganji.conf:10` | `DOMAIN-SUFFIX,wuliao.ganji.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ganji.conf:12` | `DOMAIN-SUFFIX,ganjituiguang.ganji.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ganji.conf:13` | `DOMAIN-SUFFIX,sta.ganji.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ganji.conf:9` | `DOMAIN-SUFFIX,jiaoben.ganji.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/gao-ding.conf:11` | `^https://www\.gaoding\.com/api/v\d/cp/search-words/v2/placeholder - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/go-com.conf:12` | `DOMAIN-SUFFIX,w88.go.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/go-com.conf:13` | `DOMAIN-SUFFIX,verdict.abc.go.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/go-com.conf:14` | `DOMAIN-SUFFIX,oascentral.abclocal.go.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/guide-rank.conf:11` | `^https://zone\.guiderank-app\.com/guiderank-web/app/common/getWeworkCategoryPromotionInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/guide-rank.conf:12` | `^https://zone\.guiderank-app\.com/guiderank-web/app/stockTaking/pageStockTakingForHomePage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/guide-rank.conf:13` | `^https://zone\.guiderank-app\.com/guiderank-web/app/specialSale/pageRecommendedItems - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/guide-rank.conf:14` | `^https://zone\.guiderank-app\.com/guiderank-web/app/manualOperationGoods/pageManualOperationGoods - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/guide-rank.conf:15` | `^https://zone\.guiderank-app\.com/guiderank-web/app/specialSale/listSpecialSalePageBanner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/guide-rank.conf:16` | `^https://zone\.guiderank-app\.com/guiderank-web/app/personal/getPersonPageInfo\.do - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/guide-rank.conf:9` | `^https://zone\.guiderank-app\.com/guiderank-web/app/common/getWeworkPromotionInfoBySceneType - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hanju-tv.conf:10` | `^https?://api\.hanju\.koudaibaobao\.com/api/carp/kp\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hanting-hotels.conf:10` | `^https://hweb-hotel\.huazhu\.com/home/getHomeLoinBanner$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hanting-hotels.conf:11` | `^https://hweb-hotel\.huazhu\.com//home/querySelectHotel$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hanting-hotels.conf:12` | `^https://hweb-hotel\.huazhu\.com/home/queryHotelBrand$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hanting-hotels.conf:9` | `^https://hweb-manager\.huazhu\.com/notice/getAppPopupNotifyAlert$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hao-hao-zhu.conf:9` | `^https?://api\.haohaozhu\.cn/index\.php/home/AppInit/getStartPhoto - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hao123.conf:10` | `DOMAIN-SUFFIX,1.hao123.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hao123.conf:11` | `DOMAIN-SUFFIX,mini.hao123.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hao123.conf:9` | `DOMAIN-SUFFIX,hao123rt.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/heartide-brain-wave.conf:13` | `^https://api\.psy-1\.com/cosleep/home/activity\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/heartide-brain-wave.conf:16` | `^https://api\.psy-1\.com/cosleep/search/config\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/heartide-brain-wave.conf:17` | `^https://api\.psy-1\.com/cosleep/newborn/search/ranks\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/heartide-brain-wave.conf:18` | `^https://api\.psy-1\.com/cosleep/search/inputs\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/heartide-brain-wave.conf:19` | `^https://api\.psy-1\.com/cosleep/newborn/sleeps/guides/banner\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/heartide-brain-wave.conf:20` | `^https://api\.psy-1\.com/cosleep/newborn/search/ranks/items\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/heartide-brain-wave.conf:9` | `^https://api\.psy-1\.com/cosleep/startup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hkdou-yin.conf:11` | `DOMAIN,grandpaniu-hkdouyin-disabled.invalid,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/huang-you-xiang-ji.conf:11` | `DOMAIN-SUFFIX,mob.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/huang-you-xiang-ji.conf:9` | `DOMAIN-SUFFIX,anythinktech.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hujiang-online-school.conf:9` | `DOMAIN-SUFFIX,mc.hujiang.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hupu.conf:10` | `^https://bbs\.mobileapi\.hupu\.com/\d/\d\.\d\.\d+/(bbsallapi/tag/v1/heatTag\|bbsrankapi/v1/rating/list) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hupu.conf:11` | `^https://games\.mobileapi\.hupu\.com/\d/\d\.\d\.\d+/search/v2/(hintkeylist\|hotkeylist) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hupu.conf:14` | `^https://fairy\.mobileapi\.hupu\.com/gallery/getmod2 - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hupu.conf:15` | `^https://games\.mobileapi\.hupu\.com/3/8\.0\.86/bplcommentapi/bpl/score_tab/groups - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hupu.conf:16` | `^https://games\.mobileapi\.hupu\.com/3/8\.0\.86/bplapi/banner/getLocationBanners - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/hupu.conf:9` | `^https://games\.mobileapi\.hupu\.com/\d/\d\.\d\.\d+/bplapi/reddot/v1/app/getReddot - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/huxiu.conf:13` | `^https://api-web-feed\.huxiu\.com/v1/index/recommendContentsNew$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/huxiu.conf:14` | `^https://api-search\.huxiu\.com/api/searchIndex$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/huxiu.conf:15` | `^https://api-article\.huxiu\.com/v2/article/getTextArticleRelated$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/huxiu.conf:16` | `^https://api-web-moment\.huxiu\.com/v3/moment/getDetailRecdArticle$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/i-mai-cai.conf:15` | `^https://businessapi\.ksedt\.com/signupindex/jxlist - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/i-qi-yi-video.conf:10` | `IP-CIDR,111.63.147.158/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/i-qi-yi-video.conf:11` | `IP-CIDR,116.211.198.237/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/i-qi-yi-video.conf:9` | `IP-CIDR,103.44.59.54/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/i-reader-dejian.conf:16` | `^https://dj\.palmestore\.com/zybk/api/bookshelf/index\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ithome.conf:10` | `^https?:\/\/dat\.ruanmei\.com\/ithome\/money\/acd\.json$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jd.conf:9` | `URL-REGEX,"^http:\/\/\w{32}\.jddebug\.com\/diagnose\?",REJECT,extended-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jdwaimai.conf:10` | `^https://color\.jddj\.com/client\.action\?functionId=search_recommendRanking$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jdwaimai.conf:9` | `^https://color\.jddj\.com/client\.action\?functionId=uniformRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ji-he-wang.conf:9` | `^https?://www\.gcores\.com/gapi/v1/app-start-pages\?page - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-kao-bao-dian.conf:10` | `^https://cheyouquan\.kakamobi\.com/api/open/group/recommend-subscribe-tag\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-kao-bao-dian.conf:11` | `^https://swallow\.kakamobi\.cn/api/open/config/get-config\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-kao-bao-dian.conf:12` | `^https://monkey\.kakamobi\.cn/api/open/live/get-recommend-live-protocol\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-kao-bao-dian.conf:14` | `^https://mcbd\.maiche\.com/api/open/v3/user/get-popup-window\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-kao-bao-dian.conf:15` | `^https://jiakao-misc\.kakamobi\.cn/api/open/my-tab-config/selection-list\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-kao-bao-dian.conf:16` | `^https://jiakao-misc\.kakamobi\.cn/api/open/my-tab-config/banner-list\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-kao-bao-dian.conf:17` | `^https://squirrel\.kakamobi\.cn/api/open/recommend-goods/get-my-page-banner\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-kao-bao-dian.conf:19` | `^https://monkey\.kakamobi\.cn/api/open/live-room/get-resource\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-xiao-drive.conf:10` | `^https://gouche\.ksedt\.com/config/popup/info$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-xiao-drive.conf:11` | `^https://richmanrules\.ksedt\.com/intellectWaterfallBidding/find$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-xiao-drive.conf:12` | `^https://op\.ksedt\.com/jxedtLive/liveIntroduceResource - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-xiao-drive.conf:13` | `^https://richmanrules\.ksedt\.com/intellectWaterfall/find$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-xiao-yi-dian-tong.conf:10` | `DOMAIN,richmanmain.jxedt.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-xiao-yi-dian-tong.conf:11` | `DOMAIN,richmanrules.jxedt.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-xiao-yi-dian-tong.conf:14` | `^https?://richmanrules\.ksedt\.com/intellectWaterfall(Bidding)?/find - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jia-xiao-yi-dian-tong.conf:9` | `DOMAIN,richmanapi.jxedt.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jump.conf:13` | `DOMAIN,qh-material.taobao.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/jump.conf:9` | `DOMAIN,zlsdk.1rtb.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kan-tian-xia.conf:10` | `^https?://open3\.vistastory\.com/v\d/api.*get_popup - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kebida-dushu.conf:11` | `^https?://g[a-z0-9-]+\.dushu365\.com/fs-retain/trialVip/v\d+/requestTrialVipPopDoNotSendReward - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kebida-dushu.conf:12` | `^https?://g[a-z0-9-]+\.dushu365\.com/resource-orchestration-system/vipLandingPage/v\d+/getVipLandingPageApp - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kebida-dushu.conf:13` | `^https?://g[a-z0-9-]+\.dushu365\.com/fandeng-orch/dual2211/config - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kebida-dushu.conf:14` | `^https?://g[a-z0-9-]+\.dushu365\.com/fdtalk-orch/newcomerzone/v\d+/guide - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kebida-dushu.conf:15` | `^https?://g[a-z0-9-]+\.dushu365\.com/fandeng-orch/bookboy/v\d+/vipPagePop - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kebida-dushu.conf:16` | `^https?://g[a-z0-9-]+\.dushu365\.com/chief-orch/config/config/v\d+/appConfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kebida-dushu.conf:17` | `^https?://g[a-z0-9-]+\.dushu365\.com/order-orchestration/orderWeb/exchange/v100/showExchangeButton - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kebida-dushu.conf:9` | `^https?://popup\.dushu365\.com/api/v2/sfo/(user_)?popup_(config\|display)s - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kgring.conf:9` | `^http://api\.ring\.kugou\.com/user/notice/recommend$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kingdee-my-money.conf:10` | `^https://yunmk\.feidee\.net/cab-market-ws/market/v2/contents$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kingdee-my-money.conf:12` | `^https://api\.feidee\.net/v1/configs/client/configs - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kingsoft-power-word.conf:11` | `DOMAIN,counter.kingsoft.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kingsoft-power-word.conf:12` | `DOMAIN,counter.ksosoft.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kingsoft-power-word.conf:13` | `DOMAIN,minfo.wps.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kingsoft-power-word.conf:15` | `DOMAIN,ups.ksmobile.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kingsoft-power-word.conf:16` | `DOMAIN,ws.ksmobile.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kingsoft-power-word.conf:23` | `^https?://.+?\.kingsoft-office-service\.com - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kook.conf:10` | `^https://www\.kookapp\.cn/api/v3/promotion/ongoing$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:12` | `DOMAIN,g.koowo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:18` | `DOMAIN-KEYWORD,searchrecommend.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:19` | `DOMAIN-KEYWORD,nbcollectretry.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:20` | `DOMAIN-KEYWORD,rtmretry.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:21` | `DOMAIN-KEYWORD,rt-m.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:22` | `DOMAIN-KEYWORD,nbcollect.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:33` | `DOMAIN-SUFFIX,oth.eve.mdt.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:34` | `DOMAIN-SUFFIX,channel.fanxing.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:35` | `DOMAIN-SUFFIX,d.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:36` | `DOMAIN-SUFFIX,downmobile.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:38` | `DOMAIN-SUFFIX,game.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:39` | `DOMAIN-SUFFIX,gamebox.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:40` | `DOMAIN-SUFFIX,gcapi.sy.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:41` | `DOMAIN-SUFFIX,gg.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:42` | `DOMAIN-SUFFIX,install.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:43` | `DOMAIN-SUFFIX,install2.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:44` | `DOMAIN-SUFFIX,minidcsc.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:45` | `DOMAIN-SUFFIX,mo.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:46` | `DOMAIN-SUFFIX,msg.mobile.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:48` | `DOMAIN-SUFFIX,p.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:49` | `DOMAIN-SUFFIX,push.mobile.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:50` | `DOMAIN-SUFFIX,rtmonitor.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:51` | `DOMAIN-SUFFIX,sdn.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:52` | `DOMAIN-SUFFIX,song.fanxing.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:53` | `DOMAIN-SUFFIX,update.mobile.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-music.conf:54` | `DOMAIN-SUFFIX,youxi.kugou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-youth.conf:13` | `^https://gateway\.kugou\.com/youth/v1/experiment/get_params\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-youth.conf:14` | `^https://gateway\.kugou\.com/youth/api/user/v1/init\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-youth.conf:15` | `^https://gateway\.kugou\.com/youth/v2/activity/task_list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-youth.conf:16` | `^https://gateway\.kugou\.com/youth/v1/channel/tab_list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou-youth.conf:17` | `^https://gateway\.kugou\.com/goddess/v1/content/biz_list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou.conf:24` | `^https://gateway(retry)?\.kugou\.com/v\d/feeds/follow_feed_fallback - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou.conf:25` | `^https://gateway(retry)?\.kugou\.com/mstc/musicsymbol/v\d/system/profile - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou.conf:26` | `^https://gateway(retry)?\.kugou\.com/searchnofocus/v\d/search_no_focus_word - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou.conf:28` | `^https://gateway(retry)?\.kugou\.com/singerdiscuss/v\d/entrance/comment - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou.conf:30` | `^https://gateway(retry)?\.kugou\.com/ocean/v\d/sound/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou.conf:33` | `^https://m1fxgroup\.kugou\.com/fxsing/yqc/alongInfo/getUserAlongInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou.conf:34` | `^https://hwstore\.kugou\.com/v\d/get_store_data - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku-gou.conf:35` | `^https://ep\.kugou\.com/v\d/album_shop/get_entrance_info - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku6.conf:11` | `DOMAIN-SUFFIX,pvdata.ku6.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ku6.conf:9` | `DOMAIN-SUFFIX,st.vq.ku6.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kua-ya-zip.conf:9` | `DOMAIN-SUFFIX,kuaizip.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-di100.conf:10` | `^https?://p\.kuaidi100\.com/e-commerce/act/actInfo\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-dong-baike.conf:9` | `DOMAIN-SUFFIX,ehd.baike.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-dui-zuo-ye.conf:13` | `^https://www\.kuaiduizuoye\.com/activity/init/checkappconfig$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-dui-zuo-ye.conf:14` | `^https://www\.kuaiduizuoye\.com/kdapi/conf/appbannersv3$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-dui-zuo-ye.conf:15` | `^https://www\.kuaiduizuoye\.com/kdapi/conf/initbanner$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-dui-zuo-ye.conf:16` | `^https://apivip\.kuaiduizuoye\.com/viponline/scancode/mycard$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-kan-comic.conf:10` | `DOMAIN,ipv6.kkmh.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-kan-comic.conf:11` | `DOMAIN,ipv4.kkmh.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-kan-comic.conf:26` | `^https://h5\.kuaikanmanhua\.com/v\d/kb/recharge_good/list_h5 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-kan-comic.conf:29` | `^https://h5\.kuaikanmanhua\.com/game-h5/new-user-welfare/index\.html - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-le-guang-bo.conf:13` | `DOMAIN,pin.hpplay.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-le-guang-bo.conf:14` | `DOMAIN,rp.hpplay.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-le-guang-bo.conf:15` | `DOMAIN,rpt.hpplay.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-shou.conf:10` | `^https://(apissl\|az\d-api(-js\|-idc)?)\.(gifshow\|ksapisrv)\.com/rest/n/taskCenter/task/report\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-shou.conf:12` | `^https://(apissl\|az\d-api(-js\|-idc)?)\.(gifshow\|ksapisrv)\.com/rest/n/live/feed/info/simplelive/card\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuai-shou.conf:9` | `^https://(apissl\|az\d-api(-js\|-idc)?)\.(gifshow\|ksapisrv)\.com/rest/n/nearby/widget/info\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuaishou.conf:15` | `^https://az2-api\.ksapisrv\.com/rest/n/taskCenter/task/report\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuaishou.conf:9` | `DOMAIN-SUFFIX,e.kuaishou.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuro-bbs.conf:10` | `^https://api\.kurobbs\.com/config/index/windows$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuro-bbs.conf:11` | `^https://api\.kurobbs\.com/config/search/getSearchConfig\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuro-bbs.conf:9` | `^https://api\.kurobbs\.com/config/getOpenScreen$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:10` | `URL-REGEX,"^http:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/user\/freeMode\/",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:12` | `URL-REGEX,"^http:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/app\/startup\/config",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:13` | `URL-REGEX,"^http:\/\/rich\.kuwo\.cn\/EcomResourceServer\/",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:14` | `IP-CIDR,111.206.98.63/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:16` | `URL-REGEX,"^http:\/\/searchrecterm\.kuwo\.cn\/recterm\.s",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:18` | `URL-REGEX,"^http:\/\/wapi\.kuwo\.cn\/openapi\/v\d\/app\/newMenuList\/menuListInfo",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:20` | `URL-REGEX,"^http:\/\/vip\d\.kuwo\.cn\/vip\/v\d\/sysinfo\?op=getRePayAndDoPayBox",REJECT-DICT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:25` | `^https://vip\d\.kuwo\.cn/commercia/vipconf/projectPage/getPageContent - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:26` | `^https://tingshu\.kuwo\.cn/v2/api/pay/user/info - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kuwo.conf:27` | `^https://appi\.kuwo\.cn/kuwopay/personal/cells - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kwai-videoeditor.conf:10` | `^https://api\.kmovie\.gifshow\.com/rest/n/kmovie/app/banner/common/getBannerByType\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kwai-videoeditor.conf:12` | `^https://api\.kmovie\.gifshow\.com/rest/n/kmovie/app/resource/activity/pendant\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/kwai-videoeditor.conf:9` | `^https://api\.kmovie\.gifshow\.com/rest/n/kmovie/app/resource/get\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lai-dian.conf:9` | `^https?://mobile-api\.imlaidian\.com/api/args - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lan-jie100.conf:9` | `^https?://tagit\.hyhuo\.com/recover/list - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lan-ren-ting-shu.conf:12` | `^https?://display\.wting\.info/.*.jpeg - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-bo-screen-cast.conf:11` | `DOMAIN-SUFFIX,rp.hpplay.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:10` | `DOMAIN-SUFFIX,webp2p.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:11` | `DOMAIN-SUFFIX,ark.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:12` | `DOMAIN-SUFFIX,dc.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:13` | `DOMAIN-SUFFIX,fz.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:14` | `DOMAIN-SUFFIX,g3.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:15` | `DOMAIN-SUFFIX,minisite.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:16` | `DOMAIN-SUFFIX,pro.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:18` | `DOMAIN-SUFFIX,pro.hoye.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:19` | `DOMAIN-SUFFIX,msg.m.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:21` | `DOMAIN-SUFFIX,n.mark.letv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:22` | `DOMAIN-SUFFIX,1.letvlive.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:23` | `DOMAIN-SUFFIX,2.letvlive.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:24` | `DOMAIN-SUFFIX,api.game.letvstore.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:25` | `DOMAIN-SUFFIX,api.push.le.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:26` | `DOMAIN-SUFFIX,cn.api.push.le.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:27` | `DOMAIN-SUFFIX,guang.lesports.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/le-eco.conf:9` | `DOMAIN,emma-414870e223.huodonghezi.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/leju.conf:10` | `DOMAIN-SUFFIX,src.leju.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lie-pin.conf:10` | `^https?://api-wanda\.liepin\.com/api/com\.liepin\.cbp\.baizhong\.op\.v2-show-4app - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:12` | `URL-REGEX,"^https:\/\/a\.line\.me\/oa\/v\d\/e$",REJECT-DROP` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:13` | `URL-REGEX,"^https:\/\/a\.line\.me\/cs\/v\d\/oa$",REJECT-DROP` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:16` | `URL-REGEX,"^https:\/\/crs-event\.line\.me\/v\d\/imp",REJECT-DROP` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:18` | `URL-REGEX,"^https:\/\/uts-front\.line-apps\.com\/event$",REJECT-DROP` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:19` | `URL-REGEX,"^https:\/\/uts-front\.line-apps\.com\/settings$",REJECT-DROP` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:37` | `^https://gw\.line\.naver\.jp/tr/event$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:39` | `^https://legy\.line-apps\.com:443/ext/smartch/banner/sch/v\d$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:40` | `^https://legy\.line-apps\.com/line\.gcs\.GcsModuleService/GetModulesByModuleIds$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:41` | `^https://legy\.line-apps\.com:443/tr/event$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:42` | `^https://lan\.line\.me/v\d/line/ios - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:43` | `^https://buy\.line\.me/api/graphql\?variables - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:44` | `^https://nelo2-col\.linecorp\.com/_store$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/line.conf:45` | `^https://cix\.line-apps\.com/R\d\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/live-lab.conf:10` | `^https://api\.livelab\.com\.cn/search/appHotWords/app/queryHotWords$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/live-lab.conf:11` | `^https://api\.livelab\.com\.cn/appShow/hotSearch/app/rankList$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/live-lab.conf:12` | `^https://api\.livelab\.com\.cn/appShow/app/homepage/banners\?bannerModuleId=(82\|84\|53) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lol-bible.conf:10` | `^https://mlol\.qt\.qq\.com/go/club/match/get_ai_search_words$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lol-bible.conf:11` | `^https://mlol\.qt\.qq\.com/go/mlol_news/search/varcache_hotV\d\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lol-bible.conf:12` | `^https://mlol\.qt\.qq\.com/go/customize_search/article_rank_tab\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lol-bible.conf:13` | `^https://mlol\.qt\.qq\.com/go/customize_search/article_rank\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lol-bible.conf:14` | `^https://mlol\.qt\.qq\.com/go/zone/bottomtab_tip\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lol-bible.conf:9` | `^https://mlol\.qt\.qq\.com/go/recommend/platstrongshell\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/luckin-coffee.conf:10` | `^https://capi\.lkcoffee\.com/resource/m/promotion/giftCard/topPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/luckin-coffee.conf:11` | `^https://capi\.lkcoffee\.com/resource/m/sys/base/myLittleLuck - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/luckin-coffee.conf:12` | `^https://capi\.lkcoffee\.com/resource/core/v2/menu/ordinaryUserLayeredArea - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/luckin-coffee.conf:13` | `^https://capi\.lkcoffee\.com/resource/m/sys/common/modules - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/luckin-coffee.conf:14` | `^https://capi\.lkcoffee\.com/resource/core/v2/homepage/homePageCoffeeList - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/luckin-coffee.conf:15` | `^https://capi\.lkcoffee\.com/resource/m/eorder/product/popAppTagProductList - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/luckin-coffee.conf:9` | `^https://capi\.lkcoffee\.com/resource/m/growUp/calendarList - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lv-tu-sui-shen-ting.conf:9` | `^https?://www\.1314zhilv\.com/ltsstnew/(guideScenic/getRecentlyUpdatedScenic\|city/getWeatherByCityName) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:10` | `DOMAIN-SUFFIX,cm8.lycos.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:11` | `DOMAIN-SUFFIX,oascentral.lycos.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:12` | `DOMAIN-SUFFIX,ratings.lycos.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:13` | `DOMAIN-SUFFIX,client.sidesearch.lycos.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:14` | `DOMAIN-SUFFIX,install.sidesearch.lycos.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:15` | `DOMAIN-SUFFIX,guestworld.tripod.lycos.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:16` | `DOMAIN-SUFFIX,titan.guestworld.tripod.lycos.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:17` | `DOMAIN-SUFFIX,fe.lea.lycos.co.uk,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/lycos.conf:18` | `DOMAIN-SUFFIX,hit.webcentre.lycos.co.uk,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/ma-feng-wo.conf:12` | `^https://mapi\.mafengwo\.cn/user/growth/get_growth_tip/v1\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mac-keeper.conf:11` | `DOMAIN-SUFFIX,event.mackeeper.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mac-keeper.conf:12` | `DOMAIN-SUFFIX,mackeeperapp.mackeeper.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mac-keeper.conf:13` | `DOMAIN-SUFFIX,zryydi.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mac-keeper.conf:9` | `DOMAIN-SUFFIX,mackeeper.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mai-dui-dui.conf:10` | `^https?://t-dsp\.pinduoduo\.com - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mai-dui-dui.conf:12` | `^https?://sfo\.mddcloud\.com\.cn/api/v\d/sfo/popup_displays? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mai-dui-dui.conf:13` | `^https?://tower\.ubixioe\.com/mob/mediation - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mai-dui-dui.conf:16` | `^https?://sdk1xyajs\.data\.kuiniuca\.com - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mai-mai.conf:10` | `^https://(h3\.)?open\.taou\.com/maimai/pay/v5/check_gift\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mai-mai.conf:11` | `^https://(h3\.)?open\.taou\.com/maimai/go_gossip_darwin/external/v2/query_flow_cards\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mail-master.conf:10` | `^https://dashi\.163\.com/task-center-api/fapi/task/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mail-master.conf:11` | `^https://appconf\.mail\.163\.com/mailoperating/mailmaster/api/operator/get$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mail-master.conf:9` | `^https://appconf\.mail\.163\.com/mailmaster/api/http/urlConfig\.do$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meet-you.conf:10` | `DOMAIN,axxd.xmseeyouyima.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meet-you.conf:13` | `^https://circle\.(xm)?seeyouyima\.com/v\d/article_recommend\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meitu-myxj.conf:12` | `^https://api\.meiyan\.com/operation/home_banner\.json\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meitu-myxj.conf:13` | `^https://api\.meiyan\.com/vip/permission_update_popup\.json\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meituan.conf:7` | `DOMAIN,dynamicf.sankuai.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meituan.conf:9` | `DOMAIN,live-monitor-broker.sankuai.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meizhixiuxing.conf:10` | `^https://api\.bevol\.com/appmain/app/home/popup$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meizhixiuxing.conf:11` | `^https://api\.bevol\.com/personal/page$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meizhixiuxing.conf:12` | `^https://api\.bevol\.com/seach/foundAndTopSearch$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/meizhixiuxing.conf:9` | `^https://api\.bevol\.com/appmain/app/home/launch$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mi-ho-yo-bbs.conf:10` | `^https://bbs-api(-ab)?\.miyoushe\.com/apihub/api/getHotKeywordAndEvent$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mijia.conf:12` | `^https?://home\.mi\.com/cgi-op/api/v1/recommendation/(banner\|carousel/banners\|myTab\|openingBanner) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mijia.conf:13` | `^https?://home\.mi\.com/cgi-op/api/v1/resource/realtime/openingBanner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mix.conf:9` | `^https?://dispatcher\.camera360\.com/api/v\d/list$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/moji-weather.conf:9` | `^https:\/\/fcard\.api\.moji\.com\/flycard\/flyCard\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mop.conf:10` | `DOMAIN-SUFFIX,union.mop.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mop.conf:9` | `DOMAIN-SUFFIX,pub.mop.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mr-hema.conf:10` | `^https://acs-m\.freshippo\.com/gw/mtop\.wdk\.sg\.queryinnerpage/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mr-hema.conf:12` | `^https://acs-m\.freshippo\.com/gw/mtop\.wdk\.render\.querysearchpage/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mr-hema.conf:13` | `^https://acs-m\.freshippo\.com/gw/mtop\.wdk\.sg\.querysinglescene/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mr-hema.conf:14` | `^https://acs-m\.freshippo\.com/gw/mtop\.wdk\.melon\.collocation/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mr-hema.conf:15` | `^https://acs-m\.freshippo\.com/gw/mtop\.wdk\.fc\.recommend\.feedscommondservice/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/mr-hema.conf:9` | `^https://acs-m\.freshippo\.com/gw/mtop\.wdk\.render\.querysinglepage/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/narwel-robots.conf:10` | `^https://cn-app\.narwaltech\.com/operate/cactivity/listByResourceIds\?resourceIds=(user_center_banner\|index_banner) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/narwel-robots.conf:11` | `^https://store\.narwal\.com/mall/customPage/getByPageKeyword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/netease-news.conf:14` | `^https?://c\.m\.163\.com/nc/gl/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/netease-news.conf:18` | `^https?://support\.you\.163\.com/xhr/boot/getBootMedia\.json - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/new-relic.conf:10` | `DOMAIN-SUFFIX,js-agent.newrelic.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/new-relic.conf:11` | `DOMAIN-SUFFIX,bam.nr-data.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/new-relic.conf:9` | `DOMAIN-SUFFIX,newrelic.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/niu-ting-ting.conf:10` | `^https://ntt-app\.benewtech\.cn/v6/user/\d+/messages/event - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/niu-ting-ting.conf:9` | `^https://gateway\.benewtech\.cn/resources-app/app/startup/prepage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/omofun.conf:9` | `^https?://103\.91\.210\.141\:2515/xgapp\.php/v2/top_notice - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/on-the-way.conf:9` | `^https://www\.imxingzhe\.com/api/v1/pop/window/\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/oray-sunlogin.conf:9` | `^https://client-api-v2\.oray\.com/materials/SLCC_iOS_DEVICE_FREE\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/oupeng.conf:11` | `DOMAIN-SUFFIX,notify.oupeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/oupeng.conf:12` | `DOMAIN-SUFFIX,startup.oupeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/oupeng.conf:13` | `DOMAIN-SUFFIX,c.bxb.oupeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/oupeng.conf:14` | `DOMAIN-SUFFIX,r.bxb.oupeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/oupeng.conf:9` | `DOMAIN-SUFFIX,ezine.oupeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/outfit7.conf:10` | `DOMAIN-SUFFIX,apps2.outfit7.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/outfit7.conf:13` | `DOMAIN-SUFFIX,events-api.outfit7.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/outfit7.conf:9` | `DOMAIN-SUFFIX,apps.outfit7.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pangguai-life.conf:10` | `^https://userapi\.qiekj\.com/appTitle/get$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pangguai-life.conf:12` | `^https://userapi\.qiekj\.com/local-life/category$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pangguai-life.conf:13` | `^https://userapi\.qiekj\.com/integralGoods/queryIntegralGoodsPage$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pangguai-life.conf:14` | `^https://userapi\.qiekj\.com/task/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pangguai-life.conf:9` | `^https://userapi\.qiekj\.com/slot/get$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/perfect-world-esport.conf:9` | `^https://appactivity\.wmpvp\.com/hotsearch/all\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:11` | `DOMAIN-SUFFIX,exp.3g.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:13` | `DOMAIN-SUFFIX,dmpclick.deliver.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:14` | `DOMAIN-SUFFIX,dol.deliver.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:15` | `DOMAIN-SUFFIX,dolphin.deliver.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:16` | `DOMAIN-SUFFIX,ids.deliver.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:17` | `DOMAIN-SUFFIX,ids1.deliver.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:18` | `DOMAIN-SUFFIX,iis1.deliver.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:19` | `DOMAIN-SUFFIX,iis3g.deliver.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:20` | `DOMAIN-SUFFIX,mfp.deliver.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:21` | `DOMAIN-SUFFIX,api.iapps.ifeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/phoenix-new-media.conf:23` | `DOMAIN-SUFFIX,cz.ifeng0.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/photoable.conf:9` | `DOMAIN,regist.fotoable.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pi-pi-xia.conf:10` | `^https://api(5-lq)?\.pipix\.com/bds/banner/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pi-pi-xia.conf:11` | `^https://api(5-lq)?\.pipix\.com/bds/feed/follow_feed/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:10` | `AND,((URL-REGEX,"^http:\/\/\[[0-9a-fA-F:]+\]\/d(\d)?\?",extended-matching),(USER-AGENT,"*com.xunmeng.pinduoduo*")),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:12` | `DOMAIN,titan.pinduoduo.com,REJECT-NO-DROP,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:13` | `DOMAIN,xg.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:15` | `DOMAIN,titan.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:18` | `DOMAIN,apm.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:19` | `DOMAIN,th-b.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:20` | `DOMAIN,ta.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:21` | `DOMAIN,th.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:22` | `DOMAIN,th-a.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:23` | `DOMAIN,ta-a.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:24` | `DOMAIN,meta.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:25` | `DOMAIN,apm-a.pinduoduo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pinduoduo.conf:9` | `AND,((URL-REGEX,"^http:\/\/((25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\.){3}(25[0-5]\|2[0-4][0-9]\|[01]?[0-9][0-9]?)\/d(\d)?",extended-matching),(USER-AGENT,"*com.xunmeng.pinduoduo*")),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:12` | `DOMAIN,de.as.pptv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:13` | `DOMAIN-SUFFIX,afp.pplive.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:14` | `DOMAIN-SUFFIX,gas.data.pplive.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:15` | `DOMAIN-SUFFIX,plt.data.pplive.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:16` | `DOMAIN-SUFFIX,web.data.pplive.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:17` | `DOMAIN-SUFFIX,pp2.pptv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:19` | `DOMAIN-SUFFIX,app.aplus.pptv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:20` | `DOMAIN-SUFFIX,as.aplus.pptv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pptv.conf:21` | `DOMAIN-SUFFIX,jp.as.pptv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/pu-pu-mall.conf:10` | `^https://j1\.pupuapi\.com/client/marketing/banner/v7\?position_types=100 - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:12` | `^https://magev6\.if\.qidian\.com/argus/api/v1/checkin/simpleinfo\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:14` | `^https://magev6\.if\.qidian\.com/argus/api/v1/message/getpushedmessagelist$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:15` | `^https://magev6\.if\.qidian\.com/argus/api/v1/maintain/playstrip$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:16` | `^https://magev6\.if\.qidian\.com/argus/api/v1/dailyrecommend/recommendBook\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:17` | `^https://magev6\.if\.qidian\.com/argus/api/v1/freshman/bookshelfbtn$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:18` | `^https://magev6\.if\.qidian\.com/argus/api/v1/bookshelf/getTopOperation$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:19` | `^https://magev6\.if\.qidian\.com/argus/api/v1/booksearch/hotWords\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:20` | `^https://magev6\.if\.qidian\.com/argus/api/v1/followsubscribe/showChapterEndModule\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-dian.conf:21` | `^https://magev6\.if\.qidian\.com/argus/api/v1/young/getconf$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-shui-music.conf:10` | `^https://ether-pack\.pangolin-sdk-toutiao\.com/union/endcard/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-shui-music.conf:9` | `^https://webcast-open\.douyin\.com/webcast/openapi/feed/\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-xin-bao.conf:11` | `^https://appc-v6\.qixin\.com/v4/general/getAppBanners$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-xin-bao.conf:12` | `^https://appc-v6\.qixin\.com/v4/user/getUserActivitys$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-xin-bao.conf:13` | `^https://appc-v6\.qixin\.com/v4/enterprise/homePageRecommend/recommendCard\d+ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-xin-bao.conf:14` | `^https://appc-v6\.qixin\.com/v4/user/getRecommendPersons$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-xin-bao.conf:15` | `^https://appc-v6\.qixin\.com/v4/enterprise/getRecommendEnts$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-xin-bao.conf:16` | `^https://appc-v6\.qixin\.com/v4/enterprise/getRecommendation$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-xin-bao.conf:17` | `^https://appc-v6\.qixin\.com/v4/general/getAppBottomBanners$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qi-xin-bao.conf:9` | `^https://appc\.qixin\.com/v4/general/getSearchPlaceholderRedirect$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qilu.conf:10` | `DOMAIN-SUFFIX,g4.iqilu.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qilu.conf:9` | `DOMAIN-SUFFIX,g3.iqilu.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqbrowser.conf:9` | `^https?://us\.l\.qq\.com/exapp\?spsa=\d - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:12` | `DOMAIN,huatuocode.huatuo.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:15` | `DOMAIN,ios.bugly.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:22` | `DOMAIN,qzs.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:23` | `DOMAIN,rmonitor.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:24` | `DOMAIN,sdk.e.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:30` | `DOMAIN,tpns.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:34` | `DOMAIN,wup.imtt.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:35` | `DOMAIN,tpstelemetry.tencent.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:36` | `DOMAIN-KEYWORD,trace.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:39` | `DOMAIN-SUFFIX,l.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:41` | `IP-CIDR,47.110.187.87/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:45` | `^https://wallpaper-\d+\.file\.myqcloud\.com/dsl/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:46` | `^https?://wallpaper-\d+\.file\.myqcloud\.com/hikari/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqksong.conf:49` | `^https://wnsaviator\.kg\.qq\.com/wnsaviator/api/v1/transMerge\?_webcgikey=get_activity_entry$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqmusic.conf:15` | `DOMAIN,mc.tencentmusic.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qqmusic.conf:16` | `DOMAIN,monitor.music.qq.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:13` | `^https://app\.qtfm\.cn/recommendapi/v8/ai_assistant_point$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:14` | `^https://app\.qtfm\.cn/m-bff/v1/signin/show_homepage_icon$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:15` | `^https://app\.qtfm\.cn/recommendapi/v\d/emotion$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:16` | `^https://search\.qtfm\.cn/v\d/keyword/default$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:17` | `^https://app\.qtfm\.cn/m-bff/v1/user/task/play$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:18` | `^https://app\.qtfm\.cn/m-bff/v\d/i_listen/guess_you_like\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:19` | `^https://recpage-c\.qtfm\.cn/v\d/favorites$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:20` | `^https://user\.qtfm\.cn/u\d/api/v\d/user/following_podcaster\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:21` | `^https://entry\.qtfm\.cn/api/v\d/personal/\?carrier - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:22` | `^https://search\.qtfm\.cn/v3/entry$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/qting-fm.conf:23` | `^https://woqt2\.qtfm\.cn/v2/userConfig\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/quark-scan.conf:9` | `^https://scan-order\.quark\.cn/api/member/v1/center\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/rednote.conf:9` | `AND,((PROTOCOL,QUIC),(DOMAIN-SUFFIX,xiaohongshu.com,extended-matching)),REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/risk-bird.conf:10` | `^https://m\.riskbird\.com/prod-qbb-api/searchHotEnt - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/risk-bird.conf:9` | `^https://m\.riskbird\.com/prod-qbb-api/user/getBannerList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/roborock.conf:10` | `^https://cniot\.roborock\.com/api/v1/activity/latest$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/roborock.conf:11` | `^https://cniot\.roborock\.com/api/v1/app/theme/device/icon\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/roborock.conf:9` | `^https://cniot\.roborock\.com/api/v1/activity/banner/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/safety-home.conf:12` | `^https://app\.home\.360\.cn/v1/config/custom_config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/san-lian-zhong-du.conf:9` | `https://apis.lifeweek.com.cn/api/baseConfig/getIosNewConfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/sape.conf:11` | `DOMAIN-SUFFIX,dispenser-rtb.sape.ru,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/sape.conf:12` | `DOMAIN-SUFFIX,ssp-rtb.sape.ru,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/sape.conf:9` | `DOMAIN-SUFFIX,sape.ru,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/seven-cat.conf:15` | `^https://api-bc\.wtzw\.com/api/v4/search/dispose - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/seven-cat.conf:16` | `^https://api-bc\.wtzw\.com/api/v\d/book-store/config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/seven-cat.conf:17` | `^https://api-bc\.wtzw\.com/api/v\d/book-store/push-book - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/seven-cat.conf:18` | `^https://api-bc\.wtzw\.com/api/v\d/operation - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/seven-cat.conf:20` | `^https://api-gw\.wtzw\.com/welf/app/v\d/task/red-packet - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/seven-cat.conf:22` | `^https://api-cfg\.wtzw\.com/v\d/reward/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/seven-cat.conf:26` | `^https://xiaoshuo\.wtzw\.com/api/v\d/withdraw/init - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/sf-express.conf:10` | `^https://ucmp\.sf-express\.com/proxy/esgcempcore/memberGoods/pointMallService/goodsList$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/shou-yin-tong-merchant.conf:10` | `^https://m\.fqfin\.cn/cls/leshuapay/preCredit\.json$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/shou-yin-tong-merchant.conf:12` | `^https://syt\.leshuazf\.com/merchant/merchant/getBannerConfig$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/shou-yin-tong-merchant.conf:13` | `^https://syt\.leshuazf\.com/merchant/popup/getPopupInfo$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/shu-qi-center-reader.conf:9` | `DOMAIN,render-web.11222.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/skyworth.conf:10` | `DOMAIN-SUFFIX,hoisin.coocaatv.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/skyworth.conf:11` | `DOMAIN,data-hoisin.coocaa.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/skyworth.conf:9` | `DOMAIN-SUFFIX,hoisin.coocaa.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snow-camera.conf:11` | `DOMAIN,popup-api.b612kaji.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:10` | `^https://open\.xueqiu\.com/mpaas/config/content\?.+home_visitor_relation_config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:11` | `^https://api\.xueqiu\.com/ucprofile/api/user/batchGetUserBasicInfo\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:12` | `^https://api\.xueqiu\.com/lightsnow/launch/plan/bee/query\.json\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:13` | `^https://api\.xueqiu\.com/lightsnow/optional/banner/query\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:14` | `^https://api\.xueqiu\.com/snowflake-theme/query/v1/hot_event/rich_tag_new\.json\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:15` | `^https://api\.xueqiu\.com/query/v1/hot_event/tag\.json\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:17` | `^https://api\.xueqiu\.com/recommend-proxy/card/zj_card\.json\?feed_id=207 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:18` | `^https://api\.xueqiu\.com/recommend-proxy/card/portfolio_tab_symbol\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:19` | `^https://stock\.xueqiu\.com/v5/stock/group/recommend/default/list\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:20` | `^https://api\.xueqiu\.com/livestream/structure/live/hotCard\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:21` | `^https://fund\.xueqiu\.com/fundx/activity/x/web/c/index/dataByCode\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/snowball.conf:9` | `^https://api\.xueqiu\.com/snowpard/launch_strategy/query\.json\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soda-music.conf:12` | `^https://webcast-open\.douyin\.com/webcast/openapi/feed/\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soda-music.conf:13` | `^https://(beta-luna\.douyin\|api5-lq\.qishui)\.com/luna/treasure/entrance/config\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soda-music.conf:14` | `^https://(beta-luna\.douyin\|api5-lq\.qishui)\.com/luna/activities\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soda-music.conf:16` | `^https://(beta-luna\.douyin\|api5-lq\.qishui)\.com/luna/commerce/upsells\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soda-music.conf:17` | `^https://(beta-luna\.douyin\|api5-lq\.qishui)\.com/luna/commerce/v2/commerce_info\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soda-music.conf:9` | `^https://(beta-luna\.douyin\|api5-lq\.qishui)\.com/luna/commerce/upsells_config\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/sogou-input.conf:12` | `^https?://(ios\|android)\.sogou\.com/[^/]+/sogou_input_[^/]+/[^/]+/index\.html - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/sogou-input.conf:13` | `^https?://h5api\.sginput\.qq\.com/v1/gcenter/ios/homepage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/sogou-input.conf:9` | `DOMAIN-SUFFIX,push-service-ios.sginput.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soufun.conf:10` | `DOMAIN-SUFFIX,countubn.light.soufun.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soufun.conf:9` | `DOMAIN-SUFFIX,click1n.soufun.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soul.conf:16` | `IP-CIDR,47.56.131.76/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soul.conf:17` | `IP-CIDR,47.97.215.55/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soul.conf:18` | `IP-CIDR,47.99.42.29/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soul.conf:19` | `IP-CIDR,47.110.187.87/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soul.conf:20` | `IP-CIDR,47.243.147.125/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soul.conf:21` | `IP-CIDR,120.27.235.201/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/soul.conf:22` | `IP-CIDR,121.196.197.147/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taobao-travel.conf:10` | `^https://acs\.m\.taobao\.com/gw/mtop\.fliggy\.crm\.screen\.predict/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taobao-travel.conf:11` | `^https://acs\.m\.taobao\.com/gw/mtop\.fliggy\.tripzoo\.new\.couponlist/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taobao-travel.conf:12` | `^https://acs\.m\.taobao\.com/gw/mtop\.trip\.my\.recommendcard/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taobao-travel.conf:13` | `^https://acs\.m\.taobao\.com/gw/mtop\.fliggy\.recommend\.common\.guess\.tab\.feeds/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taobao-travel.conf:9` | `^https://acs\.m\.taobao\.com/gw/mtop\.fliggy\.crm\.screen\.allresource/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taobao.conf:13` | `DOMAIN,ut.taobao.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taopiaopiao.conf:9` | `^https://acs\.m\.taobao\.com/gw/mtop\.film\.life\.popup\.get/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:10` | `^https://gw-cn\.jiaoliuqu\.com/bbs/v5/Guide/photoGuide\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:11` | `^https://gw-cn\.jiaoliuqu\.com/i/v\d/homepage/completeGuideV\d\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:12` | `^https://gw-cn\.jiaoliuqu\.com/i/v\d/asset/toast\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:13` | `^https://gw-cn\.jiaoliuqu\.com/bbs/v5/Sign/getDailySigninInfoV4\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:14` | `^https://gw-cn\.jiaoliuqu\.com/taqu-hichat/v\d/Hichat/getRecommendInfo\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:15` | `^https://gw-cn\.jiaoliuqu\.com/live_api/v\d/Banner/getBannerListV\d\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:16` | `^https://gw-cn\.jiaoliuqu\.com/live_api/v\d/HallScroll/getList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:17` | `^https://gw-cn\.jiaoliuqu\.com/taqu-msg-guide/v\d/RecommendColumn/getList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/taqu.conf:9` | `^https://gw-cn\.jiaoliuqu\.com/taqu-homepage/v\d/Banner/getBannerByPositions\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tencent-sports.conf:9` | `^https?://news\.ssp\.qq\.com/app - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tencent-video.conf:15` | `DOMAIN,tpns.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tencent-video.conf:18` | `DOMAIN-SUFFIX,l.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tencent-video.conf:19` | `DOMAIN-KEYWORD,trace.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tencent-video.conf:21` | `IP-CIDR,47.110.187.87/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/terabox.conf:9` | `DOMAIN,ymg-api.terabox.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tmall-genie.conf:9` | `^https?://zconfig\.alibabausercontent\.com/zconfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tu-guai-shou.conf:10` | `^https://api\.818ps\.com/v4/popup/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tu-guai-shou.conf:11` | `^https://api\.818ps\.com/v4/festival/newYear/pop\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tube-max.conf:11` | `DOMAIN-SUFFIX,applvn.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tube-max.conf:12` | `DOMAIN-SUFFIX,app-measurement.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tube-max.conf:13` | `DOMAIN-SUFFIX,pangle.io,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tube-max.conf:14` | `DOMAIN-SUFFIX,applovin.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tube-max.conf:15` | `DOMAIN-SUFFIX,appier.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tui-lan.conf:9` | `^https?://m\.pvp\.xoyo\.com/conf/server-mapping - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tv-assistant.conf:10` | `^https://saas\.hpplay\.cn/api/lebo-desk/endpoint/app-resource/app_home_tips - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tv-assistant.conf:11` | `^https://saas\.hpplay\.cn/api/lebo-desk/endpoint/app-resource/app_index_operate2 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tv-assistant.conf:12` | `^https://saas\.hpplay\.cn/api/lebo-rabbit/app-card/list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tv-assistant.conf:13` | `^https://saas\.hpplay\.cn/api/lebo-desk/endpoint/app-resource/app-user-banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/tv-assistant.conf:9` | `^https://saas\.hpplay\.cn/api/lebo-desk/endpoint/app-resource/app_home_pop_up - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/twitch.conf:9` | `DOMAIN-SUFFIX,fan.twitch.tv,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/twitter.conf:10` | `DOMAIN-SUFFIX,p.twitter.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/twitter.conf:11` | `DOMAIN-SUFFIX,scribe.twitter.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/twitter.conf:12` | `DOMAIN-SUFFIX,syndication.twitter.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/twitter.conf:13` | `DOMAIN-SUFFIX,syndication-o.twitter.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/twitter.conf:14` | `DOMAIN-SUFFIX,urls.api.twitter.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/uki.conf:10` | `^https://api\.chenlongtech\.cn/v\d/friends/indexBanner$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/uki.conf:11` | `^https://api\.chenlongtech\.cn/v\d/friends/getPopup - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/uki.conf:12` | `^https://api\.chenlongtech\.cn/v\d/friends/allPopUpConfig$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/uki.conf:14` | `^https://api\.chenlongtech\.cn/v\d/user/checkQTSheInsurance$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/uki.conf:9` | `^https://api\.chenlongtech\.cn/v\d/friends/startInfo$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/umetrip.conf:9` | `URL-REGEX,"^http?:\/\/(discardrp\|startup)\.umetrip\.com\/gateway\/api\/umetrip\/native",REJECT,extended-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/valorant-bible.conf:10` | `^https://app\.mval\.qq\.com/go/mlol_news/search/varcache_hotV\d\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/valorant-bible.conf:11` | `^https://app\.mval\.qq\.com/go/customize_search/article_rank_tab\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/valorant-bible.conf:9` | `^https://app\.mval\.qq\.com/go/recommend/platflashbox\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/video-go.conf:10` | `^https://i\.ys7\.com/api/user/tabList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/video-go.conf:11` | `^https://api\.ys7\.com/v3/config/service/entrance/bannerInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/video-go.conf:12` | `^https://api\.ys7\.com/v3/intelligent-app/apps/linkage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/video-go.conf:13` | `^https://api\.ys7\.com/v3/configurations/gray/info\?grayTypes=185 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wa-cai-ji-zhang.conf:10` | `^https://jz\.wacaijizhang\.com/api/banners/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wa-cai-ji-zhang.conf:11` | `^https://jz\.wacaijizhang\.com/api/resource/universal/fetch$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wa-cai-ji-zhang.conf:9` | `^https://jz\.wacaijizhang\.com/api/banners/ribbon\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/walmart.conf:11` | `^https://api-hyper\.walmartmobile\.cn/search/frontapi/discovery-words/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wasu-tv.conf:10` | `DOMAIN-SUFFIX,afp.wasu.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wasu-tv.conf:11` | `DOMAIN-SUFFIX,afpcreative.wasu.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wasu-tv.conf:12` | `DOMAIN-SUFFIX,collector.wasu.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wasu-tv.conf:13` | `DOMAIN-SUFFIX,delivery.wasu.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wasu-tv.conf:14` | `DOMAIN-SUFFIX,delivery-pc.wasu.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wasu-tv.conf:9` | `DOMAIN-SUFFIX,acsystem.wasu.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:106` | `^https://m\.ctrip\.com/restapi/soa2/12673/queryWeChatHotEvent - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:108` | `^https://wx\.maoyan\.com/maoyansh/api/mobile/(hotMatchList\|eSportsIps) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:11` | `DOMAIN,wxsnsdythumb.wxs.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:110` | `^https://wx\.maoyan\.com/maoyansh/myshow/ajax/movie/wonderShow - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:111` | `^https://wx\.maoyan\.com/maoyansh/myshow/ajax/performances/calendar/0 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:112` | `^https://wx\.maoyan\.com/maoyansh/myshow/ajax/performances/rob/main - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:113` | `^https://wx\.maoyan\.com/maoyansh/myshow/ajax/celebrityBasicList/query - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:114` | `^https://wx\.maoyan\.com/maoyansh/myshow/ajax/recommend/performances - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:115` | `^https://api\.maoyan\.com/sns/common/feed/channel/v2/list\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:117` | `^https://mkt-gateway\.tuhu\.cn/mkt-scene-marketing-service/api/scene/queryScheme - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:118` | `^https://api\.hengdianfilm\.com//cinema/queryAvailableBannerInfo/2\?cid= - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:119` | `^https://api\.hengdianfilm\.com//cinema/queryAvailableBannerInfo/4\?cid= - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:121` | `^https://api\.pinduoduo\.com/api/ktt_gateway/activity/feeds/personal_home_page/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:123` | `^https://ucmp\.sf-express\.com/proxy/esgcempcore/memberGoods/pointMallService/goodsList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:124` | `^https://as\.xiaojukeji\.com/ep/as/conf\?ns=daijia-front&name= - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:128` | `^https://mobile\.12306\.cn/wxxcx/openplatform-inner/miniprogram/wifiapps/tourism/tourismBase/api/scenic/getThemeProduct? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:130` | `^https://wx\.online-cmcc\.cn/contactpoint/customer/api/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:131` | `^https://wx\.10086\.cn/qwhdhub/activity/info - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:17` | `DOMAIN,e.jparking.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:25` | `^https://webchatapp\.fcbox\.com/fcboxactivityweb/api/v2/clientPage/modulesAggregated\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:26` | `^https://webchatapp\.fcbox\.com/fcboxactivityweb/api/v2/clientPage/getHomeLiveInfo$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:28` | `^https://webchatapp\.fcbox\.com/post/suggestion/query$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:29` | `^https://webchatapp\.fcbox\.com/fcboxactivityweb/marketingEntrance/v2/infoWithItems$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:30` | `^https://webchatapp\.fcbox\.com/fcboxactivityweb/marketingEntrance/info$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:34` | `^https://flow\.dmall\.com/app/home/pops - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:35` | `^https://api\.yonghuivip\.com/api/fp/homepage/pop - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:36` | `^https://activity\.yonghuivip\.com/api/app/fp/homepage/pop - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:38` | `^https://sauron-report\.yonghuivip\.com/collect - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:39` | `^https://res\.pizzahut\.com\.cn/CRM - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:40` | `^https://api\.mcd\.cn/bff/portal/home/hotActivity - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:41` | `^https://3pp\.starbucks\.com\.cn/wxmem/popup - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:42` | `^https://3pp\.starbucks\.com\.cn/wxmem/index/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:43` | `^https://3pp\.starbucks\.com\.cn/wxmem/index/global - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:44` | `^https://wechat-api\.i-xiaoma\.com\.cn/app/v1/bus/wechat/content - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:45` | `^https://apiproxy\.zuche\.com/resource/carrctapi/home/marketing - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:47` | `^https://miniprogram\.ishansong\.com/cms/faq/query - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:52` | `^https://applets\.jtexpress\.com\.cn - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:54` | `^https://api\.kuaidihelp\.com/g_order_core/v2/mina/User/getBannerList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:55` | `^https://wxproj\.seeyouyima\.com/data/today_tips - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:56` | `^https://suyun-guest\.daojia\.com/api/kuaigou/banjia/review - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:59` | `^https://qapi\.huolala\.cn/home_new_user - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:60` | `^https://qapi\.huolala\.cn/get_service_list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:62` | `^https://apis\.alenable\.com/mall/v1/api/mall/skin/user/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:64` | `^https://dock\.tenchii\.com/DockCard/api/mini/card/list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:65` | `^https://customer-app\.sto\.cn/api/app/banner/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:68` | `^https://hdgateway\.zto\.com/getApolloConfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:71` | `^https://hdgateway\.zto\.com/listJumperShow - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:73` | `^https://mobile-api\.imlaidian\.com/api/args - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:76` | `^https://smarket\.dian\.so - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:77` | `^https://file\.dian\.so/c/leto - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:80` | `^https://api-marketing\.zhinengxiyifang\.cn/api/v2/cloudcode/wechat/bid - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:81` | `^https://api\.songguo7\.com/(\w{3})?mp/v2/misc/(toast\|user_operate_info\|unlock_without_order\|unlock_operate_info) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:83` | `^https://tm-api\.pin-dao\.cn/home/api/index/activeConfig/v2 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:84` | `^https://tm-api\.pin-dao\.cn/home/api/resource/config/homeBannerNodes - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:85` | `^https://api-fouth-mem\.huazhu\.com/api/rights/bannerList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:86` | `^https://wxapp\.bestwehotel\.com/gw3/app-mini/trip-hotel-banner/activity/getActivityInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:87` | `^https://wx\.bthhotels\.com/miniapp/weixin/v1/home/index_banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:88` | `^https://app\.homeinns\.com/api/v6/indexs - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:89` | `^https://app\.homeinns\.com/api/v5/local - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:9` | `DOMAIN,wxsnsdy.wxs.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:90` | `^https://app\.homeinns\.com/api/v5/index - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:92` | `^https://htwkop\.xiaojukeji\.com/gateway\?api=cms\.htw\.delivery - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:93` | `^https://htwkop\.xiaojukeji\.com/gateway\?api=hm\.fa\.combineHomepageInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:94` | `^https://htwkop\.xiaojukeji\.com/gateway\?api=hm\.fa\.mallRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:95` | `^https://lawsonapi\.yorentown\.com/area/sh-lawson/app/v1/mina/systemSetting - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:96` | `^https://plt\.yorentown\.com/pltapp/v1/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-mini-programs.conf:97` | `^https://member\.lxjchina\.com\.cn/mini-server/home/page/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-official-accounts.conf:13` | `^https://mp\.weixin\.qq\.com/mp/relatedsearchword - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat-official-accounts.conf:9` | `DOMAIN-SUFFIX,wxs.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wechat.conf:9` | `DOMAIN-SUFFIX,wxs.qq.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/weibo-intl.conf:10` | `^https://api\.weibo\.cn/2/cardlist\?v_f=2 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/weibo-intl.conf:12` | `^https://weibointl\.api\.weibo\.cn/portal\.php\?a=get_searching_info - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/weibo.conf:10` | `DOMAIN,huodong.weibo.cn,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/weibo.conf:11` | `DOMAIN-SUFFIX,biz.weibo.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wpforum.conf:9` | `^https://api\.wfdata\.club/v2/yesfeng/yesList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wps.conf:10` | `^https://www\.kdocs\.cn/kdg/api/v1/cards/type/27\?iosVer=\d+\.\d+\.\d+&isGetList=1 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wps.conf:11` | `^https://f-api\.kdocs\.cn/godfather/api/thirdparty/v1/viewpager\?showLocal=mobileWebIndex - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/wps.conf:9` | `^https://www\.kdocs\.cn/kdg/api/v1/cards/type/3\?iosVer=\d+\.\d+\.\d+&isGetList=1 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xfuse.conf:9` | `^https://cili\.xfuse\.fun/s/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xia-chu-fang.conf:11` | `^https://api\.xiachufang\.com/v2/homepage1810/init_page\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xia-chu-fang.conf:12` | `^https://api\.xiachufang\.com/v2/mark_mission/get_sticker_info\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xiao-can.conf:11` | `^https://gw\.xiaocantech\.com/g/pa - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xiao-can.conf:9` | `^https://web2\.realtech-inc\.com/oss/xc-app-assets/configs/common/theme\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xiaojukeji-charge.conf:10` | `^https://energy\.xiaojukeji\.com/lego/api/orderSprint/stair/info($\|\?) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xiaojukeji-charge.conf:9` | `^https://energy\.xiaojukeji\.com/energy/hummer/api/resource/display($\|\?) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xiaomi-speaker.conf:10` | `^https://marketing-aibox\.v\.mitvos\.com/payGuide/halfScreenMulti/(home\|cache)\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xiaomi-speaker.conf:11` | `^https://marketing-aibox\.v\.mitvos\.com/payGuide/tabPage\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xiaopeng.conf:6` | `DOMAIN,apps-booster.xiaopeng.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/xiaopeng.conf:7` | `DOMAIN,collect.xiaopeng.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:10` | `DOMAIN-SUFFIX,beap-bc.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:11` | `DOMAIN-SUFFIX,comet.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:12` | `DOMAIN-SUFFIX,geo.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:13` | `DOMAIN-SUFFIX,marketingsolutions.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:14` | `DOMAIN-SUFFIX,p3p.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:15` | `DOMAIN-SUFFIX,themis.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:16` | `DOMAIN-SUFFIX,ysm.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:19` | `DOMAIN-SUFFIX,clicks.beap.bc.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:20` | `DOMAIN-SUFFIX,aliunion.cn.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:21` | `DOMAIN-SUFFIX,cm.p4p.cn.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:22` | `DOMAIN-SUFFIX,n.gemini.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:23` | `DOMAIN-SUFFIX,doubleplay-conf-yql.media.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:24` | `DOMAIN-SUFFIX,ws.progrss.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:26` | `DOMAIN-SUFFIX,locdrop.query.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:27` | `DOMAIN-SUFFIX,onepush.query.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:28` | `DOMAIN-SUFFIX,iframe.travel.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:29` | `DOMAIN-SUFFIX,m.yap.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:30` | `DOMAIN-SUFFIX,pr.ybp.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:31` | `DOMAIN-SUFFIX,pr-bh.ybp.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:32` | `DOMAIN-SUFFIX,js-apac-ss.ysm.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:33` | `DOMAIN-SUFFIX,w.homes.yahoo.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:34` | `DOMAIN-SUFFIX,yieldmanager.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:35` | `DOMAIN-SUFFIX,ard.yahoo.co.jp,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:37` | `DOMAIN-SUFFIX,yeas.yahoo.co.jp,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:38` | `DOMAIN-SUFFIX,rd.ane.yahoo.co.jp,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:39` | `DOMAIN-SUFFIX,bc.geocities.yahoo.co.jp,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:40` | `DOMAIN-SUFFIX,im.ov.yahoo.co.jp,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yahoo.conf:44` | `DOMAIN-SUFFIX,gemini.yahoo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yi-kao-bang.conf:10` | `^https://api\.yikaobang\.com\.cn/index\.php/client/Main/startPage\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yitian.conf:10` | `^https://(m2u-api\.getkwai\|api-m2u\.kuaishou)\.com/api-server/api/v4/op/actPositions\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-dict.conf:12` | `^https://dict\.youdao\.com/vip/activity/startup/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-dict.conf:13` | `^https://dict\.youdao\.com/vip/activity/retention/configs\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-dict.conf:14` | `^https://dict\.youdao\.com/vip/activity/retention/match\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-dict.conf:15` | `^https://dict\.youdao\.com/vip/user/paid/guide\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-trans.conf:10` | `^https://gorgon\.youdao\.com/gorgon/brand/prefetch\.s - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-trans.conf:11` | `^https://gorgon\.youdao\.com/gorgon/request\.s - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-trans.conf:12` | `^https://fanyiguan-server\.youdao\.com/server/banner\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-trans.conf:13` | `^https://dict\.youdao\.com/vip/activity/fanyiguan/sevendayfree/imei\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-trans.conf:14` | `^https://dict\.youdao\.com/wordbook/recommend\?all=false - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-trans.conf:15` | `^https://api-overmind\.youdao\.com/openapi/get/luna/dict/trans_abtest/online/iOS\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youdao-trans.conf:9` | `^https://gorgon\.youdao\.com/gorgon/v2/request\.s - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youku.conf:25` | `DOMAIN,vali-g1.cp31.ott.cibntv.net,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/youku.conf:26` | `DOMAIN,vali-ugc.cp31.ott.cibntv.net,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yue-dan-ba.conf:10` | `^https://api\.17gwx\.com/v2/growth/popup/remind$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yue-dan-ba.conf:11` | `^https://api\.17gwx\.com/v2/recommend/feed/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yue-dan-ba.conf:12` | `^https://api\.17gwx\.com/v2/homepage/feed/similarList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yy-voice.conf:15` | `^https://yyapp-fastnet\.yy\.com/dispatch\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yy-voice.conf:16` | `^https://data\.3g\.yy\.com/popup/topLiveCardPopup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yy-voice.conf:17` | `^https://yyapp-act-entrance\.yy\.com/entrance/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yyvoice-tool.conf:10` | `^https://yuyin-api\.baizhanlive\.com/homepage/homepage/banner\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yyvoice-tool.conf:11` | `^https://web\.yy\.com/yyvoice_task_sys/bar\.html\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yyvoice-tool.conf:12` | `^https://yuyin-api\.baizhanlive\.com/search/search/hotword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/yyvoice-tool.conf:9` | `^https://yuyin-api\.baizhanlive\.com/homepage/flashscreen/get\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zaker.conf:9` | `^https://iphone\.myzaker\.com/zaker/cover\.php\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zdm.conf:12` | `^https:\/\/h5\.smzdm\.com\/user\/coupon\/coupon_list\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhi-lian-zhao-pin.conf:12` | `^https://cgate\.zhaopin\.com/resumeapi/resumeCheck/positionDetailBottomTipCheck$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhi-lian-zhao-pin.conf:13` | `^https://cgate\.zhaopin\.com/bdp/commercial/queryLinkData$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:10` | `DOMAIN,appcloud2.in.zhihu.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:11` | `DOMAIN,crash2.zhihu.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:12` | `DOMAIN,mqtt.zhihu.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:13` | `DOMAIN,sugar.zhihu.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:14` | `DOMAIN,zxid-m.mobileservice.cn,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:15` | `IP-CIDR,103.41.167.237/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:16` | `IP-CIDR,118.89.204.198/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:17` | `IP-CIDR,182.61.194.7/32,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:18` | `IP-CIDR6,2402:4e00:1200:ed00:0:9089:6dac:96b6/128,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:21` | `^https:\/\/api\.zhihu\.com\/unlimited\/go\/my_card - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:22` | `^https:\/\/www\.zhihu\.com\/appview\/v3\/zhmore - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhihu.conf:9` | `DOMAIN,appcloud.zhihu.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhuan-zhuan.conf:10` | `^https://app\.zhuanzhuan\.com/zz/v2/zzinfoshow/getwindvanecardv2$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhuan-zhuan.conf:11` | `^https://app\.zhuanzhuan\.com/zzopen/popwindow/getallpopwin\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhuan-zhuan.conf:14` | `^https://app\.zhuanzhuan\.com/zzopen/ypmall/listData$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zhuan-zhuan.conf:15` | `^https://app\.zhuanzhuan\.com/zz/v2/zzusercenter/myprofilevariouscards$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zong-heng.conf:10` | `^https://api2\.zongheng\.com/api/giftBag/bindingBag$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zong-heng.conf:9` | `^https://api1\.zongheng\.com/iosapi/system/startup$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zui-you.conf:11` | `URL-REGEX,"^http:\/\/file-share\.izuiyou\.com\/octopus\/media\/templates\/search_home_page_(nv\|nv_v2)\/search_home_page_nv",REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zui-you.conf:14` | `^https?://api\.izuiyou\.com/config/get_banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zui-you.conf:16` | `^https://zyfile\.izuiyou\.com/zyfile/c2/a0/[a-z0-9-]+\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zuoyebang.conf:11` | `^https?:\/\/www\.kuaiduizuoye\.com\/kdapi\/conf\/appbannersv3$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Apps/zuoyebang.conf:12` | `^https?:\/\/www\.kuaiduizuoye\.com\/kdapi\/conf\/initbanner$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/analytics.conf:9` | `DOMAIN-KEYWORD,crashlytics,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:24` | `DOMAIN,api.e.kuaishou.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:27` | `DOMAIN,e.kuaishou.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:28` | `DOMAIN,ios.bugly.qq.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:31` | `DOMAIN,monitor.music.qq.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:32` | `DOMAIN,open.e.kuaishou.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:35` | `DOMAIN,popup-api.b612kaji.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:37` | `DOMAIN,retcode.taobao.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:38` | `DOMAIN,rmonitor.qq.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:42` | `DOMAIN,tns.simba.taobao.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:43` | `DOMAIN,tpstelemetry.tencent.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:52` | `DOMAIN-KEYWORD,doubleclick,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/android-compatible-ads.conf:54` | `DOMAIN-KEYWORD,googlesyndication,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Misc/generic-ads.conf:8` | `DOMAIN-SUFFIX,doubleclick.net,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:107` | `DOMAIN,ivy.pchouse.com.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:11` | `DOMAIN-SUFFIX,googlesyndication.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:111` | `DOMAIN,live-monitor-broker.sankuai.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:12` | `DOMAIN-SUFFIX,googletagservices.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:45` | `DOMAIN,apm-native.xiaohongshu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:46` | `DOMAIN,apm.gotokeep.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:47` | `DOMAIN,apmplus.volces.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:48` | `DOMAIN,appcloud.zhihu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:49` | `DOMAIN,appcloud2.in.zhihu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:50` | `DOMAIN,appgo.189.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:51` | `DOMAIN,apps-booster.xiaopeng.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:52` | `DOMAIN,appupdates.189.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:53` | `DOMAIN,atrace.chelaile.net.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:54` | `DOMAIN,axxd.xmseeyouyima.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:59` | `DOMAIN,collect.xiaopeng.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:60` | `DOMAIN,counter.kingsoft.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:61` | `DOMAIN,counter.ksosoft.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:62` | `DOMAIN,crash2.zhihu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:66` | `DOMAIN,csc-apm.sgcc.com.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:67` | `DOMAIN,cube.weixinbridge.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:68` | `DOMAIN,da.bridgeturbo.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:74` | `DOMAIN,dynamicf.sankuai.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:76` | `DOMAIN,et.ykccn.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:77` | `DOMAIN,etl.xlmc.sandai.net,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:80` | `DOMAIN,gather.colorfulclouds.net,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:81` | `DOMAIN,gwp.xiaojukeji.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:82` | `DOMAIN,hc-ssp.sm.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/Rule.conf:9` | `DOMAIN-SUFFIX,doubleclick.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:100` | `^http:\/\/home\.umetrip\.com\/gateway\/api\/umetrip\/native - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:103` | `^http:\/\/umerp\.umetrip\.com\/gateway\/api\/umetrip\/native - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:107` | `^https?:\/\/tower\.ubixioe\.com\/mob\/mediation - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:108` | `^https?:\/\/sdk1xyajs\.data\.kuiniuca\.com - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:114` | `^https:\/\/api\.wfdata\.club\/v2\/yesfeng\/yesList - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:117` | `^https:\/\/app\.10099\.com\.cn\/contact-web\/api\/version\/getFlashScreenPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:24` | `^https:\/\/flow\.dmall\.com\/app\/home\/pops - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:27` | `^https:\/\/api\.yonghuivip\.com\/api\/fp\/homepage\/pop - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:28` | `^https:\/\/activity\.yonghuivip\.com\/api\/app\/fp\/homepage\/pop - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:30` | `^https:\/\/sauron-report\.yonghuivip\.com\/collect - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:36` | `^https:\/\/hdgateway\.zto\.com\/getApolloConfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:39` | `^https:\/\/hdgateway\.zto\.com\/listJumperShow - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:49` | `^https:\/\/api-marketing\.zhinengxiyifang\.cn\/api\/v2\/cloudcode\/wechat\/bid - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:58` | `^https:\/\/api\.pinduoduo\.com\/api\/ktt_gateway\/activity\/feeds\/personal_home_page\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:68` | `^https?:\/\/home\.mi\.com\/cgi-op\/api\/v\d\/recommendation\/banner - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf:97` | `^https:\/\/acs\.m\.taobao\.com\/gw\/mtop\.taobao\.idle\.home\.welcome - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:10` | `^https?:\/\/(a\.athm\.cn\/)?mobile\.app\.autohome\.com\.cn\/platform\/carserver\/usercenter\/chat\/gse\/recquery - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1001` | `^https?:\/\/m1fxgroup\.kugou\.com\/fxsing\/yqc\/alongInfo\/getUserAlongInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1015` | `^https?:\/\/m\.client\.10010\.com\/mobileService\/customer\/getclientconfig\.htm - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1020` | `^https?:\/\/m\.fqfin\.cn\/cls\/leshuapay\/preCredit\.json$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1021` | `^https?:\/\/m\.ibuscloud\.com\/v\d\/app\/getStartPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1028` | `^https?:\/\/m\.trip\.com\/quic - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1032` | `^https?:\/\/m\.you\.163\.com\/activity\/popWindow - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1037` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/booksearch\/hotWords\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1038` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/bookshelf\/getTopOperation$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1039` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/checkin\/simpleinfo\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1040` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/dailyrecommend\/recommendBook\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1041` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/followsubscribe\/showChapterEndModule\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1042` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/freshman\/bookshelfbtn$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1043` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/maintain\/playstrip$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1044` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/message\/getpushedmessagelist$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1046` | `^https?:\/\/magev6\.if\.qidian\.com\/argus\/api\/v1\/young\/getconf$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1052` | `^https?:\/\/manga\.bilibili\.com\/twirp\/bookshelf\.v\d\.Bookshelf\/ListEmptyRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1053` | `^https?:\/\/manga\.bilibili\.com\/twirp\/bookshelf\.v\d\.Bookshelf\/NovelRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1054` | `^https?:\/\/manga\.bilibili\.com\/twirp\/comic\.v\d\.Comic\/AppInit - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1055` | `^https?:\/\/manga\.bilibili\.com\/twirp\/comic\.v\d\.Comic\/GetActivityTab - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1056` | `^https?:\/\/manga\.bilibili\.com\/twirp\/comic\.v\d\.Comic\/GetBubbles - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1057` | `^https?:\/\/manga\.bilibili\.com\/twirp\/comic\.v\d\.Comic\/GetCommonBanner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1058` | `^https?:\/\/manga\.bilibili\.com\/twirp\/comic\.v\d\.Comic\/ListFlash - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1059` | `^https?:\/\/manga\.bilibili\.com\/twirp\/comic\.v\d\.Comic\/SearchBanner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1060` | `^https?:\/\/manga\.bilibili\.com\/twirp\/novel\.v\d\.Novel\/MoreRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1061` | `^https?:\/\/manga\.bilibili\.com\/twirp\/user\.v\d\.SeasonV\d\/GetSeasonInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1064` | `^https?:\/\/mapi\.appvipshop\.com\/vips-mobile\/rest\/activity\/coupon\/float_entrance\/get\?api_key - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1066` | `^https?:\/\/mapi\.appvipshop\.com\/vips-mobile\/rest\/layout\/productList\/eventData\/v - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1067` | `^https?:\/\/mapi\.dangdang\.com\/index\.php\?action=init - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1073` | `^https?:\/\/mapi\.mafengwo\.cn\/user\/growth\/get_growth_tip\/v1\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1074` | `^https?:\/\/mapi\.sfbest\.com\/brokerservice-server\/cms\/getPositionById.* - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1076` | `^https?:\/\/mapiweb\.babytree\.com\/newapi\/luban\/behavior\/receive - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1083` | `^https?:\/\/mcbd\.maiche\.com\/api\/open\/v\d\/user\/get-popup-window - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1087` | `^https?:\/\/mcsp\.cloudpnr\.com\/api\/miniapp\/popular\/T_MINIAPP$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1089` | `^https?:\/\/member\.alipan\.com\/v\d\/activity\/sign_in_(?:info\|luckyBottle) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1090` | `^https?:\/\/member\.lxjchina\.com\.cn\/mini-server\/home\/page\/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1096` | `^https?:\/\/middle\.yun\.139\.com\/openapi\/cardConfig\/queryCardInfoV - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:11` | `^https?:\/\/(a\.athm\.cn\/)?mobile\.app\.autohome\.com\.cn\/platform\/carserver\/usercenter\/getdealertab - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1105` | `^https?:\/\/miniapp\.sexytea2013\.com\/cms\/slot\/byCode\?code=MALL_INDEX_SLOT - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1107` | `^https?:\/\/miniprogram\.ishansong\.com\/cms\/faq\/query - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1108` | `^https?:\/\/mkt-gateway\.tuhu\.cn\/mkt-scene-marketing-service\/api\/scene\/queryScheme - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1109` | `^https?:\/\/mlol\.qt\.qq\.com\/go\/club\/match\/get_ai_search_words$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1110` | `^https?:\/\/mlol\.qt\.qq\.com\/go\/customize_search\/article_rank\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1111` | `^https?:\/\/mlol\.qt\.qq\.com\/go\/customize_search\/article_rank_tab\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1112` | `^https?:\/\/mlol\.qt\.qq\.com\/go\/mlol_news\/search\/varcache_hotV\d\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1113` | `^https?:\/\/mlol\.qt\.qq\.com\/go\/recommend\/platstrongshell\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1114` | `^https?:\/\/mlol\.qt\.qq\.com\/go\/zone\/bottomtab_tip\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1122` | `^https?:\/\/mobile-api\.imlaidian\.com\/api\/args - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1123` | `^https?:\/\/mobile-consumer-sapp\.chery\.cn\/web\/position\/getShowList\?displayPlatform=1&tabType=0& - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1125` | `^https?:\/\/mobile\.1qianbao\.com\/mtp-web\/ui\/op_common_query_business_yqb\.json - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1128` | `^https?:\/\/mobileapi\.ly\.com\/wlfrontend\/app\/scenicMain - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1129` | `^https?:\/\/mobileapi\.xiamenair\.com\/mobile-starter - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1133` | `^https?:\/\/monkey\.kakamobi\.cn\/api\/open\/live-room\/get-resource - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1134` | `^https?:\/\/monkey\.kakamobi\.cn\/api\/open\/live\/get-recommend-live-protocol - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1138` | `^https?:\/\/mpcs\.suning\.com\/mpcs\/dm\/getDmInfo - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1143` | `^https?:\/\/mrp\.mcloud\.139\.com\/mc\/mc-client-service\/openapi\/letter\/query - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1147` | `^https?:\/\/msglb\.91160\.com\/msg\/outer\/broker\/get$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1150` | `^https?:\/\/myusmile\.online\/user\/version\/requestAppUpdate - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1151` | `^https?:\/\/myusmile\.online\/user\/version\/requestFirmwareUpdate\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1152` | `^https?:\/\/nbcps-mtop\.cainiao\.com\/gw\/mtop\.cainiao\.nbcps\.presentation\.fetch\.cn - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1153` | `^https?:\/\/nelo2-col\.linecorp\.com\/_store$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1156` | `^https?:\/\/news\.app\.autohome\.com\.cn\/cont_v\d+(?:\.\d+){2}\/api\/article\/extenddata - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1161` | `^https?:\/\/ntt-app\.benewtech\.cn\/v6\/user\/\d+\/messages\/event - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1165` | `^https?:\/\/ok\.166\.net\/reunionpub\/202[2-9]{1}-[0-9]{2}-[0-9]{2}\/ntesgod_cms\/.*.jpg$ - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1166` | `^https?:\/\/omgup[0-9]{1}\.xiaojukeji\.com\/api - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1168` | `^https?:\/\/online\.aicarmap\.com\/club\/api\/user\/updateloc - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1169` | `^https?:\/\/op\.ksedt\.com\/jxedtLive\/liveIntroduceResource - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1170` | `^https?:\/\/open3\.vistastory\.com\/v\d\/api.*get_popup - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1172` | `^https?:\/\/open\.e\.kuaishou\.cn\/rest\/e\/v3\/open - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1173` | `^https?:\/\/open\.e\.kuaishou\.com\/rest\/e\/v3\/open\/univ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1175` | `^https?:\/\/open\.qyer\.com\/qyer\/config\/get - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1176` | `^https?:\/\/open\.qyer\.com\/qyer\/startpage\/ - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1179` | `^https?:\/\/oss-zjrs\.haier\.net\/resource\/confFile\/\d{22}\.zip$ - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1183` | `^https?:\/\/ovs-shopwindow-server.*\.wps\.com\/api\/v\d\/shop_window\/type\/ios - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:119` | `^https?:\/\/101\.91\.69\.26:8080\/.+ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1191` | `^https?:\/\/p\.c\.music\.126.net\/.*?jpg$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1195` | `^https?:\/\/p\.kuaidi100\.com\/e-commerce\/act\/actInfo\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:12` | `^https?:\/\/(a\.athm\.cn\/)?mobile\.app\.autohome\.com\.cn\/platform\/carserver\/usercenter\/gethotactcards - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:120` | `^https?:\/\/103\.37\.155\.60\/fetch - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1204` | `^https?:\/\/p\d\.music\.126\.net\/\w+==\/\d+\.jpg$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1206` | `^https?:\/\/pages\.trip\.com\/js\/market - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1217` | `^https?:\/\/patient-api\.suh\.cn\/apt\/api\/userinfo\/GetNotice\?appname=pmsys&channel=6&device=ios&language=1&source=2&version= - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1220` | `^https?:\/\/patientgate\.91160\.com\/rec\/homepage\/open\/getUserGoodsList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1221` | `^https?:\/\/pcmx\.autohome\.com\.cn\/queryCreativeList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1228` | `^https?:\/\/plough\.babytree\.com\/plough\.do - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1229` | `^https?:\/\/plt\.yorentown\.com\/pltapp\/v\d\/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1231` | `^https?:\/\/poi\.map\.xiaojukeji\.com\/mapapi\/recommend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1235` | `^https?:\/\/preprod\.cdzghome\.com:8100\/banner\/bootUp - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1236` | `^https?:\/\/prom\.mobile\.gome\.com\.cn\/mobile\/promotion\/promscms\/\w+\.jsp - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1237` | `^https?:\/\/prom\.mobile\.gome\.com\.cn\/mobile\/promotion\/promscms\/sale\w+\.jsp - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:124` | `^https?:\/\/182\.92\.244\.70\/d\/json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1249` | `^https?:\/\/quanguo\.mygolbs\.com:8081\/MyBusServer\/servlet\/MyGoServer\.HttpPool\.HttpHandlerServlet - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:125` | `^https?:\/\/203\.107\.1\.1/\d+/ss - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1255` | `^https?:\/\/recite\.perfectlingo\.com\/api\/recite\/app-act\/act-list.+ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1256` | `^https?:\/\/recite\.perfectlingo\.com\/api\/recite\/content-recommend\/v\d\/get-by-uid.+ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1257` | `^https?:\/\/recite\.perfectlingo\.com\/api\/recite\/floating-window\/v\d\/get-show.+ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1259` | `^https?:\/\/recpage-c\.qtfm\.cn\/v\d\/favorites$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:126` | `^https?:\/\/203\.107\.1\.33/\d+/ss - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1260` | `^https?:\/\/res1\.hubcloud\.com\.cn - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1261` | `^https?:\/\/res\.hongyibo\.com\.cn\/os\/gs\/resapi\/activity\/mget\?_t - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:127` | `^https?:\/\/203\.107\.1\.66/\d+/ss - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1270` | `^https?:\/\/res\.xiaojukeji\.com\/resapi\/activity\/mget - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1272` | `^https?:\/\/restapi\.iyunmai\.com\/api\/ios\/credit\/credit-family - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1273` | `^https?:\/\/restapi\.iyunmai\.com\/behaviour\/ios\/recommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1274` | `^https?:\/\/restapi\.iyunmai\.com\/fellow-service\/ios\/popUp - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1275` | `^https?:\/\/richmanrules\.ksedt\.com\/intellectWaterfallBidding\/find$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1276` | `^https?:\/\/richmanrules\.ksedt\.com\/intellectWaterfall\/find$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:128` | `^https?:\/\/203\.107\.1\.67/\d+/ss - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1282` | `^https?:\/\/s-api\.smzdm\.com\/sou\/popup_coupon\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1283` | `^https?:\/\/s-api\.smzdm\.com\/sou\/search_default_keyword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1284` | `^https?:\/\/s1\.api\.tv\.itc\.cn\/v\d\/mobile\/control\/switch\.json - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:129` | `^https?:\/\/203\.107\.1\.97/\d+/ss - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1291` | `^https?:\/\/saas\.hpplay\.cn\/api\/lebo-desk\/endpoint\/app-resource\/app-user-banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1292` | `^https?:\/\/saas\.hpplay\.cn\/api\/lebo-desk\/endpoint\/app-resource\/app_home_pop_up - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1293` | `^https?:\/\/saas\.hpplay\.cn\/api\/lebo-desk\/endpoint\/app-resource\/app_home_tips - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1294` | `^https?:\/\/saas\.hpplay\.cn\/api\/lebo-desk\/endpoint\/app-resource\/app_index_operate2 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1295` | `^https?:\/\/saas\.hpplay\.cn\/api\/lebo-rabbit\/app-card\/list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1296` | `^https?:\/\/sauron-report\.yonghuivip\.com\/collect - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1297` | `^https?:\/\/scan-order\.quark\.cn\/api\/member\/v1\/center\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1299` | `^https?:\/\/sdk1xyajs\.data\.kuiniuca\.com - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:13` | `^https?:\/\/(a\.athm\.cn\/)?mobile\.app\.autohome\.com\.cn\/platform\/carserver\/usercenter\/getoillist - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:130` | `^https?:\/\/2401:b180:2000:20::10\/\d+\/d - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1302` | `^https?:\/\/search\.qtfm\.cn\/v\d\/keyword\/default$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1304` | `^https?:\/\/service\.busi\.inke\.cn\/api\/flash\/screen - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1305` | `^https?:\/\/service\.haiersmarthomes\.com\/management\/banner\/getBannerList\?source=4 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1309` | `^https?:\/\/sfo\.mddcloud\.com\.cn\/api\/v\d\/sfo\/popup_displays? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:131` | `^https?:\/\/2401:b180:2000:30::1c\/\d+\/d - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1314` | `^https?:\/\/shopapi\.io\.mi\.com\/mtop\/mf\/resource\/homePage\/pageConfig - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1316` | `^https?:\/\/sichuan\.95504\.net\/v\d\/gd\/index\/get - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1321` | `^https?:\/\/smarket\.dian\.so - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1325` | `^https?:\/\/snailsleep\.net\/snail\/v\d\/screen\/qn\/get\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1327` | `^https?:\/\/sns\.api\.moji\.com\/user\/dynamic_v9\/json\/someone_interest\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1328` | `^https?:\/\/snsapi\.91160\.com\/engine\/backgroundWord\/queryForFrontend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1329` | `^https?:\/\/snsapi\.91160\.com\/hotword\/open\/v1\/getHotWordPlate\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:133` | `^https?:\/\/3g\.csair\.com\/CSMBP\/data\/homePage\/getLaunchInfoNew - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1330` | `^https?:\/\/snsapi\.91160\.com\/hotword\/open\/v1\/getSearchExplore\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1331` | `^https?:\/\/snsapi\.91160\.com\/vipmemberapi\/mbCombo\/mbComboWords\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1333` | `^https?:\/\/social\.blued\.cn\/users\/recommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1334` | `^https?:\/\/spamblocker-api\.zeekstudio\.com\/checkVersion - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1335` | `^https?:\/\/spamblocker-api\.zeekstudio\.com\/profile - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1341` | `^https?:\/\/squirrel\.kakamobi\.cn\/api\/open\/recommend-goods\/get-my-page-banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1344` | `^https?:\/\/ssp\.soulapp\.cn\/api\/q - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1345` | `^https?:\/\/st7niu\.aicarmap\.com\/st_?!(a2\|a3\|e9)\w+\.webp$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1364` | `^https?:\/\/stlib\.qbb6\.com\/wclt\/js\/core\/popup - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1365` | `^https?:\/\/support.you.163.com/appversync/check.do - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1366` | `^https?:\/\/support\.you\.163\.com\/xhr\/boot\/getBootMedia\.json - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1367` | `^https?:\/\/swallow\.kakamobi\.cn\/api\/open\/config\/get-config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1369` | `^https?:\/\/syt\.leshuazf\.com\/merchant\/merchant\/getBannerConfig$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:137` | `^https?:\/\/3g\.csair\.com\/extraClient\/data\/mytrip\/getMinPriceFlight - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1372` | `^https?:\/\/syt\.leshuazf\.com\/merchant\/popup\/getPopupInfo$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1373` | `^https?:\/\/sytgate\.jslife\.com\.cn\/base-gateway\/config\/queryAppNewVersion - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1374` | `^https?:\/\/sytgate\.jslife\.com\.cn\/data-report-gateway\/syt-data-report\/receive - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1375` | `^https?:\/\/szdmobile\.suzhou\.gov\.cn\/thirdapp-center\/appUpdate\/update - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1376` | `^https?:\/\/t1\.market\.xiaomi\.com\/thumbnail\/webp\/w1170q100\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1378` | `^https?:\/\/tagit\.hyhuo\.com\/recover\/list - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1381` | `^https?:\/\/tcmobileapi\.17usoft\.com\/backendActivity\/ori\/ordercenter\/recommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1382` | `^https?:\/\/tcmobileapi\.17usoft\.com\/foundation\/foundationHandler\.ashx - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1383` | `^https?:\/\/tcmobileapi\.17usoft\.com\/userextend\/member\/myIndex - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1388` | `^https?:\/\/tiance\.wps\.cn\/dce\/exec\/api\/market\/activity - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1389` | `^https?:\/\/tianqi\.2345\.com\/api\/content\/getContentFeeds\.php - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:139` | `^https?:\/\/3g\.csair\.com\/extraClient\/data\/preSelecteSeat\/xproduct\/getXProductList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1391` | `^https?:\/\/tingshu\.kuwo\.cn\/v2\/api\/pay\/user\/info - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1395` | `^https?:\/\/tower\.ubixioe\.com\/mob\/mediation - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:14` | `^https?:\/\/(a\.athm\.cn\/)?mobile\.app\.autohome\.com\.cn\/platform\/carserver\/usercenter\/getwashcarlist - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1401` | `^https?:\/\/ucmp\.sf-express\.com\/cx-wechat-query\/query\/info-flow\/reconsitution-list - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1402` | `^https?:\/\/ucmp\.sf-express\.com\/cx-wechat-query\/query\/module-config\/query - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1403` | `^https?:\/\/ucmp\.sf-express\.com\/proxy\/esgcempcore\/memberActLengthy\/fullGiveActivityService\/fullGiveInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1404` | `^https?:\/\/ucmp\.sf-express\.com\/proxy\/esgcempcore\/memberGoods\/pointMallService\/goodsList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1405` | `^https?:\/\/ucmp\.sf-express\.com\/proxy\/esgcempcore\/memberManage\/memberEquity\/queryRecommendEquity - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1409` | `^https?:\/\/us\.l\.qq\.com\/exapp - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1410` | `^https?:\/\/user-api\.smzdm\.com\/vip\/bottom_card_list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1411` | `^https?:\/\/user\.qtfm\.cn\/u\d\/api\/v\d\/user\/following_podcaster\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1412` | `^https?:\/\/userapi\.qiekj\.com\/appTitle\/get$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1413` | `^https?:\/\/userapi\.qiekj\.com\/integralGoods\/queryIntegralGoodsPage$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1415` | `^https?:\/\/userapi\.qiekj\.com\/local-life\/category$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1416` | `^https?:\/\/userapi\.qiekj\.com\/slot\/get$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1417` | `^https?:\/\/userapi\.qiekj\.com\/task\/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:142` | `^https?:\/\/3pp\.starbucks\.com\.cn\/wxmem\/index\/(?:banner\|global) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1421` | `^https?:\/\/vapp\.tmuyun\.com\/api\/app_start_page\/list\/new - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1422` | `^https?:\/\/vapp\.tmuyun\.com\/api\/buoy\/list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1427` | `^https?:\/\/venus\.yhd\.com\/memhome\/launchConfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1428` | `^https?:\/\/vip\d\.kuwo\.cn\/commercia\/vipconf\/projectPage\/getPageContent - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:143` | `^https?:\/\/3pp\.starbucks\.com\.cn\/wxmem\/popup - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1432` | `^https?:\/\/waimai-guide\.ele\.me\/(gw\|h5)\/mtop\.alsc\.eleme\.trigger\.respond - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1433` | `^https?:\/\/waimai-guide\.ele\.me\/h5\/mtop\.ele\.growth\.fission\.client\.etmd\.et\.getmainpageicon - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1434` | `^https?:\/\/wallpaper-\d+\.file\.myqcloud\.com\/dsl\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1435` | `^https?:\/\/wallpaper-\d+\.file\.myqcloud\.com\/hikari\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1436` | `^https?:\/\/wanciwangdata\.oss-cn-beijing\.aliyuncs\.com\/startup\/resource\/content.+ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1439` | `^https?:\/\/web2\.realtech-inc\.com\/oss\/xc-app-assets\/configs\/common\/theme\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1443` | `^https?:\/\/web\.yy\.com\/yyvoice_task_sys\/bar\.html\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1444` | `^https?:\/\/webcast-open\.douyin\.com\/webcast\/openapi\/feed\/\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1446` | `^https?:\/\/webchatapp\.fcbox\.com\/fcboxactivityweb\/api\/v\d\/clientPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1447` | `^https?:\/\/wechat\.tf\.cn\/mini-financial\/model\/queryPopup - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1448` | `^https?:\/\/weibointl\.api\.weibo\.cn\/portal\.php\?a=get_searching_info - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1449` | `^https?:\/\/wemallh5\.usmile\.com\/api\/sp-portal\/store\/usmile\/activity\/dayCheck\?pop - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1451` | `^https?:\/\/wnsaviator\.kg\.qq\.com\/wnsaviator\/api\/v1\/transMerge\?_webcgikey=get_activity_entry$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1454` | `^https?:\/\/www1\.elecfans\.com\/www\/delivery\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1455` | `^https?:\/\/www\.123pan\.com\/api\/config\/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1456` | `^https?:\/\/www\.1314zhilv\.com\/ltsstnew\/(guideScenic\/getRecentlyUpdatedScenic\|city\/getWeatherByCityName) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1457` | `^https?:\/\/www\.ahzs10000\.com\/palmhall\/client\/base\/newVerson_getStartUp\.action - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1461` | `^https?:\/\/www\.dpfile\.com\/app\/fecommonservice-lottie\/ugc-write-done\/media - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1463` | `^https?:\/\/www\.dpfile\.com\/sc\/indexpromotion - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1464` | `^https?:\/\/www\.duitang\.com\/napi\/hot\/search\/list\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1466` | `^https?:\/\/www\.flyert(rip)?\.com(\.cn)?\/.*\.php\?module=basicdata&type=appinfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1467` | `^https?:\/\/www\.gaoding\.com\/api\/v\d\/cp\/search-words\/v2\/placeholder - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1470` | `^https?:\/\/www\.gcores\.com\/gapi\/v1\/app-start-pages\?page - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1475` | `^https?:\/\/www\.kdocs\.cn\/kdg\/api\/v1\/cards\/type\/27\?iosVer=\d+\.\d+\.\d+&isGetList=1 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1476` | `^https?:\/\/www\.kdocs\.cn\/kdg\/api\/v1\/cards\/type\/3\?iosVer=\d+\.\d+\.\d+&isGetList=1 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1478` | `^https?:\/\/www\.kuaiduizuoye\.com\/activity\/init\/checkappconfig$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1480` | `^https?:\/\/www\.kuaiduizuoye\.com\/kdapi\/conf\/appbannersv3$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1481` | `^https?:\/\/www\.kuaiduizuoye\.com\/kdapi\/conf\/initbanner$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1483` | `^https?:\/\/www\.linkedin\.com\/voyager\/api\/voyagerConfiguration - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1485` | `^https?:\/\/www\.msccruises\.com\.cn\/checkinapi\/common\/getPopUp - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1487` | `^https?:\/\/www\.myusmile\.online\/user\/userTagRecord\/popup - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1488` | `^https?:\/\/www\.okx\.com\/v\d\/support\/home\/app\/updateInfo - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1493` | `^https?:\/\/www\.terabox\.com\/api\/page\/tips\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1494` | `^https?:\/\/www\.terabox\.com\/rest\/1\.0\/task\/common\/inttips\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1495` | `^https?:\/\/www\.upwork\.com\/api\/v\d\/client-app-config\/platform\/ios\/app\/freelancer\/version - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1496` | `^https?:\/\/www\.xiaohongshu\.com\/api\/marketing\/box\/trigger\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1498` | `^https?:\/\/www\.xiaoxiongmeishu\.com\/api\/(home\/v1\/config\/appInit\|s\/v1\/popup\/createCouponPopup) - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1501` | `^https?:\/\/www\.zhihu\.com\/api\/v4\/hot_recommendation - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1502` | `^https?:\/\/www\.zhihu\.com\/api\/v4\/mcn\/v2\/linkcards\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1503` | `^https?:\/\/www\.zhihu\.com\/api\/v4\/search\/related_queries\/(?:article\|answer)\/\d+ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1504` | `^https?:\/\/www\.zhihu\.com\/appview\/v3\/zhmore - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1505` | `^https?:\/\/www\.zhihu\.com\/commercial_api\/banners_v3\/mobile_banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1506` | `^https?:\/\/wx(app)?\.api\.ke\.com\/pt\/platform\/platform\/shellxcx\/homepage\/popup - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1507` | `^https?:\/\/wx(app)?\.api\.ke\.com\/pt\/pt-xcx\/boot\/ping - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1509` | `^https?:\/\/wx\.17u\.cn\/homemarketapi\/(aggregator\/index\|search\/recommend) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1510` | `^https?:\/\/wx\.17u\.cn\/membermessageuserapi\/(message\/list\|category\/getCategory) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1511` | `^https?:\/\/wx\.17u\.cn\/mytourapi\/blankpage\/recommendList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1512` | `^https?:\/\/wx\.17u\.cn\/mytourapi\/mytrip\/(?:blankflight\|toptips) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1513` | `^https?:\/\/wx\.17u\.cn\/mytourapi\/recommendation\/arriveCity - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1515` | `^https?:\/\/wx\.17u\.cn\/vacation\/webapp\/tailor\/miniHomeConfig - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1516` | `^https?:\/\/wx\.17u\.cn\/wireless\/monitor\/wx\/common\/compressevent - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1518` | `^https?:\/\/wx\.17u\.cn\/xcxhomeapi\/((aggregator\/index)\|(home\/(?:screen\|banner\|converge)))$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1519` | `^https?:\/\/wx\.bthhotels\.com\/miniapp\/weixin\/v\d\/home\/index_banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1520` | `^https?:\/\/wx\.maoyan\.com\/maoyansh\/api\/mobile\/(?:hotMatchList\|eSportsIps) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1522` | `^https?:\/\/wx\.maoyan\.com\/maoyansh\/myshow\/ajax\/celebrityBasicList\/query - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1523` | `^https?:\/\/wx\.maoyan\.com\/maoyansh\/myshow\/ajax\/movie\/wonderShow - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1524` | `^https?:\/\/wx\.maoyan\.com\/maoyansh\/myshow\/ajax\/performances\/calendar\/0 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1525` | `^https?:\/\/wx\.maoyan\.com\/maoyansh\/myshow\/ajax\/performances\/rob\/main - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1526` | `^https?:\/\/wx\.maoyan\.com\/maoyansh\/myshow\/ajax\/recommend\/performances - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1529` | `^https?:\/\/xhtz.oss-cn-guangzhou\.aliyuncs\.com\/home\/member\/.+\.png$ - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:153` | `^https?:\/\/\w+\.sh\.wxgateway\.com\/xcxhomeapi\/((aggregator\/index)\|(home\/(?:screen\|banner\|converge)))$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1530` | `^https?:\/\/xiaoshuo\.wtzw\.com\/api\/v\d\/withdraw\/init - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1531` | `^https?:\/\/xxyx-client-api\.xiaoxiaoyouxuan\.com\/\w+_banner - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1532` | `^https?:\/\/xxyx-client-api\.xiaoxiaoyouxuan\.com\/activity\/show - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1534` | `^https?:\/\/xxyx-client-api\.xiaoxiaoyouxuan\.com\/client\/invite\/phone\/activity\/popup - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1535` | `^https?:\/\/xxyx-client-api\.xiaoxiaoyouxuan\.com\/client\/urban\/activity\/index\/data - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1538` | `^https?:\/\/xyz\.cnki\.net\/resourcev7\/api\/manualpush\/SlidsList$ - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:154` | `^https?:\/\/a\.athm\.cn\/clientlive\.api\.autohome\.com\.cn\/api\/live\/getserieswindowsinfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1542` | `^https?:\/\/yanxuan\.nosdn\.127\.net\/.*\.mp4 - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1549` | `^https?:\/\/yun\.tuitiger\.com\/mami-media - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:155` | `^https?:\/\/a\.sinopecsales\.com\/app\/cms - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1550` | `^https?:\/\/yunmk\.feidee\.net\/cab-market-ws\/market\/v2\/contents$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1551` | `^https?:\/\/yuyin-api\.baizhanlive\.com\/homepage\/flashscreen\/get\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1552` | `^https?:\/\/yuyin-api\.baizhanlive\.com\/homepage\/homepage\/banner\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1553` | `^https?:\/\/yuyin-api\.baizhanlive\.com\/search\/search\/hotword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1555` | `^https?:\/\/yyapp-act-entrance\.yy\.com\/entrance\/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1556` | `^https?:\/\/yyapp-fastnet\.yy\.com\/dispatch\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1558` | `^https?:\/\/zconfig\.alibabausercontent\.com\/zconfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1559` | `^https?:\/\/zhuanlan\.zhihu\.com\/api\/articles\/\d+\/recommendation - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:156` | `^https?:\/\/aag\.enmonster\.com\/apa(\/discount)?\/activity - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1562` | `^https?:\/\/zj\.haier\.net\/api-gw\/shpmResource\/servicePage\/visualize\/recommend\?dataType - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1563` | `^https?:\/\/zj\.haier\.net\/api-gw\/shpmResource\/servicePage\/weather\/query\?areaId - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1564` | `^https?:\/\/zj\.haier\.net\/api-gw\/upmapi\/appmanage\/publish\/getRecommendVersion$ - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1566` | `^https?:\/\/zj\.haier\.net\/omsappapi\/resource\/v\d\/resBagList$ - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1567` | `^https?:\/\/zj\.haier\.net\/omssceneapi\/house\/v\d\/recommend\/listByRoom$ - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1568` | `^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/common\/getWeworkCategoryPromotionInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1569` | `^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/common\/getWeworkPromotionInfoBySceneType - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1570` | `^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/manualOperationGoods\/pageManualOperationGoods - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1571` | `^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/personal\/getPersonPageInfo\.do - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1573` | `^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/specialSale\/listSpecialSalePageBanner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1574` | `^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/specialSale\/pageRecommendedItems - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1575` | `^https?:\/\/zone\.guiderank-app\.com\/guiderank-web\/app\/stockTaking\/pageStockTakingForHomePage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:1579` | `^https?:\/\/zyfile\.izuiyou\.com\/zyfile\/c2\/a0\/[a-z0-9-]+\.json - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:159` | `^https?:\/\/access.mypikpak.com/access_controller/v1/area_accessible - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:16` | `^https?:\/\/(apissl\|az\d-api(-js\|-idc)?)\.(gifshow\|ksapisrv)\.com\/rest\/n\/live\/feed\/info\/simplelive\/card\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:160` | `^https?:\/\/acs\.m\.goofish\.com\/gw\/mtop\.taobao\.idle\.item\.buy\.feeds\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:161` | `^https?:\/\/acs\.m\.goofish\.com\/gw\/mtop\.taobao\.idle\.item\.recommend\.list\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:162` | `^https?:\/\/acs\.m\.goofish\.com\/gw\/mtop\.taobao\.idle\.local\.near\.by\.corner\.info\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:163` | `^https?:\/\/acs\.m\.goofish\.com\/gw\/mtop\.taobao\.idle\.playboy\.recommend\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:164` | `^https?:\/\/acs\.m\.goofish\.com\/gw\/mtop\.taobao\.idle\.user\.strategy\.list\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:169` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.alimusic\.common\.mobileservice\.startinit - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:17` | `^https?:\/\/(apissl\|az\d-api(-js\|-idc)?)\.(gifshow\|ksapisrv)\.com\/rest\/n\/nearby\/widget\/info\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:170` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.damai\.mec\.popup\.get\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:171` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.damai\.wireless\.home\.welcome\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:173` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.film\.life\.popup\.get\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:177` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.fliggy\.crm\.screen\.(allresource\|predict) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:178` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.fliggy\.crm\.screen\.allresource\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:179` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.fliggy\.crm\.screen\.predict\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:18` | `^https?:\/\/(apissl\|az\d-api(-js\|-idc)?)\.(gifshow\|ksapisrv)\.com\/rest\/n\/taskCenter\/task\/report\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:180` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.fliggy\.recommend\.common\.guess\.tab\.feeds\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:181` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.fliggy\.tripzoo\.new\.couponlist\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:183` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.taobao\.idle\.home\.welcome - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:184` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.trip\.activity\.querytmsresources - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:185` | `^https?:\/\/acs\.m\.taobao\.com\/gw\/mtop\.trip\.my\.recommendcard\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:188` | `^https?:\/\/activity\.yonghuivip\.com\/api\/app\/fp\/homepage\/pop - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:19` | `^https?:\/\/(api\|api-bk\d+)\.tv\.sohu\.com\/agg\/api\/app\/config\/bootstrap - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:222` | `^https?:\/\/alt-r\.my\.com\/mobile - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:225` | `^https?:\/\/ap\.dongdianqiu\.com\/plat\/v4 - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:226` | `^https?:\/\/apapia-sqk\.manmanbuy\.com\/index_json\.ashx$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:228` | `^https?:\/\/api(5-lq)?\.pipix\.com\/bds\/banner\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:229` | `^https?:\/\/api(5-lq)?\.pipix\.com\/bds\/feed\/follow_feed\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:23` | `^https?:\/\/(beta-luna\.douyin\|api5-lq\.qishui)\.com\/luna\/activities\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:230` | `^https?:\/\/api-2\.duitang\.com\/napi\/vienna\/daren\/daren\/recommend\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:232` | `^https?:\/\/api-ac\.liepin\.com\/api\/com\.liepin\.pupa\.discover\.click-tab - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:235` | `^https?:\/\/api-bc\.wtzw\.com\/api\/v4\/search\/dispose - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:236` | `^https?:\/\/api-bc\.wtzw\.com\/api\/v\d\/book-store\/config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:237` | `^https?:\/\/api-bc\.wtzw\.com\/api\/v\d\/book-store\/push-book - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:238` | `^https?:\/\/api-bc\.wtzw\.com\/api\/v\d\/operation - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:243` | `^https?:\/\/api-cfg\.wtzw\.com\/v\d\/reward\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:246` | `^https?:\/\/api-changzheng\.chinaath\.com\/changzheng-basic-center-api\/api\/appConfigBanner\/listBannerRelease\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:247` | `^https?:\/\/api-changzheng\.chinaath\.com\/changzheng-content-center-api\/api\/global\/search\/hotSearch\/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:248` | `^https?:\/\/api-cslp-emt\.amazon\.cn\/gateway\/(?:recommend\|content\/widget\/popup\|config\/getUpdatePopupConfig) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:249` | `^https?:\/\/api-gw\.wtzw\.com\/welf\/app\/v\d\/task\/red-packet - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:25` | `^https?:\/\/(beta-luna\.douyin\|api5-lq\.qishui)\.com\/luna\/commerce\/upsells\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:252` | `^https?:\/\/api-marketing\.zhinengxiyifang\.cn\/api\/v2\/cloudcode\/wechat\/bid - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:255` | `^https?:\/\/api-new\.app\.acfun\.cn\/rest\/app\/flash\/screen\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:257` | `^https?:\/\/api-wanda\.liepin\.com\/api\/com\.liepin\.cbp\.baizhong\.op\.v\d-show-4app - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:258` | `^https?:\/\/api.xiaoyi.com\/v5\/app\/config\?userid=.* - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:26` | `^https?:\/\/(beta-luna\.douyin\|api5-lq\.qishui)\.com\/luna\/commerce\/upsells_config\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:260` | `^https?:\/\/api1\.zongheng\.com\/iosapi\/system\/startup$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:263` | `^https?:\/\/api2\.zongheng\.com\/api\/giftBag\/bindingBag$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:268` | `^https?:\/\/api\.17gwx\.com\/v2\/growth\/popup\/remind$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:269` | `^https?:\/\/api\.17gwx\.com\/v2\/homepage\/feed\/similarList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:27` | `^https?:\/\/(beta-luna\.douyin\|api5-lq\.qishui)\.com\/luna\/commerce\/v2\/commerce_info\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:270` | `^https?:\/\/api\.17gwx\.com\/v2\/recommend\/feed\/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:276` | `^https?:\/\/api\.babytree\.com\/preg_intf\/index_content\/index_banner - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:277` | `^https?:\/\/api\.bevol\.com\/appmain\/app\/home\/launch$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:278` | `^https?:\/\/api\.bevol\.com\/appmain\/app\/home\/popup$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:279` | `^https?:\/\/api\.bevol\.com\/personal\/page$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:280` | `^https?:\/\/api\.bevol\.com\/seach\/foundAndTopSearch$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:284` | `^https?:\/\/api\.boohee\.com\/app-interface\/v\d\/search\/search\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:285` | `^https?:\/\/api\.boohee\.com\/meta-interface\/v\d\/index\/(?:discover_chosen\|page_float_bubbles\|sensor-banners\|tool_buttons) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:286` | `^https?:\/\/api\.boohee\.com\/shop-interface\/api\/v\d\/home\/index - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:289` | `^https?:\/\/api\.bwton\.com\/bff\/app\/index\/goods - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:290` | `^https?:\/\/api\.bwton\.com\/bff\/app\/index\/recommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:292` | `^https?:\/\/api\.cc\.163\.com\/v1\/mpopuprecommend\/exit_room_conf$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:296` | `^https?:\/\/api\.coolapk\.com\/v6\/search\?.*type=hotSearch - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:297` | `^https?:\/\/api\.dangdang\.com\/mapi\d\/mobile\/init - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:30` | `^https?:\/\/(beta-luna\.douyin\|api5-lq\.qishui)\.com\/luna\/treasure\/entrance\/config\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:300` | `^https?:\/\/api\.feidee\.net\/v1\/configs\/client\/configs - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:303` | `^https?:\/\/api\.futunn\.com\/treasure-chest\/box-data - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:304` | `^https?:\/\/api\.futunn\.com\/v2\/config\/promote-config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:305` | `^https?:\/\/api\.futunn\.com\/v2\/optimus\/my-homepage-config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:309` | `^https?:\/\/api\.gotokeep\.com\/guide-webapp\/v1\/popup\/getPopUp\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:311` | `^https?:\/\/api\.gotokeep\.com\/search\/v4\/hotHashtag\/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:312` | `^https?:\/\/api\.gotokeep\.com\/search\/v4\/hotword\/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:313` | `^https?:\/\/api\.gotokeep\.com\/search\/v5\/hotCourse\/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:314` | `^https?:\/\/api\.gotokeep\.com\/search\/v6\/default\/keyword\/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:315` | `^https?:\/\/api\.gotokeep\.com\/twins\/union\/feed\/function\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:316` | `^https?:\/\/api\.gotokeep\.com\/twins\/v4\/feed\/followPage\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:317` | `^https?:\/\/api\.hanju\.koudaibaobao\.com\/api\/carp\/kp\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:319` | `^https?:\/\/api\.hellobike\.com\/api\?applet\.homepage\.medal\.activity - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:323` | `^https?:\/\/api\.huachenjie\.com\/run-front\/ai\/getAICategory - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:324` | `^https?:\/\/api\.huachenjie\.com\/run-front\/home\/sports\/getPopup - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:325` | `^https?:\/\/api\.indeedpower\.com\/v1\/m\/edu\/module\/homepage_banner\/\?randomStr - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:329` | `^https?:\/\/api\.izuiyou\.com\/config\/get_banner - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:330` | `^https?:\/\/api\.jiahui\.com\/app-rest\/app\/notice\/getAppNotice - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:331` | `^https?:\/\/api\.jr\.mi\.com\/jr\/api\/playScreen - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:336` | `^https?:\/\/api\.kmovie\.gifshow\.com\/rest\/n\/kmovie\/app\/banner\/common\/getBannerByType\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:338` | `^https?:\/\/api\.kmovie\.gifshow\.com\/rest\/n\/kmovie\/app\/resource\/activity\/pendant\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:339` | `^https?:\/\/api\.kmovie\.gifshow\.com\/rest\/n\/kmovie\/app\/resource\/get\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:340` | `^https?:\/\/api\.kurobbs\.com\/config\/getOpenScreen$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:341` | `^https?:\/\/api\.kurobbs\.com\/config\/index\/windows$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:342` | `^https?:\/\/api\.kurobbs\.com\/config\/search\/getSearchConfig\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:345` | `^https?:\/\/api\.live\.bilibili\.com\/xlive\/e-commerce-interface\/v1\/ecommerce-user\/get_shopping_info\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:348` | `^https?:\/\/api\.m\.mi\.com\/v\d\/app\/popup_info$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:349` | `^https?:\/\/api\.m\.mi\.com\/v\d\/app\/start - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:350` | `^https?:\/\/api\.m\.mi\.com\/v\d\/home\/page_feed(_v5)?$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:351` | `^https?:\/\/api\.m\.mi\.com\/v\d\/misearch\/search_input$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:352` | `^https?:\/\/api\.m\.mi\.com\/v\d\/search\/search_default$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:353` | `^https?:\/\/api\.maoyan\.com\/sns\/common\/feed\/channel\/v\d\/list\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:356` | `^https?:\/\/api\.meiyan\.com\/operation\/home_banner\.json\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:357` | `^https?:\/\/api\.meiyan\.com\/vip\/permission_update_popup\.json\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:363` | `^https?:\/\/api\.nj\.nbtv\.cn\/v\d\/common\/system-boot-inform\/detail - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:364` | `^https?:\/\/api\.petkit\.cn\/6\/\/device\/relatedProductsInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:365` | `^https?:\/\/api\.pinduoduo\.com\/api\/alexa\/goods\/back_up\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:366` | `^https?:\/\/api\.pinduoduo\.com\/api\/aquarius\/hungary\/global\/homepage\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:367` | `^https?:\/\/api\.pinduoduo\.com\/api\/aristotle\/query_order_list_tabs_element\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:368` | `^https?:\/\/api\.pinduoduo\.com\/api\/aristotle\/unrated_order_for_unreceived_tab\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:369` | `^https?:\/\/api\.pinduoduo\.com\/api\/brand-olay\/goods_detail\/bybt_guide\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:370` | `^https?:\/\/api\.pinduoduo\.com\/api\/buffon\/nasus\/recommend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:371` | `^https?:\/\/api\.pinduoduo\.com\/api\/caterham\/v3\/query\/likes\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:372` | `^https?:\/\/api\.pinduoduo\.com\/api\/caterham\/v3\/query\/my_order_group\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:373` | `^https?:\/\/api\.pinduoduo\.com\/api\/caterham\/v3\/query\/new_chat_group\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:374` | `^https?:\/\/api\.pinduoduo\.com\/api\/caterham\/v3\/query\/order_express_group\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:375` | `^https?:\/\/api\.pinduoduo\.com\/api\/caterham\/v3\/query\/personal\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:376` | `^https?:\/\/api\.pinduoduo\.com\/api\/dunkirk\/liveactivity\/push\/create\/url\/report\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:377` | `^https?:\/\/api\.pinduoduo\.com\/api\/engels\/reviews\/require\/append\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:378` | `^https?:\/\/api\.pinduoduo\.com\/api\/engels\/wait\/receive\/review\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:379` | `^https?:\/\/api\.pinduoduo\.com\/api\/growth\/nagato\/app\/index\/gather\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:380` | `^https?:\/\/api\.pinduoduo\.com\/api\/ktt_gateway\/activity\/feeds\/personal_home_page\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:381` | `^https?:\/\/api\.pinduoduo\.com\/api\/manufacturer\/cross\/shortcut\/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:382` | `^https?:\/\/api\.pinduoduo\.com\/api\/phantom\/gbdbpdv\/extra\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:383` | `^https?:\/\/api\.pinduoduo\.com\/api\/zaire_biz\/chat\/resource\/get_list_data\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:384` | `^https?:\/\/api\.pinduoduo\.com\/search_hotquery\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:387` | `^https?:\/\/api\.psy-1\.com\/cosleep\/startup - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:389` | `^https?:\/\/api\.qbb6\.com\/baby\/and\/litclass\/list\/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:390` | `^https?:\/\/api\.qbb6\.com\/baby\/relative\/visited - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:391` | `^https?:\/\/api\.qbb6\.com\/commons\/check\/app\/update - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:392` | `^https?:\/\/api\.qbb6\.com\/commons\/self\/button\/group\/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:393` | `^https?:\/\/api\.qbb6\.com\/commons\/testflight\/check\/update - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:394` | `^https?:\/\/api\.qbb6\.com\/commons\/widget\/info\/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:395` | `^https?:\/\/api\.qbb6\.com\/mamiyin\/large\/view\/get - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:397` | `^https?:\/\/api\.qbb6\.com\/timeline\/item\/list\/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:398` | `^https?:\/\/api\.ring\.kugou\.com\/user\/notice\/recommend$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:400` | `^https?:\/\/api\.sfacg\.com\/ioscfg - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:401` | `^https?:\/\/api\.shanghaionstar\.com\/sos\/contentinfo\/v1\/public\/landingpage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:402` | `^https?:\/\/api\.sodalife\.xyz\/hydr\/v\d\/poster\/posters - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:403` | `^https?:\/\/api\.sodalife\.xyz\/v\d\/goods - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:404` | `^https?:\/\/api\.sodalife\.xyz\/v\d\/posters\?location=SODA_APP%3AHOME%3ABOTTOM - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:405` | `^https?:\/\/api\.sodalife\.xyz\/v\d\/posters\?location=SODA_APP%3AHOME%3ACENTER - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:406` | `^https?:\/\/api\.sodalife\.xyz\/v\d\/posters\?location=SODA_APP%3AHOME%3ATOP - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:407` | `^https?:\/\/api\.sodalife\.xyz\/v\d\/posters\?location=SODA_APP%3AMINE%3ABOTTOM - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:408` | `^https?:\/\/api\.sodalife\.xyz\/v\d\/posters\?location=SODA_APP%3AREWARDS%3ACENTER - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:410` | `^https?:\/\/api\.songguo7\.com\/(\w{3})?mp\/v\d\/misc\/(?:toast\|user_operate_info\|unlock_without_order\|unlock_operate_info) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:418` | `^https?:\/\/api\.ulife\.group\/market\/memberCard\/listMemberCard\?isShowSecondaryCard=1 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:424` | `^https?:\/\/api\.weibo\.cn\/2\/cardlist\?v_f=2 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:425` | `^https?:\/\/api\.wfdata\.club\/v2\/yesfeng\/yesList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:427` | `^https?:\/\/api\.wmpvp\.com\/api\/v\d\/config\/promote - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:428` | `^https?:\/\/api\.xbxxhz\.com\/big_data\/v1\/home_pages - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:431` | `^https?:\/\/api\.xiachufang\.com\/v2\/homepage1810\/init_page\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:432` | `^https?:\/\/api\.xiachufang\.com\/v2\/mark_mission\/get_sticker_info\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:435` | `^https?:\/\/api\.xiaoyuzhoufm\.com\/v\d\/ai - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:436` | `^https?:\/\/api\.xiaoyuzhoufm\.com\/v\d\/category - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:437` | `^https?:\/\/api\.xiaoyuzhoufm\.com\/v\d\/flash - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:438` | `^https?:\/\/api\.xiaoyuzhoufm\.com\/v\d\/search\/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:442` | `^https?:\/\/api\.yikaobang\.com\.cn\/index\.php\/Client\/main\/startPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:443` | `^https?:\/\/api\.yikaobang\.com\.cn\/index\.php\/version\/version\/check - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:444` | `^https?:\/\/api\.yonghuivip\.com\/api\/fp\/homepage\/pop - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:447` | `^https?:\/\/api\.ys7\.com\/v3\/config\/service\/entrance\/bannerInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:448` | `^https?:\/\/api\.ys7\.com\/v3\/configurations\/gray\/info\?grayTypes=185 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:449` | `^https?:\/\/api\.ys7\.com\/v3\/intelligent-app\/apps\/linkage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:451` | `^https?:\/\/api\.zhihu\.com\/(?:bazaar\/float_window\|market\/popovers_v2) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:453` | `^https?:\/\/api\.zhihu\.com\/ab\/api\/v1\/products\/zhihu\/platforms\/ios\/config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:456` | `^https?:\/\/api\.zhihu\.com\/commercial_api\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:457` | `^https?:\/\/api\.zhihu\.com\/content-distribution-core\/bubble\/common\/settings - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:459` | `^https?:\/\/api\.zhihu\.com\/me\/guides - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:460` | `^https?:\/\/api\.zhihu\.com\/people\/homepage_entry_v2 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:461` | `^https?:\/\/api\.zhihu\.com\/prague\/related_suggestion_native\/feed\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:462` | `^https?:\/\/api\.zhihu\.com\/root\/window - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:463` | `^https?:\/\/api\.zhihu\.com\/search\/(hot_search\|preset_words) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:464` | `^https?:\/\/api\.zhihu\.com\/unlimited\/go\/my_card - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:466` | `^https?:\/\/api\.zhuishushenqi\.com\/notification\/shelfMessage - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:468` | `^https?:\/\/api\.zhuishushenqi\.com\/user\/bookshelf-updated - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:47` | `^https?:\/\/(client\.)?app(\.coc)?\.10086\.cn\/biz-orange\/DN\/emotionMarket - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:478` | `^https?:\/\/apipt\.qbb6\.com\/parenting\/pt\/home\/post\/card\/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:479` | `^https?:\/\/apis.lifeweek.com.cn/api/baseConfig/getIosNewConfig - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:480` | `^https?:\/\/apivip\.kuaiduizuoye\.com\/viponline\/scancode\/mycard$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:484` | `^https?:\/\/apm-ios\.zhipin\.com\/api\/zpApm\/ios\/gray\/release\/check - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:486` | `^https?:\/\/app-api\.smzdm\.com\/mychannel\/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:489` | `^https?:\/\/app-gw\.csdn\.net\/abtesting\/v2\/getList? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:49` | `^https?:\/\/(client\.)?app(\.coc)?\.10086\.cn\/biz-orange\/DN\/init\/startInit - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:493` | `^https?:\/\/app\.10099\.com\.cn\/contact-web\/api\/version\/getFlashScreenPage - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:50` | `^https?:\/\/(discardrp\|startup)\.umetrip\.com\/gateway\/api\/umetrip\/native - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:503` | `^https?:\/\/app\.chengfenmiao\.com\/Helper\/HotWords\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:504` | `^https?:\/\/app\.chengfenmiao\.com\/Listing\/LiveHots\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:505` | `^https?:\/\/app\.chengfenmiao\.com\/helper\/VersionCheck\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:506` | `^https?:\/\/app\.chengfenmiao\.com\/item\/closet\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:509` | `^https?:\/\/app\.dewu\.com\/api\/v1\/app\/search\/lexicon\/v1\/rank_words\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:510` | `^https?:\/\/app\.dewu\.com\/api\/v1\/app\/search\/lexicon\/v3\/background_words\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:511` | `^https?:\/\/app\.dewu\.com\/hacking-newbie\/v1\/app\/coupon\/module\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:512` | `^https?:\/\/app\.dewu\.com\/sns-rec\/v1\/attention\/feed\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:513` | `^https?:\/\/app\.dewu\.com\/sns-rec\/v1\/search\/hotword-list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:514` | `^https?:\/\/app\.dewu\.com\/sns-rec\/v1\/search\/word-skip\/new-list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:515` | `^https?:\/\/app\.flymodem\.com\.cn\/Appapi\/Public\/welecome - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:516` | `^https?:\/\/app\.hbooker\.com\/setting\/get_startpage_url_list - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:517` | `^https?:\/\/app\.home\.360\.cn\/v1\/config\/custom_config - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:518` | `^https?:\/\/app\.homeinns\.com\/api\/v\d\/(?:index\|local) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:520` | `^https?:\/\/app\.missevan\.com\/x\/recommend\/get-popup$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:521` | `^https?:\/\/app\.mval\.qq\.com\/go\/customize_search\/article_rank\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:522` | `^https?:\/\/app\.mval\.qq\.com\/go\/customize_search\/article_rank_tab\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:523` | `^https?:\/\/app\.mval\.qq\.com\/go\/mlol_news\/search\/varcache_hotV\d\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:524` | `^https?:\/\/app\.mval\.qq\.com\/go\/recommend\/platflashbox\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:526` | `^https?:\/\/app\.qtfm\.cn\/m-bff\/v\d\/i_listen\/guess_you_like\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:527` | `^https?:\/\/app\.qtfm\.cn\/recommendapi\/v\d\/emotion$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:531` | `^https?:\/\/app\.xinpianchang\.com\/open_screen\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:533` | `^https?:\/\/app\.zhuanzhuan\.com\/zz\/v2\/zzinfoshow\/getwindvanecardv2$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:535` | `^https?:\/\/app\.zhuanzhuan\.com\/zz\/v2\/zzusercenter\/myprofilevariouscards$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:536` | `^https?:\/\/app\.zhuanzhuan\.com\/zzopen\/popwindow\/getallpopwin\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:538` | `^https?:\/\/app\.zhuanzhuan\.com\/zzopen\/ypmall\/listData$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:541` | `^https?:\/\/appapi\.51jobapp\.com\/api\/market\/get_launch\.php\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:542` | `^https?:\/\/appapi\.caiyicloud\.com\/cyy_gatewayapi\/home\/pub\/v3\/banners\/app_start_page - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:543` | `^https?:\/\/appapi\.cc\.163\.com\/v\d\/mixfloatingwindow\/floating_windows\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:544` | `^https?:\/\/appapi\.huazhu\.com:\d+\/client\/app\/getAppStartPage\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:545` | `^https?:\/\/appc-v6\.qixin\.com\/v4\/enterprise\/getRecommendEnts$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:546` | `^https?:\/\/appc-v6\.qixin\.com\/v4\/enterprise\/getRecommendation$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:547` | `^https?:\/\/appc-v6\.qixin\.com\/v4\/enterprise\/homePageRecommend\/recommendCard\d+ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:548` | `^https?:\/\/appc-v6\.qixin\.com\/v4\/general\/getAppBanners$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:549` | `^https?:\/\/appc-v6\.qixin\.com\/v4\/general\/getAppBottomBanners$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:551` | `^https?:\/\/appc-v6\.qixin\.com\/v4\/user\/getRecommendPersons$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:552` | `^https?:\/\/appc-v6\.qixin\.com\/v4\/user\/getUserActivitys$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:553` | `^https?:\/\/appc\.qixin\.com\/v4\/general\/getSearchPlaceholderRedirect$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:554` | `^https?:\/\/appcloud2\.zhihu\.com\/v3\/resource\?group_name=mp - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:555` | `^https?:\/\/appconf\.mail\.163\.com\/mailmaster\/api\/http\/urlConfig\.do$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:556` | `^https?:\/\/appconf\.mail\.163\.com\/mailoperating\/mailmaster\/api\/operator\/get$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:56` | `^https?:\/\/(h3\.)?open\.taou\.com\/maimai\/go_gossip_darwin\/external\/v\d\/query_flow_cards - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:562` | `^https?:\/\/appi\.kuwo\.cn\/kuwopay\/personal\/cells - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:564` | `^https?:\/\/apps\.api\.ke\.com\/config\/config\/bootpage\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:565` | `^https?:\/\/apps\.api\.ke\.com\/config\/config\/getactivityconfig\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:566` | `^https?:\/\/apps\.api\.ke\.com\/platform\/shellapp\/userCenter\/feed\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:57` | `^https?:\/\/(h3\.)?open\.taou\.com\/maimai\/pay\/v\d\/check_gift - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:576` | `^https?:\/\/article-api\.smzdm\.com\/publish\/get_bubble\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:577` | `^https?:\/\/as\.xiaojukeji\.com\/ep\/as\/conf\?ns=daijia-front&name= - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:579` | `^https?:\/\/autoapi\.autohome\.com\.cn\/arvr-dealercloud-api\/online\/aggregation\/exhibitionList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:580` | `^https?:\/\/autoapi\.autohome\.com\.cn\/ypttd\/yjc\/web\/mkgt\/act\/seckillInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:585` | `^https?:\/\/backservice\.offerxiansheng\.com\/api\/backend-service\/bkd\/version-control\/new-version - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:587` | `^https?:\/\/bbs-api(-ab)?\.miyoushe\.com\/apihub\/api\/getHotKeywordAndEvent$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:590` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/pay\/h5\/common\/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:591` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/pay\/vip\/invitation\/assist\/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:592` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/pay\/vip\/invitation\/swell\/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:593` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/pay\/vip\/lowPriceText\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:594` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/popup\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:595` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/service\/banner\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:596` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/service\/global\/config\/vipEnter\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:597` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/service\/home\/module\?.*&moduleId=6 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:598` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/service\/version\/popup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:599` | `^https?:\/\/bd-api\.kuwo\.cn\/api\/ucenter\/vip\/give\/config\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:60` | `^https?:\/\/(info\.mina\.xiaoaisound\|marketing-aibox\.v\.mitvos)\.com\/payGuide\/userCenter - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:601` | `^https?:\/\/bgw\.xinyue\.qq\.com\/xyapi\.PageService\/GetIndexPopFlash - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:605` | `^https?:\/\/bohe\.sfo-tx-shanghai-01\.saas\.sensorsdata\.cn\/api\/v\d\/sfo\/user_popup_configs - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:606` | `^https?:\/\/booking\.bestwehotel\.com\/proxy\/trip-hotel-banner\/activity\/getActivityInfo - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:609` | `^https?:\/\/buy\.line\.me\/api\/graphql\?variables - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:61` | `^https?:\/\/(info\.mina\.xiaoaisound\|marketing-aibox\.v\.mitvos)\.com\/popup - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:610` | `^https?:\/\/c\.m\.163\.com\/nc\/gl\/ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:62` | `^https?:\/\/(ios\|android)\.sogou\.com/[^/]+/sogou_input_[^/]+/[^/]+/index\.html - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:625` | `^https?:\/\/ccsp-egmas\.sf-express\.com\/cx-app-base\/base\/app\/bms\/queryRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:646` | `^https?:\/\/cds\.wifi188\.com\/feeds\.sec - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:647` | `^https?:\/\/chat-live\.soulapp\.cn\/live\/planet\/recListV\d - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:649` | `^https?:\/\/cheyouquan\.kakamobi\.com\/api\/open\/group\/recommend-subscribe-tag - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:65` | `^https?:\/\/(m2u-api\.getkwai\|api-m2u\.kuaishou)\.com\/api-server\/api\/v4\/op\/actPositions\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:652` | `^https?:\/\/circle\.(xm)?seeyouyima\.com\/v\d\/article_recommend\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:653` | `^https?:\/\/cix\.line-apps\.com\/R4\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:655` | `^https?:\/\/client-lz\.rili\.cn\/lizhi\/api\/album\/hl_card\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:657` | `^https?:\/\/client-lz\.rili\.cn\/lizhi\/api\/fortune\/overview\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:658` | `^https?:\/\/client-lz\.rili\.cn\/lizhi\/api\/fortune\/question_spots\/panel\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:659` | `^https?:\/\/client-lz\.rili\.cn\/lizhi\/api\/jujia\/flow\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:66` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/app-skin-service\/skin\/setting\/info\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:662` | `^https?:\/\/client\.tujia\.com\/bnbapp-node - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:666` | `^https?:\/\/clubmed\.bd\.clubmedmnp\.com\/miniorder\/api\/basic\/common - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:67` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/business-sale-promotion-guide-mobile-web\/popup\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:670` | `^https?:\/\/cn-mall\.dreame\.tech\/dreame-mall\/api\/v1\/tag\/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:671` | `^https?:\/\/cn-wxmall\.dreame\.tech\/main\/goods\/get-topgoods$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:673` | `^https?:\/\/color\.jddj\.com\/client\.action\?functionId=search_recommendRanking$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:674` | `^https?:\/\/color\.jddj\.com\/client\.action\?functionId=uniformRecommend - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:678` | `^https?:\/\/conf\.diditaxi\.com\.cn\/dynamic\/conf - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:679` | `^https?:\/\/conf\.diditaxi\.com\.cn\/homepage\/v1\/other\/slow\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:68` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/discovery-feed\/v\d\/scene\/listen\/refresh\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:681` | `^https?:\/\/cstore-en-public-tx\.seewo\.com\/easinote5_public - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:682` | `^https?:\/\/ct\.xiaojukeji\.com\/agent\/v3\/feeds\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:689` | `^https?:\/\/cupid\.51jobapp\.com\/open\/51job-activities\/secJob\/queryHomeSecondConfigV2\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:69` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/firework-portal\/v\d+\/sync\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:692` | `^https?:\/\/cupid\.51jobapp\.com\/open\/operation\/get\/latest\/banner-list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:693` | `^https?:\/\/cupid\.51jobapp\.com\/open\/resume\/strategy\/resume-build\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:699` | `^https?:\/\/dashi\.163\.com\/task-center-api\/fapi\/task\/list$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:7` | `^https?:\/\/(a\.athm\.cn\/)?mobile\.app\.autohome\.com\.cn\/platform\/carserver\/carcard\/extendedcards - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:70` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/mobile-playpage\/playpage\/recommendContentV\d\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:700` | `^https?:\/\/dat\.ruanmei\.com\/ithome\/money\/acd\.json$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:701` | `^https?:\/\/data\.3g\.yy\.com\/popup\/topLiveCardPopup\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:706` | `^https?:\/\/dealer\.m\.autohome\.com\.cn\/handler\/other\/getdata\?__action=platform\.search - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:707` | `^https?:\/\/dealer\.m\.autohome\.com\.cn\/handler\/other\/getdata\?__action=super\.list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:708` | `^https?:\/\/dealer\.m\.autohome\.com\.cn\/handler\/other\/getdata\?__action=vrcore\.list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:71` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/mobile-playpage\/playpage\/recommend\/resource\/allocation\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:716` | `^https?:\/\/dispatcher\.camera360\.com\/api\/v\d\/list$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:717` | `^https?:\/\/display\.wting\.info\/.*.jpeg - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:72` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/mobile-user\/v\d\/purchased\/recommend\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:721` | `^https?:\/\/dj\.palmestore\.com\/zybk\/api\/bookshelf\/index\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:724` | `^https?:\/\/dl\.wechat\.com\/checkresupdate - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:727` | `^https?:\/\/dq\.dxy\.cn\/api\.php\?action=getpostbanners - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:73` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/social-web\/follow-stream\/category\/\d+$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:732` | `^https?:\/\/dudian-oss\.oss-cn-shenzhen\.aliyuncs\.com\/dlabel\/1\/startpage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:733` | `^https?:\/\/dxy\.com\/app\/i\/ask\/biz\/feed\/launch - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:736` | `^https?:\/\/e\.dangdang\.com\/.+?getDeviceStartPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:737` | `^https?:\/\/e\.dangdang\.com\/media\/api.+\?action=getDeviceStartPage - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:738` | `^https?:\/\/e\.jparking\.cn\/abTest-gateway\/abTest-api - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:74` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/subscribe\/v\d\/subscribe\/recommend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:740` | `^https?:\/\/e\.weather\.com\.cn\/weChat\/typhoonNull\.json - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:746` | `^https?:\/\/ecloud\.tppension\.cntaiping\.com\/fxtpplatform\/common\/anonymous\/common\/page\/queryStartPageNew\?language=zh-CN - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:749` | `^https?:\/\/edith\.xiaohongshu\.com\/api\/sns\/v\d+\/guide\/user_banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:75` | `^https?:\/\/(mobile\|mobilehera\|mobwsa)\.ximalaya\.com\/subscribe\/v\d\/subscribe\/tagAlbumList$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:751` | `^https?:\/\/edith\.xiaohongshu\.com\/api\/sns\/v\d+\/note\/guide\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:752` | `^https?:\/\/edith\.xiaohongshu\.com\/api\/sns\/v\d+\/surprisebox\/(?:get_style\|open\|submit_action) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:754` | `^https?:\/\/egw\.ejoy\.sinopec\.com\/api\/interface\/queryEffectiveBulletin - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:757` | `^https?:\/\/energy\.xiaojukeji\.com\/energy\/hummer\/api\/resource\/display($\|\?) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:758` | `^https?:\/\/energy\.xiaojukeji\.com\/lego\/api\/orderSprint\/stair\/info($\|\?) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:760` | `^https?:\/\/ep\.kugou\.com\/v\d\/album_shop\/get_entrance_info - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:764` | `^https?:\/\/external\.fcbox\.com\/wxgw\/post\/suggestion\/query - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:765` | `^https?:\/\/f-api\.kdocs\.cn\/godfather\/api\/thirdparty\/v1\/viewpager\?showLocal=mobileWebIndex - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:770` | `^https?:\/\/fcard\.api\.moji\.com\/flycard\/flyCard\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:773` | `^https?:\/\/file\.dian\.so\/c\/leto - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:774` | `^https?:\/\/flow\.dmall\.com\/app\/home\/pops - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:777` | `^https?:\/\/fm\.missevan\.com\/api\/v2\/chatroom\/sound\/recommend\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:778` | `^https?:\/\/fm\.missevan\.com\/api\/v2\/meta\/banner$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:779` | `^https?:\/\/fm\.missevan\.com\/api\/v2\/recommended\/top\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:78` | `^https?:\/\/(m\|mwsa)\.ximalaya\.com\/x-web-activity\/signIn\/getHomePageSignInInfo\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:780` | `^https?:\/\/fmapp\.chinafamilymart\.com\.cn\/api\/app\/biz\/base\/appversion\/latest - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:785` | `^https?:\/\/fuwu\.nhsa\.gov\.cn\/ebus\/fuwu\/api\/base\/cms\/iep\/web\/cms\/hmpgcfg\/queryAppHmpgCfgByApp - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:788` | `^https?:\/\/g(.*)\.dushu365\.com\/fandeng-orch\/bookboy\/v\d+\/vipPagePop - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:789` | `^https?:\/\/g(.*)\.dushu365\.com\/fandeng-orch\/dual2211\/config - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:790` | `^https?:\/\/g(.*)\.dushu365\.com\/fdtalk-orch\/newcomerzone\/v\d+\/guide - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:791` | `^https?:\/\/g(.*)\.dushu365\.com\/fs-retain\/trialVip\/v\d+\/requestTrialVipPopDoNotSendReward - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:792` | `^https?:\/\/g(.*)\.dushu365\.com\/order-orchestration\/orderWeb\/exchange\/v\d+\/showExchangeButton - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:793` | `^https?:\/\/g(.*)\.dushu365\.com\/resource-orchestration-system\/vipLandingPage\/v\d+\/getVipLandingPageApp - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:799` | `^https?:\/\/gaia\.ch\.com\/ECProduct\/homePageRevision\/(queryRecommendInfo\|findAllInfo) - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:8` | `^https?:\/\/(a\.athm\.cn\/)?mobile\.app\.autohome\.com\.cn\/platform\/carserver\/carcard\/findEquitysV5 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:800` | `^https?:\/\/gaia\.ch\.com\/ECProduct\/popupWindow - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:801` | `^https?:\/\/gaia\.ch\.com\/ECPromotion\/appFlash - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:807` | `^https?:\/\/gateway(retry)?\.kugou\.com\/mstc\/musicsymbol\/v\d\/system\/profile - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:808` | `^https?:\/\/gateway(retry)?\.kugou\.com\/ocean\/v\d\/sound\/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:81` | `^https?:\/\/(search\|searchwsa)\.ximalaya\.com\/hub\/(guideWord\|hotWord)V\d\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:810` | `^https?:\/\/gateway(retry)?\.kugou\.com\/searchnofocus\/v\d\/search_no_focus_word - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:811` | `^https?:\/\/gateway(retry)?\.kugou\.com\/singerdiscuss\/v\d\/entrance\/comment - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:812` | `^https?:\/\/gateway(retry)?\.kugou\.com\/v\d\/feeds\/follow_feed_fallback - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:813` | `^https?:\/\/gateway\.benewtech\.cn\/resources-app\/app\/startup\/prepage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:816` | `^https?:\/\/gateway\.shouqiev\.com(:\d+)?\/app\/startUp - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:823` | `^https?:\/\/go\.babytree\.com\/go_pregnancy\/api\/app_index\/get_ceramic_chip_area - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:825` | `^https?:\/\/go\.babytree\.com\/go_pregnancy\/api\/feeds - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:826` | `^https?:\/\/go\.babytree\.com\/go_pregnancy\/api\/index_activity - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:827` | `^https?:\/\/go\.babytree\.com\/go_tool\/api\/feeding_record\/get_home_banner_info - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:828` | `^https?:\/\/go\.babytree\.com\/go_tool\/api\/tools\/get_third_privacy_msgbox_list - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:831` | `^https?:\/\/gongdu\.youshu\.cc\/m\/open_screen\/list_by_udid - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:832` | `^https?:\/\/gorgon\.youdao\.com\/gorgon\/brand\/prefetch\.s\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:833` | `^https?:\/\/gorgon\.youdao\.com\/gorgon\/request\.s\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:834` | `^https?:\/\/gouche\.ksedt\.com\/config\/popup\/info$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:835` | `^https?:\/\/gsp\.gacmotor\.com\/gateway\/app-api\/app\/version\/latestupdate\?flatform=2&innerVersion= - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:837` | `^https?:\/\/guanyu\.longfor\.com\/app-server\/api\/v1\/main\/start - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:838` | `^https?:\/\/gugongmini\.dpm\.org\.cn\/gugong_applet\/open-screen - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:840` | `^https?:\/\/guide-acs\.m\.taobao\.com\/gw\/mtop\.taobao\.(volvo\.secondfloor\.getconfig\|wireless\.home\.newface\.awesome\.get) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:847` | `^https?:\/\/gw3\.ykccn\.com\/api\/omp\/mt\/charge\/activity\/package\/newest - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:848` | `^https?:\/\/gw3\.ykccn\.com\/api\/omp\/mt\/enterpriseWeChatConfig\/app\/queryCityConfig - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:852` | `^https?:\/\/gw\.etczs\.net\/api\/marketing\/marketing_plan\/release\/get - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:855` | `^https?:\/\/gw\.line\.naver\.jp\/tr\/event$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:856` | `^https?:\/\/gw\.xiaocantech\.com\/g\/pa - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:860` | `^https?:\/\/h5\.smzdm\.com\/user\/coupon\/coupon_list\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:861` | `^https?:\/\/h5api\.sginput\.qq\.com\/v\d\/gcenter\/ios\/homepage - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:871` | `^https?:\/\/hoapp\.juneyaoair\.com\/version - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:872` | `^https?:\/\/home\.mi\.com\/cgi-op\/api\/v1\/recommendation\/(banner\|carousel\/banners\|myTab\|openingBanner) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:873` | `^https?:\/\/home\.mi\.com\/cgi-op\/api\/v1\/resource\/realtime\/openingBanner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:875` | `^https?:\/\/htwkop\.xiaojukeji\.com\/gateway\?api=cms\.htw\.delivery - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:876` | `^https?:\/\/htwkop\.xiaojukeji\.com\/gateway\?api=hm\.fa\.(?:combineHomepageInfo\|mallRecommend) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:878` | `^https?:\/\/hweb-hotel\.huazhu\.com\/home\/queryRecommond - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:879` | `^https?:\/\/hweb-hotel\.huazhu\.com\/{1,2}home\/(?:queryNewNotice\|querySelectHotel\|queryHotelBrand\|queryMall\|huazhuWorld) - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:882` | `^https?:\/\/hweb-manager\.huazhu\.com\/notice\/getAppPopupNotifyAlert - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:884` | `^https?:\/\/hwstore\.kugou\.com\/v\d\/get_store_data - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:885` | `^https?:\/\/i\.ys7\.com\/api\/user\/tabList - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:899` | `^https?:\/\/imaicai\.api\.ddxq\.mobi\/guide-service\/userLike\/flowData$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:9` | `^https?:\/\/(a\.athm\.cn\/)?mobile\.app\.autohome\.com\.cn\/platform\/carserver\/carcard\/mycardv6 - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:900` | `^https?:\/\/imaicai\.api\.ddxq\.mobi\/homeApi\/marketingNotice\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:901` | `^https?:\/\/imaicai\.api\.ddxq\.mobi\/homeApi\/userLike\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:902` | `^https?:\/\/imaicai\.api\.ddxq\.mobi\/order\/getRecommend$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:903` | `^https?:\/\/imaicai\.api\.ddxq\.mobi\/search\/hotKeyword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:904` | `^https?:\/\/imaicai\.api\.ddxq\.mobi\/search\/rankingList\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:905` | `^https?:\/\/imaicai\.api\.ddxq\.mobi\/search\/rollHotKeyword\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:925` | `^https?:\/\/init\.sms\.mob\.com\/.*sdk\/init.* - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:928` | `^https?:\/\/interface\.mcake\.com\/api\/popup\/ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:930` | `^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(comment\/(feed\/inserted)\|hotcomment\/collect\|tips\/v\d\/get\|mlivestream\/entrance\/playpage\|link\/(position\/show\/strategy\|scene\/show)\|ios\/version\|v\d\/content\/exposure\/comment\/banner) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:931` | `^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(resource\/comments?\/musiciansaid\|community\/friends\/fans-group\/artist\/group\/get\|user\/sub\/artist\|music\/songshare\/text\/recommend\/get\|mine\/applet\/redpoint\|resniche\/position\/play\/new\/get) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:932` | `^https?:\/\/interface\d?\.music\.163\.com\/w?e?api\/(search\/(chart\|default\|rcmd\/keyword\|specialkeyword)\|(resource-exposure\/\|middle\/clientcfg\/config)\|activity\/bonus\/playpage\/time\/query) - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:939` | `^https?:\/\/iphone\.ac\.qq\.com\/.*\/Support\/(?:getSystemConf\|bootScreen) - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:941` | `^https?:\/\/iphone\.myzaker\.com\/zaker\/cover\.php\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:943` | `^https?:\/\/iuser\.api\.ddxq\.mobi\/userportal-service\/api\/v1\/user\/queryMyPage\/\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:944` | `^https?:\/\/j1\.pupuapi\.com\/client\/assets\/discount\/order - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:946` | `^https?:\/\/j1\.pupuapi\.com\/client\/marketing\/channel\/global_redeem\/top_tip\/v\d - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:947` | `^https?:\/\/j1\.pupuapi\.com\/client\/member_card\/index\/my - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:948` | `^https?:\/\/j1\.pupuapi\.com\/client\/member_card\/premium\/user_center - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:949` | `^https?:\/\/j1\.pupuapi\.com\/client\/recommendation\/hub\/interests\/products\/v\d - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:95` | `^https?:\/\/.*\.townmalls\.cn:1890\/mossapi\/mossp\.BannerManager\/activityList.* - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:950` | `^https?:\/\/j5\.dfcfw\.com\/WG\/(app)?conf\/202[0-9]{5}/.*.(?:jpg\|png) - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:955` | `^https?:\/\/jiakao-misc\.kakamobi\.cn\/api\/open\/my-tab-config\/(?:banner\|selection)-list - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:957` | `^https?:\/\/jiucaigongshe\.oss-cn-beijing\.aliyuncs\.com\/[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}\.png - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:959` | `^https?:\/\/jz\.wacaijizhang\.com\/api\/banners\/list\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:960` | `^https?:\/\/jz\.wacaijizhang\.com\/api\/banners\/ribbon\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:961` | `^https?:\/\/jz\.wacaijizhang\.com\/api\/resource\/universal\/fetch$ - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:963` | `^https?:\/\/kano\.guahao\.cn\/[a-zA-Z0-9]{12} - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:968` | `^https?:\/\/keapi\.fenbi\.com\/app\/iphone\/\w+\/reddot\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:972` | `^https?:\/\/lan\.line\.me\/v1\/line\/ios - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:975` | `^https?:\/\/learn\.chaoxing\.com\/apis\/service\/appConfig\? - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:976` | `^https?:\/\/learnywhere\.cn\/api\/activity\/23\/423dsj\/inapp\/bb\/promote - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:978` | `^https?:\/\/legy\.line-apps\.com:443\/ext\/smartch\/banner\/sch\/v1$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:979` | `^https?:\/\/legy\.line-apps\.com:443\/tr\/event$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:980` | `^https?:\/\/legy\.line-apps\.com\/line\.gcs\.GcsModuleService\/GetModulesByModuleIds$ - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:984` | `^https?:\/\/line3-h5-mobile-api\.biligame\.com\/game\/live\/large_card_material\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:986` | `^https?:\/\/lion\.didialift\.com\/broker\/\? - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:992` | `^https?:\/\/lop-proxy\.jd\.com\/csat\/getNPSQuestionnaire - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:993` | `^https?:\/\/lop-proxy\.jd\.com\/home\/banner - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:994` | `^https?:\/\/lop-proxy\.jd\.com\/index\/queryTabBubble - reject` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:995` | `^https?:\/\/lop-proxy\.jd\.com\/order\/getCarbonIntegral - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:996` | `^https?:\/\/lop-proxy\.jd\.com\/search\/getQuestionnaireByOrderInfo - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:997` | `^https?:\/\/lop-proxy\.jd\.com\/smartmp\/querySmartDecision - reject-dict` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rewrite/Sources/URL-Rewrite.conf:998` | `^https?:\/\/luckman\.suning\.com\/luck-web\/policy\/v\d\/msf\/index\.do - reject-200` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:100` | `DOMAIN,acs4baichuan.m.taobao.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:110` | `DOMAIN-SUFFIX,domob.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:111` | `DOMAIN-SUFFIX,inmobi.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:112` | `DOMAIN-SUFFIX,lnk0.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:114` | `DOMAIN-SUFFIX,waps.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:115` | `DOMAIN-SUFFIX,wiyun.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:116` | `DOMAIN-SUFFIX,youmi.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:117` | `DOMAIN-SUFFIX,chartbeat.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:118` | `DOMAIN-SUFFIX,quantserve.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:119` | `DOMAIN-SUFFIX,taboola.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:120` | `DOMAIN-SUFFIX,outbrain.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:121` | `DOMAIN-SUFFIX,criteo.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:122` | `DOMAIN-SUFFIX,criteo.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:126` | `DOMAIN-SUFFIX,branch.io,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:129` | `DOMAIN-SUFFIX,kochava.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:130` | `DOMAIN-SUFFIX,sentry.io,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:131` | `DOMAIN-SUFFIX,segment.io,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:14` | `DOMAIN-KEYWORD,alimama,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:19` | `DOMAIN-KEYWORD,clickstream,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:20` | `DOMAIN-KEYWORD,commercial,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:22` | `DOMAIN-KEYWORD,doubleclick,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:24` | `DOMAIN-KEYWORD,exposure,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:28` | `DOMAIN-KEYWORD,guanggao,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:32` | `DOMAIN-KEYWORD,marketing,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:33` | `DOMAIN-KEYWORD,monitor,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:35` | `DOMAIN-KEYWORD,promotion,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:40` | `DOMAIN-KEYWORD,umeng,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:44` | `DOMAIN-KEYWORD,wlmonitor,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:49` | `DOMAIN-SUFFIX,alimama.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:50` | `DOMAIN-SUFFIX,allyes.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:51` | `DOMAIN-SUFFIX,anythinktech.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:52` | `DOMAIN-SUFFIX,app-measurement.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:53` | `DOMAIN-SUFFIX,appsflyer.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:56` | `DOMAIN-SUFFIX,bugly.qq.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:57` | `DOMAIN-SUFFIX,cnzz.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:58` | `DOMAIN-SUFFIX,doubleclick.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:61` | `DOMAIN-SUFFIX,googlesyndication.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:62` | `DOMAIN-SUFFIX,gtags.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:64` | `DOMAIN-SUFFIX,irs01.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:65` | `DOMAIN-SUFFIX,miaozhen.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:66` | `DOMAIN-SUFFIX,mob.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:68` | `DOMAIN-SUFFIX,openx.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:69` | `DOMAIN-SUFFIX,pangle.io,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:70` | `DOMAIN-SUFFIX,pangolin-sdk-toutiao.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:71` | `DOMAIN-SUFFIX,scorecardresearch.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:72` | `DOMAIN-SUFFIX,sigmob.cn,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:73` | `DOMAIN-SUFFIX,sigmob.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:74` | `DOMAIN-SUFFIX,talkingdata.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:75` | `DOMAIN-SUFFIX,tanx.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:76` | `DOMAIN-SUFFIX,umeng.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:77` | `DOMAIN-SUFFIX,umengcloud.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:80` | `DOMAIN-SUFFIX,vungle.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:81` | `DOMAIN-SUFFIX,wrating.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:82` | `DOMAIN-SUFFIX,zhiziyun.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:90` | `DOMAIN,amdc.m.taobao.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:96` | `DOMAIN,retcode.taobao.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:97` | `DOMAIN,tns.simba.taobao.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/aggressive-ads.list:99` | `DOMAIN,ut.taobao.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/app-clean.list:31` | `DOMAIN,ut.taobao.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/app-clean.list:36` | `DOMAIN-SUFFIX,fds.api.moji.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/app-clean.list:39` | `DOMAIN-SUFFIX,me.api.moji.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/app-clean.list:40` | `AND,((PROTOCOL,QUIC),(DOMAIN,soulapp.cn)),REJECT-NO-DROP` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/app-clean.list:50` | `DOMAIN,market.m.taobao.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/original-remote-rule-sets.list:11` | `DOMAIN-SET,https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/original-remote-rule-sets.list:14` | `RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Hijacking/Hijacking.list,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/original-remote-rule-sets.list:15` | `RULE-SET,https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Privacy/Privacy.list,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/original-remote-rule-sets.list:17` | `RULE-SET,https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:101` | `DOMAIN,switch.cup.com.cn,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:104` | `DOMAIN,yandexmetrica.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:113` | `DOMAIN,e.jparking.cn,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:122` | `DOMAIN-SUFFIX,doubleclick-cn.net,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:123` | `DOMAIN-SUFFIX,doubleclick.net,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:127` | `DOMAIN-SUFFIX,v1d.szbdyd.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:13` | `IP-CIDR,180.76.76.112/32,REJECT,no-resolve` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:138` | `IP-CIDR,122.229.8.47/32,REJECT,no-resolve` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:139` | `IP-CIDR,122.229.29.89/32,REJECT,no-resolve` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:14` | `IP-CIDR,180.76.76.200/32,REJECT,no-resolve` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:142` | `URL-REGEX,"^http:\/\/p\.kuaidi100\.com\/mobile\/mobileapi\.do",REJECT-TINYGIF,extended-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:146` | `DOMAIN,mall-dsp2.qinlinkeji.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:147` | `DOMAIN,mallapi2.qinlinkeji.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:22` | `DOMAIN-SUFFIX,ehaier.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:50` | `IP-CIDR,103.37.155.60/32,REJECT,no-resolve` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:62` | `DOMAIN,api.zuihuimai.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:65` | `DOMAIN-SUFFIX,shuzilm.cn,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:85` | `DOMAIN,tpns.qq.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:87` | `DOMAIN-SUFFIX,l.qq.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:88` | `DOMAIN-KEYWORD,trace.qq.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:90` | `IP-CIDR,47.110.187.87/32,REJECT,no-resolve` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/qingrex-miniapp-app-ad.list:94` | `DOMAIN-SUFFIX,wxs.qq.com,REJECT,extended-matching,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:102` | `DOMAIN,popup.dushu365.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:106` | `DOMAIN,richmanapi.jxedt.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:107` | `DOMAIN,richmanmain.jxedt.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:108` | `DOMAIN,richmanrules.jxedt.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:111` | `DOMAIN,sax.sina.com.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:112` | `DOMAIN,saxn.sina.com.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:113` | `DOMAIN,saxs.sina.com.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:114` | `DOMAIN,sensors.umetrip.com.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:115` | `DOMAIN,smartop-sdkapi-ipv6.jiguang.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:116` | `DOMAIN,smartop-sdkapi.jiguang.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:17` | `DOMAIN,apm-native.xiaohongshu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:18` | `DOMAIN,apm.gotokeep.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:19` | `DOMAIN,apmplus.volces.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:20` | `DOMAIN,appcloud.zhihu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:21` | `DOMAIN,appcloud2.in.zhihu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:22` | `DOMAIN,appgo.189.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:23` | `DOMAIN,apps-booster.xiaopeng.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:24` | `DOMAIN,appupdates.189.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:25` | `DOMAIN,atrace.chelaile.net.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:26` | `DOMAIN,axxd.xmseeyouyima.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:31` | `DOMAIN,collect.xiaopeng.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:32` | `DOMAIN,counter.kingsoft.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:33` | `DOMAIN,counter.ksosoft.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:34` | `DOMAIN,crash2.zhihu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:38` | `DOMAIN,csc-apm.sgcc.com.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:39` | `DOMAIN,cube.weixinbridge.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:40` | `DOMAIN,da.bridgeturbo.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:46` | `DOMAIN,dynamicf.sankuai.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:48` | `DOMAIN,et.ykccn.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:49` | `DOMAIN,etl.xlmc.sandai.net,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:52` | `DOMAIN,gather.colorfulclouds.net,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:53` | `DOMAIN,gwp.xiaojukeji.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:54` | `DOMAIN,hc-ssp.sm.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:79` | `DOMAIN,ivy.pchouse.com.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:83` | `DOMAIN,live-monitor-broker.sankuai.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:91` | `DOMAIN,mall-dsp2.qinlinkeji.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:92` | `DOMAIN,mallapi2.qinlinkeji.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:93` | `DOMAIN,mdap.mpaas.cn-hangzhou.aliyuncs.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:94` | `DOMAIN,meta.pinduoduo.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:95` | `DOMAIN,minfo.wps.cn,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/reject.list:97` | `DOMAIN,mqtt.zhihu.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/wechat-ad.list:7` | `DOMAIN-SUFFIX,l.qq.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/wechat-ad.list:8` | `DOMAIN-SUFFIX,e.qq.com,REJECT,pre-matching` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/youtube-direct.list:11` | `DOMAIN-SUFFIX,googlesyndication.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/youtube-direct.list:12` | `DOMAIN-SUFFIX,googletagservices.com,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 未分类 REJECT | `Rules/youtube-direct.list:9` | `DOMAIN-SUFFIX,doubleclick.net,REJECT` | 非明确广告关键词，需人工复核 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/fan-qie-novel.conf:34` | `^https?://.+\.snssdk\.com/video/play/1/toutiao/.+/mp4 - reject` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/i-qi-yi-video.conf:15` | `DOMAIN,access.if.iqiyi.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/i-qi-yi-video.conf:18` | `^https?://iface2\.iqiyi\.com/control/3\.0/init_proxy\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/i-qi-yi-video.conf:19` | `^https?://act\.vip\.iqiyi\.com/interact/api/v2/show\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/i-qi-yi-video.conf:20` | `^https?://iface2\.iqiyi\.com/ivos/interact/video/data\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/i-qi-yi-video.conf:21` | `^https?://iface2\.iqiyi\.com/video/3\.0/v_interface_proxy\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/i-qi-yi-video.conf:22` | `^https?://iface2\.iqiyi\.com/views_pop/3\.0/pop_control\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:10` | `DOMAIN,credits2.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:11` | `DOMAIN,credits3.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:12` | `DOMAIN,dflow.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:13` | `DOMAIN,encounter.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:14` | `DOMAIN,floor.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:15` | `DOMAIN,layer.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:16` | `DOMAIN,mob.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:18` | `DOMAIN,rprain.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:19` | `DOMAIN,rprain.log.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:20` | `DOMAIN,vip.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:21` | `DOMAIN-SUFFIX,da.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/mgtv.conf:9` | `DOMAIN,credits.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/qqksong.conf:13` | `DOMAIN,info4.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/qqksong.conf:14` | `DOMAIN,info6.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/qqksong.conf:16` | `DOMAIN,ios.video.mpush.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/qqksong.conf:25` | `DOMAIN,sdkconfig.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/qqksong.conf:37` | `DOMAIN-KEYWORD,trace.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/reel-short.conf:10` | `^https://(v-api\.crazymaplestudios\.com\|d1k8g7qaebqd28\.cloudfront\.net)/api/video/hall/landingPage$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/reel-short.conf:11` | `^https://(v-api\.crazymaplestudios\.com\|d1k8g7qaebqd28\.cloudfront\.net)/api/video/book/getPayModeV2$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/reel-short.conf:9` | `^https://(v-api\.crazymaplestudios\.com\|d1k8g7qaebqd28\.cloudfront\.net)/api/video/app/getSplashScreenConfig$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/soda-music.conf:18` | `^https://(beta-luna\.douyin\|api5-lq\.qishui)\.com/luna/listen-video/reminder\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/taobao.conf:10` | `DOMAIN,ems.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/tencent-video.conf:10` | `DOMAIN,info4.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/tencent-video.conf:11` | `DOMAIN,info6.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/tencent-video.conf:12` | `DOMAIN,ios.video.mpush.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/tencent-video.conf:16` | `DOMAIN,vv6.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/tencent-video.conf:20` | `DOMAIN-KEYWORD,trace.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/tencent-video.conf:22` | `URL-REGEX,"^http:\/\/[\d\.:]*\/?(defaultts\.tc\|vmind\.qqvideo\.tc\|finderpdd\.video)\.qq\.com\/\w+",REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/tencent-video.conf:27` | `^https?://vv\.video\.qq\.com/(diff\|get)vmind - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/video-go.conf:14` | `^https://api\.ys7\.com/v3/videoclips/square/video/query - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:10` | `DOMAIN,wxsmsdy.video.qq.com,REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/wechat-mini-programs.conf:109` | `^https://vod-movie\.maoyan\.com/vod/video/onlineMovies\.json - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:13` | `DOMAIN,adx-core.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:14` | `DOMAIN,adx-open-service.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:15` | `DOMAIN,yk-ssp.ad.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:16` | `DOMAIN,cad.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:17` | `DOMAIN,ykad-data.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:18` | `DOMAIN,amdc.m.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:20` | `DOMAIN,youku-crm-product.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:21` | `DOMAIN,dr-danmu.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:22` | `DOMAIN,group-ssl-danmu-ori.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:23` | `DOMAIN,m.atm.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:24` | `DOMAIN,mc.atm.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:27` | `DOMAIN-SUFFIX,iyes.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youku.conf:29` | `DOMAIN,pre-acs.youku.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youtube.conf:16` | `AND,((DOMAIN-SUFFIX,googlevideo.com), (PROTOCOL,UDP)),REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Apps/youtube.conf:17` | `AND,((DOMAIN,youtubei.googleapis.com), (PROTOCOL,UDP)),REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:100` | `DOMAIN,iadmusicmatvideo.music.126.net,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:105` | `DOMAIN,ipv4.music.163.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:106` | `DOMAIN,ipv6.music.163.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:108` | `DOMAIN,layer.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:63` | `DOMAIN,credits.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:64` | `DOMAIN,credits2.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:65` | `DOMAIN,credits3.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:70` | `DOMAIN,dflow.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:75` | `DOMAIN,encounter.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/Rule.conf:78` | `DOMAIN,floor.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1092` | `^https?:\/\/mgesq\.api\.mgtv\.com\/search\/goods\/rank - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1093` | `^https?:\/\/mgesq\.api\.mgtv\.com\/user\/center\/config - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1094` | `^https?:\/\/mgesq\.api\.mgtv\.com\/v\d\/goods\/guess_you_like - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1095` | `^https?:\/\/mgesq\.api\.mgtv\.com\/v\d\/user\/center\/icon - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1126` | `^https?:\/\/mobile\.api\.mgtv\.com\/v\d\/mobile\/checkUpdate\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1131` | `^https?:\/\/mobileso\.bz\.mgtv\.com\/mobile\/recommend\/v\d\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1132` | `^https?:\/\/mobileso\.bz\.mgtv\.com\/spotlight\/search\/v\d\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1242` | `^https?:\/\/public-deliver9\.miguvideo\.com\/deliver\/site\/batchMatch\/mergeSpot\/miguvideo\/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1258` | `^https?:\/\/recommend-dy\.miguvideo\.com\/recommend-dynamic\/dataSource\/v1\/recommend\/merge - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1423` | `^https?:\/\/vdo\.api\.moji\.com\/shortvideo\/card\/subscribe$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1424` | `^https?:\/\/vdo\.api\.moji\.com\/shortvideo\/video\/index_flow\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1425` | `^https?:\/\/vdo\.api\.moji\.com\/shortvideo\/video_user\/hotGuyRcm\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1426` | `^https?:\/\/vdo\.api\.moji\.com\/shortvideo\/zone\/follow_src_zone\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1429` | `^https?:\/\/vod-movie\.maoyan\.com\/vod\/video\/onlineMovies\.json - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:1430` | `^https?:\/\/vv\.video\.qq\.com\/getvmind\? - reject-200` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:186` | `^https?:\/\/act\.vip\.iqiyi\.com\/interact\/api\/v2\/show\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:28` | `^https?:\/\/(beta-luna\.douyin\|api5-lq\.qishui)\.com\/luna\/listen-video\/reminder\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:450` | `^https?:\/\/api\.ys7\.com\/v3\/videoclips\/square\/video\/query - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:602` | `^https?:\/\/bk\.bingo\.qq\.com\/bk\/crx\/data\/videoAd - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:626` | `^https?:\/\/ccsp-egmas\.sf-express\.com\/cx-app-video\/video\/app\/video\/labelClusterList - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:675` | `^https?:\/\/common-sc\.miguvideo\.com\/videoActivity\/activityList\/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:696` | `^https?:\/\/damang\.api\.mgtv\.com\/station\/album\/red\/dot\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:703` | `^https?:\/\/dc\.bz\.mgtv\.com\/dynamic\/v\d\/channel\/ads\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:704` | `^https?:\/\/dc\.bz\.mgtv\.com\/dynamic\/v\d\/skin\/config\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:820` | `^https?:\/\/ggic\d+.miguvideo\.com\/ad\/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:821` | `^https?:\/\/ggx.+\.miguvideo\.com\/request\/sdk.+[^?]*$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:83` | `^https?:\/\/(v-api\.crazymaplestudios\.com\|d1k8g7qaebqd28\.cloudfront\.net)\/api\/video\/app\/getSplashScreenConfig$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:84` | `^https?:\/\/(v-api\.crazymaplestudios\.com\|d1k8g7qaebqd28\.cloudfront\.net)\/api\/video\/book\/getPayModeV2$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:85` | `^https?:\/\/(v-api\.crazymaplestudios\.com\|d1k8g7qaebqd28\.cloudfront\.net)\/api\/video\/hall\/landingPage$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:862` | `^https?:\/\/hb-boom\.api\.mgtv\.com\/release\/pullReleaseInfo$ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:891` | `^https?:\/\/iface2\.iqiyi\.com\/control\/3\.0\/init_proxy\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:892` | `^https?:\/\/iface2\.iqiyi\.com\/ivos\/interact\/video\/data\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:893` | `^https?:\/\/iface2\.iqiyi\.com\/video\/3\.0\/v_interface_proxy\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rewrite/Sources/URL-Rewrite.conf:894` | `^https?:\/\/iface2\.iqiyi\.com\/views_pop\/3\.0\/pop_control\? - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:18` | `DOMAIN,adx-core.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:19` | `DOMAIN,adx-open-service.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:2` | `DOMAIN,access.if.iqiyi.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:20` | `DOMAIN,amdc.m.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:21` | `DOMAIN,cad.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:22` | `DOMAIN,dr-danmu.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:23` | `DOMAIN,ems.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:24` | `DOMAIN,group-ssl-danmu-ori.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:26` | `DOMAIN,m.atm.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:27` | `DOMAIN,mc.atm.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:28` | `DOMAIN,pre-acs.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:32` | `DOMAIN,yk-ssp.ad.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:33` | `DOMAIN,ykad-data.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:35` | `DOMAIN,youku-crm-product.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/app-clean.list:37` | `DOMAIN-SUFFIX,iyes.youku.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:33` | `DOMAIN,credits.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:34` | `DOMAIN,credits2.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:35` | `DOMAIN,credits3.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:36` | `DOMAIN,dflow.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:37` | `DOMAIN,encounter.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:38` | `DOMAIN,floor.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:39` | `DOMAIN,layer.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:40` | `DOMAIN,mob.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:42` | `DOMAIN,rprain.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:43` | `DOMAIN,rprain.log.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:44` | `DOMAIN,vip.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:45` | `DOMAIN-SUFFIX,da.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:77` | `DOMAIN,info4.video.qq.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:78` | `DOMAIN,info6.video.qq.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:79` | `DOMAIN,ios.video.mpush.qq.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:8` | `DOMAIN,api.iqiyi.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/qingrex-miniapp-app-ad.list:89` | `DOMAIN-KEYWORD,trace.video.qq.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:109` | `DOMAIN,rprain.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:110` | `DOMAIN,rprain.log.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:35` | `DOMAIN,credits.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:36` | `DOMAIN,credits2.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:37` | `DOMAIN,credits3.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:42` | `DOMAIN,dflow.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:47` | `DOMAIN,encounter.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:50` | `DOMAIN,floor.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:72` | `DOMAIN,iadmusicmatvideo.music.126.net,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:77` | `DOMAIN,ipv4.music.163.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:78` | `DOMAIN,ipv6.music.163.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:80` | `DOMAIN,layer.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/reject.list:96` | `DOMAIN,mob.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/web-ads.list:79` | `DOMAIN,ad.video.51togic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 | `Rules/web-ads.list:82` | `DOMAIN,cmad.video.51togic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 国内 App 核心 API | `Rewrite/Sources/Apps/aiinquiry.conf:13` | `^https://aiqicha\.baidu\.com/app/getExpertVideoAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 国内 App 核心 API | `Rewrite/Sources/Apps/youku.conf:30` | `DOMAIN,youku-acs.m.taobao.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 国内 App 核心 API | `Rewrite/Sources/URL-Rewrite.conf:213` | `^https?:\/\/aiqicha\.baidu\.com\/app\/getExpertVideoAjax - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 国内 App 核心 API | `Rules/app-clean.list:34` | `DOMAIN,youku-acs.m.taobao.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:13` | `DOMAIN,video-dsp.pddpic.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/bilibili.conf:31` | `URL-REGEX,"^http:\/\/upos-sz-static\.bilivideo\.com\/ssaxcode\/\w{2}\/\w{2}\/\w{32}-1-SPLASH",REJECT-TINYGIF,extended-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/mgtv.conf:17` | `DOMAIN,rc-topic-api.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/qqksong.conf:47` | `^https://amsweb-cdn-\S+-\d+\.file\.myqcloud\.com/video/ad_profile/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/tencent-video.conf:23` | `URL-REGEX,"^http:\/\/apd-vlive\.apdcdn\.tc\.qq\.com\/vmind\.qqvideo\.tc\.qq\.com\/\w+",REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Apps/tencent-video.conf:24` | `URL-REGEX,"^http:\/\/apd-\w+\.v\.smtcdns\.com\/(defaultts\|omts\|vmind\.qqvideo)\.tc\.qq\.com\/\w+",REJECT` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:25` | `DOMAIN,ads-img-qc.xhscdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:26` | `DOMAIN,ads-video-al.xhscdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/Rule.conf:27` | `DOMAIN,ads-video-qc.xhscdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:224` | `^https?:\/\/amsweb-cdn-\S+-\d+\.file\.myqcloud\.com\/video\/ad_profile\/ - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:491` | `^https?:\/\/app-sc\.miguvideo\.com\/app-management\/v1\/staticcache\/settings\/miguvideo\/SHARE_PIC - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:641` | `^https?:\/\/cdn\.sdb\.com\.cn\/widget\/pb\/pb-plugins-rec-mivideo - reject-dict` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rewrite/Sources/URL-Rewrite.conf:819` | `^https?:\/\/ggc\.miguvideo\.com\/v1\/iflyad\/deliverysystem\/direct\/ - reject-img` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rules/app-clean.list:64` | `DOMAIN,ads-img-qc.xhscdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rules/app-clean.list:65` | `DOMAIN,ads-video-al.xhscdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rules/app-clean.list:66` | `DOMAIN,ads-video-qc.xhscdn.com,REJECT,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rules/qingrex-miniapp-app-ad.list:41` | `DOMAIN,rc-topic-api.bz.mgtv.com,REJECT,extended-matching,pre-matching` | 命中敏感链路关键词 |
| REJECT | medium | 视频 / 音乐播放链路 / 图片 / 静态 CDN | `Rules/reject.list:105` | `DOMAIN,rc-topic-api.bz.mgtv.com,REJECT,pre-matching` | 命中敏感链路关键词 |
