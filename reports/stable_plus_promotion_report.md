# Stable Plus 晋级候选报告

生成时间：2026-06-11 09:23:11 +0800

本报告只生成晋级建议，不自动修改 `MITM-app-clean.conf`，也不会把 Stable Plus 或 Full 自动合并进 Stable。

## 总体结论

- Stable Plus hostname 总数：97
- 可进入人工复核的候选组：0
- 暂不可晋级组：9
- 晋级前必须确认 Stable 已通过核心流程测试。
- 任一登录、验证码、支付前置、订单页异常都不能晋级。

## 候选矩阵

| App 组 | App / 服务 | 匹配 hostname 数 | 是否含敏感词 | Stable Plus 测试状态 | 可进入晋级复核 | 原因 |
|---|---|---:|---|---|---|---|
| 视频娱乐 | 爱奇艺, AcFun, 芒果 TV, 咪咕视频, 虎牙, 快手 | 20 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |
| 电商消费 | 得物, 唯品会, 当当, 转转, 什么值得买, 永辉 | 13 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |
| 餐饮消费 | 瑞幸, 麦当劳, 星巴克 | 5 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |
| 出行旅游 | 携程, 去哪儿, 途家, 途牛, 航旅纵横, 飞常准, 南航, 东航 | 11 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |
| 内容资讯 | 豆瓣, LOFTER, 虎嗅, 澎湃, 华尔街见闻, 人民 App, ZAKER | 11 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |
| 招聘职场 | 猎聘, BOSS 直聘, 51job, 猪八戒 | 8 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |
| 学习办公 | 有道, WPS, 金山文档, 超星, 粉笔 | 7 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |
| 云盘工具 | 阿里云盘, 天翼云盘, 迅雷, 向日葵 | 6 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |
| 汽车硬件 | 汽车之家, 易车, 比亚迪, 小鹏, 小牛, 米家, Zepp, 萤石, Petkit | 15 | 否 | 未找到测试记录 | 否 | 没有 Stable Plus 对应该 App 组的测试行 |

## 可进入人工复核候选

- 无

## 晋级操作边界

- 本报告不自动晋级。
- 晋级只能单项进行，不允许把整个 Stable Plus 合并进 Stable。
- 晋级目标是 `Rewrite/Sources/MITM-app-clean.conf`。
- 晋级后必须重新生成四个 Release 版本。
- 晋级后必须重新运行 `validate_repository.py`、`validate_profiles.py`、`repository_health_check.py`。

## 目前结论

如果测试记录仍为未测试，则所有 App 组都不能晋级 Stable。
