#!/usr/bin/env python3
"""Prepare a Stable Plus promotion PR report without auto-merging anything."""

from __future__ import annotations

import argparse
import datetime as dt
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "promotion_pr_report.md"
MANUAL_LOG = ROOT / "reports" / "manual_test_log.md"
PLUS_PROFILE = ROOT / "Rewrite" / "Profiles" / "stable-plus.conf"
STABLE_PROFILE = ROOT / "Rewrite" / "Profiles" / "stable.conf"
PLUS_MITM = ROOT / "Rewrite" / "Sources" / "MITM-stable-plus.conf"
WECHAT_RULE = ROOT / "Rules" / "wechat-ad.list"

SENSITIVE = ["登录", "支付", "验证码", "银行", "图片", "小程序"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def manual_result(app: str) -> tuple[str, str]:
    log = read(MANUAL_LOG)
    rows = [line for line in log.splitlines() if app.lower() in line.lower()]
    if not rows:
        return "manual-review", "没有 `manual_test_log.md` 真实通过记录"
    latest = rows[-1]
    if "通过" in latest and "未测" not in latest and "未测试" not in latest and "失败" not in latest:
        return "stable-ready", latest
    return "manual-review", latest


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
    for label, path in [("stable-plus", PLUS_PROFILE), ("stable", STABLE_PROFILE)]:
        if app.lower() in read(path).lower():
            hits.append(label)
    return hits


def risk_summary(app: str, hosts: list[str]) -> str:
    haystack = " ".join([app, *hosts]).lower()
    touched = [item for item in SENSITIVE if item in app or item.lower() in haystack]
    return "涉及：" + "、".join(touched) if touched else "未发现敏感关键词，仍需人工确认登录 / 支付 / 验证码 / 图片 / 小程序"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--app", default="未指定", help="single App name to evaluate for promotion")
    args = parser.parse_args()

    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    app = args.app
    verdict, evidence = manual_result(app)
    hosts = app_hosts(app) if app != "未指定" else []
    profile_hit = profile_mentions(app) if app != "未指定" else []
    wechat_boundary_ok = "wechat_ad_test = Rules/wechat-ad.list" in read(PLUS_PROFILE) and "wechat_ad_test" not in read(STABLE_PROFILE)

    lines = [
        "# Stable Plus 晋级 PR 报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告只准备单项 App 晋级审查材料，不会自动合并 PR，不会把 Stable Plus 整体合并进 Stable。",
        "",
        "## 当前结论",
        "",
        f"- App 名称：{app}",
        f"- 晋级判定：{verdict}",
        f"- 测试记录链接：`reports/manual_test_log.md`",
        f"- 测试证据：{evidence}",
        f"- 微信广告规则仍仅 Stable Plus：{'是' if wechat_boundary_ok else '否，需要修复'}",
        "",
        "## PR 必填信息",
        "",
        f"- App 名称：{app}",
        "- 从哪个 profile 晋级：stable-plus -> stable",
        f"- 新增 / 移动的 hostname：{', '.join(hosts) if hosts else '未自动识别，需人工填写'}",
        f"- 新增 / 移动的 rule：{str(WECHAT_RULE.relative_to(ROOT)) if app == '微信' else '需人工确认'}",
        "- 新增 / 移动的 script：无自动移动，脚本必须单独审查",
        "- 新增 / 移动的 Rewrite：需人工确认具体源文件",
        f"- 影响范围：{risk_summary(app, hosts)}",
        f"- 是否涉及登录 / 支付 / 验证码 / 银行 / 图片 / 小程序：{risk_summary(app, hosts)}",
        "- 回滚步骤：回滚对应 `Rules/`、`Scripts/`、`Rewrite/Sources/`、`Rewrite/Profiles/` 源头文件后重新运行构建与校验",
        "",
        "## 门禁",
        "",
        "- 没有 `manual_test_log.md` 真实通过记录，不允许生成 `stable-ready`。",
        "- 没有真实测试记录，只能写 `manual-review`。",
        "- 不允许 Stable Plus 整体合并进 Stable。",
        "- 只能单项 App 晋级。",
        "- PR 默认不自动 merge。",
        "",
        "## 自动识别信息",
        "",
        f"- Profile 命中：{', '.join(profile_hit) if profile_hit else '未识别'}",
        f"- Stable Plus hostname 命中数：{len(hosts)}",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Promotion PR report written to {REPORT}")


if __name__ == "__main__":
    main()
