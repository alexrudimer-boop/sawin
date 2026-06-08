"""Audit actual pure-kernel monodromy for linear F3 skew-over-flip rows."""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(TOOLS))

from run_linear_f3_skew_flip_completion_audit import (  # noqa: E402
    GL2,
    is_involutive_indices,
    is_nondegenerate as table_is_nondegenerate,
    quadruple_is_ybe,
    table_from_indices,
)
from run_linear_f3_skew_flip_monolith_audit import (  # noqa: E402
    meet_partitions,
    solution_from_table,
)
from ybe_domination import (  # noqa: E402
    congruences,
    contextual_completion_data,
    equality_congruence,
    identity_extension_rack_solution,
    identity_extension_summary,
    quotient_solution,
)
from ybe_domination.braid_laws import pure_braid_generator  # noqa: E402
from ybe_domination.finite_group import (  # noqa: E402
    compose_permutations,
    invert_permutation,
)
from ybe_domination.residual import (  # noqa: E402
    action_permutation,
    permutation_order,
)

OUT_JSON = ROOT / "proofs" / "linear_f3_skew_flip_pure_kernel_monodromy_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_skew_flip_pure_kernel_monodromy_audit.md"


def degenerate_noninvolutive_rows():
    row_index = 0
    for indices in itertools.product(range(len(GL2)), repeat=4):
        if not quadruple_is_ybe(indices):
            continue
        table = table_from_indices(indices)
        if table_is_nondegenerate(table) or is_involutive_indices(indices):
            continue
        yield row_index, indices, table
        row_index += 1


def permutation_power(permutation: tuple[int, ...], exponent: int) -> tuple[int, ...]:
    out = tuple(range(len(permutation)))
    base = permutation
    while exponent:
        if exponent & 1:
            out = compose_permutations(base, out)
        base = compose_permutations(base, base)
        exponent //= 2
    return out


def is_identity_permutation(permutation: tuple[int, ...]) -> bool:
    return all(index == image for index, image in enumerate(permutation))


def row_context(row_index: int, indices: tuple[int, int, int, int], table):
    solution = solution_from_table(table)
    all_congruences = congruences(solution, max_size=7)
    equality = equality_congruence(solution.elements)
    nontrivial = [
        partition
        for partition in all_congruences
        if partition != equality
    ]
    monolith = meet_partitions(nontrivial)
    if monolith == equality or len(monolith) == 1:
        return None
    data = contextual_completion_data(solution)
    identity_summary = identity_extension_summary(data)
    if not identity_summary.identity_extension_witnesses_active_lifts:
        return {
            "row_index": row_index,
            "matrix_indices": list(indices),
            "skipped_reason": "identity-extension contextual rack certificate failed",
        }
    quotient = quotient_solution(solution, monolith).quotient
    contextual_rack = identity_extension_rack_solution(data)
    return {
        "row_index": row_index,
        "matrix_indices": list(indices),
        "matrices": [list(GL2[index]) for index in indices],
        "solution": solution,
        "monolith": monolith,
        "quotient": quotient,
        "contextual_data": data,
        "contextual_rack": contextual_rack,
    }


def two_strand_audit(context: dict) -> dict:
    word = pure_braid_generator(1, 2)
    quotient_perm = action_permutation(context["quotient"], 2, word)
    context_perm = action_permutation(context["contextual_rack"], 2, word)
    x_perm = action_permutation(context["solution"], 2, word)
    quotient_order = permutation_order(quotient_perm)
    context_order = permutation_order(context_perm)
    x_order = permutation_order(x_perm)
    detector_order = math.lcm(quotient_order, context_order)
    x_kernel_perm = permutation_power(x_perm, detector_order)
    return {
        "row_index": context["row_index"],
        "matrix_indices": context["matrix_indices"],
        "contextual_class_count": context["contextual_data"].class_count,
        "monolith_block_sizes": sorted(len(block) for block in context["monolith"]),
        "quotient_class_count": len(context["monolith"]),
        "pure_generator": "A_1_2",
        "quotient_order": quotient_order,
        "contextual_rack_order": context_order,
        "x_order": x_order,
        "detector_order_lcm": detector_order,
        "x_action_trivial_on_cyclic_detector_kernel": is_identity_permutation(
            x_kernel_perm
        ),
    }


def exact_three_strand_joint_closure(
    context: dict,
    *,
    max_image_size: int,
) -> dict:
    generators = []
    for i, j in itertools.combinations(range(1, 4), 2):
        word = pure_braid_generator(i, j)
        generators.append(
            {
                "label": f"A_{i}_{j}",
                "quotient": action_permutation(context["quotient"], 3, word),
                "context": action_permutation(context["contextual_rack"], 3, word),
                "x": action_permutation(context["solution"], 3, word),
            }
        )

    quotient_identity = tuple(range(len(generators[0]["quotient"])))
    context_identity = tuple(range(len(generators[0]["context"])))
    x_identity = tuple(range(len(generators[0]["x"])))

    symmetric_generators = []
    generator_orders = []
    for generator in generators:
        generator_orders.append(
            {
                "label": generator["label"],
                "quotient_order": permutation_order(generator["quotient"]),
                "contextual_rack_order": permutation_order(generator["context"]),
                "x_order": permutation_order(generator["x"]),
            }
        )
        symmetric_generators.append(
            (
                generator["quotient"],
                generator["context"],
                generator["x"],
                generator["label"],
            )
        )
        symmetric_generators.append(
            (
                invert_permutation(generator["quotient"]),
                invert_permutation(generator["context"]),
                invert_permutation(generator["x"]),
                f"{generator['label']}^-1",
            )
        )

    identity_key = (quotient_identity, context_identity, x_identity)
    seen = {identity_key: ()}
    queue = deque([(quotient_identity, context_identity, x_identity, ())])
    first_kernel_witness = None
    truncated = False

    while queue:
        quotient_perm, context_perm, x_perm, word = queue.popleft()
        for gen_quotient, gen_context, gen_x, label in symmetric_generators:
            next_quotient = compose_permutations(gen_quotient, quotient_perm)
            next_context = compose_permutations(gen_context, context_perm)
            next_x = compose_permutations(gen_x, x_perm)
            key = (next_quotient, next_context, next_x)
            if key in seen:
                continue
            next_word = word + (label,)
            seen[key] = next_word
            queue.append((next_quotient, next_context, next_x, next_word))
            if (
                next_quotient == quotient_identity
                and next_context == context_identity
                and next_x != x_identity
                and first_kernel_witness is None
            ):
                first_kernel_witness = next_word
            if len(seen) >= max_image_size:
                truncated = bool(queue)
                queue.clear()
                break

    if not truncated:
        kernel_nontrivial = any(
            quotient_perm == quotient_identity
            and context_perm == context_identity
            and x_perm != x_identity
            for quotient_perm, context_perm, x_perm in seen
        )
    else:
        kernel_nontrivial = first_kernel_witness is not None

    return {
        "row_index": context["row_index"],
        "matrix_indices": context["matrix_indices"],
        "contextual_class_count": context["contextual_data"].class_count,
        "monolith_block_sizes": sorted(len(block) for block in context["monolith"]),
        "quotient_class_count": len(context["monolith"]),
        "arity": 3,
        "pure_generator_orders": generator_orders,
        "joint_image_size": len(seen),
        "max_image_size": max_image_size,
        "truncated": truncated,
        "detector_kernel_x_nontrivial": kernel_nontrivial,
        "first_kernel_witness_word": (
            None if first_kernel_witness is None else list(first_kernel_witness)
        ),
    }


def run_audit(max_image_size: int) -> dict:
    contexts = []
    skipped_contexts = []
    source_row_count = 0
    for row_index, indices, table in degenerate_noninvolutive_rows():
        source_row_count += 1
        context = row_context(row_index, indices, table)
        if context is None:
            continue
        if "skipped_reason" in context:
            skipped_contexts.append(context)
            continue
        contexts.append(context)

    two_rows = [two_strand_audit(context) for context in contexts]
    two_nontrivial = [
        row
        for row in two_rows
        if not row["x_action_trivial_on_cyclic_detector_kernel"]
    ]

    min_contextual_class_count = min(
        context["contextual_data"].class_count
        for context in contexts
    )
    selected_three_contexts = [
        context
        for context in contexts
        if context["contextual_data"].class_count == min_contextual_class_count
    ]
    three_rows = [
        exact_three_strand_joint_closure(
            context,
            max_image_size=max_image_size,
        )
        for context in selected_three_contexts
    ]
    three_nontrivial = [
        row
        for row in three_rows
        if row["detector_kernel_x_nontrivial"]
    ]
    three_truncated = [
        row
        for row in three_rows
        if row["truncated"]
    ]

    distribution = Counter(
        (
            context["contextual_data"].class_count,
            tuple(sorted(len(block) for block in context["monolith"])),
        )
        for context in contexts
    )
    report = {
        "family": "linear_f3_skew_over_flip_degenerate_noninvolutive",
        "detector_model": (
            "monolith quotient action plus identity-extension contextual rack"
        ),
        "row_count": source_row_count,
        "subdirectly_irreducible_proper_quotient_rows": len(contexts),
        "skipped_context_count": len(skipped_contexts),
        "skipped_contexts": skipped_contexts,
        "two_strand": {
            "audited_rows": len(two_rows),
            "detector_kernel_x_nontrivial_count": len(two_nontrivial),
            "nontrivial_examples": two_nontrivial[:8],
        },
        "three_strand": {
            "selection_rule": "all rows with minimal contextual_class_count",
            "minimal_contextual_class_count": min_contextual_class_count,
            "audited_rows": len(three_rows),
            "detector_kernel_x_nontrivial_count": len(three_nontrivial),
            "truncated_count": len(three_truncated),
            "nontrivial_examples": three_nontrivial[:4],
            "truncated_examples": three_truncated[:4],
            "rows": three_rows,
        },
        "subdirect_distribution": [
            {
                "case_count": count,
                "contextual_class_count": key[0],
                "monolith_block_sizes": list(key[1]),
            }
            for key, count in sorted(distribution.items(), key=lambda item: item[0])
        ],
    }
    report["all_claimed_checks_passed"] = (
        report["row_count"] == 144
        and
        report["subdirectly_irreducible_proper_quotient_rows"] == 64
        and report["skipped_context_count"] == 0
        and report["two_strand"]["detector_kernel_x_nontrivial_count"] == 0
        and report["three_strand"]["audited_rows"] == 4
        and report["three_strand"]["detector_kernel_x_nontrivial_count"] == 0
        and report["three_strand"]["truncated_count"] == 0
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Pure-Kernel Monodromy Audit",
        "",
        "This generated audit tests the corrected monolith obstruction against",
        "actual pure detector-kernel monodromy in the 144 degenerate",
        "non-involutive six-point linear skew-over-flip rows.",
        "",
        "The detector used for the audit is stronger than the abstract detector",
        "in the minimal-counterexample theorem: it is the monolith quotient",
        "action itself, together with the identity-extension contextual rack.",
        "Therefore triviality here is evidence against actual pure-kernel",
        "monodromy in these finite test cases, while a nontrivial element would",
        "only be a candidate for a rack-detector witness.",
        "",
        "## Summary",
        "",
        f"- subdirect rows audited: "
        f"`{report['subdirectly_irreducible_proper_quotient_rows']}`;",
        f"- skipped contextual completions: `{report['skipped_context_count']}`;",
        "- two-strand pure detector-kernel X-motion count: "
        f"`{report['two_strand']['detector_kernel_x_nontrivial_count']}`;",
        "- three-strand rows audited: "
        f"`{report['three_strand']['audited_rows']}` "
        f"(minimal contextual class count "
        f"`{report['three_strand']['minimal_contextual_class_count']}`);",
        "- three-strand pure detector-kernel X-motion count: "
        f"`{report['three_strand']['detector_kernel_x_nontrivial_count']}`;",
        f"- three-strand truncations: `{report['three_strand']['truncated_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "## Three-Strand Exact Closures",
        "",
        "| row | matrices | P classes | joint image | kernel X-motion | truncated |",
        "|---:|---|---:|---:|---|---|",
    ]
    for row in report["three_strand"]["rows"]:
        lines.append(
            "| {row_index} | {matrix_indices} | {contextual_class_count} | "
            "{joint_image_size} | {detector_kernel_x_nontrivial} | "
            "{truncated} |".format(**row)
        )
    lines.extend(
        [
            "",
            "## Distribution",
            "",
            "| cases | P classes | monolith block sizes |",
            "|---:|---:|---|",
        ]
    )
    for row in report["subdirect_distribution"]:
        lines.append(
            "| {case_count} | {contextual_class_count} | "
            "{monolith_block_sizes} |".format(**row)
        )
    lines.extend(
        [
            "",
            "## Consequence",
            "",
            "All 64 subdirectly irreducible proper-quotient rows have trivial",
            "two-strand pure kernel against the monolith quotient plus contextual",
            "rack detector.  The four smallest contextual quotients also have exact",
            "three-strand joint image size 216 and no detector-kernel X-motion.",
            "",
            "This does not prove domination.  It narrows the current obstruction:",
            "the formal monolith contextual collisions seen earlier are not",
            "automatically realized by small-arity pure detector-kernel monodromy",
            "in this six-point family.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-image-size", type=int, default=10_000)
    args = parser.parse_args()
    report = run_audit(args.max_image_size)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 pure-kernel monodromy audit failed")
    print("OK linear F3 pure-kernel monodromy audit")
    print(
        "subdirect rows "
        f"{report['subdirectly_irreducible_proper_quotient_rows']}"
    )
    print(
        "n2 kernel X-motion "
        f"{report['two_strand']['detector_kernel_x_nontrivial_count']}"
    )
    print(
        "n3 kernel X-motion "
        f"{report['three_strand']['detector_kernel_x_nontrivial_count']}"
    )


if __name__ == "__main__":
    main()
