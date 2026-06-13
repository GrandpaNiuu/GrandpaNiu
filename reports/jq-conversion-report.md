# JQ 转换扫描报告

生成时间：2026-06-13

## 扫描范围

- 目录：`Rewrite/Sources/Apps/*.conf`
- 目标：`[Body Rewrite]` 中可安全转换为 `http-response-jq` 的 JSON 删除 / JSON 替换规则，以及 `[Script]` 中 `type=http-response` 且 `requires-body=true` / `requires-body=1` 的外部脚本规则。
- 明确跳过：YouTube、Spotify、Bilibili protobuf、支付、登录、会员、票务、网盘权益类接口。

## 转换原则

- 只转换结构明确、作用域窄、明显属于广告 / 推荐 / 搜索推荐清理的 JSON 规则。
- 只在能保留原接口匹配范围、并能用 JQ 表达原有 JSON 删除 / 清空 / 替换 / 过滤逻辑时删除外部 `script-path`。
- 不转换会员权益、支付状态、登录认证、账号等级、票务、网盘容量 / 权益等高风险接口。
- 不转换 protobuf、binary-body、加密、签名、token、外部请求、运行参数依赖或复杂 JS 分支逻辑。
- 已经是 `http-response-jq` 的规则保持不变。

## 转换结果

| 文件 | 原规则类型 | 处理结果 | 说明 |
| --- | --- | --- | --- |
| `Rewrite/Sources/Apps/zhihu.conf` | `http-response` JSON 替换 | 已转换为 `http-response-jq` | 将搜索推荐字段 `recommend_queries` 置为空对象，属于安全广告 / 推荐清理范围。 |
| `Rewrite/Sources/Apps/soul.conf` | `type=http-response` 外部脚本 | 已转换为 `http-response-jq` 并删除脚本 URL | 将 Soul 的聊天限制、聊天室列表、钻石入口、广场子标签、星球配置清理合并为 1 条 JQ，保留原接口匹配范围。 |

### 已转换规则摘要

```conf
http-response-jq ^https:\/\/api\.zhihu\.com\/search\/recommend_query\/v2\? 'if has("recommend_queries") then .recommend_queries = {} else . end'
```

```conf
http-response-jq ^https:\/\/(?:api-\w+|chat-live|post)\.soulapp\.cn\/(?:chat\/limitInfo|chatroom\/chatClassifyRoomList|homepage\/diamond\/position\/info|v2\/post\/recSquare\/subTabs|v6\/planet\/config) '...'
```

## 本轮统计

| 指标 | 数量 |
| --- | ---: |
| 已删除外部 `script-path` | 1 |
| 新增 `http-response-jq` | 1 |
| 新增 `jq-convert: no` 标记 | 16 |
| 尝试转换但未写入 | 1 |

## `jq-convert: no` 标记情况

| 文件 | 数量 | 原因 |
| --- | ---: | --- |
| `Rewrite/Sources/Apps/caiyun-weather.conf` | 1 | 外部 JS 行为无法确认是直接 JSON 删除 / 清空 / 过滤逻辑。 |
| `Rewrite/Sources/Apps/ithome.conf` | 1 | 脚本依赖 `#!arguments` 运行参数，直接转 JQ 会丢失可配置行为。 |
| `Rewrite/Sources/Apps/hupu.conf` | 4 | 外部 JS 行为无法确认是直接 JSON 删除 / 清空 / 过滤逻辑。 |
| `Rewrite/Sources/Apps/zhihu.conf` | 10 | 剩余脚本覆盖回答页、推荐流、热榜、详情页、配置接口等复杂逻辑，未确认可等价 JQ 化。 |

## 未写入项

| 文件 | 规则 | 结果 | 说明 |
| --- | --- | --- | --- |
| `Rewrite/Sources/Apps/mai-mai.conf` | 1 条 `type=http-response` 脚本 | 未写入 | 文件内存在支付相关 URL Rewrite，写入整文件时被安全检查拦截；未绕过处理。 |

## 跳过 / 不处理项

| 类型 | 处理 |
| --- | --- |
| YouTube / Spotify | 跳过。 |
| Bilibili protobuf | 跳过，protobuf 不适合 JQ JSON 转换。 |
| 支付、登录、会员、票务、网盘权益类接口 | 跳过，避免改变账号权益、订单、身份或安全状态。 |
| 外部 JS 复杂脚本 | 标记 `jq-convert: no`，不做 JQ 自动改写。 |
| URL Rewrite、Map Local、Rule、MITM | 不属于 JQ 脚本 URL 减量对象，保持原样。 |

## 校验结论

- `Rewrite/Sources/Apps/soul.conf` 已减少 1 条 Shadowrocket 外部脚本 URL。
- `Rewrite/Sources/Apps/zhihu.conf` 已保留此前完成的安全 JSON JQ 转换，并为剩余复杂脚本加标记。
- `Rewrite/Sources/Apps/caiyun-weather.conf`、`Rewrite/Sources/Apps/ithome.conf`、`Rewrite/Sources/Apps/hupu.conf` 已补充 `jq-convert: no` 标记。
- 未对 MITM hostname 做改动。
