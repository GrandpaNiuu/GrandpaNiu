from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "generate_mitm_reject_risk_ledger_test",
    ROOT / "tools" / "generate_mitm_reject_risk_ledger.py",
)
assert SPEC and SPEC.loader
ledger = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = ledger
SPEC.loader.exec_module(ledger)

FALSE_POSITIVE_SPEC = importlib.util.spec_from_file_location(
    "generate_false_positive_review_report_test",
    ROOT / "tools" / "generate_false_positive_review_report.py",
)
assert FALSE_POSITIVE_SPEC and FALSE_POSITIVE_SPEC.loader
false_positive = importlib.util.module_from_spec(FALSE_POSITIVE_SPEC)
sys.modules[FALSE_POSITIVE_SPEC.name] = false_positive
FALSE_POSITIVE_SPEC.loader.exec_module(false_positive)


class MitmRejectRiskLedgerTests(unittest.TestCase):
    def test_mitm_output_status_distinguishes_exact_covered_and_source_only(self) -> None:
        optimized = {"api.example.com", "*.covered.example"}
        removals = {"deep.covered.example": "*.covered.example"}

        self.assertEqual("final-exact", ledger.mitm_output_status("API.Example.com", optimized, removals))
        self.assertEqual(
            "final-covered-by:*.covered.example",
            ledger.mitm_output_status("deep.covered.example", optimized, removals),
        )
        self.assertEqual("source-only", ledger.mitm_output_status("unused.example", optimized, removals))

    def test_reject_output_status_is_exact_only_and_does_not_guess(self) -> None:
        final_lines = {"DOMAIN,ads.example,REJECT,pre-matching"}
        self.assertEqual(
            "final-exact",
            ledger.reject_output_status("DOMAIN,ads.example,REJECT,pre-matching", final_lines),
        )
        self.assertEqual(
            "source-only-or-compiled",
            ledger.reject_output_status("DOMAIN,api.example,REJECT,pre-matching", final_lines),
        )

    def test_false_positive_queue_preserves_output_status_column(self) -> None:
        rows = false_positive.parse_risk_rows(
            "| MITM | high | Login | `source.conf:2` | `final-exact` | `login.example` | sensitive |"
        )

        self.assertEqual(1, len(rows))
        self.assertEqual("final-exact", rows[0]["output_status"])
        self.assertEqual("login.example", rows[0]["entry"])

    def test_false_positive_queue_preserves_escaped_regex_alternation(self) -> None:
        rows = false_positive.parse_risk_rows(
            r"| REJECT | medium | API | `source.conf:3` | `final-exact` | `^https?://(ads\|promo)\.example/` | review |"
        )

        self.assertEqual(1, len(rows))
        self.assertEqual(r"^https?://(ads|promo)\.example/", rows[0]["entry"])
        self.assertEqual("review", rows[0]["reason"])


if __name__ == "__main__":
    unittest.main()
