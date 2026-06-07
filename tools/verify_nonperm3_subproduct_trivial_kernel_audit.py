"""Verify subproduct-triviality certificates for nonperm3 detector products."""

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
)
from ybe_domination.rack_residual_tower import (  # noqa: E402
    componentwise_stabilizer_realized_parabolic_cross_effect_audit,
)

KIND = "nonperm3_subproduct_trivial_kernel_audit_v1"
BRANCH = "nonpermutation_size3"


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _detector_index_by_table(payload: dict):
    out = {}
    for index, entry in enumerate(payload.get("detector_index", [])):
        if not isinstance(entry, dict):
            raise ValueError(f"detector_index[{index}] is not an object")
        table = normalize_flat_ybe_table(entry.get("ybe_table"))
        detectors = entry.get("detectors")
        if not isinstance(detectors, list):
            raise ValueError(f"detector_index[{index}].detectors is not a list")
        if table in out:
            raise ValueError(f"duplicate detector_index table: {table}")
        out[table] = detectors
    return out


def _int_list(value, *, context: str):
    if not isinstance(value, list) or any(
        isinstance(item, bool) or not isinstance(item, int) for item in value
    ):
        raise ValueError(f"{context} must be a list of integers")
    return list(value)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audit_json")
    parser.add_argument("--arity", type=int, required=True)
    parser.add_argument("--state-limit", type=int, default=1_000_000)
    parser.add_argument(
        "--require-trivial-full-product",
        action="store_true",
        help="Require every row to conclude full-product triviality.",
    )
    args = parser.parse_args()

    payload = _load_json(Path(args.audit_json))
    failures: list[str] = []
    if not isinstance(payload, dict):
        failures.append("payload must be a JSON object")
        payload = {}
    if payload.get("kind") != KIND:
        failures.append(f"kind must be {KIND!r}")
    if payload.get("branch") != BRANCH:
        failures.append(f"branch must be {BRANCH!r}")
    if payload.get("arity") != args.arity:
        failures.append(f"arity mismatch: {payload.get('arity')!r} != {args.arity!r}")
    bound = payload.get("bound")
    if isinstance(bound, bool) or not isinstance(bound, int) or bound < 1:
        failures.append("bound must be a positive integer")
        bound = 3

    try:
        index_by_table = _detector_index_by_table(payload)
    except (TypeError, ValueError) as exc:
        failures.append(f"invalid detector_index: {exc}")
        index_by_table = {}

    rows = payload.get("rows")
    if not isinstance(rows, list):
        failures.append("rows must be a list")
        rows = []
    if payload.get("row_count") != len(rows):
        failures.append("row_count mismatch")

    recomputed_rows = 0
    trivial_rows = 0
    for row_index, row in enumerate(rows):
        context = f"rows[{row_index}]"
        if not isinstance(row, dict):
            failures.append(f"{context}: row must be an object")
            continue
        try:
            table = normalize_flat_ybe_table(row.get("ybe_table"))
        except (TypeError, ValueError) as exc:
            failures.append(f"{context}: invalid ybe_table: {exc}")
            continue
        detector_entries = index_by_table.get(table)
        if detector_entries is None:
            failures.append(f"{context}: ybe_table not present in detector_index")
            continue
        try:
            full_rack_tables = [
                normalize_rack_table(detector["rack_table"])
                for detector in detector_entries
            ]
        except (TypeError, ValueError, KeyError) as exc:
            failures.append(f"{context}: invalid detector rack table: {exc}")
            continue
        full_sizes = [len(rack_table) for rack_table in full_rack_tables]
        try:
            audited_indices = _int_list(
                row.get("audited_detector_component_indices"),
                context=f"{context}.audited_detector_component_indices",
            )
            omitted_indices = _int_list(
                row.get("omitted_detector_component_indices"),
                context=f"{context}.omitted_detector_component_indices",
            )
        except ValueError as exc:
            failures.append(str(exc))
            continue
        all_indices = set(range(len(full_rack_tables)))
        if set(audited_indices) | set(omitted_indices) != all_indices:
            failures.append(f"{context}: audited and omitted indices do not cover components")
        if set(audited_indices) & set(omitted_indices):
            failures.append(f"{context}: audited and omitted indices overlap")
        if not audited_indices:
            failures.append(f"{context}: no audited subproduct components")
            continue
        if not omitted_indices:
            failures.append(f"{context}: omitted component list is empty")

        expected_audited_sizes = [full_sizes[index] for index in audited_indices]
        expected_omitted_sizes = [full_sizes[index] for index in omitted_indices]
        for field, expected in {
            "arity": args.arity,
            "bound": bound,
            "full_detector_component_count": len(full_rack_tables),
            "full_detector_component_sizes": full_sizes,
            "audited_detector_component_count": len(audited_indices),
            "audited_detector_component_sizes": expected_audited_sizes,
            "omitted_detector_component_sizes": expected_omitted_sizes,
            "subproduct_kernel_image_size": 1,
            "subproduct_parabolic_image_size": 1,
            "subproduct_quotient_size": 1,
            "subproduct_quotient_nontrivial": False,
            "subproduct_truncated": False,
            "full_product_kernel_image_size": 1,
            "full_product_parabolic_image_size": 1,
            "full_product_quotient_size": 1,
            "full_product_quotient_nontrivial": False,
            "conclusion": "full_product_detector_kernel_x_image_trivial_by_subproduct",
        }.items():
            if row.get(field) != expected:
                failures.append(
                    f"{context}: {field}={row.get(field)!r}, expected {expected!r}"
                )

        solution = solution_from_flat_table(table)
        audited_detectors = tuple(
            rack_from_table(full_rack_tables[index]) for index in audited_indices
        )
        audit = componentwise_stabilizer_realized_parabolic_cross_effect_audit(
            solution,
            audited_detectors,
            bound=bound,
            n=args.arity,
            state_limit=args.state_limit,
        )
        recomputed_rows += 1
        if audit.truncated:
            failures.append(f"{context}: recomputed subproduct audit truncated")
            continue
        if row.get("subproduct_joint_image_size") != audit.joint_image_size:
            failures.append(
                f"{context}: subproduct_joint_image_size={row.get('subproduct_joint_image_size')!r}, "
                f"expected {audit.joint_image_size!r}"
            )
        if audit.kernel_image_size != 1:
            failures.append(
                f"{context}: recomputed subproduct kernel image is not trivial: "
                f"{audit.kernel_image_size!r}"
            )
            continue
        trivial_rows += 1
        if args.require_trivial_full_product:
            # Proof obligation: K(full product) <= K(audited subproduct).
            # Since the recomputed subproduct X-image is trivial, the full
            # product X-image is also trivial.
            for field in (
                "full_product_kernel_image_size",
                "full_product_parabolic_image_size",
                "full_product_quotient_size",
            ):
                if row.get(field) != 1:
                    failures.append(f"{context}: {field} must be 1")
            if row.get("full_product_quotient_nontrivial") is not False:
                failures.append(f"{context}: full_product_quotient_nontrivial must be false")

    if failures:
        print("FAILED nonperm3 subproduct trivial-kernel audit verification")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("OK nonperm3 subproduct trivial-kernel audit verification")
    print(f"arity {args.arity}")
    print(f"recomputed_rows {recomputed_rows}")
    print(f"trivial_subproduct_rows {trivial_rows}")


if __name__ == "__main__":
    main()
