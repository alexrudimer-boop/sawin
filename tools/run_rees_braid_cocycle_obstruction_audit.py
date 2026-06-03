import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    cyclic_group,
    labeled_permutation_braid_audit,
    rees_rectangle_cocycle,
    rees_rectangle_cocycle_audit,
)


OUT_JSON = ROOT / "proofs" / "rees_braid_cocycle_obstruction_audit.json"
OUT_MD = ROOT / "proofs" / "rees_braid_cocycle_obstruction_audit.md"


def _pattern_data():
    group = cyclic_group(2)
    rows = ("lambda0", "lambda1")
    columns = ("i0", "i1")
    sandwich = {
        ("lambda0", "i0"): 0,
        ("lambda0", "i1"): 0,
        ("lambda1", "i0"): 0,
        ("lambda1", "i1"): 1,
    }
    states = ("q00", "q01", "q10", "q11")
    row1 = {
        "q00": "q10",
        "q01": "q11",
        "q10": "q01",
        "q11": "q00",
    }
    row2 = {
        "q00": "q01",
        "q01": "q10",
        "q10": "q11",
        "q11": "q00",
    }
    labels1 = {"q00": 0, "q01": 0, "q10": 0, "q11": 1}
    labels2 = {"q00": 0, "q01": 0, "q10": 1, "q11": 0}
    return group, rows, columns, sandwich, states, row1, labels1, row2, labels2


def build_report():
    (
        group,
        rows,
        columns,
        sandwich,
        states,
        row1,
        labels1,
        row2,
        labels2,
    ) = _pattern_data()
    omega = rees_rectangle_cocycle(
        group, sandwich, "lambda0", "lambda1", "i0", "i1"
    )
    rectangle_audit = rees_rectangle_cocycle_audit(group, rows, columns, sandwich)
    braid_audit = labeled_permutation_braid_audit(
        group,
        states,
        row1,
        labels1,
        row2,
        labels2,
    )
    report = {
        "description": (
            "Small C2 Rees braid-cocycle obstruction pattern: nonflat "
            "sandwich rectangle plus YBE-compatible labeled quotient rows."
        ),
        "group": "C2_additive_0_identity_1_nonidentity",
        "states": states,
        "row1": row1,
        "row1_labels": labels1,
        "row2": row2,
        "row2_labels": labels2,
        "distinguished_rectangle_omega": omega,
        "rectangle_audit": {
            **asdict(rectangle_audit),
            "is_flat": rectangle_audit.is_flat,
            "rectangle_cocycles_are_trivial": (
                rectangle_audit.rectangle_cocycles_are_trivial
            ),
            "sandwich_is_row_column_coboundary": (
                rectangle_audit.sandwich_is_row_column_coboundary
            ),
        },
        "braid_audit": {
            **asdict(braid_audit),
            "beta_has_constant_label": braid_audit.beta_has_constant_label,
            "beta_constant_label": braid_audit.beta_constant_label,
            "beta_constant_label_is_nontrivial": (
                braid_audit.beta_constant_label_is_nontrivial
            ),
            "verifies_closed_nontrivial_braid_holonomy": (
                braid_audit.verifies_closed_nontrivial_braid_holonomy
            ),
        },
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    return report


def render_markdown(report):
    rectangle = report["rectangle_audit"]
    braid = report["braid_audit"]
    lines = [
        "# Rees braid-cocycle obstruction audit",
        "",
        "Date: 2026-06-03",
        "",
        "This generated audit records the smallest finite pattern currently",
        "suggested by the Rees-flatness pressure test.  It is not claimed to",
        "be an actual finite bijective YBE solution.  It is a finite local",
        "quotient-row pattern that satisfies the braid relation while keeping",
        "a nontrivial Rees rectangle cocycle.",
        "",
        "The group is `C2`, written additively as `0` for the identity and",
        "`1` for the nonidentity element.",
        "",
        "## Rees Rectangle",
        "",
        "The sandwich matrix is",
        "",
        "```text",
        "          i0  i1",
        "lambda0   0   0",
        "lambda1   0   1",
        "```",
        "",
        f"- distinguished rectangle omega: `{report['distinguished_rectangle_omega']}`;",
        f"- rectangle failure count: `{rectangle['rectangle_failure_count']}`;",
        f"- coboundary failure count: `{rectangle['coboundary_failure_count']}`;",
        f"- rectangle cocycles are trivial: `{rectangle['rectangle_cocycles_are_trivial']}`;",
        f"- sandwich is row-column coboundary: `{rectangle['sandwich_is_row_column_coboundary']}`;",
        f"- is flat: `{rectangle['is_flat']}`.",
        "",
        "## Labeled Braid Rows",
        "",
        "States are `q00, q01, q10, q11`.  The two quotient rows are",
        "",
        "```text",
        "q        q00  q01  q10  q11",
        "s1(q)    q10  q11  q01  q00",
        "ell1(q)  0    0    0    1",
        "s2(q)    q01  q10  q11  q00",
        "ell2(q)  0    0    1    0",
        "```",
        "",
        "A row `(s, ell)` acts on `Omega x C2` by",
        "",
        "```text",
        "(q,g) |-> (s(q), g + ell(q)).",
        "```",
        "",
        f"- quotient braid relation holds: `{braid['quotient_braid_relation_holds']}`;",
        f"- labeled braid relation holds: `{braid['braid_relation_holds']}`;",
        f"- beta word: `{tuple(braid['beta_word'])}`;",
        f"- beta is quotient-closed: `{braid['beta_is_quotient_closed']}`;",
        f"- beta distinct labels: `{tuple(braid['beta_distinct_labels'])}`;",
        f"- beta constant label: `{braid['beta_constant_label']}`;",
        (
            "- verifies closed nontrivial braid holonomy: "
            f"`{braid['verifies_closed_nontrivial_braid_holonomy']}`."
        ),
        "",
        "The beta state images are:",
        "",
        "```text",
    ]
    for source, target, label in braid["beta_state_images"]:
        lines.append(f"{source} -> ({target}, {label})")
    lines.extend(
        [
            "```",
            "",
            "## Consequence",
            "",
            "The local braid/YBE relation only checks a braid cocycle identity",
            "for the labels.  This audit shows that such an identity can hold",
            "while the Rees rectangle cocycle is still nontrivial.  Therefore",
            "a positive finite-rack-domination route needs an additional",
            "realization or flatness lemma: actual finite bijective YBE local",
            "quotient-fibre intervals must either avoid this pattern or force",
            "it into a bounded vertical coboundary.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(report["braid_audit"], sort_keys=True))


if __name__ == "__main__":
    main()
