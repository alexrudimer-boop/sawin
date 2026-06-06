"""Run the first finite rack endpoint-detector smoke test."""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.finite_braided_set import FiniteBraidedSet
from ybe_domination.finite_rack_sat import (
    Endpoint,
    build_context_presentation,
    detector_to_dict,
    find_rack_detector,
    trivial_monoid,
    verify_detector,
)
from ybe_domination.small_search import all_bijection_solutions


def constant_action_flip_solution() -> FiniteBraidedSet:
    return FiniteBraidedSet(
        (0, 1),
        {(i, j): (1 - j, i) for i in (0, 1) for j in (0, 1)},
    )


def main() -> None:
    solution = constant_action_flip_solution()
    monoid = trivial_monoid(generator_count=2)
    presentation = build_context_presentation(
        solution,
        monoid,
        Endpoint(prefix=(), letter=0, suffix=()),
        Endpoint(prefix=(), letter=1, suffix=()),
    )
    detector = find_rack_detector(presentation, qmax=2)
    if detector is None:
        raise SystemExit("no finite rack detector found")
    if not verify_detector(presentation, detector):
        raise SystemExit("detector certificate failed verification")

    payload = {
        "example": "two_element_constant_action_rack",
        "solution_is_ybe": solution.is_ybe(),
        "size_two_ybe_solution_count": sum(1 for _ in all_bijection_solutions(2)),
        "context_class_count": presentation.class_count,
        "context_equation_count": len(presentation.equations),
        "detector": detector_to_dict(presentation, detector),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
