import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    admits_rack_quotient_cover,
    flip_disjoint_union_solution,
    identity_solution,
    is_rack_solution,
    is_subsolution_subset,
    opposite_solution,
    product_solution,
    rack_quotient_obstructions,
    rack_solution,
    reverse_braid_word,
    subsolution,
    symmetric_group,
)


class FiniteBraidedSetTests(unittest.TestCase):
    @staticmethod
    def component_pattern(tup):
        return tuple(element[0] for element in tup)

    @staticmethod
    def symmetric_pattern_action(word, pattern):
        out = list(pattern)
        for signed_generator in word:
            index = abs(signed_generator) - 1
            out[index], out[index + 1] = out[index + 1], out[index]
        return tuple(out)

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

    def test_flip_disjoint_union_solution_is_ybe(self):
        left = rack_solution([0, 1], lambda _left, right: right)
        right = identity_solution(["x", "y"])

        union = flip_disjoint_union_solution(left, right, "L", "R")

        self.assertTrue(union.is_ybe())
        self.assertEqual(
            union.R[(("L", 0), ("R", "x"))],
            (("R", "x"), ("L", 0)),
        )
        self.assertEqual(
            union.R[(("R", "x"), ("L", 0))],
            (("L", 0), ("R", "x")),
        )

    def test_flip_disjoint_union_of_racks_is_a_rack(self):
        left = rack_solution([0, 1], lambda _left, right: 1 - right)
        right = rack_solution(["x", "y"], lambda _left, right: right)

        union = flip_disjoint_union_solution(left, right, "L", "R")

        self.assertTrue(union.is_ybe())
        self.assertTrue(is_rack_solution(union))

    def test_flip_disjoint_union_color_map_is_braid_equivariant(self):
        left = identity_solution(["a", "b"])
        right = rack_solution([0, 1], lambda _left, right: 1 - right)
        union = flip_disjoint_union_solution(left, right, "L", "R")
        word = (1, 2, -1, 2)

        for tup in product(union.elements, repeat=3):
            image = union.braid_action(word, tup)
            self.assertEqual(
                self.component_pattern(image),
                self.symmetric_pattern_action(word, self.component_pattern(tup)),
            )

    def test_flip_disjoint_union_pure_braid_deletes_to_same_color_subbraid(self):
        left = rack_solution([0, 1], lambda _left, right: 1 - right)
        right = identity_solution(["r"])
        union = flip_disjoint_union_solution(left, right, "L", "R")
        pure_word = (2, 1, 1, -2)

        for a, b in product(left.elements, repeat=2):
            tup = (("L", a), ("R", "r"), ("L", b))
            image = union.braid_action(pure_word, tup)
            left_image = left.braid_action((1, 1), (a, b))
            self.assertEqual(
                image,
                (("L", left_image[0]), ("R", "r"), ("L", left_image[1])),
            )

    def test_faithful_endpoint_bisections_form_absorbing_product_rack(self):
        group = symmetric_group(3)
        identity = group.identity
        elements = tuple((operator, fibre) for operator in group.elements for fibre in group.elements)

        def endpoint_rack_op(left, right):
            operator, _fibre = left
            right_operator, right_fibre = right
            return (
                group.mul(group.mul(operator, right_operator), group.inv(operator)),
                group.mul(operator, right_fibre),
            )

        rack = rack_solution(elements, endpoint_rack_op)
        transposition = next(
            element
            for element in group.elements
            if element != identity and group.mul(element, element) == identity
        )

        self.assertTrue(rack.is_ybe())
        self.assertTrue(is_rack_solution(rack))
        self.assertNotEqual(
            endpoint_rack_op((transposition, identity), (identity, identity)),
            (identity, identity),
        )

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
