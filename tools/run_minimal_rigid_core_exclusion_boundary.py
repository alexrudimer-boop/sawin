from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "proofs" / "minimal_rigid_core_exclusion_boundary.json"
OUT_MD = ROOT / "proofs" / "minimal_rigid_core_exclusion_boundary.md"


def build_report() -> dict[str, object]:
    rigid_core_conditions = [
        "left and right degenerate",
        "non-involutive",
        (
            "not a rack and not braid-kernel equivalent to a finite rack "
            "through a finite total sequential gauge"
        ),
        "no nontrivial total YBE quotient congruence",
        "no nonempty proper crossing-closed subsolution",
        "no nonconstant one-state invariant observer",
        "not a flip-across or twisted union of proper dominated pieces",
        (
            "no proper active-factor certificate into racks or strictly smaller "
            "already dominated YBE solutions, even with optional invariant "
            "observer channels"
        ),
    ]
    terminal_branches = [
        "left- or right-nondegenerate solutions via the derived/guitar rack",
        "involutive solutions via the two-point flip rack",
        "flip-across unions of smaller dominated pieces via product racks",
        (
            "point-separating families of proper total YBE quotients, whose "
            "quotients are dominated by minimality"
        ),
        (
            "proper active-factor certificates into racks and smaller "
            "already dominated YBE solutions"
        ),
        "explicit finite sequential rack gauges or all-arity rack conjugacies",
    ]
    finite_search_checks = [
        "YBE and bijectivity",
        "left- and right-degeneracy",
        "non-involutivity",
        "quotient-rigidity by congruence enumeration",
        "absence of nonempty proper crossing-closed subsolutions",
        "observer-rigidity via the row-output connectivity graph",
        "absence of flip-across decompositions",
        (
            "absence of currently recognized transport-split, monodromy, or "
            "proper active-factor certificates"
        ),
        "real rack-prefix pressure N_{m,n}(X) != 1 for a small rack prefix",
    ]
    return {
        "title": "Minimal rigid-core exclusion boundary",
        "source_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-minimal-rigid-core-resolution_answered.md"
        ),
        "status": (
            "boundary theorem, not a proof of Sawin and not a finite "
            "counterexample"
        ),
        "strict_smaller_theorem": {
            "name": "Minimal rigid-core exclusion",
            "statement": (
                "No finite bijective set-theoretic YBE solution satisfies all "
                "rigid-core conditions."
            ),
            "conditions": rigid_core_conditions,
        },
        "implication": {
            "hypothesis": "Minimal rigid-core exclusion plus existing positive branches",
            "conclusion": "Every finite bijective YBE solution is dominated by a finite rack",
            "argument": (
                "Choose a counterexample of minimal cardinality.  Each terminal "
                "branch or proper quotient/active-factor mechanism gives a "
                "rack domination certificate by known closure theorems and "
                "minimality.  Therefore a minimal counterexample would be a "
                "rigid core, contradicting exclusion."
            ),
            "terminal_branches": terminal_branches,
        },
        "negative_target": {
            "description": (
                "A genuine Sawin-negative table must be a rigid core and must "
                "satisfy cofinal rack-prefix nonseparation."
            ),
            "rack_prefix": "P_m = Y_1 x ... x Y_m for an enumeration of finite racks",
            "joint_image": (
                "Gamma_{m,n}(X)=< (rho^{P_m}_n(sigma_i), "
                "rho^X_n(sigma_i)) : 1 <= i < n >"
            ),
            "detector_kernel_image": (
                "N_{m,n}(X)={g_X : (1,g_X) in Gamma_{m,n}(X)}"
            ),
            "cofinal_obstruction": "for all m there exists n with N_{m,n}(X) != 1",
        },
        "finite_table_search_checks": finite_search_checks,
        "current_known_status": [
            "No proof of minimal rigid-core exclusion is recorded.",
            "No finite table with cofinal rack-prefix obstruction is recorded.",
            (
                "The affine F_2^3 q=3 pressure row is already resolved "
                "positively by all-arity kernel equality with the tetrahedral "
                "four-element rack."
            ),
            (
                "Future negative evidence must show cofinal rack-prefix "
                "pressure, not merely pressure against a bounded rack prefix."
            ),
        ],
        "conclusion": (
            "The current exact endpoint is: prove minimal rigid-core exclusion, "
            "or find a rigid core and then prove the cofinal nontriviality of "
            "N_{m,n}(X)."
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    theorem = report["strict_smaller_theorem"]
    implication = report["implication"]
    negative = report["negative_target"]
    lines = [
        "# Minimal Rigid-Core Exclusion Boundary",
        "",
        f"Status: {report['status']}.",
        "",
        "This generated note records the Pro response to the minimal rigid-core",
        "prompt.  It does not claim a proof of Sawin's problem.  It isolates",
        "the strict theorem that would now close the existing proof strategy,",
        "and the exact extra property a finite counterexample would need.",
        "",
        "## Strict Smaller Theorem",
        "",
        f"Name: `{theorem['name']}`.",
        "",
        theorem["statement"],
        "",
        "A rigid core is a finite bijective YBE solution satisfying all of:",
        "",
    ]
    for condition in theorem["conditions"]:
        lines.append(f"- {condition};")
    lines.extend(
        [
            "",
            "## Why It Implies Sawin-Positive",
            "",
            f"Hypothesis: `{implication['hypothesis']}`.",
            "",
            f"Conclusion: `{implication['conclusion']}`.",
            "",
            implication["argument"],
            "",
            "The terminal or proper-factor branches used in the minimality",
            "argument are:",
            "",
        ]
    )
    for branch in implication["terminal_branches"]:
        lines.append(f"- {branch};")
    lines.extend(
        [
            "",
            "## Genuine Negative Target",
            "",
            negative["description"],
            "",
            "For an enumeration of finite racks, set:",
            "",
            f"- rack prefix: `{negative['rack_prefix']}`;",
            f"- joint image: `{negative['joint_image']}`;",
            f"- detector-kernel image: `{negative['detector_kernel_image']}`;",
            f"- cofinal obstruction: `{negative['cofinal_obstruction']}`.",
            "",
            "Thus a table that merely survives current certificates is not yet",
            "Sawin-negative.  It must also have nontrivial rack-prefix pressure",
            "cofinally in the rack enumeration.",
            "",
            "## Falsifiable Finite-Table Checks",
            "",
        ]
    )
    for check in report["finite_table_search_checks"]:
        lines.append(f"- {check};")
    lines.extend(
        [
            "",
            "## Current Known Status",
            "",
        ]
    )
    for item in report["current_known_status"]:
        lines.append(f"- {item}")
    lines.extend(["", "## Conclusion", "", report["conclusion"]])
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
