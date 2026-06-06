import sys
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination.nonperm3_endpoint_detector_basis import (
    canonical_partitions_3,
    detector_schema_to_record,
    first_detector_for_candidate,
    is_associative_monoid,
    nonpermutation_size3_solutions,
    principal_bad_endpoint_candidates,
    principal_bad_endpoint_candidates_for_nonperm3,
    reconstruct_detector_basis_payload,
    solution_from_flat_table,
    truncated_structure_monoid_length_1,
    truncated_structure_monoid_length_2,
    verify_detector_basis_payload,
    verify_detector_schema_record,
)
from ybe_domination.nonperm3_detector_products import verify_contextual_detector_record
from ybe_domination.small_search import all_bijection_solutions, is_permutation_solution_form


class NonPerm3EndpointDetectorBasisTests(unittest.TestCase):
    def test_monoid_families_satisfy_structure_relations_for_size_three_tables(self):
        length_one = truncated_structure_monoid_length_1()
        nonperm_length_two_sizes = []

        for solution in all_bijection_solutions(3):
            length_two = truncated_structure_monoid_length_2(solution)
            if not is_permutation_solution_form(solution):
                nonperm_length_two_sizes.append(length_two.size)

            for monoid in (length_one, length_two):
                self.assertTrue(is_associative_monoid(monoid))
                for x in range(3):
                    for y in range(3):
                        x_prime, y_prime = solution.R[(x, y)]
                        left = monoid.mul[monoid.gen[x]][monoid.gen[y]]
                        right = monoid.mul[monoid.gen[x_prime]][monoid.gen[y_prime]]
                        self.assertEqual(left, right)

        self.assertGreaterEqual(min(nonperm_length_two_sizes), 8)
        self.assertLessEqual(max(nonperm_length_two_sizes), 14)

    def test_reconstructs_nonperm3_bad_endpoint_counts(self):
        rows2 = principal_bad_endpoint_candidates_for_nonperm3(arity=2)
        rows3 = principal_bad_endpoint_candidates_for_nonperm3(arity=3)

        self.assertEqual(len(nonpermutation_size3_solutions()), 55)
        self.assertEqual(len(rows2), 2064)
        self.assertEqual(len(rows3), 37692)
        self.assertEqual(
            Counter(row.partition for row in rows2),
            Counter(
                {
                    (0, 0, 0): 1416,
                    (0, 0, 1): 216,
                    (0, 1, 0): 216,
                    (0, 1, 1): 216,
                }
            ),
        )
        self.assertEqual(canonical_partitions_3()[-1], (0, 1, 2))
        self.assertNotIn((0, 1, 2), {row.partition for row in rows2})

    def test_first_q4_unresolved_pair_is_reconstructed(self):
        solution = solution_from_flat_table((0, 3, 6, 1, 4, 7, 5, 2, 8))
        rows = principal_bad_endpoint_candidates(
            solution,
            solution_index=5,
            arity=3,
        )

        self.assertTrue(
            any(
                row.partition == (0, 0, 0)
                and row.e_word == (0, 0, 2)
                and row.e_position == 2
                and row.eprime_word == (2, 0, 0)
                and row.eprime_position == 0
                for row in rows
            )
        )

    def test_exports_and_verifies_first_found_detector_schema(self):
        solution = solution_from_flat_table((0, 3, 6, 1, 4, 7, 5, 2, 8))
        candidate = next(
            row
            for row in principal_bad_endpoint_candidates(
                solution,
                solution_index=5,
                arity=3,
            )
            if row.partition == (0, 0, 0)
            and row.e_word == (0, 0, 2)
            and row.e_position == 2
            and row.eprime_word == (2, 0, 0)
            and row.eprime_position == 0
        )

        schema = first_detector_for_candidate(
            solution,
            candidate,
            monoid_family_names=(
                "truncated_structure_monoid_length_1",
                "truncated_structure_monoid_length_2",
            ),
            qmax=5,
            source_batch="test_batch",
        )

        self.assertIsNotNone(schema)
        assert schema is not None
        record = detector_schema_to_record(schema)
        self.assertEqual(verify_detector_schema_record(record), tuple())
        self.assertTrue(verify_contextual_detector_record(record).ok)
        self.assertNotEqual(record["endpoint_values"][0], record["endpoint_values"][1])

    def test_reconstruction_payload_verifier_accepts_development_probe(self):
        payload = reconstruct_detector_basis_payload(
            arity=2,
            qmax=2,
            monoid_family_names=("truncated_structure_monoid_length_1",),
            enforce_checkpoint_counts=False,
        )

        self.assertEqual(verify_detector_basis_payload(payload), tuple())
        self.assertEqual(payload["kind"], "nonperm3_endpoint_detector_basis_reconstruction_v1")
        self.assertLess(payload["positive_detector_coverages"], 2064)
        self.assertGreater(payload["unresolved_obstruction_candidates"], 0)


if __name__ == "__main__":
    unittest.main()
