import sys
import unittest
from math import factorial
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    AdjacentTwoBodyRealizationAudit,
    QuotientMap,
    RightStabilizationLongitudeAudit,
    TransformationMonoid,
    LocalNormalizedLawPrefixWitnessAudit,
    BraidLocalityShadowAudit,
    LabeledPermutationBraidAudit,
    ReesRectangleCocycleAudit,
    UnitPerfectResidualLongitudeAudit,
    aperiodic_permutation_audit,
    adjacent_two_body_realization_audit,
    braid_locality_shadow_audit,
    compose_transformation_word,
    cyclic_group,
    identity_solution,
    is_aperiodic_element,
    is_aperiodic_monoid,
    is_permutation_transformation,
    labeled_permutation_braid_audit,
    local_normalized_law_prefix_witness_audit,
    local_symmetric_normalized_law_prefix_witness_audit,
    monoid_permutation_group,
    permutation_elements,
    permutation_fixed_partitions,
    pure_braid_generator,
    rack_solution,
    rees_rectangle_cocycle,
    rees_rectangle_cocycle_audit,
    transformation_power,
    unit_composite_abelianization_audit,
    unit_composite_detection_audit,
    unit_composite_derived_series_lift_audit,
    unit_composite_longitude_expression_audit,
    unit_composite_longitude_route_audit,
    unit_composite_product_detection_audit,
    unit_composite_product_derived_series_lift_audit,
    unit_composite_product_longitude_expression_audit,
    unit_factorization_audit,
    unit_longitude_subgroup_audit,
    unit_perfect_residual_longitude_audit,
    unit_perfect_residual_normalized_seed_audit,
    unit_perfect_residual_symmetric_seed_audit,
    unit_perfect_residual_symmetric_tower_prefix_audit,
    unit_section_detection_audit,
    unit_section_product_detection_audit,
)


class SemigroupHolonomyTests(unittest.TestCase):
    def test_rees_rectangle_cocycle_audit_accepts_row_column_matrix(self):
        group = cyclic_group(3)
        rows = ("lambda0", "lambda1")
        columns = ("i0", "i1", "i2")
        row_factor = {"lambda0": 1, "lambda1": 2}
        column_factor = {"i0": 0, "i1": 2, "i2": 1}
        sandwich = {
            (row, column): group.mul(row_factor[row], column_factor[column])
            for row in rows
            for column in columns
        }

        audit = rees_rectangle_cocycle_audit(group, rows, columns, sandwich)

        self.assertIsInstance(audit, ReesRectangleCocycleAudit)
        self.assertTrue(audit.rectangle_cocycles_are_trivial)
        self.assertTrue(audit.sandwich_is_row_column_coboundary)
        self.assertTrue(audit.flatness_matches_coboundary)
        self.assertTrue(audit.is_flat)
        self.assertEqual(audit.rectangle_failure_count, 0)
        self.assertEqual(audit.coboundary_failure_count, 0)
        self.assertEqual(audit.row_factors, (("lambda0", 1), ("lambda1", 2)))
        self.assertEqual(audit.column_factors, (("i0", 0), ("i1", 2), ("i2", 1)))

    def test_rees_rectangle_cocycle_audit_finds_c2_nonflat_square(self):
        group = cyclic_group(2)
        rows = ("lambda0", "lambda1")
        columns = ("i0", "i1")
        sandwich = {
            ("lambda0", "i0"): 0,
            ("lambda0", "i1"): 0,
            ("lambda1", "i0"): 0,
            ("lambda1", "i1"): 1,
        }

        omega = rees_rectangle_cocycle(
            group,
            sandwich,
            "lambda0",
            "lambda1",
            "i0",
            "i1",
        )
        audit = rees_rectangle_cocycle_audit(group, rows, columns, sandwich)

        self.assertEqual(omega, 1)
        self.assertFalse(audit.rectangle_cocycles_are_trivial)
        self.assertFalse(audit.sandwich_is_row_column_coboundary)
        self.assertTrue(audit.flatness_matches_coboundary)
        self.assertFalse(audit.is_flat)
        self.assertEqual(audit.rectangle_failure_count, 4)
        self.assertEqual(audit.coboundary_failure_count, 1)
        self.assertEqual(audit.recorded_rectangle_failures[0].omega, 1)
        self.assertEqual(audit.recorded_coboundary_failures[0].actual, 1)
        self.assertEqual(audit.recorded_coboundary_failures[0].expected, 0)

    def test_labeled_permutation_braid_audit_finds_nonflat_c2_holonomy(self):
        group = cyclic_group(2)
        states = ("q00", "q01", "q10", "q11")
        row1 = {
            "q00": "q10",
            "q01": "q11",
            "q10": "q01",
            "q11": "q00",
        }
        row2 = {
            "q00": "q01",
            "q01": "q10",
            "q10": "q11",
            "q11": "q00",
        }
        labels1 = {"q00": 0, "q01": 0, "q10": 0, "q11": 1}
        labels2 = {"q00": 0, "q01": 0, "q10": 1, "q11": 0}

        audit = labeled_permutation_braid_audit(
            group,
            states,
            row1,
            labels1,
            row2,
            labels2,
        )

        self.assertIsInstance(audit, LabeledPermutationBraidAudit)
        self.assertTrue(audit.quotient_braid_relation_holds)
        self.assertTrue(audit.braid_relation_holds)
        self.assertEqual(audit.beta_word, (1, 1, 2, 2, -1, -1, -2, -2))
        self.assertTrue(audit.beta_is_quotient_closed)
        self.assertEqual(
            audit.beta_state_images,
            (
                ("q00", "q00", 1),
                ("q01", "q01", 1),
                ("q10", "q10", 1),
                ("q11", "q11", 1),
            ),
        )
        self.assertEqual(audit.beta_distinct_labels, (1,))
        self.assertEqual(audit.beta_constant_label, 1)
        self.assertTrue(audit.beta_constant_label_is_nontrivial)
        self.assertTrue(audit.verifies_closed_nontrivial_braid_holonomy)

    def test_braid_locality_shadow_accepts_direct_coordinate_model(self):
        states = ("00", "01", "10", "11")
        row1 = {"00": "10", "10": "00", "01": "11", "11": "01"}
        row2 = {"00": "01", "01": "00", "10": "11", "11": "10"}

        audit = braid_locality_shadow_audit(states, row1, row2)

        self.assertIsInstance(audit, BraidLocalityShadowAudit)
        self.assertEqual(audit.row1_cycle_lengths, (2, 2))
        self.assertEqual(audit.row2_cycle_lengths, (2, 2))
        self.assertTrue(audit.row1_has_nontrivial_fixed_partition)
        self.assertTrue(audit.row2_has_nontrivial_fixed_partition)
        self.assertGreaterEqual(audit.jointly_separating_fixed_pair_count, 1)
        self.assertTrue(audit.direct_coordinate_shadow_possible)

    def test_braid_locality_shadow_rejects_c2_obstruction_rows_directly(self):
        states = ("q00", "q01", "q10", "q11")
        row1 = {
            "q00": "q10",
            "q01": "q11",
            "q10": "q01",
            "q11": "q00",
        }
        row2 = {
            "q00": "q01",
            "q01": "q10",
            "q10": "q11",
            "q11": "q00",
        }

        row1_partitions = permutation_fixed_partitions(states, row1)
        row2_partitions = permutation_fixed_partitions(states, row2)
        audit = braid_locality_shadow_audit(states, row1, row2)

        self.assertEqual(row1_partitions, ((("q00", "q01", "q10", "q11"),),))
        self.assertEqual(row2_partitions, ((("q00", "q01", "q10", "q11"),),))
        self.assertEqual(audit.row1_cycle_lengths, (4,))
        self.assertEqual(audit.row2_cycle_lengths, (4,))
        self.assertFalse(audit.row1_has_nontrivial_fixed_partition)
        self.assertFalse(audit.row2_has_nontrivial_fixed_partition)
        self.assertEqual(audit.jointly_separating_fixed_pair_count, 0)
        self.assertFalse(audit.direct_coordinate_shadow_possible)

    def test_adjacent_two_body_realization_audit_accepts_swap_control(self):
        states = tuple((a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1))
        swap = {(a, b): (b, a) for a in (0, 1) for b in (0, 1)}
        row1 = {state: (state[1], state[0], state[2]) for state in states}
        row2 = {state: (state[0], state[2], state[1]) for state in states}
        embedding = {state: state for state in states}

        audit = adjacent_two_body_realization_audit(
            states,
            row1,
            row2,
            basis_size=2,
            candidate_pair_maps=(swap,),
            candidate_embeddings=(embedding,),
        )

        self.assertIsInstance(audit, AdjacentTwoBodyRealizationAudit)
        self.assertTrue(audit.require_ybe)
        self.assertTrue(audit.realization_found)
        self.assertEqual(audit.pair_bijection_count, 1)
        self.assertEqual(audit.candidate_embedding_count, 1)
        self.assertIsNotNone(audit.recorded_pair_map)
        self.assertIsNotNone(audit.recorded_embedding)

    def test_adjacent_two_body_realization_audit_rejects_c2_obstruction_rows(self):
        states = ("q00", "q01", "q10", "q11")
        row1 = {
            "q00": "q10",
            "q01": "q11",
            "q10": "q01",
            "q11": "q00",
        }
        row2 = {
            "q00": "q01",
            "q01": "q10",
            "q10": "q11",
            "q11": "q00",
        }

        audit = adjacent_two_body_realization_audit(
            states,
            row1,
            row2,
            basis_size=2,
            require_ybe=False,
        )
        ybe_audit = adjacent_two_body_realization_audit(
            states,
            row1,
            row2,
            basis_size=2,
        )

        self.assertEqual(audit.pair_bijection_count, 24)
        self.assertEqual(audit.candidate_embedding_count, 1680)
        self.assertFalse(audit.require_ybe)
        self.assertFalse(audit.realization_found)
        self.assertIsNone(audit.recorded_pair_map)
        self.assertFalse(ybe_audit.realization_found)
        self.assertLessEqual(ybe_audit.checked_embedding_count, audit.checked_embedding_count)

    def test_reset_element_is_aperiodic(self):
        reset = (0, 0, 2)

        self.assertTrue(is_aperiodic_element(reset))
        self.assertEqual(transformation_power(reset, 2), reset)

    def test_nontrivial_permutation_is_not_aperiodic(self):
        swap = (1, 0)

        self.assertFalse(is_aperiodic_element(swap))
        self.assertTrue(is_permutation_transformation(swap))
        self.assertEqual(transformation_power(swap, 2), (0, 1))

    def test_permutation_composite_forces_permutation_factors(self):
        swap = (1, 0)
        audit = unit_factorization_audit((swap, swap))

        self.assertEqual(compose_transformation_word((swap, swap)), (0, 1))
        self.assertTrue(audit.composite_is_unit)
        self.assertTrue(audit.all_factors_are_units)
        self.assertTrue(audit.permutation_composite_forces_unit_factors)
        self.assertEqual(audit.nonunit_factors, ())

    def test_nonunit_factor_cannot_hide_inside_permutation_product(self):
        reset = (0, 0)
        swap = (1, 0)

        audit = unit_factorization_audit((swap, reset, swap))

        self.assertFalse(audit.composite_is_unit)
        self.assertFalse(audit.all_factors_are_units)
        self.assertTrue(audit.permutation_composite_forces_unit_factors)
        self.assertEqual(audit.nonunit_factor_indices, (1,))
        self.assertEqual(audit.nonunit_factors, (reset,))

    def test_empty_unit_factorization_uses_explicit_degree(self):
        audit = unit_factorization_audit((), degree=3)

        self.assertEqual(audit.composite, (0, 1, 2))
        self.assertTrue(audit.composite_is_unit)
        self.assertTrue(audit.all_factors_are_units)

    def test_aperiodic_monoid_has_only_identity_permutation(self):
        monoid = TransformationMonoid.generated(((0, 0),))
        audit = aperiodic_permutation_audit(monoid)

        self.assertTrue(is_aperiodic_monoid(monoid))
        self.assertEqual(permutation_elements(monoid.elements), ((0, 1),))
        self.assertTrue(audit.is_aperiodic)
        self.assertEqual(audit.permutation_count, 1)
        self.assertEqual(audit.nonidentity_permutation_count, 0)
        self.assertEqual(audit.nonidentity_permutations, ())

    def test_group_component_has_nonidentity_permutation(self):
        swap = (1, 0)
        monoid = TransformationMonoid.generated((swap,))
        audit = aperiodic_permutation_audit(monoid)
        group = monoid_permutation_group(monoid)

        self.assertFalse(is_aperiodic_monoid(monoid))
        self.assertIn(swap, permutation_elements(monoid.elements))
        self.assertFalse(audit.is_aperiodic)
        self.assertEqual(audit.nonidentity_permutations, (swap,))
        self.assertEqual(group.identity, (0, 1))
        self.assertEqual(group.elements, ((0, 1), (1, 0)))
        self.assertEqual(group.mul(swap, swap), (0, 1))

    def test_unit_longitude_subgroup_audit_sees_unit_label(self):
        swap = (1, 0)
        monoid = TransformationMonoid.generated((swap,))

        audit = unit_longitude_subgroup_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            labels=(swap,),
        )

        self.assertEqual(audit.artin_permutation, (0, 1))
        self.assertEqual(audit.unit_group_order, 2)
        self.assertEqual(audit.longitude_subgroup_size, 2)
        self.assertTrue(audit.labels_are_units)
        self.assertTrue(audit.labels_lie_in_longitude_subgroup)
        self.assertEqual(audit.nonunit_labels, ())
        self.assertEqual(audit.labels_outside_longitude_subgroup, ())

    def test_unit_longitude_subgroup_audit_reports_missing_unit_label(self):
        swap = (1, 0)
        monoid = TransformationMonoid.generated((swap,))

        audit = unit_longitude_subgroup_audit(
            monoid,
            n=2,
            braid_word=(1, 1, 1, 1),
            labels=(swap,),
        )

        self.assertEqual(audit.unit_group_order, 2)
        self.assertEqual(audit.longitude_subgroup_size, 1)
        self.assertTrue(audit.labels_are_units)
        self.assertFalse(audit.labels_lie_in_longitude_subgroup)
        self.assertEqual(audit.labels_outside_longitude_subgroup, (swap,))

    def test_unit_longitude_subgroup_audit_rejects_nonunit_label(self):
        reset = (0, 0)
        monoid = TransformationMonoid.generated((reset,))

        audit = unit_longitude_subgroup_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            labels=(reset,),
        )

        self.assertEqual(audit.unit_group_order, 1)
        self.assertFalse(audit.labels_are_units)
        self.assertFalse(audit.labels_lie_in_longitude_subgroup)
        self.assertEqual(audit.nonunit_labels, (reset,))
        self.assertEqual(audit.labels_outside_longitude_subgroup, ())

    def test_unit_section_detection_accepts_longitude_unit_branch(self):
        swap = (1, 0)
        monoid = TransformationMonoid.generated((swap,))

        audit = unit_section_detection_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(swap,),
        )

        self.assertTrue(audit.is_permutation_branch)
        self.assertTrue(audit.factors_are_unit_sections)
        self.assertTrue(audit.factors_lie_in_longitude_subgroup)
        self.assertFalse(audit.identity_longitude_signature)
        self.assertFalse(audit.composite_is_identity)
        self.assertTrue(audit.identity_longitudes_kill_branch)

    def test_unit_section_detection_kills_trivial_identity_signature_branch(self):
        swap = (1, 0)
        monoid = TransformationMonoid.generated((swap,))

        audit = unit_section_detection_audit(
            monoid,
            n=2,
            braid_word=(1, 1, 1, 1),
            factors=((0, 1),),
        )

        self.assertTrue(audit.identity_longitude_signature)
        self.assertTrue(audit.factors_lie_in_longitude_subgroup)
        self.assertTrue(audit.composite_is_identity)
        self.assertTrue(audit.identity_longitudes_kill_branch)

    def test_unit_section_detection_rejects_reset_branch(self):
        reset = (0, 0)
        monoid = TransformationMonoid.generated((reset,))

        audit = unit_section_detection_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(reset,),
        )

        self.assertFalse(audit.is_permutation_branch)
        self.assertFalse(audit.factors_are_unit_sections)
        self.assertFalse(audit.factors_lie_in_longitude_subgroup)
        self.assertFalse(audit.identity_longitudes_kill_branch)

    def test_unit_composite_detection_accepts_telescoped_identity(self):
        swap = (1, 0)
        monoid = TransformationMonoid.generated((swap,))

        section = unit_section_detection_audit(
            monoid,
            n=2,
            braid_word=(1, 1, 1, 1),
            factors=(swap, swap),
        )
        composite = unit_composite_detection_audit(
            monoid,
            n=2,
            braid_word=(1, 1, 1, 1),
            factors=(swap, swap),
        )

        self.assertFalse(section.factors_lie_in_longitude_subgroup)
        self.assertTrue(composite.identity_longitude_signature)
        self.assertTrue(composite.composite_is_identity)
        self.assertTrue(composite.composite_lies_in_longitude_subgroup)
        self.assertTrue(composite.identity_longitudes_kill_composite)

    def test_unit_composite_detection_rejects_visible_unit_at_identity_signature(self):
        cycle = (1, 2, 0)
        monoid = TransformationMonoid.generated((cycle,))

        audit = unit_composite_detection_audit(
            monoid,
            n=2,
            braid_word=(1,) * 6,
            factors=(cycle,),
        )

        self.assertTrue(audit.is_permutation_branch)
        self.assertTrue(audit.identity_longitude_signature)
        self.assertFalse(audit.composite_is_identity)
        self.assertFalse(audit.composite_lies_in_longitude_subgroup)
        self.assertFalse(audit.identity_longitudes_kill_composite)
        self.assertTrue(audit.is_finite_unit_detector_failure)

    def test_unit_composite_abelianization_accepts_visible_cyclic_endpoint(self):
        cycle = (1, 2, 0)
        monoid = TransformationMonoid.generated((cycle,))

        audit = unit_composite_abelianization_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(cycle,),
        )

        self.assertTrue(audit.is_permutation_branch)
        self.assertEqual(audit.unit_group_order, 3)
        self.assertEqual(audit.commutator_subgroup_size, 1)
        self.assertEqual(audit.abelianization_order, 3)
        self.assertTrue(audit.group_has_nontrivial_abelianization)
        self.assertEqual(audit.abelian_longitude_subgroup_size, 3)
        self.assertTrue(audit.abelian_projection_lies_in_longitude_subgroup)
        self.assertTrue(audit.abelian_projection_closed_by_matrix_route)
        self.assertTrue(audit.identity_abelian_longitudes_kill_projection)
        self.assertTrue(
            audit.commutator_correction_is_only_remaining_after_abelian_route
        )
        self.assertFalse(audit.is_finite_abelian_unit_detector_failure)

    def test_unit_composite_abelianization_flags_identity_signature_failure(self):
        cycle = (1, 2, 0)
        monoid = TransformationMonoid.generated((cycle,))

        audit = unit_composite_abelianization_audit(
            monoid,
            n=2,
            braid_word=(1,) * 6,
            factors=(cycle,),
        )

        self.assertTrue(audit.is_permutation_branch)
        self.assertTrue(audit.identity_abelian_longitude_signature)
        self.assertFalse(audit.abelian_endpoint_is_identity)
        self.assertEqual(audit.abelian_longitude_subgroup_size, 1)
        self.assertFalse(audit.abelian_projection_lies_in_longitude_subgroup)
        self.assertFalse(audit.abelian_projection_closed_by_matrix_route)
        self.assertFalse(audit.identity_abelian_longitudes_kill_projection)
        self.assertTrue(audit.is_finite_abelian_unit_detector_failure)

    def test_unit_composite_abelianization_rejects_nonunit_endpoint(self):
        reset = (0, 0)
        monoid = TransformationMonoid.generated((reset,))

        audit = unit_composite_abelianization_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(reset,),
        )

        self.assertFalse(audit.is_permutation_branch)
        self.assertIsNone(audit.abelian_endpoint)
        self.assertIsNone(audit.abelian_longitude_subgroup_size)
        self.assertIsNone(audit.abelian_endpoint_lies_in_longitude_subgroup)
        self.assertFalse(audit.abelian_projection_closed_by_matrix_route)

    def test_unit_composite_derived_series_lift_closes_cyclic_endpoint(self):
        cycle = (1, 2, 0)
        identity = (0, 1, 2)
        monoid = TransformationMonoid.generated((cycle,))
        stage_witness = (((cycle, identity), 1, 1),)

        audit = unit_composite_derived_series_lift_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(cycle,),
            stage_lifted_witnesses=(stage_witness,),
        )

        self.assertEqual(audit.derived_subgroup_orders, (3, 1))
        self.assertEqual(audit.expected_stage_count, 1)
        self.assertTrue(audit.stage_count_matches_derived_series)
        self.assertTrue(audit.all_stage_lifts_pass)
        self.assertTrue(audit.perfect_residual_is_trivial)
        self.assertEqual(audit.final_residual, identity)
        self.assertTrue(audit.final_witness_matches_residual)
        self.assertEqual(audit.combined_witness_value, cycle)
        self.assertTrue(audit.combined_witness_matches_endpoint)
        self.assertTrue(audit.proves_endpoint_in_longitude_subgroup_by_derived_lift)

    def test_unit_composite_derived_series_lift_handles_s3_endpoint(self):
        transposition = (1, 0, 2)
        three_cycle = (1, 2, 0)
        identity = (0, 1, 2)
        monoid = TransformationMonoid.generated((transposition, three_cycle))
        group = monoid_permutation_group(monoid)
        endpoint = group.mul(three_cycle, transposition)
        stage0 = (((transposition, identity), 1, 1),)
        stage1 = (((three_cycle, identity), 1, 1),)

        audit = unit_composite_derived_series_lift_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(endpoint,),
            stage_lifted_witnesses=(stage0, stage1),
        )

        self.assertEqual(audit.unit_group_order, 6)
        self.assertEqual(audit.derived_subgroup_orders, (6, 3, 1))
        self.assertEqual(tuple(stage.stage_passes for stage in audit.stage_audits), (True, True))
        self.assertEqual(audit.stage_audits[0].correction, three_cycle)
        self.assertEqual(audit.stage_audits[1].correction, identity)
        self.assertEqual(audit.final_residual, identity)
        self.assertEqual(audit.combined_witness_value, endpoint)
        self.assertTrue(audit.proves_endpoint_in_longitude_subgroup_by_derived_lift)

    def test_unit_composite_derived_series_lift_requires_all_stages(self):
        transposition = (1, 0, 2)
        three_cycle = (1, 2, 0)
        identity = (0, 1, 2)
        monoid = TransformationMonoid.generated((transposition, three_cycle))
        group = monoid_permutation_group(monoid)
        endpoint = group.mul(three_cycle, transposition)
        stage0 = (((transposition, identity), 1, 1),)

        audit = unit_composite_derived_series_lift_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(endpoint,),
            stage_lifted_witnesses=(stage0,),
        )

        self.assertEqual(audit.expected_stage_count, 2)
        self.assertEqual(audit.supplied_stage_count, 1)
        self.assertFalse(audit.stage_count_matches_derived_series)
        self.assertFalse(audit.all_stage_lifts_pass)
        self.assertFalse(audit.final_witness_matches_residual)
        self.assertFalse(audit.combined_witness_matches_endpoint)
        self.assertFalse(audit.proves_endpoint_in_longitude_subgroup_by_derived_lift)

    def test_unit_perfect_residual_audit_handles_trivial_residual(self):
        transposition = (1, 0, 2)
        three_cycle = (1, 2, 0)
        identity = (0, 1, 2)
        monoid = TransformationMonoid.generated((transposition, three_cycle))

        audit = unit_perfect_residual_longitude_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            residual_endpoint=identity,
        )

        self.assertEqual(audit.derived_subgroup_orders, (6, 3, 1))
        self.assertTrue(audit.perfect_residual_is_trivial)
        self.assertTrue(audit.residual_endpoint_in_perfect_residual)
        self.assertTrue(audit.residual_endpoint_lies_in_perfect_residual_longitude_subgroup)
        self.assertTrue(audit.proves_perfect_residual_endpoint_in_longitude_subgroup)
        self.assertTrue(audit.identity_longitudes_kill_perfect_residual_endpoint)

    def test_unit_perfect_residual_audit_checks_a5_residual(self):
        three_cycle = (1, 2, 0, 3, 4)
        five_cycle = (1, 2, 3, 4, 0)
        monoid = TransformationMonoid.generated((three_cycle, five_cycle))

        audit = unit_perfect_residual_longitude_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            residual_endpoint=three_cycle,
            max_assignments=10_000,
        )

        self.assertEqual(audit.unit_group_order, 60)
        self.assertEqual(audit.derived_subgroup_orders, (60,))
        self.assertFalse(audit.perfect_residual_is_trivial)
        self.assertEqual(audit.perfect_residual_size, 60)
        self.assertTrue(audit.residual_endpoint_in_perfect_residual)
        self.assertEqual(audit.perfect_residual_longitude_subgroup_size, 60)
        self.assertTrue(audit.proves_perfect_residual_endpoint_in_longitude_subgroup)
        self.assertTrue(audit.identity_longitudes_kill_perfect_residual_endpoint)
        self.assertFalse(audit.is_finite_perfect_residual_detector_failure)

    def test_unit_perfect_residual_audit_flags_identity_signature_failure(self):
        three_cycle = (1, 2, 0, 3, 4)
        five_cycle = (1, 2, 3, 4, 0)
        monoid = TransformationMonoid.generated((three_cycle, five_cycle))

        audit = unit_perfect_residual_longitude_audit(
            monoid,
            n=2,
            braid_word=(),
            residual_endpoint=three_cycle,
            max_assignments=10_000,
        )

        self.assertTrue(audit.residual_endpoint_in_perfect_residual)
        self.assertTrue(audit.identity_perfect_residual_longitude_signature)
        self.assertFalse(audit.residual_endpoint_lies_in_perfect_residual_longitude_subgroup)
        self.assertFalse(audit.proves_perfect_residual_endpoint_in_longitude_subgroup)
        self.assertFalse(audit.identity_longitudes_kill_perfect_residual_endpoint)
        self.assertTrue(audit.is_finite_perfect_residual_detector_failure)

    def test_unit_perfect_residual_normalized_seed_pairs_one_prefix_row(self):
        total = rack_solution([0, 1], lambda _left, right: 1 - right)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        local_prefix = local_normalized_law_prefix_witness_audit(
            qmap,
            identity_solution(["q"]),
            (cyclic_group(1),),
            2,
            pure_braid_generator(1, 2),
            ("*", "*"),
            (0, 0),
            extra_strands=1,
            fill_value=0,
        )
        three_cycle = (1, 2, 0, 3, 4)
        perfect_miss = UnitPerfectResidualLongitudeAudit(
            artin_permutation=(0, 1),
            unit_group_order=60,
            derived_subgroup_orders=(60,),
            perfect_residual_size=60,
            residual_endpoint=three_cycle,
            residual_endpoint_in_unit_group=True,
            residual_endpoint_in_perfect_residual=True,
            perfect_residual_longitude_subgroup_size=1,
            residual_endpoint_lies_in_perfect_residual_longitude_subgroup=False,
            perfect_residual_identity=(0, 1, 2, 3, 4),
        )

        audit = unit_perfect_residual_normalized_seed_audit(
            local_prefix,
            perfect_miss,
            same_braid_word=True,
            endpoint_readout_matches_residual_motion=True,
        )

        self.assertTrue(local_prefix.proves_one_local_prefix_normalized_law_witness)
        self.assertTrue(audit.same_source_degree)
        self.assertTrue(audit.perfect_residual_has_finite_detector_miss)
        self.assertTrue(audit.proves_one_local_perfect_residual_normalized_seed)

    def test_unit_perfect_residual_normalized_seed_requires_readout_match(self):
        total = rack_solution([0, 1], lambda _left, right: 1 - right)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        local_prefix = local_normalized_law_prefix_witness_audit(
            qmap,
            identity_solution(["q"]),
            (cyclic_group(1),),
            2,
            pure_braid_generator(1, 2),
            ("*", "*"),
            (0, 0),
            extra_strands=1,
            fill_value=0,
        )
        perfect_miss = UnitPerfectResidualLongitudeAudit(
            artin_permutation=(0, 1),
            unit_group_order=60,
            derived_subgroup_orders=(60,),
            perfect_residual_size=60,
            residual_endpoint=(1, 2, 0, 3, 4),
            residual_endpoint_in_unit_group=True,
            residual_endpoint_in_perfect_residual=True,
            perfect_residual_longitude_subgroup_size=1,
            residual_endpoint_lies_in_perfect_residual_longitude_subgroup=False,
            perfect_residual_identity=(0, 1, 2, 3, 4),
        )

        audit = unit_perfect_residual_normalized_seed_audit(
            local_prefix,
            perfect_miss,
            same_braid_word=True,
            endpoint_readout_matches_residual_motion=False,
        )

        self.assertFalse(audit.proves_one_local_perfect_residual_normalized_seed)

    def test_unit_perfect_residual_symmetric_seed_records_tower_row(self):
        total = rack_solution(list(range(5)), lambda _left, right: (right + 1) % 5)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        braid = (1,) * 12
        local_prefix = local_symmetric_normalized_law_prefix_witness_audit(
            qmap,
            identity_solution(["q"]),
            3,
            2,
            braid,
            ("*", "*"),
            (0, 0),
            extra_strands=3,
            fill_value=0,
        )
        perfect_miss = UnitPerfectResidualLongitudeAudit(
            artin_permutation=(0, 1),
            unit_group_order=3,
            derived_subgroup_orders=(3,),
            perfect_residual_size=3,
            residual_endpoint=(1, 2, 0),
            residual_endpoint_in_unit_group=True,
            residual_endpoint_in_perfect_residual=True,
            perfect_residual_longitude_subgroup_size=1,
            residual_endpoint_lies_in_perfect_residual_longitude_subgroup=False,
            perfect_residual_identity=(0, 1, 2),
        )

        audit = unit_perfect_residual_symmetric_seed_audit(
            local_prefix,
            perfect_miss,
            symmetric_degree=3,
            same_braid_word=True,
            endpoint_readout_matches_residual_motion=True,
        )

        self.assertTrue(local_prefix.proves_one_local_prefix_normalized_law_witness)
        self.assertTrue(audit.uses_declared_symmetric_row)
        self.assertTrue(audit.right_stabilized_by_symmetric_degree)
        self.assertTrue(audit.symmetric_degree_covers_perfect_residual)
        self.assertTrue(audit.proves_one_local_perfect_residual_symmetric_seed)

    def test_unit_perfect_residual_symmetric_seed_requires_degree_cover(self):
        total = rack_solution(list(range(5)), lambda _left, right: (right + 1) % 5)
        quotient = identity_solution(["*"])
        qmap = QuotientMap(total, quotient, {element: "*" for element in total.elements})
        local_prefix = local_symmetric_normalized_law_prefix_witness_audit(
            qmap,
            identity_solution(["q"]),
            3,
            2,
            (1,) * 12,
            ("*", "*"),
            (0, 0),
            extra_strands=3,
            fill_value=0,
        )
        perfect_miss = UnitPerfectResidualLongitudeAudit(
            artin_permutation=(0, 1),
            unit_group_order=60,
            derived_subgroup_orders=(60,),
            perfect_residual_size=60,
            residual_endpoint=(1, 2, 0, 3, 4),
            residual_endpoint_in_unit_group=True,
            residual_endpoint_in_perfect_residual=True,
            perfect_residual_longitude_subgroup_size=1,
            residual_endpoint_lies_in_perfect_residual_longitude_subgroup=False,
            perfect_residual_identity=(0, 1, 2, 3, 4),
        )

        audit = unit_perfect_residual_symmetric_seed_audit(
            local_prefix,
            perfect_miss,
            symmetric_degree=3,
            same_braid_word=True,
            endpoint_readout_matches_residual_motion=True,
        )

        self.assertFalse(audit.symmetric_degree_covers_perfect_residual)
        self.assertFalse(audit.proves_one_local_perfect_residual_symmetric_seed)

    def test_unit_perfect_residual_symmetric_tower_prefix_checks_tail_degrees(self):
        row60 = self._synthetic_perfect_residual_symmetric_seed_row(60)
        row61 = self._synthetic_perfect_residual_symmetric_seed_row(61)

        audit = unit_perfect_residual_symmetric_tower_prefix_audit((row60, row61))

        self.assertEqual(audit.common_residual_size, 60)
        self.assertEqual(audit.symmetric_degrees, (60, 61))
        self.assertTrue(audit.degrees_are_tail_prefix_from_residual_size)
        self.assertTrue(audit.proves_supplied_perfect_residual_symmetric_tail_prefix)

    def test_unit_perfect_residual_symmetric_tower_prefix_rejects_gap(self):
        row60 = self._synthetic_perfect_residual_symmetric_seed_row(60)
        row62 = self._synthetic_perfect_residual_symmetric_seed_row(62)

        audit = unit_perfect_residual_symmetric_tower_prefix_audit((row60, row62))

        self.assertEqual(audit.symmetric_degrees, (60, 62))
        self.assertFalse(audit.degrees_are_tail_prefix_from_residual_size)
        self.assertFalse(audit.proves_supplied_perfect_residual_symmetric_tail_prefix)

    def test_unit_composite_detection_rejects_nonunit_composite(self):
        reset = (0, 0)
        monoid = TransformationMonoid.generated((reset,))

        audit = unit_composite_detection_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(reset,),
        )

        self.assertFalse(audit.is_permutation_branch)
        self.assertFalse(audit.composite_lies_in_longitude_subgroup)
        self.assertFalse(audit.identity_longitudes_kill_composite)

    def _synthetic_perfect_residual_symmetric_seed_row(self, symmetric_degree):
        source_n = 2
        local_prefix = LocalNormalizedLawPrefixWitnessAudit(
            source_n=source_n,
            target_n=source_n + symmetric_degree,
            braid_word=tuple(),
            group_orders=(factorial(symmetric_degree),),
            product_group_order=factorial(symmetric_degree),
            source_base_detector_identity_action=True,
            target_base_detector_identity_action=True,
            source_product_identity_signature=True,
            target_product_identity_signature=True,
            source_factor_identity_signatures=(True,),
            target_factor_identity_signatures=(True,),
            right_stabilization=RightStabilizationLongitudeAudit(
                old_n=source_n,
                new_n=source_n + symmetric_degree,
                braid_word=tuple(),
                old_permutation=(0, 1),
                new_permutation=tuple(range(source_n + symmetric_degree)),
                old_longitudes=((), ()),
                new_restricted_longitudes=((), ()),
                added_longitudes=tuple(() for _ in range(symmetric_degree)),
            ),
            base_tuple=("*", "*"),
            source_base_image=("*", "*"),
            source_quotient_base_fixed=True,
            fibre_tuple=(0, 0),
            source_image=(1, 1),
            source_image_base=("*", "*"),
            source_stays_over_base=True,
            source_residual_tuple_moved=True,
            stabilized_base_tuple=tuple("*" for _ in range(source_n + symmetric_degree)),
            target_base_image=tuple("*" for _ in range(source_n + symmetric_degree)),
            target_quotient_base_fixed=True,
            stabilized_fibre_tuple=tuple(0 for _ in range(source_n + symmetric_degree)),
            stabilized_image=(1, 1) + tuple(0 for _ in range(symmetric_degree)),
            stabilized_image_base=tuple("*" for _ in range(source_n + symmetric_degree)),
            target_stays_over_base=True,
            target_residual_tuple_moved=True,
            finite_checks_derived_from_tables=True,
        )
        perfect_miss = UnitPerfectResidualLongitudeAudit(
            artin_permutation=(0, 1),
            unit_group_order=60,
            derived_subgroup_orders=(60,),
            perfect_residual_size=60,
            residual_endpoint=(1, 2, 0, 3, 4),
            residual_endpoint_in_unit_group=True,
            residual_endpoint_in_perfect_residual=True,
            perfect_residual_longitude_subgroup_size=1,
            residual_endpoint_lies_in_perfect_residual_longitude_subgroup=False,
            perfect_residual_identity=(0, 1, 2, 3, 4),
        )
        return unit_perfect_residual_symmetric_seed_audit(
            local_prefix,
            perfect_miss,
            symmetric_degree=symmetric_degree,
            same_braid_word=True,
            endpoint_readout_matches_residual_motion=True,
        )

    def test_unit_composite_longitude_route_records_single_witness(self):
        swap = (1, 0)
        monoid = TransformationMonoid.generated((swap,))

        audit = unit_composite_longitude_route_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(swap,),
        )

        self.assertTrue(audit.is_permutation_branch)
        self.assertEqual(audit.unit_group_order, 2)
        self.assertEqual(audit.longitude_subgroup_size, 2)
        self.assertTrue(audit.composite_lies_in_longitude_subgroup)
        self.assertTrue(audit.has_single_longitude_witness)
        self.assertIsNotNone(audit.witness_longitude_index)
        self.assertIsNotNone(audit.witness_assignment)
        self.assertFalse(audit.identity_longitude_signature)
        self.assertTrue(audit.identity_longitudes_kill_composite)

    def test_unit_composite_longitude_expression_certifies_endpoint(self):
        swap = (1, 0)
        identity = (0, 1)
        monoid = TransformationMonoid.generated((swap,))

        audit = unit_composite_longitude_expression_audit(
            monoid,
            n=2,
            braid_word=(1, 1),
            factors=(swap,),
            assignment=(swap, identity),
            expression=((1, 1),),
        )

        self.assertTrue(audit.is_permutation_branch)
        self.assertTrue(audit.assignment_in_unit_group)
        self.assertEqual(audit.expression_value, swap)
        self.assertTrue(audit.expression_matches_composite)
        self.assertTrue(audit.composite_lies_in_longitude_subgroup_by_expression)
        self.assertFalse(audit.identity_longitude_signature)
        self.assertTrue(audit.identity_longitudes_kill_composite_by_expression)

    def test_unit_composite_longitude_expression_rejects_bad_certificate(self):
        swap = (1, 0)
        identity = (0, 1)
        monoid = TransformationMonoid.generated((swap,))

        audit = unit_composite_longitude_expression_audit(
            monoid,
            n=2,
            braid_word=(1, 1, 1, 1),
            factors=(swap,),
            assignment=(swap, identity),
            expression=(),
        )

        self.assertTrue(audit.identity_longitude_signature)
        self.assertFalse(audit.composite_is_identity)
        self.assertEqual(audit.expression_value, identity)
        self.assertFalse(audit.expression_matches_composite)
        self.assertFalse(audit.composite_lies_in_longitude_subgroup_by_expression)
        self.assertFalse(audit.identity_longitudes_kill_composite_by_expression)

    def test_unit_composite_longitude_route_flags_subgroup_failure(self):
        cycle = (1, 2, 0)
        monoid = TransformationMonoid.generated((cycle,))

        audit = unit_composite_longitude_route_audit(
            monoid,
            n=2,
            braid_word=(1,) * 6,
            factors=(cycle,),
        )

        self.assertTrue(audit.is_permutation_branch)
        self.assertEqual(audit.longitude_subgroup_size, 1)
        self.assertFalse(audit.composite_lies_in_longitude_subgroup)
        self.assertFalse(audit.has_single_longitude_witness)
        self.assertTrue(audit.identity_longitude_signature)
        self.assertFalse(audit.identity_longitudes_kill_composite)
        self.assertTrue(audit.is_finite_unit_detector_failure)

    def test_unit_section_product_detection_uses_one_product_group(self):
        swap = (1, 0)
        cycle = (1, 2, 0)
        c2 = TransformationMonoid.generated((swap,))
        c3 = TransformationMonoid.generated((cycle,))

        audit = unit_section_product_detection_audit(
            (c2, c3),
            n=2,
            braid_word=(1, 1),
            factor_words=((swap,), (cycle,)),
        )

        self.assertEqual(audit.unit_group_orders, (2, 3))
        self.assertEqual(audit.product_group_order, 6)
        self.assertFalse(audit.truncated)
        self.assertTrue(audit.all_factor_words_in_monoids)
        self.assertTrue(audit.all_permutation_branches)
        self.assertTrue(audit.all_factors_lie_in_longitude_subgroups)
        self.assertTrue(audit.all_identity_longitudes_kill_branches)
        self.assertEqual(audit.product_subgroup_size, 6)
        self.assertEqual(audit.expected_product_subgroup_size, 6)
        self.assertTrue(audit.product_subgroup_equals_factor_product)
        self.assertTrue(audit.proves_single_product_detector_when_enumerated)

    def test_unit_section_product_detection_identity_signature_product(self):
        swap = (1, 0)
        cycle = (1, 2, 0)
        c2 = TransformationMonoid.generated((swap,))
        c3 = TransformationMonoid.generated((cycle,))

        audit = unit_section_product_detection_audit(
            (c2, c3),
            n=2,
            braid_word=(1,) * 12,
            factor_words=(((0, 1),), ((0, 1, 2),)),
        )

        self.assertFalse(audit.truncated)
        self.assertTrue(audit.all_factors_lie_in_longitude_subgroups)
        self.assertTrue(audit.all_identity_longitudes_kill_branches)
        self.assertEqual(audit.product_subgroup_size, 1)
        self.assertEqual(audit.expected_product_subgroup_size, 1)
        self.assertTrue(audit.product_subgroup_equals_factor_product)

    def test_unit_section_product_detection_can_skip_large_product(self):
        cycle2 = TransformationMonoid.generated(((1, 0),))
        cycle3 = TransformationMonoid.generated(((1, 2, 0),))

        audit = unit_section_product_detection_audit(
            (cycle2, cycle3),
            n=2,
            braid_word=(1, 1),
            factor_words=(((1, 0),), ((1, 2, 0),)),
            max_product_order=5,
        )

        self.assertTrue(audit.truncated)
        self.assertEqual(audit.product_group_order, 6)
        self.assertIsNone(audit.product_subgroup_size)
        self.assertFalse(audit.proves_single_product_detector_when_enumerated)

    def test_unit_section_product_detection_requires_parallel_words(self):
        c2 = TransformationMonoid.generated(((1, 0),))
        with self.assertRaises(ValueError):
            unit_section_product_detection_audit((c2,), 2, (1, 1), ())

    def test_unit_composite_product_detection_accepts_telescoped_endpoints(self):
        swap = (1, 0)
        cycle = (1, 2, 0)
        c2 = TransformationMonoid.generated((swap,))
        c3 = TransformationMonoid.generated((cycle,))

        section = unit_section_product_detection_audit(
            (c2, c3),
            n=2,
            braid_word=(1,) * 12,
            factor_words=((swap, swap), (cycle, cycle, cycle)),
        )
        composite = unit_composite_product_detection_audit(
            (c2, c3),
            n=2,
            braid_word=(1,) * 12,
            factor_words=((swap, swap), (cycle, cycle, cycle)),
        )

        self.assertFalse(section.all_factors_lie_in_longitude_subgroups)
        self.assertTrue(composite.all_factor_words_in_monoids)
        self.assertTrue(composite.all_permutation_branches)
        self.assertTrue(composite.all_composites_lie_in_longitude_subgroups)
        self.assertTrue(composite.all_identity_longitudes_kill_composites)
        self.assertEqual(composite.product_endpoint, ((0, 1), (0, 1, 2)))
        self.assertTrue(composite.product_endpoint_in_product_subgroup)
        self.assertTrue(composite.product_endpoint_lies_in_product_longitude_subgroup)
        self.assertTrue(composite.identity_product_longitude_signature)
        self.assertTrue(composite.identity_longitudes_kill_product_endpoint)
        self.assertEqual(composite.product_subgroup_size, 1)
        self.assertEqual(composite.expected_product_subgroup_size, 1)
        self.assertTrue(composite.product_subgroup_equals_factor_product)
        self.assertTrue(composite.proves_single_product_detector_when_enumerated)
        self.assertTrue(composite.proves_product_endpoint_detector_when_enumerated)

    def test_unit_composite_product_expression_certifies_product_endpoint(self):
        swap = (1, 0)
        cycle = (1, 2, 0)
        c2 = TransformationMonoid.generated((swap,))
        c3 = TransformationMonoid.generated((cycle,))

        audit = unit_composite_product_longitude_expression_audit(
            (c2, c3),
            n=2,
            braid_word=(1, 1),
            factor_words=((swap,), (cycle,)),
            assignments=(((swap, (0, 1))), ((cycle, (0, 1, 2)))),
            expressions=(((1, 1),), ((1, 1),)),
        )

        self.assertEqual(audit.unit_group_orders, (2, 3))
        self.assertEqual(audit.product_group_order, 6)
        self.assertEqual(audit.product_endpoint, (swap, cycle))
        self.assertTrue(audit.all_factor_words_in_monoids)
        self.assertTrue(audit.all_permutation_branches)
        self.assertTrue(audit.all_assignments_in_unit_groups)
        self.assertTrue(audit.all_expressions_match_composites)
        self.assertEqual(len(audit.product_witness), 2)
        self.assertEqual(audit.product_witness_value, audit.product_endpoint)
        self.assertTrue(audit.product_witness_matches_endpoint)
        self.assertTrue(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_expression
        )
        self.assertFalse(audit.identity_product_longitude_signature)
        self.assertTrue(audit.identity_longitudes_kill_product_endpoint_by_expression)
        self.assertTrue(audit.proves_product_endpoint_detector_by_expression)

    def test_unit_composite_product_derived_series_lift_uses_one_product_detector(self):
        cycle = (1, 2, 0)
        c3_identity = (0, 1, 2)
        transposition = (1, 0, 2)
        three_cycle = (1, 2, 0)
        s3_identity = (0, 1, 2)
        cyclic_monoid = TransformationMonoid.generated((cycle,))
        s3_monoid = TransformationMonoid.generated((transposition, three_cycle))
        s3_group = monoid_permutation_group(s3_monoid)
        s3_endpoint = s3_group.mul(three_cycle, transposition)
        c3_stage = (((cycle, c3_identity), 1, 1),)
        s3_stage0 = (((transposition, s3_identity), 1, 1),)
        s3_stage1 = (((three_cycle, s3_identity), 1, 1),)

        audit = unit_composite_product_derived_series_lift_audit(
            (cyclic_monoid, s3_monoid),
            n=2,
            braid_word=(1, 1),
            factor_words=((cycle,), (s3_endpoint,)),
            stage_lifted_witnesses=((c3_stage,), (s3_stage0, s3_stage1)),
        )

        self.assertEqual(audit.unit_group_orders, (3, 6))
        self.assertEqual(audit.product_group_order, 18)
        self.assertEqual(audit.product_endpoint, (cycle, s3_endpoint))
        self.assertTrue(audit.all_factor_words_in_monoids)
        self.assertTrue(audit.all_permutation_branches)
        self.assertTrue(audit.all_derived_lifts_prove_factor_endpoints)
        self.assertIsNotNone(audit.product_witness)
        self.assertEqual(audit.product_witness_value, audit.product_endpoint)
        self.assertTrue(audit.product_witness_matches_endpoint)
        self.assertTrue(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_derived_lift
        )
        self.assertTrue(audit.proves_product_endpoint_detector_by_derived_lift)

    def test_unit_composite_product_derived_series_lift_rejects_bad_factor(self):
        cycle = (1, 2, 0)
        identity = (0, 1, 2)
        monoid = TransformationMonoid.generated((cycle,))
        stage_witness = (((identity, identity), 1, 1),)

        audit = unit_composite_product_derived_series_lift_audit(
            (monoid,),
            n=2,
            braid_word=(1, 1),
            factor_words=((cycle,),),
            stage_lifted_witnesses=((stage_witness,),),
        )

        self.assertFalse(audit.all_derived_lifts_prove_factor_endpoints)
        self.assertIsNone(audit.product_witness)
        self.assertIsNone(audit.product_witness_value)
        self.assertFalse(audit.product_witness_matches_endpoint)
        self.assertFalse(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_derived_lift
        )
        self.assertFalse(audit.proves_product_endpoint_detector_by_derived_lift)

    def test_unit_composite_product_expression_kills_identity_signature_endpoint(self):
        swap = (1, 0)
        cycle = (1, 2, 0)
        c2 = TransformationMonoid.generated((swap,))
        c3 = TransformationMonoid.generated((cycle,))

        audit = unit_composite_product_longitude_expression_audit(
            (c2, c3),
            n=2,
            braid_word=(1,) * 12,
            factor_words=((swap, swap), (cycle, cycle, cycle)),
            assignments=(((swap, (0, 1))), ((cycle, (0, 1, 2)))),
            expressions=((), ()),
        )

        self.assertEqual(audit.product_endpoint, ((0, 1), (0, 1, 2)))
        self.assertEqual(audit.product_witness, ())
        self.assertEqual(audit.product_witness_value, audit.product_endpoint)
        self.assertTrue(audit.product_witness_matches_endpoint)
        self.assertTrue(audit.identity_product_longitude_signature)
        self.assertTrue(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_expression
        )
        self.assertTrue(audit.identity_longitudes_kill_product_endpoint_by_expression)

    def test_unit_composite_product_expression_rejects_bad_factor(self):
        swap = (1, 0)
        cycle = (1, 2, 0)
        c2 = TransformationMonoid.generated((swap,))
        c3 = TransformationMonoid.generated((cycle,))

        audit = unit_composite_product_longitude_expression_audit(
            (c2, c3),
            n=2,
            braid_word=(1,) * 12,
            factor_words=((swap,), (cycle, cycle, cycle)),
            assignments=(((swap, (0, 1))), ((cycle, (0, 1, 2)))),
            expressions=((), ()),
        )

        self.assertTrue(audit.identity_product_longitude_signature)
        self.assertFalse(audit.factor_audits[0].expression_matches_composite)
        self.assertNotEqual(audit.product_witness_value, audit.product_endpoint)
        self.assertFalse(audit.product_witness_matches_endpoint)
        self.assertFalse(
            audit.product_endpoint_lies_in_product_longitude_subgroup_by_expression
        )
        self.assertFalse(audit.identity_longitudes_kill_product_endpoint_by_expression)

    def test_unit_composite_product_expression_requires_parallel_data(self):
        c2 = TransformationMonoid.generated(((1, 0),))
        with self.assertRaises(ValueError):
            unit_composite_product_longitude_expression_audit(
                (c2,),
                2,
                (1, 1),
                (((1, 0),),),
                (),
                (((1, 1),),),
            )

    def test_unit_composite_product_detection_records_vacuous_visible_endpoint(self):
        swap = (1, 0)
        cycle = (1, 2, 0)
        c2 = TransformationMonoid.generated((swap,))
        c3 = TransformationMonoid.generated((cycle,))

        audit = unit_composite_product_detection_audit(
            (c2, c3),
            n=2,
            braid_word=(1, 1),
            factor_words=((swap,), (cycle,)),
        )

        self.assertFalse(audit.identity_product_longitude_signature)
        self.assertEqual(audit.product_endpoint, (swap, cycle))
        self.assertTrue(audit.product_endpoint_lies_in_product_longitude_subgroup)
        self.assertTrue(audit.identity_longitudes_kill_product_endpoint)
        self.assertTrue(audit.proves_product_endpoint_detector_when_enumerated)

    def test_unit_composite_product_detection_rejects_visible_endpoint(self):
        cycle = (1, 2, 0)
        c3 = TransformationMonoid.generated((cycle,))

        audit = unit_composite_product_detection_audit(
            (c3,),
            n=2,
            braid_word=(1,) * 6,
            factor_words=((cycle,),),
        )

        self.assertTrue(audit.all_permutation_branches)
        self.assertEqual(audit.product_endpoint, (cycle,))
        self.assertFalse(audit.all_composites_lie_in_longitude_subgroups)
        self.assertFalse(audit.all_identity_longitudes_kill_composites)
        self.assertFalse(audit.product_endpoint_in_product_subgroup)
        self.assertTrue(audit.identity_product_longitude_signature)
        self.assertFalse(audit.product_endpoint_lies_in_product_longitude_subgroup)
        self.assertFalse(audit.identity_longitudes_kill_product_endpoint)
        self.assertEqual(audit.product_subgroup_size, 1)
        self.assertFalse(audit.proves_single_product_detector_when_enumerated)
        self.assertFalse(audit.proves_product_endpoint_detector_when_enumerated)
        self.assertTrue(audit.is_finite_product_unit_detector_failure)

    def test_unit_composite_product_detection_can_skip_large_product(self):
        cycle2 = TransformationMonoid.generated(((1, 0),))
        cycle3 = TransformationMonoid.generated(((1, 2, 0),))

        audit = unit_composite_product_detection_audit(
            (cycle2, cycle3),
            n=2,
            braid_word=(1, 1),
            factor_words=(((1, 0),), ((1, 2, 0),)),
            max_product_order=5,
        )

        self.assertTrue(audit.truncated)
        self.assertEqual(audit.product_endpoint, ((1, 0), (1, 2, 0)))
        self.assertEqual(audit.product_group_order, 6)
        self.assertIsNone(audit.product_subgroup_size)
        self.assertIsNone(audit.product_endpoint_in_product_subgroup)
        self.assertFalse(audit.product_endpoint_lies_in_product_longitude_subgroup)
        self.assertFalse(audit.identity_longitudes_kill_product_endpoint)
        self.assertFalse(audit.proves_single_product_detector_when_enumerated)
        self.assertFalse(audit.proves_product_endpoint_detector_when_enumerated)

    def test_unit_composite_product_detection_requires_parallel_words(self):
        c2 = TransformationMonoid.generated(((1, 0),))
        with self.assertRaises(ValueError):
            unit_composite_product_detection_audit((c2,), 2, (1, 1), ())


if __name__ == "__main__":
    unittest.main()
