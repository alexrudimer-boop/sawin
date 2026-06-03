import json
import sys
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_vertical_defect_transport_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_vertical_defect_transport_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_vertical_defect_transport_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["row_count"] = audit.row_count
    row["all_additional_faces_surjective"] = audit.all_additional_faces_surjective
    row["all_defects_are_transportable"] = audit.all_defects_are_transportable
    row["all_transports_commute"] = audit.all_transports_commute
    row["total_mismatch_count"] = audit.total_mismatch_count
    row["order_pair_spectrum"] = audit.order_pair_spectrum
    row["verifies_first_vertical_defect_face_transport"] = (
        audit.verifies_first_vertical_defect_face_transport
    )
    by_transition = defaultdict(list)
    for transport_row in audit.rows:
        by_transition[
            (
                transport_row.from_deletion_level,
                transport_row.to_deletion_level,
            )
        ].append(transport_row)
    row["transition_summaries"] = {
        f"{source}->{target}": {
            "row_count": len(rows),
            "mismatch_count": sum(item.mismatch_count for item in rows),
            "order_pair_spectrum": sorted(
                {
                    (item.from_defect_order, item.to_defect_order)
                    for item in rows
                }
            ),
            "identity_pair_count": sum(
                1
                for item in rows
                if item.from_identity_defect and item.to_identity_defect
            ),
            "transport_commuting_count": sum(
                1 for item in rows if item.transport_commutes
            ),
        }
        for (source, target), rows in sorted(by_transition.items())
    }
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
        ("degenerate_identity_vertical_transport", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_vertical_defect_transport_audit(solution),
            )
        )
    report = {
        "description": (
            "Face-transport audit for already-vertical diagonal deletion "
            "defects."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def _render_witness(row):
    if row["first_witness_target_input"] is None:
        return "`none`"
    return (
        f"`{tuple(row['first_witness_target_input'])}` gives left "
        f"`{tuple(row['first_left_after_defect_then_delete'])}` and right "
        f"`{tuple(row['first_right_after_delete_then_defect'])}`"
    )


def render_markdown(report):
    lines = [
        "# Prefix vertical defect transport audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit checks the first face-transport law for the",
        "vertical coefficient candidates extracted from diagonal",
        "point-forgetting defects.  It fixes source point-pushing arity `5`",
        "and asks whether an already-vertical defect remains compatible after",
        "one additional stationary strand is deleted.",
        "",
        "For a deletion face `F`, an extra stationary index `r` not in `F`,",
        "and a source generator `i` already in `F`, it checks the square",
        "",
        "```text",
        "delete_r after defect_F  =  defect_{F union {r}} after delete_r",
        "```",
        "",
        "on all post-deletion target tuples.",
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
                (
                    "- left-prefix monoid size: "
                    f"`{row['left_prefix_monoid_size']}`;"
                ),
                f"- nonunit prefix count: `{row['nonunit_prefix_count']}`;",
                f"- source point-pushing arity: `{row['source_point_pushing_arity']}`;",
                f"- row count: `{row['row_count']}`;",
                (
                    "- all additional faces surjective: "
                    f"`{row['all_additional_faces_surjective']}`;"
                ),
                (
                    "- all defects transportable: "
                    f"`{row['all_defects_are_transportable']}`;"
                ),
                f"- all transports commute: `{row['all_transports_commute']}`;",
                f"- total mismatch count: `{row['total_mismatch_count']}`;",
                f"- order-pair spectrum: `{tuple(row['order_pair_spectrum'])}`;",
                (
                    "- verifies transport audit: "
                    f"`{row['verifies_first_vertical_defect_face_transport']}`."
                ),
                "",
                "Transition summaries:",
                "",
            ]
        )
        for transition, summary in row["transition_summaries"].items():
            lines.append(
                "- "
                f"`{transition}`: rows `{summary['row_count']}`, "
                f"mismatches `{summary['mismatch_count']}`, "
                f"orders `{tuple(summary['order_pair_spectrum'])}`, "
                f"identity pairs `{summary['identity_pair_count']}`, "
                f"commuting rows `{summary['transport_commuting_count']}`."
            )
        lines.extend(["", "Transport rows:", ""])
        for transport_row in row["rows"]:
            lines.append(
                "- "
                f"`{transport_row['from_deletion_level']}` -> "
                f"`{transport_row['to_deletion_level']}`, "
                f"face `{tuple(transport_row['from_forget_stationary_indices'])}`, "
                f"extra `{transport_row['extra_stationary_index']}`, "
                f"target `{tuple(transport_row['to_forget_stationary_indices'])}`, "
                f"source `alpha_{{{transport_row['source_generator_index']},"
                f"{transport_row['source_braid_index']}}}`: "
                f"orders `({transport_row['from_defect_order']}, "
                f"{transport_row['to_defect_order']})`, "
                f"commutes `{transport_row['transport_commutes']}`, "
                f"mismatches `{transport_row['mismatch_count']}`, "
                f"witness {_render_witness(transport_row)}."
            )
        lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "For the nondegenerate prefix witness, every already-vertical",
            "order-two defect commutes with deleting one further stationary",
            "strand.  The vertical coefficient candidates therefore form a",
            "face-compatible system at this first transport layer.",
            "",
            "For the degenerate identity row, all transported defects are",
            "identity permutations, and all transport squares commute.",
            "",
            "This is still not a Peiffer/Postnikov obstruction.  It verifies",
            "only the functorial transport of already-existing vertical",
            "defects.  The next layer must compare two different vertical",
            "defects around a deletion square and quotient by the section",
            "change law.",
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
            [
                {
                    "name": row["name"],
                    "row_count": row["row_count"],
                    "total_mismatch_count": row["total_mismatch_count"],
                    "order_pair_spectrum": row["order_pair_spectrum"],
                    "transition_summaries": row["transition_summaries"],
                    "verifies": row[
                        "verifies_first_vertical_defect_face_transport"
                    ],
                }
                for row in report["rows"]
            ],
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
