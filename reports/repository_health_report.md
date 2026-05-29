# 仓库健康检查报告

生成时间：2026-05-30 07:15:35 +0800

## 总体状态

- 阻断问题：0
- 提醒事项：0
- 统一验证：通过
- Root 与 Release 一致：yes
- 启用远程源：11
- 启用候选源：7
- pending 脚本候选：1
- 脚本总数：104
- MITM hostname 数量：1009

## 模块区块行数

- Rule: 531
- URL Rewrite: 1597
- Header Rewrite: 5
- Body Rewrite: 455
- Map Local: 15
- Script: 214
- MITM: 2

## 阻断问题

- 无

## 提醒事项

- 无

## 缺失资料文件

- 无

## 缺失工作流

- 无

## 主模块缺失关键标记

- 无

## 重复脚本名

- 无

## 重复 MITM hostname

- 无

## README 失效本地链接

- 无

## Pending 脚本候选

- app2smile Tieba script

## 统一验证输出

```text
Repository validation passed.
```

## 后续维护建议

1. 每次修改源头文件后运行 Module Factory Build。
2. Root 与 Release 必须保持一致。
3. 新脚本默认 pending，不直接进入 stable。
4. 耗电异常时优先测试 lite profile。
5. 远程源连续失败 2 天后再处理，避免临时网络波动误删。
