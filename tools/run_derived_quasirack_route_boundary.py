from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "proofs" / "derived_quasirack_route_boundary.json"
OUT_MD = ROOT / "proofs" / "derived_quasirack_route_boundary.md"


def build_report() -> dict[str, object]:
    return {
        "title": "Derived quasi-rack route boundary",
        "source_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-derived-quasirack-route_partially_answered.md"
        ),
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-asymptotic-rigid-core-endpoint_ask_now.md"
        ),
        "cover_lemma": {
            "statement": (
                "If a finite YBE solution X is a homomorphic image of a finite "
                "left-nondegenerate solution Z, then X is dominated by a "
                "finite rack."
            ),
            "proof_steps": [
                "A surjective solution morphism pi:Z->X makes pi^n:Z^n->X^n B_n-equivariant and surjective.",
                "Therefore ker rho^Z_n <= ker rho^X_n for every n.",
                "By the left-nondegenerate derived/guitar theorem, some finite rack Y has ker rho^Y_n <= ker rho^Z_n for every n.",
                "Transitivity gives ker rho^Y_n <= ker rho^X_n for every n.",
            ],
            "status": "sufficient but not known to be necessary",
        },
        "derived_quasirack_target": {
            "kernel_target": (
                "construct a finite derived/quasi-rack object D(X) with "
                "ker rho^{D(X)}_n <= ker rho^X_n, or kernel equality after "
                "finite observer factors"
            ),
            "rack_domination_target": (
                "prove every finite D(X) is rack-dominated, for example by "
                "showing it is a Plonka sum, g-twist, or finite extension of "
                "actual racks with kernel-trivial fixed factors"
            ),
            "affine_f2_q3_model": (
                "the resolved affine F_2^3 candidate realizes this pattern: "
                "after a position-dependent twist, the moving factor is the "
                "tetrahedral rack and the remaining observer bits are fixed"
            ),
        },
        "quasirack_gap_example": {
            "name": "three_point_nonaffine_involutive_r1",
            "table_rows": [
                ["(0,0)", "(0,1)", "(2,0)"],
                ["(1,0)", "(1,1)", "(2,1)"],
                ["(0,2)", "(1,2)", "(2,2)"],
            ],
            "lambda_rows": {
                "lambda_0": (0, 0, 2),
                "lambda_1": (1, 1, 2),
                "lambda_2": (0, 1, 2),
            },
            "quasi_left_nondegenerate_failure": (
                "lambda_0 lambda_1 = (0,0,2) but lambda_1 lambda_0 = "
                "(1,1,2), so the idempotent commutation condition fails"
            ),
            "domination_status": (
                "involutive, hence dominated by the two-point flip rack"
            ),
            "lesson": (
                "quasi-rack literature covers an important degenerate subclass "
                "but does not automatically cover every finite bijective "
                "degenerate solution"
            ),
        },
        "open_requirements": [
            "define D(X) for genuinely degenerate finite bijective solutions without hidden nondegeneracy assumptions",
            "prove or refute the all-arity kernel comparison between D(X) and X",
            "prove or refute finite rack domination for the resulting quasi-rack class",
            "test the construction on a genuinely degenerate non-affine finite table of size at least four that is non-involutive",
        ],
        "conclusion": (
            "The cover lemma gives a useful sufficient branch, but the naive "
            "derived quasi-rack route is not yet a theorem for all degenerate "
            "solutions.  The next decisive test is a size-four or larger "
            "degenerate non-involutive table outside the quasi-left-"
            "nondegenerate subclass."
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    cover = report["cover_lemma"]
    target = report["derived_quasirack_target"]
    gap = report["quasirack_gap_example"]
    lines = [
        "# Derived Quasi-Rack Route Boundary",
        "",
        "This generated note records the current state of the cover and",
        "derived/quasi-rack routes.  The left-nondegenerate cover lemma is",
        "sufficient, but the naive quasi-rack route does not automatically",
        "cover every finite degenerate solution.",
        "",
        "## Cover Lemma",
        "",
        cover["statement"],
        "",
        "Proof sketch:",
        "",
    ]
    for step in cover["proof_steps"]:
        lines.append(f"- {step};")
    lines.extend(
        [
            "",
            f"Status: `{cover['status']}`.",
            "",
            "## Derived/Quasi-Rack Target",
            "",
            f"- kernel target: `{target['kernel_target']}`;",
            f"- rack-domination target: `{target['rack_domination_target']}`;",
            f"- affine F_2^3 model: `{target['affine_f2_q3_model']}`.",
            "",
            "## Quasi-Rack Gap Example",
            "",
            f"Name: `{gap['name']}`.",
            "",
            "Table rows:",
            "",
        ]
    )
    for row in gap["table_rows"]:
        lines.append(f"- `{row}`;")
    lines.extend(
        [
            "",
            f"- lambda rows: `{gap['lambda_rows']}`;",
            "- quasi-left-nondegenerate failure: "
            f"`{gap['quasi_left_nondegenerate_failure']}`;",
            f"- domination status: `{gap['domination_status']}`;",
            f"- lesson: `{gap['lesson']}`.",
            "",
            "## Open Requirements",
            "",
        ]
    )
    for item in report["open_requirements"]:
        lines.append(f"- {item};")
    lines.extend(
        [
            "",
            "## Prompt",
            "",
            f"Next prompt: `{report['next_prompt']}`.",
            "",
            "## Conclusion",
            "",
            report["conclusion"],
        ]
    )
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
