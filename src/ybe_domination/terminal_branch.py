from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import FrozenSet, Tuple

from .congruence import (
    Partition,
    common_refinement,
    congruences,
    equality_congruence,
    generated_partition,
    universal_congruence,
)
from .finite_braided_set import Element, FiniteBraidedSet, is_subsolution_subset


@dataclass(frozen=True)
class FlipAcrossPartition:
    left: FrozenSet[Element]
    right: FrozenSet[Element]


@dataclass(frozen=True)
class TerminalBranchTriageAudit:
    """Finite audit for standard entry branches into proper compression."""

    solution: FiniteBraidedSet
    proper_congruences: Tuple[Partition, ...]
    subsolution_fibre_congruences: Tuple[Partition, ...]
    quotient_common_refinement: Partition
    proper_subsolutions: Tuple[FrozenSet[Element], ...]
    flip_across_partitions: Tuple[FlipAcrossPartition, ...]
    observer_partition: Partition

    @property
    def has_nontrivial_proper_quotient(self) -> bool:
        return any(
            1 < len(partition) < len(self.solution.elements)
            for partition in self.proper_congruences
        )

    @property
    def has_point_separating_proper_quotients(self) -> bool:
        return self.quotient_common_refinement == equality_congruence(
            self.solution.elements
        )

    @property
    def has_subsolution_fibre_congruence(self) -> bool:
        return bool(self.subsolution_fibre_congruences)

    @property
    def has_proper_subsolution(self) -> bool:
        return bool(self.proper_subsolutions)

    @property
    def has_flip_across_decomposition(self) -> bool:
        return bool(self.flip_across_partitions)

    @property
    def has_nontrivial_one_state_observer(self) -> bool:
        return 1 < len(self.observer_partition)

    @property
    def has_standard_entry_branch(self) -> bool:
        return (
            self.has_point_separating_proper_quotients
            or self.has_proper_subsolution
            or self.has_subsolution_fibre_congruence
            or self.has_flip_across_decomposition
            or self.has_nontrivial_one_state_observer
        )


def _proper_nonempty_subsets(elements: Tuple[Element, ...]):
    for size in range(1, len(elements)):
        for subset in combinations(elements, size):
            yield frozenset(subset)


def is_flip_across_partition(
    solution: FiniteBraidedSet,
    left: FrozenSet[Element],
    right: FrozenSet[Element],
) -> bool:
    """Return whether `X=left union right` is a flip-across decomposition."""

    elements = set(solution.elements)
    if not left or not right:
        return False
    if left.intersection(right):
        return False
    if left.union(right) != elements:
        return False
    if not is_subsolution_subset(solution, left):
        return False
    if not is_subsolution_subset(solution, right):
        return False
    for a in left:
        for b in right:
            if solution.R[(a, b)] != (b, a):
                return False
            if solution.R[(b, a)] != (a, b):
                return False
    return True


def flip_across_partitions(
    solution: FiniteBraidedSet,
    max_size: int = 8,
) -> Tuple[FlipAcrossPartition, ...]:
    """Enumerate unordered two-block flip-across decompositions."""

    elements = tuple(solution.elements)
    if len(elements) > max_size:
        raise ValueError("flip-across partition enumeration is disabled for this size")
    if not elements:
        return ()
    out = []
    first = elements[0]
    for left in _proper_nonempty_subsets(elements):
        if first not in left:
            continue
        right = frozenset(set(elements).difference(left))
        if is_flip_across_partition(solution, left, right):
            out.append(FlipAcrossPartition(left, right))
    return tuple(out)


def proper_subsolution_subsets(
    solution: FiniteBraidedSet,
    max_size: int = 8,
) -> Tuple[FrozenSet[Element], ...]:
    """Enumerate nonempty proper crossing-closed subsets."""

    elements = tuple(solution.elements)
    if len(elements) > max_size:
        raise ValueError("subsolution enumeration is disabled for this size")
    return tuple(
        subset
        for subset in _proper_nonempty_subsets(elements)
        if is_subsolution_subset(solution, subset)
    )


def is_subsolution_fibre_congruence(
    solution: FiniteBraidedSet,
    partition: Partition,
) -> bool:
    """Return whether every congruence block is a crossing-closed subsolution."""

    return all(is_subsolution_subset(solution, block) for block in partition)


def subsolution_fibre_congruences(
    solution: FiniteBraidedSet,
    max_size: int = 7,
) -> Tuple[Partition, ...]:
    """Enumerate proper congruences whose blocks are all subsolutions."""

    return tuple(
        partition
        for partition in congruences(solution, max_size=max_size)
        if partition != equality_congruence(solution.elements)
        and partition != universal_congruence(solution.elements)
        and is_subsolution_fibre_congruence(solution, partition)
    )


def one_state_invariant_observer_partition(solution: FiniteBraidedSet) -> Partition:
    """Return the coarsest partition through which every one-state observer factors."""

    pairs = []
    for left in solution.elements:
        for right in solution.elements:
            out_left, out_right = solution.R[(left, right)]
            pairs.append((left, out_left))
            pairs.append((right, out_right))
    return generated_partition(solution.elements, pairs)


def terminal_branch_triage_audit(
    solution: FiniteBraidedSet,
    max_size: int = 7,
) -> TerminalBranchTriageAudit:
    """Run the exact small-table checks for standard proper-compression starts."""

    all_congruences = tuple(congruences(solution, max_size=max_size))
    proper = tuple(
        partition
        for partition in all_congruences
        if partition != equality_congruence(solution.elements)
        and len(partition) < len(solution.elements)
    )
    subsolution_fibres = tuple(
        partition
        for partition in proper
        if partition != universal_congruence(solution.elements)
        and is_subsolution_fibre_congruence(solution, partition)
    )
    if not proper:
        refinement = universal_congruence(solution.elements)
    else:
        refinement = proper[0]
        for partition in proper[1:]:
            refinement = common_refinement(refinement, partition)
    return TerminalBranchTriageAudit(
        solution=solution,
        proper_congruences=proper,
        subsolution_fibre_congruences=subsolution_fibres,
        quotient_common_refinement=refinement,
        proper_subsolutions=proper_subsolution_subsets(solution, max_size=max_size),
        flip_across_partitions=flip_across_partitions(solution, max_size=max_size),
        observer_partition=one_state_invariant_observer_partition(solution),
    )
