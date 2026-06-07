"""Certify full detector-product triviality from detector subproducts.

If a detector subproduct ``Y'`` already has
``rho^X_n(K^{Y'}_n)=1``, then any larger detector product
``Y=Y' x Y''`` also has trivial realized detector-kernel image on ``X^n``:
``K^Y_n <= K^{Y'}_n``.  This tool records that proof-safe shortcut for rows
where the full stabilizer computation is too expensive.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    componentwise_stabilizer_realized_parabolic_cross_effect_audit,
)
from ybe_domination.nonperm3_detector_products import (  # noqa: E402
    detector_index_by_ybe_table,
    extract_detector_schema_records,
    nonpermutation_size3_flat_tables,
    rack_from_table,
    solution_from_flat_table,
)

KIND = "nonperm3_subproduct_trivial_kernel_audit_v1"
BRANCH = "nonpermutation_size3"


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _row_for_table(
    table,
    rack_tables,
    *,
    arity: int,
    bound: int,
    state_limit: int,
    component_size_max: int,
    include_timing: bool,
):
    full_sizes = [len(rack_table) for rack_table in rack_tables]
    audited_indices = [
        index
        for index, rack_table in enumerate(rack_tables)
        if len(rack_table) <= component_size_max
    ]
    omitted_indices = [
        index for index in range(len(rack_tables)) if index not in set(audited_indices)
    ]
    if not audited_indices:
        raise ValueError(f"no audited subproduct components for table {table!r}")
    if not omitted_indices:
        raise ValueError(f"subproduct is not proper for table {table!r}")

    audited_rack_tables = tuple(rack_tables[index] for index in audited_indices)
    detectors = tuple(rack_from_table(rack_table) for rack_table in audited_rack_tables)
    solution = solution_from_flat_table(table)
    started_at = time.perf_counter()
    audit = componentwise_stabilizer_realized_parabolic_cross_effect_audit(
        solution,
        detectors,
        bound=bound,
        n=arity,
        state_limit=state_limit,
    )
    elapsed = round(time.perf_counter() - started_at, 6)
    if audit.truncated:
        raise RuntimeError(f"subproduct audit truncated for table {table!r}")
    if audit.kernel_image_size != 1:
        raise RuntimeError(
            f"subproduct kernel image is not trivial for table {table!r}: "
            f"{audit.kernel_image_size}"
        )

    audit_data = asdict(audit)
    return {
        "ybe_table": list(table),
        "arity": arity,
        "bound": bound,
        "full_detector_component_count": len(rack_tables),
        "full_detector_component_sizes": full_sizes,
        "audited_detector_component_indices": audited_indices,
        "audited_detector_component_count": len(audited_indices),
        "audited_detector_component_sizes": [
            full_sizes[index] for index in audited_indices
        ],
        "omitted_detector_component_indices": omitted_indices,
        "omitted_detector_component_sizes": [
            full_sizes[index] for index in omitted_indices
        ],
        "subproduct_joint_image_size": audit_data["joint_image_size"],
        "subproduct_kernel_image_size": audit_data["kernel_image_size"],
        "subproduct_parabolic_image_size": audit_data["parabolic_image_size"],
        "subproduct_quotient_size": audit_data["quotient_size"],
        "subproduct_quotient_nontrivial": audit_data["quotient_nontrivial"],
        "subproduct_seed_count": audit_data["seed_count"],
        "subproduct_truncated": audit_data["truncated"],
        "full_product_kernel_image_size": 1,
        "full_product_parabolic_image_size": 1,
        "full_product_quotient_size": 1,
        "full_product_quotient_nontrivial": False,
        "conclusion": "full_product_detector_kernel_x_image_trivial_by_subproduct",
        **({"elapsed_seconds": elapsed} if include_timing else {}),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        action="append",
        required=True,
        help="Detector schema certificate JSON. May be supplied more than once.",
    )
    parser.add_argument("--arity", type=int, required=True)
    parser.add_argument("--bound", type=int, default=3)
    parser.add_argument("--state-limit", type=int, default=1_000_000)
    parser.add_argument(
        "--component-size-max",
        type=int,
        required=True,
        help="Use only detector components of size at most this value.",
    )
    parser.add_argument(
        "--only-table-index",
        type=int,
        action="append",
        default=None,
        help="Audit only the supplied detector-index row. May be repeated.",
    )
    parser.add_argument(
        "--only-ybe-table",
        action="append",
        default=None,
        help=(
            "Audit only the supplied comma-separated flat size-three YBE table. "
            "May be repeated."
        ),
    )
    parser.add_argument(
        "--require-all-selected-trivial",
        action="store_true",
        help="Fail if any selected row cannot be certified by the subproduct.",
    )
    parser.add_argument("--include-row-timing", action="store_true")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    if args.arity < 1:
        raise SystemExit("arity must be positive")
    if args.bound < 1:
        raise SystemExit("bound must be positive")
    if args.component_size_max < 1:
        raise SystemExit("component-size-max must be positive")

    certificate_paths = tuple(Path(path) for path in args.certificate)
    payloads = tuple(_load_json(path) for path in certificate_paths)
    records = tuple(
        record
        for payload in payloads
        for record in extract_detector_schema_records(payload)
    )
    detector_index_by_table = detector_index_by_ybe_table(payloads)
    nonperm_tables = nonpermutation_size3_flat_tables()
    imported_tables = tuple(
        table for table in nonperm_tables if table in detector_index_by_table
    )

    if args.only_table_index is not None and args.only_ybe_table is not None:
        raise SystemExit("--only-table-index and --only-ybe-table are mutually exclusive")
    if args.only_ybe_table is not None:
        selected = []
        for raw_table in args.only_ybe_table:
            try:
                table = tuple(int(part.strip()) for part in raw_table.split(","))
            except ValueError as exc:
                raise SystemExit(f"invalid --only-ybe-table: {raw_table!r}") from exc
            if table not in detector_index_by_table:
                raise SystemExit(f"table not present in detector index: {table!r}")
            selected.append(table)
        selected_tables = tuple(selected)
    elif args.only_table_index is None:
        selected_tables = tuple(
            table
            for table in imported_tables
            if any(
                len(component.rack_table) > args.component_size_max
                for component in detector_index_by_table[table]
            )
            and any(
                len(component.rack_table) <= args.component_size_max
                for component in detector_index_by_table[table]
            )
        )
    else:
        selected = []
        for index in args.only_table_index:
            if index < 0 or index >= len(imported_tables):
                raise SystemExit(f"table index out of range: {index}")
            selected.append(imported_tables[index])
        selected_tables = tuple(selected)

    rows = []
    failures = []
    for table in selected_tables:
        rack_tables = tuple(
            component.rack_table for component in detector_index_by_table[table]
        )
        try:
            rows.append(
                _row_for_table(
                    table,
                    rack_tables,
                    arity=args.arity,
                    bound=args.bound,
                    state_limit=args.state_limit,
                    component_size_max=args.component_size_max,
                    include_timing=args.include_row_timing,
                )
            )
        except Exception as exc:  # pragma: no cover - CLI diagnostic path
            message = f"{list(table)}: {exc}"
            failures.append(message)
            if args.require_all_selected_trivial:
                raise SystemExit(message) from exc

    detector_index = [
        {
            "ybe_table": list(table),
            "detectors": [
                {
                    "rack_table": [list(row) for row in component.rack_table],
                    "source_schema_ids": list(component.source_schema_ids),
                }
                for component in detector_index_by_table[table]
            ],
        }
        for table in imported_tables
    ]
    output = {
        "kind": KIND,
        "branch": BRANCH,
        "certificate_paths": [str(path) for path in certificate_paths],
        "arity": args.arity,
        "bound": args.bound,
        "state_limit": args.state_limit,
        "audit_method": "stabilizer_subproduct_trivial_kernel",
        "component_size_max": args.component_size_max,
        "schema_like_detector_records": len(records),
        "nonpermutation_ybe_tables": len(nonperm_tables),
        "tables_with_detector_components": len(imported_tables),
        "detector_index": detector_index,
        "selected_table_count": len(selected_tables),
        "row_count": len(rows),
        "rows": rows,
        "failures": failures,
    }
    Path(args.output).write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
