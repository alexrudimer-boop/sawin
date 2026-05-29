from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Dict, FrozenSet, Iterable, List, Sequence, Tuple

from .finite_braided_set import Element, FiniteBraidedSet
from .local_interval import LocalInterval, canonical_partition, set_partitions
from .residual import QuotientMap

Block = FrozenSet[Element]
Partition = Tuple[Block, ...]


def normalize_partition(blocks: Iterable[Iterable[Element]]) -> Partition:
    return canonical_partition(blocks)


def equality_congruence(elements: Sequence[Element]) -> Partition:
    return normalize_partition(frozenset([x]) for x in elements)


def universal_congruence(elements: Sequence[Element]) -> Partition:
    return (frozenset(elements),)


def block_map(partition: Partition) -> Dict[Element, Block]:
    mapping: Dict[Element, Block] = {}
    for block in partition:
        for element in block:
            if element in mapping:
                raise ValueError("partition blocks overlap")
            mapping[element] = block
    return mapping


def is_partition_of(partition: Partition, elements: Sequence[Element]) -> bool:
    mapping = block_map(partition)
    return set(mapping.keys()) == set(elements)


def refines(finer: Partition, coarser: Partition) -> bool:
    coarser_blocks = tuple(coarser)
    return all(any(block <= big for big in coarser_blocks) for block in finer)


def strictly_refines(finer: Partition, coarser: Partition) -> bool:
    return finer != coarser and refines(finer, coarser)


def common_refinement(left: Partition, right: Partition) -> Partition:
    blocks = []
    for a, b in product(left, right):
        intersection = a.intersection(b)
        if intersection:
            blocks.append(intersection)
    return normalize_partition(blocks)


def generated_partition(elements: Sequence[Element], pairs: Iterable[Tuple[Element, Element]]) -> Partition:
    parent = {x: x for x in elements}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    for a, b in pairs:
        union(a, b)
    groups: Dict[Element, List[Element]] = {}
    for x in elements:
        groups.setdefault(find(x), []).append(x)
    return normalize_partition(groups.values())


def _partition_key(partition: Partition):
    return (len(partition), tuple(tuple(sorted(map(repr, block))) for block in partition))


def is_congruence(solution: FiniteBraidedSet, partition: Partition) -> bool:
    if not is_partition_of(partition, solution.elements):
        return False
    mapping = block_map(partition)
    for x1, x2, y1, y2 in product(solution.elements, repeat=4):
        if mapping[x1] != mapping[x2] or mapping[y1] != mapping[y2]:
            continue
        u1, v1 = solution.R[(x1, y1)]
        u2, v2 = solution.R[(x2, y2)]
        if mapping[u1] != mapping[u2] or mapping[v1] != mapping[v2]:
            return False
    return True


def congruences(solution: FiniteBraidedSet, max_size: int = 7) -> List[Partition]:
    if len(solution.elements) > max_size:
        raise ValueError("congruence enumeration is disabled for this size")
    out = []
    for partition in set_partitions(solution.elements):
        normalized = normalize_partition(partition)
        if is_congruence(solution, normalized):
            out.append(normalized)
    return sorted(out, key=_partition_key)


def quotient_solution(solution: FiniteBraidedSet, partition: Partition) -> QuotientMap:
    if not is_congruence(solution, partition):
        raise ValueError("partition must be a congruence")
    mapping = block_map(partition)
    elements = tuple(partition)
    table = {}
    for a, b in product(elements, repeat=2):
        x = next(iter(a))
        y = next(iter(b))
        u, v = solution.R[(x, y)]
        table[(a, b)] = (mapping[u], mapping[v])
    quotient = FiniteBraidedSet(elements, table)
    return QuotientMap(solution, quotient, mapping)


def interval_covers(all_congruences: Sequence[Partition]) -> List[Tuple[Partition, Partition]]:
    covers = []
    for lower, upper in product(all_congruences, repeat=2):
        if not strictly_refines(lower, upper):
            continue
        has_middle = any(
            strictly_refines(lower, middle) and strictly_refines(middle, upper)
            for middle in all_congruences
        )
        if not has_middle:
            covers.append((lower, upper))
    return covers


def maximal_congruence_chain(solution: FiniteBraidedSet, max_size: int = 7) -> List[Partition]:
    lattice = congruences(solution, max_size=max_size)
    bottom = equality_congruence(solution.elements)
    top = universal_congruence(solution.elements)
    covers = interval_covers(lattice)
    by_lower: Dict[Partition, List[Partition]] = {}
    for lower, upper in covers:
        by_lower.setdefault(lower, []).append(upper)
    chain = [bottom]
    current = bottom
    seen = {bottom}
    while current != top:
        candidates = [upper for upper in by_lower.get(current, []) if upper not in seen]
        if not candidates:
            raise ValueError("no maximal chain to top found")
        candidates.sort(key=_partition_key)
        current = candidates[0]
        chain.append(current)
        seen.add(current)
    return chain


@dataclass(frozen=True)
class CongruenceInterval:
    solution: FiniteBraidedSet
    lower: Partition
    upper: Partition

    def __post_init__(self) -> None:
        if not is_congruence(self.solution, self.lower):
            raise ValueError("lower must be a congruence")
        if not is_congruence(self.solution, self.upper):
            raise ValueError("upper must be a congruence")
        if not refines(self.lower, self.upper):
            raise ValueError("lower must refine upper")

    def quotient_map(self) -> QuotientMap:
        lower_quotient = quotient_solution(self.solution, self.lower)
        upper_mapping = block_map(self.upper)
        lower_to_upper = {block: upper_mapping[next(iter(block))] for block in self.lower}
        upper_quotient = quotient_solution(self.solution, self.upper).quotient
        return QuotientMap(lower_quotient.quotient, upper_quotient, lower_to_upper)

    def local_interval(self) -> LocalInterval:
        qmap = self.quotient_map()
        colors = tuple(qmap.quotient.elements)
        fibres: Dict[Block, Tuple[Block, ...]] = {
            color: tuple(block for block in qmap.total.elements if qmap.pi[block] == color)
            for color in colors
        }
        base_R = qmap.quotient.R
        table = {}
        for a, b in product(colors, repeat=2):
            for x, y in product(fibres[a], fibres[b]):
                u, v = qmap.total.R[(x, y)]
                table[(a, b, x, y)] = (u, v)
        return LocalInterval(colors, fibres, base_R, table)

