import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    rack_point_pushing_operator_label_audit,
    rack_solution,
)


class RackPointPushingOperatorLabelTests(unittest.TestCase):
    def test_trivial_rack_has_trivial_operator_label_extension(self):
        rack = rack_solution([0, 1], lambda _left, right: right)

        audit = rack_point_pushing_operator_label_audit(rack, arity=3)

        self.assertTrue(audit.verifies_rack_operator_label_extension)
        self.assertEqual(audit.inner_group_order, 1)
        self.assertEqual(audit.inner_group_exponent, 1)
        self.assertEqual(audit.operator_label_tuple_count, 1)
        self.assertEqual(audit.point_pushing_group_order, 1)
        self.assertEqual(audit.hurwitz_quotient_order, 1)
        self.assertEqual(audit.vertical_kernel_exponent, 1)

    def test_dihedral_rack_whole_image_exponent_is_not_the_invariant(self):
        rack = rack_solution(
            [0, 1, 2],
            lambda left, right: (2 * left - right) % 3,
        )

        audit = rack_point_pushing_operator_label_audit(
            rack,
            arity=3,
            max_size=2000,
        )

        self.assertTrue(audit.verifies_rack_operator_label_extension)
        self.assertEqual(audit.inner_group_order, 6)
        self.assertEqual(audit.inner_group_exponent, 6)
        self.assertEqual(audit.point_pushing_group_order, 648)
        self.assertEqual(audit.point_pushing_group_exponent, 36)
        self.assertGreater(
            audit.point_pushing_group_exponent,
            audit.inner_group_exponent,
        )
        self.assertEqual(audit.hurwitz_quotient_order, 648)
        self.assertEqual(audit.vertical_kernel_size, 1)
        self.assertEqual(audit.vertical_kernel_exponent, 1)
        self.assertTrue(audit.vertical_exponent_divides_inner_exponent)


if __name__ == "__main__":
    unittest.main()
