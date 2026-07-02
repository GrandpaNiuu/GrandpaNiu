#!/usr/bin/env python3
"""Validate the single Fusion module repository."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

from validate_module_integrity import validate_all as validate_module_integrity

ROOT = Path(__file__).resolve().parents[1]
MODULE = ROOT / "Ronghemokuai.sgmodule"
RELEASE = ROOT / "Release" / "Ronghemokuai.sgmodule"
RELEASE_ALIAS = ROOT / "Release" / "Module.sgmodule"
README = ROOT / "README.md"
SOURCES_JSON = ROOT / "Rewrite" / "Remotes" / "sources.json"
CANDIDATES_JSON = ROOT / "Rewrite" / "Remotes" / "candidates.json"
EXPECTED_UPDATE_URL = "#!update-url=https://grandpaniuu.github.io/GrandpaNiu/Ronghemokuai.sgmodule"

REQUIRED_MARKERS = (
    "[Rule]",
    "[URL Rewrite]",
    "[Header Rewrite]",
    "[Body Rewrite]",
    "[Map Local]",
    "[Script]",
    "[MITM]",
    "spotify-json",
    "spotify-proto",
    "youtube.response",
    "zhihu-enhance",
    "bilibili.protobuf.request.js",
    "bilibili.protobuf.response.js",
    EXPECTED_UPDATE_URL,
)

REQUIRED_FILES = (
    "README.md",
    "SECURITY.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "Ronghemokuai.sgmodule",
    "Release/Ronghemokuai.sgmodule",
    "Release/Module.sgmodule",
    "Rewrite/Profiles/fusion.conf",
    "Rewrite/Remotes/sources.json",
    "Rewrite/Remotes/candidates.json",
    "Rewrite/Sources/MITM-core.conf",
    "Rewrite/Sources/MITM-app-clean.conf",
    "Rewrite/Sources/MITM-stable-plus.conf",
    "Rewrite/Sources/MITM-extended.conf",
    "Rules/direct.list",
    "Rules/reject.list",
    "Rules/wechat-ad.list",
    "Rules/aggressive-ad-sources.list",
    "Scripts/app-cleaner.js",
    "Scripts/app-cleaner-active.conf",
    "Scripts/generated/fusion-script-bundle.cache.json",
    "Scripts/spotify.conf",
    "Scripts/youtube.conf",
    "Scripts/zhihu-enhance.conf",
    "Scripts/zhihu-enhance.js",
    "scripts/refresh_module_date.py",
    "scripts/build_module.py",
    "scripts/build_release_variants.py",
    "scripts/factory_finalize.py",
    "scripts/build_windows_v2rayn.py",
    "scripts/check_automation_status.py",
    "tools/generate_automation_gap_report.py",
    "scripts/commit_generated_changes.sh",
    "tools/acquire_automation_lock.sh",
    "tools/release_automation_lock.sh",
    "scripts/validate_profiles.py",
    "scripts/validate_module_integrity.py",
    "scripts/validate_repository.py",
    "tools/generate_automated_quality_evidence.py",
    "reports/multi_release_report.md",
    "reports/module_integrity_report.md",
    "reports/automated_quality_evidence.md",
    "reports/automation_gap_report.md",
    "Windows/v2rayN/GrandpaNiu-v2rayN-custom-routing.json",
    "Windows/v2rayN/README.md",
)

REQUIRED_WORKFLOWS = (
    ".github/workflows/module-factory-build.yml",
    ".github/workflows/daily-module-update.yml",
    ".github/workflows/daily-audit-and-repair.yml",
    ".github/workflows/daily-invalid-source-repair.yml",
    ".github/workflows/upstream-collect.yml",
    ".github/workflows/scheduled-module-update.yml",
    ".github/workflows/upstream-app-module-sync.yml",
    ".github/workflows/daily-schedule-watchdog.yml",
    ".github/workflows/repository-health.yml",
)

EXPECTED_WORKFLOW_CRONS = {
    ".github/workflows/daily-module-update.yml": "37 16 * * *",          # Beijing 00:37
    ".github/workflows/daily-audit-and-repair.yml": "43 16 * * *",      # Beijing 00:43
    ".github/workflows/daily-invalid-source-repair.yml": "49 16 * * *", # Beijing 00:49
    ".github/workflows/upstream-collect.yml": "55 16 * * *",            # Beijing 00:55
    ".github/workflows/scheduled-module-update.yml": "7 17 * * *",      # Beijing 01:07
    ".github/workflows/upstream-app-module-sync.yml": "19 17 * * *",    # Beijing 01:19
    ".github/workflows/daily-schedule-watchdog.yml": "30 20 * * *",     # Beijing 04:30
}

ALLOWED_REMOTE_TYPES = {"RULE-SET", "DOMAIN-SET"}
ALLOWED_POLICIES = {"REJECT", "REJECT-DROP", "DIRECT"}
DISALLOWED_MAIN_RULE_POLICIES = {"DIRECT", "PROXY"}
RULE_PREFIXES = {
    "AND",
    "DOMAIN",
    "DOMAIN-KEYWORD",
    "DOMAIN-SET",
    "DOMAIN-SUFFIX",
    "IP-CIDR",
    "IP-CIDR6",
    "RULE-SET",
    "URL-REGEX",
}
RULE_POLICY_TOKENS = {"DIRECT", "PROXY", "REJECT", "REJECT-DROP", "REJECT-TINYGIF", "REJECT-IMG"}
BLOCKED_URL_TOKENS = ("ghproxy", "mirror", "tinyurl", "bit.ly", "t.co/", "shorturl")
SECTION_RE = re.compile(r"^\[([^\]]+)\]\s*$")
SCRIPT_NAME_RE = re.compile(r"^\s*([^#\s][^=]+?)\s*=")
HOSTNAME_RE = re.compile(r"^\s*hostname\s*=\s*(.+)$")
MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
UNRESOLVED_ARGUMENT_RE = re.compile(r"\{\{\{[^}]+\}\}\}")
PROTECTED_REJECT_TOKENS = (
    "api.biliapi",
    "app.biliapi",
    "api.biliapi.com",
    "api.biliapi.net",
    "app.biliapi.com",
    "app.biliapi.net",
    "api.iqiyi.com",
    "ipv4.music.163.com",
    "ipv6.music.163.com",
    "httpdns",
    "httpdns.",
    "httpdns-",
    "httpdns.music.163.com",
    "httpdns.baidubce.com",
    "httpdnsmultiapi.meituan.com",
    "httpdnsmultiapivip.meituan.com",
    "hdns.ksyun.com",
    "lofter.httpdns.c.163.com",
    "wechatpay",
    "alipay",
    "adgw.alipay.com",
    "amdc.alipay.com",
    "amdc-sibling.alipay.com.cn",
    "mobiledc.stable.alipay.net",
    "rtms.alipay.com",
    "api.verify.mob.com",
    "log-verify.mob.com",
    "mdap.wallet.pbcdci.cn",
    "mdc.wallet.pbcdci.cn",
    "abchina.com.cn",
    "boc.cn",
    "icbc",
    "ccb.com",
    "cmbchina",
    "bankcomm",
    "psbc",
    "cd-1.pddpic.com",
    "cdl-1.pddpic.com",
    "cdl-p2.pddpic.com",
    "ossgw.alicdn.com",
    "hudong.alicdn.com",
    "baichuan-sdk.alicdn.com",
    "nbsdk-baichuan.alicdn.com",
    "baidustatic.com",
    "zijieapi.com",
    "zijieapi.net",
    "zijiecdn.com",
    "snssdk.com",
)
BILIBILI_DISALLOWED_BODY_REWRITE_TOKENS = (
    "data.payment",
    "/x/v2/account/mine",
    "vip_section",
    "modular_vip_section",
)
TEXT_FILE_SUFFIXES = {
    ".conf",
    ".sgmodule",
    ".module",
    ".list",
    ".py",
    ".js",
    ".json",
    ".md",
    ".yml",
    ".yaml",
    ".html",
    ".txt",
    ".editorconfig",
    ".gitattributes",
    ".gitignore",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def read_text(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8", errors="replace")


def read_json(path: Path) -> dict:
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")


def active_lines(text: str):
    for line in text.splitlines():
        stripped = line.strip()
        if stripped and not stripped.startswith("#"):
            yield stripped


def split_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = {}
    current = "META"
    sections[current] = []
    for line in text.splitlines():
        match = SECTION_RE.match(line.strip())
        if match:
            current = match.group(1)
            sections.setdefault(current, [])
            continue
        sections.setdefault(current, []).append(line.rstrip())
    return sections


def rule_policy(line: str) -> str | None:
    stripped = line.strip()
    if not stripped or stripped.startswith("#"):
        return None
    parts = stripped.split(",")
    if parts[0] not in RULE_PREFIXES:
        return None
    for part in parts[2:]:
        token = part.strip().upper()
        if token in RULE_POLICY_TOKENS:
            return token
    return None


def workflow_has_fusion_build(text: str) -> bool:
    """Accept shell commands and Python subprocess list syntax."""
    normalized = re.sub(r"\s+", " ", text)
    has_builder = "build_module.py" in text or "Rewrite/Generator/Builder.py" in text
    patterns = (
        "--profile fusion",
        "--profile=fusion",
        '"--profile", "fusion"',
        "'--profile', 'fusion'",
        '"--profile","fusion"',
        "'--profile','fusion'",
        "fusion-build-marker: scripts/build_module.py --build --profile fusion",
    )
    return has_builder and any(pattern in normalized or pattern in text for pattern in patterns)


def parse_hosts(text: str) -> list[str]:
    hosts: list[str] = []
    for line in text.splitlines():
        match = HOSTNAME_RE.match(line)
        if not match:
            continue
        value = match.group(1).replace("%APPEND%", "")
        hosts.extend(host.strip() for host in value.split(",") if host.strip())
    return hosts


def unresolved_argument_names(text: str) -> set[str]:
    return {match.group(0)[3:-3].strip() for match in UNRESOLVED_ARGUMENT_RE.finditer(text)}


def declared_argument_names(text: str) -> set[str]:
    names: set[str] = set()
    for raw in text.splitlines():
        stripped = raw.strip()
        if not stripped.startswith("#!arguments="):
            continue
        for item in stripped.split("=", 1)[1].split(","):
            if ":" not in item:
                continue
            name = item.split(":", 1)[0].strip()
            if name:
                names.add(name)
    return names


def validate_root_release() -> None:
    root_text = read_text(MODULE)
    release_text = read_text(RELEASE)
    if root_text != release_text:
        fail("Ronghemokuai.sgmodule and Release/Ronghemokuai.sgmodule differ")
    if read_text(RELEASE_ALIAS) != release_text:
        fail("Release/Module.sgmodule and Release/Ronghemokuai.sgmodule differ")
    for marker in REQUIRED_MARKERS:
        if marker not in root_text:
            fail(f"required marker missing from root module: {marker}")
    unresolved = unresolved_argument_names(root_text)
    if unresolved:
        missing = sorted(unresolved - declared_argument_names(root_text))
        if missing:
            fail("root module contains undeclared argument placeholders: " + ", ".join(missing))
    sections = split_sections(root_text)
    for line in active_lines("\n".join(sections.get("Rule", []))):
        policy = rule_policy(line)
        if policy in DISALLOWED_MAIN_RULE_POLICIES:
            fail(f"root Fusion [Rule] must not contain {policy} routing/protection rule: {line}")
    for line in active_lines(root_text):
        upper = line.upper()
        lowered = line.lower()
        normalized = lowered.replace(r"\/", "/")
        if "bilibili" in normalized:
            if 'data="{' in normalized:
                fail("root module contains raw JSON Bilibili map-local data; use base64 data instead")
            for token in BILIBILI_DISALLOWED_BODY_REWRITE_TOKENS:
                if token in normalized:
                    fail(f"root module contains disallowed Bilibili account/payment rewrite token: {token}")
        if "REJECT" not in upper:
            continue
        if line.startswith("AND,") and "PROTOCOL,UDP" in upper and (
            "googlevideo.com" in lowered or "youtubei.googleapis.com" in lowered
        ):
            continue
        if any(token in lowered for token in PROTECTED_REJECT_TOKENS):
            fail(f"root module rejects protected core endpoint: {line}")


def validate_single_release_report() -> None:
    report = read_text(ROOT / "reports" / "multi_release_report.md")
    if "单一融合版发布报告" not in report:
        fail("multi_release_report.md must describe the single fusion release")
    if "Ronghemokuai.sgmodule" not in report or "fusion" not in report:
        fail("multi_release_report.md missing fusion release entry")


def validate_remote_schema() -> None:
    data = read_json(SOURCES_JSON)
    urls: set[str] = set()
    for index, item in enumerate(data.get("rule_sets", []), 1):
        for key in ("name", "type", "url", "policy", "enabled", "protected", "purpose"):
            if key not in item:
                fail(f"sources.json rule_sets[{index}] missing {key}")
        if item["type"] not in ALLOWED_REMOTE_TYPES:
            fail(f"sources.json rule_sets[{index}] invalid type: {item['type']}")
        if item["policy"] not in ALLOWED_POLICIES:
            fail(f"sources.json rule_sets[{index}] invalid policy: {item['policy']}")
        url = str(item["url"])
        if not url.startswith("https://"):
            fail(f"sources.json rule_sets[{index}] must use https: {url}")
        if any(token in url.lower() for token in BLOCKED_URL_TOKENS):
            fail(f"sources.json rule_sets[{index}] uses blocked host/token: {url}")
        if url in urls:
            fail(f"duplicate remote source url in sources.json: {url}")
        urls.add(url)

    candidates = read_json(CANDIDATES_JSON)
    if candidates.get("policy", {}).get("search_web") is not False:
        fail("candidates.json policy.search_web must stay false")
    trusted = candidates.get("trusted_repositories", [])
    if not isinstance(trusted, list) or not trusted:
        fail("candidates.json must define trusted_repositories")


def validate_scripts() -> None:
    spotify_text = read_text(ROOT / "Scripts" / "spotify.conf")
    youtube_text = read_text(ROOT / "Scripts" / "youtube.conf")
    app_text = read_text(ROOT / "Scripts" / "app-clean.conf")

    if "spotify-json" not in spotify_text or "spotify-proto" not in spotify_text:
        fail("Scripts/spotify.conf must contain the app2smile Spotify JSON/protobuf scripts")
    if "youtube.response" not in youtube_text:
        fail("Scripts/youtube.conf must contain youtube.response")
    if "zhihu-enhance" not in read_text(ROOT / "Scripts" / "zhihu-enhance.conf"):
        fail("Scripts/zhihu-enhance.conf must contain zhihu-enhance")
    if not any(token in app_text.lower() for token in ("tieba", "qq-news", "vgtime", "fmz200", "zirawell", "wool_scripts", "app2smile")):
        fail("Scripts/app-clean.conf does not appear to contain app cleanup scripts")

    names: set[str] = set()
    for path in (ROOT / "Scripts").glob("*.conf"):
        for line in active_lines(read_text(path)):
            match = SCRIPT_NAME_RE.match(line)
            if not match:
                continue
            name = match.group(1).strip()
            if name in names:
                fail(f"duplicate script name: {name}")
            names.add(name)


def validate_mitm() -> None:
    text = read_text(MODULE)
    mitm_start = text.find("[MITM]")
    if mitm_start < 0:
        fail("[MITM] missing")
    hosts = parse_hosts(text[mitm_start:])
    if not hosts:
        fail("MITM hostname list is empty")
    for host in ("spclient.wg.spotify.com", "*.spclient.spotify.com"):
        if host not in hosts:
            fail(f"root module missing Spotify MITM hostname: {host}")
    if "-grpc.biliapi.net" in hosts or "-grpc.biliapi.net" in text:
        fail("root module must not exclude grpc.biliapi.net; Bilibili protobuf cleanup requires MITM")
    if "grpc.biliapi.net" not in hosts:
        fail("root module missing Bilibili gRPC MITM hostname: grpc.biliapi.net")
    dupes = sorted({host for host in hosts if hosts.count(host) > 1})
    if dupes:
        fail("duplicate MITM hostnames: " + ", ".join(dupes[:20]))


def validate_fusion_profile() -> None:
    fusion = read_text(ROOT / "Rewrite" / "Profiles" / "fusion.conf")
    required_tokens = (
        "name = fusion",
        "Rules/wechat-ad.list",
        "Rules/aggressive-ad-sources.list",
        "Scripts/app2smile-qqnews-stable-plus.conf",
        "Rewrite/Sources/MITM-core.conf",
        "Rewrite/Sources/MITM-app-clean.conf",
        "Rewrite/Sources/MITM-stable-plus.conf",
        "Rewrite/Sources/MITM-extended.conf",
        "single_public_entry = true",
    )
    for token in required_tokens:
        if token not in fusion:
            fail(f"fusion.conf missing required token: {token}")


def validate_files() -> None:
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).exists():
            fail(f"required file missing: {relative}")


def validate_no_utf8_bom() -> None:
    offenders: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix.lower() not in TEXT_FILE_SUFFIXES and path.name not in {"LICENSE", "README.md", "CONTRIBUTING.md"}:
            continue
        if b"\xef\xbb\xbf" in path.read_bytes():
            offenders.append(path.relative_to(ROOT).as_posix())
    if offenders:
        fail("UTF-8 BOM found in tracked text candidates: " + ", ".join(sorted(offenders)[:20]))


def validate_readme_links() -> None:
    text = read_text(README)
    for match in MD_LINK_RE.finditer(text):
        target = match.group(1).strip()
        if not target or target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        path_part = target.split("#", 1)[0]
        if path_part and not (ROOT / path_part).exists():
            fail(f"README link target missing: {target}")


def workflow_contains_cron(text: str, cron: str) -> bool:
    return f'cron: "{cron}"' in text or f"cron: '{cron}'" in text


def validate_workflows() -> None:
    helper = read_text(ROOT / "scripts" / "commit_generated_changes.sh")
    acquire_lock = read_text(ROOT / "tools" / "acquire_automation_lock.sh")
    release_lock = read_text(ROOT / "tools" / "release_automation_lock.sh")
    for token in (
        'git add -- "$@"',
        "for attempt in 1 2 3",
        "git push origin HEAD:main",
        "git fetch origin main",
        "git rebase origin/main",
    ):
        if token not in helper:
            fail(f"generated commit helper missing safety token: {token}")
    for token in ("git add -A", "git reset --hard", "git clean -fd", "git push --force"):
        if token in helper:
            fail(f"generated commit helper contains unsafe command: {token}")

    for token in ("refs/heads/automation-maintenance-lock", "git merge --ff-only", "git commit-tree"):
        if token not in acquire_lock:
            fail(f"automation lock acquire helper missing safety token: {token}")
    for token in ("--force-with-lease", "Automation lock ownership changed"):
        if token not in release_lock:
            fail(f"automation lock release helper missing ownership token: {token}")
    for token in ("git reset --hard", "git clean -fd"):
        if token in acquire_lock or token in release_lock:
            fail(f"automation lock helper contains unsafe command: {token}")

    for relative in REQUIRED_WORKFLOWS:
        path = ROOT / relative
        if not path.exists():
            fail(f"required workflow missing: {relative}")
        text = read_text(path)
        if "contents: write" not in text:
            fail(f"workflow must declare contents: write: {relative}")
        expected_group = "group: module-maintenance-${{ github.workflow }}-${{ github.ref }}"
        if expected_group not in text:
            fail(f"workflow must use isolated maintenance concurrency: {relative}")
        if "scripts/commit_generated_changes.sh" not in text:
            fail(f"workflow must use the generated commit helper: {relative}")
        if "tools/acquire_automation_lock.sh" not in text:
            fail(f"workflow must acquire the cross-workflow maintenance lock: {relative}")
        if "tools/release_automation_lock.sh" not in text or "if: always()" not in text:
            fail(f"workflow must always release the cross-workflow maintenance lock: {relative}")
        for token in ("git add -A", "git reset --hard", "git clean -fd", "git push --force"):
            if token in text:
                fail(f"workflow contains unsafe git command {token}: {relative}")

    for relative in REQUIRED_WORKFLOWS:
        text = read_text(ROOT / relative)
        if not workflow_has_fusion_build(text):
            fail(f"{relative} must build with fusion profile")

    daily = read_text(ROOT / ".github" / "workflows" / "daily-module-update.yml")
    for token in ("build_module.py", "factory_finalize.py", "build_release_variants.py", "validate_repository.py"):
        if token not in daily:
            fail(f"daily-module-update workflow missing command token: {token}")

    for relative, cron in EXPECTED_WORKFLOW_CRONS.items():
        text = read_text(ROOT / relative)
        if not workflow_contains_cron(text, cron):
            fail(f"{relative} must run at expected staggered Beijing schedule: {cron}")

    scheduled = read_text(ROOT / ".github" / "workflows" / "scheduled-module-update.yml")
    if "\n  push:\n" in scheduled:
        fail("scheduled-module-update must not duplicate the Module Factory push validation trigger")
    if "scripts/refresh_module_date.py" not in scheduled:
        fail("scheduled-module-update workflow must refresh Beijing module date before building")

    upstream_app = read_text(ROOT / ".github" / "workflows" / "upstream-app-module-sync.yml")
    if "Rewrite/Sources/Meta.conf" not in upstream_app:
        fail("upstream-app-module-sync workflow must commit refreshed Meta.conf")

    for relative in REQUIRED_WORKFLOWS:
        text = read_text(ROOT / relative)
        if "Rewrite/Generator/Builder.py --profile fusion --release" not in text:
            continue
        if "scripts/commit_generated_changes.sh" not in text:
            continue
        for generated_path in ("Android", "Windows"):
            if f"\n            {generated_path} \\" not in text and f"\n            {generated_path}\n" not in text:
                fail(f"{relative} runs the full Builder but does not commit {generated_path} outputs")

    invalid_source = read_text(ROOT / ".github" / "workflows" / "daily-invalid-source-repair.yml")
    for token in ("collect_upstreams.py", "audit_repair_invalid_sources.py", "validate_remote_rule_syntax.py"):
        if token not in invalid_source:
            fail(f"daily-invalid-source-repair workflow missing command token: {token}")
    audit = read_text(ROOT / ".github" / "workflows" / "daily-audit-and-repair.yml")
    if "\n  push:\n" in audit:
        fail("daily-audit-and-repair must not duplicate the Module Factory push validation trigger")
    if "validate_remote_rule_syntax.py" not in audit:
        fail("daily-audit-and-repair workflow missing validate_remote_rule_syntax.py")

    health = read_text(ROOT / ".github" / "workflows" / "repository-health.yml")
    for token in ("generate_stable_plus_promotion_report.py", "create_promotion_pr.py"):
        if token in health:
            fail(f"repository-health workflow must not run legacy promotion command: {token}")

    watcher = read_text(ROOT / ".github" / "workflows" / "workflow-failure-issue.yml")
    if re.search(r"fromJSON\([^)]*cancelled", watcher):
        fail("workflow-failure-issue must not open issues for cancelled runs")
    if "close-resolved-issues" not in watcher:
        fail("workflow-failure-issue must close stale automation issues after successful runs")

    watchdog = read_text(ROOT / ".github" / "workflows" / "daily-schedule-watchdog.yml")
    for token in ("actions: read", "scripts/check_automation_status.py", "--strict --no-write"):
        if token not in watchdog:
            fail(f"daily-schedule-watchdog workflow missing automation status token: {token}")


def validate_windows_v2rayn() -> None:
    path = ROOT / "Windows" / "v2rayN" / "GrandpaNiu-v2rayN-custom-routing.json"
    try:
        rules = json.loads(read_text(path))
    except json.JSONDecodeError as exc:
        fail(f"invalid v2rayN JSON: {exc}")
    if not isinstance(rules, list) or not rules:
        fail("v2rayN custom routing must be a non-empty JSON array")
    ad_rules = [rule for rule in rules if isinstance(rule, dict) and rule.get("outboundTag") == "block"]
    if not ad_rules:
        fail("v2rayN custom routing must contain block ad rules")
    for rule in ad_rules:
        for key in ("type", "outboundTag", "enabled", "remarks"):
            if key not in rule:
                fail(f"v2rayN ad rule missing {key}")
        if rule.get("enabled") is not True:
            fail("v2rayN ad rule must set enabled=true")
        if rule.get("remarks") != "GrandpaNiu 广告拦截":
            fail("v2rayN ad rule remarks must be GrandpaNiu 广告拦截")

    required_tail = [
        {"domain": ["geosite:private"], "outboundTag": "direct", "remarks": "国内直连"},
        {"domain": ["geosite:cn"], "outboundTag": "direct", "remarks": "国内直连"},
        {"ip": ["geoip:private"], "outboundTag": "direct", "remarks": "国内直连"},
        {"ip": ["geoip:cn"], "outboundTag": "direct", "remarks": "国内直连"},
        {"port": "0-65535", "outboundTag": "proxy", "remarks": "其他全部代理"},
    ]
    if len(rules) < len(required_tail) or rules[-len(required_tail):] != [
        {**item, "type": "field", "enabled": True} for item in required_tail
    ]:
        fail("v2rayN custom routing missing direct/proxy tail rules")


def validate_no_tool_traces() -> None:
    for relative in (".claude", "CLAUDE.md"):
        if (ROOT / relative).exists():
            fail(f"tool trace file should not exist: {relative}")


def validate_automation_gap_report() -> None:
    text = read_text(ROOT / "reports" / "automation_gap_report.md")
    if "- Blocking gaps: 0" not in text:
        fail("automation_gap_report.md must have zero blocking gaps")


def main() -> None:
    validate_files()
    validate_no_utf8_bom()
    validate_root_release()
    validate_module_integrity(write_report=True)
    validate_single_release_report()
    validate_remote_schema()
    validate_scripts()
    validate_mitm()
    validate_fusion_profile()
    validate_readme_links()
    validate_workflows()
    validate_windows_v2rayn()
    validate_automation_gap_report()
    validate_no_tool_traces()
    print("Repository validation passed.")


if __name__ == "__main__":
    main()
