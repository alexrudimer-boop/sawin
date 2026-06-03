import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_point_pushing_surface_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_point_pushing_surface_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_point_pushing_surface_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["checked_arities"] = audit.checked_arities
    row["all_rows_untruncated"] = audit.all_rows_untruncated
    row["verifies_prefix_point_pushing_surface"] = (
        audit.verifies_prefix_point_pushing_surface
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
        ("degenerate_identity_prefix_surface", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_point_pushing_surface_audit(
                    solution,
                    max_subgroup_size=10000,
                ),
            )
        )
    report = {
        "description": (
            "Concrete Q_X(3), Q_X(4) prefix-transducer point-pushing surface."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Prefix point-pushing surface audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit computes the first concrete point-pushing",
        "surfaces `Q_X(3)` and `Q_X(4)` for the prefix-edge transducer",
        "route.  It uses the standard pure generators",
        "`alpha_{i,n+1}=A_{i,n+1}` and checks that the prefix-path encoding",
        "sees the same marked action as the original tuple action.",
        "",
        "The audit is still finite-prefix evidence.  It is not a proof that",
        "every arity admits a fixed group-Hurwitz compression, and it is not",
        "a normalized-law counterexample.  It records the first concrete",
        "surface where such a compression has to be tested.",
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
                f"- checked arities: `{tuple(row['checked_arities'])}`;",
                f"- all rows untruncated: `{row['all_rows_untruncated']}`;",
                (
                    "- verifies prefix point-pushing surface: "
                    f"`{row['verifies_prefix_point_pushing_surface']}`."
                ),
                "",
            ]
        )
        for surface in row["rows"]:
            lines.extend(
                [
                    (
                        f"#### Q_X({surface['point_pushing_arity']}) "
                        f"in B_{surface['braid_index']}"
                    ),
                    "",
                    f"- tuple count: `{surface['tuple_count']}`;",
                    f"- prefix path count: `{surface['prefix_path_count']}`;",
                    (
                        "- prefix encoding injective: "
                        f"`{surface['prefix_encoding_injective']}`;"
                    ),
                    f"- generator count: `{surface['generator_count']}`;",
                    (
                        "- generator braid words: "
                        f"`{tuple(tuple(word) for word in surface['generator_braid_words'])}`;"
                    ),
                    f"- generator orders: `{tuple(surface['generator_orders'])}`;",
                    (
                        "- point-pushing group size: "
                        f"`{surface['point_pushing_group_size']}`;"
                    ),
                    (
                        "- point-pushing group exponent: "
                        f"`{surface['point_pushing_group_exponent']}`;"
                    ),
                    (
                        "- prefix action matches tuple action: "
                        f"`{surface['prefix_action_matches_tuple_action']}`;"
                    ),
                    f"- truncated: `{surface['truncated']}`.",
                    "",
                ]
            )
    lines.extend(
        [
            "## Meaning",
            "",
            "The rows make the `Q_X(3), Q_X(4)` pressure surface explicit.",
            "For the nondegenerate two-point witness, the point-pushing",
            "groups have sizes `8` and `16` with exponent `2`; for the",
            "degenerate identity row, the point-pushing groups are trivial",
            "even though the left-prefix monoid contains nonunit memory.",
            "A genuine obstruction must therefore use a less trivial",
            "degenerate table and show that every fixed group-Hurwitz",
            "compression leaves incompatible or unbounded vertical data",
            "on this surface and throughout the tower.",
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
