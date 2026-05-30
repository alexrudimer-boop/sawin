from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Tuple

from .artin_longitudes import (
    BraidWord,
    FreeWord,
    artin_longitudes,
    has_identity_longitude_signature,
    longitude_subgroup_profile,
)
from .finite_group import FiniteGroup
from .group_laws import is_law_on_group


@dataclass(frozen=True)
class LastStrandLawExactnessAudit:
    """Finite check of the point-pushing law/kernel equivalence."""

    group_order: int
    arity: int
    braid_index: int
    braid_word: BraidWord
    word_is_law: bool
    identity_longitude_signature: bool

    @property
    def point_pushing_exactness_holds(self) -> bool:
        return self.word_is_law == self.identity_longitude_signature


def invert_braid_word(word: BraidWord) -> Tuple[int, ...]:
    return tuple(-letter for letter in reversed(word))


def reverse_braid_word(n: int, word: BraidWord) -> Tuple[int, ...]:
    """Apply the strand-reversal automorphism `sigma_i -> sigma_{n-i}`."""

    if n < 2:
        if word:
            raise ValueError("nonempty braid word requires at least two strands")
        return tuple()
    out = []
    for signed_generator in word:
        if signed_generator == 0:
            raise ValueError("braid generators are nonzero")
        generator = abs(signed_generator)
        if generator >= n:
            raise IndexError(generator)
        reversed_generator = n - generator
        out.append(reversed_generator if signed_generator > 0 else -reversed_generator)
    return tuple(out)


def pure_braid_generator(i: int, j: int) -> Tuple[int, ...]:
    """Return the standard pure braid A_{i,j}, with one-based indices."""

    if i < 1 or j <= i:
        raise ValueError("require 1 <= i < j")
    conjugating = tuple(range(j - 1, i, -1))
    core = (i, i)
    return conjugating + core + invert_braid_word(conjugating)


def free_word_to_braid(word: FreeWord, generator_braids: Mapping[int, BraidWord]) -> Tuple[int, ...]:
    braid = []
    for generator, exponent in word:
        if generator not in generator_braids:
            raise ValueError(f"missing braid image for free generator {generator}")
        image = tuple(generator_braids[generator])
        if exponent < 0:
            image = invert_braid_word(image)
        braid.extend(image)
    return tuple(braid)


def law_word_on_last_strand(word: FreeWord, arity: int) -> Tuple[int, Tuple[int, ...]]:
    """Embed a free word into P_{arity+1} using A_{r+1,n} generators."""

    if arity < 1:
        raise ValueError("arity must be positive")
    n = arity + 1
    images = {r: pure_braid_generator(r + 1, n) for r in range(arity)}
    return n, free_word_to_braid(word, images)


def last_strand_law_exactness_audit(
    group: FiniteGroup,
    word: FreeWord,
    arity: int,
) -> LastStrandLawExactnessAudit:
    """Check one instance of ``iota(w) in K_G`` iff ``w`` is a law on ``G``."""

    n, braid = law_word_on_last_strand(word, arity)
    return LastStrandLawExactnessAudit(
        group_order=len(group.elements),
        arity=arity,
        braid_index=n,
        braid_word=braid,
        word_is_law=is_law_on_group(group, word, arity=arity),
        identity_longitude_signature=has_identity_longitude_signature(
            group,
            n,
            braid,
        ),
    )


def longitude_identity_profile_for_law_braid(
    groups: Mapping[str, FiniteGroup], word: FreeWord, arity: int
) -> Tuple[Tuple[str, ...], Tuple[str, ...]]:
    n, braid = law_word_on_last_strand(word, arity)
    invisible = []
    visible = []
    for name, group in groups.items():
        if has_identity_longitude_signature(group, n, braid):
            invisible.append(name)
        else:
            visible.append(name)
    return tuple(invisible), tuple(visible)


def law_braid_longitudes(word: FreeWord, arity: int):
    n, braid = law_word_on_last_strand(word, arity)
    return artin_longitudes(n, braid)


def law_braid_longitude_subgroup_profile(
    groups: Mapping[str, FiniteGroup],
    word: FreeWord,
    arity: int,
    *,
    max_assignments: int | None = None,
):
    n, braid = law_word_on_last_strand(word, arity)
    return longitude_subgroup_profile(
        groups,
        n,
        braid,
        max_assignments=max_assignments,
    )
