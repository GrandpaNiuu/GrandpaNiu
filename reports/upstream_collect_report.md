# 候选源收集报告

- 日期：2026-08-03
- 候选总数：12
- 新增远程规则源：0
- 新增本地规则组：0
- 新增脚本入口：0
- 跳过候选源：12
- 收集器是否修改主模块：否
- 收集前 Root/Release 是否一致：是
- 收集后 Root/Release 是否一致：是

本收集器保持保守：不搜索全网，只读取 `Rewrite/Remotes/candidates.json`，拒绝风险词和不可信仓库，pending 脚本不会进入模块，也不会自动替换 Spotify / YouTube / 知乎核心项。

## 新增远程规则源
- 无

## 新增本地规则
- 无

## 新增脚本
- 无

## 跳过候选源
- blackmatrix7 Advertising Lite: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- blackmatrix7 Hijacking: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- blackmatrix7 Privacy: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- blackmatrix7 Advertising MiTV: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- ACL4SSR BanProgramAD: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- ACL4SSR BanEasyListChina: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- ACL4SSR BanEasyList: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- ACL4SSR BanEasyPrivacy: duplicate URL already present in sources, Rules, Scripts, or Rewrite/Sources
- Loyalsoldier reject domain set: candidate disabled
- Cats-Team AdRules DNS list: candidate disabled
- app2smile Tieba script: candidate disabled
- Maasea YouTube Enhance reference: candidate disabled

## 是否需要自动化验证
- 本次没有新增源，自动化验证可按需执行。
