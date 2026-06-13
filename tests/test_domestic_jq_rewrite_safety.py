import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BODY_REWRITE = ROOT / "Rewrite" / "Sources" / "Body-Rewrite.conf"
URL_REWRITE = ROOT / "Rewrite" / "Sources" / "URL-Rewrite.conf"
JD_SOURCE = ROOT / "Rewrite" / "Sources" / "Apps" / "jd.conf"
CANDIDATE_REPORT = ROOT / "reports" / "jq_rewrite_candidate_report.md"

SAFE_SECTION_RE = re.compile(
    r"# === Domestic App Safe JQ Reinforcement START ===\n(?P<body>.*?)\n# === Domestic App Safe JQ Reinforcement END ===",
    re.S,
)
ALLOWED_SAFE_HOSTS = (
    "api\\.m\\.jd\\.com",
    "mapi\\.dianping\\.com",
    "m\\.dianping\\.com",
)
FORBIDDEN_SAFE_TOKENS = re.compile(
    r"vip|member|pay|login|token|cookie|auth|password|orderTrackBusiness|myOrderInfo",
    re.I,
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


class DomesticJqRewriteSafetyTests(unittest.TestCase):
    def safe_section(self) -> str:
        match = SAFE_SECTION_RE.search(read(BODY_REWRITE))
        self.assertIsNotNone(match, "Body-Rewrite.conf must document the domestic safe JQ batch")
        return match.group("body")

    def test_jd_remote_script_is_converted_to_endpoint_scoped_jq(self) -> None:
        jd_source = read(JD_SOURCE)
        self.assertNotIn("JD_remove_ads.js", jd_source)
        self.assertNotIn("移除京东广告 = type=http-response", jd_source)

        section = self.safe_section()
        self.assertIn("api\\.m\\.jd\\.com\\/client\\.action\\?functionId=(deliverLayer|getTabHomeInfo|personinfoBusiness|start|welcomeHome)", section)
        self.assertNotRegex(section, re.compile(r"orderTrackBusiness|myOrderInfo", re.I))

    def test_dianping_high_level_rejects_are_replaced_with_jq(self) -> None:
        url_rewrite = read(URL_REWRITE)
        self.assertNotIn("m\\.dianping\\.com\\/mapi\\/mgw\\/growth\\/queryhaima - reject-dict", url_rewrite)
        self.assertNotIn("mapi\\.dianping\\.com\\/mapi\\/mgw\\/growth\\/clipboardquery - reject-dict", url_rewrite)
        self.assertNotIn("mapi\\.dianping\\.com\\/mapi\\/operating\\/(?:indexopsmodules|loadsplashconfig) - reject", url_rewrite)

        section = self.safe_section()
        self.assertIn("mapi\\.dianping\\.com\\/mapi\\/operating\\/(indexopsmodules|loadsplashconfig)", section)
        self.assertIn("m\\.dianping\\.com\\/mapi\\/mgw\\/growth\\/queryhaima", section)
        self.assertIn("mapi\\.dianping\\.com\\/mapi\\/mgw\\/growth\\/clipboardquery", section)

    def test_new_safe_jq_batch_is_host_scoped_and_avoids_sensitive_fields(self) -> None:
        section = self.safe_section()
        jq_lines = [line for line in section.splitlines() if line.startswith("http-response-jq ")]
        self.assertGreaterEqual(len(jq_lines), 3)
        for line in jq_lines:
            self.assertTrue(
                any(host in line for host in ALLOWED_SAFE_HOSTS),
                f"JQ line must be scoped to an approved domestic app host: {line}",
            )
            self.assertNotIn("^https?:\\/\\/.*", line)
            self.assertNotRegex(line, FORBIDDEN_SAFE_TOKENS)

    def test_jq_candidate_report_records_conversion_decisions(self) -> None:
        report = read(CANDIDATE_REPORT)
        self.assertIn("| 京东 |", report)
        self.assertIn("JD_remove_ads.js", report)
        self.assertIn("已改为 JQ", report)
        self.assertIn("| 大众点评 |", report)
        self.assertIn("reject 改为 JQ", report)
        self.assertIn("| Spotify / YouTube / Bilibili protobuf |", report)
        self.assertIn("不适合 JQ", report)


if __name__ == "__main__":
    unittest.main()
