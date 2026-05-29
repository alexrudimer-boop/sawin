import json
import sys
from collections import Counter
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    all_bijection_solutions,
    branch_tags,
    pure_generator_order_profile,
    pure_subgroup_growth_profile,
)
from run_linear_f2_audit import linear_solution, mat_rank  # noqa: E402


OUT = ROOT / "proofs" / "pure_power_growth_audit.json"


def row_to_dict(row):
    return {
        "braid_index": row.braid_index,
        "tuple_count": row.tuple_count,
        "generator_orders": list(row.generator_orders),
        "max_order": row.max_order,
    }


def growth_row_to_dict(row):
    return {
        "braid_index": row.braid_index,
        "tuple_count": row.tuple_count,
        "generator_count": row.generator_count,
        "subgroup_size": row.subgroup_size,
        "subgroup_exponent": row.subgroup_exponent,
        "truncated": row.truncated,
    }


def summarize_order_profiles(solutions, max_q):
    maximum = 0
    by_tags = Counter()
    examples = []
    for index, solution in enumerate(solutions):
        profile = pure_generator_order_profile(solution, max_q=max_q)
        solution_max = max(row.max_order for row in profile)
        maximum = max(maximum, solution_max)
        tags = branch_tags(solution)
        by_tags[(solution_max, tags)] += 1
        if len(examples) < 8 or solution_max > min(example["max_order"] for example in examples):
            examples.append(
                {
                    "solution_index": index,
                    "max_order": solution_max,
                    "branch_tags": list(tags),
                    "profile": [row_to_dict(row) for row in profile],
                }
            )
            examples = sorted(examples, key=lambda item: item["max_order"], reverse=True)[:8]
    return {
        "solution_count": len(solutions),
        "max_q": max_q,
        "maximum_pure_generator_order": maximum,
        "max_order_branch_tag_counts": {
            f"max_order={order}|tags={'+'.join(tags) if tags else '(untagged)'}": count
            for (order, tags), count in sorted(by_tags.items(), key=lambda item: repr(item[0]))
        },
        "top_examples": examples,
    }


def linear_f2_solutions():
    rows = tuple(product((0, 1), repeat=4))
    out = []
    for matrix in product(rows, repeat=4):
        if mat_rank(matrix) != 4:
            continue
        solution = linear_solution(matrix, 2)
        if solution.is_ybe():
            out.append(solution)
    return out


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


def main():
    size2 = list(all_bijection_solutions(2))
    size3 = list(all_bijection_solutions(3))
    linear = linear_f2_solutions()
    candidate = size3_commutator_candidate()
    report = {
        "whole_size_2": summarize_order_profiles(size2, max_q=6),
        "whole_size_3": summarize_order_profiles(size3, max_q=6),
        "linear_f2_dimension_2": summarize_order_profiles(linear, max_q=5),
        "size3_commutator_candidate_pure_subgroup_growth": [
            growth_row_to_dict(row)
            for row in pure_subgroup_growth_profile(
                candidate,
                max_q=5,
                max_subgroup_size=5000,
            )
        ],
    }
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
