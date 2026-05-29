import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    LocalInterval,
    bifree_corridor_detector_target,
    bifree_corridor_bounded_failures,
    bifree_corridor_exact_image_audit,
    bifree_corridor_product_subgroup_audit,
    bifree_corridor_word_certificate,
    commutator,
    free_word_power,
    law_word_on_last_strand,
)


def interval_from_solution(solution):
    colors = ("*",)
    fibres = {"*": tuple(solution.elements)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): solution.R[(x, y)]
        for x, y in product(solution.elements, repeat=2)
    }
    return LocalInterval(colors, fibres, base_R, T)


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


class BiFreeCorridorCertificateTests(unittest.TestCase):
    def test_detector_target_records_fixed_green_factor_product(self):
        interval = interval_from_solution(size_three_affine_candidate())

        target = bifree_corridor_detector_target(interval)

        self.assertEqual(sorted(target.factor_orders), [2, 3, 6])
        self.assertEqual(target.detector_order, 36)
        self.assertEqual(target.total_size, 3)
        self.assertEqual(target.quotient_size, 1)
        self.assertFalse(target.applies)

    def test_word_certificate_records_visible_symmetric_factor(self):
        interval = interval_from_solution(size_three_affine_candidate())
        law = commutator(free_word_power(0, 1), free_word_power(1, 1))
        n, braid = law_word_on_last_strand(law, arity=2)

        certificate = bifree_corridor_word_certificate(interval, n, braid)

        self.assertTrue(certificate.quotient_fixed)
        self.assertIsNotNone(certificate.moved_residual_tuple)
        self.assertFalse(certificate.all_listed_factors_invisible)
        self.assertTrue(
            any(name.endswith("_order_6") for name in certificate.visible_factor_names)
        )
        self.assertFalse(certificate.is_b_failure_against_listed_factors)

    def test_product_subgroup_audit_matches_listed_corridor_factors(self):
        interval = interval_from_solution(size_three_affine_candidate())

        audit = bifree_corridor_product_subgroup_audit(interval, 2, (1, 1))

        self.assertFalse(audit.truncated)
        self.assertEqual(sorted(audit.factor_orders), [2, 3, 6])
        self.assertEqual(audit.product_group_order, 36)
        self.assertTrue(audit.product_subgroup_equals_factor_product)
        self.assertEqual(
            audit.product_subgroup_size,
            audit.expected_product_subgroup_size,
        )
        self.assertFalse(audit.all_factor_identity_signatures)
        self.assertFalse(audit.product_identity_signature)
        self.assertTrue(audit.product_identity_signature_equivalent)

    def test_product_subgroup_audit_can_skip_large_product_enumeration(self):
        interval = interval_from_solution(size_three_affine_candidate())

        audit = bifree_corridor_product_subgroup_audit(
            interval,
            2,
            (1, 1),
            max_product_order=10,
        )

        self.assertTrue(audit.truncated)
        self.assertEqual(audit.product_group_order, 36)
        self.assertIsNone(audit.product_subgroup_equals_factor_product)
        self.assertIsNone(audit.product_identity_signature_equivalent)

    def test_bounded_failure_scan_finds_no_affine_short_escape(self):
        interval = interval_from_solution(size_three_affine_candidate())

        failures = bifree_corridor_bounded_failures(
            interval,
            n=3,
            max_word_length=4,
        )

        self.assertEqual(failures, ())

    def test_exact_image_audit_reuses_corridor_factor_list(self):
        interval = interval_from_solution(size_three_affine_candidate())

        audit = bifree_corridor_exact_image_audit(interval, n=2, state_limit=1000)

        self.assertFalse(audit.truncated)
        self.assertIsNone(audit.kernel_failure)
        self.assertIsNone(audit.collision_failure)
        self.assertTrue(audit.proves_fixed_n_implication)
        self.assertEqual(audit.visited_state_count, 12)


if __name__ == "__main__":
    unittest.main()
