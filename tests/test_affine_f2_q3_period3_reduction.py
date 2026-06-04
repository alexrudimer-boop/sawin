from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AffineF2Q3PeriodThreeReductionAuditTest(unittest.TestCase):
    def test_intertwiner_and_rank_pattern(self) -> None:
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_period3_reduction_audit.json")
            .read_text(encoding="utf-8")
        )
        self.assertEqual(report["max_arity"], 18)
        self.assertTrue(report["all_checked_generators_intertwine"])
        self.assertTrue(report["all_checked_kernels_fixed"])
        self.assertTrue(report["missing_dimension_pattern_holds"])

        for row in report["rank_rows"]:
            n = row["arity"]
            self.assertEqual(row["d_rank"], 2 * n - 2)
            self.assertEqual(row["d_kernel_dimension"], n + 2)
            self.assertEqual(row["invariant_observer_dimension"], n + 2)
            self.assertEqual(row["missing_dimension"], 2 if n % 3 == 0 else 0)

    def test_first_unresolved_arity_is_nine(self) -> None:
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_period3_reduction_audit.json")
            .read_text(encoding="utf-8")
        )
        missing_rows = [
            row["arity"]
            for row in report["rank_rows"]
            if row["missing_dimension"]
        ]
        self.assertEqual(missing_rows[:5], [3, 6, 9, 12, 15])


if __name__ == "__main__":
    unittest.main()
