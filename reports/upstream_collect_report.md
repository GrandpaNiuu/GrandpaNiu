# Upstream Collect Report

Date: 2026-05-30
Candidates total: 8
Added remote sources: 4
Added local rule groups: 0
Added script entries: 0
Skipped candidates: 4
Main module changed by collector: no
Root and Release matched before collector: yes
Root and Release match after collector: yes

This collector is conservative: it never searches the web, only reads `Rewrite/Remotes/candidates.json`, rejects risky keywords and untrusted repositories, keeps pending scripts out of the module, and never auto-replaces Spotify or YouTube core items.

## Added Remote Sources
- blackmatrix7 Hijacking: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Hijacking/Hijacking.list -> Rewrite/Remotes/sources.json; passed checks and was registered
- blackmatrix7 Privacy: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Privacy/Privacy.list -> Rewrite/Remotes/sources.json; passed checks and was registered
- ACL4SSR BanProgramAD: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanProgramAD.list -> Rewrite/Remotes/sources.json; passed checks and was registered
- ACL4SSR BanEasyListChina: https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanEasyListChina.list -> Rewrite/Remotes/sources.json; passed checks and was registered

## Added Local Rules
- none

## Added Scripts
- none

## Skipped Candidates
- blackmatrix7 Advertising Lite: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- Cats-Team AdRules DNS list: candidate disabled
- app2smile Tieba script: candidate disabled
- Maasea YouTube Enhance reference: candidate disabled

## Manual Test Needed
- yes, update the module and test affected Apps plus Spotify and YouTube core flows.
