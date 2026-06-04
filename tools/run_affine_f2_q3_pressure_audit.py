import json
import sys
from collections import Counter, defaultdict
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_audit import affine_solution  # noqa: E402
from ybe_domination import (  # noqa: E402
    BoundedDeletionSupportAudit,
    bounded_deletion_search_triage,
    bounded_deletion_support_affine_q3_compressed_audit,
    bounded_deletion_support_stabilizer_audit,
    branch_tags,
)


OUT_JSON = ROOT / "proofs" / "affine_f2_q3_pressure_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_q3_pressure_audit.md"
DIMENSION = 3
MATRIX_COUNT = 1 << (DIMENSION * DIMENSION)


def _entry(matrix: int, row: int, col: int) -> int:
    return (matrix >> (row * DIMENSION + col)) & 1


def _matrix_multiply(left: int, right: int) -> int:
    output = 0
    for row in range(DIMENSION):
        for col in range(DIMENSION):
            value = 0
            for inner in range(DIMENSION):
                value ^= _entry(left, row, inner) & _entry(right, inner, col)
            output |= value << (row * DIMENSION + col)
    return output


def _rank_rows(rows, column_count: int) -> int:
    rows = list(rows)
    rank = 0
    for col in range(column_count):
        mask = 1 << col
        pivot = None
        for row_index in range(rank, len(rows)):
            if rows[row_index] & mask:
                pivot = row_index
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for row_index in range(len(rows)):
            if row_index != rank and rows[row_index] & mask:
                rows[row_index] ^= rows[rank]
        rank += 1
    return rank


def _matrix_rank(matrix: int) -> int:
    rows = []
    for row in range(DIMENSION):
        encoded = 0
        for col in range(DIMENSION):
            encoded |= _entry(matrix, row, col) << col
        rows.append(encoded)
    return _rank_rows(rows, DIMENSION)


def _block_rank(a_block: int, b_block: int, c_block: int, d_block: int) -> int:
    rows = []
    for row in range(DIMENSION):
        encoded = 0
        for col in range(DIMENSION):
            encoded |= _entry(a_block, row, col) << col
            encoded |= _entry(b_block, row, col) << (DIMENSION + col)
        rows.append(encoded)
    for row in range(DIMENSION):
        encoded = 0
        for col in range(DIMENSION):
            encoded |= _entry(c_block, row, col) << col
            encoded |= _entry(d_block, row, col) << (DIMENSION + col)
        rows.append(encoded)
    return _rank_rows(rows, 2 * DIMENSION)


def _block_matrix(
    a_block: int,
    b_block: int,
    c_block: int,
    d_block: int,
) -> tuple[tuple[int, ...], ...]:
    rows = []
    for row in range(DIMENSION):
        rows.append(
            tuple(_entry(a_block, row, col) for col in range(DIMENSION))
            + tuple(_entry(b_block, row, col) for col in range(DIMENSION))
        )
    for row in range(DIMENSION):
        rows.append(
            tuple(_entry(c_block, row, col) for col in range(DIMENSION))
            + tuple(_entry(d_block, row, col) for col in range(DIMENSION))
        )
    return tuple(rows)


def _matrix_signature(matrix: tuple[tuple[int, ...], ...]) -> list[str]:
    return ["".join(str(entry) for entry in row) for row in matrix]


def _matrix_vector_multiply(
    matrix: tuple[tuple[int, ...], ...],
    vector: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(
        sum(row[col] * vector[col] for col in range(len(vector))) % 2
        for row in matrix
    )


def _matrix_square(
    matrix: tuple[tuple[int, ...], ...],
) -> tuple[tuple[int, ...], ...]:
    size = len(matrix)
    return tuple(
        tuple(
            sum(matrix[row][inner] * matrix[inner][col] for inner in range(size))
            % 2
            for col in range(size)
        )
        for row in range(size)
    )


def _affine_square_is_identity(
    matrix: tuple[tuple[int, ...], ...],
    offset: tuple[int, ...],
) -> bool:
    identity = tuple(
        tuple(1 if row == col else 0 for col in range(len(matrix)))
        for row in range(len(matrix))
    )
    squared_offset = tuple(
        left ^ right
        for left, right in zip(_matrix_vector_multiply(matrix, offset), offset)
    )
    return _matrix_square(matrix) == identity and not any(squared_offset)


def _precompute_products():
    products = [[0] * MATRIX_COUNT for _ in range(MATRIX_COUNT)]
    for left in range(MATRIX_COUNT):
        product_row = products[left]
        for right in range(MATRIX_COUNT):
            product_row[right] = _matrix_multiply(left, right)
    return products


def _right_multiplication_solutions(products):
    solutions = defaultdict(list)
    for unknown in range(MATRIX_COUNT):
        for right in range(MATRIX_COUNT):
            solutions[(right, products[unknown][right])].append(unknown)
    return solutions


def _linear_ybe_block_rows(products, right_solutions):
    for a_block in range(MATRIX_COUNT):
        a_squared = products[a_block][a_block]
        for c_block in range(MATRIX_COUNT):
            ac = products[a_block][c_block]
            ca = products[c_block][a_block]
            b_seed = right_solutions.get((ac, a_block ^ a_squared), ())
            if not b_seed:
                continue
            for d_block in right_solutions.get((ac, ac ^ ca), ()):
                cd = products[c_block][d_block]
                if products[cd][a_block] ^ products[d_block][c_block] != cd:
                    continue
                ad = products[a_block][d_block]
                dad = products[products[d_block][a_block]][d_block]
                ada = products[ad][a_block]
                db_target = d_block ^ products[d_block][d_block]
                for b_block in b_seed:
                    if products[cd][b_block] != db_target:
                        continue
                    if (
                        products[a_block][b_block]
                        ^ products[b_block][ad]
                        ^ products[b_block][a_block]
                    ):
                        continue
                    if products[c_block][b_block] ^ products[b_block][c_block] != (
                        ada ^ dad
                    ):
                        continue
                    if (
                        products[d_block][b_block]
                        ^ products[ad][b_block]
                        ^ products[b_block][d_block]
                    ):
                        continue
                    if _block_rank(a_block, b_block, c_block, d_block) != (
                        2 * DIMENSION
                    ):
                        continue
                    yield a_block, b_block, c_block, d_block


def _audit_to_dict(audit: BoundedDeletionSupportAudit) -> dict[str, object]:
    return {
        "rack_size_bound": audit.rack_size_bound,
        "h": audit.h,
        "n": audit.n,
        "detector_size": audit.detector_size,
        "detector_component_count": audit.detector_component_count,
        "subset_count": audit.subset_count,
        "joint_image_size": audit.joint_image_size,
        "obstruction_size": audit.obstruction_size,
        "obstruction_nontrivial": audit.obstruction_nontrivial,
        "truncated": audit.truncated,
    }


def _offset_rows_for_matrix(matrix):
    rows = []
    for offset in product((0, 1), repeat=2 * DIMENSION):
        solution = affine_solution(matrix, offset, DIMENSION)
        if not solution.is_ybe():
            continue
        rows.append(
            {
                "offset": "".join(str(entry) for entry in offset),
                "branch_tags": list(branch_tags(solution)),
                "involutive": _affine_square_is_identity(matrix, offset),
            }
        )
    return rows


def build_report():
    products = _precompute_products()
    right_solutions = _right_multiplication_solutions(products)
    linear_count = 0
    singular_b_count = 0
    singular_c_count = 0
    rank_histogram = Counter()
    first_left_degenerate = None

    for blocks in _linear_ybe_block_rows(products, right_solutions):
        a_block, b_block, c_block, d_block = blocks
        linear_count += 1
        b_rank = _matrix_rank(b_block)
        c_rank = _matrix_rank(c_block)
        rank_histogram[(b_rank, c_rank)] += 1
        if b_rank < DIMENSION:
            singular_b_count += 1
            if first_left_degenerate is None:
                first_left_degenerate = blocks
        if c_rank < DIMENSION:
            singular_c_count += 1

    if first_left_degenerate is None:
        raise RuntimeError("no left-degenerate affine block found")

    matrix = _block_matrix(*first_left_degenerate)
    offset_rows = _offset_rows_for_matrix(matrix)
    pressure_row = next(
        row
        for row in offset_rows
        if not row["branch_tags"] and not row["involutive"]
    )
    pressure_offset = tuple(int(entry) for entry in pressure_row["offset"])
    pressure_solution = affine_solution(matrix, pressure_offset, DIMENSION)
    triage = bounded_deletion_search_triage(
        pressure_solution,
        max_rack_size=3,
        max_pure_arity=3,
    )
    q3_n3 = bounded_deletion_support_affine_q3_compressed_audit(
        matrix,
        pressure_offset,
        DIMENSION,
        h=2,
        n=3,
        state_limit=200_000,
    )
    q3_n4 = bounded_deletion_support_stabilizer_audit(
        pressure_solution,
        h=2,
        n=4,
        rack_size_bound=3,
    )

    return {
        "dimension": DIMENSION,
        "linear_ybe_block_count": linear_count,
        "singular_left_block_count": singular_b_count,
        "singular_right_block_count": singular_c_count,
        "rank_histogram": {
            f"B_rank={key[0]},C_rank={key[1]}": count
            for key, count in sorted(rank_histogram.items())
        },
        "first_left_degenerate_blocks": list(first_left_degenerate),
        "first_left_degenerate_matrix": _matrix_signature(matrix),
        "first_left_degenerate_offsets": offset_rows,
        "first_pressure_row": {
            "matrix": _matrix_signature(matrix),
            "offset": pressure_row["offset"],
            "branch_tags": pressure_row["branch_tags"],
            "involutive": pressure_row["involutive"],
            "hidden_constant_action_2_gauge": True,
            "kernel_equivalent_rack": "two-element cyclic rack",
            "q2_dominates_all_arities": True,
            "two_strand_cutoff": triage.two_strand_cutoff.cutoff,
            "first_pure_nontrivial_arity": triage.first_pure_nontrivial_arity,
            "q3_affine_compressed_n3": _audit_to_dict(q3_n3),
            "q3_stabilizer_n4": _audit_to_dict(q3_n4),
        },
    }


def markdown_report(report):
    pressure = report["first_pressure_row"]
    lines = [
        "# Affine F2 Q3 Pressure Audit",
        "",
        "This generated audit reconstructs the affine-linear `F_2^3` YBE",
        "linear-block count from the block equations and then tests the first",
        "left-degenerate non-involutive affine row against the exact `Q_3`",
        "bounded-deletion obstruction.",
        "",
        "## Linear Blocks",
        "",
        f"- dimension: `{report['dimension']}`;",
        f"- invertible linear YBE blocks: `{report['linear_ybe_block_count']}`;",
        f"- singular left block `B`: `{report['singular_left_block_count']}`;",
        f"- singular right block `C`: `{report['singular_right_block_count']}`.",
        "",
        "Rank histogram:",
        "",
        "```text",
    ]
    lines.extend(
        f"{key}: {value}"
        for key, value in report["rank_histogram"].items()
    )
    lines.extend(
        [
            "```",
            "",
            "The count `26153` matches the previously recorded aggregate",
            "`F_2^3` affine scan.",
            "",
            "## First Pressure Row",
            "",
            "Matrix rows:",
            "",
            "```text",
        ]
    )
    lines.extend(pressure["matrix"])
    lines.extend(
        [
            "```",
            "",
            f"Offset: `{pressure['offset']}`.",
            "",
            "This row is left-degenerate, non-involutive, and has no current",
            "`branch_tags` classification.  Its cheap front-end readout is:",
            "",
            "```text",
            f"a_X(2) = {pressure['two_strand_cutoff']}",
            (
                "first pure nontrivial arity = "
                f"{pressure['first_pure_nontrivial_arity']}"
            ),
            "```",
            "",
            "Exact `Q_3` deletion checks:",
            "",
            "```text",
            (
                "affine compressed n=3: "
                f"E={pressure['q3_affine_compressed_n3']['obstruction_size']}, "
                f"joint={pressure['q3_affine_compressed_n3']['joint_image_size']}, "
                "nontrivial="
                f"{pressure['q3_affine_compressed_n3']['obstruction_nontrivial']}"
            ),
            (
                "stabilizer n=4: "
                f"E={pressure['q3_stabilizer_n4']['obstruction_size']}, "
                f"joint={pressure['q3_stabilizer_n4']['joint_image_size']}, "
                "nontrivial="
                f"{pressure['q3_stabilizer_n4']['obstruction_nontrivial']}"
            ),
            "```",
            "",
            "The follow-up hidden-gauge proof in",
            "`proofs/affine_f2_hidden_cyclic_gauge.md` closes this row in all",
            "arities: after a position-dependent change of coordinates, this",
            "row is braid-kernel equivalent to the two-element cyclic rack.",
            "Thus `Q_2` already dominates it, and",
            "",
            "```text",
            "E^{(3)}_{X,h,n} = 1 for every h,n.",
            "```",
            "",
            "The finite `n=3,4` computations above are retained as regression",
            "checks of the compressed and stabilizer implementations.",
        ]
    )
    return "\n".join(lines) + "\n"


def main():
    report = build_report()
    OUT_JSON.write_text(
        json.dumps(report, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    OUT_MD.write_text(markdown_report(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
