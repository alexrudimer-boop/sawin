import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from tools.run_size5_6_component_stage_b_frontier_audit import build_report


class SizeFiveSixComponentStageBFrontierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.report = build_report(
            stage_a_max_nodes=20,
            stage_a_max_examples=1,
            max_component_solutions=10,
            max_v_examples=1,
            max_bucket_permutations=1,
        )

    def test_report_runs_bounded_size_five_and_six_frontiers(self):
        rows = {row["size"]: row for row in self.report["rows"]}

        self.assertEqual(set(rows), {5, 6})
        self.assertEqual(rows[5]["stage_a"]["emitted_count"], 1)
        self.assertEqual(rows[6]["stage_a"]["emitted_count"], 1)
        self.assertTrue(rows[5]["stage_a"]["truncated"])
        self.assertTrue(rows[6]["stage_a"]["truncated"])

    def test_stage_b_skip_is_explicit_under_low_permutation_bound(self):
        for row in self.report["rows"]:
            u_row = row["u_rows"][0]
            self.assertIsNotNone(u_row["stage_b_skipped_reason"])
            self.assertIn("bucket permutation", u_row["stage_b_skipped_reason"])

    def test_artifact_points_to_current_prompt(self):
        self.assertTrue(
            self.report["next_prompt"].endswith(
                "2026-06-04-everywhere-singular-rigid-core-theory_ask_now.md"
            )
        )


if __name__ == "__main__":
    unittest.main()
