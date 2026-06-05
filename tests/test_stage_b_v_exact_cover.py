import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.run_sequential_primitivity_frontier_audit import affine_f2_type_a_solution
from tools.run_stage_b_v_exact_cover_audit import build_report
from ybe_domination import identity_solution
from ybe_domination.stage_a_u_arrays import (
    solution_from_uv_arrays,
    stage_b_v_exact_cover_audit,
    uv_arrays_from_solution,
    uv_is_involutive,
    uv_pair_orthogonal,
    uv_y2_y3_hold,
    v_columns_singular,
)


class StageBVExactCoverTests(unittest.TestCase):
    def test_identity_u_has_unique_column_singular_ybe_completion(self):
        u_array, v_array = uv_arrays_from_solution(identity_solution((0, 1, 2)))
        audit = stage_b_v_exact_cover_audit(
            u_array,
            require_column_singular=True,
            max_examples=None,
        )

        self.assertEqual(audit.exact_cover_count, 1)
        self.assertEqual(audit.column_singular_count, 1)
        self.assertEqual(audit.y2_y3_count, 1)
        self.assertEqual(audit.accepted_count, 1)
        self.assertIn(v_array, audit.examples)

    def test_affine_type_a_u_recovers_unique_noninvolutive_completion(self):
        solution = affine_f2_type_a_solution()
        u_array, v_array = uv_arrays_from_solution(solution)

        self.assertTrue(uv_pair_orthogonal(u_array, v_array))
        self.assertTrue(v_columns_singular(v_array))
        self.assertTrue(uv_y2_y3_hold(u_array, v_array))
        self.assertFalse(uv_is_involutive(u_array, v_array))

        audit = stage_b_v_exact_cover_audit(
            u_array,
            require_column_singular=True,
            require_noninvolutive=True,
            max_examples=None,
        )

        self.assertEqual(audit.exact_cover_count, 2)
        self.assertEqual(audit.column_singular_count, 2)
        self.assertEqual(audit.y2_y3_count, 2)
        self.assertEqual(audit.noninvolutive_count, 1)
        self.assertEqual(audit.accepted_count, 1)
        self.assertIn(v_array, audit.examples)
        self.assertTrue(solution_from_uv_arrays(u_array, v_array).is_ybe())

    def test_node_budget_reports_truncation(self):
        u_array, _v_array = uv_arrays_from_solution(affine_f2_type_a_solution())
        audit = stage_b_v_exact_cover_audit(
            u_array,
            require_column_singular=True,
            max_nodes=1,
        )

        self.assertTrue(audit.truncated)
        self.assertEqual(audit.node_count, 1)
        self.assertEqual(audit.accepted_count, 0)

    def test_generated_stage_b_report_records_regressions(self):
        report = build_report()
        rows = {row["name"]: row for row in report["rows"]}

        self.assertIn("bucket domain", report["constraints"][0])
        self.assertTrue(rows["identity_3"]["actual_v_recovered"])
        self.assertTrue(rows["size4_affine_type_a"]["actual_v_recovered"])
        self.assertEqual(
            rows["size4_affine_type_a"]["audit"]["noninvolutive_count"],
            1,
        )
        self.assertEqual(
            rows["size4_affine_type_a"]["audit"]["accepted_count"],
            1,
        )


if __name__ == "__main__":
    unittest.main()
