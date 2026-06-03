import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_point_forgetting_restriction_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_point_forgetting_restriction_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_point_forgetting_restriction_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["row_count"] = audit.row_count
    row["total_mismatch_count"] = audit.total_mismatch_count
    row["diagonal_mismatch_count"] = audit.diagonal_mismatch_count
    row["off_diagonal_all_match"] = audit.off_diagonal_all_match
    row["all_rows_match"] = audit.all_rows_match
    row["verifies_first_point_forgetting_restriction_surface"] = (
        audit.verifies_first_point_forgetting_restriction_surface
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
        ("degenerate_identity_restriction_surface", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_point_forgetting_restriction_audit(solution),
            )
        )
    report = {
        "description": (
            "First marked point-forgetting restriction surface from "
            "Q_X(4) to Q_X(3)."
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
        f"`{tuple(row['first_witness_input'])}` maps after deletion to "
        f"`{tuple(row['first_deleted_after_source'])}`, expected "
        f"`{tuple(row['first_expected_target'])}`"
    )


def render_markdown(report):
    lines = [
        "# Prefix point-forgetting restriction audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit compares the marked `Q_X(4)` point-pushing",
        "generators with their expected `Q_X(3)` images after deleting one",
        "stationary strand.  With the standard generators",
        "`alpha_{i,5}`, deleting stationary strand `j` should send the",
        "marked generator to:",
        "",
        "```text",
        "identity,             if i=j,",
        "alpha_{i,4},          if i<j,",
        "alpha_{i-1,4},        if i>j.",
        "```",
        "",
        "When the tuple action does not match that expected marked action,",
        "the difference is exactly the first visible vertical cocycle data",
        "that a finite Artin-envelope tower must absorb.",
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
                (
                    "- source and target arities: "
                    f"`Q_X({row['source_point_pushing_arity']}) -> "
                    f"Q_X({row['target_point_pushing_arity']})`;"
                ),
                f"- row count: `{row['row_count']}`;",
                f"- total mismatch count: `{row['total_mismatch_count']}`;",
                (
                    "- diagonal mismatch count: "
                    f"`{row['diagonal_mismatch_count']}`;"
                ),
                f"- off-diagonal all match: `{row['off_diagonal_all_match']}`;",
                f"- all rows match: `{row['all_rows_match']}`;",
                (
                    "- verifies first restriction surface: "
                    f"`{row['verifies_first_point_forgetting_restriction_surface']}`."
                ),
                "",
                "Restriction rows:",
                "",
            ]
        )
        for restriction in row["rows"]:
            target = (
                "identity"
                if restriction["target_generator_index"] is None
                else f"alpha_{{{restriction['target_generator_index']},4}}"
            )
            lines.append(
                "- "
                f"forget `{restriction['forget_stationary_index']}`, "
                f"source `alpha_{{{restriction['source_generator_index']},5}}`, "
                f"target `{target}`: "
                f"mismatches `{restriction['mismatch_count']}`, "
                f"witness {_render_witness(restriction)}."
            )
        lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "The nondegenerate witness has perfect off-diagonal restriction",
            "compatibility, but the four diagonal rows each have `32`",
            "mismatches.  This is the first concrete vertical point-forgetting",
            "cocycle: after deleting the stationary strand that was looped",
            "around, the abstract point-pushing generator forgets to the",
            "identity, but the tuple labels retain monodromy.",
            "",
            "The degenerate identity row has no mismatch, even though its",
            "left-prefix monoid has nonunit memory.  Thus the restriction",
            "surface separates two issues: nonunit prefix memory and actual",
            "vertical point-forgetting monodromy.",
            "",
            "A positive finite-rack-domination proof must show that these",
            "diagonal vertical rows are controlled by one fixed finite",
            "operator-label base with bounded vertical exponent.  A negative",
            "proof must find a local interval or larger table where the same",
            "restriction cocycles cannot be made compatible through the tower.",
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
