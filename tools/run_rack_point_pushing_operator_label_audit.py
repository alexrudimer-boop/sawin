import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    rack_point_pushing_operator_label_audit,
    rack_solution,
)


OUT_JSON = ROOT / "proofs" / "rack_point_pushing_operator_label_audit.json"
OUT_MD = ROOT / "proofs" / "rack_point_pushing_operator_label_audit.md"


def _audit_dict(name, audit):
    row = asdict(audit)
    row["rack_name"] = name
    row["verifies_rack_operator_label_extension"] = (
        audit.verifies_rack_operator_label_extension
    )
    return row


def build_report():
    racks = {
        "trivial_rack_2": rack_solution([0, 1], lambda _left, right: right),
        "dihedral_rack_3": rack_solution(
            [0, 1, 2],
            lambda left, right: (2 * left - right) % 3,
        ),
    }
    rows = []
    for name, rack in racks.items():
        for arity in (1, 2, 3):
            audit = rack_point_pushing_operator_label_audit(
                rack,
                arity,
                max_size=5000,
            )
            rows.append(_audit_dict(name, audit))
    report = {
        "description": (
            "Finite rack point-pushing operator-label quotient and bounded "
            "vertical-kernel audit."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Rack point-pushing operator-label audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit checks finite rows of the rack-only",
        "point-pushing structure recorded in",
        "`proofs/rack_point_pushing_operator_label_invariant.md`.",
        "For a rack `Y`, the point-pushing image is compared with its",
        "operator-label quotient on tuples `(L_y)` and with the vertical",
        "kernel acting trivially on those labels.",
        "",
        "The audit is finite-prefix evidence only.  The theorem-level",
        "statement is the symbolic rack operator-label extension; this",
        "report only locks down conventions and warning examples.",
        "",
        "## Rows",
        "",
    ]
    for row in report["rows"]:
        lines.extend(
            [
                f"### {row['rack_name']} arity {row['arity']}",
                "",
                f"- braid index: `{row['braid_index']}`;",
                f"- tuple count: `{row['tuple_count']}`;",
                f"- operator-label tuple count: `{row['operator_label_tuple_count']}`;",
                f"- `|Inn(Y)|`: `{row['inner_group_order']}`;",
                f"- `exp Inn(Y)`: `{row['inner_group_exponent']}`;",
                f"- point-pushing image order: `{row['point_pushing_group_order']}`;",
                (
                    "- point-pushing image exponent: "
                    f"`{row['point_pushing_group_exponent']}`;"
                ),
                f"- Hurwitz quotient order: `{row['hurwitz_quotient_order']}`;",
                f"- vertical kernel size: `{row['vertical_kernel_size']}`;",
                f"- vertical kernel exponent: `{row['vertical_kernel_exponent']}`;",
                (
                    "- vertical exponent divides `exp Inn(Y)`: "
                    f"`{row['vertical_exponent_divides_inner_exponent']}`;"
                ),
                (
                    "- verifies checked operator-label extension: "
                    f"`{row['verifies_rack_operator_label_extension']}`."
                ),
                "",
            ]
        )
    lines.extend(
        [
            "## Consequence",
            "",
            "The dihedral rack rows show why the whole-image exponent is the",
            "wrong invariant: at arity `3`, `exp Inn(Y)=6` but the",
            "point-pushing image exponent is `36`.  The checked rack invariant",
            "is instead the extension by a vertical kernel whose exponent",
            "divides `exp Inn(Y)`.",
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
