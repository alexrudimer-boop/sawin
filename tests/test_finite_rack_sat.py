import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination.finite_braided_set import FiniteBraidedSet
from ybe_domination.finite_rack_sat import (
    Endpoint,
    build_context_presentation,
    find_rack_detector,
    is_rack_table,
    q2_fast_detector,
    trivial_monoid,
    verify_detector,
)
from ybe_domination.small_search import all_bijection_solutions


SIZE_TWO_TABLES = [
    (0, 1, 2, 3),
    (0, 2, 1, 3),
    (1, 3, 0, 2),
    (2, 0, 3, 1),
    (3, 1, 2, 0),
]


def constant_action_flip_solution() -> FiniteBraidedSet:
    return FiniteBraidedSet(
        (0, 1),
        {(i, j): (1 - j, i) for i in (0, 1) for j in (0, 1)},
    )


def solution_from_flat_table(table):
    pairs = [(0, 0), (0, 1), (1, 0), (1, 1)]
    values = [divmod(value, 2) for value in table]
    return FiniteBraidedSet((0, 1), dict(zip(pairs, values)))


def apply_generator(solution, word, index):
    left, right = solution.R[(word[index], word[index + 1])]
    return word[:index] + (left, right) + word[index + 2 :]


def xor_monoid():
    from ybe_domination.finite_rack_sat import MonoidQuotient

    return MonoidQuotient(
        size=2,
        identity=0,
        mul=((0, 1), (1, 0)),
        gen=(1, 1),
    )


def m4_monoid():
    from ybe_domination.finite_rack_sat import MonoidQuotient

    return MonoidQuotient(
        size=4,
        identity=0,
        mul=(
            (0, 1, 2, 3),
            (1, 1, 1, 1),
            (2, 1, 1, 1),
            (3, 1, 1, 1),
        ),
        gen=(2, 3),
    )


def schema_satisfies_contextual_relations(solution, monoid, table, alpha):
    for p in range(monoid.size):
        for s in range(monoid.size):
            for x in (0, 1):
                for y in (0, 1):
                    xp, yp = solution.R[(x, y)]
                    left_t = alpha(p, x, monoid.mul[monoid.gen[y]][s])
                    right_t = alpha(monoid.mul[p][monoid.gen[xp]], yp, s)
                    if left_t != right_t:
                        return False
                    first = alpha(p, x, monoid.mul[monoid.gen[y]][s])
                    second = alpha(monoid.mul[p][monoid.gen[x]], y, s)
                    out = alpha(p, xp, monoid.mul[monoid.gen[yp]][s])
                    if table[first][second] != out:
                        return False
    return True


class FiniteRackSatTests(unittest.TestCase):
    def test_two_element_constant_action_detector(self):
        solution = constant_action_flip_solution()
        self.assertTrue(solution.is_ybe())
        monoid = trivial_monoid(generator_count=2)
        presentation = build_context_presentation(
            solution,
            monoid,
            Endpoint(prefix=(), letter=0, suffix=()),
            Endpoint(prefix=(), letter=1, suffix=()),
        )

        detector = find_rack_detector(presentation, qmax=2)

        self.assertIsNotNone(detector)
        assert detector is not None
        self.assertTrue(verify_detector(presentation, detector))
        self.assertNotEqual(
            detector.assignment[presentation.endpoint_class],
            detector.assignment[presentation.endpoint_prime_class],
        )
        self.assertEqual(detector.table, ((1, 0), (1, 0)))

    def test_two_element_flip_solution_identity_detector(self):
        solution = FiniteBraidedSet(
            (0, 1),
            {(i, j): (j, i) for i in (0, 1) for j in (0, 1)},
        )
        self.assertTrue(solution.is_ybe())
        presentation = build_context_presentation(
            solution,
            trivial_monoid(generator_count=2),
            Endpoint(prefix=(), letter=0, suffix=()),
            Endpoint(prefix=(), letter=1, suffix=()),
        )

        detector = q2_fast_detector(presentation)

        self.assertIsNotNone(detector)
        assert detector is not None
        self.assertTrue(verify_detector(presentation, detector))
        self.assertEqual(detector.table, ((0, 1), (0, 1)))

    def test_rack_table_axioms_allow_non_idempotent_racks(self):
        self.assertTrue(is_rack_table(((1, 0), (1, 0))))
        self.assertFalse(is_rack_table(((0, 0), (1, 1))))

    def test_size_two_ybe_smoke_count(self):
        self.assertEqual(sum(1 for _ in all_bijection_solutions(2)), 5)

    def test_size_two_labelled_ybe_classification(self):
        actual = []
        for solution in all_bijection_solutions(2):
            actual.append(
                tuple(2 * solution.R[pair][0] + solution.R[pair][1] for pair in [(0, 0), (0, 1), (1, 0), (1, 1)])
            )
        self.assertEqual(actual, SIZE_TWO_TABLES)

    def test_x2_is_braid_conjugate_to_constant_action_rack(self):
        x2 = solution_from_flat_table((1, 3, 0, 2))
        q2 = constant_action_flip_solution()

        def F(word):
            return tuple(value ^ (1 if index % 2 == 0 else 0) for index, value in enumerate(word))

        for n in range(2, 7):
            for word_index in range(2**n):
                word = tuple((word_index >> shift) & 1 for shift in range(n))
                for index in range(n - 1):
                    left = F(apply_generator(q2, F(word), index))
                    right = apply_generator(x2, word, index)
                    self.assertEqual(left, right)

    def test_size_two_unbounded_q2_detector_schemas_are_valid(self):
        q_id = ((0, 1), (0, 1))
        q_flip = ((1, 0), (1, 0))
        m1 = trivial_monoid(2)
        m2 = xor_monoid()
        m4 = m4_monoid()
        e = 0
        a0 = 2
        a1 = 3

        schemas = [
            ((0, 2, 1, 3), m1, q_id, lambda p, x, s: x),
            (
                (1, 3, 0, 2),
                m4,
                q_id,
                lambda p, x, s: 1
                if (p, x, s) in {(e, 0, a1), (e, 1, a0), (a0, 0, e), (a1, 1, e)}
                else 0,
            ),
            ((1, 3, 0, 2), m2, q_flip, lambda p, x, s: x ^ p),
            (
                (1, 3, 0, 2),
                m4,
                q_id,
                lambda p, x, s: 1
                if (p, x, s) in {(e, 0, a0), (e, 1, a1), (a0, 1, e), (a1, 0, e)}
                else 0,
            ),
            (
                (2, 0, 3, 1),
                m4,
                q_id,
                lambda p, x, s: 1
                if (p, x, s) in {(e, 0, a1), (e, 1, a0), (a0, 0, e), (a1, 1, e)}
                else 0,
            ),
            ((2, 0, 3, 1), m1, q_flip, lambda p, x, s: x),
            (
                (2, 0, 3, 1),
                m4,
                q_id,
                lambda p, x, s: 1
                if (p, x, s) in {(e, 0, a0), (e, 1, a1), (a0, 1, e), (a1, 0, e)}
                else 0,
            ),
            (
                (3, 1, 2, 0),
                m2,
                q_id,
                lambda p, x, s: 1 if (p, x, s) in {(0, 1, 1), (1, 0, 0)} else 0,
            ),
            (
                (3, 1, 2, 0),
                m2,
                q_id,
                lambda p, x, s: 1 if (p, x, s) in {(0, 1, 0), (1, 0, 1)} else 0,
            ),
        ]

        for flat_table, monoid, rack_table, alpha in schemas:
            with self.subTest(flat_table=flat_table, rack_table=rack_table):
                self.assertTrue(
                    schema_satisfies_contextual_relations(
                        solution_from_flat_table(flat_table),
                        monoid,
                        rack_table,
                        alpha,
                    )
                )


if __name__ == "__main__":
    unittest.main()
