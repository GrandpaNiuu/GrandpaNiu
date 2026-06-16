# GrandpaNiu 问题排查说明

本文件用于排查 `Ronghemokuai.sgmodule` 使用过程中的常见问题。原则：先定位、再局部修复，不要直接回滚或大面积删除规则。

## Spotify 自动跳歌 / 加载失败

优先检查：

1. Shadowrocket 是否已更新模块和脚本。
2. 是否只启用了 `Ronghemokuai.sgmodule`，没有同时启用其他 Spotify 模块。
3. `[Rule]` 最前面是否仍有 Spotify 白名单。
4. `[Header Rewrite]` 是否仍残留旧 app2smile 的 `header-del if-none-match`。
5. `[Script]` 是否只有一套 Spotify JSON/protobuf 处理链，且包含 `spotify-json` / `spotify-proto`。
6. `[MITM]` 是否包含 `spclient.wg.spotify.com` 和 `*spclient.spotify.com`。
7. 最近新增的远程规则是否误拦 Spotify 播放链路。

不要同时启用额外 Spotify 模块，避免同一 protobuf 接口被两套脚本重复处理。

## YouTube 转圈 / 播放异常

优先检查：

1. `[Script]` 是否仍有 `youtube.response`。
2. YouTube 相关 MITM hostname 是否存在。
3. `[Map Local]` 中是否存在 `googlevideo initplayback + oad` 拦截规则。
4. 最近是否新增 YouTube 相关 Body Rewrite 或 Map Local。

如果只有播放转圈，可以先临时注释 `googlevideo initplayback + oad` 相关规则测试，不要删除整个 YouTube Enhance。

## 知乎广告仍出现 / 知乎空白

优先检查：

1. Shadowrocket 是否更新模块和脚本。
2. HTTPS 解密是否开启，证书是否已信任。
3. `[Script]` 是否包含 `zhihu-enhance`。
4. `Scripts/zhihu-enhance.conf` 是否仍被 `stable.conf` 引用。
5. `[MITM]` 是否覆盖知乎需要的 hostname。
6. 杀掉知乎后台后重新打开。

如果知乎出现空白、刷新失败或评论异常，先临时关闭 `zhihu-enhance` 测试，不要删除整个模块。

## Bilibili 广告仍出现

当前 Bilibili 是局部净化，不是完整独立脚本模块。

优先检查：

1. `Rules/reject.list` 中 biliapi 相关规则是否仍存在。
2. `Rewrite/Sources/Map-Local.conf` 中 Bilibili 活动、搜索、广告素材、PGC 活动物料接口是否仍存在。
3. 是否因为 App 更新导致接口变更。

不要加入账号权益、付费内容或会员状态相关改写。

## 登录 / 支付 / 验证码异常

涉及淘宝、京东、拼多多、微信、支付宝、银行类 App 时，优先级最高。

处理步骤：

1. 临时关闭模块确认是否恢复。
2. 只启用本模块，关闭其他模块再次测试。
3. 检查最近新增的 `[Rule]`、`[Body Rewrite]`、`[Map Local]`、`[MITM]`。
4. 不要先删除远程规则源，先定位具体 App。
5. 如果是支付或验证码接口被误伤，应优先加 DIRECT 白名单或移除对应局部规则。

## 耗电异常

优先检查：

1. iPhone 设置中的 Shadowrocket 电池占比。
2. 最近是否新增高频 `http-response` 脚本。
3. 最近是否扩大 MITM hostname。
4. 最近是否新增 YouTube、知乎、小红书、微博、淘宝等高频接口 Body Rewrite。
5. 是否长时间刷视频、信息流或直播。

处理方式：

1. 查看 `docs/PERFORMANCE.md`。
2. 测试 `Rewrite/Profiles/lite.conf`。
3. 优先减少脚本和 MITM，不要先删除远程规则源。

## GitHub Actions 失败

处理步骤：

1. 进入 Actions 页面。
2. 打开失败的工作流。
3. 查看失败步骤日志。
4. 不要从旧失败页面重复运行旧版本。
5. 回到 Actions 首页，运行最新的工作流。

`Daily Module Update` 只允许做检查和日期更新，不应自动删除规则。

## 模块无法一键导入

检查：

1. `README.md` 安装按钮是否指向 `redirect.html`。
2. `redirect.html` 是否存在。
3. GitHub Pages 是否已刷新。
4. iPhone 是否安装 Shadowrocket。
5. 是否使用 Safari 或 GitHub App 打开。

如果内置浏览器拦截跳转，使用 Safari 打开备用页面：

```text
https://grandpaniuu.github.io/GrandpaNiu/import.html
```

## 远程链接检查失败

每日报告中的 `CHECK_FAILED` 不一定代表失效，可能是临时网络问题。

处理原则：

1. 不要立即删除链接。
2. 手动打开链接确认。
3. 第二天仍失败再进一步检查。
4. 只有确认 404、410、仓库不存在、文件不存在，才考虑替换或删除。

## 新规则导致异常

处理步骤：

1. 查看最近一次提交。
2. 对比新增的规则类型。
3. 只回退新增的局部规则，不回滚整个仓库。
4. Spotify / YouTube / 知乎 / 登录 / 支付异常优先处理。
5. 修复后观察 24 小时。

## 快速稳定策略

如果出现多个 App 同时异常：

1. 停止继续添加新规则。
2. 保留 Spotify 白名单。
3. 保留 YouTube 核心脚本。
4. 保留知乎增强脚本，但可以临时关闭测试。
5. 回滚最近一次新增规则提交。
6. 测试 24 小时后再继续维护。
