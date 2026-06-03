import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    edge_memory_tower_audit,
)


OUT_JSON = ROOT / "proofs" / "edge_memory_tower_audit.json"
OUT_MD = ROOT / "proofs" / "edge_memory_tower_audit.md"


def _audit_dict(name, solution, audit):
    row = asdict(audit)
    row["name"] = name
    row["table"] = {
        repr(key): value
        for key, value in solution.R.items()
    }
    row["all_generator_updates_well_defined"] = (
        audit.all_generator_updates_well_defined
    )
    row["all_point_forgetting_maps_well_defined"] = (
        audit.all_point_forgetting_maps_well_defined
    )
    row["verifies_edge_memory_triple_quadruple_prefix"] = (
        audit.verifies_edge_memory_triple_quadruple_prefix
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
        ("degenerate_identity_edge_memory", degenerate_identity),
    ):
        rows.append(_audit_dict(name, solution, edge_memory_tower_audit(solution)))
    report = {
        "description": (
            "Finite triple/quadruple prefix audit for adjacent edge memory."
        ),
        "rows": rows,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    lines = [
        "# Edge memory tower audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit checks the first tower gates for the finite",
        "adjacent edge-memory object.  The edge label of a pair `(x,y)` is",
        "`(lambda_x(y),x,y)`.  Adjacent edge labels encode tuples",
        "injectively, so braid-generator updates and point-forgetting maps",
        "are finite maps on the edge-memory state space.  This audit checks",
        "the braid triple and arity-four forgetting prefixes; it does not",
        "yet prove the bounded vertical-kernel part of the augmented",
        "Artin-envelope lemma.",
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
                f"- edge label count: `{row['edge_label_count']}`;",
                f"- arity-3 tuple count: `{row['arity3_tuple_count']}`;",
                f"- arity-4 tuple count: `{row['arity4_tuple_count']}`;",
                f"- arity-3 encoding injective: `{row['arity3_encoding_injective']}`;",
                f"- arity-4 encoding injective: `{row['arity4_encoding_injective']}`;",
                (
                    "- braid relation on edge memory: "
                    f"`{row['braid_relation_on_edge_memory']}`;"
                ),
                (
                    "- generator updates well-defined: "
                    f"`{tuple(tuple(item) for item in row['generator_updates_well_defined'])}`;"
                ),
                (
                    "- point-forgetting maps well-defined: "
                    f"`{tuple(tuple(item) for item in row['point_forgetting_well_defined'])}`;"
                ),
                (
                    "- verifies edge-memory triple/quadruple prefix: "
                    f"`{row['verifies_edge_memory_triple_quadruple_prefix']}`."
                ),
                "",
            ]
        )
    lines.extend(
        [
            "## Meaning",
            "",
            "The finite edge-memory object survives the first local tower",
            "checks in these rows.  What remains open is whether its",
            "point-pushing vertical kernel is uniformly bounded-exponent",
            "over a fixed finite group-Hurwitz base, or whether a genuine",
            "degenerate candidate can force unbounded vertical memory.",
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
