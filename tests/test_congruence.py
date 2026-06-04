import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    CongruenceInterval,
    FiniteBraidedSet,
    congruences,
    equality_congruence,
    interval_covers,
    is_congruence,
    maximal_congruence_chain,
    quotient_factor_compression_audit,
    quotient_solution,
    rack_solution,
    universal_congruence,
)


class CongruenceTests(unittest.TestCase):
    def test_flip_solution_has_extreme_congruences(self):
        solution = rack_solution([0, 1], lambda a, b: b)
        lattice = congruences(solution)
        self.assertIn(equality_congruence(solution.elements), lattice)
        self.assertIn(universal_congruence(solution.elements), lattice)

    def test_noncongruence_partition_rejected(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        bad = (frozenset([0, 1]), frozenset([2]))
        self.assertFalse(is_congruence(solution, bad))

    def test_quotient_solution_is_ybe_and_homomorphism(self):
        elements = ((0, "a"), (0, "b"), (1, "a"), (1, "b"))
        solution = rack_solution(elements, lambda a, b: b)
        partition = (
            frozenset([(0, "a"), (0, "b")]),
            frozenset([(1, "a"), (1, "b")]),
        )
        qmap = quotient_solution(solution, partition)
        self.assertTrue(qmap.quotient.is_ybe())
        qmap.validate_homomorphism()

    def test_interval_local_table_from_cover(self):
        elements = ((0, "a"), (0, "b"), (1, "a"), (1, "b"))
        solution = rack_solution(elements, lambda a, b: b)
        lower = equality_congruence(solution.elements)
        upper = (
            frozenset([(0, "a"), (0, "b")]),
            frozenset([(1, "a"), (1, "b")]),
        )
        interval = CongruenceInterval(solution, lower, upper).local_interval()
        self.assertTrue(interval.is_colored_ybe())

    def test_cover_interval_is_local_minimal_in_local_table(self):
        solution = rack_solution([0, 1, 2], lambda a, b: b)
        lattice = congruences(solution)
        lower, upper = interval_covers(lattice)[0]
        interval = CongruenceInterval(solution, lower, upper).local_interval()
        self.assertTrue(interval.is_local_minimal())

    def test_cover_interval_with_block_fibre_points_is_local_minimal(self):
        elements = tuple((a, b) for a in range(2) for b in range(2))
        table = {
            (x, y): ((x[0], y[1]), (y[0], x[1]))
            for x in elements
            for y in elements
        }
        solution = FiniteBraidedSet(elements, table)
        for lower, upper in interval_covers(congruences(solution, max_size=4)):
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            self.assertTrue(interval.is_local_minimal(max_fibre_size=4))

    def test_maximal_chain_reaches_universal(self):
        solution = rack_solution([0, 1], lambda a, b: b)
        chain = maximal_congruence_chain(solution)
        self.assertEqual(chain[0], equality_congruence(solution.elements))
        self.assertEqual(chain[-1], universal_congruence(solution.elements))
        covers = interval_covers(congruences(solution))
        self.assertTrue(all((a, b) in covers for a, b in zip(chain, chain[1:])))

    def test_point_separating_quotients_give_proper_active_factor_certificate(self):
        elements = tuple((a, b) for a in range(2) for b in range(2))
        solution = rack_solution(elements, lambda _left, right: right)
        first_coordinate = (
            frozenset([(0, 0), (0, 1)]),
            frozenset([(1, 0), (1, 1)]),
        )
        second_coordinate = (
            frozenset([(0, 0), (1, 0)]),
            frozenset([(0, 1), (1, 1)]),
        )

        audit = quotient_factor_compression_audit(
            solution,
            (first_coordinate, second_coordinate),
        )

        self.assertTrue(audit.proves_proper_quotient_compression)
        self.assertEqual(audit.quotient_sizes, (2, 2))
        self.assertIsNone(audit.injectivity_witness)

    def test_nonseparating_quotient_family_has_injectivity_witness(self):
        elements = tuple((a, b) for a in range(2) for b in range(2))
        solution = rack_solution(elements, lambda _left, right: right)
        first_coordinate = (
            frozenset([(0, 0), (0, 1)]),
            frozenset([(1, 0), (1, 1)]),
        )

        audit = quotient_factor_compression_audit(solution, (first_coordinate,))

        self.assertFalse(audit.proves_proper_quotient_compression)
        self.assertFalse(audit.point_reconstruction_holds)
        self.assertIsNotNone(audit.injectivity_witness)

    def test_noncongruence_quotient_family_is_rejected(self):
        solution = rack_solution([0, 1, 2], lambda a, b: (2 * a - b) % 3)
        bad = (frozenset([0, 1]), frozenset([2]))

        audit = quotient_factor_compression_audit(solution, (bad,))

        self.assertFalse(audit.all_partitions_are_congruences)
        self.assertIsNone(audit.certificate)


if __name__ == "__main__":
    unittest.main()
