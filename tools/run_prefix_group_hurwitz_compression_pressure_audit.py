import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    prefix_group_hurwitz_compression_pressure_audit,
)


OUT_JSON = ROOT / "proofs" / "prefix_group_hurwitz_compression_pressure_audit.json"
OUT_MD = ROOT / "proofs" / "prefix_group_hurwitz_compression_pressure_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {repr(key): value for key, value in solution.R.items()}
    row["records_group_hurwitz_compression_pressure"] = (
        audit.records_group_hurwitz_compression_pressure
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
        ("degenerate_identity_nonunit_prefix", degenerate_identity),
    ):
        rows.append(
            _audit_dict(
                name,
                solution,
                prefix_group_hurwitz_compression_pressure_audit(solution),
            )
        )
    report = {
        "description": (
            "Finite equation ledger for compressing prefix-edge memory to "
            "a fixed group-Hurwitz tower."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Prefix group-Hurwitz compression pressure audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the finite equation family that a",
        "group-Hurwitz compression of the prefix-edge transducer must solve.",
        "A compression would assign each prefix edge `(P,x,P lambda_x)` a",
        "label in one finite group, with conjugation-stable image, so that",
        "local prefix-edge braid moves descend to ordinary Hurwitz moves.",
        "",
        "The audit does not search all finite groups.  It records the",
        "local Hurwitz-label equations, the corresponding total-product",
        "invariance equations, the point-forgetting rescan lumpability",
        "equations, and whether the left-prefix monoid contains nonunits.",
        "Nonunit prefixes cannot be faithfully embedded as a transformation",
        "monoid inside a group, so a true group-Hurwitz model must quotient",
        "or encode that memory with extra bounded vertical noise.",
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
                f"- edge state count: `{row['edge_state_count']}`;",
                f"- nonunit prefix count: `{row['nonunit_prefix_count']}`;",
                (
                    "- faithful prefix-monoid group embedding obstructed: "
                    f"`{row['faithful_prefix_monoid_group_embedding_obstructed']}`;"
                ),
                (
                    "- local Hurwitz-label equation count: "
                    f"`{row['local_hurwitz_label_equation_count']}`;"
                ),
                (
                    "- product-invariance equation count: "
                    f"`{row['product_invariance_equation_count']}`;"
                ),
                (
                    "- forgetting-rescan lumpability equation count: "
                    f"`{row['forgetting_rescan_lumpability_equation_count']}`;"
                ),
                (
                    "- first obstruction arities: "
                    f"`{tuple(row['first_obstruction_arities'])}`;"
                ),
                (
                    "- records group-Hurwitz compression pressure: "
                    f"`{row['records_group_hurwitz_compression_pressure']}`."
                ),
                "",
            ]
        )
    lines.extend(
        [
            "## Meaning",
            "",
            "The prefix-edge transducer is finite, but a finite transducer",
            "tower is weaker than a finite group-Hurwitz tower.  The next",
            "positive route must produce a fixed finite group label model",
            "satisfying these local equations and compatible with rescanning",
            "under point-forgetting.  The next negative route must find a",
            "finite degenerate solution where every such label model leaves",
            "vertical behaviour in `Q_X(3), Q_X(4), ...` that cannot be",
            "bounded by one fixed exponent.",
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
