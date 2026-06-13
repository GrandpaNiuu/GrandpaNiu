#!/usr/bin/env python3
"""Prepare a promotion PR report from automated evidence."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "promotion_pr_report.md"
EVIDENCE = ROOT / "reports" / "automated_quality_evidence.md"
FUSION_PROFILE = ROOT / "Rewrite" / "Profiles" / "fusion.conf"
PLUS_MITM = ROOT / "Rewrite" / "Sources" / "MITM-stable-plus.conf"
WECHAT_RULE = ROOT / "Rules" / "wechat-ad.list"

SENSITIVE = ["登录", "支付", "验证码", "银行", "图片", "小程序", "token", "cookie", "passport", "pay"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def automated_gate_summary() -> str:
    text = read(EVIDENCE)
    if "UTF-8 BOM 命中：0" in text and "Root / Release 一致：是" in text:
        return "自动门禁证据存在且核心结论通过"
    if text:
        return "自动门禁证据存在，但需要查看报告中的未通过项"
    return "缺少自动门禁证据，请先运行 scripts/quality_gate.py"


def app_hosts(app: str) -> list[str]:
    text = read(PLUS_MITM)
    lowered_app = app.lower()
    hosts: list[str] = []
    for raw in re.split(r"[,\s]+", text.replace("hostname", "").replace("=", "").replace("%APPEND%", "")):
        host = raw.strip()
        if host and lowered_app in host.lower():
            hosts.append(host)
    return sorted(set(hosts))


def profile_mentions(app: str) -> list[str]:
    hits: list[str] = []
    if app.lower() in read(FUSION_PROFILE).lower():
        hits.append("fusion")
    return hits


def risk_summary(app: str, hosts: list[str]) -> str:
    haystack = " ".join([app, *hosts]).lower()
    touched = [item for item in SENSITIVE if item in app or item.lower() in haystack]
    return "涉及：" + "、".join(touched) if touched else "未自动发现敏感关键词，仍需保留来源、风险和回滚说明"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app", default="未指定", help="single App name to evaluate for promotion")
    args = parser.parse_args()

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    app = args.app
    hosts = app_hosts(app) if app != "未指定" else []
    profile_hit = profile_mentions(app) if app != "未指定" else []
    wechat_boundary_ok = "wechat_ad_test = Rules/wechat-ad.list" in read(FUSION_PROFILE) or WECHAT_RULE.exists()

    lines = [
        "# 自动化晋级 PR 准备报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告只准备单项 App / 单组规则的 PR 审查材料，不自动合并，也不依赖人工设备记录。",
        "",
        "## 当前结论",
        "",
        f"- App 名称：{app}",
        f"- 自动门禁：{automated_gate_summary()}",
        "- 证据链接：`reports/automated_quality_evidence.md`",
        f"- 微信广告规则源存在：{'是' if wechat_boundary_ok else '否，需要修复'}",
        "- 整体合并限制：不允许批量提升风险层，只能单项、可回滚、可审计。",
        "",
        "## PR 必填信息",
        "",
        f"- App 名称：{app}",
        "- 目标入口：fusion",
        f"- 新增 / 移动的 hostname：{', '.join(hosts) if hosts else '未自动识别，需由 PR 明确列出'}",
        f"- 新增 / 移动的 rule：{WECHAT_RULE.relative_to(ROOT).as_posix() if app == '微信' and WECHAT_RULE.exists() else '需由 PR 明确列出'}",
        "- 新增 / 移动的 script：脚本必须单独审查来源、风险和回滚路径",
        "- 新增 / 移动的 Rewrite：需列出具体源文件",
        f"- 影响范围：{risk_summary(app, hosts)}",
        f"- 是否涉及敏感链路：{risk_summary(app, hosts)}",
        "- 回滚步骤：回滚对应 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Profiles/` 源头文件后重新运行质量门禁",
        "",
        "## 门禁",
        "",
        "- 必须先运行 `python scripts/quality_gate.py`。",
        "- 必须保留来源、风险、影响范围和回滚路径。",
        "- 不允许把候选层或风险层整体合并进公开入口。",
        "- PR 默认不自动 merge。",
        "",
        "## 自动识别信息",
        "",
        f"- Profile 命中：{', '.join(profile_hit) if profile_hit else '未识别'}",
        f"- 风险层 hostname 命中数：{len(hosts)}",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Promotion PR report written to {REPORT}")


if __name__ == "__main__":
    main()
