import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    braid_images_for_words,
    compose_permutations,
    commutator,
    evaluate_free_word_on_permutations,
    free_word_power,
    generated_permutation_subgroup,
    identity_permutation,
    invert_permutation,
    law_braid_action_certificate,
    law_word_on_last_strand,
    pure_generator_order_profile,
    pure_braid_generator,
    pure_subgroup_growth_profile,
    rack_solution,
    short_law_separating_permutation_assignment,
    cyclic_group,
)


class ActionImageTests(unittest.TestCase):
    def test_permutation_group_operations(self):
        p = (1, 0, 2)
        q = (0, 2, 1)
        self.assertEqual(compose_permutations(p, invert_permutation(p)), identity_permutation(3))
        self.assertEqual(compose_permutations(p, q), (1, 2, 0))

    def test_generated_subgroup(self):
        subgroup = generated_permutation_subgroup([(1, 0, 2), (0, 2, 1)])
        self.assertEqual(len(subgroup), 6)

    def test_pure_generator_order_profile_for_trivial_rack(self):
        solution = rack_solution([0, 1], lambda a, b: b)
        profile = pure_generator_order_profile(solution, max_q=4)
        self.assertEqual([row.max_order for row in profile], [1, 1, 1])

    def test_pure_subgroup_growth_profile_for_dihedral_quandle(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        profile = pure_subgroup_growth_profile(
            solution,
            max_q=3,
            max_subgroup_size=100,
        )
        self.assertEqual(profile[0].subgroup_size, 3)
        self.assertEqual(profile[0].subgroup_exponent, 3)
        self.assertFalse(profile[0].truncated)
        self.assertEqual(profile[1].subgroup_size, 24)
        self.assertEqual(profile[1].subgroup_exponent, 12)
        self.assertFalse(profile[1].truncated)

    def test_free_word_evaluation_matches_law_braid_action(self):
        solution = rack_solution([0, 1], lambda a, b: b)
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        n, braid = law_word_on_last_strand(word, arity=2)
        images = braid_images_for_words(
            solution,
            n,
            {0: pure_braid_generator(1, n), 1: pure_braid_generator(2, n)},
        )
        evaluated = evaluate_free_word_on_permutations(word, images)
        direct = braid_images_for_words(solution, n, {0: braid})[0]
        self.assertEqual(evaluated, direct)

    def test_law_braid_action_certificate_records_fixed_image_barrier(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        exponent_word = free_word_power(0, 12)
        exponent_certificate = law_braid_action_certificate(
            solution, exponent_word, arity=1
        )
        self.assertTrue(exponent_certificate.direct_matches_evaluated)
        self.assertTrue(exponent_certificate.word_is_law_on_image_subgroup)
        self.assertTrue(exponent_certificate.evaluated_word_is_identity)
        self.assertTrue(exponent_certificate.direct_braid_is_identity)

        commutator_word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        commutator_certificate = law_braid_action_certificate(
            solution, commutator_word, arity=2
        )
        self.assertTrue(commutator_certificate.direct_matches_evaluated)
        self.assertFalse(commutator_certificate.word_is_law_on_image_subgroup)
        self.assertFalse(commutator_certificate.evaluated_word_is_identity)
        self.assertFalse(commutator_certificate.direct_braid_is_identity)

    def test_short_law_separating_permutation_assignment_records_mover(self):
        swap01 = (1, 0, 2)
        swap12 = (0, 2, 1)

        separation = short_law_separating_permutation_assignment(
            (cyclic_group(2), cyclic_group(3)),
            {0: swap01, 1: swap12},
            max_length=4,
        )

        self.assertEqual(
            separation.separating_word,
            ((0, 1), (1, 1), (0, -1), (1, -1)),
        )
        self.assertEqual(separation.arity, 2)
        self.assertEqual(separation.target_degree, 3)
        self.assertIsNotNone(separation.evaluated_permutation)
        self.assertIsNotNone(separation.moved_index)
        self.assertNotEqual(
            separation.evaluated_permutation[separation.moved_index],
            separation.moved_index,
        )


if __name__ == "__main__":
    unittest.main()
