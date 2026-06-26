#!/usr/bin/env python3
"""Validate the generated script aggregation bundle and manifest."""

from __future__ import annotations

from collections import Counter
import datetime as dt
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "Scripts" / "generated" / "fusion-script-bundle.js"
MANIFEST = ROOT / "Scripts" / "generated" / "fusion-script-bundle.manifest.json"
CACHE = ROOT / "Scripts" / "generated" / "fusion-script-bundle.cache.json"
MODULE = ROOT / "Release" / "Ronghemokuai.sgmodule"
REPORT = ROOT / "reports" / "script_aggregation_validation_report.md"

SCRIPT_BUNDLE_URL = "https://raw.githubusercontent.com/GrandpaNiuu/GrandpaNiu/main/Scripts/generated/fusion-script-bundle.js"
SCRIPT_BUNDLE_VERSION = "grandpaniu-fusion-script-bundle-v1"
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path, errors: list[str]) -> str:
    if not path.exists():
        errors.append(f"missing file: {rel(path)}")
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def duplicate_values(values: list[str]) -> list[str]:
    counts = Counter(values)
    return sorted(value for value, count in counts.items() if count > 1)


def script_lines(module_text: str) -> list[str]:
    current = ""
    lines: list[str] = []
    for raw in module_text.splitlines():
        line = raw.strip()
        match = SECTION_RE.match(line)
        if match:
            current = match.group(1)
            continue
        if current == "Script" and line and not line.startswith("#"):
            lines.append(line)
    return lines


def load_manifest(errors: list[str]) -> dict[str, object]:
    text = read_text(MANIFEST, errors)
    if not text:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"invalid manifest json: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append("manifest root must be an object")
        return {}
    return data


def load_cache(errors: list[str]) -> dict[str, object]:
    if not CACHE.exists():
        errors.append(f"missing file: {rel(CACHE)}")
        return {}
    text = read_text(CACHE, errors)
    if not text:
        return {}
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        errors.append(f"invalid cache json: {exc}")
        return {}
    if not isinstance(data, dict):
        errors.append("cache root must be an object")
        return {}
    return data


def write_report(errors: list[str], warnings: list[str], summary: dict[str, object]) -> None:
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Script Aggregation Validation Report",
        "",
        f"- generated: {dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')}",
        f"- status: {'failed' if errors else 'passed'}",
        f"- routes: {summary.get('routes', 0)}",
        f"- sources: {summary.get('sources', 0)}",
        f"- chunks: {summary.get('chunks', 0)}",
        f"- release bundle entries: {summary.get('release_bundle_entries', 0)}",
        "",
        "## Errors",
    ]
    lines.extend(f"- {item}" for item in errors) if errors else lines.append("- None")
    lines.extend(["", "## Warnings"])
    lines.extend(f"- {item}" for item in warnings) if warnings else lines.append("- None")
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def validate() -> tuple[list[str], list[str], dict[str, object]]:
    errors: list[str] = []
    warnings: list[str] = []
    manifest = load_manifest(errors)
    cache = load_cache(errors)
    bundle_text = read_text(BUNDLE, errors)
    module_text = read_text(MODULE, errors)
    summary: dict[str, object] = {}
    if not manifest:
        return errors, warnings, summary

    bundle = manifest.get("bundle", {})
    policy = manifest.get("policy", {})
    routes = manifest.get("routes", [])
    sources = manifest.get("sources", [])
    manifest_summary = manifest.get("summary", {})
    if not isinstance(bundle, dict):
        errors.append("manifest bundle must be an object")
        bundle = {}
    if not isinstance(policy, dict):
        errors.append("manifest policy must be an object")
        policy = {}
    if not isinstance(routes, list):
        errors.append("manifest routes must be a list")
        routes = []
    if not isinstance(sources, list):
        errors.append("manifest sources must be a list")
        sources = []
    if not isinstance(manifest_summary, dict):
        errors.append("manifest summary must be an object")
        manifest_summary = {}
    cache_sources = cache.get("sources", {}) if isinstance(cache, dict) else {}
    if not isinstance(cache_sources, dict):
        errors.append("cache sources must be an object")
        cache_sources = {}

    chunks = int(bundle.get("chunks") or 0)
    summary.update({
        "routes": len(routes),
        "sources": len(sources),
        "chunks": chunks,
    })

    if manifest.get("schema_version") != 1:
        errors.append("manifest schema_version must be 1")
    if bundle.get("version") != SCRIPT_BUNDLE_VERSION:
        errors.append("bundle version mismatch")
    if bundle.get("path") != rel(BUNDLE):
        errors.append("bundle path mismatch")
    if bundle.get("url") != SCRIPT_BUNDLE_URL:
        errors.append("bundle URL mismatch")
    if bundle_text and bundle.get("sha256") != sha256_text(bundle_text):
        errors.append("bundle sha256 mismatch")
    if bundle_text and SCRIPT_BUNDLE_VERSION not in bundle_text:
        errors.append("bundle version marker missing from JS")

    route_names = [str(item.get("name", "")) for item in routes if isinstance(item, dict)]
    source_keys = [str(item.get("key", "")) for item in sources if isinstance(item, dict)]
    for name in duplicate_values([name for name in route_names if name]):
        errors.append(f"duplicate bundled route name: {name}")
    for key in duplicate_values([key for key in source_keys if key]):
        errors.append(f"duplicate bundled source key: {key}")

    source_set = {key for key in source_keys if key}
    allowed_prefixes = tuple(str(item) for item in policy.get("allowed_prefixes", []) if str(item))
    preserve_tokens = tuple(str(item).lower() for item in policy.get("preserve_tokens", []) if str(item))
    for item in sources:
        if not isinstance(item, dict):
            errors.append("source item must be an object")
            continue
        key = str(item.get("key", ""))
        url = str(item.get("url", ""))
        if key and bundle_text and key not in bundle_text:
            errors.append(f"source key missing from bundle JS: {key}")
        if allowed_prefixes and url and not url.startswith(allowed_prefixes):
            errors.append(f"source URL is outside aggregator allowlist: {url}")
        cached = cache_sources.get(url)
        if isinstance(cached, dict):
            cached_source = str(cached.get("source", ""))
            cached_sha = str(cached.get("sha256", ""))
            if cached_source and cached_sha != sha256_text(cached_source):
                errors.append(f"cache sha256 mismatch for source URL: {url}")
            if cached_source and str(item.get("sha256", "")) != sha256_text(cached_source):
                warnings.append(f"cache source differs from current bundled source: {url}")
        else:
            warnings.append(f"cache missing bundled source URL: {url}")

    for item in routes:
        if not isinstance(item, dict):
            errors.append("route item must be an object")
            continue
        name = str(item.get("name", ""))
        pattern = str(item.get("pattern", ""))
        source_key = str(item.get("source_key", ""))
        source_url = str(item.get("source_url", ""))
        chunk = int(item.get("chunk") or 0)
        if not name or not pattern or not source_key:
            errors.append(f"incomplete bundled route: {name or '<unnamed>'}")
        if source_key not in source_set:
            errors.append(f"route references missing source key: {name} -> {source_key}")
        if chunk < 1 or chunk > max(chunks, 1):
            errors.append(f"route has invalid chunk index: {name} -> {chunk}")
        lowered = " ".join([name, pattern, source_url]).lower()
        matched_tokens = [token for token in preserve_tokens if token and token in lowered]
        if matched_tokens:
            errors.append(f"protected token bundled in route {name}: {', '.join(matched_tokens[:5])}")
        if item.get("pattern_sha256") != sha256_text(pattern):
            errors.append(f"pattern sha256 mismatch for route: {name}")

    release_bundle_lines = [
        line for line in script_lines(module_text)
        if "grandpaniu-script-bundle-" in line or SCRIPT_BUNDLE_URL in line
    ]
    summary["release_bundle_entries"] = len(release_bundle_lines)
    if routes and len(release_bundle_lines) != chunks:
        errors.append(f"Release bundle entry count mismatch: expected {chunks}, got {len(release_bundle_lines)}")
    if not routes and release_bundle_lines:
        errors.append("Release contains bundle entries but manifest has no routes")
    for line in release_bundle_lines:
        if SCRIPT_BUNDLE_URL not in line:
            errors.append(f"Release bundle line uses unexpected script path: {line}")
        if "type=http-response" not in line or "requires-body=1" not in line:
            errors.append(f"Release bundle line has unsafe execution options: {line}")

    if manifest_summary.get("bundled_entries") != len(routes):
        errors.append("summary bundled_entries does not match routes")
    if manifest_summary.get("bundled_sources") != len(sources):
        errors.append("summary bundled_sources does not match sources")
    return errors, warnings, summary


def main() -> None:
    errors, warnings, summary = validate()
    write_report(errors, warnings, summary)
    if errors:
        for item in errors:
            print(f"ERROR: {item}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Script aggregation validation passed; report={rel(REPORT)}")


if __name__ == "__main__":
    main()
