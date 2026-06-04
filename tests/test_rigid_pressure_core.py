import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_rigid_pressure_core_audit import build_report


class RigidPressureCoreTests(unittest.TestCase):
    def test_size_three_and_named_pressure_rows_have_no_core_candidate(self):
        report = build_report()

        self.assertEqual(report["size_3"]["solution_count"], 73)
        self.assertEqual(report["size_3"]["terminal_survivor_count"], 0)
        self.assertEqual(report["size_3"]["structural_survivor_count"], 0)
        self.assertEqual(report["size_3"]["candidate_count"], 0)
        self.assertEqual(report["representative_candidate_count"], 0)

        representatives = {row["name"]: row for row in report["representatives"]}
        self.assertEqual(
            representatives["size4_affine_type_a"]["first_failed_filter"],
            "quotient_rigid",
        )
        self.assertEqual(
            representatives["size4_type_b_flip_across"]["first_failed_filter"],
            "not_flip_across",
        )
        self.assertFalse(
            representatives["affine_f2_hidden_cyclic_pressure_row"][
                "observer_rigid"
            ]
        )


if __name__ == "__main__":
    unittest.main()
