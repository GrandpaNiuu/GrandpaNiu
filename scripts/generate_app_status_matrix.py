#!/usr/bin/env python3
"""Generate a conservative App status matrix for manual quality tracking."""

from __future__ import annotations

import datetime as dt
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports" / "app_status_matrix.md"
MANUAL_LOG = ROOT / "reports" / "manual_test_log.md"

APPS = [
    ("Spotify", "音乐", ["spotify", "spclient"], "中"),
    ("YouTube", "视频", ["youtube", "youtubei", "googlevideo"], "中"),
    ("知乎", "内容社区", ["zhihu", "zhihu-enhance"], "中"),
    ("Bilibili", "视频", ["bilibili", "biliapi", "hdslb"], "中"),
    ("微博", "社交", ["weibo"], "中"),
    ("百度贴吧", "社交", ["tieba", "tiebac"], "中"),
    ("小红书", "社交电商", ["xiaohongshu", "xhscdn", "edith"], "中"),
    ("酷安", "工具社区", ["coolapk"], "中"),
    ("淘宝", "电商", ["taobao", "tmall", "alicdn"], "高"),
    ("闲鱼", "电商", ["goofish", "idle"], "中"),
    ("京东", "电商", ["jd.com", "jingdong", "360buyimg", "jdimg"], "高"),
    ("拼多多", "电商", ["pinduoduo", "yangkeduo", "pddpic"], "高"),
    ("美团", "本地生活", ["meituan"], "高"),
    ("大众点评", "本地生活", ["dianping", "dpfile"], "高"),
    ("饿了么", "本地生活", ["ele.me", "eleme"], "高"),
    ("滴滴", "出行", ["diditaxi", "xiaojukeji", "didi"], "高"),
    ("12306", "出行", ["12306"], "高"),
    ("高德地图", "地图", ["amap"], "高"),
    ("百度地图", "地图", ["map.baidu", "baidu.com"], "高"),
    ("网易云音乐", "音乐", ["music.163", "netease"], "中"),
    ("喜马拉雅", "音频", ["ximalaya", "xmly"], "中"),
    ("小宇宙", "音频", ["xiaoyuzhou"], "中"),
    ("斗鱼", "直播", ["douyu"], "中"),
    ("Reddit", "社交", ["reddit"], "低"),
    ("微信", "社交 / 支付 / 小程序 / 图片", ["weixin", "wechat", "wxs.qq.com", "servicewechat", "wechatpay", "qpic", "gtimg", "qlogo"], "高"),
    ("支付宝", "支付", ["alipay"], "高"),
    ("银行 / 验证码", "安全敏感", ["bank", "captcha", "verify", "passport"], "高"),
    ("图片 CDN", "资源加载", ["qpic", "gtimg", "alicdn", "pddpic", "360buyimg", "jdimg", "biliimg", "hdslb", "dpfile"], "高"),
    ("小程序资源", "微信生态", ["servicewechat", "wxapp.tc.qq.com"], "高"),
]

SOURCE_FILES = {
    "Rule": [ROOT / "Rules"],
    "Script": [ROOT / "Scripts"],
    "Rewrite": [ROOT / "Rewrite" / "Sources"],
    "MITM": [
        ROOT / "Rewrite" / "Sources" / "MITM-core.conf",
        ROOT / "Rewrite" / "Sources" / "MITM-app-clean.conf",
        ROOT / "Rewrite" / "Sources" / "MITM-stable-plus.conf",
        ROOT / "Rewrite" / "Sources" / "MITM-extended.conf",
    ],
    "Remote": [ROOT / "Rewrite" / "Remotes" / "sources.json"],
}

PROFILE_FILES = {
    "stable": ROOT / "Rewrite" / "Profiles" / "stable.conf",
    "stable-plus": ROOT / "Rewrite" / "Profiles" / "stable-plus.conf",
    "lite": ROOT / "Rewrite" / "Profiles" / "lite.conf",
    "full": ROOT / "Rewrite" / "Profiles" / "full.conf",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def collect_text(path: Path) -> str:
    if not path.exists():
        return ""
    if path.is_file():
        return read(path)
    return "\n".join(read(item) for item in path.rglob("*") if item.is_file())


def source_hits(keywords: list[str]) -> tuple[list[str], list[str]]:
    methods: list[str] = []
    files: list[str] = []
    lowered_keywords = [item.lower() for item in keywords]
    for method, paths in SOURCE_FILES.items():
        matched = False
        for path in paths:
            text = collect_text(path).lower()
            if any(keyword in text for keyword in lowered_keywords):
                matched = True
                if path.is_dir():
                    for item in path.rglob("*"):
                        if item.is_file() and any(keyword in read(item).lower() for keyword in lowered_keywords):
                            files.append(str(item.relative_to(ROOT)).replace("\\", "/"))
                else:
                    files.append(str(path.relative_to(ROOT)).replace("\\", "/"))
        if matched:
            methods.append(method)
    return sorted(set(methods)), sorted(set(files))


def profile_hits(files: list[str]) -> list[str]:
    result: list[str] = []
    for profile, path in PROFILE_FILES.items():
        text = read(path)
        if any(file_name in text for file_name in files):
            result.append(profile)
    return result


def manual_status(app: str) -> tuple[str, str]:
    log = read(MANUAL_LOG)
    matched = [line for line in log.splitlines() if app.lower() in line.lower()]
    if not matched:
        return "未测", "未记录"
    latest = matched[-1]
    date_match = re.search(r"\d{4}-\d{2}-\d{2}", latest)
    test_date = date_match.group(0) if date_match else "未记录"
    if "失败" in latest:
        return "失败", test_date
    if "部分通过" in latest:
        return "部分通过", test_date
    if "通过" in latest and "未测试" not in latest and "未测" not in latest:
        return "通过", test_date
    return "未测", test_date


def stable_allowed(app: str, risk: str, status: str, profiles: list[str]) -> str:
    if app in {"微信", "支付宝", "银行 / 验证码", "图片 CDN", "小程序资源"}:
        return "否，需人工复核"
    if "stable-plus" in profiles and "stable" not in profiles:
        return "否，Stable Plus 测试中"
    if risk == "高" and status != "通过":
        return "否，需真实测试"
    if status == "通过":
        return "可晋级候选"
    return "未测，不允许晋级"


def rollback_path(files: list[str]) -> str:
    if not files:
        return "从候选或对应源文件移除"
    roots = sorted({file.split("/", 1)[0] for file in files})
    return "回滚 " + "、".join(roots) + " 中对应源头后重建"


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    rows: list[str] = []
    for app, category, keywords, base_risk in APPS:
        methods, files = source_hits(keywords)
        profiles = profile_hits(files)
        status, latest_date = manual_status(app)
        risk = "高" if app in {"微信", "支付宝", "银行 / 验证码", "图片 CDN", "小程序资源"} else base_risk
        rows.append(
            "| {app} | {category} | {methods} | {profiles} | {status} | {risk} | {latest} | {allowed} | {rollback} | {note} |".format(
                app=app,
                category=category,
                methods=", ".join(methods) if methods else "未发现",
                profiles=", ".join(profiles) if profiles else "未确认",
                status=status,
                risk=risk,
                latest=latest_date,
                allowed=stable_allowed(app, risk, status, profiles),
                rollback=rollback_path(files),
                note="覆盖存在不等于测试通过；未测必须保持未测",
            )
        )

    lines = [
        "# App 状态矩阵",
        "",
        f"生成时间：{now}",
        "",
        "本矩阵是质量总览，不把静态覆盖写成已验证。真实测试来源只允许来自 `reports/manual_test_log.md`，没有记录时一律标记为“未测”。",
        "",
        "| App 名称 | 所属类别 | 覆盖来源 | 所属版本 | 测试状态 | 风险等级 | 最近测试日期 | 是否允许进入 Stable | 回滚路径 | 备注 |",
        "|---|---|---|---|---|---|---|---|---|---|",
        *rows,
        "",
        "## 晋级边界",
        "",
        "- 未测试不得写通过。",
        "- 微信、支付宝、银行、验证码、支付、图片 CDN、小程序默认高风险。",
        "- Stable Plus 中的内容只有真实测试通过后，才能写“可晋级候选”。",
        "- 不允许把 Stable Plus 整体合并进 Stable，只能单项 App 晋级。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"App status matrix written to {REPORT}")


if __name__ == "__main__":
    main()
