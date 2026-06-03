import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import ybe_finite_state_rack_cover_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "ybe_finite_state_rack_cover_audit.json"
OUT_MD = ROOT / "proofs" / "ybe_finite_state_rack_cover_audit.md"


def build_report():
    audit = ybe_finite_state_rack_cover_audit()
    report = asdict(audit)
    report["case_keys"] = audit.case_keys
    report["records_finite_state_rack_cover_criterion"] = (
        audit.records_finite_state_rack_cover_criterion
    )
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# YBE finite-state rack-cover audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the obstruction to the most tempting",
        "direct rack-cover construction.  A rack crossing copies one strand,",
        "whereas a general bijective YBE crossing updates both strands.  Finite",
        "labels attached coordinatewise to `X` do not remove that mismatch.",
        "The only remaining direct-cover formulation is a finite-state decoder",
        "whose state can reinterpret the copied rack strand after a crossing.",
        "",
        "## Flags",
        "",
        (
            "- coordinatewise rack quotient obstruction identified: "
            f"`{report['coordinatewise_rack_quotient_obstruction_identified']}`;"
        ),
        (
            "- fibre-label first-coordinate obstruction identified: "
            f"`{report['fiber_label_first_coordinate_obstruction_identified']}`;"
        ),
        (
            "- rack-shadow identity recorded: "
            f"`{report['rack_shadow_identity_recorded']}`;"
        ),
        (
            "- label cocycle equation recorded: "
            f"`{report['label_cocycle_equation_recorded']}`;"
        ),
        (
            "- finite-state decoder criterion recorded: "
            f"`{report['finite_state_decoder_criterion_recorded']}`;"
        ),
        (
            "- decoder surjectivity requirement recorded: "
            f"`{report['decoder_surjectivity_requirement_recorded']}`;"
        ),
        (
            "- structure-group obstruction recorded: "
            f"`{report['structure_group_obstruction_recorded']}`;"
        ),
        (
            "- right-update defect identified: "
            f"`{report['right_update_defect_identified']}`;"
        ),
        (
            "- records finite-state rack-cover criterion: "
            f"`{report['records_finite_state_rack_cover_criterion']}`."
        ),
        "",
        "## Formulas",
        "",
        f"- rack switch: `{report['rack_switch_formula']}`;",
        f"- coordinatewise obstruction: `{report['coordinatewise_obstruction_formula']}`;",
        f"- rack-shadow identity: `{report['rack_shadow_identity_formula']}`;",
        f"- YBE twisted identity: `{report['ybe_twisted_identity_formula']}`;",
        f"- label cocycle: `{report['label_cocycle_formula']}`;",
        f"- decoder equations: `{report['decoder_equations_formula']}`;",
        f"- right-update defect: `{report['right_update_defect_formula']}`.",
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
            "The naive coordinatewise construction is not a proof strategy for",
            "Sawin's question.  It would force the right action to be trivial",
            "under the rack convention `R_Y(a,b)=(a > b,a)`, and the opposite",
            "convention analogously forces the left action to be trivial.",
            "",
            "The sharper positive route is finite-state rather than",
            "coordinatewise: find a finite rack `Y`, a finite decoder state set",
            "`Q`, maps `d` and `tau`, and surjective decoded maps `Phi_n` for",
            "every arity.  The sharper negative route is to prove that no such",
            "finite decoder can absorb the right-update defect",
            "`Delta(x,y)=lambda_{rho_y(x)} lambda_x^-1` for a given solution.",
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
                "records": report["records_finite_state_rack_cover_criterion"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
