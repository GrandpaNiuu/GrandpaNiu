# 国内 App 联网与加载误伤风险排查报告

生成时间：2026-06-26 12:21:27 +0800

本报告用于排查国内 App 图片加载失败、页面加载不完整、微信不能发图片等问题。报告只分析，不自动修改规则。

## 初步结论模板

- 如果 `reject.list` 命中微信媒体、图片 CDN、HTTPDNS 或核心 API，优先怀疑规则误杀。
- 如果 `app-cleaner-active.conf` 使用宽域名匹配，优先怀疑脚本入口误伤。
- 如果 `app-cleaner.js` 通用 cleaner 删除普通 `banner / promotion / sections`，优先怀疑融合逻辑误伤。
- 如果 `node --check` 通过，通常不是代码语法问题，而是规则或清理逻辑问题。

## Direct 保护覆盖检查

| 类别 | 检查项 | direct.list 是否包含 |
|---|---|---|
| wechat-media | `weixin.qq.com` | 是 |
| wechat-media | `wxs.qq.com` | 是 |
| wechat-media | `qpic.cn` | 是 |
| wechat-media | `gtimg.cn` | 是 |
| wechat-media | `qlogo.cn` | 是 |
| image-cdn | `alicdn.com` | 是 |
| image-cdn | `pddpic.com` | 否 |
| image-cdn | `360buyimg.com` | 是 |
| image-cdn | `jdimg.com` | 是 |
| image-cdn | `biliimg.com` | 是 |
| image-cdn | `meituan.net` | 是 |

## Reject 风险命中

### wechat-media

- `DOMAIN,badjs.weixinbridge.com,REJECT,pre-matching`
- `DOMAIN,cube.weixinbridge.com,REJECT,pre-matching`

### image-cdn

- `DOMAIN,adx-api.zdmimg.com,REJECT,pre-matching`
- `DOMAIN,cd-1.pddpic.com,REJECT,pre-matching`
- `DOMAIN,cdl-1.pddpic.com,REJECT,pre-matching`
- `DOMAIN,cdl-p2.pddpic.com,REJECT,pre-matching`
- `DOMAIN,hudong.alicdn.com,REJECT,pre-matching`
- `DOMAIN,huyafile.msstatic.com,REJECT,pre-matching`
- `DOMAIN,livewebbs2.msstatic.com,REJECT,pre-matching`
- `DOMAIN,livewebbs2pcdn.msstatic.com,REJECT,pre-matching`
- `DOMAIN,nbsdk-baichuan.alicdn.com,REJECT,pre-matching`
- `DOMAIN,ossgw.alicdn.com,REJECT,pre-matching`
- `DOMAIN,pp-cdnfile2pcdn.msstatic.com,REJECT,pre-matching`

### httpdns

- 无

### domestic-core-api

- `DOMAIN,afdconf.baidu.com,REJECT,pre-matching`
- `DOMAIN,amap-aos-info-nogw.amap.com,REJECT,pre-matching`
- `DOMAIN,dpmtpush.dianping.com,REJECT,pre-matching`
- `DOMAIN,free-aos-cdn-image.amap.com,REJECT,pre-matching`
- `DOMAIN,hlx.meituan.com,REJECT,pre-matching`
- `DOMAIN,layout.meituan.net,REJECT,pre-matching`
- `DOMAIN,lc.map.baidu.com,REJECT,pre-matching`
- `DOMAIN,lx0.meituan.com,REJECT,pre-matching`
- `DOMAIN,r.dianping.com,REJECT,pre-matching`

### bank-payment

- `DOMAIN,iisp-oidea.mbs.boc.cn,REJECT,pre-matching`
- `DOMAIN,iisp.mbs.boc.cn,REJECT,pre-matching`
- `DOMAIN,msmp.abchina.com.cn,REJECT,pre-matching`

## app-cleaner active 宽匹配风险

- `qq\.com`
- `gtimg`
- `qpic`

## app-cleaner 逻辑风险提示

- app-cleaner contains banner logic; verify generic cleaner is conservative and does not remove ordinary homepage image modules.
- app-cleaner contains promotion logic; verify ordinary promotion/feature entrances are not dropped unless explicitly ad-marked.

## 建议排查顺序

1. 先确认 `node --check Scripts/app-cleaner.js` 是否通过。
2. 再看 Shadowrocket 日志中具体命中 REJECT、MITM 还是 Script。
3. 如果命中 REJECT，优先单条加入 Direct pre-matching 或注释该 REJECT。
4. 如果命中 Script，收窄 `app-cleaner-active.conf` 或增加媒体 bypass。
5. 如果命中 MITM，检查该 hostname 是否应从 stable MITM 层移到 stable-plus 或 full。
6. 不要一次性删除大量规则；国内 App 联网问题应逐域名单条修复。
