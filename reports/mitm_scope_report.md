# MITM Scope Report

- Generated at: 2026-07-03 00:58:58 +0800
- Total hostnames: 1233
- Wildcard hostnames: 34
- Unique base domains: 673

## Category Counts

| Category | Hosts |
|---|---:|
| `payment_bank_wallet` | 2 |
| `login_account_auth` | 1 |
| `video_music_playback` | 29 |
| `image_static_cdn` | 16 |
| `httpdns` | 0 |
| `shopping_life` | 30 |
| `social_content` | 28 |
| `other_app_or_service` | 1127 |

## Top Base Domains

- `com.cn`: 72
- `qq.com`: 31
- `baidu.com`: 22
- `163.com`: 21
- `meituan.com`: 10
- `smzdm.com`: 10
- `kkmh.com`: 10
- `ksapisrv.com`: 9
- `zhihu.com`: 8
- `ximalaya.com`: 8
- `mgtv.com`: 8
- `miguvideo.com`: 8
- `kugou.com`: 8
- `amap.com`: 7
- `meituan.net`: 7
- `huxiu.com`: 7
- `yy.com`: 7
- `kakamobi.cn`: 7
- `aliyuncs.com`: 6
- `xiaojukeji.com`: 6
- `mi.com`: 6
- `net.cn`: 6
- `line.me`: 6
- `ksedt.com`: 6
- `qtfm.cn`: 6
- `douyucdn.cn`: 5
- `xiaohongshu.com`: 5
- `fcbox.com`: 5
- `youdao.com`: 5
- `umetrip.com`: 5
- `line-scdn.net`: 5
- `wtzw.com`: 5
- `qbb6.com`: 5
- `cainiao.com`: 5
- `moji.com`: 5
- `91160.com`: 5
- `bilibili.com`: 4
- `weibo.cn`: 4
- `elemecdn.com`: 4
- `maoyan.com`: 4

## Maintenance Notes

- This report is informational and does not change MITM behavior.
- Payment, bank, login, video playback and CDN categories should be narrowed only with real breakage evidence.
- Broad wildcard entries should keep a clear source path and rollback path in `Rewrite/Registry.md`.
