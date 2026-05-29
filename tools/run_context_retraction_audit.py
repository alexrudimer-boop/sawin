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
    congruences,
    direct_product_witness,
    context_retraction_audit,
    interval_covers,
    product_permutation_witness,
    solution_from_local_interval,
    solution_table_signature,
)


OUT = ROOT / "proofs" / "context_retraction_audit.json"


def partition_signature(partition):
    return [sorted(repr(element) for element in block) for block in partition]


def family_signature(interval, family):
    return {
        repr(color): partition_signature(family[color])
        for color in interval.colors
    }


def table_signature(solution):
    return [list(value) for value in solution_table_signature(solution)]


def scan_size(size):
    counts = Counter()
    initial_counts = Counter()
    coretraction_counts = Counter()
    combined_counts = Counter()
    combined_branch_tag_counts = Counter()
    local_minimal_count = 0
    max_stable_depth = 0
    max_coretraction_stable_depth = 0
    initial_admissible_count = 0
    coretraction_initial_admissible_count = 0
    universal_product_permutation_count = 0
    universal_direct_product_count = 0
    equality_known_branch_counts = Counter()
    bifree_known_branch_counts = Counter()
    non_admissible = []
    mixed = []
    examples_by_kind = {}
    for solution_index, solution in enumerate(all_bijection_solutions(size)):
        lattice = congruences(solution)
        for lower, upper in interval_covers(lattice):
            interval = CongruenceInterval(solution, lower, upper).local_interval()
            if not interval.is_local_minimal():
                continue
            local_minimal_count += 1
            audit = context_retraction_audit(interval)
            coretraction = context_coretraction_audit(interval)
            counts[(audit.kind, audit.admissible)] += 1
            coretraction_counts[(coretraction.kind, coretraction.admissible)] += 1
            combined_counts[(audit.kind, coretraction.kind)] += 1
            if audit.initial_admissible:
                initial_admissible_count += 1
            if coretraction.initial_admissible:
                coretraction_initial_admissible_count += 1
            initial_kind = "initial_" + (
                "equality"
                if all(
                    len(audit.initial_family[color]) == len(interval.fibres[color])
                    for color in interval.colors
                )
                else "non_equality"
            )
            initial_counts[initial_kind] += 1
            max_stable_depth = max(max_stable_depth, audit.stable_depth)
            max_coretraction_stable_depth = max(
                max_coretraction_stable_depth, coretraction.stable_depth
            )
            interval_total = solution_from_local_interval(interval).total
            tags = branch_tags(interval_total)
            combined_branch_tag_counts[(audit.kind, coretraction.kind, tags)] += 1
            if audit.kind == "equality":
                equality_known_branch_counts[tags] += 1
            if audit.kind == "equality" and coretraction.kind == "equality":
                bifree_known_branch_counts[tags] += 1
            if audit.kind == "universal" and product_permutation_witness(interval) is not None:
                universal_product_permutation_count += 1
            if (
                coretraction.kind == "universal"
                and direct_product_witness(interval) is not None
            ):
                universal_direct_product_count += 1
            if audit.kind not in examples_by_kind:
                examples_by_kind[audit.kind] = {
                    "solution_index": solution_index,
                    "original_table_values": table_signature(solution),
                    "lower_partition": partition_signature(lower),
                    "upper_partition": partition_signature(upper),
                    "stable_depth": audit.stable_depth,
                    "branch_tags": list(tags),
                    "initial_family": family_signature(interval, audit.initial_family),
                    "stable_family": family_signature(interval, audit.stable_family),
                }
            if not audit.admissible and len(non_admissible) < 5:
                non_admissible.append(examples_by_kind[audit.kind])
            if audit.kind not in ("equality", "universal") and len(mixed) < 5:
                mixed.append(examples_by_kind[audit.kind])
    return {
        "size": size,
        "local_minimal_cover_count": local_minimal_count,
        "stable_kind_counts": {
            f"{kind}|admissible={admissible}": count
            for (kind, admissible), count in sorted(counts.items())
        },
        "coretraction_stable_kind_counts": {
            f"{kind}|admissible={admissible}": count
            for (kind, admissible), count in sorted(coretraction_counts.items())
        },
        "combined_retraction_coretraction_counts": {
            f"retraction={retraction}|coretraction={coretraction}": count
            for (retraction, coretraction), count in sorted(combined_counts.items())
        },
        "combined_branch_tag_counts": {
            f"retraction={retraction}|coretraction={coretraction}|tags={'+'.join(tags) if tags else '(untagged)'}": count
            for (retraction, coretraction, tags), count in sorted(
                combined_branch_tag_counts.items(), key=lambda item: repr(item[0])
            )
        },
        "initial_kind_counts": dict(sorted(initial_counts.items())),
        "max_stable_depth": max_stable_depth,
        "max_coretraction_stable_depth": max_coretraction_stable_depth,
        "initial_admissible_count": initial_admissible_count,
        "coretraction_initial_admissible_count": coretraction_initial_admissible_count,
        "universal_product_permutation_count": universal_product_permutation_count,
        "universal_direct_product_count": universal_direct_product_count,
        "equality_branch_tag_counts": {
            " + ".join(tags) if tags else "(untagged)": count
            for tags, count in sorted(equality_known_branch_counts.items(), key=lambda item: repr(item[0]))
        },
        "bifree_branch_tag_counts": {
            " + ".join(tags) if tags else "(untagged)": count
            for tags, count in sorted(bifree_known_branch_counts.items(), key=lambda item: repr(item[0]))
        },
        "non_admissible_examples": non_admissible,
        "mixed_examples": mixed,
        "examples_by_kind": examples_by_kind,
    }


def main():
    report = {
        "size_2_exhaustive": scan_size(2),
        "size_3_exhaustive": scan_size(3),
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
