import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_size4_nonaffine_frontier_audit import build_report


class SizeFourNonAffineFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()
        cls.rows = {row["name"]: row for row in cls.report["rows"]}

    def test_type_a_is_affine_and_degenerate_noninvolutive(self):
        row = self.rows["size4_type_a_affine_f2"]

        self.assertTrue(row["is_ybe"])
        self.assertFalse(row["is_involutive"])
        self.assertTrue(row["coordinate_degeneracy"]["left_degenerate"])
        self.assertTrue(row["coordinate_degeneracy"]["right_degenerate"])
        self.assertTrue(
            row["affine_f2_square_model"][
                "is_affine_over_f2_square_up_to_relabeling"
            ]
        )
        self.assertIn("cyclic rack", row["mechanism"])

    def test_type_b_is_nonaffine_but_closed_by_flip_across(self):
        row = self.rows["size4_type_b_flip_across_nonaffine"]

        self.assertTrue(row["is_ybe"])
        self.assertFalse(row["is_involutive"])
        self.assertTrue(row["coordinate_degeneracy"]["left_degenerate"])
        self.assertTrue(row["coordinate_degeneracy"]["right_degenerate"])
        self.assertFalse(
            row["affine_f2_square_model"][
                "is_affine_over_f2_square_up_to_relabeling"
            ]
        )
        self.assertTrue(row["has_flip_across_decomposition"])
        self.assertTrue(row["active_certificate"]["finite_conditions_hold"])
        self.assertIsNone(row["active_certificate"]["injectivity_witness"])

    def test_remaining_gap_is_outside_type_a_and_type_b(self):
        self.assertIn("outside the Type A", self.report["remaining_gap"])
        self.assertTrue(self.report["next_prompt"].endswith("_ask_now.md"))


if __name__ == "__main__":
    unittest.main()
