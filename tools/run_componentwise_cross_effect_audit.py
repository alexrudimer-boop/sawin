"""Run a componentwise realized parabolic cross-effect audit.

Input JSON shape:

{
  "ybe_table": [0, 3, 6, 1, 4, 7, 5, 2, 8],
  "detectors": [
    {"rack_table": [[0, 1], [0, 1]]}
  ],
  "bound": 3,
  "arity": 4,
  "state_limit": 100000
}
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import asdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    componentwise_realized_parabolic_cross_effect_audit,
    rack_solution,
)
from ybe_domination.finite_rack_sat import is_rack_table  # noqa: E402


def solution_from_flat_table(table: list[int]) -> FiniteBraidedSet:
    size_squared = len(table)
    size = int(size_squared**0.5)
    if size * size != size_squared:
        raise ValueError("flat YBE table length must be a square")
    pairs = [(x, y) for x in range(size) for y in range(size)]
    values = [divmod(value, size) for value in table]
    return FiniteBraidedSet(tuple(range(size)), dict(zip(pairs, values)))


def rack_from_table(table: list[list[int]]) -> FiniteBraidedSet:
    rack_table = tuple(tuple(row) for row in table)
    if not is_rack_table(rack_table):
        raise ValueError(f"invalid rack table: {table!r}")
    return rack_solution(
        tuple(range(len(rack_table))),
        lambda left, right: rack_table[left][right],
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input_json")
    args = parser.parse_args()

    if args.input_json == "-":
        payload = json.loads(sys.stdin.read())
    else:
        payload = json.loads(Path(args.input_json).read_text(encoding="utf-8"))
    solution = solution_from_flat_table(payload["ybe_table"])
    if not solution.is_ybe():
        raise SystemExit("input ybe_table is not a YBE solution")

    detectors = tuple(
        rack_from_table(entry["rack_table"])
        for entry in payload["detectors"]
    )
    audit = componentwise_realized_parabolic_cross_effect_audit(
        solution,
        detectors,
        bound=int(payload["bound"]),
        n=int(payload["arity"]),
        state_limit=int(payload.get("state_limit", 100_000)),
    )
    audit_data = asdict(audit)
    audit_data["arity"] = audit_data["n"]
    output = {
        "ybe_table": payload["ybe_table"],
        "detector_component_count": len(detectors),
        "detector_component_sizes": [len(detector.elements) for detector in detectors],
        **audit_data,
    }
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
