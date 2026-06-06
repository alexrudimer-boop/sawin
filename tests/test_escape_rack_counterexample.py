import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination.finite_braided_set import FiniteBraidedSet


def encode(pair):
    return 2 * pair[0] + pair[1]


def decode(value):
    return divmod(value, 2)


def affine_escape_solution() -> FiniteBraidedSet:
    table = {}
    for x in range(4):
        a, b = decode(x)
        for y in range(4):
            c, d = decode(y)
            left = (d, a ^ b ^ d)
            right = (a ^ c ^ d ^ 1, a ^ 1)
            table[(x, y)] = (encode(left), encode(right))
    return FiniteBraidedSet(tuple(range(4)), table)


class EscapeRackStrandSeparationCounterexampleTests(unittest.TestCase):
    def test_affine_table_is_bijective_ybe_solution(self):
        solution = affine_escape_solution()

        self.assertTrue(solution.is_ybe())
        self.assertEqual(len(set(solution.R.values())), 16)

    def test_expanded_ybe_formula_matches_both_sides(self):
        solution = affine_escape_solution()

        for a in range(2):
            for b in range(2):
                for c in range(2):
                    for d in range(2):
                        for e in range(2):
                            for f in range(2):
                                triple = (encode((a, b)), encode((c, d)), encode((e, f)))
                                left = solution.apply_R_at(
                                    solution.apply_R_at(solution.apply_R_at(triple, 0), 1),
                                    0,
                                )
                                right = solution.apply_R_at(
                                    solution.apply_R_at(solution.apply_R_at(triple, 1), 0),
                                    1,
                                )
                                expected_bits = (
                                    c ^ d ^ f,
                                    a ^ b ^ c ^ d ^ f,
                                    c ^ 1,
                                    d ^ 1,
                                    a ^ c ^ d ^ e ^ f,
                                    a ^ c ^ d,
                                )
                                expected = (
                                    encode(expected_bits[0:2]),
                                    encode(expected_bits[2:4]),
                                    encode(expected_bits[4:6]),
                                )
                                self.assertEqual(left, expected)
                                self.assertEqual(right, expected)

    def test_every_left_and_right_map_has_image_size_two(self):
        solution = affine_escape_solution()
        expected_minimal_images = {frozenset({0, 3}), frozenset({1, 2})}

        left_images = set()
        for x in range(4):
            image = frozenset(solution.R[(x, y)][0] for y in range(4))
            self.assertEqual(len(image), 2)
            left_images.add(image)

        right_images = set()
        for y in range(4):
            image = frozenset(solution.R[(x, y)][1] for x in range(4))
            self.assertEqual(len(image), 2)
            right_images.add(image)

        self.assertEqual(left_images, expected_minimal_images)
        self.assertEqual(right_images, expected_minimal_images)

    def test_escape_label_spanning_tree_collapses_all_elementary_labels(self):
        labels = [(p, i, j) for p in range(2) for i in range(2) for j in range(2)]
        parent = {label: label for label in labels}

        def find(label):
            if parent[label] != label:
                parent[label] = find(parent[label])
            return parent[label]

        def union(left, right):
            parent[find(right)] = find(left)

        edges = [
            ((0, 0, 0), (0, 0, 1)),
            ((0, 0, 0), (0, 1, 0)),
            ((0, 1, 0), (1, 1, 0)),
            ((0, 0, 1), (1, 0, 0)),
            ((1, 0, 0), (0, 1, 1)),
            ((0, 1, 1), (1, 0, 1)),
            ((1, 0, 1), (1, 1, 1)),
        ]
        for left, right in edges:
            union(left, right)

        self.assertEqual({find(label) for label in labels}, {find(labels[0])})

    def test_same_orbit_collision_with_constant_escape_label(self):
        solution = affine_escape_solution()
        word = (0, 1)
        path = [word]
        current = word
        for _ in range(4):
            current = solution.apply_R_at(current, 0)
            path.append(current)

        self.assertEqual(path, [(0, 1), (3, 1), (3, 2), (0, 2), (0, 1)])
        self.assertNotEqual(path[0], path[3])


if __name__ == "__main__":
    unittest.main()
