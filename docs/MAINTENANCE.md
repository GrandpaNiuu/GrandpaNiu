# GrandpaNiu 模块维护说明

本仓库以 `Ronghemokuai.sgmodule` 作为唯一主模块入口。维护原则是：稳定优先、局部修复、少量新增、可回滚。

## 目录结构

```text
Ronghemokuai.sgmodule              主模块，Shadowrocket / Surge 导入入口
README.md                          仓库说明和一键安装入口
import.html                        备用导入页面
redirect.html                      Shadowrocket 跳转页
.github/workflows/                 自动更新、检查、维护工作流
scripts/                           审计、迁移、安全整理脚本
reports/                           每日检查报告、迁移报告、整理报告
docs/                              维护说明和问题排查文档
```

## 每日维护

每天通常不需要修改仓库。只需要观察和测试：

1. 查看 `Daily Module Update` 是否成功运行。
2. 查看 `reports/daily_update_report.md` 是否生成或更新。
3. 在 Shadowrocket 中更新模块、更新脚本、更新全部。
4. 测试 Spotify 播放、歌手页、专辑页是否正常。
5. 测试 YouTube 首页、搜索、播放、Shorts 是否正常。
6. 测试淘宝、京东、拼多多、微信、支付宝、银行类 App 的登录、支付、验证码。

若没有异常，不要修改仓库。

## 每周维护

每周检查一次：

1. `reports/daily_update_report.md` 中是否有远程链接失败。
2. `Ronghemokuai.sgmodule` 是否仍包含 `[Rule]`、`[Script]`、`[MITM]`。
3. `spotify-json`、`spotify-proto`、`youtube.response` 是否仍存在。
4. README 的一键安装按钮是否能打开跳转页。
5. GitHub Pages 模块地址是否能访问。

## 每月维护

每月做一次低风险整理：

1. 检查重复规则、重复脚本名、重复 MITM hostname。
2. 检查远程 `script-path`、`RULE-SET`、`DOMAIN-SET` 是否可访问。
3. 只生成审计报告，不自动删除规则。
4. 如果当前版本稳定，记录当前提交哈希，必要时复制为稳定备份。

## 新增规则原则

新增规则必须按类别小步添加，不要一次性全网堆叠。

推荐顺序：

```text
音乐类：Spotify / QQ 音乐 / 网易云 / 酷狗 / 喜马拉雅
视频类：YouTube / Bilibili / 优酷 / 爱奇艺 / 芒果 / 腾讯视频
社交类：微博 / 小红书 / 知乎 / 贴吧 / Soul
电商类：淘宝 / 京东 / 拼多多 / 闲鱼 / 什么值得买
工具类：高德 / 百度地图 / 有道 / Keep / 12306
网页类：通用网页广告 / 追踪 / 统计
```

每次只改一类，提交后观察 24 小时。

## 禁止加入内容

不要加入以下内容：

```text
会员解锁
Premium 破解
支付绕过
登录绕过
账户权益伪造
证书绕过
Cookie 签到任务
BoxJS 账号任务
成人内容
博彩内容
短链跳转脚本
未知混淆脚本
```

## 修改前检查

每次修改 `Ronghemokuai.sgmodule` 前，先确认：

1. 是否会影响 Spotify。
2. 是否会影响 YouTube。
3. 是否会影响登录、支付、验证码。
4. 是否新增了 MITM hostname。
5. 是否新增了远程脚本。
6. 是否可以快速回滚。

## 推荐提交说明

```text
Daily module update
Fix Spotify playback conflict
Update YouTube enhancement rules
Migrate selected valid legacy ad rules
Audit and refine merged adblock module
Add maintenance documentation
```

不要使用过于模糊的提交说明，例如 `update`、`fix`、`改一下`。
