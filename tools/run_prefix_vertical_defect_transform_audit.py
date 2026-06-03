import json
import sys
from collections import defaultdict
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_vertical_defect_transform_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_vertical_defect_transform_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_vertical_defect_transform_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["row_count"] = audit.row_count
    row["all_defects_well_defined"] = audit.all_defects_well_defined
    row["all_defects_are_permutations"] = audit.all_defects_are_permutations
    row["nontrivial_defect_count"] = audit.nontrivial_defect_count
    row["order_spectrum"] = audit.order_spectrum
    row["verifies_vertical_defect_transform_extraction"] = (
        audit.verifies_vertical_defect_transform_extraction
    )
    by_level = defaultdict(list)
    for defect_row in audit.rows:
        by_level[defect_row.deletion_level].append(defect_row)
    row["level_summaries"] = {
        str(level): {
            "row_count": len(rows),
            "target_tuple_counts": sorted({item.target_tuple_count for item in rows}),
            "order_spectrum": sorted({item.defect_order for item in rows}),
            "identity_count": sum(1 for item in rows if item.identity_defect),
            "nontrivial_count": sum(1 for item in rows if item.nontrivial_defect),
            "distinct_defect_count": len({item.defect_permutation for item in rows}),
        }
        for level, rows in sorted(by_level.items())
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
        ("degenerate_identity_vertical_defects", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_vertical_defect_transform_audit(solution),
            )
        )
    report = {
        "description": (
            "Target-tuple transformation extraction for diagonal/deleted "
            "point-forgetting defects."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def _render_witness(row):
    if row["first_witness_input"] is None:
        return "`none`"
    return (
        f"`{tuple(row['first_witness_input'])}` has target input "
        f"`{tuple(row['first_deleted_input'])}` and maps to "
        f"`{tuple(row['first_deleted_after_source'])}`"
    )


def render_markdown(report):
    lines = [
        "# Prefix vertical defect transform audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit extracts the diagonal/deleted-generator",
        "point-forgetting defects as transformations of the remaining target",
        "tuple space.  It is the first coefficient-candidate step after the",
        "single, square, and cube deletion ledgers.",
        "",
        "For each deleted-generator row it groups source tuples by the tuple",
        "left after deleting the stationary strands.  If every group has one",
        "deleted-after-source value, the defect descends to a transformation",
        "of the target tuple space; if that transformation is bijective, it is",
        "a finite vertical coefficient candidate.",
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
                f"- row count: `{row['row_count']}`;",
                (
                    "- all defects well-defined on post-deletion target tuples: "
                    f"`{row['all_defects_well_defined']}`;"
                ),
                (
                    "- all defects are permutations: "
                    f"`{row['all_defects_are_permutations']}`;"
                ),
                f"- nontrivial defect count: `{row['nontrivial_defect_count']}`;",
                f"- order spectrum: `{tuple(row['order_spectrum'])}`;",
                (
                    "- verifies extraction: "
                    f"`{row['verifies_vertical_defect_transform_extraction']}`."
                ),
                "",
                "Level summaries:",
                "",
            ]
        )
        for level, summary in row["level_summaries"].items():
            lines.append(
                "- "
                f"deletion level `{level}`: rows `{summary['row_count']}`, "
                f"target tuple counts `{tuple(summary['target_tuple_counts'])}`, "
                f"orders `{tuple(summary['order_spectrum'])}`, "
                f"identity rows `{summary['identity_count']}`, "
                f"nontrivial rows `{summary['nontrivial_count']}`, "
                f"distinct defects `{summary['distinct_defect_count']}`."
            )
        lines.extend(["", "Defect rows:", ""])
        for defect_row in row["rows"]:
            lines.append(
                "- "
                f"level `{defect_row['deletion_level']}`, "
                f"forget `{tuple(defect_row['forget_stationary_indices'])}`, "
                f"source `alpha_{{{defect_row['source_generator_index']},"
                f"{defect_row['source_braid_index']}}}`: "
                f"well-defined `{defect_row['well_defined_on_deleted_tuple']}`, "
                f"permutation `{defect_row['defect_is_permutation']}`, "
                f"order `{defect_row['defect_order']}`, "
                f"identity `{defect_row['identity_defect']}`, "
                f"witness {_render_witness(defect_row)}."
            )
        lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "For the nondegenerate prefix witness, all `54` deleted-generator",
            "defects descend to permutations of the remaining tuple space and",
            "all have order `2`.  At each deletion level there is one distinct",
            "nontrivial defect permutation.  This turns the raw mismatch ledgers",
            "into a concrete finite coefficient candidate.",
            "",
            "For the degenerate identity row, all `54` defects are identity",
            "permutations.  Thus nonunit prefix memory alone does not produce",
            "vertical point-forgetting coefficients.",
            "",
            "This still does not compute a gauge-invariant Peiffer class.  It",
            "identifies the vertical groups on which such a class would live:",
            "a positive proof must show that these coefficient candidates and",
            "their face transports pull back from one fixed finite operator-label",
            "Artin envelope; a negative proof must find incompatible transported",
            "square boundaries.",
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
                    "nontrivial_defect_count": row["nontrivial_defect_count"],
                    "order_spectrum": row["order_spectrum"],
                    "level_summaries": row["level_summaries"],
                    "verifies": row[
                        "verifies_vertical_defect_transform_extraction"
                    ],
                }
                for row in report["rows"]
            ],
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
