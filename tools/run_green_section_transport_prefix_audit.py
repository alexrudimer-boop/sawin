import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    all_bijection_solutions,
    bounded_atom_trivial_loop_group_summaries,
    bounded_category_summary,
    branch_tags,
    green_branch_audits,
    is_involutive_solution,
    solution_table_signature,
)


OUT_JSON = ROOT / "proofs" / "green_section_transport_prefix_audit.json"
OUT_MD = ROOT / "proofs" / "green_section_transport_prefix_audit.md"


def scan_size(size, *, depth=2, morphism_limit=10000):
    ybe_count = 0
    green_audit_count = 0
    hidden_atom_trivial_loop_solution_count = 0
    hidden_bijective_loop_solution_count = 0
    nonidentity_group_loop_solution_count = 0
    nonidentity_group_loop_involutive_solution_count = 0
    nonidentity_group_loop_known_branch_solution_count = 0
    unresolved_nonidentity_group_loop_solution_count = 0
    first_nonidentity_group_loop_examples = []

    for solution in all_bijection_solutions(size):
        ybe_count += 1
        audits = green_branch_audits(solution)
        green_audit_count += len(audits)
        category_summaries = [
            bounded_category_summary(
                audit,
                depth,
                morphism_limit=morphism_limit,
            )
            for audit in audits
        ]
        loop_groups = [
            summary
            for audit in audits
            for summary in bounded_atom_trivial_loop_group_summaries(
                audit,
                depth,
                morphism_limit=morphism_limit,
            )
        ]

        if any(summary.hidden_atom_trivial_loop_count for summary in category_summaries):
            hidden_atom_trivial_loop_solution_count += 1
        if any(summary.hidden_bijective_loop_count for summary in category_summaries):
            hidden_bijective_loop_solution_count += 1

        nonidentity_groups = [
            summary
            for summary in loop_groups
            if summary.nonidentity_loop_count or summary.group_order > 1
        ]
        if not nonidentity_groups:
            continue

        tags = branch_tags(solution)
        nonidentity_group_loop_solution_count += 1
        if is_involutive_solution(solution):
            nonidentity_group_loop_involutive_solution_count += 1
        if tags:
            nonidentity_group_loop_known_branch_solution_count += 1
        else:
            unresolved_nonidentity_group_loop_solution_count += 1
        if len(first_nonidentity_group_loop_examples) < 5:
            first_nonidentity_group_loop_examples.append(
                {
                    "branch_tags": list(tags),
                    "is_involutive_solution": is_involutive_solution(solution),
                    "table_values": [
                        list(value) for value in solution_table_signature(solution)
                    ],
                    "nonidentity_loop_groups": [
                        {
                            "group_order": summary.group_order,
                            "nonidentity_loop_count": summary.nonidentity_loop_count,
                            "word_count": summary.word_count,
                        }
                        for summary in nonidentity_groups
                    ],
                }
            )

    return {
        "size": size,
        "depth": depth,
        "morphism_limit": morphism_limit,
        "ybe_count": ybe_count,
        "green_audit_count": green_audit_count,
        "hidden_atom_trivial_loop_solution_count": (
            hidden_atom_trivial_loop_solution_count
        ),
        "hidden_bijective_loop_solution_count": hidden_bijective_loop_solution_count,
        "nonidentity_group_loop_solution_count": nonidentity_group_loop_solution_count,
        "nonidentity_group_loop_involutive_solution_count": (
            nonidentity_group_loop_involutive_solution_count
        ),
        "nonidentity_group_loop_known_branch_solution_count": (
            nonidentity_group_loop_known_branch_solution_count
        ),
        "unresolved_nonidentity_group_loop_solution_count": (
            unresolved_nonidentity_group_loop_solution_count
        ),
        "first_nonidentity_group_loop_examples": (
            first_nonidentity_group_loop_examples
        ),
    }


def build_report():
    scans = {
        "size_2_depth_2": scan_size(2, depth=2),
        "size_3_depth_2": scan_size(3, depth=2),
    }
    report = {
        "date": "2026-06-03",
        "scans": scans,
        "all_nonidentity_group_loops_known_through_prefix": all(
            scan["unresolved_nonidentity_group_loop_solution_count"] == 0
            for scan in scans.values()
        ),
        "meaning": (
            "Through size 3 at depth 2, every actual group-like atom-trivial "
            "completed-context loop is routed to an existing known branch; "
            "reset-like atom-trivial loops are not counted as residual motion."
        ),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Green section transport prefix audit",
        "",
        f"Date: {report['date']}",
        "",
        "This generated audit is a finite-prefix check for the actual",
        "Green-section transport rigidity gate.  It scans all finite",
        "bijective YBE solutions of sizes `2` and `3`, keeps only the",
        "actual deterministic completed-context category generated by",
        "supported rows, and counts group-like atom-trivial loops through",
        "depth `2`.",
        "",
        "Reset-like atom-trivial context collapses are not counted as",
        "residual motion: residual braid actions are permutations.  The live",
        "finite-prefix target is a nonidentity total bijective atom-trivial",
        "loop outside all already known branch tags.",
        "",
        "## Summary",
        "",
        (
            "- all nonidentity group-like loops known through prefix: "
            f"`{report['all_nonidentity_group_loops_known_through_prefix']}`."
        ),
        "",
        "## Scans",
        "",
    ]
    for name, scan in report["scans"].items():
        lines.extend(
            [
                f"### {name}",
                "",
                f"- YBE solutions: `{scan['ybe_count']}`;",
                f"- Green R-class audits: `{scan['green_audit_count']}`;",
                (
                    "- hidden atom-trivial loop solutions: "
                    f"`{scan['hidden_atom_trivial_loop_solution_count']}`;"
                ),
                (
                    "- hidden bijective loop solutions: "
                    f"`{scan['hidden_bijective_loop_solution_count']}`;"
                ),
                (
                    "- nonidentity group-like loop solutions: "
                    f"`{scan['nonidentity_group_loop_solution_count']}`;"
                ),
                (
                    "- involutive nonidentity group-loop solutions: "
                    f"`{scan['nonidentity_group_loop_involutive_solution_count']}`;"
                ),
                (
                    "- known-branch nonidentity group-loop solutions: "
                    f"`{scan['nonidentity_group_loop_known_branch_solution_count']}`;"
                ),
                (
                    "- unresolved nonidentity group-loop solutions: "
                    f"`{scan['unresolved_nonidentity_group_loop_solution_count']}`."
                ),
                "",
            ]
        )
        if scan["first_nonidentity_group_loop_examples"]:
            lines.extend(["First examples:", ""])
            for example in scan["first_nonidentity_group_loop_examples"]:
                lines.extend(
                    [
                        f"- branch tags: `{example['branch_tags']}`;",
                        (
                            "  loop groups: "
                            f"`{example['nonidentity_loop_groups']}`;"
                        ),
                        f"  table: `{example['table_values']}`.",
                    ]
                )
            lines.append("")
    lines.extend(
        [
            "## Meaning",
            "",
            report["meaning"],
            "",
            "This is finite-prefix evidence only.  It does not prove the",
            "all-depth Green-section rigidity lemma, but it filters candidate",
            "counterexamples: a genuine B-route example must produce an",
            "actual group-like atom-trivial loop that is not already explained",
            "by an involutive or other known finite-G branch.",
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
                "all_known": report[
                    "all_nonidentity_group_loops_known_through_prefix"
                ],
                "size_2_unresolved": report["scans"]["size_2_depth_2"][
                    "unresolved_nonidentity_group_loop_solution_count"
                ],
                "size_3_unresolved": report["scans"]["size_3_depth_2"][
                    "unresolved_nonidentity_group_loop_solution_count"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
