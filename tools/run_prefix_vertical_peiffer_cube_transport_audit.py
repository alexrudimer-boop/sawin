import json
import sys
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_vertical_peiffer_cube_transport_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_vertical_peiffer_cube_transport_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_vertical_peiffer_cube_transport_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["row_count"] = audit.row_count
    row["all_peiffer_boundaries_transportable"] = (
        audit.all_peiffer_boundaries_transportable
    )
    row["all_peiffer_transports_commute"] = audit.all_peiffer_transports_commute
    row["all_pair_peiffer_boundaries_identity"] = (
        audit.all_pair_peiffer_boundaries_identity
    )
    row["all_triple_peiffer_boundaries_identity"] = (
        audit.all_triple_peiffer_boundaries_identity
    )
    row["total_mismatch_count"] = audit.total_mismatch_count
    row["total_pair_peiffer_moved_tuple_count"] = (
        audit.total_pair_peiffer_moved_tuple_count
    )
    row["total_triple_peiffer_moved_tuple_count"] = (
        audit.total_triple_peiffer_moved_tuple_count
    )
    row["peiffer_order_pair_spectrum"] = audit.peiffer_order_pair_spectrum
    row["verifies_first_vertical_peiffer_cube_transport"] = (
        audit.verifies_first_vertical_peiffer_cube_transport
    )
    by_triple = defaultdict(list)
    for cube_row in audit.rows:
        by_triple[cube_row.triple_forget_stationary_indices].append(cube_row)
    row["triple_summaries"] = {
        repr(triple): {
            "row_count": len(rows),
            "pair_faces": [item.pair_forget_stationary_indices for item in rows],
            "mismatch_count": sum(item.mismatch_count for item in rows),
            "peiffer_order_pairs": sorted(
                {
                    (item.pair_peiffer_order, item.triple_peiffer_order)
                    for item in rows
                }
            ),
            "pair_moved_tuple_count": sum(
                item.pair_peiffer_moved_tuple_count for item in rows
            ),
            "triple_moved_tuple_count": sum(
                item.triple_peiffer_moved_tuple_count for item in rows
            ),
        }
        for triple, rows in sorted(by_triple.items())
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
        ("degenerate_identity_peiffer_cube_transport", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_vertical_peiffer_cube_transport_audit(solution),
            )
        )
    report = {
        "description": (
            "Cube transport audit for vertical Peiffer square boundaries."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def _render_witness(row):
    if row["first_witness_pair_target_input"] is None:
        return "`none`"
    return (
        f"`{tuple(row['first_witness_pair_target_input'])}` gives left "
        f"`{tuple(row['first_left_after_pair_peiffer_then_delete'])}` and "
        f"right `{tuple(row['first_right_after_delete_then_triple_peiffer'])}`"
    )


def render_markdown(report):
    lines = [
        "# Prefix vertical Peiffer cube-transport audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit checks the first cube-level transport law for",
        "vertical Peiffer square boundaries.  It fixes source point-pushing",
        "arity `5`.  For each deleted triple `T` and each pair face",
        "`F subset T`, it compares",
        "",
        "```text",
        "delete_{T-F} after Peiffer_F",
        "=",
        "Peiffer_T(F) after delete_{T-F}.",
        "```",
        "",
        "This is a low-dimensional cubical coherence check for the normalized",
        "deletion two-cocycle described by the external theoretical pressure",
        "test: it is not yet the quotient by section gauge or by pullback from",
        "a fixed finite operator-label Hurwitz base.",
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
                    "- all Peiffer boundaries transportable: "
                    f"`{row['all_peiffer_boundaries_transportable']}`;"
                ),
                (
                    "- all Peiffer transports commute: "
                    f"`{row['all_peiffer_transports_commute']}`;"
                ),
                (
                    "- all pair Peiffer boundaries identity: "
                    f"`{row['all_pair_peiffer_boundaries_identity']}`;"
                ),
                (
                    "- all triple Peiffer boundaries identity: "
                    f"`{row['all_triple_peiffer_boundaries_identity']}`;"
                ),
                f"- total mismatch count: `{row['total_mismatch_count']}`;",
                (
                    "- total pair Peiffer moved tuple count: "
                    f"`{row['total_pair_peiffer_moved_tuple_count']}`;"
                ),
                (
                    "- total triple Peiffer moved tuple count: "
                    f"`{row['total_triple_peiffer_moved_tuple_count']}`;"
                ),
                (
                    "- Peiffer order-pair spectrum: "
                    f"`{tuple(row['peiffer_order_pair_spectrum'])}`;"
                ),
                (
                    "- verifies cube transport audit: "
                    f"`{row['verifies_first_vertical_peiffer_cube_transport']}`."
                ),
                "",
                "Triple summaries:",
                "",
            ]
        )
        for triple, summary in row["triple_summaries"].items():
            lines.append(
                "- "
                f"`{triple}`: rows `{summary['row_count']}`, "
                f"pairs `{tuple(tuple(face) for face in summary['pair_faces'])}`, "
                f"mismatches `{summary['mismatch_count']}`, "
                f"Peiffer orders `{tuple(summary['peiffer_order_pairs'])}`, "
                f"pair moved `{summary['pair_moved_tuple_count']}`, "
                f"triple moved `{summary['triple_moved_tuple_count']}`."
            )
        lines.extend(["", "Cube transport rows:", ""])
        for cube_row in row["rows"]:
            lines.append(
                "- "
                f"triple `{tuple(cube_row['triple_forget_stationary_indices'])}`, "
                f"pair `{tuple(cube_row['pair_forget_stationary_indices'])}`, "
                f"extra `{cube_row['extra_stationary_index']}`: "
                f"pair/triple Peiffer orders "
                f"`({cube_row['pair_peiffer_order']}, "
                f"{cube_row['triple_peiffer_order']})`, "
                f"transport commutes `{cube_row['peiffer_transport_commutes']}`, "
                f"mismatches `{cube_row['mismatch_count']}`, "
                f"witness {_render_witness(cube_row)}."
            )
        lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "For the nondegenerate prefix witness, all `30` cube-transport",
            "rows commute.  The transported pair Peiffer boundaries and the",
            "direct triple-face Peiffer boundaries are all identity.",
            "",
            "For the degenerate identity row, the same cube-transport checks are",
            "trivial for the identity-defect reason.",
            "",
            "This eliminates the first cubical coherence obstruction for the",
            "current prefix surface.  The remaining pressure test is the",
            "section-change/gauge quotient and the pullback test against one",
            "fixed finite operator-label Hurwitz base.",
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
                    "peiffer_order_pair_spectrum": row[
                        "peiffer_order_pair_spectrum"
                    ],
                    "verifies": row[
                        "verifies_first_vertical_peiffer_cube_transport"
                    ],
                }
                for row in report["rows"]
            ],
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
