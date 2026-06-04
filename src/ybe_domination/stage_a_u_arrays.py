from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import permutations
from typing import Sequence

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
