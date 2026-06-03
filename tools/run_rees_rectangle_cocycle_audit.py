import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    cyclic_group,
    rees_rectangle_cocycle,
    rees_rectangle_cocycle_audit,
)


OUT_JSON = ROOT / "proofs" / "rees_rectangle_cocycle_audit.json"
OUT_MD = ROOT / "proofs" / "rees_rectangle_cocycle_audit.md"


def _audit_dict(name, audit, distinguished_omega=None):
    row = asdict(audit)
    row["case"] = name
    row["rectangle_cocycles_are_trivial"] = audit.rectangle_cocycles_are_trivial
    row["sandwich_is_row_column_coboundary"] = audit.sandwich_is_row_column_coboundary
    row["flatness_matches_coboundary"] = audit.flatness_matches_coboundary
    row["is_flat"] = audit.is_flat
    row["distinguished_omega"] = distinguished_omega
    return row


def _flat_c3_case():
    group = cyclic_group(3)
    rows = ("lambda0", "lambda1")
    columns = ("i0", "i1", "i2")
    row_factor = {"lambda0": 1, "lambda1": 2}
    column_factor = {"i0": 0, "i1": 2, "i2": 1}
    sandwich = {
        (row, column): group.mul(row_factor[row], column_factor[column])
        for row in rows
        for column in columns
    }
    return rees_rectangle_cocycle_audit(group, rows, columns, sandwich)


def _nonflat_c2_case():
    group = cyclic_group(2)
    rows = ("lambda0", "lambda1")
    columns = ("i0", "i1")
    sandwich = {
        ("lambda0", "i0"): 0,
        ("lambda0", "i1"): 0,
        ("lambda1", "i0"): 0,
        ("lambda1", "i1"): 1,
    }
    omega = rees_rectangle_cocycle(
        group,
        sandwich,
        "lambda0",
        "lambda1",
        "i0",
        "i1",
    )
    audit = rees_rectangle_cocycle_audit(group, rows, columns, sandwich)
    return audit, omega


def build_report():
    flat_audit = _flat_c3_case()
    nonflat_audit, nonflat_omega = _nonflat_c2_case()
    report = {
        "description": (
            "Finite Rees rectangle cocycle audit for the semigroup-corridor "
            "flatness pressure test."
        ),
        "rows": (
            _audit_dict("row_column_flat_C3_2x3", flat_audit),
            _audit_dict("nonflat_C2_2x2", nonflat_audit, nonflat_omega),
        ),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Rees rectangle cocycle audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the finite sandwich-matrix convention",
        "used by `proofs/rees_rectangle_cocycle_flatness_target.md`.",
        "For a Rees matrix component `M[G; I, Lambda; P]`, rows are",
        "`Lambda`, columns are `I`, and the rectangle cocycle is",
        "",
        "```text",
        "omega(lambda, mu; i, j)",
        "  = p[lambda,i] p[mu,i]^{-1} p[mu,j] p[lambda,j]^{-1}.",
        "```",
        "",
        "The base-gauge flatness check is the row-column factorization",
        "",
        "```text",
        "p[lambda,i]",
        "  = p[lambda,i0] p[lambda0,i0]^{-1} p[lambda0,i].",
        "```",
        "",
        "The audit is not a YBE realization claim.  It only fixes the exact",
        "finite obstruction that a YBE-specific flatness lemma must kill, or",
        "that an obstruction construction must realize inside actual local",
        "bijective YBE rows.",
        "",
        "## Rows",
        "",
    ]
    for row in report["rows"]:
        lines.extend(
            [
                f"### {row['case']}",
                "",
                f"- group order: `{row['group_order']}`;",
                f"- rows: `{row['row_count']}`; columns: `{row['column_count']}`;",
                f"- rectangle count: `{row['rectangle_count']}`;",
                f"- rectangle failure count: `{row['rectangle_failure_count']}`;",
                f"- coboundary failure count: `{row['coboundary_failure_count']}`;",
                (
                    "- rectangle cocycles are trivial: "
                    f"`{row['rectangle_cocycles_are_trivial']}`;"
                ),
                (
                    "- sandwich is row-column coboundary: "
                    f"`{row['sandwich_is_row_column_coboundary']}`;"
                ),
                f"- flatness matches coboundary: `{row['flatness_matches_coboundary']}`;",
                f"- is flat: `{row['is_flat']}`;",
            ]
        )
        if row["distinguished_omega"] is not None:
            lines.append(f"- distinguished `omega`: `{row['distinguished_omega']}`;")
        if row["recorded_rectangle_failures"]:
            failure = row["recorded_rectangle_failures"][0]
            lines.extend(
                [
                    "- first rectangle failure:",
                    (
                        "  `("
                        f"{failure['row_top']}, {failure['row_bottom']}; "
                        f"{failure['column_left']}, {failure['column_right']}"
                        f") -> {failure['omega']}`;"
                    ),
                ]
            )
        if row["recorded_coboundary_failures"]:
            failure = row["recorded_coboundary_failures"][0]
            lines.extend(
                [
                    "- first coboundary failure:",
                    (
                        "  `("
                        f"{failure['row']}, {failure['column']}"
                        f"): actual {failure['actual']}, expected {failure['expected']}`;"
                    ),
                ]
            )
        lines.append("")
    lines.extend(
        [
            "## Consequence",
            "",
            "The `C2` square is the smallest algebraic rectangle obstruction:",
            "three sandwich entries are the identity and the fourth is the",
            "nonidentity element.  A positive semigroup-corridor proof must",
            "show that actual Artin/YBE corridors never traverse such a",
            "nonflat Rees rectangle except as a coboundary.  A negative route",
            "must realize this exact square, or a larger analogue, in a finite",
            "bijective YBE local quotient-fibre interval.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(report["rows"][-1], sort_keys=True))


if __name__ == "__main__":
    main()
