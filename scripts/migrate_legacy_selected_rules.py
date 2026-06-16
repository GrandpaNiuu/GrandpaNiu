from __future__ import annotations

from collections import defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
import re
import urllib.error
import urllib.request

CURRENT_PATH = Path("Ronghemokuai.sgmodule")
LEGACY_PATH = Path(".maintenance/legacy_26_1_27.sgmodule")
REPORT_PATH = Path("reports/legacy_selected_migration_report.md")

SECTIONS = [
    "Rule",
    "URL Rewrite",
    "Header Rewrite",
    "Body Rewrite",
    "Map Local",
    "Script",
    "MITM",
]

AD_HINT_RE = re.compile(
    r"ad|ads|advert|banner|splash|popup|pop|promotion|promote|market|marketing|recommend|hotword|feed|float|card|notice|activity|运营|广告|开屏|弹窗|横幅|推荐|信息流|活动",
    re.I,
)

HIGH_RISK_RE = re.compile(
    r"vip|premium|crack|unlock|member|membership|pay|payment|wallet|bank|login|passport|auth|verify|captcha|token|certificate|cert|wechat|alipay|adult|porn|casino|bet|会员|解锁|破解|支付|钱包|银行|登录|验证码|认证|证书|微信安全|支付宝|成人|博彩",
    re.I,
)

SAFE_SCRIPT_HOSTS = (
    "https://raw.githubusercontent.com/",
    "https://gist.githubusercontent.com/",
)

LIMITS = {
    "Rule": 220,
    "URL Rewrite": 160,
    "Body Rewrite": 80,
    "Map Local": 35,
    "Script": 6,
}


def read_text(path: Path) -> str:
    if not path.exists():
        raise RuntimeError(f"missing file: {path}")
    return path.read_text(encoding="utf-8", errors="replace")


def split_sections(text: str) -> dict[str, list[str]]:
    sections: dict[str, list[str]] = defaultdict(list)
    current = "__header__"
    for line in text.splitlines():
        m = re.match(r"^\[([^\]]+)\]\s*$", line.strip())
        if m:
            current = m.group(1)
            sections[current].append(line)
        else:
            sections[current].append(line)
    return sections


def section_bounds(text: str, section: str) -> tuple[int, int, int]:
    m = re.search(rf"(?m)^\[{re.escape(section)}\]\s*$", text)
    if not m:
        raise RuntimeError(f"missing section: [{section}]")
    body_start = m.end()
    n = re.search(r"(?m)^\[[^\]]+\]\s*$", text[body_start:])
    body_end = body_start + n.start() if n else len(text)
    return m.start(), body_start, body_end


def normalize(line: str) -> str:
    return re.sub(r"\s+", " ", line.strip())


def is_comment_or_empty(line: str) -> bool:
    s = line.strip()
    return not s or s.startswith("#") or re.match(r"^\[[^\]]+\]$", s)


def safe_keyword(line: str) -> bool:
    return bool(AD_HINT_RE.search(line)) and not HIGH_RISK_RE.search(line)


def rule_key(line: str) -> tuple[str, str] | None:
    parts = [p.strip() for p in line.split(",")]
    if len(parts) < 2:
        return None
    if parts[0] in {"DOMAIN", "DOMAIN-SUFFIX", "DOMAIN-KEYWORD", "IP-CIDR", "IP-CIDR6", "URL-REGEX", "AND"}:
        return parts[0], parts[1]
    return None


def existing_rule_actions(lines: list[str]) -> dict[tuple[str, str], set[str]]:
    out: dict[tuple[str, str], set[str]] = defaultdict(set)
    for line in lines:
        if is_comment_or_empty(line):
            continue
        key = rule_key(line.strip())
        if not key:
            continue
        parts = [p.strip() for p in line.split(",")]
        if len(parts) >= 3:
            out[key].add(parts[2].upper())
    return out


def script_url(line: str) -> str | None:
    m = re.search(r"script-path=(https?://[^,\s]+)", line)
    return m.group(1) if m else None


def remote_ok(url: str) -> tuple[bool, str]:
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "GrandpaNiu-legacy-migration/1.0"})
    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            code = resp.getcode()
            if 200 <= code < 400:
                return True, f"HTTP {code}"
            return False, f"HTTP {code}"
    except urllib.error.HTTPError as exc:
        if exc.code in (403, 405):
            try:
                req2 = urllib.request.Request(url, headers={"User-Agent": "GrandpaNiu-legacy-migration/1.0", "Range": "bytes=0-2048"})
                with urllib.request.urlopen(req2, timeout=25) as resp:
                    body = resp.read(2048)
                    if resp.getcode() in (200, 206) and body:
                        return True, f"GET HTTP {resp.getcode()}"
                    return False, f"GET HTTP {resp.getcode()} empty"
            except Exception as exc2:  # noqa: BLE001
                return False, str(exc2)
        if exc.code in (404, 410):
            return False, f"HTTP {exc.code}"
        return False, f"HTTP {exc.code}"
    except Exception as exc:  # noqa: BLE001
        return False, str(exc)


def should_add_rule(line: str, current_rule_actions: dict[tuple[str, str], set[str]]) -> tuple[bool, str]:
    s = line.strip()
    if not s.startswith(("DOMAIN,", "DOMAIN-SUFFIX,", "DOMAIN-KEYWORD,", "IP-CIDR,", "IP-CIDR6,", "URL-REGEX,")):
        return False, "不是可迁移的规则类型"
    if "REJECT" not in s.upper():
        return False, "非 REJECT 去广告规则"
    if not safe_keyword(s):
        return False, "关键词不符合去广告安全筛选或包含高风险词"
    key = rule_key(s)
    if key and key in current_rule_actions and any(action == "DIRECT" for action in current_rule_actions[key]):
        return False, "当前模块已有同目标 DIRECT 白名单，跳过避免冲突"
    return True, "通过"


def should_add_url_rewrite(line: str) -> tuple[bool, str]:
    s = line.strip()
    if " - reject" not in s.lower() and " reject" not in s.lower():
        return False, "不是 reject 类 URL Rewrite"
    if not safe_keyword(s):
        return False, "关键词不符合去广告安全筛选或包含高风险词"
    return True, "通过"


def should_add_body_rewrite(line: str) -> tuple[bool, str]:
    s = line.strip()
    if not s.startswith(("http-response ", "http-response-jq ")):
        return False, "不是 Body Rewrite"
    if not safe_keyword(s):
        return False, "关键词不符合去广告安全筛选或包含高风险词"
    return True, "通过"


def should_add_map_local(line: str) -> tuple[bool, str]:
    s = line.strip()
    if "data-type=" not in s or "status-code=" not in s:
        return False, "不是 Map Local 本地响应"
    if "http://" in s.split(" data-type=", 1)[1] or "https://" in s.split(" data-type=", 1)[1]:
        return False, "响应体包含外部资源，跳过"
    if not safe_keyword(s):
        return False, "关键词不符合去广告安全筛选或包含高风险词"
    return True, "通过"


def should_add_script(line: str) -> tuple[bool, str]:
    s = line.strip()
    if "script-path=" not in s or not s.startswith(tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_")):
        return False, "不是脚本条目"
    if any(x in s for x in ["argument=", "binary-body-mode=1"]):
        return False, "复杂脚本或二进制脚本，跳过避免破坏"
    if not safe_keyword(s):
        return False, "关键词不符合去广告安全筛选或包含高风险词"
    url = script_url(s)
    if not url:
        return False, "没有 script-path URL"
    if not url.startswith(SAFE_SCRIPT_HOSTS):
        return False, "脚本来源不在可信 raw GitHub 范围"
    ok, detail = remote_ok(url)
    if not ok:
        return False, f"脚本 URL 不可确认：{detail}"
    return True, f"通过：{detail}"


def remove_existing_migration_block(text: str, section: str) -> str:
    start = f"# === Legacy 26.1.27 Selected Migration: {section} START ==="
    end = f"# === Legacy 26.1.27 Selected Migration: {section} END ==="
    return re.sub(rf"\n?{re.escape(start)}\n.*?\n{re.escape(end)}\n?", "\n", text, flags=re.S)


def inject_section_block(text: str, section: str, lines: list[str]) -> str:
    if not lines:
        return text
    text = remove_existing_migration_block(text, section)
    _, body_start, body_end = section_bounds(text, section)
    before = text[:body_end].rstrip("\n")
    after = text[body_end:]
    block = [
        "",
        f"# === Legacy 26.1.27 Selected Migration: {section} START ===",
        "# 从旧版融合模块逐条筛选迁移；仅加入缺失、低风险、非重复、非高风险去广告规则。",
        *lines,
        f"# === Legacy 26.1.27 Selected Migration: {section} END ===",
        "",
    ]
    return before + "\n" + "\n".join(block) + after


def update_date(text: str) -> str:
    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d")
    text = re.sub(r"^#!desc=.*$", f"#!desc={today}", text, flags=re.M)
    text = re.sub(r"^# update-date:.*$", f"# update-date: {today}", text, flags=re.M)
    return text


def main() -> None:
    current = read_text(CURRENT_PATH)
    legacy = read_text(LEGACY_PATH)

    for section in ["Rule", "URL Rewrite", "Header Rewrite", "Body Rewrite", "Map Local", "Script", "MITM"]:
        section_bounds(current, section)

    current_sections = split_sections(current)
    legacy_sections = split_sections(legacy)
    current_norm = {normalize(line) for line in current.splitlines() if normalize(line)}
    current_rule_actions = existing_rule_actions(current_sections.get("Rule", []))

    selected: dict[str, list[str]] = {section: [] for section in ["Rule", "URL Rewrite", "Body Rewrite", "Map Local", "Script"]}
    skipped: dict[str, list[str]] = defaultdict(list)

    checks = {
        "Rule": should_add_rule,
        "URL Rewrite": should_add_url_rewrite,
        "Body Rewrite": should_add_body_rewrite,
        "Map Local": should_add_map_local,
        "Script": should_add_script,
    }

    for section, checker in checks.items():
        limit = LIMITS[section]
        for raw_line in legacy_sections.get(section, []):
            line = raw_line.strip()
            if is_comment_or_empty(line):
                continue
            if normalize(line) in current_norm:
                continue
            if section == "Rule":
                ok, reason = checker(line, current_rule_actions)  # type: ignore[misc]
            else:
                ok, reason = checker(line)  # type: ignore[misc]
            if ok and len(selected[section]) < limit:
                selected[section].append(line)
                current_norm.add(normalize(line))
            elif ok:
                skipped[section].append(f"达到本次迁移上限，未加入：{line[:180]}")
            else:
                if len(skipped[section]) < 80:
                    skipped[section].append(f"{reason}：{line[:180]}")

    updated = current
    for section in ["Rule", "URL Rewrite", "Body Rewrite", "Map Local", "Script"]:
        updated = inject_section_block(updated, section, selected[section])
    updated = update_date(updated)

    for marker in ["[Rule]", "[Script]", "[MITM]", "spotify-json", "spotify-proto", "youtube.response"]:
        if marker not in updated:
            raise RuntimeError(f"关键项缺失，停止提交：{marker}")

    CURRENT_PATH.write_text(updated, encoding="utf-8")
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)

    report_lines = [
        "# 旧版 26.1.27 精选规则迁移报告",
        "",
        f"生成时间：{datetime.now(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S %z')}",
        "",
        "## 迁移原则",
        "",
        "- 保留当前新框架，不整包覆盖。",
        "- 只从旧版中迁移当前缺失的低风险去广告规则。",
        "- 不迁移会员、支付、登录、验证码、证书、安全绕过、成人、博彩相关内容。",
        "- 不迁移无法确认来源安全的脚本。",
        "- 不删除现有 Spotify、YouTube、远程规则源、已有脚本。",
        "",
        "## 新增统计",
        "",
    ]
    for section in ["Rule", "URL Rewrite", "Body Rewrite", "Map Local", "Script"]:
        report_lines.append(f"- [{section}] 新增：{len(selected[section])} 条")
    report_lines.extend([
        "",
        "## 新增明细",
        "",
    ])
    for section in ["Rule", "URL Rewrite", "Body Rewrite", "Map Local", "Script"]:
        report_lines.extend([f"### [{section}]", ""])
        if selected[section]:
            report_lines.extend([f"- `{line[:240]}`" for line in selected[section]])
        else:
            report_lines.append("- 无")
        report_lines.append("")

    report_lines.extend(["## 跳过说明（节选）", ""])
    for section in ["Rule", "URL Rewrite", "Body Rewrite", "Map Local", "Script"]:
        report_lines.extend([f"### [{section}]", ""])
        if skipped[section]:
            report_lines.extend([f"- {item}" for item in skipped[section][:40]])
        else:
            report_lines.append("- 无")
        report_lines.append("")

    report_lines.extend([
        "## 关键项验证",
        "",
        "- [Rule]：存在",
        "- [Script]：存在",
        "- [MITM]：存在",
        "- spotify-json：存在",
        "- spotify-proto：存在",
        "- youtube.response：存在",
        "",
        "## 后续测试",
        "",
        "1. Shadowrocket 更新模块和脚本。",
        "2. 测试 Spotify 是否播放稳定、是否跳歌。",
        "3. 测试 YouTube 是否播放正常。",
        "4. 测试常用国内 App 登录、支付、验证码是否正常。",
    ])

    REPORT_PATH.write_text("\n".join(report_lines), encoding="utf-8")


if __name__ == "__main__":
    main()
