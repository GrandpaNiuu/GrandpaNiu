from __future__ import annotations

from collections import Counter, defaultdict
from datetime import datetime, timezone, timedelta
from pathlib import Path
import re

MODULE_PATH = Path("Ronghemokuai.sgmodule")
REPORT_PATH = Path("reports/module_refine_report.md")

REQUIRED_SECTIONS = [
    "Rule",
    "Header Rewrite",
    "Body Rewrite",
    "Map Local",
    "Script",
    "MITM",
]

ESSENTIAL_SCRIPT_PREFIXES = (
    "youtube.response",
    "spotify-upstream",
    "Spotify_remove_ads.js",
)

SAFE_MERGE_MAX_PATTERN_LEN = 1800
SAFE_MERGE_MAX_ITEMS = 6


def section_bounds(text: str, section_name: str) -> tuple[int, int, int]:
    match = re.search(rf"(?m)^\[{re.escape(section_name)}\]\s*$", text)
    if not match:
        raise RuntimeError(f"missing section: [{section_name}]")

    body_start = match.end()
    next_header = re.search(r"(?m)^\[[^\]]+\]\s*$", text[body_start:])
    body_end = body_start + next_header.start() if next_header else len(text)
    return match.start(), body_start, body_end


def validate_sections(text: str) -> list[str]:
    missing = []
    for section in REQUIRED_SECTIONS:
        try:
            section_bounds(text, section)
        except RuntimeError:
            missing.append(section)
    return missing


def split_fields(value: str) -> list[str]:
    # Conservative parser for Shadowrocket / Surge script lines.
    # This intentionally refuses complex lines with argument= before merging.
    return [part.strip() for part in value.split(",")]


def parse_script_line(line: str) -> dict[str, str] | None:
    if "script-path=" not in line:
        return None
    if "argument=" in line:
        return None

    match = re.match(r"^([A-Za-z0-9_.-]+)\s*=\s*(.+)$", line.strip())
    if not match:
        return None

    name = match.group(1).strip()
    if name.startswith(ESSENTIAL_SCRIPT_PREFIXES):
        return None

    fields = split_fields(match.group(2))
    parsed: dict[str, str] = {"__name__": name, "__line__": line}
    for field in fields:
        if "=" not in field:
            return None
        key, val = field.split("=", 1)
        parsed[key.strip()] = val.strip()

    if "pattern" not in parsed or "script-path" not in parsed or "type" not in parsed:
        return None

    return parsed


def signature(parsed: dict[str, str]) -> tuple[tuple[str, str], ...]:
    ignored = {"__name__", "__line__", "pattern"}
    return tuple(sorted((k, v) for k, v in parsed.items() if k not in ignored))


def build_script_line(name: str, parsed: dict[str, str], patterns: list[str]) -> str:
    ordered_keys = []
    for key in [
        "type",
        "pattern",
        "requires-body",
        "max-size",
        "binary-body-mode",
        "script-path",
        "timeout",
        "script-update-interval",
    ]:
        if key in parsed or key == "pattern":
            ordered_keys.append(key)

    for key in parsed:
        if key.startswith("__") or key == "pattern" or key in ordered_keys:
            continue
        ordered_keys.append(key)

    merged_pattern = "(?:" + "|".join(patterns) + ")"
    values = dict(parsed)
    values["pattern"] = merged_pattern

    fields = [f"{key}={values[key]}" for key in ordered_keys if key in values]
    return f"{name} = " + ",".join(fields)


def refine_script_section(text: str) -> tuple[str, list[str], int, int]:
    _, body_start, body_end = section_bounds(text, "Script")
    before = text[:body_start]
    body = text[body_start:body_end]
    after = text[body_end:]

    lines = body.splitlines()
    parsed_by_line: dict[int, dict[str, str]] = {}
    groups: dict[tuple[tuple[str, str], ...], list[int]] = defaultdict(list)

    for index, line in enumerate(lines):
        parsed = parse_script_line(line)
        if not parsed:
            continue
        parsed_by_line[index] = parsed
        groups[signature(parsed)].append(index)

    merge_heads: dict[int, list[int]] = {}
    skipped_groups = 0
    for indices in groups.values():
        if len(indices) < 2:
            continue

        patterns = [parsed_by_line[i]["pattern"] for i in indices]
        merged_pattern_len = len("(?:" + "|".join(patterns) + ")")
        if len(indices) > SAFE_MERGE_MAX_ITEMS or merged_pattern_len > SAFE_MERGE_MAX_PATTERN_LEN:
            skipped_groups += 1
            continue

        merge_heads[indices[0]] = indices

    consumed = set()
    new_lines: list[str] = []
    logs: list[str] = []

    for index, line in enumerate(lines):
        if index in consumed:
            continue

        if index in merge_heads:
            indices = merge_heads[index]
            first = parsed_by_line[index]
            names = [parsed_by_line[i]["__name__"] for i in indices]
            patterns = [parsed_by_line[i]["pattern"] for i in indices]
            new_name = first["__name__"] + "_merged"
            new_line = build_script_line(new_name, first, patterns)
            new_lines.append(f"# merged-script: fused {len(indices)} entries with the same script-path; originals={', '.join(names)}")
            new_lines.append(new_line)
            consumed.update(indices)
            logs.append(f"融合脚本：{', '.join(names)} -> {new_name}")
            continue

        new_lines.append(line)

    new_body = "\n".join(new_lines).rstrip("\n") + "\n"
    old_script_lines = sum(1 for line in lines if parse_script_line(line) or re.match(r"^[A-Za-z0-9_.-]+\s*=\s*", line.strip()))
    new_script_lines = sum(1 for line in new_lines if parse_script_line(line) or re.match(r"^[A-Za-z0-9_.-]+\s*=\s*", line.strip()))
    refined = before + "\n" + new_body + after
    if skipped_groups:
        logs.append(f"跳过过长或过大的可融合组：{skipped_groups} 组")
    return refined, logs, old_script_lines, new_script_lines


def count_duplicates(text: str) -> dict[str, int]:
    counters = {
        "script_names": Counter(),
        "rule_lines": Counter(),
        "mitm_hosts": Counter(),
    }

    current_section = ""
    for line in text.splitlines():
        header = re.match(r"^\[([^\]]+)\]\s*$", line.strip())
        if header:
            current_section = header.group(1)
            continue

        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if current_section == "Script":
            match = re.match(r"^([A-Za-z0-9_.-]+)\s*=", stripped)
            if match:
                counters["script_names"][match.group(1)] += 1
        elif current_section == "Rule":
            if stripped.startswith(("DOMAIN,", "DOMAIN-SUFFIX,", "DOMAIN-KEYWORD,", "IP-CIDR,", "URL-REGEX,", "RULE-SET,", "DOMAIN-SET,")):
                counters["rule_lines"][stripped] += 1
        elif current_section == "MITM" and stripped.startswith("hostname") and "%APPEND%" in stripped:
            hosts = stripped.split("%APPEND%", 1)[1]
            for host in [item.strip() for item in hosts.split(",") if item.strip()]:
                counters["mitm_hosts"][host] += 1

    return {
        "duplicate_script_names": sum(1 for v in counters["script_names"].values() if v > 1),
        "duplicate_rule_lines": sum(1 for v in counters["rule_lines"].values() if v > 1),
        "duplicate_mitm_hosts": sum(1 for v in counters["mitm_hosts"].values() if v > 1),
    }


def write_report(
    *,
    before_text: str,
    after_text: str,
    logs: list[str],
    old_script_lines: int,
    new_script_lines: int,
    duplicate_summary: dict[str, int],
) -> None:
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone(timedelta(hours=8))).strftime("%Y-%m-%d %H:%M:%S %z")

    required_status = []
    for marker in ["[Rule]", "[Script]", "[MITM]", "spotify-upstream", "Spotify_remove_ads.js", "youtube.response"]:
        required_status.append(f"- {marker}: {'存在' if marker in after_text else '缺失'}")

    content = [
        f"# 模块安全整理报告",
        "",
        f"生成时间：{today}",
        "",
        "## 本次原则",
        "",
        "- 不删除现有有效规则。",
        "- 不改写 Spotify、YouTube 核心脚本。",
        "- 不自动删除 script-path、RULE-SET、DOMAIN-SET。",
        "- 只融合同一 script-path 且执行参数一致的脚本条目。",
        "- 过长 pattern 或复杂 argument 脚本不融合。",
        "",
        "## 结果",
        "",
        f"- 整理前脚本条目数：{old_script_lines}",
        f"- 整理后脚本条目数：{new_script_lines}",
        f"- 减少显示脚本数：{max(0, old_script_lines - new_script_lines)}",
        "",
        "## 融合记录",
        "",
        *([f"- {item}" for item in logs] if logs else ["- 没有发现可安全融合的脚本组，因此未强行合并。"]),
        "",
        "## 重复统计",
        "",
        f"- 重复脚本名称组：{duplicate_summary['duplicate_script_names']}",
        f"- 重复规则行组：{duplicate_summary['duplicate_rule_lines']}",
        f"- 重复 MITM hostname 组：{duplicate_summary['duplicate_mitm_hosts']}",
        "",
        "## 关键项验证",
        "",
        *required_status,
        "",
        "## 自动化验证建议",
        "",
        "1. Shadowrocket 更新模块。",
        "2. 更新脚本。",
        "3. 测试 Spotify 播放、专辑页、歌手页。",
        "4. 测试 YouTube 首页、搜索、播放、Shorts。",
        "5. 测试淘宝、京东、微信、支付宝、银行类 App 登录和支付页。",
        "",
    ]
    REPORT_PATH.write_text("\n".join(content), encoding="utf-8")


def main() -> None:
    if not MODULE_PATH.exists():
        raise RuntimeError("Ronghemokuai.sgmodule not found")

    before = MODULE_PATH.read_text(encoding="utf-8")
    missing = validate_sections(before)
    if missing:
        raise RuntimeError("missing required sections: " + ", ".join(missing))

    after, logs, old_script_lines, new_script_lines = refine_script_section(before)

    for marker in ["spotify-upstream", "Spotify_remove_ads.js", "youtube.response", "[Rule]", "[Script]", "[MITM]"]:
        if marker not in after:
            raise RuntimeError(f"safety check failed, missing: {marker}")

    duplicate_summary = count_duplicates(after)

    MODULE_PATH.write_text(after, encoding="utf-8")
    write_report(
        before_text=before,
        after_text=after,
        logs=logs,
        old_script_lines=old_script_lines,
        new_script_lines=new_script_lines,
        duplicate_summary=duplicate_summary,
    )


if __name__ == "__main__":
    main()
