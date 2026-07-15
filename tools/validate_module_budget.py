#!/usr/bin/env python3
"""Validate conservative size and complexity budgets for the generated Fusion module."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
DEFAULT_CONFIG = ROOT / "Rewrite" / "Generator" / "module-budgets.json"
DEFAULT_JSON_REPORT = ROOT / "reports" / "module_budget_report.json"
DEFAULT_MD_REPORT = ROOT / "reports" / "module_budget_report.md"


def as_int(value: object, label: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{label} must be a non-negative integer")
    return value


def exception_for_line(
    section: str, line: str, exceptions: list[dict[str, object]]
) -> dict[str, object] | None:
    for item in exceptions:
        if str(item.get("section", "")) != section:
            continue
        marker = str(item.get("contains", ""))
        if marker and marker in line:
            return item
    return None


def mitm_tokens(lines: list[str]) -> list[str]:
    tokens: list[str] = []
    for line in lines:
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        if key.strip().lower() != "hostname":
            continue
        value = value.strip()
        if value.upper().startswith("%APPEND%"):
            value = value[len("%APPEND%") :].strip()
        for token in value.split(","):
            normalized = token.strip()
            if not normalized:
                continue
            tokens.append(normalized.lower())
    return tokens


def analyze_module_text(
    text: str, config: dict[str, object], *, module_size: int | None = None
) -> dict[str, object]:
    if config.get("schema") != 1:
        raise ValueError("unsupported module budget schema")
    module_config = dict(config.get("module", {}))
    section_config = dict(config.get("sections", {}))
    mitm_config = dict(config.get("mitm", {}))
    raw_exceptions = config.get("large_line_exceptions", [])
    if not isinstance(raw_exceptions, list):
        raise ValueError("large_line_exceptions must be a list")
    exceptions = [dict(item) for item in raw_exceptions if isinstance(item, dict)]
    exception_ids: set[str] = set()
    for item in exceptions:
        exception_id = str(item.get("id", "")).strip()
        if not exception_id:
            raise ValueError("large-line exception id is required")
        if exception_id in exception_ids:
            raise ValueError(f"duplicate large-line exception id: {exception_id}")
        exception_ids.add(exception_id)
        if not str(item.get("section", "")).strip() or not str(item.get("contains", "")):
            raise ValueError(f"large-line exception {exception_id} requires section and contains")
        as_int(item.get("max_chars"), f"exception {exception_id}.max_chars")
        as_int(item.get("expected_matches", 1), f"exception {exception_id}.expected_matches")

    max_bytes = as_int(module_config.get("max_bytes"), "module.max_bytes")
    max_lines = as_int(module_config.get("max_lines"), "module.max_lines")
    max_default_line_chars = as_int(
        module_config.get("max_default_line_chars"), "module.max_default_line_chars"
    )

    lines = text.splitlines()
    encoded_size = len(text.encode("utf-8")) if module_size is None else module_size
    current_section = "Meta"
    active_counts: Counter[str] = Counter()
    active_by_section: dict[str, list[str]] = {}
    line_details: list[dict[str, object]] = []
    exception_matches: Counter[str] = Counter()
    errors: list[str] = []

    for number, raw in enumerate(lines, 1):
        stripped = raw.strip()
        if stripped.startswith("[") and stripped.endswith("]"):
            current_section = stripped[1:-1]
            continue
        if not stripped or (stripped.startswith("#") and not stripped.startswith("#!")):
            continue

        active_counts[current_section] += 1
        active_by_section.setdefault(current_section, []).append(stripped)
        matched = exception_for_line(current_section, stripped, exceptions)
        uses_exception = len(raw) > max_default_line_chars and matched is not None
        exception_id = str(matched.get("id", "")) if uses_exception and matched else ""
        if uses_exception and exception_id:
            exception_matches[exception_id] += 1

        detail = {
            "line": number,
            "section": current_section,
            "chars": len(raw),
            "sha256": hashlib.sha256(raw.encode("utf-8")).hexdigest(),
            "prefix": raw[:120],
            "exception_id": exception_id or None,
        }
        line_details.append(detail)

        if len(raw) <= max_default_line_chars:
            continue
        if not uses_exception or matched is None:
            errors.append(
                f"unregistered oversized line {number} in [{current_section}]: "
                f"{len(raw)} > {max_default_line_chars} chars"
            )
            continue
        exception_limit = as_int(matched.get("max_chars"), f"exception {exception_id}.max_chars")
        if len(raw) > exception_limit:
            errors.append(
                f"large-line exception {exception_id} exceeded at line {number}: "
                f"{len(raw)} > {exception_limit} chars"
            )

    if encoded_size > max_bytes:
        errors.append(f"module bytes exceeded: {encoded_size} > {max_bytes}")
    if len(lines) > max_lines:
        errors.append(f"module lines exceeded: {len(lines)} > {max_lines}")

    for section, raw_budget in section_config.items():
        if not isinstance(raw_budget, dict):
            raise ValueError(f"sections.{section} must be an object")
        limit = as_int(raw_budget.get("max_active_lines"), f"sections.{section}.max_active_lines")
        actual = active_counts.get(str(section), 0)
        if actual > limit:
            errors.append(f"[{section}] active lines exceeded: {actual} > {limit}")

    tokens = mitm_tokens(active_by_section.get("MITM", []))
    wildcard_count = sum(token.startswith("*.") for token in tokens)
    max_mitm_tokens = as_int(mitm_config.get("max_tokens"), "mitm.max_tokens")
    max_wildcards = as_int(mitm_config.get("max_wildcards"), "mitm.max_wildcards")
    if len(tokens) > max_mitm_tokens:
        errors.append(f"MITM tokens exceeded: {len(tokens)} > {max_mitm_tokens}")
    if wildcard_count > max_wildcards:
        errors.append(f"MITM wildcards exceeded: {wildcard_count} > {max_wildcards}")

    for item in exceptions:
        exception_id = str(item["id"])
        expected_matches = as_int(
            item.get("expected_matches", 1), f"exception {exception_id}.expected_matches"
        )
        match_count = exception_matches.get(exception_id, 0)
        if match_count != expected_matches:
            errors.append(
                f"large-line exception {exception_id} expected {expected_matches} oversized line(s), "
                f"matched {match_count}"
            )

    longest_lines = sorted(line_details, key=lambda item: (-int(item["chars"]), int(item["line"])))[:10]
    return {
        "status": "failed" if errors else "passed",
        "errors": errors,
        "module": {
            "bytes": encoded_size,
            "max_bytes": max_bytes,
            "lines": len(lines),
            "max_lines": max_lines,
            "active_lines": sum(active_counts.values()),
            "max_default_line_chars": max_default_line_chars,
        },
        "section_counts": dict(sorted(active_counts.items())),
        "section_budgets": section_config,
        "mitm": {
            "tokens": len(tokens),
            "max_tokens": max_mitm_tokens,
            "wildcards": wildcard_count,
            "max_wildcards": max_wildcards,
        },
        "longest_lines": longest_lines,
        "exception_matches": dict(sorted(exception_matches.items())),
        "large_line_exceptions": exceptions,
    }


def build_markdown(payload: dict[str, object]) -> str:
    module = dict(payload["module"])
    mitm = dict(payload["mitm"])
    lines = [
        "# Fusion Module Complexity Budget",
        "",
        f"- Generated at: `{payload['generated_at']}`",
        f"- Status: `{payload['status']}`",
        "- Scope: generated Fusion complexity only; this validator does not rewrite module content.",
        f"- Module bytes: `{module['bytes']}` / `{module['max_bytes']}`",
        f"- Module lines: `{module['lines']}` / `{module['max_lines']}`",
        f"- Active lines: `{module['active_lines']}`",
        f"- MITM tokens: `{mitm['tokens']}` / `{mitm['max_tokens']}`",
        f"- MITM wildcards: `{mitm['wildcards']}` / `{mitm['max_wildcards']}`",
        "",
        "## Section Budgets",
        "",
        "| Section | Active | Budget |",
        "|---|---:|---:|",
    ]
    counts = dict(payload["section_counts"])
    budgets = dict(payload["section_budgets"])
    for section, raw_budget in budgets.items():
        budget = dict(raw_budget)
        lines.append(f"| `{section}` | {counts.get(section, 0)} | {budget['max_active_lines']} |")

    lines.extend(
        [
            "",
            "## Longest Active Lines",
            "",
            "| Line | Section | Characters | Exception | SHA-256 | Prefix |",
            "|---:|---|---:|---|---|---|",
        ]
    )
    for item in list(payload["longest_lines"]):
        row = dict(item)
        prefix = str(row["prefix"]).replace("|", "\\|").replace("`", "'")
        lines.append(
            f"| {row['line']} | `{row['section']}` | {row['chars']} | "
            f"`{row['exception_id'] or '-'}` | `{str(row['sha256'])[:12]}` | `{prefix}` |"
        )

    lines.extend(["", "## Errors", ""])
    errors = list(payload["errors"])
    lines.extend(f"- {error}" for error in errors)
    if not errors:
        lines.append("- None")
    lines.append("")
    return "\n".join(lines)


def resolve_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else ROOT / path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--module", default=str(DEFAULT_MODULE.relative_to(ROOT)))
    parser.add_argument("--config", default=str(DEFAULT_CONFIG.relative_to(ROOT)))
    parser.add_argument("--json-report", default=str(DEFAULT_JSON_REPORT.relative_to(ROOT)))
    parser.add_argument("--markdown-report", default=str(DEFAULT_MD_REPORT.relative_to(ROOT)))
    args = parser.parse_args()

    module_path = resolve_path(args.module)
    config_path = resolve_path(args.config)
    json_report = resolve_path(args.json_report)
    markdown_report = resolve_path(args.markdown_report)

    try:
        text = module_path.read_text(encoding="utf-8")
        config: dict[str, Any] = json.loads(config_path.read_text(encoding="utf-8"))
        payload = analyze_module_text(text, config, module_size=module_path.stat().st_size)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: module budget validation setup failed: {exc}", file=sys.stderr)
        return 1

    payload["generated_at"] = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    payload["module_path"] = module_path.relative_to(ROOT).as_posix()
    payload["config_path"] = config_path.relative_to(ROOT).as_posix()
    json_report.parent.mkdir(parents=True, exist_ok=True)
    json_report.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    markdown_report.write_text(build_markdown(payload), encoding="utf-8", newline="\n")

    print(
        f"Module budget {payload['status']}: {payload['module']['bytes']} bytes, "
        f"{payload['module']['lines']} lines, {payload['mitm']['tokens']} MITM tokens."
    )
    for error in payload["errors"]:
        print(f"ERROR: {error}", file=sys.stderr)
    return 1 if payload["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
