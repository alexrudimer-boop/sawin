"""Run the non-permutation size-three detector-product cross-effect audit.

The full arity-3 q=5 detector schema certificate is not currently local.
This tool therefore has two modes:

* by default, summarize which detector rack components can be imported from
  the supplied certificate JSON files;
* with ``--run-audit``, run the fixed-arity componentwise cross-effect audit
  for every non-permutation size-three table whose detector product is present.

The intended full computation is arity 4, bound 3, after importing the complete
arity-2 and arity-3 detector schema certificates.
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import componentwise_realized_parabolic_cross_effect_audit  # noqa: E402
from ybe_domination.nonperm3_detector_products import (  # noqa: E402
    detector_index_by_ybe_table,
    extract_detector_schema_records,
    nonpermutation_size3_flat_tables,
    rack_from_table,
    solution_from_flat_table,
)


def _load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def _audit_row(table, rack_tables, *, bound: int, arity: int, state_limit: int):
    solution = solution_from_flat_table(table)
    if not solution.is_ybe():
        raise ValueError(f"imported table is not a YBE solution: {table!r}")
    detectors = tuple(rack_from_table(rack_table) for rack_table in rack_tables)
    audit = componentwise_realized_parabolic_cross_effect_audit(
        solution,
        detectors,
        bound=bound,
        n=arity,
        state_limit=state_limit,
    )
    audit_data = asdict(audit)
    audit_data["arity"] = audit_data["n"]
    return {
        "ybe_table": list(table),
        "detector_component_count": len(detectors),
        "detector_component_sizes": [len(detector.elements) for detector in detectors],
        **audit_data,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--certificate",
        action="append",
        required=True,
        help="Certificate JSON file to import. May be supplied more than once.",
    )
    parser.add_argument("--bound", type=int, default=3)
    parser.add_argument("--arity", type=int, default=4)
    parser.add_argument("--state-limit", type=int, default=100_000)
    parser.add_argument(
        "--run-audit",
        action="store_true",
        help="Run componentwise cross-effect closure for imported detector products.",
    )
    parser.add_argument(
        "--require-all-55",
        action="store_true",
        help="Exit with status 2 unless all 55 non-permutation tables have detectors.",
    )
    parser.add_argument(
        "--max-tables",
        type=int,
        default=None,
        help="Optional cap on audited tables, for smoke checks only.",
    )
    parser.add_argument("--output", default=None)
    args = parser.parse_args()

    certificate_paths = tuple(Path(path) for path in args.certificate)
    payloads = tuple(_load_json(path) for path in certificate_paths)
    records = tuple(
        record
        for payload in payloads
        for record in extract_detector_schema_records(payload)
    )
    detector_index_by_table = detector_index_by_ybe_table(payloads)
    components_by_table = {
        table: tuple(component.rack_table for component in components)
        for table, components in detector_index_by_table.items()
    }
    nonperm_tables = nonpermutation_size3_flat_tables()
    nonperm_table_set = set(nonperm_tables)
    imported_nonperm_tables = tuple(
        table for table in nonperm_tables if table in components_by_table
    )
    extra_tables = tuple(
        table for table in components_by_table if table not in nonperm_table_set
    )
    missing_tables = tuple(
        table for table in nonperm_tables if table not in components_by_table
    )

    rows = []
    if args.run_audit:
        audited_tables = imported_nonperm_tables
        if args.max_tables is not None:
            audited_tables = audited_tables[: args.max_tables]
        for table in audited_tables:
            rows.append(
                _audit_row(
                    table,
                    components_by_table[table],
                    bound=args.bound,
                    arity=args.arity,
                    state_limit=args.state_limit,
                )
            )

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
        for table in imported_nonperm_tables
    ]
    output = {
        "kind": "nonperm3_width3_componentwise_cross_effect_audit_v1",
        "type": "nonperm3_detector_product_cross_effect_audit",
        "branch": "nonpermutation_size3",
        "certificate_paths": [str(path) for path in certificate_paths],
        "bound": args.bound,
        "arity": args.arity,
        "state_limit": args.state_limit,
        "schema_like_detector_records": len(records),
        "nonpermutation_ybe_tables": len(nonperm_tables),
        "tables_with_detector_components": len(imported_nonperm_tables),
        "missing_table_count": len(missing_tables),
        "missing_ybe_tables": [list(table) for table in missing_tables],
        "extra_imported_table_count": len(extra_tables),
        "extra_imported_ybe_tables": [list(table) for table in extra_tables],
        "incomplete_detector_basis": bool(missing_tables),
        "detector_index": detector_index,
        "run_audit": args.run_audit,
        "row_count": len(rows),
        "rows": rows,
    }
    text = json.dumps(output, indent=2, sort_keys=True)
    if args.output:
        Path(args.output).write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    if args.require_all_55 and missing_tables:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
