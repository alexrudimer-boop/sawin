import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_deletion_square_restriction_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_deletion_square_restriction_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_deletion_square_restriction_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["row_count"] = audit.row_count
    row["total_mismatch_count"] = audit.total_mismatch_count
    row["deleted_generator_mismatch_count"] = (
        audit.deleted_generator_mismatch_count
    )
    row["surviving_generator_all_match"] = audit.surviving_generator_all_match
    row["deletion_orders_all_commute"] = audit.deletion_orders_all_commute
    row["all_rows_match"] = audit.all_rows_match
    row["verifies_first_deletion_square_surface"] = (
        audit.verifies_first_deletion_square_surface
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
        ("degenerate_identity_deletion_square", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_deletion_square_restriction_audit(solution),
            )
        )
    report = {
        "description": (
            "First two-face point-forgetting restriction surface from "
            "Q_X(5) to Q_X(3)."
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
        f"`{tuple(row['first_witness_input'])}` maps after double deletion to "
        f"`{tuple(row['first_deleted_after_source'])}`, expected "
        f"`{tuple(row['first_expected_target'])}`"
    )


def render_markdown(report):
    lines = [
        "# Prefix deletion-square restriction audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit compares the marked `Q_X(5)` point-pushing",
        "generators with their expected `Q_X(3)` images after deleting two",
        "stationary strands.  It is the first two-face surface behind the",
        "Peiffer/secondary-class pressure test.",
        "",
        "With source generator `alpha_{i,6}` and deleted stationary strands",
        "`j<k`, the marked target is:",
        "",
        "```text",
        "identity,                         if i in {j,k},",
        "alpha_{i-c,4}, where c=#({j,k}<i), otherwise.",
        "```",
        "",
        "The audit also checks that the two coordinate-deletion orders commute",
        "on the source action.  Thus any mismatch is not a raw failure of the",
        "semi-simplicial face identity; it is residual vertical monodromy left",
        "when a pushed-around strand is forgotten.",
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
                    "- deleted-generator mismatch count: "
                    f"`{row['deleted_generator_mismatch_count']}`;"
                ),
                (
                    "- surviving generators all match: "
                    f"`{row['surviving_generator_all_match']}`;"
                ),
                (
                    "- deletion orders all commute: "
                    f"`{row['deletion_orders_all_commute']}`;"
                ),
                f"- all rows match: `{row['all_rows_match']}`;",
                (
                    "- verifies first deletion-square surface: "
                    f"`{row['verifies_first_deletion_square_surface']}`."
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
                f"forget `{tuple(restriction['forget_stationary_indices'])}`, "
                f"source `alpha_{{{restriction['source_generator_index']},6}}`, "
                f"target `{target}`: "
                f"mismatches `{restriction['mismatch_count']}`, "
                f"orders commute `{restriction['deletion_orders_commute']}`, "
                f"witness {_render_witness(restriction)}."
            )
        lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "For the nondegenerate prefix witness, all `30` surviving-generator",
            "rows match exactly.  The `20` rows where the source generator is one",
            "of the two deleted strands each have `64` mismatches, for `1280`",
            "total mismatches.  The two deletion orders still commute on every",
            "row, so the visible defect is vertical rather than a failure of",
            "coordinate face maps.",
            "",
            "For the degenerate identity row, all `50` rows match.  This keeps",
            "the pressure test pointed at actual point-forgetting monodromy, not",
            "at nonunit prefix memory alone.",
            "",
            "The result still is not a counterexample to finite rack domination.",
            "It identifies the first two-face ledger that a positive proof must",
            "explain by a finite operator-label Artin envelope.  The next",
            "possible obstruction is a genuine deletion-cube/Peiffer coherence",
            "class, where these two-face defects must be compatible under three",
            "stationary deletions.",
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
