import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    bounded_deletion_search_triage,
    bounded_deletion_support_audit,
    bounded_deletion_support_affine_q3_compressed_audit,
    bounded_deletion_support_q3_compressed_audit,
    bounded_deletion_support_stabilizer_audit,
    FiniteBraidedSet,
    componentwise_realized_parabolic_cross_effect_audit,
    componentwise_stabilizer_realized_parabolic_cross_effect_audit,
    flip_disjoint_union_solution,
    identity_solution,
    pure_braid_image_audit,
    product_solution,
    rack_product_prefixes,
    rack_residual_obstruction_audit,
    rack_solution,
    realized_parabolic_cross_effect_audit,
    small_rack_prefix_obstruction_rows,
    small_rack_representatives,
    two_strand_rack_cutoff_audit,
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


def affine_f2_type_a_matrix_data():
    return (
        (
            (0, 0, 0, 1),
            (1, 1, 0, 1),
            (1, 0, 1, 1),
            (1, 0, 0, 0),
        ),
        (0, 0, 1, 1),
        2,
    )


def affine_f2_hidden_cyclic_gauge_solution():
    elements = tuple(product((0, 1), repeat=3))
    table = {}
    for a, z1, z2 in elements:
        for b, w1, w2 in elements:
            table[((a, z1, z2), (b, w1, w2))] = (
                (a, w2, w1),
                (b, (z2 + 1) % 2, (z1 + 1) % 2),
            )
    return FiniteBraidedSet(elements, table)


def flip_across_type_b_solution():
    trivial2 = rack_solution((0, 1), lambda _left, right: right)
    perm2 = FiniteBraidedSet(
        (2, 3),
        {
            (left, right): (right, 5 - left)
            for left in (2, 3)
            for right in (2, 3)
        },
    )
    return flip_disjoint_union_solution(trivial2, perm2)


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

    def test_small_rack_representatives_size_three_prefix_is_practical(self):
        representatives = small_rack_representatives(3)
        prefixes = rack_product_prefixes(representatives, max_detector_size=256)

        self.assertEqual(len(representatives), 9)
        self.assertEqual(
            [len(rack.elements) for rack in representatives],
            [1, 2, 2, 3, 3, 3, 3, 3, 3],
        )
        self.assertEqual(
            [len(prefix.elements) for prefix in prefixes],
            [1, 2, 4, 12, 36, 108],
        )

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

    def test_affine_f2_hidden_cyclic_gauge_row_is_non_bisectional(self):
        solution = affine_f2_hidden_cyclic_gauge_solution()
        left = (0, 0, 0)
        first_outputs = {
            solution.R[(left, right)][0]
            for right in solution.elements
        }

        self.assertTrue(solution.is_ybe())
        self.assertEqual(len(solution.elements), 8)
        self.assertEqual(len(first_outputs), 4)
        self.assertNotEqual(set(first_outputs), set(solution.elements))

    def test_one_point_detector_has_high_arity_cross_effect_at_bound_one(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)
        detector = identity_solution(("z",))

        audit = realized_parabolic_cross_effect_audit(
            solution, detector, bound=1, n=2
        )

        self.assertFalse(audit.truncated)
        self.assertTrue(audit.quotient_nontrivial)
        self.assertTrue(audit.proves_realized_high_arity_obstruction)
        self.assertEqual(audit.parabolic_image_size, 1)
        self.assertEqual(audit.first_witness_word, (1,))
        self.assertNotEqual(audit.first_moved_tuple, audit.first_moved_tuple_image)

    def test_flip_detector_cross_effect_vanishes_at_bound_two(self):
        solution = affine_f2_type_a_solution()
        detector = rack_solution((0, 1), lambda _left, right: right)

        audit = realized_parabolic_cross_effect_audit(
            solution, detector, bound=2, n=3
        )

        self.assertFalse(audit.truncated)
        self.assertFalse(audit.quotient_nontrivial)
        self.assertEqual(audit.kernel_image_size, audit.parabolic_image_size)

    def test_componentwise_cross_effect_matches_single_detector(self):
        solution = affine_f2_type_a_solution()
        detector = rack_solution((0, 1), lambda _left, right: right)

        expanded = realized_parabolic_cross_effect_audit(
            solution, detector, bound=2, n=3
        )
        componentwise = componentwise_realized_parabolic_cross_effect_audit(
            solution, (detector,), bound=2, n=3
        )

        self.assertEqual(componentwise, expanded)

    def test_componentwise_stabilizer_cross_effect_matches_single_detector(self):
        solution = affine_f2_type_a_solution()
        detector = rack_solution((0, 1), lambda _left, right: right)

        enumerated = componentwise_realized_parabolic_cross_effect_audit(
            solution, (detector,), bound=2, n=3
        )
        stabilizer = componentwise_stabilizer_realized_parabolic_cross_effect_audit(
            solution, (detector,), bound=2, n=3
        )

        self.assertFalse(stabilizer.truncated)
        self.assertEqual(stabilizer.joint_image_size, enumerated.joint_image_size)
        self.assertEqual(stabilizer.kernel_image_size, enumerated.kernel_image_size)
        self.assertEqual(
            stabilizer.parabolic_image_size,
            enumerated.parabolic_image_size,
        )
        self.assertEqual(stabilizer.quotient_size, enumerated.quotient_size)
        self.assertEqual(
            stabilizer.quotient_nontrivial,
            enumerated.quotient_nontrivial,
        )

    def test_componentwise_cross_effect_matches_small_product_detector(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)
        detector_left = rack_solution((0, 1), lambda _left, right: right)
        detector_right = rack_solution((0, 1), lambda _left, right: 1 - right)
        product_detector = product_solution(detector_left, detector_right)

        expanded = realized_parabolic_cross_effect_audit(
            solution, product_detector, bound=2, n=3
        )
        componentwise = componentwise_realized_parabolic_cross_effect_audit(
            solution, (detector_left, detector_right), bound=2, n=3
        )

        self.assertEqual(componentwise.joint_image_size, expanded.joint_image_size)
        self.assertEqual(componentwise.kernel_image_size, expanded.kernel_image_size)
        self.assertEqual(
            componentwise.parabolic_image_size,
            expanded.parabolic_image_size,
        )
        self.assertEqual(componentwise.quotient_size, expanded.quotient_size)
        self.assertEqual(
            componentwise.quotient_nontrivial,
            expanded.quotient_nontrivial,
        )

    def test_componentwise_stabilizer_cross_effect_matches_small_product_detector(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)
        detector_left = rack_solution((0, 1), lambda _left, right: right)
        detector_right = rack_solution((0, 1), lambda _left, right: 1 - right)

        enumerated = componentwise_realized_parabolic_cross_effect_audit(
            solution, (detector_left, detector_right), bound=2, n=3
        )
        stabilizer = componentwise_stabilizer_realized_parabolic_cross_effect_audit(
            solution, (detector_left, detector_right), bound=2, n=3
        )

        self.assertFalse(stabilizer.truncated)
        self.assertEqual(stabilizer.joint_image_size, enumerated.joint_image_size)
        self.assertEqual(stabilizer.kernel_image_size, enumerated.kernel_image_size)
        self.assertEqual(
            stabilizer.parabolic_image_size,
            enumerated.parabolic_image_size,
        )
        self.assertEqual(stabilizer.quotient_size, enumerated.quotient_size)
        self.assertEqual(
            stabilizer.quotient_nontrivial,
            enumerated.quotient_nontrivial,
        )

    def test_bounded_deletion_support_audit_vanishes_for_cyclic_rack(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)

        audit = bounded_deletion_support_audit(
            solution,
            h=2,
            n=3,
            rack_size_bound=2,
        )

        self.assertFalse(audit.truncated)
        self.assertEqual(audit.detector_size, 4)
        self.assertEqual(audit.detector_component_count, 3)
        self.assertEqual(audit.subset_count, 3)
        self.assertFalse(audit.obstruction_nontrivial)
        self.assertFalse(audit.proves_bounded_deletion_support_failure)

    def test_compressed_q3_bounded_deletion_audit_closes_type_b_at_arity_three(self):
        solution = flip_across_type_b_solution()

        audit = bounded_deletion_support_audit(
            solution,
            h=2,
            n=3,
            rack_size_bound=3,
        )

        self.assertFalse(audit.truncated)
        self.assertEqual(audit.detector_size, 2916)
        self.assertEqual(audit.detector_component_count, 9)
        self.assertEqual(audit.joint_image_size, 1728)
        self.assertFalse(audit.obstruction_nontrivial)

    def test_q3_linking_compressed_audit_matches_type_b_at_arity_three(self):
        solution = flip_across_type_b_solution()

        audit = bounded_deletion_support_q3_compressed_audit(
            solution,
            h=2,
            n=3,
        )

        self.assertFalse(audit.truncated)
        self.assertEqual(audit.detector_size, 2916)
        self.assertEqual(audit.detector_component_count, 3)
        self.assertEqual(audit.subset_count, 3)
        self.assertEqual(audit.joint_image_size, 1728)
        self.assertEqual(audit.obstruction_size, 1)
        self.assertFalse(audit.obstruction_nontrivial)

    def test_affine_q3_compressed_audit_matches_type_a_at_arity_three(self):
        solution = affine_f2_type_a_solution()
        matrix, offset, dimension = affine_f2_type_a_matrix_data()

        permutation_audit = bounded_deletion_support_q3_compressed_audit(
            solution,
            h=2,
            n=3,
        )
        affine_audit = bounded_deletion_support_affine_q3_compressed_audit(
            matrix,
            offset,
            dimension,
            h=2,
            n=3,
        )

        self.assertFalse(affine_audit.truncated)
        self.assertEqual(affine_audit.detector_size, 2916)
        self.assertEqual(affine_audit.detector_component_count, 3)
        self.assertEqual(affine_audit.subset_count, 3)
        self.assertEqual(
            affine_audit.joint_image_size,
            permutation_audit.joint_image_size,
        )
        self.assertEqual(
            affine_audit.obstruction_size,
            permutation_audit.obstruction_size,
        )
        self.assertEqual(
            affine_audit.obstruction_nontrivial,
            permutation_audit.obstruction_nontrivial,
        )

    def test_fixed_q3_affine_rack_has_brunnian_obstruction_at_arity_three(self):
        solution = rack_solution(
            tuple(range(5)),
            lambda left, right: (-left + 2 * right) % 5,
        )

        audit = bounded_deletion_support_q3_compressed_audit(
            solution,
            h=2,
            n=3,
        )

        self.assertFalse(audit.truncated)
        self.assertEqual(audit.detector_size, 2916)
        self.assertEqual(audit.detector_component_count, 3)
        self.assertEqual(audit.subset_count, 3)
        self.assertEqual(audit.joint_image_size, 3456)
        self.assertEqual(audit.obstruction_size, 2)
        self.assertTrue(audit.obstruction_nontrivial)
        self.assertIsNotNone(audit.first_witness_word)
        self.assertNotEqual(audit.first_moved_tuple, audit.first_moved_tuple_image)

    def test_stabilizer_q3_bounded_deletion_audit_closes_type_b_at_arity_four(self):
        solution = flip_across_type_b_solution()

        audit = bounded_deletion_support_stabilizer_audit(
            solution,
            h=2,
            n=4,
            rack_size_bound=3,
        )

        self.assertFalse(audit.truncated)
        self.assertEqual(audit.detector_size, 2916)
        self.assertEqual(audit.detector_component_count, 9)
        self.assertEqual(audit.subset_count, 6)
        self.assertEqual(audit.joint_image_size, 1119744)
        self.assertEqual(audit.obstruction_size, 1)
        self.assertFalse(audit.obstruction_nontrivial)

    def test_two_strand_rack_cutoff_finds_cyclic_rack_stage(self):
        solution = rack_solution((0, 1), lambda _left, right: 1 - right)

        audit = two_strand_rack_cutoff_audit(solution, max_rack_size=2)

        self.assertEqual(audit.solution_crossing_order, 4)
        self.assertEqual(audit.cutoff, 2)
        self.assertFalse(audit.rows[0].detects_solution)
        self.assertTrue(audit.rows[1].detects_solution)
        self.assertEqual(audit.rows[1].crossing_lcm, 4)

    def test_pure_braid_image_trigger_detects_cyclic_but_not_flip_rack(self):
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)
        flip = rack_solution((0, 1), lambda _left, right: right)

        cyclic_audit = pure_braid_image_audit(cyclic, n=2)
        flip_audit = pure_braid_image_audit(flip, n=3)

        self.assertTrue(cyclic_audit.image_nontrivial)
        self.assertEqual(cyclic_audit.first_witness_word, (1, 1))
        self.assertNotEqual(
            cyclic_audit.first_moved_tuple,
            cyclic_audit.first_moved_tuple_image,
        )
        self.assertFalse(flip_audit.image_nontrivial)

    def test_bounded_deletion_search_triage_suggests_next_detector_bound(self):
        solution = affine_f2_type_a_solution()

        triage = bounded_deletion_search_triage(
            solution,
            max_rack_size=2,
            max_pure_arity=3,
        )

        self.assertEqual(triage.two_strand_cutoff.cutoff, 2)
        self.assertEqual(triage.suggested_rack_size_bound, 3)
        self.assertEqual(triage.first_pure_nontrivial_arity, 2)


if __name__ == "__main__":
    unittest.main()
