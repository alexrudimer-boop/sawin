from __future__ import annotations

import json
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

OUT_JSON = ROOT / "proofs" / "affine_f2_q3_dihedral_native_image_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_q3_dihedral_native_image_audit.md"

CANDIDATE_MATRIX_ROWS = (
    "010100",
    "100100",
    "000001",
    "001101",
    "110110",
    "110101",
)
CANDIDATE_OFFSET = "001100"


@dataclass(frozen=True)
class NativeImageRow:
    arity: int
    d3_image_order: int | None
    x_image_order: int | None
    orders_match: bool | None
    d3_truncated: bool
    x_truncated: bool


@dataclass(frozen=True)
class NativeKernelWitness:
    arity: int
    witness_word: tuple[int, ...]
    witness_word_length: int
    explored_state_count: int
    moved_zero_tuple_image: tuple[tuple[int, int, int], ...]
    truncated: bool


def _identity_rows(size: int) -> tuple[int, ...]:
    return tuple(1 << index for index in range(size))


def _matrix_vector_f2(rows: tuple[int, ...], vector: int) -> int:
    output = 0
    for row_index, mask in enumerate(rows):
        if (mask & vector).bit_count() & 1:
            output |= 1 << row_index
    return output


def _matrix_product_f2(
    left_rows: tuple[int, ...],
    right_rows: tuple[int, ...],
) -> tuple[int, ...]:
    output = []
    for mask in left_rows:
        row = 0
        active = mask
        index = 0
        while active:
            if active & 1:
                row ^= right_rows[index]
            active >>= 1
            index += 1
        output.append(row)
    return tuple(output)


def _compose_affine_f2(
    left: tuple[tuple[int, ...], int],
    right: tuple[tuple[int, ...], int],
) -> tuple[tuple[int, ...], int]:
    left_matrix, left_offset = left
    right_matrix, right_offset = right
    return (
        _matrix_product_f2(left_matrix, right_matrix),
        _matrix_vector_f2(left_matrix, right_offset) ^ left_offset,
    )


def _candidate_local_rows() -> tuple[int, ...]:
    return tuple(
        sum(int(entry) << column for column, entry in enumerate(row))
        for row in CANDIDATE_MATRIX_ROWS
    )


def _candidate_offset_bits() -> int:
    return sum(int(entry) << index for index, entry in enumerate(CANDIDATE_OFFSET))


def _candidate_generator(arity: int, index: int) -> tuple[tuple[int, ...], int]:
    dimension = 3 * arity
    rows = list(_identity_rows(dimension))
    offset = 0
    local_rows = _candidate_local_rows()
    local_offset = _candidate_offset_bits()
    for row in range(6):
        mask = 0
        for column in range(6):
            if (local_rows[row] >> column) & 1:
                mask |= 1 << (3 * index + column)
        rows[3 * index + row] = mask
        if (local_offset >> row) & 1:
            offset |= 1 << (3 * index + row)
    return (tuple(rows), offset)


def _affine_f2_image_order(
    arity: int,
    *,
    state_limit: int,
) -> tuple[int | None, bool]:
    generators = tuple(_candidate_generator(arity, index) for index in range(arity - 1))
    identity = (_identity_rows(3 * arity), 0)
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = _compose_affine_f2(generator, current)
            if candidate in seen:
                continue
            seen.add(candidate)
            if len(seen) > state_limit:
                return None, True
            queue.append(candidate)
    return len(seen), False


def _bits_to_f2_triples(vector: int, arity: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple((vector >> (3 * index + bit)) & 1 for bit in range(3))
        for index in range(arity)
    )


def _identity_matrix_mod(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(1 if row == column else 0 for column in range(size))
        for row in range(size)
    )


def _matrix_product_mod(
    left: tuple[tuple[int, ...], ...],
    right: tuple[tuple[int, ...], ...],
    modulus: int,
) -> tuple[tuple[int, ...], ...]:
    size = len(left)
    return tuple(
        tuple(
            sum(left[row][inner] * right[inner][column] for inner in range(size))
            % modulus
            for column in range(size)
        )
        for row in range(size)
    )


def _d3_generator(arity: int, index: int) -> tuple[tuple[int, ...], ...]:
    matrix = [list(row) for row in _identity_matrix_mod(arity)]
    matrix[index] = [0] * arity
    matrix[index + 1] = [0] * arity
    matrix[index][index] = 2
    matrix[index][index + 1] = 2
    matrix[index + 1][index] = 1
    return tuple(tuple(row) for row in matrix)


def _d3_image_order(arity: int, *, state_limit: int) -> tuple[int | None, bool]:
    generators = tuple(_d3_generator(arity, index) for index in range(arity - 1))
    identity = _identity_matrix_mod(arity)
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for generator in generators:
            candidate = _matrix_product_mod(generator, current, 3)
            if candidate in seen:
                continue
            seen.add(candidate)
            if len(seen) > state_limit:
                return None, True
            queue.append(candidate)
    return len(seen), False


def _native_kernel_witness(
    arity: int,
    *,
    state_limit: int,
) -> NativeKernelWitness | None:
    """Find a braid word that is trivial on D3 but nontrivial on X."""

    x_identity = (_identity_rows(3 * arity), 0)
    d3_identity = _identity_matrix_mod(arity)
    generators = tuple(
        (
            _d3_generator(arity, index),
            _candidate_generator(arity, index),
            index + 1,
        )
        for index in range(arity - 1)
    )
    start = (d3_identity, x_identity)
    seen = {start: ()}
    queue = deque([start])
    while queue:
        d3_current, x_current = queue.popleft()
        word = seen[(d3_current, x_current)]
        for d3_generator, x_generator, label in generators:
            d3_candidate = _matrix_product_mod(d3_generator, d3_current, 3)
            x_candidate = _compose_affine_f2(x_generator, x_current)
            state = (d3_candidate, x_candidate)
            if state in seen:
                continue
            witness_word = word + (label,)
            if d3_candidate == d3_identity and x_candidate != x_identity:
                return NativeKernelWitness(
                    arity=arity,
                    witness_word=witness_word,
                    witness_word_length=len(witness_word),
                    explored_state_count=len(seen) + 1,
                    moved_zero_tuple_image=_bits_to_f2_triples(
                        x_candidate[1],
                        arity,
                    ),
                    truncated=False,
                )
            if len(seen) + 1 > state_limit:
                return NativeKernelWitness(
                    arity=arity,
                    witness_word=(),
                    witness_word_length=0,
                    explored_state_count=len(seen),
                    moved_zero_tuple_image=(),
                    truncated=True,
                )
            seen[state] = witness_word
            queue.append(state)
    return None


def build_report(max_arity: int = 5, state_limit: int = 1_000_000) -> dict:
    rows = []
    first_d3_failure_arity = None
    for arity in range(2, max_arity + 1):
        d3_order, d3_truncated = _d3_image_order(arity, state_limit=state_limit)
        x_order, x_truncated = _affine_f2_image_order(arity, state_limit=state_limit)
        if (
            first_d3_failure_arity is None
            and not d3_truncated
            and not x_truncated
            and d3_order is not None
            and x_order is not None
            and x_order > d3_order
        ):
            first_d3_failure_arity = arity
        rows.append(
            NativeImageRow(
                arity=arity,
                d3_image_order=d3_order,
                x_image_order=x_order,
                orders_match=(
                    None
                    if d3_truncated or x_truncated
                    else d3_order == x_order
                ),
                d3_truncated=d3_truncated,
                x_truncated=x_truncated,
            )
        )
    witness = (
        None
        if first_d3_failure_arity is None
        else _native_kernel_witness(first_d3_failure_arity, state_limit=state_limit)
    )
    return {
        "title": "Affine F2^3 dihedral native image audit",
        "candidate_matrix_rows": CANDIDATE_MATRIX_ROWS,
        "candidate_offset": CANDIDATE_OFFSET,
        "max_arity": max_arity,
        "state_limit": state_limit,
        "rows": [row.__dict__ for row in rows],
        "all_computed_orders_match": all(
            row.orders_match is True for row in rows
        ),
        "any_truncated": any(row.d3_truncated or row.x_truncated for row in rows),
        "first_d3_failure_arity": first_d3_failure_arity,
        "first_d3_kernel_witness": None if witness is None else witness.__dict__,
        "conclusion": (
            "Native linear/affine image generation shows that the "
            "three-element dihedral rack repair matches the affine F_2^3 "
            "candidate through arity 4 but fails at arity 5: the X image is "
            "larger than the D3 image, and a native joint-image search gives "
            "an explicit braid word in the D3 kernel that moves X.  This rules "
            "out D3 domination of this candidate but does not rule out a "
            "larger finite rack detector."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Affine F2^3 Dihedral Native Image Audit",
        "",
        "This generated audit compares native image groups for the affine",
        "`F_2^3` survivor and the three-element dihedral rack.  It uses",
        "affine transformations over `F_2` for `X` and linear transformations",
        "over `F_3` for `D_3`, avoiding tuple-permutation enumeration.",
        "",
        f"- max arity: `{report['max_arity']}`;",
        f"- state limit: `{report['state_limit']}`;",
        f"- any truncated: `{report['any_truncated']}`;",
        f"- all computed orders match: `{report['all_computed_orders_match']}`.",
        f"- first D3 failure arity: `{report['first_d3_failure_arity']}`.",
        "",
        "| n | D3 image order | X image order | match | truncated |",
        "| ---: | ---: | ---: | --- | --- |",
    ]
    for row in report["rows"]:
        truncated = row["d3_truncated"] or row["x_truncated"]
        lines.append(
            f"| {row['arity']} | {row['d3_image_order']} | "
            f"{row['x_image_order']} | {row['orders_match']} | {truncated} |"
        )
    witness = report["first_d3_kernel_witness"]
    lines.extend(["", "## First D3-Kernel Witness", ""])
    if witness is None:
        lines.append("No D3-kernel witness was found in the computed range.")
    elif witness["truncated"]:
        lines.append(
            f"The joint witness search truncated after "
            f"`{witness['explored_state_count']}` states."
        )
    else:
        lines.extend(
            [
                f"- arity: `{witness['arity']}`;",
                f"- word length: `{witness['witness_word_length']}`;",
                f"- witness word: `{witness['witness_word']}`;",
                f"- explored states: `{witness['explored_state_count']}`;",
                "- image of the zero tuple under the X action: "
                f"`{witness['moved_zero_tuple_image']}`.",
            ]
        )
    lines.extend(["", "## Conclusion", "", report["conclusion"]])
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    if argv not in (None, ()):
        raise SystemExit("no arguments are supported")
    report = build_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
