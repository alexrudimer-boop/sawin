from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AffineF2Q3AritySixMatrixGroupAuditTest(unittest.TestCase):
    def test_arity_six_joint_kernel_is_trivial(self) -> None:
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_arity6_matrix_group_audit.json")
            .read_text(encoding="utf-8")
        )
        self.assertEqual(report["arity"], 6)
        self.assertEqual(report["orders"]["Y"], 39_813_120)
        self.assertEqual(report["orders"]["X"], 39_813_120)
        self.assertEqual(report["orders"]["joint"], 39_813_120)
        self.assertTrue(report["all_orders_equal"])
        self.assertTrue(report["joint_kernel_trivial"])
        self.assertEqual(report["pro_expected_unitary_order"], 41_057_280)


if __name__ == "__main__":
    unittest.main()
