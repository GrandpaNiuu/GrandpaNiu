# 手动测试标准

本文件用于记录模块发布前后的人工测试流程。自动化只能检查结构、链接和重复项，不能替代真实 App 使用测试。

## 测试前准备

1. 在 GitHub Actions 运行 `Module Factory Build`。
2. 确认 `reports/module_factory_diff_report.md` 中 `Diff lines = 0`。
3. 确认 `validate_repository.py` 与 `repository_health_check.py` 通过。
4. 在 Shadowrocket 中更新模块、更新脚本、更新全部资源。
5. 杀后台重开需要测试的 App。

## 必测对象

| 分类 | App / 服务 | 必测项目 |
|---|---|---|
| 核心播放 | Spotify | 连续播放 10 首歌、切歌、搜索、歌单加载 |
| 核心视频 | YouTube | 首页、搜索、播放、Shorts、评论区 |
| 核心净化 | 知乎 | 首页、回答页、搜索页、评论、点赞、收藏 |
| 局部净化 | Bilibili | 首页、搜索、播放页、评论区 |
| 电商 | 淘宝、京东、拼多多 | 首页、搜索、商品详情、购物车、订单页 |
| 本地生活 | 美团、大众点评、饿了么 | 首页、搜索、店铺页、下单流程前置页面 |
| 出行地图 | 滴滴、高德地图、百度地图、12306 | 首页、搜索、路线、订单/车票查询 |
| 敏感流程 | 微信、支付宝、银行 App | 登录、验证码、支付前置流程、消息推送 |

## 必测风险项

```text
登录
支付
验证码
视频播放
音乐播放
信息流刷新
搜索
评论
点赞
收藏
推送通知
```

## 测试结果记录

测试结果写入：

```text
reports/manual_test_log.md
```

不要伪造通过结果。没有测试就写“未测试”。

## 异常处理

出现异常时：

1. 先停用模块确认是否恢复。
2. 检查最近一次变更影响报告。
3. 检查是否涉及 MITM、Script、Body Rewrite、Map Local。
4. 优先回滚最近一次局部修改。
5. 不要直接删除 Spotify、YouTube、知乎核心脚本。
6. 修复后重新构建、同步、验证并再次测试。

## 回滚后验证

回滚后必须运行：

```text
python3 scripts/build_module.py --build --profile stable
python3 scripts/factory_finalize.py --sync-root
python3 scripts/validate_repository.py
python3 scripts/repository_health_check.py
```
