# MITM 分层报告

当前状态：待运行 `scripts/split_mitm_sources.py` 后生成正式结果。

## 预期输出

- 原 MITM hostname 总数：待生成
- core 数量：待生成
- app-clean 数量：待生成
- extended 数量：待生成
- 未分类数量：待生成
- 是否存在重复 hostname：待生成
- 是否疑似包含支付 / 登录 / 验证码 / 银行相关 hostname：待生成
- stable 使用哪些 MITM 文件：待人工确认
- lite 使用哪些 MITM 文件：待人工确认
- full 使用哪些 MITM 文件：待人工确认

## 分层文件

运行脚本后应生成：

```text
Rewrite/Sources/MITM-core.conf
Rewrite/Sources/MITM-app-clean.conf
Rewrite/Sources/MITM-extended.conf
```

## 运行命令

```text
python3 scripts/split_mitm_sources.py
```

## 注意

- 本报告是占位模板，不代表 MITM 已经安全分层完成。
- 正式分层必须由脚本生成，并经过人工抽查。
- 切换 profile 使用分层 MITM 前，必须测试 Spotify、YouTube、知乎、登录、支付和验证码。
