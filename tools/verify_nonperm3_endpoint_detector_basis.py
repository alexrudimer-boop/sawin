"""Verify reconstructed non-permutation endpoint detector basis certificates."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.nonperm3_endpoint_detector_basis import (  # noqa: E402
    verify_detector_basis_payload,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate_json")
    parser.add_argument(
        "--require-candidate-partition",
        action="store_true",
        help=(
            "Require the built-in covered/baseline/unresolved candidate "
            "partition check. This is currently always enforced."
        ),
    )
    args = parser.parse_args()

    payload = json.loads(Path(args.certificate_json).read_text(encoding="utf-8"))
    failures = verify_detector_basis_payload(payload)
    if failures:
        print("FAILED nonperm3 endpoint detector basis verification")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("OK nonperm3 endpoint detector basis verification")
    for key in (
        "source_batch",
        "arity",
        "qmax",
        "positive_detector_schemas",
        "reconstructed_positive_detector_schemas",
        "positive_detector_coverages",
        "baseline_covered_candidate_count",
        "unresolved_obstruction_candidates",
        "combined_positive_detector_coverages",
        "remaining_unresolved_candidates",
        "coverage_partition_verified",
    ):
        if key in payload:
            print(f"{key} {payload[key]}")


if __name__ == "__main__":
    main()
