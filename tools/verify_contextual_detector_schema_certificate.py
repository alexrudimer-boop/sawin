"""Verify contextual finite-rack detector schema records in a certificate JSON."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.nonperm3_detector_products import (  # noqa: E402
    contextual_detector_payload_failures,
    contextual_detector_payload_summary,
)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("certificate_json")
    parser.add_argument(
        "--require-records",
        action="store_true",
        help="Fail if no contextual detector records are found.",
    )
    args = parser.parse_args()

    payload = json.loads(Path(args.certificate_json).read_text(encoding="utf-8"))
    summary = contextual_detector_payload_summary(payload)
    failures = list(contextual_detector_payload_failures(payload))
    if not args.require_records and failures == ["no contextual detector records found"]:
        failures = []

    if failures:
        print("FAILED contextual detector schema verification")
        for key, value in summary.items():
            print(f"{key} {value}")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("OK contextual detector schema verification")
    for key, value in summary.items():
        print(f"{key} {value}")


if __name__ == "__main__":
    main()
