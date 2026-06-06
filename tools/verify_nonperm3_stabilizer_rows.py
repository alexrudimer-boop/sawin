"""Independently verify stabilizer-kernel rows in a nonperm3 width audit."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.nonperm3_detector_products import (  # noqa: E402
    normalize_flat_ybe_table,
    normalize_rack_table,
    rack_from_table,
    solution_from_flat_table,
    verify_width3_audit_payload,
    width3_complete_audit_row_failures,
)
from ybe_domination.rack_residual_tower import (  # noqa: E402
    _componentwise_stabilizer_kernel_generators,
    _subgroup_generated_by_permutations,
)


def _identity_permutation(size: int) -> tuple[int, ...]:
    return tuple(range(size))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audit_json")
    parser.add_argument("--arity", type=int, required=True)
    parser.add_argument("--state-limit", type=int, default=1_000_000)
    parser.add_argument(
        "--require-complete-basis",
        action="store_true",
        help="Require all 55 non-permutation tables in the detector index.",
    )
    parser.add_argument(
        "--require-run-audit",
        action="store_true",
        help="Require exactly one row for every detector-index table.",
    )
    parser.add_argument(
        "--require-trivial-kernel-image",
        action="store_true",
        help="Require the recomputed X-image of every detector kernel to be trivial.",
    )
    args = parser.parse_args()

    payload = json.loads(Path(args.audit_json).read_text(encoding="utf-8"))
    failures = list(verify_width3_audit_payload(payload))

    if payload.get("arity") != args.arity:
        failures.append(
            f"payload arity {payload.get('arity')!r} does not match --arity {args.arity}"
        )
    detector_index = payload.get("detector_index", [])
    rows = payload.get("rows", [])
    if args.require_complete_basis:
        if payload.get("incomplete_detector_basis") is not False:
            failures.append("complete basis required but incomplete_detector_basis is true")
        if payload.get("missing_table_count") != 0:
            failures.append("complete basis required but missing_table_count is nonzero")
        if not isinstance(detector_index, list) or len(detector_index) != 55:
            failures.append("complete basis required but detector_index length is not 55")
    if args.require_run_audit:
        if payload.get("run_audit") is not True:
            failures.append("run audit required but run_audit is not true")
        failures.extend(width3_complete_audit_row_failures(payload))

    if not isinstance(detector_index, list):
        detector_index = []
    if not isinstance(rows, list):
        rows = []
    index_by_table = {}
    for index, entry in enumerate(detector_index):
        if not isinstance(entry, dict):
            continue
        try:
            table = normalize_flat_ybe_table(entry.get("ybe_table"))
        except (TypeError, ValueError) as exc:
            failures.append(f"detector_index[{index}]: invalid ybe_table: {exc}")
            continue
        index_by_table[table] = entry

    recomputed_rows = 0
    trivial_kernel_rows = 0
    for row_index, row in enumerate(rows):
        if not isinstance(row, dict):
            failures.append(f"rows[{row_index}]: row must be an object")
            continue
        try:
            table = normalize_flat_ybe_table(row.get("ybe_table"))
        except (TypeError, ValueError) as exc:
            failures.append(f"rows[{row_index}]: invalid ybe_table: {exc}")
            continue
        entry = index_by_table.get(table)
        if entry is None:
            failures.append(f"rows[{row_index}]: no detector_index entry")
            continue
        detector_entries = entry.get("detectors", [])
        if not detector_entries:
            continue
        if row.get("audit_method") != "stabilizer":
            failures.append(f"rows[{row_index}]: audit_method is not 'stabilizer'")

        solution = solution_from_flat_table(table)
        try:
            rack_tables = [
                normalize_rack_table(detector["rack_table"])
                for detector in detector_entries
            ]
        except (TypeError, ValueError, KeyError) as exc:
            failures.append(f"rows[{row_index}]: invalid detector rack table: {exc}")
            continue
        detectors = tuple(rack_from_table(rack_table) for rack_table in rack_tables)

        joint_size, _stabilizer_size, kernel_generators = (
            _componentwise_stabilizer_kernel_generators(
                solution,
                detectors,
                args.arity,
            )
        )
        recomputed_rows += 1
        if row.get("joint_image_size") != joint_size:
            failures.append(
                f"rows[{row_index}]: joint_image_size mismatch: "
                f"{row.get('joint_image_size')} != {joint_size}"
            )

        identity = _identity_permutation(len(solution.elements) ** args.arity)
        kernel_image, truncated = _subgroup_generated_by_permutations(
            identity,
            kernel_generators,
            args.state_limit,
        )
        if truncated:
            failures.append(f"rows[{row_index}]: kernel-image recomputation truncated")
            continue
        if row.get("kernel_image_size") != len(kernel_image):
            failures.append(
                f"rows[{row_index}]: kernel_image_size mismatch: "
                f"{row.get('kernel_image_size')} != {len(kernel_image)}"
            )
        if len(kernel_image) == 1:
            trivial_kernel_rows += 1
        if args.require_trivial_kernel_image:
            if len(kernel_image) != 1:
                failures.append(
                    f"rows[{row_index}]: nontrivial recomputed kernel image"
                )
            for field, expected in {
                "parabolic_image_size": 1,
                "quotient_size": 1,
                "quotient_nontrivial": False,
                "truncated": False,
            }.items():
                if row.get(field) != expected:
                    failures.append(
                        f"rows[{row_index}]: {field}={row.get(field)!r}, "
                        f"expected {expected!r}"
                    )

    if failures:
        print("FAILED independent stabilizer-row verification")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("OK independent stabilizer-row verification")
    print(f"arity {args.arity}")
    print(f"recomputed_stabilizer_rows {recomputed_rows}")
    print(f"trivial_kernel_rows {trivial_kernel_rows}")


if __name__ == "__main__":
    main()
