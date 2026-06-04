from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_q3_period3_reduction_audit import C_ROWS  # noqa: E402
from run_affine_f2_q3_tetrahedral_module_audit import (  # noqa: E402
    _candidate_generator,
    _matrix_product_f2,
    _matrix_rank_f2,
    _matrix_vector_f2,
    _rack24_generator,
)

OUT_JSON = ROOT / "proofs" / "affine_f2_q3_full_tetrahedral_conjugacy_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_q3_full_tetrahedral_conjugacy_audit.md"


def _p_rows(arity: int) -> tuple[int, ...]:
    """Rows of P_n:X^n -> Y^n in shifted X coordinates.

    The two rows for z_1 are C_n(a_1,c_1).  For i<n, the adjacent difference
    z_i+z_{i+1} is C_{n-i}(a_i+b_i+a_{i+1}, c_i+c_{i+1}).
    """

    rows = []
    a_1 = 1
    c_1 = 1 << 2
    for c_row in C_ROWS[arity % 3]:
        row = 0
        if c_row & 1:
            row ^= a_1
        if c_row & 2:
            row ^= c_1
        rows.append(row)

    for edge_one_based in range(1, arity):
        left = edge_one_based - 1
        right = edge_one_based
        p_row = (
            (1 << (3 * left))
            ^ (1 << (3 * left + 1))
            ^ (1 << (3 * right))
        )
        q_row = (1 << (3 * left + 2)) ^ (1 << (3 * right + 2))
        eta_rows = []
        for c_row in C_ROWS[(arity - edge_one_based) % 3]:
            row = 0
            if c_row & 1:
                row ^= p_row
            if c_row & 2:
                row ^= q_row
            eta_rows.append(row)
        rows.append(rows[2 * (edge_one_based - 1)] ^ eta_rows[0])
        rows.append(rows[2 * (edge_one_based - 1) + 1] ^ eta_rows[1])
    return tuple(rows)


def _r_rows(arity: int) -> tuple[int, ...]:
    """Rows of the invariant observer R_n:X^n -> F_2^n."""

    rows = []
    prefix = 0
    for index in range(arity):
        rows.append(prefix ^ (1 << (3 * index)) ^ (1 << (3 * index + 1)))
        prefix ^= (1 << (3 * index)) ^ (1 << (3 * index + 2))
    return tuple(rows)


def _phi_rows(arity: int) -> tuple[int, ...]:
    return _p_rows(arity) + _r_rows(arity)


def _y_plus_fixed_generator(arity: int, index: int) -> tuple[int, ...]:
    rows = list(_rack24_generator(arity, index))
    for fixed_index in range(arity):
        rows.append(1 << (2 * arity + fixed_index))
    return tuple(rows)


def _row(arity: int) -> dict:
    phi = _phi_rows(arity)
    rank = _matrix_rank_f2(phi)
    failures = []
    r_failures = []
    p_failures = []
    for index in range(arity - 1):
        x_rows, _offset = _candidate_generator(arity, index)
        left = _matrix_product_f2(phi, x_rows)
        right = _matrix_product_f2(_y_plus_fixed_generator(arity, index), phi)
        if left != right:
            failures.append(index + 1)
        if _matrix_product_f2(_p_rows(arity), x_rows) != _matrix_product_f2(
            _rack24_generator(arity, index),
            _p_rows(arity),
        ):
            p_failures.append(index + 1)
        if _matrix_product_f2(_r_rows(arity), x_rows) != _r_rows(arity):
            r_failures.append(index + 1)
    return {
        "arity": arity,
        "ambient_dimension": 3 * arity,
        "p_dimension": 2 * arity,
        "r_dimension": arity,
        "phi_rank": rank,
        "phi_bijective": rank == 3 * arity,
        "p_equivariant": not p_failures,
        "p_failing_generators": p_failures,
        "r_invariant": not r_failures,
        "r_failing_generators": r_failures,
        "phi_conjugates_generators": not failures,
        "phi_failing_generators": failures,
    }


def _apply(rows: tuple[int, ...], vector: int) -> int:
    return _matrix_vector_f2(rows, vector)


def _state_level_row(arity: int) -> dict:
    state_count = 1 << (3 * arity)
    x_generators = tuple(
        _candidate_generator(arity, index)[0] for index in range(arity - 1)
    )
    y_generators = tuple(
        _rack24_generator(arity, index) for index in range(arity - 1)
    )
    p_rows = _p_rows(arity)
    r_rows = _r_rows(arity)
    phi_rows = _phi_rows(arity)
    phi_images = set()
    p_failures = []
    r_failures = []
    braid_failures = []
    commute_failures = []

    for state in range(state_count):
        phi_images.add(_apply(phi_rows, state))
        for index, x_generator in enumerate(x_generators):
            x_image = _apply(x_generator, state)
            if _apply(p_rows, x_image) != _apply(
                y_generators[index],
                _apply(p_rows, state),
            ):
                p_failures.append((state, index + 1))
            if _apply(r_rows, x_image) != _apply(r_rows, state):
                r_failures.append((state, index + 1))
        for index in range(max(0, arity - 2)):
            left = _apply(
                x_generators[index],
                _apply(
                    x_generators[index + 1],
                    _apply(x_generators[index], state),
                ),
            )
            right = _apply(
                x_generators[index + 1],
                _apply(
                    x_generators[index],
                    _apply(x_generators[index + 1], state),
                ),
            )
            if left != right:
                braid_failures.append((state, index + 1))
        for left_index in range(arity - 1):
            for right_index in range(left_index + 2, arity - 1):
                left = _apply(
                    x_generators[left_index],
                    _apply(x_generators[right_index], state),
                )
                right = _apply(
                    x_generators[right_index],
                    _apply(x_generators[left_index], state),
                )
                if left != right:
                    commute_failures.append((state, left_index + 1, right_index + 1))

    return {
        "arity": arity,
        "state_count": state_count,
        "p_equivariant_on_states": not p_failures,
        "p_first_failure": None if not p_failures else p_failures[0],
        "r_invariant_on_states": not r_failures,
        "r_first_failure": None if not r_failures else r_failures[0],
        "phi_image_count": len(phi_images),
        "phi_bijective_on_states": len(phi_images) == state_count,
        "x_adjacent_braid_relations_on_states": not braid_failures,
        "x_first_braid_failure": None if not braid_failures else braid_failures[0],
        "x_distant_commute_relations_on_states": not commute_failures,
        "x_first_commute_failure": None
        if not commute_failures
        else commute_failures[0],
    }


def _state_level_checks(max_state_arity: int) -> list[dict]:
    return [_state_level_row(arity) for arity in range(1, max_state_arity + 1)]


def build_report(max_arity: int = 30, max_state_arity: int = 6) -> dict:
    rows = [_row(arity) for arity in range(1, max_arity + 1)]
    state_rows = _state_level_checks(max_state_arity)
    return {
        "title": "Affine F2^3 full tetrahedral conjugacy audit",
        "max_arity": max_arity,
        "max_state_arity": max_state_arity,
        "rows": rows,
        "state_rows": state_rows,
        "all_checked_phi_bijective": all(row["phi_bijective"] for row in rows),
        "all_checked_p_equivariant": all(row["p_equivariant"] for row in rows),
        "all_checked_r_invariant": all(row["r_invariant"] for row in rows),
        "all_checked_conjugacy": all(
            row["phi_conjugates_generators"] for row in rows
        ),
        "all_state_checked_phi_bijective": all(
            row["phi_bijective_on_states"] for row in state_rows
        ),
        "all_state_checked_p_equivariant": all(
            row["p_equivariant_on_states"] for row in state_rows
        ),
        "all_state_checked_r_invariant": all(
            row["r_invariant_on_states"] for row in state_rows
        ),
        "all_state_checked_x_braid_relations": all(
            row["x_adjacent_braid_relations_on_states"]
            and row["x_distant_commute_relations_on_states"]
            for row in state_rows
        ),
        "conclusion": (
            "The explicit maps P_n and R_n identify the shifted affine X action "
            "with the tetrahedral rack action plus n fixed observer bits in "
            "every checked arity.  The formulas are local-recursive in n, so "
            "the accompanying proof records the all-arity argument: "
            "Phi_n=(P_n,R_n) is bijective and B_n-equivariant from X^n to "
            "Y^n x F_2^n, with B_n acting trivially on the second factor.  "
            "Consequently the braid kernels of this X and the tetrahedral "
            "rack Y are equal in every arity."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Affine F2^3 Full Tetrahedral Conjugacy Audit",
        "",
        report["conclusion"],
        "",
        "## Maps",
        "",
        "Work in shifted `X` coordinates `x_i=(a_i,b_i,c_i)`.  Let",
        "",
        "```text",
        "C_0=[[1,0],[1,1]], C_1=[[1,1],[0,1]], C_2=[[0,1],[1,0]].",
        "```",
        "",
        "Define `P_n:X^n -> Y^n` recursively by",
        "",
        "```text",
        "z_1 = C_n(a_1,c_1)",
        "p_i = a_i+b_i+a_{i+1}",
        "q_i = c_i+c_{i+1}",
        "z_{i+1} = z_i + C_{n-i}(p_i,q_i).",
        "```",
        "",
        "Define invariant observer bits",
        "",
        "```text",
        "S_{i-1}=sum_{j<i}(a_j+c_j)",
        "r_i=S_{i-1}+a_i+b_i.",
        "```",
        "",
        "Set `Phi_n=(P_n,R_n):X^n -> Y^n x F_2^n`.",
        "",
        "## Corrected Local Rule",
        "",
        "The shifted local `X` matrix sends adjacent inputs",
        "`(a,b,c),(A,B,C)` to",
        "",
        "```text",
        "((b+A, a+A, C), (c+A+C, a+b+A+B, a+b+A+C)).",
        "```",
        "",
        "The fifth coordinate is `B'=a+b+A+B`.  Omitting the `A` term breaks",
        "`R_n`-invariance already at arity `2`; the matrix row",
        "`(1,1,0,1,1,0)` is the source of the corrected term.",
        "",
        "## Checked Rows",
        "",
        "| n | rank Phi | bijective | P equivariant | R invariant | conjugates generators |",
        "|---|---:|---|---|---|---|",
    ]
    for row in report["rows"]:
        lines.append(
            f"| {row['arity']} | {row['phi_rank']} | "
            f"{row['phi_bijective']} | {row['p_equivariant']} | "
            f"{row['r_invariant']} | {row['phi_conjugates_generators']} |"
        )
    lines.extend(
        [
            "",
            "## Exhaustive State Checks",
            "",
            "| n | states | Phi bijective | P equivariant | R invariant | braid relations |",
            "|---|---:|---|---|---|---|",
        ]
    )
    for row in report["state_rows"]:
        braid_ok = (
            row["x_adjacent_braid_relations_on_states"]
            and row["x_distant_commute_relations_on_states"]
        )
        lines.append(
            f"| {row['arity']} | {row['state_count']} | "
            f"{row['phi_bijective_on_states']} | "
            f"{row['p_equivariant_on_states']} | "
            f"{row['r_invariant_on_states']} | {braid_ok} |"
        )
    lines.extend(
        [
            "",
            "## Proof Skeleton",
            "",
            "The generator check is local.  For a crossing at positions `i,i+1`, "
            "only `z_i,z_{i+1}` and the adjacent recurrence equations involving "
            "`i-1,i,i+1,i+2` change.  Substituting the shifted `X` local block "
            "and using `T C_r=C_{r+1}` and `(I+T)C_r=C_{r-1}` gives",
            "",
            "```text",
            "P_n rho^X_n(sigma_i) = rho^Y_n(sigma_i) P_n.",
            "```",
            "",
            "The same substitution shows each `r_i` is invariant.  Finally, "
            "`Phi_n` is inverted recursively: recover `z_i+z_{i+1}`, hence "
            "`p_i,q_i`; recover `(a_1,c_1)` from `z_1`; then recover "
            "`b_i`, `a_{i+1}`, and `c_{i+1}` successively from `r_i,p_i,q_i`.  "
            "Thus `Phi_n` is bijective for all `n`.",
            "",
            "Therefore",
            "",
            "```text",
            "Phi_n rho^X_n(beta) = (rho^Y_n(beta) x id) Phi_n",
            "```",
            "",
            "for every braid `beta`, and",
            "",
            "```text",
            "ker rho^X_n = ker rho^Y_n",
            "```",
            "",
            "for every arity `n`.",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    max_arity = int(argv[0]) if argv else 30
    max_state_arity = int(argv[1]) if argv and len(argv) > 1 else 6
    report = build_report(max_arity=max_arity, max_state_arity=max_state_arity)
    OUT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
