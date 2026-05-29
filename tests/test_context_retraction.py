import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    LocalInterval,
    coordinate_kernel_seed_pairs,
    context_coretraction_audit,
    context_retraction_audit,
    direct_product_witness,
    generated_admissible_congruence_audit,
    generated_admissible_congruence_family,
    identity_solution,
    inverse_local_interval,
    one_step_context_profile_family,
    product_permutation_witness,
    relation_family_kind,
    solution_from_local_interval,
)


def one_color_interval(table):
    points = (0, 1)
    return LocalInterval(
        colors=("*",),
        fibres={"*": points},
        base_R={("*", "*"): ("*", "*")},
        T={("*", "*", x, y): table[(x, y)] for x in points for y in points},
    )


class ContextRetractionTests(unittest.TestCase):
    def test_identity_interval_has_equality_context_retraction(self):
        interval = one_color_interval({(x, y): (x, y) for x in (0, 1) for y in (0, 1)})
        audit = context_retraction_audit(interval)
        self.assertTrue(audit.initial_admissible)
        self.assertTrue(audit.admissible)
        self.assertEqual(audit.kind, "equality")
        self.assertEqual(audit.stable_depth, 1)

    def test_flip_interval_has_universal_context_retraction(self):
        interval = one_color_interval({(x, y): (y, x) for x in (0, 1) for y in (0, 1)})
        self.assertTrue(solution_from_local_interval(interval).total.is_ybe())
        audit = context_retraction_audit(interval)
        self.assertTrue(audit.initial_admissible)
        self.assertTrue(audit.admissible)
        self.assertEqual(audit.kind, "universal")
        witness = product_permutation_witness(interval)
        self.assertIsNotNone(witness)
        self.assertEqual(witness.left_maps[("*", "*")], {0: 0, 1: 1})
        self.assertEqual(witness.right_maps[("*", "*")], {0: 0, 1: 1})

        coretraction = context_coretraction_audit(interval)
        self.assertTrue(coretraction.admissible)
        self.assertEqual(coretraction.kind, "equality")

    def test_identity_interval_is_not_product_permutation_branch(self):
        interval = one_color_interval({(x, y): (x, y) for x in (0, 1) for y in (0, 1)})
        self.assertIsNone(product_permutation_witness(interval))

        coretraction = context_coretraction_audit(interval)
        self.assertTrue(coretraction.initial_admissible)
        self.assertTrue(coretraction.admissible)
        self.assertEqual(coretraction.kind, "universal")
        witness = direct_product_witness(interval)
        self.assertIsNotNone(witness)
        self.assertEqual(witness.left_maps[("*", "*")], {0: 0, 1: 1})
        self.assertEqual(witness.right_maps[("*", "*")], {0: 0, 1: 1})

    def test_rectangular_involutive_solution_has_mixed_retraction(self):
        points = tuple((a, b) for a in range(2) for b in range(2))
        interval = LocalInterval(
            colors=("*",),
            fibres={"*": points},
            base_R={("*", "*"): ("*", "*")},
            T={
                ("*", "*", x, y): ((x[0], y[1]), (y[0], x[1]))
                for x in points
                for y in points
            },
        )
        audit = context_retraction_audit(interval)
        self.assertTrue(audit.initial_admissible)
        self.assertEqual(audit.kind, "proper_mixed")
        coretraction = context_coretraction_audit(interval)
        self.assertTrue(coretraction.initial_admissible)
        self.assertEqual(coretraction.kind, "proper_mixed")
        self.assertFalse(interval.is_local_minimal(max_fibre_size=4))

    def test_context_retraction_of_quotient_singletons_is_equality(self):
        qmap = solution_from_local_interval(
            LocalInterval(
                colors=("a", "b"),
                fibres={"a": (0,), "b": (1,)},
                base_R={
                    ("a", "a"): ("a", "a"),
                    ("a", "b"): ("b", "a"),
                    ("b", "a"): ("a", "b"),
                    ("b", "b"): ("b", "b"),
                },
                T={
                    (left, right, x, y): (y, x)
                    for left in ("a", "b")
                    for right in ("a", "b")
                    for x in ((0,) if left == "a" else (1,))
                    for y in ((0,) if right == "a" else (1,))
                },
            )
        )
        audit = context_retraction_audit(
            LocalInterval(
                colors=qmap.quotient.elements,
                fibres={color: tuple(point for point in qmap.total.elements if point[0] == color) for color in qmap.quotient.elements},
                base_R=qmap.quotient.R,
                T={
                    (a, b, x, y): (qmap.total.R[(x, y)][0], qmap.total.R[(x, y)][1])
                    for a in qmap.quotient.elements
                    for b in qmap.quotient.elements
                    for x in tuple(point for point in qmap.total.elements if point[0] == a)
                    for y in tuple(point for point in qmap.total.elements if point[0] == b)
                },
            )
        )
        self.assertTrue(audit.admissible)
        self.assertEqual(audit.kind, "equality")

    def test_two_sided_closure_handles_non_ybe_bijection(self):
        points = (0, 1, 2)
        image = (
            (2, 1),
            (1, 1),
            (0, 1),
            (0, 0),
            (1, 2),
            (2, 2),
            (0, 2),
            (1, 0),
            (2, 0),
        )
        interval = LocalInterval(
            colors=("*",),
            fibres={"*": points},
            base_R={("*", "*"): ("*", "*")},
            T={
                ("*", "*", x, y): value
                for (x, y), value in zip(
                    ((x, y) for x in points for y in points), image
                )
            },
        )

        self.assertFalse(
            interval.is_admissible_congruence_family(
                one_step_context_profile_family(interval)
            )
        )
        audit = context_retraction_audit(interval)
        self.assertTrue(audit.admissible)
        self.assertEqual(audit.kind, "equality")

    def test_inverse_local_interval_roundtrips(self):
        interval = one_color_interval({(x, y): (y, x) for x in (0, 1) for y in (0, 1)})
        inverse = inverse_local_interval(interval)
        inverse_inverse = inverse_local_interval(inverse)
        self.assertEqual(inverse_inverse.base_R, interval.base_R)
        self.assertEqual(inverse_inverse.T, interval.T)

    def test_coordinate_kernel_generated_family_for_identity_interval(self):
        interval = one_color_interval({(x, y): (x, y) for x in (0, 1) for y in (0, 1)})
        seeds = coordinate_kernel_seed_pairs(interval)
        self.assertGreater(sum(len(pairs) for pairs in seeds.values()), 0)
        family = generated_admissible_congruence_family(interval, seeds)
        self.assertTrue(interval.is_admissible_congruence_family(family))
        self.assertEqual(relation_family_kind(interval, family), "universal")
        audit = generated_admissible_congruence_audit(interval, seeds)
        self.assertEqual(audit.kind, "universal")
        self.assertEqual(audit.stable_depth, 0)
        self.assertGreater(sum(count for _color, count in audit.edge_count_rows), 0)
        self.assertEqual(max(diameter for _color, diameter in audit.diameter_rows), 1)

    def test_output_kernel_generated_family_for_flip_interval_is_equality(self):
        interval = one_color_interval({(x, y): (y, x) for x in (0, 1) for y in (0, 1)})
        output_seeds = coordinate_kernel_seed_pairs(interval)
        self.assertEqual(sum(len(pairs) for pairs in output_seeds.values()), 0)
        output_family = generated_admissible_congruence_family(interval, output_seeds)
        self.assertTrue(interval.is_admissible_congruence_family(output_family))
        self.assertEqual(relation_family_kind(interval, output_family), "equality")

        all_seeds = coordinate_kernel_seed_pairs(
            interval,
            include_coretraction_kernels=True,
        )
        self.assertGreater(sum(len(pairs) for pairs in all_seeds.values()), 0)


if __name__ == "__main__":
    unittest.main()
