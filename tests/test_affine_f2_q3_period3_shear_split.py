from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AffineF2Q3PeriodThreeShearSplitAuditTest(unittest.TestCase):
    def test_period_three_shear_is_nonsplit(self) -> None:
        report = json.loads(
            (
                ROOT
                / "proofs"
                / "affine_f2_q3_period3_shear_split_audit.json"
            ).read_text(encoding="utf-8")
        )
        self.assertEqual(report["max_arity"], 30)
        self.assertTrue(report["all_checked_hidden_spaces_fixed"])
        self.assertTrue(report["all_checked_shears_nonsplit"])
        self.assertEqual(
            [row["arity"] for row in report["rows"]],
            [3, 6, 9, 12, 15, 18, 21, 24, 27, 30],
        )
        for row in report["rows"]:
            self.assertEqual(row["hidden_dimension"], 2)
            self.assertFalse(row["section_coboundary_exists"])


if __name__ == "__main__":
    unittest.main()
