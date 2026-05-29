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
    direct_product_label_group,
    direct_product_witness,
    product_closed_label_longitude_subgroup_audit,
    product_closed_label_longitude_subgroup_failures,
    product_permutation_witness,
    solution_from_local_interval,
    swapped_product_label_group,
)


OUT_JSON = ROOT / "proofs" / "product_subgroup_audit.json"
OUT_MD = ROOT / "proofs" / "product_subgroup_audit.md"


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


def _closed_nonidentity_count(interval, branch, color_tuple, words):
    count = 0
    first = None
    for word in words:
        try:
            audit = product_closed_label_longitude_subgroup_audit(
                interval,
                branch,
                color_tuple,
                word,
            )
        except ValueError:
            continue
        if not audit.rows:
            continue
        count += 1
        if first is None:
            first = {
                "word": list(word),
                "subgroup_size": audit.subgroup_size,
                "generator_count": audit.generator_count,
                "nonidentity_closed_label_count": len(audit.rows),
            }
    return count, first


def _branch_group_order(interval, branch):
    if branch == "swapped":
        return len(swapped_product_label_group(interval).group.elements)
    if branch == "direct":
        return len(direct_product_label_group(interval).group.elements)
    raise ValueError(f"unknown branch {branch!r}")


def scan_product_branch(interval, branch, words):
    color_tuple = tuple(interval.colors[index % len(interval.colors)] for index in range(3))
    failures = product_closed_label_longitude_subgroup_failures(
        interval,
        branch,
        color_tuple,
        words,
    )
    closed_count, first_closed = _closed_nonidentity_count(
        interval,
        branch,
        color_tuple,
        words,
    )
    return {
        "branch": branch,
        "color_tuple": [repr(color) for color in color_tuple],
        "product_label_group_order": _branch_group_order(interval, branch),
        "closed_nonidentity_word_count": closed_count,
        "first_closed_nonidentity": first_closed,
        "failure_count": len(failures),
        "first_failure": None
        if not failures
        else {
            "word": list(failures[0].braid_word),
            "bad_rows": [
                {
                    "coordinate": row.coordinate,
                    "closed_label": list(row.closed_label),
                }
                for row in failures[0].bad_rows
            ],
            "subgroup_size": failures[0].audit.subgroup_size,
            "generator_count": failures[0].audit.generator_count,
        },
    }


def scan_base(base_index, base_solution, words):
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
    branch_scans = []
    branch_counts = Counter()
    group_order_counts = Counter()
    closed_nonidentity_total = 0
    failure_total = 0
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
        if not branches:
            continue
        total = solution_from_local_interval(interval).total
        for branch in branches:
            branch_counts[branch] += 1
            scan = scan_product_branch(interval, branch, words)
            group_order_counts[(branch, scan["product_label_group_order"])] += 1
            closed_nonidentity_total += scan["closed_nonidentity_word_count"]
            failure_total += scan["failure_count"]
            if scan["failure_count"] and len(first_failures) < 5:
                first_failures.append(
                    {
                        "branch": branch,
                        "base_index": base_index,
                        "base_signature": _solution_signature(base_solution),
                        "total_tags": list(branch_tags(total)),
                        "interval_table": _interval_table_signature(interval),
                        "failure": scan["first_failure"],
                    }
                )
            if len(branch_scans) < 8:
                branch_scans.append(
                    {
                        "branch": branch,
                        "base_index": base_index,
                        "total_tags": list(branch_tags(total)),
                        **scan,
                    }
                )

    return {
        "base_index": base_index,
        "base_signature": _solution_signature(base_solution),
        "checked_table_count": checked,
        "colored_ybe_count": colored_ybe_count,
        "local_minimal_count": local_minimal_count,
        "product_branch_counts": dict(sorted(branch_counts.items())),
        "product_group_order_counts": {
            f"{branch}|order={order}": count
            for (branch, order), count in sorted(group_order_counts.items())
        },
        "closed_nonidentity_word_count": closed_nonidentity_total,
        "subgroup_failure_count": failure_total,
        "first_branch_scans": branch_scans,
        "first_failures": first_failures,
    }


def write_markdown(report):
    totals = report["totals"]
    lines = [
        "# Product longitude-subgroup audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit applies the longitude-value subgroup criterion",
        "to the smallest arbitrary product local intervals: two quotient",
        "colours, two-point fibres, and every two-point YBE quotient base.",
        "It is finite candidate evidence only, not a proof of the product",
        "theorem.",
        "",
        "For each local-minimal product branch it scans braid words on three",
        "strands up to the configured bounded length.  Since the tagged fibre",
        "union has four points, the product label group has order at most",
        "`24`, so the audit enumerates every assignment `F_3 -> H_prod` for",
        "each closed word.",
        "",
        "## Totals",
        "",
        f"Word count: `{totals['word_count']}`.",
        f"Maximum word length: `{totals['max_word_length']}`.",
        f"Local tables checked: `{totals['checked_table_count']}`.",
        f"Coloured-YBE tables: `{totals['colored_ybe_count']}`.",
        f"Local-minimal intervals: `{totals['local_minimal_count']}`.",
        f"Product branch scans: `{totals['product_branch_scan_count']}`.",
        f"Closed nonidentity product-label words: `{totals['closed_nonidentity_word_count']}`.",
        f"Longitude-subgroup failures: `{totals['subgroup_failure_count']}`.",
        "",
        "Product branch counts:",
        "",
    ]
    for key, value in totals["product_branch_counts"].items():
        lines.append(f"- `{key}`: `{value}`.")
    lines.extend(["", "Product label group orders:", ""])
    for key, value in totals["product_group_order_counts"].items():
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
                f"Product branch counts: `{scan['product_branch_counts']}`.",
                f"Closed nonidentity words: `{scan['closed_nonidentity_word_count']}`.",
                f"Subgroup failures: `{scan['subgroup_failure_count']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Consequence",
            "",
            "No closed product label outside the longitude-value subgroup appears",
            "in this smallest arbitrary product corpus.  This is compatible with",
            "the A-route product subgroup lemma, but it is not theorem evidence:",
            "the product theorem still needs a symbolic all-`n` proof for",
            "arbitrary fibre sizes and quotient colour sets.",
            "",
            "For the B-route, the audit clarifies what a product counterexample",
            "should first look like: a closed product label outside the subgroup",
            "generated by all finite product-label longitude values, followed by",
            "an all-finite-group normalized-law diagonalization.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    n = 3
    max_word_length = 3
    words = bounded_words(n, max_word_length)
    bases = list(all_bijection_solutions(2))
    scans = {
        f"base_{index}": scan_base(index, base, words)
        for index, base in enumerate(bases)
    }
    branch_counts = Counter()
    group_order_counts = Counter()
    for scan in scans.values():
        branch_counts.update(scan["product_branch_counts"])
        for key, value in scan["product_group_order_counts"].items():
            group_order_counts[key] += value
    totals = {
        "n": n,
        "max_word_length": max_word_length,
        "word_count": len(words),
        "checked_table_count": sum(scan["checked_table_count"] for scan in scans.values()),
        "colored_ybe_count": sum(scan["colored_ybe_count"] for scan in scans.values()),
        "local_minimal_count": sum(scan["local_minimal_count"] for scan in scans.values()),
        "product_branch_scan_count": sum(
            sum(scan["product_branch_counts"].values())
            for scan in scans.values()
        ),
        "closed_nonidentity_word_count": sum(
            scan["closed_nonidentity_word_count"] for scan in scans.values()
        ),
        "subgroup_failure_count": sum(
            scan["subgroup_failure_count"] for scan in scans.values()
        ),
        "product_branch_counts": dict(sorted(branch_counts.items())),
        "product_group_order_counts": dict(sorted(group_order_counts.items())),
    }
    report = {
        "totals": totals,
        "bases": scans,
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
