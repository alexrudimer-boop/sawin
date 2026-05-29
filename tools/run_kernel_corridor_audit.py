import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    CongruenceInterval,
    all_bijection_solutions,
    branch_tags,
    context_coretraction_audit,
    context_retraction_audit,
    congruences,
    coordinate_kernel_seed_pairs,
    direct_product_witness,
    generated_admissible_congruence_audit,
    interval_covers,
    product_permutation_witness,
    solution_from_local_interval,
    solution_table_signature,
)

OUT_JSON = ROOT / "proofs" / "kernel_corridor_audit.json"
OUT_MD = ROOT / "proofs" / "kernel_corridor_audit.md"


def _table_signature(solution):
    return [list(value) for value in solution_table_signature(solution)]


def _partition_signature(partition):
    return [sorted(repr(element) for element in block) for block in partition]


def _family_signature(interval, family):
    return {
        repr(color): _partition_signature(family[color])
        for color in interval.colors
    }


def _seed_count(seed_pairs):
    return sum(len(pairs) for pairs in seed_pairs.values())


def _row_key(row):
    return (
        row["retraction"],
        row["coretraction"],
        tuple(row["tags"]),
        row["output_kind"],
        row["output_depth"],
        row["all_coordinate_kind"],
        row["all_coordinate_depth"],
        row["output_seed_count"],
        row["all_coordinate_seed_count"],
        row["has_product_witness"],
        row["has_direct_witness"],
    )


def scan_size(size):
    local_minimal_cover_count = 0
    semisplit_leaks = []
    row_counts = Counter()
    output_kind_counts = Counter()
    all_coordinate_kind_counts = Counter()
    output_universal_depth_counts = Counter()
    bifree_output_kind_counts = Counter()
    bifree_universal_depth_counts = Counter()
    product_side_counts = Counter()
    examples = {}

    for solution_index, solution in enumerate(all_bijection_solutions(size)):
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            if not interval.is_local_minimal():
                continue
            local_minimal_cover_count += 1

            semisplit = interval.semisplit_families()
            if semisplit and len(semisplit_leaks) < 5:
                semisplit_leaks.append(
                    {
                        "solution_index": solution_index,
                        "lower_partition": _partition_signature(lower),
                        "upper_partition": _partition_signature(upper),
                        "semisplit_count": len(semisplit),
                        "first_semisplit": _family_signature(interval, semisplit[0]),
                        "original_table_values": _table_signature(solution),
                    }
                )

            retraction = context_retraction_audit(interval)
            coretraction = context_coretraction_audit(interval)
            total = solution_from_local_interval(interval).total
            tags = branch_tags(total)
            output_seeds = coordinate_kernel_seed_pairs(
                interval,
                include_coretraction_kernels=False,
            )
            all_coordinate_seeds = coordinate_kernel_seed_pairs(
                interval,
                include_coretraction_kernels=True,
            )
            output_audit = generated_admissible_congruence_audit(
                interval,
                output_seeds,
            )
            all_coordinate_audit = generated_admissible_congruence_audit(
                interval,
                all_coordinate_seeds,
            )
            has_product = product_permutation_witness(interval) is not None
            has_direct = direct_product_witness(interval) is not None
            row = {
                "retraction": retraction.kind,
                "coretraction": coretraction.kind,
                "tags": list(tags),
                "output_kind": output_audit.kind,
                "output_depth": output_audit.stable_depth,
                "all_coordinate_kind": all_coordinate_audit.kind,
                "all_coordinate_depth": all_coordinate_audit.stable_depth,
                "output_seed_count": _seed_count(output_seeds),
                "all_coordinate_seed_count": _seed_count(all_coordinate_seeds),
                "output_edge_counts": [
                    [repr(color), count]
                    for color, count in output_audit.edge_count_rows
                ],
                "output_diameters": [
                    [repr(color), diameter]
                    for color, diameter in output_audit.diameter_rows
                ],
                "has_product_witness": has_product,
                "has_direct_witness": has_direct,
            }
            key = _row_key(row)
            row_counts[key] += 1
            output_kind_counts[output_audit.kind] += 1
            all_coordinate_kind_counts[all_coordinate_audit.kind] += 1
            if output_audit.kind == "universal":
                output_universal_depth_counts[output_audit.stable_depth] += 1
            if retraction.kind == "equality" and coretraction.kind == "equality":
                bifree_output_kind_counts[output_audit.kind] += 1
                if output_audit.kind == "universal":
                    bifree_universal_depth_counts[output_audit.stable_depth] += 1
            if retraction.kind == "universal" or coretraction.kind == "universal":
                product_side_counts[
                    (
                        retraction.kind,
                        coretraction.kind,
                        has_product,
                        has_direct,
                    )
                ] += 1

            example_key = (
                retraction.kind,
                coretraction.kind,
                output_audit.kind,
                output_audit.stable_depth,
                tuple(tags),
            )
            if example_key not in examples:
                examples[example_key] = {
                    "solution_index": solution_index,
                    "lower_partition": _partition_signature(lower),
                    "upper_partition": _partition_signature(upper),
                    "row": row,
                    "output_family": _family_signature(interval, output_audit.family),
                    "original_table_values": _table_signature(solution),
                }

    return {
        "size": size,
        "local_minimal_cover_count": local_minimal_cover_count,
        "semisplit_leak_count": len(semisplit_leaks),
        "semisplit_leaks": semisplit_leaks,
        "output_kind_counts": dict(sorted(output_kind_counts.items())),
        "all_coordinate_kind_counts": dict(sorted(all_coordinate_kind_counts.items())),
        "output_universal_depth_counts": {
            str(depth): count
            for depth, count in sorted(output_universal_depth_counts.items())
        },
        "bifree_output_kind_counts": dict(sorted(bifree_output_kind_counts.items())),
        "bifree_universal_depth_counts": {
            str(depth): count
            for depth, count in sorted(bifree_universal_depth_counts.items())
        },
        "product_side_counts": {
            (
                f"retraction={retraction}|coretraction={coretraction}|"
                f"product={has_product}|direct={has_direct}"
            ): count
            for (retraction, coretraction, has_product, has_direct), count in sorted(
                product_side_counts.items(),
                key=lambda item: repr(item[0]),
            )
        },
        "corridor_rows": [
            {
                "retraction": key[0],
                "coretraction": key[1],
                "tags": list(key[2]),
                "output_kind": key[3],
                "output_depth": key[4],
                "all_coordinate_kind": key[5],
                "all_coordinate_depth": key[6],
                "output_seed_count": key[7],
                "all_coordinate_seed_count": key[8],
                "has_product_witness": key[9],
                "has_direct_witness": key[10],
                "count": count,
            }
            for key, count in sorted(row_counts.items(), key=lambda item: repr(item[0]))
        ],
        "examples": {
            (
                f"retraction={key[0]}|coretraction={key[1]}|"
                f"output={key[2]}|depth={key[3]}|"
                f"tags={'+'.join(key[4]) if key[4] else '(untagged)'}"
            ): value
            for key, value in sorted(examples.items(), key=lambda item: repr(item[0]))
        },
    }


def _format_count_map(counts):
    if not counts:
        return "`{}`"
    return ", ".join(f"`{key}`: `{value}`" for key, value in counts.items())


def write_markdown(report):
    lines = [
        "# Kernel corridor audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit scans local-minimal congruence-cover intervals and",
        "records the least admissible congruence family generated by coordinate",
        "kernels.  It is a finite stress test only.  It does not prove the",
        "Master Local-Minimal Residual Theorem.",
        "",
        "The output-kernel closure uses the two nondegeneracy coordinate kernels",
        "`y -> pr_1 T(x,y)` and `x -> pr_2 T(x,y)`.  The all-coordinate closure",
        "also includes the coretraction-side kernels `x -> pr_1 T(x,y)` and",
        "`y -> pr_2 T(x,y)`.  The stable depth is `0` exactly when the seed",
        "kernel graph already has the final connected components before any",
        "transport through local tables or inverse local tables adds a new",
        "edge.",
        "",
    ]
    for name, scan in report.items():
        lines.extend([f"## {name}", ""])
        lines.append(f"Local-minimal covers: `{scan['local_minimal_cover_count']}`.")
        lines.append(f"Semisplit leaks among local-minimal covers: `{scan['semisplit_leak_count']}`.")
        lines.append("")
        lines.append(
            "Output closure kinds: "
            + _format_count_map(scan["output_kind_counts"])
            + "."
        )
        lines.append(
            "All-coordinate closure kinds: "
            + _format_count_map(scan["all_coordinate_kind_counts"])
            + "."
        )
        lines.append(
            "Output universal depths: "
            + _format_count_map(scan["output_universal_depth_counts"])
            + "."
        )
        lines.append(
            "Bi-free output closure kinds: "
            + _format_count_map(scan["bifree_output_kind_counts"])
            + "."
        )
        lines.append(
            "Bi-free universal depths: "
            + _format_count_map(scan["bifree_universal_depth_counts"])
            + "."
        )
        lines.append("")
        lines.append("Product-side witness counts:")
        lines.append("")
        if scan["product_side_counts"]:
            for key, count in scan["product_side_counts"].items():
                lines.append(f"- `{key}`: `{count}`")
        else:
            lines.append("- none")
        lines.append("")
        lines.append("Corridor rows:")
        lines.append("")
        for row in scan["corridor_rows"]:
            tag_text = "+".join(row["tags"]) if row["tags"] else "(untagged)"
            lines.append(
                "- "
                f"retraction `{row['retraction']}`, "
                f"coretraction `{row['coretraction']}`, "
                f"tags `{tag_text}`, "
                f"output `{row['output_kind']}` depth `{row['output_depth']}` "
                f"from `{row['output_seed_count']}` seeds, "
                f"all-coordinate `{row['all_coordinate_kind']}` depth "
                f"`{row['all_coordinate_depth']}` from "
                f"`{row['all_coordinate_seed_count']}` seeds, "
                f"product witness `{row['has_product_witness']}`, "
                f"direct witness `{row['has_direct_witness']}`: "
                f"`{row['count']}`."
            )
        lines.append("")
    lines.extend(
        [
            "## Consequence",
            "",
            "The audit has two roles.  First, it checks that semisplit admissible",
            "families do not leak into the tiny local-minimal cover corpus.  This",
            "is only finite evidence; the theorem still needs the symbolic",
            "local-minimality argument.",
            "",
            "Second, it distinguishes seed-only universal corridors from corridors",
            "that require transported edges.  In the audited size-2 and size-3",
            "local-minimal cover corpus, every output-kernel universal closure has",
            "stable depth `0`.  On the bi-free side, the only universal output",
            "corridors are the already tagged involutive rows.  This does not close",
            "the universal coordinate-kernel branch, but it makes the next lemma",
            "more precise: a proof should first handle seed-only universal",
            "coordinate-kernel corridors symbolically, while a counterexample",
            "search should look for a transported-depth corridor or a seed-only",
            "corridor with residual holonomy outside the known measurable",
            "branches.",
            "",
        ]
    )
    OUT_MD.write_text("\n".join(lines), encoding="utf-8")


def main():
    report = {
        "size_2_exhaustive": scan_size(2),
        "size_3_exhaustive": scan_size(3),
    }
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    write_markdown(report)
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
