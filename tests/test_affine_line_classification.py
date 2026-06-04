import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_affine_line_classification_audit import build_report


class AffineLineClassificationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_bidegenerate_affine_line_solution_is_forced_identity(self):
        classification = self.report["bidegenerate_classification"]

        self.assertEqual(
            classification["conclusion"],
            "the only bidegenerate bijective affine-line YBE solution is r(x,y)=(x,y)",
        )
        self.assertIn("a=1", classification["deduction"][0])
        self.assertIn("e=1", classification["deduction"][1])
        self.assertIn("f=0", classification["deduction"][2])
        self.assertIn("c=0", classification["deduction"][3])

    def test_finite_prime_spot_checks_have_only_identity_bidegenerate_rows(self):
        checks = self.report["finite_prime_checks"]

        expected_counts = {
            "F_2": 5,
            "F_3": 31,
            "F_5": 221,
            "F_7": 715,
        }
        for field, count in expected_counts.items():
            with self.subTest(field=field):
                self.assertEqual(checks[field]["affine_ybe_count"], count)
                self.assertEqual(checks[field]["terminal_survivor_count"], 0)
                self.assertEqual(
                    checks[field]["bidegenerate_bijective_ybe_row_count"], 1
                )
                self.assertTrue(checks[field]["all_bidegenerate_rows_identity"])

    def test_ybe_equation_list_contains_degeneracy_forcing_equations(self):
        equations = set(self.report["ybe_equations"])

        self.assertIn("a(a+bd-1)=0", equations)
        self.assertIn("e(1-e-bd)=0", equations)
        self.assertIn("e(cd+f)=0", equations)


if __name__ == "__main__":
    unittest.main()
