from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from typing import Dict, Hashable, Mapping, Tuple

from .finite_braided_set import FiniteBraidedSet, rack_solution

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
    r_maps: Tuple[Transformation, ...]
    m_maps: Tuple[Transformation, ...]
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

    @property
    def element_index(self) -> Mapping[Hashable, int]:
        return {element: index for index, element in enumerate(self.elements)}


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


@dataclass(frozen=True)
class ActiveLiftExistenceSummary:
    """Evidence for a coherent active-lift system."""

    class_count: int
    identity_extension_singleton_witness: bool
    identity_extension_forced_pair_closure_failures: int

    @property
    def proves_active_lift_system_exists(self) -> bool:
        return self.identity_extension_singleton_witness


@dataclass(frozen=True)
class ContextSignatureQuotientSummary:
    """Check whether equal `(m_x,r_x)` signatures define a braided quotient."""

    element_count: int
    quotient_class_count: int
    block_sizes: Tuple[int, ...]
    is_braided_congruence: bool
    failure: Mapping[str, object] | None

    @property
    def is_strict_quotient(self) -> bool:
        return self.quotient_class_count < self.element_count


@dataclass(frozen=True)
class ContextSignatureCoreSummary:
    """Largest checked braided-congruence core inside context signatures."""

    element_count: int
    raw_quotient_class_count: int
    core_class_count: int
    raw_block_sizes: Tuple[int, ...]
    core_block_sizes: Tuple[int, ...]
    refinement_iterations: int
    is_braided_congruence: bool
    verification_failure: Mapping[str, object] | None

    @property
    def core_is_equality(self) -> bool:
        return self.core_class_count == self.element_count

    @property
    def core_equals_raw_context_quotient(self) -> bool:
        return self.core_class_count == self.raw_quotient_class_count


@dataclass(frozen=True)
class RelativeContextualSeparationSummary:
    """Finite automaton check for injectivity of `(pi^n,J_n)` in all arities."""

    element_count: int
    quotient_class_count: int
    left_monoid_size: int
    right_monoid_size: int
    valid_vertex_count: int | None
    checked: bool
    skipped_reason: str | None
    collision_found: bool
    collision_length: int | None
    collision_path_indices: Tuple[Tuple[int, int], ...]
    collision_path: Tuple[Tuple[str, str], ...]

    @property
    def proves_all_arity_injective(self) -> bool:
        return self.checked and not self.collision_found


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
        r_maps=tuple(r_maps[index] for index in range(size)),
        m_maps=tuple(m_maps[index] for index in range(size)),
        left_monoid=left_monoid,
        right_monoid=right_monoid,
        class_of_triple=class_of_triple,
        partial_translations=partial,
        conflict_count=conflict_count,
    )


def context_signature_quotient_summary(
    solution: FiniteBraidedSet,
    data: ContextualCompletionData | None = None,
) -> ContextSignatureQuotientSummary:
    """Return whether `x -> (m_x,r_x)` is a braided congruence quotient."""

    if data is None:
        data = contextual_completion_data(solution)
    elements = tuple(solution.elements)
    element_index = data.element_index
    indexed_table = {
        (element_index[x], element_index[y]): (
            element_index[solution.R[(x, y)][0]],
            element_index[solution.R[(x, y)][1]],
        )
        for x, y in product(elements, repeat=2)
    }
    signature_to_class: Dict[Tuple[Transformation, Transformation], int] = {}
    class_of_index = []
    for index in range(len(elements)):
        signature = (data.m_maps[index], data.r_maps[index])
        if signature not in signature_to_class:
            signature_to_class[signature] = len(signature_to_class)
        class_of_index.append(signature_to_class[signature])
    block_counter = {
        class_id: class_of_index.count(class_id)
        for class_id in range(len(signature_to_class))
    }

    for x, x_prime, y, y_prime in product(range(len(elements)), repeat=4):
        if class_of_index[x] != class_of_index[x_prime]:
            continue
        if class_of_index[y] != class_of_index[y_prime]:
            continue
        u, v = indexed_table[(x, y)]
        u_prime, v_prime = indexed_table[(x_prime, y_prime)]
        if (
            class_of_index[u] != class_of_index[u_prime]
            or class_of_index[v] != class_of_index[v_prime]
        ):
            return ContextSignatureQuotientSummary(
                element_count=len(elements),
                quotient_class_count=len(signature_to_class),
                block_sizes=tuple(sorted(block_counter.values())),
                is_braided_congruence=False,
                failure={
                    "x": repr(elements[x]),
                    "x_prime": repr(elements[x_prime]),
                    "y": repr(elements[y]),
                    "y_prime": repr(elements[y_prime]),
                    "R_x_y": [repr(elements[u]), repr(elements[v])],
                    "R_x_prime_y_prime": [
                        repr(elements[u_prime]),
                        repr(elements[v_prime]),
                    ],
                    "input_classes": [
                        class_of_index[x],
                        class_of_index[y],
                    ],
                    "output_classes": [
                        class_of_index[u],
                        class_of_index[v],
                    ],
                    "output_prime_classes": [
                        class_of_index[u_prime],
                        class_of_index[v_prime],
                    ],
                },
            )

    return ContextSignatureQuotientSummary(
        element_count=len(elements),
        quotient_class_count=len(signature_to_class),
        block_sizes=tuple(sorted(block_counter.values())),
        is_braided_congruence=True,
        failure=None,
    )


def _normalize_partition(keys: Tuple[Hashable, ...]) -> Tuple[int, ...]:
    key_to_class: Dict[Hashable, int] = {}
    classes = []
    for key in keys:
        if key not in key_to_class:
            key_to_class[key] = len(key_to_class)
        classes.append(key_to_class[key])
    return tuple(classes)


def context_signature_labels(data: ContextualCompletionData) -> Mapping[Hashable, int]:
    """Return labels for the raw `(m_x,r_x)` context-signature partition."""

    classes = _normalize_partition(
        tuple((data.m_maps[index], data.r_maps[index]) for index in range(len(data.elements)))
    )
    return {
        element: classes[index]
        for index, element in enumerate(data.elements)
    }


def _partition_block_sizes(classes: Tuple[int, ...]) -> Tuple[int, ...]:
    return tuple(
        sorted(classes.count(class_id) for class_id in sorted(set(classes)))
    )


def _congruence_failure_for_classes(
    solution: FiniteBraidedSet,
    classes: Tuple[int, ...],
) -> Mapping[str, object] | None:
    elements = tuple(solution.elements)
    element_index = {element: index for index, element in enumerate(elements)}
    indexed_table = {
        (element_index[x], element_index[y]): (
            element_index[solution.R[(x, y)][0]],
            element_index[solution.R[(x, y)][1]],
        )
        for x, y in product(elements, repeat=2)
    }
    indexed_inverse = {value: key for key, value in indexed_table.items()}
    operations = (
        ("R_1", lambda x, y: indexed_table[(x, y)][0]),
        ("R_2", lambda x, y: indexed_table[(x, y)][1]),
        ("Rinv_1", lambda x, y: indexed_inverse[(x, y)][0]),
        ("Rinv_2", lambda x, y: indexed_inverse[(x, y)][1]),
    )
    for op_name, operation in operations:
        for x, x_prime, y, y_prime in product(range(len(elements)), repeat=4):
            if classes[x] != classes[x_prime] or classes[y] != classes[y_prime]:
                continue
            output = operation(x, y)
            output_prime = operation(x_prime, y_prime)
            if classes[output] != classes[output_prime]:
                return {
                    "operation": op_name,
                    "x": repr(elements[x]),
                    "x_prime": repr(elements[x_prime]),
                    "y": repr(elements[y]),
                    "y_prime": repr(elements[y_prime]),
                    "output": repr(elements[output]),
                    "output_prime": repr(elements[output_prime]),
                    "input_classes": [classes[x], classes[y]],
                    "output_classes": [
                        classes[output],
                        classes[output_prime],
                    ],
                }
    return None


def context_signature_core_summary(
    solution: FiniteBraidedSet,
    data: ContextualCompletionData | None = None,
) -> ContextSignatureCoreSummary:
    """Refine context signatures to a braided congruence core."""

    if data is None:
        data = contextual_completion_data(solution)
    elements = tuple(solution.elements)
    element_index = data.element_index
    indexed_table = {
        (element_index[x], element_index[y]): (
            element_index[solution.R[(x, y)][0]],
            element_index[solution.R[(x, y)][1]],
        )
        for x, y in product(elements, repeat=2)
    }
    indexed_inverse = {value: key for key, value in indexed_table.items()}
    operations = (
        lambda x, y: indexed_table[(x, y)][0],
        lambda x, y: indexed_table[(x, y)][1],
        lambda x, y: indexed_inverse[(x, y)][0],
        lambda x, y: indexed_inverse[(x, y)][1],
    )
    raw_classes = _normalize_partition(
        tuple((data.m_maps[index], data.r_maps[index]) for index in range(len(elements)))
    )
    classes = raw_classes
    iterations = 0
    while True:
        block_ids = tuple(sorted(set(classes)))
        blocks = {
            block_id: tuple(index for index, cls in enumerate(classes) if cls == block_id)
            for block_id in block_ids
        }
        keys = []
        for x in range(len(elements)):
            profile = [classes[x]]
            for operation in operations:
                for block_id in block_ids:
                    block = blocks[block_id]
                    profile.append(tuple(classes[operation(x, y)] for y in block))
                    profile.append(tuple(classes[operation(y, x)] for y in block))
            keys.append(tuple(profile))
        refined = _normalize_partition(tuple(keys))
        if refined == classes:
            break
        classes = refined
        iterations += 1

    failure = _congruence_failure_for_classes(solution, classes)
    return ContextSignatureCoreSummary(
        element_count=len(elements),
        raw_quotient_class_count=len(set(raw_classes)),
        core_class_count=len(set(classes)),
        raw_block_sizes=_partition_block_sizes(raw_classes),
        core_block_sizes=_partition_block_sizes(classes),
        refinement_iterations=iterations,
        is_braided_congruence=failure is None,
        verification_failure=failure,
    )


def context_signature_core_labels(
    solution: FiniteBraidedSet,
    data: ContextualCompletionData | None = None,
) -> Mapping[Hashable, int]:
    """Return labels for the refined context-signature congruence core."""

    if data is None:
        data = contextual_completion_data(solution)
    elements = tuple(solution.elements)
    element_index = data.element_index
    indexed_table = {
        (element_index[x], element_index[y]): (
            element_index[solution.R[(x, y)][0]],
            element_index[solution.R[(x, y)][1]],
        )
        for x, y in product(elements, repeat=2)
    }
    indexed_inverse = {value: key for key, value in indexed_table.items()}
    operations = (
        lambda x, y: indexed_table[(x, y)][0],
        lambda x, y: indexed_table[(x, y)][1],
        lambda x, y: indexed_inverse[(x, y)][0],
        lambda x, y: indexed_inverse[(x, y)][1],
    )
    classes = _normalize_partition(
        tuple((data.m_maps[index], data.r_maps[index]) for index in range(len(elements)))
    )
    while True:
        block_ids = tuple(sorted(set(classes)))
        blocks = {
            block_id: tuple(index for index, cls in enumerate(classes) if cls == block_id)
            for block_id in block_ids
        }
        keys = []
        for x in range(len(elements)):
            profile = [classes[x]]
            for operation in operations:
                for block_id in block_ids:
                    block = blocks[block_id]
                    profile.append(tuple(classes[operation(x, y)] for y in block))
                    profile.append(tuple(classes[operation(y, x)] for y in block))
            keys.append(tuple(profile))
        refined = _normalize_partition(tuple(keys))
        if refined == classes:
            break
        classes = refined
    return {
        element: classes[index]
        for index, element in enumerate(elements)
    }


def relative_contextual_separation_summary(
    data: ContextualCompletionData,
    quotient_labels: Mapping[Hashable, Hashable],
    *,
    max_vertices: int = 2_000_000,
) -> RelativeContextualSeparationSummary:
    """Check all-arity injectivity of `(pi^n,J_n)` by finite reachability."""

    elements = tuple(data.elements)
    element_index = data.element_index
    labels = tuple(quotient_labels[element] for element in elements)
    quotient_class_count = len(set(labels))
    size = len(elements)
    identity = tuple(range(size))
    left_identity = data.left_monoid.index(identity)
    right_identity = data.right_monoid.index(identity)
    left_index = {mapping: index for index, mapping in enumerate(data.left_monoid)}
    right_predecessors: Dict[Tuple[int, int], Tuple[int, ...]] = {}
    for target_right_id, target_right in enumerate(data.right_monoid):
        for y in range(size):
            predecessors = [
                source_id
                for source_id, source_right in enumerate(data.right_monoid)
                if compose_transformations(source_right, data.r_maps[y])
                == target_right
            ]
            right_predecessors[(target_right_id, y)] = tuple(predecessors)

    valid_vertices = set()
    for left, left_prime, right, right_prime, x, x_prime in product(
        range(len(data.left_monoid)),
        range(len(data.left_monoid)),
        range(len(data.right_monoid)),
        range(len(data.right_monoid)),
        range(size),
        range(size),
    ):
        if labels[x] != labels[x_prime]:
            continue
        if (
            data.class_of_triple[(left, x, right)]
            != data.class_of_triple[(left_prime, x_prime, right_prime)]
        ):
            continue
        valid_vertices.add((left, left_prime, right, right_prime, x, x_prime))
        if len(valid_vertices) > max_vertices:
            return RelativeContextualSeparationSummary(
                element_count=size,
                quotient_class_count=quotient_class_count,
                left_monoid_size=len(data.left_monoid),
                right_monoid_size=len(data.right_monoid),
                valid_vertex_count=None,
                checked=False,
                skipped_reason=f"valid vertex count exceeds {max_vertices}",
                collision_found=False,
                collision_length=None,
                collision_path_indices=(),
                collision_path=(),
            )

    queue = deque()
    seen = set()
    parent: Dict[Tuple[Tuple[int, ...], bool], Tuple[Tuple[int, ...], bool] | None] = {}
    for vertex in valid_vertices:
        left, left_prime, right, right_prime, x, x_prime = vertex
        if left != left_identity or left_prime != left_identity:
            continue
        state = (vertex, x != x_prime)
        queue.append(state)
        seen.add(state)
        parent[state] = None

    terminal_state = None
    while queue:
        vertex, mismatch = queue.popleft()
        left, left_prime, right, right_prime, x, x_prime = vertex
        if right == right_identity and right_prime == right_identity and mismatch:
            terminal_state = (vertex, mismatch)
            break
        next_left = left_index[
            compose_transformations(data.left_monoid[left], data.m_maps[x])
        ]
        next_left_prime = left_index[
            compose_transformations(
                data.left_monoid[left_prime],
                data.m_maps[x_prime],
            )
        ]
        for y, y_prime in product(range(size), repeat=2):
            if labels[y] != labels[y_prime]:
                continue
            for next_right in right_predecessors[(right, y)]:
                for next_right_prime in right_predecessors[(right_prime, y_prime)]:
                    next_vertex = (
                        next_left,
                        next_left_prime,
                        next_right,
                        next_right_prime,
                        y,
                        y_prime,
                    )
                    if next_vertex not in valid_vertices:
                        continue
                    next_state = (next_vertex, mismatch or y != y_prime)
                    if next_state in seen:
                        continue
                    seen.add(next_state)
                    parent[next_state] = (vertex, mismatch)
                    queue.append(next_state)

    if terminal_state is None:
        return RelativeContextualSeparationSummary(
            element_count=size,
            quotient_class_count=quotient_class_count,
            left_monoid_size=len(data.left_monoid),
            right_monoid_size=len(data.right_monoid),
            valid_vertex_count=len(valid_vertices),
            checked=True,
            skipped_reason=None,
            collision_found=False,
            collision_length=None,
            collision_path_indices=(),
            collision_path=(),
        )

    reversed_path = []
    current = terminal_state
    while current is not None:
        vertex, _ = current
        reversed_path.append(vertex)
        current = parent[current]
    path = tuple(reversed(reversed_path))
    collision_path = tuple(
        (repr(elements[vertex[4]]), repr(elements[vertex[5]]))
        for vertex in path
    )
    collision_path_indices = tuple(
        (vertex[4], vertex[5])
        for vertex in path
    )
    return RelativeContextualSeparationSummary(
        element_count=size,
        quotient_class_count=quotient_class_count,
        left_monoid_size=len(data.left_monoid),
        right_monoid_size=len(data.right_monoid),
        valid_vertex_count=len(valid_vertices),
        checked=True,
        skipped_reason=None,
        collision_found=True,
        collision_length=len(path),
        collision_path_indices=collision_path_indices,
        collision_path=collision_path,
    )


def identity_extension_left_translations(
    data: ContextualCompletionData,
) -> Tuple[Transformation, ...]:
    class_count = data.class_count
    identity = tuple(range(class_count))
    rows = []
    for p in range(class_count):
        row = list(identity)
        for source, target in data.partial_translations[p].items():
            row[source] = target
        rows.append(tuple(row))
    return tuple(rows)


def _identity_extension_forced_pair_closure_failures(
    data: ContextualCompletionData,
) -> int:
    rows = identity_extension_left_translations(data)
    if not all(len(set(row)) == data.class_count for row in rows):
        return data.forced_product_count
    inverses = tuple(invert_permutation(row) for row in rows)
    failures = 0
    for p, partial_row in data.partial_translations.items():
        for q, out in partial_row.items():
            conjugate = compose_transformations(
                compose_transformations(rows[p], rows[q]),
                inverses[p],
            )
            if rows[out] != conjugate:
                failures += 1
    return failures


def active_lift_existence_summary(
    data: ContextualCompletionData,
) -> ActiveLiftExistenceSummary:
    """Return finite evidence for coherent active-lift sets.

    The identity-extension rows give a concrete singleton active-lift system
    when they are total permutations and satisfy the forced-pair conjugacy
    rule.  This proves existence of active lift sets, but it does not rely on
    the previously proposed pruning operator, which is not monotone in
    general.
    """

    class_count = data.class_count
    summary = identity_extension_summary(data)
    forced_pair_failures = _identity_extension_forced_pair_closure_failures(data)
    identity_witness = (
        summary.conflict_count == 0
        and summary.partial_translations_injective
        and summary.identity_extension_total_permutations
        and forced_pair_failures == 0
    )
    return ActiveLiftExistenceSummary(
        class_count=class_count,
        identity_extension_singleton_witness=identity_witness,
        identity_extension_forced_pair_closure_failures=forced_pair_failures,
    )


def contextual_readout(
    data: ContextualCompletionData,
    word: Tuple[Hashable, ...],
) -> Tuple[int, ...]:
    element_index = data.element_index
    indexed_word = tuple(element_index[element] for element in word)
    size = len(data.elements)
    identity = tuple(range(size))
    left_index = {mapping: index for index, mapping in enumerate(data.left_monoid)}
    right_index = {mapping: index for index, mapping in enumerate(data.right_monoid)}

    left_contexts = []
    current = identity
    for x in indexed_word:
        left_contexts.append(current)
        current = compose_transformations(current, data.m_maps[x])

    right_contexts = [identity for _ in indexed_word]
    current = identity
    for index in range(len(indexed_word) - 1, -1, -1):
        right_contexts[index] = current
        current = compose_transformations(current, data.r_maps[indexed_word[index]])

    return tuple(
        data.class_of_triple[
            (
                left_index[left_contexts[index]],
                indexed_word[index],
                right_index[right_contexts[index]],
            )
        ]
        for index in range(len(indexed_word))
    )


def orbit_readout_collision(
    solution: FiniteBraidedSet,
    data: ContextualCompletionData,
    arity: int,
) -> dict[str, object] | None:
    """Return a first same-orbit contextual-readout collision, if one exists."""

    all_words = tuple(product(solution.elements, repeat=arity))
    seen = set()
    orbit_count = 0
    max_orbit_size = 0

    for start in all_words:
        if start in seen:
            continue
        orbit_count += 1
        queue = deque([start])
        seen.add(start)
        readout_owner = {contextual_readout(data, tuple(start)): start}
        orbit_size = 0
        while queue:
            current = queue.popleft()
            orbit_size += 1
            for generator in range(1, arity):
                for signed in (generator, -generator):
                    image = solution.braid_action((signed,), current)
                    image_readout = contextual_readout(data, tuple(image))
                    owner = readout_owner.get(image_readout)
                    if owner is not None and owner != image:
                        return {
                            "arity": arity,
                            "collision_readout": list(image_readout),
                            "first_word": [repr(element) for element in owner],
                            "second_word": [repr(element) for element in image],
                        }
                    readout_owner[image_readout] = image
                    if image not in seen:
                        seen.add(image)
                        queue.append(image)
        max_orbit_size = max(max_orbit_size, orbit_size)

    return {
        "arity": arity,
        "orbit_count": orbit_count,
        "max_orbit_size": max_orbit_size,
        "collision": None,
    }


def identity_extension_rack_solution(data: ContextualCompletionData) -> FiniteBraidedSet:
    left_translations = identity_extension_left_translations(data)
    if not all(len(set(row)) == data.class_count for row in left_translations):
        raise ValueError("identity extension rows are not total permutations")
    return rack_solution(
        tuple(range(data.class_count)),
        lambda left, right: left_translations[left][right],
    )


def contextual_readout_equivariance_failure(
    solution: FiniteBraidedSet,
    data: ContextualCompletionData,
    arity: int,
) -> dict[str, object] | None:
    """Return a first identity-extension rack equivariance failure."""

    rack = identity_extension_rack_solution(data)
    for word in product(solution.elements, repeat=arity):
        readout = contextual_readout(data, tuple(word))
        for generator in range(1, arity):
            for signed in (generator, -generator):
                x_image = solution.braid_action((signed,), word)
                y_image = rack.braid_action((signed,), readout)
                expected = contextual_readout(data, tuple(x_image))
                if y_image != expected:
                    return {
                        "arity": arity,
                        "generator": signed,
                        "word": [repr(element) for element in word],
                        "x_image": [repr(element) for element in x_image],
                        "readout": list(readout),
                        "rack_image": list(y_image),
                        "expected_readout": list(expected),
                    }
    return {
        "arity": arity,
        "failure": None,
    }


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
