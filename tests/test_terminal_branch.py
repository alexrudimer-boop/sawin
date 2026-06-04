import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    flip_disjoint_union_solution,
    identity_solution,
    one_state_invariant_observer_partition,
    rack_solution,
    subsolution_fibre_congruences,
    subsolution_fibre_transition_audit,
    subsolution_fibre_transport_isomorphism_audit,
    subsolution_fibre_transport_monodromy_audit,
    terminal_branch_triage_audit,
)


class TerminalBranchTriageTests(unittest.TestCase):
    def test_product_solution_has_point_separating_proper_quotients(self):
        elements = tuple(product((0, 1), repeat=2))
        solution = rack_solution(elements, lambda _left, right: right)

        audit = terminal_branch_triage_audit(solution)

        self.assertTrue(audit.has_nontrivial_proper_quotient)
        self.assertTrue(audit.has_point_separating_proper_quotients)
        self.assertTrue(audit.has_standard_entry_branch)

    def test_flip_across_union_reports_flip_partition(self):
        trivial = identity_solution(("a", "b"))
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)
        solution = flip_disjoint_union_solution(trivial, cyclic, "T", "C")

        audit = terminal_branch_triage_audit(solution)

        self.assertTrue(audit.has_flip_across_decomposition)
        self.assertEqual(len(audit.flip_across_partitions), 1)
        self.assertTrue(audit.has_subsolution_fibre_congruence)

    def test_identity_solution_has_one_state_invariant_observer(self):
        solution = identity_solution((0, 1))

        audit = terminal_branch_triage_audit(solution)

        self.assertTrue(audit.has_nontrivial_one_state_observer)
        self.assertEqual(
            one_state_invariant_observer_partition(solution),
            (frozenset([0]), frozenset([1])),
        )

    def test_connected_flip_rack_has_no_one_state_invariant_observer(self):
        solution = rack_solution((0, 1), lambda _left, right: right)

        audit = terminal_branch_triage_audit(solution)

        self.assertFalse(audit.has_nontrivial_one_state_observer)
        self.assertEqual(audit.observer_partition, (frozenset([0, 1]),))

    def test_subsolution_fibre_congruence_detects_block_partition(self):
        left = identity_solution(("a", "b"))
        right = identity_solution(("c", "d"))
        solution = flip_disjoint_union_solution(left, right, "L", "R")

        partitions = subsolution_fibre_congruences(solution)

        self.assertIn(
            (
                frozenset([("L", "a"), ("L", "b")]),
                frozenset([("R", "c"), ("R", "d")]),
            ),
            partitions,
        )

    def test_flip_across_mixed_fibre_transitions_are_swapped_product_like(self):
        left = identity_solution(("a", "b"))
        right = identity_solution(("c", "d"))
        solution = flip_disjoint_union_solution(left, right, "L", "R")
        partition = (
            frozenset([("L", "a"), ("L", "b")]),
            frozenset([("R", "c"), ("R", "d")]),
        )

        audit = subsolution_fibre_transition_audit(solution, partition)

        self.assertTrue(audit.all_mixed_transitions_product_like)
        self.assertTrue(audit.all_mixed_transitions_swapped_product_like)
        self.assertFalse(audit.all_mixed_transitions_direct_product_like)

        transport = subsolution_fibre_transport_isomorphism_audit(solution, partition)

        self.assertTrue(transport.all_mixed_rows_product_like)
        self.assertTrue(transport.all_product_like_rows_have_transport_isomorphisms)

        monodromy = subsolution_fibre_transport_monodromy_audit(solution, partition)

        self.assertTrue(monodromy.all_rows_transport_isomorphic)
        self.assertTrue(monodromy.all_loop_groups_trivial)

    def test_transport_isomorphic_rows_can_have_nontrivial_loop_monodromy(self):
        elements = tuple(product((0, 1), (0, 1, 2)))
        table = {}
        for left_color, left_point in elements:
            for right_color, right_point in elements:
                table[((left_color, left_point), (right_color, right_point))] = (
                    (left_color, right_point),
                    (right_color, (left_point + 1) % 3),
                )
        solution = FiniteBraidedSet(elements, table)
        partition = (
            frozenset((0, point) for point in (0, 1, 2)),
            frozenset((1, point) for point in (0, 1, 2)),
        )

        self.assertTrue(solution.is_ybe())

        transport = subsolution_fibre_transport_isomorphism_audit(solution, partition)
        self.assertTrue(transport.all_mixed_rows_product_like)
        self.assertTrue(transport.all_product_like_rows_have_transport_isomorphisms)

        monodromy = subsolution_fibre_transport_monodromy_audit(solution, partition)
        self.assertTrue(monodromy.all_rows_transport_isomorphic)
        self.assertFalse(monodromy.all_loop_groups_trivial)
        self.assertEqual(
            tuple(row.loop_group_order for row in monodromy.rows),
            (3, 3),
        )


if __name__ == "__main__":
    unittest.main()
