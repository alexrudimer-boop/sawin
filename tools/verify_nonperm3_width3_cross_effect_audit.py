"""Verify a nonperm3 width-3 componentwise cross-effect audit JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.nonperm3_detector_products import (  # noqa: E402
    verify_width3_audit_payload,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("audit_json")
    parser.add_argument(
        "--require-complete-basis",
        action="store_true",
        help="Require detector components for all 55 non-permutation tables.",
    )
    parser.add_argument(
        "--require-run-audit",
        action="store_true",
        help="Require one audit row for every detector-index row.",
    )
    parser.add_argument(
        "--require-untruncated-trivial",
        action="store_true",
        help="Require every audit row to be untruncated with quotient_size 1.",
    )
    args = parser.parse_args()

    payload = json.loads(Path(args.audit_json).read_text(encoding="utf-8"))
    failures = list(verify_width3_audit_payload(payload))

    detector_index = payload.get("detector_index", [])
    rows = payload.get("rows", [])
    if args.require_complete_basis:
        if payload.get("incomplete_detector_basis") is not False:
            failures.append("complete basis required but incomplete_detector_basis is true")
        if payload.get("missing_table_count") != 0:
            failures.append("complete basis required but missing_table_count is nonzero")
        if len(detector_index) != 55:
            failures.append("complete basis required but detector_index length is not 55")
    if args.require_run_audit:
        if payload.get("run_audit") is not True:
            failures.append("run audit required but run_audit is not true")
        if len(rows) != len(detector_index):
            failures.append("run audit required but row count differs from detector_index")
    if args.require_untruncated_trivial:
        if not rows:
            failures.append("untruncated trivial rows required but no rows are present")
        for index, row in enumerate(rows if isinstance(rows, list) else []):
            if row.get("truncated") is not False:
                failures.append(f"rows[{index}] is truncated")
            if row.get("quotient_size") != 1:
                failures.append(f"rows[{index}] has nontrivial or unknown quotient_size")
            if row.get("quotient_nontrivial") is not False:
                failures.append(f"rows[{index}] has nontrivial or unknown quotient flag")

    if failures:
        print("FAILED nonperm3 width-3 audit verification")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("OK nonperm3 width-3 audit verification")
    print(f"detector_index_rows {len(detector_index)}")
    print(f"audit_rows {len(rows)}")
    print(f"incomplete_detector_basis {payload.get('incomplete_detector_basis')}")


if __name__ == "__main__":
    main()
