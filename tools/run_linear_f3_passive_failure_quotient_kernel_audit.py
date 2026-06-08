"""Check small-arity quotient-kernel motion for passive-failure F3 rows."""

from __future__ import annotations

import itertools
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(TOOLS))

from run_linear_f3_skew_flip_completion_audit import (  # noqa: E402
    table_from_indices,
)
from run_linear_f3_skew_flip_monolith_audit import (  # noqa: E402
    meet_partitions,
    solution_from_table,
)
from ybe_domination import (  # noqa: E402
    congruences,
    equality_congruence,
    quotient_solution,
)

SOURCE_JSON = ROOT / "proofs" / "linear_f3_collision_quotient_invariant_audit.json"
OUT_JSON = ROOT / "proofs" / "linear_f3_passive_failure_quotient_kernel_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_passive_failure_quotient_kernel_audit.md"


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(right)))


def invert(perm: tuple[int, ...]) -> tuple[int, ...]:
    inverse = [0] * len(perm)
    for index, image in enumerate(perm):
        inverse[image] = index
    return tuple(inverse)


def generator_permutation(solution, arity: int, index: int) -> tuple[int, ...]:
    tuples = list(itertools.product(solution.elements, repeat=arity))
    lookup = {tup: position for position, tup in enumerate(tuples)}
    return tuple(
        lookup[solution.apply_R_at(tup, index)]
        for tup in tuples
    )


def kernel_motion_summary(solution, quotient, arity: int, max_size: int) -> dict:
    x_generators = [
        generator_permutation(solution, arity, index)
        for index in range(arity - 1)
    ]
    z_generators = [
        generator_permutation(quotient, arity, index)
        for index in range(arity - 1)
    ]
    x_identity = tuple(range(len(x_generators[0])))
    z_identity = tuple(range(len(z_generators[0])))
    generators = []
    for x_generator, z_generator in zip(x_generators, z_generators):
        generators.append((x_generator, z_generator))
        generators.append((invert(x_generator), invert(z_generator)))

    seen = {(x_identity, z_identity)}
    queue = deque([(x_identity, z_identity)])
    while queue:
        x_current, z_current = queue.popleft()
        for x_generator, z_generator in generators:
            x_next = compose(x_generator, x_current)
            z_next = compose(z_generator, z_current)
            if (x_next, z_next) in seen:
                continue
            if z_next == z_identity and x_next != x_identity:
                return {
                    "arity": arity,
                    "checked": True,
                    "truncated": False,
                    "combined_image_size_before_witness": len(seen) + 1,
                    "quotient_kernel_x_motion_found": True,
                }
            seen.add((x_next, z_next))
            queue.append((x_next, z_next))
            if len(seen) > max_size:
                return {
                    "arity": arity,
                    "checked": False,
                    "truncated": True,
                    "combined_image_size_before_witness": len(seen),
                    "quotient_kernel_x_motion_found": None,
                }
    return {
        "arity": arity,
        "checked": True,
        "truncated": False,
        "combined_image_size": len(seen),
        "quotient_kernel_x_motion_found": False,
    }


def row_solution_and_quotient(matrix_indices: tuple[int, int, int, int]):
    solution = solution_from_table(table_from_indices(matrix_indices))
    all_congruences = congruences(solution, max_size=7)
    equality = equality_congruence(solution.elements)
    monolith = meet_partitions(
        [partition for partition in all_congruences if partition != equality]
    )
    quotient = quotient_solution(solution, monolith).quotient
    return solution, quotient


def run_audit(max_arity: int = 3, max_group_size: int = 2_000_000) -> dict:
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    passive_failure_rows = [
        row for row in source["rows"]
        if (
            row.get("quotient_invariant_certificate")
            and not row["quotient_invariant_certificate"]["certified"]
        )
    ]
    rows = []
    motion_rows = []
    truncations = []
    for row in passive_failure_rows:
        matrix_indices = tuple(row["matrix_indices"])
        solution, quotient = row_solution_and_quotient(matrix_indices)
        arity_summaries = [
            kernel_motion_summary(solution, quotient, arity, max_group_size)
            for arity in range(2, max_arity + 1)
        ]
        if any(item["quotient_kernel_x_motion_found"] for item in arity_summaries):
            motion_rows.append(row["row_index"])
        if any(item["truncated"] for item in arity_summaries):
            truncations.append(row["row_index"])
        rows.append(
            {
                "row_index": row["row_index"],
                "matrix_indices": row["matrix_indices"],
                "arity_summaries": arity_summaries,
            }
        )
    report = {
        "family": "linear_f3_skew_over_flip_passive_failure_rows",
        "source_artifact": str(SOURCE_JSON.relative_to(ROOT)),
        "passive_failure_row_count": len(passive_failure_rows),
        "max_arity": max_arity,
        "max_group_size": max_group_size,
        "quotient_kernel_x_motion_row_count": len(motion_rows),
        "quotient_kernel_x_motion_rows": motion_rows,
        "truncated_row_count": len(truncations),
        "truncated_rows": truncations,
        "rows": rows,
    }
    report["all_claimed_checks_passed"] = (
        report["passive_failure_row_count"] == 16
        and report["quotient_kernel_x_motion_row_count"] == 0
        and report["truncated_row_count"] == 0
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Passive-Failure Quotient-Kernel Audit",
        "",
        "This generated audit checks whether the `16` passive-failure rows",
        "from the quotient-invariant audit already have small-arity motion",
        "inside the kernel of their nondegenerate four-point monolith quotient.",
        "",
        "## Summary",
        "",
        f"- source artifact: `{report['source_artifact']}`;",
        f"- passive-failure rows: `{report['passive_failure_row_count']}`;",
        f"- arities checked: `2..{report['max_arity']}`;",
        "- rows with quotient-kernel `X`-motion: "
        f"`{report['quotient_kernel_x_motion_row_count']}`;",
        f"- truncated rows: `{report['truncated_row_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "## Interpretation",
        "",
        "No passive-failure row has quotient-kernel `X`-motion in arity `2`",
        "or `3`.  This is finite evidence only.  It says the passive",
        "transport failure is a real gap in the simple invariant, not yet an",
        "actual quotient-kernel braid witness.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_audit()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 passive-failure quotient-kernel audit failed")
    print("OK linear F3 passive-failure quotient-kernel audit")
    print(f"passive-failure rows {report['passive_failure_row_count']}")
    print(
        "quotient-kernel X-motion rows "
        f"{report['quotient_kernel_x_motion_row_count']}"
    )


if __name__ == "__main__":
    main()
