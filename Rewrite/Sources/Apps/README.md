# Rewrite Sources / Apps

This directory stores app-scoped source fragments used by the module factory.

`Release/Modules/*.sgmodule` is generated from these files by `scripts/build_release_modules.py`.
Do not edit generated files under `Release/Modules/` as the source of truth.

## Build behavior

1. Manual module specs are read from `Rewrite/Generate.conf` `[release_modules]`.
2. `Rewrite/Sources/Apps/*.conf` is scanned after manual specs are loaded.
3. If `<slug>.conf` is not manually registered, it is auto-discovered and generated with conservative keywords.
4. If a source file is missing for a manual spec, the builder falls back to extracting matching lines from `Release/Ronghemokuai.sgmodule`.
5. Empty modules are skipped unless `include_empty_modules = true` is set in `Rewrite/Generate.conf`.

## Active app source files

| Slug | Source | Registration |
|---|---|---|
| amap | `Rewrite/Sources/Apps/amap.conf` | auto-discovered |
| baidu | `Rewrite/Sources/Apps/baidu.conf` | auto-discovered |
| bilibili | `Rewrite/Sources/Apps/bilibili.conf` | manual |
| huya | `Rewrite/Sources/Apps/huya.conf` | manual |
| jd | `Rewrite/Sources/Apps/jd.conf` | manual |
| meituan | `Rewrite/Sources/Apps/meituan.conf` | auto-discovered |
| mgtv | `Rewrite/Sources/Apps/mgtv.conf` | manual |
| netease-music | `Rewrite/Sources/Apps/netease-music.conf` | manual |
| pcauto | `Rewrite/Sources/Apps/pcauto.conf` | manual |
| pinduoduo | `Rewrite/Sources/Apps/pinduoduo.conf` | manual |
| qqnews | `Rewrite/Sources/Apps/qqnews.conf` | manual |
| quark | `Rewrite/Sources/Apps/quark.conf` | auto-discovered |
| rednote | `Rewrite/Sources/Apps/rednote.conf` | manual |
| soul | `Rewrite/Sources/Apps/soul.conf` | auto-discovered |
| spotify | `Rewrite/Sources/Apps/spotify.conf` | manual |
| taobao | `Rewrite/Sources/Apps/taobao.conf` | manual |
| umetrip | `Rewrite/Sources/Apps/umetrip.conf` | manual |
| wechat | `Rewrite/Sources/Apps/wechat.conf` | manual |
| weibo | `Rewrite/Sources/Apps/weibo.conf` | manual |
| wps | `Rewrite/Sources/Apps/wps.conf` | auto-discovered |
| xiaopeng | `Rewrite/Sources/Apps/xiaopeng.conf` | manual |
| yiche | `Rewrite/Sources/Apps/yiche.conf` | manual |
| youku | `Rewrite/Sources/Apps/youku.conf` | auto-discovered |
| youtube | `Rewrite/Sources/Apps/youtube.conf` | manual |
| zdm | `Rewrite/Sources/Apps/zdm.conf` | auto-discovered |
| zhihu | `Rewrite/Sources/Apps/zhihu.conf` | manual |
| zuoyebang | `Rewrite/Sources/Apps/zuoyebang.conf` | auto-discovered |

## Maintenance rule

Keep app files conservative. Do not add payment bypasses, login bypasses, membership unlocking, token/cookie rewriting, or high-risk upstream script bundles. If an app fragment causes breakage, disable or narrow the app source and regenerate through:

```bash
python3 Rewrite/Generator/Builder.py --profile fusion --release
```
