from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Dict, Hashable, Iterable, List, Mapping, Sequence, Tuple

Element = Hashable
Pair = Tuple[Element, Element]
Word = Sequence[int]


@dataclass(frozen=True)
class FiniteBraidedSet:
    """A finite bijective set-theoretic braid solution."""

    elements: Tuple[Element, ...]
    R: Mapping[Pair, Pair]

    def __post_init__(self) -> None:
        object.__setattr__(self, "elements", tuple(self.elements))
        domain = {(a, b) for a in self.elements for b in self.elements}
        image = set(self.R.values())
        if set(self.R.keys()) != domain:
            missing = domain.difference(self.R.keys())
            extra = set(self.R.keys()).difference(domain)
            raise ValueError(f"R domain mismatch: missing={missing}, extra={extra}")
        if image != domain or len(image) != len(domain):
            raise ValueError("R must be a bijection on X x X")

    @property
    def inverse_R(self) -> Dict[Pair, Pair]:
        return {value: key for key, value in self.R.items()}

    def apply_R_at(
        self, tup: Sequence[Element], index: int, inverse: bool = False
    ) -> Tuple[Element, ...]:
        """Apply R to positions index,index+1 using zero-based indexing."""

        if index < 0 or index + 1 >= len(tup):
            raise IndexError(index)
        table = self.inverse_R if inverse else self.R
        out = list(tup)
        out[index], out[index + 1] = table[(out[index], out[index + 1])]
        return tuple(out)

    def braid_action(self, word: Word, tup: Sequence[Element]) -> Tuple[Element, ...]:
        """Apply a braid word to a tuple.

        Generators are one-based: `i` means sigma_i, `-i` means sigma_i^{-1}.
        """

        out = tuple(tup)
        for signed_generator in word:
            if signed_generator == 0:
                raise ValueError("braid generators are nonzero")
            inverse = signed_generator < 0
            index = abs(signed_generator) - 1
            out = self.apply_R_at(out, index, inverse=inverse)
        return out

    def action_table(self, word: Word, n: int) -> Dict[Tuple[Element, ...], Tuple[Element, ...]]:
        return {
            tuple(tup): self.braid_action(word, tup)
            for tup in product(self.elements, repeat=n)
        }

    def is_ybe(self) -> bool:
        """Check R_12 R_23 R_12 = R_23 R_12 R_23 on X^3."""

        for tup in product(self.elements, repeat=3):
            left = self.apply_R_at(self.apply_R_at(self.apply_R_at(tup, 0), 1), 0)
            right = self.apply_R_at(self.apply_R_at(self.apply_R_at(tup, 1), 0), 1)
            if left != right:
                return False
        return True

    def ybe_failures(self) -> List[Tuple[Tuple[Element, ...], Tuple[Element, ...], Tuple[Element, ...]]]:
        failures = []
        for tup in product(self.elements, repeat=3):
            left = self.apply_R_at(self.apply_R_at(self.apply_R_at(tup, 0), 1), 0)
            right = self.apply_R_at(self.apply_R_at(self.apply_R_at(tup, 1), 0), 1)
            if left != right:
                failures.append((tuple(tup), left, right))
        return failures


def identity_solution(elements: Iterable[Element]) -> FiniteBraidedSet:
    elems = tuple(elements)
    return FiniteBraidedSet(elems, {(a, b): (a, b) for a in elems for b in elems})


def opposite_solution(solution: FiniteBraidedSet) -> FiniteBraidedSet:
    """Return the side-opposite braided set ``P R P``.

    If ``R(x,y)=(lambda_x(y), rho_y(x))``, then the opposite solution has
    first-coordinate maps given by the right actions of ``R``:
    ``R^op(x,y)=(rho_x(y), lambda_y(x))``.
    """

    table = {}
    for x, y in product(solution.elements, repeat=2):
        u, v = solution.R[(y, x)]
        table[(x, y)] = (v, u)
    return FiniteBraidedSet(solution.elements, table)


def rack_solution(elements: Iterable[Element], op) -> FiniteBraidedSet:
    """Build the braided set associated to a rack operation.

    The convention is R(a,b) = (op(a,b), a), matching the Sawin question.
    """

    elems = tuple(elements)
    return FiniteBraidedSet(elems, {(a, b): (op(a, b), a) for a in elems for b in elems})


def is_rack_solution(solution: FiniteBraidedSet) -> bool:
    """Return whether a braided set is in rack form ``R(a,b)=(a▷b,a)``."""

    for left in solution.elements:
        images = []
        for right in solution.elements:
            first, second = solution.R[(left, right)]
            if second != left:
                return False
            images.append(first)
        if set(images) != set(solution.elements):
            return False
    return True


def product_solution(left: FiniteBraidedSet, right: FiniteBraidedSet) -> FiniteBraidedSet:
    """Return the Cartesian product of two finite braided sets."""

    elements = tuple((a, b) for a in left.elements for b in right.elements)
    table = {}
    for a1, b1 in elements:
        for a2, b2 in elements:
            u1, u2 = left.R[(a1, a2)]
            v1, v2 = right.R[(b1, b2)]
            table[((a1, b1), (a2, b2))] = ((u1, v1), (u2, v2))
    return FiniteBraidedSet(elements, table)


def flip_disjoint_union_solution(
    left: FiniteBraidedSet,
    right: FiniteBraidedSet,
    left_tag: Hashable = 0,
    right_tag: Hashable = 1,
) -> FiniteBraidedSet:
    """Return the disjoint union that flips across the two components.

    Elements are tagged as ``(left_tag, x)`` and ``(right_tag, y)``.  Crossings
    inside one component use that component's table, while mixed-component
    crossings are the flip ``(x,y) -> (y,x)``.  If both inputs are racks, this
    is the rack disjoint union with cross-component left translations acting
    trivially on the other component.
    """

    if left_tag == right_tag:
        raise ValueError("component tags must be distinct")
    left_elements = tuple((left_tag, element) for element in left.elements)
    right_elements = tuple((right_tag, element) for element in right.elements)
    elements = left_elements + right_elements
    left_set = set(left_elements)
    right_set = set(right_elements)
    table = {}
    for first in elements:
        for second in elements:
            first_tag, first_value = first
            second_tag, second_value = second
            if first in left_set and second in left_set:
                out_first, out_second = left.R[(first_value, second_value)]
                table[(first, second)] = (
                    (left_tag, out_first),
                    (left_tag, out_second),
                )
            elif first in right_set and second in right_set:
                out_first, out_second = right.R[(first_value, second_value)]
                table[(first, second)] = (
                    (right_tag, out_first),
                    (right_tag, out_second),
                )
            else:
                table[(first, second)] = (second, first)
    return FiniteBraidedSet(elements, table)


def is_subsolution_subset(
    solution: FiniteBraidedSet, subset: Iterable[Element]
) -> bool:
    """Return whether a subset is closed under the braided-set crossing."""

    selected = frozenset(subset)
    if not selected.issubset(set(solution.elements)):
        return False
    return all(
        solution.R[(left, right)][0] in selected
        and solution.R[(left, right)][1] in selected
        for left in selected
        for right in selected
    )


def subsolution(
    solution: FiniteBraidedSet, subset: Iterable[Element]
) -> FiniteBraidedSet:
    """Return the braided subset induced by a crossing-closed subset."""

    elems = tuple(subset)
    if not is_subsolution_subset(solution, elems):
        raise ValueError("subset is not closed under the braided-set crossing")
    selected = frozenset(elems)
    return FiniteBraidedSet(
        elems,
        {
            (left, right): solution.R[(left, right)]
            for left in selected
            for right in selected
        },
    )


def rack_quotient_obstructions(solution: FiniteBraidedSet) -> Tuple[Tuple[Element, Element, Element], ...]:
    """Return pairs obstructing a surjective rack cover of this braided set.

    If a rack `Y` maps onto `X` as a braided-set homomorphism, then for
    `R_X(x,y)=(u,v)` one must have `v=x`, because every rack crossing has
    second output equal to its left input.  The returned triples are
    `(x,y,v)` with `v != x`.
    """

    obstructions = []
    for x, y in product(solution.elements, repeat=2):
        _u, v = solution.R[(x, y)]
        if v != x:
            obstructions.append((x, y, v))
    return tuple(obstructions)


def admits_rack_quotient_cover(solution: FiniteBraidedSet) -> bool:
    """Return whether the direct rack-cover obstruction vanishes."""

    return not rack_quotient_obstructions(solution)
