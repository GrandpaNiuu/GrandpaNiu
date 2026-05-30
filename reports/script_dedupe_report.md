# 脚本去重报告

生成时间：2026-05-31 06:23:38 +0800

## QQ News script-path 去重

- 保留入口：`cmp_block_097_ad`
- 移除入口：无，`legacy_safe_qqnews` 已不存在
- script-path：`https://raw.githubusercontent.com/app2smile/rules/master/js/qq-news.js`
- 功能判断：保留入口覆盖 `legacy_safe_qqnews` 的 URL 范围，并额外覆盖 `gw/page/event_detail`。
- 操作类型：去重，不是功能删除。
- 后续要求：重新构建四个 Release 版本，并运行 validate_repository.py / validate_profiles.py。

## 被移除的原始行

- 无
