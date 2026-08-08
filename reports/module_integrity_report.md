# Fusion 模块完整性报告

- 日期：2026-08-08
- 结论：Fusion 输出语法结构、重复项、脚本入口、MITM hostname 和远程规则源索引均通过本地静态检查。
- 说明：跨规则包重复只作为信息记录；最终 `Ronghemokuai.sgmodule` 构建时会按 active line 去重，单独规则包仍保留各自可独立使用的交集。

## 输出模块

| 检查项 | 结果 |
|---|---|
| Root / Release 内容一致 | 通过 |
| 重复 section | 无 |
| 重复 active rule / rewrite / script / MITM line | 无 |
| Script 入口数 | 45 |
| MITM hostname 数 | 1189 |

## Section 规模

| Section | Active line 数 |
|---|---:|
| `Rule` | 1194 |
| `URL Rewrite` | 40 |
| `Header Rewrite` | 2 |
| `Body Rewrite` | 1435 |
| `Map Local` | 37 |
| `Script` | 45 |
| `MITM` | 1 |

## 规则源

| 检查项 | 结果 |
|---|---:|
| 本地规则 active entries | 3351 |
| 跨文件交集 entries | 1341 |
| 远程规则源总数 | 16 |
| 已启用远程规则源 | 14 |

## 维护边界

- 同一文件内部的重复 active rule 会阻断验证。
- 最终 Fusion 模块中的重复 active line、重复 script name、重复 MITM hostname 会阻断验证。
- 跨文件重复不直接删除，因为 Android 包、单 App 包和兼容包可能需要独立保留相同规则。
- 远程 URL 可用性以 `scripts/validate_remote_rule_syntax.py` 和 `scripts/audit_repair_invalid_sources.py` 的结果为准。
