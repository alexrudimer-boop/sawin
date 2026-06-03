import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import ybe_coskeletal_mechanism_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "ybe_coskeletal_mechanism_audit.json"
OUT_MD = ROOT / "proofs" / "ybe_coskeletal_mechanism_audit.md"


def build_report():
    audit = ybe_coskeletal_mechanism_audit()
    report = asdict(audit)
    report["case_keys"] = audit.case_keys
    report["records_ybe_coskeletal_mechanism_boundary"] = (
        audit.records_ybe_coskeletal_mechanism_boundary
    )
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# YBE coskeletal mechanism audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the YBE-specific side of the",
        "pullback-coskeletal question.  The point is not to add another",
        "bounded prefix computation.  The point is to state what kind of",
        "finite-type theorem would turn bounded prefix data into an",
        "all-arity pullback theorem.",
        "",
        "Finite bijective YBE data gives finite local transition rules and",
        "local generation of braid/deletion moves.  It does not automatically",
        "give local detection of the nonabelian deletion-cohomology class.",
        "The desired bounded theorem becomes formal only after adding finite",
        "operator labels satisfying genuine bounded-width descent for the",
        "point-pushing groupoids and their deletion coefficient bands.",
        "",
        "## Flags",
        "",
        (
            "- finite bijectivity gives local generation: "
            f"`{report['finite_bijectivity_gives_local_generation']}`;"
        ),
        (
            "- finite bijectivity does not give local cohomology detection: "
            f"`{report['finite_bijectivity_does_not_give_local_cohomology_detection']}`;"
        ),
        (
            "- bounded-state recursion would imply coskeletality: "
            f"`{report['bounded_state_recursion_would_imply_coskeletality']}`;"
        ),
        (
            "- high cross-effect bisections are a live obstruction: "
            f"`{report['high_cross_effect_bisections_are_live_obstruction']}`;"
        ),
        (
            "- w-local operator-label descent is an extra hypothesis: "
            f"`{report['w_local_operator_label_descent_is_extra_hypothesis']}`;"
        ),
        (
            "- coefficient inverse-limit condition recorded: "
            f"`{report['coefficient_inverse_limit_condition_recorded']}`;"
        ),
        (
            "- comparison commutes with inverse-limit reconstructions: "
            f"`{report['comparison_commutes_with_inverse_limits_recorded']}`;"
        ),
        (
            "- bounded relation arity cutoff recorded: "
            f"`{report['bounded_relation_arity_cutoff_recorded']}`;"
        ),
        (
            "- Brunnian cross-effect criterion recorded: "
            f"`{report['brunnian_cross_effect_criterion_recorded']}`;"
        ),
        (
            "- records YBE coskeletal mechanism boundary: "
            f"`{report['records_ybe_coskeletal_mechanism_boundary']}`."
        ),
        "",
        "## Conditional theorem",
        "",
        "Let the finite operator-label enrichment be `w`-local: the labelled",
        "point-pushing groupoid in arity `I` is the inverse limit of its",
        "restrictions to subsets of size at most `w`, and for deletion sets",
        "`D` with `|D| <= 3` the coefficient band `A_D^I` is the inverse",
        "limit of the `A_D^J` with `D subset J` and `|J| <= |D|+w`.",
        "The base coefficients must satisfy the same condition, and the",
        "comparison maps must be the inverse-limit extensions of their",
        "bounded-subset restrictions.",
        "",
        (
            "If transport, cocycle, and gauge equations are generated in "
            f"relation arity `r`, the cutoff is `{report['cutoff_formula']}`."
        ),
        report["conditional_pullback_coskeletal_theorem"],
        "",
        "The proof is formal from these hypotheses: nonabelian cochains,",
        "cocycles, gauges, and pullback equations are assembled by finite",
        "products, finite fibre products, and finite equalizers, which are",
        "preserved by the right Kan extension from the bounded arities.",
        "",
        "## Brunnian obstruction",
        "",
        f"`{report['brunnian_cross_effect_formula']}`.",
        "",
        report["brunnian_obstruction_criterion"],
        "",
        "Positive YBE-specific theorem obligations:",
        "",
        *[f"- {item};" for item in report["positive_ybe_theorem_obligations"]],
        "",
        "## Mechanisms",
        "",
    ]
    for case in report["cases"]:
        lines.extend(
            [
                f"### {case['key']}",
                "",
                f"- role: `{case['role']}`;",
                f"- mechanism: {case['mechanism']};",
                f"- finite YBE status: {case['finite_ybe_status']};",
                f"- theorem obligation: {case['theorem_obligation']};",
                f"- obstruction signature: {case['obstruction_signature']}.",
                "",
            ]
        )
    lines.extend(
        [
            "## Meaning",
            "",
            "The positive theorem route needs more than finite local moves.",
            "It needs `w`-local inverse-limit descent for the operator-labelled",
            "tower and coefficient bands, plus bounded relation arity for the",
            "transport, cocycle, and gauge equations.",
            "",
            "The negative route should not look for unbounded whole-image",
            "orders.  It should look for genuinely high-arity vertical",
            "`2`-cocycle classes whose restrictions to every bounded skeleton",
            "are gauge-trivial but whose all-arity class is not pulled back",
            "from one fixed finite operator-label base.  Equivalently, it should",
            "force nontrivial Brunnian relative deletion `2`-obstruction sets",
            "in arbitrarily large arities.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(
        json.dumps(
            {
                "case_keys": report["case_keys"],
                "records": report["records_ybe_coskeletal_mechanism_boundary"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
