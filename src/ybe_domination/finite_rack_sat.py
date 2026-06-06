"""Finite rack certificates for contextual endpoint detectors.

This module is intentionally small and exact.  It builds the finite
presentation of C_M(X) for fixed endpoints, collapses the transport
relations, and searches for a finite rack table plus an assignment separating
the two endpoint classes.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from itertools import permutations, product
from typing import Sequence

from .finite_braided_set import FiniteBraidedSet


@dataclass(frozen=True)
class Endpoint:
    """A contextual endpoint before evaluation in a finite monoid quotient."""

    prefix: tuple[int, ...]
    letter: int
    suffix: tuple[int, ...]


@dataclass(frozen=True)
class MonoidQuotient:
    """A finite quotient of the structure monoid L_X."""

    size: int
    identity: int
    mul: tuple[tuple[int, ...], ...]
    gen: tuple[int, ...]

    def eval_word(self, word: Sequence[int]) -> int:
        out = self.identity
        for letter in word:
            out = self.mul[out][self.gen[letter]]
        return out


@dataclass(frozen=True)
class ContextPresentation:
    """T-collapsed finite presentation fragment for C_M(X)."""

    class_count: int
    equations: tuple[tuple[int, int, int], ...]
    endpoint_class: int
    endpoint_prime_class: int
    raw_to_class: tuple[int, ...]


@dataclass(frozen=True)
class RackDetector:
    """A finite rack quotient certificate separating two endpoints."""

    q: int
    table: tuple[tuple[int, ...], ...]
    assignment: tuple[int, ...]


class _DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, left: int, right: int) -> bool:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1
        return True


class _ParityDSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.xor_to_parent = [0] * size

    def find(self, item: int) -> tuple[int, int]:
        parent = self.parent[item]
        if parent == item:
            return item, 0
        root, parity = self.find(parent)
        self.parent[item] = root
        self.xor_to_parent[item] ^= parity
        return self.parent[item], self.xor_to_parent[item]

    def union(self, left: int, right: int, parity: int) -> bool:
        left_root, left_xor = self.find(left)
        right_root, right_xor = self.find(right)
        if left_root == right_root:
            return (left_xor ^ right_xor) == parity
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
            left_xor, right_xor = right_xor, left_xor
        self.parent[right_root] = left_root
        self.xor_to_parent[right_root] = left_xor ^ right_xor ^ parity
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1
        return True


def trivial_monoid(generator_count: int) -> MonoidQuotient:
    """Return the one-element quotient of L_X."""

    return MonoidQuotient(
        size=1,
        identity=0,
        mul=((0,),),
        gen=(0,) * generator_count,
    )


def _validate_zero_based_solution(solution: FiniteBraidedSet) -> int:
    elements = tuple(solution.elements)
    if elements != tuple(range(len(elements))):
        raise ValueError("finite rack SAT helpers expect elements 0..d-1")
    return len(elements)


def _raw_id(d: int, monoid_size: int, prefix: int, letter: int, suffix: int) -> int:
    return (prefix * d + letter) * monoid_size + suffix


def _endpoint_raw_id(
    d: int, monoid: MonoidQuotient, endpoint: Endpoint
) -> int:
    return _raw_id(
        d,
        monoid.size,
        monoid.eval_word(endpoint.prefix),
        endpoint.letter,
        monoid.eval_word(endpoint.suffix),
    )


def build_context_presentation(
    solution: FiniteBraidedSet,
    monoid: MonoidQuotient,
    endpoint: Endpoint,
    endpoint_prime: Endpoint,
) -> ContextPresentation:
    """Build the finite T-collapsed contextual endpoint presentation.

    Relations use the Sawin rack convention R_Q(u,v)=(u triangleright v,u).
    For r_X(x,y)=(x',y'), the T-relation is

        [p,x, y s] = [p x', y', s],

    and the R-relation is

        [p,x, y s] triangleright [p x, y, s] = [p,x', y' s].
    """

    d = _validate_zero_based_solution(solution)
    if len(monoid.gen) != d:
        raise ValueError("monoid generator tuple must have one entry per X element")
    raw_count = monoid.size * d * monoid.size
    dsu = _DSU(raw_count)

    def gid(prefix: int, letter: int, suffix: int) -> int:
        return _raw_id(d, monoid.size, prefix, letter, suffix)

    for prefix in range(monoid.size):
        for suffix in range(monoid.size):
            for x in range(d):
                for y in range(d):
                    x_prime, y_prime = solution.R[(x, y)]
                    left = gid(prefix, x, monoid.mul[monoid.gen[y]][suffix])
                    right = gid(monoid.mul[prefix][monoid.gen[x_prime]], y_prime, suffix)
                    dsu.union(left, right)

    root_to_class: dict[int, int] = {}
    raw_to_class = []
    for raw in range(raw_count):
        root = dsu.find(raw)
        if root not in root_to_class:
            root_to_class[root] = len(root_to_class)
        raw_to_class.append(root_to_class[root])

    equations = set()
    for prefix in range(monoid.size):
        for suffix in range(monoid.size):
            for x in range(d):
                for y in range(d):
                    x_prime, y_prime = solution.R[(x, y)]
                    a = raw_to_class[gid(prefix, x, monoid.mul[monoid.gen[y]][suffix])]
                    b = raw_to_class[gid(monoid.mul[prefix][monoid.gen[x]], y, suffix)]
                    c = raw_to_class[gid(prefix, x_prime, monoid.mul[monoid.gen[y_prime]][suffix])]
                    equations.add((a, b, c))

    endpoint_class = raw_to_class[_endpoint_raw_id(d, monoid, endpoint)]
    endpoint_prime_class = raw_to_class[_endpoint_raw_id(d, monoid, endpoint_prime)]
    return ContextPresentation(
        class_count=len(root_to_class),
        equations=tuple(sorted(equations)),
        endpoint_class=endpoint_class,
        endpoint_prime_class=endpoint_prime_class,
        raw_to_class=tuple(raw_to_class),
    )


def is_rack_table(table: Sequence[Sequence[int]]) -> bool:
    """Check left-bijectivity and self-distributivity."""

    q = len(table)
    universe = list(range(q))
    if q == 0:
        return False
    for row in table:
        if len(row) != q or sorted(row) != universe:
            return False
    for a in range(q):
        for b in range(q):
            for c in range(q):
                left = table[table[a][b]][table[a][c]]
                right = table[a][table[b][c]]
                if left != right:
                    return False
    return True


@lru_cache(maxsize=None)
def enumerate_rack_tables(q: int) -> tuple[tuple[tuple[int, ...], ...], ...]:
    """Enumerate all labelled rack operation tables on q elements."""

    rows = tuple(permutations(range(q)))
    out = []
    for table in product(rows, repeat=q):
        candidate = tuple(tuple(row) for row in table)
        if is_rack_table(candidate):
            out.append(candidate)
    return tuple(out)


def _propagate_assignment(
    table: tuple[tuple[int, ...], ...],
    equations: tuple[tuple[int, int, int], ...],
    assignment: list[int],
) -> bool:
    q = len(table)
    inverse_rows = []
    for row in table:
        inverse = [0] * q
        for source, target in enumerate(row):
            inverse[target] = source
        inverse_rows.append(tuple(inverse))

    changed = True
    while changed:
        changed = False
        for left, right, out in equations:
            left_value = assignment[left]
            right_value = assignment[right]
            out_value = assignment[out]
            if left_value >= 0 and right_value >= 0:
                forced = table[left_value][right_value]
                if out_value >= 0 and out_value != forced:
                    return False
                if out_value < 0:
                    assignment[out] = forced
                    changed = True
            left_value = assignment[left]
            out_value = assignment[out]
            right_value = assignment[right]
            if left_value >= 0 and out_value >= 0:
                forced = inverse_rows[left_value][out_value]
                if right_value >= 0 and right_value != forced:
                    return False
                if right_value < 0:
                    assignment[right] = forced
                    changed = True
    return True


def _assignment_for_fixed_rack(
    presentation: ContextPresentation,
    table: tuple[tuple[int, ...], ...],
) -> tuple[int, ...] | None:
    if presentation.class_count == 0:
        return None
    if presentation.endpoint_class == presentation.endpoint_prime_class:
        return None
    q = len(table)
    if q < 2:
        return None

    base = [-1] * presentation.class_count
    base[presentation.endpoint_class] = 0
    base[presentation.endpoint_prime_class] = 1
    if not _propagate_assignment(table, presentation.equations, base):
        return None

    variables = []
    seen = set()
    for equation in presentation.equations:
        for variable in equation:
            if variable not in seen:
                seen.add(variable)
                variables.append(variable)
    for variable in range(presentation.class_count):
        if variable not in seen:
            variables.append(variable)

    def search(current: list[int]) -> tuple[int, ...] | None:
        if not _propagate_assignment(table, presentation.equations, current):
            return None
        try:
            variable = next(item for item in variables if current[item] < 0)
        except StopIteration:
            return tuple(current)
        for value in range(q):
            candidate = list(current)
            candidate[variable] = value
            result = search(candidate)
            if result is not None:
                return result
        return None

    return search(base)


def _q2_detector_with_right_parity(
    presentation: ContextPresentation,
    table: tuple[tuple[int, ...], tuple[int, ...]],
    equation_parity: int,
) -> RackDetector | None:
    if presentation.endpoint_class == presentation.endpoint_prime_class:
        return None
    dsu = _ParityDSU(presentation.class_count)
    for _left, right, out in presentation.equations:
        if not dsu.union(right, out, equation_parity):
            return None
    if not dsu.union(presentation.endpoint_class, presentation.endpoint_prime_class, 1):
        return None

    endpoint_root, endpoint_value = dsu.find(presentation.endpoint_class)
    assignment = []
    root_values = {endpoint_root: endpoint_value}
    for item in range(presentation.class_count):
        root, parity = dsu.find(item)
        if root not in root_values:
            root_values[root] = 0
        assignment.append(root_values[root] ^ parity)

    detector = RackDetector(q=2, table=table, assignment=tuple(assignment))
    if verify_detector(presentation, detector):
        return detector
    return None


def q2_fast_detector(presentation: ContextPresentation) -> RackDetector | None:
    """Use the two q=2 racks as parity-DSU detector tests.

    The identity-action rack T[a,b]=b turns each equation a▷b=c into b=c.
    The flip-action rack T[a,b]=1-b turns each equation into b xor c = 1.
    """

    identity_table = ((0, 1), (0, 1))
    detector = _q2_detector_with_right_parity(
        presentation, identity_table, equation_parity=0
    )
    if detector is not None:
        return detector
    flip_table = ((1, 0), (1, 0))
    return _q2_detector_with_right_parity(
        presentation, flip_table, equation_parity=1
    )


def verify_detector(
    presentation: ContextPresentation,
    detector: RackDetector,
) -> bool:
    """Verify a finite rack detector certificate."""

    if detector.q != len(detector.table):
        return False
    if len(detector.assignment) != presentation.class_count:
        return False
    if not is_rack_table(detector.table):
        return False
    if any(value < 0 or value >= detector.q for value in detector.assignment):
        return False
    for left, right, out in presentation.equations:
        if detector.table[detector.assignment[left]][detector.assignment[right]] != detector.assignment[out]:
            return False
    return (
        detector.assignment[presentation.endpoint_class]
        != detector.assignment[presentation.endpoint_prime_class]
    )


def find_rack_detector(
    presentation: ContextPresentation,
    qmax: int,
) -> RackDetector | None:
    """Search labelled rack tables of size at most qmax for a separator."""

    if presentation.endpoint_class == presentation.endpoint_prime_class:
        return None
    for q in range(2, qmax + 1):
        if q == 2:
            detector = q2_fast_detector(presentation)
            if detector is not None:
                return detector
            continue
        for table in enumerate_rack_tables(q):
            assignment = _assignment_for_fixed_rack(presentation, table)
            if assignment is None:
                continue
            detector = RackDetector(q=q, table=table, assignment=assignment)
            if verify_detector(presentation, detector):
                return detector
    return None


def detector_to_dict(
    presentation: ContextPresentation,
    detector: RackDetector,
) -> dict[str, object]:
    """Return a JSON-friendly finite detector certificate."""

    return {
        "type": "finite_rack_detector",
        "q": detector.q,
        "rack_table": [list(row) for row in detector.table],
        "assignment": list(detector.assignment),
        "endpoint_class": presentation.endpoint_class,
        "endpoint_prime_class": presentation.endpoint_prime_class,
        "endpoint_value": detector.assignment[presentation.endpoint_class],
        "endpoint_prime_value": detector.assignment[presentation.endpoint_prime_class],
    }
