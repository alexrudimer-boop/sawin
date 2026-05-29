import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    commutator,
    cyclic_group,
    exponent_law_profile,
    exponent_law_word,
    free_word_power,
    group_exponent,
    has_identity_longitude_signature,
    is_law_on_group,
    is_normal_subgroup,
    law_braid_longitude_subgroup_profile,
    law_sequence_prefix_audit,
    lcm_upto,
    normal_closure_elements,
    quotient_group_by_normal_subgroup,
    reduced_free_words,
    short_law_escaping_variety,
    short_law_separating_groups,
    subgroup_generated_elements,
    symmetric_group,
    two_strand_exponent_law_braid,
    two_strand_longitude_period,
    two_strand_pure_power,
    two_strand_symmetric_longitude_period,
)


class GroupLawTests(unittest.TestCase):
    def test_lcm_upto(self):
        self.assertEqual(lcm_upto(1), 1)
        self.assertEqual(lcm_upto(3), 6)
        self.assertEqual(lcm_upto(5), 60)

    def test_group_exponent(self):
        self.assertEqual(group_exponent(cyclic_group(2)), 2)
        self.assertEqual(group_exponent(cyclic_group(3)), 3)
        self.assertEqual(group_exponent(symmetric_group(3)), 6)

    def test_subgroup_generated_elements_inside_finite_group(self):
        group = symmetric_group(3)
        transposition = (1, 0, 2)
        subgroup = subgroup_generated_elements(group, [transposition])
        self.assertEqual(set(subgroup), {group.identity, transposition})

    def test_normal_closure_and_quotient_group_for_s3(self):
        group = symmetric_group(3)
        transposition = (1, 0, 2)
        three_cycle = (1, 2, 0)

        transposition_closure = normal_closure_elements(group, [transposition])
        self.assertEqual(set(transposition_closure), set(group.elements))
        self.assertTrue(is_normal_subgroup(group, transposition_closure))

        alternating_closure = normal_closure_elements(group, [three_cycle])
        self.assertEqual(
            set(alternating_closure),
            {group.identity, (1, 2, 0), (2, 0, 1)},
        )
        self.assertTrue(is_normal_subgroup(group, alternating_closure))

        quotient, projection = quotient_group_by_normal_subgroup(
            group,
            alternating_closure,
        )

        self.assertEqual(len(quotient.elements), 2)
        self.assertTrue(projection.is_surjective)
        self.assertEqual(
            {
                element
                for element in group.elements
                if projection.apply(element) == quotient.identity
            },
            set(alternating_closure),
        )

    def test_exponent_law_for_small_groups(self):
        word = exponent_law_word(3)
        self.assertTrue(is_law_on_group(cyclic_group(2), word, arity=1))
        self.assertTrue(is_law_on_group(cyclic_group(3), word, arity=1))
        self.assertTrue(is_law_on_group(symmetric_group(3), word, arity=1))

    def test_too_small_exponent_is_not_law(self):
        self.assertFalse(is_law_on_group(cyclic_group(3), free_word_power(0, 2), arity=1))

    def test_commutator_law_on_abelian_group_not_s3(self):
        word = commutator(free_word_power(0, 1), free_word_power(1, 1))
        self.assertTrue(is_law_on_group(cyclic_group(5), word, arity=2))
        self.assertFalse(is_law_on_group(symmetric_group(3), word, arity=2))

    def test_reduced_free_words_avoid_immediate_cancellation(self):
        words = list(reduced_free_words(arity=1, max_length=3))
        self.assertEqual(words, [
            ((0, 1),),
            ((0, -1),),
            ((0, 1), (0, 1)),
            ((0, -1), (0, -1)),
            ((0, 1), (0, 1), (0, 1)),
            ((0, -1), (0, -1), (0, -1)),
        ])

    def test_short_law_separating_groups_finds_commutator(self):
        word = short_law_separating_groups(
            [cyclic_group(2), cyclic_group(3)],
            symmetric_group(3),
            arity=2,
            max_length=4,
        )
        self.assertIsNotNone(word)
        self.assertTrue(is_law_on_group(cyclic_group(2), word, arity=2))
        self.assertTrue(is_law_on_group(cyclic_group(3), word, arity=2))
        self.assertFalse(is_law_on_group(symmetric_group(3), word, arity=2))

    def test_short_law_escaping_variety_detects_nonabelian_escape(self):
        word = short_law_escaping_variety(
            cyclic_group(6),
            symmetric_group(3),
            arity=2,
            max_length=4,
        )
        self.assertEqual(
            word,
            ((0, 1), (1, 1), (0, -1), (1, -1)),
        )

        no_subgroup_escape = short_law_escaping_variety(
            symmetric_group(3),
            cyclic_group(3),
            arity=2,
            max_length=5,
        )
        self.assertIsNone(no_subgroup_escape)

    def test_exponent_law_profile(self):
        profile = exponent_law_profile(
            {"C2": cyclic_group(2), "C3": cyclic_group(3), "S3": symmetric_group(3)},
            3,
        )
        self.assertEqual(profile["exponent"], 6)
        self.assertEqual(profile["failures"], ())

    def test_law_sequence_prefix_audit_checks_order_bound(self):
        groups = {
            "C2": cyclic_group(2),
            "C3": cyclic_group(3),
            "S3": symmetric_group(3),
        }
        words = tuple(exponent_law_word(bound) for bound in range(1, 7))

        audit = law_sequence_prefix_audit(groups, words, arity=1)

        self.assertEqual(audit.word_count, 6)
        self.assertTrue(audit.all_required_prefix_laws_hold)
        self.assertEqual(audit.failed_rows, ())
        self.assertIn(
            (6, "S3", 6, True),
            tuple(
                (row.index, row.group_name, row.group_order, row.is_law)
                for row in audit.rows
            ),
        )
        self.assertNotIn(
            "S3",
            tuple(row.group_name for row in audit.rows if row.index < 6),
        )

    def test_law_sequence_prefix_audit_reports_failures(self):
        audit = law_sequence_prefix_audit(
            {"C2": cyclic_group(2)},
            (free_word_power(0, 1),),
            arity=1,
            start_index=2,
        )

        self.assertFalse(audit.all_required_prefix_laws_hold)
        self.assertEqual(len(audit.failed_rows), 1)
        self.assertEqual(audit.failed_rows[0].group_name, "C2")

        with self.assertRaises(ValueError):
            law_sequence_prefix_audit({}, (), arity=1, start_index=0)

    def test_two_strand_exponent_law_braid_is_longitude_invisible(self):
        braid = two_strand_exponent_law_braid(3)
        self.assertEqual(braid, two_strand_pure_power(6))
        self.assertTrue(has_identity_longitude_signature(cyclic_group(2), 2, braid))
        self.assertTrue(has_identity_longitude_signature(cyclic_group(3), 2, braid))
        self.assertTrue(has_identity_longitude_signature(symmetric_group(3), 2, braid))

    def test_two_strand_longitude_period_is_exact_for_small_groups(self):
        for group in (cyclic_group(1), cyclic_group(2), cyclic_group(3), symmetric_group(3)):
            period = two_strand_longitude_period(group)
            self.assertEqual(period, 2 * group_exponent(group))
            self.assertTrue(has_identity_longitude_signature(group, 2, (1,) * period))
            for exponent in range(1, period):
                self.assertFalse(
                    has_identity_longitude_signature(group, 2, (1,) * exponent),
                    msg=(group.elements, exponent, period),
                )

    def test_two_strand_symmetric_longitude_period(self):
        self.assertEqual(two_strand_symmetric_longitude_period(1), 2)
        self.assertEqual(two_strand_symmetric_longitude_period(2), 4)
        self.assertEqual(two_strand_symmetric_longitude_period(3), 12)
        self.assertEqual(two_strand_symmetric_longitude_period(4), 24)

    def test_law_braid_longitude_subgroup_profile(self):
        word = exponent_law_word(3)
        profile = law_braid_longitude_subgroup_profile(
            {"C2": cyclic_group(2), "C3": cyclic_group(3)},
            word,
            arity=1,
        )
        self.assertEqual(tuple(row.subgroup_size for row in profile), (1, 1))
        self.assertTrue(all(row.identity_longitude_signature for row in profile))


if __name__ == "__main__":
    unittest.main()
