from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Dict, Mapping, Sequence, Tuple

from .artin_longitudes import BraidWord, has_identity_longitude_signature
from .finite_braided_set import FiniteBraidedSet
from .finite_group import FiniteGroup
from .local_interval import Color, FibrePoint, LocalInterval
from .residual import QuotientMap, bounded_words, is_identity_action

TotalPoint = Tuple[Color, FibrePoint]


def solution_from_local_interval(interval: LocalInterval) -> QuotientMap:
    """Realize a local interval as a finite braided-set quotient map."""

    quotient = FiniteBraidedSet(interval.colors, interval.base_R)
    elements = tuple((color, point) for color in interval.colors for point in interval.fibres[color])
    table = {}
    for (a, x), (b, y) in product(elements, repeat=2):
        c, d = interval.base_R[(a, b)]
        u, v = interval.T[(a, b, x, y)]
        table[((a, x), (b, y))] = ((c, u), (d, v))
    total = FiniteBraidedSet(elements, table)
    return QuotientMap(total, quotient, {element: element[0] for element in elements})


@dataclass(frozen=True)
class BoundedObstruction:
    braid_word: Tuple[int, ...]
    moved_base: Tuple[object, ...]
    moved_tuple: Tuple[object, ...]
    moved_image: Tuple[object, ...]
    invisible_groups: Tuple[str, ...]
    visible_groups: Tuple[str, ...]


def group_name(group: FiniteGroup) -> str:
    return f"|G|={len(group.elements)}"


def longitude_visibility_profile(
    groups: Mapping[str, FiniteGroup],
    n: int,
    braid_word: BraidWord,
) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    invisible = []
    visible = []
    for name, group in groups.items():
        if has_identity_longitude_signature(group, n, braid_word):
            invisible.append(name)
        else:
            visible.append(name)
    return tuple(invisible), tuple(visible)


def bounded_local_obstructions(
    interval: LocalInterval,
    base_detector: FiniteBraidedSet,
    groups: Mapping[str, FiniteGroup],
    n: int,
    max_word_length: int,
) -> Dict[Tuple[int, ...], BoundedObstruction]:
    """Find bounded words that move the interval and fool all listed groups."""

    qmap = solution_from_local_interval(interval)
    out: Dict[Tuple[int, ...], BoundedObstruction] = {}
    for word in bounded_words(n, max_word_length):
        if not word:
            continue
        if not is_identity_action(base_detector, n, word):
            continue
        moved = qmap.moved_residual_tuple(n, word)
        if moved is None:
            continue
        invisible, visible = longitude_visibility_profile(groups, n, word)
        if visible:
            continue
        base, tup, image = moved
        out[word] = BoundedObstruction(word, base, tup, image, invisible, visible)
    return out


def moved_by_interval(interval: LocalInterval, n: int, braid_word: Sequence[int]):
    return solution_from_local_interval(interval).moved_residual_tuple(n, braid_word)

