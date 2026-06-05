import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.run_stage_pipeline_frontier_audit import build_report


class StagePipelineFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report()

    def test_exact_size_three_frontier_has_no_noninvolutive_completion(self):
        frontiers = self.report["stage_a_frontiers"]
        rows = {row["name"]: row for row in self.report["rows"]}

        self.assertFalse(frontiers["exact_size_3"]["truncated"])
        self.assertEqual(frontiers["exact_size_3"]["canonical_count"], 1)
        self.assertEqual(rows["row_exact_size3_u0"]["stage_b"]["accepted_count"], 0)
        self.assertEqual(rows["row_exact_size3_u0"]["gac_stage_b"]["accepted_count"], 0)
        self.assertFalse(rows["row_exact_size3_u0"]["stage_b"]["truncated"])
        self.assertFalse(rows["row_exact_size3_u0"]["gac_stage_b"]["truncated"])

    def test_budgeted_size_four_frontier_is_clearly_nonexhaustive(self):
        frontiers = self.report["stage_a_frontiers"]
        rows = {row["name"]: row for row in self.report["rows"]}

        self.assertTrue(frontiers["budget_size_4"]["truncated"])
        self.assertEqual(frontiers["budget_size_4"]["emitted_count"], 1)
        self.assertEqual(rows["row_budget_size4_u0"]["stage_b"]["accepted_count"], 0)
        self.assertEqual(rows["row_budget_size4_u0"]["gac_stage_b"]["accepted_count"], 0)

    def test_known_affine_type_a_pipeline_reaches_rigid_filter(self):
        rows = {row["name"]: row for row in self.report["rows"]}
        affine = rows["known_affine_type_a"]

        self.assertTrue(affine["bucket_csp"]["locally_consistent"])
        self.assertEqual(affine["stage_b"]["accepted_count"], 1)
        self.assertEqual(affine["gac_stage_b"]["accepted_count"], 1)
        self.assertEqual(len(affine["solution_rows"]), 1)
        self.assertEqual(
            affine["solution_rows"][0]["rigid_pressure_core_row"]["first_failed_filter"],
            "quotient_rigid",
        )


if __name__ == "__main__":
    unittest.main()
