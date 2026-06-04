from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations
from typing import Dict, FrozenSet, Tuple

from .congruence import (
    Partition,
    block_map,
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


@dataclass(frozen=True)
class MixedFibreTransitionRow:
    input_left_block: FrozenSet[Element]
    input_right_block: FrozenSet[Element]
    output_left_block: FrozenSet[Element]
    output_right_block: FrozenSet[Element]
    first_depends_only_on_left: bool
    first_depends_only_on_right: bool
    second_depends_only_on_left: bool
    second_depends_only_on_right: bool

    @property
    def direct_product_like(self) -> bool:
        return self.first_depends_only_on_left and self.second_depends_only_on_right

    @property
    def swapped_product_like(self) -> bool:
        return self.first_depends_only_on_right and self.second_depends_only_on_left

    @property
    def product_like(self) -> bool:
        return self.direct_product_like or self.swapped_product_like


@dataclass(frozen=True)
class SubsolutionFibreTransitionAudit:
    solution: FiniteBraidedSet
    partition: Partition
    rows: Tuple[MixedFibreTransitionRow, ...]

    @property
    def all_mixed_transitions_product_like(self) -> bool:
        return all(row.product_like for row in self.rows)

    @property
    def all_mixed_transitions_direct_product_like(self) -> bool:
        return all(row.direct_product_like for row in self.rows)

    @property
    def all_mixed_transitions_swapped_product_like(self) -> bool:
        return all(row.swapped_product_like for row in self.rows)


@dataclass(frozen=True)
class MixedFibreTransportMap:
    input_left_block: FrozenSet[Element]
    input_right_block: FrozenSet[Element]
    source_block: FrozenSet[Element]
    target_block: FrozenSet[Element]
    source_coordinate: str
    output_coordinate: str
    mapping: Tuple[Tuple[Element, Element], ...]
    is_well_defined: bool
    is_bijection: bool
    is_subsolution_isomorphism: bool


@dataclass(frozen=True)
class MixedFibreTransportRow:
    input_left_block: FrozenSet[Element]
    input_right_block: FrozenSet[Element]
    first_from_left: MixedFibreTransportMap
    first_from_right: MixedFibreTransportMap
    second_from_left: MixedFibreTransportMap
    second_from_right: MixedFibreTransportMap

    @property
    def direct_product_like(self) -> bool:
        return (
            self.first_from_left.is_well_defined
            and self.second_from_right.is_well_defined
        )

    @property
    def swapped_product_like(self) -> bool:
        return (
            self.first_from_right.is_well_defined
            and self.second_from_left.is_well_defined
        )

    @property
    def direct_transport_isomorphism(self) -> bool:
        return (
            self.first_from_left.is_subsolution_isomorphism
            and self.second_from_right.is_subsolution_isomorphism
        )

    @property
    def swapped_transport_isomorphism(self) -> bool:
        return (
            self.first_from_right.is_subsolution_isomorphism
            and self.second_from_left.is_subsolution_isomorphism
        )

    @property
    def product_like_transport_isomorphism(self) -> bool:
        return self.direct_transport_isomorphism or self.swapped_transport_isomorphism


@dataclass(frozen=True)
class SubsolutionFibreTransportIsomorphismAudit:
    solution: FiniteBraidedSet
    partition: Partition
    rows: Tuple[MixedFibreTransportRow, ...]

    @property
    def all_mixed_rows_product_like(self) -> bool:
        return all(
            row.direct_product_like or row.swapped_product_like for row in self.rows
        )

    @property
    def all_product_like_rows_have_transport_isomorphisms(self) -> bool:
        return all(row.product_like_transport_isomorphism for row in self.rows)


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


def subsolution_fibre_transition_audit(
    solution: FiniteBraidedSet,
    partition: Partition,
) -> SubsolutionFibreTransitionAudit:
    """Audit coordinate-dependence of mixed crossings between fibre blocks."""

    mapping = block_map(partition)
    rows = []
    for left_block in partition:
        for right_block in partition:
            if left_block == right_block:
                continue

            output_left_blocks = set()
            output_right_blocks = set()
            first_by_left = []
            first_by_right = []
            second_by_left = []
            second_by_right = []

            for left in left_block:
                first_values = set()
                second_values = set()
                for right in right_block:
                    out_left, out_right = solution.R[(left, right)]
                    output_left_blocks.add(mapping[out_left])
                    output_right_blocks.add(mapping[out_right])
                    first_values.add(out_left)
                    second_values.add(out_right)
                first_by_left.append(first_values)
                second_by_left.append(second_values)

            for right in right_block:
                first_values = set()
                second_values = set()
                for left in left_block:
                    out_left, out_right = solution.R[(left, right)]
                    first_values.add(out_left)
                    second_values.add(out_right)
                first_by_right.append(first_values)
                second_by_right.append(second_values)

            if len(output_left_blocks) != 1 or len(output_right_blocks) != 1:
                raise ValueError(
                    "partition must be compatible with mixed-block outputs"
                )
            output_left_block = next(iter(output_left_blocks))
            output_right_block = next(iter(output_right_blocks))

            rows.append(
                MixedFibreTransitionRow(
                    input_left_block=left_block,
                    input_right_block=right_block,
                    output_left_block=output_left_block,
                    output_right_block=output_right_block,
                    first_depends_only_on_left=all(
                        len(values) <= 1 for values in first_by_left
                    ),
                    first_depends_only_on_right=all(
                        len(values) <= 1 for values in first_by_right
                    ),
                    second_depends_only_on_left=all(
                        len(values) <= 1 for values in second_by_left
                    ),
                    second_depends_only_on_right=all(
                        len(values) <= 1 for values in second_by_right
                    ),
                )
            )
    return SubsolutionFibreTransitionAudit(solution, partition, tuple(rows))


def _is_subsolution_isomorphism(
    solution: FiniteBraidedSet,
    source_block: FrozenSet[Element],
    target_block: FrozenSet[Element],
    mapping: Dict[Element, Element],
) -> bool:
    if set(mapping.keys()) != set(source_block):
        return False
    if set(mapping.values()) != set(target_block):
        return False
    if len(set(mapping.values())) != len(mapping):
        return False
    for left in source_block:
        for right in source_block:
            out_left, out_right = solution.R[(left, right)]
            target_left, target_right = solution.R[(mapping[left], mapping[right])]
            if (target_left, target_right) != (mapping[out_left], mapping[out_right]):
                return False
    return True


def _mixed_coordinate_transport_map(
    solution: FiniteBraidedSet,
    input_left_block: FrozenSet[Element],
    input_right_block: FrozenSet[Element],
    source_coordinate: str,
    output_coordinate: str,
    target_block: FrozenSet[Element],
) -> MixedFibreTransportMap:
    source_block = input_left_block if source_coordinate == "left" else input_right_block
    other_block = input_right_block if source_coordinate == "left" else input_left_block
    mapping: Dict[Element, Element] = {}
    well_defined = True

    for source in source_block:
        values = set()
        for other in other_block:
            if source_coordinate == "left":
                out_left, out_right = solution.R[(source, other)]
            else:
                out_left, out_right = solution.R[(other, source)]
            values.add(out_left if output_coordinate == "first" else out_right)
        if len(values) != 1:
            well_defined = False
        else:
            mapping[source] = next(iter(values))

    is_bijection = (
        well_defined
        and set(mapping.keys()) == set(source_block)
        and set(mapping.values()) == set(target_block)
        and len(set(mapping.values())) == len(mapping)
    )
    is_isomorphism = well_defined and _is_subsolution_isomorphism(
        solution,
        source_block,
        target_block,
        mapping,
    )
    return MixedFibreTransportMap(
        input_left_block=input_left_block,
        input_right_block=input_right_block,
        source_block=source_block,
        target_block=target_block,
        source_coordinate=source_coordinate,
        output_coordinate=output_coordinate,
        mapping=tuple(sorted(mapping.items(), key=lambda item: repr(item[0]))),
        is_well_defined=well_defined,
        is_bijection=is_bijection,
        is_subsolution_isomorphism=is_isomorphism,
    )


def subsolution_fibre_transport_isomorphism_audit(
    solution: FiniteBraidedSet,
    partition: Partition,
) -> SubsolutionFibreTransportIsomorphismAudit:
    """Audit whether product-like mixed transports preserve block solutions."""

    transition_audit = subsolution_fibre_transition_audit(solution, partition)
    rows = []
    for row in transition_audit.rows:
        rows.append(
            MixedFibreTransportRow(
                input_left_block=row.input_left_block,
                input_right_block=row.input_right_block,
                first_from_left=_mixed_coordinate_transport_map(
                    solution,
                    row.input_left_block,
                    row.input_right_block,
                    "left",
                    "first",
                    row.output_left_block,
                ),
                first_from_right=_mixed_coordinate_transport_map(
                    solution,
                    row.input_left_block,
                    row.input_right_block,
                    "right",
                    "first",
                    row.output_left_block,
                ),
                second_from_left=_mixed_coordinate_transport_map(
                    solution,
                    row.input_left_block,
                    row.input_right_block,
                    "left",
                    "second",
                    row.output_right_block,
                ),
                second_from_right=_mixed_coordinate_transport_map(
                    solution,
                    row.input_left_block,
                    row.input_right_block,
                    "right",
                    "second",
                    row.output_right_block,
                ),
            )
        )
    return SubsolutionFibreTransportIsomorphismAudit(solution, partition, tuple(rows))


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
