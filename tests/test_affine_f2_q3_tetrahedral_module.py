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

    def test_x_linearization_and_slice_conjugacy_checks(self) -> None:
        report = json.loads(
            (ROOT / "proofs" / "affine_f2_q3_tetrahedral_module_audit.json")
            .read_text(encoding="utf-8")
        )
        self.assertEqual(
            [
                row["arity"]
                for row in report["x_linearized_model"]["linearization_rows"]
                if row["all_generators_linearized"]
            ],
            list(range(2, 11)),
        )
        self.assertEqual(
            report["x_linearized_model"]["local_matrix_rows"],
            [
                "010100",
                "100100",
                "000001",
                "001101",
                "110110",
                "110101",
            ],
        )
        conjugacy_rows = report["invariant_slice_model"]["conjugacy_rows"]
        self.assertEqual([row["arity"] for row in conjugacy_rows], list(range(2, 11)))
        self.assertTrue(all(row["has_matching_slice"] for row in conjugacy_rows))
        self.assertEqual(
            {
                row["arity"]: row["matching_slice_constant_names"]
                for row in conjugacy_rows
            },
            {
                2: ["0", "1", "t", "t+1"],
                3: ["1", "t", "t+1"],
                4: ["0", "1", "t", "t+1"],
                5: ["0", "1", "t", "t+1"],
                6: ["0"],
                7: ["0", "1", "t", "t+1"],
                8: ["0", "1", "t", "t+1"],
                9: ["1", "t", "t+1"],
                10: ["0", "1", "t", "t+1"],
            },
        )


if __name__ == "__main__":
    unittest.main()
