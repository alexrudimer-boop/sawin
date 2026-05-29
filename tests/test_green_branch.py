import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    BranchRow,
    GreenBranchAudit,
    all_bijection_solutions,
    atom_action_summary,
    atom_descent_closure_summary,
    atom_descent_quotient_inner_detector_lift_audit,
    atom_descent_quotient_rack_audit,
    atom_descent_quotient_solution,
    atom_quotient_inner_detector_lift_audit,
    atom_quotient_inner_group,
    atom_quotient_inner_groups,
    atom_quotient_rack_audit,
    atom_quotient_solution,
    atom_projection_summary,
    bounded_atom_trivial_loop_group_summaries,
    bounded_category_summary,
    coordinate_action_maps,
    coordinate_action_relation_failures,
    context_words_by_target,
    depth_observer_summary,
    green_branch_audits,
    kernel_block_first_output_defect_audits,
    induced_kernel_permutation,
    kernel_action_summary,
    opposite_green_branch_audits,
    rack_solution,
    right_coordinate_action_maps,
    right_coordinate_action_relation_failures,
    schutzenberger_action_groups,
    schutzenberger_first_output_defect_audits,
    schutzenberger_groups,
    schutzenberger_kernel_block_homomorphism,
    schutzenberger_kernel_defect_pushforward_audits,
    schutzenberger_summaries,
    two_sided_atom_quotient_inner_groups,
    two_sided_green_detector_groups,
    two_sided_green_detector_product,
    two_sided_schutzenberger_groups,
    transformation_kernel,
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


class GreenBranchTests(unittest.TestCase):
    def test_coordinate_action_relation_for_rack(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        self.assertEqual(coordinate_action_relation_failures(solution), [])

    def test_coordinate_action_relation_for_affine_candidate(self):
        solution = size_three_affine_candidate()
        tau = coordinate_action_maps(solution)
        self.assertEqual(tau[1], (2, 0, 1))
        self.assertEqual(coordinate_action_relation_failures(solution), [])

    def test_right_coordinate_action_relation_for_affine_candidate(self):
        solution = size_three_affine_candidate()
        rho = right_coordinate_action_maps(solution)
        self.assertEqual(rho[1], (0, 2, 1))
        self.assertEqual(right_coordinate_action_relation_failures(solution), [])
        self.assertEqual(
            len(opposite_green_branch_audits(solution)),
            len(green_branch_audits(solution)),
        )

    def test_green_branch_audit_has_no_direct_failure_for_affine_candidate(self):
        audits = green_branch_audits(size_three_affine_candidate())
        self.assertEqual(len(audits), 1)
        audit = audits[0]
        self.assertEqual(len(audit.edge_germs), 9)
        self.assertEqual(len(audit.rows), 27)
        self.assertEqual(len(audit.atom_partition), 3)
        self.assertEqual(audit.branch_choice_failures, ())

    def test_context_observer_for_affine_candidate_has_no_hidden_split(self):
        audit = green_branch_audits(size_three_affine_candidate())[0]
        words = context_words_by_target(audit, 2)
        self.assertEqual(sorted(len(value) for value in words.values()), [13, 13, 13])
        summary = depth_observer_summary(audit, 2)
        self.assertEqual(summary.undefined_profile_count, 0)
        self.assertEqual(summary.atom_profile_conflict_count, 0)
        self.assertEqual(summary.hidden_profile_split_count, 0)

    def test_context_observer_for_trivial_rack(self):
        audit = green_branch_audits(rack_solution([0, 1], lambda a, b: b))[0]
        self.assertEqual(depth_observer_summary(audit, 2).context_word_counts, (("(0, 1)", 7),))

    def test_bounded_completed_category_for_affine_candidate(self):
        audit = green_branch_audits(size_three_affine_candidate())[0]
        summary = bounded_category_summary(audit, 2)
        self.assertFalse(summary.truncated)
        self.assertEqual(summary.morphism_count, 18)
        self.assertEqual(summary.hidden_atom_trivial_loop_count, 0)
        self.assertEqual(summary.hidden_bijective_loop_count, 0)

    def test_bounded_atom_trivial_loop_group_is_trivial_for_affine_candidate(self):
        audit = green_branch_audits(size_three_affine_candidate())[0]
        summaries = bounded_atom_trivial_loop_group_summaries(audit, 2)

        self.assertEqual(len(summaries), 3)
        self.assertTrue(all(not summary.truncated for summary in summaries))
        self.assertEqual({summary.group_order for summary in summaries}, {1})
        self.assertEqual({summary.nonidentity_loop_count for summary in summaries}, {0})

    def test_reset_like_atom_trivial_context_loops_do_not_create_group_holonomy(self):
        identity = FiniteBraidedSet(
            (0, 1), {(x, y): (x, y) for x in (0, 1) for y in (0, 1)}
        )
        reset_audits = [
            audit for audit in green_branch_audits(identity) if audit.edge_germs
        ]

        self.assertTrue(
            any(
                bounded_category_summary(audit, 2).hidden_atom_trivial_loop_count
                for audit in reset_audits
            )
        )
        summaries = [
            summary
            for audit in reset_audits
            for summary in bounded_atom_trivial_loop_group_summaries(audit, 2)
        ]
        self.assertEqual({summary.group_order for summary in summaries}, {1})
        self.assertEqual({summary.nonidentity_loop_count for summary in summaries}, {0})

    def test_schutzenberger_summary_for_affine_candidate_is_global_group(self):
        summary = schutzenberger_summaries(size_three_affine_candidate())[0]
        self.assertEqual(summary.right_stabilizer_size, 3)
        self.assertEqual(summary.permutation_count, 3)
        self.assertEqual(summary.nonpermutation_stabilizer_count, 0)
        self.assertTrue(summary.permutation_group_closed)
        self.assertEqual(summary.globally_stabilizing_labels, (0, 1, 2))
        self.assertEqual(summary.local_only_edge_germ_count, 0)

    def test_schutzenberger_action_groups_are_exposed_as_finite_groups(self):
        solution = size_three_affine_candidate()
        action_group = schutzenberger_action_groups(solution)[0]
        self.assertEqual(len(action_group.r_class), 3)
        self.assertEqual(len(action_group.actions), 3)
        self.assertEqual(len(action_group.group.elements), 3)

        self.assertEqual(len(schutzenberger_groups(solution)), 1)
        self.assertEqual(
            sorted(len(group.elements) for group in two_sided_schutzenberger_groups(solution)),
            [2, 3],
        )
        self.assertEqual(
            sorted(len(group.elements) for group in atom_quotient_inner_groups(solution)),
            [6],
        )
        self.assertEqual(
            sorted(len(group.elements) for group in two_sided_atom_quotient_inner_groups(solution)),
            [6],
        )
        green_factors = two_sided_green_detector_groups(solution)
        self.assertEqual(sorted(len(group.elements) for group in green_factors), [2, 3, 6])
        self.assertEqual(len(two_sided_green_detector_product(solution).elements), 36)

    def test_kernel_action_for_affine_candidate(self):
        summary = kernel_action_summary(size_three_affine_candidate())[0]
        self.assertEqual(len(summary.kernel_partition), 3)
        self.assertEqual(summary.retained_labels, (0, 1, 2))
        self.assertEqual(summary.induced_group_size, 3)
        self.assertEqual(summary.nonpermutation_label_count, 0)

    def test_green_first_output_defect_normal_form_for_affine_candidate(self):
        solution = size_three_affine_candidate()
        sch_audit = schutzenberger_first_output_defect_audits(solution)[0]
        kernel_audit = kernel_block_first_output_defect_audits(solution)[0]

        self.assertEqual(sch_audit.row_count, 27)
        self.assertEqual(sch_audit.missing_row_count, 0)
        self.assertEqual(sch_audit.local_only_edge_germ_count, 0)
        self.assertEqual(sch_audit.nonidentity_defect_count, 18)
        self.assertTrue(sch_audit.all_rows_have_defect_normal_form)
        self.assertTrue(
            sch_audit.all_observed_rows_are_right_rack_when_defects_identity
        )
        self.assertTrue(sch_audit.proves_first_output_defect_reduction)

        self.assertEqual(kernel_audit.row_count, 27)
        self.assertEqual(kernel_audit.missing_row_count, 0)
        self.assertEqual(kernel_audit.nonidentity_defect_count, 18)
        self.assertTrue(kernel_audit.proves_first_output_defect_reduction)

    def test_kernel_defects_push_forward_from_schutzenberger_defects(self):
        solution = size_three_affine_candidate()
        r_class = green_branch_audits(solution)[0].r_class
        homomorphism = schutzenberger_kernel_block_homomorphism(solution, r_class)
        audits = schutzenberger_kernel_defect_pushforward_audits(solution)

        self.assertIsNotNone(homomorphism)
        self.assertEqual(len(audits), 1)
        audit = audits[0]
        self.assertEqual(audit.source_order, 3)
        self.assertEqual(audit.target_order, 3)
        self.assertEqual(audit.local_only_edge_germ_count, 0)
        self.assertTrue(audit.homomorphism_exists)
        self.assertEqual(audit.compared_row_count, 27)
        self.assertEqual(audit.defect_pushforward_failure_count, 0)
        self.assertTrue(
            audit.proves_kernel_defects_are_schutzenberger_pushforwards
        )

    def test_induced_kernel_permutation_detects_block_action(self):
        kernel = transformation_kernel((0, 0, 1, 1))
        self.assertEqual(kernel, (frozenset({0, 1}), frozenset({2, 3})))
        self.assertEqual(induced_kernel_permutation(kernel, (2, 3, 0, 1)), (1, 0))
        self.assertIsNone(induced_kernel_permutation(kernel, (0, 2, 1, 3)))

    def test_atom_projection_distinguishes_affine_from_identity_branch(self):
        affine_audit = green_branch_audits(size_three_affine_candidate())[0]
        affine_projection = atom_projection_summary(affine_audit)
        self.assertEqual(affine_projection.equality_source_count, 3)
        self.assertEqual(affine_projection.universal_source_count, 0)
        self.assertEqual(affine_projection.mixed_source_count, 0)

        identity = FiniteBraidedSet(
            (0, 1), {(x, y): (x, y) for x in (0, 1) for y in (0, 1)}
        )
        identity_projections = [
            atom_projection_summary(audit) for audit in green_branch_audits(identity)
        ]
        self.assertTrue(
            any(summary.universal_source_count for summary in identity_projections)
        )

    def test_atom_action_summary_descends_for_affine_candidate(self):
        audit = green_branch_audits(size_three_affine_candidate())[0]
        summary = atom_action_summary(audit)
        closure = atom_descent_closure_summary(audit)

        self.assertTrue(summary.well_defined)
        self.assertEqual(summary.atom_count, 3)
        self.assertEqual(summary.row_count, 27)
        self.assertEqual(summary.supported_pair_count, 9)
        self.assertEqual(summary.undefined_pair_count, 0)
        self.assertEqual(summary.triangleright_failures, ())
        self.assertEqual(summary.triangleleft_failures, ())
        self.assertTrue(closure.closes_without_coarsening)
        self.assertTrue(closure.proves_stable_atom_action)
        self.assertEqual(closure.added_related_pair_count, 0)

    def test_atom_quotient_solution_is_right_rack_like_for_affine_candidate(self):
        audit = green_branch_audits(size_three_affine_candidate())[0]
        quotient = atom_quotient_solution(audit)
        descent_quotient = atom_descent_quotient_solution(audit)
        rack_audit = atom_quotient_rack_audit(audit)
        descent_rack_audit = atom_descent_quotient_rack_audit(audit)

        self.assertEqual(quotient.elements, (0, 1, 2))
        self.assertEqual(descent_quotient.elements, quotient.elements)
        self.assertEqual(descent_quotient.R, quotient.R)
        self.assertTrue(quotient.is_ybe())
        self.assertTrue(
            all(
                quotient.R[(left, right)][0] == right
                for left in quotient.elements
                for right in quotient.elements
            )
        )
        self.assertTrue(rack_audit.constructed)
        self.assertIsNone(rack_audit.construction_error)
        self.assertTrue(rack_audit.right_rack_like)
        self.assertTrue(rack_audit.right_translations_bijective)
        self.assertTrue(rack_audit.right_self_distributive)
        self.assertTrue(rack_audit.is_ybe)
        self.assertTrue(rack_audit.proves_right_rack_ybe_layer)
        self.assertTrue(descent_rack_audit.proves_right_rack_ybe_layer)
        self.assertEqual(len(atom_quotient_inner_group(audit).elements), 6)
        row_audit = atom_quotient_inner_detector_lift_audit(audit)
        descent_row_audit = atom_descent_quotient_inner_detector_lift_audit(audit)
        self.assertEqual(row_audit.rack_size, 3)
        self.assertEqual(row_audit.inner_group_order, 6)
        self.assertTrue(row_audit.proves_rack_inner_detector_lift_rows)
        self.assertTrue(descent_row_audit.proves_rack_inner_detector_lift_rows)

    def test_atom_action_summary_has_no_size_two_conflicts(self):
        for solution in all_bijection_solutions(2):
            for audit in green_branch_audits(solution):
                summary = atom_action_summary(audit)
                self.assertTrue(summary.well_defined)
                self.assertEqual(summary.undefined_pair_count, 0)
                quotient = atom_quotient_solution(audit)
                self.assertTrue(quotient.is_ybe())
                self.assertTrue(
                    all(
                        quotient.R[(left, right)][0] == right
                        for left in quotient.elements
                        for right in quotient.elements
                    )
                )
                self.assertTrue(
                    atom_quotient_rack_audit(audit).proves_right_rack_ybe_layer
                )
                self.assertTrue(
                    atom_descent_closure_summary(audit).proves_stable_atom_action
                )
                self.assertGreaterEqual(
                    len(atom_quotient_inner_group(audit).elements),
                    1,
                )

    def test_atom_descent_closure_records_forced_coarsening(self):
        source = (0,)
        a1 = (source, "a1")
        a2 = (source, "a2")
        q1 = (source, "q1")
        q2 = (source, "q2")
        out1 = (source, "out1")
        out2 = (source, "out2")
        audit = GreenBranchAudit(
            r_class=(source,),
            edge_germs=(a1, a2, q1, q2, out1, out2),
            edge_targets=tuple(
                (edge, source) for edge in (a1, a2, q1, q2, out1, out2)
            ),
            rows=(
                BranchRow(a=a1, q=q1, q_under_a=q1, a_under_q=out1),
                BranchRow(a=a2, q=q2, q_under_a=q2, a_under_q=out2),
            ),
            atom_partition=(
                frozenset((a1, a2)),
                frozenset((q1, q2)),
                frozenset((out1,)),
                frozenset((out2,)),
            ),
            branch_choice_failures=(),
        )

        action = atom_action_summary(audit)
        closure = atom_descent_closure_summary(audit)

        self.assertFalse(action.well_defined)
        self.assertEqual(action.triangleright_failure_count, 1)
        self.assertEqual(closure.initial_atom_count, 4)
        self.assertEqual(closure.closed_atom_count, 3)
        self.assertGreater(closure.added_related_pair_count, 0)
        self.assertTrue(closure.well_defined_after_closure)
        self.assertFalse(closure.closes_without_coarsening)
        descent_rack_audit = atom_descent_quotient_rack_audit(audit)
        self.assertFalse(descent_rack_audit.constructed)
        self.assertIn("not defined", descent_rack_audit.construction_error)

    def test_descent_closed_atom_quotient_can_absorb_coarsening(self):
        source = (0,)
        a1 = (source, "a1")
        a2 = (source, "a2")
        q = (source, "q")
        out1 = (source, "out1")
        out2 = (source, "out2")
        audit = GreenBranchAudit(
            r_class=(source,),
            edge_germs=(a1, a2, q, out1, out2),
            edge_targets=tuple((edge, source) for edge in (a1, a2, q, out1, out2)),
            rows=(
                BranchRow(a=a1, q=q, q_under_a=q, a_under_q=out1),
                BranchRow(a=a2, q=q, q_under_a=q, a_under_q=out2),
                BranchRow(a=a1, q=q, q_under_a=q, a_under_q=q),
                BranchRow(a=q, q=q, q_under_a=q, a_under_q=q),
                BranchRow(a=out1, q=q, q_under_a=q, a_under_q=q),
                BranchRow(a=q, q=q, q_under_a=q, a_under_q=q),
            ),
            atom_partition=(
                frozenset((a1, a2)),
                frozenset((q,)),
                frozenset((out1,)),
                frozenset((out2,)),
            ),
            branch_choice_failures=(),
        )

        action = atom_action_summary(audit)
        closure = atom_descent_closure_summary(audit)
        descent = atom_descent_quotient_solution(audit)
        rack_audit = atom_descent_quotient_rack_audit(audit)

        self.assertFalse(action.well_defined)
        self.assertEqual(closure.closed_atom_count, 1)
        self.assertTrue(closure.well_defined_after_closure)
        self.assertEqual(closure.undefined_pair_count_after_closure, 0)
        self.assertEqual(descent.elements, (0,))
        self.assertTrue(rack_audit.proves_right_rack_ybe_layer)


if __name__ == "__main__":
    unittest.main()
