import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_artin_envelope_cohomology_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_artin_envelope_cohomology_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_artin_envelope_cohomology_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["checked_arities"] = audit.checked_arities
    row["all_rows_untruncated"] = audit.all_rows_untruncated
    row["records_artin_envelope_cohomology_pressure"] = (
        audit.records_artin_envelope_cohomology_pressure
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
        ("degenerate_identity_cohomology_surface", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_artin_envelope_cohomology_audit(
                    solution,
                    max_subgroup_size=10000,
                ),
            )
        )
    report = {
        "description": (
            "Finite action-groupoid ledger for the missing "
            "operator-label Artin-envelope cohomology lemma."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Prefix Artin-envelope cohomology audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the first finite action-groupoid",
        "surface for the missing finite operator-label Artin-envelope lemma.",
        "It is a cohomology pressure ledger, not a computation of group",
        "cohomology.",
        "",
        "For each of `Q_X(3)` and `Q_X(4)` it records:",
        "",
        "- the point-pushing image size and exponent, when untruncated;",
        "- the number of orbits of the action on `X^{n+1}`;",
        "- the action-groupoid arrow count `|Q_X(n)| |X|^{n+1}`;",
        "- stabilizer-loop arrows, where vertical cocycles must be bounded;",
        "- generator-indexed vertical cocycle values;",
        "- the first point-forgetting naturality squares from `Q_X(4)` to",
        "  `Q_X(3)`.",
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
                    "- operator-label variable count: "
                    f"`{row['operator_label_variable_count']}`;"
                ),
                f"- checked arities: `{tuple(row['checked_arities'])}`;",
                f"- all rows untruncated: `{row['all_rows_untruncated']}`;",
                (
                    "- records cohomology pressure: "
                    f"`{row['records_artin_envelope_cohomology_pressure']}`."
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
                    f"- generator count: `{surface['generator_count']}`;",
                    (
                        "- point-pushing group size: "
                        f"`{surface['point_pushing_group_size']}`;"
                    ),
                    (
                        "- point-pushing group exponent: "
                        f"`{surface['point_pushing_group_exponent']}`;"
                    ),
                    f"- orbit count: `{surface['orbit_count']}`;",
                    f"- max orbit size: `{surface['max_orbit_size']}`;",
                    (
                        "- action-groupoid arrow count: "
                        f"`{surface['action_groupoid_arrow_count']}`;"
                    ),
                    (
                        "- stabilizer-loop arrow count: "
                        f"`{surface['stabilizer_loop_arrow_count']}`;"
                    ),
                    (
                        "- generator cocycle value count: "
                        f"`{surface['generator_cocycle_value_count']}`;"
                    ),
                    (
                        "- restriction to previous required: "
                        f"`{surface['restriction_to_previous_required']}`;"
                    ),
                    (
                        "- forgetting-naturality square count: "
                        f"`{surface['forgetting_naturality_square_count']}`;"
                    ),
                    f"- truncated: `{surface['truncated']}`.",
                    "",
                ]
            )
    lines.extend(
        [
            "## Meaning",
            "",
        "At a fixed arity, `K_n` is free, so the cohomology pressure is",
        "not a pure-braid presentation-relator issue.  The finite",
        "obligations are instead action-groupoid obligations: choose a",
        "fixed finite group-Hurwitz quotient, express the remaining",
        "motion as a vertical cocycle over its orbits and stabilizers,",
        "and make those cocycles compatible under point-forgetting.",
        "Equivalently, a positive proof needs a bounded",
        "Artin-equivariant transgression lemma: one finite operator-label",
        "groupoid, one finite coefficient system, and one bounded class",
        "whose pullbacks recover the residual point-pushing extension",
        "classes in every arity.",
        "",
        "The nondegenerate witness has two orbits at both checked",
            "arities and action-groupoid arrow counts `128` and `512`.",
            "The degenerate identity row has nonunit prefix memory but",
            "trivial point-pushing image, so every tuple is a singleton",
            "orbit and the only stabilizer loops are identity loops.",
            "",
            "A positive proof must show that this ledger is controlled by",
            "one finite operator-label model with uniformly bounded vertical",
            "exponent in every arity.  A negative proof must find a local",
            "interval or larger finite table where these orbit-stabilizer",
            "cocycle ledgers are incompatible with every fixed finite",
            "group-Hurwitz base.",
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
