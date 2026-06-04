from __future__ import annotations

import json
import sys
from collections import deque
from pathlib import Path
from typing import Callable, Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_q3_dihedral_native_image_audit import (  # noqa: E402
    CANDIDATE_MATRIX_ROWS,
    _candidate_generator,
    _compose_affine_f2,
    _identity_rows,
)

OUT_JSON = ROOT / "proofs" / "affine_f2_q3_tetrahedral_module_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_q3_tetrahedral_module_audit.md"

# Rack representative 24 from small_rack_representatives(4):
# [0,2,3,1], [3,1,0,2], [1,3,2,0], [2,0,1,3].
# Under the identity labelling {0,1,2,3}=F_2^2, this is the Alexander rack
#     a*b = T b + (I+T)a
# where T has row masks (2,3) and order 3 in GL_2(F_2).  The braid crossing is
#     (a,b) -> (a*b,a).
TETRAHEDRAL_T_ROWS = (2, 3)
TETRAHEDRAL_LOCAL_ROWS = (11, 13, 1, 2)
F4_NAMES = ("0", "1", "t", "t+1")


def _matrix_vector_f2(rows: tuple[int, ...], vector: int) -> int:
    output = 0
    for row_index, mask in enumerate(rows):
        if (mask & vector).bit_count() & 1:
            output |= 1 << row_index
    return output


def _matrix_product_f2(
    left_rows: tuple[int, ...],
    right_rows: tuple[int, ...],
) -> tuple[int, ...]:
    output = []
    for mask in left_rows:
        row = 0
        active = mask
        index = 0
        while active:
            if active & 1:
                row ^= right_rows[index]
            active >>= 1
            index += 1
        output.append(row)
    return tuple(output)


def _compose_linear_f2(
    left: tuple[int, ...],
    right: tuple[int, ...],
) -> tuple[int, ...]:
    return _matrix_product_f2(left, right)


def _compose_pair(
    left: tuple[object, object],
    right: tuple[object, object],
    first_compose: Callable,
    second_compose: Callable,
) -> tuple[object, object]:
    return (
        first_compose(left[0], right[0]),
        second_compose(left[1], right[1]),
    )


def _f4_multiply(left: int, right: int) -> int:
    left_0 = left & 1
    left_1 = (left >> 1) & 1
    right_0 = right & 1
    right_1 = (right >> 1) & 1
    # t^2=t+1 in the identity F_2^2 labelling.
    return (
        (left_0 & right_0) ^ (left_1 & right_1)
    ) | (
        ((left_0 & right_1) ^ (left_1 & right_0) ^ (left_1 & right_1)) << 1
    )


def _f4_t_power(power: int) -> int:
    value = 1
    for _ in range(power % 3):
        value = _f4_multiply(value, 2)
    return value


def _f4_inverse(value: int) -> int:
    if value == 0:
        raise ZeroDivisionError("0 has no inverse in F_4")
    for candidate in (1, 2, 3):
        if _f4_multiply(value, candidate) == 1:
            return candidate
    raise AssertionError("unreachable for F_4")


def _image_order(
    generators: tuple,
    identity,
    compose: Callable,
    *,
    state_limit: int,
) -> tuple[int | None, bool]:
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = compose(generator, current)
            if candidate in seen:
                continue
            seen.add(candidate)
            if len(seen) > state_limit:
                return None, True
            queue.append(candidate)
    return len(seen), False


def _rack24_generator(arity: int, index: int) -> tuple[int, ...]:
    rows = list(_identity_rows(2 * arity))
    for row in range(4):
        mask = 0
        for column in range(4):
            if (TETRAHEDRAL_LOCAL_ROWS[row] >> column) & 1:
                mask |= 1 << (2 * index + column)
        rows[2 * index + row] = mask
    return tuple(rows)


def _f4_columns_to_f2_rows(
    columns: Sequence[Sequence[int]],
    dimension_over_f4: int,
) -> tuple[int, ...]:
    rows = [0] * (2 * dimension_over_f4)
    for column_index, column in enumerate(columns):
        for row_index, coefficient in enumerate(column):
            for source_bit, source_scalar in ((0, 1), (1, 2)):
                value = _f4_multiply(source_scalar, coefficient)
                for target_bit in (0, 1):
                    if (value >> target_bit) & 1:
                        rows[2 * row_index + target_bit] |= (
                            1 << (2 * column_index + source_bit)
                        )
    return tuple(rows)


def _rack24_invariant_slice_generator(
    arity: int,
    index: int,
    slice_constant: int,
) -> tuple[tuple[int, ...], int]:
    """Rack24 action on L_n=s, using z_1,...,z_{n-1} coordinates."""

    dimension_over_f4 = arity - 1
    inverse_last_weight = _f4_inverse(_f4_t_power(arity - 1))

    def full_tuple_from_coordinates(vector: int) -> list[int]:
        entries = [
            (vector >> (2 * entry_index)) & 3
            for entry_index in range(dimension_over_f4)
        ]
        total = slice_constant
        for entry_index, entry in enumerate(entries):
            total ^= _f4_multiply(_f4_t_power(entry_index), entry)
        entries.append(_f4_multiply(inverse_last_weight, total))
        return entries

    def coordinates_from_full_tuple(entries: Sequence[int]) -> int:
        output = 0
        for entry_index, entry in enumerate(entries[:dimension_over_f4]):
            output |= entry << (2 * entry_index)
        return output

    def apply_braid(entries: Sequence[int]) -> list[int]:
        output = list(entries)
        left = output[index]
        right = output[index + 1]
        output[index] = _f4_multiply(3, left) ^ _f4_multiply(2, right)
        output[index + 1] = left
        return output

    offset = coordinates_from_full_tuple(apply_braid(full_tuple_from_coordinates(0)))
    columns = []
    for column_index in range(dimension_over_f4):
        image = coordinates_from_full_tuple(
            apply_braid(full_tuple_from_coordinates(1 << (2 * column_index)))
        )
        image ^= offset
        columns.append(
            [
                (image >> (2 * row_index)) & 3
                for row_index in range(dimension_over_f4)
            ]
        )
    return _f4_columns_to_f2_rows(columns, dimension_over_f4), offset


def _row_reduce(vectors: Sequence[int]) -> tuple[int, ...]:
    basis: list[int] = []
    for vector in vectors:
        reduced = vector
        for basis_vector in basis:
            reduced = min(reduced, reduced ^ basis_vector)
        if not reduced:
            continue
        pivot = reduced.bit_length() - 1
        for index, basis_vector in enumerate(basis):
            if (basis_vector >> pivot) & 1:
                basis[index] = basis_vector ^ reduced
        basis.append(reduced)
        basis.sort(reverse=True)
    return tuple(basis)


def _matrix_rank_f2(rows: Sequence[int]) -> int:
    return len(_row_reduce(rows))


def _in_span(vector: int, basis: Sequence[int]) -> bool:
    reduced = vector
    for basis_vector in _row_reduce(basis):
        reduced = min(reduced, reduced ^ basis_vector)
    return reduced == 0


def _coordinates_in_basis(vector: int, basis: Sequence[int]) -> int:
    """Return coordinates of vector in the given independent F_2 basis."""

    dimension = len(basis)
    row_count = max(
        [vector.bit_length(), *(basis_vector.bit_length() for basis_vector in basis), 1]
    )
    rows = []
    rhs = []
    for bit in range(row_count):
        mask = 0
        for index, basis_vector in enumerate(basis):
            if (basis_vector >> bit) & 1:
                mask |= 1 << index
        rows.append(mask)
        rhs.append((vector >> bit) & 1)

    rank = 0
    pivots = []
    for column in range(dimension):
        pivot = None
        for row_index in range(rank, row_count):
            if (rows[row_index] >> column) & 1:
                pivot = row_index
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        rhs[rank], rhs[pivot] = rhs[pivot], rhs[rank]
        for row_index in range(row_count):
            if row_index != rank and ((rows[row_index] >> column) & 1):
                rows[row_index] ^= rows[rank]
                rhs[row_index] ^= rhs[rank]
        pivots.append(column)
        rank += 1

    for row_index in range(rank, row_count):
        if rows[row_index] == 0 and rhs[row_index]:
            raise ValueError("vector is not in the supplied basis span")

    coordinates = 0
    for row_index, column in enumerate(pivots):
        if rhs[row_index]:
            coordinates |= 1 << column
    return coordinates


def _x_fibre_basis(arity: int) -> tuple[int, ...]:
    """Basis for the 2n-2 dimensional translation/fibre module of X^n.

    Coordinates on each X-strand are named (a_i,b_i,c_i).  The basis is the
    explicit alternating prefix basis that appears by closing the generator
    offsets under the linear parts of the affine X-action.
    """

    basis = []
    for edge in range(1, arity):
        if edge % 2:
            first = 1 << 2
            for strand in range(2, edge + 1):
                first ^= 1 << (3 * (strand - 1) + 1)
            first ^= 1 << (3 * edge)

            second = (1 << 0) ^ (1 << 1)
            for strand in range(2, edge + 2):
                second ^= 1 << (3 * (strand - 1) + 1)
            second ^= 1 << (3 * edge + 2)
        else:
            first = (1 << 0) ^ (1 << 1)
            for strand in range(2, edge + 1):
                first ^= 1 << (3 * (strand - 1) + 1)
            first ^= 1 << (3 * edge)

            second = 1 << 2
            for strand in range(2, edge + 2):
                second ^= 1 << (3 * (strand - 1) + 1)
            second ^= 1 << (3 * edge + 2)
        basis.extend([first, second])
    return tuple(basis)


def _x_fibre_generator(arity: int, index: int) -> tuple[tuple[int, ...], int]:
    x_rows, x_offset = _candidate_generator(arity, index)
    basis = _x_fibre_basis(arity)
    columns = []
    for basis_vector in basis:
        image = _matrix_vector_f2(x_rows, basis_vector)
        if not _in_span(image, basis):
            raise AssertionError("X fibre basis is not invariant")
        columns.append(_coordinates_in_basis(image, basis))
    rows = []
    for row in range(len(basis)):
        mask = 0
        for column, coordinate_mask in enumerate(columns):
            if (coordinate_mask >> row) & 1:
                mask |= 1 << column
        rows.append(mask)
    if not _in_span(x_offset, basis):
        raise AssertionError("X offset is not in the fibre basis span")
    return tuple(rows), _coordinates_in_basis(x_offset, basis)


def _x_position_shift(arity: int) -> int:
    shift = 0
    for index in range(arity):
        if (index + 1) & 1:
            shift |= 1 << (3 * index + 2)
    return shift


def _x_linearization_rows(max_arity: int) -> list[dict]:
    rows = []
    for arity in range(2, max_arity + 1):
        shift = _x_position_shift(arity)
        generator_results = []
        for index in range(arity - 1):
            matrix, offset = _candidate_generator(arity, index)
            generator_results.append(
                _matrix_vector_f2(matrix, shift) ^ offset == shift
            )
        rows.append(
            {
                "arity": arity,
                "position_shift_bits": shift,
                "all_generators_linearized": all(generator_results),
                "generator_results": generator_results,
            }
        )
    return rows


def _solve_affine_conjugacy(
    source_generators: Sequence[tuple[tuple[int, ...], int]],
    target_generators: Sequence[tuple[tuple[int, ...], int]],
) -> dict:
    """Solve P(Ax+a)+c=B(Px+c)+b and test for invertible P."""

    dimension = len(source_generators[0][0])
    variable_count = dimension * dimension + dimension
    equations: list[int] = []
    rhs: list[int] = []
    for (source_rows, source_offset), (target_rows, target_offset) in zip(
        source_generators,
        target_generators,
    ):
        for row in range(dimension):
            for column in range(dimension):
                mask = 0
                for inner in range(dimension):
                    if (source_rows[inner] >> column) & 1:
                        mask ^= 1 << (row * dimension + inner)
                for inner in range(dimension):
                    if (target_rows[row] >> inner) & 1:
                        mask ^= 1 << (inner * dimension + column)
                if mask:
                    equations.append(mask)
                    rhs.append(0)
        for row in range(dimension):
            mask = 0
            for inner in range(dimension):
                if (source_offset >> inner) & 1:
                    mask ^= 1 << (row * dimension + inner)
            mask ^= 1 << (dimension * dimension + row)
            for inner in range(dimension):
                if (target_rows[row] >> inner) & 1:
                    mask ^= 1 << (dimension * dimension + inner)
            equations.append(mask)
            rhs.append((target_offset >> row) & 1)

    matrix = list(equations)
    values = list(rhs)
    rank = 0
    pivots: list[int] = []
    for column in range(variable_count):
        pivot = None
        for row_index in range(rank, len(matrix)):
            if (matrix[row_index] >> column) & 1:
                pivot = row_index
                break
        if pivot is None:
            continue
        matrix[rank], matrix[pivot] = matrix[pivot], matrix[rank]
        values[rank], values[pivot] = values[pivot], values[rank]
        for row_index in range(len(matrix)):
            if row_index != rank and ((matrix[row_index] >> column) & 1):
                matrix[row_index] ^= matrix[rank]
                values[row_index] ^= values[rank]
        pivots.append(column)
        rank += 1

    for row_index in range(rank, len(matrix)):
        if matrix[row_index] == 0 and values[row_index]:
            return {
                "consistent": False,
                "invertible_solution_found": False,
                "solution_nullity": None,
            }

    pivot_set = set(pivots)
    free_columns = [
        column for column in range(variable_count) if column not in pivot_set
    ]
    particular = 0
    for row_index, column in enumerate(pivots):
        if values[row_index]:
            particular |= 1 << column
    nullspace = []
    for free_column in free_columns:
        vector = 1 << free_column
        for row_index, column in enumerate(pivots):
            if (matrix[row_index] >> free_column) & 1:
                vector |= 1 << column
        nullspace.append(vector)

    if len(nullspace) > 20:
        raise RuntimeError("conjugacy solution space is unexpectedly large")

    for combination in range(1 << len(nullspace)):
        vector = particular
        for index, null_vector in enumerate(nullspace):
            if (combination >> index) & 1:
                vector ^= null_vector
        rows = tuple(
            sum(
                ((vector >> (row * dimension + column)) & 1) << column
                for column in range(dimension)
            )
            for row in range(dimension)
        )
        if _matrix_rank_f2(rows) == dimension:
            affine_shift = (vector >> (dimension * dimension)) & (
                (1 << dimension) - 1
            )
            return {
                "consistent": True,
                "invertible_solution_found": True,
                "solution_nullity": len(nullspace),
                "first_invertible_combination": combination,
                "affine_shift": affine_shift,
            }
    return {
        "consistent": True,
        "invertible_solution_found": False,
        "solution_nullity": len(nullspace),
    }


def _slice_conjugacy_rows(max_arity: int) -> list[dict]:
    rows = []
    for arity in range(2, max_arity + 1):
        source_generators = tuple(
            _x_fibre_generator(arity, index) for index in range(arity - 1)
        )
        attempted_constants = []
        matching_constants = []
        for slice_constant in range(4):
            target_generators = tuple(
                _rack24_invariant_slice_generator(
                    arity,
                    index,
                    slice_constant,
                )
                for index in range(arity - 1)
            )
            result = _solve_affine_conjugacy(source_generators, target_generators)
            attempted_constants.append(
                {
                    "slice_constant": slice_constant,
                    "slice_constant_name": F4_NAMES[slice_constant],
                    **result,
                }
            )
            if result["invertible_solution_found"]:
                matching_constants.append(slice_constant)
        rows.append(
            {
                "arity": arity,
                "matching_slice_constants": matching_constants,
                "matching_slice_constant_names": [
                    F4_NAMES[constant] for constant in matching_constants
                ],
                "has_matching_slice": bool(matching_constants),
                "attempted_constants": attempted_constants,
            }
        )
    return rows


def _format_fibre_vector(vector: int, arity: int) -> str:
    names = []
    for strand in range(arity):
        for bit, name in enumerate(("a", "b", "c")):
            if (vector >> (3 * strand + bit)) & 1:
                names.append(f"{name}{strand + 1}")
    return "+".join(names) or "0"


def _rack24_operation_table() -> list[list[int]]:
    table = []
    for left in range(4):
        row = []
        for right in range(4):
            vector = _matrix_vector_f2(TETRAHEDRAL_T_ROWS, right)
            vector ^= left
            vector ^= _matrix_vector_f2(TETRAHEDRAL_T_ROWS, left)
            row.append(vector)
        table.append(row)
    return table


def build_report(
    max_arity: int = 5,
    state_limit: int = 2_000_000,
    max_conjugacy_arity: int = 10,
) -> dict:
    rows = []
    for arity in range(2, max_arity + 1):
        rack_generators = tuple(_rack24_generator(arity, index) for index in range(arity - 1))
        x_generators = tuple(_candidate_generator(arity, index) for index in range(arity - 1))
        fibre_generators = tuple(
            _x_fibre_generator(arity, index) for index in range(arity - 1)
        )

        rack_identity = _identity_rows(2 * arity)
        x_identity = (_identity_rows(3 * arity), 0)
        fibre_identity = (_identity_rows(2 * arity - 2), 0)

        rack_order, rack_truncated = _image_order(
            rack_generators,
            rack_identity,
            _compose_linear_f2,
            state_limit=state_limit,
        )
        x_order, x_truncated = _image_order(
            x_generators,
            x_identity,
            _compose_affine_f2,
            state_limit=state_limit,
        )
        fibre_order, fibre_truncated = _image_order(
            fibre_generators,
            fibre_identity,
            _compose_affine_f2,
            state_limit=state_limit,
        )

        rack_x_joint_order, rack_x_joint_truncated = _image_order(
            tuple(zip(rack_generators, x_generators)),
            (rack_identity, x_identity),
            lambda left, right: _compose_pair(
                left,
                right,
                _compose_linear_f2,
                _compose_affine_f2,
            ),
            state_limit=state_limit,
        )
        rack_fibre_joint_order, rack_fibre_joint_truncated = _image_order(
            tuple(zip(rack_generators, fibre_generators)),
            (rack_identity, fibre_identity),
            lambda left, right: _compose_pair(
                left,
                right,
                _compose_linear_f2,
                _compose_affine_f2,
            ),
            state_limit=state_limit,
        )
        fibre_x_joint_order, fibre_x_joint_truncated = _image_order(
            tuple(zip(fibre_generators, x_generators)),
            (fibre_identity, x_identity),
            lambda left, right: _compose_pair(
                left,
                right,
                _compose_affine_f2,
                _compose_affine_f2,
            ),
            state_limit=state_limit,
        )

        rows.append(
            {
                "arity": arity,
                "rack24_image_order": rack_order,
                "x_image_order": x_order,
                "x_fibre_affine_image_order": fibre_order,
                "rack24_x_joint_order": rack_x_joint_order,
                "rack24_fibre_joint_order": rack_fibre_joint_order,
                "fibre_x_joint_order": fibre_x_joint_order,
                "truncated": any(
                    (
                        rack_truncated,
                        x_truncated,
                        fibre_truncated,
                        rack_x_joint_truncated,
                        rack_fibre_joint_truncated,
                        fibre_x_joint_truncated,
                    )
                ),
                "all_orders_match": all(
                    order == rack_order
                    for order in (
                        x_order,
                        fibre_order,
                        rack_x_joint_order,
                        rack_fibre_joint_order,
                        fibre_x_joint_order,
                    )
                ),
            }
        )

    fibre_basis_examples = {
        str(arity): [
            _format_fibre_vector(vector, arity)
            for vector in _x_fibre_basis(arity)
        ]
        for arity in range(2, min(max_arity, 5) + 1)
    }
    return {
        "title": "Affine F2^3 tetrahedral rack module audit",
        "max_arity": max_arity,
        "max_conjugacy_arity": max_conjugacy_arity,
        "state_limit": state_limit,
        "rack24_alexander_model": {
            "field": "F_2^2 under identity labels 0,1,2,3",
            "T_row_masks": list(TETRAHEDRAL_T_ROWS),
            "local_braid_row_masks": list(TETRAHEDRAL_LOCAL_ROWS),
            "operation_table_rows": _rack24_operation_table(),
            "formula": "a*b = T b + (I+T)a; braid crossing (a,b)->(a*b,a)",
        },
        "x_linearized_model": {
            "position_shift": "s_i=(0,0,i mod 2), with i one-based",
            "local_matrix_rows": list(CANDIDATE_MATRIX_ROWS),
            "linearization_rows": _x_linearization_rows(max_conjugacy_arity),
        },
        "x_fibre_basis_examples": fibre_basis_examples,
        "rows": rows,
        "invariant_slice_model": {
            "field": "F_4=F_2[t]/(t^2+t+1)",
            "invariant_functional": (
                "L_n(z_1,...,z_n)=sum_{i=1}^n t^{i-1} z_i"
            ),
            "slice": "L_n=s",
            "conjugacy_rows": _slice_conjugacy_rows(max_conjugacy_arity),
        },
        "conclusion": (
            "Rack representative 24 is the Alexander rack over F_2^2 with "
            "T row masks (2,3).  The affine X-action has an explicit "
            "2n-2 dimensional fibre module generated by the affine offsets. "
            "Through arity 5, the rack24 image, the X image, the induced "
            "X-fibre affine image, and all pairwise joint images have the "
            "same order.  The stronger slice-conjugacy check shows through "
            "arity 10 that the X-fibre affine action is conjugate to rack24 "
            "on an invariant affine slice L_n=s.  This isolates the all-n "
            "task to proving that this slice conjugacy persists uniformly."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Affine F2^3 Tetrahedral Rack Module Audit",
        "",
        report["conclusion"],
        "",
        "## Rack24 Alexander Model",
        "",
        f"- `T` row masks over `F_2^2`: `{report['rack24_alexander_model']['T_row_masks']}`.",
        "- formula: `a*b = T b + (I+T)a`; braid crossing `(a,b)->(a*b,a)`.",
        "- operation table rows:",
    ]
    for row in report["rack24_alexander_model"]["operation_table_rows"]:
        lines.append(f"  - `{row}`")
    lines.extend(
        [
            "",
            "## X Linearization",
            "",
            "- position shift: `s_i=(0,0,i mod 2)`, with `i` one-based.",
            "- in shifted coordinates, the local affine `X` block is the "
            "linear matrix with rows:",
        ]
    )
    for row in report["x_linearized_model"]["local_matrix_rows"]:
        lines.append(f"  - `{row}`")
    linearized_arities = [
        row["arity"]
        for row in report["x_linearized_model"]["linearization_rows"]
        if row["all_generators_linearized"]
    ]
    lines.append(
        "- verified arities for the shift identity: "
        f"`{linearized_arities}`."
    )
    lines.extend(
        [
            "",
            "## Image Orders",
            "",
            "| n | rack24 | X | X fibre affine | rack-X joint | rack-fibre joint | fibre-X joint | all match | truncated |",
            "|---|---:|---:|---:|---:|---:|---:|---|---|",
        ]
    )
    for row in report["rows"]:
        lines.append(
            "| {arity} | {rack24_image_order} | {x_image_order} | "
            "{x_fibre_affine_image_order} | {rack24_x_joint_order} | "
            "{rack24_fibre_joint_order} | {fibre_x_joint_order} | "
            "{all_orders_match} | {truncated} |".format(**row)
        )
    lines.extend(["", "## Fibre Basis Examples", ""])
    for arity, basis in report["x_fibre_basis_examples"].items():
        lines.append(f"- `n={arity}`: `{basis}`")
    lines.extend(
        [
            "",
            "## Invariant Slice Conjugacy",
            "",
            "For rack24 over `F_4=F_2[t]/(t^2+t+1)`, the full Alexander "
            "representation preserves",
            "",
            "```text",
            "L_n(z_1,...,z_n)=sum_{i=1}^n t^{i-1}z_i.",
            "```",
            "",
            "The level set `L_n=s` has `F_2` dimension `2n-2`.  The table below "
            "records whether the induced `X` fibre action is affine-conjugate "
            "to rack24 restricted to one of these invariant slices.",
            "",
            "| n | matching slice constants | any match |",
            "|---|---|---|",
        ]
    )
    for row in report["invariant_slice_model"]["conjugacy_rows"]:
        lines.append(
            f"| {row['arity']} | `{row['matching_slice_constant_names']}` | "
            f"{row['has_matching_slice']} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "The old tuple-permutation check showed rack24 has no detector-kernel "
            "obstruction against `X` through arity 5.  This native audit gives "
            "the structural reason visible so far: the affine offsets of `X` "
            "generate a `2n-2` dimensional fibre module, and the induced affine "
            "action has the same marked image as rack24 through every checked "
            "arity.  The invariant-slice check strengthens this: through arity "
            "10, the fibre action is affine-conjugate to the restriction of "
            "the full tetrahedral Alexander representation to `L_n=s` for at "
            "least one constant `s`.  A proof of the uniform slice conjugacy "
            "would close this candidate positively.",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    max_arity = int(argv[0]) if argv else 5
    state_limit = int(argv[1]) if argv and len(argv) > 1 else 2_000_000
    max_conjugacy_arity = int(argv[2]) if argv and len(argv) > 2 else 10
    report = build_report(
        max_arity=max_arity,
        state_limit=state_limit,
        max_conjugacy_arity=max_conjugacy_arity,
    )
    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
