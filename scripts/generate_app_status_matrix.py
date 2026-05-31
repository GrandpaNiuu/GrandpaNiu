#!/usr/bin/env python3
"""Generate a conservative App status matrix for manual quality tracking."""

from __future__ import annotations

import datetime as dt
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

STABLE_FIRST_ROUND_APPS = {
    "Spotify",
    "YouTube",
    "知乎",
    "Bilibili",
    "淘宝",
    "京东",
    "拼多多",
    "美团",
    "大众点评",
    "饿了么",
    "微信",
    "支付宝",
    "银行 / 验证码",
    "图片 CDN",
    "小程序资源",
    "闲鱼",
    "喜马拉雅",
    "滴滴",
    "斗鱼",
}

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


def stable_round_confirmation() -> tuple[bool, str]:
    log = read(MANUAL_LOG)
    has_confirmation = (
        "Stable 第一轮真实测试" in log
        and "用户确认" in log
        and "通过" in log
        and "国内 App 图片 / 联网 / 微信发图" in log
        and "已恢复正常" in log
    )
    matches = re.findall(r"\d{4}-\d{2}-\d{2}", log)
    return has_confirmation, matches[-1] if matches else "未记录"


def manual_status(app: str) -> tuple[str, str, str]:
    log = read(MANUAL_LOG)
    matched = [line for line in log.splitlines() if app.lower() in line.lower()]
    for latest in reversed(matched):
        date_match = re.search(r"\d{4}-\d{2}-\d{2}", latest)
        test_date = date_match.group(0) if date_match else "未记录"
        if "失败" in latest:
            return "失败", test_date, "manual_test_log.md / 用户确认"
        if "部分通过" in latest:
            return "部分通过", test_date, "manual_test_log.md / 用户确认"
        if "通过" in latest and "未测" not in latest and date_match:
            return "通过", test_date, "manual_test_log.md / 用户确认"

    round_ok, round_date = stable_round_confirmation()
    if round_ok and app in STABLE_FIRST_ROUND_APPS:
        return "通过", round_date, "manual_test_log.md / 用户确认"
    return "未测", "未记录", "无真实记录"


def stable_allowed(app: str, risk: str, status: str, profiles: list[str]) -> str:
    if status == "通过" and app in STABLE_FIRST_ROUND_APPS:
        if risk == "高":
            return "Stable 第一轮通过；后续敏感链路变更仍需复测"
        return "Stable 第一轮通过"
    if "stable-plus" in profiles and "stable" not in profiles:
        return "仅 Stable Plus，需单项 PR 审查"
    if risk == "高":
        return "未测或高风险，需人工复核"
    if status == "通过":
        return "可作为已验证覆盖保留"
    return "未测，不允许晋级"


def rollback_path(files: list[str]) -> str:
    if not files:
        return "从候选或对应源文件移除后重建"
    roots = sorted({file.split("/", 1)[0] for file in files})
    return "回滚 " + "、".join(roots) + " 中对应源头后重建"


def main() -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    rows: list[str] = []
    for app, category, keywords, base_risk in APPS:
        methods, files = source_hits(keywords)
        profiles = profile_hits(files)
        status, latest_date, source = manual_status(app)
        risk = "高" if app in {"微信", "支付宝", "银行 / 验证码", "图片 CDN", "小程序资源"} else base_risk
        note = (
            "用户确认，不是助手亲测；大改后仍需复测"
            if status == "通过"
            else "覆盖存在不等于测试通过；未测必须保持未测"
        )
        rows.append(
            "| {app} | {category} | {methods} | {profiles} | {status} | {risk} | {latest} | {source} | {allowed} | {rollback} | {note} |".format(
                app=app,
                category=category,
                methods=", ".join(methods) if methods else "未发现",
                profiles=", ".join(profiles) if profiles else "未确认",
                status=status,
                risk=risk,
                latest=latest_date,
                source=source,
                allowed=stable_allowed(app, risk, status, profiles),
                rollback=rollback_path(files),
                note=note,
            )
        )

    lines = [
        "# App 状态矩阵",
        "",
        f"生成时间：{now}",
        "",
        "本矩阵是质量总览，不把静态覆盖写成已经验证。真实测试来源只允许来自 `reports/manual_test_log.md`；没有记录时一律标记为“未测”。",
        "",
        "| App 名称 | 所属类别 | 覆盖来源 | 所属版本 | 测试状态 | 风险等级 | 最近测试日期 | 测试来源 | 是否允许进入 Stable | 回滚路径 | 备注 |",
        "|---|---|---|---|---|---|---|---|---|---|---|",
        *rows,
        "",
        "## 晋级边界",
        "",
        "- 未测试不得写通过。",
        "- 本次 Stable 第一轮通过来源为 `manual_test_log.md / 用户确认`，不是助手亲测。",
        "- 微信、支付宝、银行、验证码、支付、图片 CDN、小程序默认高风险；即使本轮通过，后续涉及这些链路的规则变更仍需重新测试。",
        "- Stable Plus 中的内容只有真实测试通过后，才能进入单项晋级流程。",
        "- 不允许把 Stable Plus 整体合并进 Stable，只能单项 App 晋级。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"App status matrix written to {REPORT}")


if __name__ == "__main__":
    main()
