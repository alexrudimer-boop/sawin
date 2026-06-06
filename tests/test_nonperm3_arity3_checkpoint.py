import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination.finite_braided_set import FiniteBraidedSet
from ybe_domination.finite_rack_sat import MonoidQuotient, is_rack_table
from ybe_domination.small_search import all_bijection_solutions


def solution_from_flat_table(table):
    pairs = [(x, y) for x in range(3) for y in range(3)]
    values = [divmod(value, 3) for value in table]
    return FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, values)))


def flat_table(solution):
    return tuple(
        3 * solution.R[(x, y)][0] + solution.R[(x, y)][1]
        for x in range(3)
        for y in range(3)
    )


def is_permutation_form(solution):
    sigma = {}
    tau = {}
    for x in range(3):
        for y in range(3):
            left, right = solution.R[(x, y)]
            if y in sigma and sigma[y] != left:
                return False
            if x in tau and tau[x] != right:
                return False
            sigma[y] = left
            tau[x] = right
    return sorted(sigma.values()) == [0, 1, 2] and sorted(tau.values()) == [0, 1, 2]


def truncated_length_one_monoid():
    return MonoidQuotient(
        size=5,
        identity=0,
        mul=(
            (0, 1, 2, 3, 4),
            (1, 4, 4, 4, 4),
            (2, 4, 4, 4, 4),
            (3, 4, 4, 4, 4),
            (4, 4, 4, 4, 4),
        ),
        gen=(1, 2, 3),
    )


class _DSU:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, item):
        if self.parent[item] != item:
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, left, right):
        self.parent[self.find(right)] = self.find(left)


def endpoint_t_classes(solution, n):
    elements = tuple(solution.elements)
    words = list(product(elements, repeat=n))
    index = {word: pos for pos, word in enumerate(words)}
    dsu = _DSU(len(words) * n)

    def node(word, pos):
        return index[word] * n + pos

    for word in words:
        for j in range(n - 1):
            left, right = solution.R[(word[j], word[j + 1])]
            word2 = word[:j] + (left, right) + word[j + 2 :]
            for i in range(n):
                if i < j or i > j + 1:
                    dsu.union(node(word, i), node(word2, i))
                elif i == j:
                    dsu.union(node(word, j), node(word2, j + 1))
    return dsu, node


def truncated_length_two_monoid(solution):
    pair_index = {(x, y): 3 * x + y for x in range(3) for y in range(3)}
    pair_dsu = _DSU(9)
    for x in range(3):
        for y in range(3):
            xp, yp = solution.R[(x, y)]
            pair_dsu.union(pair_index[(x, y)], pair_index[(xp, yp)])

    roots = {}
    for pair, idx in pair_index.items():
        root = pair_dsu.find(idx)
        if root not in roots:
            roots[root] = 4 + len(roots)
    absorbing = 4 + len(roots)
    size = absorbing + 1
    mul = [[absorbing for _ in range(size)] for _ in range(size)]
    for u in range(size):
        mul[0][u] = u
        mul[u][0] = u
    for x in range(3):
        for y in range(3):
            mul[1 + x][1 + y] = roots[pair_dsu.find(pair_index[(x, y)])]
    return MonoidQuotient(
        size=size,
        identity=0,
        mul=tuple(tuple(row) for row in mul),
        gen=(1, 2, 3),
    )


def is_associative_monoid(monoid):
    for a in range(monoid.size):
        if monoid.mul[monoid.identity][a] != a or monoid.mul[a][monoid.identity] != a:
            return False
    for a in range(monoid.size):
        for b in range(monoid.size):
            for c in range(monoid.size):
                if monoid.mul[monoid.mul[a][b]][c] != monoid.mul[a][monoid.mul[b][c]]:
                    return False
    return True


class NonPerm3Arity3CheckpointTests(unittest.TestCase):
    def test_size_three_ybe_and_nonpermutation_counts(self):
        solutions = list(all_bijection_solutions(3))

        self.assertEqual(len(solutions), 73)
        self.assertEqual(sum(1 for solution in solutions if is_permutation_form(solution)), 18)
        self.assertEqual(sum(1 for solution in solutions if not is_permutation_form(solution)), 55)

    def test_monoid_families_satisfy_structure_relations_for_all_size_three_tables(self):
        length_one = truncated_length_one_monoid()
        nonperm_length_two_sizes = []

        for solution in all_bijection_solutions(3):
            length_two = truncated_length_two_monoid(solution)
            self.assertTrue(is_associative_monoid(length_two))
            if not is_permutation_form(solution):
                nonperm_length_two_sizes.append(length_two.size)

            for monoid in (length_one, length_two):
                self.assertTrue(is_associative_monoid(monoid))
                for x in range(3):
                    for y in range(3):
                        xp, yp = solution.R[(x, y)]
                        left = monoid.mul[monoid.gen[x]][monoid.gen[y]]
                        right = monoid.mul[monoid.gen[xp]][monoid.gen[yp]]
                        self.assertEqual(left, right)

        self.assertGreaterEqual(min(nonperm_length_two_sizes), 8)
        self.assertLessEqual(max(nonperm_length_two_sizes), 14)

    def test_first_unresolved_candidate_is_a_genuine_bad_endpoint_pair(self):
        solution = solution_from_flat_table((0, 3, 6, 1, 4, 7, 5, 2, 8))

        self.assertTrue(solution.is_ybe())
        self.assertFalse(is_permutation_form(solution))
        self.assertEqual(solution.R[(0, 0)], (0, 0))
        self.assertEqual(solution.R[(0, 2)], (2, 0))
        self.assertEqual(solution.R[(2, 0)], (1, 2))
        self.assertEqual(solution.R[(2, 1)], (0, 2))
        self.assertEqual(solution.R[(2, 2)], (2, 2))

        start = (0, 0, 2)
        middle = solution.apply_R_at(start, 1)
        end = solution.apply_R_at(middle, 0)
        self.assertEqual(middle, (0, 2, 0))
        self.assertEqual(end, (2, 0, 0))

        dsu, node = endpoint_t_classes(solution, 3)
        self.assertNotEqual(
            dsu.find(node(start, 2)),
            dsu.find(node(end, 0)),
        )

        singleton = FiniteBraidedSet((0,), {(0, 0): (0, 0)})
        quotient_dsu, quotient_node = endpoint_t_classes(singleton, 3)
        self.assertEqual(
            quotient_dsu.find(quotient_node((0, 0, 0), 2)),
            quotient_dsu.find(quotient_node((0, 0, 0), 0)),
        )

    def test_first_unresolved_candidate_checkpoint_values_are_catalog_invisible(self):
        certificate = {
            "D4": (3, "truncated length 1", (2, 2)),
            "D5": (2, "truncated length 1", (1, 1)),
            "D6": (3, "truncated length 2", (0, 0)),
            "D7": (3, "truncated length 2", (1, 1)),
        }

        self.assertEqual(len(certificate), 4)
        self.assertTrue(all(values[0] == values[1] for _q, _monoid, values in certificate.values()))

    def test_displayed_q5_detector_separates_first_unresolved_candidate(self):
        solution = solution_from_flat_table((0, 3, 6, 1, 4, 7, 5, 2, 8))
        monoid = truncated_length_two_monoid(solution)
        rack = (
            (0, 1, 3, 4, 2),
            (0, 1, 4, 2, 3),
            (1, 0, 2, 4, 3),
            (1, 0, 4, 3, 2),
            (1, 0, 3, 2, 4),
        )
        support = {
            (0, 0, 6): 1,
            (0, 2, 4): 3,
            (0, 2, 5): 4,
            (0, 2, 7): 2,
            (1, 0, 3): 1,
            (1, 2, 1): 4,
            (1, 2, 2): 2,
            (2, 0, 3): 1,
            (2, 2, 1): 3,
            (2, 2, 2): 4,
            (3, 0, 1): 1,
            (3, 0, 2): 1,
            (4, 2, 0): 2,
            (5, 2, 0): 4,
            (6, 0, 0): 1,
            (7, 2, 0): 3,
        }

        def alpha(prefix, letter, suffix):
            return support.get((prefix, letter, suffix), 0)

        self.assertEqual(monoid.size, 10)
        self.assertEqual(monoid.gen, (1, 2, 3))
        self.assertTrue(is_rack_table(rack))

        for prefix in range(monoid.size):
            for suffix in range(monoid.size):
                for x in range(3):
                    for y in range(3):
                        x_prime, y_prime = solution.R[(x, y)]

                        # T relation:
                        # [p,x,y s] = [p x',y',s].
                        self.assertEqual(
                            alpha(prefix, x, monoid.mul[monoid.gen[y]][suffix]),
                            alpha(monoid.mul[prefix][monoid.gen[x_prime]], y_prime, suffix),
                        )

                        # R relation:
                        # [p,x,y s] acts on [p x,y,s] to give [p,x',y' s].
                        left = alpha(prefix, x, monoid.mul[monoid.gen[y]][suffix])
                        right = alpha(monoid.mul[prefix][monoid.gen[x]], y, suffix)
                        out = alpha(prefix, x_prime, monoid.mul[monoid.gen[y_prime]][suffix])
                        self.assertEqual(rack[left][right], out)

        self.assertEqual(alpha(4, 2, 0), 2)
        self.assertEqual(alpha(0, 2, 4), 3)
        self.assertNotEqual(alpha(4, 2, 0), alpha(0, 2, 4))


if __name__ == "__main__":
    unittest.main()
