#!/usr/bin/env python3
"""Discover and sync upstream app-scoped module sources.

This script owns Rewrite/Remotes/app-modules.json and rewrites only
Rewrite/Sources/Apps/*.conf targets. Release artifacts are intentionally left to
Rewrite/Generator/Builder.py so generated files stay source-first.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONFIG = ROOT / "Rewrite" / "Remotes" / "app-modules.json"
DEFAULT_APPS_DIR = ROOT / "Rewrite" / "Sources" / "Apps"
DEFAULT_REPORT = ROOT / "reports" / "upstream_app_module_sync_report.md"
BACKUP_ROOT = ROOT / "backup" / "upstream-app-modules"

ALLOWED_SECTIONS = [
    "General",
    "Rule",
    "URL Rewrite",
    "Header Rewrite",
    "Body Rewrite",
    "Map Local",
    "Script",
    "MITM",
]
DROP_META_KEYS = {"icon", "category", "openurl", "homepage", "author", "loon_version", "tag"}
REQUIRED_RECORD_KEYS = [
    "id",
    "name",
    "source_url",
    "target",
    "enabled",
    "direct_commit",
    "risk",
    "backup",
    "upstream_project",
    "last_sync_mode",
]
CORE_BACKUP_IDS = {"spotify", "youtube", "zhihu", "wechat", "weibo", "bilibili"}
HIGH_RISK_IDS = CORE_BACKUP_IDS | {"terabox"}
TRUSTED_REPOSITORIES = ["QingRex/LoonKissSurge", "app2smile/rules", "Maasea/sgmodule"]

URL_RE = re.compile(r"https?://[^\s,\"'<>]+")
SECTION_RE = re.compile(r"^\s*\[([^\]]+)\]\s*$")
META_RE = re.compile(r"^\s*#!([^=\s]+)\s*=\s*(.*)$")
COMMENT_FIELD_RE = re.compile(r"^\s*#\s*([A-Za-z0-9_-]+)\s*:\s*(.+?)\s*$")
SCRIPT_PATH_RE = re.compile(r"script-path=(https?://[^,\s]+)", re.IGNORECASE)
RULE_SET_RE = re.compile(r"RULE-SET,(https?://[^,\s]+)", re.IGNORECASE)
RAW_MODULE_HINT_RE = re.compile(r"\.(?:sgmodule|module|conf)(?:$|[?#])", re.IGNORECASE)
SUSPICIOUS_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"(vip|premium|member(?:ship)?).{0,12}(unlock|crack|free|true)",
        r"(unlock|crack|bypass|remove).{0,12}(vip|premium|member(?:ship)?)",
        r"(receipt|entitlement|in[_-]?app[_-]?purchase|purchase[_-]?receipt)",
        r"(payment|pay|bank|alipay|wechatpay).{0,12}(bypass|crack|unlock)",
        r"(login|passport|auth).{0,12}(bypass|crack|unlock)",
        r"(account|账号).{0,12}(share|共享)",
        r"(会员|付费|订阅).{0,12}(解锁|破解|绕过|免费)",
        r"(支付|登录|验证码|银行).{0,12}(绕过|破解|解锁)",
    )
]


class SyncError(RuntimeError):
    """Fatal sync configuration error."""


def repo_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8", newline="\n")


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {"trusted_repositories": TRUSTED_REPOSITORIES, "modules": []}
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        raise SyncError(f"invalid json: {rel(path)}: {exc}") from exc
    if not isinstance(data, dict):
        raise SyncError(f"invalid json root: {rel(path)} must be an object")
    data.setdefault("trusted_repositories", TRUSTED_REPOSITORIES)
    data.setdefault("modules", [])
    if not isinstance(data["modules"], list):
        raise SyncError(f"invalid modules list: {rel(path)}")
    return data


def clean_app_name(raw: str, slug: str) -> str:
    name = raw.strip()
    if name.startswith("GrandpaNiu "):
        name = name[len("GrandpaNiu ") :]
    if name.endswith(" Source"):
        name = name[: -len(" Source")]
    if not name:
        name = title_from_slug(slug)
    return name.strip()


def title_from_slug(slug: str) -> str:
    special = {"jd": "JD", "wps": "WPS", "qqmusic": "QQ Music", "qqnews": "QQ News"}
    if slug in special:
        return special[slug]
    return " ".join(part.upper() if part in {"jd", "qq", "wps"} else part.capitalize() for part in slug.split("-"))


def name_from_source(path: Path, slug: str) -> str:
    for line in read_text(path).splitlines():
        match = META_RE.match(line)
        if match and match.group(1).lower() == "name":
            return clean_app_name(match.group(2), slug)
    return title_from_slug(slug)


def github_project_from_url(url: str) -> str:
    match = re.search(r"raw\.githubusercontent\.com/([^/]+/[^/]+)/", url, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"github\.com/([^/]+/[^/]+)", url, re.IGNORECASE)
    if match:
        return match.group(1)
    match = re.search(r"https?://([^/]+)/", url, re.IGNORECASE)
    return match.group(1) if match else ""


def raw_module_url(url: str) -> bool:
    return bool(url and RAW_MODULE_HINT_RE.search(url))


def clue_urls(text: str) -> list[str]:
    urls: list[str] = []
    seen: set[str] = set()
    for line in text.splitlines():
        for pattern in (SCRIPT_PATH_RE, RULE_SET_RE):
            for match in pattern.finditer(line):
                url = match.group(1)
                clean = url.rstrip(").]")
                if clean not in seen:
                    seen.add(clean)
                    urls.append(clean)
    return urls


def extract_source_clues(path: Path) -> dict[str, str]:
    text = read_text(path)
    explicit_url = ""
    converted_from = ""
    upstream_project = ""
    for line in text.splitlines():
        field = COMMENT_FIELD_RE.match(line)
        if not field:
            continue
        key = field.group(1).lower().replace("_", "-")
        value = field.group(2).strip()
        if key in {"source-url", "source", "upstream-url"}:
            urls = URL_RE.findall(value)
            if urls:
                explicit_url = urls[0]
        elif key == "converted-from":
            converted_from = value
            project = value.split()[0].strip()
            if "/" in project:
                upstream_project = project
        elif key in {"upstream-base", "upstream-name"} and not upstream_project:
            upstream_project = value
    if explicit_url and not upstream_project:
        upstream_project = github_project_from_url(explicit_url)
    if not upstream_project:
        for url in clue_urls(text):
            project = github_project_from_url(url)
            if project:
                upstream_project = project
                break
    return {
        "source_url": explicit_url,
        "converted_from": converted_from,
        "upstream_project": upstream_project,
    }


def inferred_risk(slug: str, path: Path, existing: dict[str, Any] | None) -> str:
    if existing and existing.get("risk"):
        return str(existing["risk"])
    if slug in HIGH_RISK_IDS:
        return "high"
    for line in read_text(path).splitlines():
        field = COMMENT_FIELD_RE.match(line)
        if field and field.group(1).lower() == "risk":
            return field.group(2).strip().lower() or "medium"
    return "medium"


def complete_record(slug: str, path: Path, existing: dict[str, Any] | None = None) -> dict[str, Any]:
    existing = dict(existing or {})
    clues = extract_source_clues(path)
    source_url = str(existing.get("source_url") or clues["source_url"] or "").strip()
    source_is_module = raw_module_url(source_url)
    source_name = name_from_source(path, slug)
    existing_name = clean_app_name(str(existing.get("name") or ""), slug) if existing.get("name") else ""
    fallback_name = title_from_slug(slug)
    if not existing_name or (existing_name == fallback_name and source_name != fallback_name):
        name = source_name
    else:
        name = existing_name
    risk = inferred_risk(slug, path, existing)
    backup = bool(existing.get("backup", slug in CORE_BACKUP_IDS or risk == "high"))
    enabled = bool(existing.get("enabled", bool(source_url and source_is_module and existing)))
    direct_commit = bool(existing.get("direct_commit", enabled and bool(source_url)))
    existing_project = str(existing.get("upstream_project") or "").strip()
    if not source_url and existing_project.startswith(("api.", "app.", "manga.", "m.", "www.")):
        existing_project = ""
    upstream_project = existing_project or clues["upstream_project"] or github_project_from_url(source_url)
    mode = str(existing.get("last_sync_mode") or ("configured" if enabled else "discovered-disabled"))
    if source_url and not source_is_module and not existing.get("enabled"):
        mode = "clue-only"
        enabled = False
        direct_commit = False
    record = {
        "id": slug,
        "name": name,
        "source_url": source_url,
        "target": rel(path),
        "enabled": enabled,
        "direct_commit": direct_commit,
        "risk": risk,
        "backup": backup,
        "upstream_project": upstream_project,
        "last_sync_mode": mode,
    }
    for key in REQUIRED_RECORD_KEYS:
        record.setdefault(key, "")
    return record


def discover_modules(config: dict[str, Any], apps_dir: Path) -> list[dict[str, Any]]:
    existing_by_id = {
        str(item.get("id")): item
        for item in config.get("modules", [])
        if isinstance(item, dict) and item.get("id")
    }
    records: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in sorted(apps_dir.glob("*.conf")):
        slug = path.stem
        if slug.startswith("_"):
            continue
        records.append(complete_record(slug, path, existing_by_id.get(slug)))
        seen.add(slug)
    for slug, item in sorted(existing_by_id.items()):
        if slug in seen:
            continue
        target = repo_path(item.get("target") or f"Rewrite/Sources/Apps/{slug}.conf")
        records.append(complete_record(slug, target, item))
    records.sort(key=lambda item: item["id"])
    return records


def fetch_text(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "GrandpaNiu-Upstream-App-Sync/1.0",
            "Accept": "text/plain,*/*;q=0.8",
        },
    )
    with urllib.request.urlopen(request, timeout=35) as response:
        data = response.read()
    return data.decode("utf-8-sig", errors="replace")


def suspicious_reason(text: str) -> str:
    for pattern in SUSPICIOUS_PATTERNS:
        match = pattern.search(text)
        if match:
            return match.group(0).strip()
    return ""


def split_module(text: str) -> tuple[list[str], dict[str, list[str]]]:
    meta: list[str] = []
    sections: dict[str, list[str]] = {name: [] for name in ALLOWED_SECTIONS}
    current: str | None = None
    for raw in text.splitlines():
        line = raw.rstrip()
        match = SECTION_RE.match(line)
        if match:
            name = match.group(1).strip()
            current = name if name in sections else None
            continue
        if current is None:
            meta.append(line)
        else:
            sections[current].append(line)
    return meta, sections


def upstream_name(meta: list[str], fallback: str) -> str:
    for line in meta:
        match = META_RE.match(line)
        if match and match.group(1).lower() == "name":
            return match.group(2).strip() or fallback
    return fallback


def preserved_arguments(meta: list[str]) -> list[str]:
    out: list[str] = []
    seen: set[str] = set()
    for line in meta:
        match = META_RE.match(line)
        if not match:
            continue
        key = match.group(1)
        low = key.lower()
        if low in DROP_META_KEYS:
            continue
        if low in {"arguments", "arguments-desc"}:
            clean = f"#!{key}={match.group(2).strip()}"
            if clean not in seen:
                seen.add(clean)
                out.append(clean)
    return out


def clean_section_lines(lines: list[str]) -> list[str]:
    out: list[str] = []
    seen_active: set[str] = set()
    last_blank = False
    for raw in lines:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            if out and not last_blank:
                out.append("")
            last_blank = True
            continue
        if not stripped.startswith("#"):
            if stripped in seen_active:
                continue
            seen_active.add(stripped)
        out.append(line)
        last_blank = False
    while out and not out[-1].strip():
        out.pop()
    return out


def converted_source(record: dict[str, Any], upstream_text: str) -> tuple[str, str]:
    meta, sections = split_module(upstream_text)
    body_sections = {name: clean_section_lines(lines) for name, lines in sections.items()}
    body_sections = {name: lines for name, lines in body_sections.items() if lines}
    if not body_sections:
        raise ValueError("no supported module sections found")

    app_name = clean_app_name(str(record["name"]), str(record["id"]))
    source_url = str(record["source_url"])
    upstream = upstream_name(meta, app_name)
    lines = [
        f"#!name=GrandpaNiu {app_name} Source",
        "#!desc=Auto-synced app-scoped source fragment",
        "# auto-sync: true",
        f"# source-url: {source_url}",
        f"# upstream-name: {upstream}",
        f"# risk: {record['risk']}",
    ]
    lines.extend(preserved_arguments(meta))
    for section in ALLOWED_SECTIONS:
        section_lines = body_sections.get(section)
        if not section_lines:
            continue
        lines.append("")
        lines.append(f"[{section}]")
        lines.extend(section_lines)
    return "\n".join(lines).rstrip() + "\n", upstream


def backup_target(target: Path, module_id: str, timestamp: str) -> str:
    if not target.exists():
        return ""
    backup = BACKUP_ROOT / module_id / f"{timestamp}.conf"
    backup.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(target, backup)
    return rel(backup)


def sync_records(records: list[dict[str, Any]], config_only: bool) -> tuple[list[dict[str, str]], list[dict[str, str]], list[dict[str, str]], list[dict[str, str]]]:
    updated: list[dict[str, str]] = []
    skipped: list[dict[str, str]] = []
    blocked: list[dict[str, str]] = []
    errors: list[dict[str, str]] = []
    timestamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S")

    for record in records:
        module_id = str(record["id"])
        target = repo_path(record["target"])
        source_url = str(record["source_url"])
        if config_only:
            record["last_sync_mode"] = "config-only"
            skipped.append({"id": module_id, "reason": "config-only"})
            continue
        if not record.get("enabled"):
            skipped.append({"id": module_id, "reason": "disabled"})
            continue
        if not record.get("direct_commit"):
            skipped.append({"id": module_id, "reason": "direct_commit=false"})
            continue
        if not source_url:
            record["last_sync_mode"] = "missing-source"
            skipped.append({"id": module_id, "reason": "missing source_url"})
            continue
        if not raw_module_url(source_url):
            record["last_sync_mode"] = "not-module-url"
            skipped.append({"id": module_id, "reason": "source_url is not a raw module"})
            continue
        try:
            upstream_text = fetch_text(source_url)
        except (urllib.error.URLError, TimeoutError, OSError) as exc:
            record["last_sync_mode"] = "fetch-failed"
            errors.append({"id": module_id, "reason": f"fetch failed: {exc}"})
            continue
        reason = suspicious_reason(upstream_text + "\n" + source_url + "\n" + str(record.get("name", "")))
        if reason:
            record["last_sync_mode"] = "blocked-risk"
            blocked.append({"id": module_id, "reason": reason})
            continue
        try:
            converted, upstream = converted_source(record, upstream_text)
        except ValueError as exc:
            record["last_sync_mode"] = "convert-failed"
            errors.append({"id": module_id, "reason": str(exc)})
            continue
        previous = read_text(target)
        if previous == converted:
            record["last_sync_mode"] = "unchanged"
            skipped.append({"id": module_id, "reason": "unchanged"})
            continue
        backup_path = backup_target(target, module_id, timestamp) if record.get("backup") else ""
        write_text(target, converted)
        record["upstream_project"] = str(record.get("upstream_project") or github_project_from_url(source_url))
        record["last_sync_mode"] = "updated"
        updated.append({"id": module_id, "source": source_url, "backup": backup_path, "upstream": upstream})
    return updated, skipped, blocked, errors


def write_config(path: Path, config: dict[str, Any], records: list[dict[str, Any]]) -> None:
    config["trusted_repositories"] = config.get("trusted_repositories") or TRUSTED_REPOSITORIES
    config["modules"] = [{key: record.get(key, "") for key in REQUIRED_RECORD_KEYS} for record in records]
    write_text(path, json.dumps(config, ensure_ascii=False, indent=2))


def table(rows: list[dict[str, str]], columns: list[str]) -> list[str]:
    if not rows:
        return ["_None._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(column, "")).replace("|", "\\|") for column in columns) + " |")
    return lines


def write_report(
    path: Path,
    records: list[dict[str, Any]],
    updated: list[dict[str, str]],
    skipped: list[dict[str, str]],
    blocked: list[dict[str, str]],
    errors: list[dict[str, str]],
) -> None:
    enabled = sum(1 for record in records if record.get("enabled"))
    direct = sum(1 for record in records if record.get("direct_commit"))
    lines = [
        "# Upstream App Module Sync Report",
        "",
        f"- generated: {dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}",
        f"- modules: {len(records)}",
        f"- enabled: {enabled}",
        f"- direct_commit: {direct}",
        f"- updated: {len(updated)}",
        f"- skipped: {len(skipped)}",
        f"- blocked: {len(blocked)}",
        f"- errors: {len(errors)}",
        "",
        "## Updated",
        *table(updated, ["id", "upstream", "backup", "source"]),
        "",
        "## Skipped",
        *table(skipped, ["id", "reason"]),
        "",
        "## Blocked",
        *table(blocked, ["id", "reason"]),
        "",
        "## Errors",
        *table(errors, ["id", "reason"]),
    ]
    write_text(path, "\n".join(lines))


def main() -> int:
    parser = argparse.ArgumentParser(description="Sync upstream raw app modules into Rewrite/Sources/Apps.")
    parser.add_argument("--config", default=rel(DEFAULT_CONFIG), help="Path to Rewrite/Remotes/app-modules.json")
    parser.add_argument("--apps-dir", default=rel(DEFAULT_APPS_DIR), help="App source directory")
    parser.add_argument("--report", default=rel(DEFAULT_REPORT), help="Markdown report path")
    parser.add_argument("--config-only", action="store_true", help="Only discover and write app-modules.json/report")
    args = parser.parse_args()

    config_path = repo_path(args.config)
    apps_dir = repo_path(args.apps_dir)
    report_path = repo_path(args.report)

    try:
        config = read_json(config_path)
        records = discover_modules(config, apps_dir)
        updated, skipped, blocked, errors = sync_records(records, args.config_only)
        write_config(config_path, config, records)
        write_report(report_path, records, updated, skipped, blocked, errors)
    except SyncError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    print(
        "Upstream app module sync complete: "
        f"{len(records)} module(s), {len(updated)} updated, "
        f"{len(blocked)} blocked, {len(errors)} error(s)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
