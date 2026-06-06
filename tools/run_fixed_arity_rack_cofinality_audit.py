from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
OUT_JSON = ROOT / "proofs" / "fixed_arity_rack_cofinality_audit.json"
OUT_MD = ROOT / "proofs" / "fixed_arity_rack_cofinality_audit.md"


SOURCE_URLS = {
    "mcreynolds": "https://arxiv.org/abs/0901.4663",
    "stylianakis": "https://eprints.gla.ac.uk/159155/1/159155.pdf",
    "brendle_notes": "https://www.maths.gla.ac.uk/~tbrendle/papers/BraidCongruence.pdf",
}


def build_report() -> dict[str, object]:
    return {
        "title": "Fixed-arity rack cofinality audit",
        "source_urls": SOURCE_URLS,
        "literature_input": {
            "name": "pure braid congruence subgroup property",
            "statement": (
                "For the Artin embedding P_n -> Aut(F_n), every finite-index "
                "subgroup of P_n contains a principal congruence kernel "
                "ker(P_n -> Aut(F_n/K)) for some characteristic finite-index "
                "subgroup K <= F_n."
            ),
            "status": (
                "Used as external literature input.  McReynolds records "
                "Thurston's proof for pure braid groups.  The full B_n "
                "fixed-arity theorem below adds an elementary congruence "
                "quotient detecting the strand permutation."
            ),
        },
        "fixed_arity_theorem": {
            "statement": (
                "Fix n >= 2. For every finite quotient representation "
                "theta:B_n -> H, there is a finite rack Y such that "
                "ker rho^Y_n <= ker theta."
            ),
            "detector": (
                "Y is the conjugation rack of G=F_n/K, where "
                "K=K_0 cap K_1 combines the mod-2 permutation quotient with "
                "the characteristic finite-index subgroup supplied by pure "
                "braid CSP."
            ),
            "proof_steps": [
                "Let N=ker theta. Since H is finite, N has finite index in B_n.",
                "Let P_n be the pure braid group and N_P=N cap P_n.",
                "By pure braid CSP, choose characteristic finite-index K_1 <= F_n with ker(P_n -> Aut(F_n/K_1)) <= N_P.",
                "Let K_0=[F_n,F_n]F_n^2.  The induced action on F_n/K_0=(Z/2)^n records the strand permutation, so ker(B_n -> Aut(F_n/K_0)) <= P_n.",
                "Set K=K_0 cap K_1, still characteristic and finite-index.  If beta acts trivially on F_n/K, then beta acts trivially on F_n/K_0 and F_n/K_1; hence beta in P_n and then beta in N_P <= N.",
                "Set G=F_n/K and give G the conjugation rack operation a*b=aba^{-1}.",
                "Under the standard Artin convention sigma_i sends (x_i,x_{i+1}) to (x_i x_{i+1} x_i^{-1}, x_i), which is exactly the conjugation rack crossing on the tuple of quotient generators.",
                "If beta is trivial on the rack action on G^n, it fixes every tuple, in particular the tuple of quotient free generators.",
                "Those quotient generators generate G, so beta is trivial in Aut(G), hence beta lies in ker(B_n -> Aut(F_n/K)) <= N.",
            ],
            "consequence_for_ybe": (
                "For every finite YBE solution X and every fixed arity n, "
                "some finite rack Y_n satisfies ker rho^{Y_n}_n <= ker rho^X_n."
            ),
        },
        "sharpened_negative_condition": {
            "old_condition": "forall m exists n with N_{m,n}(X) != 1",
            "new_condition": "forall m forall N exists n>N with N_{m,n}(X) != 1",
            "proof": [
                "Let P be a finite product of racks.",
                "If P dominates X in all arities above N_0, use fixed-arity cofinality to choose racks Q_n for the bounded arities 2 <= n <= N_0.",
                "Then Y=P x product_{2 <= n <= N_0} Q_n is a finite rack dominating X in every arity.",
                "Therefore a genuinely non-dominated X must have rack-prefix pressure above every finite arity cutoff.",
            ],
        },
        "asymptotic_endpoint": {
            "statement": (
                "No finite bijective YBE solution is simultaneously a rigid "
                "core and asymptotically rack-invisible, i.e. satisfies "
                "forall m forall N exists n>N with N_{m,n}(X) != 1."
            ),
            "why_it_implies_sawin_yes": (
                "A minimal Sawin counterexample must avoid all settled positive "
                "branches, hence must be rigid. Fixed-arity rack cofinality "
                "then forces its obstruction to be unbounded in arity. "
                "Excluding asymptotically rack-invisible rigid cores excludes "
                "minimal counterexamples."
            ),
            "strictly_smaller_than_rigid_core_exclusion": (
                "Rigid-looking cores whose rack-prefix pressure is bounded in "
                "arity no longer need to be excluded separately, because "
                "fixed-arity cofinality would patch the bounded arities."
            ),
        },
        "singular_coordinate_filter": {
            "statement": (
                "A minimal counterexample outside the left/right-nondegenerate "
                "branches and with no proper crossing-closed subsolution has "
                "every L_x and every R_x non-bijective."
            ),
            "proof_steps": [
                "Let U_L={x: L_x is bijective}.",
                "The first YBE component identity gives L_{L_x(y)} L_{R_y(x)} = L_x L_y.",
                "If x,y in U_L, the right side is bijective; over a finite set both left-side factors are bijective.",
                "Thus r(U_L^2) is contained in U_L^2, and bijectivity of r makes this equality.",
                "So U_L is empty, all of X, or a proper crossing-closed subsolution.",
                "The left-nondegenerate branch excludes U_L=X, and the no-proper-subsolution rigid-core condition excludes nonempty proper U_L.",
                "The same argument using R_z R_y = R_{R_z(y)} R_{L_y(z)} gives the right-coordinate conclusion.",
            ],
            "finite_table_filter": (
                "A rigid-core search can reject any nonterminal candidate with "
                "at least one bijective left coordinate map or at least one "
                "bijective right coordinate map."
            ),
        },
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md"
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    theorem = report["fixed_arity_theorem"]
    negative = report["sharpened_negative_condition"]
    endpoint = report["asymptotic_endpoint"]
    singular = report["singular_coordinate_filter"]
    literature = report["literature_input"]
    lines = [
        "# Fixed-Arity Rack Cofinality Audit",
        "",
        "This generated audit records a sharpened endpoint for the finite-rack",
        "domination problem.  It uses the pure braid congruence subgroup",
        "property as an external theorem, plus an elementary permutation",
        "quotient to pass from pure braids to the full braid group.",
        "",
        "## Literature Input",
        "",
        f"Name: `{literature['name']}`.",
        "",
        f"Statement used: {literature['statement']}",
        "",
        f"Status: {literature['status']}",
        "",
        "Sources checked:",
        "",
    ]
    for name, url in report["source_urls"].items():
        lines.append(f"- `{name}`: {url}")
    lines.extend(
        [
            "",
            "## Fixed-Arity Theorem",
            "",
            theorem["statement"],
            "",
            f"Detector: {theorem['detector']}",
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
            f"Consequence: {theorem['consequence_for_ybe']}",
            "",
            "## Sharpened Negative Condition",
            "",
            f"Old condition: `{negative['old_condition']}`.",
            "",
            f"New condition: `{negative['new_condition']}`.",
            "",
            "Reason:",
            "",
        ]
    )
    for step in negative["proof"]:
        lines.append(f"- {step};")
    lines.extend(
        [
            "",
            "## Asymptotic Endpoint",
            "",
            endpoint["statement"],
            "",
            f"Why it implies Sawin YES: {endpoint['why_it_implies_sawin_yes']}",
            "",
            "Why this is sharper than full rigid-core exclusion: "
            f"{endpoint['strictly_smaller_than_rigid_core_exclusion']}",
            "",
            "## Singular Coordinate Filter",
            "",
            singular["statement"],
            "",
            "Proof steps:",
            "",
        ]
    )
    for step in singular["proof_steps"]:
        lines.append(f"- {step};")
    lines.extend(
        [
            "",
            f"Finite-table filter: {singular['finite_table_filter']}",
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
