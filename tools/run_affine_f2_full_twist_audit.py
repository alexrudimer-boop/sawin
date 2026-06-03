import itertools
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_audit import affine_solution  # noqa: E402
from run_linear_f2_audit import mat_rank, matrix_signature  # noqa: E402
from ybe_domination import branch_tags, full_twist_braid_word  # noqa: E402


OUT_JSON = ROOT / "proofs" / "affine_f2_full_twist_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_full_twist_audit.md"


def identity_matrix(size):
    return tuple(
        tuple(1 if row == col else 0 for col in range(size))
        for row in range(size)
    )


def zero_vector(size):
    return (0,) * size


def matrix_matrix_mul(left, right):
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][mid] * right[mid][col] for mid in range(size)) % 2
            for col in range(size)
        )
        for row in range(size)
    )


def matrix_vector_mul(matrix, vector):
    return tuple(
        sum(matrix[row][col] * vector[col] for col in range(len(vector))) % 2
        for row in range(len(matrix))
    )


def vector_add(left, right):
    return tuple(a ^ b for a, b in zip(left, right))


def compose_affine(left, right):
    """Return ``left after right`` for affine maps over ``F_2``."""

    left_matrix, left_offset = left
    right_matrix, right_offset = right
    return (
        matrix_matrix_mul(left_matrix, right_matrix),
        vector_add(matrix_vector_mul(left_matrix, right_offset), left_offset),
    )


def generator_affine_map(matrix, offset, dimension, braid_index, generator):
    """Affine map for ``sigma_generator`` on ``(F_2^dimension)^braid_index``."""

    if not 1 <= generator < braid_index:
        raise ValueError("generator must satisfy 1 <= generator < braid_index")
    total_dimension = dimension * braid_index
    start = dimension * (generator - 1)
    linear = [list(row) for row in identity_matrix(total_dimension)]
    translation = [0] * total_dimension
    for row in range(2 * dimension):
        target_row = start + row
        for col in range(total_dimension):
            linear[target_row][col] = 0
        for col in range(2 * dimension):
            linear[target_row][start + col] = matrix[row][col]
        translation[target_row] = offset[row]
    return tuple(tuple(row) for row in linear), tuple(translation)


def braid_affine_map(matrix, offset, dimension, braid_index, braid_word):
    current = (identity_matrix(dimension * braid_index), zero_vector(dimension * braid_index))
    for generator in braid_word:
        if generator <= 0:
            raise ValueError("this audit only uses positive braid words")
        current = compose_affine(
            generator_affine_map(matrix, offset, dimension, braid_index, generator),
            current,
        )
    return current


def affine_map_order(linear, translation, *, max_order=100000):
    size = len(linear)
    identity = identity_matrix(size)
    zero = zero_vector(size)
    current = (identity, zero)
    step = (linear, translation)
    for order in range(1, max_order + 1):
        current = compose_affine(step, current)
        if current == (identity, zero):
            return order
    return None


def affine_full_twist_order(matrix, offset, dimension, braid_index, *, max_order=100000):
    linear, translation = braid_affine_map(
        matrix,
        offset,
        dimension,
        braid_index,
        full_twist_braid_word(braid_index),
    )
    return affine_map_order(linear, translation, max_order=max_order)


def affine_full_twist_profile(matrix, offset, dimension, max_n, *, max_order=100000):
    return tuple(
        affine_full_twist_order(
            matrix,
            offset,
            dimension,
            braid_index,
            max_order=max_order,
        )
        for braid_index in range(1, max_n + 1)
    )


def _profile_key(profile):
    return ",".join(">" if value is None else str(value) for value in profile)


def _tags_key(tags):
    return "+".join(tags) if tags else "(untagged)"


def scan(dimension, *, max_n=7, max_order=100000):
    rows = tuple(itertools.product((0, 1), repeat=2 * dimension))
    offsets = tuple(itertools.product((0, 1), repeat=2 * dimension))
    checked = 0
    invertible = 0
    ybe_count = 0
    profile_counts = Counter()
    untagged_profile_counts = Counter()
    max_prefix_order = 1
    cap_exceeded_count = 0
    untagged_examples = []
    first_examples_by_profile = {}

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
            tags = branch_tags(solution)
            profile = affine_full_twist_profile(
                matrix,
                offset,
                dimension,
                max_n,
                max_order=max_order,
            )
            if any(value is None for value in profile):
                cap_exceeded_count += 1
            else:
                max_prefix_order = max(max_prefix_order, max(profile))
            key = (_tags_key(tags), _profile_key(profile))
            profile_counts[key] += 1
            first_examples_by_profile.setdefault(
                key,
                {
                    "matrix": matrix_signature(matrix),
                    "offset": "".join(str(cell) for cell in offset),
                    "branch_tags": list(tags),
                    "full_twist_orders": list(profile),
                },
            )
            if not tags:
                untagged_profile_counts[profile] += 1
                if len(untagged_examples) < 8:
                    untagged_examples.append(
                        {
                            "matrix": matrix_signature(matrix),
                            "offset": "".join(str(cell) for cell in offset),
                            "full_twist_orders": list(profile),
                        }
                    )

    return {
        "dimension": dimension,
        "point_count": 2**dimension,
        "max_n": max_n,
        "max_order_cap": max_order,
        "checked_affine_map_count": checked,
        "invertible_affine_map_count": invertible,
        "affine_ybe_count": ybe_count,
        "max_observed_prefix_order": max_prefix_order,
        "order_cap_exceeded_count": cap_exceeded_count,
        "profile_counts": {
            f"tags={tags}|orders={profile}": count
            for (tags, profile), count in sorted(profile_counts.items())
        },
        "first_examples_by_profile": {
            f"tags={tags}|orders={profile}": example
            for (tags, profile), example in sorted(first_examples_by_profile.items())
        },
        "untagged_count": sum(untagged_profile_counts.values()),
        "untagged_profile_counts": {
            _profile_key(profile): count
            for profile, count in sorted(untagged_profile_counts.items())
        },
        "untagged_examples": untagged_examples,
    }


def markdown_report(report):
    scan_report = report["f2_dimension_2"]
    lines = [
        "# Affine F2 Full-Twist Audit",
        "",
        "## Purpose",
        "",
        "This generated audit stress-tests the central full-twist obstruction in",
        "the translated affine four-point universe.  It is a finite-prefix",
        "candidate-search audit, not an all-arity theorem.",
        "",
        "The calculation uses affine block-map composition over `F_2`; it does",
        "not enumerate all tuples in `(F_2^2)^n` when computing full-twist",
        "orders.",
        "",
        "## Results",
        "",
        f"- affine maps checked: `{scan_report['checked_affine_map_count']}`;",
        f"- invertible affine maps: `{scan_report['invertible_affine_map_count']}`;",
        f"- affine YBE tables: `{scan_report['affine_ybe_count']}`;",
        f"- checked braid indices: `1 <= n <= {scan_report['max_n']}`;",
        f"- maximum observed central full-twist order: `{scan_report['max_observed_prefix_order']}`;",
        f"- order-cap misses: `{scan_report['order_cap_exceeded_count']}`;",
        f"- untagged affine rows: `{scan_report['untagged_count']}`.",
        "",
        "Untagged full-twist profiles:",
        "",
        "```text",
    ]
    for profile, count in scan_report["untagged_profile_counts"].items():
        lines.append(f"{profile}: {count}")
    lines.extend(
        [
            "```",
            "",
            "Thus every untagged affine `F_2^2` row in this finite universe has",
            "central full-twist prefix orders",
            "",
            "```text",
            "1, 2, 1, 2, 1, 2, 1",
            "```",
            "",
            "for `n=1,...,7`.  These rows are already non-primitive in the",
            "`proofs/affine_f2_audit.md` sense because they have proper mixed",
            "retraction/coretraction families; this audit adds that they also do",
            "not stress the central full-twist obstruction in the checked prefix.",
            "",
            "## Consequence",
            "",
            "The central full-twist route to outcome B must leave the four-point",
            "translated affine `F_2` universe, or find behavior invisible in this",
            "prefix.  In particular, the currently untagged affine rows do not",
            "supply the needed unbounded orders of",
            "`rho_X,n((sigma_1 ... sigma_{n-1})^n)`.",
            "",
        ]
    )
    return "\n".join(lines)


def main():
    report = {"f2_dimension_2": scan(2)}
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(markdown_report(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)


if __name__ == "__main__":
    main()
