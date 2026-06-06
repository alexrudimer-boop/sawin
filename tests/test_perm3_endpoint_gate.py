import sys
import unittest
from collections import deque
from itertools import permutations, product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination.finite_braided_set import FiniteBraidedSet
from ybe_domination.finite_rack_sat import (
    Endpoint,
    MonoidQuotient,
    RackDetector,
    build_context_presentation,
    is_rack_table,
    verify_detector,
)


S3 = tuple(permutations(range(3)))


def compose(left, right):
    return tuple(left[right[i]] for i in range(len(left)))


def inverse(perm):
    out = [0] * len(perm)
    for i, value in enumerate(perm):
        out[value] = i
    return tuple(out)


def perm_power(perm, exponent):
    out = tuple(range(len(perm)))
    for _ in range(exponent):
        out = compose(perm, out)
    return out


def perm_order(perm):
    out = tuple(range(len(perm)))
    for exponent in range(1, 7):
        out = compose(perm, out)
        if out == tuple(range(len(perm))):
            return exponent
    raise AssertionError("unexpected S3 order")


def permutation_form_solution(sigma, tau):
    return FiniteBraidedSet(
        tuple(range(3)),
        {(x, y): (sigma[y], tau[x]) for x in range(3) for y in range(3)},
    )


def flat_table(solution):
    return tuple(
        3 * solution.R[(x, y)][0] + solution.R[(x, y)][1]
        for x in range(3)
        for y in range(3)
    )


def cyclic_monoid(order):
    if order == 1:
        return MonoidQuotient(size=1, identity=0, mul=((0,),), gen=(0, 0, 0))
    return MonoidQuotient(
        size=order,
        identity=0,
        mul=tuple(tuple((i + j) % order for j in range(order)) for i in range(order)),
        gen=(1, 1, 1),
    )


def five_element_prefix_suffix_monoid():
    return MonoidQuotient(
        size=5,
        identity=0,
        mul=(
            (0, 1, 2, 3, 4),
            (1, 1, 1, 1, 1),
            (2, 1, 1, 1, 1),
            (3, 1, 1, 1, 1),
            (4, 1, 1, 1, 1),
        ),
        gen=(2, 3, 4),
    )


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


def constant_action_rack(rho):
    return tuple(tuple(rho[value] for value in range(3)) for _ in range(3))


def detector_alpha(tau, p, x, _s):
    tau_inv = inverse(tau)
    value = x
    for _ in range(p):
        value = tau_inv[value]
    return value


def low_arity_alpha(p, x, s):
    support = {
        (0, 0, 4),
        (0, 1, 2),
        (0, 2, 3),
        (2, 0, 0),
        (3, 1, 0),
        (4, 2, 0),
    }
    return 1 if (p, x, s) in support else 0


def schema_satisfies_contextual_relations(solution, monoid, rack_table, alpha):
    for p in range(monoid.size):
        for s in range(monoid.size):
            for x in range(3):
                for y in range(3):
                    xp, yp = solution.R[(x, y)]
                    left_t = alpha(p, x, monoid.mul[monoid.gen[y]][s])
                    right_t = alpha(monoid.mul[p][monoid.gen[xp]], yp, s)
                    if left_t != right_t:
                        return False
                    first = alpha(p, x, monoid.mul[monoid.gen[y]][s])
                    second = alpha(monoid.mul[p][monoid.gen[x]], y, s)
                    out = alpha(p, xp, monoid.mul[monoid.gen[yp]][s])
                    if rack_table[first][second] != out:
                        return False
    return True


def assignment_from_raw_alpha(presentation, monoid, alpha):
    assignment = [None] * presentation.class_count
    for p in range(monoid.size):
        for x in range(3):
            for s in range(monoid.size):
                raw = (p * 3 + x) * monoid.size + s
                cls = presentation.raw_to_class[raw]
                value = alpha(p, x, s)
                if assignment[cls] is None:
                    assignment[cls] = value
                elif assignment[cls] != value:
                    raise AssertionError("alpha is not constant on T-classes")
    return tuple(0 if value is None else value for value in assignment)


def context_orbit(rho, word):
    if len(word) < 2:
        return {tuple(word)}
    seen = {tuple(word)}
    queue = deque([tuple(word)])
    while queue:
        current = queue.popleft()
        for i in range(len(current) - 1):
            nxt = (
                current[:i]
                + (rho[current[i + 1]], current[i])
                + current[i + 2 :]
            )
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return seen


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


class Perm3EndpointGateTests(unittest.TestCase):
    def test_commuting_pairs_are_exactly_permutation_form_ybe_solutions(self):
        commuting = [(sigma, tau) for sigma in S3 for tau in S3 if compose(sigma, tau) == compose(tau, sigma)]

        self.assertEqual(len(commuting), 18)
        for sigma, tau in commuting:
            self.assertTrue(permutation_form_solution(sigma, tau).is_ybe())
        for sigma in S3:
            for tau in S3:
                if compose(sigma, tau) != compose(tau, sigma):
                    self.assertFalse(permutation_form_solution(sigma, tau).is_ybe())

    def test_detector_schema_satisfies_contextual_relations_for_all_commuting_pairs(self):
        for sigma in S3:
            for tau in S3:
                if compose(sigma, tau) != compose(tau, sigma):
                    continue
                solution = permutation_form_solution(sigma, tau)
                rho = compose(tau, sigma)
                rack_table = constant_action_rack(rho)
                monoid = cyclic_monoid(perm_order(tau))

                with self.subTest(sigma=sigma, tau=tau):
                    self.assertTrue(is_rack_table(rack_table))
                    self.assertTrue(
                        schema_satisfies_contextual_relations(
                            solution,
                            monoid,
                            rack_table,
                            lambda p, x, s, tau=tau: detector_alpha(tau, p, x, s),
                        )
                    )

    def test_context_orbit_classifiers_for_rho_cycle_types(self):
        identity = (0, 1, 2)
        transposition = (1, 0, 2)
        three_cycle = (1, 2, 0)

        for m in range(1, 5):
            for word in product(range(3), repeat=m):
                orbit = context_orbit(identity, word)
                expected = {candidate for candidate in product(range(3), repeat=m) if sorted(candidate) == sorted(word)}
                self.assertEqual(orbit, expected)

        fixed = 2
        for m in range(2, 5):
            for word in product(range(3), repeat=m):
                orbit = context_orbit(transposition, word)
                fixed_count = sum(1 for value in word if value == fixed)
                expected = {
                    candidate
                    for candidate in product(range(3), repeat=m)
                    if sum(1 for value in candidate if value == fixed) == fixed_count
                }
                self.assertEqual(orbit, expected)

        for m in range(3, 5):
            self.assertEqual(
                len(context_orbit(three_cycle, tuple(0 for _ in range(m)))),
                3**m,
            )

        orbit_plus = context_orbit(three_cycle, (0, 1))
        self.assertEqual(orbit_plus, {(0, 1), (1, 2), (2, 0)})
        self.assertEqual(len(context_orbit(three_cycle, (0, 0))), 6)

    def test_shortest_invisible_pair_for_constant_action_three_cycle(self):
        sigma = (1, 2, 0)
        tau = (0, 1, 2)
        solution = permutation_form_solution(sigma, tau)

        self.assertEqual(flat_table(solution), (3, 6, 0, 4, 7, 1, 5, 8, 2))
        dsu, node = endpoint_t_classes(solution, 2)
        word = (0, 0)
        self.assertNotEqual(dsu.find(node(word, 0)), dsu.find(node(word, 1)))

        singleton = FiniteBraidedSet((0,), {(0, 0): (0, 0)})
        quotient_dsu, quotient_node = endpoint_t_classes(singleton, 2)
        self.assertEqual(
            quotient_dsu.find(quotient_node((0, 0), 0)),
            quotient_dsu.find(quotient_node((0, 0), 1)),
        )

        monoid = cyclic_monoid(1)
        rack_table = constant_action_rack(sigma)
        self.assertTrue(
            schema_satisfies_contextual_relations(
                solution, monoid, rack_table, lambda _p, x, _s: x
            )
        )
        presentation = build_context_presentation(
            solution,
            monoid,
            Endpoint(prefix=(), letter=0, suffix=(0,)),
            Endpoint(prefix=(0,), letter=0, suffix=()),
        )
        self.assertEqual(presentation.endpoint_class, presentation.endpoint_prime_class)

    def test_low_arity_target_positive_q2_detector_certificate(self):
        solution = permutation_form_solution((1, 2, 0), (0, 1, 2))
        monoid = five_element_prefix_suffix_monoid()
        rack_table = ((0, 1), (0, 1))

        self.assertEqual(flat_table(solution), (3, 6, 0, 4, 7, 1, 5, 8, 2))
        self.assertTrue(is_rack_table(rack_table))
        self.assertTrue(
            schema_satisfies_contextual_relations(
                solution, monoid, rack_table, low_arity_alpha
            )
        )

        presentation = build_context_presentation(
            solution,
            monoid,
            Endpoint(prefix=(), letter=0, suffix=(0,)),
            Endpoint(prefix=(0,), letter=0, suffix=()),
        )
        assignment = assignment_from_raw_alpha(presentation, monoid, low_arity_alpha)
        detector = RackDetector(q=2, table=rack_table, assignment=assignment)

        self.assertTrue(verify_detector(presentation, detector))
        self.assertEqual(assignment[presentation.endpoint_class], 0)
        self.assertEqual(assignment[presentation.endpoint_prime_class], 1)

    def test_finished_low_arity_table_common_monoid_and_racks(self):
        monoid = truncated_length_one_monoid()
        q2_identity = ((0, 1), (0, 1))
        q3_rack = ((0, 1, 2), (0, 1, 2), (1, 0, 2))

        self.assertTrue(is_rack_table(q2_identity))
        self.assertTrue(is_rack_table(q3_rack))

        for sigma in S3:
            for tau in S3:
                if compose(sigma, tau) != compose(tau, sigma):
                    continue
                with self.subTest(sigma=sigma, tau=tau):
                    for x in range(3):
                        for y in range(3):
                            xp = sigma[y]
                            yp = tau[x]
                            left = monoid.mul[monoid.gen[x]][monoid.gen[y]]
                            right = monoid.mul[monoid.gen[xp]][monoid.gen[yp]]
                            self.assertEqual(left, right)

    def test_finished_low_arity_table_sample_strong_collapse_witness(self):
        solution = permutation_form_solution((1, 2, 0), (0, 1, 2))
        dsu, node = endpoint_t_classes(solution, 3)

        A = ((0, 0, 0), 0)
        Aprime = ((0, 0, 2), 0)
        C = ((1, 0, 0), 0)
        Cprime = ((1, 0, 2), 0)
        B = ((0, 0, 0), 1)
        Bprime = ((0, 0, 2), 1)
        e = ((0, 0, 0), 0)
        eprime = ((0, 0, 0), 1)

        self.assertEqual(solution.R[(0, 0)], (1, 0))
        self.assertEqual(dsu.find(node(*A)), dsu.find(node(*Aprime)))
        self.assertEqual(dsu.find(node(*C)), dsu.find(node(*Cprime)))
        self.assertEqual(dsu.find(node(*B)), dsu.find(node(*eprime)))
        self.assertEqual(dsu.find(node(*Bprime)), dsu.find(node(*e)))


if __name__ == "__main__":
    unittest.main()
