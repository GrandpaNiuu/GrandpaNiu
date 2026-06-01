# GrandpaNiu AdGuard DNS 规则

这是从 GrandpaNiu 可迁移域名规则导出的 AdGuard DNS 文本规则。

规则地址：

```text
https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Android/adguard/GrandpaNiu-DNS.txt
```

## 怎么用

Android 系统自带的“私人 DNS”不能直接导入 txt 过滤规则。

如果要使用 `GrandpaNiu-DNS.txt`，请使用支持自定义过滤规则的方式，例如：

- AdGuard Android App
- AdGuard DNS 用户规则
- AdGuard Home 自定义过滤规则

## 能拦截什么

它主要通过域名、域名后缀和关键词拦截常见广告域名、追踪域名和部分 App 广告请求。IP-CIDR 规则不会写入 AdGuard DNS 文本，因为 DNS 规则主要处理域名。

它不保证去除所有广告，尤其是 YouTube、TikTok、Instagram、Facebook 等平台内嵌广告。
