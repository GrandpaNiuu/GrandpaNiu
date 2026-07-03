#!/usr/bin/env python3
"""Generate upstream provenance, trust-tier, and license visibility report."""

from __future__ import annotations

import datetime as dt
import json
import re
import urllib.parse
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
APP_MODULES = ROOT / "Rewrite" / "Remotes" / "app-modules.json"
SOURCES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
REPORT = ROOT / "reports" / "upstream_provenance_report.md"

UNSAFE_TOKENS = (
    "vip",
    "premium",
    "unlock",
    "crack",
    "receipt",
    "entitlement",
    "purchase",
    "payment",
    "pay-bypass",
    "login-bypass",
    "cookie",
    "token",
)


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def escape(value: object) -> str:
    return str(value if value is not None else "").replace("|", "\\|").replace("\n", "<br>")


def github_project_from_url(url: str) -> str:
    parsed = urllib.parse.urlparse(url)
    parts = [part for part in parsed.path.split("/") if part]
    host = parsed.netloc.lower()
    if host in {"raw.githubusercontent.com", "github.com"} and len(parts) >= 2:
        return f"{parts[0]}/{parts[1]}"
    if "kelee.one" in host:
        return "Kelee PluginHub"
    return parsed.netloc or "unknown"


def has_unsafe_token(*values: object) -> bool:
    haystack = " ".join(str(value).lower() for value in values)
    return any(token in haystack for token in UNSAFE_TOKENS)


def module_trust_tier(record: dict[str, Any]) -> str:
    enabled = bool(record.get("enabled"))
    direct_commit = bool(record.get("direct_commit"))
    risk = str(record.get("risk", "")).lower()
    last_mode = str(record.get("last_sync_mode", "")).lower()
    backup = bool(record.get("backup"))
    if "blocked" in last_mode or has_unsafe_token(record.get("name"), record.get("source_url"), record.get("upstream_project")):
        return "blocked"
    if not enabled or not direct_commit:
        return "reference_only"
    if risk in {"high", "critical"} or backup:
        return "observe"
    if risk in {"low", "safe"}:
        return "trusted"
    return "observe"


def remote_source_trust_tier(item: dict[str, Any], reference: bool) -> str:
    if reference or not item.get("enabled"):
        return "reference_only"
    if has_unsafe_token(item.get("name"), item.get("url"), item.get("purpose")):
        return "blocked"
    if item.get("protected"):
        return "trusted"
    return "observe"


def license_value(item: dict[str, Any]) -> str:
    value = item.get("license") or item.get("licence")
    return str(value).strip() if value else "未记录"


def table(rows: list[dict[str, object]], columns: list[str]) -> list[str]:
    if not rows:
        return ["_None._"]
    out = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        out.append("| " + " | ".join(escape(row.get(column, "")) for column in columns) + " |")
    return out


def source_hint(path: str) -> str:
    target = ROOT / path
    if target.exists():
        for line in target.read_text(encoding="utf-8", errors="replace").splitlines():
            stripped = line.strip()
            if stripped.startswith("# source-url:"):
                return stripped.split(":", 1)[1].strip()
            if stripped.startswith("# converted-from:"):
                return stripped.split(":", 1)[1].strip()
    return ""


def app_rows(records: list[dict[str, Any]]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for record in records:
        source_url = str(record.get("source_url") or source_hint(str(record.get("target", ""))))
        project = str(record.get("upstream_project") or github_project_from_url(source_url))
        rows.append(
            {
                "id": record.get("id", ""),
                "name": record.get("name", ""),
                "tier": module_trust_tier(record),
                "risk": record.get("risk", ""),
                "enabled": record.get("enabled", False),
                "direct_commit": record.get("direct_commit", False),
                "backup": record.get("backup", False),
                "upstream_project": project,
                "license": license_value(record),
                "last_sync_mode": record.get("last_sync_mode", ""),
                "target": record.get("target", ""),
                "source_url": source_url,
            }
        )
    return rows


def remote_rows(data: dict[str, Any]) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for item in data.get("rule_sets", []):
        url = str(item.get("url", ""))
        rows.append(
            {
                "kind": "rule_set",
                "name": item.get("name", ""),
                "tier": remote_source_trust_tier(item, reference=False),
                "enabled": item.get("enabled", False),
                "protected": item.get("protected", False),
                "type": item.get("type", ""),
                "policy": item.get("policy", ""),
                "upstream_project": github_project_from_url(url),
                "license": license_value(item),
                "purpose": item.get("purpose", ""),
                "url": url,
            }
        )
    for item in data.get("reference_modules", []):
        url = str(item.get("url", ""))
        rows.append(
            {
                "kind": "reference_module",
                "name": item.get("name", ""),
                "tier": remote_source_trust_tier(item, reference=True),
                "enabled": item.get("enabled", False),
                "protected": item.get("protected", False),
                "type": "module",
                "policy": "reference",
                "upstream_project": github_project_from_url(url),
                "license": license_value(item),
                "purpose": item.get("purpose", ""),
                "url": url,
            }
        )
    return rows


def compact_url(url: str) -> str:
    return re.sub(r"https://raw\.githubusercontent\.com/([^/]+/[^/]+)/.*", r"\1 raw", url)


def main() -> int:
    app_data = read_json(APP_MODULES)
    remote_data = read_json(SOURCES_JSON)
    apps = app_rows(app_data.get("modules", []))
    remotes = remote_rows(remote_data)
    app_tiers = Counter(str(row["tier"]) for row in apps)
    remote_tiers = Counter(str(row["tier"]) for row in remotes)
    missing_license = sum(1 for row in apps + remotes if row["license"] == "未记录")
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    project_counts = Counter(str(row["upstream_project"]) for row in apps)
    project_rows = [
        {
            "upstream_project": project,
            "module_count": count,
            "sample": ", ".join(
                str(row["id"])
                for row in apps
                if row["upstream_project"] == project
            )[:180],
        }
        for project, count in project_counts.most_common()
    ]

    app_table_rows = [
        {
            **row,
            "source_url": compact_url(str(row["source_url"])),
        }
        for row in apps
    ]
    remote_table_rows = [
        {
            **row,
            "url": compact_url(str(row["url"])),
        }
        for row in remotes
    ]

    lines = [
        "# 上游来源、许可证与可信分层报告",
        "",
        f"- 生成时间：{now}",
        f"- App 同步记录：{len(apps)}",
        f"- 远程规则 / 参考模块记录：{len(remotes)}",
        f"- 未记录 license 的来源：{missing_license}",
        "",
        "## 分层定义",
        "",
        "- `trusted`：已启用、直接同步、风险较低，并通过当前风险门禁。",
        "- `observe`：可以同步，但需要备份或人工观察，常见于核心 App、高风险 App、未知风险来源。",
        "- `reference_only`：仅作参考或已禁用，不直接写入正式模块。",
        "- `blocked`：同步模式或来源文本命中高危绕过/解锁/凭证类信号，不应直接进入正式模块。",
        "",
        "## 总览",
        "",
        "| 范围 | trusted | observe | reference_only | blocked |",
        "|---|---:|---:|---:|---:|",
        f"| App modules | {app_tiers['trusted']} | {app_tiers['observe']} | {app_tiers['reference_only']} | {app_tiers['blocked']} |",
        f"| Remote sources | {remote_tiers['trusted']} | {remote_tiers['observe']} | {remote_tiers['reference_only']} | {remote_tiers['blocked']} |",
        "",
        "## 上游项目分布",
        "",
        *table(project_rows, ["upstream_project", "module_count", "sample"]),
        "",
        "## App 模块来源台账",
        "",
        *table(
            app_table_rows,
            [
                "id",
                "name",
                "tier",
                "risk",
                "enabled",
                "direct_commit",
                "backup",
                "upstream_project",
                "license",
                "last_sync_mode",
                "target",
                "source_url",
            ],
        ),
        "",
        "## 远程规则与参考模块台账",
        "",
        *table(
            remote_table_rows,
            [
                "kind",
                "name",
                "tier",
                "enabled",
                "protected",
                "type",
                "policy",
                "upstream_project",
                "license",
                "purpose",
                "url",
            ],
        ),
        "",
        "## 维护要求",
        "",
        "- 新增直接同步 App 前，必须能在本报告中看到 `source_url`、`risk`、`backup`、`direct_commit` 和上游项目。",
        "- `license = 未记录` 不会阻断构建，但公开使用前应优先补来源许可或在文档中说明未知。",
        "- `observe` 不是错误；它表示需要保留备份、风险说明和回滚路径。",
        "- `blocked` 记录不得绕过风险门禁加入正式模块。",
        "",
    ]
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines), encoding="utf-8", newline="\n")
    print(f"Upstream provenance report written to {rel(REPORT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
