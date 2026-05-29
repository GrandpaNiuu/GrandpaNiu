# Invalid Sources Audit and Repair Report

- 日期：2026-05-30
- 维护模式：source-first
- 扫描源文件链接总数：356
- 正常链接数量：355
- 本次是否修改源头文件：no

本系统优先修复 `Rewrite/Remotes/`、`Rules/`、`Scripts/`、`Rewrite/Sources/`，随后由工作流重新构建 Release 并同步根目录主模块。不会因单日失败删除规则。

## 今日首次失败链接
- `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PrivacyLite/PrivacyLite.list`

## 连续失败 2 天链接
- 无

## 已自动替换链接
- 无

## 已自动注释链接
- 无

## 已自动删除链接
- 无

## 已自动禁用 JSON 源
- 无

## 受保护但失败链接
- 无

## 需要人工确认链接
- 无

## 今日失败明细
- `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PrivacyLite/PrivacyLite.list (HTTP 404 HTTP 404)`
