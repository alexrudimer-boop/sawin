from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_q3_tetrahedral_module_audit import (  # noqa: E402
    _candidate_generator,
    _f4_multiply,
    _matrix_product_f2,
    _matrix_rank_f2,
    _matrix_vector_f2,
    _rack24_generator,
)

OUT_JSON = ROOT / "proofs" / "affine_f2_q3_period3_reduction_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_q3_period3_reduction_audit.md"

C_ROWS = {
    0: (1, 3),  # [[1,0],[1,1]]
    1: (3, 2),  # [[1,1],[0,1]]
    2: (2, 1),  # [[0,1],[1,0]]
}


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


def _nullspace(equations: Sequence[int], dimension: int) -> tuple[int, ...]:
    rows = list(equations)
    rank = 0
    pivots: list[int] = []
    for column in range(dimension):
        pivot = None
        for row_index in range(rank, len(rows)):
            if (rows[row_index] >> column) & 1:
                pivot = row_index
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for row_index in range(len(rows)):
            if row_index != rank and ((rows[row_index] >> column) & 1):
                rows[row_index] ^= rows[rank]
        pivots.append(column)
        rank += 1

    pivot_set = set(pivots)
    basis = []
    for free_column in range(dimension):
        if free_column in pivot_set:
            continue
        vector = 1 << free_column
        for row_index, pivot_column in enumerate(pivots):
            if (rows[row_index] >> free_column) & 1:
                vector |= 1 << pivot_column
        basis.append(vector)
    return tuple(basis)


def _d_rows(arity: int) -> tuple[int, ...]:
    rows = []
    for edge_one_based in range(1, arity):
        left = edge_one_based - 1
        right = edge_one_based
        p_row = (
            (1 << (3 * left))
            ^ (1 << (3 * left + 1))
            ^ (1 << (3 * right))
        )
        q_row = (1 << (3 * left + 2)) ^ (1 << (3 * right + 2))
        for c_row in C_ROWS[(arity - edge_one_based) % 3]:
            row = 0
            if c_row & 1:
                row ^= p_row
            if c_row & 2:
                row ^= q_row
            rows.append(row)
    return tuple(rows)


def _f4_vector_to_int(entries: Sequence[int]) -> int:
    output = 0
    for index, entry in enumerate(entries):
        output |= entry << (2 * index)
    return output


def _int_to_f4_vector(vector: int, dimension: int) -> list[int]:
    return [(vector >> (2 * index)) & 3 for index in range(dimension)]


def _full_from_adjacent_differences(differences: Sequence[int]) -> list[int]:
    entries = [0] * (len(differences) + 1)
    for index in range(len(differences) - 1, -1, -1):
        entries[index] = differences[index] ^ entries[index + 1]
    return entries


def _adjacent_differences(entries: Sequence[int]) -> list[int]:
    return [entries[index] ^ entries[index + 1] for index in range(len(entries) - 1)]


def _reduced_tetrahedral_generator(arity: int, index: int) -> tuple[int, ...]:
    """Induced tetrahedral action on eta_i=z_i+z_{i+1} coordinates."""

    dimension = arity - 1
    full_generator = _rack24_generator(arity, index)
    columns = []
    for column in range(dimension):
        for source_scalar in (1, 2):
            differences = [0] * dimension
            differences[column] = source_scalar
            full = _f4_vector_to_int(_full_from_adjacent_differences(differences))
            image = _matrix_vector_f2(full_generator, full)
            output = _adjacent_differences(_int_to_f4_vector(image, arity))
            columns.append(_f4_vector_to_int(output))

    rows = []
    for row in range(2 * dimension):
        mask = 0
        for column, image in enumerate(columns):
            if (image >> row) & 1:
                mask |= 1 << column
        rows.append(mask)
    return tuple(rows)


def _invariant_observer_rows(arity: int) -> tuple[int, ...]:
    dimension = 3 * arity
    equations = [0] * dimension
    for index in range(arity - 1):
        x_rows, _offset = _candidate_generator(arity, index)
        for source_bit in range(dimension):
            row_difference = (
                _matrix_product_f2((1 << source_bit,), x_rows)[0]
                ^ (1 << source_bit)
            )
            for target_bit in range(dimension):
                if (row_difference >> target_bit) & 1:
                    equations[target_bit] ^= 1 << source_bit
    return _nullspace(equations, dimension)


def _kernel_basis(rows: Sequence[int], dimension: int) -> tuple[int, ...]:
    return _nullspace(rows, dimension)


def _intertwiner_row(arity: int) -> dict:
    d_rows = _d_rows(arity)
    failures = []
    for index in range(arity - 1):
        x_rows, _offset = _candidate_generator(arity, index)
        left = _matrix_product_f2(d_rows, x_rows)
        right = _matrix_product_f2(
            _reduced_tetrahedral_generator(arity, index),
            d_rows,
        )
        if left != right:
            failures.append(index + 1)
    return {
        "arity": arity,
        "all_generators_intertwine": not failures,
        "failing_generators": failures,
    }


def _rank_row(arity: int) -> dict:
    dimension = 3 * arity
    d_rows = _d_rows(arity)
    invariant_rows = _invariant_observer_rows(arity)
    d_kernel = _kernel_basis(d_rows, dimension)
    fixed_kernel = all(
        all(
            _matrix_vector_f2(_candidate_generator(arity, index)[0], vector)
            == vector
            for index in range(arity - 1)
        )
        for vector in d_kernel
    )
    combined_rank = _matrix_rank_f2(tuple(d_rows) + tuple(invariant_rows))
    return {
        "arity": arity,
        "ambient_dimension": dimension,
        "d_rank": _matrix_rank_f2(d_rows),
        "d_kernel_dimension": len(d_kernel),
        "invariant_observer_dimension": len(invariant_rows),
        "d_kernel_pointwise_fixed": fixed_kernel,
        "combined_rank": combined_rank,
        "missing_dimension": dimension - combined_rank,
        "arity_divisible_by_3": arity % 3 == 0,
    }


def build_report(max_arity: int = 18) -> dict:
    rows = [_rank_row(arity) for arity in range(2, max_arity + 1)]
    intertwiner_rows = [
        _intertwiner_row(arity)
        for arity in range(2, max_arity + 1)
    ]
    return {
        "title": "Affine F2^3 period-3 reduction audit",
        "max_arity": max_arity,
        "d_map": {
            "edge_defects": "p_i=a_i+b_i+a_{i+1}, q_i=c_i+c_{i+1}",
            "twists": {
                "0": [[1, 0], [1, 1]],
                "1": [[1, 1], [0, 1]],
                "2": [[0, 1], [1, 0]],
            },
            "formula": "D_n(x)_i=C_{n-i mod 3}(p_i,q_i)",
        },
        "intertwiner_rows": intertwiner_rows,
        "rank_rows": rows,
        "all_checked_generators_intertwine": all(
            row["all_generators_intertwine"] for row in intertwiner_rows
        ),
        "all_checked_kernels_fixed": all(
            row["d_kernel_pointwise_fixed"] for row in rows
        ),
        "missing_dimension_pattern_holds": all(
            row["missing_dimension"] == (2 if row["arity_divisible_by_3"] else 0)
            for row in rows
        ),
        "conclusion": (
            "The explicit D_n map intertwines the shifted-linear X action with "
            "the reduced tetrahedral action on adjacent-difference coordinates "
            "through every checked arity.  Its kernel is pointwise fixed by the "
            "X generators, and D_n together with all linear invariant observers "
            "separates the full X module except for a two-dimensional remainder "
            "exactly when n is divisible by 3.  This supports the reduction of "
            "the remaining rack24-domination question to a period-3 shear "
            "cocycle at arities 3k."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Affine F2^3 Period-3 Reduction Audit",
        "",
        report["conclusion"],
        "",
        "## Intertwiner",
        "",
        "For edge `i`, define",
        "",
        "```text",
        "p_i = a_i + b_i + a_{i+1}",
        "q_i = c_i + c_{i+1}",
        "D_n(x)_i = C_{n-i mod 3}(p_i,q_i).",
        "```",
        "",
        "The three matrices are:",
        "",
        "- `C_0=[[1,0],[1,1]]`;",
        "- `C_1=[[1,1],[0,1]]`;",
        "- `C_2=[[0,1],[1,0]]`.",
        "",
        "The audit checks",
        "",
        "```text",
        "D_n X_i = Ybar_i D_n",
        "```",
        "",
        "where `Ybar_i` is the tetrahedral rack action induced on adjacent "
        "differences `eta_i=z_i+z_{i+1}`.",
        "",
        "## Rank Rows",
        "",
        "| n | rank D | dim ker D | dim Inv | ker D fixed | combined rank | missing dim | 3 divides n |",
        "|---|---:|---:|---:|---|---:|---:|---|",
    ]
    for row in report["rank_rows"]:
        lines.append(
            f"| {row['arity']} | {row['d_rank']} | "
            f"{row['d_kernel_dimension']} | "
            f"{row['invariant_observer_dimension']} | "
            f"{row['d_kernel_pointwise_fixed']} | "
            f"{row['combined_rank']} | "
            f"{row['missing_dimension']} | "
            f"{row['arity_divisible_by_3']} |"
        )
    lines.extend(
        [
            "",
            "## Consequence",
            "",
            "If `beta` is trivial in the full tetrahedral rack action, then it is "
            "trivial on the reduced adjacent-difference action.  The `D_n` "
            "intertwiner therefore forces the non-fixed part of the shifted "
            "`X` action to be trivial.  The invariant observers are fixed by "
            "every braid.  For `3` not dividing `n`, these data have full rank, "
            "so rack24 domination holds in those arities.  For `n=3k`, the only "
            "remaining possible mismatch is a two-dimensional shear.",
            "",
            "The first unchecked arity after the existing `n=3` and `n=6` "
            "joint-kernel computations is therefore `n=9`.",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    max_arity = int(argv[0]) if argv else 18
    report = build_report(max_arity=max_arity)
    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
