import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import ybe_brunnian_derivative_gate_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "ybe_brunnian_derivative_gate_audit.json"
OUT_MD = ROOT / "proofs" / "ybe_brunnian_derivative_gate_audit.md"


def build_report():
    audit = ybe_brunnian_derivative_gate_audit()
    report = asdict(audit)
    report["case_keys"] = audit.case_keys
    report["records_brunnian_derivative_gate"] = (
        audit.records_brunnian_derivative_gate
    )
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# YBE Brunnian derivative gate audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the next Brunnian pressure-test.",
        "The naive route from Brunnian pure braids to deletion-degree-2",
        "obstructions is false: ordinary one-strand point-pushing derivatives",
        "are section-gauge coboundaries.  The real target is the residual",
        "double-deletion quotient after modding out one-strand derivatives,",
        "bounded two-strand mutual data, and fixed-base pullback.",
        "",
        "## Flags",
        "",
        (
            "- naive Brunnian pure-braid obstruction rejected: "
            f"`{report['naive_brunnian_pure_braid_obstruction_rejected']}`;"
        ),
        (
            "- one-strand derivatives are gauge coboundaries: "
            f"`{report['one_strand_derivatives_are_gauge_coboundaries']}`;"
        ),
        (
            "- Brunnian point-push shadow is gauge: "
            f"`{report['brunnian_point_push_shadow_is_gauge']}`;"
        ),
        (
            "- nonabelian derivative chain rule recorded: "
            f"`{report['nonabelian_derivative_chain_rule_recorded']}`;"
        ),
        (
            "- residual double-deletion quotient identified: "
            f"`{report['residual_double_deletion_quotient_identified']}`;"
        ),
        (
            "- Fadell-Neuwirth decomposition would kill high Brunnian classes: "
            f"`{report['fadell_neuwirth_decomposition_would_kill_high_brunnian_classes']}`;"
        ),
        (
            "- records Brunnian derivative gate: "
            f"`{report['records_brunnian_derivative_gate']}`."
        ),
        "",
        "## Formulas",
        "",
        f"- derivative: `{report['derivative_formula']}`;",
        f"- gauge: `{report['gauge_formula']}`;",
        f"- chain rule: `{report['chain_rule_formula']}`;",
        f"- residual quotient: `{report['residual_quotient_formula']}`;",
        f"- decomposition route: `{report['decomposition_formula']}`.",
        "",
        "## Rows",
        "",
    ]
    for case in report["cases"]:
        lines.extend(
            [
                f"### {case['key']}",
                "",
                f"- role: `{case['role']}`;",
                f"- statement: {case['statement']};",
                f"- consequence: {case['consequence']}.",
                "",
            ]
        )
    lines.extend(
        [
            "## Meaning",
            "",
            "Brunnian point-pushing can produce high-arity vertical bisections,",
            "but their ordinary two-deletion shadows are gauge.  A genuine",
            "relative deletion `2`-obstruction must survive the residual",
            "quotient `R_{p,q}^I`.",
            "",
            "Thus the positive route is now sharper: prove a Fadell-Neuwirth",
            "decomposition of every double-deletion vertical bisection into",
            "one-strand derivatives, bounded mutual terms, and fixed-base",
            "pullback.  The negative route must construct a residual element",
            "of `R_{p,q}^I`, not just a Brunnian pure braid.",
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
                "records": report["records_brunnian_derivative_gate"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
