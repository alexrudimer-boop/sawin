from __future__ import annotations

import json
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_affine_f2_q3_dihedral_native_image_audit import (  # noqa: E402
    _candidate_generator,
    _compose_affine_f2,
    _identity_rows,
)
from ybe_domination import small_rack_representatives  # noqa: E402
from ybe_domination.residual import (  # noqa: E402
    action_permutation,
    permutation_order,
)

OUT_JSON = ROOT / "proofs" / "affine_f2_q3_small_rack_native_detector_audit.json"
OUT_MD = ROOT / "proofs" / "affine_f2_q3_small_rack_native_detector_audit.md"


@dataclass(frozen=True)
class SmallRackNativeDetectorRow:
    rack_index: int
    rack_size: int
    two_strand_order: int
    arity: int
    explored_state_count: int
    detector_image_order: int
    x_image_order: int
    truncated: bool
    obstruction_found: bool
    witness_word: tuple[int, ...] | None
    witness_word_length: int | None
    moved_zero_tuple_image: tuple[tuple[int, int, int], ...] | None


def _compose_permutations(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(left[right[index]] for index in range(len(left)))


def _bits_to_f2_triples(vector: int, arity: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(
        tuple((vector >> (3 * index + bit)) & 1 for bit in range(3))
        for index in range(arity)
    )


def _audit_rack_detector(
    *,
    rack_index: int,
    rack,
    arity: int,
    state_limit: int,
) -> SmallRackNativeDetectorRow:
    detector_generators = tuple(
        action_permutation(rack, arity, (index,))
        for index in range(1, arity)
    )
    x_generators = tuple(
        _candidate_generator(arity, index)
        for index in range(arity - 1)
    )
    detector_identity = tuple(range(len(detector_generators[0])))
    x_identity = (_identity_rows(3 * arity), 0)
    start = (detector_identity, x_identity)
    seen = {start: ()}
    detector_seen = {detector_identity}
    x_seen = {x_identity}
    queue = deque([start])
    while queue:
        detector_state, x_state = queue.popleft()
        word = seen[(detector_state, x_state)]
        for generator_index, (detector_generator, x_generator) in enumerate(
            zip(detector_generators, x_generators),
            start=1,
        ):
            detector_candidate = _compose_permutations(
                detector_generator,
                detector_state,
            )
            x_candidate = _compose_affine_f2(x_generator, x_state)
            state = (detector_candidate, x_candidate)
            if state in seen:
                continue
            detector_seen.add(detector_candidate)
            x_seen.add(x_candidate)
            witness_word = word + (generator_index,)
            if detector_candidate == detector_identity and x_candidate != x_identity:
                return SmallRackNativeDetectorRow(
                    rack_index=rack_index,
                    rack_size=len(rack.elements),
                    two_strand_order=permutation_order(
                        action_permutation(rack, 2, (1,))
                    ),
                    arity=arity,
                    explored_state_count=len(seen) + 1,
                    detector_image_order=len(detector_seen),
                    x_image_order=len(x_seen),
                    truncated=False,
                    obstruction_found=True,
                    witness_word=witness_word,
                    witness_word_length=len(witness_word),
                    moved_zero_tuple_image=_bits_to_f2_triples(
                        x_candidate[1],
                        arity,
                    ),
                )
            if len(seen) + 1 > state_limit:
                return SmallRackNativeDetectorRow(
                    rack_index=rack_index,
                    rack_size=len(rack.elements),
                    two_strand_order=permutation_order(
                        action_permutation(rack, 2, (1,))
                    ),
                    arity=arity,
                    explored_state_count=len(seen),
                    detector_image_order=len(detector_seen),
                    x_image_order=len(x_seen),
                    truncated=True,
                    obstruction_found=False,
                    witness_word=None,
                    witness_word_length=None,
                    moved_zero_tuple_image=None,
                )
            seen[state] = witness_word
            queue.append(state)
    return SmallRackNativeDetectorRow(
        rack_index=rack_index,
        rack_size=len(rack.elements),
        two_strand_order=permutation_order(action_permutation(rack, 2, (1,))),
        arity=arity,
        explored_state_count=len(seen),
        detector_image_order=len(detector_seen),
        x_image_order=len(x_seen),
        truncated=False,
        obstruction_found=False,
        witness_word=None,
        witness_word_length=None,
        moved_zero_tuple_image=None,
    )


def build_report(
    *,
    max_rack_size: int = 4,
    arity: int = 5,
    state_limit: int = 250_000,
) -> dict:
    racks = small_rack_representatives(max_rack_size)
    viable = []
    rejected = []
    for rack_index, rack in enumerate(racks, start=1):
        two_strand_order = permutation_order(action_permutation(rack, 2, (1,)))
        row = {
            "rack_index": rack_index,
            "rack_size": len(rack.elements),
            "two_strand_order": two_strand_order,
        }
        if two_strand_order % 3:
            rejected.append(row)
        else:
            viable.append((rack_index, rack, row))

    rows = [
        _audit_rack_detector(
            rack_index=rack_index,
            rack=rack,
            arity=arity,
            state_limit=state_limit,
        ).__dict__
        for rack_index, rack, _row in viable
    ]
    promising_rack_index = 24
    promising_rack = racks[promising_rack_index - 1]
    promising_rows = [
        _audit_rack_detector(
            rack_index=promising_rack_index,
            rack=promising_rack,
            arity=checked_arity,
            state_limit=state_limit,
        ).__dict__
        for checked_arity in range(2, arity + 1)
    ]
    return {
        "title": "Affine F2^3 small rack native detector audit",
        "max_rack_size": max_rack_size,
        "arity": arity,
        "state_limit": state_limit,
        "rack_representative_count": len(racks),
        "two_strand_rejected_count": len(rejected),
        "two_strand_viable_count": len(viable),
        "two_strand_rejected": rejected,
        "rows": rows,
        "promising_rack": {
            "rack_index": promising_rack_index,
            "rack_size": len(promising_rack.elements),
            "operation_table_rows": [
                [promising_rack.R[(left, right)][0] for right in promising_rack.elements]
                for left in promising_rack.elements
            ],
            "checked_rows": promising_rows,
            "kernel_inclusion_holds_through_checked_arities": all(
                not row["truncated"] and not row["obstruction_found"]
                for row in promising_rows
            ),
            "image_orders_match_through_checked_arities": all(
                row["explored_state_count"]
                == row["detector_image_order"]
                == row["x_image_order"]
                for row in promising_rows
                if not row["truncated"]
            ),
        },
        "unobstructed_nontruncated_rows": [
            row for row in rows if not row["truncated"] and not row["obstruction_found"]
        ],
        "obstructed_rows": [row for row in rows if row["obstruction_found"]],
        "truncated_rows": [row for row in rows if row["truncated"]],
        "conclusion": (
            "Among rack representatives of size at most 4, only those whose "
            "two-strand crossing order is divisible by 3 can possibly dominate "
            "the affine F_2^3 candidate. This audit tests the viable individual "
            "racks at arity 5 using native affine state for X. Obstructed rows "
            "give concrete detector-kernel braid words; unobstructed rows need "
            "larger arity or an all-n proof."
        ),
    }


def render_markdown(report: dict) -> str:
    lines = [
        "# Affine F2^3 Small Rack Native Detector Audit",
        "",
        "This generated audit tests individual small rack representatives",
        "against the affine `F_2^3` survivor using tuple permutations on the",
        "rack side and native affine transformations on the `X` side.",
        "",
        f"- max rack size: `{report['max_rack_size']}`;",
        f"- arity: `{report['arity']}`;",
        f"- state limit: `{report['state_limit']}`;",
        f"- rack representatives: `{report['rack_representative_count']}`;",
        f"- rejected by two-strand order: `{report['two_strand_rejected_count']}`;",
        f"- viable by two-strand order: `{report['two_strand_viable_count']}`;",
        f"- obstructed viable rows: `{len(report['obstructed_rows'])}`;",
        f"- truncated viable rows: `{len(report['truncated_rows'])}`;",
        "- unobstructed nontruncated viable rows: "
        f"`{len(report['unobstructed_nontruncated_rows'])}`.",
        "",
        (
            "| rack index | size | order R | explored | detector image | "
            "X image | obstruction | truncated | word length |"
        ),
        "| ---: | ---: | ---: | ---: | ---: | ---: | --- | --- | ---: |",
    ]
    for row in report["rows"]:
        lines.append(
            f"| {row['rack_index']} | {row['rack_size']} | "
            f"{row['two_strand_order']} | {row['explored_state_count']} | "
            f"{row['detector_image_order']} | {row['x_image_order']} | "
            f"{row['obstruction_found']} | {row['truncated']} | "
            f"{row['witness_word_length']} |"
        )
    promising = report["promising_rack"]
    lines.extend(
        [
            "",
            "## Promising Size-4 Rack",
            "",
            f"- rack index: `{promising['rack_index']}`;",
            f"- rack size: `{promising['rack_size']}`;",
            "- kernel inclusion holds through checked arities: "
            f"`{promising['kernel_inclusion_holds_through_checked_arities']}`;",
            "- image orders match through checked arities: "
            f"`{promising['image_orders_match_through_checked_arities']}`.",
            "",
            "Rack operation table rows:",
            "",
            "```text",
        ]
    )
    lines.extend(str(row) for row in promising["operation_table_rows"])
    lines.extend(
        [
            "```",
            "",
            "| n | joint image | detector image | X image | obstruction | truncated |",
            "| ---: | ---: | ---: | ---: | --- | --- |",
        ]
    )
    for row in promising["checked_rows"]:
        lines.append(
            f"| {row['arity']} | {row['explored_state_count']} | "
            f"{row['detector_image_order']} | {row['x_image_order']} | "
            f"{row['obstruction_found']} | {row['truncated']} |"
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
