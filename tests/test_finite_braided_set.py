import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    admits_rack_quotient_cover,
    identity_solution,
    is_rack_solution,
    is_subsolution_subset,
    opposite_solution,
    product_solution,
    rack_quotient_obstructions,
    rack_solution,
    reverse_braid_word,
    subsolution,
)


class FiniteBraidedSetTests(unittest.TestCase):
    def test_identity_solution_is_ybe(self):
        solution = identity_solution([0, 1])
        self.assertTrue(solution.is_ybe())
        self.assertEqual(solution.braid_action([1, -1], (0, 1)), (0, 1))

    def test_trivial_rack_solution_is_flip(self):
        solution = rack_solution([0, 1, 2], lambda a, b: b)
        self.assertTrue(solution.is_ybe())
        self.assertTrue(is_rack_solution(solution))
        self.assertEqual(solution.braid_action([1], (0, 2)), (2, 0))
        self.assertTrue(admits_rack_quotient_cover(solution))
        self.assertEqual(rack_quotient_obstructions(solution), tuple())

    def test_product_of_racks_is_rack_form(self):
        left = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        right = rack_solution(["a", "b"], lambda _left, right: right)

        product = product_solution(left, right)

        self.assertTrue(product.is_ybe())
        self.assertTrue(is_rack_solution(product))
        self.assertEqual(len(product.elements), 6)

    def test_identity_solution_is_not_rack_form_unless_singleton(self):
        self.assertFalse(is_rack_solution(identity_solution([0, 1])))
        self.assertTrue(is_rack_solution(identity_solution([0])))

    def test_subsolution_restricts_braid_action(self):
        solution = rack_solution([0, 1, 2], lambda _left, right: right)
        restricted = subsolution(solution, [0, 2])
        word = (1, 2, -1, 2)
        tup = (0, 2, 0)

        self.assertTrue(is_subsolution_subset(solution, [0, 2]))
        self.assertTrue(restricted.is_ybe())
        self.assertEqual(restricted.braid_action(word, tup), solution.braid_action(word, tup))

    def test_subsolution_rejects_nonclosed_subset(self):
        solution = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)

        self.assertFalse(is_subsolution_subset(solution, [0, 1]))
        with self.assertRaises(ValueError):
            subsolution(solution, [0, 1])

    def test_opposite_solution_preserves_ybe(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        opposite = opposite_solution(solution)
        self.assertTrue(opposite.is_ybe())
        self.assertEqual(opposite.R[(0, 1)], (1, 2))

    def test_opposite_solution_action_is_strand_reversed_original_action(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        opposite = opposite_solution(solution)
        word = (1, 2, -1, 2, -2)
        tup = (0, 1, 2)

        self.assertEqual(
            opposite.braid_action(word, tup),
            tuple(
                reversed(
                    solution.braid_action(
                        reverse_braid_word(len(tup), word),
                        tuple(reversed(tup)),
                    )
                )
            ),
        )

    def test_rack_quotient_cover_obstruction_for_identity_solution(self):
        solution = identity_solution([0, 1])
        self.assertFalse(admits_rack_quotient_cover(solution))
        self.assertIn((0, 1, 1), rack_quotient_obstructions(solution))

    def test_dihedral_quandle_order_three_is_ybe(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        self.assertTrue(solution.is_ybe())

    def test_ybe_failure_is_reported(self):
        elements = [0, 1]
        bad = FiniteBraidedSet(
            elements,
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 1),
                (1, 1): (1, 0),
            },
        )
        self.assertFalse(bad.is_ybe())
        self.assertTrue(bad.ybe_failures())


if __name__ == "__main__":
    unittest.main()
