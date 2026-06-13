# 脚本审核清单

本清单用于判断脚本是否可以从候选或 pending 状态进入稳定配置。脚本风险高于普通规则，必须先审核、再测试、最后才允许进入 `stable`。

## 来源检查

- 来源必须公开、可信、可访问。
- URL 必须是 HTTPS，优先使用 raw GitHub 链接。
- 仓库所有者、文件路径、维护来源必须清楚。
- 不使用短链、`ghproxy`、镜像站或未知主机。
- 不使用无法确认来源的复制脚本。

## 代码安全

- 不允许未知混淆代码。
- 不允许采集 Cookie 或 Token。
- 不允许采集 Authorization header。
- 不允许修改会员、Premium、支付、登录、账号权益或付费内容字段。
- 不允许成人、博彩、灰产、签到薅羊毛或账号任务逻辑。
- 不允许把用户请求内容转发到未知服务器。

## 请求范围

- `pattern` 必须精准，并且只匹配目标 App 的广告或净化接口。
- 不得匹配登录、支付、验证码、银行、微信、支付宝、证书校验或账号安全接口。
- `requires-body` 必须确有必要。
- `max-size` 应与接口响应体规模匹配，避免过大范围解析。
- 二进制 body 模式只在明确需要时使用。

## MITM 范围

- hostname 必须最小化。
- 优先精确 hostname，不优先使用大范围通配。
- 不允许扩大到银行、支付、登录、验证码或账号安全域名。
- 新增 MITM 必须说明影响 App、用途和回滚方式。

## 放置位置

| 脚本类型 | 位置 |
|---|---|
| Spotify | `Scripts/spotify.conf` |
| YouTube | `Scripts/youtube.conf` |
| 知乎增强 | `Scripts/zhihu-enhance.conf` 或配套知乎专项文件 |
| 普通 App 净化 | `Scripts/app-clean.conf` |

新脚本默认 pending，除非经过人工审核和自动化验证，不得直接进入 `stable`。

## 测试要求

启用脚本前必须：

```text
python3 scripts/build_module.py --build --profile fusion
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

并自动化验证：

- 受影响 App 的首页、搜索、详情页、评论、刷新流程。
- Spotify、YouTube、知乎等核心链路。
- 登录、支付、验证码、微信、支付宝、银行类 App。

## 回滚要求

每个新增脚本必须能说明：

1. 删除或禁用哪一行脚本入口。
2. 是否需要移除对应 MITM hostname。
3. 是否需要回滚 Rules / Rewrite / Body Rewrite。
4. 回滚后应运行哪些验证命令。

不能说明回滚方式的脚本，不允许进入 stable。
