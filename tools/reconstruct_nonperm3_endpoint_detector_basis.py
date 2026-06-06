"""Reconstruct non-permutation size-three endpoint detector schema certificates."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.nonperm3_endpoint_detector_basis import (  # noqa: E402
    REPORTED_Q5_SHA256,
    canonical_payload_sha256,
    reconstruct_detector_basis_payload,
    verify_detector_basis_payload,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--arity", type=int, required=True)
    parser.add_argument("--qmax", type=int, required=True)
    parser.add_argument("--monoid-family", action="append", required=True)
    parser.add_argument("--baseline", default=None)
    parser.add_argument("--emit-new-q5-only", action="store_true")
    parser.add_argument(
        "--no-enforce-checkpoint-counts",
        action="store_true",
        help="Skip archived count checks; intended only for development probes.",
    )
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    baseline = None
    if args.baseline:
        baseline = json.loads(Path(args.baseline).read_text(encoding="utf-8"))

    payload = reconstruct_detector_basis_payload(
        arity=args.arity,
        qmax=args.qmax,
        monoid_family_names=tuple(args.monoid_family),
        baseline_payload=baseline,
        emit_new_q5_only=args.emit_new_q5_only,
        enforce_checkpoint_counts=not args.no_enforce_checkpoint_counts,
    )
    payload["reconstructed_sha256"] = canonical_payload_sha256(payload)
    if args.emit_new_q5_only:
        payload["sha256_matches_reported"] = (
            payload["reconstructed_sha256"] == REPORTED_Q5_SHA256
        )

    failures = verify_detector_basis_payload(payload)
    if failures:
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    text = json.dumps(payload, indent=2, sort_keys=True)
    Path(args.output).write_text(text + "\n", encoding="utf-8")
    print("OK nonperm3 endpoint detector basis reconstruction")
    print(f"output {args.output}")
    print(f"positive_detector_schemas {payload['positive_detector_schemas']}")
    print(f"positive_detector_coverages {payload['positive_detector_coverages']}")
    print(
        "unresolved_obstruction_candidates "
        f"{payload['unresolved_obstruction_candidates']}"
    )
    print(f"reconstructed_sha256 {payload['reconstructed_sha256']}")


if __name__ == "__main__":
    main()
