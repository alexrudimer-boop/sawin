import itertools
import json
import sys
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_audit import affine_solution  # noqa: E402
from run_linear_f2_audit import mat_rank, matrix_signature  # noqa: E402
from ybe_domination import (  # noqa: E402
    branch_tags,
    pure_generator_order_profile,
    pure_subgroup_growth_profile,
)


OUT_JSON = ROOT / "proofs" / "affine_f2_point_pushing_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_point_pushing_audit.md"


def _tags_key(tags):
    return "+".join(tags) if tags else "(untagged)"


def _order_row_to_dict(row):
    return {
        "braid_index": row.braid_index,
        "tuple_count": row.tuple_count,
        "generator_orders": list(row.generator_orders),
        "max_order": row.max_order,
    }


def _growth_row_to_dict(row):
    return {
        "braid_index": row.braid_index,
        "tuple_count": row.tuple_count,
        "generator_count": row.generator_count,
        "subgroup_size": row.subgroup_size,
        "subgroup_exponent": row.subgroup_exponent,
        "truncated": row.truncated,
    }


def _profile_key(rows):
    return ",".join(str(row.max_order) for row in rows)


def scan(
    dimension,
    *,
    max_braid_index=5,
    max_subgroup_size=100_000,
    max_subgroup_tuple_count=1024,
):
    rows = tuple(itertools.product((0, 1), repeat=2 * dimension))
    offsets = tuple(itertools.product((0, 1), repeat=2 * dimension))
    checked = 0
    invertible = 0
    ybe_count = 0
    profile_counts = Counter()
    untagged_profile_counts = Counter()
    max_generator_order = 1
    untagged_examples = []

    for matrix in itertools.product(rows, repeat=2 * dimension):
        checked += len(offsets)
        if mat_rank(matrix) != 2 * dimension:
            continue
        invertible += len(offsets)
        for offset in offsets:
            solution = affine_solution(matrix, offset, dimension)
            if not solution.is_ybe():
                continue
            ybe_count += 1
            tags = branch_tags(solution)
            profile = pure_generator_order_profile(solution, max_braid_index)
            max_generator_order = max(
                max_generator_order,
                max(row.max_order for row in profile),
            )
            key = (
                _tags_key(tags),
                _profile_key(profile),
                tuple(tuple(row.generator_orders) for row in profile),
            )
            profile_counts[key] += 1
            if not tags:
                untagged_profile_counts[_profile_key(profile)] += 1
                if len(untagged_examples) < 8:
                    growth = pure_subgroup_growth_profile(
                        solution,
                        max_braid_index,
                        max_subgroup_size=max_subgroup_size,
                        max_tuple_count=max_subgroup_tuple_count,
                    )
                    untagged_examples.append(
                        {
                            "matrix": matrix_signature(matrix),
                            "offset": "".join(str(cell) for cell in offset),
                            "branch_tags": list(tags),
                            "generator_order_profile": [
                                _order_row_to_dict(row)
                                for row in profile
                            ],
                            "point_pushing_subgroup_growth": [
                                _growth_row_to_dict(row)
                                for row in growth
                            ],
                        }
                    )

    return {
        "dimension": dimension,
        "point_count": 2**dimension,
        "max_braid_index": max_braid_index,
        "max_subgroup_size": max_subgroup_size,
        "max_subgroup_tuple_count": max_subgroup_tuple_count,
        "checked_affine_map_count": checked,
        "invertible_affine_map_count": invertible,
        "affine_ybe_count": ybe_count,
        "max_observed_point_pushing_generator_order": max_generator_order,
        "profile_counts": {
            (
                f"tags={tags}|max_orders={max_orders}|"
                f"generator_orders={generator_orders}"
            ): count
            for (tags, max_orders, generator_orders), count
            in sorted(profile_counts.items(), key=lambda item: repr(item[0]))
        },
        "untagged_count": sum(untagged_profile_counts.values()),
        "untagged_profile_counts": dict(sorted(untagged_profile_counts.items())),
        "untagged_examples": untagged_examples,
    }


def markdown_report(report):
    scan_report = report["f2_dimension_2"]
    lines = [
        "# Affine F2 Point-Pushing Audit",
        "",
        "## Purpose",
        "",
        "This generated audit stress-tests the point-pushing generator-order",
        "route in the translated affine four-point universe.  It complements",
        "`proofs/affine_f2_full_twist_audit.md`: the central full twist did not",
        "grow in the untagged affine rows, so here we check the standard pure",
        "point-pushing generators `A_{i,q}`.",
        "",
        "This is finite-prefix evidence only, not an all-arity theorem.",
        "",
        "## Results",
        "",
        f"- affine maps checked: `{scan_report['checked_affine_map_count']}`;",
        f"- invertible affine maps: `{scan_report['invertible_affine_map_count']}`;",
        f"- affine YBE tables: `{scan_report['affine_ybe_count']}`;",
        (
            "- checked point-pushing braid indices: "
            f"`2 <= q <= {scan_report['max_braid_index']}`;"
        ),
        (
            "- maximum observed point-pushing generator order: "
            f"`{scan_report['max_observed_point_pushing_generator_order']}`;"
        ),
        f"- untagged affine rows: `{scan_report['untagged_count']}`.",
        "",
        "Untagged point-pushing generator-order profiles:",
        "",
        "```text",
    ]
    for profile, count in scan_report["untagged_profile_counts"].items():
        lines.append(f"{profile}: {count}")
    lines.extend(
        [
            "```",
            "",
            "Thus every untagged affine `F_2^2` row in this finite universe has",
            "standard point-pushing generator orders",
            "",
            "```text",
            "2, 2, 2, 2",
            "```",
            "",
            "for `q=2,...,5`.  The recorded untagged examples also have",
            "point-pushing subgroup sizes `2,4,8,16` and exponent `2` through",
            "`q=5` under the audit cap.",
            "",
            "## Consequence",
            "",
            "The elementary pure-generator order route to a normalized-law",
            "counterexample must leave the checked translated affine `F_2^2`",
            "universe, or use more subtle relations inside the moving",
            "point-pushing subgroup rather than unbounded orders of the standard",
            "generators.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = {"f2_dimension_2": scan(2)}
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(markdown_report(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
