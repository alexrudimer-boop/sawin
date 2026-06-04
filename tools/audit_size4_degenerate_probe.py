from __future__ import annotations

import argparse
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination.finite_braided_set import FiniteBraidedSet, rack_solution
from ybe_domination.residual import action_permutation

Permutation = Tuple[int, ...]


@dataclass(frozen=True)
class RackImageOrderRow:
    name: str
    n: int
    tuple_count: int
    image_order: int
    expected_order: int | None

    @property
    def matches_expected(self) -> bool:
        return self.expected_order is None or self.image_order == self.expected_order


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return ``left`` after ``right``."""

    if len(left) != len(right):
        raise ValueError("permutations must have the same degree")
    return tuple(left[right[index]] for index in range(len(left)))


def invert(permutation: Permutation) -> Permutation:
    inverse = [0] * len(permutation)
    for index, image in enumerate(permutation):
        inverse[image] = index
    return tuple(inverse)


def generated_permutation_count(generators: Iterable[Permutation]) -> int:
    """Count a generated permutation group without building a multiplication table."""

    gens = tuple(generators)
    if not gens:
        return 1
    degree = len(gens[0])
    if any(len(gen) != degree for gen in gens):
        raise ValueError("generators must have the same degree")
    symmetric_gens = tuple(dict.fromkeys(gens + tuple(invert(gen) for gen in gens)))
    identity = tuple(range(degree))
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for gen in symmetric_gens:
            candidate = compose(gen, current)
            if candidate in seen:
                continue
            seen.add(candidate)
            queue.append(candidate)
    return len(seen)


def size_two_cyclic_rack() -> FiniteBraidedSet:
    """The rack with crossing ``R(a,b)=(1-b,a)``."""

    return rack_solution((0, 1), lambda _left, right: 1 - right)


def size_three_degenerate_universal_rack() -> FiniteBraidedSet:
    """The rack with left translations ``L_0=L_1=id`` and ``L_2=(01)``."""

    def op(left: int, right: int) -> int:
        if left in (0, 1):
            return right
        if right in (0, 1):
            return 1 - right
        return 2

    return rack_solution((0, 1, 2), op)


def image_order(rack: FiniteBraidedSet, n: int) -> int:
    if n < 1:
        raise ValueError("n must be positive")
    generators = tuple(action_permutation(rack, n, (i,)) for i in range(1, n))
    return generated_permutation_count(generators)


def audit_rack(
    name: str,
    rack: FiniteBraidedSet,
    degrees: Sequence[int],
    expected: dict[int, int],
) -> tuple[RackImageOrderRow, ...]:
    if not rack.is_ybe():
        raise ValueError(f"{name} is not a YBE solution")
    rows = []
    for n in degrees:
        rows.append(
            RackImageOrderRow(
                name=name,
                n=n,
                tuple_count=len(rack.elements) ** n,
                image_order=image_order(rack, n),
                expected_order=expected.get(n),
            )
        )
    return tuple(rows)


def render_markdown(rows: Sequence[RackImageOrderRow]) -> str:
    lines = [
        "| rack | n | tuple count | image order | expected | status |",
        "| --- | ---: | ---: | ---: | ---: | --- |",
    ]
    for row in rows:
        expected = "" if row.expected_order is None else str(row.expected_order)
        status = "ok" if row.matches_expected else "mismatch"
        lines.append(
            f"| {row.name} | {row.n} | {row.tuple_count} | "
            f"{row.image_order} | {expected} | {status} |"
        )
    return "\n".join(lines)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Audit the rack image-order sequences appearing in the size-4 "
            "degenerate non-involutive probe."
        )
    )
    parser.add_argument("--max-c2", type=int, default=6)
    parser.add_argument("--max-size3", type=int, default=5)
    args = parser.parse_args(argv)

    c2_degrees = tuple(range(2, args.max_c2 + 1))
    size3_degrees = tuple(range(2, args.max_size3 + 1))
    rows = []
    rows.extend(
        audit_rack(
            "C2 cyclic rack R(a,b)=(1-b,a)",
            size_two_cyclic_rack(),
            c2_degrees,
            {2: 4, 3: 24, 4: 192, 5: 1920, 6: 23040},
        )
    )
    rows.extend(
        audit_rack(
            "size-3 rack L0=L1=id, L2=(01)",
            size_three_degenerate_universal_rack(),
            size3_degrees,
            {2: 4, 3: 48, 4: 1536, 5: 122880},
        )
    )
    print(render_markdown(rows))
    return 0 if all(row.matches_expected for row in rows) else 1


if __name__ == "__main__":
    raise SystemExit(main())
