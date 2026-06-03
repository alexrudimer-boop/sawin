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
    degenerate_preimage_memory_audit,
    derived_hurwitz_envelope_audit,
    edge_memory_tower_audit,
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


if __name__ == "__main__":
    unittest.main()
