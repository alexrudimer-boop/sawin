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
    delete_right_based_new_strand_word,
    point_pushing_action_group,
    point_pushing_action_quotient_separation_audit,
    point_pushing_base_arity_certificate,
    point_pushing_base_free_brunnian_tail_prefix,
    point_pushing_base_free_threshold_audit,
    point_pushing_base_free_threshold_prefix_audit,
    point_pushing_brunnian_failure_certificate,
    point_pushing_brunnian_gate_prefix_audit,
    point_pushing_brunnian_normalized_prefix_audit,
    point_pushing_brunnian_orbit_audit,
    point_pushing_brunnian_tail_certificate_prefix,
    point_pushing_brunnian_tail_prefix_audit,
    point_pushing_brunnian_witness_certificate,
    point_pushing_product_prefix_first_failure_audit,
    point_pushing_exponent_escape_audit,
    point_pushing_monolithic_compression_audit,
    point_pushing_marked_quotient_audit,
    point_pushing_mu_prefix_audit,
    point_pushing_recursive_conjugacy_audit,
    point_pushing_suffix_shuttle_action,
    point_pushing_suffix_shuttle_audit,
    point_pushing_vertical_witness_certificate,
    point_pushing_variety_escape_audit,
    point_pushing_variety_prefix_audit,
    pure_generator_order_profile,
    right_based_point_pushing_word_to_left,
    pure_braid_generator,
    pure_subgroup_growth_profile,
    product_solution,
    rack_solution,
    short_law_separating_permutation_assignment,
    cyclic_group,
    symmetric_group,
)
from ybe_domination.action_images import (
    _minimal_normal_subgroups,
    _monolith_conjugation_data,
    _normal_subgroups_bruteforce,
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

    def test_right_based_point_pushing_conversion_and_deletion(self):
        word = ((1, 1), (0, 1), (1, -1), (0, -1))

        self.assertEqual(
            right_based_point_pushing_word_to_left(word, arity=2),
            ((0, 1), (1, 1), (0, -1), (1, -1)),
        )
        self.assertEqual(
            delete_right_based_new_strand_word(word, arity=2),
            tuple(),
        )

        with self.assertRaises(ValueError):
            right_based_point_pushing_word_to_left(((2, 1),), arity=2)
        with self.assertRaises(ValueError):
            delete_right_based_new_strand_word(((0, 1),), arity=0)

    def test_point_pushing_brunnian_witness_certificate_checks_new_strand(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        right_word = ((1, 1), (1, 1))

        certificate = point_pushing_brunnian_witness_certificate(
            solution,
            cyclic_group(2),
            right_word,
            arity=2,
        )

        self.assertEqual(certificate.right_based_word, right_word)
        self.assertEqual(certificate.left_based_word, ((0, 1), (0, 1)))
        self.assertEqual(certificate.deletion_word, tuple())
        self.assertTrue(certificate.deletion_trivial)
        self.assertTrue(certificate.vertical.valid_vertical_witness)
        self.assertTrue(certificate.valid_brunnian_witness)

    def test_point_pushing_brunnian_witness_rejects_old_suffix_word(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        right_word = ((0, 1), (0, 1))

        certificate = point_pushing_brunnian_witness_certificate(
            solution,
            cyclic_group(2),
            right_word,
            arity=2,
        )

        self.assertEqual(certificate.left_based_word, ((1, 1), (1, 1)))
        self.assertEqual(certificate.deletion_word, right_word)
        self.assertFalse(certificate.deletion_trivial)
        self.assertFalse(certificate.valid_brunnian_witness)

    def test_point_pushing_brunnian_orbit_audit_finds_relative_witness(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_brunnian_orbit_audit(
            solution,
            cyclic_group(2),
            arity=2,
        )

        self.assertFalse(audit.truncated)
        self.assertTrue(audit.found_brunnian_vertical_witness)
        self.assertFalse(audit.relative_vertical_kernel_trivial)
        self.assertEqual(audit.braid_index, 3)
        self.assertEqual(audit.detector_state_count, 64)
        self.assertEqual(audit.ybe_tuple_count, 27)
        self.assertIsNotNone(audit.detector_stabilizer_size)
        self.assertGreaterEqual(audit.detector_stabilizer_size, 1)
        self.assertFalse(audit.stabilizer_centralizes_new_action)
        self.assertEqual(audit.failure_kind, "stabilizer")
        self.assertFalse(audit.orbit_map_well_defined)
        self.assertIsNotNone(audit.detector_orbit_size)
        self.assertIsNotNone(audit.action_orbit_size)
        self.assertGreaterEqual(audit.conjugate_generator_count, audit.detector_orbit_size)
        self.assertIsNotNone(audit.witness_right_word)
        self.assertEqual(
            delete_right_based_new_strand_word(audit.witness_right_word, arity=2),
            tuple(),
        )
        self.assertEqual(
            right_based_point_pushing_word_to_left(audit.witness_right_word, arity=2),
            audit.witness_left_word,
        )
        self.assertIsNotNone(audit.moved_index)

    def test_point_pushing_brunnian_orbit_audit_records_trivial_relative_kernel(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_brunnian_orbit_audit(
            solution,
            cyclic_group(2),
            arity=2,
        )

        self.assertFalse(audit.truncated)
        self.assertIsNotNone(audit.detector_stabilizer_size)
        self.assertTrue(audit.stabilizer_centralizes_new_action)
        self.assertTrue(audit.orbit_map_well_defined)
        self.assertFalse(audit.found_brunnian_vertical_witness)
        self.assertTrue(audit.relative_vertical_kernel_trivial)
        self.assertEqual(audit.failure_kind, "none")
        self.assertEqual(audit.relative_subgroup_size, 2)
        self.assertEqual(audit.relative_detector_projection_size, 2)
        self.assertEqual(audit.relative_action_projection_size, 1)
        self.assertIsNone(audit.witness_right_word)

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

    def test_point_pushing_brunnian_gate_prefix_detects_trivial_prefix(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_brunnian_gate_prefix_audit(
            solution,
            cyclic_group(2),
            max_arity=3,
        )

        self.assertTrue(audit.prefix_detected)
        self.assertEqual(audit.checked_arities, (1, 2, 3))
        self.assertTrue(audit.base_audit.marked_quotient_holds)
        self.assertEqual(tuple(row.failure_kind for row in audit.extension_rows), ("none", "none"))
        self.assertIsNone(audit.first_failure_arity)
        self.assertIsNone(audit.first_failure_kind)

    def test_point_pushing_brunnian_gate_prefix_records_base_failure(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_brunnian_gate_prefix_audit(
            solution,
            cyclic_group(1),
            max_arity=3,
        )

        self.assertFalse(audit.prefix_detected)
        self.assertEqual(audit.checked_arities, (1,))
        self.assertFalse(audit.base_audit.marked_quotient_holds)
        self.assertEqual(audit.first_failure_arity, 1)
        self.assertEqual(audit.first_failure_kind, "base_marked_quotient")
        self.assertEqual(audit.extension_rows, tuple())

    def test_point_pushing_brunnian_tail_prefix_records_degrees(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_brunnian_tail_prefix_audit(
            solution,
            max_symmetric_degree=2,
            max_arity=2,
        )

        self.assertEqual(audit.detected_degrees, (1, 2))
        self.assertEqual(audit.unresolved_degrees, tuple())
        self.assertEqual(audit.failure_kinds, tuple())
        self.assertTrue(all(row.prefix_detected for row in audit.rows))

    def test_point_pushing_brunnian_tail_prefix_records_first_failure(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_brunnian_tail_prefix_audit(
            solution,
            max_symmetric_degree=1,
            max_arity=2,
        )

        self.assertEqual(audit.detected_degrees, tuple())
        self.assertEqual(audit.unresolved_degrees, (1,))
        self.assertEqual(audit.failure_kinds, ("base_marked_quotient",))
        self.assertEqual(audit.rows[0].first_failure_arity, 1)

    def test_point_pushing_base_arity_certificate_closes_rack_base_gate(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        certificate = point_pushing_base_arity_certificate(solution)

        self.assertEqual(certificate.tuple_count, 9)
        self.assertEqual(certificate.pure_generator_order, 3)
        self.assertEqual(certificate.symmetric_degree_bound, 3)
        self.assertEqual(certificate.symmetric_exponent % certificate.pure_generator_order, 0)
        self.assertTrue(certificate.proves_base_arity_detected)
        self.assertTrue(
            point_pushing_marked_quotient_audit(
                solution,
                cyclic_group(certificate.pure_generator_order),
                arity=1,
            ).marked_quotient_holds
        )

    def test_point_pushing_base_arity_certificate_handles_involutive_solution(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        certificate = point_pushing_base_arity_certificate(solution)

        self.assertEqual(certificate.pure_generator_order, 1)
        self.assertEqual(certificate.symmetric_degree_bound, 1)
        self.assertTrue(certificate.proves_base_arity_detected)

    def test_point_pushing_base_arity_certificate_uses_minimal_symmetric_cutoff(self):
        left = rack_solution(list(range(8)), lambda a, b: (2 * a - b) % 8)
        right = rack_solution(list(range(3)), lambda a, b: (2 * a - b) % 3)
        solution = product_solution(left, right)

        certificate = point_pushing_base_arity_certificate(solution)

        self.assertEqual(certificate.pure_generator_order, 12)
        self.assertEqual(certificate.symmetric_degree_bound, 4)
        self.assertEqual(certificate.symmetric_exponent, 12)
        self.assertTrue(certificate.proves_base_arity_detected)

    def test_point_pushing_base_free_tail_prefix_starts_at_base_cutoff(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        prefix = point_pushing_base_free_brunnian_tail_prefix(
            solution,
            max_symmetric_degree=2,
            max_arity=2,
        )

        self.assertEqual(prefix.base_cutoff, 3)
        self.assertEqual(prefix.checked_degrees, tuple())
        self.assertTrue(prefix.base_cutoff_respected)
        self.assertEqual(prefix.certified_nonbase_degrees, tuple())

    def test_point_pushing_base_free_tail_prefix_checks_after_cutoff(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        prefix = point_pushing_base_free_brunnian_tail_prefix(
            solution,
            max_symmetric_degree=2,
            max_arity=2,
        )

        self.assertEqual(prefix.base_cutoff, 1)
        self.assertEqual(prefix.checked_degrees, (1, 2))
        self.assertEqual(prefix.detected_degrees, (1, 2))
        self.assertEqual(prefix.uncertified_failure_degrees, tuple())
        self.assertTrue(prefix.base_cutoff_respected)

    def test_point_pushing_base_free_threshold_audit_detects_trivial_prefix(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_base_free_threshold_audit(
            solution,
            max_symmetric_degree=2,
            max_arity=2,
        )

        self.assertEqual(audit.base_cutoff, 1)
        self.assertFalse(audit.bound_below_base_cutoff)
        self.assertEqual(audit.checked_degrees, (1, 2))
        self.assertEqual(audit.minimal_detecting_degree, 1)
        self.assertTrue(audit.detected_within_bound)
        self.assertEqual(audit.unresolved_degrees, tuple())

    def test_point_pushing_base_free_threshold_audit_reports_low_bound(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_base_free_threshold_audit(
            solution,
            max_symmetric_degree=2,
            max_arity=2,
        )

        self.assertEqual(audit.base_cutoff, 3)
        self.assertTrue(audit.bound_below_base_cutoff)
        self.assertEqual(audit.checked_degrees, tuple())
        self.assertIsNone(audit.minimal_detecting_degree)
        self.assertFalse(audit.detected_within_bound)

    def test_point_pushing_base_free_threshold_prefix_audit_records_sequence(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_base_free_threshold_prefix_audit(
            solution,
            max_symmetric_degree=2,
            max_arity=3,
        )

        self.assertEqual(audit.base_cutoff, 1)
        self.assertEqual(audit.threshold_sequence, (1, 1, 1))
        self.assertEqual(audit.detected_arities, (1, 2, 3))
        self.assertEqual(audit.unresolved_arities, tuple())
        self.assertTrue(audit.detected_thresholds_weakly_increase)

    def test_point_pushing_base_free_threshold_prefix_audit_records_unresolved_prefix(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_base_free_threshold_prefix_audit(
            solution,
            max_symmetric_degree=2,
            max_arity=2,
        )

        self.assertEqual(audit.base_cutoff, 3)
        self.assertEqual(audit.threshold_sequence, (None, None))
        self.assertEqual(audit.detected_arities, tuple())
        self.assertEqual(audit.unresolved_arities, (1, 2))
        self.assertTrue(audit.detected_thresholds_weakly_increase)

    def test_point_pushing_brunnian_failure_certificate_records_moved_tuple(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        certificate = point_pushing_brunnian_failure_certificate(
            solution,
            cyclic_group(2),
            arity=2,
        )

        self.assertEqual(certificate.failure_kind, "stabilizer")
        self.assertTrue(certificate.has_real_failure_kind)
        self.assertIsNotNone(certificate.witness)
        self.assertTrue(certificate.valid_failure_certificate)
        self.assertEqual(certificate.witness.right_based_word, certificate.orbit_audit.witness_right_word)
        self.assertIsNotNone(certificate.witness.vertical.moved_tuple)
        self.assertNotEqual(
            certificate.witness.vertical.moved_tuple,
            certificate.witness.vertical.moved_tuple_image,
        )

    def test_point_pushing_brunnian_failure_certificate_rejects_passing_row(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        certificate = point_pushing_brunnian_failure_certificate(
            solution,
            cyclic_group(2),
            arity=2,
        )

        self.assertEqual(certificate.failure_kind, "none")
        self.assertFalse(certificate.has_real_failure_kind)
        self.assertIsNone(certificate.witness)
        self.assertFalse(certificate.valid_failure_certificate)

    def test_point_pushing_brunnian_tail_certificate_prefix_records_detected_degrees(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        prefix = point_pushing_brunnian_tail_certificate_prefix(
            solution,
            max_symmetric_degree=2,
            max_arity=2,
        )

        self.assertEqual(prefix.detected_degrees, (1, 2))
        self.assertEqual(prefix.certified_nonbase_degrees, tuple())
        self.assertEqual(prefix.uncertified_failure_degrees, tuple())
        self.assertEqual(prefix.certified_failure_kinds, tuple())
        self.assertTrue(all(row.certificate is None for row in prefix.rows))

    def test_point_pushing_brunnian_tail_certificate_prefix_keeps_base_failures_uncertified(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        prefix = point_pushing_brunnian_tail_certificate_prefix(
            solution,
            max_symmetric_degree=1,
            max_arity=2,
        )

        self.assertEqual(prefix.detected_degrees, tuple())
        self.assertEqual(prefix.certified_nonbase_degrees, tuple())
        self.assertEqual(prefix.uncertified_failure_degrees, (1,))
        self.assertEqual(prefix.rows[0].first_failure_kind, "base_marked_quotient")
        self.assertIsNone(prefix.rows[0].certificate)

    def test_point_pushing_product_prefix_first_failure_detects_trivial_prefix(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_product_prefix_first_failure_audit(
            solution,
            (cyclic_group(1), cyclic_group(2)),
            max_arity=2,
        )

        self.assertEqual(audit.prefix_count, 2)
        self.assertEqual(audit.detected_prefix_indices, (1, 2))
        self.assertEqual(audit.unresolved_prefix_indices, tuple())
        self.assertTrue(audit.first_failure_arities_weakly_increase)

    def test_point_pushing_product_prefix_first_failure_records_base_then_tail(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_product_prefix_first_failure_audit(
            solution,
            (cyclic_group(1), cyclic_group(3)),
            max_arity=2,
        )

        self.assertEqual(audit.rows[0].first_failure_arity, 1)
        self.assertEqual(audit.rows[0].first_failure_kind, "base_marked_quotient")
        self.assertNotEqual(audit.rows[1].first_failure_kind, "base_marked_quotient")
        self.assertTrue(audit.first_failure_arities_weakly_increase)

    def test_point_pushing_action_group_records_marked_action_image(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        group = point_pushing_action_group(solution, arity=1)

        self.assertEqual(len(group.elements), 3)

    def test_point_pushing_action_quotient_separation_audit_records_depths(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_action_quotient_separation_audit(
            solution,
            max_arity=1,
            max_action_group_order=8,
        )

        self.assertEqual(audit.computed_arities, (1,))
        self.assertEqual(audit.truncated_arities, tuple())
        self.assertEqual(audit.rows[0].action_group_order, 3)
        self.assertEqual(audit.rows[0].max_separating_quotient_size, 3)
        self.assertEqual(audit.prefix_separation_bound, 3)

    def test_point_pushing_action_quotient_separation_audit_truncates_large_rows(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_action_quotient_separation_audit(
            solution,
            max_arity=1,
            max_action_group_order=2,
        )

        self.assertEqual(audit.computed_arities, tuple())
        self.assertEqual(audit.truncated_arities, (1,))
        self.assertIsNone(audit.prefix_separation_bound)

    def test_point_pushing_monolithic_compression_audit_compresses_mover(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_monolithic_compression_audit(
            solution,
            ((0, 1),),
            arity=1,
            prefix_order_bound=2,
            max_action_group_order=8,
        )

        self.assertTrue(audit.action_value_nontrivial)
        self.assertEqual(audit.action_group_order, 3)
        self.assertEqual(audit.quotient_order, 3)
        self.assertEqual(audit.quotient_kernel_size, 1)
        self.assertEqual(audit.monolith_order, 3)
        self.assertEqual(audit.monolith_type, "elementary_abelian")
        self.assertEqual(audit.monolith_prime, 3)
        self.assertEqual(audit.monolith_element_orders, (3,))
        self.assertEqual(audit.monolith_centralizer_order, 3)
        self.assertEqual(audit.monolith_action_quotient_order, 1)
        self.assertEqual(audit.monolith_commutator_order, 1)
        self.assertTrue(audit.monolith_is_central)
        self.assertTrue(audit.quotient_is_monolithic)
        self.assertTrue(audit.projected_value_in_monolith)
        self.assertTrue(audit.quotient_escapes_prefix_bound)
        self.assertTrue(audit.proves_monolithic_compression)

    def test_monolith_conjugation_data_splits_noncentral_abelian_case(self):
        group = symmetric_group(3)
        normals = _normal_subgroups_bruteforce(group, max_group_order=8)
        self.assertIsNotNone(normals)
        monoliths = _minimal_normal_subgroups(group, normals)

        self.assertEqual(len(monoliths), 1)
        centralizer_order, action_order, commutator_order, is_central = (
            _monolith_conjugation_data(group, monoliths[0])
        )

        self.assertEqual(len(monoliths[0]), 3)
        self.assertEqual(centralizer_order, 3)
        self.assertEqual(action_order, 2)
        self.assertEqual(commutator_order, 3)
        self.assertFalse(is_central)

    def test_point_pushing_monolithic_compression_audit_keeps_identity_uncertified(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_monolithic_compression_audit(
            solution,
            tuple(),
            arity=1,
            max_action_group_order=8,
        )

        self.assertFalse(audit.action_value_nontrivial)
        self.assertIsNone(audit.quotient_order)
        self.assertFalse(audit.proves_monolithic_compression)

    def test_point_pushing_brunnian_normalized_prefix_audit_certifies_stabilized_row(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        audit = point_pushing_brunnian_normalized_prefix_audit(
            solution,
            symmetric_degree=2,
            arity=2,
            fill_value=0,
        )

        self.assertTrue(audit.certificate.valid_failure_certificate)
        self.assertIsNotNone(audit.normalized_prefix)
        self.assertEqual(audit.extra_strands, 2)
        self.assertTrue(audit.proves_one_symmetric_normalized_prefix)
        self.assertEqual(audit.normalized_prefix.source_n, 3)
        self.assertEqual(audit.normalized_prefix.target_n, 5)
        self.assertTrue(audit.normalized_prefix.product_invisibility_survives_stabilization)
        self.assertTrue(audit.normalized_prefix.movement_survives_stabilization)

    def test_point_pushing_brunnian_normalized_prefix_audit_keeps_nonfailures_uncertified(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        audit = point_pushing_brunnian_normalized_prefix_audit(
            solution,
            symmetric_degree=2,
            arity=2,
            fill_value=0,
        )

        self.assertFalse(audit.certificate.valid_failure_certificate)
        self.assertIsNone(audit.normalized_prefix)
        self.assertFalse(audit.proves_one_symmetric_normalized_prefix)

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

    def test_point_pushing_recursive_conjugacy_audit(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        for braid_index in (2, 3, 4):
            audit = point_pushing_recursive_conjugacy_audit(
                solution,
                braid_index=braid_index,
            )
            self.assertTrue(audit.first_generator_recursion_matches)
            self.assertTrue(audit.all_suffix_shift_generators_match)
            self.assertTrue(audit.point_pushing_recursion_verified)
            self.assertEqual(audit.tuple_count, 3**braid_index)
            self.assertIsNone(audit.first_failure_generator)

    def test_point_pushing_recursive_conjugacy_validates_braid_index(self):
        solution = rack_solution([0, 1], lambda a, b: b)

        with self.assertRaises(ValueError):
            point_pushing_recursive_conjugacy_audit(solution, braid_index=1)


if __name__ == "__main__":
    unittest.main()
