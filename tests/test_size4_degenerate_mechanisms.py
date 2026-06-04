import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import FiniteBraidedSet, is_involutive_solution, rack_solution


def affine_f2_type_a_solution():
    elements = tuple(product((0, 1), repeat=2))
    table = {}
    for a, b in elements:
        for c, d in elements:
            table[((a, b), (c, d))] = (
                (d, (a + b + d) % 2),
                ((a + c + d + 1) % 2, (a + 1) % 2),
            )
    return FiniteBraidedSet(elements, table)


def parity_vector(tup):
    return tuple((a + b) % 2 for a, b in tup)


def fibre_coordinates(tup):
    parities = parity_vector(tup)
    offsets = [0]
    for index in range(len(tup) - 1):
        offsets.append((offsets[-1] + parities[index + 1] + 1) % 2)
    return tuple((a + offset) % 2 for (a, _b), offset in zip(tup, offsets))


class SizeFourDegenerateMechanismTests(unittest.TestCase):
    def test_affine_f2_type_a_is_degenerate_noninvolutive_ybe(self):
        solution = affine_f2_type_a_solution()

        self.assertTrue(solution.is_ybe())
        self.assertFalse(is_involutive_solution(solution))
        self.assertEqual(solution.R[((0, 0), (0, 0))], ((0, 0), (1, 1)))
        self.assertEqual(solution.R[solution.R[((0, 0), (0, 0))]], ((1, 1), (1, 1)))

    def test_affine_f2_type_a_is_fibrewise_cyclic_rack_action(self):
        solution = affine_f2_type_a_solution()
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)

        for n in range(2, 5):
            for generator in range(1, n):
                for tup in product(solution.elements, repeat=n):
                    image = solution.braid_action((generator,), tup)
                    self.assertEqual(parity_vector(image), parity_vector(tup))
                    self.assertEqual(
                        fibre_coordinates(image),
                        cyclic.braid_action((generator,), fibre_coordinates(tup)),
                    )


if __name__ == "__main__":
    unittest.main()
