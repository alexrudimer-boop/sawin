import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    TransformationMonoid,
    aperiodic_permutation_audit,
    compose_transformation_word,
    is_aperiodic_element,
    is_aperiodic_monoid,
    is_permutation_transformation,
    monoid_permutation_group,
    permutation_elements,
    transformation_power,
    unit_composite_detection_audit,
    unit_composite_longitude_expression_audit,
    unit_composite_longitude_route_audit,
    unit_composite_product_detection_audit,
    unit_composite_product_longitude_expression_audit,
    unit_factorization_audit,
    unit_longitude_subgroup_audit,
    unit_section_detection_audit,
    unit_section_product_detection_audit,
)


class SemigroupHolonomyTests(unittest.TestCase):
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
