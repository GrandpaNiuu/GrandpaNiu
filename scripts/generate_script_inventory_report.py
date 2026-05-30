#!/usr/bin/env python3
"""Generate script inventory and consolidation analysis.

This script is analysis-only. It does not delete, merge, rewrite, or disable any
script. The goal is to identify what can be safely reviewed for consolidation
without reducing module functionality.
"""

from __future__ import annotations

import datetime as dt
import re
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / "Scripts"
REPORT = ROOT / "reports" / "script_inventory_report.md"
SCRIPT_LINE_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=\s*(.+)$")
KEY_VALUE_RE = re.compile(r"([a-zA-Z0-9_-]+)=([^,]+)")

CORE_NAME_TOKENS = ("spotify", "youtube", "zhihu")
KEEP_INDEPENDENT_TOKENS = (
    "spotify", "youtube", "zhihu", "membership", "payment", "login", "paid", "paywall"
)
RULE_CANDIDATE_TOKENS = (
    "splash", "ad", "ads", "advert", "banner", "pop", "popup", "track", "stat", "analytics", "metrics"
)
COMMON_CLEANER_SOURCES = (
    "zirawell/R-Store", "app2smile/rules", "fmz200/wool_scripts", "wool_scripts"
)
SOURCE_LABELS = {
    "app2smile/rules": "app2smile",
    "zirawell/R-Store": "zirawell R-Store",
    "fmz200/wool_scripts": "fmz200 wool_scripts",
    "Maasea/sgmodule": "Maasea",
    "GrandpaNiuu/GrandpaNiu": "local",
}
APP_HINTS = {
    "spotify": "Spotify",
    "youtube": "YouTube",
    "zhihu": "知乎",
    "tieba": "贴吧",
    "qq-news": "QQ 新闻",
    "qqnews": "QQ 新闻",
    "vgtime": "VGTime",
    "weibo": "微博",
    "kkmh": "快看漫画",
    "keep": "Keep",
    "soul": "Soul",
    "mgtv": "芒果 TV",
    "tflj": "铁路/出行类",
    "cotti": "库迪咖啡",
    "goofish": "闲鱼",
    "xmly": "喜马拉雅",
    "didi": "滴滴",
    "smzdm": "什么值得买",
    "taobao": "淘宝",
    "163news": "网易新闻",
    "163music": "网易云音乐",
    "xiaohongshu": "小红书",
    "coolapk": "酷安",
    "dianping": "大众点评",
    "pdd": "拼多多",
    "kuaishou": "快手",
    "xunlei": "迅雷",
    "amap": "高德地图",
    "qidian": "起点",
    "bilibili": "Bilibili",
    "jd": "京东",
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def parse_attrs(value: str) -> dict[str, str]:
    attrs: dict[str, str] = {}
    for match in KEY_VALUE_RE.finditer(value):
        attrs[match.group(1)] = match.group(2).strip()
    return attrs


def source_label(script_path: str) -> str:
    for token, label in SOURCE_LABELS.items():
        if token.lower() in script_path.lower():
            return label
    if script_path.startswith("http"):
        host = urlparse(script_path).netloc or "remote"
        return host
    if script_path:
        return "local/relative"
    return "unknown"


def infer_app(name: str, value: str, script_path: str) -> str:
    haystack = f"{name} {value} {script_path}".lower()
    hits = [label for token, label in APP_HINTS.items() if token in haystack]
    if hits:
        # Keep stable ordering while removing duplicates.
        seen: set[str] = set()
        unique: list[str] = []
        for item in hits:
            if item not in seen:
                seen.add(item)
                unique.append(item)
        return " / ".join(unique[:3])
    return "未识别 / 通用"


def category_for(name: str, value: str, attrs: dict[str, str]) -> tuple[str, str]:
    script_path = attrs.get("script-path", "")
    haystack = f"{name} {value} {script_path}".lower()
    requires_body = attrs.get("requires-body", "")
    binary = attrs.get("binary-body-mode", "")

    if any(token in haystack for token in CORE_NAME_TOKENS):
        return "必须独立保留", "核心专项脚本，合并风险高"
    if any(token in haystack for token in ("membership", "payment", "login", "paid_content", "paywall")):
        return "必须独立保留", "涉及安全边界或权益保护，不能合并进通用清理"
    if binary == "1":
        return "必须独立保留", "二进制 body / protobuf 类处理，不能简单合并"
    if requires_body == "0":
        return "可改规则候选", "不依赖响应 body，后续可人工评估是否改为 Rule / URL Rewrite"
    if any(token in script_path for token in COMMON_CLEANER_SOURCES):
        return "可合并候选", "普通 App JSON 清理脚本，可评估合并到统一 app-cleaner"
    if any(token in haystack for token in RULE_CANDIDATE_TOKENS) and requires_body != "1":
        return "可改规则候选", "疑似广告/统计/开屏接口，可评估规则化"
    return "需要人工复核", "无法静态判断，需结合脚本内容和真机测试"


def parse_script_entries() -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for path in sorted(SCRIPTS_DIR.glob("*.conf")):
        for line_no, line in enumerate(read(path).splitlines(), 1):
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            match = SCRIPT_LINE_RE.match(stripped)
            if not match:
                continue
            name, value = match.group(1).strip(), match.group(2).strip()
            attrs = parse_attrs(value)
            script_path = attrs.get("script-path", "")
            category, reason = category_for(name, value, attrs)
            entries.append({
                "file": path.relative_to(ROOT).as_posix(),
                "line": str(line_no),
                "name": name,
                "type": attrs.get("type", "unknown"),
                "requires_body": attrs.get("requires-body", "unknown"),
                "binary": attrs.get("binary-body-mode", "0"),
                "pattern": attrs.get("pattern", ""),
                "script_path": script_path,
                "source": source_label(script_path),
                "app": infer_app(name, value, script_path),
                "category": category,
                "reason": reason,
            })
    return entries


def duplicate_names(entries: list[dict[str, str]]) -> list[str]:
    counts = Counter(entry["name"] for entry in entries)
    return sorted(name for name, count in counts.items() if count > 1)


def duplicate_script_paths(entries: list[dict[str, str]]) -> dict[str, list[str]]:
    by_path: dict[str, list[str]] = defaultdict(list)
    for entry in entries:
        path = entry["script_path"]
        if path:
            by_path[path].append(entry["name"])
    return {path: names for path, names in by_path.items() if len(names) > 1}


def rows_for(entries: list[dict[str, str]], limit: int = 250) -> list[str]:
    rows: list[str] = []
    for entry in entries[:limit]:
        pattern_short = entry["pattern"][:90].replace("|", "\\|")
        script_short = entry["script_path"].replace("|", "\\|")
        rows.append(
            f"| `{entry['name']}` | {entry['file']}:{entry['line']} | {entry['app']} | {entry['type']} | {entry['requires_body']} | {entry['source']} | {entry['category']} | {entry['reason']} | `{pattern_short}` | `{script_short}` |"
        )
    return rows


def main() -> None:
    entries = parse_script_entries()
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    by_category = Counter(entry["category"] for entry in entries)
    by_source = Counter(entry["source"] for entry in entries)
    by_file = Counter(entry["file"] for entry in entries)
    dup_names = duplicate_names(entries)
    dup_paths = duplicate_script_paths(entries)
    app_count = len({entry["app"] for entry in entries if entry["app"] != "未识别 / 通用"})

    lines: list[str] = [
        "# 脚本清单与瘦身分析报告",
        "",
        f"生成时间：{now}",
        "",
        "本报告只做静态分析，不删除、不合并、不禁用任何脚本。减少脚本前必须先完成真机测试和回滚准备。",
        "",
        "## 总体统计",
        "",
        f"- 脚本入口总数：{len(entries)}",
        f"- 识别到的 App / 服务方向数量：{app_count}",
        f"- 重复脚本名：{len(dup_names)}",
        f"- 多入口共用同一 script-path：{len(dup_paths)}",
        "",
        "## 分类统计",
        "",
    ]
    for category in ["必须独立保留", "可合并候选", "可改规则候选", "需要人工复核"]:
        lines.append(f"- {category}：{by_category.get(category, 0)}")
    lines += [
        "",
        "## 来源统计",
        "",
    ]
    for source, count in by_source.most_common():
        lines.append(f"- {source}：{count}")
    lines += [
        "",
        "## 文件分布",
        "",
    ]
    for file_name, count in by_file.most_common():
        lines.append(f"- `{file_name}`：{count}")
    lines += [
        "",
        "## 重复脚本名",
        "",
    ]
    lines += [f"- `{name}`" for name in dup_names] if dup_names else ["- 无"]
    lines += [
        "",
        "## 多入口共用同一 script-path",
        "",
    ]
    if dup_paths:
        for path, names in sorted(dup_paths.items()):
            lines.append(f"- `{path}`：{', '.join(f'`{name}`' for name in names)}")
    else:
        lines.append("- 无")
    lines += [
        "",
        "## 可合并候选摘要",
        "",
    ]
    merge_candidates = [entry for entry in entries if entry["category"] == "可合并候选"]
    for source, count in Counter(entry["source"] for entry in merge_candidates).most_common():
        lines.append(f"- {source}：{count} 个，可考虑进入统一 `app-cleaner.js` 的配置化处理")
    if not merge_candidates:
        lines.append("- 无")
    lines += [
        "",
        "## 可改规则候选摘要",
        "",
    ]
    rule_candidates = [entry for entry in entries if entry["category"] == "可改规则候选"]
    if rule_candidates:
        for entry in rule_candidates:
            lines.append(f"- `{entry['name']}`：{entry['app']}，{entry['reason']}")
    else:
        lines.append("- 无")
    lines += [
        "",
        "## 全量脚本清单",
        "",
        "| 脚本名 | 位置 | App / 服务 | 类型 | requires-body | 来源 | 分类 | 原因 | pattern 摘要 | script-path |",
        "|---|---|---|---|---|---|---|---|---|---|",
        *rows_for(entries),
        "",
        "## 下一步建议",
        "",
        "1. 第一阶段只处理重复 script-path 和明显普通 JSON 清理脚本，不动 Spotify、YouTube、知乎。",
        "2. 先设计统一 `app-cleaner.js` 和配置表，不直接删除旧入口。",
        "3. 通过 `stable-plus` 做灰度验证，确认无异常后再减少入口。",
        "4. 能用 Rule / URL Rewrite 解决的静态广告接口，应从脚本迁移到规则层。",
        "5. 每次减少脚本后都要重新生成四个 Release 版本，并更新测试记录。",
        "",
    ]
    write(REPORT, "\n".join(lines))
    print(f"Script inventory report written to {REPORT}")


if __name__ == "__main__":
    main()
