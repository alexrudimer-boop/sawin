import sys
import unittest
from itertools import product
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteBraidedSet,
    InvariantTransducer,
    MealyTransducer,
    all_length_injectivity_witness,
    combined_transducer_output,
    identity_solution,
    rack_solution,
    transducer_rackification_audit,
)


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


def affine_type_a_transducers(solution):
    states = (("start", 0), ("seen", 0), ("seen", 1))
    rack_delta = {}
    rack_omega = {}
    inv_delta = {}
    inv_nu = {}
    for state in states:
        for letter in solution.elements:
            a, b = letter
            parity = (a + b) % 2
            kind, offset = state
            if kind == "start":
                current_offset = 0
                next_state = ("seen", 0)
            else:
                current_offset = (offset + parity + 1) % 2
                next_state = ("seen", current_offset)
            rack_delta[(state, letter)] = next_state
            rack_omega[(state, letter)] = (a + current_offset) % 2
            inv_delta[(state, letter)] = state
            inv_nu[(state, letter)] = parity
    return (MealyTransducer(states, ("start", 0), rack_delta, rack_omega),
            InvariantTransducer(states, ("start", 0), inv_delta, inv_nu))


def affine_f2_hidden_cyclic_solution():
    elements = tuple(product((0, 1), repeat=3))
    table = {}
    for a, z1, z2 in elements:
        for b, w1, w2 in elements:
            table[((a, z1, z2), (b, w1, w2))] = (
                (a, w2, w1),
                (b, (z2 + 1) % 2, (z1 + 1) % 2),
            )
    return FiniteBraidedSet(elements, table)


def affine_f2_hidden_cyclic_transducers(solution):
    states = (0, 1)
    rack_delta = {}
    rack_omega = {}
    inv_delta = {}
    inv_nu = {}
    for state in states:
        for letter in solution.elements:
            a, z1, z2 = letter
            rack_delta[(state, letter)] = 1 - state
            if state == 0:
                rack_omega[(state, letter)] = (z1, z2)
            else:
                rack_omega[(state, letter)] = ((z2 + 1) % 2, (z1 + 1) % 2)
            inv_delta[(state, letter)] = state
            inv_nu[(state, letter)] = a
    return (MealyTransducer(states, 0, rack_delta, rack_omega),
            InvariantTransducer(states, 0, inv_delta, inv_nu))


class TransducerCertificateTests(unittest.TestCase):
    def test_affine_type_a_has_finite_transducer_certificate(self):
        solution = affine_f2_type_a_solution()
        quotient = identity_solution(("z",))
        quotient_map = {element: "z" for element in solution.elements}
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)
        rack_transducer, invariant_transducer = affine_type_a_transducers(solution)

        audit = transducer_rackification_audit(
            solution,
            quotient,
            quotient_map,
            cyclic,
            rack_transducer,
            invariant_transducer,
        )

        self.assertTrue(audit.finite_conditions_hold)

    def test_affine_type_a_combined_outputs_are_parity_and_cyclic_coordinate(self):
        solution = affine_f2_type_a_solution()
        quotient_map = {element: "z" for element in solution.elements}
        rack_transducer, invariant_transducer = affine_type_a_transducers(solution)
        word = ((0, 1), (1, 1), (0, 0), (1, 0))

        quotient_word, parities, cyclic_coordinates = combined_transducer_output(
            word, quotient_map, rack_transducer, invariant_transducer
        )

        self.assertEqual(quotient_word, ("z", "z", "z", "z"))
        self.assertEqual(parities, (1, 0, 0, 1))
        self.assertEqual(cyclic_coordinates, (0, 0, 0, 1))

    def test_affine_type_a_needs_the_invariant_output_for_injectivity(self):
        solution = affine_f2_type_a_solution()
        quotient_map = {element: "z" for element in solution.elements}
        rack_transducer, _invariant_transducer = affine_type_a_transducers(solution)

        witness = all_length_injectivity_witness(
            solution, quotient_map, rack_transducer
        )

        self.assertIsNotNone(witness)
        self.assertNotEqual(witness.left_word, witness.right_word)

    def test_bad_rack_output_fails_local_equivariance(self):
        solution = affine_f2_type_a_solution()
        quotient = identity_solution(("z",))
        quotient_map = {element: "z" for element in solution.elements}
        cyclic = rack_solution((0, 1), lambda _left, right: 1 - right)
        rack_transducer, invariant_transducer = affine_type_a_transducers(solution)
        bad_omega = {key: key[1][0] for key in rack_transducer.omega}
        bad_rack_transducer = MealyTransducer(
            rack_transducer.states,
            rack_transducer.initial,
            rack_transducer.delta,
            bad_omega,
        )

        audit = transducer_rackification_audit(
            solution,
            quotient,
            quotient_map,
            cyclic,
            bad_rack_transducer,
            invariant_transducer,
        )

        self.assertFalse(audit.finite_conditions_hold)
        self.assertTrue(audit.rack_failures)

    def test_affine_f2_hidden_cyclic_gauge_has_sequential_certificate(self):
        solution = affine_f2_hidden_cyclic_solution()
        quotient = identity_solution(("z",))
        quotient_map = {element: "z" for element in solution.elements}
        fibre = tuple(product((0, 1), repeat=2))
        constant_action = rack_solution(
            fibre,
            lambda _left, right: ((right[0] + 1) % 2, (right[1] + 1) % 2),
        )
        rack_transducer, invariant_transducer = (
            affine_f2_hidden_cyclic_transducers(solution)
        )

        audit = transducer_rackification_audit(
            solution,
            quotient,
            quotient_map,
            constant_action,
            rack_transducer,
            invariant_transducer,
        )

        self.assertTrue(audit.finite_conditions_hold)


if __name__ == "__main__":
    unittest.main()
