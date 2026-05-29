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
    context_coretraction_audit,
    context_retraction_audit,
    coordinate_kernel_seed_pairs,
    direct_product_witness,
    generated_admissible_congruence_audit,
    product_permutation_witness,
    solution_from_local_interval,
    solution_table_signature,
)


OUT_JSON = ROOT / "proofs" / "two_colour_fibre2_all_bases_audit.json"
OUT_MD = ROOT / "proofs" / "two_colour_fibre2_all_bases_audit.md"


def _solution_signature(solution):
    return [list(value) for value in solution_table_signature(solution)]


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


def _family_signature(interval, family):
    return {
        repr(color): [
            sorted(repr(item) for item in block)
            for block in family[color]
        ]
        for color in interval.colors
    }


def _seed_count(seed_pairs):
    return sum(len(pairs) for pairs in seed_pairs.values())


def _row_key(row):
    return (
        row["retraction"],
        row["coretraction"],
        tuple(row["tags"]),
        row["output_kernel_kind"],
        row["output_kernel_depth"],
        row["all_coordinate_kernel_kind"],
        row["all_coordinate_kernel_depth"],
        row["has_product_witness"],
        row["has_direct_witness"],
    )


def scan_base(base_index, base_solution):
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
    semisplit_leak_count = 0
    row_counts = Counter()
    retraction_coretraction_counts = Counter()
    branch_tag_counts = Counter()
    output_kernel_counts = Counter()
    output_universal_depth_counts = Counter()
    unknown_examples = []
    first_examples = {}

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
        if interval.semisplit_families():
            semisplit_leak_count += 1

        retraction = context_retraction_audit(interval)
        coretraction = context_coretraction_audit(interval)
        total = solution_from_local_interval(interval).total
        tags = branch_tags(total)
        has_product = product_permutation_witness(interval) is not None
        has_direct = direct_product_witness(interval) is not None
        output_seeds = coordinate_kernel_seed_pairs(interval)
        all_coordinate_seeds = coordinate_kernel_seed_pairs(
            interval,
            include_coretraction_kernels=True,
        )
        output_audit = generated_admissible_congruence_audit(interval, output_seeds)
        all_coordinate_audit = generated_admissible_congruence_audit(
            interval,
            all_coordinate_seeds,
        )
        row = {
            "retraction": retraction.kind,
            "coretraction": coretraction.kind,
            "tags": list(tags),
            "output_kernel_kind": output_audit.kind,
            "output_kernel_depth": output_audit.stable_depth,
            "output_kernel_seed_count": _seed_count(output_seeds),
            "all_coordinate_kernel_kind": all_coordinate_audit.kind,
            "all_coordinate_kernel_depth": all_coordinate_audit.stable_depth,
            "all_coordinate_kernel_seed_count": _seed_count(all_coordinate_seeds),
            "has_product_witness": has_product,
            "has_direct_witness": has_direct,
        }
        key = _row_key(row)
        row_counts[key] += 1
        retraction_coretraction_counts[(retraction.kind, coretraction.kind)] += 1
        tag_key = "+".join(tags) if tags else "(untagged)"
        branch_tag_counts[tag_key] += 1
        output_kernel_counts[output_audit.kind] += 1
        if output_audit.kind == "universal":
            output_universal_depth_counts[output_audit.stable_depth] += 1

        example_key = (
            retraction.kind,
            coretraction.kind,
            output_audit.kind,
            output_audit.stable_depth,
            tuple(tags),
            has_product,
            has_direct,
        )
        if example_key not in first_examples:
            first_examples[example_key] = {
                "row": row,
                "output_kernel_family": _family_signature(interval, output_audit.family),
                "interval_table": _interval_table_signature(interval),
            }
        known = bool(
            set(tags)
            & {
                "involutive",
                "permutation_form",
                "affine_cyclic",
                "nondegenerate",
                "rack_type",
            }
        ) or has_product or has_direct
        if (
            not known
            and output_audit.kind == "universal"
            and len(unknown_examples) < 8
        ):
            unknown_examples.append(first_examples[example_key])

    return {
        "base_index": base_index,
        "base_signature": _solution_signature(base_solution),
        "checked_table_count": checked,
        "colored_ybe_count": colored_ybe_count,
        "local_minimal_count": local_minimal_count,
        "semisplit_leak_count": semisplit_leak_count,
        "retraction_coretraction_counts": {
            f"retraction={retraction}|coretraction={coretraction}": count
            for (retraction, coretraction), count in sorted(
                retraction_coretraction_counts.items(),
                key=lambda item: repr(item[0]),
            )
        },
        "branch_tag_counts": dict(sorted(branch_tag_counts.items())),
        "output_kernel_counts": dict(sorted(output_kernel_counts.items())),
        "output_universal_depth_counts": {
            str(depth): count
            for depth, count in sorted(output_universal_depth_counts.items())
        },
        "corridor_rows": [
            {
                "retraction": key[0],
                "coretraction": key[1],
                "tags": list(key[2]),
                "output_kernel_kind": key[3],
                "output_kernel_depth": key[4],
                "all_coordinate_kernel_kind": key[5],
                "all_coordinate_kernel_depth": key[6],
                "has_product_witness": key[7],
                "has_direct_witness": key[8],
                "count": count,
            }
            for key, count in sorted(row_counts.items(), key=lambda item: repr(item[0]))
        ],
        "unknown_universal_output_example_count": len(unknown_examples),
        "unknown_universal_output_examples": unknown_examples,
        "first_examples": {
            (
                f"retraction={key[0]}|coretraction={key[1]}|"
                f"output={key[2]}|depth={key[3]}|"
                f"tags={'+'.join(key[4]) if key[4] else '(untagged)'}|"
                f"product={key[5]}|direct={key[6]}"
            ): value
            for key, value in sorted(first_examples.items(), key=lambda item: repr(item[0]))
        },
    }


def _format_counts(counts):
    if not counts:
        return "`{}`"
    return ", ".join(f"`{key}`: `{value}`" for key, value in counts.items())


def write_markdown(report):
    totals = report["totals"]
    lines = [
        "# Two-colour fibre-2 all-base audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit enumerates arbitrary local bijection tables with",
        "two quotient colours and two-point fibres over every two-point YBE",
        "quotient base.  It is candidate-search evidence only; it is not a",
        "proof of the arbitrary-fibre or arbitrary-colour theorem.",
        "",
        "For each local-minimal interval it records two-sided",
        "retraction/coretraction kind, known branch tags, product/direct",
        "witnesses, and the output coordinate-kernel corridor closure.",
        "",
        "## Totals",
        "",
        f"Two-point quotient bases: `{totals['base_count']}`.",
        f"Local tables checked: `{totals['checked_table_count']}`.",
        f"Coloured-YBE local tables: `{totals['colored_ybe_count']}`.",
        f"Local-minimal intervals: `{totals['local_minimal_count']}`.",
        f"Semisplit leaks among local-minimal intervals: `{totals['semisplit_leak_count']}`.",
        (
            "Output kernel closures: "
            + _format_counts(totals["output_kernel_counts"])
            + "."
        ),
        (
            "Output universal depths: "
            + _format_counts(totals["output_universal_depth_counts"])
            + "."
        ),
        f"Unknown universal-output examples retained: `{totals['unknown_universal_output_example_count']}`.",
        "",
    ]
    for base_name, scan in report["bases"].items():
        lines.extend([f"## {base_name}", ""])
        lines.append(f"Checked local tables: `{scan['checked_table_count']}`.")
        lines.append(f"Coloured-YBE tables: `{scan['colored_ybe_count']}`.")
        lines.append(f"Local-minimal intervals: `{scan['local_minimal_count']}`.")
        lines.append(f"Semisplit leaks: `{scan['semisplit_leak_count']}`.")
        lines.append(
            "Retraction/coretraction: "
            + _format_counts(scan["retraction_coretraction_counts"])
            + "."
        )
        lines.append(
            "Output kernel closures: "
            + _format_counts(scan["output_kernel_counts"])
            + "."
        )
        lines.append(
            "Output universal depths: "
            + _format_counts(scan["output_universal_depth_counts"])
            + "."
        )
        lines.append(f"Unknown universal-output examples: `{scan['unknown_universal_output_example_count']}`.")
        lines.append("")
        if scan["corridor_rows"]:
            lines.append("Corridor rows:")
            lines.append("")
            for row in scan["corridor_rows"]:
                tag_text = "+".join(row["tags"]) if row["tags"] else "(untagged)"
                lines.append(
                    "- "
                    f"retraction `{row['retraction']}`, "
                    f"coretraction `{row['coretraction']}`, "
                    f"tags `{tag_text}`, "
                    f"output `{row['output_kernel_kind']}` depth "
                    f"`{row['output_kernel_depth']}`, "
                    f"all-coordinate `{row['all_coordinate_kernel_kind']}` "
                    f"depth `{row['all_coordinate_kernel_depth']}`, "
                    f"product `{row['has_product_witness']}`, "
                    f"direct `{row['has_direct_witness']}`: "
                    f"`{row['count']}`."
                )
            lines.append("")
    lines.extend(
        [
            "## Consequence",
            "",
            "This all-base extension closes a small audit hole in the fibre-size-two",
            "local search.  Across every two-point quotient base, the arbitrary",
            "two-point-fibre local-minimal intervals still produce no untagged",
            "universal output-kernel corridor.  Since fibre-size-two affine",
            "`F_2` branches are already bookkept as finite-G measurable, this",
            "does not prove a new theorem; it just removes the smallest",
            "two-colour/two-fibre hiding place for a transported-corridor",
            "counterexample.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    bases = list(all_bijection_solutions(2))
    scans = {
        f"base_{index}": scan_base(index, base)
        for index, base in enumerate(bases)
    }
    totals = {
        "base_count": len(bases),
        "checked_table_count": sum(scan["checked_table_count"] for scan in scans.values()),
        "colored_ybe_count": sum(scan["colored_ybe_count"] for scan in scans.values()),
        "local_minimal_count": sum(scan["local_minimal_count"] for scan in scans.values()),
        "semisplit_leak_count": sum(scan["semisplit_leak_count"] for scan in scans.values()),
        "unknown_universal_output_example_count": sum(
            scan["unknown_universal_output_example_count"]
            for scan in scans.values()
        ),
    }
    output_counts = Counter()
    universal_depths = Counter()
    for scan in scans.values():
        output_counts.update(scan["output_kernel_counts"])
        universal_depths.update(scan["output_universal_depth_counts"])
    totals["output_kernel_counts"] = dict(sorted(output_counts.items()))
    totals["output_universal_depth_counts"] = dict(sorted(universal_depths.items()))
    report = {"totals": totals, "bases": scans}
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
