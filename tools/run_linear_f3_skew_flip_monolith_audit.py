"""Audit monolith J-separation for linear F3 skew-over-flip hard rows."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import Counter
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(TOOLS))

from run_linear_f3_skew_flip_completion_audit import (  # noqa: E402
    COLORS,
    GL2,
    quadruple_is_ybe,
    table_from_indices,
    is_nondegenerate as table_is_nondegenerate,
    is_involutive_indices,
)
from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    common_refinement,
    congruences,
    contextual_completion_data,
    equality_congruence,
    generated_partition,
    refines,
    relative_contextual_separation_summary,
)

OUT_JSON = ROOT / "proofs" / "linear_f3_skew_flip_monolith_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_skew_flip_monolith_audit.md"


def solution_from_table(table: tuple[tuple[int, int], ...]) -> FiniteBraidedSet:
    elements = tuple(COLORS)
    size = len(elements)
    return FiniteBraidedSet(
        elements,
        {
            (x, y): table[size * x + y]
            for x in elements
            for y in elements
        },
    )


def meet_partitions(partitions):
    current = partitions[0]
    for partition in partitions[1:]:
        current = common_refinement(current, partition)
    return current


def partition_labels(partition) -> dict[int, int]:
    return {
        element: block_index
        for block_index, block in enumerate(partition)
        for element in block
    }


def least_congruence_containing_pairs(all_congruences, elements, pairs):
    seed = generated_partition(elements, pairs)
    containing = [
        partition
        for partition in all_congruences
        if refines(seed, partition)
    ]
    return meet_partitions(containing)


def degenerate_noninvolutive_rows():
    for indices in itertools.product(range(len(GL2)), repeat=4):
        if not quadruple_is_ybe(indices):
            continue
        table = table_from_indices(indices)
        if table_is_nondegenerate(table) or is_involutive_indices(indices):
            continue
        yield indices, table


def run_audit(max_vertices: int) -> dict:
    rows = []
    distribution = Counter()
    subdirect_count = 0
    braided_simple_count = 0
    monolith_separating_count = 0
    monolith_collision_count = 0
    monolith_skip_count = 0
    generated_mismatch_failures = []

    for row_index, (indices, table) in enumerate(degenerate_noninvolutive_rows()):
        solution = solution_from_table(table)
        data = contextual_completion_data(solution)
        all_congruences = congruences(solution, max_size=7)
        equality = equality_congruence(solution.elements)
        nontrivial = [
            partition
            for partition in all_congruences
            if partition != equality
        ]
        nontrivial_proper = [
            partition
            for partition in nontrivial
            if len(partition) != 1
        ]
        if not nontrivial_proper:
            braided_simple_count += 1

        monolith = meet_partitions(nontrivial)
        monolith_nontrivial = monolith != equality
        monolith_payload = None
        generated_by_mismatches = None
        separation_payload = None

        if monolith_nontrivial:
            subdirect_count += 1
            labels = partition_labels(monolith)
            separation = relative_contextual_separation_summary(
                data,
                labels,
                max_vertices=max_vertices,
            )
            separation_payload = {
                **asdict(separation),
                "proves_all_arity_injective": (
                    separation.proves_all_arity_injective
                ),
            }
            if not separation.checked:
                monolith_skip_count += 1
            elif separation.collision_found:
                monolith_collision_count += 1
                mismatch_pairs = [
                    (solution.elements[left], solution.elements[right])
                    for left, right in separation.collision_path_indices
                    if left != right
                ]
                generated = least_congruence_containing_pairs(
                    all_congruences,
                    solution.elements,
                    mismatch_pairs,
                )
                generated_by_mismatches = generated == monolith
                if not generated_by_mismatches:
                    generated_mismatch_failures.append(
                        {
                            "row_index": row_index,
                            "matrix_indices": list(indices),
                            "mismatch_pairs": [list(pair) for pair in mismatch_pairs],
                        }
                    )
            else:
                monolith_separating_count += 1

            monolith_payload = {
                "block_sizes": sorted(len(block) for block in monolith),
                "quotient_class_count": len(monolith),
                "relative_separation": separation_payload,
                "collision_mismatches_generate_monolith": generated_by_mismatches,
            }

        distribution[
            (
                len(nontrivial_proper),
                tuple(sorted(len(block) for block in monolith)),
                monolith_nontrivial,
                (
                    None
                    if separation_payload is None
                    else separation_payload["collision_found"]
                ),
                (
                    None
                    if separation_payload is None
                    else not separation_payload["checked"]
                ),
            )
        ] += 1

        rows.append(
            {
                "row_index": row_index,
                "matrix_indices": list(indices),
                "matrices": [list(GL2[index]) for index in indices],
                "congruence_count": len(all_congruences),
                "nontrivial_proper_congruence_count": len(nontrivial_proper),
                "monolith_is_nontrivial": monolith_nontrivial,
                "monolith": monolith_payload,
                "contextual_class_count": data.class_count,
                "left_monoid_size": len(data.left_monoid),
                "right_monoid_size": len(data.right_monoid),
            }
        )

    distribution_rows = [
        {
            "case_count": count,
            "nontrivial_proper_congruence_count": key[0],
            "monolith_block_sizes": list(key[1]),
            "monolith_is_nontrivial": key[2],
            "monolith_collision_found": key[3],
            "monolith_check_skipped": key[4],
        }
        for key, count in sorted(distribution.items(), key=lambda item: (-item[1], item[0]))
    ]
    report = {
        "family": "linear_f3_skew_over_flip_degenerate_noninvolutive",
        "row_count": len(rows),
        "max_vertices": max_vertices,
        "braided_simple_count": braided_simple_count,
        "subdirectly_irreducible_count": subdirect_count,
        "monolith_separating_count": monolith_separating_count,
        "monolith_collision_count": monolith_collision_count,
        "monolith_skip_count": monolith_skip_count,
        "collision_mismatch_generation_failure_count": len(
            generated_mismatch_failures
        ),
        "collision_mismatch_generation_failures": generated_mismatch_failures[:8],
        "distribution": distribution_rows,
        "rows": rows,
        "all_claimed_checks_passed": (
            len(rows) == 144
            and braided_simple_count == 0
            and monolith_skip_count == 0
            and not generated_mismatch_failures
        ),
    }
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Skew-Over-Flip Monolith Audit",
        "",
        "This generated audit applies the minimal-counterexample monolith",
        "criterion to the 144 degenerate non-involutive six-point linear",
        "skew-over-flip rows.",
        "",
        "## Summary",
        "",
        f"- rows checked: `{report['row_count']}`;",
        f"- braided-simple rows: `{report['braided_simple_count']}`;",
        "- subdirectly irreducible rows with nontrivial monolith: "
        f"`{report['subdirectly_irreducible_count']}`;",
        "- monolith J-separating rows: "
        f"`{report['monolith_separating_count']}`;",
        "- monolith J-collision rows: "
        f"`{report['monolith_collision_count']}`;",
        f"- monolith check skips: `{report['monolith_skip_count']}`;",
        "- collision mismatch-generation failures: "
        f"`{report['collision_mismatch_generation_failure_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "Rows whose monolith has a formal contextual collision are checked",
        "further: the mismatch pairs from the finite path generate the",
        "monolith as a braided congruence.",
        "",
        "## Distribution",
        "",
        "| cases | proper congruences | monolith blocks | nontrivial monolith | collision | skipped |",
        "|---:|---:|---|---|---|---|",
    ]
    for row in report["distribution"]:
        lines.append(
            "| {case_count} | {nontrivial_proper_congruence_count} | "
            "{monolith_block_sizes} | {monolith_is_nontrivial} | "
            "{monolith_collision_found} | {monolith_check_skipped} |".format(**row)
        )
    lines.extend(
        [
            "",
            "## Consequence",
            "",
            "None of these 144 degenerate non-involutive six-point rows is",
            "braided-simple.  The subdirectly irreducible rows split between",
            "formal monolith J-separation and formal monolith J-collision.",
            "This is still not a Sawin counterexample: a true minimal",
            "counterexample requires a Brunnian-realized detector-kernel",
            "collision, not merely a formal contextual collision.",
        ]
    )
    if report["collision_mismatch_generation_failures"]:
        lines.extend(["", "## Mismatch Generation Failures", "", "```json"])
        lines.append(
            json.dumps(
                report["collision_mismatch_generation_failures"],
                indent=2,
            )
        )
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-vertices", type=int, default=2_000_000)
    args = parser.parse_args()
    report = run_audit(args.max_vertices)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 skew-over-flip monolith audit failed")
    print("OK linear F3 skew-over-flip monolith audit")
    print(f"rows {report['row_count']}")
    print(f"subdirectly irreducible {report['subdirectly_irreducible_count']}")
    print(f"monolith collisions {report['monolith_collision_count']}")


if __name__ == "__main__":
    main()
