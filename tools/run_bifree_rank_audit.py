import json
import sys
from collections import Counter
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    CongruenceInterval,
    all_bijection_solutions,
    branch_tags,
    coordinate_kernel_seed_pairs,
    context_coretraction_audit,
    context_retraction_audit,
    congruences,
    generated_admissible_congruence_audit,
    interval_covers,
    solution_from_local_interval,
    solution_table_signature,
)
from ybe_domination.local_interval import canonical_partition  # noqa: E402


OUT_JSON = ROOT / "proofs" / "bifree_rank_audit.json"
OUT_MD = ROOT / "proofs" / "bifree_rank_audit.md"


def table_signature(solution):
    return [list(value) for value in solution_table_signature(solution)]


def kernel_partition(domain, values_by_input):
    fibres = {}
    for item in domain:
        fibres.setdefault(values_by_input[item], []).append(item)
    return canonical_partition(fibres.values())


def kernel_shape(partition):
    return tuple(sorted(len(block) for block in partition))


def add_kernel_profile(profile, name, domain, values_by_input):
    partition = kernel_partition(domain, values_by_input)
    profile[name]["ranks"].append(len(partition))
    profile[name]["shapes"].append(kernel_shape(partition))
    profile[name]["partitions"].add(
        tuple(tuple(sorted(repr(item) for item in block)) for block in partition)
    )


def summarize_kernel_profile(profile):
    return {
        name: {
            "ranks": sorted(set(data["ranks"])),
            "kernel_shapes": sorted(set(data["shapes"])),
            "distinct_kernel_count": len(data["partitions"]),
        }
        for name, data in profile.items()
    }


def rank_profile(interval):
    profile = {
        "left_output": {"ranks": [], "shapes": [], "partitions": set()},
        "right_output": {"ranks": [], "shapes": [], "partitions": set()},
        "right_input_first_output": {"ranks": [], "shapes": [], "partitions": set()},
        "left_input_second_output": {"ranks": [], "shapes": [], "partitions": set()},
    }
    for a, b in product(interval.colors, repeat=2):
        for x in interval.fibres[a]:
            add_kernel_profile(
                profile,
                "left_output",
                interval.fibres[b],
                {
                    y: interval.T[(a, b, x, y)][0]
                    for y in interval.fibres[b]
                },
            )
            add_kernel_profile(
                profile,
                "left_input_second_output",
                interval.fibres[b],
                {
                    y: interval.T[(a, b, x, y)][1]
                    for y in interval.fibres[b]
                },
            )
        for y in interval.fibres[b]:
            add_kernel_profile(
                profile,
                "right_output",
                interval.fibres[a],
                {
                    x: interval.T[(a, b, x, y)][1]
                    for x in interval.fibres[a]
                },
            )
            add_kernel_profile(
                profile,
                "right_input_first_output",
                interval.fibres[a],
                {
                    x: interval.T[(a, b, x, y)][0]
                    for x in interval.fibres[a]
                },
            )
    summary = summarize_kernel_profile(profile)
    return {
        "left_output_ranks": summary["left_output"]["ranks"],
        "right_output_ranks": summary["right_output"]["ranks"],
        "right_input_first_output_ranks": summary["right_input_first_output"]["ranks"],
        "left_input_second_output_ranks": summary["left_input_second_output"]["ranks"],
        "left_output_kernel_shapes": summary["left_output"]["kernel_shapes"],
        "right_output_kernel_shapes": summary["right_output"]["kernel_shapes"],
        "right_input_first_output_kernel_shapes": summary[
            "right_input_first_output"
        ]["kernel_shapes"],
        "left_input_second_output_kernel_shapes": summary[
            "left_input_second_output"
        ]["kernel_shapes"],
        "left_output_distinct_kernel_count": summary["left_output"][
            "distinct_kernel_count"
        ],
        "right_output_distinct_kernel_count": summary["right_output"][
            "distinct_kernel_count"
        ],
        "right_input_first_output_distinct_kernel_count": summary[
            "right_input_first_output"
        ]["distinct_kernel_count"],
        "left_input_second_output_distinct_kernel_count": summary[
            "left_input_second_output"
        ]["distinct_kernel_count"],
    }


def scan_size(size):
    counts = Counter()
    bifree_counts = Counter()
    bifree_examples = []
    for solution_index, solution in enumerate(all_bijection_solutions(size)):
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            if not interval.is_local_minimal():
                continue
            retraction = context_retraction_audit(interval).kind
            coretraction = context_coretraction_audit(interval).kind
            total = solution_from_local_interval(interval).total
            tags = branch_tags(total)
            profile = rank_profile(interval)
            output_kernel_seeds = coordinate_kernel_seed_pairs(
                interval,
                include_coretraction_kernels=False,
            )
            all_coordinate_kernel_seeds = coordinate_kernel_seed_pairs(
                interval,
                include_coretraction_kernels=True,
            )
            output_kernel_audit = generated_admissible_congruence_audit(
                interval,
                output_kernel_seeds,
            )
            all_coordinate_kernel_audit = generated_admissible_congruence_audit(
                interval,
                all_coordinate_kernel_seeds,
            )
            output_kernel_closure_kind = output_kernel_audit.kind
            all_coordinate_kernel_closure_kind = all_coordinate_kernel_audit.kind
            output_kernel_seed_count = sum(
                len(pairs) for pairs in output_kernel_seeds.values()
            )
            all_coordinate_kernel_seed_count = sum(
                len(pairs) for pairs in all_coordinate_kernel_seeds.values()
            )
            key = (
                retraction,
                coretraction,
                tuple(tags),
                tuple(profile["left_output_ranks"]),
                tuple(profile["right_output_ranks"]),
                tuple(profile["right_input_first_output_ranks"]),
                tuple(profile["left_input_second_output_ranks"]),
                tuple(tuple(shape) for shape in profile["left_output_kernel_shapes"]),
                tuple(tuple(shape) for shape in profile["right_output_kernel_shapes"]),
                tuple(
                    tuple(shape)
                    for shape in profile["right_input_first_output_kernel_shapes"]
                ),
                tuple(
                    tuple(shape)
                    for shape in profile["left_input_second_output_kernel_shapes"]
                ),
                profile["left_output_distinct_kernel_count"],
                profile["right_output_distinct_kernel_count"],
                profile["right_input_first_output_distinct_kernel_count"],
                profile["left_input_second_output_distinct_kernel_count"],
                output_kernel_seed_count,
                all_coordinate_kernel_seed_count,
                output_kernel_closure_kind,
                all_coordinate_kernel_closure_kind,
                output_kernel_audit.stable_depth,
                all_coordinate_kernel_audit.stable_depth,
                tuple(count for _color, count in output_kernel_audit.edge_count_rows),
                tuple(count for _color, count in output_kernel_audit.diameter_rows),
            )
            counts[key] += 1
            if retraction == "equality" and coretraction == "equality":
                bifree_counts[key] += 1
                if len(bifree_examples) < 8:
                    bifree_examples.append(
                        {
                            "solution_index": solution_index,
                            "tags": tags,
                            "rank_profile": profile,
                            "output_kernel_seed_count": output_kernel_seed_count,
                            "all_coordinate_kernel_seed_count": all_coordinate_kernel_seed_count,
                            "output_kernel_closure_kind": output_kernel_closure_kind,
                            "all_coordinate_kernel_closure_kind": all_coordinate_kernel_closure_kind,
                            "output_kernel_stable_depth": output_kernel_audit.stable_depth,
                            "all_coordinate_kernel_stable_depth": all_coordinate_kernel_audit.stable_depth,
                            "output_kernel_edge_counts": [
                                [repr(color), count]
                                for color, count in output_kernel_audit.edge_count_rows
                            ],
                            "output_kernel_diameters": [
                                [repr(color), diameter]
                                for color, diameter in output_kernel_audit.diameter_rows
                            ],
                            "original_table_values": table_signature(solution),
                        }
                    )
    return {
        "size": size,
        "combined_rank_counts": [
            {
                "retraction": key[0],
                "coretraction": key[1],
                "tags": list(key[2]),
                "left_output_ranks": list(key[3]),
                "right_output_ranks": list(key[4]),
                "right_input_first_output_ranks": list(key[5]),
                "left_input_second_output_ranks": list(key[6]),
                "left_output_kernel_shapes": [list(shape) for shape in key[7]],
                "right_output_kernel_shapes": [list(shape) for shape in key[8]],
                "right_input_first_output_kernel_shapes": [
                    list(shape) for shape in key[9]
                ],
                "left_input_second_output_kernel_shapes": [
                    list(shape) for shape in key[10]
                ],
                "left_output_distinct_kernel_count": key[11],
                "right_output_distinct_kernel_count": key[12],
                "right_input_first_output_distinct_kernel_count": key[13],
                "left_input_second_output_distinct_kernel_count": key[14],
                "output_kernel_seed_count": key[15],
                "all_coordinate_kernel_seed_count": key[16],
                "output_kernel_closure_kind": key[17],
                "all_coordinate_kernel_closure_kind": key[18],
                "output_kernel_stable_depth": key[19],
                "all_coordinate_kernel_stable_depth": key[20],
                "output_kernel_edge_counts": list(key[21]),
                "output_kernel_diameters": list(key[22]),
                "count": count,
            }
            for key, count in sorted(counts.items(), key=lambda item: repr(item[0]))
        ],
        "bifree_rank_counts": [
            {
                "tags": list(key[2]),
                "left_output_ranks": list(key[3]),
                "right_output_ranks": list(key[4]),
                "right_input_first_output_ranks": list(key[5]),
                "left_input_second_output_ranks": list(key[6]),
                "left_output_kernel_shapes": [list(shape) for shape in key[7]],
                "right_output_kernel_shapes": [list(shape) for shape in key[8]],
                "right_input_first_output_kernel_shapes": [
                    list(shape) for shape in key[9]
                ],
                "left_input_second_output_kernel_shapes": [
                    list(shape) for shape in key[10]
                ],
                "left_output_distinct_kernel_count": key[11],
                "right_output_distinct_kernel_count": key[12],
                "right_input_first_output_distinct_kernel_count": key[13],
                "left_input_second_output_distinct_kernel_count": key[14],
                "output_kernel_seed_count": key[15],
                "all_coordinate_kernel_seed_count": key[16],
                "output_kernel_closure_kind": key[17],
                "all_coordinate_kernel_closure_kind": key[18],
                "output_kernel_stable_depth": key[19],
                "all_coordinate_kernel_stable_depth": key[20],
                "output_kernel_edge_counts": list(key[21]),
                "output_kernel_diameters": list(key[22]),
                "count": count,
            }
            for key, count in sorted(bifree_counts.items(), key=lambda item: repr(item[0]))
        ],
        "bifree_examples": bifree_examples,
    }


def write_markdown(report):
    lines = [
        "# Bi-free rank audit",
        "",
        "Date: 2026-05-28",
        "",
        "This generated audit records coordinate-map rank and kernel profiles for",
        "local-minimal congruence-cover intervals.  It is a candidate-discovery",
        "diagnostic only: it does not replace the required all-`n` residual",
        "detector proof.",
        "",
        "For a local table `T_{a,b}(x,y)=(u,v)`, the rank profile records:",
        "",
        "- ranks of `y -> u` for fixed left input `x`;",
        "- ranks of `x -> v` for fixed right input `y`;",
        "- ranks of `x -> u` for fixed right input `y`;",
        "- ranks of `y -> v` for fixed left input `x`.",
        "",
        "For each of these four coordinate-map families it also records the",
        "kernel-partition block-size shapes and the number of distinct kernel",
        "partitions seen in the interval.  These kernels are the Green-relevant",
        "data behind the rank diagnostic.",
        "",
        "Finally, it forms the least admissible congruence family generated by",
        "the nondegeneracy coordinate kernels, and again by all four coordinate",
        "kernel families.  In a local-minimal interval, any non-equality closure",
        "must be universal.  The audit records stable closure depth, generated",
        "edge counts, and fibre graph diameters for the nondegeneracy-kernel",
        "closure.",
        "",
    ]
    for key, scan in report.items():
        lines.extend([f"## {key}", ""])
        if not scan["bifree_rank_counts"]:
            lines.append("No bi-free local-minimal intervals.")
            lines.append("")
            continue
        lines.append("Bi-free rank-count rows:")
        lines.append("")
        for row in scan["bifree_rank_counts"]:
            tag_text = "+".join(row["tags"]) if row["tags"] else "(untagged)"
            lines.append(
                "- "
                f"tags `{tag_text}`, "
                f"left ranks `{row['left_output_ranks']}`, "
                f"right ranks `{row['right_output_ranks']}`, "
                f"input-first ranks `{row['right_input_first_output_ranks']}`, "
                f"input-second ranks `{row['left_input_second_output_ranks']}`: "
                f"`{row['count']}`."
            )
            lines.append(
                "  Kernel shapes "
                f"left `{row['left_output_kernel_shapes']}`, "
                f"right `{row['right_output_kernel_shapes']}`, "
                f"input-first `{row['right_input_first_output_kernel_shapes']}`, "
                f"input-second `{row['left_input_second_output_kernel_shapes']}`; "
                "distinct kernels "
                f"`({row['left_output_distinct_kernel_count']}, "
                f"{row['right_output_distinct_kernel_count']}, "
                f"{row['right_input_first_output_distinct_kernel_count']}, "
                f"{row['left_input_second_output_distinct_kernel_count']})`."
            )
            lines.append(
                "  Kernel-generated closures "
                f"output `{row['output_kernel_closure_kind']}` "
                f"from `{row['output_kernel_seed_count']}` seed pairs; "
                f"all-coordinate `{row['all_coordinate_kernel_closure_kind']}` "
                f"from `{row['all_coordinate_kernel_seed_count']}` seed pairs."
            )
            lines.append(
                "  Output-kernel corridor "
                f"depth `{row['output_kernel_stable_depth']}`, "
                f"edge counts `{row['output_kernel_edge_counts']}`, "
                f"diameters `{row['output_kernel_diameters']}`."
            )
        lines.append("")
    lines.extend(
        [
            "## Consequence",
            "",
            "In the exhaustive size-3 local-minimal cover corpus, every bi-free",
            "interval is already tagged as involutive, nondegenerate, or rack-type",
            "nondegenerate.  The rank profiles show no untagged intermediate-rank",
            "bi-free row in this corpus.  The kernel profiles separate the",
            "rank-collapsed involutive rows from the full-rank nondegenerate rows",
            "without producing a third primitive shape.  This supports the",
            "symbolic rank/Green target.  The kernel-generated closures make the",
            "fork explicit: no output-kernel seeds gives the nondegenerate branch,",
            "while nontrivial output kernels close to the universal family in the",
            "audited local-minimal rows.  The corridor depths and diameters give",
            "a concrete finite object to compare against Green kernel-block",
            "transport.  This remains finite candidate-search evidence only until",
            "the universal kernel-closure side is controlled symbolically.",
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
