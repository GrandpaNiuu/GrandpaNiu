# 安全策略与风险声明

GrandpaNiu 是个人自用的 Shadowrocket / Surge 融合净化模块工厂。仓库目标是广告净化、播放链路保护、网页广告过滤、App 弹窗 / 横幅 / 信息流广告清理，以及远程规则源的可用性审计。

本仓库不用于破解、绕过、伪造权益、处理账号敏感信息或破坏第三方服务正常运行。

安全修复必须遵循 source-first 原则：优先修改 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Remotes/`、`Rewrite/Profiles/`，然后重新构建 Release 并同步根目录主模块。

---

## 允许范围

本仓库允许处理：

```text
广告拦截
开屏广告清理
弹窗清理
横幅清理
信息流广告净化
推荐位清理
活动卡片清理
网页广告过滤
广告 SDK / 追踪统计域名过滤
Spotify 播放链路保护
YouTube Enhance 保留
知乎广告卡片净化
Bilibili 局部广告接口净化
远程规则源失效审计
源头驱动模块构建
报告生成与回滚维护
```

---

## 禁止范围

本仓库禁止加入或维护任何用于以下目的的内容：

```text
会员解锁
Premium 破解
付费内容绕过
支付绕过
登录绕过
账户权益伪造
账号状态修改
Cookie / Token 读取或修改
BoxJS 账号任务
签到薅羊毛脚本
证书绕过
风控绕过
验证码绕过
成人内容
博彩内容
灰产内容
恶意跳转
短链脚本
未知混淆脚本
ghproxy / mirror 正式源
来源不可验证脚本
```

如果某个规则、脚本或模块涉及上述行为，应立即移除，不得加入 `stable` profile，不得作为正式模块发布。

---

## 高风险区域

以下区域默认不做拦截、不做脚本改写、不做大范围 MITM：

```text
登录接口
支付接口
验证码接口
银行 App
微信
支付宝
账号安全接口
证书校验接口
Cookie / Token
会员权益字段
付费内容字段
钱包 / 余额 / 订单支付字段
```

如果这些 App 或接口中出现广告，只允许做极小范围、可回滚、可测试的局部处理。

---

## 脚本安全标准

新增脚本必须满足：

1. 来源公开、可信、可访问。
2. 必须使用 HTTPS 原始链接。
3. 不允许短链、代理、镜像链接。
4. 不允许混淆代码。
5. 不允许读取或修改 Cookie、Token、账号状态。
6. 不允许修改会员、付费、登录、支付、权益字段。
7. 不允许绕过验证码、支付、登录或证书校验。
8. `pattern` 必须精准，不能大范围覆盖无关接口。
9. MITM hostname 必须最小化。
10. 必须有明确回滚方式。
11. 默认进入 pending，不直接加入 `stable`。
12. 必须经过人工测试后再启用。

脚本放置规则：

```text
Scripts/spotify.conf        只放 Spotify 相关脚本
Scripts/youtube.conf        只放 YouTube 相关脚本
Scripts/zhihu-enhance.conf  只放知乎增强净化脚本
Scripts/app-clean.conf      普通 App 广告净化脚本
```

---

## 远程规则源安全标准

新增远程规则源必须满足：

1. 来源可信。
2. 链接可访问。
3. 内容格式明确。
4. 只用于广告、追踪、劫持、网页广告、App 广告 SDK 过滤。
5. 不使用短链、代理、镜像。
6. 不添加未知来源。
7. 不添加破解、会员、支付、登录、账号权益相关规则。
8. 必须能被报告追踪。
9. 必须可回滚。

候选源只允许写入：

```text
Rewrite/Remotes/candidates.json
```

通过检查后再进入：

```text
Rewrite/Remotes/sources.json
```

本仓库不开启全网大规模自动收集，只使用可信候选池。

---

## 失效源处理原则

失效源处理采用 source-first 策略。

优先处理源头文件：

```text
Rewrite/Remotes/sources.json
Rewrite/Remotes/candidates.json
Rules/*.list
Scripts/*.conf
Rewrite/Sources/*.conf
```

处理顺序：

1. 单日失败只记录，不删除。
2. 连续 2 天确认失败后才处理。
3. 优先查找同源可信替代链接。
4. 找不到替代时，优先禁用或注释。
5. 只有低风险独立远程规则才允许删除。
6. Spotify、YouTube、知乎增强、update-url、安装页、导入页只报告，不自动破坏。

禁止因为 GitHub 临时网络错误直接删除规则。

---

## 核心保护项

以下内容属于硬保护项，不应被自动删除、替换或注释：

```text
spotify-json
spotify-proto
youtube.response
zhihu-enhance
Spotify DIRECT 白名单
Spotify Header Rewrite
YouTube Enhance 脚本
知乎增强净化脚本
update-url
redirect.html
import.html
Ronghemokuai.sgmodule
Release/Ronghemokuai.sgmodule
```

Spotify 出现跳歌时，优先检查远程广告规则是否误杀播放链路，不要直接删除 Spotify 脚本。

YouTube 出现转圈时，优先检查 Map Local、MITM 和 YouTube 相关 rewrite，不要直接删除 YouTube Enhance。

知乎出现空白时，优先临时关闭 `zhihu-enhance` 测试，不要删除整个模块。

---

## MITM 安全策略

MITM hostname 必须控制范围。

允许：

```text
Spotify 必要域名
YouTube 必要域名
知乎广告净化必要域名
明确需要 HTTPS 解密的 App 广告接口
```

不建议：

```text
无脑追加通配符
大范围添加整个主域
覆盖银行、支付、验证码、登录接口
覆盖证书校验接口
覆盖账号安全接口
```

如果出现登录、支付、验证码异常，优先检查：

```text
Rewrite/Sources/MITM.conf
Rewrite/Sources/URL-Rewrite.conf
Rewrite/Sources/Body-Rewrite.conf
Scripts/*.conf
Rules/*.list
```

---

## 使用风险

使用本仓库内容可能产生以下风险：

```text
网络连接异常
App 加载失败
网页显示异常
广告拦截不完整
正常内容被误拦截
视频播放转圈
音乐播放跳歌
登录异常
支付异常
验证码异常
消息推送异常
App 账号风控
HTTPS 解密证书信任风险
电量消耗增加
流量消耗增加
设备发热
第三方规则源失效
第三方脚本源失效
GitHub 或上游仓库不可访问
规则更新导致兼容性变化
App 更新后接口变化导致规则失效
```

使用者应自行承担上述风险。本仓库维护者不对因使用、复制、修改、分发、导入或运行本仓库内容造成的任何直接或间接损失负责。

---

## 第三方来源风险

本仓库可能引用公开第三方规则源、脚本源或模块参考来源。第三方内容的版权、许可、可用性、安全性、准确性、稳定性和后续变更均由其原始维护者负责。

本仓库只做整理、引用、检查、过滤和保守维护，不代表对第三方内容进行担保。

第三方来源可能发生：

```text
仓库删除
文件迁移
链接失效
内容变更
规则误杀
脚本失效
上游停止维护
上游格式变化
上游加入不兼容规则
```

因此，任何远程规则或脚本在加入前都应经过检查；出现异常时，应优先查看失效源报告、构建报告和最近提交记录。

---

## HTTPS 解密风险

部分脚本、Body Rewrite、Map Local 和 App 净化功能可能依赖 MITM / HTTPS 解密。

启用 HTTPS 解密前，使用者应理解以下风险：

```text
需要安装并信任本地证书
可能影响部分 App 的正常通信
可能触发部分 App 的安全检测
可能导致登录、支付、验证码、银行类 App 异常
可能增加设备资源消耗
可能使调试和排查复杂度上升
```

本仓库不建议对银行、支付、验证码、登录、账号安全、证书校验等敏感接口进行大范围 MITM。若出现相关异常，应优先停用模块或缩小 MITM 范围。

---

## 账号与权益风险

本仓库不用于，也不接受任何用于以下目的的内容：

```text
会员解锁
Premium 破解
付费内容绕过
支付绕过
登录绕过
账户权益伪造
账号状态修改
Cookie / Token 读取或修改
BoxJS 账号任务
签到薅羊毛脚本
证书绕过
风控绕过
验证码绕过
```

如果某个规则、脚本或模块涉及上述行为，应立即移除，不得加入 `stable` profile，不得作为正式模块发布。

---

## 合规风险

使用者需要自行确认本仓库内容的使用方式是否符合：

```text
所在地法律法规
网络服务提供商规则
App 用户协议
平台服务条款
公司 / 学校 / 组织网络管理规定
第三方开源项目许可证
```

本仓库不鼓励、不支持、不提供任何违法违规、侵犯第三方权益、绕过付费机制、规避平台风控或破坏服务正常运行的用途。

---

## 数据与隐私风险

本仓库不主动收集个人数据，也不应加入任何收集、上传、记录或转发个人隐私信息的脚本。

禁止加入以下类型逻辑：

```text
上传 Cookie
上传 Token
上传账号信息
上传设备标识
上传定位信息
上传通讯录
上传浏览记录
上传请求体中的敏感字段
记录用户隐私数据
转发用户请求内容到未知服务器
```

若发现脚本存在此类行为，应立即删除或禁用，并在安全报告中标记为高风险来源。

---

## 可用性声明

本仓库不保证：

```text
所有广告都能去除
所有 App 都能正常使用
所有规则永久有效
所有上游链接永久可访问
所有脚本长期兼容
所有系统版本都能正常运行
所有网络环境都能正常更新
```

App、系统、Shadowrocket、Surge、GitHub、第三方规则源或脚本源的更新，都可能导致模块行为变化。

---

## 维护与回滚责任

使用者在更新模块前，应自行备份可用版本。

推荐保留：

```text
当前可用的 Ronghemokuai.sgmodule
Release/Ronghemokuai.sgmodule
backup/ 中的稳定备份
最近一次可用 Git commit
```

出现异常时，应优先按以下顺序处理：

```text
临时停用模块
回滚最近一次提交
切换到稳定备份
检查 reports/ 下的报告
检查最近新增 Rules / Scripts / Rewrite / MITM
逐项恢复，而不是一次性删除整个仓库结构
```

---

## 安全问题处理流程

发现风险后，按以下顺序处理：

1. 停止新增规则或脚本。
2. 确认是否由最近提交引起。
3. 检查最近修改的 Rules、Scripts、Rewrite、MITM、Remotes。
4. 优先回滚局部修改，不回滚整个仓库。
5. 保留 Spotify、YouTube、知乎核心保护项。
6. 修复后运行完整验证。
7. 在 Shadowrocket 中重新测试。

必须运行：

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

---

## 发布前安全检查

每次发布前必须确认：

```text
Root 与 Release 完全一致
validate_repository.py 通过
repository_health_check.py 通过
没有重复脚本名
没有重复 MITM hostname
README 本地链接有效
update-url 正确
spotify-json 存在
spotify-proto 存在
youtube.response 存在
zhihu-enhance 存在
没有新增高风险脚本
没有新增破解、支付、登录、账号权益相关内容
```

Shadowrocket 中必须测试：

```text
Spotify 连续播放
YouTube 首页、搜索、播放、Shorts
知乎首页、回答页、搜索页
Bilibili 首页、搜索、播放页
淘宝 / 京东 / 拼多多基础浏览
微信 / 支付宝 / 银行 App 登录、支付、验证码
```

---

## 最终声明

使用本仓库即代表使用者理解并接受：

```text
本仓库为个人自用维护项目
本仓库不提供任何使用担保
本仓库不承担第三方规则源或脚本源责任
本仓库不承担使用者设备、账号、网络、数据、支付、登录或业务损失责任
使用者需自行承担配置、导入、修改、运行和分发带来的全部风险
```

如无法理解 HTTPS 解密、MITM、脚本改写、远程规则源和代理配置可能带来的影响，不建议直接使用本仓库的完整模块。
