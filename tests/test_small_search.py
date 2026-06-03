import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    affine_cyclic_form,
    all_bijection_solutions,
    branch_tags,
    commutator_law_braid_moves,
    coordinate_dependency_branch_audit,
    dependency_profile,
    derived_rack_operation_table,
    derived_rack_solution,
    direct_symmetric_known_branch_reason,
    is_identity_table,
    is_involutive_solution,
    is_left_nondegenerate,
    is_nondegenerate,
    is_permutation_solution_form,
    is_rack_type,
    is_right_nondegenerate,
    known_branch_full_twist_order_bound_audit,
    known_branch_detector_certificate,
    permutation_order,
    permutation_form_detector_group,
    permutation_solution_crossing_order_formula,
    permutation_solution_pure_longitude_factorization,
    permutation_solution_maps,
    permutation_solution_twist_order,
    rack_solution,
    small_solution_summary,
    two_strand_symmetric_gate_summary,
    two_strand_product_gate_summary,
    two_strand_guitar_conjugacy_holds,
    two_strand_guitar_map,
    two_strand_symmetric_detector_covers_solution,
)
from ybe_domination.residual import action_permutation


class SmallSearchTests(unittest.TestCase):
    def test_rack_type_recognition(self):
        solution = rack_solution([0, 1, 2], lambda a, b: b)
        self.assertTrue(is_rack_type(solution))

    def test_commutator_law_braid_does_not_move_trivial_rack(self):
        solution = rack_solution([0, 1], lambda a, b: b)
        self.assertFalse(commutator_law_braid_moves(solution))

    def test_size_two_summary_runs(self):
        summary = small_solution_summary(2)
        self.assertEqual(summary["checked"], 24)
        self.assertGreaterEqual(summary["ybe_count"], 1)

    def test_affine_cyclic_form_detects_size_three_candidate(self):
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
        solution = FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, values)))
        self.assertEqual(
            affine_cyclic_form(solution),
            {"modulus": 3, "matrix": [[2, 1], [2, 0]], "offset": [0, 0]},
        )
        self.assertFalse(is_involutive_solution(solution))

    def test_involutive_solution_detector(self):
        values = {
            (0, 0): (0, 0),
            (0, 1): (1, 0),
            (1, 0): (0, 1),
            (1, 1): (1, 1),
        }
        solution = FiniteBraidedSet((0, 1), values)
        self.assertTrue(is_involutive_solution(solution))
        self.assertTrue(is_permutation_solution_form(solution))
        self.assertFalse(is_identity_table(solution))
        self.assertIn("permutation_form", branch_tags(solution))

    def test_permutation_solution_maps_and_twist_order(self):
        elements = (0, 1, 2)
        solution = FiniteBraidedSet(
            elements,
            {
                (x, y): ((y + 1) % 3, x)
                for x in elements
                for y in elements
            },
        )

        self.assertTrue(solution.is_ybe())
        self.assertTrue(is_permutation_solution_form(solution))
        sigma, tau = permutation_solution_maps(solution)
        self.assertEqual(sigma, {0: 1, 1: 2, 2: 0})
        self.assertEqual(tau, {0: 0, 1: 1, 2: 2})
        self.assertEqual(permutation_solution_twist_order(solution), 3)
        self.assertEqual(permutation_solution_crossing_order_formula(solution), 6)
        self.assertEqual(
            permutation_order(action_permutation(solution, 2, (1,))),
            permutation_solution_crossing_order_formula(solution),
        )
        self.assertTrue(two_strand_symmetric_detector_covers_solution(solution))

    def test_permutation_form_detector_certificate_uses_fixed_cyclic_group(self):
        elements = (0, 1, 2)
        solution = FiniteBraidedSet(
            elements,
            {
                (x, y): ((y + 1) % 3, x)
                for x in elements
                for y in elements
            },
        )

        group = permutation_form_detector_group(solution)
        certificate = known_branch_detector_certificate(solution)

        self.assertEqual(len(group.elements), 3)
        self.assertIsNotNone(certificate)
        self.assertEqual(certificate.reason, "permutation_twist_subgroup")
        self.assertEqual(certificate.detector_kind, "cyclic_twist_group")
        self.assertEqual(certificate.detector_group_order, 3)
        self.assertEqual(certificate.sharp_rack_factor_size, 18)
        self.assertEqual(certificate.twist_order, 3)
        self.assertTrue(certificate.braid_index_independent)

    def test_involutive_detector_certificate_uses_trivial_group(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (1, 0),
                (1, 0): (0, 1),
                (1, 1): (1, 1),
            },
        )

        certificate = known_branch_detector_certificate(solution)

        self.assertIsNotNone(certificate)
        self.assertEqual(certificate.reason, "involutive_artin_permutation")
        self.assertEqual(certificate.detector_kind, "trivial_group")
        self.assertEqual(certificate.detector_group_order, 1)
        self.assertEqual(certificate.sharp_rack_factor_size, 2)
        self.assertIsNone(certificate.twist_order)

    def test_rack_known_branch_certificate_uses_direct_symmetric_group(self):
        solution = rack_solution(
            [0, 1, 2],
            lambda left, right: (2 * left - right) % 3,
        )

        certificate = known_branch_detector_certificate(solution)

        self.assertIsNotNone(certificate)
        self.assertEqual(certificate.reason, "rack_inner_group_subgroup")
        self.assertEqual(certificate.detector_kind, "direct_symmetric_group")
        self.assertEqual(certificate.detector_group_order, 6)
        self.assertEqual(certificate.sharp_rack_factor_size, 72)

    def test_permutation_solution_crossing_order_formula_for_one_point(self):
        solution = FiniteBraidedSet((0,), {(0, 0): (0, 0)})

        self.assertTrue(is_permutation_solution_form(solution))
        self.assertEqual(permutation_solution_twist_order(solution), 1)
        self.assertEqual(permutation_solution_crossing_order_formula(solution), 1)

    def test_two_strand_symmetric_gate_summary_classifies_known_branches(self):
        involutive = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (1, 0),
                (1, 0): (0, 1),
                (1, 1): (1, 1),
            },
        )
        rack = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        permutation = FiniteBraidedSet(
            (0, 1, 2),
            {
                (x, y): ((y + 1) % 3, (x + 1) % 3)
                for x in (0, 1, 2)
                for y in (0, 1, 2)
            },
        )

        self.assertEqual(
            two_strand_symmetric_gate_summary(involutive).explanation,
            "involutive_order_two",
        )
        self.assertEqual(
            two_strand_symmetric_gate_summary(rack).explanation,
            "rack_inner_group_branch",
        )
        self.assertEqual(
            two_strand_symmetric_gate_summary(permutation).explanation,
            "permutation_form_twist_order_3",
        )

    def test_two_strand_guitar_conjugacy_for_nondegenerate_row(self):
        pairs = [(x, y) for x in range(3) for y in range(3)]
        values = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (1, 2),
            (2, 2),
            (0, 2),
            (1, 1),
            (2, 1),
        ]
        solution = FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, values)))

        self.assertTrue(solution.is_ybe())
        self.assertTrue(is_nondegenerate(solution))
        self.assertEqual(
            two_strand_symmetric_gate_summary(solution).explanation,
            "left_nondegenerate_derived_rack_branch",
        )

        operation = derived_rack_operation_table(solution)
        self.assertIsNotNone(operation)
        derived = derived_rack_solution(solution)
        self.assertIsNotNone(derived)
        self.assertTrue(is_rack_type(derived))
        self.assertTrue(two_strand_guitar_conjugacy_holds(solution))

        guitar = two_strand_guitar_map(solution)
        self.assertEqual(len(guitar), 9)
        for pair in pairs:
            self.assertEqual(
                guitar[solution.R[pair]],
                derived.R[guitar[pair]],
            )
        self.assertEqual(
            permutation_order(action_permutation(solution, 2, (1,))),
            permutation_order(action_permutation(derived, 2, (1,))),
        )

    def test_size_three_two_strand_gate_has_no_unclassified_rows(self):
        counts = {}
        for solution in all_bijection_solutions(3):
            explanation = two_strand_symmetric_gate_summary(solution).explanation
            counts[explanation] = counts.get(explanation, 0) + 1

        self.assertNotIn("passes_unclassified", counts)
        self.assertEqual(counts["left_nondegenerate_derived_rack_branch"], 35)

    def test_direct_symmetric_known_branch_filter_covers_size_three_corpus(self):
        counts = {}
        for solution in all_bijection_solutions(3):
            reason = direct_symmetric_known_branch_reason(solution)
            counts[reason] = counts.get(reason, 0) + 1

        self.assertNotIn(None, counts)
        self.assertEqual(
            counts,
            {
                "involutive_artin_permutation": 18,
                "rack_inner_group_subgroup": 13,
                "left_nondegenerate_guitar_derived_rack": 35,
                "permutation_twist_subgroup": 7,
            },
        )

    def test_two_strand_symmetric_gate_is_product_closed(self):
        rack = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        permutation = FiniteBraidedSet(
            (0, 1),
            {
                (x, y): (1 - y, x)
                for x in (0, 1)
                for y in (0, 1)
            },
        )

        self.assertTrue(two_strand_symmetric_detector_covers_solution(rack))
        self.assertTrue(two_strand_symmetric_detector_covers_solution(permutation))
        summary = two_strand_product_gate_summary(rack, permutation)

        self.assertEqual(summary.left_size, 3)
        self.assertEqual(summary.right_size, 2)
        self.assertEqual(summary.product_size, 6)
        self.assertTrue(summary.passes)
        self.assertEqual(
            summary.product_symmetric_longitude_period % summary.product_crossing_order,
            0,
        )

    def test_permutation_solution_pure_longitude_factorization(self):
        elements = (0, 1, 2)
        solution = FiniteBraidedSet(
            elements,
            {
                (x, y): ((y + 1) % 3, x)
                for x in elements
                for y in elements
            },
        )

        for braid in ((1, 1), (-1, -1), (1, 2, 2, 1)):
            tup = (0, 1, 2)[: max(abs(i) for i in braid) + 1]
            factorization = permutation_solution_pure_longitude_factorization(
                solution,
                braid,
                tup,
            )
            self.assertEqual(
                factorization.output,
                solution.braid_action(braid, tup),
            )

        with self.assertRaises(ValueError):
            permutation_solution_pure_longitude_factorization(
                solution,
                (1,),
                (0, 1),
            )

    def test_permutation_solution_full_twist_orders_divide_twist_order(self):
        elements = (0, 1, 2, 3)
        solution = FiniteBraidedSet(
            elements,
            {
                (x, y): ((y + 1) % 4, x)
                for x in elements
                for y in elements
            },
        )

        audit = known_branch_full_twist_order_bound_audit(solution, max_n=6)

        self.assertEqual(audit.reason, "permutation_form_twist_order")
        self.assertEqual(audit.uniform_bound, 4)
        self.assertEqual(audit.action_orders, (1, 4, 2, 4, 1, 4))
        self.assertTrue(audit.checked_orders_divide_bound)
        self.assertTrue(audit.proves_checked_known_branch_full_twist_bound)

    def test_left_nondegenerate_full_twist_bound_routes_to_derived_rack(self):
        pairs = [(x, y) for x in range(3) for y in range(3)]
        values = [
            (0, 0),
            (1, 0),
            (2, 0),
            (0, 1),
            (1, 2),
            (2, 2),
            (0, 2),
            (1, 1),
            (2, 1),
        ]
        solution = FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, values)))

        audit = known_branch_full_twist_order_bound_audit(solution, max_n=5)

        self.assertEqual(audit.reason, "left_nondegenerate_derived_rack_exponent")
        self.assertIsNotNone(audit.uniform_bound)
        self.assertTrue(audit.checked_orders_divide_bound)
        self.assertTrue(audit.proves_checked_known_branch_full_twist_bound)

    def test_size_three_known_branches_have_checked_full_twist_bounds(self):
        counts = {}
        for solution in all_bijection_solutions(3):
            audit = known_branch_full_twist_order_bound_audit(solution, max_n=5)
            counts[audit.reason] = counts.get(audit.reason, 0) + 1
            self.assertTrue(audit.proves_checked_known_branch_full_twist_bound)

        self.assertNotIn(None, counts)
        self.assertEqual(
            counts,
            {
                "involutive_artin_permutation": 19,
                "rack_inner_group_exponent": 7,
                "left_nondegenerate_derived_rack_exponent": 35,
                "permutation_form_twist_order": 12,
            },
        )

    def test_same_side_coordinate_dependency_collapses_in_tiny_corpus(self):
        for size in (2, 3):
            for solution in all_bijection_solutions(size):
                profile = dependency_profile(solution)
                if not (
                    profile["first_depends_only_on_x"]
                    or profile["second_depends_only_on_y"]
                ):
                    continue
                audit = coordinate_dependency_branch_audit(solution, max_n=5)

                self.assertEqual(
                    audit.reason,
                    "same_side_dependency_identity_collapse",
                )
                self.assertTrue(audit.identity_table)
                self.assertTrue(audit.proves_coordinate_dependency_closed_branch)

    def test_opposite_side_coordinate_dependency_routes_to_nondegenerate_branch(self):
        counts = {}
        for solution in all_bijection_solutions(3):
            profile = dependency_profile(solution)
            has_opposite_side_dependency = (
                profile["first_depends_only_on_y"]
                or profile["second_depends_only_on_x"]
            )
            has_same_side_dependency = (
                profile["first_depends_only_on_x"]
                or profile["second_depends_only_on_y"]
            )
            if not has_opposite_side_dependency or has_same_side_dependency:
                continue
            audit = coordinate_dependency_branch_audit(solution, max_n=5)
            counts[audit.known_full_twist_reason] = (
                counts.get(audit.known_full_twist_reason, 0) + 1
            )

            self.assertEqual(
                audit.reason,
                "opposite_side_dependency_nondegenerate_branch",
            )
            self.assertTrue(audit.nondegenerate)
            self.assertTrue(audit.proves_coordinate_dependency_closed_branch)

        self.assertEqual(
            counts,
            {
                "involutive_artin_permutation": 6,
                "rack_inner_group_exponent": 7,
                "left_nondegenerate_derived_rack_exponent": 29,
                "permutation_form_twist_order": 12,
            },
        )

    def test_nondegeneracy_detectors(self):
        values = {
            (0, 0): (0, 0),
            (0, 1): (1, 0),
            (1, 0): (0, 1),
            (1, 1): (1, 1),
        }
        solution = FiniteBraidedSet((0, 1), values)
        self.assertTrue(is_left_nondegenerate(solution))
        self.assertTrue(is_right_nondegenerate(solution))
        self.assertTrue(is_nondegenerate(solution))

        degenerate = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (1, 1),
                (1, 0): (1, 0),
                (1, 1): (0, 1),
            },
        )
        self.assertTrue(is_left_nondegenerate(degenerate))
        self.assertFalse(is_right_nondegenerate(degenerate))
        self.assertFalse(is_nondegenerate(degenerate))

    def test_dependency_profile_identity_table(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {
                (0, 0): (0, 0),
                (0, 1): (0, 1),
                (1, 0): (1, 0),
                (1, 1): (1, 1),
            },
        )
        self.assertEqual(
            dependency_profile(solution),
            {
                "first_depends_only_on_x": True,
                "first_depends_only_on_y": False,
                "second_depends_only_on_x": False,
                "second_depends_only_on_y": True,
            },
        )
        self.assertTrue(is_identity_table(solution))
        self.assertEqual(
            branch_tags(solution),
            ("involutive", "identity_table", "affine_cyclic"),
        )


if __name__ == "__main__":
    unittest.main()
