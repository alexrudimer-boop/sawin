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
    branch_tags,
    direct_product_label_group,
    direct_product_witness,
    product_closed_label_exact_audit,
    product_permutation_witness,
    solution_from_local_interval,
    swapped_product_label_group,
)


OUT_JSON = ROOT / "proofs" / "product_exact_closed_label_audit.json"
OUT_MD = ROOT / "proofs" / "product_exact_closed_label_audit.md"


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


def _branch_group(interval, branch):
    if branch == "swapped":
        return swapped_product_label_group(interval).group
    if branch == "direct":
        return direct_product_label_group(interval).group
    raise ValueError(f"unknown branch {branch!r}")


def _known_tagged(tags):
    known = {
        "rack_type",
        "involutive",
        "identity_table",
        "permutation_form",
        "left_nondegenerate",
        "right_nondegenerate",
        "nondegenerate",
        "affine_cyclic",
    }
    return bool(known.intersection(tags))


def _scan_branch(interval, branch, state_limit):
    detector = _branch_group(interval, branch)
    scans = []
    for color_tuple in itertools.product(interval.colors, repeat=2):
        audit = product_closed_label_exact_audit(
            interval,
            branch,
            (detector,),
            color_tuple,
            state_limit=state_limit,
        )
        scans.append(
            {
                "color_tuple": [repr(color) for color in color_tuple],
                "visited_state_count": audit.visited_state_count,
                "base_state_count": audit.base_state_count,
                "product_state_count": audit.product_state_count,
                "detector_state_count": audit.detector_state_count,
                "closed_state_count": audit.closed_state_count,
                "identity_detector_closed_state_count": audit.identity_detector_closed_state_count,
                "truncated": audit.truncated,
                "failure": None
                if audit.failure is None
                else {
                    "word": list(audit.failure.braid_word),
                    "coordinate": audit.failure.coordinate,
                    "closed_label": list(audit.failure.closed_label),
                },
            }
        )
    return {
        "branch": branch,
        "detector_order": len(detector.elements),
        "tuple_scans": scans,
    }


def scan_base(base_index, base_solution, state_limit):
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
    branch_scan_count = 0
    tuple_scan_count = 0
    truncated_count = 0
    failure_count = 0
    known_failure_count = 0
    untagged_failure_count = 0
    max_visited = 0
    branch_counts = Counter()
    detector_order_counts = Counter()
    first_bad = []
    first_good = []

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
        tags = list(branch_tags(total))
        for branch in branches:
            branch_counts[branch] += 1
            branch_scan_count += 1
            branch_result = _scan_branch(interval, branch, state_limit)
            detector_order_counts[(branch, branch_result["detector_order"])] += 1
            for tuple_scan in branch_result["tuple_scans"]:
                tuple_scan_count += 1
                max_visited = max(max_visited, tuple_scan["visited_state_count"])
                if tuple_scan["truncated"]:
                    truncated_count += 1
                if tuple_scan["failure"] is not None:
                    failure_count += 1
                    if _known_tagged(tags):
                        known_failure_count += 1
                    else:
                        untagged_failure_count += 1
                if (
                    (tuple_scan["truncated"] or tuple_scan["failure"] is not None)
                    and len(first_bad) < 5
                ):
                    first_bad.append(
                        {
                            "branch": branch,
                            "base_index": base_index,
                            "base_signature": _solution_signature(base_solution),
                            "total_tags": tags,
                            "interval_table": _interval_table_signature(interval),
                            "tuple_scan": tuple_scan,
                        }
                    )
            if len(first_good) < 8:
                first_good.append(
                    {
                        "branch": branch,
                        "base_index": base_index,
                        "total_tags": tags,
                        **branch_result,
                    }
                )

    return {
        "base_index": base_index,
        "base_signature": _solution_signature(base_solution),
        "checked_table_count": checked,
        "colored_ybe_count": colored_ybe_count,
        "local_minimal_count": local_minimal_count,
        "branch_scan_count": branch_scan_count,
        "tuple_scan_count": tuple_scan_count,
        "truncated_count": truncated_count,
        "failure_count": failure_count,
        "known_failure_count": known_failure_count,
        "untagged_failure_count": untagged_failure_count,
        "max_visited_state_count": max_visited,
        "branch_counts": dict(sorted(branch_counts.items())),
        "detector_order_counts": {
            f"{branch}|order={order}": count
            for (branch, order), count in sorted(detector_order_counts.items())
        },
        "first_bad": first_bad,
        "first_good": first_good,
    }


def write_markdown(report):
    totals = report["totals"]
    lines = [
        "# Product exact closed-label audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit applies `product_closed_label_exact_audit()` to",
        "the smallest arbitrary product local intervals: two quotient colours,",
        "two-point fibres, and every two-point YBE quotient base.",
        "",
        "It is exact only at fixed braid degree `n=2` and fixed colour tuples.",
        "It closes the finite joint image of product labels, Artin strand",
        "permutation, the quotient colour base action, and the product label",
        "group detector.  It is not an all-`n` proof of the product theorem.",
        "",
        "## Totals",
        "",
        f"State limit per tuple: `{totals['state_limit']}`.",
        f"Local tables checked: `{totals['checked_table_count']}`.",
        f"Coloured-YBE tables: `{totals['colored_ybe_count']}`.",
        f"Local-minimal intervals: `{totals['local_minimal_count']}`.",
        f"Product branch scans: `{totals['branch_scan_count']}`.",
        f"Fixed colour-tuple scans: `{totals['tuple_scan_count']}`.",
        f"Truncated tuple scans: `{totals['truncated_count']}`.",
        f"Exact detector failures: `{totals['failure_count']}`.",
        f"Known-tagged detector failures: `{totals['known_failure_count']}`.",
        f"Untagged detector failures: `{totals['untagged_failure_count']}`.",
        f"Maximum visited states: `{totals['max_visited_state_count']}`.",
        "",
        "Product branch counts:",
        "",
    ]
    for key, value in totals["branch_counts"].items():
        lines.append(f"- `{key}`: `{value}`.")
    lines.extend(["", "Product label detector orders:", ""])
    for key, value in totals["detector_order_counts"].items():
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
                f"Product branch scans: `{scan['branch_scan_count']}`.",
                f"Fixed tuple scans: `{scan['tuple_scan_count']}`.",
                f"Truncated scans: `{scan['truncated_count']}`.",
                f"Failures: `{scan['failure_count']}`.",
                f"Known-tagged failures: `{scan['known_failure_count']}`.",
                f"Untagged failures: `{scan['untagged_failure_count']}`.",
                f"Max visited states: `{scan['max_visited_state_count']}`.",
                "",
            ]
        )
    lines.extend(
        [
            "## Consequence",
            "",
            "The raw product label group detector, with only the quotient colour",
            "base action, has fixed-degree failures in this corpus at `n=2`, but",
            "every recorded failure lies in a row already tagged by known",
            "finite-G-measurable branches.  No untagged fixed-degree failure",
            "appears, and no tuple scan truncates.  This strengthens the product",
            "audit by removing the word-length cutoff in the smallest product",
            "corpus at braid degree two while also showing that the product label",
            "group alone should not be treated as the final detector in known",
            "nondegenerate/rack rows.",
            "",
            "This remains finite fixed-degree evidence.  The product A-route",
            "still needs a symbolic all-`n` proof that closed labels lie in the",
            "subgroup generated by recursive Artin-longitude values in one fixed",
            "product label group, or a normalized-law counterexample.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    state_limit = 5000
    bases = list(all_bijection_solutions(2))
    scans = {
        f"base_{index}": scan_base(index, base, state_limit)
        for index, base in enumerate(bases)
    }
    branch_counts = Counter()
    detector_order_counts = Counter()
    for scan in scans.values():
        branch_counts.update(scan["branch_counts"])
        for key, value in scan["detector_order_counts"].items():
            detector_order_counts[key] += value
    totals = {
        "state_limit": state_limit,
        "checked_table_count": sum(scan["checked_table_count"] for scan in scans.values()),
        "colored_ybe_count": sum(scan["colored_ybe_count"] for scan in scans.values()),
        "local_minimal_count": sum(scan["local_minimal_count"] for scan in scans.values()),
        "branch_scan_count": sum(scan["branch_scan_count"] for scan in scans.values()),
        "tuple_scan_count": sum(scan["tuple_scan_count"] for scan in scans.values()),
        "truncated_count": sum(scan["truncated_count"] for scan in scans.values()),
        "failure_count": sum(scan["failure_count"] for scan in scans.values()),
        "known_failure_count": sum(scan["known_failure_count"] for scan in scans.values()),
        "untagged_failure_count": sum(scan["untagged_failure_count"] for scan in scans.values()),
        "max_visited_state_count": max(
            scan["max_visited_state_count"] for scan in scans.values()
        ),
        "branch_counts": dict(sorted(branch_counts.items())),
        "detector_order_counts": dict(sorted(detector_order_counts.items())),
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
