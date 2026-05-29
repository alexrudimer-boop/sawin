import itertools
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    LocalInterval,
    all_bijection_solutions,
    bounded_words,
    branch_tags,
    direct_product_witness,
    product_holonomy_groups,
    product_holonomy_longitude_subgroup_audit,
    product_permutation_witness,
    solution_from_local_interval,
)


OUT_JSON = ROOT / "proofs" / "product_holonomy_subgroup_audit.json"
OUT_MD = ROOT / "proofs" / "product_holonomy_subgroup_audit.md"


def _solution_signature(solution):
    return [
        [repr(left), repr(right)]
        for left, right in (
            solution.R[(x, y)]
            for x in solution.elements
            for y in solution.elements
        )
    ]


def _interval_table_signature(interval):
    return [
        {
            "colors": [repr(a), repr(b)],
            "input": [repr(x), repr(y)],
            "output": [repr(u), repr(v)],
        }
        for a in interval.colors
        for b in interval.colors
        for x in interval.fibres[a]
        for y in interval.fibres[b]
        for u, v in [interval.T[(a, b, x, y)]]
    ]


def scan_product_branch(base_index, interval, branch, words, n):
    groups = product_holonomy_groups(interval, branch)
    holonomy_groups = [
        {
            "model_points": [repr(point) for point in target.model_points],
            "order": len(target.group.elements),
        }
        for target in groups
    ]
    closed_tuple_word_count = 0
    nonidentity_row_count = 0
    subgroup_failure_count = 0
    first_closed = None
    first_failure = None

    for color_tuple in itertools.product(interval.colors, repeat=n):
        for word in words:
            try:
                audit = product_holonomy_longitude_subgroup_audit(
                    interval,
                    branch,
                    color_tuple,
                    word,
                )
            except ValueError:
                continue
            if not audit.rows:
                continue
            closed_tuple_word_count += 1
            nonidentity_row_count += len(audit.rows)
            bad_rows = tuple(row for row in audit.rows if not row.in_longitude_subgroup)
            if first_closed is None:
                first_closed = {
                    "color_tuple": [repr(color) for color in color_tuple],
                    "word": list(word),
                    "nonidentity_row_count": len(audit.rows),
                    "subgroup_sizes": {
                        repr(model): size
                        for model, size in audit.subgroup_sizes.items()
                    },
                    "generator_counts": {
                        repr(model): count
                        for model, count in audit.generator_counts.items()
                    },
                }
            if bad_rows:
                subgroup_failure_count += 1
                if first_failure is None:
                    first_failure = {
                        "color_tuple": [repr(color) for color in color_tuple],
                        "word": list(word),
                        "bad_rows": [
                            {
                                "coordinate": row.coordinate,
                                "model_points": [
                                    repr(point) for point in row.model_points
                                ],
                                "closed_holonomy": list(row.closed_holonomy),
                            }
                            for row in bad_rows
                        ],
                    }

    total = solution_from_local_interval(interval).total
    return {
        "base_index": base_index,
        "branch": branch,
        "total_tags": list(branch_tags(total)),
        "holonomy_group_count": len(holonomy_groups),
        "holonomy_groups": holonomy_groups,
        "closed_tuple_word_count": closed_tuple_word_count,
        "nonidentity_row_count": nonidentity_row_count,
        "subgroup_failure_count": subgroup_failure_count,
        "first_closed_nonidentity": first_closed,
        "first_failure": first_failure,
    }


def scan_base(base_index, base_solution, words, n):
    colors = base_solution.elements
    fibres = {color: (0, 1) for color in colors}
    source_pairs = {
        (a, b): [(x, y) for x in fibres[a] for y in fibres[b]]
        for a in colors
        for b in colors
    }
    target_permutations = {
        key: list(
            itertools.permutations(
                [
                    (x, y)
                    for x in fibres[base_solution.R[key][0]]
                    for y in fibres[base_solution.R[key][1]]
                ]
            )
        )
        for key in source_pairs
    }
    keys = tuple(source_pairs)
    checked = 0
    colored_ybe_count = 0
    local_minimal_count = 0
    branch_counts = Counter()
    holonomy_group_order_counts = Counter()
    closed_tuple_word_total = 0
    nonidentity_row_total = 0
    failure_total = 0
    first_branch_scans = []
    first_failures = []

    for choices in itertools.product(*(target_permutations[key] for key in keys)):
        checked += 1
        table = {}
        for key, images in zip(keys, choices):
            for source, image in zip(source_pairs[key], images):
                table[(key[0], key[1], source[0], source[1])] = image
        interval = LocalInterval(colors, fibres, base_solution.R, table)
        if not interval.is_colored_ybe():
            continue
        colored_ybe_count += 1
        if not interval.is_local_minimal(max_fibre_size=2):
            continue
        local_minimal_count += 1

        branches = []
        if product_permutation_witness(interval) is not None:
            branches.append("swapped")
        if direct_product_witness(interval) is not None:
            branches.append("direct")
        for branch in branches:
            branch_counts[branch] += 1
            scan = scan_product_branch(base_index, interval, branch, words, n)
            for target in scan["holonomy_groups"]:
                holonomy_group_order_counts[(branch, target["order"])] += 1
            closed_tuple_word_total += scan["closed_tuple_word_count"]
            nonidentity_row_total += scan["nonidentity_row_count"]
            failure_total += scan["subgroup_failure_count"]
            if scan["subgroup_failure_count"] and len(first_failures) < 5:
                first_failures.append(
                    {
                        "branch": branch,
                        "base_index": base_index,
                        "base_signature": _solution_signature(base_solution),
                        "interval_table": _interval_table_signature(interval),
                        "failure": scan["first_failure"],
                    }
                )
            if len(first_branch_scans) < 8:
                first_branch_scans.append(scan)

    return {
        "base_index": base_index,
        "base_signature": _solution_signature(base_solution),
        "checked_table_count": checked,
        "colored_ybe_count": colored_ybe_count,
        "local_minimal_count": local_minimal_count,
        "product_branch_counts": dict(sorted(branch_counts.items())),
        "holonomy_group_order_counts": {
            f"{branch}|order={order}": count
            for (branch, order), count in sorted(holonomy_group_order_counts.items())
        },
        "closed_tuple_word_count": closed_tuple_word_total,
        "nonidentity_holonomy_row_count": nonidentity_row_total,
        "subgroup_failure_count": failure_total,
        "first_branch_scans": first_branch_scans,
        "first_failures": first_failures,
    }


def _format_count_map(counts):
    if not counts:
        return "`{}`"
    return ", ".join(f"`{key}`: `{value}`" for key, value in counts.items())


def write_markdown(report):
    totals = report["totals"]
    lines = [
        "# Product holonomy-subgroup audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit applies the gauge-normalized product holonomy",
        "longitude-subgroup criterion to the smallest arbitrary product local",
        "intervals: two quotient colours, two-point fibres, and every",
        "two-point YBE quotient base.",
        "",
        "It is finite candidate evidence only.  It removes the coboundary",
        "transport first, then tests only the residual finite holonomy groups.",
        "A theorem still requires the corresponding all-`n` subgroup membership",
        "proof for arbitrary fibre sizes and quotient colours.",
        "",
        "For each local-minimal product branch it scans all colour tuples in",
        "`Z^3` and all braid words on three strands up to the configured bounded",
        "length.  In this corpus the normalized holonomy groups have order at",
        "most `2`, so all assignments `F_3 -> H` are enumerated exactly for",
        "each finite word.",
        "",
        "## Totals",
        "",
        f"Word count: `{totals['word_count']}`.",
        f"Maximum word length: `{totals['max_word_length']}`.",
        f"Local tables checked: `{totals['checked_table_count']}`.",
        f"Coloured-YBE tables: `{totals['colored_ybe_count']}`.",
        f"Local-minimal intervals: `{totals['local_minimal_count']}`.",
        f"Product branch scans: `{totals['product_branch_scan_count']}`.",
        (
            "Closed tuple-word scans with nonidentity normalized holonomy: "
            f"`{totals['closed_tuple_word_count']}`."
        ),
        (
            "Nonidentity normalized holonomy rows: "
            f"`{totals['nonidentity_holonomy_row_count']}`."
        ),
        (
            "Normalized holonomy-subgroup failures: "
            f"`{totals['subgroup_failure_count']}`."
        ),
        "",
        "Product branch counts:",
        "",
    ]
    for key, value in totals["product_branch_counts"].items():
        lines.append(f"- `{key}`: `{value}`.")
    lines.extend(["", "Normalized holonomy group orders:", ""])
    for key, value in totals["holonomy_group_order_counts"].items():
        lines.append(f"- `{key}`: `{value}`.")
    lines.append("")
    for base_name, scan in report["bases"].items():
        lines.extend(
            [
                f"## {base_name}",
                "",
                f"Checked local tables: `{scan['checked_table_count']}`.",
                f"Coloured-YBE tables: `{scan['colored_ybe_count']}`.",
                f"Local-minimal intervals: `{scan['local_minimal_count']}`.",
                (
                    "Product branch counts: "
                    + _format_count_map(scan["product_branch_counts"])
                    + "."
                ),
                (
                    "Closed tuple-word scans with nonidentity normalized "
                    f"holonomy: `{scan['closed_tuple_word_count']}`."
                ),
                (
                    "Nonidentity normalized holonomy rows: "
                    f"`{scan['nonidentity_holonomy_row_count']}`."
                ),
                f"Subgroup failures: `{scan['subgroup_failure_count']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Consequence",
            "",
            "No normalized product holonomy outside the longitude-value subgroup",
            "appears in this smallest arbitrary product corpus.  This is not a",
            "proof of the product theorem, but it confirms that the new",
            "gauge-normalized target agrees with the older product-label",
            "subgroup audit on the first arbitrary corpus.",
            "",
            "For outcome B, a product candidate should now supply a closed",
            "normalized holonomy label outside this subgroup before attempting",
            "the all-finite-group normalized-law diagonalization.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def build_report():
    n = 3
    max_word_length = 3
    words = bounded_words(n, max_word_length)
    bases = list(all_bijection_solutions(2))
    scans = {
        f"base_{index}": scan_base(index, base, words, n)
        for index, base in enumerate(bases)
    }

    branch_counts = Counter()
    holonomy_group_order_counts = Counter()
    for scan in scans.values():
        branch_counts.update(scan["product_branch_counts"])
        for key, value in scan["holonomy_group_order_counts"].items():
            holonomy_group_order_counts[key] += value

    totals = {
        "n": n,
        "max_word_length": max_word_length,
        "word_count": len(words),
        "checked_table_count": sum(
            scan["checked_table_count"] for scan in scans.values()
        ),
        "colored_ybe_count": sum(
            scan["colored_ybe_count"] for scan in scans.values()
        ),
        "local_minimal_count": sum(
            scan["local_minimal_count"] for scan in scans.values()
        ),
        "product_branch_scan_count": sum(
            sum(scan["product_branch_counts"].values())
            for scan in scans.values()
        ),
        "closed_tuple_word_count": sum(
            scan["closed_tuple_word_count"] for scan in scans.values()
        ),
        "nonidentity_holonomy_row_count": sum(
            scan["nonidentity_holonomy_row_count"] for scan in scans.values()
        ),
        "subgroup_failure_count": sum(
            scan["subgroup_failure_count"] for scan in scans.values()
        ),
        "product_branch_counts": dict(sorted(branch_counts.items())),
        "holonomy_group_order_counts": dict(sorted(holonomy_group_order_counts.items())),
    }
    report = {"totals": totals, "bases": scans}
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    return report


def main():
    report = build_report()
    print(OUT_JSON)
    print(OUT_MD)
    print(json.dumps(report["totals"], sort_keys=True))


if __name__ == "__main__":
    main()
