from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from typing import Dict, Hashable, Mapping, Tuple

from .finite_braided_set import FiniteBraidedSet

Transformation = Tuple[int, ...]


def compose_transformations(left: Transformation, right: Transformation) -> Transformation:
    """Return the transformation `left after right`."""

    return tuple(left[right[index]] for index in range(len(left)))


def invert_permutation(permutation: Transformation) -> Transformation:
    inverse = [0] * len(permutation)
    for index, image in enumerate(permutation):
        inverse[image] = index
    return tuple(inverse)


def close_transformation_monoid(
    generators: set[Transformation],
    size: int,
) -> Tuple[Transformation, ...]:
    identity = tuple(range(size))
    monoid = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for other in tuple(monoid | generators):
            for candidate in (
                compose_transformations(current, other),
                compose_transformations(other, current),
            ):
                if candidate not in monoid:
                    monoid.add(candidate)
                    queue.append(candidate)
    return tuple(sorted(monoid))


class UnionFind:
    def __init__(self, count: int) -> None:
        self.parent = list(range(count))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root != right_root:
            self.parent[right_root] = left_root


@dataclass(frozen=True)
class ContextualCompletionData:
    """Two-sided contextual quotient and forced partial translations."""

    elements: Tuple[Hashable, ...]
    left_monoid: Tuple[Transformation, ...]
    right_monoid: Tuple[Transformation, ...]
    class_of_triple: Mapping[Tuple[int, int, int], int]
    partial_translations: Mapping[int, Mapping[int, int]]
    conflict_count: int

    @property
    def class_count(self) -> int:
        if not self.class_of_triple:
            return 0
        return 1 + max(self.class_of_triple.values())

    @property
    def forced_product_count(self) -> int:
        return sum(len(row) for row in self.partial_translations.values())

    @property
    def domain_sizes(self) -> Tuple[int, ...]:
        return tuple(sorted({len(row) for row in self.partial_translations.values()}))


@dataclass(frozen=True)
class IdentityExtensionSummary:
    """Finite checks for the identity-outside contextual rack completion."""

    class_count: int
    left_monoid_size: int
    right_monoid_size: int
    left_right_monoids_equal: bool
    forced_product_count: int
    domain_sizes: Tuple[int, ...]
    conflict_count: int
    partial_translations_injective: bool
    balanced_domains: bool
    identity_extension_total_permutations: bool
    identity_extension_conjugacy_covariance: bool
    full_forced_graph_local_covariance_failures: int
    nontrivial_left_translation_count: int

    @property
    def identity_extension_witnesses_active_lifts(self) -> bool:
        return (
            self.conflict_count == 0
            and self.partial_translations_injective
            and self.balanced_domains
            and self.identity_extension_total_permutations
            and self.identity_extension_conjugacy_covariance
        )


def contextual_completion_data(solution: FiniteBraidedSet) -> ContextualCompletionData:
    elements = tuple(solution.elements)
    element_index = {element: index for index, element in enumerate(elements)}
    size = len(elements)
    indexed_table = {
        (element_index[x], element_index[y]): (
            element_index[solution.R[(x, y)][0]],
            element_index[solution.R[(x, y)][1]],
        )
        for x, y in product(elements, repeat=2)
    }
    inverse_table = {value: key for key, value in indexed_table.items()}
    r_maps = {
        y: tuple(indexed_table[(x, y)][1] for x in range(size))
        for y in range(size)
    }
    m_maps = {
        u: tuple(inverse_table[(u, v)][0] for v in range(size))
        for u in range(size)
    }
    left_monoid = close_transformation_monoid(set(m_maps.values()), size)
    right_monoid = close_transformation_monoid(set(r_maps.values()), size)
    left_index = {mapping: index for index, mapping in enumerate(left_monoid)}
    right_index = {mapping: index for index, mapping in enumerate(right_monoid)}

    triples = tuple(
        (left, x, right)
        for left in range(len(left_monoid))
        for x in range(size)
        for right in range(len(right_monoid))
    )
    triple_index = {triple: index for index, triple in enumerate(triples)}
    union_find = UnionFind(len(triples))

    for left_id, left_map in enumerate(left_monoid):
        for right_id, right_map in enumerate(right_monoid):
            for x, y in product(range(size), repeat=2):
                u, v = indexed_table[(x, y)]
                first = (
                    left_id,
                    x,
                    right_index[compose_transformations(right_map, r_maps[y])],
                )
                second = (
                    left_index[compose_transformations(left_map, m_maps[u])],
                    v,
                    right_id,
                )
                union_find.union(triple_index[first], triple_index[second])

    class_index_by_root: Dict[int, int] = {}
    class_of_triple: Dict[Tuple[int, int, int], int] = {}
    for triple in triples:
        root = union_find.find(triple_index[triple])
        if root not in class_index_by_root:
            class_index_by_root[root] = len(class_index_by_root)
        class_of_triple[triple] = class_index_by_root[root]

    class_count = len(class_index_by_root)
    partial: Dict[int, Dict[int, int]] = {index: {} for index in range(class_count)}
    conflict_count = 0
    for left_id, left_map in enumerate(left_monoid):
        for right_id, right_map in enumerate(right_monoid):
            for x, y in product(range(size), repeat=2):
                u, v = indexed_table[(x, y)]
                p = class_of_triple[
                    (
                        left_id,
                        x,
                        right_index[compose_transformations(right_map, r_maps[y])],
                    )
                ]
                q = class_of_triple[
                    (
                        left_index[compose_transformations(left_map, m_maps[x])],
                        y,
                        right_id,
                    )
                ]
                out = class_of_triple[
                    (
                        left_id,
                        u,
                        right_index[compose_transformations(right_map, r_maps[v])],
                    )
                ]
                previous = partial[p].get(q)
                if previous is not None and previous != out:
                    conflict_count += 1
                partial[p][q] = out

    return ContextualCompletionData(
        elements=elements,
        left_monoid=left_monoid,
        right_monoid=right_monoid,
        class_of_triple=class_of_triple,
        partial_translations=partial,
        conflict_count=conflict_count,
    )


def identity_extension_summary(
    data: ContextualCompletionData,
) -> IdentityExtensionSummary:
    class_count = data.class_count
    identity = tuple(range(class_count))
    left_translations = []
    partial_injective = True
    balanced_domains = True
    for p in range(class_count):
        row_data = data.partial_translations[p]
        image = set(row_data.values())
        if len(image) != len(row_data):
            partial_injective = False
        if image != set(row_data):
            balanced_domains = False
        row = list(identity)
        for source, target in row_data.items():
            row[source] = target
        left_translations.append(tuple(row))

    total_permutations = all(
        len(set(row)) == class_count
        for row in left_translations
    )
    covariance = False
    if total_permutations:
        inverses = tuple(invert_permutation(row) for row in left_translations)
        covariance = True
        for p in range(class_count):
            for q in range(class_count):
                conjugate = compose_transformations(
                    compose_transformations(left_translations[p], left_translations[q]),
                    inverses[p],
                )
                if left_translations[left_translations[p][q]] != conjugate:
                    covariance = False
                    break
            if not covariance:
                break

    local_covariance_failures = 0
    for p, row in data.partial_translations.items():
        for q, pq in row.items():
            for a, qa in data.partial_translations[q].items():
                if a not in row or qa not in row:
                    continue
                pa = row[a]
                if pa not in data.partial_translations[pq]:
                    continue
                if data.partial_translations[pq][pa] != row[qa]:
                    local_covariance_failures += 1

    return IdentityExtensionSummary(
        class_count=class_count,
        left_monoid_size=len(data.left_monoid),
        right_monoid_size=len(data.right_monoid),
        left_right_monoids_equal=set(data.left_monoid) == set(data.right_monoid),
        forced_product_count=data.forced_product_count,
        domain_sizes=data.domain_sizes,
        conflict_count=data.conflict_count,
        partial_translations_injective=partial_injective,
        balanced_domains=balanced_domains,
        identity_extension_total_permutations=total_permutations,
        identity_extension_conjugacy_covariance=covariance,
        full_forced_graph_local_covariance_failures=local_covariance_failures,
        nontrivial_left_translation_count=sum(
            1 for row in left_translations if row != identity
        ),
    )
