import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    DegeneratePreimageMemoryAudit,
    DerivedHurwitzEnvelopeAudit,
    EdgeMemoryTowerAudit,
    FiniteAugmentedArtinEnvelopePressureAudit,
    FiniteAugmentedArtinEnvelopePressureCase,
    FiniteAugmentedArtinEnvelopeRouteAudit,
    FiniteBraidedSet,
    PointPushingGeneratorRow,
    PrefixArtinEnvelopeCohomologyAudit,
    PrefixDeletionCubeRestrictionAudit,
    PrefixDeletionSquareRestrictionAudit,
    PrefixEdgeTransducerAudit,
    PrefixFiniteBasePullbackGaugeAudit,
    PrefixGroupHurwitzCompressionPressureAudit,
    PrefixPointForgettingRestrictionAudit,
    PrefixPointPushingSurfaceAudit,
    PullbackCoskeletalCriterionAudit,
    YBEBrunnianDerivativeGateAudit,
    YBECoskeletalMechanismAudit,
    PrefixVerticalPeifferCubeTransportAudit,
    PrefixVerticalPeifferSquareAudit,
    PrefixVerticalDefectTransportAudit,
    PrefixVerticalDefectTransformAudit,
    degenerate_preimage_memory_audit,
    derived_hurwitz_envelope_audit,
    edge_memory_tower_audit,
    finite_augmented_artin_envelope_pressure_audit,
    finite_augmented_artin_envelope_route_audit,
    prefix_deletion_cube_restriction_audit,
    prefix_deletion_square_restriction_audit,
    prefix_artin_envelope_cohomology_audit,
    prefix_edge_transducer_audit,
    prefix_finite_base_pullback_gauge_audit,
    prefix_group_hurwitz_compression_pressure_audit,
    prefix_point_forgetting_restriction_audit,
    prefix_point_pushing_surface_audit,
    prefix_vertical_peiffer_cube_transport_audit,
    prefix_vertical_peiffer_square_audit,
    prefix_vertical_defect_transport_audit,
    prefix_vertical_defect_transform_audit,
    pullback_coskeletal_criterion_audit,
    ybe_brunnian_derivative_gate_audit,
    ybe_coskeletal_mechanism_audit,
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

    def test_augmented_artin_envelope_route_records_first_pressure_tests(self):
        audit = finite_augmented_artin_envelope_route_audit()

        self.assertIsInstance(audit, FiniteAugmentedArtinEnvelopeRouteAudit)
        self.assertTrue(audit.rack_side_invariant_is_ready)
        self.assertTrue(audit.records_route_one_pressure_test)
        self.assertEqual(
            audit.remaining_theorem_lemmas,
            (
                "finite augmented Artin-envelope lemma",
                (
                    "finite rack realization of compatible augmented "
                    "Artin-envelope towers"
                ),
            ),
        )
        self.assertEqual(audit.obstruction_arities, (3, 4))
        self.assertEqual(len(audit.generator_rows), 7)
        self.assertTrue(
            all(
                isinstance(row, PointPushingGeneratorRow)
                for row in audit.generator_rows
            )
        )
        self.assertEqual(
            [
                (row.point_pushing_arity, row.generator_index, row.braid_word)
                for row in audit.generator_rows
            ],
            [
                (3, 1, (3, 2, 1, 1, -2, -3)),
                (3, 2, (3, 2, 2, -3)),
                (3, 3, (3, 3)),
                (4, 1, (4, 3, 2, 1, 1, -2, -3, -4)),
                (4, 2, (4, 3, 2, 2, -3, -4)),
                (4, 3, (4, 3, 3, -4)),
                (4, 4, (4, 4)),
            ],
        )

    def test_augmented_artin_envelope_pressure_audit_lists_mechanisms(self):
        audit = finite_augmented_artin_envelope_pressure_audit()

        self.assertIsInstance(audit, FiniteAugmentedArtinEnvelopePressureAudit)
        self.assertTrue(audit.route.records_route_one_pressure_test)
        self.assertEqual(audit.case_count, 7)
        self.assertEqual(audit.positive_obligation_count, 3)
        self.assertEqual(audit.failure_mechanism_count, 4)
        self.assertTrue(audit.records_true_or_false_mechanisms)
        self.assertTrue(
            all(
                isinstance(case, FiniteAugmentedArtinEnvelopePressureCase)
                for case in audit.cases
            )
        )
        self.assertEqual(
            audit.case_keys,
            (
                "rack_operator_conjugation_baseline",
                "translation_pair_label_candidate",
                "finite_structure_action_candidate",
                "nonconjugation_stable_label_failure",
                "ordered_neighbor_memory_failure",
                "point_forgetting_incompatibility",
                "unbounded_vertical_kernel_failure",
            ),
        )
        self.assertNotIn("whole_exponent_growth", audit.case_keys)
        self.assertEqual(
            {
                case.key
                for case in audit.cases
                if case.role == "negative_mechanism"
            },
            {
                "nonconjugation_stable_label_failure",
                "ordered_neighbor_memory_failure",
                "point_forgetting_incompatibility",
                "unbounded_vertical_kernel_failure",
            },
        )

    def test_derived_hurwitz_envelope_audit_accepts_nondegenerate_row(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = derived_hurwitz_envelope_audit(solution)

        self.assertIsInstance(audit, DerivedHurwitzEnvelopeAudit)
        self.assertTrue(audit.nondegenerate)
        self.assertTrue(audit.derived_operation_total)
        self.assertTrue(audit.derived_rack_ybe)
        self.assertTrue(audit.two_strand_guitar_conjugacy)
        self.assertTrue(audit.three_strand_guitar_conjugacy)
        self.assertFalse(audit.interior_forgetting_unaugmented_matches)
        self.assertEqual(audit.prefix_left_group_order, 2)
        self.assertEqual(audit.preimage_failure_count, 0)
        self.assertTrue(audit.proves_nondegenerate_derived_hurwitz_envelope_prefix)

    def test_derived_hurwitz_envelope_audit_rejects_left_degenerate_row(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = derived_hurwitz_envelope_audit(solution)

        self.assertFalse(audit.left_nondegenerate)
        self.assertFalse(audit.nondegenerate)
        self.assertFalse(audit.derived_operation_total)
        self.assertFalse(audit.derived_rack_ybe)
        self.assertGreater(audit.preimage_failure_count, 0)
        self.assertTrue(audit.detects_degenerate_derived_operation_failure)
        self.assertIn(
            audit.recorded_preimage_failures[0].kind,
            {"missing_preimage", "multiple_preimages_same_candidate"},
        )

    def test_degenerate_preimage_memory_audit_accepts_singleton_fibres(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = degenerate_preimage_memory_audit(solution)

        self.assertIsInstance(audit, DegeneratePreimageMemoryAudit)
        self.assertEqual(audit.edge_memory_state_count, 4)
        self.assertEqual(audit.singleton_fibre_count, 4)
        self.assertEqual(audit.missing_fibre_count, 0)
        self.assertEqual(audit.multiple_same_candidate_count, 0)
        self.assertEqual(audit.ambiguous_candidate_count, 0)
        self.assertFalse(audit.hidden_preimage_memory_needed)
        self.assertTrue(audit.visible_compression_is_safe)
        self.assertTrue(audit.records_degenerate_memory_gate)

    def test_degenerate_preimage_memory_audit_records_missing_memory_gate(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = degenerate_preimage_memory_audit(solution)

        self.assertEqual(audit.edge_memory_state_count, 4)
        self.assertEqual(audit.singleton_fibre_count, 0)
        self.assertEqual(audit.missing_fibre_count, 2)
        self.assertEqual(audit.multiple_same_candidate_count, 2)
        self.assertEqual(audit.ambiguous_candidate_count, 0)
        self.assertTrue(audit.hidden_preimage_memory_needed)
        self.assertFalse(audit.visible_compression_is_safe)
        self.assertTrue(audit.records_degenerate_memory_gate)
        self.assertEqual(
            {fibre.status for fibre in audit.recorded_fibres},
            {"missing", "multiple_same_candidate"},
        )

    def test_edge_memory_tower_audit_checks_first_tower_gates(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = edge_memory_tower_audit(solution)

        self.assertIsInstance(audit, EdgeMemoryTowerAudit)
        self.assertEqual(audit.edge_label_count, 4)
        self.assertEqual(audit.arity3_tuple_count, 8)
        self.assertEqual(audit.arity4_tuple_count, 16)
        self.assertTrue(audit.arity3_encoding_injective)
        self.assertTrue(audit.arity4_encoding_injective)
        self.assertTrue(audit.braid_relation_on_edge_memory)
        self.assertEqual(
            audit.generator_updates_well_defined,
            ((0, True), (1, True), (2, True)),
        )
        self.assertEqual(
            audit.point_forgetting_well_defined,
            ((0, True), (1, True), (2, True), (3, True)),
        )
        self.assertTrue(audit.verifies_edge_memory_triple_quadruple_prefix)

    def test_edge_memory_tower_audit_also_handles_degenerate_identity_row(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = edge_memory_tower_audit(solution)

        self.assertEqual(audit.edge_label_count, 4)
        self.assertTrue(audit.arity3_encoding_injective)
        self.assertTrue(audit.arity4_encoding_injective)
        self.assertTrue(audit.braid_relation_on_edge_memory)
        self.assertTrue(audit.all_generator_updates_well_defined)
        self.assertTrue(audit.all_point_forgetting_maps_well_defined)
        self.assertTrue(audit.verifies_edge_memory_triple_quadruple_prefix)

    def test_prefix_edge_transducer_audit_checks_left_prefix_tower(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_edge_transducer_audit(solution)

        self.assertIsInstance(audit, PrefixEdgeTransducerAudit)
        self.assertEqual(audit.element_count, 2)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.arity3_path_count, 8)
        self.assertEqual(audit.arity4_path_count, 16)
        self.assertTrue(audit.left_prefix_identity_holds)
        self.assertEqual(
            audit.generator_updates_bijective,
            ((0, True), (1, True), (2, True)),
        )
        self.assertTrue(audit.braid_relation_on_prefix_paths)
        self.assertEqual(
            audit.point_forgetting_well_defined,
            ((0, True), (1, True), (2, True), (3, True)),
        )
        self.assertTrue(
            all(
                size <= audit.element_count
                for _index, size in audit.point_forgetting_max_fibre_sizes
            )
        )
        self.assertTrue(audit.verifies_prefix_edge_transducer_prefix)

    def test_prefix_edge_transducer_audit_handles_left_degenerate_row(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_edge_transducer_audit(solution)

        self.assertEqual(audit.left_prefix_monoid_size, 3)
        self.assertGreaterEqual(audit.edge_state_count, 4)
        self.assertTrue(audit.arity3_encoding_injective)
        self.assertTrue(audit.arity4_encoding_injective)
        self.assertTrue(audit.left_prefix_identity_holds)
        self.assertTrue(audit.all_generator_updates_bijective)
        self.assertTrue(audit.all_point_forgetting_maps_well_defined)
        self.assertTrue(audit.forgetting_fibres_bounded_by_element_count)
        self.assertTrue(audit.verifies_prefix_edge_transducer_prefix)

    def test_prefix_group_hurwitz_pressure_records_group_like_prefix_case(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_group_hurwitz_compression_pressure_audit(solution)

        self.assertIsInstance(
            audit,
            PrefixGroupHurwitzCompressionPressureAudit,
        )
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertFalse(audit.faithful_prefix_monoid_group_embedding_obstructed)
        self.assertEqual(audit.local_hurwitz_label_equation_count, 8)
        self.assertEqual(audit.product_invariance_equation_count, 8)
        self.assertEqual(audit.forgetting_rescan_lumpability_equation_count, 16)
        self.assertEqual(audit.first_obstruction_arities, (3, 4))
        self.assertTrue(audit.records_group_hurwitz_compression_pressure)

    def test_prefix_group_hurwitz_pressure_detects_nonunit_prefix_monoid(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_group_hurwitz_compression_pressure_audit(solution)

        self.assertEqual(audit.left_prefix_monoid_size, 3)
        self.assertEqual(audit.nonunit_prefix_count, 2)
        self.assertTrue(audit.faithful_prefix_monoid_group_embedding_obstructed)
        self.assertEqual(audit.local_hurwitz_label_equation_count, 12)
        self.assertEqual(audit.product_invariance_equation_count, 12)
        self.assertEqual(audit.forgetting_rescan_lumpability_equation_count, 36)
        self.assertTrue(audit.records_group_hurwitz_compression_pressure)

    def test_prefix_point_pushing_surface_records_first_obstruction_rows(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_point_pushing_surface_audit(solution, max_subgroup_size=1000)

        self.assertIsInstance(audit, PrefixPointPushingSurfaceAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.checked_arities, (3, 4))
        self.assertTrue(audit.verifies_prefix_point_pushing_surface)
        self.assertEqual(
            [row.generator_braid_words for row in audit.rows],
            [
                (
                    (3, 2, 1, 1, -2, -3),
                    (3, 2, 2, -3),
                    (3, 3),
                ),
                (
                    (4, 3, 2, 1, 1, -2, -3, -4),
                    (4, 3, 2, 2, -3, -4),
                    (4, 3, 3, -4),
                    (4, 4),
                ),
            ],
        )
        self.assertEqual(
            [
                (
                    row.tuple_count,
                    row.prefix_path_count,
                    row.point_pushing_group_size,
                    row.point_pushing_group_exponent,
                )
                for row in audit.rows
            ],
            [(16, 16, 8, 2), (32, 32, 16, 2)],
        )

    def test_prefix_point_pushing_surface_handles_degenerate_identity_row(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_point_pushing_surface_audit(solution)

        self.assertEqual(audit.left_prefix_monoid_size, 3)
        self.assertEqual(audit.nonunit_prefix_count, 2)
        self.assertTrue(audit.verifies_prefix_point_pushing_surface)
        self.assertEqual(
            [
                (
                    row.tuple_count,
                    row.prefix_path_count,
                    row.point_pushing_group_size,
                    row.point_pushing_group_exponent,
                    row.generator_orders,
                )
                for row in audit.rows
            ],
            [
                (16, 16, 1, 1, (1, 1, 1)),
                (32, 32, 1, 1, (1, 1, 1, 1)),
            ],
        )

    def test_prefix_artin_envelope_cohomology_records_action_groupoid(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_artin_envelope_cohomology_audit(
            solution,
            max_subgroup_size=1000,
        )

        self.assertIsInstance(audit, PrefixArtinEnvelopeCohomologyAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.operator_label_variable_count, 4)
        self.assertEqual(audit.checked_arities, (3, 4))
        self.assertTrue(audit.records_artin_envelope_cohomology_pressure)
        self.assertTrue(audit.all_rows_untruncated)
        self.assertEqual(
            [
                (
                    row.point_pushing_group_size,
                    row.point_pushing_group_exponent,
                    row.orbit_count,
                    row.max_orbit_size,
                    row.action_groupoid_arrow_count,
                    row.stabilizer_loop_arrow_count,
                    row.generator_cocycle_value_count,
                    row.restriction_to_previous_required,
                    row.forgetting_naturality_square_count,
                )
                for row in audit.rows
            ],
            [
                (8, 2, 2, 8, 128, 16, 48, False, 0),
                (16, 2, 2, 16, 512, 32, 128, True, 512),
            ],
        )

    def test_prefix_artin_envelope_cohomology_handles_identity_action(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_artin_envelope_cohomology_audit(solution)

        self.assertEqual(audit.left_prefix_monoid_size, 3)
        self.assertEqual(audit.nonunit_prefix_count, 2)
        self.assertEqual(audit.operator_label_variable_count, 6)
        self.assertTrue(audit.records_artin_envelope_cohomology_pressure)
        self.assertEqual(
            [
                (
                    row.point_pushing_group_size,
                    row.orbit_count,
                    row.max_orbit_size,
                    row.action_groupoid_arrow_count,
                    row.stabilizer_loop_arrow_count,
                )
                for row in audit.rows
            ],
            [
                (1, 16, 1, 16, 16),
                (1, 32, 1, 32, 32),
            ],
        )

    def test_prefix_finite_base_pullback_gauge_records_trivial_prefix_class(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_finite_base_pullback_gauge_audit(
            solution,
            max_subgroup_size=10000,
        )

        self.assertIsInstance(audit, PrefixFiniteBasePullbackGaugeAudit)
        self.assertEqual(audit.translation_pair_label_count, 1)
        self.assertEqual(audit.left_translation_label_count, 1)
        self.assertEqual(audit.right_translation_label_count, 1)
        self.assertTrue(audit.crossing_descends_to_translation_pair_labels)
        self.assertEqual(audit.crossing_label_ambiguity_count, 0)
        self.assertEqual(audit.checked_arities, (3, 4, 5))
        self.assertTrue(audit.all_rows_untruncated)
        self.assertTrue(audit.all_label_actions_well_defined)
        self.assertTrue(audit.all_quotient_maps_well_defined)
        self.assertFalse(audit.all_canonical_section_gauges_trivial)
        self.assertEqual(audit.vertical_kernel_exponent_spectrum, (2,))
        self.assertEqual(audit.vertical_defect_transport_mismatch_count, 0)
        self.assertEqual(audit.vertical_defect_order_spectrum, (2, 2))
        self.assertEqual(audit.peiffer_square_nontrivial_boundary_count, 0)
        self.assertEqual(audit.peiffer_cube_transport_mismatch_count, 0)
        self.assertEqual(audit.peiffer_order_pair_spectrum, ((1, 1),))
        self.assertTrue(audit.observed_deletion_two_cocycle_gauge_trivial)
        self.assertTrue(audit.fixed_translation_pair_base_only)
        self.assertTrue(audit.group_hurwitz_realization_still_required)
        self.assertTrue(audit.records_prefix_finite_base_pullback_gauge_surface)
        self.assertEqual(
            [
                (
                    row.point_pushing_arity,
                    row.label_tuple_count,
                    row.max_label_fibre_size,
                    row.tuple_action_group_size,
                    row.label_action_group_size,
                    row.vertical_kernel_size,
                    row.vertical_kernel_exponent,
                    row.canonical_section_displacement_count,
                )
                for row in audit.rows
            ],
            [
                (3, 1, 16, 8, 1, 8, 2, 3),
                (4, 1, 32, 16, 1, 16, 2, 4),
                (5, 1, 64, 32, 1, 32, 2, 5),
            ],
        )

    def test_prefix_finite_base_pullback_gauge_handles_identity_base(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_finite_base_pullback_gauge_audit(solution)

        self.assertTrue(audit.records_prefix_finite_base_pullback_gauge_surface)
        self.assertEqual(audit.translation_pair_label_count, 2)
        self.assertEqual(audit.left_translation_label_count, 2)
        self.assertEqual(audit.right_translation_label_count, 2)
        self.assertEqual(audit.vertical_kernel_exponent_spectrum, (1,))
        self.assertEqual(audit.vertical_defect_order_spectrum, (1, 1))
        self.assertTrue(audit.observed_deletion_two_cocycle_gauge_trivial)
        self.assertTrue(audit.all_canonical_section_gauges_trivial)
        self.assertEqual(
            [
                (
                    row.point_pushing_arity,
                    row.label_tuple_count,
                    row.max_label_fibre_size,
                    row.tuple_action_group_size,
                    row.label_action_group_size,
                    row.vertical_kernel_size,
                    row.vertical_kernel_exponent,
                    row.canonical_section_displacement_count,
                )
                for row in audit.rows
            ],
            [
                (3, 16, 1, 1, 1, 1, 1, 0),
                (4, 32, 1, 1, 1, 1, 1, 0),
                (5, 64, 1, 1, 1, 1, 1, 0),
            ],
        )

    def test_pullback_coskeletal_criterion_separates_compactness_from_cutoff(self):
        audit = pullback_coskeletal_criterion_audit()

        self.assertIsInstance(audit, PullbackCoskeletalCriterionAudit)
        self.assertTrue(audit.records_pullback_coskeletal_route_boundary)
        self.assertTrue(audit.fixed_base_inverse_limit_compactness_recorded)
        self.assertTrue(
            audit.uniform_bounded_arity_cutoff_rejected_without_extra_hypothesis
        )
        self.assertTrue(audit.pullback_coskeletal_hypothesis_identified)
        self.assertTrue(audit.finite_obstruction_certificate_identified)
        self.assertEqual(
            audit.case_keys,
            (
                "fixed_base_inverse_limit",
                "bounded_cutoff_requires_coskeletality",
                "finite_obstruction_certificate",
                "general_uniform_cutoff_failure",
            ),
        )
        self.assertIn("d-pullback-coskeletal", audit.missing_pullback_coskeletal_lemma)
        self.assertEqual(
            [case.role for case in audit.cases],
            [
                "valid_compactness_principle",
                "missing_positive_hypothesis",
                "valid_negative_certificate_for_fixed_base",
                "warning_countermechanism",
            ],
        )

    def test_ybe_coskeletal_mechanism_records_live_high_arity_obstruction(self):
        audit = ybe_coskeletal_mechanism_audit()

        self.assertIsInstance(audit, YBECoskeletalMechanismAudit)
        self.assertTrue(audit.records_ybe_coskeletal_mechanism_boundary)
        self.assertTrue(audit.finite_bijectivity_gives_local_generation)
        self.assertTrue(
            audit.finite_bijectivity_does_not_give_local_cohomology_detection
        )
        self.assertTrue(audit.bounded_state_recursion_would_imply_coskeletality)
        self.assertTrue(audit.high_cross_effect_bisections_are_live_obstruction)
        self.assertTrue(audit.w_local_operator_label_descent_is_extra_hypothesis)
        self.assertTrue(audit.coefficient_inverse_limit_condition_recorded)
        self.assertTrue(audit.comparison_commutes_with_inverse_limits_recorded)
        self.assertTrue(audit.bounded_relation_arity_cutoff_recorded)
        self.assertTrue(audit.brunnian_cross_effect_criterion_recorded)
        self.assertEqual(audit.cutoff_formula, "N0 = max(r, w + 3)")
        self.assertIn("Omega", audit.conditional_pullback_coskeletal_theorem)
        self.assertIn("Pi^sharp", audit.conditional_pullback_coskeletal_theorem)
        self.assertIn("cr_ij^I", audit.brunnian_cross_effect_formula)
        self.assertIn("Br^2_I", audit.brunnian_obstruction_criterion)
        self.assertEqual(len(audit.positive_ybe_theorem_obligations), 4)
        self.assertEqual(
            audit.case_keys,
            (
                "formal_w_local_descent_theorem",
                "fadell_neuwirth_recursion",
                "finite_operator_state_recursion",
                "garside_or_automaton_normal_forms",
                "fi_fb_finite_generation",
                "brunnian_cross_effect_obstruction",
            ),
        )
        self.assertEqual(
            audit.cases[0].role,
            "conditional_positive_theorem",
        )
        self.assertEqual(
            audit.cases[-1].role,
            "negative_countermechanism",
        )
        self.assertIn("d-skeleton", audit.cases[-1].obstruction_signature)

    def test_ybe_brunnian_derivative_gate_rejects_naive_pure_braid_obstruction(self):
        audit = ybe_brunnian_derivative_gate_audit()

        self.assertIsInstance(audit, YBEBrunnianDerivativeGateAudit)
        self.assertTrue(audit.records_brunnian_derivative_gate)
        self.assertTrue(audit.naive_brunnian_pure_braid_obstruction_rejected)
        self.assertTrue(audit.one_strand_derivatives_are_gauge_coboundaries)
        self.assertTrue(audit.brunnian_point_push_shadow_is_gauge)
        self.assertTrue(audit.nonabelian_derivative_chain_rule_recorded)
        self.assertTrue(audit.residual_double_deletion_quotient_identified)
        self.assertTrue(
            audit.fadell_neuwirth_decomposition_would_kill_high_brunnian_classes
        )
        self.assertEqual(
            audit.derivative_formula,
            "nabla_q b = tau_q(b) inf_q(partial_q b)^-1",
        )
        self.assertEqual(
            audit.gauge_formula,
            "(delta u)_{p,q}^I = nabla_q b",
        )
        self.assertIn("R_{p,q}^I", audit.residual_quotient_formula)
        self.assertIn("Pi^sharp(theta)", audit.decomposition_formula)
        self.assertEqual(
            audit.case_keys,
            (
                "one_strand_derivative_gauge_gate",
                "pure_braid_brunnian_shadow_triviality",
                "nonabelian_derivative_chain_rule",
                "residual_double_deletion_quotient",
                "fadell_neuwirth_decomposition_route",
            ),
        )

    def test_prefix_point_forgetting_restriction_records_vertical_rows(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_point_forgetting_restriction_audit(solution)

        self.assertIsInstance(audit, PrefixPointForgettingRestrictionAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.row_count, 16)
        self.assertTrue(audit.verifies_first_point_forgetting_restriction_surface)
        self.assertTrue(audit.off_diagonal_all_match)
        self.assertFalse(audit.all_rows_match)
        self.assertEqual(audit.total_mismatch_count, 128)
        self.assertEqual(audit.diagonal_mismatch_count, 128)
        diagonal_rows = tuple(
            row
            for row in audit.rows
            if row.diagonal_forgetting_row
        )
        self.assertEqual(len(diagonal_rows), 4)
        self.assertTrue(
            all(
                row.expected_identity_after_forgetting
                and row.target_generator_index is None
                and row.mismatch_count == 32
                and row.first_witness_input == (0, 0, 0, 0, 0)
                and row.first_deleted_after_source == (0, 0, 0, 1)
                and row.first_expected_target == (0, 0, 0, 0)
                for row in diagonal_rows
            )
        )

    def test_prefix_point_forgetting_restriction_identity_row_is_trivial(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_point_forgetting_restriction_audit(solution)

        self.assertEqual(audit.left_prefix_monoid_size, 3)
        self.assertEqual(audit.nonunit_prefix_count, 2)
        self.assertTrue(audit.verifies_first_point_forgetting_restriction_surface)
        self.assertTrue(audit.all_rows_match)
        self.assertEqual(audit.total_mismatch_count, 0)
        self.assertTrue(
            all(
                row.first_witness_input is None
                and row.first_deleted_after_source is None
                and row.first_expected_target is None
                for row in audit.rows
            )
        )

    def test_prefix_deletion_square_restriction_records_two_face_rows(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_deletion_square_restriction_audit(solution)

        self.assertIsInstance(audit, PrefixDeletionSquareRestrictionAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.source_point_pushing_arity, 5)
        self.assertEqual(audit.target_point_pushing_arity, 3)
        self.assertEqual(audit.row_count, 50)
        self.assertTrue(audit.verifies_first_deletion_square_surface)
        self.assertTrue(audit.deletion_orders_all_commute)
        self.assertTrue(audit.surviving_generator_all_match)
        self.assertFalse(audit.all_rows_match)
        self.assertEqual(audit.total_mismatch_count, 1280)
        self.assertEqual(audit.deleted_generator_mismatch_count, 1280)
        deleted_rows = tuple(
            row
            for row in audit.rows
            if row.source_generator_deleted
        )
        surviving_rows = tuple(
            row
            for row in audit.rows
            if not row.source_generator_deleted
        )
        self.assertEqual(len(deleted_rows), 20)
        self.assertEqual(len(surviving_rows), 30)
        self.assertTrue(all(row.mismatch_count == 64 for row in deleted_rows))
        self.assertTrue(all(row.mismatch_count == 0 for row in surviving_rows))
        first_row = deleted_rows[0]
        self.assertEqual(first_row.forget_stationary_indices, (1, 2))
        self.assertEqual(first_row.source_generator_index, 1)
        self.assertIsNone(first_row.target_generator_index)
        self.assertEqual(first_row.first_witness_input, (0, 0, 0, 0, 0, 0))
        self.assertEqual(first_row.first_deleted_after_source, (0, 0, 0, 1))
        self.assertEqual(first_row.first_expected_target, (0, 0, 0, 0))

    def test_prefix_deletion_square_restriction_identity_row_is_trivial(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_deletion_square_restriction_audit(solution)

        self.assertEqual(audit.left_prefix_monoid_size, 3)
        self.assertEqual(audit.nonunit_prefix_count, 2)
        self.assertTrue(audit.verifies_first_deletion_square_surface)
        self.assertTrue(audit.deletion_orders_all_commute)
        self.assertTrue(audit.all_rows_match)
        self.assertEqual(audit.total_mismatch_count, 0)
        self.assertTrue(
            all(
                row.first_witness_input is None
                and row.first_deleted_after_source is None
                and row.first_expected_target is None
                for row in audit.rows
            )
        )

    def test_prefix_deletion_cube_restriction_records_three_face_rows(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_deletion_cube_restriction_audit(solution)

        self.assertIsInstance(audit, PrefixDeletionCubeRestrictionAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.source_point_pushing_arity, 5)
        self.assertEqual(audit.target_point_pushing_arity, 2)
        self.assertEqual(audit.row_count, 50)
        self.assertTrue(audit.verifies_first_deletion_cube_surface)
        self.assertTrue(audit.deletion_orders_all_commute)
        self.assertTrue(audit.surviving_generator_all_match)
        self.assertFalse(audit.all_rows_match)
        self.assertEqual(audit.total_mismatch_count, 1920)
        self.assertEqual(audit.deleted_generator_mismatch_count, 1920)
        deleted_rows = tuple(
            row
            for row in audit.rows
            if row.source_generator_deleted
        )
        surviving_rows = tuple(
            row
            for row in audit.rows
            if not row.source_generator_deleted
        )
        self.assertEqual(len(deleted_rows), 30)
        self.assertEqual(len(surviving_rows), 20)
        self.assertTrue(all(row.deletion_order_count == 6 for row in audit.rows))
        self.assertTrue(all(row.mismatch_count == 64 for row in deleted_rows))
        self.assertTrue(all(row.mismatch_count == 0 for row in surviving_rows))
        first_row = deleted_rows[0]
        self.assertEqual(first_row.forget_stationary_indices, (1, 2, 3))
        self.assertEqual(first_row.source_generator_index, 1)
        self.assertIsNone(first_row.target_generator_index)
        self.assertEqual(first_row.first_witness_input, (0, 0, 0, 0, 0, 0))
        self.assertEqual(first_row.first_deleted_after_source, (0, 0, 1))
        self.assertEqual(first_row.first_expected_target, (0, 0, 0))

    def test_prefix_deletion_cube_restriction_identity_row_is_trivial(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_deletion_cube_restriction_audit(solution)

        self.assertEqual(audit.left_prefix_monoid_size, 3)
        self.assertEqual(audit.nonunit_prefix_count, 2)
        self.assertTrue(audit.verifies_first_deletion_cube_surface)
        self.assertTrue(audit.deletion_orders_all_commute)
        self.assertTrue(audit.all_rows_match)
        self.assertEqual(audit.total_mismatch_count, 0)
        self.assertTrue(
            all(
                row.first_witness_input is None
                and row.first_deleted_after_source is None
                and row.first_expected_target is None
                for row in audit.rows
            )
        )

    def test_prefix_vertical_defect_transform_extracts_order_two_rows(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_vertical_defect_transform_audit(solution)

        self.assertIsInstance(audit, PrefixVerticalDefectTransformAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.row_count, 54)
        self.assertTrue(audit.verifies_vertical_defect_transform_extraction)
        self.assertTrue(audit.all_defects_well_defined)
        self.assertTrue(audit.all_defects_are_permutations)
        self.assertEqual(audit.nontrivial_defect_count, 54)
        self.assertEqual(audit.order_spectrum, (2,))
        self.assertEqual(
            [
                (
                    row.deletion_level,
                    row.target_braid_index,
                    row.target_tuple_count,
                    row.defect_order,
                    row.identity_defect,
                    row.ambiguous_deleted_tuple_count,
                    row.max_outputs_per_deleted_tuple,
                )
                for row in audit.rows[:5]
            ],
            [
                (1, 4, 16, 2, False, 0, 1),
                (1, 4, 16, 2, False, 0, 1),
                (1, 4, 16, 2, False, 0, 1),
                (1, 4, 16, 2, False, 0, 1),
                (2, 4, 16, 2, False, 0, 1),
            ],
        )
        self.assertEqual(
            {
                deletion_level: len(
                    {
                        row.defect_permutation
                        for row in audit.rows
                        if row.deletion_level == deletion_level
                    }
                )
                for deletion_level in (1, 2, 3)
            },
            {1: 1, 2: 1, 3: 1},
        )

    def test_prefix_vertical_defect_transform_identity_rows_are_trivial(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_vertical_defect_transform_audit(solution)

        self.assertEqual(audit.left_prefix_monoid_size, 3)
        self.assertEqual(audit.nonunit_prefix_count, 2)
        self.assertTrue(audit.verifies_vertical_defect_transform_extraction)
        self.assertEqual(audit.nontrivial_defect_count, 0)
        self.assertEqual(audit.order_spectrum, (1,))
        self.assertTrue(all(row.identity_defect for row in audit.rows))

    def test_prefix_vertical_defect_transport_commutes_for_order_two_rows(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_vertical_defect_transport_audit(solution)

        self.assertIsInstance(audit, PrefixVerticalDefectTransportAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.row_count, 80)
        self.assertTrue(audit.verifies_first_vertical_defect_face_transport)
        self.assertTrue(audit.all_additional_faces_surjective)
        self.assertTrue(audit.all_defects_are_transportable)
        self.assertTrue(audit.all_transports_commute)
        self.assertEqual(audit.total_mismatch_count, 0)
        self.assertEqual(audit.order_pair_spectrum, ((2, 2),))
        self.assertEqual(
            {
                (row.from_deletion_level, row.to_deletion_level): sum(
                    1
                    for other in audit.rows
                    if (
                        other.from_deletion_level,
                        other.to_deletion_level,
                    )
                    == (row.from_deletion_level, row.to_deletion_level)
                )
                for row in audit.rows
            },
            {(1, 2): 20, (2, 3): 60},
        )
        self.assertTrue(
            all(
                row.first_witness_target_input is None
                and row.first_left_after_defect_then_delete is None
                and row.first_right_after_delete_then_defect is None
                for row in audit.rows
            )
        )

    def test_prefix_vertical_defect_transport_identity_rows_are_trivial(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_vertical_defect_transport_audit(solution)

        self.assertTrue(audit.verifies_first_vertical_defect_face_transport)
        self.assertEqual(audit.total_mismatch_count, 0)
        self.assertEqual(audit.order_pair_spectrum, ((1, 1),))
        self.assertTrue(
            all(
                row.from_identity_defect
                and row.to_identity_defect
                and row.transport_commutes
                for row in audit.rows
            )
        )

    def test_prefix_vertical_peiffer_square_boundary_is_trivial_for_prefix_rows(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_vertical_peiffer_square_audit(solution)

        self.assertIsInstance(audit, PrefixVerticalPeifferSquareAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.row_count, 10)
        self.assertTrue(audit.verifies_first_vertical_peiffer_square_boundary)
        self.assertTrue(audit.all_defects_are_permutations)
        self.assertTrue(audit.all_single_transports_commute)
        self.assertTrue(audit.all_peiffer_boundaries_identity)
        self.assertEqual(audit.nontrivial_peiffer_boundary_count, 0)
        self.assertEqual(audit.total_peiffer_moved_tuple_count, 0)
        self.assertEqual(audit.defect_order_pair_spectrum, ((2, 2),))
        self.assertEqual(audit.peiffer_order_spectrum, (1,))
        self.assertTrue(
            all(
                row.first_witness_target_input is None
                and row.first_witness_after_commutator is None
                for row in audit.rows
            )
        )

    def test_prefix_vertical_peiffer_square_identity_rows_are_trivial(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_vertical_peiffer_square_audit(solution)

        self.assertTrue(audit.verifies_first_vertical_peiffer_square_boundary)
        self.assertTrue(audit.all_peiffer_boundaries_identity)
        self.assertEqual(audit.nontrivial_peiffer_boundary_count, 0)
        self.assertEqual(audit.total_peiffer_moved_tuple_count, 0)
        self.assertEqual(audit.defect_order_pair_spectrum, ((1, 1),))
        self.assertEqual(audit.peiffer_order_spectrum, (1,))

    def test_prefix_vertical_peiffer_cube_transport_is_trivial_for_prefix_rows(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (1, 0),
                (0, 1): (0, 0),
                (1, 0): (1, 1),
                (1, 1): (0, 1),
            },
        )

        audit = prefix_vertical_peiffer_cube_transport_audit(solution)

        self.assertIsInstance(audit, PrefixVerticalPeifferCubeTransportAudit)
        self.assertEqual(audit.left_prefix_monoid_size, 2)
        self.assertEqual(audit.nonunit_prefix_count, 0)
        self.assertEqual(audit.row_count, 30)
        self.assertTrue(audit.verifies_first_vertical_peiffer_cube_transport)
        self.assertTrue(audit.all_peiffer_boundaries_transportable)
        self.assertTrue(audit.all_peiffer_transports_commute)
        self.assertTrue(audit.all_pair_peiffer_boundaries_identity)
        self.assertTrue(audit.all_triple_peiffer_boundaries_identity)
        self.assertEqual(audit.total_mismatch_count, 0)
        self.assertEqual(audit.total_pair_peiffer_moved_tuple_count, 0)
        self.assertEqual(audit.total_triple_peiffer_moved_tuple_count, 0)
        self.assertEqual(audit.peiffer_order_pair_spectrum, ((1, 1),))
        self.assertEqual(
            {
                row.triple_forget_stationary_indices: sum(
                    1
                    for other in audit.rows
                    if other.triple_forget_stationary_indices
                    == row.triple_forget_stationary_indices
                )
                for row in audit.rows
            },
            {
                (1, 2, 3): 3,
                (1, 2, 4): 3,
                (1, 2, 5): 3,
                (1, 3, 4): 3,
                (1, 3, 5): 3,
                (1, 4, 5): 3,
                (2, 3, 4): 3,
                (2, 3, 5): 3,
                (2, 4, 5): 3,
                (3, 4, 5): 3,
            },
        )
        self.assertTrue(
            all(
                row.first_witness_pair_target_input is None
                and row.first_left_after_pair_peiffer_then_delete is None
                and row.first_right_after_delete_then_triple_peiffer is None
                for row in audit.rows
            )
        )

    def test_prefix_vertical_peiffer_cube_transport_identity_rows_are_trivial(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )

        audit = prefix_vertical_peiffer_cube_transport_audit(solution)

        self.assertTrue(audit.verifies_first_vertical_peiffer_cube_transport)
        self.assertEqual(audit.total_mismatch_count, 0)
        self.assertEqual(audit.total_pair_peiffer_moved_tuple_count, 0)
        self.assertEqual(audit.total_triple_peiffer_moved_tuple_count, 0)
        self.assertEqual(audit.peiffer_order_pair_spectrum, ((1, 1),))
        self.assertTrue(
            all(
                row.pair_peiffer_identity
                and row.triple_peiffer_identity
                and row.peiffer_transport_commutes
                for row in audit.rows
            )
        )


if __name__ == "__main__":
    unittest.main()
