import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    LocalInterval,
    branch_tags,
    context_retraction_audit,
    product_permutation_witness,
    two_strand_crossing_order,
    two_strand_symmetric_gate_summary,
    two_strand_symmetric_detector_covers_solution,
    two_strand_symmetric_longitude_period,
)


OUT = ROOT / "proofs" / "linear_f2_audit.json"


def mat_mul(matrix, vector):
    return tuple(
        sum(matrix[i][j] * vector[j] for j in range(len(vector))) % 2
        for i in range(len(matrix))
    )


def mat_rank(matrix):
    rows = [list(row) for row in matrix]
    if not rows:
        return 0
    row_count = len(rows)
    col_count = len(rows[0])
    rank = 0
    pivot_row = 0
    for col in range(col_count):
        pivot = None
        for row in range(pivot_row, row_count):
            if rows[row][col]:
                pivot = row
                break
        if pivot is None:
            continue
        rows[pivot_row], rows[pivot] = rows[pivot], rows[pivot_row]
        for row in range(row_count):
            if row != pivot_row and rows[row][col]:
                rows[row] = [a ^ b for a, b in zip(rows[row], rows[pivot_row])]
        rank += 1
        pivot_row += 1
    return rank


def linear_solution(matrix, dimension):
    elements = tuple(itertools.product((0, 1), repeat=dimension))
    table = {}
    for x in elements:
        for y in elements:
            output = mat_mul(matrix, x + y)
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


def matrix_signature(matrix):
    return ["".join(str(cell) for cell in row) for row in matrix]


def scan(dimension):
    rows = tuple(itertools.product((0, 1), repeat=2 * dimension))
    checked = 0
    invertible = 0
    ybe_count = 0
    retraction_branch_counts = {}
    crossing_order_histogram = {}
    crossing_gate_explanation_counts = {}
    symmetric_gate_bad_count = 0
    first_symmetric_gate_bad = None
    unknown_examples = []
    first_examples_by_kind = {}
    for matrix in itertools.product(rows, repeat=2 * dimension):
        checked += 1
        if mat_rank(matrix) != 2 * dimension:
            continue
        invertible += 1
        solution = linear_solution(matrix, dimension)
        if not solution.is_ybe():
            continue
        ybe_count += 1
        crossing_order = two_strand_crossing_order(solution)
        crossing_order_histogram[str(crossing_order)] = (
            crossing_order_histogram.get(str(crossing_order), 0) + 1
        )
        gate_summary = two_strand_symmetric_gate_summary(solution)
        crossing_gate_explanation_counts[gate_summary.explanation] = (
            crossing_gate_explanation_counts.get(gate_summary.explanation, 0) + 1
        )
        if not two_strand_symmetric_detector_covers_solution(solution):
            symmetric_gate_bad_count += 1
            if first_symmetric_gate_bad is None:
                first_symmetric_gate_bad = {
                    "matrix": matrix_signature(matrix),
                    "crossing_order": crossing_order,
                }
        interval = one_colour_interval(solution)
        audit = context_retraction_audit(interval)
        tags = branch_tags(solution)
        has_product_witness = product_permutation_witness(interval) is not None
        key = (
            audit.kind,
            " + ".join(tags) if tags else "(untagged)",
            "product" if has_product_witness else "no_product",
        )
        retraction_branch_counts[key] = retraction_branch_counts.get(key, 0) + 1
        known = bool(
            set(tags)
            & {
                "involutive",
                "permutation_form",
                "affine_cyclic",
                "nondegenerate",
                "rack_type",
            }
        ) or has_product_witness
        if audit.kind not in first_examples_by_kind:
            first_examples_by_kind[audit.kind] = {
                "matrix": matrix_signature(matrix),
                "branch_tags": list(tags),
                "product_permutation_witness": has_product_witness,
            }
        if not known and len(unknown_examples) < 5:
            unknown_examples.append(
                {
                    "matrix": matrix_signature(matrix),
                    "retraction_kind": audit.kind,
                    "branch_tags": list(tags),
                }
            )
    return {
        "dimension": dimension,
        "point_count": 2**dimension,
        "checked_matrix_count": checked,
        "invertible_matrix_count": invertible,
        "linear_ybe_count": ybe_count,
        "two_strand_symmetric_longitude_period": two_strand_symmetric_longitude_period(
            2**dimension
        ),
        "crossing_order_histogram": dict(
            sorted(crossing_order_histogram.items(), key=lambda item: int(item[0]))
        ),
        "crossing_gate_explanation_counts": dict(
            sorted(crossing_gate_explanation_counts.items())
        ),
        "symmetric_gate_bad_count": symmetric_gate_bad_count,
        "first_symmetric_gate_bad": first_symmetric_gate_bad,
        "retraction_branch_counts": {
            " | ".join(key): count
            for key, count in sorted(retraction_branch_counts.items())
        },
        "unknown_example_count": len(unknown_examples),
        "unknown_examples": unknown_examples,
        "first_examples_by_kind": first_examples_by_kind,
    }


def main():
    report = {"f2_dimension_2": scan(2)}
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
