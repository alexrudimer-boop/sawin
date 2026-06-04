import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    flip_disjoint_union_solution,
    identity_solution,
    is_involutive_solution,
    is_rack_solution,
    rack_residual_obstruction_audit,
    rack_solution,
    subsolution_fibre_congruences,
    subsolution_fibre_transition_audit,
    subsolution_fibre_transport_isomorphism_audit,
    subsolution_fibre_transport_monodromy_audit,
    terminal_branch_triage_audit,
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


def parity_vector(tup):
    return tuple((a + b) % 2 for a, b in tup)


def fibre_coordinates(tup):
    parities = parity_vector(tup)
    offsets = [0]
    for index in range(len(tup) - 1):
        offsets.append((offsets[-1] + parities[index + 1] + 1) % 2)
    return tuple((a + offset) % 2 for (a, _b), offset in zip(tup, offsets))


def permutation_solution_with_toggle():
    elements = (0, 1)
    return FiniteBraidedSet(
        elements,
        {(left, right): (right, 1 - left) for left in elements for right in elements},
    )


def color_pattern(tup):
    return tuple(tag for tag, _value in tup)


class SizeFourDegenerateMechanismTests(unittest.TestCase):
    def test_affine_f2_type_a_is_degenerate_noninvolutive_ybe(self):
        solution = affine_f2_type_a_solution()

        self.assertTrue(solution.is_ybe())
        self.assertFalse(is_involutive_solution(solution))
        self.assertEqual(solution.R[((0, 0), (0, 0))], ((0, 0), (1, 1)))
        self.assertEqual(solution.R[solution.R[((0, 0), (0, 0))]], ((1, 1), (1, 1)))

    def test_affine_f2_type_a_is_fibrewise_cyclic_rack_action(self):
        solution = affine_f2_type_a_solution()
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)

        for n in range(2, 5):
            for generator in range(1, n):
                for tup in product(solution.elements, repeat=n):
                    image = solution.braid_action((generator,), tup)
                    self.assertEqual(parity_vector(image), parity_vector(tup))
                    self.assertEqual(
                        fibre_coordinates(image),
                        cyclic.braid_action((generator,), fibre_coordinates(tup)),
                    )

    def test_flip_across_union_of_solutions_is_ybe_and_color_equivariant(self):
        trivial = identity_solution((0, 1))
        permutation = permutation_solution_with_toggle()
        union = flip_disjoint_union_solution(trivial, permutation, "T", "P")

        self.assertTrue(union.is_ybe())
        self.assertFalse(is_involutive_solution(union))

        for n in range(2, 5):
            for generator in range(1, n):
                for tup in product(union.elements, repeat=n):
                    image = union.braid_action((generator,), tup)
                    expected_colors = list(color_pattern(tup))
                    expected_colors[generator - 1], expected_colors[generator] = (
                        expected_colors[generator],
                        expected_colors[generator - 1],
                    )
                    self.assertEqual(color_pattern(image), tuple(expected_colors))

    def test_flip_across_union_preserves_rack_domination_in_small_arities(self):
        trivial = identity_solution((0, 1))
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)
        flip_rack = rack_solution((0, 1), lambda _left, right: right)

        target = flip_disjoint_union_solution(trivial, cyclic, "T", "C")
        detector = flip_disjoint_union_solution(flip_rack, cyclic, "T", "C")

        self.assertTrue(target.is_ybe())
        self.assertTrue(detector.is_ybe())
        self.assertTrue(is_rack_solution(detector))

        for n in range(2, 4):
            audit = rack_residual_obstruction_audit(target, detector, n)
            self.assertFalse(audit.truncated)
            self.assertFalse(audit.kernel_contains_nonidentity)

    def test_terminal_branch_triage_sees_size_four_mechanisms(self):
        type_a_solution = affine_f2_type_a_solution()
        type_a = terminal_branch_triage_audit(type_a_solution)
        self.assertFalse(type_a.has_point_separating_proper_quotients)
        self.assertFalse(type_a.has_flip_across_decomposition)
        self.assertTrue(type_a.has_nontrivial_one_state_observer)
        self.assertTrue(type_a.has_proper_subsolution)
        self.assertTrue(type_a.has_subsolution_fibre_congruence)
        self.assertEqual(
            len(subsolution_fibre_congruences(type_a_solution)),
            1,
        )
        type_a_transition = subsolution_fibre_transition_audit(
            type_a_solution,
            type_a.subsolution_fibre_congruences[0],
        )
        self.assertTrue(type_a_transition.all_mixed_transitions_product_like)
        self.assertTrue(type_a_transition.all_mixed_transitions_swapped_product_like)
        self.assertFalse(type_a_transition.all_mixed_transitions_direct_product_like)
        type_a_transport = subsolution_fibre_transport_isomorphism_audit(
            type_a_solution,
            type_a.subsolution_fibre_congruences[0],
        )
        self.assertTrue(type_a_transport.all_mixed_rows_product_like)
        self.assertFalse(
            type_a_transport.all_product_like_rows_have_transport_isomorphisms
        )
        type_a_monodromy = subsolution_fibre_transport_monodromy_audit(
            type_a_solution,
            type_a.subsolution_fibre_congruences[0],
        )
        self.assertFalse(type_a_monodromy.all_rows_transport_isomorphic)

        type_b_solution = flip_disjoint_union_solution(
            identity_solution((0, 1)),
            permutation_solution_with_toggle(),
            "T",
            "P",
        )
        type_b = terminal_branch_triage_audit(type_b_solution)
        self.assertTrue(type_b.has_point_separating_proper_quotients)
        self.assertTrue(type_b.has_flip_across_decomposition)
        self.assertTrue(type_b.has_subsolution_fibre_congruence)
        type_b_transition = subsolution_fibre_transition_audit(
            type_b_solution,
            type_b.subsolution_fibre_congruences[0],
        )
        self.assertTrue(type_b_transition.all_mixed_transitions_product_like)
        self.assertTrue(type_b_transition.all_mixed_transitions_swapped_product_like)
        self.assertFalse(type_b_transition.all_mixed_transitions_direct_product_like)
        type_b_transport = subsolution_fibre_transport_isomorphism_audit(
            type_b_solution,
            type_b.subsolution_fibre_congruences[0],
        )
        self.assertTrue(type_b_transport.all_mixed_rows_product_like)
        self.assertTrue(
            type_b_transport.all_product_like_rows_have_transport_isomorphisms
        )
        type_b_monodromy = subsolution_fibre_transport_monodromy_audit(
            type_b_solution,
            type_b.subsolution_fibre_congruences[0],
        )
        self.assertTrue(type_b_monodromy.all_loop_groups_trivial)


if __name__ == "__main__":
    unittest.main()
