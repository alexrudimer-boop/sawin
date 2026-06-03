import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    derived_hurwitz_envelope_audit,
)


OUT_JSON = ROOT / "proofs" / "derived_hurwitz_envelope_audit.json"
OUT_MD = ROOT / "proofs" / "derived_hurwitz_envelope_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {
        repr(key): value
        for key, value in solution.R.items()
    }
    row["preimage_failure_count"] = audit.preimage_failure_count
    row["proves_nondegenerate_derived_hurwitz_envelope_prefix"] = (
        audit.proves_nondegenerate_derived_hurwitz_envelope_prefix
    )
    row["detects_degenerate_derived_operation_failure"] = (
        audit.detects_degenerate_derived_operation_failure
    )
    return row


def build_report():
    nondegenerate_prefix_witness = FiniteBraidedSet(
        (0, 1),
        {
            (0, 0): (1, 0),
            (0, 1): (0, 0),
            (1, 0): (1, 1),
            (1, 1): (0, 1),
        },
    )
    degenerate_identity = FiniteBraidedSet(
        (0, 1),
        {
            (0, 0): (0, 0),
            (0, 1): (0, 1),
            (1, 0): (1, 0),
            (1, 1): (1, 1),
        },
    )
    rows = []
    for name, solution in (
        ("nondegenerate_prefix_witness", nondegenerate_prefix_witness),
        ("degenerate_identity_failure", degenerate_identity),
    ):
        rows.append(_audit_dict(name, solution, derived_hurwitz_envelope_audit(solution)))
    report = {
        "description": (
            "Finite convention audit for the guitar-derived Hurwitz envelope "
            "and its degenerate preimage failure gate."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Derived Hurwitz envelope audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit checks finite rows for the route-(1)",
        "guitar-derived Hurwitz envelope.  It records one nondegenerate",
        "row where the derived rack envelope works and prefix bookkeeping",
        "is visibly needed, and one degenerate row where the derived",
        "operation is not total.",
        "",
        "## Rows",
        "",
    ]
    for row in report["rows"]:
        lines.extend(
            [
                f"### {row['name']}",
                "",
                f"- element count: `{row['element_count']}`;",
                f"- left nondegenerate: `{row['left_nondegenerate']}`;",
                f"- right nondegenerate: `{row['right_nondegenerate']}`;",
                f"- nondegenerate: `{row['nondegenerate']}`;",
                f"- derived operation total: `{row['derived_operation_total']}`;",
                f"- derived rack YBE: `{row['derived_rack_ybe']}`;",
                (
                    "- two-strand guitar conjugacy: "
                    f"`{row['two_strand_guitar_conjugacy']}`;"
                ),
                (
                    "- three-strand guitar conjugacy: "
                    f"`{row['three_strand_guitar_conjugacy']}`;"
                ),
                (
                    "- unaugmented interior forgetting matches: "
                    f"`{row['interior_forgetting_unaugmented_matches']}`;"
                ),
                f"- prefix left-group order: `{row['prefix_left_group_order']}`;",
                f"- preimage failure count: `{row['preimage_failure_count']}`;",
                (
                    "- proves nondegenerate derived-envelope prefix: "
                    f"`{row['proves_nondegenerate_derived_hurwitz_envelope_prefix']}`;"
                ),
                (
                    "- detects degenerate derived-operation failure: "
                    f"`{row['detects_degenerate_derived_operation_failure']}`."
                ),
                "",
            ]
        )
        if row["recorded_preimage_failures"]:
            lines.append("Recorded preimage failures:")
            lines.append("")
            for failure in row["recorded_preimage_failures"]:
                lines.append(
                    "- "
                    f"kind `{failure['kind']}`, "
                    f"derived label `{failure['derived_left_label']}`, "
                    f"original label `{failure['original_left_label']}`, "
                    f"preimages `{tuple(failure['preimages'])}`."
                )
            lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "For nondegenerate rows, the route object is not the raw",
            "`lambda/rho` operator label.  It is the guitar-conjugated",
            "derived rack envelope, augmented by the finite left-prefix",
            "group for point-forgetting bookkeeping.  For genuinely",
            "left-degenerate rows, the first finite obstruction is that",
            "the derived operation may not be a total function.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(report["rows"], sort_keys=True))


if __name__ == "__main__":
    main()
