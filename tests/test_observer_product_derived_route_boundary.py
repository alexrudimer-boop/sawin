import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_observer_product_derived_route_boundary import build_report


class ObserverProductDerivedRouteBoundaryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_example_is_everywhere_degenerate_noninvolutive_ybe(self):
        report = self.report

        self.assertTrue(report["is_ybe"])
        self.assertFalse(report["is_involutive"])
        self.assertTrue(report["everywhere_left_singular"])
        self.assertTrue(report["everywhere_right_singular"])
        self.assertEqual(set(report["lambda_image_sizes"]), {6})
        self.assertEqual(set(report["rho_image_sizes"]), {6})

    def test_fixed_point_counts_obstruct_abelian_affine_model(self):
        counts = set(self.report["lambda_fixed_point_counts"].values())

        self.assertEqual(counts, {2, 3, 6})
        self.assertIn("affine model over an abelian group", self.report["nonaffine_reason"])

    def test_derived_and_quasi_derived_routes_fail(self):
        report = self.report
        witness = report["quasi_left_failure_witness"]

        self.assertIn("undefined", report["classical_derived_status"])
        self.assertFalse(witness["commutes"])
        self.assertNotEqual(
            witness["lambda_x0_lambda_y_z"],
            witness["lambda_y_lambda_x0_z"],
        )

    def test_solution_splits_as_conjugation_rack_plus_observer(self):
        report = self.report

        self.assertTrue(report["split_equivariance_check"]["checked"])
        self.assertIsNone(report["split_equivariance_check"]["first_failure"])
        self.assertIn("kernels are equal", report["all_arity_kernel_statement"])
        self.assertTrue(report["next_prompt"].endswith("_ask_now.md"))


if __name__ == "__main__":
    unittest.main()
