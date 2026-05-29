# Rules

本目录用于放置纯规则文件。

建议后续拆分：

```text
direct.list           白名单规则
reject.list           本地广告拦截规则
spotify-direct.list   Spotify 播放链路保护
youtube-direct.list   YouTube 播放链路保护
app-clean.list        常用 App 净化补充
web-ads.list          网页广告补充
```

当前阶段先建立目录，不迁移正式规则。

维护原则：

- 白名单优先，避免误杀播放、登录、支付、验证码。
- 本地拦截规则只放确认有效、低风险内容。
- 远程规则源登记在 `Rewrite/Remotes/Index.md`。
