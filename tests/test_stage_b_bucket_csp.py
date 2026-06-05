import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.run_sequential_primitivity_frontier_audit import affine_f2_type_a_solution
from tools.run_stage_b_bucket_csp_audit import build_report
from ybe_domination import identity_solution, rack_solution
from ybe_domination.stage_a_u_arrays import (
    stage_a_bucket_domains,
    stage_b_bucket_csp_profile,
    stage_b_bucket_triple_has_support,
    stage_b_bucket_triple_value_has_support,
    stage_b_bucket_permutation_gac_audit,
    stage_b_bucket_permutation_v_search_audit,
    stage_b_bucket_constraint_hypergraph_audit,
    stage_b_stabilizer_branch_audit,
    stage_b_bucket_column_singularity_possible,
    stage_b_bucket_noninvolutive_possible,
    stage_b_bucket_domain_state_is_canonical,
    stage_b_column_singularity_possible,
    stage_b_gac_dynamic_universe,
    stage_b_gac_propagation_audit,
    stage_b_gac_v_search_audit,
    stage_b_hall_all_different_ok,
    u_array_from_solution,
    u_array_automorphisms,
    uv_arrays_from_solution,
)


class StageBBucketCSPTests(unittest.TestCase):
    def test_identity_bucket_profile_has_three_large_domains(self):
        u_array = u_array_from_solution(identity_solution((0, 1, 2)))
        profile = stage_b_bucket_csp_profile(u_array)

        self.assertEqual(profile.bucket_count, 3)
        self.assertEqual(profile.domain_size_counts, ((3, 9),))
        self.assertEqual(profile.forced_variable_count, 0)
        self.assertTrue(profile.hall_all_different_ok)
        self.assertEqual(profile.unsupported_y2_y3_triple_count, 0)
        self.assertTrue(profile.locally_consistent)

    def test_dihedral_bucket_profile_is_forced(self):
        solution = rack_solution((0, 1, 2), lambda left, right: (2 * left - right) % 3)
        profile = stage_b_bucket_csp_profile(u_array_from_solution(solution))

        self.assertEqual(profile.bucket_count, 9)
        self.assertEqual(profile.domain_size_counts, ((1, 9),))
        self.assertEqual(profile.forced_variable_count, 9)
        self.assertTrue(profile.locally_consistent)

    def test_affine_type_a_bucket_profile_has_two_cell_buckets(self):
        profile = stage_b_bucket_csp_profile(
            u_array_from_solution(affine_f2_type_a_solution())
        )

        self.assertEqual(profile.bucket_count, 8)
        self.assertEqual(profile.domain_size_counts, ((2, 16),))
        self.assertEqual(profile.maximum_domain_size, 2)
        self.assertTrue(profile.hall_all_different_ok)
        self.assertEqual(profile.unsupported_y2_y3_triple_count, 0)

    def test_local_triple_support_and_hall_are_explicit_checks(self):
        u_array = u_array_from_solution(affine_f2_type_a_solution())
        domains = stage_a_bucket_domains(u_array)

        self.assertTrue(stage_b_hall_all_different_ok(u_array, domains))
        self.assertTrue(stage_b_bucket_triple_has_support(u_array, domains, (0, 1, 2)))

    def test_gac_forces_dihedral_rack_v_array(self):
        solution = rack_solution((0, 1, 2), lambda left, right: (2 * left - right) % 3)
        u_array, v_array = uv_arrays_from_solution(solution)
        audit = stage_b_gac_propagation_audit(u_array)

        self.assertTrue(audit.locally_consistent)
        self.assertTrue(audit.all_singleton)
        self.assertEqual(audit.extracted_v, v_array)
        self.assertEqual(audit.singleton_y2_y3_verified, True)

    def test_gac_keeps_known_affine_stage_b_solution_available(self):
        u_array, v_array = uv_arrays_from_solution(affine_f2_type_a_solution())
        audit = stage_b_gac_propagation_audit(u_array)

        self.assertTrue(audit.locally_consistent)
        self.assertFalse(audit.all_singleton)
        self.assertEqual(audit.initial_domain_mass, 32)
        self.assertEqual(audit.final_domain_mass, 32)
        for x, row in enumerate(v_array):
            for y, value in enumerate(row):
                self.assertIn(value, audit.domains[x][y])

    def test_gac_search_recovers_known_affine_noninvolutive_completion(self):
        u_array, v_array = uv_arrays_from_solution(affine_f2_type_a_solution())
        audit = stage_b_gac_v_search_audit(
            u_array,
            require_column_singular=True,
            require_noninvolutive=True,
        )

        self.assertEqual(audit.accepted_count, 1)
        self.assertEqual(audit.examples, (v_array,))
        self.assertFalse(audit.truncated)

    def test_bucket_permutation_gac_forces_identity_completion(self):
        u_array = u_array_from_solution(identity_solution((0, 1, 2)))
        audit = stage_b_bucket_permutation_gac_audit(u_array)

        self.assertTrue(audit.locally_consistent)
        self.assertTrue(audit.all_singleton)
        self.assertEqual(audit.final_domain_product, "1")
        self.assertEqual(audit.singleton_y2_y3_verified, True)
        self.assertEqual(audit.noninvolutive, False)

    def test_u_array_automorphisms_are_computed_exactly_on_regressions(self):
        identity_u = u_array_from_solution(identity_solution((0, 1, 2)))
        affine_u = u_array_from_solution(affine_f2_type_a_solution())

        self.assertEqual(len(u_array_automorphisms(identity_u)), 6)
        self.assertEqual(len(u_array_automorphisms(affine_u)), 2)

    def test_bucket_permutation_search_recovers_affine_completion(self):
        u_array, v_array = uv_arrays_from_solution(affine_f2_type_a_solution())
        audit = stage_b_bucket_permutation_v_search_audit(
            u_array,
            require_column_singular=True,
            require_noninvolutive=True,
        )

        self.assertEqual(audit.node_count, 3)
        self.assertEqual(audit.aut_u_order, 2)
        self.assertEqual(audit.canonical_rejection_count, 0)
        self.assertEqual(audit.accepted_count, 1)
        self.assertEqual(audit.examples, (v_array,))
        self.assertFalse(audit.truncated)

    def test_bucket_column_singularity_feasibility_is_exact_on_regressions(self):
        dihedral = rack_solution((0, 1, 2), lambda left, right: (2 * left - right) % 3)
        dihedral_u = u_array_from_solution(dihedral)
        dihedral_gac = stage_b_bucket_permutation_gac_audit(dihedral_u)
        affine_u = u_array_from_solution(affine_f2_type_a_solution())
        affine_gac = stage_b_bucket_permutation_gac_audit(affine_u)

        self.assertFalse(
            stage_b_bucket_column_singularity_possible(
                dihedral_u,
                dihedral_gac.domains,
            )
        )
        self.assertTrue(
            stage_b_bucket_column_singularity_possible(
                affine_u,
                affine_gac.domains,
            )
        )

    def test_bucket_noninvolutive_feasibility_is_exact_on_regressions(self):
        identity_u = u_array_from_solution(identity_solution((0, 1, 2)))
        identity_gac = stage_b_bucket_permutation_gac_audit(identity_u)
        dihedral = rack_solution((0, 1, 2), lambda left, right: (2 * left - right) % 3)
        dihedral_u = u_array_from_solution(dihedral)
        dihedral_gac = stage_b_bucket_permutation_gac_audit(dihedral_u)
        affine_u = u_array_from_solution(affine_f2_type_a_solution())
        affine_gac = stage_b_bucket_permutation_gac_audit(affine_u)

        self.assertFalse(
            stage_b_bucket_noninvolutive_possible(
                identity_u,
                identity_gac.domains,
            )
        )
        self.assertTrue(
            stage_b_bucket_noninvolutive_possible(
                dihedral_u,
                dihedral_gac.domains,
            )
        )
        self.assertTrue(
            stage_b_bucket_noninvolutive_possible(
                affine_u,
                affine_gac.domains,
            )
        )

    def test_bucket_constraint_hypergraph_components_on_regressions(self):
        identity_u = u_array_from_solution(identity_solution((0, 1, 2)))
        affine_u = u_array_from_solution(affine_f2_type_a_solution())

        identity_audit = stage_b_bucket_constraint_hypergraph_audit(identity_u)
        affine_audit = stage_b_bucket_constraint_hypergraph_audit(affine_u)

        self.assertEqual(identity_audit.unresolved_bucket_count, 0)
        self.assertEqual(identity_audit.component_count, 0)
        self.assertTrue(identity_audit.column_singularity_possible)
        self.assertFalse(identity_audit.noninvolutive_possible)
        self.assertFalse(identity_audit.locally_consistent)
        self.assertEqual(affine_audit.unresolved_bucket_count, 8)
        self.assertEqual(affine_audit.ybe_pattern_count, 156)
        self.assertEqual(affine_audit.column_pattern_count, 16)
        self.assertEqual(affine_audit.noninvolutive_witness_count, 24)
        self.assertEqual(affine_audit.component_count, 1)
        self.assertEqual(affine_audit.largest_component_size, 8)
        self.assertGreaterEqual(affine_audit.ybe_hyperedge_count, 1)
        self.assertTrue(affine_audit.locally_consistent)

    def test_bucket_domain_state_canonical_checker_accepts_root_state(self):
        u_array = u_array_from_solution(affine_f2_type_a_solution())
        gac = stage_b_bucket_permutation_gac_audit(u_array)

        self.assertTrue(stage_b_bucket_domain_state_is_canonical(u_array, gac.domains))

    def test_stabilizer_branch_audit_selects_affine_branch_frontier(self):
        identity_u = u_array_from_solution(identity_solution((0, 1, 2)))
        affine_u = u_array_from_solution(affine_f2_type_a_solution())

        identity_audit = stage_b_stabilizer_branch_audit(identity_u)
        affine_audit = stage_b_stabilizer_branch_audit(affine_u)

        self.assertFalse(identity_audit.locally_consistent)
        self.assertTrue(affine_audit.locally_consistent)
        self.assertEqual(affine_audit.aut_u_order, 2)
        self.assertEqual(affine_audit.stabilizer_order, 2)
        self.assertEqual(affine_audit.component_orbit_count, 1)
        self.assertEqual(affine_audit.selected_component, tuple(range(8)))
        self.assertEqual(affine_audit.selected_bucket, 0)
        self.assertEqual(affine_audit.selected_bucket_orbit_size, 2)
        self.assertEqual(affine_audit.selected_value_representatives, (0, 1))
        self.assertEqual(affine_audit.child_domain_count, 2)

    def test_column_singularity_feasibility_filter_detects_forced_permutation(self):
        self.assertFalse(
            stage_b_column_singularity_possible(
                (
                    ((0,), (0,)),
                    ((1,), (1,)),
                )
            )
        )
        self.assertTrue(
            stage_b_column_singularity_possible(
                (
                    ((0, 1), (0,)),
                    ((1,), (0, 1)),
                )
            )
        )

    def test_dynamic_universe_and_value_support_are_exact_queries(self):
        u_array = u_array_from_solution(affine_f2_type_a_solution())
        domains = stage_a_bucket_domains(u_array)
        universe = stage_b_gac_dynamic_universe(u_array, domains, (0, 1, 2))

        self.assertIn((0, 1), universe)
        self.assertTrue(
            stage_b_bucket_triple_value_has_support(
                u_array,
                domains,
                (0, 1, 2),
                (0, 1),
                domains[0][1][0],
            )
        )

    def test_generated_bucket_csp_audit_records_examples(self):
        report = build_report()
        rows = {row["name"]: row for row in report["rows"]}

        self.assertIn("Hall all-different", " ".join(report["checks"]))
        self.assertTrue(rows["identity_3"]["profile"]["locally_consistent"])
        self.assertEqual(
            rows["dihedral_rack_3"]["profile"]["forced_variable_count"],
            9,
        )
        self.assertEqual(
            rows["size4_affine_type_a"]["profile"]["maximum_domain_size"],
            2,
        )
        self.assertEqual(
            rows["size4_affine_type_a"]["gac_noninvolutive_search"]["accepted_count"],
            1,
        )
        self.assertEqual(
            rows["size4_affine_type_a"]["bucket_permutation_search"]["accepted_count"],
            1,
        )
        self.assertTrue(report["next_prompt"].endswith("_ask_now.md"))


if __name__ == "__main__":
    unittest.main()
