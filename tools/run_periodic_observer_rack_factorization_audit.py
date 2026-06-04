from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]

OUT_JSON = ROOT / "proofs" / "periodic_observer_rack_factorization_audit.json"
OUT_MD = ROOT / "proofs" / "periodic_observer_rack_factorization_audit.md"


def build_report() -> dict[str, object]:
    return {
        "title": "Periodic observer-rack factorization audit",
        "theorem": {
            "name": "Periodic observer-rack factorization",
            "data": [
                "finite bijective YBE solution X",
                "finite rack Y",
                "period d >= 1",
                "finite rack-output state set Q with initial states q_r for r in Z/d",
                "finite observer state set P with initial states p_r for r in Z/d",
                "transition maps delta:Q x X -> Q and Delta:P x X -> P",
                "output maps omega:Q x X -> Y and nu:P x X -> I",
            ],
            "local_equations": [
                "delta(delta(q,x),y)=delta(delta(q,u),v)",
                "r_Y(omega(q,x), omega(delta(q,x),y))=(omega(q,u), omega(delta(q,u),v))",
                "Delta(Delta(p,x),y)=Delta(Delta(p,u),v)",
                "(nu(p,x), nu(Delta(p,x),y))=(nu(p,u), nu(Delta(p,u),v))",
            ],
            "conclusion": (
                "If the left-to-right code Phi_n:X^n -> Y^n x I^n built "
                "from the n mod d initial states is injective for every n, "
                "then ker rho^Y_n <= ker rho^X_n for every n.  If the Y-output "
                "projection is surjective in every arity, then the kernels are "
                "equal."
            ),
            "proof_steps": [
                "The first two local equations give B_n-equivariance of the Y-output coordinate.",
                "The last two local equations give B_n-invariance of the observer coordinate.",
                "A Y-trivial braid fixes the Y-output and the observer output of every X-word.",
                "All-length injectivity of Phi_n forces the braid to fix every X-word.",
                "Surjectivity of the Y-output gives the reverse kernel inclusion.",
            ],
        },
        "examples": [
            {
                "name": "observer_product_s3_conjugation",
                "period": 1,
                "rack": "S_3 conjugation rack",
                "observer": "E={0,1} coordinate",
                "status": "kernel equality",
                "artifact": "proofs/observer_product_derived_route_boundary.md",
            },
            {
                "name": "affine_f2_q3_tetrahedral",
                "period": 3,
                "rack": "four-element tetrahedral Alexander rack",
                "observer": "n invariant F_2 bits r_i=sum_{j<i}(a_j+c_j)+a_i+b_i",
                "status": "kernel equality after shifted linear coordinates",
                "artifact": "proofs/affine_f2_q3_full_tetrahedral_conjugacy_audit.md",
            },
            {
                "name": "inert_observer_pointwise_subcase",
                "period": 1,
                "rack": "arbitrary finite rack Y",
                "observer": "pointwise observer o:X->I fixed coordinatewise",
                "status": "strict subcase of the periodic theorem",
                "artifact": "proofs/inert_observer_rack_factor_audit.md",
            },
        ],
        "relationship_to_sawin": {
            "strictly_stronger_than_domination": (
                "Kernel inclusion can hold without a finite symbolic "
                "left-to-right reconstruction.  Periodic observer-rack "
                "factorization is therefore a positive branch, not an "
                "equivalent reformulation of Sawin."
            ),
            "finite_checkability": (
                "For proposed finite data, the local equations are finite.  "
                "All-length injectivity is checked by the usual pair automaton "
                "for left-to-right transducer outputs."
            ),
        },
        "next_computation": (
            "Search sizes 5 and 6 for everywhere-singular rigid-core "
            "candidates, applying quotient/subsolution/observer/flip-across/"
            "minimal-image filters before any rack-prefix pressure computation."
        ),
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md"
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    theorem = report["theorem"]
    relation = report["relationship_to_sawin"]
    lines = [
        "# Periodic Observer-Rack Factorization Audit",
        "",
        "This generated audit records the all-arity positive mechanism",
        "underlying the observer-product and affine tetrahedral examples.",
        "",
        "## Theorem",
        "",
        f"Name: `{theorem['name']}`.",
        "",
        "Data:",
        "",
    ]
    for item in theorem["data"]:
        lines.append(f"- {item};")
    lines.extend(["", "Local equations:", ""])
    for equation in theorem["local_equations"]:
        lines.append(f"- `{equation}`;")
    lines.extend(
        [
            "",
            f"Conclusion: {theorem['conclusion']}",
            "",
            "Proof steps:",
            "",
        ]
    )
    for step in theorem["proof_steps"]:
        lines.append(f"- {step};")
    lines.extend(
        [
            "",
            "## Examples",
            "",
            "| example | period | rack | observer | status | artifact |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for example in report["examples"]:
        lines.append(
            f"| `{example['name']}` | `{example['period']}` | "
            f"`{example['rack']}` | `{example['observer']}` | "
            f"`{example['status']}` | `{example['artifact']}` |"
        )
    lines.extend(
        [
            "",
            "## Relationship To Sawin",
            "",
            relation["strictly_stronger_than_domination"],
            "",
            relation["finite_checkability"],
            "",
            "## Next Computation",
            "",
            report["next_computation"],
            "",
            "## Next Prompt",
            "",
            f"`{report['next_prompt']}`.",
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
