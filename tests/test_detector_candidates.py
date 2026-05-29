import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    QuotientMap,
    commutator,
    cyclic_group,
    detector_collision_failures,
    exact_detector_image_audit,
    exact_detector_product_readout_audit,
    exact_detector_readout_audit,
    first_moved_tuple,
    free_word_power,
    bounded_words,
    identity_solution,
    invisible_to_all_groups,
    kernel_action_groups,
    kernel_symmetric_groups,
    law_word_on_last_strand,
    longitude_subgroup_mover_profiles,
    permutation_group_from_generators,
    residual_detector_blind_movers,
    residual_detector_dependency_failures,
    residual_longitude_subgroup_mover_profiles,
    rack_solution,
    symmetric_detector_readout_audit,
    symmetric_group,
    two_strand_crossing_order,
    two_strand_cyclic_detector_certificate,
    two_strand_group_detector_failure_certificate,
    two_strand_group_detector_covers_solution,
    two_strand_symmetric_detector_failure_certificate,
    two_strand_symmetric_detector_covers_solution,
    two_sided_kernel_symmetric_groups,
)


def size_three_affine_candidate():
    pairs = [(x, y) for x in range(3) for y in range(3)]
    values = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 2),
        (0, 2),
        (1, 2),
        (1, 1),
        (2, 1),
        (0, 1),
    ]
    return FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, values)))


class DetectorCandidateTests(unittest.TestCase):
    def test_permutation_group_from_generators(self):
        group = permutation_group_from_generators(((1, 2, 0),), degree=3)
        self.assertEqual(len(group.elements), 3)
        self.assertEqual(group.identity, (0, 1, 2))

    def test_actual_kernel_group_is_too_small_for_affine_commutator(self):
        solution = size_three_affine_candidate()
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        n, braid = law_word_on_last_strand(word, arity=2)
        actual_groups = kernel_action_groups(solution)
        self.assertEqual([len(group.elements) for group in actual_groups], [3])
        self.assertTrue(invisible_to_all_groups(actual_groups, n, braid))
        self.assertIsNotNone(first_moved_tuple(solution, n, braid))

    def test_symmetric_kernel_group_sees_affine_commutator(self):
        solution = size_three_affine_candidate()
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        n, braid = law_word_on_last_strand(word, arity=2)
        symmetric_groups = kernel_symmetric_groups(solution, max_degree=3)
        self.assertEqual([len(group.elements) for group in symmetric_groups], [6])
        self.assertFalse(invisible_to_all_groups(symmetric_groups, n, braid))

    def test_two_sided_symmetric_kernel_groups_deduplicate_affine_candidate(self):
        solution = size_three_affine_candidate()
        groups = two_sided_kernel_symmetric_groups(solution, max_degree=3)
        self.assertEqual([len(group.elements) for group in groups], [6])

    def test_two_strand_detector_gate_for_standard_examples(self):
        rack = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        affine = size_three_affine_candidate()

        self.assertEqual(two_strand_crossing_order(rack), 3)
        self.assertEqual(two_strand_crossing_order(affine), 3)
        self.assertTrue(two_strand_symmetric_detector_covers_solution(rack))
        self.assertTrue(two_strand_symmetric_detector_covers_solution(affine))
        self.assertFalse(two_strand_group_detector_covers_solution(rack, cyclic_group(2)))
        self.assertTrue(two_strand_group_detector_covers_solution(rack, symmetric_group(3)))

    def test_two_strand_detector_failure_certificate_records_mover(self):
        rack = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        certificate = two_strand_group_detector_failure_certificate(
            rack,
            cyclic_group(2),
        )

        self.assertIsNotNone(certificate)
        self.assertEqual(certificate.group_order, 2)
        self.assertEqual(certificate.longitude_period, 4)
        self.assertEqual(certificate.crossing_order, 3)
        self.assertEqual(certificate.braid_word, (1, 1, 1, 1))
        self.assertTrue(certificate.braid_is_group_longitude_invisible)
        self.assertTrue(certificate.braid_moves_solution)
        self.assertTrue(certificate.proves_group_detector_failure)
        self.assertEqual(
            rack.braid_action(certificate.braid_word, certificate.moved[0]),
            certificate.moved[1],
        )

    def test_two_strand_cyclic_detector_certificate_covers_crossing_order(self):
        rack = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)

        certificate = two_strand_cyclic_detector_certificate(rack)

        self.assertEqual(certificate.crossing_order, 3)
        self.assertEqual(certificate.group_order, 3)
        self.assertEqual(certificate.longitude_period, 6)
        self.assertTrue(certificate.kernel_containment_holds)
        self.assertTrue(
            two_strand_group_detector_covers_solution(
                rack,
                certificate.detector_group,
            )
        )
        self.assertIsNone(
            two_strand_group_detector_failure_certificate(
                rack,
                certificate.detector_group,
            )
        )

    def test_two_strand_symmetric_failure_certificate_is_none_when_gate_passes(self):
        rack = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        affine = size_three_affine_candidate()

        self.assertIsNone(two_strand_symmetric_detector_failure_certificate(rack))
        self.assertIsNone(two_strand_symmetric_detector_failure_certificate(affine))

    def test_residual_detector_blind_movers_respects_base_kernel(self):
        solution = size_three_affine_candidate()
        quotient = identity_solution(["*"])
        qmap = QuotientMap(solution, quotient, {element: "*" for element in solution.elements})
        symmetric_groups = kernel_symmetric_groups(solution, max_degree=3)
        failures = residual_detector_blind_movers(
            qmap,
            quotient,
            symmetric_groups,
            3,
            bounded_words(3, 2),
        )
        self.assertEqual(failures, {})

    def test_residual_detector_dependency_failures_classify_multi_input_motion(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(solution, quotient, {element: "*" for element in solution.elements})

        failures = residual_detector_dependency_failures(
            qmap,
            quotient,
            (cyclic_group(1),),
            2,
            [(1,), (1, 1)],
        )

        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0].braid_word, (1, 1))
        self.assertTrue(failures[0].has_multi_input_support)
        self.assertGreaterEqual(failures[0].max_arity, 2)

    def test_longitude_subgroup_mover_profiles_record_invisible_mover(self):
        solution = size_three_affine_candidate()
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        n, braid = law_word_on_last_strand(word, arity=2)

        profiles = longitude_subgroup_mover_profiles(
            solution,
            {"C3": cyclic_group(3)},
            n,
            [braid],
            require_invisible=True,
        )

        self.assertEqual(len(profiles), 1)
        self.assertEqual(profiles[0].braid_word, tuple(braid))
        self.assertTrue(profiles[0].all_groups_invisible)
        self.assertEqual(profiles[0].subgroup_profile[0].subgroup_size, 1)
        self.assertIsNotNone(profiles[0].moved)

    def test_longitude_subgroup_mover_profiles_record_visible_group(self):
        solution = size_three_affine_candidate()
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        n, braid = law_word_on_last_strand(word, arity=2)

        profiles = longitude_subgroup_mover_profiles(
            solution,
            {"S3": symmetric_group(3)},
            n,
            [braid],
            require_invisible=False,
        )

        self.assertEqual(len(profiles), 1)
        self.assertFalse(profiles[0].all_groups_invisible)
        self.assertEqual(profiles[0].visible_group_names, ("S3",))

    def test_residual_longitude_subgroup_mover_profiles(self):
        solution = size_three_affine_candidate()
        quotient = identity_solution(["*"])
        qmap = QuotientMap(solution, quotient, {element: "*" for element in solution.elements})
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        n, braid = law_word_on_last_strand(word, arity=2)

        profiles = residual_longitude_subgroup_mover_profiles(
            qmap,
            quotient,
            {"C3": cyclic_group(3)},
            n,
            [braid],
            require_invisible=True,
        )

        self.assertEqual(len(profiles), 1)
        self.assertEqual(profiles[0].moved[0], tuple("*" for _ in range(n)))
        self.assertTrue(profiles[0].all_groups_invisible)
        self.assertEqual(profiles[0].subgroup_profile[0].subgroup_size, 1)

    def test_detector_collision_failures_find_none_for_short_affine_scan(self):
        solution = size_three_affine_candidate()
        quotient = identity_solution(["*"])
        qmap = QuotientMap(solution, quotient, {element: "*" for element in solution.elements})
        failures = detector_collision_failures(
            qmap,
            quotient,
            kernel_symmetric_groups(solution, max_degree=3),
            3,
            bounded_words(3, 2),
        )
        self.assertEqual(failures, ())

    def test_exact_detector_image_audit_for_affine_candidate_n2(self):
        solution = size_three_affine_candidate()
        quotient = identity_solution(["*"])
        qmap = QuotientMap(solution, quotient, {element: "*" for element in solution.elements})
        audit = exact_detector_image_audit(
            qmap,
            quotient,
            kernel_symmetric_groups(solution, max_degree=3),
            2,
            state_limit=1000,
        )
        self.assertFalse(audit.truncated)
        self.assertEqual(audit.visited_state_count, 12)
        self.assertEqual(audit.detector_state_count, 12)
        self.assertEqual(audit.residual_state_count, 3)
        self.assertEqual(audit.base_kernel_detector_state_count, 12)
        self.assertEqual(audit.base_kernel_residual_state_count, 3)
        self.assertTrue(audit.proves_fixed_n_implication)
        self.assertIsNone(audit.kernel_failure)
        self.assertIsNone(audit.collision_failure)

    def test_exact_detector_readout_audit_materializes_fixed_n_readout(self):
        solution = size_three_affine_candidate()
        quotient = identity_solution(["*"])
        qmap = QuotientMap(solution, quotient, {element: "*" for element in solution.elements})

        audit = exact_detector_readout_audit(
            qmap,
            quotient,
            kernel_symmetric_groups(solution, max_degree=3),
            2,
            state_limit=1000,
        )

        self.assertFalse(audit.truncated)
        self.assertTrue(audit.proves_fixed_n_readout)
        self.assertEqual(audit.readout_state_count, audit.base_kernel_detector_state_count)
        self.assertEqual(audit.readout_state_count, 12)
        self.assertEqual(audit.base_kernel_residual_state_count, 3)
        self.assertEqual(audit.readout_rows[0].representative_braid_word, ())
        self.assertEqual(audit.readout_rows[0].residual_permutation, tuple(range(9)))
        self.assertTrue(
            all(row.preserves_quotient_fibres for row in audit.readout_rows)
        )
        self.assertEqual(audit.readout_rows[0].moved_base_tuple_count, 0)
        self.assertEqual(audit.readout_rows[0].moved_total_tuple_count, 0)
        self.assertGreater(
            max(row.moved_total_tuple_count for row in audit.readout_rows),
            0,
        )

    def test_exact_detector_readout_audit_records_missing_detector_failure(self):
        solution = size_three_affine_candidate()
        quotient = identity_solution(["*"])
        qmap = QuotientMap(solution, quotient, {element: "*" for element in solution.elements})

        audit = exact_detector_readout_audit(qmap, quotient, (), 2, state_limit=1000)

        self.assertFalse(audit.truncated)
        self.assertFalse(audit.proves_fixed_n_readout)
        self.assertEqual(audit.kernel_failure, (1,))
        self.assertEqual(audit.collision_failure, ((), (1,)))

    def test_exact_detector_product_readout_matches_factor_list(self):
        solution = identity_solution(["*"])
        qmap = QuotientMap(solution, solution, {"*": "*"})

        audit = exact_detector_product_readout_audit(
            qmap,
            solution,
            (cyclic_group(2), cyclic_group(3)),
            2,
            state_limit=1000,
        )

        self.assertFalse(audit.product_skipped)
        self.assertEqual(audit.factor_orders, (2, 3))
        self.assertEqual(audit.product_group_order, 6)
        self.assertTrue(audit.product_readout_equivalent_when_enumerated)
        self.assertEqual(
            audit.factor_audit.proves_fixed_n_readout,
            audit.product_audit.proves_fixed_n_readout,
        )
        self.assertEqual(audit.factor_residual_readouts, audit.product_residual_readouts)

    def test_exact_detector_product_readout_can_skip_large_product(self):
        solution = identity_solution(["*"])
        qmap = QuotientMap(solution, solution, {"*": "*"})

        audit = exact_detector_product_readout_audit(
            qmap,
            solution,
            (cyclic_group(2), cyclic_group(3)),
            2,
            max_product_order=5,
        )

        self.assertTrue(audit.product_skipped)
        self.assertIsNone(audit.product_audit)
        self.assertIsNone(audit.product_readout_equivalent_when_enumerated)

    def test_symmetric_detector_readout_audit_uses_one_point_quotient(self):
        solution = size_three_affine_candidate()

        audit = symmetric_detector_readout_audit(solution, 2, state_limit=1000)

        self.assertFalse(audit.truncated)
        self.assertTrue(audit.proves_fixed_n_readout)
        self.assertEqual(audit.readout_state_count, 12)
        self.assertEqual(audit.base_kernel_residual_state_count, 3)
        self.assertTrue(
            all(row.preserves_quotient_fibres for row in audit.readout_rows)
        )
        self.assertGreater(
            max(row.moved_total_tuple_count for row in audit.readout_rows),
            0,
        )


if __name__ == "__main__":
    unittest.main()
