import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import ybe_guitar_decoder_boundary_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "ybe_guitar_decoder_boundary_audit.json"
OUT_MD = ROOT / "proofs" / "ybe_guitar_decoder_boundary_audit.md"


def build_report():
    audit = ybe_guitar_decoder_boundary_audit()
    report = asdict(audit)
    report["case_keys"] = audit.case_keys
    report["records_guitar_decoder_boundary"] = (
        audit.records_guitar_decoder_boundary
    )
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# YBE guitar decoder boundary audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the exact boundary between the",
        "one-sided nondegenerate guitar-map theorem and the genuinely",
        "degenerate finite-state decoder problem.  In the nondegenerate",
        "branch, the decoder state is a finite group of suffix actions.  In",
        "the degenerate branch, the corresponding transformation monoid is",
        "still finite, but inverse branches are not canonical and become a",
        "deterministic cocycle obligation.",
        "",
        "## Flags",
        "",
        (
            "- right-guitar hypothesis recorded: "
            f"`{report['right_guitar_hypothesis_recorded']}`;"
        ),
        (
            "- derived rack operation recorded: "
            f"`{report['derived_rack_operation_recorded']}`;"
        ),
        (
            "- all-arity kernel equality recorded: "
            f"`{report['all_arity_kernel_equality_recorded']}`;"
        ),
        (
            "- finite-state decoder realization recorded: "
            f"`{report['finite_state_decoder_realization_recorded']}`;"
        ),
        (
            "- degenerate J2 failure recorded: "
            f"`{report['degenerate_j2_failure_recorded']}`;"
        ),
        (
            "- monoid inverse-branch gate recorded: "
            f"`{report['monoid_inverse_branch_gate_recorded']}`;"
        ),
        (
            "- no automatic unbounded-memory obstruction recorded: "
            f"`{report['no_automatic_unbounded_memory_obstruction_recorded']}`;"
        ),
        (
            "- deterministic decoder obligation recorded: "
            f"`{report['deterministic_decoder_obligation_recorded']}`;"
        ),
        (
            "- records guitar decoder boundary: "
            f"`{report['records_guitar_decoder_boundary']}`."
        ),
        "",
        "## Formulas",
        "",
        f"- right guitar: `{report['right_guitar_formula']}`;",
        f"- derived rack: `{report['derived_rack_formula']}`;",
        f"- kernel equality: `{report['kernel_equality_formula']}`;",
        f"- decoder state: `{report['decoder_state_formula']}`;",
        f"- degenerate J2 failure: `{report['degenerate_j2_failure_formula']}`;",
        f"- monoid gate: `{report['monoid_gate_formula']}`.",
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
            "The one-sided nondegenerate branch is closed: the finite derived",
            "rack has braid-action kernels equal to the original YBE solution",
            "in every arity.  This is precisely the finite-state decoder",
            "criterion with `Q=G_rho` and inverse suffix states.",
            "",
            "The degenerate branch does not automatically require unbounded",
            "memory, because `M_rho` is finite.  The missing theorem is sharper:",
            "choose coherent inverse branches over `M_rho` that satisfy the",
            "finite-state decoder equations and make the induced operation a",
            "rack.  Failure of those deterministic branch choices is the next",
            "direct-cover obstruction.",
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
                "records": report["records_guitar_decoder_boundary"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
