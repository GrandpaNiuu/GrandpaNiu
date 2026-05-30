# 贡献与维护规则

本仓库是源头驱动的 Shadowrocket / Surge 模块工厂。不要把 `Ronghemokuai.sgmodule` 当作唯一长期维护源头；它是最终生成结果。

无论是人工维护者、GPT、Codex，还是其他自动化工具，都必须遵守同一套 source-first 规则。

## 修改应该放在哪里

| 类型 | 位置 |
|---|---|
| 新增可信远程规则候选 | `Rewrite/Remotes/candidates.json` |
| 已验证稳定远程规则 | `Rewrite/Remotes/sources.json` |
| 本地域名 / IP / 规则 | `Rules/*.list` |
| URL Rewrite / Body Rewrite / Map Local / MITM | `Rewrite/Sources/*.conf` |
| Spotify 脚本 | `Scripts/spotify.conf` |
| YouTube 脚本 | `Scripts/youtube.conf` |
| 知乎增强脚本 | `Scripts/zhihu-enhance.conf` 与 `Scripts/zhihu-enhance.js` |
| 普通 App 净化脚本 | `Scripts/app-clean.conf` |
| 文档 | `docs/*.md`、`README.md`、`SECURITY.md` 等 |
| 报告 | `reports/*` |

## 脚本规则

- 新脚本默认保持 pending，不直接进入 `stable`。
- 不添加未知混淆脚本。
- 不添加会修改会员、付费、登录、支付、账号权益、Cookie、Token、验证码、付费内容的脚本。
- 不添加 BoxJS 账号任务、签到任务或账号敏感任务。
- `pattern` 必须精准，不能覆盖无关接口。
- MITM hostname 必须最小化。
- 新脚本启用前必须能说明来源、用途、影响 App、回滚方式和测试范围。

## 禁止内容

禁止加入：

```text
会员解锁
Premium 破解
支付绕过
登录绕过
账户权益伪造
证书绕过
Cookie / Token / BoxJS 账号任务
成人内容
博彩内容
灰产内容
短链脚本
未知混淆脚本
ghproxy / mirror 正式源
来源不可验证脚本
```

## 必跑命令

修改后至少运行：

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```

涉及 profile、覆盖矩阵、变更影响、workflow、compat、MITM 时，还应运行对应生成脚本并更新报告。

## 变更说明必须包含

每次提交或交接说明应写清：

1. 修改了哪些源头文件。
2. 影响哪些 App 或服务。
3. 是否涉及脚本。
4. 是否涉及 MITM。
5. 是否涉及 Body Rewrite / Map Local。
6. 是否涉及远程规则源。
7. 更新了哪些报告。
8. 如何回滚。
9. Shadowrocket 里需要测试什么。

## 回滚原则

优先回滚最近一次提交。若模块输出异常，可使用：

```text
backup/Ronghemokuai.stable.sgmodule
backup/Ronghemokuai.before-factory-refactor.sgmodule
```

回滚后必须重新构建、同步、验证并生成健康报告。
