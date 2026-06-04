import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_inert_observer_rack_factor_audit import build_report


class InertObserverRackFactorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()
        cls.rows = {row["name"]: row for row in cls.report["rows"]}

    def test_observer_product_s3_passes_pointwise_factor_theorem(self):
        row = self.rows["observer_product_s3_conjugation"]
        audit = row["audit"]

        self.assertTrue(audit["finite_conditions_hold"])
        self.assertIsNone(audit["observer_failure"])
        self.assertIsNone(audit["rack_factor_failure"])
        self.assertIsNone(audit["injectivity_collision"])
        self.assertEqual(audit["kernel_conclusion"], "ker rho^X_n = ker rho^Y_n for every n")

    def test_type_a_fails_because_it_needs_sequential_gauge(self):
        row = self.rows["size4_affine_type_a_naive_pointwise"]
        audit = row["audit"]

        self.assertFalse(audit["finite_conditions_hold"])
        self.assertIsNone(audit["observer_failure"])
        self.assertIsNotNone(audit["rack_factor_failure"])
        self.assertIn("sequential", row["expectation"])

    def test_type_b_fails_because_flip_across_routes_observer(self):
        row = self.rows["size4_type_b_flip_across_naive_tag"]
        audit = row["audit"]

        self.assertFalse(audit["finite_conditions_hold"])
        self.assertIsNotNone(audit["observer_failure"])
        self.assertIn("route", row["expectation"])

    def test_theorem_is_recorded_as_strict_positive_branch(self):
        self.assertIn("o:X->I", self.report["theorem"])
        self.assertIn("strict positive branch", self.report["conclusion"])
        self.assertTrue(self.report["next_prompt"].endswith("_ask_now.md"))


if __name__ == "__main__":
    unittest.main()
