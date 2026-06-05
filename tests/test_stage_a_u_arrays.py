import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tools.run_sequential_primitivity_frontier_audit import affine_f2_type_a_solution
from tools.run_stage_a_u_array_audit import build_report
from ybe_domination import identity_solution, rack_solution
from ybe_domination.stage_a_u_arrays import (
    balanced_symbol_counts,
    canonical_u_array,
    compose_maps,
    relabel_u_array,
    rows_singular,
    stage_a_bucket_domains,
    stage_a_factorization_buckets,
    stage_a_feasibility_sets,
    stage_a_enumeration_audit,
    stage_a_multiset_factorization_holds,
    stage_a_profile_from_solution,
    u_array_from_solution,
)


class StageAUArrayTests(unittest.TestCase):
    def test_identity_solution_passes_stage_a_with_all_candidates(self):
        solution = identity_solution((0, 1, 2))
        profile = stage_a_profile_from_solution(solution)

        self.assertTrue(profile.balanced_symbol_counts)
        self.assertTrue(profile.rows_singular)
        self.assertTrue(profile.feasibility_nonempty)
        self.assertTrue(profile.multiset_factorization)
        self.assertTrue(profile.stage_a_candidate)
        self.assertEqual(profile.minimum_feasibility_size, 3)
        self.assertEqual(profile.maximum_feasibility_size, 3)
        self.assertEqual(profile.bucket_count, 3)
        self.assertEqual(profile.maximum_bucket_size, 3)

    def test_nondegenerate_rack_fails_row_singularity(self):
        solution = rack_solution((0, 1, 2), lambda left, right: (2 * left - right) % 3)
        profile = stage_a_profile_from_solution(solution)

        self.assertTrue(profile.balanced_symbol_counts)
        self.assertFalse(profile.rows_singular)
        self.assertFalse(profile.stage_a_candidate)

    def test_affine_type_a_is_nontrivial_stage_a_candidate(self):
        solution = affine_f2_type_a_solution()
        profile = stage_a_profile_from_solution(solution)

        self.assertTrue(solution.is_ybe())
        self.assertTrue(profile.balanced_symbol_counts)
        self.assertTrue(profile.rows_singular)
        self.assertTrue(profile.feasibility_nonempty)
        self.assertTrue(profile.multiset_factorization)
        self.assertTrue(profile.stage_a_candidate)
        self.assertEqual(profile.minimum_feasibility_size, 2)
        self.assertEqual(profile.maximum_feasibility_size, 2)
        self.assertEqual(profile.bucket_count, 8)
        self.assertEqual(profile.maximum_bucket_size, 2)

    def test_feasibility_sets_are_exact_y1_candidates(self):
        solution = affine_f2_type_a_solution()
        u_array = u_array_from_solution(solution)
        feasibility = stage_a_feasibility_sets(u_array)

        for x, row in enumerate(u_array):
            for y, left_output in enumerate(row):
                target = compose_maps(u_array[x], u_array[y])
                candidates = {
                    v
                    for v in range(len(u_array))
                    if compose_maps(u_array[left_output], u_array[v]) == target
                }
                self.assertEqual(set(feasibility[x][y]), candidates)
                self.assertTrue(candidates)

    def test_canonicalization_is_invariant_under_simultaneous_relabeling(self):
        solution = affine_f2_type_a_solution()
        u_array = u_array_from_solution(solution)
        relabeled = relabel_u_array(u_array, (2, 0, 3, 1))

        self.assertNotEqual(u_array, relabeled)
        self.assertEqual(canonical_u_array(u_array), canonical_u_array(relabeled))
        self.assertEqual(
            balanced_symbol_counts(u_array),
            balanced_symbol_counts(relabeled),
        )
        self.assertEqual(rows_singular(u_array), rows_singular(relabeled))

    def test_generated_audit_records_stage_a_frontier(self):
        report = build_report()
        rows = {row["name"]: row for row in report["rows"]}
        enumeration = report["enumeration"]

        self.assertIn("A_xy={v", " ".join(report["stage_a_constraints"]))
        self.assertTrue(rows["identity_3"]["profile"]["stage_a_candidate"])
        self.assertFalse(rows["dihedral_rack_3"]["profile"]["rows_singular"])
        self.assertTrue(rows["size4_affine_type_a"]["profile"]["stage_a_candidate"])
        self.assertTrue(report["canonicalization"]["canonical_equal"])
        self.assertEqual(enumeration["exact_size_2"]["canonical_count"], 1)
        self.assertEqual(enumeration["exact_size_3"]["feasibility_nonempty_count"], 19)
        self.assertEqual(enumeration["exact_size_3"]["multiset_factorization_count"], 1)
        self.assertEqual(enumeration["exact_size_3"]["canonical_count"], 1)
        self.assertTrue(enumeration["budgeted_size_4"]["truncated"])
        self.assertTrue(report["next_prompt"].endswith("_ask_now.md"))

    def test_exact_tiny_stage_a_enumeration_counts(self):
        size_2 = stage_a_enumeration_audit(2, max_examples=None)
        size_3 = stage_a_enumeration_audit(3, max_examples=None)

        self.assertFalse(size_2.truncated)
        self.assertEqual(size_2.feasibility_nonempty_count, 1)
        self.assertEqual(size_2.multiset_factorization_count, 1)
        self.assertEqual(size_2.canonical_count, 1)
        self.assertEqual(size_2.emitted_count, 1)
        self.assertFalse(size_3.truncated)
        self.assertEqual(size_3.feasibility_nonempty_count, 19)
        self.assertEqual(size_3.multiset_factorization_count, 1)
        self.assertEqual(size_3.canonical_count, 1)
        self.assertEqual(size_3.emitted_count, 1)

    def test_budgeted_enumeration_reports_truncation(self):
        audit = stage_a_enumeration_audit(4, max_nodes=1000, max_examples=2)

        self.assertTrue(audit.truncated)
        self.assertEqual(audit.node_count, 1000)
        self.assertLessEqual(audit.emitted_count, 2)

    def test_multiset_factorization_and_buckets_refine_a_xy(self):
        solution = affine_f2_type_a_solution()
        u_array = u_array_from_solution(solution)

        self.assertTrue(stage_a_multiset_factorization_holds(u_array))
        buckets = stage_a_factorization_buckets(u_array)
        domains = stage_a_bucket_domains(u_array)
        self.assertEqual(len(buckets), 8)
        self.assertTrue(all(len(bucket.cells) == len(bucket.values) for bucket in buckets))
        self.assertTrue(all(len(bucket.cells) <= 2 for bucket in buckets))
        self.assertTrue(
            all(
                domains[x][y]
                for x in range(len(u_array))
                for y in range(len(u_array))
            )
        )


if __name__ == "__main__":
    unittest.main()
