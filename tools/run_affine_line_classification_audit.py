from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_rigid_pressure_core_audit import (  # noqa: E402
    affine_prime_line_solution,
    scan_affine_prime_line,
)
from ybe_domination import is_involutive_solution  # noqa: E402

OUT_JSON = ROOT / "proofs" / "affine_line_classification_audit.json"
OUT_MD = ROOT / "proofs" / "affine_line_classification_audit.md"


YBE_EQUATIONS = (
    "a(a+bd-1)=0",
    "abe=0",
    "a(bf+c)=0",
    "ade=0",
    "ae(e-a)=0",
    "-ace+aef-af-bf+cd+ce-c+f=0",
    "e(1-e-bd)=0",
    "e(cd+f)=0",
)


def determinant(coeffs: tuple[int, ...], prime: int) -> int:
    a, b, _c, d, e, _f = coeffs
    return (a * e - b * d) % prime


def bidegenerate_bijective_affine_line_rows(prime: int) -> list[dict[str, object]]:
    rows = []
    for coeffs in product(range(prime), repeat=6):
        a, b, c, d, e, f = coeffs
        if b != 0 or d != 0:
            continue
        if determinant(coeffs, prime) == 0:
            continue
        solution = affine_prime_line_solution(prime, coeffs)
        if not solution.is_ybe():
            continue
        rows.append(
            {
                "coefficients": coeffs,
                "involutive": is_involutive_solution(solution),
                "identity": all(solution.R[(x, y)] == (x, y) for x, y in solution.R),
            }
        )
    return rows


def finite_prime_checks(primes: Sequence[int]) -> dict[str, object]:
    checks = {}
    for prime in primes:
        scan = scan_affine_prime_line(prime)
        bidegenerate_rows = bidegenerate_bijective_affine_line_rows(prime)
        checks[f"F_{prime}"] = {
            "affine_ybe_count": scan["affine_ybe_count"],
            "terminal_survivor_count": scan["terminal_survivor_count"],
            "bidegenerate_bijective_ybe_rows": bidegenerate_rows,
            "bidegenerate_bijective_ybe_row_count": len(bidegenerate_rows),
            "all_bidegenerate_rows_identity": all(
                row["identity"] for row in bidegenerate_rows
            ),
        }
    return checks


def build_report() -> dict[str, object]:
    return {
        "title": "Affine-line classification audit",
        "ansatz": "r(x,y)=(a x+b y+c, d x+e y+f) over a field",
        "ybe_equations": YBE_EQUATIONS,
        "left_degenerate_condition": "b=0",
        "right_degenerate_condition": "d=0",
        "bijection_condition": "ae-bd != 0",
        "bidegenerate_classification": {
            "assumptions": "b=d=0 and ae != 0",
            "deduction": [
                "a(a-1)=0 and a != 0 force a=1",
                "e(1-e)=0 and e != 0 force e=1",
                "e(cd+f)=0 with d=0 and e=1 forces f=0",
                "the middle constant equation then forces c=0",
            ],
            "conclusion": "the only bidegenerate bijective affine-line YBE solution is r(x,y)=(x,y)",
            "consequence": "no bidegenerate non-involutive affine-line rigid core exists over any field",
        },
        "finite_prime_checks": finite_prime_checks((2, 3, 5, 7)),
        "conclusion": (
            "The prime-line scans over F_3, F_5, and F_7 are instances of an "
            "all-field lemma: bidegenerate bijective affine-line YBE maps are "
            "forced to be the identity solution.  Hence the one-dimensional "
            "affine-line family cannot contain a minimal rigid core."
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    classification = report["bidegenerate_classification"]
    lines = [
        "# Affine-Line Classification Audit",
        "",
        "This generated audit upgrades the finite affine-line scans to a",
        "symbolic all-field lemma for one-dimensional affine YBE maps.",
        "",
        "## Ansatz",
        "",
        f"`{report['ansatz']}`.",
        "",
        "The Yang-Baxter equation is equivalent to the following polynomial",
        "relations:",
        "",
    ]
    for equation in report["ybe_equations"]:
        lines.append(f"- `{equation}`;")
    lines.extend(
        [
            "",
            "The left-degenerate condition is `b=0`, the right-degenerate",
            "condition is `d=0`, and bijectivity is `ae-bd != 0`.",
            "",
            "## Bidegenerate Classification",
            "",
            f"Assume `{classification['assumptions']}`.",
            "",
        ]
    )
    for step in classification["deduction"]:
        lines.append(f"- {step};")
    lines.extend(
        [
            "",
            f"Conclusion: {classification['conclusion']}.",
            "",
            f"Consequence: {classification['consequence']}.",
            "",
            "## Finite Spot Checks",
            "",
        ]
    )
    for field, check in report["finite_prime_checks"].items():
        lines.extend(
            [
                f"### `{field}`",
                "",
                f"- affine YBE count: `{check['affine_ybe_count']}`;",
                f"- terminal survivor count: `{check['terminal_survivor_count']}`;",
                "- bidegenerate bijective YBE row count: "
                f"`{check['bidegenerate_bijective_ybe_row_count']}`;",
                "- all bidegenerate rows identity: "
                f"`{check['all_bidegenerate_rows_identity']}`.",
                "",
            ]
        )
    lines.extend(["## Conclusion", "", report["conclusion"]])
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    if argv not in (None, ()):
        raise SystemExit("no arguments are supported")
    report = build_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
