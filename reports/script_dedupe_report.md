# 脚本去重与 app-cleaner active 迁移报告

生成时间：2026-05-31 07:36:16 +0800

## 本次迁移

- 迁移范围：QQ News、VGTime、SQKB、163News、小黑盒、Manner、超格教育、SMZDM、淘宝、吉祥航空、叮咚买菜、掌上公交、快看漫画、闲鱼、喜马拉雅、滴滴
- 新承接入口：`Scripts/app-cleaner-active.conf` / `app-cleaner-active-json-clean`
- 新承接脚本：`Scripts/app-cleaner.js`
- 计划替换旧入口数量：17
- Scripts/app-clean.conf 本次移除旧入口数量：0
- 所有源文件合计本次移除旧入口数量：0
- 新增 active 入口数量：1
- 说明：这是批量低风险 JSON / 字段清理融合，不是全量脚本合并。

## 移除的旧入口

### `Scripts/app-clean.conf`

- 无，目标旧入口已不存在。

### `Rewrite/Sources/Script.conf`

- 无，目标旧入口已不存在。

## 不变范围

- 不动 Spotify。
- 不动 YouTube。
- 不动知乎增强与知乎 R-Store 条目。
- 不动 Tieba JSON / proto。
- 不动小红书、Cotti、RRTV、网易云音乐等复杂脚本。
- 不动登录、支付、验证码、银行相关条目。
- 不合并复杂加密、持久化配置、会员权益、binary-body 脚本。
