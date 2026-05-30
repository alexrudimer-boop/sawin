import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    commutator,
    cyclic_group,
    free_word_power,
    has_identity_longitude_signature,
    is_law_on_group,
    last_strand_law_exactness_audit,
    law_braid_longitudes,
    law_word_on_last_strand,
    longitude_identity_profile_for_law_braid,
    point_pushing_derivative_detector_generators,
    point_pushing_kernel_membership_audit,
    pure_braid_generator,
    reverse_braid_word,
    symmetric_group,
)


class BraidLawTests(unittest.TestCase):
    def test_standard_pure_braid_generator(self):
        self.assertEqual(pure_braid_generator(1, 2), (1, 1))
        self.assertEqual(pure_braid_generator(1, 3), (2, 1, 1, -2))

    def test_reverse_braid_word_is_involutive(self):
        word = (1, -2, 3, 2, -1)
        reversed_word = reverse_braid_word(4, word)

        self.assertEqual(reversed_word, (3, -2, 1, 2, -3))
        self.assertEqual(reverse_braid_word(4, reversed_word), word)

    def test_exponent_law_word_on_last_strand(self):
        n, braid = law_word_on_last_strand(free_word_power(0, 6), arity=1)
        self.assertEqual(n, 2)
        self.assertEqual(braid, tuple(1 for _ in range(12)))
        self.assertTrue(has_identity_longitude_signature(cyclic_group(2), n, braid))
        self.assertTrue(has_identity_longitude_signature(cyclic_group(3), n, braid))

    def test_commutator_law_embedding_is_seen_by_s3(self):
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        invisible, visible = longitude_identity_profile_for_law_braid(
            {"C5": cyclic_group(5), "S3": symmetric_group(3)},
            word,
            arity=2,
        )
        self.assertIn("C5", invisible)
        self.assertIn("S3", visible)

    def test_law_braid_longitudes_are_pure(self):
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        data = law_braid_longitudes(word, arity=2)
        self.assertEqual(data.permutation, (0, 1, 2))

    def test_sampled_laws_give_longitude_invisible_law_braids(self):
        groups = [cyclic_group(2), cyclic_group(3), symmetric_group(3)]
        words = [
            (free_word_power(0, 6), 1),
            (commutator(free_word_power(0, 1), free_word_power(1, 1)), 2),
            (commutator(free_word_power(0, 2), free_word_power(1, 3)), 2),
        ]
        for word, arity in words:
            n, braid = law_word_on_last_strand(word, arity=arity)
            for group in groups:
                if is_law_on_group(group, word, arity=arity):
                    self.assertTrue(
                        has_identity_longitude_signature(group, n, braid)
                    )

    def test_last_strand_law_audit_records_necessary_condition(self):
        law = free_word_power(0, 6)
        law_audit = last_strand_law_exactness_audit(
            symmetric_group(3),
            law,
            arity=1,
        )

        self.assertTrue(law_audit.word_is_law)
        self.assertTrue(law_audit.identity_longitude_signature)
        self.assertTrue(law_audit.necessary_law_condition_holds)
        self.assertTrue(law_audit.law_implies_kernel_holds)
        self.assertTrue(law_audit.point_pushing_exactness_holds)

        nonlaw = commutator(free_word_power(0, 1), free_word_power(1, 1))
        nonlaw_audit = last_strand_law_exactness_audit(
            symmetric_group(3),
            nonlaw,
            arity=2,
        )

        self.assertFalse(nonlaw_audit.word_is_law)
        self.assertFalse(nonlaw_audit.identity_longitude_signature)
        self.assertTrue(nonlaw_audit.necessary_law_condition_holds)
        self.assertTrue(nonlaw_audit.law_implies_kernel_holds)
        self.assertTrue(nonlaw_audit.point_pushing_exactness_holds)

    def test_last_strand_law_audit_exposes_forward_gap(self):
        flattened = tuple(letter for _ in range(6) for letter in ((0, 1), (1, -1)))
        audit = last_strand_law_exactness_audit(
            symmetric_group(3),
            flattened,
            arity=2,
        )

        self.assertTrue(audit.word_is_law)
        self.assertFalse(audit.identity_longitude_signature)
        self.assertTrue(audit.necessary_law_condition_holds)
        self.assertFalse(audit.law_implies_kernel_holds)
        self.assertFalse(audit.point_pushing_exactness_holds)
        self.assertTrue(audit.exposes_law_to_kernel_gap)

    def test_point_pushing_kernel_membership_matches_detector_states(self):
        law = free_word_power(0, 6)
        audit = point_pushing_kernel_membership_audit(
            symmetric_group(3),
            law,
            arity=1,
        )

        self.assertTrue(audit.word_is_law)
        self.assertTrue(audit.identity_longitude_signature)
        self.assertTrue(audit.initial_detector_states_fixed)
        self.assertTrue(audit.detector_states_match_longitude_signature)
        self.assertTrue(audit.necessary_law_condition_holds)

    def test_point_pushing_derivative_detector_generators_act_on_full_state_space(self):
        generators = point_pushing_derivative_detector_generators(
            cyclic_group(2),
            arity=2,
        )

        self.assertEqual(set(generators), {0, 1})
        self.assertEqual(len(generators[0]), 64)
        self.assertEqual(len(generators[1]), 64)

    def test_point_pushing_kernel_membership_exposes_law_gap(self):
        law_gap = tuple(letter for _ in range(6) for letter in ((0, 1), (1, -1)))
        audit = point_pushing_kernel_membership_audit(
            symmetric_group(3),
            law_gap,
            arity=2,
        )

        self.assertTrue(audit.word_is_law)
        self.assertFalse(audit.identity_longitude_signature)
        self.assertFalse(audit.initial_detector_states_fixed)
        self.assertTrue(audit.detector_states_match_longitude_signature)
        self.assertTrue(audit.necessary_law_condition_holds)
        self.assertTrue(audit.exposes_law_to_kernel_gap)


if __name__ == "__main__":
    unittest.main()
