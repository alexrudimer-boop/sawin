import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    CongruenceInterval,
    LocalInterval,
    all_bijection_solutions,
    congruences,
    interval_covers,
    local_master_bottleneck_summary,
)
from ybe_domination.local_bottleneck import (
    KNOWN_TOTAL_DETECTOR_TAGS,
    _verdict_and_obligation,
)


def two_color_identity_interval():
    colors = ("a", "b")
    fibres = {"a": (0, 1), "b": (0, 1)}
    base_R = {(x, y): (x, y) for x in colors for y in colors}
    T = {
        (a, b, x, y): (x, y)
        for a in colors
        for b in colors
        for x in fibres[a]
        for y in fibres[b]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_flip_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (y, x)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_identity_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (x, y)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def one_color_large_flip_interval():
    colors = ("*",)
    fibres = {"*": tuple(range(6))}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): (y, x)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def dihedral_three_rack_interval():
    colors = ("*",)
    fibres = {"*": (0, 1, 2)}
    base_R = {("*", "*"): ("*", "*")}
    T = {
        ("*", "*", x, y): ((2 * x - y) % 3, x)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, T)


def three_color_direct_fibre2_affine_interval():
    base = tuple(all_bijection_solutions(3))[6]
    colors = base.elements
    points = (0, 1)
    fibres = {color: points for color in colors}
    labels = {
        (0, 0): {"L": 0, "R": 0},
        (0, 1): {"L": 0, "R": 0},
        (0, 2): {"L": 1, "R": 0},
        (1, 0): {"L": 0, "R": 0},
        (1, 1): {"L": 0, "R": 0},
        (1, 2): {"L": 1, "R": 0},
        (2, 0): {"L": 1, "R": 0},
        (2, 1): {"L": 1, "R": 0},
        (2, 2): {"L": 0, "R": 0},
    }
    table = {}
    for a, b in product(colors, repeat=2):
        for x, y in product(points, repeat=2):
            table[(a, b, x, y)] = (
                x ^ labels[(a, b)]["L"],
                y ^ labels[(a, b)]["R"],
            )
    return LocalInterval(colors, fibres, base.R, table)


class LocalMasterBottleneckTests(unittest.TestCase):
    def test_semisplit_leak_is_routed_before_master_interval(self):
        summary = local_master_bottleneck_summary(two_color_identity_interval())

        self.assertTrue(summary.colored_ybe)
        self.assertGreater(summary.semisplit_count, 0)
        self.assertFalse(summary.local_minimal)
        self.assertEqual(summary.local_minimal_pair_count, 2)
        self.assertEqual(summary.local_minimal_pair_failure_count, 2)
        self.assertEqual(summary.output_kernel_pair_count, 2)
        self.assertEqual(summary.output_kernel_pair_failure_count, 2)
        self.assertFalse(summary.output_kernel_pairs_all_universal)
        self.assertEqual(summary.verdict, "semisplit_leak")

    def test_universal_retraction_product_branch_is_routed_to_product_labels(self):
        summary = local_master_bottleneck_summary(one_color_flip_interval())

        self.assertTrue(summary.local_minimal)
        self.assertEqual(summary.local_minimal_pair_count, 1)
        self.assertEqual(summary.local_minimal_pair_failure_count, 0)
        self.assertIn(summary.product_branch, {"swapped", "swapped_and_direct"})
        self.assertIn("swapped_coboundary", summary.product_holonomy_details)
        self.assertEqual(summary.verdict, "product_finite_g_branch")

    def test_large_fibre_interval_uses_pair_closure_local_minimality_gate(self):
        summary = local_master_bottleneck_summary(one_color_large_flip_interval())

        self.assertTrue(summary.colored_ybe)
        self.assertFalse(summary.local_minimal)
        self.assertIsNone(summary.local_minimal_error)
        self.assertEqual(summary.local_minimal_pair_count, 15)
        self.assertEqual(summary.local_minimal_pair_failure_count, 15)
        self.assertIn(summary.product_branch, {"swapped", "swapped_and_direct"})
        self.assertEqual(summary.verdict, "not_local_minimal")

    def test_locally_nondegenerate_branch_is_not_the_corridor_bottleneck(self):
        summary = local_master_bottleneck_summary(dihedral_three_rack_interval())

        self.assertTrue(summary.local_minimal)
        self.assertEqual(summary.output_kernel_kind, "equality")
        self.assertEqual(summary.output_kernel_pair_count, 0)
        self.assertTrue(summary.output_kernel_pairs_all_universal)
        self.assertEqual(summary.verdict, "locally_nondegenerate_branch")
        self.assertNotEqual(summary.verdict, "bi_free_universal_corridor_bottleneck")

    def test_elementary_kernel_pairs_are_recorded_for_universal_corridor(self):
        summary = local_master_bottleneck_summary(one_color_identity_interval())

        self.assertTrue(summary.local_minimal)
        self.assertEqual(summary.output_kernel_kind, "universal")
        self.assertEqual(summary.output_kernel_pair_count, 1)
        self.assertEqual(summary.output_kernel_pair_failure_count, 0)
        self.assertEqual(summary.output_kernel_pair_max_depth, 0)
        self.assertTrue(summary.output_kernel_pairs_all_universal)

    def test_size_three_involutive_rows_are_not_corridor_bottlenecks(self):
        counts = {}
        for solution in all_bijection_solutions(3):
            for lower, upper in interval_covers(congruences(solution)):
                interval = CongruenceInterval(solution, lower, upper).local_interval()
                if not interval.is_local_minimal():
                    continue
                summary = local_master_bottleneck_summary(interval)
                counts[summary.verdict] = counts.get(summary.verdict, 0) + 1

        self.assertEqual(counts.get("product_finite_g_branch", 0), 116)
        self.assertEqual(counts.get("product_genuinely_coloured_bottleneck", 0), 0)
        self.assertEqual(counts.get("bi_free_universal_corridor_bottleneck", 0), 0)
        self.assertEqual(counts.get("known_total_branch", 0), 6)

    def test_affine_cyclic_tag_alone_is_not_a_known_total_detector(self):
        self.assertNotIn("affine_cyclic", KNOWN_TOTAL_DETECTOR_TAGS)

        verdict, obligation = _verdict_and_obligation(
            colored_ybe=True,
            semisplit_count=0,
            local_minimal=True,
            retraction_kind="two_sided_free",
            coretraction_kind="two_sided_free",
            product_branch="none",
            product_holonomy_details=(),
            output_kernel_kind="universal",
            total_branch_tags=("affine_cyclic",),
        )

        self.assertEqual(verdict, "bi_free_universal_corridor_bottleneck")
        self.assertIn("Green/corridor", obligation)

    def test_three_color_fibre_two_product_routes_to_affine_subbranch(self):
        interval = three_color_direct_fibre2_affine_interval()
        summary = local_master_bottleneck_summary(interval)

        self.assertTrue(interval.is_colored_ybe())
        self.assertTrue(summary.local_minimal)
        self.assertEqual(summary.total_branch_tags, ())
        self.assertIn("direct_fibre2_affine", summary.product_holonomy_details)
        self.assertEqual(summary.verdict, "product_finite_g_branch")


if __name__ == "__main__":
    unittest.main()
