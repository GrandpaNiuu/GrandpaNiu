# 图片加载与微信发图误伤修复报告

## 问题

用户反馈：

- 去广告 App 图片加载不出来。
- 微信不能发送图片。

这是高优先级误伤问题。处理优先级高于继续扩展规则或继续融合脚本。

## 初步判断

可能原因包括：

1. `Rules/reject.list` 中存在图片 CDN、HTTPDNS、微信相关域名的 REJECT / pre-matching。
2. `Rules/direct.list` 原本缺少微信媒体、图片 CDN、常用静态资源域名的安全直连保护。
3. `Scripts/app-cleaner-active.conf` 之前使用较宽的 `qq.com`、CDN 类匹配，可能导致微信媒体链路或普通图片接口进入 app-cleaner 脚本检查路径。
4. 大批量通用 JSON cleaner 应避免命中媒体 CDN、图片资源、微信图片上传/下载接口。

## 已执行修复

### 1. 增加微信媒体安全直连

已在 `Rules/direct.list` 增加并设为 `pre-matching`：

```text
DOMAIN-SUFFIX,weixin.qq.com,DIRECT,pre-matching
DOMAIN-SUFFIX,wx.qq.com,DIRECT,pre-matching
DOMAIN-SUFFIX,wechat.com,DIRECT,pre-matching
DOMAIN-SUFFIX,servicewechat.com,DIRECT,pre-matching
DOMAIN-SUFFIX,wechatpay.cn,DIRECT,pre-matching
DOMAIN,dns.weixin.qq.com.cn,DIRECT,pre-matching
DOMAIN,wxs.qq.com,DIRECT,pre-matching
DOMAIN,res.wx.qq.com,DIRECT,pre-matching
DOMAIN,wxapp.tc.qq.com,DIRECT,pre-matching
DOMAIN,mmsns.qpic.cn,DIRECT,pre-matching
DOMAIN,shmmsns.qpic.cn,DIRECT,pre-matching
DOMAIN,wx.qlogo.cn,DIRECT,pre-matching
DOMAIN-SUFFIX,qpic.cn,DIRECT,pre-matching
DOMAIN-SUFFIX,gtimg.cn,DIRECT,pre-matching
DOMAIN-SUFFIX,weixinbridge.com,DIRECT,pre-matching
DOMAIN-SUFFIX,qlogo.cn,DIRECT,pre-matching
```

### 2. 增加常见图片 CDN 安全直连

已在 `Rules/direct.list` 增加：

```text
DOMAIN-SUFFIX,alicdn.com,DIRECT,pre-matching
DOMAIN-SUFFIX,alicdn.net,DIRECT,pre-matching
DOMAIN-SUFFIX,tbcdn.cn,DIRECT,pre-matching
DOMAIN-SUFFIX,taobaocdn.com,DIRECT,pre-matching
DOMAIN-SUFFIX,pddpic.com,DIRECT,pre-matching
DOMAIN-SUFFIX,360buyimg.com,DIRECT,pre-matching
DOMAIN-SUFFIX,jdimg.com,DIRECT,pre-matching
DOMAIN-SUFFIX,bdimg.com,DIRECT,pre-matching
DOMAIN-SUFFIX,hdslb.com,DIRECT,pre-matching
DOMAIN-SUFFIX,biliimg.com,DIRECT,pre-matching
DOMAIN-SUFFIX,bilivideo.com,DIRECT,pre-matching
DOMAIN-SUFFIX,meituan.net,DIRECT,pre-matching
DOMAIN-SUFFIX,dpfile.com,DIRECT,pre-matching
DOMAIN-SUFFIX,msstatic.com,DIRECT,pre-matching
DOMAIN-SUFFIX,zdmimg.com,DIRECT,pre-matching
DOMAIN-SUFFIX,amap.com,DIRECT,pre-matching
```

### 3. 收窄 app-cleaner active 匹配范围

已修改 `Scripts/app-cleaner-active.conf`：

- 移除宽泛 `qq.com` 级别匹配。
- 不使用 `gtimg.cn`、`qpic.cn`、通用 CDN 后缀进入 app-cleaner。
- 改成更接近接口级、服务级 endpoint 的匹配。

这样可以降低微信图片、普通图片 CDN、媒体文件被脚本入口命中的概率。

## 暂未执行的动作

没有直接删除 `Rules/reject.list` 中的原始规则。原因：

- 本轮先做保守止损，优先通过 direct pre-matching 和收窄脚本入口恢复图片与微信媒体链路。
- 如果仍异常，再逐项移除或降级 REJECT 规则，避免一次性放开过多广告规则。

## 用户需要测试

请重新运行构建后，在 Shadowrocket 中更新模块、脚本和全部资源，然后测试：

1. 微信发送图片。
2. 微信接收图片。
3. 微信朋友圈图片预览。
4. 微信聊天图片预览。
5. 淘宝 / 拼多多 / 京东商品图。
6. Bilibili 封面图和视频页缩略图。
7. 美团 / 大众点评店铺图。
8. 斗鱼 / VGTime / 什么值得买图片加载。

## 如果仍然异常

下一步处理顺序：

1. 检查 Shadowrocket 日志中被 REJECT 的具体域名。
2. 把该域名加入 `Rules/direct.list` 的 emergency 部分。
3. 若日志显示命中 `app-cleaner-active-json-clean`，继续收窄 `Scripts/app-cleaner-active.conf`。
4. 若日志显示命中 MITM hostname，检查该域名是否应从 stable MITM 层移出。
5. 若日志显示被 `reject.list` 中精确域名拦截，再单条注释或删除，不做批量删除。

## 回滚方式

如果本次修复造成广告明显变多：

1. 回滚 `Rules/direct.list` 中本次新增的 emergency direct 规则。
2. 保留 `Scripts/app-cleaner-active.conf` 的收窄匹配，因为它对稳定性更安全。
3. 重新运行：

```bash
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
```

## 结论

本次属于误伤止损修复。专业仓库应该优先保证 App 正常运行，再追求去广告覆盖。图片 CDN、微信媒体、登录、验证码、支付前置链路不应被通用去广告逻辑粗暴命中。
