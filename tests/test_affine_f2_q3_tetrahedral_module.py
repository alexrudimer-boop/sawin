from __future__ import annotations

import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class AffineF2Q3TetrahedralModuleAuditTest(unittest.TestCase):
    def test_native_module_orders_match_through_arity_five(self) -> None:
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_tetrahedral_module_audit.json")
            .read_text(encoding="utf-8")
        )
        self.assertEqual(
            [
                row["rack24_image_order"]
                for row in report["rows"]
            ],
            [3, 24, 648, 77760],
        )
        for row in report["rows"]:
            self.assertFalse(row["truncated"])
            self.assertTrue(row["all_orders_match"])
            self.assertEqual(row["rack24_image_order"], row["x_image_order"])
            self.assertEqual(
                row["rack24_image_order"],
                row["x_fibre_affine_image_order"],
            )
            self.assertEqual(
                row["rack24_image_order"],
                row["rack24_x_joint_order"],
            )
            self.assertEqual(
                row["rack24_image_order"],
                row["rack24_fibre_joint_order"],
            )
            self.assertEqual(
                row["rack24_image_order"],
                row["fibre_x_joint_order"],
            )

    def test_rack24_alexander_model_matches_representative_table(self) -> None:
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_tetrahedral_module_audit.json")
            .read_text(encoding="utf-8")
        )
        self.assertEqual(
            report["rack24_alexander_model"]["operation_table_rows"],
            [
                [0, 2, 3, 1],
                [3, 1, 0, 2],
                [1, 3, 2, 0],
                [2, 0, 1, 3],
            ],
        )
        self.assertEqual(report["rack24_alexander_model"]["T_row_masks"], [2, 3])


if __name__ == "__main__":
    unittest.main()
