import sys
import unittest
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
from ybe_domination.small_search import all_bijection_solutions


def solution_from_flat_table(table):
    pairs = [(x, y) for x in range(3) for y in range(3)]
    values = [divmod(value, 3) for value in table]
    return FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, values)))


def universal_length_one_monoid():
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


class NonPerm3Arity2EndpointGateTests(unittest.TestCase):
    def test_size_three_ybe_and_nonpermutation_counts(self):
        solutions = list(all_bijection_solutions(3))

        self.assertEqual(len(solutions), 73)
        self.assertEqual(sum(1 for solution in solutions if is_permutation_form(solution)), 18)
        self.assertEqual(sum(1 for solution in solutions if not is_permutation_form(solution)), 55)

    def test_universal_length_one_monoid_satisfies_all_size_three_structure_relations(self):
        monoid = universal_length_one_monoid()

        for solution in all_bijection_solutions(3):
            for x in range(3):
                for y in range(3):
                    xp, yp = solution.R[(x, y)]
                    left = monoid.mul[monoid.gen[x]][monoid.gen[y]]
                    right = monoid.mul[monoid.gen[xp]][monoid.gen[yp]]
                    self.assertEqual(left, right)

    def test_sample_nonpermutation_detector_certificate(self):
        solution = solution_from_flat_table((0, 1, 6, 3, 4, 7, 2, 5, 8))
        monoid = universal_length_one_monoid()
        rack_table = ((0, 1), (0, 1))
        support = {(0, 2, 1), (1, 2, 0)}

        def alpha(p, x, s):
            return 1 if (p, x, s) in support else 0

        self.assertTrue(solution.is_ybe())
        self.assertFalse(is_permutation_form(solution))
        self.assertTrue(is_rack_table(rack_table))

        presentation = build_context_presentation(
            solution,
            monoid,
            Endpoint(prefix=(), letter=0, suffix=(2,)),
            Endpoint(prefix=(0,), letter=2, suffix=()),
        )
        assignment = assignment_from_raw_alpha(presentation, monoid, alpha)
        detector = RackDetector(q=2, table=rack_table, assignment=assignment)

        self.assertTrue(verify_detector(presentation, detector))
        self.assertEqual(assignment[presentation.endpoint_class], 0)
        self.assertEqual(assignment[presentation.endpoint_prime_class], 1)


if __name__ == "__main__":
    unittest.main()
