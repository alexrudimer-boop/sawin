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


def constant_action_flip_solution() -> FiniteBraidedSet:
    return FiniteBraidedSet(
        (0, 1),
        {(i, j): (1 - j, i) for i in (0, 1) for j in (0, 1)},
    )


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


if __name__ == "__main__":
    unittest.main()
