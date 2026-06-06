import sys
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination.nonperm3_endpoint_detector_basis import (
    canonical_partitions_3,
    is_associative_monoid,
    nonpermutation_size3_solutions,
    principal_bad_endpoint_candidates,
    principal_bad_endpoint_candidates_for_nonperm3,
    solution_from_flat_table,
    truncated_structure_monoid_length_1,
    truncated_structure_monoid_length_2,
)
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


if __name__ == "__main__":
    unittest.main()
