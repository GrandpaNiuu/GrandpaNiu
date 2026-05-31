#!/usr/bin/env python3
"""Score upstream candidates before any promotion into modules."""

from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "Rewrite" / "Remotes" / "candidates.json"
REPORT = ROOT / "reports" / "candidate_security_score_report.md"

SHORT_LINK_HOSTS = {"bit.ly", "t.co", "tinyurl.com", "goo.gl", "is.gd", "cutt.ly", "reurl.cc"}
PROXY_TOKENS = ["ghproxy", "mirror", "fastgit", "gh.llkk.cc", "raw.iqiq.io"]
OBFUSCATION_TOKENS = ["eval(", "atob(", "obfusc", "jjencode", "aaencode", "base64", "crypto-js", "minified"]
COOKIE_TOKEN_TOKENS = ["cookie", "token", "boxjs", "session", "authorization", "bearer"]
PAYMENT_LOGIN_TOKENS = ["login", "auth", "passport", "captcha", "verify", "payment", "pay", "wallet", "bank", "alipay", "wechatpay"]
MEMBERSHIP_TOKENS = ["premium", "vip", "member", "membership", "unlock", "paywall", "entitlement", "paid"]
RULE_HINTS = ["rule-set", "domain-set", "domain", "domain-suffix", "reject", "advert", "privacy", "tracker", "hijacking"]

ALLOWED_VERDICTS = {"safe-rule-candidate", "stable-plus-only", "manual-review", "blocked"}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def load_json(path: Path) -> dict:
    try:
        return json.loads(read(path))
    except Exception:
        return {}


def hits(text: str, tokens: list[str]) -> list[str]:
    lowered = text.lower()
    return sorted({token for token in tokens if token.lower() in lowered})


def trusted_score(url: str, trusted: list[str]) -> tuple[int, str]:
    lowered = url.lower()
    for repo in trusted:
        if repo.lower() in lowered:
            return 95, repo
    return 40, "unknown"


def bool_label(value: bool) -> str:
    return "是" if value else "否"


def risk_label(items: list[str]) -> str:
    return "高：" + ", ".join(items) if items else "低"


def request_body_risk(item: dict, combined: str) -> str:
    entry = str(item.get("script_entry", ""))
    if "requires-body=1" in entry or "type=http-request" in entry or "request-body" in combined.lower():
        return "中"
    return "低"


def license_status(item: dict) -> str:
    if item.get("license"):
        return str(item["license"])
    if item.get("kind") == "remote_rule":
        return "upstream-public-rule"
    if item.get("kind") == "reference_module":
        return "reference-only"
    return "unknown"


def final_verdict(item: dict, combined: str, fields: dict[str, str | int]) -> str:
    kind = str(item.get("kind", "unknown"))
    enabled = bool(item.get("enabled", False))
    activate = bool(item.get("activate", False))
    disabled_reason = str(item.get("disabled_reason", ""))

    if fields["obfuscation_risk"] != "低":
        return "blocked"
    if fields["cookie_token_risk"] != "低":
        return "blocked"
    if fields["payment_login_risk"] != "低":
        return "blocked"
    if fields["membership_unlock_risk"] != "低":
        return "blocked"
    if any(token in combined.lower() for token in PROXY_TOKENS):
        return "blocked"
    if urlparse(str(item.get("url", ""))).netloc.lower() in SHORT_LINK_HOSTS:
        return "blocked"
    if "404" in disabled_reason or "confirmed" in disabled_reason.lower():
        return "manual-review"
    if kind == "script":
        return "manual-review"
    if kind == "reference_module":
        return "manual-review"
    if kind == "remote_rule" and enabled and activate and int(fields["source_trust_score"]) >= 80:
        return "safe-rule-candidate"
    if kind == "remote_rule":
        return "manual-review"
    return "manual-review"


def score_candidate(item: dict, trusted: list[str]) -> dict[str, object]:
    name = str(item.get("name", "unnamed"))
    kind = str(item.get("kind", "unknown"))
    url = str(item.get("url", ""))
    combined = " ".join(
        [
            name,
            kind,
            url,
            str(item.get("status", "")),
            str(item.get("purpose", "")),
            str(item.get("script_entry", "")),
            str(item.get("disabled_reason", "")),
        ]
    )
    trust, trust_note = trusted_score(url, trusted)
    obfuscation = hits(combined, OBFUSCATION_TOKENS)
    cookie_token = hits(combined, COOKIE_TOKEN_TOKENS)
    payment_login = hits(combined, PAYMENT_LOGIN_TOKENS)
    membership = hits(combined, MEMBERSHIP_TOKENS)
    rule_hint = hits(combined, RULE_HINTS)
    rollback = "是" if item.get("target") or kind in {"remote_rule", "reference_module"} else "否"

    fields: dict[str, str | int] = {
        "source_trust_score": trust,
        "obfuscation_risk": risk_label(obfuscation),
        "request_body_risk": request_body_risk(item, combined),
        "cookie_token_risk": risk_label(cookie_token),
        "payment_login_risk": risk_label(payment_login),
        "membership_unlock_risk": risk_label(membership),
        "license_status": license_status(item),
        "rollback_available": rollback,
    }
    verdict = final_verdict(item, combined, fields)
    assert verdict in ALLOWED_VERDICTS
    reasons = [f"trust={trust_note}"]
    if rule_hint:
        reasons.append("rule-hints=" + ",".join(rule_hint[:6]))
    if str(item.get("disabled_reason", "")):
        reasons.append("disabled=" + str(item.get("disabled_reason", "")))
    if kind == "script":
        reasons.append("script默认 pending，不能自动进入 stable")
    if kind == "reference_module":
        reasons.append("reference only")

    return {
        "name": name,
        "kind": kind,
        "enabled": bool_label(bool(item.get("enabled", False))),
        "activate": bool_label(bool(item.get("activate", False))),
        "url": url,
        "final_verdict": verdict,
        "reasons": "; ".join(reasons),
        **fields,
    }


def main() -> None:
    data = load_json(CANDIDATES)
    trusted = [str(item) for item in data.get("trusted_repositories", [])]
    candidates = data.get("candidates", []) if isinstance(data.get("candidates", []), list) else []
    rows = [score_candidate(item, trusted) for item in candidates if isinstance(item, dict)]
    counts = {verdict: 0 for verdict in sorted(ALLOWED_VERDICTS)}
    for row in rows:
        counts[str(row["final_verdict"])] += 1

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# 候选源安全评分报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告只评分候选源，不自动启用、禁用、下载、替换或晋级 Stable。未知脚本默认 `manual-review`，高风险内容一律 `blocked`。",
        "",
        "## 统计",
        "",
        f"- 候选总数：{len(rows)}",
        f"- safe-rule-candidate：{counts['safe-rule-candidate']}",
        f"- stable-plus-only：{counts['stable-plus-only']}",
        f"- manual-review：{counts['manual-review']}",
        f"- blocked：{counts['blocked']}",
        "",
        "## 结论定义",
        "",
        "- `safe-rule-candidate`：可信、低风险、规则类候选，可继续进入候选收集和测试流程。",
        "- `stable-plus-only`：只适合测试版，不进入默认 Stable。",
        "- `manual-review`：需要人工复核，不能自动进入默认模块。",
        "- `blocked`：不得进入任何默认模块。",
        "",
        "## 评分明细",
        "",
        "| 候选 | 类型 | 启用 | 激活 | source_trust_score | obfuscation_risk | request_body_risk | cookie_token_risk | payment_login_risk | membership_unlock_risk | license_status | rollback_available | final_verdict | 原因 | URL |",
        "|---|---|---|---|---:|---|---|---|---|---|---|---|---|---|---|",
    ]
    for row in rows:
        lines.append(
            "| {name} | {kind} | {enabled} | {activate} | {source_trust_score} | {obfuscation_risk} | {request_body_risk} | {cookie_token_risk} | {payment_login_risk} | {membership_unlock_risk} | {license_status} | {rollback_available} | {final_verdict} | {reasons} | `{url}` |".format(
                **row
            )
        )
    lines += [
        "",
        "## 安全边界",
        "",
        "- `blocked` 不得进入任何默认模块。",
        "- 未知脚本默认 `manual-review`。",
        "- 混淆脚本必须 `blocked`。",
        "- Cookie / Token / BoxJS 必须 `blocked`。",
        "- 会员破解 / 权益伪造必须 `blocked`。",
        "- request-body 脚本默认不能进 Stable。",
        "- 普通规则源可以进入 pending 或候选收集，但不能无审核进 Stable。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Candidate security score report written to {REPORT}")


if __name__ == "__main__":
    main()
