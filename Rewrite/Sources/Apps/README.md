# Rewrite Sources / Apps

This directory is reserved for app-scoped source fragments.

Target layout:

```text
Rewrite/Sources/Apps/
├─ spotify.conf
├─ youtube.conf
├─ zhihu.conf
├─ bilibili.conf
├─ rednote.conf
├─ wechat.conf
├─ qqnews.conf
└─ weibo.conf
```

Current policy:

- Do not move working fragments here until the generator reads app-level source files.
- App-specific fragments should be registered in `Rewrite/Generate.conf` and `Rewrite/Registry.md` before they are enabled.
- Generated output belongs under `Release/Modules/`, not here.
