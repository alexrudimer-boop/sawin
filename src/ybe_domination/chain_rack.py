from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, Tuple

from .artin_longitudes import sharp_obstruction_rack
from .finite_braided_set import FiniteBraidedSet, is_rack_solution
from .finite_group import FiniteGroup


@dataclass(frozen=True)
class CongruenceChainRackStep:
    """One sharp-obstruction step ``Q_i = Q_{i+1} x A_{G_i}``."""

    interval_index: int
    input_rack_size: int
    detector_group_order: int
    detector_rack_size: int
    output_rack_size: int

    @property
    def expected_output_rack_size(self) -> int:
        return self.input_rack_size * self.detector_rack_size

    @property
    def size_formula_holds(self) -> bool:
        return self.output_rack_size == self.expected_output_rack_size


@dataclass(frozen=True)
class CongruenceChainRackAssembly:
    """Executable audit of the finite rack produced by a detector chain."""

    terminal_rack_size: int
    detector_group_orders: Tuple[int, ...]
    steps: Tuple[CongruenceChainRackStep, ...]
    rack: FiniteBraidedSet

    @property
    def final_rack_size(self) -> int:
        return len(self.rack.elements)

    @property
    def expected_final_rack_size(self) -> int:
        size = self.terminal_rack_size
        for group_order in self.detector_group_orders:
            size *= 2 * group_order * group_order
        return size

    @property
    def size_formula_holds(self) -> bool:
        return (
            self.final_rack_size == self.expected_final_rack_size
            and all(step.size_formula_holds for step in self.steps)
        )


def assemble_congruence_chain_rack(
    terminal_rack: FiniteBraidedSet,
    detector_groups: Sequence[FiniteGroup],
    *,
    first_interval_index: int = 0,
) -> CongruenceChainRackAssembly:
    """Return the finite rack obtained by iterating the sharp obstruction step.

    The detector groups are supplied in the order in which the induction
    descends from the terminal quotient rack toward the original solution.  At
    each step this constructs exactly ``Q_i = Q_{i+1} x A_{G_i}``, where
    ``A_G`` is the fixed Artin-longitude detector rack.  The groups are fixed
    finite objects; no braid degree ``n`` is an input to this construction.
    """

    if not is_rack_solution(terminal_rack):
        raise ValueError("terminal detector must be a finite rack")

    groups = tuple(detector_groups)
    current = terminal_rack
    steps = []
    for offset, group in enumerate(groups):
        input_rack_size = len(current.elements)
        detector_group_order = len(group.elements)
        detector_rack_size = 2 * detector_group_order * detector_group_order
        current = sharp_obstruction_rack(current, group)
        steps.append(
            CongruenceChainRackStep(
                interval_index=first_interval_index + offset,
                input_rack_size=input_rack_size,
                detector_group_order=detector_group_order,
                detector_rack_size=detector_rack_size,
                output_rack_size=len(current.elements),
            )
        )

    return CongruenceChainRackAssembly(
        terminal_rack_size=len(terminal_rack.elements),
        detector_group_orders=tuple(len(group.elements) for group in groups),
        steps=tuple(steps),
        rack=current,
    )
