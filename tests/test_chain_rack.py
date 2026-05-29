import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    assemble_congruence_chain_rack,
    cyclic_group,
    identity_solution,
    is_rack_solution,
    rack_solution,
)


class CongruenceChainRackTests(unittest.TestCase):
    def test_empty_detector_chain_returns_terminal_rack(self):
        terminal = rack_solution(["*"], lambda _left, right: right)

        assembly = assemble_congruence_chain_rack(terminal, ())

        self.assertIs(assembly.rack, terminal)
        self.assertEqual(assembly.terminal_rack_size, 1)
        self.assertEqual(assembly.detector_group_orders, ())
        self.assertEqual(assembly.steps, ())
        self.assertEqual(assembly.final_rack_size, 1)
        self.assertEqual(assembly.expected_final_rack_size, 1)
        self.assertTrue(assembly.size_formula_holds)

    def test_chain_records_exact_sharp_factor_sizes(self):
        terminal = rack_solution(["top"], lambda _left, right: right)

        assembly = assemble_congruence_chain_rack(
            terminal,
            (cyclic_group(2), cyclic_group(3)),
            first_interval_index=4,
        )

        self.assertEqual(assembly.detector_group_orders, (2, 3))
        self.assertEqual(assembly.final_rack_size, 1 * 8 * 18)
        self.assertEqual(assembly.expected_final_rack_size, 1 * 8 * 18)
        self.assertTrue(assembly.size_formula_holds)
        self.assertTrue(is_rack_solution(assembly.rack))

        first, second = assembly.steps
        self.assertEqual(first.interval_index, 4)
        self.assertEqual(first.input_rack_size, 1)
        self.assertEqual(first.detector_group_order, 2)
        self.assertEqual(first.detector_rack_size, 8)
        self.assertEqual(first.output_rack_size, 8)
        self.assertTrue(first.size_formula_holds)

        self.assertEqual(second.interval_index, 5)
        self.assertEqual(second.input_rack_size, 8)
        self.assertEqual(second.detector_group_order, 3)
        self.assertEqual(second.detector_rack_size, 18)
        self.assertEqual(second.output_rack_size, 144)
        self.assertTrue(second.size_formula_holds)

    def test_small_assembled_rack_is_ybe(self):
        terminal = rack_solution(["top"], lambda _left, right: right)

        assembly = assemble_congruence_chain_rack(
            terminal,
            (cyclic_group(2), cyclic_group(1)),
        )

        self.assertEqual(assembly.final_rack_size, 16)
        self.assertTrue(assembly.rack.is_ybe())

    def test_terminal_detector_must_be_a_rack_even_for_empty_chain(self):
        with self.assertRaises(ValueError):
            assemble_congruence_chain_rack(identity_solution([0, 1]), ())


if __name__ == "__main__":
    unittest.main()
