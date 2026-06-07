"""Assemble direct and subproduct trivial-kernel rows into one certificate."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.nonperm3_detector_products import (  # noqa: E402
    normalize_flat_ybe_table,
    nonpermutation_size3_flat_tables,
    verify_width3_audit_payload,
)

KIND = "nonperm3_combined_trivial_kernel_audit_v1"
BRANCH = "nonpermutation_size3"
DIRECT_KIND = "nonperm3_width3_componentwise_cross_effect_audit_v1"
SUBPRODUCT_KIND = "nonperm3_subproduct_trivial_kernel_audit_v1"


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _canonical_row_key(row: dict) -> tuple[int, ...]:
    return normalize_flat_ybe_table(row.get("ybe_table"))


def _direct_certified_row(row: dict, source: Path) -> dict:
    table = _canonical_row_key(row)
    required = {
        "truncated": False,
        "kernel_image_size": 1,
        "parabolic_image_size": 1,
        "quotient_size": 1,
        "quotient_nontrivial": False,
    }
    for field, expected in required.items():
        if row.get(field) != expected:
            raise ValueError(
                f"{source}: direct row {table} has {field}={row.get(field)!r}, "
                f"expected {expected!r}"
            )
    return {
        "ybe_table": list(table),
        "certification_method": "direct_full_product_stabilizer",
        "source_audit": str(source),
        "detector_component_count": row["detector_component_count"],
        "detector_component_sizes": row["detector_component_sizes"],
        "full_product_joint_image_size": row["joint_image_size"],
        "full_product_kernel_image_size": row["kernel_image_size"],
        "full_product_parabolic_image_size": row["parabolic_image_size"],
        "full_product_quotient_size": row["quotient_size"],
        "full_product_quotient_nontrivial": row["quotient_nontrivial"],
        "truncated": row["truncated"],
        "seed_count": row["seed_count"],
    }


def _subproduct_certified_row(row: dict, source: Path) -> dict:
    table = _canonical_row_key(row)
    required = {
        "subproduct_truncated": False,
        "subproduct_kernel_image_size": 1,
        "subproduct_parabolic_image_size": 1,
        "subproduct_quotient_size": 1,
        "subproduct_quotient_nontrivial": False,
        "full_product_kernel_image_size": 1,
        "full_product_parabolic_image_size": 1,
        "full_product_quotient_size": 1,
        "full_product_quotient_nontrivial": False,
        "conclusion": "full_product_detector_kernel_x_image_trivial_by_subproduct",
    }
    for field, expected in required.items():
        if row.get(field) != expected:
            raise ValueError(
                f"{source}: subproduct row {table} has {field}={row.get(field)!r}, "
                f"expected {expected!r}"
            )
    return {
        "ybe_table": list(table),
        "certification_method": "subproduct_trivial_kernel",
        "source_audit": str(source),
        "detector_component_count": row["full_detector_component_count"],
        "detector_component_sizes": row["full_detector_component_sizes"],
        "audited_detector_component_indices": row["audited_detector_component_indices"],
        "audited_detector_component_sizes": row["audited_detector_component_sizes"],
        "omitted_detector_component_indices": row["omitted_detector_component_indices"],
        "omitted_detector_component_sizes": row["omitted_detector_component_sizes"],
        "subproduct_joint_image_size": row["subproduct_joint_image_size"],
        "subproduct_kernel_image_size": row["subproduct_kernel_image_size"],
        "subproduct_parabolic_image_size": row["subproduct_parabolic_image_size"],
        "subproduct_quotient_size": row["subproduct_quotient_size"],
        "subproduct_quotient_nontrivial": row["subproduct_quotient_nontrivial"],
        "full_product_kernel_image_size": row["full_product_kernel_image_size"],
        "full_product_parabolic_image_size": row["full_product_parabolic_image_size"],
        "full_product_quotient_size": row["full_product_quotient_size"],
        "full_product_quotient_nontrivial": row["full_product_quotient_nontrivial"],
        "truncated": row["subproduct_truncated"],
        "seed_count": row["subproduct_seed_count"],
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--direct-audit", action="append", default=[])
    parser.add_argument("--subproduct-audit", action="append", default=[])
    parser.add_argument("--arity", type=int, required=True)
    parser.add_argument("--bound", type=int, default=3)
    parser.add_argument("--require-all-55", action="store_true")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    if not args.direct_audit and not args.subproduct_audit:
        raise SystemExit("at least one source audit is required")

    rows_by_table: dict[tuple[int, ...], dict] = {}
    source_paths = [Path(path) for path in args.direct_audit + args.subproduct_audit]

    for source in (Path(path) for path in args.direct_audit):
        payload = _load_json(source)
        if payload.get("kind") != DIRECT_KIND:
            raise SystemExit(f"{source}: expected kind {DIRECT_KIND!r}")
        if payload.get("branch") != BRANCH:
            raise SystemExit(f"{source}: expected branch {BRANCH!r}")
        if payload.get("arity") != args.arity or payload.get("bound") != args.bound:
            raise SystemExit(f"{source}: arity/bound mismatch")
        failures = verify_width3_audit_payload(payload)
        if failures:
            raise SystemExit(f"{source}: structural verification failed: {failures}")
        for row in payload.get("rows", []):
            certified = _direct_certified_row(row, source)
            table = tuple(certified["ybe_table"])
            previous = rows_by_table.get(table)
            if previous is None:
                rows_by_table[table] = certified
            elif previous != certified and previous["certification_method"] != certified["certification_method"]:
                # Prefer direct full-product rows over subproduct rows when both exist.
                rows_by_table[table] = certified

    for source in (Path(path) for path in args.subproduct_audit):
        payload = _load_json(source)
        if payload.get("kind") != SUBPRODUCT_KIND:
            raise SystemExit(f"{source}: expected kind {SUBPRODUCT_KIND!r}")
        if payload.get("branch") != BRANCH:
            raise SystemExit(f"{source}: expected branch {BRANCH!r}")
        if payload.get("arity") != args.arity or payload.get("bound") != args.bound:
            raise SystemExit(f"{source}: arity/bound mismatch")
        for row in payload.get("rows", []):
            certified = _subproduct_certified_row(row, source)
            table = tuple(certified["ybe_table"])
            rows_by_table.setdefault(table, certified)

    expected_tables = tuple(nonpermutation_size3_flat_tables())
    missing = [table for table in expected_tables if table not in rows_by_table]
    extra = [table for table in rows_by_table if table not in set(expected_tables)]
    if args.require_all_55 and (missing or extra):
        raise SystemExit(
            f"combined rows do not match the 55 non-permutation tables: "
            f"missing={missing}, extra={extra}"
        )

    ordered_rows = [rows_by_table[table] for table in expected_tables if table in rows_by_table]
    method_counts: dict[str, int] = {}
    for row in ordered_rows:
        method = row["certification_method"]
        method_counts[method] = method_counts.get(method, 0) + 1
    output = {
        "kind": KIND,
        "branch": BRANCH,
        "arity": args.arity,
        "bound": args.bound,
        "source_audits": [str(path) for path in source_paths],
        "nonpermutation_ybe_tables": len(expected_tables),
        "row_count": len(ordered_rows),
        "missing_table_count": len(missing),
        "missing_ybe_tables": [list(table) for table in missing],
        "extra_table_count": len(extra),
        "extra_ybe_tables": [list(table) for table in extra],
        "certification_method_counts": method_counts,
        "full_product_kernel_image_size_distribution": {"1": len(ordered_rows)},
        "full_product_quotient_size_distribution": {"1": len(ordered_rows)},
        "rows": ordered_rows,
    }
    Path(args.output).write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
