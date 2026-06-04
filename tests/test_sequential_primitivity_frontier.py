import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_sequential_primitivity_frontier_audit import build_report


class SequentialPrimitivityFrontierTests(unittest.TestCase):
    def test_size_three_and_pressure_rows_have_no_frontier_candidate(self):
        report = build_report()

        self.assertEqual(report["size_3"]["solution_count"], 73)
        self.assertEqual(report["size_3"]["candidate_count"], 0)
        self.assertEqual(report["representative_candidate_count"], 0)
        self.assertEqual(report["candidate_names"], [])

        representatives = {row["name"]: row for row in report["representatives"]}
        self.assertTrue(
            representatives["size4_affine_type_a"]["finite_conditions_hold"]
        )
        self.assertTrue(
            representatives["size4_type_b_flip_across"]["finite_conditions_hold"]
        )
        self.assertTrue(
            representatives["affine_f2_hidden_cyclic_pressure_row"][
                "finite_conditions_hold"
            ]
        )


if __name__ == "__main__":
    unittest.main()
