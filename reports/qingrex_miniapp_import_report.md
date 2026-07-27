# QingRex mini-program/app module import report

- Status: downloaded upstream and regenerated source layers
- Upstream: https://raw.githubusercontent.com/QingRex/LoonKissSurge/refs/heads/main/Surge/Official/%E5%B0%8F%E7%A8%8B%E5%BA%8F%E5%92%8C%E5%BA%94%E7%94%A8%E6%87%92%E4%BA%BA%E5%8E%BB%E5%B9%BF%E5%91%8A%E5%90%88%E9%9B%86.official.sgmodule
- Generated at: 2026-07-28 02:09:11
- Integration: source-first layer, connected through Rewrite/Profiles/fusion.conf.
- Rollback: remove qingrex_miniapp* entries from Rewrite/Profiles/fusion.conf and rebuild Fusion.

## Imported sections

| Section | Target | Active lines |
|---|---|---:|
| Rule | `Rules/qingrex-miniapp-app-ad.list` | 83 |
| URL Rewrite | `Rewrite/Sources/URL-Rewrite-qingrex-miniapp-app-ad.conf` | 54 |
| Body Rewrite | `Rewrite/Sources/Body-Rewrite-qingrex-miniapp-app-ad.conf` | 5 |
| Map Local | `Rewrite/Sources/Map-Local-qingrex-miniapp-app-ad.conf` | 137 |
| Script | `Scripts/qingrex-miniapp-app-ad.conf` | 0 |
| MITM | `Rewrite/Sources/MITM-qingrex-miniapp-app-ad.conf` | 1 |

## Function summary

- App and mini-program ad domain/IP rejects.
- Mini-program URL reject rules for popups, splash ads, banners and recommendation placements.
- Map Local mock responses for empty ad/config payloads.
- jq Body Rewrite cleanup for selected ad payload fields.
- QingRex response-body script entries stay inactive because the same endpoints are covered by Rewrite/Sources/Apps/wechat-mini-programs.conf.
- MITM hostname coverage required by these rewrite/map-local/script rules.

## Excluded from Stable import

These lines are intentionally not imported into Fusion because they are not pure ad-removal entries or have high false-positive risk.

```text
#>安全浏览限制解除
DOMAIN,lookup.api.bsb.baidu.com,REJECT,extended-matching,pre-matching
DOMAIN-SUFFIX,u3.ucweb.com,REJECT,extended-matching,pre-matching
DOMAIN-KEYWORD,safebrowsing.,REJECT,extended-matching,pre-matching

DOMAIN,dns.weixin.qq.com.cn,REJECT,extended-matching,pre-matching
DOMAIN,dns.weixin.qq.com,REJECT,extended-matching,pre-matching
```
