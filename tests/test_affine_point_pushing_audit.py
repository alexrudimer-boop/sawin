import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_audit import affine_solution  # noqa: E402
from ybe_domination import (  # noqa: E402
    branch_tags,
    pure_generator_order_profile,
    pure_subgroup_growth_profile,
)


class AffineF2PointPushingAuditTests(unittest.TestCase):
    def test_untagged_affine_row_has_bounded_point_pushing_generators(self):
        matrix = (
            (0, 0, 0, 1),
            (1, 1, 0, 1),
            (1, 0, 1, 1),
            (1, 0, 0, 0),
        )
        offset = (0, 0, 1, 1)
        solution = affine_solution(matrix, offset, 2)

        self.assertTrue(solution.is_ybe())
        self.assertEqual(branch_tags(solution), ())

        profile = pure_generator_order_profile(solution, max_q=5)
        self.assertEqual(
            tuple(row.max_order for row in profile),
            (2, 2, 2, 2),
        )
        self.assertEqual(
            tuple(row.generator_orders for row in profile),
            ((2,), (2, 2), (2, 2, 2), (2, 2, 2, 2)),
        )

        growth = pure_subgroup_growth_profile(
            solution,
            max_q=5,
            max_subgroup_size=100_000,
            max_tuple_count=1024,
        )
        self.assertEqual(
            tuple(row.subgroup_size for row in growth),
            (2, 4, 8, 16),
        )
        self.assertEqual(
            tuple(row.subgroup_exponent for row in growth),
            (2, 2, 2, 2),
        )
        self.assertFalse(any(row.truncated for row in growth))


if __name__ == "__main__":
    unittest.main()
