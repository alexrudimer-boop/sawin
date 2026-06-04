import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_derived_quasirack_route_boundary import build_report


class DerivedQuasirackRouteBoundaryTests(unittest.TestCase):
    def test_cover_lemma_records_sufficient_domination_branch(self):
        report = build_report()
        cover = report["cover_lemma"]

        self.assertIn("homomorphic image", cover["statement"])
        self.assertIn("finite rack", cover["statement"])
        self.assertEqual(cover["status"], "sufficient but not known to be necessary")
        self.assertTrue(any("Transitivity" in step for step in cover["proof_steps"]))

    def test_derived_quasirack_target_records_kernel_comparison_goal(self):
        report = build_report()
        target = report["derived_quasirack_target"]

        self.assertIn("ker rho", target["kernel_target"])
        self.assertIn("Plonka", target["rack_domination_target"])
        self.assertIn("tetrahedral", target["affine_f2_q3_model"])
        self.assertTrue(report["next_prompt"].endswith("_ask_now.md"))

    def test_quasirack_gap_example_records_size_three_failure(self):
        report = build_report()
        gap = report["quasirack_gap_example"]

        self.assertEqual(gap["name"], "three_point_nonaffine_involutive_r1")
        self.assertEqual(gap["lambda_rows"]["lambda_0"], (0, 0, 2))
        self.assertIn("commutation condition fails", gap["quasi_left_nondegenerate_failure"])
        self.assertIn("two-point flip rack", gap["domination_status"])

    def test_noninvolutive_observer_product_gap_records_broader_positive_branch(self):
        report = build_report()
        gap = report["noninvolutive_observer_product_gap"]

        self.assertEqual(gap["name"], "observer_product_s3_conjugation")
        self.assertIn("S_3", gap["table_formula"])
        self.assertTrue(any("non-involutive" in item for item in gap["properties"]))
        self.assertTrue(
            any("rack-kernel equivalent" in item for item in gap["properties"])
        )
        self.assertIn("size5-6", report["next_prompt"])


if __name__ == "__main__":
    unittest.main()
