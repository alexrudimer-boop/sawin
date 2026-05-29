import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    braid_action_preserves_structure_orbits,
    identity_solution,
    level_structure_orbit_partition,
    rack_inner_group,
    rack_solution,
    structure_orbit,
    structure_orbit_factorization_summary,
    structure_orbit_holonomy_summary,
    structure_orbit_law_separation,
)
from ybe_domination.finite_group import cyclic_group


class StructureOrbitTests(unittest.TestCase):
    def test_identity_solution_has_singleton_structure_orbits(self):
        solution = identity_solution([0, 1])
        partition = level_structure_orbit_partition(solution, 2)
        self.assertEqual(len(partition), 4)
        self.assertTrue(all(len(block) == 1 for block in partition))

    def test_trivial_rack_structure_orbit_is_multiset_class(self):
        solution = rack_solution([0, 1], lambda _left, right: right)
        orbit = structure_orbit(solution, (0, 1, 1))
        self.assertEqual(orbit, ((0, 1, 1), (1, 0, 1), (1, 1, 0)))

    def test_braid_action_preserves_structure_orbits(self):
        solution = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        self.assertTrue(
            braid_action_preserves_structure_orbits(
                solution,
                3,
                (1, 2, -1, 2, 1),
            )
        )

    def test_structure_orbit_holonomy_summary_for_identity_solution(self):
        solution = identity_solution([0, 1])
        summary = structure_orbit_holonomy_summary(solution, 2)
        self.assertEqual(summary.orbit_count, 4)
        self.assertEqual(summary.orbit_sizes, (1, 1, 1, 1))
        self.assertEqual(summary.orbit_group_sizes, (1, 1, 1, 1))
        self.assertEqual(summary.orbit_group_exponents, (1, 1, 1, 1))
        self.assertEqual(summary.truncated_orbit_count, 0)

    def test_structure_orbit_holonomy_summary_for_trivial_rack(self):
        solution = rack_solution([0, 1], lambda _left, right: right)
        summary = structure_orbit_holonomy_summary(solution, 3)
        rows = sorted(zip(summary.orbit_sizes, summary.orbit_group_sizes))
        self.assertIn((3, 6), rows)
        self.assertEqual(summary.truncated_orbit_count, 0)

    def test_structure_orbit_factorization_summary_for_trivial_rack(self):
        solution = rack_solution([0, 1], lambda _left, right: right)
        summary = structure_orbit_factorization_summary(solution, 3)
        self.assertEqual(summary.tuple_count, 8)
        self.assertEqual(summary.global_group_size, 6)
        self.assertEqual(summary.global_group_exponent, 6)
        self.assertEqual(summary.product_group_size_bound, 36)
        self.assertEqual(summary.projections_match_orbit_groups, True)
        self.assertEqual(summary.orbit_group_truncated_count, 0)
        self.assertFalse(summary.global_group_truncated)

    def test_action_image_growth_is_not_a_counterexample_for_racks(self):
        solution = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)

        degree_three = structure_orbit_factorization_summary(
            solution,
            3,
            max_group_size=2000,
        )
        degree_four = structure_orbit_factorization_summary(
            solution,
            4,
            max_group_size=2000,
        )

        self.assertEqual(degree_three.global_group_size, 24)
        self.assertEqual(degree_four.global_group_size, 648)
        self.assertGreater(degree_four.global_group_size, degree_three.global_group_size)
        self.assertFalse(degree_three.global_group_truncated)
        self.assertFalse(degree_four.global_group_truncated)

    def test_structure_orbit_law_separation_finds_orbit_local_mover(self):
        solution = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        separation = structure_orbit_law_separation(
            solution,
            3,
            (cyclic_group(2), cyclic_group(3)),
            max_length=4,
        )
        self.assertEqual(separation.n, 3)
        self.assertEqual(separation.arity, 2)
        self.assertEqual(
            separation.separating_word,
            ((0, 1), (1, 1), (0, -1), (1, -1)),
        )
        self.assertIsNotNone(separation.moved_tuple)
        self.assertIsNotNone(separation.moved_image)
        self.assertNotEqual(separation.moved_tuple, separation.moved_image)

    def test_structure_orbit_law_separation_respects_rack_inner_detector(self):
        solution = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)
        separation = structure_orbit_law_separation(
            solution,
            3,
            (rack_inner_group(solution),),
            max_length=6,
        )
        self.assertIsNone(separation.separating_word)
        self.assertIsNone(separation.moved_tuple)

    def test_structure_orbit_law_separation_uses_assigned_pure_generators(self):
        solution = rack_solution([0, 1, 2], lambda left, right: (2 * left - right) % 3)

        too_small = structure_orbit_law_separation(
            solution,
            4,
            (cyclic_group(2), cyclic_group(3)),
            max_length=4,
            max_group_size=2000,
        )
        self.assertEqual(
            too_small.separating_word,
            ((0, 1), (1, 1), (0, -1), (1, -1)),
        )
        self.assertEqual(too_small.target_group_size, 648)
        self.assertIsNotNone(too_small.moved_tuple)

        with_inner = structure_orbit_law_separation(
            solution,
            4,
            (rack_inner_group(solution),),
            max_length=4,
            max_group_size=2000,
        )
        self.assertIsNone(with_inner.separating_word)
        self.assertIsNone(with_inner.moved_tuple)


if __name__ == "__main__":
    unittest.main()
