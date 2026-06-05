from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from itertools import permutations, product
from typing import Iterator, Sequence

from .finite_braided_set import FiniteBraidedSet

UArray = tuple[tuple[int, ...], ...]
VArray = tuple[tuple[int, ...], ...]
Cell = tuple[int, int]


@dataclass(frozen=True)
class StageABucket:
    output_u: int
    composition_id: int
    cells: tuple[Cell, ...]
    values: tuple[int, ...]


@dataclass(frozen=True)
class StageAUArrayProfile:
    size: int
    balanced_symbol_counts: bool
    rows_singular: bool
    feasibility_nonempty: bool
    multiset_factorization: bool
    stage_a_candidate: bool
    minimum_feasibility_size: int
    maximum_feasibility_size: int
    feasibility_size_counts: tuple[tuple[int, int], ...]
    bucket_count: int
    maximum_bucket_size: int
    canonical: bool | None


@dataclass(frozen=True)
class StageAEnumerationAudit:
    size: int
    node_count: int
    completed_balanced_count: int
    row_singular_count: int
    feasibility_nonempty_count: int
    multiset_factorization_count: int
    canonical_count: int
    emitted_count: int
    truncated: bool
    examples: tuple[UArray, ...]


@dataclass(frozen=True)
class StageBVExactCoverAudit:
    size: int
    node_count: int
    exact_cover_count: int
    column_singular_count: int
    y2_y3_count: int
    noninvolutive_count: int
    accepted_count: int
    emitted_count: int
    truncated: bool
    examples: tuple[VArray, ...]


@dataclass(frozen=True)
class StageBBucketCSPProfile:
    size: int
    variable_count: int
    bucket_count: int
    domain_size_counts: tuple[tuple[int, int], ...]
    forced_variable_count: int
    maximum_domain_size: int
    hall_all_different_ok: bool
    unsupported_y2_y3_triple_count: int
    locally_consistent: bool


@dataclass(frozen=True)
class StageBGACPropagationAudit:
    size: int
    variable_count: int
    bucket_count: int
    initial_domain_size_counts: tuple[tuple[int, int], ...]
    final_domain_size_counts: tuple[tuple[int, int], ...]
    initial_domain_mass: int
    final_domain_mass: int
    hall_value_deletion_count: int
    unsupported_value_deletion_count: int
    iteration_count: int
    forced_variable_count: int
    unresolved_variable_count: int
    maximum_domain_size: int
    hall_contradiction: bool
    empty_domain: bool
    all_singleton: bool
    singleton_y2_y3_verified: bool | None
    locally_consistent: bool
    domains: tuple[tuple[tuple[int, ...], ...], ...]
    extracted_v: VArray | None


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


def normalize_v_array(array: Sequence[Sequence[int]], *, size: int | None = None) -> VArray:
    rows = tuple(tuple(row) for row in array)
    if size is None:
        size = len(rows)
    if size == 0:
        raise ValueError("V array must be nonempty")
    if len(rows) != size or any(len(row) != size for row in rows):
        raise ValueError("V array must be square with the requested size")
    allowed = set(range(size))
    entries = {entry for row in rows for entry in row}
    if not entries.issubset(allowed):
        raise ValueError(f"V entries must lie in {sorted(allowed)}")
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


def solution_from_uv_arrays(
    u_array: Sequence[Sequence[int]],
    v_array: Sequence[Sequence[int]],
) -> FiniteBraidedSet:
    u_rows = normalize_u_array(u_array)
    v_rows = normalize_v_array(v_array, size=len(u_rows))
    size = len(u_rows)
    elements = tuple(range(size))
    return FiniteBraidedSet(
        elements,
        {
            (x, y): (u_rows[x][y], v_rows[x][y])
            for x in elements
            for y in elements
        },
    )


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


def transformation_id(mapping: Sequence[int], *, size: int | None = None) -> int:
    values = tuple(mapping)
    if size is None:
        size = len(values)
    if size <= 0:
        raise ValueError("size must be positive")
    if any(value < 0 or value >= size for value in values):
        raise ValueError("mapping values must lie in the requested domain")
    out = 0
    place = 1
    for value in values:
        out += value * place
        place *= size
    return out


def composition_id(
    left: Sequence[int],
    right: Sequence[int],
    *,
    size: int | None = None,
) -> int:
    values = compose_maps(left, right)
    return transformation_id(values, size=size)


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


def stage_a_multiset_factorization_holds(array: Sequence[Sequence[int]]) -> bool:
    rows = normalize_u_array(array)
    size = len(rows)
    for output_u in range(size):
        cell_products = Counter(
            composition_id(rows[x], rows[y], size=size)
            for x in range(size)
            for y in range(size)
            if rows[x][y] == output_u
        )
        target_products = Counter(
            composition_id(rows[output_u], rows[v], size=size)
            for v in range(size)
        )
        if cell_products != target_products:
            return False
    return True


def stage_a_factorization_buckets(
    array: Sequence[Sequence[int]],
) -> tuple[StageABucket, ...]:
    rows = normalize_u_array(array)
    size = len(rows)
    cell_buckets: dict[tuple[int, int], list[Cell]] = {}
    value_buckets: dict[tuple[int, int], list[int]] = {}
    for x in range(size):
        for y in range(size):
            output_u = rows[x][y]
            product_id = composition_id(rows[x], rows[y], size=size)
            cell_buckets.setdefault((output_u, product_id), []).append((x, y))
    for output_u in range(size):
        for value in range(size):
            product_id = composition_id(rows[output_u], rows[value], size=size)
            value_buckets.setdefault((output_u, product_id), []).append(value)

    keys = sorted(set(cell_buckets).union(value_buckets))
    buckets = []
    for output_u, product_id in keys:
        cells = tuple(cell_buckets.get((output_u, product_id), ()))
        values = tuple(value_buckets.get((output_u, product_id), ()))
        if len(cells) != len(values):
            raise ValueError("U array does not satisfy multiset factorization")
        if cells:
            buckets.append(
                StageABucket(
                    output_u=output_u,
                    composition_id=product_id,
                    cells=cells,
                    values=values,
                )
            )
    return tuple(buckets)


def stage_a_bucket_domains(
    array: Sequence[Sequence[int]],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    rows = normalize_u_array(array)
    size = len(rows)
    domains = [[tuple() for _y in range(size)] for _x in range(size)]
    for bucket in stage_a_factorization_buckets(rows):
        for x, y in bucket.cells:
            domains[x][y] = bucket.values
    return tuple(tuple(row) for row in domains)


def _assign_domain_value(
    assignment: dict[Cell, int],
    domains: Sequence[Sequence[Sequence[int]]],
    cell: Cell,
    value: int,
) -> bool:
    x, y = cell
    if value not in domains[x][y]:
        return False
    old = assignment.get(cell)
    if old is not None:
        return old == value
    assignment[cell] = value
    return True


def stage_b_bucket_triple_has_support(
    array: Sequence[Sequence[int]],
    domains: Sequence[Sequence[Sequence[int]]],
    triple: tuple[int, int, int],
) -> bool:
    u_rows = normalize_u_array(array)
    size = len(u_rows)
    x, y, z = triple
    x_uyz_cell = (x, u_rows[y][z])
    yz_cell = (y, z)
    xy_cell = (x, y)
    for v_xy in domains[x][y]:
        left_y2_cell = (u_rows[x][y], u_rows[v_xy][z])
        left_y3_cell = (v_xy, z)
        for v_x_uyz in domains[x_uyz_cell[0]][x_uyz_cell[1]]:
            for v_yz in domains[y][z]:
                right_y2 = u_rows[v_x_uyz][v_yz]
                right_y3_cell = (v_x_uyz, v_yz)
                base = {}
                if not _assign_domain_value(base, domains, xy_cell, v_xy):
                    continue
                if not _assign_domain_value(base, domains, x_uyz_cell, v_x_uyz):
                    continue
                if not _assign_domain_value(base, domains, yz_cell, v_yz):
                    continue
                if not _assign_domain_value(base, domains, left_y2_cell, right_y2):
                    continue
                for y3_value in range(size):
                    assignment = dict(base)
                    if not _assign_domain_value(
                        assignment,
                        domains,
                        left_y3_cell,
                        y3_value,
                    ):
                        continue
                    if _assign_domain_value(
                        assignment,
                        domains,
                        right_y3_cell,
                        y3_value,
                    ):
                        return True
    return False


def _domain_size_counts(
    domains: Sequence[Sequence[Sequence[int]]],
) -> tuple[tuple[int, int], ...]:
    sizes = tuple(len(cell_domain) for row in domains for cell_domain in row)
    return tuple(sorted(Counter(sizes).items()))


def _domain_mass(domains: Sequence[Sequence[Sequence[int]]]) -> int:
    return sum(len(cell_domain) for row in domains for cell_domain in row)


def _frozen_domains(
    domains: Sequence[Sequence[set[int]]],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    return tuple(
        tuple(tuple(sorted(cell_domain)) for cell_domain in row)
        for row in domains
    )


def _domain_sets(
    domains: Sequence[Sequence[Sequence[int]]],
) -> list[list[set[int]]]:
    return [[set(cell_domain) for cell_domain in row] for row in domains]


def _normalize_domains(
    domains: Sequence[Sequence[Sequence[int]]],
    *,
    size: int,
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    if len(domains) != size:
        raise ValueError("domain array must have one row per U row")
    normalized_rows = []
    allowed = set(range(size))
    for row in domains:
        if len(row) != size:
            raise ValueError("domain array must be square")
        normalized_row = []
        for cell_domain in row:
            values = tuple(sorted(set(cell_domain)))
            if any(value not in allowed for value in values):
                raise ValueError("domain values must lie in the U domain")
            normalized_row.append(values)
        normalized_rows.append(tuple(normalized_row))
    return tuple(normalized_rows)


def _intersect_domains(
    left: Sequence[Sequence[Sequence[int]]],
    right: Sequence[Sequence[Sequence[int]]],
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    size = len(left)
    rows = []
    for x in range(size):
        row = []
        for y in range(size):
            row.append(tuple(sorted(set(left[x][y]).intersection(right[x][y]))))
        rows.append(tuple(row))
    return tuple(rows)


def stage_b_gac_dynamic_universe(
    array: Sequence[Sequence[int]],
    domains: Sequence[Sequence[Sequence[int]]],
    triple: tuple[int, int, int],
) -> tuple[Cell, ...]:
    u_rows = normalize_u_array(array)
    x, y, z = triple
    core_x_uyz = (x, u_rows[y][z])
    cells: set[Cell] = {(x, y), core_x_uyz, (y, z)}
    output_u = u_rows[x][y]
    for value_xy in domains[x][y]:
        cells.add((output_u, u_rows[value_xy][z]))
        cells.add((value_xy, z))
    for value_x_uyz in domains[core_x_uyz[0]][core_x_uyz[1]]:
        for value_yz in domains[y][z]:
            cells.add((value_x_uyz, value_yz))
    return tuple(sorted(cells))


def _stage_b_bucket_triple_value_has_support_for_rows(
    u_rows: UArray,
    domains: Sequence[Sequence[Sequence[int]]],
    triple: tuple[int, int, int],
    tested_cell: Cell,
    tested_value: int,
) -> bool:
    size = len(u_rows)
    x, y, z = triple
    output_u = u_rows[x][y]
    xy_cell = (x, y)
    x_uyz_cell = (x, u_rows[y][z])
    yz_cell = (y, z)
    for value_xy in domains[x][y]:
        left_y2_cell = (output_u, u_rows[value_xy][z])
        left_y3_cell = (value_xy, z)
        for value_x_uyz in domains[x_uyz_cell[0]][x_uyz_cell[1]]:
            for value_yz in domains[y][z]:
                right_y2 = u_rows[value_x_uyz][value_yz]
                right_y3_cell = (value_x_uyz, value_yz)
                base: dict[Cell, int] = {}
                if not _assign_domain_value(base, domains, xy_cell, value_xy):
                    continue
                if not _assign_domain_value(
                    base,
                    domains,
                    x_uyz_cell,
                    value_x_uyz,
                ):
                    continue
                if not _assign_domain_value(base, domains, yz_cell, value_yz):
                    continue
                if not _assign_domain_value(
                    base,
                    domains,
                    left_y2_cell,
                    right_y2,
                ):
                    continue
                for y3_value in range(size):
                    assignment = dict(base)
                    if not _assign_domain_value(
                        assignment,
                        domains,
                        left_y3_cell,
                        y3_value,
                    ):
                        continue
                    if not _assign_domain_value(
                        assignment,
                        domains,
                        right_y3_cell,
                        y3_value,
                    ):
                        continue
                    assigned_value = assignment.get(tested_cell)
                    if assigned_value is None or assigned_value == tested_value:
                        return True
    return False


def stage_b_bucket_triple_value_has_support(
    array: Sequence[Sequence[int]],
    domains: Sequence[Sequence[Sequence[int]]],
    triple: tuple[int, int, int],
    tested_cell: Cell,
    tested_value: int,
) -> bool:
    u_rows = normalize_u_array(array)
    x, y = tested_cell
    if tested_value not in domains[x][y]:
        return False
    return _stage_b_bucket_triple_value_has_support_for_rows(
        u_rows,
        domains,
        triple,
        tested_cell,
        tested_value,
    )


def _enforce_bucket_hall_filtering(
    domains: list[list[set[int]]],
    buckets: Sequence[StageABucket],
) -> tuple[bool, int]:
    deletion_count = 0
    for bucket in buckets:
        cells = tuple(bucket.cells)
        cell_count = len(cells)
        for mask in range(1, 1 << cell_count):
            subset_values: set[int] = set()
            subset_size = 0
            for index, cell in enumerate(cells):
                if mask & (1 << index):
                    subset_size += 1
                    subset_values.update(domains[cell[0]][cell[1]])
            if len(subset_values) < subset_size:
                return False, deletion_count
            if len(subset_values) == subset_size:
                for index, cell in enumerate(cells):
                    if mask & (1 << index):
                        continue
                    cell_domain = domains[cell[0]][cell[1]]
                    before = len(cell_domain)
                    cell_domain.difference_update(subset_values)
                    deletion_count += before - len(cell_domain)
                    if not cell_domain:
                        return False, deletion_count
    return True, deletion_count


def _enforce_triple_gac_filtering(
    u_rows: UArray,
    domains: list[list[set[int]]],
    triple: tuple[int, int, int],
) -> tuple[bool, int]:
    deletion_count = 0
    frozen = _frozen_domains(domains)
    for cell in stage_b_gac_dynamic_universe(u_rows, frozen, triple):
        x, y = cell
        for value in tuple(domains[x][y]):
            current = _frozen_domains(domains)
            if not _stage_b_bucket_triple_value_has_support_for_rows(
                u_rows,
                current,
                triple,
                cell,
                value,
            ):
                domains[x][y].remove(value)
                deletion_count += 1
                if not domains[x][y]:
                    return False, deletion_count
    return True, deletion_count


def _domains_extract_v(
    domains: Sequence[Sequence[Sequence[int]]],
) -> VArray | None:
    rows = []
    for domain_row in domains:
        values = []
        for cell_domain in domain_row:
            if len(cell_domain) != 1:
                return None
            values.append(tuple(cell_domain)[0])
        rows.append(tuple(values))
    return tuple(rows)


def stage_b_gac_propagation_audit(
    array: Sequence[Sequence[int]],
    initial_domains: Sequence[Sequence[Sequence[int]]] | None = None,
) -> StageBGACPropagationAudit:
    u_rows = normalize_u_array(array)
    size = len(u_rows)
    variable_count = size * size
    empty_domains: tuple[tuple[tuple[int, ...], ...], ...] = tuple(
        tuple(tuple() for _y in range(size)) for _x in range(size)
    )
    if not stage_a_multiset_factorization_holds(u_rows):
        return StageBGACPropagationAudit(
            size=size,
            variable_count=variable_count,
            bucket_count=0,
            initial_domain_size_counts=tuple(),
            final_domain_size_counts=tuple(),
            initial_domain_mass=0,
            final_domain_mass=0,
            hall_value_deletion_count=0,
            unsupported_value_deletion_count=0,
            iteration_count=0,
            forced_variable_count=0,
            unresolved_variable_count=variable_count,
            maximum_domain_size=0,
            hall_contradiction=True,
            empty_domain=True,
            all_singleton=False,
            singleton_y2_y3_verified=None,
            locally_consistent=False,
            domains=empty_domains,
            extracted_v=None,
        )

    buckets = stage_a_factorization_buckets(u_rows)
    bucket_domains = stage_a_bucket_domains(u_rows)
    if initial_domains is None:
        starting_domains = bucket_domains
    else:
        normalized_initial_domains = _normalize_domains(initial_domains, size=size)
        starting_domains = _intersect_domains(bucket_domains, normalized_initial_domains)
    domains = _domain_sets(starting_domains)
    initial_mass = _domain_mass(starting_domains)
    hall_deletions = 0
    unsupported_deletions = 0
    hall_contradiction = False
    empty_domain = False
    iteration_count = 0

    while True:
        iteration_count += 1
        before_mass = _domain_mass(_frozen_domains(domains))
        hall_ok, deleted = _enforce_bucket_hall_filtering(domains, buckets)
        hall_deletions += deleted
        if not hall_ok:
            hall_contradiction = True
            empty_domain = any(not cell_domain for row in domains for cell_domain in row)
            break
        for x in range(size):
            for y in range(size):
                for z in range(size):
                    triple_ok, deleted = _enforce_triple_gac_filtering(
                        u_rows,
                        domains,
                        (x, y, z),
                    )
                    unsupported_deletions += deleted
                    if not triple_ok:
                        empty_domain = True
                        break
                if empty_domain:
                    break
            if empty_domain:
                break
        after_mass = _domain_mass(_frozen_domains(domains))
        if empty_domain or after_mass == before_mass:
            break

    final_domains = _frozen_domains(domains)
    final_sizes = tuple(len(final_domains[x][y]) for x in range(size) for y in range(size))
    extracted_v = _domains_extract_v(final_domains)
    singleton_y2_y3_verified = (
        uv_y2_y3_hold(u_rows, extracted_v) if extracted_v is not None else None
    )
    locally_consistent = (
        not hall_contradiction
        and not empty_domain
        and (singleton_y2_y3_verified is not False)
    )
    return StageBGACPropagationAudit(
        size=size,
        variable_count=variable_count,
        bucket_count=len(buckets),
        initial_domain_size_counts=_domain_size_counts(starting_domains),
        final_domain_size_counts=_domain_size_counts(final_domains),
        initial_domain_mass=initial_mass,
        final_domain_mass=_domain_mass(final_domains),
        hall_value_deletion_count=hall_deletions,
        unsupported_value_deletion_count=unsupported_deletions,
        iteration_count=iteration_count,
        forced_variable_count=sum(1 for size_ in final_sizes if size_ == 1),
        unresolved_variable_count=sum(1 for size_ in final_sizes if size_ > 1),
        maximum_domain_size=max(final_sizes) if final_sizes else 0,
        hall_contradiction=hall_contradiction,
        empty_domain=empty_domain,
        all_singleton=extracted_v is not None,
        singleton_y2_y3_verified=singleton_y2_y3_verified,
        locally_consistent=locally_consistent,
        domains=final_domains,
        extracted_v=extracted_v,
    )


def _stage_b_branch_domains(
    domains: Sequence[Sequence[Sequence[int]]],
    buckets: Sequence[StageABucket],
    cell: Cell,
    value: int,
) -> tuple[tuple[tuple[int, ...], ...], ...]:
    domain_sets = _domain_sets(domains)
    x, y = cell
    domain_sets[x][y] = {value}
    for bucket in buckets:
        if cell not in bucket.cells:
            continue
        for other in bucket.cells:
            if other == cell:
                continue
            domain_sets[other[0]][other[1]].discard(value)
        break
    return _frozen_domains(domain_sets)


def _stage_b_choose_branch_cell(
    domains: Sequence[Sequence[Sequence[int]]],
) -> Cell | None:
    best_cell = None
    best_size = len(domains) + 1
    for x, row in enumerate(domains):
        for y, cell_domain in enumerate(row):
            domain_size = len(cell_domain)
            if 1 < domain_size < best_size:
                best_cell = (x, y)
                best_size = domain_size
    return best_cell


def stage_b_gac_v_search_audit(
    u_array: Sequence[Sequence[int]],
    *,
    require_column_singular: bool = True,
    require_noninvolutive: bool = False,
    max_nodes: int | None = None,
    max_examples: int | None = 20,
) -> StageBVExactCoverAudit:
    u_rows = normalize_u_array(u_array)
    size = len(u_rows)
    if max_nodes is not None and max_nodes < 0:
        raise ValueError("max_nodes must be nonnegative")
    if max_examples is not None and max_examples < 0:
        raise ValueError("max_examples must be nonnegative")

    if (
        not balanced_symbol_counts(u_rows)
        or not stage_a_feasibility_nonempty(u_rows)
        or not stage_a_multiset_factorization_holds(u_rows)
    ):
        return StageBVExactCoverAudit(
            size=size,
            node_count=0,
            exact_cover_count=0,
            column_singular_count=0,
            y2_y3_count=0,
            noninvolutive_count=0,
            accepted_count=0,
            emitted_count=0,
            truncated=False,
            examples=tuple(),
        )

    buckets = stage_a_factorization_buckets(u_rows)
    node_count = 0
    exact_cover_count = 0
    column_singular_count = 0
    y2_y3_count = 0
    noninvolutive_count = 0
    accepted_count = 0
    examples: list[VArray] = []
    truncated = False

    def record_if_complete(v_rows: VArray) -> None:
        nonlocal exact_cover_count
        nonlocal column_singular_count
        nonlocal y2_y3_count
        nonlocal noninvolutive_count
        nonlocal accepted_count

        if not uv_pair_orthogonal(u_rows, v_rows):
            return
        exact_cover_count += 1
        column_singular = v_columns_singular(v_rows)
        if column_singular:
            column_singular_count += 1
        if require_column_singular and not column_singular:
            return
        if not uv_y2_y3_hold(u_rows, v_rows):
            return
        y2_y3_count += 1
        noninvolutive = not uv_is_involutive(u_rows, v_rows)
        if noninvolutive:
            noninvolutive_count += 1
        if require_noninvolutive and not noninvolutive:
            return
        accepted_count += 1
        if max_examples is None or len(examples) < max_examples:
            examples.append(v_rows)

    def search(domains: Sequence[Sequence[Sequence[int]]]) -> None:
        nonlocal node_count
        nonlocal truncated

        if truncated:
            return
        if max_nodes is not None and node_count >= max_nodes:
            truncated = True
            return
        node_count += 1

        gac = stage_b_gac_propagation_audit(u_rows, domains)
        if not gac.locally_consistent:
            return
        v_rows = gac.extracted_v
        if v_rows is not None:
            record_if_complete(v_rows)
            return
        cell = _stage_b_choose_branch_cell(gac.domains)
        if cell is None:
            return
        x, y = cell
        for value in gac.domains[x][y]:
            branch_domains = _stage_b_branch_domains(gac.domains, buckets, cell, value)
            search(branch_domains)
            if truncated:
                break

    search(stage_a_bucket_domains(u_rows))
    return StageBVExactCoverAudit(
        size=size,
        node_count=node_count,
        exact_cover_count=exact_cover_count,
        column_singular_count=column_singular_count,
        y2_y3_count=y2_y3_count,
        noninvolutive_count=noninvolutive_count,
        accepted_count=accepted_count,
        emitted_count=len(examples),
        truncated=truncated,
        examples=tuple(examples),
    )


def stage_b_hall_all_different_ok(
    array: Sequence[Sequence[int]],
    domains: Sequence[Sequence[Sequence[int]]],
) -> bool:
    u_rows = normalize_u_array(array)
    size = len(u_rows)
    for output_u in range(size):
        cells = [
            (x, y)
            for x in range(size)
            for y in range(size)
            if u_rows[x][y] == output_u
        ]
        for mask in range(1, 1 << len(cells)):
            union_values = set()
            subset_size = 0
            for index, cell in enumerate(cells):
                if mask & (1 << index):
                    subset_size += 1
                    union_values.update(domains[cell[0]][cell[1]])
            if len(union_values) < subset_size:
                return False
    return True


def stage_b_bucket_csp_profile(
    array: Sequence[Sequence[int]],
) -> StageBBucketCSPProfile:
    u_rows = normalize_u_array(array)
    size = len(u_rows)
    if not stage_a_multiset_factorization_holds(u_rows):
        return StageBBucketCSPProfile(
            size=size,
            variable_count=size * size,
            bucket_count=0,
            domain_size_counts=tuple(),
            forced_variable_count=0,
            maximum_domain_size=0,
            hall_all_different_ok=False,
            unsupported_y2_y3_triple_count=size**3,
            locally_consistent=False,
        )
    buckets = stage_a_factorization_buckets(u_rows)
    domains = stage_a_bucket_domains(u_rows)
    domain_sizes = tuple(len(domains[x][y]) for x in range(size) for y in range(size))
    hall_ok = stage_b_hall_all_different_ok(u_rows, domains)
    unsupported = 0
    for x in range(size):
        for y in range(size):
            for z in range(size):
                if not stage_b_bucket_triple_has_support(u_rows, domains, (x, y, z)):
                    unsupported += 1
    return StageBBucketCSPProfile(
        size=size,
        variable_count=size * size,
        bucket_count=len(buckets),
        domain_size_counts=tuple(sorted(Counter(domain_sizes).items())),
        forced_variable_count=sum(1 for size_ in domain_sizes if size_ == 1),
        maximum_domain_size=max(domain_sizes) if domain_sizes else 0,
        hall_all_different_ok=hall_ok,
        unsupported_y2_y3_triple_count=unsupported,
        locally_consistent=hall_ok and unsupported == 0,
    )


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
    multiset_factorization = stage_a_multiset_factorization_holds(rows)
    buckets: tuple[StageABucket, ...] = tuple()
    if multiset_factorization:
        buckets = stage_a_factorization_buckets(rows)
    bucket_sizes = tuple(len(bucket.cells) for bucket in buckets)
    canonical = is_canonical_u_array(rows) if canonicalize else None
    return StageAUArrayProfile(
        size=len(rows),
        balanced_symbol_counts=balanced,
        rows_singular=singular,
        feasibility_nonempty=nonempty,
        multiset_factorization=multiset_factorization,
        stage_a_candidate=balanced and singular and nonempty and multiset_factorization,
        minimum_feasibility_size=min(sizes),
        maximum_feasibility_size=max(sizes),
        feasibility_size_counts=size_counts,
        bucket_count=len(buckets),
        maximum_bucket_size=max(bucket_sizes) if bucket_sizes else 0,
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
    multiset_factorization_count = 0
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
        nonlocal multiset_factorization_count
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
        if not stage_a_multiset_factorization_holds(array):
            return
        multiset_factorization_count += 1
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
        multiset_factorization_count=multiset_factorization_count,
        canonical_count=canonical_count,
        emitted_count=len(examples),
        truncated=truncated,
        examples=tuple(examples),
    )


def singular_transformations(size: int) -> tuple[tuple[int, ...], ...]:
    if size <= 0:
        raise ValueError("size must be positive")
    return tuple(
        mapping
        for mapping in product(range(size), repeat=size)
        if len(set(mapping)) < size
    )


def transformation_symbol_counts(mapping: Sequence[int], *, size: int | None = None) -> tuple[int, ...]:
    values = tuple(mapping)
    if size is None:
        size = len(values)
    counts = [0] * size
    for value in values:
        if value < 0 or value >= size:
            raise ValueError("mapping values must lie in the requested domain")
        counts[value] += 1
    return tuple(counts)


def row_catalogue_stage_a_enumeration_audit(
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

    rows = singular_transformations(size)
    row_counts = tuple(transformation_symbol_counts(row, size=size) for row in rows)
    assigned: list[tuple[int, ...]] = []
    counts = [0] * size
    node_count = 0
    completed_balanced_count = 0
    feasibility_nonempty_count = 0
    multiset_factorization_count = 0
    canonical_count = 0
    examples: list[UArray] = []
    truncated = False

    def can_still_balance(depth: int) -> bool:
        remaining_rows = size - depth
        return all(count <= size and count + remaining_rows * size >= size for count in counts)

    def record_if_candidate() -> None:
        nonlocal completed_balanced_count
        nonlocal feasibility_nonempty_count
        nonlocal multiset_factorization_count
        nonlocal canonical_count

        array = tuple(assigned)
        if any(count != size for count in counts):
            return
        completed_balanced_count += 1
        if not stage_a_feasibility_nonempty(array):
            return
        feasibility_nonempty_count += 1
        if not stage_a_multiset_factorization_holds(array):
            return
        multiset_factorization_count += 1
        if canonical_only and not is_canonical_u_array(array):
            return
        canonical_count += 1
        if max_examples is None or len(examples) < max_examples:
            examples.append(array)

    def search(depth: int) -> None:
        nonlocal node_count
        nonlocal truncated

        if truncated:
            return
        if max_nodes is not None and node_count >= max_nodes:
            truncated = True
            return
        node_count += 1

        if depth == size:
            record_if_candidate()
            return

        for row, count_vector in zip(rows, row_counts):
            if any(counts[value] + count_vector[value] > size for value in range(size)):
                continue
            for value in range(size):
                counts[value] += count_vector[value]
            assigned.append(row)
            if can_still_balance(depth + 1):
                search(depth + 1)
            assigned.pop()
            for value in range(size):
                counts[value] -= count_vector[value]
            if truncated:
                break

    search(0)
    return StageAEnumerationAudit(
        size=size,
        node_count=node_count,
        completed_balanced_count=completed_balanced_count,
        row_singular_count=completed_balanced_count,
        feasibility_nonempty_count=feasibility_nonempty_count,
        multiset_factorization_count=multiset_factorization_count,
        canonical_count=canonical_count,
        emitted_count=len(examples),
        truncated=truncated,
        examples=tuple(examples),
    )


def uv_pair_orthogonal(
    u_array: Sequence[Sequence[int]],
    v_array: Sequence[Sequence[int]],
) -> bool:
    u_rows = normalize_u_array(u_array)
    v_rows = normalize_v_array(v_array, size=len(u_rows))
    size = len(u_rows)
    pairs = {
        (u_rows[x][y], v_rows[x][y])
        for x in range(size)
        for y in range(size)
    }
    return len(pairs) == size * size


def v_columns_singular(v_array: Sequence[Sequence[int]]) -> bool:
    v_rows = normalize_v_array(v_array)
    size = len(v_rows)
    return all(
        len({v_rows[x][y] for x in range(size)}) < size
        for y in range(size)
    )


def uv_y2_y3_hold(
    u_array: Sequence[Sequence[int]],
    v_array: Sequence[Sequence[int]],
) -> bool:
    u_rows = normalize_u_array(u_array)
    v_rows = normalize_v_array(v_array, size=len(u_rows))
    size = len(u_rows)
    for x in range(size):
        for y in range(size):
            for z in range(size):
                left_y2 = v_rows[u_rows[x][y]][u_rows[v_rows[x][y]][z]]
                right_y2 = u_rows[v_rows[x][u_rows[y][z]]][v_rows[y][z]]
                if left_y2 != right_y2:
                    return False
                left_y3 = v_rows[v_rows[x][y]][z]
                right_y3 = v_rows[v_rows[x][u_rows[y][z]]][v_rows[y][z]]
                if left_y3 != right_y3:
                    return False
    return True


def uv_is_involutive(
    u_array: Sequence[Sequence[int]],
    v_array: Sequence[Sequence[int]],
) -> bool:
    u_rows = normalize_u_array(u_array)
    v_rows = normalize_v_array(v_array, size=len(u_rows))
    size = len(u_rows)
    return all(
        (u_rows[u_rows[x][y]][v_rows[x][y]], v_rows[u_rows[x][y]][v_rows[x][y]])
        == (x, y)
        for x in range(size)
        for y in range(size)
    )


def _partial_y2_y3_consistent(
    u_rows: UArray,
    entries: Sequence[int],
) -> bool:
    size = len(u_rows)

    def value(row: int, col: int) -> int:
        return entries[row * size + col]

    for x in range(size):
        for y in range(size):
            for z in range(size):
                v_xy = value(x, y)
                if v_xy != -1:
                    left_y2_col = u_rows[v_xy][z]
                    left_y2 = value(u_rows[x][y], left_y2_col)
                    v_x_uyz = value(x, u_rows[y][z])
                    v_yz = value(y, z)
                    if left_y2 != -1 and v_x_uyz != -1 and v_yz != -1:
                        right_y2 = u_rows[v_x_uyz][v_yz]
                        if left_y2 != right_y2:
                            return False

                    left_y3 = value(v_xy, z)
                    if left_y3 != -1 and v_x_uyz != -1 and v_yz != -1:
                        right_y3 = value(v_x_uyz, v_yz)
                        if right_y3 != -1 and left_y3 != right_y3:
                            return False
    return True


def stage_b_v_exact_cover_audit(
    u_array: Sequence[Sequence[int]],
    *,
    require_column_singular: bool = True,
    require_noninvolutive: bool = False,
    max_nodes: int | None = None,
    max_examples: int | None = 20,
) -> StageBVExactCoverAudit:
    u_rows = normalize_u_array(u_array)
    size = len(u_rows)
    if max_nodes is not None and max_nodes < 0:
        raise ValueError("max_nodes must be nonnegative")
    if max_examples is not None and max_examples < 0:
        raise ValueError("max_examples must be nonnegative")

    total_cells = size * size
    gac = stage_b_gac_propagation_audit(u_rows)
    bucket_domains = gac.domains if gac.locally_consistent else None
    if not balanced_symbol_counts(u_rows) or not stage_a_feasibility_nonempty(u_rows) or bucket_domains is None:
        return StageBVExactCoverAudit(
            size=size,
            node_count=0,
            exact_cover_count=0,
            column_singular_count=0,
            y2_y3_count=0,
            noninvolutive_count=0,
            accepted_count=0,
            emitted_count=0,
            truncated=False,
            examples=tuple(),
        )

    entries = [-1] * total_cells
    used_by_output_u = [0] * size
    column_seen = [0] * size
    column_duplicate = [False] * size
    column_assigned = [0] * size
    node_count = 0
    exact_cover_count = 0
    column_singular_count = 0
    y2_y3_count = 0
    noninvolutive_count = 0
    accepted_count = 0
    examples: list[VArray] = []
    truncated = False

    def current_v_array() -> VArray:
        return tuple(
            tuple(entries[row * size + col] for col in range(size))
            for row in range(size)
        )

    def available_values(position: int) -> tuple[int, ...]:
        x = position // size
        y = position % size
        output_u = u_rows[x][y]
        used = used_by_output_u[output_u]
        return tuple(
            candidate
            for candidate in bucket_domains[x][y]
            if not (used & (1 << candidate))
        )

    def choose_position() -> tuple[int | None, tuple[int, ...]]:
        best_position = None
        best_values: tuple[int, ...] = tuple(range(size + 1))
        for position, assigned in enumerate(entries):
            if assigned != -1:
                continue
            values = available_values(position)
            if not values:
                return position, tuple()
            if len(values) < len(best_values):
                best_position = position
                best_values = values
        return best_position, best_values

    def record_if_complete() -> None:
        nonlocal exact_cover_count
        nonlocal column_singular_count
        nonlocal y2_y3_count
        nonlocal noninvolutive_count
        nonlocal accepted_count

        v_rows = current_v_array()
        exact_cover_count += 1
        column_singular = v_columns_singular(v_rows)
        if column_singular:
            column_singular_count += 1
        if require_column_singular and not column_singular:
            return
        if not uv_y2_y3_hold(u_rows, v_rows):
            return
        y2_y3_count += 1
        noninvolutive = not uv_is_involutive(u_rows, v_rows)
        if noninvolutive:
            noninvolutive_count += 1
        if require_noninvolutive and not noninvolutive:
            return
        accepted_count += 1
        if max_examples is None or len(examples) < max_examples:
            examples.append(v_rows)

    def search() -> None:
        nonlocal node_count
        nonlocal truncated

        if truncated:
            return
        if max_nodes is not None and node_count >= max_nodes:
            truncated = True
            return
        node_count += 1

        position, values = choose_position()
        if position is None:
            record_if_complete()
            return
        if not values:
            return

        x = position // size
        y = position % size
        output_u = u_rows[x][y]
        for value in values:
            old_used = used_by_output_u[output_u]
            old_seen = column_seen[y]
            old_duplicate = column_duplicate[y]
            old_assigned = column_assigned[y]

            entries[position] = value
            used_by_output_u[output_u] = old_used | (1 << value)
            column_duplicate[y] = old_duplicate or bool(old_seen & (1 << value))
            column_seen[y] = old_seen | (1 << value)
            column_assigned[y] = old_assigned + 1

            column_ok = True
            if (
                require_column_singular
                and column_assigned[y] == size
                and not column_duplicate[y]
            ):
                column_ok = False
            if column_ok and _partial_y2_y3_consistent(u_rows, entries):
                search()

            entries[position] = -1
            used_by_output_u[output_u] = old_used
            column_seen[y] = old_seen
            column_duplicate[y] = old_duplicate
            column_assigned[y] = old_assigned
            if truncated:
                break

    search()
    return StageBVExactCoverAudit(
        size=size,
        node_count=node_count,
        exact_cover_count=exact_cover_count,
        column_singular_count=column_singular_count,
        y2_y3_count=y2_y3_count,
        noninvolutive_count=noninvolutive_count,
        accepted_count=accepted_count,
        emitted_count=len(examples),
        truncated=truncated,
        examples=tuple(examples),
    )
