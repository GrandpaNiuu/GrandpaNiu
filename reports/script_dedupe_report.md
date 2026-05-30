# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-05-31 07:01:12 +0800

## 本次迁移

- 迁移范围：QQ News + VGTime
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-qqnews-vgtime`
- 新承接脚本：`Scripts/app-cleaner.js`
- Scripts/app-clean.conf 移除旧入口数量：0
- 所有源文件合计移除旧入口数量：0
- 新增 active 入口数量：1
- 目标：Stable 脚本数从 104 降到 102。

## 移除的旧入口

### `Scripts/app-clean.conf`

- 无，目标旧入口已不存在。

### `Rewrite/Sources/Script.conf`

- 无，目标旧入口已不存在。

## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强。
- 不动 Tieba JSON / proto。
- 不动登录、支付、验证码、银行相关条目。
