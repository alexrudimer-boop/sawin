"""Reconstruct non-permutation size-three endpoint detector inputs.

The functions in this module reconstruct the finite endpoint candidates and
monoid quotients used by the non-permutation ``|X|=3`` endpoint-gate
experiments.  They deliberately separate the proved finite data being
reconstructed from the later detector search and all-arity interpretation.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Sequence

from .finite_braided_set import FiniteBraidedSet
from .finite_rack_sat import Endpoint, MonoidQuotient
from .small_search import all_bijection_solutions, is_permutation_solution_form

FlatYbeTable = tuple[int, ...]


class _DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, left: int, right: int) -> bool:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1
        return True


@dataclass(frozen=True)
class EndpointCandidate:
    """A principal endpoint pair made equal by a rack-admissible quotient."""

    candidate_id: str
    ybe_table: FlatYbeTable
    solution_index: int
    partition: tuple[int, ...]
    partition_index: int
    arity: int
    e_word: tuple[int, ...]
    e_position: int
    eprime_word: tuple[int, ...]
    eprime_position: int

    @property
    def endpoint(self) -> Endpoint:
        return Endpoint(
            prefix=self.e_word[: self.e_position],
            letter=self.e_word[self.e_position],
            suffix=self.e_word[self.e_position + 1 :],
        )

    @property
    def endpoint_prime(self) -> Endpoint:
        return Endpoint(
            prefix=self.eprime_word[: self.eprime_position],
            letter=self.eprime_word[self.eprime_position],
            suffix=self.eprime_word[self.eprime_position + 1 :],
        )


def flat_table_from_solution(solution: FiniteBraidedSet) -> FlatYbeTable:
    """Return the flat ``d*x+y`` table convention used by certificates."""

    size = len(solution.elements)
    return tuple(
        size * solution.R[(x, y)][0] + solution.R[(x, y)][1]
        for x in solution.elements
        for y in solution.elements
    )


def solution_from_flat_table(table: Iterable[int]) -> FiniteBraidedSet:
    """Build a zero-based finite braided set from a flat pair table."""

    flat = tuple(int(entry) for entry in table)
    size_squared = len(flat)
    size = int(size_squared**0.5)
    if size * size != size_squared:
        raise ValueError("flat YBE table length must be a square")
    elements = tuple(range(size))
    pairs = tuple(product(elements, repeat=2))
    values = tuple(divmod(value, size) for value in flat)
    return FiniteBraidedSet(elements, dict(zip(pairs, values)))


def nonpermutation_size3_solutions() -> tuple[tuple[int, FiniteBraidedSet], ...]:
    """Return ``(global_solution_index, solution)`` for the 55 target tables."""

    return tuple(
        (index, solution)
        for index, solution in enumerate(all_bijection_solutions(3))
        if not is_permutation_solution_form(solution)
    )


def truncated_structure_monoid_length_1() -> MonoidQuotient:
    """Universal truncation retaining the empty word and length-one words."""

    return MonoidQuotient(
        size=5,
        identity=0,
        mul=(
            (0, 1, 2, 3, 4),
            (1, 4, 4, 4, 4),
            (2, 4, 4, 4, 4),
            (3, 4, 4, 4, 4),
            (4, 4, 4, 4, 4),
        ),
        gen=(1, 2, 3),
    )


def truncated_structure_monoid_length_2(
    solution: FiniteBraidedSet,
) -> MonoidQuotient:
    """Solution-dependent truncation retaining structure-monoid words of length 2."""

    if tuple(solution.elements) != (0, 1, 2):
        raise ValueError("length-two truncation is implemented for size-three tables")
    pair_index = {(x, y): 3 * x + y for x in range(3) for y in range(3)}
    pair_dsu = _DSU(9)
    for x in range(3):
        for y in range(3):
            x_prime, y_prime = solution.R[(x, y)]
            pair_dsu.union(pair_index[(x, y)], pair_index[(x_prime, y_prime)])

    roots: dict[int, int] = {}
    for pair, index in pair_index.items():
        root = pair_dsu.find(index)
        if root not in roots:
            roots[root] = 4 + len(roots)
    absorbing = 4 + len(roots)
    size = absorbing + 1
    mul = [[absorbing for _ in range(size)] for _ in range(size)]
    for value in range(size):
        mul[0][value] = value
        mul[value][0] = value
    for x in range(3):
        for y in range(3):
            mul[1 + x][1 + y] = roots[pair_dsu.find(pair_index[(x, y)])]
    return MonoidQuotient(
        size=size,
        identity=0,
        mul=tuple(tuple(row) for row in mul),
        gen=(1, 2, 3),
    )


def canonical_partitions_3() -> tuple[tuple[int, int, int], ...]:
    """Return canonical set partitions of ``{0,1,2}`` in restricted-growth order."""

    return (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (0, 1, 2),
    )


def quotient_solution_by_partition(
    solution: FiniteBraidedSet,
    partition: Sequence[int],
) -> FiniteBraidedSet | None:
    """Return the quotient braided set induced by ``partition``, if well-defined."""

    partition = tuple(int(value) for value in partition)
    if len(partition) != len(solution.elements):
        raise ValueError("partition length must match solution size")
    classes = tuple(sorted(set(partition)))
    table = {}
    for left_class in classes:
        for right_class in classes:
            values = set()
            for x in solution.elements:
                for y in solution.elements:
                    if partition[x] == left_class and partition[y] == right_class:
                        x_prime, y_prime = solution.R[(x, y)]
                        values.add((partition[x_prime], partition[y_prime]))
            if len(values) != 1:
                return None
            table[(left_class, right_class)] = values.pop()
    try:
        quotient = FiniteBraidedSet(classes, table)
    except ValueError:
        return None
    if not quotient.is_ybe():
        return None
    return quotient


def endpoint_t_classes(
    solution: FiniteBraidedSet,
    arity: int,
) -> tuple[_DSU, object, tuple[tuple[int, ...], ...]]:
    """Return endpoint T-classes for all positions in all ``X^arity`` tuples."""

    elements = tuple(solution.elements)
    words = tuple(tuple(word) for word in product(elements, repeat=arity))
    index = {word: position for position, word in enumerate(words)}
    dsu = _DSU(len(words) * arity)

    def node(word: Sequence[int], position: int) -> int:
        return index[tuple(word)] * arity + position

    for word in words:
        for crossing in range(arity - 1):
            left, right = solution.R[(word[crossing], word[crossing + 1])]
            word2 = word[:crossing] + (left, right) + word[crossing + 2 :]
            for position in range(arity):
                if position < crossing or position > crossing + 1:
                    dsu.union(node(word, position), node(word2, position))
                elif position == crossing:
                    dsu.union(node(word, crossing), node(word2, crossing + 1))
    return dsu, node, words


def tuple_orbits(
    solution: FiniteBraidedSet,
    arity: int,
) -> tuple[_DSU, dict[tuple[int, ...], int], tuple[tuple[int, ...], ...]]:
    """Return tuple braid-orbit components using the forward generators."""

    words = tuple(
        tuple(word)
        for word in product(tuple(solution.elements), repeat=arity)
    )
    index = {word: position for position, word in enumerate(words)}
    dsu = _DSU(len(words))
    for word in words:
        for crossing in range(arity - 1):
            word2 = solution.apply_R_at(word, crossing)
            dsu.union(index[word], index[word2])
    return dsu, index, words


def principal_bad_endpoint_candidates(
    solution: FiniteBraidedSet,
    *,
    solution_index: int,
    arity: int,
) -> tuple[EndpointCandidate, ...]:
    """Enumerate compact principal bad endpoint pairs for one size-three table."""

    if tuple(solution.elements) != (0, 1, 2):
        raise ValueError("principal nonperm3 candidates require elements 0,1,2")
    if arity < 1:
        raise ValueError("arity must be positive")

    ybe_table = flat_table_from_solution(solution)
    x_t_dsu, x_t_node, words = endpoint_t_classes(solution, arity)
    orbit_dsu, orbit_index, _ = tuple_orbits(solution, arity)
    all_endpoints = tuple((word, position) for word in words for position in range(arity))
    out: list[EndpointCandidate] = []
    local_index = 0

    for partition_index, partition in enumerate(canonical_partitions_3()):
        quotient = quotient_solution_by_partition(solution, partition)
        if quotient is None:
            continue
        quotient_t_dsu, quotient_t_node, _ = endpoint_t_classes(quotient, arity)
        for left_index, (word, position) in enumerate(all_endpoints):
            for right_index, (word2, position2) in enumerate(all_endpoints):
                if right_index <= left_index:
                    continue
                if orbit_dsu.find(orbit_index[word]) != orbit_dsu.find(orbit_index[word2]):
                    continue
                quotient_word = tuple(partition[x] for x in word)
                quotient_word2 = tuple(partition[x] for x in word2)
                quotient_equal = (
                    quotient_t_dsu.find(quotient_t_node(quotient_word, position))
                    == quotient_t_dsu.find(quotient_t_node(quotient_word2, position2))
                )
                x_equal = (
                    x_t_dsu.find(x_t_node(word, position))
                    == x_t_dsu.find(x_t_node(word2, position2))
                )
                if quotient_equal and not x_equal:
                    out.append(
                        EndpointCandidate(
                            candidate_id=(
                                f"a{arity}:X{solution_index:03d}:"
                                f"P{partition_index}:E{local_index:06d}"
                            ),
                            ybe_table=ybe_table,
                            solution_index=solution_index,
                            partition=tuple(partition),
                            partition_index=partition_index,
                            arity=arity,
                            e_word=tuple(word),
                            e_position=position,
                            eprime_word=tuple(word2),
                            eprime_position=position2,
                        )
                    )
                    local_index += 1
    return tuple(out)


def principal_bad_endpoint_candidates_for_nonperm3(
    *,
    arity: int,
) -> tuple[EndpointCandidate, ...]:
    """Enumerate principal bad endpoint candidates over all 55 target tables."""

    out: list[EndpointCandidate] = []
    for solution_index, solution in nonpermutation_size3_solutions():
        out.extend(
            principal_bad_endpoint_candidates(
                solution,
                solution_index=solution_index,
                arity=arity,
            )
        )
    return tuple(out)


def is_associative_monoid(monoid: MonoidQuotient) -> bool:
    """Check monoid associativity and identity laws."""

    for value in range(monoid.size):
        if monoid.mul[monoid.identity][value] != value:
            return False
        if monoid.mul[value][monoid.identity] != value:
            return False
    for a in range(monoid.size):
        for b in range(monoid.size):
            for c in range(monoid.size):
                if monoid.mul[monoid.mul[a][b]][c] != monoid.mul[a][monoid.mul[b][c]]:
                    return False
    return True
