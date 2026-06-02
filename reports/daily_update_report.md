# 每日模块更新报告

- 日期：2026-06-03
- 日期源头：Rewrite/Sources/Meta.conf
- 构建流程：Meta.conf -> build_module.py --build --profile stable -> factory_finalize.py --sync-root -> build_release_variants.py -> validate_repository.py -> repository_health_check.py

## 完整区块检查结果

- `[Rule]`：通过
- `[URL Rewrite]`：通过
- `[Header Rewrite]`：通过
- `[Body Rewrite]`：通过
- `[Map Local]`：通过
- `[Script]`：通过
- `[MITM]`：通过

## 核心检查结果

- `spotify-json`：通过
- `spotify-proto`：通过
- `youtube.response`：通过
- `zhihu-enhance`：通过
- `zhihu-enhance.js`：通过
- `update-url`：通过
- `meta-date`：通过

## 多版本文件检查

- `Release/Ronghemokuai-stable.sgmodule`：通过
- `Release/Ronghemokuai-stable-plus.sgmodule`：通过
- `Release/Ronghemokuai-lite.sgmodule`：通过
- `Release/Ronghemokuai-full.sgmodule`：通过

## 远程链接检查结果

- `https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule`：OK HTTP 200
- `https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/zhihu-enhance.js`：OK HTTP 200
- `https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Advertising/Advertising.list`：OK HTTP 200
- `https://raw.githubusercontent.com/Cats-Team/AdRules/main/adrules_surge_domainset.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/privacy-protection-tools/anti-AD/master/anti-ad-surge2.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/ACL4SSR/ACL4SSR/master/Clash/BanAD.list`：OK HTTP 200
- `https://raw.githubusercontent.com/Loyalsoldier/surge-rules/release/reject.txt`：OK HTTP 200
- `https://raw.githubusercontent.com/217heidai/adblockfilters/main/rules/adblocksurge.list`：OK HTTP 200
- `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-json.js`：OK HTTP 200
- `https://raw.githubusercontent.com/app2smile/rules/master/js/spotify-proto.js`：OK HTTP 200
- `https://raw.githubusercontent.com/Maasea/sgmodule/master/Script/Youtube/youtube.response.js`：OK HTTP 200

## validate_repository.py 输出

```text
Repository validation passed.
```

## 治理报告刷新输出

```text
$ validate_profiles.py
Profile validation report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/profile_validation_report.md

$ audit_reject_risk.py
Reject risk report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/reject_risk_report.md

$ generate_app_status_matrix.py
App status matrix written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/app_status_matrix.md

$ create_promotion_pr.py
Promotion PR report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/promotion_pr_report.md

$ score_candidates.py
Candidate security score report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/candidate_security_score_report.md

$ audit_domestic_app_connectivity.py
Domestic App connectivity audit written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/domestic_app_connectivity_audit.md

$ generate_workflow_health_report.py
Workflow health report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/workflow_health_report.md

$ check_report_freshness.py
Report freshness report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/report_freshness_report.md
```

## repository_health_check.py 输出

```text
Repository health report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/repository_health_report.md
```

## check_report_freshness.py 输出

```text
Report freshness report written to /home/runner/work/GrandpaNiu/GrandpaNiu/reports/report_freshness_report.md
```

## 自动更新边界说明

- 本 workflow 会更新源头日期、重新构建 stable、同步 Release 与 Root，并生成四个独立 Release 版本。
- 默认根目录 Ronghemokuai.sgmodule 仍保持 stable。
- 不自动删除规则。
- 不自动注释脚本。
- 不自动替换 Spotify / YouTube / 知乎核心脚本。
- 不自动修改 MITM hostname 内容；MITM 分层由 profile 选择，源头完整列表保留可回滚。
