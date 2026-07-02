import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_module  # noqa: E402


class ModuleCompactionTests(unittest.TestCase):
    def test_url_rewrite_compaction_preserves_reject_suffix(self) -> None:
        body = "\n".join(
            [
                r"^https?:\/\/a\.example\.com\/ad - reject",
                r"^https?:\/\/b\.example\.com\/ad - reject",
                r"^https?:\/\/c\.example\.com\/ad - reject-dict",
                r"^https?:\/\/link\.example\.com\/x http://$1 302",
            ]
        )

        compacted = build_module.compact_url_rewrite(body)

        self.assertIn(r"(?:^https?:\/\/a\.example\.com\/ad)|(?:^https?:\/\/b\.example\.com\/ad) - reject", compacted)
        self.assertIn(r"(?:^https?:\/\/c\.example\.com\/ad) - reject-dict", compacted)
        self.assertIn(r"^https?:\/\/link\.example\.com\/x http://$1 302", compacted)
        self.assertNotIn(r"\/ad reject", compacted)

    def test_body_rewrite_compaction_only_merges_identical_operations(self) -> None:
        body = "\n".join(
            [
                r"http-response ^https?:\/\/a\.example\.com\/api ad_list []",
                r"http-response ^https?:\/\/b\.example\.com\/api ad_list []",
                r"http-response ^https?:\/\/c\.example\.com\/api ad_list {}",
            ]
        )

        compacted = build_module.compact_body_rewrite(body)

        self.assertIn(r"http-response (?:^https?:\/\/a\.example\.com\/api)|(?:^https?:\/\/b\.example\.com\/api) ad_list []", compacted)
        self.assertIn(r"http-response (?:^https?:\/\/c\.example\.com\/api) ad_list {}", compacted)

    def test_map_local_compaction_only_merges_identical_responses(self) -> None:
        body = "\n".join(
            [
                r"^https?:\/\/a\.example\.com\/ad data-type=text data=\"{}\" status-code=200",
                r"^https?:\/\/b\.example\.com\/ad data-type=text data=\"{}\" status-code=200",
                r"^https?:\/\/c\.example\.com\/ad data-type=text data=\"[]\" status-code=200",
            ]
        )

        compacted = build_module.compact_map_local(body)

        self.assertIn(
            r"(?:^https?:\/\/a\.example\.com\/ad)|(?:^https?:\/\/b\.example\.com\/ad) data-type=text data=\"{}\" status-code=200",
            compacted,
        )
        self.assertIn(r"(?:^https?:\/\/c\.example\.com\/ad) data-type=text data=\"[]\" status-code=200", compacted)


if __name__ == "__main__":
    unittest.main()
