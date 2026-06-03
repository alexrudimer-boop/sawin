import json
import sys
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_vertical_peiffer_square_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_vertical_peiffer_square_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_vertical_peiffer_square_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["row_count"] = audit.row_count
    row["all_defects_are_permutations"] = audit.all_defects_are_permutations
    row["all_single_transports_commute"] = audit.all_single_transports_commute
    row["all_peiffer_boundaries_identity"] = audit.all_peiffer_boundaries_identity
    row["nontrivial_peiffer_boundary_count"] = (
        audit.nontrivial_peiffer_boundary_count
    )
    row["total_peiffer_moved_tuple_count"] = audit.total_peiffer_moved_tuple_count
    row["defect_order_pair_spectrum"] = audit.defect_order_pair_spectrum
    row["peiffer_order_spectrum"] = audit.peiffer_order_spectrum
    row["verifies_first_vertical_peiffer_square_boundary"] = (
        audit.verifies_first_vertical_peiffer_square_boundary
    )
    by_pair = defaultdict(list)
    for square_row in audit.rows:
        by_pair[square_row.forget_stationary_indices].append(square_row)
    row["pair_summaries"] = {
        repr(pair): {
            "row_count": len(rows),
            "defect_order_pairs": sorted(
                {
                    (item.first_defect_order, item.second_defect_order)
                    for item in rows
                }
            ),
            "peiffer_orders": sorted(
                {item.peiffer_commutator_order for item in rows}
            ),
            "moved_tuple_count": sum(
                item.peiffer_moved_tuple_count for item in rows
            ),
            "nontrivial_boundary_count": sum(
                1 for item in rows if item.nontrivial_peiffer_boundary
            ),
        }
        for pair, rows in sorted(by_pair.items())
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
        ("degenerate_identity_peiffer_square", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_vertical_peiffer_square_audit(solution),
            )
        )
    report = {
        "description": (
            "First Peiffer commutator audit for diagonal vertical deletion "
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
        f"`{tuple(row['first_witness_target_input'])}` maps to "
        f"`{tuple(row['first_witness_after_commutator'])}`"
    )


def render_markdown(report):
    lines = [
        "# Prefix vertical Peiffer square audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit computes the first Peiffer square boundary for",
        "diagonal vertical deletion defects.  It fixes source point-pushing",
        "arity `5`.  For each deleted stationary pair `{i,j}`, it forms the",
        "two vertical defect permutations on the target tuple space after",
        "deleting both strands and computes their commutator",
        "",
        "```text",
        "[defect_i, defect_j]",
        "```",
        "",
        "using the repository's left-after-right permutation convention.",
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
                    "- all defects are permutations: "
                    f"`{row['all_defects_are_permutations']}`;"
                ),
                (
                    "- all single transports commute: "
                    f"`{row['all_single_transports_commute']}`;"
                ),
                (
                    "- all Peiffer boundaries identity: "
                    f"`{row['all_peiffer_boundaries_identity']}`;"
                ),
                (
                    "- nontrivial Peiffer boundary count: "
                    f"`{row['nontrivial_peiffer_boundary_count']}`;"
                ),
                (
                    "- total Peiffer moved tuple count: "
                    f"`{row['total_peiffer_moved_tuple_count']}`;"
                ),
                (
                    "- defect order-pair spectrum: "
                    f"`{tuple(row['defect_order_pair_spectrum'])}`;"
                ),
                (
                    "- Peiffer order spectrum: "
                    f"`{tuple(row['peiffer_order_spectrum'])}`;"
                ),
                (
                    "- verifies Peiffer square audit: "
                    f"`{row['verifies_first_vertical_peiffer_square_boundary']}`."
                ),
                "",
                "Pair summaries:",
                "",
            ]
        )
        for pair, summary in row["pair_summaries"].items():
            lines.append(
                "- "
                f"`{pair}`: defect orders `{tuple(summary['defect_order_pairs'])}`, "
                f"Peiffer orders `{tuple(summary['peiffer_orders'])}`, "
                f"moved tuples `{summary['moved_tuple_count']}`, "
                f"nontrivial boundaries `{summary['nontrivial_boundary_count']}`."
            )
        lines.extend(["", "Peiffer rows:", ""])
        for square_row in row["rows"]:
            lines.append(
                "- "
                f"delete `{tuple(square_row['forget_stationary_indices'])}`: "
                f"defect orders `({square_row['first_defect_order']}, "
                f"{square_row['second_defect_order']})`, "
                f"transports `({square_row['first_single_transport_commutes']}, "
                f"{square_row['second_single_transport_commutes']})`, "
                f"Peiffer order `{square_row['peiffer_commutator_order']}`, "
                f"identity `{square_row['peiffer_commutator_is_identity']}`, "
                f"moved tuples `{square_row['peiffer_moved_tuple_count']}`, "
                f"witness {_render_witness(square_row)}."
            )
        lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "For the nondegenerate prefix witness, the first Peiffer commutator",
            "boundary is trivial on every two-deletion face.  The diagonal",
            "vertical defects are order-two permutations, but their pair-face",
            "commutators are identity.",
            "",
            "For the degenerate identity row, the same Peiffer boundaries are",
            "identity for the trivial reason that all diagonal defects are",
            "identity permutations.",
            "",
            "This rules out the simplest square-boundary obstruction for this",
            "toy prefix surface.  It still does not prove finite rack domination:",
            "the next obstruction layer must normalize section choices and test",
            "whether higher or mixed square classes pull back from one fixed",
            "finite operator-label Hurwitz base.",
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
                    "nontrivial_peiffer_boundary_count": row[
                        "nontrivial_peiffer_boundary_count"
                    ],
                    "total_peiffer_moved_tuple_count": row[
                        "total_peiffer_moved_tuple_count"
                    ],
                    "defect_order_pair_spectrum": row[
                        "defect_order_pair_spectrum"
                    ],
                    "peiffer_order_spectrum": row["peiffer_order_spectrum"],
                    "verifies": row[
                        "verifies_first_vertical_peiffer_square_boundary"
                    ],
                }
                for row in report["rows"]
            ],
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
