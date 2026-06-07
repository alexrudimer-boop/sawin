"""Verify a combined nonperm3 trivial-kernel certificate."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.nonperm3_detector_products import (  # noqa: E402
    normalize_flat_ybe_table,
    nonpermutation_size3_flat_tables,
)

KIND = "nonperm3_combined_trivial_kernel_audit_v1"
BRANCH = "nonpermutation_size3"


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audit_json")
    parser.add_argument("--arity", type=int, required=True)
    parser.add_argument("--require-all-55", action="store_true")
    parser.add_argument("--require-trivial-full-product", action="store_true")
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
    if payload.get("bound") != 3:
        failures.append("bound must be 3")

    rows = payload.get("rows")
    if not isinstance(rows, list):
        failures.append("rows must be a list")
        rows = []
    if payload.get("row_count") != len(rows):
        failures.append("row_count mismatch")

    expected_tables = tuple(nonpermutation_size3_flat_tables())
    expected_table_set = set(expected_tables)
    seen_tables: set[tuple[int, ...]] = set()
    method_counter: Counter[str] = Counter()
    kernel_counter: Counter[int] = Counter()
    quotient_counter: Counter[int] = Counter()
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
        if table in seen_tables:
            failures.append(f"{context}: duplicate ybe_table")
        seen_tables.add(table)
        if table not in expected_table_set:
            failures.append(f"{context}: ybe_table is not one of the 55 nonperm tables")

        method = row.get("certification_method")
        if method not in {"direct_full_product_stabilizer", "subproduct_trivial_kernel"}:
            failures.append(f"{context}: invalid certification_method {method!r}")
        else:
            method_counter[method] += 1
        if not isinstance(row.get("source_audit"), str) or not row["source_audit"]:
            failures.append(f"{context}: missing source_audit")

        for field in ("detector_component_count", "seed_count"):
            value = row.get(field)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                failures.append(f"{context}: {field} must be a nonnegative integer")
        sizes = row.get("detector_component_sizes")
        if not isinstance(sizes, list) or any(
            isinstance(size, bool) or not isinstance(size, int) or size < 1
            for size in sizes
        ):
            failures.append(f"{context}: detector_component_sizes must be positive ints")
        elif row.get("detector_component_count") != len(sizes):
            failures.append(f"{context}: detector_component_count mismatch")

        if row.get("full_product_kernel_image_size") != 1:
            failures.append(f"{context}: full_product_kernel_image_size must be 1")
        else:
            kernel_counter[1] += 1
        if row.get("full_product_parabolic_image_size") != 1:
            failures.append(f"{context}: full_product_parabolic_image_size must be 1")
        if row.get("full_product_quotient_size") != 1:
            failures.append(f"{context}: full_product_quotient_size must be 1")
        else:
            quotient_counter[1] += 1
        if row.get("full_product_quotient_nontrivial") is not False:
            failures.append(f"{context}: full_product_quotient_nontrivial must be false")
        if row.get("truncated") is not False:
            failures.append(f"{context}: truncated must be false")

        if method == "direct_full_product_stabilizer":
            value = row.get("full_product_joint_image_size")
            if isinstance(value, bool) or not isinstance(value, int) or value < 1:
                failures.append(f"{context}: full_product_joint_image_size must be positive")
        elif method == "subproduct_trivial_kernel":
            required = {
                "subproduct_kernel_image_size": 1,
                "subproduct_parabolic_image_size": 1,
                "subproduct_quotient_size": 1,
                "subproduct_quotient_nontrivial": False,
            }
            for field, expected in required.items():
                if row.get(field) != expected:
                    failures.append(
                        f"{context}: {field}={row.get(field)!r}, expected {expected!r}"
                    )
            audited = row.get("audited_detector_component_indices")
            omitted = row.get("omitted_detector_component_indices")
            if not isinstance(audited, list) or not audited:
                failures.append(f"{context}: audited_detector_component_indices missing")
            if not isinstance(omitted, list) or not omitted:
                failures.append(f"{context}: omitted_detector_component_indices missing")

    missing = [table for table in expected_tables if table not in seen_tables]
    extra = [table for table in seen_tables if table not in expected_table_set]
    if payload.get("missing_table_count") != len(missing):
        failures.append("missing_table_count mismatch")
    if payload.get("extra_table_count") != len(extra):
        failures.append("extra_table_count mismatch")
    if args.require_all_55:
        if len(rows) != 55:
            failures.append("require-all-55 but row_count is not 55")
        if missing:
            failures.append(f"require-all-55 but missing tables: {missing}")
        if extra:
            failures.append(f"require-all-55 but extra tables: {extra}")
    if args.require_trivial_full_product:
        if kernel_counter[1] != len(rows):
            failures.append("not every row has full_product_kernel_image_size 1")
        if quotient_counter[1] != len(rows):
            failures.append("not every row has full_product_quotient_size 1")

    supplied_methods = payload.get("certification_method_counts")
    if supplied_methods is not None:
        expected_methods = dict(method_counter)
        if supplied_methods != expected_methods:
            failures.append(
                f"certification_method_counts mismatch: "
                f"{supplied_methods!r} != {expected_methods!r}"
            )
    if payload.get("full_product_kernel_image_size_distribution") != {"1": len(rows)}:
        failures.append("full_product_kernel_image_size_distribution mismatch")
    if payload.get("full_product_quotient_size_distribution") != {"1": len(rows)}:
        failures.append("full_product_quotient_size_distribution mismatch")

    if failures:
        print("FAILED nonperm3 combined trivial-kernel audit verification")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("OK nonperm3 combined trivial-kernel audit verification")
    print(f"arity {args.arity}")
    print(f"rows {len(rows)}")
    print(f"methods {dict(method_counter)}")


if __name__ == "__main__":
    main()
