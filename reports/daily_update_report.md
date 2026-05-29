# 每日模块更新报告

日期：2026-05-30

## 关键结构检查

- [Rule]: 正常
- [Script]: 正常
- [MITM]: 正常
- spotify-json: 正常
- spotify-proto: 正常
- youtube.response: 正常
- update-url: 正常

## 远程链接检查

- `https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule`：OK HTTP 200
- `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list`：OK HTTP 200
- `https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list`：OK HTTP 200
- `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list`：OK HTTP 200
- `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-json.js`：OK HTTP 200
- `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-proto.js`：OK HTTP 200
- `https://raw.githubusercontent.com/Maasea/sgmodule/master/Script/Youtube/youtube.response.js`：OK HTTP 200

## 自动更新边界

- 只更新模块日期。
- 只生成每日检查报告。
- 不自动删除规则。
- 不自动注释 script-path。
- 不自动替换 Spotify / YouTube。
- 不自动修改 MITM hostname。

## 手动检查建议

1. 在 Shadowrocket 更新模块和脚本。
2. 测试 Spotify 播放是否跳歌。
3. 测试 YouTube 是否转圈。
4. 测试淘宝、京东、微信、支付宝、银行类 App 登录、支付、验证码是否正常。
