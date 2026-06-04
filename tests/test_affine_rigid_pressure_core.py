import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_affine_rigid_pressure_core_audit import build_report


class AffineRigidPressureCoreTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_affine_f2_dimension_two_has_no_rigid_pressure_core(self):
        dimension_two = self.report["dimension_two"]

        self.assertTrue(dimension_two["exact_exhaustive_affine_linear"])
        self.assertEqual(dimension_two["affine_ybe_count"], 481)
        self.assertEqual(dimension_two["terminal_survivor_count"], 24)
        self.assertEqual(dimension_two["structural_survivor_count"], 0)
        self.assertEqual(dimension_two["rigid_pressure_core_candidate_count"], 0)
        self.assertEqual(
            dimension_two["first_failed_filter_counts"],
            {
                "bidegenerate": 408,
                "noninvolutive": 49,
                "quotient_rigid": 24,
            },
        )

    def test_named_affine_f2_dimension_three_pressure_row_is_not_rigid(self):
        pressure_row = self.report["dimension_three_named_pressure_row"]

        self.assertTrue(pressure_row["terminal_filter_survives"])
        self.assertFalse(pressure_row["observer_rigid"])
        self.assertFalse(pressure_row["subsolution_rigid"])
        self.assertFalse(pressure_row["rigid_pressure_core_candidate"])


if __name__ == "__main__":
    unittest.main()
