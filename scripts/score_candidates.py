#!/usr/bin/env python3
"""Score upstream candidates before any promotion into modules.

This script is report-only. It does not enable, disable, promote, delete, or fetch
remote content. It scores candidate metadata from Rewrite/Remotes/candidates.json
so risky candidates cannot be treated as safe by default.
"""

from __future__ import annotations

import datetime as dt
import json
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CANDIDATES = ROOT / "Rewrite" / "Remotes" / "candidates.json"
REPORT = ROOT / "reports" / "candidate_security_score_report.md"

BLOCK_KEYWORDS = (
    "premium", "unlock", "vip", "membership", "paywall", "paid", "cookie", "token", "boxjs",
    "login", "auth", "password", "payment", "pay", "captcha", "verify", "verification", "bank",
    "wallet", "account", "session", "porn", "adult", "gambling", "casino", "ghproxy", "mirror",
)
WARN_KEYWORDS = (
    "script", "request", "rewrite", "body", "header", "proxy", "redirect", "inject", "eval",
    "obfusc", "minify", "base64", "crypto", "aes", "rsa", "hook",
)
SAFE_KEYWORDS = (
    "advert", "advertising", "ad", "ads", "privacy", "hijacking", "reject", "tracker", "anti-ad",
    "domain-set", "rule-set", "surge", "lite",
)
SHORT_LINK_HOSTS = ("bit.ly", "t.co", "tinyurl.com", "goo.gl", "is.gd", "cutt.ly", "reurl.cc")


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


def trusted_hit(url: str, trusted: list[str]) -> str:
    lower = url.lower()
    for repo in trusted:
        if repo.lower() in lower:
            return repo
    return ""


def keyword_hits(text: str, keywords: tuple[str, ...]) -> list[str]:
    lower = text.lower()
    return sorted({keyword for keyword in keywords if keyword in lower})


def score_candidate(item: dict, trusted: list[str]) -> dict[str, str | int | list[str]]:
    name = str(item.get("name", "unnamed"))
    kind = str(item.get("kind", "unknown"))
    url = str(item.get("url", ""))
    status = str(item.get("status", ""))
    purpose = str(item.get("purpose", ""))
    enabled = bool(item.get("enabled", False))
    activate = bool(item.get("activate", False))
    protected = bool(item.get("protected", False))
    combined = " ".join([name, kind, url, status, purpose, str(item.get("script_entry", ""))])
    host = urlparse(url).netloc.lower()
    trusted_repo = trusted_hit(url, trusted)
    block_hits = keyword_hits(combined, BLOCK_KEYWORDS)
    warn_hits = keyword_hits(combined, WARN_KEYWORDS)
    safe_hits = keyword_hits(combined, SAFE_KEYWORDS)

    score = 100
    reasons: list[str] = []

    if trusted_repo:
        reasons.append(f"trusted:{trusted_repo}")
    else:
        score -= 25
        reasons.append("untrusted-source")

    if host in SHORT_LINK_HOSTS:
        score -= 40
        reasons.append("short-link")

    if "ghproxy" in url.lower() or "mirror" in url.lower():
        score -= 35
        reasons.append("proxy-or-mirror")

    if kind == "script":
        score -= 15
        reasons.append("script-candidate")
    elif kind == "reference_module":
        score -= 10
        reasons.append("reference-only")
    elif kind == "remote_rule":
        reasons.append("remote-rule")
    else:
        score -= 10
        reasons.append("unknown-kind")

    if status == "pending":
        score -= 5
        reasons.append("pending")
    if protected:
        score -= 5
        reasons.append("protected-reference")

    if block_hits:
        score -= 35 + 5 * len(block_hits)
        reasons.append("blocking-keywords:" + ",".join(block_hits[:8]))
    if warn_hits:
        score -= 5 * min(len(warn_hits), 5)
        reasons.append("warning-keywords:" + ",".join(warn_hits[:8]))
    if safe_hits and not block_hits:
        score += min(10, 2 * len(safe_hits))
        reasons.append("safe-keywords:" + ",".join(safe_hits[:8]))

    score = max(0, min(100, score))
    if block_hits or score < 50:
        verdict = "block"
    elif score < 80 or kind in {"script", "reference_module"}:
        verdict = "manual-review"
    else:
        verdict = "candidate-ok"

    if enabled and activate and verdict == "block":
        verdict = "enabled-risk"

    return {
        "name": name,
        "kind": kind,
        "enabled": "是" if enabled else "否",
        "activate": "是" if activate else "否",
        "score": score,
        "verdict": verdict,
        "reasons": reasons,
        "url": url,
    }


def main() -> None:
    data = load_json(CANDIDATES)
    trusted = [str(item) for item in data.get("trusted_repositories", [])]
    candidates = data.get("candidates", []) if isinstance(data.get("candidates", []), list) else []
    rows = [score_candidate(item, trusted) for item in candidates if isinstance(item, dict)]
    verdict_counts: dict[str, int] = {}
    for row in rows:
        verdict_counts[str(row["verdict"])] = verdict_counts.get(str(row["verdict"]), 0) + 1

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    lines = [
        "# 候选源安全评分报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告只评分候选源，不自动启用、不自动禁用、不自动晋级 Stable。",
        "",
        "## 总体统计",
        "",
        f"- 候选总数：{len(rows)}",
        f"- candidate-ok：{verdict_counts.get('candidate-ok', 0)}",
        f"- manual-review：{verdict_counts.get('manual-review', 0)}",
        f"- block：{verdict_counts.get('block', 0)}",
        f"- enabled-risk：{verdict_counts.get('enabled-risk', 0)}",
        "",
        "## 判定规则",
        "",
        "- `candidate-ok`：可信来源、低风险规则类候选，可以继续进入候选/测试流程。",
        "- `manual-review`：需要人工复核，不能直接进入 Stable。",
        "- `block`：包含高风险关键词、未知来源或风险过高，不能启用。",
        "- `enabled-risk`：已启用但评分为阻断风险，必须人工处理。",
        "",
        "## 候选评分明细",
        "",
        "| 候选 | 类型 | 启用 | 激活 | 分数 | 结论 | 原因 | URL |",
        "|---|---|---|---|---:|---|---|---|",
    ]
    for row in rows:
        reason_text = "; ".join(str(item) for item in row["reasons"])
        lines.append(
            f"| {row['name']} | {row['kind']} | {row['enabled']} | {row['activate']} | {row['score']} | {row['verdict']} | {reason_text} | `{row['url']}` |"
        )
    lines += [
        "",
        "## 处理原则",
        "",
        "1. 规则源可以自动进入候选报告，但不能无审核直接进入 Stable。",
        "2. 脚本候选默认 pending，必须人工复核和真机测试。",
        "3. 出现 Cookie、Token、登录、支付、验证码、会员权益、混淆、代理镜像等关键词时，不得自动启用。",
        "4. Stable Plus 或 pending 通过真实测试后，才允许单项晋级 Stable。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Candidate security score report written to {REPORT}")


if __name__ == "__main__":
    main()
