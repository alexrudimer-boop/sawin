import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import ybe_inverse_branch_determinization_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "ybe_inverse_branch_determinization_audit.json"
OUT_MD = ROOT / "proofs" / "ybe_inverse_branch_determinization_audit.md"


def build_report():
    audit = ybe_inverse_branch_determinization_audit()
    report = asdict(audit)
    report["case_keys"] = audit.case_keys
    report["records_inverse_branch_determinization_gate"] = (
        audit.records_inverse_branch_determinization_gate
    )
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# YBE inverse-branch determinization audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the sharpened boundary of the",
        "degenerate guitar route.  Replacing the suffix group `G_rho` by the",
        "finite transformation monoid `M_rho` gives a finite memory set, but",
        "a total deterministic monoid-guitar decoder would force the relevant",
        "one-sided YBE actions to be surjective, hence bijective for finite",
        "`X`.  Thus powersets, relation-valued branches, and Green-class data",
        "do not by themselves give a total rack cover in the genuinely",
        "degenerate case.",
        "",
        "## Flags",
        "",
        (
            "- total decoder surjectivity recorded: "
            f"`{report['total_decoder_surjectivity_recorded']}`;"
        ),
        (
            "- local surjectivity equation recorded: "
            f"`{report['local_surjectivity_equation_recorded']}`;"
        ),
        (
            "- finite side bijection forced: "
            f"`{report['finite_side_bijection_forced']}`;"
        ),
        (
            "- total monoid-guitar negative recorded: "
            f"`{report['total_monoid_guitar_negative_recorded']}`;"
        ),
        (
            "- powerset/relation failure recorded: "
            f"`{report['powerset_relation_failure_recorded']}`;"
        ),
        (
            "- Green rank-drop failure recorded: "
            f"`{report['green_rank_drop_failure_recorded']}`;"
        ),
        (
            "- restricted-language cocycle recorded: "
            f"`{report['restricted_language_cocycle_recorded']}`;"
        ),
        (
            "- nondeterministic kernel gap recorded: "
            f"`{report['nondeterministic_kernel_gap_recorded']}`;"
        ),
        (
            "- records inverse-branch determinization gate: "
            f"`{report['records_inverse_branch_determinization_gate']}`."
        ),
        "",
        "## Formulas",
        "",
        f"- initial state: `{report['initial_state_formula']}`;",
        (
            "- local surjectivity equation: "
            f"`{report['local_surjectivity_equation_formula']}`;"
        ),
        f"- forced bijection: `{report['forced_bijection_formula']}`;",
        f"- monoid rank: `{report['monoid_rank_formula']}`;",
        f"- branch cocycle: `{report['branch_cocycle_formula']}`.",
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
            "This does not refute finite rack domination.  It refutes a",
            "specific tempting shortcut: a total finite monoid-guitar",
            "determinization on all words.  If a degenerate solution is still",
            "rack-dominated, the cover must either use a non-guitar finite",
            "decoder or work through a restricted invariant language whose",
            "partial branch choices satisfy the remaining arity-3 cocycle.",
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
                "records": report["records_inverse_branch_determinization_gate"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
