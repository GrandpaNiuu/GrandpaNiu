#!/usr/bin/env python3
"""Validate automatic upstream app sync risk boundaries."""

from __future__ import annotations

import datetime as dt
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
CONFIG = ROOT / "Rewrite" / "Remotes" / "app-modules.json"
APPS_DIR = ROOT / "Rewrite" / "Sources" / "Apps"
REPORT = ROOT / "reports" / "upstream_risk_gate_report.md"

TRUSTED_HOSTS = {"raw.githubusercontent.com", "github.com", "kelee.one"}
CORE_BACKUP_IDS = {"spotify", "youtube", "zhihu", "wechat", "weibo", "bilibili"}
SENSITIVE_ID_TOKENS = (
    "bank",
    "pay",
    "wallet",
    "alipay",
    "wechatpay",
    "passport",
    "login",
    "auth",
    "captcha",
    "verify",
    "insurance",
    "flight",
    "air",
    "12306",
)
HARD_FORBIDDEN_PATTERNS = [
    re.compile(pattern, re.IGNORECASE)
    for pattern in (
        r"\b(vip|premium|membership|member)\b.{0,24}\b(unlock|crack|free|bypass)\b",
        r"\b(unlock|crack|bypass)\b.{0,24}\b(vip|premium|membership|member)\b",
        r"\b(payment|pay|bank|alipay|wechatpay)\b.{0,24}\b(bypass|crack|unlock)\b",
        r"\b(login|passport|auth|captcha)\b.{0,24}\b(bypass|crack|unlock)\b",
        r"\b(receipt|entitlement|in[_-]?app[_-]?purchase|purchase[_-]?receipt)\b",
        r"(会员|订阅|付费|内购).{0,16}(解锁|破解|绕过|免费)",
        r"(登录|认证|验证码|支付|银行).{0,16}(绕过|破解|解锁)",
    )
]
HEADER_AUTH_RE = re.compile(r"\b(cookie|authorization|x-token|x-auth-token|set-cookie)\b", re.IGNORECASE)


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""


def write_report(errors: list[str], warnings: list[str], rows: list[dict[str, object]]) -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    enabled = [row for row in rows if row.get("enabled")]
    direct = [row for row in enabled if row.get("direct_commit")]
    high = [row for row in enabled if row.get("risk") == "high"]
    lines = [
        "# Upstream Risk Gate Report",
        "",
        f"- Generated at: {now}",
        f"- Status: {'failed' if errors else 'passed'}",
        f"- Records: {len(rows)}",
        f"- Enabled: {len(enabled)}",
        f"- Direct commit: {len(direct)}",
        f"- High risk enabled: {len(high)}",
        "",
        "## Errors",
    ]
    lines.extend(f"- {item}" for item in errors) if errors else lines.append("- None")
    lines.extend(["", "## Warnings"])
    lines.extend(f"- {item}" for item in warnings) if warnings else lines.append("- None")
    lines.extend([
        "",
        "## Policy",
        "",
        "- Enabled direct-commit records must use HTTPS and trusted hosts.",
        "- High-risk and core app records must keep backup enabled.",
        "- Target paths must stay under `Rewrite/Sources/Apps/`.",
        "- Clear VIP unlock, payment bypass, login bypass, purchase receipt and token rewrites are blocked.",
        "",
        "## High Risk Enabled Records",
        "",
    ])
    for row in high[:120]:
        lines.append(f"- `{row['id']}` -> `{row['target']}` ({row['upstream_project']})")
    if len(high) > 120:
        lines.append(f"- ... {len(high) - 120} more")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def load_config() -> tuple[list[dict[str, object]], list[str]]:
    errors: list[str] = []
    if not CONFIG.exists():
        return [], [f"missing config: {rel(CONFIG)}"]
    try:
        data = json.loads(read_text(CONFIG))
    except json.JSONDecodeError as exc:
        return [], [f"invalid app-modules json: {exc}"]
    modules = data.get("modules", [])
    if not isinstance(modules, list):
        return [], ["app-modules.json `modules` must be a list"]
    return [item for item in modules if isinstance(item, dict)], errors


def target_path(value: str) -> Path:
    path = ROOT / value
    return path.resolve()


def trusted_source(url: str) -> bool:
    parsed = urlparse(url)
    return parsed.scheme == "https" and parsed.netloc.lower() in TRUSTED_HOSTS


def has_sensitive_id(record_id: str, name: str) -> bool:
    text = f"{record_id} {name}".lower()
    return any(token in text for token in SENSITIVE_ID_TOKENS)


def scan_source(record_id: str, path: Path, errors: list[str], warnings: list[str]) -> None:
    text = read_text(path)
    if not text.strip():
        errors.append(f"{record_id}: target source is empty: {rel(path)}")
        return
    for pattern in HARD_FORBIDDEN_PATTERNS:
        match = pattern.search(text)
        if match:
            errors.append(f"{record_id}: forbidden upstream behavior matched `{match.group(0)[:80]}` in {rel(path)}")
            break
    for line_no, line in enumerate(text.splitlines(), 1):
        lowered = line.lower()
        if "header-rewrite" in lowered and HEADER_AUTH_RE.search(line):
            errors.append(f"{record_id}: header auth/cookie rewrite near {rel(path)}:{line_no}")
        if "script-path=" in lowered and any(token in lowered for token in ("receipt", "entitlement", "in-app-purchase", "purchase")):
            errors.append(f"{record_id}: purchase-related script path near {rel(path)}:{line_no}")
    if "auto-sync: true" not in text and "source-url:" not in text:
        warnings.append(f"{record_id}: target lacks auto-sync/source-url markers")


def validate() -> tuple[list[str], list[str], list[dict[str, object]]]:
    rows, errors = load_config()
    warnings: list[str] = []
    seen_ids: set[str] = set()
    seen_targets: set[str] = set()
    apps_root = APPS_DIR.resolve()
    for item in rows:
        record_id = str(item.get("id", "")).strip()
        name = str(item.get("name", "")).strip()
        source_url = str(item.get("source_url", "")).strip()
        target = str(item.get("target", "")).strip()
        enabled = bool(item.get("enabled"))
        direct_commit = bool(item.get("direct_commit"))
        risk = str(item.get("risk", "")).strip().lower()
        backup = bool(item.get("backup"))
        if not record_id:
            errors.append("record missing id")
            continue
        if record_id in seen_ids:
            errors.append(f"duplicate app module id: {record_id}")
        seen_ids.add(record_id)
        if not target:
            errors.append(f"{record_id}: missing target")
            continue
        resolved = target_path(target)
        try:
            resolved.relative_to(apps_root)
        except ValueError:
            errors.append(f"{record_id}: target escapes app source directory: {target}")
        if target in seen_targets:
            errors.append(f"{record_id}: duplicate target: {target}")
        seen_targets.add(target)
        if enabled and direct_commit:
            if not trusted_source(source_url):
                errors.append(f"{record_id}: direct_commit source is not trusted HTTPS: {source_url}")
            if risk not in {"low", "medium", "high"}:
                errors.append(f"{record_id}: invalid risk value: {risk or '<empty>'}")
            if (risk == "high" or record_id in CORE_BACKUP_IDS or has_sensitive_id(record_id, name)) and not backup:
                errors.append(f"{record_id}: high/sensitive direct_commit record must keep backup=true")
            if not resolved.exists():
                errors.append(f"{record_id}: enabled target missing: {target}")
            else:
                scan_source(record_id, resolved, errors, warnings)
    return errors, warnings, rows


def main() -> None:
    errors, warnings, rows = validate()
    write_report(errors, warnings, rows)
    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Upstream risk gate passed; report={rel(REPORT)}")


if __name__ == "__main__":
    main()
