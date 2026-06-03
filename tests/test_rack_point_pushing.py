import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteAugmentedArtinEnvelopePressureAudit,
    FiniteAugmentedArtinEnvelopePressureCase,
    FiniteAugmentedArtinEnvelopeRouteAudit,
    PointPushingGeneratorRow,
    finite_augmented_artin_envelope_pressure_audit,
    finite_augmented_artin_envelope_route_audit,
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


if __name__ == "__main__":
    unittest.main()
