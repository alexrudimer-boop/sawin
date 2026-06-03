import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_audit import affine_solution  # noqa: E402
from run_affine_f2_full_twist_audit import affine_full_twist_profile  # noqa: E402
from ybe_domination import (  # noqa: E402
    braid_action_order,
    branch_tags,
    full_twist_braid_word,
)


class AffineF2FullTwistAuditTests(unittest.TestCase):
    def test_fast_affine_full_twist_orders_match_tuple_action(self):
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

        direct_orders = tuple(
            braid_action_order(solution, n, full_twist_braid_word(n))
            for n in range(1, 6)
        )
        fast_orders = affine_full_twist_profile(matrix, offset, 2, max_n=5)

        self.assertEqual(direct_orders, (1, 2, 1, 2, 1))
        self.assertEqual(fast_orders, direct_orders)


if __name__ == "__main__":
    unittest.main()
