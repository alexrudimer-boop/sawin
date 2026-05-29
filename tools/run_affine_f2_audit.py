import itertools
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_linear_f2_audit import mat_mul, mat_rank, matrix_signature  # noqa: E402
from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    LocalInterval,
    branch_tags,
    context_coretraction_audit,
    context_retraction_audit,
    coordinate_kernel_seed_pairs,
    direct_product_witness,
    generated_admissible_congruence_audit,
    product_permutation_witness,
)


OUT = ROOT / "proofs" / "affine_f2_audit.json"


def affine_solution(matrix, offset, dimension):
    elements = tuple(itertools.product((0, 1), repeat=dimension))
    table = {}
    for x in elements:
        for y in elements:
            linear = mat_mul(matrix, x + y)
            output = tuple(linear[i] ^ offset[i] for i in range(2 * dimension))
            table[(x, y)] = (output[:dimension], output[dimension:])
    return FiniteBraidedSet(elements, table)


def one_colour_interval(solution):
    return LocalInterval(
        colors=("*",),
        fibres={"*": solution.elements},
        base_R={("*", "*"): ("*", "*")},
        T={
            ("*", "*", x, y): solution.R[(x, y)]
            for x in solution.elements
            for y in solution.elements
        },
    )


def scan(dimension):
    rows = tuple(itertools.product((0, 1), repeat=2 * dimension))
    offsets = tuple(itertools.product((0, 1), repeat=2 * dimension))
    checked = 0
    invertible = 0
    ybe_count = 0
    kind_counts = Counter()
    local_minimal_kind_counts = Counter()
    combined_counts = Counter()
    combined_branch_counts = Counter()
    local_minimal_branch_counts = Counter()
    local_minimal_output_kernel_counts = Counter()
    local_minimal_output_universal_depth_counts = Counter()
    local_minimal_corridor_branch_counts = Counter()
    witness_counts = Counter()
    local_minimal_count = 0
    affine_only_bifree_examples = []
    local_minimal_universal_output_examples = []
    first_examples = {}
    for matrix in itertools.product(rows, repeat=2 * dimension):
        checked += len(offsets)
        if mat_rank(matrix) != 2 * dimension:
            continue
        invertible += len(offsets)
        for offset in offsets:
            solution = affine_solution(matrix, offset, dimension)
            if not solution.is_ybe():
                continue
            ybe_count += 1
            interval = one_colour_interval(solution)
            retraction = context_retraction_audit(interval)
            coretraction = context_coretraction_audit(interval)
            product = product_permutation_witness(interval) is not None
            direct = direct_product_witness(interval) is not None
            tags = branch_tags(solution)
            local_minimal = interval.is_local_minimal(max_fibre_size=4)
            if local_minimal:
                local_minimal_count += 1
                output_kernel_audit = generated_admissible_congruence_audit(
                    interval,
                    coordinate_kernel_seed_pairs(interval),
                )
                local_minimal_output_kernel_counts[output_kernel_audit.kind] += 1
                if output_kernel_audit.kind == "universal":
                    local_minimal_output_universal_depth_counts[
                        output_kernel_audit.stable_depth
                    ] += 1
                local_minimal_corridor_branch_counts[
                    (
                        retraction.kind,
                        coretraction.kind,
                        tags,
                        output_kernel_audit.kind,
                        output_kernel_audit.stable_depth,
                    )
                ] += 1
                if (
                    output_kernel_audit.kind == "universal"
                    and len(local_minimal_universal_output_examples) < 8
                ):
                    local_minimal_universal_output_examples.append(
                        {
                            "matrix": matrix_signature(matrix),
                            "offset": "".join(str(cell) for cell in offset),
                            "branch_tags": list(tags),
                            "output_kernel_depth": output_kernel_audit.stable_depth,
                            "output_kernel_edge_counts": [
                                [repr(color), count]
                                for color, count in output_kernel_audit.edge_count_rows
                            ],
                            "output_kernel_diameters": [
                                [repr(color), diameter]
                                for color, diameter in output_kernel_audit.diameter_rows
                            ],
                        }
                    )
            kind_counts[(retraction.kind, coretraction.kind)] += 1
            if local_minimal:
                local_minimal_kind_counts[(retraction.kind, coretraction.kind)] += 1
            combined_counts[(retraction.kind, coretraction.kind, product, direct)] += 1
            combined_branch_counts[(retraction.kind, coretraction.kind, tags)] += 1
            if local_minimal:
                local_minimal_branch_counts[(retraction.kind, coretraction.kind, tags)] += 1
            if product:
                witness_counts["product_permutation"] += 1
            if direct:
                witness_counts["direct_product"] += 1
            key = (retraction.kind, coretraction.kind)
            if key not in first_examples:
                first_examples[key] = {
                    "matrix": matrix_signature(matrix),
                    "offset": "".join(str(cell) for cell in offset),
                    "branch_tags": list(tags),
                    "product_permutation_witness": product,
                    "direct_product_witness": direct,
                }
            tag_set = set(tags)
            if (
                retraction.kind == "equality"
                and coretraction.kind == "equality"
                and not (
                    tag_set
                    & {
                        "involutive",
                        "permutation_form",
                        "nondegenerate",
                        "rack_type",
                    }
                )
                and len(affine_only_bifree_examples) < 8
            ):
                affine_only_bifree_examples.append(
                    {
                        "matrix": matrix_signature(matrix),
                        "offset": "".join(str(cell) for cell in offset),
                        "branch_tags": list(tags),
                    }
                )
    return {
        "dimension": dimension,
        "point_count": 2**dimension,
        "checked_affine_map_count": checked,
        "invertible_affine_map_count": invertible,
        "affine_ybe_count": ybe_count,
        "local_minimal_count": local_minimal_count,
        "retraction_coretraction_counts": {
            f"retraction={retraction}|coretraction={coretraction}": count
            for (retraction, coretraction), count in sorted(kind_counts.items())
        },
        "local_minimal_retraction_coretraction_counts": {
            f"retraction={retraction}|coretraction={coretraction}": count
            for (retraction, coretraction), count in sorted(local_minimal_kind_counts.items())
        },
        "witness_counts": dict(sorted(witness_counts.items())),
        "combined_witness_counts": {
            (
                f"retraction={retraction}|coretraction={coretraction}|"
                f"product={product}|direct={direct}"
            ): count
            for (retraction, coretraction, product, direct), count in sorted(
                combined_counts.items(), key=lambda item: repr(item[0])
            )
        },
        "combined_branch_tag_counts": {
            (
                f"retraction={retraction}|coretraction={coretraction}|"
                f"tags={'+'.join(tags) if tags else '(untagged)'}"
            ): count
            for (retraction, coretraction, tags), count in sorted(
                combined_branch_counts.items(), key=lambda item: repr(item[0])
            )
        },
        "local_minimal_branch_tag_counts": {
            (
                f"retraction={retraction}|coretraction={coretraction}|"
                f"tags={'+'.join(tags) if tags else '(untagged)'}"
            ): count
            for (retraction, coretraction, tags), count in sorted(
                local_minimal_branch_counts.items(), key=lambda item: repr(item[0])
            )
        },
        "local_minimal_output_kernel_counts": dict(
            sorted(local_minimal_output_kernel_counts.items())
        ),
        "local_minimal_output_universal_depth_counts": {
            str(depth): count
            for depth, count in sorted(
                local_minimal_output_universal_depth_counts.items()
            )
        },
        "local_minimal_corridor_branch_counts": {
            (
                f"retraction={retraction}|coretraction={coretraction}|"
                f"tags={'+'.join(tags) if tags else '(untagged)'}|"
                f"output={output_kind}|depth={depth}"
            ): count
            for (
                retraction,
                coretraction,
                tags,
                output_kind,
                depth,
            ), count in sorted(
                local_minimal_corridor_branch_counts.items(),
                key=lambda item: repr(item[0]),
            )
        },
        "affine_only_bifree_example_count": len(affine_only_bifree_examples),
        "affine_only_bifree_examples": affine_only_bifree_examples,
        "local_minimal_universal_output_example_count": len(
            local_minimal_universal_output_examples
        ),
        "local_minimal_universal_output_examples": local_minimal_universal_output_examples,
        "first_examples": {
            f"retraction={key[0]}|coretraction={key[1]}": value
            for key, value in sorted(first_examples.items())
        },
    }


def main():
    report = {"f2_dimension_2": scan(2)}
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
