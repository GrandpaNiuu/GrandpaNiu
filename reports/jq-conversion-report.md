# JQ 转换扫描报告

生成时间：2026-06-13

## 扫描范围

- 目录：`Rewrite/Sources/Apps/*.conf`
- 目标：Body Rewrite 中可安全转换为 `http-response-jq` 的 JSON 删除 / JSON 替换规则
- 明确跳过：YouTube、Spotify、Bilibili protobuf、支付、登录、会员、票务、网盘权益类接口

## 转换原则

- 只转换结构明确、作用域窄、明显属于广告 / 推荐 / 搜索推荐清理的 JSON 规则。
- 不转换脚本型 `type=http-response` 规则；这类规则依赖外部 JavaScript 逻辑，不属于直接 JSON 删除 / 替换表达式。
- 不转换会员权益、支付状态、登录认证、账号等级、票务、网盘容量 / 权益等高风险接口。
- 已经是 `http-response-jq` 的规则保持不变。

## 转换结果

| 文件 | 原规则类型 | 处理结果 | 说明 |
| --- | --- | --- | --- |
| `Rewrite/Sources/Apps/zhihu.conf` | `http-response` JSON 替换 | 已转换为 `http-response-jq` | 将搜索推荐字段 `recommend_queries` 置为空对象，属于安全广告 / 推荐清理范围。 |

### 已转换规则

```conf
http-response-jq ^https:\/\/api\.zhihu\.com\/search\/recommend_query\/v2\? 'if has("recommend_queries") then .recommend_queries = {} else . end'
```

## `jq-convert: no` 标记情况

本次扫描没有发现仍需保留为旧式 Body Rewrite JSON 删除 / 替换、且无法安全转换的规则，因此没有新增 `jq-convert: no` 标记。

以下内容未纳入 `jq-convert: no` 标记范围：

- `[Script]` 中的 `type=http-response` 脚本规则：不是直接 JSON 删除 / 替换规则。
- 已存在的 `http-response-jq` 规则：已经完成 JQ 化。
- URL Rewrite、Map Local、Rule、MITM：不是 Body Rewrite JSON 转换对象。

## 跳过 / 不处理项

| 类型 | 处理 |
| --- | --- |
| YouTube / Spotify | 不在本次 Apps JSON 转换范围内处理。 |
| Bilibili protobuf | 跳过，protobuf 不适合 JQ JSON 转换。 |
| 支付、登录、会员、票务、网盘权益类接口 | 跳过，避免改变账号权益、订单、身份或安全状态。 |
| 外部 JS 脚本响应规则 | 跳过，不做 JQ 自动改写。 |

## 校验结论

- `Rewrite/Sources/Apps/zhihu.conf` 中的旧式 Body Rewrite JSON 替换已完成 JQ 化。
- 本次没有发现其它需要转换的安全 JSON 广告旧式 Body Rewrite。
- 本次没有发现需要新增 `jq-convert: no` 的非 JQ Body Rewrite JSON 删除 / 替换规则。
