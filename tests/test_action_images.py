import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    braid_images_for_words,
    compose_permutations,
    commutator,
    evaluate_free_word_on_permutations,
    free_word_power,
    generated_permutation_subgroup,
    identity_permutation,
    invert_permutation,
    law_braid_action_certificate,
    law_word_on_last_strand,
    point_pushing_exponent_escape_audit,
    point_pushing_marked_quotient_audit,
    point_pushing_mu_prefix_audit,
    point_pushing_suffix_shuttle_action,
    point_pushing_suffix_shuttle_audit,
    point_pushing_vertical_witness_certificate,
    point_pushing_variety_escape_audit,
    point_pushing_variety_prefix_audit,
    pure_generator_order_profile,
    pure_braid_generator,
    pure_subgroup_growth_profile,
    rack_solution,
    short_law_separating_permutation_assignment,
    cyclic_group,
)


class ActionImageTests(unittest.TestCase):
    def test_permutation_group_operations(self):
        p = (1, 0, 2)
        q = (0, 2, 1)
        self.assertEqual(compose_permutations(p, invert_permutation(p)), identity_permutation(3))
        self.assertEqual(compose_permutations(p, q), (1, 2, 0))

    def test_generated_subgroup(self):
        subgroup = generated_permutation_subgroup([(1, 0, 2), (0, 2, 1)])
        self.assertEqual(len(subgroup), 6)

    def test_pure_generator_order_profile_for_trivial_rack(self):
        solution = rack_solution([0, 1], lambda a, b: b)
        profile = pure_generator_order_profile(solution, max_q=4)
        self.assertEqual([row.max_order for row in profile], [1, 1, 1])

    def test_pure_subgroup_growth_profile_for_dihedral_quandle(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        profile = pure_subgroup_growth_profile(
            solution,
            max_q=3,
            max_subgroup_size=100,
        )
        self.assertEqual(profile[0].subgroup_size, 3)
        self.assertEqual(profile[0].subgroup_exponent, 3)
        self.assertFalse(profile[0].truncated)
        self.assertEqual(profile[1].subgroup_size, 24)
        self.assertEqual(profile[1].subgroup_exponent, 12)
        self.assertFalse(profile[1].truncated)

    def test_free_word_evaluation_matches_law_braid_action(self):
        solution = rack_solution([0, 1], lambda a, b: b)
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        n, braid = law_word_on_last_strand(word, arity=2)
        images = braid_images_for_words(
            solution,
            n,
            {0: pure_braid_generator(1, n), 1: pure_braid_generator(2, n)},
        )
        evaluated = evaluate_free_word_on_permutations(word, images)
        direct = braid_images_for_words(solution, n, {0: braid})[0]
        self.assertEqual(evaluated, direct)

    def test_law_braid_action_certificate_records_fixed_image_barrier(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        exponent_word = free_word_power(0, 12)
        exponent_certificate = law_braid_action_certificate(
            solution, exponent_word, arity=1
        )
        self.assertTrue(exponent_certificate.direct_matches_evaluated)
        self.assertTrue(exponent_certificate.word_is_law_on_image_subgroup)
        self.assertTrue(exponent_certificate.evaluated_word_is_identity)
        self.assertTrue(exponent_certificate.direct_braid_is_identity)

        commutator_word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        commutator_certificate = law_braid_action_certificate(
            solution, commutator_word, arity=2
        )
        self.assertTrue(commutator_certificate.direct_matches_evaluated)
        self.assertFalse(commutator_certificate.word_is_law_on_image_subgroup)
        self.assertFalse(commutator_certificate.evaluated_word_is_identity)
        self.assertFalse(commutator_certificate.direct_braid_is_identity)

    def test_short_law_separating_permutation_assignment_records_mover(self):
        swap01 = (1, 0, 2)
        swap12 = (0, 2, 1)

        separation = short_law_separating_permutation_assignment(
            (cyclic_group(2), cyclic_group(3)),
            {0: swap01, 1: swap12},
            max_length=4,
        )

        self.assertEqual(
            separation.separating_word,
            ((0, 1), (1, 1), (0, -1), (1, -1)),
        )
        self.assertEqual(separation.arity, 2)
        self.assertEqual(separation.target_degree, 3)
        self.assertIsNotNone(separation.evaluated_permutation)
        self.assertIsNotNone(separation.moved_index)
        self.assertNotEqual(
            separation.evaluated_permutation[separation.moved_index],
            separation.moved_index,
        )

    def test_point_pushing_variety_escape_keeps_representing_words(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_variety_escape_audit(
            solution,
            symmetric_degree=2,
            point_pushing_arity=1,
            law_arity=1,
            max_length=2,
        )

        self.assertFalse(audit.truncated)
        self.assertEqual(audit.braid_index, 2)
        self.assertEqual(audit.tuple_count, 9)
        self.assertEqual(audit.action_image_size, 3)
        self.assertTrue(audit.found_variety_escape)
        self.assertIsNotNone(audit.separating_word)
        self.assertEqual(len(audit.assignment_representatives), 1)
        self.assertIsNotNone(audit.substituted_point_pushing_word)
        self.assertTrue(audit.substituted_word_is_symmetric_law)
        self.assertTrue(audit.direct_matches_evaluated)
        self.assertTrue(audit.substituted_word_gives_point_pushing_mover)
        self.assertNotEqual(
            audit.direct_braid_permutation[audit.moved_index],
            audit.moved_index,
        )

    def test_point_pushing_variety_escape_records_truncation(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_variety_escape_audit(
            solution,
            symmetric_degree=2,
            point_pushing_arity=1,
            law_arity=1,
            max_length=2,
            max_subgroup_size=1,
        )

        self.assertTrue(audit.truncated)
        self.assertIsNone(audit.action_image_size)
        self.assertFalse(audit.found_variety_escape)

    def test_point_pushing_variety_prefix_records_bounded_escapes(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_variety_prefix_audit(
            solution,
            symmetric_degree=2,
            max_point_pushing_arity=2,
            law_arity=1,
            max_length=2,
        )

        self.assertEqual(audit.row_count, 2)
        self.assertTrue(audit.arities_are_initial_segment)
        self.assertEqual(audit.escaped_arities, (1, 2))
        self.assertEqual(audit.truncated_rows, ())
        self.assertTrue(audit.all_escape_rows_give_movers)
        self.assertFalse(audit.no_bounded_escape_found)

    def test_point_pushing_variety_prefix_records_no_bounded_escape(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_variety_prefix_audit(
            solution,
            symmetric_degree=3,
            max_point_pushing_arity=1,
            law_arity=1,
            max_length=4,
        )

        self.assertEqual(audit.row_count, 1)
        self.assertEqual(audit.escape_rows, ())
        self.assertEqual(audit.truncated_rows, ())
        self.assertTrue(audit.no_bounded_escape_found)

    def test_point_pushing_exponent_escape_records_power_law_mover(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_exponent_escape_audit(
            solution,
            law_bound=3,
            point_pushing_arity=2,
        )

        self.assertFalse(audit.truncated)
        self.assertEqual(audit.exponent_bound, 6)
        self.assertEqual(audit.action_image_size, 24)
        self.assertEqual(audit.escaping_element_order, 4)
        self.assertTrue(audit.found_exponent_escape)
        self.assertTrue(audit.direct_matches_evaluated)
        self.assertTrue(audit.gives_power_law_mover)
        self.assertFalse(audit.symmetric_identity_longitude_signature)
        self.assertTrue(audit.exposes_naive_law_gap)
        self.assertIsNotNone(audit.exponent_law_word)
        self.assertNotEqual(
            audit.direct_braid_permutation[audit.moved_index],
            audit.moved_index,
        )

    def test_point_pushing_exponent_escape_records_no_escape(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_exponent_escape_audit(
            solution,
            law_bound=3,
            point_pushing_arity=1,
        )

        self.assertFalse(audit.truncated)
        self.assertEqual(audit.exponent_bound, 6)
        self.assertEqual(audit.action_image_size, 3)
        self.assertFalse(audit.found_exponent_escape)
        self.assertFalse(audit.gives_power_law_mover)
        self.assertIsNone(audit.symmetric_identity_longitude_signature)

    def test_point_pushing_marked_quotient_holds_for_trivial_action(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_marked_quotient_audit(
            solution,
            cyclic_group(2),
            arity=2,
        )

        self.assertFalse(audit.truncated)
        self.assertTrue(audit.marked_quotient_holds)
        self.assertTrue(audit.vertical_kernel_trivial)
        self.assertFalse(audit.found_kernel_mover)
        self.assertEqual(audit.detector_state_count, 64)
        self.assertEqual(audit.ybe_tuple_count, 8)
        self.assertEqual(audit.action_image_size, 1)

    def test_point_pushing_marked_quotient_finds_kernel_mover(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_marked_quotient_audit(
            solution,
            cyclic_group(2),
            arity=2,
        )

        self.assertFalse(audit.truncated)
        self.assertFalse(audit.marked_quotient_holds)
        self.assertFalse(audit.vertical_kernel_trivial)
        self.assertTrue(audit.found_kernel_mover)
        self.assertEqual(audit.witness_word, ((0, 1), (0, 1)))
        self.assertIsNotNone(audit.witness_action_value)
        self.assertIsNotNone(audit.moved_index)
        self.assertNotEqual(
            audit.witness_action_value[audit.moved_index],
            audit.moved_index,
        )

    def test_point_pushing_vertical_witness_certificate_checks_braid(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        word = ((0, 1), (0, 1))

        certificate = point_pushing_vertical_witness_certificate(
            solution,
            cyclic_group(2),
            word,
            arity=2,
        )

        self.assertTrue(certificate.detector_word_identity)
        self.assertFalse(certificate.evaluated_action_identity)
        self.assertFalse(certificate.direct_braid_identity)
        self.assertTrue(certificate.direct_matches_evaluated)
        self.assertTrue(certificate.moves_solution)
        self.assertTrue(certificate.valid_vertical_witness)
        self.assertEqual(certificate.braid_index, 3)
        self.assertEqual(certificate.detector_state_count, 64)
        self.assertEqual(certificate.ybe_tuple_count, 27)
        self.assertEqual(
            certificate.braid_word,
            pure_braid_generator(1, 3) + pure_braid_generator(1, 3),
        )
        self.assertIsNotNone(certificate.moved_tuple)
        self.assertNotEqual(certificate.moved_tuple, certificate.moved_tuple_image)

    def test_point_pushing_vertical_witness_certificate_rejects_nonmoving(self):
        solution = rack_solution([0, 1], lambda a, b: b)
        word = ((0, 1), (0, 1))

        certificate = point_pushing_vertical_witness_certificate(
            solution,
            cyclic_group(2),
            word,
            arity=2,
        )

        self.assertTrue(certificate.detector_word_identity)
        self.assertTrue(certificate.direct_braid_identity)
        self.assertFalse(certificate.moves_solution)
        self.assertFalse(certificate.valid_vertical_witness)

    def test_point_pushing_mu_prefix_audit_detects_trivial_prefix(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_mu_prefix_audit(
            solution,
            max_arity=2,
            max_symmetric_degree=2,
        )

        self.assertTrue(audit.detected_prefix_within_bound)
        self.assertEqual(audit.detected_arities, (1, 2))
        self.assertEqual(audit.unresolved_arities, tuple())
        self.assertEqual(
            tuple(row.minimal_symmetric_degree for row in audit.rows),
            (1, 1),
        )

    def test_point_pushing_mu_prefix_audit_records_vertical_witness(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_mu_prefix_audit(
            solution,
            max_arity=2,
            max_symmetric_degree=1,
        )

        self.assertFalse(audit.detected_prefix_within_bound)
        self.assertEqual(audit.unresolved_arities, (1, 2))
        self.assertTrue(all(row.has_vertical_witness_within_bound for row in audit.rows))
        self.assertEqual(tuple(row.first_witness_degree for row in audit.rows), (1, 1))

    def test_point_pushing_suffix_shuttle_matches_direct_action(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        for generator in (1, 2, 3):
            audit = point_pushing_suffix_shuttle_audit(
                solution,
                braid_index=4,
                generator=generator,
            )
            self.assertTrue(audit.matches_direct_action)
            self.assertEqual(audit.tuple_count, 81)
            self.assertIsNone(audit.first_failure_input)

    def test_point_pushing_suffix_shuttle_action_validates_indices(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        with self.assertRaises(ValueError):
            point_pushing_suffix_shuttle_action(solution, 1, 1, (0,))
        with self.assertRaises(ValueError):
            point_pushing_suffix_shuttle_action(solution, 3, 3, (0, 0, 0))
        with self.assertRaises(ValueError):
            point_pushing_suffix_shuttle_action(solution, 3, 1, (0, 0))


if __name__ == "__main__":
    unittest.main()
