from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Dict, Mapping, Tuple

from .local_interval import (
    Color,
    FibrePoint,
    LocalInterval,
    Partition,
    canonical_partition,
    same_block,
    universal_partition,
)


RelationFamily = Mapping[Color, Partition]


@dataclass(frozen=True)
class ContextRetractionStep:
    depth: int
    family: RelationFamily
    changed: bool


@dataclass(frozen=True)
class ContextRetractionAudit:
    stable_depth: int
    initial_family: RelationFamily
    initial_admissible: bool
    stable_family: RelationFamily
    admissible: bool
    kind: str
    steps: Tuple[ContextRetractionStep, ...]


@dataclass(frozen=True)
class ProductPermutationWitness:
    left_maps: Mapping[Tuple[Color, Color], Mapping[FibrePoint, FibrePoint]]
    right_maps: Mapping[Tuple[Color, Color], Mapping[FibrePoint, FibrePoint]]


@dataclass(frozen=True)
class DirectProductWitness:
    left_maps: Mapping[Tuple[Color, Color], Mapping[FibrePoint, FibrePoint]]
    right_maps: Mapping[Tuple[Color, Color], Mapping[FibrePoint, FibrePoint]]


def _partition_from_pairs(
    items: Tuple[FibrePoint, ...], related_pairs: set[Tuple[FibrePoint, FibrePoint]]
) -> Partition:
    parent = {item: item for item in items}

    def find(item):
        while parent[item] != item:
            parent[item] = parent[parent[item]]
            item = parent[item]
        return item

    def union(left, right) -> None:
        root_left = find(left)
        root_right = find(right)
        if root_left != root_right:
            parent[root_right] = root_left

    for left, right in related_pairs:
        union(left, right)
    blocks: Dict[FibrePoint, list[FibrePoint]] = {}
    for item in items:
        blocks.setdefault(find(item), []).append(item)
    return canonical_partition(blocks.values())


def meet_partition(left: Partition, right: Partition) -> Partition:
    """Return the common refinement of two partitions on the same fibre."""

    return canonical_partition(
        left_block.intersection(right_block)
        for left_block in left
        for right_block in right
    )


def meet_relation_families(
    interval: LocalInterval, *families: RelationFamily
) -> Dict[Color, Partition]:
    """Return the fibrewise common refinement of relation families."""

    if not families:
        raise ValueError("at least one family is required")
    current = {color: families[0][color] for color in interval.colors}
    for family in families[1:]:
        current = {
            color: meet_partition(current[color], family[color])
            for color in interval.colors
        }
    return current


def inverse_local_interval(interval: LocalInterval) -> LocalInterval:
    """Return the local interval obtained by inverting every coloured bijection."""

    inverse_base = {
        target: source for source, target in interval.base_R.items()
    }
    inverse_T = {}
    for a, b in product(interval.colors, repeat=2):
        c, d = interval.base_R[(a, b)]
        for x in interval.fibres[a]:
            for y in interval.fibres[b]:
                u, v = interval.T[(a, b, x, y)]
                inverse_T[(c, d, u, v)] = (x, y)
    return LocalInterval(
        colors=interval.colors,
        fibres=interval.fibres,
        base_R=inverse_base,
        T=inverse_T,
    )


def one_step_context_profile_family(interval: LocalInterval) -> Dict[Color, Partition]:
    """Return the standard local retraction relation.

    A point indexes two families of unary maps: the first-output maps
    ``y -> pr_1 T(x,y)`` and the second-output maps ``y -> pr_2 T(y,x)``.
    Equality of these profiles is the coloured version of the usual
    retraction relation for a set-theoretic solution.
    """

    family: Dict[Color, Partition] = {}
    for color in interval.colors:
        related_pairs: set[Tuple[FibrePoint, FibrePoint]] = set()
        for left, right in product(interval.fibres[color], repeat=2):
            equivalent = True
            for other_color in interval.colors:
                for other in interval.fibres[other_color]:
                    if interval.T[(color, other_color, left, other)][0] != interval.T[
                        (color, other_color, right, other)
                    ][0]:
                        equivalent = False
                        break
                    if interval.T[(other_color, color, other, left)][1] != interval.T[
                        (other_color, color, other, right)
                    ][1]:
                        equivalent = False
                        break
                if not equivalent:
                    break
            if equivalent:
                related_pairs.add((left, right))
        family[color] = _partition_from_pairs(interval.fibres[color], related_pairs)
    return family


def two_sided_context_profile_family(interval: LocalInterval) -> Dict[Color, Partition]:
    """Return profile equality for the table and for its inverse table.

    The forward profile is the usual equality of first-output and second-output
    unary maps.  The inverse profile adds the same test after replacing each
    coloured bijection by its inverse.  This stronger relation avoids using
    nondegenerate one-sided cancellation when the underlying YBE solution is
    merely bijective on pairs.
    """

    inverse = inverse_local_interval(interval)
    return meet_relation_families(
        interval,
        one_step_context_profile_family(interval),
        one_step_context_profile_family(inverse),
    )


def one_step_coretraction_profile_family(interval: LocalInterval) -> Dict[Color, Partition]:
    """Return the dual local retraction relation.

    A point is now viewed as an input coordinate rather than as the parameter
    indexing one-sided operations: the profile records the first output when
    the point is the right input and the second output when it is the left
    input.
    """

    family: Dict[Color, Partition] = {}
    for color in interval.colors:
        related_pairs: set[Tuple[FibrePoint, FibrePoint]] = set()
        for left, right in product(interval.fibres[color], repeat=2):
            equivalent = True
            for other_color in interval.colors:
                for other in interval.fibres[other_color]:
                    if interval.T[(other_color, color, other, left)][0] != interval.T[
                        (other_color, color, other, right)
                    ][0]:
                        equivalent = False
                        break
                    if interval.T[(color, other_color, left, other)][1] != interval.T[
                        (color, other_color, right, other)
                    ][1]:
                        equivalent = False
                        break
                if not equivalent:
                    break
            if equivalent:
                related_pairs.add((left, right))
        family[color] = _partition_from_pairs(interval.fibres[color], related_pairs)
    return family


def two_sided_coretraction_profile_family(interval: LocalInterval) -> Dict[Color, Partition]:
    """Return dual profile equality for the table and its inverse table."""

    inverse = inverse_local_interval(interval)
    return meet_relation_families(
        interval,
        one_step_coretraction_profile_family(interval),
        one_step_coretraction_profile_family(inverse),
    )


def context_closure_step(
    interval: LocalInterval, family: RelationFamily
) -> Dict[Color, Partition]:
    """Refine a family by one round of opposite unary context closure."""

    next_family: Dict[Color, Partition] = {}
    for color in interval.colors:
        related_pairs: set[Tuple[FibrePoint, FibrePoint]] = set()
        for left, right in product(interval.fibres[color], repeat=2):
            if not same_block(family[color], left, right):
                continue
            equivalent = True
            for other_color in interval.colors:
                for other in interval.fibres[other_color]:
                    first_left = interval.T[(other_color, color, other, left)][0]
                    first_right = interval.T[(other_color, color, other, right)][0]
                    first_color = interval.base_R[(other_color, color)][0]
                    if not same_block(family[first_color], first_left, first_right):
                        equivalent = False
                        break
                    second_left = interval.T[(color, other_color, left, other)][1]
                    second_right = interval.T[(color, other_color, right, other)][1]
                    second_color = interval.base_R[(color, other_color)][1]
                    if not same_block(family[second_color], second_left, second_right):
                        equivalent = False
                        break
                if not equivalent:
                    break
            if equivalent:
                related_pairs.add((left, right))
        next_family[color] = _partition_from_pairs(interval.fibres[color], related_pairs)
    return next_family


def _family_key(interval: LocalInterval, family: RelationFamily):
    return tuple((color, family[color]) for color in interval.colors)


def _family_kind(interval: LocalInterval, family: RelationFamily) -> str:
    equality = all(len(family[color]) == len(interval.fibres[color]) for color in interval.colors)
    universal = all(
        family[color] == universal_partition(interval.fibres[color])
        for color in interval.colors
    )
    if equality:
        return "equality"
    if universal:
        return "universal"
    if any(family[color] == universal_partition(interval.fibres[color]) for color in interval.colors):
        return "semisplit_or_mixed"
    return "proper_mixed"


def product_permutation_witness(
    interval: LocalInterval,
) -> ProductPermutationWitness | None:
    """Return fibre-permutation data when `T(x,y)` splits as `(L(y), R(x))`.

    In this branch the first output is independent of the left fibre point and
    the second output is independent of the right fibre point.  Since each
    `T_{a,b}` is already a bijection, the two coordinate maps are bijections
    between the corresponding source and target fibres.
    """

    left_maps: Dict[Tuple[Color, Color], Dict[FibrePoint, FibrePoint]] = {}
    right_maps: Dict[Tuple[Color, Color], Dict[FibrePoint, FibrePoint]] = {}
    for a, b in product(interval.colors, repeat=2):
        c, d = interval.base_R[(a, b)]
        left_map: Dict[FibrePoint, FibrePoint] = {}
        for y in interval.fibres[b]:
            values = {interval.T[(a, b, x, y)][0] for x in interval.fibres[a]}
            if len(values) != 1:
                return None
            left_map[y] = next(iter(values))
        if set(left_map.values()) != set(interval.fibres[c]):
            return None
        right_map: Dict[FibrePoint, FibrePoint] = {}
        for x in interval.fibres[a]:
            values = {interval.T[(a, b, x, y)][1] for y in interval.fibres[b]}
            if len(values) != 1:
                return None
            right_map[x] = next(iter(values))
        if set(right_map.values()) != set(interval.fibres[d]):
            return None
        left_maps[(a, b)] = left_map
        right_maps[(a, b)] = right_map
    return ProductPermutationWitness(left_maps=left_maps, right_maps=right_maps)


def direct_product_witness(interval: LocalInterval) -> DirectProductWitness | None:
    """Return coordinate-permutation data when `T(x,y)` splits as `(L(x), R(y))`."""

    left_maps: Dict[Tuple[Color, Color], Dict[FibrePoint, FibrePoint]] = {}
    right_maps: Dict[Tuple[Color, Color], Dict[FibrePoint, FibrePoint]] = {}
    for a, b in product(interval.colors, repeat=2):
        c, d = interval.base_R[(a, b)]
        left_map: Dict[FibrePoint, FibrePoint] = {}
        for x in interval.fibres[a]:
            values = {interval.T[(a, b, x, y)][0] for y in interval.fibres[b]}
            if len(values) != 1:
                return None
            left_map[x] = next(iter(values))
        if set(left_map.values()) != set(interval.fibres[c]):
            return None
        right_map: Dict[FibrePoint, FibrePoint] = {}
        for y in interval.fibres[b]:
            values = {interval.T[(a, b, x, y)][1] for x in interval.fibres[a]}
            if len(values) != 1:
                return None
            right_map[y] = next(iter(values))
        if set(right_map.values()) != set(interval.fibres[d]):
            return None
        left_maps[(a, b)] = left_map
        right_maps[(a, b)] = right_map
    return DirectProductWitness(left_maps=left_maps, right_maps=right_maps)


def _two_sided_stable_audit(
    interval: LocalInterval, initial: RelationFamily
) -> ContextRetractionAudit:
    inverse = inverse_local_interval(interval)
    initial_admissible = interval.is_admissible_congruence_family(initial)
    steps = [ContextRetractionStep(depth=0, family=initial, changed=True)]
    current = initial
    depth = 0
    while True:
        depth += 1
        next_family = meet_relation_families(
            interval,
            context_closure_step(interval, current),
            context_closure_step(inverse, current),
        )
        changed = _family_key(interval, next_family) != _family_key(interval, current)
        steps.append(ContextRetractionStep(depth=depth, family=next_family, changed=changed))
        current = next_family
        if not changed:
            break
    return ContextRetractionAudit(
        stable_depth=depth,
        initial_family=initial,
        initial_admissible=initial_admissible,
        stable_family=current,
        admissible=interval.is_admissible_congruence_family(current),
        kind=_family_kind(interval, current),
        steps=tuple(steps),
    )


def context_retraction_audit(interval: LocalInterval) -> ContextRetractionAudit:
    """Compute the two-sided finite context-profile congruence candidate.

    The initial family identifies points with identical one-sided local
    profiles for both the table and its inverse.  Repeated closure by opposite
    variable contexts for both orientations gives the largest relation below
    that two-sided profile relation that is stable under all one-sided local
    operations.  Forward closure gives transport into the target relation, and
    inverse closure gives the reverse inclusion; hence the stable family is an
    exact admissible local congruence for arbitrary finite coloured bijections.
    """

    initial = two_sided_context_profile_family(interval)
    return _two_sided_stable_audit(interval, initial)


def context_coretraction_audit(interval: LocalInterval) -> ContextRetractionAudit:
    """Compute the two-sided dual context-profile congruence candidate.

    The initial family identifies points with identical input-coordinate
    profiles for both the table and its inverse.  The same two-sided closure
    argument used for `context_retraction_audit` makes the stable family an
    exact admissible local congruence.
    """

    initial = two_sided_coretraction_profile_family(interval)
    return _two_sided_stable_audit(interval, initial)
