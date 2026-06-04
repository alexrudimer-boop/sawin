from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import permutations
from typing import Iterator, Sequence

from .finite_braided_set import FiniteBraidedSet

UArray = tuple[tuple[int, ...], ...]
VArray = tuple[tuple[int, ...], ...]


@dataclass(frozen=True)
class StageAUArrayProfile:
    size: int
    balanced_symbol_counts: bool
    rows_singular: bool
    feasibility_nonempty: bool
    stage_a_candidate: bool
    minimum_feasibility_size: int
    maximum_feasibility_size: int
    feasibility_size_counts: tuple[tuple[int, int], ...]
    canonical: bool | None


@dataclass(frozen=True)
class StageAEnumerationAudit:
    size: int
    node_count: int
    completed_balanced_count: int
    row_singular_count: int
    feasibility_nonempty_count: int
    canonical_count: int
    emitted_count: int
    truncated: bool
    examples: tuple[UArray, ...]


def normalize_u_array(array: Sequence[Sequence[int]]) -> UArray:
    rows = tuple(tuple(row) for row in array)
    size = len(rows)
    if size == 0:
        raise ValueError("U array must be nonempty")
    if any(len(row) != size for row in rows):
        raise ValueError("U array must be square")
    allowed = set(range(size))
    entries = {entry for row in rows for entry in row}
    if not entries.issubset(allowed):
        raise ValueError(f"U entries must lie in {sorted(allowed)}")
    return rows


def uv_arrays_from_solution(solution: FiniteBraidedSet) -> tuple[UArray, VArray]:
    element_index = {element: index for index, element in enumerate(solution.elements)}
    u_rows = []
    v_rows = []
    for left in solution.elements:
        u_row = []
        v_row = []
        for right in solution.elements:
            out_left, out_right = solution.R[(left, right)]
            u_row.append(element_index[out_left])
            v_row.append(element_index[out_right])
        u_rows.append(tuple(u_row))
        v_rows.append(tuple(v_row))
    return tuple(u_rows), tuple(v_rows)


def u_array_from_solution(solution: FiniteBraidedSet) -> UArray:
    return uv_arrays_from_solution(solution)[0]


def balanced_symbol_counts(array: Sequence[Sequence[int]]) -> bool:
    rows = normalize_u_array(array)
    size = len(rows)
    counts = Counter(entry for row in rows for entry in row)
    return all(counts[value] == size for value in range(size))


def rows_singular(array: Sequence[Sequence[int]]) -> bool:
    rows = normalize_u_array(array)
    size = len(rows)
    return all(len(set(row)) < size for row in rows)


def compose_maps(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    if len(left) != len(right):
        raise ValueError("maps must have the same domain")
    return tuple(left[right[index]] for index in range(len(left)))


def stage_a_feasibility_sets(
    array: Sequence[Sequence[int]],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    rows = normalize_u_array(array)
    size = len(rows)
    feasibility_rows = []
    for x in range(size):
        feasibility_row = []
        for y in range(size):
            target = compose_maps(rows[x], rows[y])
            left_output = rows[x][y]
            candidates = tuple(
                v
                for v in range(size)
                if compose_maps(rows[left_output], rows[v]) == target
            )
            feasibility_row.append(candidates)
        feasibility_rows.append(tuple(feasibility_row))
    return tuple(feasibility_rows)


def stage_a_feasibility_nonempty(array: Sequence[Sequence[int]]) -> bool:
    return all(
        bool(candidates)
        for row in stage_a_feasibility_sets(array)
        for candidates in row
    )


def relabel_u_array(array: Sequence[Sequence[int]], permutation: Sequence[int]) -> UArray:
    rows = normalize_u_array(array)
    size = len(rows)
    perm = tuple(permutation)
    if sorted(perm) != list(range(size)):
        raise ValueError("permutation must relabel the U array domain")
    inverse = [0] * size
    for old, new in enumerate(perm):
        inverse[new] = old
    return tuple(
        tuple(perm[rows[inverse[x]][inverse[y]]] for y in range(size))
        for x in range(size)
    )


def u_array_word(array: Sequence[Sequence[int]]) -> tuple[int, ...]:
    rows = normalize_u_array(array)
    return tuple(entry for row in rows for entry in row)


def canonical_u_array(array: Sequence[Sequence[int]]) -> UArray:
    rows = normalize_u_array(array)
    size = len(rows)
    return min(
        (relabel_u_array(rows, perm) for perm in permutations(range(size))),
        key=u_array_word,
    )


def is_canonical_u_array(array: Sequence[Sequence[int]]) -> bool:
    rows = normalize_u_array(array)
    return rows == canonical_u_array(rows)


def stage_a_profile_from_u(
    array: Sequence[Sequence[int]],
    *,
    canonicalize: bool = True,
) -> StageAUArrayProfile:
    rows = normalize_u_array(array)
    feasibility = stage_a_feasibility_sets(rows)
    sizes = tuple(len(candidates) for row in feasibility for candidates in row)
    size_counts = tuple(sorted(Counter(sizes).items()))
    balanced = balanced_symbol_counts(rows)
    singular = rows_singular(rows)
    nonempty = all(size > 0 for size in sizes)
    canonical = is_canonical_u_array(rows) if canonicalize else None
    return StageAUArrayProfile(
        size=len(rows),
        balanced_symbol_counts=balanced,
        rows_singular=singular,
        feasibility_nonempty=nonempty,
        stage_a_candidate=balanced and singular and nonempty,
        minimum_feasibility_size=min(sizes),
        maximum_feasibility_size=max(sizes),
        feasibility_size_counts=size_counts,
        canonical=canonical,
    )


def stage_a_profile_from_solution(
    solution: FiniteBraidedSet,
    *,
    canonicalize: bool = True,
) -> StageAUArrayProfile:
    return stage_a_profile_from_u(
        u_array_from_solution(solution),
        canonicalize=canonicalize,
    )


def enumerate_stage_a_u_arrays(
    size: int,
    *,
    canonical_only: bool = True,
    max_nodes: int | None = None,
) -> Iterator[UArray]:
    audit = stage_a_enumeration_audit(
        size,
        canonical_only=canonical_only,
        max_nodes=max_nodes,
        max_examples=None,
    )
    yield from audit.examples


def stage_a_enumeration_audit(
    size: int,
    *,
    canonical_only: bool = True,
    max_nodes: int | None = None,
    max_examples: int | None = 20,
) -> StageAEnumerationAudit:
    if size <= 0:
        raise ValueError("size must be positive")
    if max_nodes is not None and max_nodes < 0:
        raise ValueError("max_nodes must be nonnegative")
    if max_examples is not None and max_examples < 0:
        raise ValueError("max_examples must be nonnegative")

    total_cells = size * size
    entries = [-1] * total_cells
    counts = [0] * size
    row_seen = [0] * size
    row_has_duplicate = [False] * size
    node_count = 0
    completed_balanced_count = 0
    row_singular_count = 0
    feasibility_nonempty_count = 0
    canonical_count = 0
    examples: list[UArray] = []
    truncated = False

    def can_still_balance(next_position: int) -> bool:
        remaining = total_cells - next_position
        return all(count <= size and count + remaining >= size for count in counts)

    def current_array() -> UArray:
        return tuple(
            tuple(entries[row * size + col] for col in range(size))
            for row in range(size)
        )

    def record_if_candidate() -> None:
        nonlocal completed_balanced_count
        nonlocal row_singular_count
        nonlocal feasibility_nonempty_count
        nonlocal canonical_count

        array = current_array()
        if not balanced_symbol_counts(array):
            return
        completed_balanced_count += 1
        if not rows_singular(array):
            return
        row_singular_count += 1
        if not stage_a_feasibility_nonempty(array):
            return
        feasibility_nonempty_count += 1
        if canonical_only and not is_canonical_u_array(array):
            return
        canonical_count += 1
        if max_examples is None or len(examples) < max_examples:
            examples.append(array)

    def search(position: int) -> None:
        nonlocal node_count
        nonlocal truncated

        if truncated:
            return
        if max_nodes is not None and node_count >= max_nodes:
            truncated = True
            return
        node_count += 1

        if position == total_cells:
            record_if_candidate()
            return

        row = position // size
        is_row_end = position % size == size - 1
        for value in range(size):
            if counts[value] >= size:
                continue

            old_seen = row_seen[row]
            old_duplicate = row_has_duplicate[row]
            bit = 1 << value
            entries[position] = value
            counts[value] += 1
            row_has_duplicate[row] = old_duplicate or bool(old_seen & bit)
            row_seen[row] = old_seen | bit

            row_ok = True
            if is_row_end and not row_has_duplicate[row]:
                row_ok = False
            if row_ok and can_still_balance(position + 1):
                search(position + 1)

            row_seen[row] = old_seen
            row_has_duplicate[row] = old_duplicate
            counts[value] -= 1
            entries[position] = -1
            if truncated:
                break

    search(0)
    return StageAEnumerationAudit(
        size=size,
        node_count=node_count,
        completed_balanced_count=completed_balanced_count,
        row_singular_count=row_singular_count,
        feasibility_nonempty_count=feasibility_nonempty_count,
        canonical_count=canonical_count,
        emitted_count=len(examples),
        truncated=truncated,
        examples=tuple(examples),
    )
