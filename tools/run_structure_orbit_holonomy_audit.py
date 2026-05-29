import json
import sys
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    identity_solution,
    rack_solution,
    structure_orbit_factorization_summary,
    structure_orbit_holonomy_summary,
)


OUT_JSON = ROOT / "proofs" / "structure_orbit_holonomy_audit.json"
OUT_MD = ROOT / "proofs" / "structure_orbit_holonomy_audit.md"


def size3_commutator_candidate():
    pairs = list(product(range(3), repeat=2))
    signature = [
        (0, 0),
        (1, 0),
        (2, 0),
        (2, 2),
        (0, 2),
        (1, 2),
        (1, 1),
        (2, 1),
        (0, 1),
    ]
    return FiniteBraidedSet(tuple(range(3)), dict(zip(pairs, signature)))


def summary_payload(solution, n, max_group_size):
    summary = structure_orbit_holonomy_summary(
        solution,
        n,
        max_group_size=max_group_size,
    )
    factorization = structure_orbit_factorization_summary(
        solution,
        n,
        max_group_size=max_group_size,
    )
    rows = tuple(
        sorted(
            (
                {
                    "orbit_size": orbit_size,
                    "group_size": group_size,
                    "group_exponent": group_exponent,
                    "projection_image_size": projection_image_size,
                }
                for (
                    orbit_size,
                    group_size,
                    group_exponent,
                    projection_image_size,
                ) in zip(
                    summary.orbit_sizes,
                    summary.orbit_group_sizes,
                    summary.orbit_group_exponents,
                    factorization.projection_image_sizes,
                )
            ),
            key=lambda row: (
                row["orbit_size"],
                -1 if row["group_size"] is None else row["group_size"],
                -1 if row["group_exponent"] is None else row["group_exponent"],
            ),
        )
    )
    closed_sizes = tuple(
        row["group_size"] for row in rows if row["group_size"] is not None
    )
    return {
        "n": n,
        "orbit_count": summary.orbit_count,
        "truncated_orbit_count": summary.truncated_orbit_count,
        "max_closed_group_size": max(closed_sizes) if closed_sizes else None,
        "global_group_size": factorization.global_group_size,
        "global_group_exponent": factorization.global_group_exponent,
        "global_group_truncated": factorization.global_group_truncated,
        "product_group_size_bound": factorization.product_group_size_bound,
        "projection_image_sizes": tuple(row["projection_image_size"] for row in rows),
        "projections_match_orbit_groups": factorization.projections_match_orbit_groups,
        "rows": rows,
    }


def write_markdown(report):
    lines = [
        "# Structure-orbit holonomy audit",
        "",
        "Date: 2026-05-28",
        "",
        "This audit refines the structure-orbit reduction.  Degree-`n`",
        "structure classes are exactly braid orbits in `X^n`; the new helper",
        "`structure_orbit_holonomy_summary()` computes the finite braid-action",
        "group on each orbit separately.  The companion helper",
        "`structure_orbit_factorization_summary()` computes the global fixed-degree",
        "image and compares its projections with the orbit-holonomy factors.",
        "This is still fixed-`n` data, not an all-`n` proof.",
        "",
        "## Diagnostic rows",
        "",
    ]
    for name, rows in report.items():
        lines.extend([f"### {name}", ""])
        for row in rows:
            lines.extend(
                [
                    f"- `n={row['n']}`: orbits `{row['orbit_count']}`,",
                    f"  truncated orbits `{row['truncated_orbit_count']}`,",
                    f"  max closed group size `{row['max_closed_group_size']}`.",
                ]
            )
            compact = [
                (
                    item["orbit_size"],
                    item["group_size"],
                    item["group_exponent"],
                    item["projection_image_size"],
                )
                for item in row["rows"]
            ]
            lines.append(
                "  Orbit rows `(size, group size, exponent, projection size)`: "
                f"`{compact}`."
            )
            lines.append(
                "  Global image "
                f"`(size, exponent, truncated)=({row['global_group_size']}, "
                f"{row['global_group_exponent']}, {row['global_group_truncated']})`; "
                f"product bound `{row['product_group_size_bound']}`; "
                f"projection sizes `{row['projection_image_sizes']}`; "
                f"projections match orbit groups `{row['projections_match_orbit_groups']}`."
            )
        lines.append("")
    lines.extend(
        [
            "## Consequence",
            "",
            "The size-3 affine commutator diagnostic and the dihedral quandle have",
            "the same orbit-holonomy profile through the audited range.  At",
            "`n=4`, the nontrivial orbit groups have sizes `216`, `648`, and",
            "`648`, with exponents `12`, `36`, and `36`; the global image has",
            "size `648` and exponent `36`, while the product of orbit-holonomy",
            "factor sizes is `90699264`.  Thus the global image is a correlated",
            "subdirect subgroup of the orbit factors, not the whole product.",
            "At `n=5`, the three large orbit closures exceed the configured",
            "group-size cap.  This explains the moving-image warning in",
            "orbit-local terms: a normalized-law B candidate must keep a word",
            "nontrivial in one of these moving structure-orbit holonomy groups",
            "and in the correlated global image while becoming invisible to every",
            "fixed finite-G longitude detector.",
            "",
            "No truncated row is used as theorem evidence.  The rows only identify",
            "where the all-`n` proof or a B construction must control internal",
            "structure-orbit holonomy.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    solutions = {
        "identity_2": identity_solution([0, 1]),
        "trivial_rack_2": rack_solution([0, 1], lambda _left, right: right),
        "dihedral_quandle_3": rack_solution(
            [0, 1, 2], lambda left, right: (2 * left - right) % 3
        ),
        "size3_commutator_candidate": size3_commutator_candidate(),
    }
    report = {}
    for name, solution in solutions.items():
        max_n = 5 if name in {"dihedral_quandle_3", "size3_commutator_candidate"} else 4
        report[name] = [
            summary_payload(solution, n, max_group_size=5000)
            for n in range(2, max_n + 1)
        ]
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
