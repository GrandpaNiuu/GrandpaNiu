# MITM 策略

当前模块的 MITM hostname 数量已经较大。后续维护重点不是继续扩大 MITM，而是控制增长、记录来源、分层管理、降低误伤。

## 分层原则

### core

核心层只保留高价值、必须保护的功能域名：

- Spotify 播放保护。
- YouTube Enhance。
- 知乎增强净化。
- 其他必须依赖 HTTPS 解密才能稳定运行的核心脚本。

core 层变更后必须测试 Spotify、YouTube、知乎。

### app-clean

App 净化层用于常见 App 的广告净化，包括信息流、开屏、弹窗、横幅和活动卡片。

这类 hostname 必须有明确 App、明确接口用途和自动化验证计划。

### extended

扩展层用于低频 App、实验项或高风险观察项。

extended 不应默认进入稳定发布版本。需要更广覆盖时，只在 full profile 中测试。

### blocked

禁止为以下对象新增 MITM：

```text
银行
支付
验证码
登录
证书校验
账号安全
微信支付
支付宝支付
Cookie / Token / 账号状态接口
```

## 新增 MITM 规则

- 不允许无说明地追加通配符。
- 优先使用精确 hostname，而不是整域通配。
- 新增 hostname 必须写清影响 App、来源、用途和回滚方式。
- 只为广告净化、脚本响应体处理或明确必要接口启用 MITM。
- 如果登录、支付、验证码异常，优先检查 MITM。
- 临时测试 hostname 应进入 extended，不应直接进入 stable。

## 未来拆分计划

建议后续将 MITM 拆为：

```text
Rewrite/Sources/MITM-core.conf
Rewrite/Sources/MITM-app-clean.conf
Rewrite/Sources/MITM-extended.conf
```

Profile 建议：

```text
lite   = core
stable = core + app-clean
full   = core + app-clean + extended
```

在正式拆分前，必须生成 `reports/mitm_split_report.md`，确认没有重复 hostname，没有支付/登录/验证码/银行相关 hostname 被错误加入稳定层。

## 回滚

如果 MITM 改动导致异常：

1. 先关闭最近新增的 MITM hostname。
2. 再回滚对应脚本或 rewrite。
3. 不要直接删除 Spotify、YouTube、知乎核心 hostname。
4. 重新构建并运行 `validate_repository.py` 与 `repository_health_check.py`。
