import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    LocalInterval,
    bounded_local_obstructions,
    cyclic_group,
    identity_solution,
    moved_by_interval,
    solution_from_local_interval,
)


def one_color_flip_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    table = {
        ("*", "*", x, y): (y, x)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, table)


def one_color_permutation_interval():
    colors = ("*",)
    fibres = {"*": (0, 1)}
    base_R = {("*", "*"): ("*", "*")}
    flip = {0: 1, 1: 0}
    table = {
        ("*", "*", x, y): (flip[y], x)
        for x in fibres["*"]
        for y in fibres["*"]
    }
    return LocalInterval(colors, fibres, base_R, table)


class LocalModelTests(unittest.TestCase):
    def test_local_interval_realizes_ybe_solution(self):
        qmap = solution_from_local_interval(one_color_flip_interval())
        self.assertTrue(qmap.total.is_ybe())
        qmap.validate_homomorphism()

    def test_moved_by_interval_reports_residual_motion(self):
        moved = moved_by_interval(one_color_flip_interval(), 2, [1])
        self.assertIsNotNone(moved)

    def test_bounded_local_obstruction_for_trivial_group(self):
        interval = one_color_permutation_interval()
        base_detector = identity_solution(["*"])
        obstructions = bounded_local_obstructions(
            interval,
            base_detector,
            {"trivial": cyclic_group(1)},
            2,
            2,
        )
        self.assertIn((1, 1), obstructions)
        self.assertEqual(obstructions[(1, 1)].visible_groups, ())

    def test_nontrivial_group_sees_the_small_pure_braid(self):
        interval = one_color_permutation_interval()
        base_detector = identity_solution(["*"])
        obstructions = bounded_local_obstructions(
            interval,
            base_detector,
            {"C2": cyclic_group(2)},
            2,
            2,
        )
        self.assertNotIn((1, 1), obstructions)


if __name__ == "__main__":
    unittest.main()
