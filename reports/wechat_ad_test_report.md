# 微信插入广告去除测试报告

## 目标

用户希望去除微信内插入广告。由于近期出现过微信不能发送图片、App 图片加载异常的问题，本次只做保守测试接入，不直接进入默认 GrandpaNiu / Stable。

## 当前策略

- 新增规则文件：`Rules/wechat-ad.list`
- 接入版本：`Stable Plus` only
- 不接入默认 `GrandpaNiu` / `Stable`
- 不新增微信 MITM
- 不新增微信脚本
- 不触碰微信媒体、登录、支付、验证码、小程序关键链路

## 已加入规则范围

### 腾讯广告 / 广点通

- `gdt.qq.com`
- `l.qq.com`
- `e.qq.com`
- `pgdt.gtimg.cn`
- `mi.gdt.qq.com`
- `ii.gdt.qq.com`
- `win.gdt.qq.com`
- `v.gdt.qq.com`
- `c.gdt.qq.com`
- `m.gdt.qq.com`
- `adsmind.gdtimg.com`

### 腾讯广告统计 / 展示端点

- `ad.qq.com`
- `adsfile.qq.com`
- `adfilter.imtt.qq.com`
- `adping.qq.com`
- `adpm.app.qq.com`
- `adsclick.qq.com`
- `adsgroup.qq.com`
- `adshmct.qq.com`
- `adslvfile.qq.com`
- `adslvseed.qq.com`
- `adsmind.apdcdn.tc.qq.com`
- `adsolution.imtt.qq.com`
- `adsrich.qq.com`
- `adstextview.qq.com`
- `adsview.qq.com`

## 明确不处理范围

以下域名不得加入微信广告规则：

- `qpic.cn`
- `gtimg.cn`
- `qlogo.cn`
- `wx.qq.com`
- `wxs.qq.com`
- `weixin.qq.com`
- `servicewechat.com`
- `wxapp.tc.qq.com`
- `wechatpay.cn`

原因：这些链路可能影响微信图片、头像、聊天图片、小程序资源、支付、登录和媒体上传。

## 测试步骤

请先启用 `GrandpaNiu Stable Plus`，不要启用多个模块。

1. 更新模块。
2. 更新脚本。
3. 更新全部资源。
4. 完全退出并重新打开 Shadowrocket。
5. 打开微信。
6. 测试微信聊天发送图片。
7. 测试微信接收图片。
8. 测试朋友圈图片加载。
9. 测试公众号文章图片加载。
10. 测试小程序打开和图片资源。
11. 测试微信支付前置页面，不需要真实付款。
12. 观察微信内广告插入是否减少。

## 通过条件

只有同时满足以下条件，才允许考虑晋级默认 Stable：

- 微信发送图片正常。
- 微信接收图片正常。
- 聊天图片预览正常。
- 朋友圈图片正常。
- 公众号文章图片正常。
- 小程序资源正常。
- 微信支付前置页面正常。
- 微信登录状态正常。
- 插入广告确实减少。
- Shadowrocket 日志没有微信媒体域名被 REJECT。

## 失败条件

出现以下任一情况，应立即回滚或保持 Stable Plus 测试，不得晋级默认 Stable：

- 微信不能发送图片。
- 微信不能接收图片。
- 朋友圈图片不加载。
- 小程序资源异常。
- 微信支付前置异常。
- 登录状态异常。
- 大量 `qpic.cn`、`gtimg.cn`、`wxs.qq.com`、`servicewechat.com` 被 REJECT。

## 回滚方式

1. 从 `Rewrite/Profiles/stable-plus.conf` 移除：

```text
wechat_ad_test = Rules/wechat-ad.list
```

2. 保留 `Rules/wechat-ad.list` 作为候选文件，但不接入任何 profile。
3. 重新运行：

```bash
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/build_release_variants.py
python3 scripts/validate_repository.py
python3 scripts/validate_profiles.py
```

## 当前结论

本次只是将微信广告插入去除加入 `Stable Plus` 测试。默认 `GrandpaNiu` / `Stable` 暂不加入，避免再次影响微信图片和媒体功能。
