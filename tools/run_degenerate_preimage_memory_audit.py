import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    degenerate_preimage_memory_audit,
)


OUT_JSON = ROOT / "proofs" / "degenerate_preimage_memory_audit.json"
OUT_MD = ROOT / "proofs" / "degenerate_preimage_memory_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {
        repr(key): value
        for key, value in solution.R.items()
    }
    row["hidden_preimage_memory_needed"] = audit.hidden_preimage_memory_needed
    row["visible_compression_is_safe"] = audit.visible_compression_is_safe
    row["records_degenerate_memory_gate"] = audit.records_degenerate_memory_gate
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
        ("nondegenerate_singleton_fibres", nondegenerate_prefix_witness),
        ("degenerate_identity_memory_gate", degenerate_identity),
    ):
        rows.append(_audit_dict(name, solution, degenerate_preimage_memory_audit(solution)))
    report = {
        "description": (
            "Finite preimage-memory audit for degenerate derived-Hurwitz "
            "preimage ambiguity."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Degenerate preimage memory audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the finite two-strand memory object",
        "for the degenerate derived-Hurwitz preimage gate.  A visible pair",
        "`(a,b)` asks for hidden neighbours `y` with `lambda_b(y)=a`.",
        "The nondegenerate derived rack route is exactly the singleton-fibre",
        "case.  The finite local repair keeps the edge-memory state",
        "`(a,b,y)` for actual pairs `(b,y)`, but this is not yet a tower",
        "proof; triple and quadruple consistency remain to be checked.",
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
                f"- visible pair count: `{row['visible_pair_count']}`;",
                f"- edge-memory state count: `{row['edge_memory_state_count']}`;",
                f"- singleton fibre count: `{row['singleton_fibre_count']}`;",
                f"- missing fibre count: `{row['missing_fibre_count']}`;",
                (
                    "- multiple same-candidate count: "
                    f"`{row['multiple_same_candidate_count']}`;"
                ),
                f"- ambiguous candidate count: `{row['ambiguous_candidate_count']}`;",
                (
                    "- visible derived operation total: "
                    f"`{row['visible_derived_operation_total']}`;"
                ),
                (
                    "- finite edge memory repairs two-strand gate: "
                    f"`{row['finite_edge_memory_repairs_two_strand']}`;"
                ),
                f"- tower consistency status: `{row['tower_consistency_status']}`;",
                (
                    "- hidden preimage memory needed: "
                    f"`{row['hidden_preimage_memory_needed']}`;"
                ),
                f"- visible compression is safe: `{row['visible_compression_is_safe']}`;",
                (
                    "- records degenerate memory gate: "
                    f"`{row['records_degenerate_memory_gate']}`."
                ),
                "",
            ]
        )
        if row["recorded_fibres"]:
            lines.append("Recorded nonsingleton fibres:")
            lines.append("")
            for fibre in row["recorded_fibres"]:
                lines.append(
                    "- "
                    f"status `{fibre['status']}`, "
                    f"derived label `{fibre['derived_left_label']}`, "
                    f"original label `{fibre['original_left_label']}`, "
                    f"preimages `{tuple(fibre['preimages'])}`."
                )
            lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "The finite edge-memory object repairs only the local ambiguity.",
            "A proof of the augmented Artin-envelope lemma still needs to",
            "show that these edge memories can be propagated through YBE",
            "triples and through point-forgetting with one fixed finite",
            "operator group and bounded vertical kernel.  A counterexample",
            "should look for failure of exactly that triple/quadruple",
            "compatibility, not for whole-image exponent growth.",
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
