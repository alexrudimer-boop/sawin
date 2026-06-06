import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_fixed_arity_rack_cofinality_audit import build_report


class FixedArityRackCofinalityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_fixed_arity_theorem_uses_conjugation_rack_detector(self):
        theorem = self.report["fixed_arity_theorem"]
        literature = self.report["literature_input"]

        self.assertIn("theta:B_n -> H", theorem["statement"])
        self.assertIn("pure braid", literature["name"])
        self.assertIn("conjugation rack", theorem["detector"])
        self.assertTrue(
            any("N_P" in step and "P_n" in step for step in theorem["proof_steps"])
        )
        self.assertTrue(
            any("strand permutation" in step for step in theorem["proof_steps"])
        )
        self.assertTrue(
            any("Artin convention" in step for step in theorem["proof_steps"])
        )
        self.assertTrue(
            any("quotient free generators" in step for step in theorem["proof_steps"])
        )

    def test_sharpened_negative_condition_is_unbounded_in_arity(self):
        condition = self.report["sharpened_negative_condition"]

        self.assertEqual(
            condition["new_condition"],
            "forall m forall N exists n>N with N_{m,n}(X) != 1",
        )
        self.assertTrue(any("bounded arities" in step for step in condition["proof"]))

    def test_asymptotic_endpoint_is_strictly_smaller_than_rigid_core_exclusion(self):
        endpoint = self.report["asymptotic_endpoint"]

        self.assertIn("asymptotically rack-invisible", endpoint["statement"])
        self.assertIn("minimal counterexamples", endpoint["why_it_implies_sawin_yes"])
        self.assertIn(
            "bounded in arity",
            endpoint["strictly_smaller_than_rigid_core_exclusion"],
        )

    def test_singular_coordinate_filter_records_everywhere_singularity(self):
        singular = self.report["singular_coordinate_filter"]

        self.assertIn("every L_x and every R_x non-bijective", singular["statement"])
        self.assertTrue(any("U_L" in step for step in singular["proof_steps"]))
        self.assertIn("reject", singular["finite_table_filter"])


if __name__ == "__main__":
    unittest.main()
