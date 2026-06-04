import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    identity_solution,
    rack_product_prefixes,
    rack_residual_obstruction_audit,
    rack_solution,
    small_rack_prefix_obstruction_rows,
    small_rack_representatives,
)


def affine_f2_type_a_solution():
    elements = tuple(product((0, 1), repeat=2))
    table = {}
    for a, b in elements:
        for c, d in elements:
            table[((a, b), (c, d))] = (
                (d, (a + b + d) % 2),
                ((a + c + d + 1) % 2, (a + 1) % 2),
            )
    return FiniteBraidedSet(elements, table)


class RackResidualTowerTests(unittest.TestCase):
    def test_detector_equal_to_solution_has_trivial_residual_kernel(self):
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)

        audit = rack_residual_obstruction_audit(cyclic, cyclic, n=3)

        self.assertFalse(audit.truncated)
        self.assertFalse(audit.kernel_contains_nonidentity)
        self.assertFalse(audit.proves_fixed_width_domination_failure)

    def test_trivial_detector_finds_cyclic_rack_mover(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)
        detector = identity_solution(("z",))

        audit = rack_residual_obstruction_audit(solution, detector, n=2)

        self.assertFalse(audit.truncated)
        self.assertTrue(audit.kernel_contains_nonidentity)
        self.assertTrue(audit.proves_fixed_width_domination_failure)
        self.assertEqual(audit.first_witness_word, (1,))
        self.assertNotEqual(audit.first_moved_tuple, audit.first_moved_tuple_image)

    def test_small_rack_representatives_deduplicate_size_two(self):
        representatives = small_rack_representatives(2)

        self.assertEqual([len(rack.elements) for rack in representatives], [1, 2, 2])

    def test_product_prefix_containing_solution_has_no_cyclic_mover(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)
        prefixes = rack_product_prefixes(small_rack_representatives(2))

        audit = rack_residual_obstruction_audit(solution, prefixes[-1], n=3)

        self.assertFalse(audit.kernel_contains_nonidentity)

    def test_small_prefix_rows_record_obstruction_then_disappearance(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)

        rows = small_rack_prefix_obstruction_rows(
            solution,
            max_rack_size=2,
            max_arity=2,
            max_detector_size=4,
        )

        self.assertTrue(rows[1].obstruction_found)
        self.assertFalse(rows[-1].obstruction_found)

    def test_affine_type_a_prefix_vanishes_when_cyclic_rack_enters(self):
        solution = affine_f2_type_a_solution()

        rows = small_rack_prefix_obstruction_rows(
            solution,
            max_rack_size=2,
            max_arity=3,
            max_detector_size=4,
        )
        by_prefix_and_arity = {
            (row.detector_prefix_length, row.arity): row for row in rows
        }

        self.assertTrue(by_prefix_and_arity[(1, 2)].obstruction_found)
        self.assertTrue(by_prefix_and_arity[(2, 2)].obstruction_found)
        self.assertFalse(by_prefix_and_arity[(3, 2)].obstruction_found)
        self.assertFalse(by_prefix_and_arity[(3, 3)].obstruction_found)


if __name__ == "__main__":
    unittest.main()
