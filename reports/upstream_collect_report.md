# Upstream Collect Report

Date: 2026-05-29
Candidates total: 4
Added remote sources: 1
Added local rule groups: 0
Added script entries: 0
Skipped candidates: 3
Main module changed by collector: no
Root and Release matched before collector: yes
Root and Release match after collector: yes

This collector is conservative: it never searches the web, only reads `Rewrite/Remotes/candidates.json`, rejects risky keywords and untrusted repositories, keeps pending scripts out of the module, and never auto-replaces Spotify or YouTube core items.

## Added Remote Sources
- blackmatrix7 Advertising Lite: https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/AdvertisingLite/AdvertisingLite.list -> Rewrite/Remotes/sources.json; passed checks and was registered

## Added Local Rules
- none

## Added Scripts
- none

## Skipped Candidates
- Cats-Team AdRules DNS list: risk keyword in content: premium, status=206
- app2smile Tieba script: candidate disabled
- Maasea YouTube Enhance reference: candidate disabled

## Manual Test Needed
- yes, update the module and test affected Apps plus Spotify and YouTube core flows.
