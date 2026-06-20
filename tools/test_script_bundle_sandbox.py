#!/usr/bin/env python3
"""Run the generated script bundle in a Shadowrocket-like Node sandbox."""

from __future__ import annotations

import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BUNDLE = ROOT / "Scripts" / "generated" / "fusion-script-bundle.js"
MANIFEST = ROOT / "Scripts" / "generated" / "fusion-script-bundle.manifest.json"
REPORT = ROOT / "reports" / "script_bundle_sandbox_report.md"


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def node_executable() -> str:
    configured = os.environ.get("NODE_BINARY")
    if configured and Path(configured).exists():
        return configured
    found = shutil.which("node")
    if found:
        return found
    raise SystemExit("ERROR: node executable not found")


def read_text(path: Path) -> str:
    if not path.exists():
        raise SystemExit(f"ERROR: missing file: {rel(path)}")
    return path.read_text(encoding="utf-8", errors="replace")


def load_routes() -> list[dict[str, object]]:
    data = json.loads(read_text(MANIFEST))
    routes = data.get("routes", [])
    if not isinstance(routes, list):
        raise SystemExit("ERROR: manifest routes must be a list")
    return [item for item in routes if isinstance(item, dict)]


def sample_body() -> str:
    return json.dumps(
        {
            "code": 0,
            "data": {
                "items": [{"id": 1, "isAd": True}, {"id": 2, "title": "normal"}],
                "ads": [{"id": "ad"}],
                "ad": {"id": "ad"},
                "banner": [{"id": "banner"}],
                "popup": {"show": True},
            },
            "result": {"list": [{"ad": True}, {"name": "normal"}]},
        },
        ensure_ascii=False,
    )


def harness(bundle_text: str, target_index: int) -> str:
    return "\n".join(
        [
            "const targetIndex = %d;" % target_index,
            "let doneCalled = false;",
            "let donePayload = null;",
            "let routeProbe = 0;",
            "const originalTest = RegExp.prototype.test;",
            "RegExp.prototype.test = function(value) {",
            "  if (value === '__grandpaniu_sandbox_url__') {",
            "    const current = routeProbe++;",
            "    return current === targetIndex;",
            "  }",
            "  return originalTest.call(this, value);",
            "};",
            "globalThis.$request = { url: '__grandpaniu_sandbox_url__', method: 'GET', headers: {} };",
            "globalThis.$response = { body: %s, headers: { 'content-type': 'application/json' } };" % json.dumps(sample_body()),
            "globalThis.$done = function(payload) { doneCalled = true; donePayload = payload || {}; };",
            "globalThis.console = console;",
            bundle_text,
            "if (!doneCalled) { throw new Error('bundle did not call $done'); }",
            "if (donePayload !== null && typeof donePayload !== 'object') { throw new Error('$done payload must be an object'); }",
            "",
        ]
    )


def run_case(node: str, bundle_text: str, target_index: int, name: str) -> tuple[bool, str]:
    with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False, encoding="utf-8", newline="\n") as handle:
        handle.write(harness(bundle_text, target_index))
        temp_path = Path(handle.name)
    try:
        proc = subprocess.run(
            [node, str(temp_path)],
            cwd=ROOT,
            text=True,
            encoding="utf-8",
            errors="replace",
            capture_output=True,
            timeout=20,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return False, f"{type(exc).__name__}: {exc}"
    finally:
        try:
            temp_path.unlink()
        except OSError:
            pass
    if proc.returncode != 0:
        output = (proc.stdout + proc.stderr).strip()
        return False, output[-800:] or f"node exited {proc.returncode}"
    return True, "passed"


def write_report(rows: list[dict[str, object]]) -> None:
    now = dt.datetime.now(dt.timezone.utc).astimezone(dt.timezone(dt.timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")
    failed = [row for row in rows if not row["ok"]]
    lines = [
        "# Script Bundle Sandbox Report",
        "",
        f"- Generated at: {now}",
        f"- Status: {'failed' if failed else 'passed'}",
        f"- Cases: {len(rows)}",
        f"- Failed: {len(failed)}",
        "",
        "## Failed Cases",
    ]
    if failed:
        lines.extend(f"- `{row['name']}`: {row['message']}" for row in failed)
    else:
        lines.append("- None")
    lines.extend(["", "## Coverage", ""])
    for row in rows[:160]:
        lines.append(f"- `{row['name']}`: {row['message']}")
    if len(rows) > 160:
        lines.append(f"- ... {len(rows) - 160} more")
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> None:
    node = node_executable()
    routes = load_routes()
    bundle_text = read_text(BUNDLE)
    rows: list[dict[str, object]] = []
    ok, message = run_case(node, bundle_text, -1, "no-route-pass-through")
    rows.append({"name": "no-route-pass-through", "ok": ok, "message": message})
    for index, route in enumerate(routes):
        name = str(route.get("name") or f"route-{index}")
        ok, message = run_case(node, bundle_text, index, name)
        rows.append({"name": name, "ok": ok, "message": message})
    write_report(rows)
    failed = [row for row in rows if not row["ok"]]
    if failed:
        for row in failed:
            print(f"ERROR: {row['name']}: {row['message']}", file=sys.stderr)
        raise SystemExit(1)
    print(f"Script bundle sandbox passed; report={rel(REPORT)}")


if __name__ == "__main__":
    main()
