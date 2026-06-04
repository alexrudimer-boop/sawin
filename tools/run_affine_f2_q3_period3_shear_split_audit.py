from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_q3_period3_reduction_audit import (  # noqa: E402
    _d_rows,
    _invariant_observer_rows,
    _nullspace,
    _row_reduce,
)
from run_affine_f2_q3_tetrahedral_module_audit import (  # noqa: E402
    _candidate_generator,
    _coordinates_in_basis,
    _matrix_vector_f2,
)

OUT_JSON = ROOT / "proofs" / "affine_f2_q3_period3_shear_split_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_q3_period3_shear_split_audit.md"


def _in_span(vector: int, basis: Sequence[int]) -> bool:
    reduced = vector
    for basis_vector in _row_reduce(basis):
        reduced = min(reduced, reduced ^ basis_vector)
    return reduced == 0


def _extend_basis(seed: Sequence[int], dimension: int) -> tuple[int, ...]:
    output = list(seed)
    for bit in range(dimension):
        vector = 1 << bit
        if not _in_span(vector, output):
            output.append(vector)
    return tuple(output)


def _solve_linear_system(
    equations: Sequence[int],
    rhs: Sequence[int],
    variable_count: int,
) -> dict:
    rows = list(equations)
    values = list(rhs)
    rank = 0
    pivots: list[int] = []
    for column in range(variable_count):
        pivot = None
        for row_index in range(rank, len(rows)):
            if (rows[row_index] >> column) & 1:
                pivot = row_index
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        values[rank], values[pivot] = values[pivot], values[rank]
        for row_index in range(len(rows)):
            if row_index != rank and ((rows[row_index] >> column) & 1):
                rows[row_index] ^= rows[rank]
                values[row_index] ^= values[rank]
        pivots.append(column)
        rank += 1

    contradiction_row = None
    for row_index in range(rank, len(rows)):
        if rows[row_index] == 0 and values[row_index]:
            contradiction_row = row_index
            break
    if contradiction_row is not None:
        return {
            "consistent": False,
            "rank": rank,
            "nullity": None,
            "contradiction_row": contradiction_row,
        }

    return {
        "consistent": True,
        "rank": rank,
        "nullity": variable_count - rank,
        "contradiction_row": None,
    }


def _split_row(arity: int) -> dict:
    dimension = 3 * arity
    combined_rows = tuple(_d_rows(arity)) + tuple(_invariant_observer_rows(arity))
    hidden_basis = _nullspace(combined_rows, dimension)
    if len(hidden_basis) != 2:
        return {
            "arity": arity,
            "hidden_dimension": len(hidden_basis),
            "tested": False,
            "reason": "period-3 hidden shear space is absent",
        }

    extended = _extend_basis(hidden_basis, dimension)
    quotient_basis = extended[len(hidden_basis):]
    basis = tuple(quotient_basis) + tuple(hidden_basis)
    quotient_dimension = len(quotient_basis)
    equations = []
    rhs = []
    fixed_hidden = True

    for generator_index in range(arity - 1):
        x_rows, _offset = _candidate_generator(arity, generator_index)
        for hidden_index, hidden_vector in enumerate(hidden_basis):
            hidden_image = _coordinates_in_basis(
                _matrix_vector_f2(x_rows, hidden_vector),
                basis,
            )
            if hidden_image != (1 << (quotient_dimension + hidden_index)):
                fixed_hidden = False

        for column_index, quotient_vector in enumerate(quotient_basis):
            coordinate_image = _coordinates_in_basis(
                _matrix_vector_f2(x_rows, quotient_vector),
                basis,
            )
            quotient_column = coordinate_image & ((1 << quotient_dimension) - 1)
            shear_column = (coordinate_image >> quotient_dimension) & 3

            # Search for a linear section correction P:Q -> H satisfying
            #     shear_i(q) = P(A_i q) + P(q)
            # for every generator i and quotient basis vector q.
            for hidden_row in range(2):
                mask = 0
                for target_column in range(quotient_dimension):
                    if (quotient_column >> target_column) & 1:
                        mask ^= 1 << (hidden_row * quotient_dimension + target_column)
                mask ^= 1 << (hidden_row * quotient_dimension + column_index)
                equations.append(mask)
                rhs.append((shear_column >> hidden_row) & 1)

    solve_result = _solve_linear_system(
        equations,
        rhs,
        2 * quotient_dimension,
    )
    return {
        "arity": arity,
        "hidden_dimension": len(hidden_basis),
        "quotient_dimension": quotient_dimension,
        "tested": True,
        "hidden_basis_pointwise_fixed": fixed_hidden,
        "variables": 2 * quotient_dimension,
        "equations": len(equations),
        "section_coboundary_exists": solve_result["consistent"],
        **solve_result,
    }


def build_report(max_arity: int = 30) -> dict:
    rows = [_split_row(arity) for arity in range(3, max_arity + 1, 3)]
    return {
        "title": "Affine F2^3 period-3 shear split audit",
        "max_arity": max_arity,
        "rows": rows,
        "all_checked_hidden_spaces_fixed": all(
            row.get("hidden_basis_pointwise_fixed", True) for row in rows
        ),
        "all_checked_shears_nonsplit": all(
            not row.get("section_coboundary_exists", True) for row in rows
            if row["tested"]
        ),
        "conclusion": (
            "The period-3 hidden shear space is pointwise fixed in every checked "
            "arity, but the generator shear is not a global linear coboundary "
            "through arity 30.  Thus the remaining domination question cannot "
            "be closed by a simple section change that splits the extension.  "
            "The kernel question remains subtler: the nonsplit extension may "
            "still be trivial on the tetrahedral rack kernel."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Affine F2^3 Period-3 Shear Split Audit",
        "",
        report["conclusion"],
        "",
        "## Rows",
        "",
        "| n | quotient dim | hidden fixed | variables | equations | section coboundary exists | rank |",
        "|---|---:|---|---:|---:|---|---:|",
    ]
    for row in report["rows"]:
        lines.append(
            f"| {row['arity']} | {row.get('quotient_dimension')} | "
            f"{row.get('hidden_basis_pointwise_fixed')} | "
            f"{row.get('variables')} | {row.get('equations')} | "
            f"{row.get('section_coboundary_exists')} | "
            f"{row.get('rank')} |"
        )
    lines.extend(
        [
            "",
            "## Interpretation",
            "",
            "For `n=3k`, the map `D_n` plus invariant observers leaves a "
            "two-dimensional hidden space.  Since this hidden space is fixed, "
            "one might hope that the generator shear is merely a coboundary "
            "`P(A_i q)+P(q)` and can be removed by changing the section.  This "
            "audit solves exactly that finite linear system.  It is "
            "inconsistent in every checked arity, including `n=3` and `n=6` "
            "where the full joint-kernel check is already known to pass.  So "
            "the all-arity proof must use relations in the tetrahedral rack "
            "image, not just a split-extension gauge.",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    max_arity = int(argv[0]) if argv else 30
    report = build_report(max_arity=max_arity)
    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
