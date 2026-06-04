from __future__ import annotations

import json
import sys
from collections import deque
from pathlib import Path
from typing import Callable, Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_q3_dihedral_native_image_audit import (  # noqa: E402
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


def build_report(max_arity: int = 5, state_limit: int = 2_000_000) -> dict:
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
        "state_limit": state_limit,
        "rack24_alexander_model": {
            "field": "F_2^2 under identity labels 0,1,2,3",
            "T_row_masks": list(TETRAHEDRAL_T_ROWS),
            "local_braid_row_masks": list(TETRAHEDRAL_LOCAL_ROWS),
            "operation_table_rows": _rack24_operation_table(),
            "formula": "a*b = T b + (I+T)a; braid crossing (a,b)->(a*b,a)",
        },
        "x_fibre_basis_examples": fibre_basis_examples,
        "rows": rows,
        "conclusion": (
            "Rack representative 24 is the Alexander rack over F_2^2 with "
            "T row masks (2,3).  The affine X-action has an explicit "
            "2n-2 dimensional fibre module generated by the affine offsets. "
            "Through arity 5, the rack24 image, the X image, the induced "
            "X-fibre affine image, and all pairwise joint images have the "
            "same order.  This gives a native confirmation of kernel equality "
            "through arity 5 and isolates the all-n task to proving that this "
            "fibre-module identification persists uniformly."
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
            "## Interpretation",
            "",
            "The old tuple-permutation check showed rack24 has no detector-kernel "
            "obstruction against `X` through arity 5.  This native audit gives "
            "the structural reason visible so far: the affine offsets of `X` "
            "generate a `2n-2` dimensional fibre module, and the induced affine "
            "action has the same marked image as rack24 through every checked "
            "arity.  A proof of the uniform fibre-module/rack24 equivalence "
            "would close this candidate positively.",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    max_arity = int(argv[0]) if argv else 5
    state_limit = int(argv[1]) if argv and len(argv) > 1 else 2_000_000
    report = build_report(max_arity=max_arity, state_limit=state_limit)
    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
