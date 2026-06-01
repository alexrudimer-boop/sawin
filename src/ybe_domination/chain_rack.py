from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol, Sequence, Tuple

from .artin_longitudes import sharp_obstruction_rack
from .finite_braided_set import FiniteBraidedSet, is_rack_solution
from .finite_group import FiniteGroup

CLOSED_LOCAL_DETECTOR_VERDICTS = frozenset(
    {
        "product_finite_g_branch",
        "known_total_branch",
        "locally_nondegenerate_branch",
        "closed_by_triangular_recovery_endpoint_witness",
        "closed_by_triangular_recovery_symmetric_endpoint_fork",
        "closed_by_universal_continuation_endpoint_witness",
        "closed_by_universal_continuation_symmetric_endpoint_fork",
        "closed_by_mixed_unit_context_endpoint_witness",
        "closed_by_mixed_unit_symmetric_endpoint_fork",
        "closed_by_routed_endpoint_witnesses",
        "closed_by_routed_endpoint_certificates",
    }
)


class ClosedLocalDetectorSummary(Protocol):
    """Protocol for local summaries that expose closed detector data."""

    verdict: str
    remaining_obligation: str

    @property
    def closed_detector_product_group(self) -> FiniteGroup | None:
        ...

    @property
    def closed_detector_gaps(self) -> Tuple[str, ...]:
        ...


@dataclass(frozen=True)
class ClosedLocalDetectorGap:
    """One local interval that cannot yet supply a fixed finite detector."""

    interval_index: int
    verdict: str
    gaps: Tuple[str, ...]
    remaining_obligation: str

    @property
    def is_open_verdict(self) -> bool:
        return self.verdict not in CLOSED_LOCAL_DETECTOR_VERDICTS

    @property
    def has_detector_gap(self) -> bool:
        return bool(self.gaps)


@dataclass(frozen=True)
class ClosedLocalDetectorChain:
    """Flatten closed local summaries into one fixed detector group per interval."""

    first_interval_index: int
    verdicts: Tuple[str, ...]
    detector_groups: Tuple[FiniteGroup, ...]
    gap_rows: Tuple[ClosedLocalDetectorGap, ...]

    @property
    def detector_group_orders(self) -> Tuple[int, ...]:
        return tuple(len(group.elements) for group in self.detector_groups)

    @property
    def is_complete(self) -> bool:
        return not self.gap_rows

    def require_complete(self) -> Tuple[FiniteGroup, ...]:
        if self.is_complete:
            return self.detector_groups
        details = "; ".join(
            f"interval {row.interval_index}: {row.verdict} gaps={row.gaps or ('open',)}"
            for row in self.gap_rows
        )
        raise ValueError(
            "not every local interval has an explicit fixed detector group: "
            f"{details}"
        )


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


def closed_local_detector_chain(
    summaries: Sequence[ClosedLocalDetectorSummary],
    *,
    first_interval_index: int = 0,
) -> ClosedLocalDetectorChain:
    """Collect one fixed finite detector group from each closed local summary."""

    detector_groups = []
    gap_rows = []
    verdicts = []
    for offset, summary in enumerate(tuple(summaries)):
        interval_index = first_interval_index + offset
        verdicts.append(summary.verdict)
        gaps = tuple(summary.closed_detector_gaps)
        group = summary.closed_detector_product_group
        if summary.verdict not in CLOSED_LOCAL_DETECTOR_VERDICTS:
            gap_rows.append(
                ClosedLocalDetectorGap(
                    interval_index=interval_index,
                    verdict=summary.verdict,
                    gaps=gaps,
                    remaining_obligation=summary.remaining_obligation,
                )
            )
            continue
        if gaps:
            gap_rows.append(
                ClosedLocalDetectorGap(
                    interval_index=interval_index,
                    verdict=summary.verdict,
                    gaps=gaps,
                    remaining_obligation=summary.remaining_obligation,
                )
            )
            continue
        if group is None:
            gap_rows.append(
                ClosedLocalDetectorGap(
                    interval_index=interval_index,
                    verdict=summary.verdict,
                    gaps=gaps or ("missing_closed_detector_group",),
                    remaining_obligation=summary.remaining_obligation,
                )
            )
            continue
        detector_groups.append(group)
    return ClosedLocalDetectorChain(
        first_interval_index=first_interval_index,
        verdicts=tuple(verdicts),
        detector_groups=tuple(detector_groups),
        gap_rows=tuple(gap_rows),
    )


def assemble_closed_local_detector_chain_rack(
    terminal_rack: FiniteBraidedSet,
    summaries: Sequence[ClosedLocalDetectorSummary],
    *,
    first_interval_index: int = 0,
) -> CongruenceChainRackAssembly:
    """Assemble the congruence-chain rack from closed local summary rows.

    Each local summary contributes one interval-level group ``G_i``.  If a row
    is open or has a delegated detector gap, the function refuses to assemble
    a rack rather than hiding a missing master-local proof step.
    """

    chain = closed_local_detector_chain(
        summaries,
        first_interval_index=first_interval_index,
    )
    return assemble_congruence_chain_rack(
        terminal_rack,
        chain.require_complete(),
        first_interval_index=first_interval_index,
    )
