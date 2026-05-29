import sys
import unittest
from dataclasses import dataclass
from pathlib import Path
from typing import Tuple

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from ybe_domination import (
    FiniteGroup,
    assemble_closed_local_detector_chain_rack,
    assemble_congruence_chain_rack,
    closed_local_detector_chain,
    cyclic_group,
    identity_solution,
    is_rack_solution,
    rack_solution,
)


@dataclass(frozen=True)
class FakeLocalSummary:
    verdict: str
    closed_detector_product_group: FiniteGroup | None
    closed_detector_gaps: Tuple[str, ...]
    remaining_obligation: str = "test obligation"


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

    def test_closed_local_detector_chain_collects_one_group_per_interval(self):
        summaries = (
            FakeLocalSummary("product_finite_g_branch", cyclic_group(2), ()),
            FakeLocalSummary("known_total_branch", cyclic_group(3), ()),
        )

        chain = closed_local_detector_chain(summaries, first_interval_index=4)

        self.assertTrue(chain.is_complete)
        self.assertEqual(chain.first_interval_index, 4)
        self.assertEqual(chain.verdicts, ("product_finite_g_branch", "known_total_branch"))
        self.assertEqual(chain.detector_group_orders, (2, 3))
        self.assertEqual(chain.gap_rows, ())

    def test_closed_local_summary_assembly_refuses_open_and_gap_rows(self):
        summaries = (
            FakeLocalSummary(
                "bi_free_universal_corridor_bottleneck",
                None,
                (),
                "prove corridor theorem",
            ),
            FakeLocalSummary(
                "product_finite_g_branch",
                None,
                ("direct_fibre2_affine",),
                "delegated affine detector",
            ),
        )

        chain = closed_local_detector_chain(summaries, first_interval_index=7)

        self.assertFalse(chain.is_complete)
        self.assertEqual(chain.detector_group_orders, ())
        first_gap, second_gap = chain.gap_rows
        self.assertEqual(first_gap.interval_index, 7)
        self.assertTrue(first_gap.is_open_verdict)
        self.assertEqual(first_gap.gaps, ())
        self.assertEqual(second_gap.interval_index, 8)
        self.assertFalse(second_gap.is_open_verdict)
        self.assertTrue(second_gap.has_detector_gap)
        self.assertEqual(second_gap.gaps, ("direct_fibre2_affine",))

        terminal = rack_solution(["top"], lambda _left, right: right)
        with self.assertRaisesRegex(ValueError, "interval 7"):
            assemble_closed_local_detector_chain_rack(
                terminal,
                summaries,
                first_interval_index=7,
            )

    def test_closed_local_summary_assembly_uses_product_groups(self):
        terminal = rack_solution(["top"], lambda _left, right: right)
        summaries = (
            FakeLocalSummary("product_finite_g_branch", cyclic_group(2), ()),
            FakeLocalSummary("locally_nondegenerate_branch", cyclic_group(1), ()),
        )

        assembly = assemble_closed_local_detector_chain_rack(
            terminal,
            summaries,
            first_interval_index=12,
        )

        self.assertEqual(assembly.detector_group_orders, (2, 1))
        self.assertEqual(assembly.final_rack_size, 1 * 8 * 2)
        self.assertTrue(assembly.size_formula_holds)
        self.assertEqual(tuple(step.interval_index for step in assembly.steps), (12, 13))


if __name__ == "__main__":
    unittest.main()
