import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import prefix_point_pushing_tiny_corpus_audit  # noqa: E402


OUT_JSON = ROOT / "proofs" / "prefix_point_pushing_tiny_corpus_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_point_pushing_tiny_corpus_audit.md"


def _audit_dict(size):
    audit = prefix_point_pushing_tiny_corpus_audit(size)
    row = asdict(audit)
    row["no_left_degenerate_nonunit_surface_candidates"] = (
        audit.no_left_degenerate_nonunit_surface_candidates
    )
    return row


def build_report():
    rows = [_audit_dict(size) for size in (2, 3)]
    report = {
        "description": (
            "Exhaustive whole-table size-2 and size-3 scan for "
            "left-degenerate nonunit-prefix solutions with nontrivial "
            "Q_X(3), Q_X(4) prefix point-pushing surface."
        ),
        "scope": (
            "finite whole-table corpus only; quotient-fibre intervals and "
            "larger tables are not scanned"
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def _render_tag_counts(tag_profile_counts):
    lines = []
    for tag_profile, count in tag_profile_counts:
        lines.append(f"- `{tag_profile}`: `{count}`")
    return lines


def _render_left_degenerate_rows(rows):
    lines = []
    for row in rows:
        tags = ", ".join(row["branch_tags"]) or "(untagged)"
        lines.append(
            "- "
            f"index `{row['solution_index']}`; tags `{tags}`; "
            f"nonunit prefixes `{row['nonunit_prefix_count']}`; "
            f"`|Q_X(3)|={row['qx3_group_size']}`; "
            f"`|Q_X(4)|={row['qx4_group_size']}`; "
            f"truncated `{row['surface_truncated']}`"
        )
    return lines or ["- none"]


def render_markdown(report):
    lines = [
        "# Prefix point-pushing tiny corpus audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit exhaustively scans all bijective YBE whole",
        "tables on two and three points.  It asks whether the first",
        "point-pushing pressure surface",
        "",
        "```text",
        "Q_X(3) <= G_X(4),       Q_X(4) <= G_X(5)",
        "```",
        "",
        "already contains a left-degenerate solution with nonunit prefix",
        "memory and nontrivial point-pushing image.",
        "",
        "The scan is deliberately finite.  It does not search four-point",
        "tables, quotient-fibre local intervals, or all possible finite",
        "group-Hurwitz compressions.",
        "",
        "## Corpus Rows",
        "",
    ]
    for row in report["rows"]:
        lines.extend(
            [
                f"### Size {row['size']}",
                "",
                f"- bijective YBE solution count: `{row['solution_count']}`;",
                f"- left-degenerate count: `{row['left_degenerate_count']}`;",
                (
                    "- left-degenerate with nonunit prefix count: "
                    f"`{row['left_degenerate_nonunit_count']}`;"
                ),
                (
                    "- left-degenerate nonunit rows with nontrivial surface: "
                    f"`{row['left_degenerate_nonunit_nontrivial_surface_count']}`;"
                ),
                (
                    "- any-row nontrivial surface count: "
                    f"`{row['nontrivial_surface_count']}`;"
                ),
                f"- truncated surface count: `{row['truncated_surface_count']}`;",
                (
                    "- no bad left-degenerate nonunit surface candidates: "
                    f"`{row['no_left_degenerate_nonunit_surface_candidates']}`."
                ),
                "",
                "Recorded left-degenerate nonunit rows:",
                "",
            ]
        )
        lines.extend(_render_left_degenerate_rows(row["recorded_left_degenerate_nonunit_rows"]))
        lines.extend(["", "Tag profile counts:", ""])
        lines.extend(_render_tag_counts(row["tag_profile_counts"]))
        lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            "The first bad surface is absent from the exhaustive whole-table",
            "corpus on two and three points.  In size `2`, the only",
            "left-degenerate nonunit-prefix table is the identity table, and",
            "its `Q_X(3)` and `Q_X(4)` images are trivial.  In size `3`, all",
            "seven left-degenerate nonunit-prefix rows again have trivial",
            "`Q_X(3)` and `Q_X(4)` images.",
            "",
            "Thus a negative point-pushing route cannot start with a whole",
            "size-2 or size-3 table.  A genuine obstruction must move to",
            "larger whole tables or to quotient-fibre local intervals, and",
            "must still show incompatibility with every fixed finite",
            "group-Hurwitz base plus bounded-exponent vertical kernel.",
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
                    "size": row["size"],
                    "solution_count": row["solution_count"],
                    "left_degenerate_nonunit_count": (
                        row["left_degenerate_nonunit_count"]
                    ),
                    "bad_candidate_count": (
                        row[
                            "left_degenerate_nonunit_nontrivial_surface_count"
                        ]
                    ),
                }
                for row in report["rows"]
            ],
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
