import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    abelian_longitude_image_audit,
    abelian_longitude_matrix_witness_audit,
    abelian_longitude_matrix_witness_to_subgroup_witness,
    abelian_longitude_value_generators,
    abelian_longitude_value_subgroup_elements,
    artin_detector_rack,
    artin_detector_lift_braid_audit,
    artin_detector_lift_inverse_row_audit,
    artin_detector_lift_negative_update,
    artin_detector_lift_positive_update,
    artin_detector_lift_state,
    artin_detector_lift_transition_audit,
    artin_images,
    artin_longitudes,
    artin_longitude_exponent_matrix,
    conjugate_longitude_subgroup_witness,
    conjugate_longitude_subgroup_witness_audit,
    cyclic_group,
    detector_rack_state,
    direct_product_group,
    direct_product_detector_action_audit,
    direct_product_longitude_subgroup_audit,
    direct_product_longitude_subgroup_witness,
    direct_product_longitude_subgroup_witness_audit,
    diagonal_product_invisibility_audit,
    evaluate_artin_images,
    evaluate_artin_longitudes,
    evaluate_abelian_longitude_matrix_witness,
    evaluate_longitude_expression,
    evaluate_longitude_subgroup_witness,
    evaluate_terminal_label_expression,
    FiniteBraidedSet,
    FiniteGroupHomomorphism,
    has_identity_longitude_signature,
    has_identity_abelian_longitude_signature,
    has_trivial_abelian_longitudes_mod,
    homomorphic_longitude_subgroup_audit,
    identity_solution,
    is_rack_solution,
    is_abelian_group,
    is_identity_action,
    left_regular_representation,
    longitude_blind_movers,
    longitude_subgroup_profile,
    longitude_value_generators,
    longitude_value_subgroup_elements,
    normal_quotient_longitude_lift_audit,
    normalized_law_prefix_witness_audit,
    pure_braid_generator,
    principal_gauge_cocycle_failures,
    principal_gauge_extension_detector_audit,
    principal_gauge_extension_rack,
    pushforward_longitude_subgroup_witness,
    pushforward_longitude_subgroup_witness_audit,
    quotient_group_by_normal_subgroup,
    rack_extension_detector_audit,
    rack_inner_group,
    rack_inner_detector_lift_audit,
    rack_inner_detector_lift_row_audit,
    rack_longitude_action,
    rack_longitude_factorization,
    right_stabilization_longitude_audit,
    right_rack_inner_detector_lift_audit,
    rack_solution,
    reverse_braid_word,
    sharp_obstruction_rack,
    symmetric_detector_reduction_audit,
    symmetric_normalized_law_prefix_witness_audit,
    symmetric_group,
    transport_state_left_translation_failures,
    transport_state_rack,
    transport_state_rackification_audit,
)


class ArtinLongitudeTests(unittest.TestCase):
    def test_artin_images_satisfy_braid_relation(self):
        self.assertEqual(artin_images(3, [1, 2, 1]), artin_images(3, [2, 1, 2]))

    def test_artin_generator_longitudes(self):
        data = artin_longitudes(2, [1])
        self.assertEqual(data.permutation, (1, 0))
        self.assertEqual(data.longitudes, (((0, 1),), ()))

    def test_canceling_braid_has_identity_signature(self):
        group = symmetric_group(3)
        self.assertTrue(has_identity_longitude_signature(group, 2, [1, -1]))

    def test_positive_generator_is_not_identity_signature(self):
        group = cyclic_group(2)
        self.assertFalse(has_identity_longitude_signature(group, 2, [1]))

    def test_longitude_value_subgroup_for_positive_generator(self):
        group = cyclic_group(3)
        generators = longitude_value_generators(group, 2, [1])
        subgroup = longitude_value_subgroup_elements(group, 2, [1])

        self.assertEqual(set(generators), {0, 1, 2})
        self.assertEqual(set(subgroup), {0, 1, 2})

    def test_longitude_subgroup_profile_matches_identity_signature(self):
        groups = {"C2": cyclic_group(2), "C3": cyclic_group(3)}
        braid = pure_braid_generator(1, 2) * 6
        profile = longitude_subgroup_profile(groups, 2, braid)

        self.assertEqual(tuple(row.name for row in profile), ("C2", "C3"))
        self.assertTrue(all(row.identity_longitude_signature for row in profile))
        self.assertEqual(tuple(row.subgroup_size for row in profile), (1, 1))

    def test_pure_generator_abelian_longitude_matrix(self):
        braid = pure_braid_generator(1, 3)
        self.assertEqual(
            artin_longitude_exponent_matrix(3, braid),
            (
                (0, 0, 1),
                (0, 0, 0),
                (1, 0, 0),
            ),
        )

    def test_abelian_longitude_modulus_criterion(self):
        braid = pure_braid_generator(1, 2)
        self.assertFalse(has_trivial_abelian_longitudes_mod(3, 2, braid))
        triple = braid + braid + braid
        self.assertTrue(has_trivial_abelian_longitudes_mod(3, 2, triple))
        self.assertTrue(has_identity_longitude_signature(cyclic_group(3), 2, triple))

    def test_abelian_longitude_matrix_formula_matches_exhaustive_subgroup(self):
        group = cyclic_group(4)
        braid = pure_braid_generator(1, 2) * 2

        audit = abelian_longitude_image_audit(
            group,
            2,
            braid,
            compare_by_enumeration=True,
        )

        self.assertTrue(is_abelian_group(group))
        self.assertEqual(audit.exponent_matrix, ((0, 2), (2, 0)))
        self.assertEqual(audit.coefficient_entries, (0, 2))
        self.assertEqual(set(audit.matrix_generators), {0, 2})
        self.assertEqual(set(audit.matrix_subgroup), {0, 2})
        self.assertEqual(set(audit.enumerated_subgroup), {0, 2})
        self.assertTrue(audit.enumeration_matches_matrix_formula)
        self.assertFalse(audit.identity_signature_by_matrix)
        self.assertFalse(has_identity_abelian_longitude_signature(group, 2, braid))

    def test_abelian_longitude_matrix_formula_handles_products(self):
        group = direct_product_group((cyclic_group(2), cyclic_group(3)))
        braid = pure_braid_generator(1, 2)
        invisible = braid * 6

        self.assertEqual(
            set(abelian_longitude_value_subgroup_elements(group, 2, braid)),
            set(group.elements),
        )
        self.assertEqual(
            set(abelian_longitude_value_generators(group, 2, invisible)),
            {group.identity},
        )
        self.assertTrue(has_identity_abelian_longitude_signature(group, 2, invisible))

    def test_abelian_longitude_matrix_formula_rejects_nonabelian_groups(self):
        self.assertFalse(is_abelian_group(symmetric_group(3)))
        with self.assertRaises(ValueError):
            abelian_longitude_value_subgroup_elements(
                symmetric_group(3),
                2,
                pure_braid_generator(1, 2),
            )

    def test_abelian_matrix_witness_becomes_literal_longitude_witness(self):
        group = cyclic_group(4)
        braid = pure_braid_generator(1, 2) * 2
        witness = ((1, 0, 1, 1),)

        audit = abelian_longitude_matrix_witness_audit(
            group,
            2,
            braid,
            endpoint=2,
            witness=witness,
        )

        self.assertEqual(
            evaluate_abelian_longitude_matrix_witness(group, 2, braid, witness),
            2,
        )
        self.assertEqual(
            abelian_longitude_matrix_witness_to_subgroup_witness(group, 2, witness),
            (((0, 1), 0, 1),),
        )
        self.assertEqual(audit.matrix_witness_value, 2)
        self.assertEqual(audit.longitude_subgroup_witness_value, 2)
        self.assertTrue(audit.endpoint_matches_matrix_witness)
        self.assertTrue(audit.matrix_witness_matches_longitude_witness)
        self.assertTrue(audit.proves_endpoint_in_abelian_longitude_subgroup)

    def test_abelian_matrix_witness_uses_signed_letters(self):
        group = cyclic_group(5)
        braid = pure_braid_generator(1, 2)
        witness = ((2, 0, 1, 1), (3, 1, 0, -1))

        audit = abelian_longitude_matrix_witness_audit(
            group,
            2,
            braid,
            endpoint=4,
            witness=witness,
        )

        self.assertEqual(audit.matrix_witness_value, 4)
        self.assertTrue(audit.proves_endpoint_in_abelian_longitude_subgroup)

    def test_abelian_matrix_witness_validates_rows(self):
        group = cyclic_group(3)
        braid = pure_braid_generator(1, 2)

        with self.assertRaises(ValueError):
            evaluate_abelian_longitude_matrix_witness(
                symmetric_group(3),
                2,
                braid,
                (),
            )
        with self.assertRaises(ValueError):
            evaluate_abelian_longitude_matrix_witness(group, 2, braid, ((4, 0, 0, 1),))
        with self.assertRaises(IndexError):
            evaluate_abelian_longitude_matrix_witness(group, 2, braid, ((1, 2, 0, 1),))
        with self.assertRaises(IndexError):
            evaluate_abelian_longitude_matrix_witness(group, 2, braid, ((1, 0, 2, 1),))
        with self.assertRaises(ValueError):
            evaluate_abelian_longitude_matrix_witness(group, 2, braid, ((1, 0, 0, 2),))

    def test_longitude_data_stabilizes_under_extra_right_strands(self):
        braid = pure_braid_generator(1, 3)
        small = artin_longitudes(3, braid)
        large = artin_longitudes(5, braid)
        self.assertEqual(large.permutation, (small.permutation[0], small.permutation[1], small.permutation[2], 3, 4))
        self.assertEqual(large.longitudes[:3], small.longitudes)
        self.assertEqual(large.longitudes[3:], (tuple(), tuple()))
        self.assertEqual(
            artin_longitude_exponent_matrix(5, braid),
            (
                (0, 0, 1, 0, 0),
                (0, 0, 0, 0, 0),
                (1, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
                (0, 0, 0, 0, 0),
            ),
        )

    def test_longitude_identity_is_invariant_under_strand_reversal(self):
        group = symmetric_group(3)
        braid = (1, 2, -1, 2, 2, -1)
        reversed_braid = reverse_braid_word(3, braid)
        invisible = pure_braid_generator(1, 3) * 6

        self.assertEqual(
            has_identity_longitude_signature(group, 3, braid),
            has_identity_longitude_signature(group, 3, reversed_braid),
        )
        self.assertTrue(has_identity_longitude_signature(group, 3, invisible))
        self.assertTrue(
            has_identity_longitude_signature(
                group,
                3,
                reverse_braid_word(3, invisible),
            )
        )

    def test_direct_product_group_combines_longitude_detectors(self):
        left = cyclic_group(2)
        right = cyclic_group(3)
        product_group = direct_product_group((left, right))
        braid = pure_braid_generator(1, 2)
        self.assertFalse(has_identity_longitude_signature(product_group, 2, braid))

        sixth_power = braid * 6
        self.assertTrue(has_identity_longitude_signature(left, 2, sixth_power))
        self.assertTrue(has_identity_longitude_signature(right, 2, sixth_power))
        self.assertTrue(has_identity_longitude_signature(product_group, 2, sixth_power))

        double = braid * 2
        self.assertTrue(has_identity_longitude_signature(left, 2, double))
        self.assertFalse(has_identity_longitude_signature(right, 2, double))
        self.assertFalse(has_identity_longitude_signature(product_group, 2, double))

    def test_direct_product_longitude_subgroup_is_product_of_factor_subgroups(self):
        left = cyclic_group(2)
        right = cyclic_group(3)
        braid = pure_braid_generator(1, 2)

        audit = direct_product_longitude_subgroup_audit((left, right), 2, braid)

        self.assertEqual(audit.factor_orders, (2, 3))
        self.assertEqual(audit.factor_subgroup_sizes, (2, 3))
        self.assertEqual(audit.product_group_order, 6)
        self.assertEqual(audit.product_subgroup_size, 6)
        self.assertEqual(audit.expected_product_subgroup_size, 6)
        self.assertTrue(audit.product_subgroup_equals_factor_product)

        invisible = braid * 6
        trivial = direct_product_longitude_subgroup_audit((left, right), 2, invisible)
        self.assertEqual(trivial.factor_subgroup_sizes, (1, 1))
        self.assertEqual(trivial.product_subgroup_size, 1)
        self.assertTrue(trivial.product_subgroup_equals_factor_product)

    def test_empty_direct_product_longitude_subgroup_is_trivial(self):
        audit = direct_product_longitude_subgroup_audit((), 2, pure_braid_generator(1, 2))

        self.assertEqual(audit.factor_orders, ())
        self.assertEqual(audit.factor_subgroup_sizes, ())
        self.assertEqual(audit.product_group_order, 1)
        self.assertEqual(audit.product_subgroup_size, 1)
        self.assertEqual(audit.expected_product_subgroup_size, 1)
        self.assertTrue(audit.product_subgroup_equals_factor_product)

    def test_longitude_value_subgroups_are_functorial_under_surjections(self):
        source = cyclic_group(6)
        target = cyclic_group(3)
        quotient = FiniteGroupHomomorphism(
            source,
            target,
            {element: element % 3 for element in source.elements},
        )

        audit = homomorphic_longitude_subgroup_audit(
            quotient,
            n=2,
            braid_word=pure_braid_generator(1, 2),
        )

        self.assertTrue(audit.homomorphism_surjective)
        self.assertTrue(audit.image_contained_in_target_subgroup)
        self.assertTrue(audit.target_subgroup_equals_image)
        self.assertEqual(audit.target_subgroup_size, 3)

    def test_longitude_value_subgroup_image_can_be_proper_for_nonsurjection(self):
        source = cyclic_group(2)
        target = cyclic_group(4)
        inclusion = FiniteGroupHomomorphism(
            source,
            target,
            {element: (2 * element) % 4 for element in source.elements},
        )

        audit = homomorphic_longitude_subgroup_audit(
            inclusion,
            n=2,
            braid_word=pure_braid_generator(1, 2),
        )

        self.assertFalse(audit.homomorphism_surjective)
        self.assertTrue(audit.image_contained_in_target_subgroup)
        self.assertFalse(audit.target_subgroup_equals_image)
        self.assertEqual(audit.image_subgroup_size, 2)
        self.assertEqual(audit.target_subgroup_size, 4)

    def test_longitude_subgroup_witness_pushes_forward_under_homomorphism(self):
        source = cyclic_group(6)
        target = cyclic_group(3)
        quotient = FiniteGroupHomomorphism(
            source,
            target,
            {element: element % 3 for element in source.elements},
        )
        witness = ((((4, 0), 1, 1),))

        pushed = pushforward_longitude_subgroup_witness(quotient, witness)
        audit = pushforward_longitude_subgroup_witness_audit(
            quotient,
            n=2,
            braid_word=(1, 1),
            witness=witness,
        )

        self.assertEqual(pushed, ((((1, 0), 1, 1),)))
        self.assertEqual(audit.pushed_witness, pushed)
        self.assertEqual(audit.target_image_value, quotient.apply(audit.source_value))
        self.assertEqual(audit.pushed_witness_value, audit.target_image_value)
        self.assertTrue(audit.pushforward_matches_image)

        with self.assertRaises(ValueError):
            pushforward_longitude_subgroup_witness(
                quotient,
                ((((7, 0), 1, 1),)),
            )

    def test_normal_quotient_lift_splits_abelian_and_kernel_witnesses(self):
        group = symmetric_group(3)
        alternating = ((0, 1, 2), (1, 2, 0), (2, 0, 1))
        quotient, projection = quotient_group_by_normal_subgroup(
            group,
            alternating,
        )
        braid = (1, 1)
        identity = group.identity
        transposition = (1, 0, 2)
        three_cycle = (1, 2, 0)
        endpoint = group.mul(three_cycle, transposition)
        lifted_witness = (((transposition, identity), 1, 1),)
        kernel_witness = (((three_cycle, identity), 1, 1),)
        quotient_witness = (
            (
                tuple(projection.apply(value) for value in (transposition, identity)),
                1,
                1,
            ),
        )

        audit = normal_quotient_longitude_lift_audit(
            projection,
            2,
            braid,
            endpoint,
            quotient_witness,
            lifted_witness,
            kernel_witness,
        )

        self.assertEqual(audit.kernel_size, 3)
        self.assertEqual(audit.quotient_endpoint, projection.apply(endpoint))
        self.assertTrue(audit.quotient_witness_matches_endpoint)
        self.assertTrue(audit.lifted_witness_projects_to_quotient_witness)
        self.assertTrue(audit.kernel_correction_in_kernel)
        self.assertTrue(audit.kernel_witness_assignments_in_kernel)
        self.assertTrue(audit.kernel_witness_matches_correction)
        self.assertTrue(audit.combined_witness_matches_endpoint)
        self.assertTrue(audit.proves_endpoint_in_longitude_subgroup_by_normal_lift)

    def test_normal_quotient_lift_rejects_nonkernel_correction_witness(self):
        group = symmetric_group(3)
        alternating = ((0, 1, 2), (1, 2, 0), (2, 0, 1))
        _quotient, projection = quotient_group_by_normal_subgroup(
            group,
            alternating,
        )
        braid = (1, 1)
        identity = group.identity
        transposition = (1, 0, 2)
        three_cycle = (1, 2, 0)
        endpoint = group.mul(three_cycle, transposition)
        lifted_witness = (((transposition, identity), 1, 1),)
        bad_kernel_witness = (((transposition, identity), 1, 1),)
        quotient_witness = (
            (
                tuple(projection.apply(value) for value in (transposition, identity)),
                1,
                1,
            ),
        )

        audit = normal_quotient_longitude_lift_audit(
            projection,
            2,
            braid,
            endpoint,
            quotient_witness,
            lifted_witness,
            bad_kernel_witness,
        )

        self.assertFalse(audit.kernel_witness_assignments_in_kernel)
        self.assertFalse(audit.kernel_witness_matches_correction)
        self.assertFalse(audit.proves_endpoint_in_longitude_subgroup_by_normal_lift)

    def test_longitude_subgroup_witness_is_stable_under_chart_conjugation(self):
        group = symmetric_group(3)
        conjugator = (1, 2, 0)
        witness = (
            (((1, 0, 2), (0, 2, 1)), 0, 1),
            (((0, 2, 1), (1, 2, 0)), 1, -1),
        )
        braid = (1, 1)

        conjugated = conjugate_longitude_subgroup_witness(
            group,
            conjugator,
            witness,
        )
        audit = conjugate_longitude_subgroup_witness_audit(
            group,
            2,
            braid,
            conjugator,
            witness,
        )

        self.assertEqual(audit.conjugated_witness, conjugated)
        self.assertEqual(
            audit.conjugated_witness_value,
            audit.expected_conjugate_value,
        )
        self.assertTrue(audit.conjugated_witness_matches)

        with self.assertRaises(ValueError):
            conjugate_longitude_subgroup_witness(
                group,
                (0, 0, 0),
                witness,
            )

    def test_direct_product_longitude_subgroup_witness_assembles_factors(self):
        left = cyclic_group(2)
        right = cyclic_group(3)
        braid = (1, 1)
        factor_witnesses = (
            ((((1, 0), 1, 1),)),
            ((((1, 0), 1, 1),)),
        )

        witness = direct_product_longitude_subgroup_witness(
            (left, right),
            2,
            factor_witnesses,
        )
        audit = direct_product_longitude_subgroup_witness_audit(
            (left, right),
            2,
            braid,
            factor_witnesses,
        )

        self.assertEqual(
            witness,
            (
                (((1, 0), (0, 0)), 1, 1),
                (((0, 1), (0, 0)), 1, 1),
            ),
        )
        self.assertEqual(audit.factor_values, (1, 1))
        self.assertEqual(audit.expected_product_value, (1, 1))
        self.assertEqual(audit.product_witness, witness)
        self.assertEqual(audit.product_witness_value, (1, 1))
        self.assertTrue(audit.product_witness_matches_factors)

    def test_direct_product_longitude_subgroup_witness_handles_empty_product(self):
        audit = direct_product_longitude_subgroup_witness_audit(
            (),
            2,
            (1, 1),
            (),
        )

        self.assertEqual(audit.factor_values, ())
        self.assertEqual(audit.product_witness, ())
        self.assertEqual(audit.product_witness_value, ())
        self.assertEqual(audit.expected_product_value, ())
        self.assertTrue(audit.product_witness_matches_factors)

        with self.assertRaises(ValueError):
            direct_product_longitude_subgroup_witness(
                (cyclic_group(2),),
                2,
                (),
            )

        with self.assertRaises(ValueError):
            direct_product_longitude_subgroup_witness(
                (cyclic_group(2),),
                2,
                ((((1,), 1, 1),),),
            )

    def test_artin_detector_rack_is_ybe(self):
        group = symmetric_group(3)
        rack = artin_detector_rack(group)
        self.assertTrue(rack.is_ybe())

    def test_trivial_two_factor_forces_artin_permutation(self):
        group = cyclic_group(1)
        with_trivial_two = artin_detector_rack(group, include_trivial_two=True)
        without_trivial_two = artin_detector_rack(group, include_trivial_two=False)

        self.assertFalse(is_identity_action(with_trivial_two, 2, (1,)))
        self.assertTrue(is_identity_action(with_trivial_two, 2, (1, 1)))
        self.assertTrue(is_identity_action(without_trivial_two, 2, (1,)))

    def test_sharp_obstruction_rack_is_explicit_product_rack(self):
        quotient_rack = rack_solution(["a", "b"], lambda _left, right: right)
        group = cyclic_group(2)

        rack = sharp_obstruction_rack(quotient_rack, group)

        self.assertTrue(rack.is_ybe())
        self.assertTrue(is_rack_solution(rack))
        self.assertEqual(len(rack.elements), len(quotient_rack.elements) * 2 * 2 * 2)

    def test_sharp_obstruction_rack_kernel_is_intersection(self):
        quotient_rack = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        group = cyclic_group(2)
        rack = sharp_obstruction_rack(quotient_rack, group)
        words = [
            tuple(),
            (1,),
            (1, -1),
            (1, 1),
            (1, 2, 1),
            (1, 1, 2, 2, -1, -2),
        ]

        for word in words:
            self.assertEqual(
                is_identity_action(rack, 3, word),
                is_identity_action(quotient_rack, 3, word)
                and has_identity_longitude_signature(group, 3, word),
                msg=word,
            )

    def test_sharp_obstruction_rack_requires_rack_detector(self):
        with self.assertRaises(ValueError):
            sharp_obstruction_rack(identity_solution([0, 1]), cyclic_group(2))

    def test_detector_rack_kernel_matches_longitude_signature(self):
        group = cyclic_group(2)
        rack = artin_detector_rack(group)
        words = [
            tuple(),
            (1,),
            (1, -1),
            (1, 1),
            (1, 2, 1),
            (1, 2, -1, -2),
            (1, 1, 2, 2, -1, -2),
        ]
        for word in words:
            self.assertEqual(
                is_identity_action(rack, 3, word),
                has_identity_longitude_signature(group, 3, word),
                msg=word,
            )

    def test_detector_rack_state_matches_artin_data(self):
        group = symmetric_group(3)
        assignment = (group.elements[1], group.elements[2], group.elements[3])
        word = [1, 2, -1, 2]
        image_values, longitude_values = detector_rack_state(group, assignment, word)
        self.assertEqual(image_values, evaluate_artin_images(group, assignment, word))
        self.assertEqual(longitude_values, evaluate_artin_longitudes(group, assignment, word))

    def test_artin_detector_lift_local_rows_match_active_detector(self):
        group = symmetric_group(3)
        left = ((1, 0, 2), (0, 1, 2))
        right = ((0, 2, 1), (1, 2, 0))

        positive_left, positive_right = artin_detector_lift_positive_update(
            group,
            left,
            right,
        )
        positive = artin_detector_lift_transition_audit(
            group,
            1,
            left,
            right,
            positive_left,
            positive_right,
        )

        self.assertTrue(positive.row_matches_artin_detector)
        self.assertEqual(positive.expected_left, positive_left)
        self.assertEqual(positive.expected_right, positive_right)

        negative_left, negative_right = artin_detector_lift_negative_update(
            group,
            left,
            right,
        )
        negative = artin_detector_lift_transition_audit(
            group,
            -1,
            left,
            right,
            negative_left,
            negative_right,
        )

        self.assertTrue(negative.row_matches_artin_detector)
        self.assertEqual(negative.expected_left, negative_left)
        self.assertEqual(negative.expected_right, negative_right)

        bad = artin_detector_lift_transition_audit(
            group,
            -1,
            left,
            right,
            left,
            right,
        )
        self.assertFalse(bad.row_matches_artin_detector)

    def test_negative_detector_lift_row_is_positive_inverse(self):
        group = symmetric_group(3)
        left = ((1, 0, 2), (0, 1, 2))
        right = ((0, 2, 1), (1, 2, 0))

        audit = artin_detector_lift_inverse_row_audit(group, left, right)

        self.assertTrue(audit.positive_then_negative_recovers_input)
        self.assertTrue(audit.negative_then_positive_recovers_input)
        self.assertTrue(audit.negative_row_is_positive_inverse)

    def test_rack_inner_rows_satisfy_detector_lift_identities(self):
        rack = rack_solution(range(3), lambda left, right: (2 * left - right) % 3)
        group = rack_inner_group(rack)

        row = rack_inner_detector_lift_row_audit(
            rack,
            0,
            1,
            endpoint_left=group.elements[1],
            endpoint_right=group.elements[2],
        )
        audit = rack_inner_detector_lift_audit(
            rack,
            endpoint_labels=group.elements,
        )

        self.assertTrue(row.left_translation_conjugacy_matches)
        self.assertTrue(row.right_output_translation_matches)
        self.assertTrue(row.endpoint_transport_matches_crossing)
        self.assertTrue(row.positive_row_matches_artin_detector)
        self.assertTrue(row.negative_row_is_positive_inverse)
        self.assertTrue(row.proves_rack_inner_detector_lift_row)
        self.assertEqual(audit.rack_size, 3)
        self.assertEqual(audit.endpoint_label_count, len(group.elements))
        self.assertEqual(audit.row_count, 9 * len(group.elements) ** 2)
        self.assertTrue(audit.all_positive_rows_match_artin_detector)
        self.assertTrue(audit.all_translation_conjugacies_match)
        self.assertTrue(audit.all_endpoint_transports_match_crossing)
        self.assertTrue(audit.all_negative_rows_follow_by_inverse)
        self.assertTrue(audit.proves_rack_inner_detector_lift_rows)

    def test_right_rack_layer_uses_side_opposite_inner_rows(self):
        right_layer = rack_solution(
            range(3),
            lambda left, right: (2 * left - right) % 3,
        )
        # Convert the left rack fixture into the atom-layer convention
        # R(a,b)=(b,a^b) by taking its side-opposite solution.
        table = {
            (left, right): (right, right_layer.R[(right, left)][0])
            for left in right_layer.elements
            for right in right_layer.elements
        }
        atom_layer = FiniteBraidedSet(right_layer.elements, table)

        audit = right_rack_inner_detector_lift_audit(atom_layer)

        self.assertEqual(audit.rack_size, 3)
        self.assertTrue(audit.proves_rack_inner_detector_lift_rows)

    def test_principal_gauge_extension_detector_closes_cocycle_rows(self):
        base = rack_solution(range(2), lambda _left, right: right)
        unit = cyclic_group(3)
        cocycle = {
            (left, right): left % 3
            for left in base.elements
            for right in base.elements
        }

        failures = principal_gauge_cocycle_failures(base, unit, cocycle)
        extension = principal_gauge_extension_rack(base, unit, cocycle)
        audit = principal_gauge_extension_detector_audit(base, unit, cocycle)

        self.assertEqual(failures, tuple())
        self.assertEqual(len(extension.elements), 6)
        self.assertTrue(is_rack_solution(extension))
        self.assertTrue(extension.is_ybe())
        self.assertEqual(audit.base_rack_size, 2)
        self.assertEqual(audit.unit_group_order, 3)
        self.assertEqual(audit.extension_size, 6)
        self.assertTrue(audit.cocycle_identity_holds)
        self.assertTrue(audit.principal_extension_is_finite_rack)
        self.assertIsNotNone(audit.detector_lift_audit)
        self.assertTrue(audit.proves_principal_gauge_detector)

    def test_principal_gauge_extension_audit_exposes_nonprincipal_failure(self):
        base = rack_solution(range(2), lambda _left, right: right)
        unit = symmetric_group(3)
        transposition_01 = (1, 0, 2)
        transposition_12 = (0, 2, 1)
        cocycle = {
            (left, right): unit.identity
            for left in base.elements
            for right in base.elements
        }
        cocycle[(0, 0)] = transposition_01
        cocycle[(1, 0)] = transposition_12

        audit = principal_gauge_extension_detector_audit(base, unit, cocycle)

        self.assertGreater(len(audit.cocycle_failures), 0)
        self.assertFalse(audit.cocycle_identity_holds)
        self.assertTrue(audit.extension_is_rack_form)
        self.assertFalse(audit.extension_is_ybe)
        self.assertFalse(audit.principal_extension_is_finite_rack)
        self.assertFalse(audit.proves_principal_gauge_detector)

    def test_transport_state_rackification_closes_nonprincipal_gauge(self):
        atom = rack_solution(range(2), lambda _left, right: right)
        states = tuple(range(3))

        def transition(_left_atom, _right_atom, left_state, right_state):
            return (2 * left_state - right_state) % 3

        transport = transport_state_rack(atom, states, transition)
        audit = transport_state_rackification_audit(atom, states, transition)
        extension_audit = rack_extension_detector_audit(
            transport,
            atom,
            {element: element[0] for element in transport.elements},
        )

        self.assertEqual(len(transport.elements), 6)
        self.assertTrue(is_rack_solution(transport))
        self.assertTrue(transport.is_ybe())
        self.assertEqual(audit.left_translation_failures, tuple())
        self.assertTrue(audit.all_left_translations_bijective)
        self.assertTrue(audit.transport_state_is_finite_rack_extension)
        self.assertTrue(audit.proves_transport_state_detector)
        self.assertTrue(extension_audit.projection_is_rack_homomorphism)
        self.assertTrue(extension_audit.proves_rack_extension_detector)

    def test_transport_state_rackification_flags_nonbijective_transition(self):
        atom = rack_solution(range(2), lambda _left, right: right)
        states = tuple(range(2))

        def transition(_left_atom, _right_atom, _left_state, _right_state):
            return 0

        failures = transport_state_left_translation_failures(
            atom,
            states,
            transition,
        )
        audit = transport_state_rackification_audit(atom, states, transition)

        self.assertGreater(len(failures), 0)
        self.assertFalse(audit.all_left_translations_bijective)
        self.assertFalse(audit.transport_rack_built)
        self.assertIsNone(audit.extension_detector_audit)
        self.assertFalse(audit.proves_transport_state_detector)

    def test_artin_detector_lift_state_matches_artin_images_and_longitudes(self):
        group = symmetric_group(3)
        assignment = (group.elements[1], group.elements[2], group.elements[3])
        word = (1, 2, -1, 2)

        state = artin_detector_lift_state(group, assignment, word)
        image_values, longitude_values = detector_rack_state(group, assignment, word)
        audit = artin_detector_lift_braid_audit(
            group,
            assignment,
            word,
            endpoint_expression=((0, 1), (2, -1)),
        )

        self.assertEqual(tuple(label[0] for label in state), image_values)
        self.assertEqual(tuple(label[1] for label in state), longitude_values)
        self.assertTrue(audit.meridians_match_artin_images)
        self.assertTrue(audit.longitudes_match_artin_longitudes)
        self.assertEqual(
            audit.endpoint_value,
            evaluate_terminal_label_expression(
                group,
                longitude_values,
                ((0, 1), (2, -1)),
            ),
        )
        self.assertEqual(audit.endpoint_value, audit.expected_endpoint_value)
        self.assertTrue(audit.endpoint_matches_longitude_expression)
        self.assertTrue(audit.proves_detector_lift_recursion)

    def test_longitude_expression_evaluates_word_in_longitude_values(self):
        group = cyclic_group(3)
        assignment = (1, 2)
        braid = (1, 1)

        values = evaluate_artin_longitudes(group, assignment, braid)
        expression_value = evaluate_longitude_expression(
            group,
            assignment,
            braid,
            ((0, 1), (1, -1)),
        )

        self.assertEqual(expression_value, group.mul(values[0], group.inv(values[1])))

        with self.assertRaises(ValueError):
            evaluate_longitude_expression(group, assignment, braid, ((0, 2),))

        with self.assertRaises(IndexError):
            evaluate_longitude_expression(group, assignment, braid, ((2, 1),))

    def test_longitude_subgroup_witness_allows_separate_assignments(self):
        left = cyclic_group(2)
        right = cyclic_group(3)
        product_group = direct_product_group((left, right))
        braid = (1, 1)

        value = evaluate_longitude_subgroup_witness(
            product_group,
            2,
            braid,
            (
                (((1, 0), (0, 0)), 1, 1),
                (((0, 1), (0, 0)), 1, 1),
            ),
        )
        inverse_value = evaluate_longitude_subgroup_witness(
            product_group,
            2,
            braid,
            ((((0, 1), (0, 0)), 1, -1),),
        )

        self.assertEqual(value, (1, 1))
        self.assertEqual(inverse_value, (0, 2))

    def test_longitude_subgroup_witness_validates_letters(self):
        group = cyclic_group(2)

        self.assertEqual(
            evaluate_longitude_subgroup_witness(group, 2, (1, 1), ()),
            group.identity,
        )

        with self.assertRaises(ValueError):
            evaluate_longitude_subgroup_witness(
                group,
                2,
                (1, 1),
                (((1,), 1, 1),),
            )

        with self.assertRaises(ValueError):
            evaluate_longitude_subgroup_witness(
                group,
                2,
                (1, 1),
                (((1, 0), 1, 2),),
            )

        with self.assertRaises(ValueError):
            evaluate_longitude_subgroup_witness(
                group,
                2,
                (1, 1),
                (((2, 0), 1, 1),),
            )

        with self.assertRaises(IndexError):
            evaluate_longitude_subgroup_witness(
                group,
                2,
                (1, 1),
                (((1, 0), 2, 1),),
            )

    def test_product_detector_action_projects_to_factor_actions(self):
        left = cyclic_group(2)
        right = cyclic_group(3)
        word = (1, 2, -1, 2, 1)

        audit = direct_product_detector_action_audit(
            (left, right),
            (
                (0, 1, 1),
                (0, 1, 2),
            ),
            word,
        )

        self.assertEqual(audit.factor_orders, (2, 3))
        self.assertTrue(audit.image_projections_match)
        self.assertTrue(audit.longitude_projections_match)
        self.assertTrue(audit.detector_projections_match)
        self.assertEqual(audit.projected_image_values, audit.factor_image_values)
        self.assertEqual(audit.projected_longitude_values, audit.factor_longitude_values)

    def test_product_detector_action_requires_factor_assignments(self):
        with self.assertRaises(ValueError):
            direct_product_detector_action_audit((), (), (1,))

        with self.assertRaises(ValueError):
            direct_product_detector_action_audit(
                (cyclic_group(2), cyclic_group(3)),
                ((0, 1),),
                (1,),
            )

    def test_diagonal_product_invisibility_equivalent_to_factors(self):
        left = cyclic_group(2)
        right = cyclic_group(3)
        invisible = pure_braid_generator(1, 2) * 12
        visible_to_left = pure_braid_generator(1, 2) * 3

        all_invisible = diagonal_product_invisibility_audit(
            (left, right),
            2,
            invisible,
        )
        left_visible = diagonal_product_invisibility_audit(
            (left, right),
            2,
            visible_to_left,
        )

        self.assertEqual(all_invisible.group_orders, (2, 3))
        self.assertEqual(all_invisible.product_group_order, 6)
        self.assertEqual(all_invisible.factor_identity_signatures, (True, True))
        self.assertTrue(all_invisible.product_identity_signature)
        self.assertTrue(all_invisible.product_signature_equivalent_to_factors)

        self.assertEqual(left_visible.factor_identity_signatures, (False, True))
        self.assertFalse(left_visible.product_identity_signature)
        self.assertTrue(left_visible.product_signature_equivalent_to_factors)

    def test_right_stabilization_preserves_longitude_data(self):
        braid = pure_braid_generator(1, 3) * 2

        audit = right_stabilization_longitude_audit(3, braid, extra_strands=2)

        self.assertEqual(audit.old_n, 3)
        self.assertEqual(audit.new_n, 5)
        self.assertEqual(audit.new_permutation[:3], audit.old_permutation)
        self.assertEqual(audit.new_permutation[3:], (3, 4))
        self.assertEqual(audit.new_restricted_longitudes, audit.old_longitudes)
        self.assertEqual(audit.added_longitudes, ((), ()))
        self.assertTrue(audit.old_data_preserved)
        self.assertTrue(audit.added_strands_trivial)
        self.assertTrue(audit.stabilization_valid)

    def test_right_stabilization_requires_nonnegative_extra_strands(self):
        with self.assertRaises(ValueError):
            right_stabilization_longitude_audit(2, (1, 1), extra_strands=-1)

    def test_rack_action_is_longitude_action_in_inner_group(self):
        rack = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        self.assertEqual(len(rack_inner_group(rack).elements), 6)
        for tup in ((0, 1, 2), (2, 2, 0), (1, 0, 1)):
            for word in ([1], [1, 2, 1], [2, -1, 2, 1], [1, 1, 2, -1]):
                self.assertEqual(
                    rack_longitude_action(rack, word, tup),
                    rack.braid_action(word, tup),
                )

    def test_rack_longitude_factorization_exposes_input_dependent_assignment(self):
        rack = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        tup = (0, 1, 2)
        word = (1, 2, -1, 2)

        factorization = rack_longitude_factorization(rack, word, tup)

        self.assertEqual(factorization.permutation, artin_longitudes(3, word).permutation)
        self.assertEqual(len(factorization.assignment), len(tup))
        self.assertEqual(len(factorization.longitude_values), len(tup))
        self.assertEqual(factorization.output, rack.braid_action(word, tup))

    def test_rack_longitude_invisibility_kills_finite_rack_action(self):
        rack = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        group = rack_inner_group(rack)
        braid = pure_braid_generator(1, 2) * 6
        self.assertTrue(has_identity_longitude_signature(group, 2, braid))
        for tup in ((0, 1), (1, 2), (2, 0)):
            self.assertEqual(rack_longitude_action(rack, braid, tup), tup)
            self.assertEqual(rack.braid_action(braid, tup), tup)

    def test_inner_group_detector_kernel_is_inside_rack_kernel(self):
        rack = rack_solution([0, 1], lambda _left, right: 1 - right)
        group = rack_inner_group(rack)
        detector = artin_detector_rack(group)
        words = (
            tuple(),
            (1, -1),
            pure_braid_generator(1, 2) * 2,
            (1, 2, -2, -1),
        )

        for word in words:
            if is_identity_action(detector, 3, word):
                self.assertTrue(is_identity_action(rack, 3, word), msg=word)

    def test_identity_longitude_signature_survives_right_stabilization(self):
        group = cyclic_group(2)
        braid = pure_braid_generator(1, 2) * 2

        audit = right_stabilization_longitude_audit(2, braid, extra_strands=3)

        self.assertTrue(has_identity_longitude_signature(group, 2, braid))
        self.assertTrue(audit.stabilization_valid)
        self.assertTrue(has_identity_longitude_signature(group, 5, braid))

    def test_normalized_law_prefix_witness_checks_product_and_stabilization(self):
        solution = rack_solution([0, 1], lambda _left, right: 1 - right)
        braid = pure_braid_generator(1, 2)

        audit = normalized_law_prefix_witness_audit(
            solution,
            (cyclic_group(1),),
            2,
            braid,
            (0, 0),
            extra_strands=2,
            fill_value=0,
        )

        self.assertEqual(audit.group_orders, (1,))
        self.assertTrue(audit.source_product_identity_signature)
        self.assertTrue(audit.target_product_identity_signature)
        self.assertEqual(audit.source_factor_identity_signatures, (True,))
        self.assertEqual(audit.target_factor_identity_signatures, (True,))
        self.assertTrue(audit.right_stabilization.stabilization_valid)
        self.assertEqual(audit.source_image, (1, 1))
        self.assertEqual(audit.stabilized_image, (1, 1, 0, 0))
        self.assertTrue(audit.product_invisibility_survives_stabilization)
        self.assertTrue(audit.movement_survives_stabilization)
        self.assertTrue(audit.proves_one_prefix_normalized_law_witness)

    def test_normalized_law_prefix_witness_rejects_nonmoving_tuple(self):
        solution = identity_solution([0, 1])
        braid = pure_braid_generator(1, 2)

        audit = normalized_law_prefix_witness_audit(
            solution,
            (cyclic_group(1),),
            2,
            braid,
            (0, 1),
            extra_strands=1,
            fill_value=0,
        )

        self.assertTrue(audit.product_invisibility_survives_stabilization)
        self.assertFalse(audit.movement_survives_stabilization)
        self.assertFalse(audit.proves_one_prefix_normalized_law_witness)

    def test_symmetric_normalized_law_prefix_witness_uses_symmetric_tower(self):
        solution = rack_solution([0, 1], lambda _left, right: 1 - right)
        braid = pure_braid_generator(1, 2)

        audit = symmetric_normalized_law_prefix_witness_audit(
            solution,
            1,
            2,
            braid,
            (0, 0),
            extra_strands=1,
            fill_value=0,
        )

        self.assertEqual(audit.group_orders, (1,))
        self.assertEqual(audit.product_group_order, 1)
        self.assertTrue(audit.proves_one_prefix_normalized_law_witness)

    def test_left_regular_representation_embeds_group_in_symmetric_group(self):
        group = cyclic_group(3)
        embedding = left_regular_representation(group, degree=5)

        self.assertEqual(len(embedding.target.identity), 5)
        self.assertEqual(len(set(embedding.mapping.values())), len(group.elements))
        self.assertEqual(embedding.apply(group.identity), embedding.target.identity)

    def test_symmetric_detector_reduction_audit_records_kernel_inclusion(self):
        group = cyclic_group(3)
        trivial = symmetric_detector_reduction_audit(group, 2, (1, -1), degree=3)
        positive = symmetric_detector_reduction_audit(group, 2, (1,), degree=3)

        self.assertTrue(trivial.symmetric_identity_signature)
        self.assertTrue(trivial.source_identity_signature)
        self.assertTrue(trivial.proves_symmetric_detector_reduction)
        self.assertFalse(positive.symmetric_identity_signature)
        self.assertTrue(positive.proves_symmetric_detector_reduction)

    def test_detector_action_readout_is_killed_by_identity_signature(self):
        group = cyclic_group(2)
        detector = artin_detector_rack(group)
        start = ((0, 1, group.identity), (0, 0, group.identity))
        invisible = pure_braid_generator(1, 2) * 2

        def toy_readout(word):
            image = detector.braid_action(word, start)
            return tuple(cell[2] for cell in image)

        self.assertTrue(has_identity_longitude_signature(group, 2, invisible))
        self.assertEqual(toy_readout(invisible), toy_readout(tuple()))

    def test_longitude_blind_mover_finds_none_for_identity_solution(self):
        group = cyclic_group(2)
        solution = identity_solution([0, 1])
        movers = longitude_blind_movers(solution, group, 2, [[1, -1]])
        self.assertEqual(movers, {})


if __name__ == "__main__":
    unittest.main()
