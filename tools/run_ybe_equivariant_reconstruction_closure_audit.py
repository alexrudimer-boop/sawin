import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import ybe_equivariant_reconstruction_closure_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "ybe_equivariant_reconstruction_closure_audit.json"
OUT_MD = ROOT / "proofs" / "ybe_equivariant_reconstruction_closure_audit.md"


def build_report():
    audit = ybe_equivariant_reconstruction_closure_audit()
    report = asdict(audit)
    report["case_keys"] = audit.case_keys
    report["records_equivariant_reconstruction_closure_gate"] = (
        audit.records_equivariant_reconstruction_closure_gate
    )
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# YBE equivariant reconstruction closure audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the sharp gluing theorem for finite",
        "families of known quotient, subsolution, and subquotient detector",
        "towers.  The safe principle is not merely that dominated pieces",
        "exist; their marked braid-action factors must reconstruct the whole",
        "`X^n` action equivariantly and injectively, or the visible kernel",
        "must be proved trivial on hidden reconstruction fibres.",
        "",
        "## Flags",
        "",
        (
            "- marked tower reconstruction recorded: "
            f"`{report['marked_tower_reconstruction_recorded']}`;"
        ),
        (
            "- product kernel implication recorded: "
            f"`{report['product_kernel_implication_recorded']}`;"
        ),
        (
            "- total quotient corollary recorded: "
            f"`{report['total_quotient_corollary_recorded']}`;"
        ),
        (
            "- partial domain totalization required: "
            f"`{report['partial_domain_totalization_required']}`;"
        ),
        (
            "- point separation insufficient recorded: "
            f"`{report['point_separation_insufficient_recorded']}`;"
        ),
        (
            "- off-diagonal transition data required: "
            f"`{report['off_diagonal_transition_data_required']}`;"
        ),
        (
            "- arity-3 extension cocycle obstruction recorded: "
            f"`{report['arity3_extension_cocycle_obstruction_recorded']}`;"
        ),
        (
            "- hidden fibre kernel criterion recorded: "
            f"`{report['hidden_fibre_kernel_criterion_recorded']}`;"
        ),
        (
            "- records equivariant reconstruction closure gate: "
            f"`{report['records_equivariant_reconstruction_closure_gate']}`."
        ),
        "",
        "## Formulas",
        "",
        f"- reconstruction: `{report['reconstruction_formula']}`;",
        f"- product kernel: `{report['product_kernel_formula']}`;",
        f"- total quotients: `{report['total_quotient_formula']}`;",
        f"- visible kernel: `{report['visible_kernel_formula']}`;",
        f"- hidden fibres: `{report['hidden_fibre_formula']}`;",
        f"- partial domains: `{report['partial_domain_formula']}`;",
        f"- extension cocycle: `{report['extension_cocycle_formula']}`;",
        f"- arity-3 stress test: `{report['arity3_stress_formula']}`.",
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
            "If total marked factors `T^alpha_bullet` are dominated by finite",
            "racks and the product map `F_n:X^n -> product_alpha T^alpha_n`",
            "is `B_n`-equivariant and injective for every `n`, then the",
            "coordinatewise product rack dominates `X`.  This is just the",
            "kernel argument through the product action.",
            "",
            "For genuine total YBE quotients, point-separating quotient maps",
            "are enough because the coordinatewise product remains injective",
            "in every arity.  For partial subquotients or block data, one must",
            "first promote the data to total marked braid factors.  If the",
            "visible product map is not injective, the exact remaining",
            "criterion is triviality of the visible-kernel action on each",
            "hidden reconstruction fibre.",
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
                "hidden_fibre_criterion": report[
                    "hidden_fibre_kernel_criterion_recorded"
                ],
                "records": report[
                    "records_equivariant_reconstruction_closure_gate"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
