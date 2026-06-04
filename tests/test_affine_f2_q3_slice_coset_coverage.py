from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AffineF2Q3SliceCosetCoverageAuditTest(unittest.TestCase):
    def test_all_cosets_are_slice_covered_through_arity_eight(self) -> None:
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_slice_coset_coverage_audit.json")
            .read_text(encoding="utf-8")
        )
        self.assertEqual(report["max_arity"], 8)
        self.assertTrue(report["all_checked_cosets_covered"])
        self.assertEqual([row["arity"] for row in report["rows"]], list(range(2, 9)))
        for row in report["rows"]:
            self.assertTrue(row["all_cosets_covered"])
            self.assertIsNone(row["first_uncovered_coset"])
        self.assertEqual(
            {
                row["arity"]: row["matching_slice_counts"]
                for row in report["rows"]
            },
            {
                2: {"0": 16, "1": 16, "t": 16, "t+1": 16},
                3: {"0": 8, "1": 24, "t": 24, "t+1": 24},
                4: {"0": 64, "1": 64, "t": 64, "t+1": 64},
                5: {"0": 128, "1": 128, "t": 128, "t+1": 128},
                6: {"0": 64, "1": 192, "t": 192, "t+1": 192},
                7: {"0": 512, "1": 512, "t": 512, "t+1": 512},
                8: {"0": 1024, "1": 1024, "t": 1024, "t+1": 1024},
            },
        )


if __name__ == "__main__":
    unittest.main()
