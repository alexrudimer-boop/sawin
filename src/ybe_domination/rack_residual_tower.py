from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from functools import lru_cache
from itertools import combinations, permutations, product
from math import lcm
from typing import Iterable, Optional, Tuple

from .finite_braided_set import (
    Element,
    FiniteBraidedSet,
    Word,
    product_solution,
    rack_solution,
)
from .residual import action_permutation

Permutation = Tuple[int, ...]


@dataclass(frozen=True)
class RackResidualObstructionAudit:
    """Fixed-width audit for a detector rack versus one YBE solution."""

    n: int
    joint_image_size: Optional[int]
    solution_image_size: Optional[int]
    detector_image_size: Optional[int]
    kernel_size: Optional[int]
    kernel_contains_nonidentity: Optional[bool]
    first_witness_word: Optional[Word]
    first_moved_tuple: Optional[Tuple[Element, ...]]
    first_moved_tuple_image: Optional[Tuple[Element, ...]]
    truncated: bool

    @property
    def proves_fixed_width_domination_failure(self) -> bool:
        return not self.truncated and self.kernel_contains_nonidentity is True


@dataclass(frozen=True)
class RackPrefixObstructionRow:
    detector_prefix_length: int
    detector_size: int
    arity: int
    audit: RackResidualObstructionAudit

    @property
    def obstruction_found(self) -> bool:
        return self.audit.proves_fixed_width_domination_failure


@dataclass(frozen=True)
class RealizedParabolicCrossEffectAudit:
    """Finite arity audit for the realized parabolic cross-effect."""

    bound: int
    n: int
    joint_image_size: Optional[int]
    kernel_image_size: Optional[int]
    parabolic_image_size: Optional[int]
    quotient_size: Optional[int]
    quotient_nontrivial: Optional[bool]
    seed_count: int
    first_witness_word: Optional[Word]
    first_moved_tuple: Optional[Tuple[Element, ...]]
    first_moved_tuple_image: Optional[Tuple[Element, ...]]
    truncated: bool

    @property
    def proves_realized_high_arity_obstruction(self) -> bool:
        return not self.truncated and self.quotient_nontrivial is True


@dataclass(frozen=True)
class BoundedDeletionSupportAudit:
    """Finite arity audit for the dummy-color bounded-deletion obstruction."""

    rack_size_bound: int
    h: int
    n: int
    detector_size: Optional[int]
    detector_component_count: int
    subset_count: int
    joint_image_size: Optional[int]
    obstruction_size: Optional[int]
    obstruction_nontrivial: Optional[bool]
    first_witness_word: Optional[Word]
    first_moved_tuple: Optional[Tuple[Element, ...]]
    first_moved_tuple_image: Optional[Tuple[Element, ...]]
    truncated: bool

    @property
    def proves_bounded_deletion_support_failure(self) -> bool:
        return not self.truncated and self.obstruction_nontrivial is True


@dataclass(frozen=True)
class TwoStrandRackCutoffRow:
    """One rack-size stage in the two-strand cutoff audit."""

    rack_size: int
    representative_count: int
    detector_size: int
    crossing_lcm: int
    detects_solution: bool


@dataclass(frozen=True)
class TwoStrandRackCutoffAudit:
    """Cheap two-strand rack-size cutoff for a finite solution."""

    max_rack_size: int
    solution_crossing_order: int
    cutoff: Optional[int]
    rows: Tuple[TwoStrandRackCutoffRow, ...]

    @property
    def cutoff_found(self) -> bool:
        return self.cutoff is not None


@dataclass(frozen=True)
class PureBraidImageAudit:
    """Exact check for whether pure braid generators act nontrivially."""

    n: int
    generator_count: int
    image_nontrivial: bool
    first_witness_word: Optional[Word]
    first_moved_tuple: Optional[Tuple[Element, ...]]
    first_moved_tuple_image: Optional[Tuple[Element, ...]]


@dataclass(frozen=True)
class BoundedDeletionSearchTriage:
    """Front-end filters for bounded-deletion obstruction searches."""

    max_rack_size: int
    max_pure_arity: int
    two_strand_cutoff: TwoStrandRackCutoffAudit
    pure_image_audits: Tuple[PureBraidImageAudit, ...]

    @property
    def first_pure_nontrivial_arity(self) -> Optional[int]:
        for audit in self.pure_image_audits:
            if audit.image_nontrivial:
                return audit.n
        return None

    @property
    def suggested_rack_size_bound(self) -> Optional[int]:
        if self.two_strand_cutoff.cutoff is None:
            return None
        return self.two_strand_cutoff.cutoff + 1


def _permutation_order(permutation: Permutation) -> int:
    visited = [False] * len(permutation)
    order = 1
    for start in range(len(permutation)):
        if visited[start]:
            continue
        length = 0
        current = start
        while not visited[current]:
            visited[current] = True
            length += 1
            current = permutation[current]
        if length:
            order = lcm(order, length)
    return order


def _compose_permutations(left: Permutation, right: Permutation) -> Permutation:
    if len(left) != len(right):
        raise ValueError("permutations must have the same size")
    return tuple(left[right[i]] for i in range(len(left)))


def _invert_permutation(permutation: Permutation) -> Permutation:
    inverse = [0] * len(permutation)
    for index, image in enumerate(permutation):
        inverse[image] = index
    return tuple(inverse)


PairPermutation = Tuple[Permutation, Permutation]
MultiPermutation = Tuple[Permutation, ...]


def _compose_pair(left: PairPermutation, right: PairPermutation) -> PairPermutation:
    return (
        _compose_permutations(left[0], right[0]),
        _compose_permutations(left[1], right[1]),
    )


def _invert_pair(pair: PairPermutation) -> PairPermutation:
    return (_invert_permutation(pair[0]), _invert_permutation(pair[1]))


def _compose_multi(left: MultiPermutation, right: MultiPermutation) -> MultiPermutation:
    if len(left) != len(right):
        raise ValueError("multi-permutations must have the same arity")
    return tuple(
        _compose_permutations(left_part, right_part)
        for left_part, right_part in zip(left, right)
    )


def _invert_multi(permutation: MultiPermutation) -> MultiPermutation:
    return tuple(_invert_permutation(part) for part in permutation)


def _first_moved_tuple(
    solution: FiniteBraidedSet, n: int, permutation: Permutation
) -> Tuple[Optional[Tuple[Element, ...]], Optional[Tuple[Element, ...]]]:
    tuples = tuple(product(solution.elements, repeat=n))
    for index, image_index in enumerate(permutation):
        if index != image_index:
            return tuple(tuples[index]), tuple(tuples[image_index])
    return None, None


def _invert_word(word: Word) -> Word:
    return tuple(-signed for signed in reversed(word))


def _pure_generator_word(left: int, right: int) -> Word:
    """Return the standard pure braid generator A_{left,right}."""

    if left < 1 or right <= left:
        raise ValueError("pure generator requires 1 <= left < right")
    return (
        tuple(range(right - 1, left, -1))
        + (left, left)
        + tuple(-generator for generator in range(left + 1, right))
    )


def _deletion_subsets(n: int, h: int) -> Tuple[Tuple[int, ...], ...]:
    return tuple(
        subset
        for size in range(2, min(h, n) + 1)
        for subset in combinations(range(1, n + 1), size)
    )


def _deleted_pure_generator_word(
    left: int, right: int, subset: Tuple[int, ...]
) -> Optional[Word]:
    if left not in subset or right not in subset:
        return None
    rank = {strand: index + 1 for index, strand in enumerate(subset)}
    return _pure_generator_word(rank[left], rank[right])


def _joint_generators(
    solution: FiniteBraidedSet, detector: FiniteBraidedSet, n: int
) -> Tuple[Tuple[int, PairPermutation], ...]:
    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    return tuple(
        (
            signed,
            (
                action_permutation(detector, n, (signed,)),
                action_permutation(solution, n, (signed,)),
            ),
        )
        for signed in alphabet
    )


def _joint_image_with_words(
    solution: FiniteBraidedSet,
    detector: FiniteBraidedSet,
    n: int,
    state_limit: int,
) -> Tuple[dict[PairPermutation, Word], Tuple[Tuple[int, PairPermutation], ...], bool]:
    detector_identity = tuple(range(len(detector.elements) ** n))
    solution_identity = tuple(range(len(solution.elements) ** n))
    identity = (detector_identity, solution_identity)
    generators = _joint_generators(solution, detector, n)
    seen: dict[PairPermutation, Word] = {identity: tuple()}
    queue = deque((identity,))
    while queue:
        state = queue.popleft()
        word = seen[state]
        for signed, generator in generators:
            next_state = _compose_pair(generator, state)
            if next_state in seen:
                continue
            seen[next_state] = word + (signed,)
            if len(seen) > state_limit:
                return seen, generators, True
            queue.append(next_state)
    return seen, generators, False


def rack_residual_obstruction_audit(
    solution: FiniteBraidedSet,
    detector: FiniteBraidedSet,
    n: int,
    state_limit: int = 100_000,
) -> RackResidualObstructionAudit:
    """Compute the fixed-arity rack-residual obstruction group.

    The audit closes the image of `B_n` on
    `solution^n x detector^n`.  It then checks whether the kernel of the
    projection to the detector coordinate has a nonidentity solution
    projection.  For fixed `solution`, `detector`, and `n` this is a finite
    computation; the Sawin problem is the remaining unbounded quantifier over
    detector racks and braid arities.
    """

    if n < 1:
        raise ValueError("braid degree must be positive")
    solution_identity = tuple(range(len(solution.elements) ** n))
    detector_identity = tuple(range(len(detector.elements) ** n))
    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    if not alphabet:
        return RackResidualObstructionAudit(
            n=n,
            joint_image_size=1,
            solution_image_size=1,
            detector_image_size=1,
            kernel_size=1,
            kernel_contains_nonidentity=False,
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=False,
        )

    solution_generators = {
        signed: action_permutation(solution, n, (signed,)) for signed in alphabet
    }
    detector_generators = {
        signed: action_permutation(detector, n, (signed,)) for signed in alphabet
    }

    start = (detector_identity, solution_identity, tuple())
    queue = deque((start,))
    seen = {(detector_identity, solution_identity)}
    solution_projection = {solution_identity}
    detector_projection = {detector_identity}
    kernel_solution = {solution_identity}
    first_witness_word = None
    first_witness_permutation = None

    while queue:
        detector_state, solution_state, word = queue.popleft()
        for signed in alphabet:
            next_word = word + (signed,)
            next_detector = _compose_permutations(
                detector_generators[signed], detector_state
            )
            next_solution = _compose_permutations(
                solution_generators[signed], solution_state
            )
            key = (next_detector, next_solution)
            if key in seen:
                continue
            seen.add(key)
            solution_projection.add(next_solution)
            detector_projection.add(next_detector)
            if next_detector == detector_identity:
                kernel_solution.add(next_solution)
                if (
                    next_solution != solution_identity
                    and first_witness_word is None
                ):
                    first_witness_word = next_word
                    first_witness_permutation = next_solution
            if len(seen) > state_limit:
                moved, moved_image = (
                    (None, None)
                    if first_witness_permutation is None
                    else _first_moved_tuple(solution, n, first_witness_permutation)
                )
                return RackResidualObstructionAudit(
                    n=n,
                    joint_image_size=None,
                    solution_image_size=None,
                    detector_image_size=None,
                    kernel_size=None,
                    kernel_contains_nonidentity=None,
                    first_witness_word=first_witness_word,
                    first_moved_tuple=moved,
                    first_moved_tuple_image=moved_image,
                    truncated=True,
                )
            queue.append((next_detector, next_solution, next_word))

    moved, moved_image = (
        (None, None)
        if first_witness_permutation is None
        else _first_moved_tuple(solution, n, first_witness_permutation)
    )
    return RackResidualObstructionAudit(
        n=n,
        joint_image_size=len(seen),
        solution_image_size=len(solution_projection),
        detector_image_size=len(detector_projection),
        kernel_size=len(kernel_solution),
        kernel_contains_nonidentity=any(
            item != solution_identity for item in kernel_solution
        ),
        first_witness_word=first_witness_word,
        first_moved_tuple=moved,
        first_moved_tuple_image=moved_image,
        truncated=False,
    )


def _decode_index(index: int, base_size: int, length: int) -> list[int]:
    digits = [0] * length
    for position in range(length - 1, -1, -1):
        digits[position] = index % base_size
        index //= base_size
    return digits


def _encode_digits(digits: Iterable[int], base_size: int) -> int:
    index = 0
    for digit in digits:
        index = index * base_size + digit
    return index


def _block_embed_permutation(
    permutation: Permutation,
    base_size: int,
    width: int,
    n: int,
    block_start: int,
) -> Permutation:
    """Embed a permutation of `base_size**width` block-tuples into arity `n`."""

    if width < 1:
        raise ValueError("block width must be positive")
    if not 0 <= block_start <= n - width:
        raise ValueError("block does not fit in the target arity")
    if len(permutation) != base_size**width:
        raise ValueError("permutation size does not match the block width")

    embedded = []
    for index in range(base_size**n):
        digits = _decode_index(index, base_size, n)
        block = digits[block_start : block_start + width]
        block_index = _encode_digits(block, base_size)
        image_block = _decode_index(permutation[block_index], base_size, width)
        digits[block_start : block_start + width] = image_block
        embedded.append(_encode_digits(digits, base_size))
    return tuple(embedded)


def _subgroup_generated_by_pairs(
    identity: PairPermutation,
    generators: Iterable[PairPermutation],
    state_limit: int,
) -> Tuple[set[PairPermutation], bool]:
    generator_tuple = tuple(generator for generator in generators if generator != identity)
    subgroup = {identity}
    queue = deque((identity,))
    while queue:
        state = queue.popleft()
        for generator in generator_tuple:
            next_state = _compose_pair(generator, state)
            if next_state in subgroup:
                continue
            subgroup.add(next_state)
            if len(subgroup) > state_limit:
                return subgroup, True
            queue.append(next_state)
    return subgroup, False


def _normal_closure_in_joint_image(
    identity: PairPermutation,
    group_elements: Iterable[PairPermutation],
    seeds: Iterable[PairPermutation],
    state_limit: int,
) -> Tuple[set[PairPermutation], bool]:
    seed_tuple = tuple(seed for seed in seeds if seed != identity)
    if not seed_tuple:
        return {identity}, False
    conjugates = []
    for group_element in group_elements:
        inverse = _invert_pair(group_element)
        for seed in seed_tuple:
            conjugates.append(_compose_pair(_compose_pair(group_element, seed), inverse))
            if len(conjugates) > state_limit:
                return set((identity,)), True
    return _subgroup_generated_by_pairs(identity, conjugates, state_limit)


def realized_parabolic_cross_effect_audit(
    solution: FiniteBraidedSet,
    detector: FiniteBraidedSet,
    bound: int,
    n: int,
    state_limit: int = 100_000,
) -> RealizedParabolicCrossEffectAudit:
    """Compute the finite realized parabolic cross-effect at one arity.

    The result compares the detector kernel image in the finite joint action
    with the normal closure of all parabolically embedded lower-width detector
    kernel images for widths at most ``bound``.
    """

    if bound < 1:
        raise ValueError("bound must be positive")
    if n < 1:
        raise ValueError("braid degree must be positive")

    full_seen, _full_generators, full_truncated = _joint_image_with_words(
        solution, detector, n, state_limit
    )
    detector_identity = tuple(range(len(detector.elements) ** n))
    solution_identity = tuple(range(len(solution.elements) ** n))
    identity = (detector_identity, solution_identity)
    if full_truncated:
        return RealizedParabolicCrossEffectAudit(
            bound=bound,
            n=n,
            joint_image_size=None,
            kernel_image_size=None,
            parabolic_image_size=None,
            quotient_size=None,
            quotient_nontrivial=None,
            seed_count=0,
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=True,
        )

    kernel_image = {
        pair for pair in full_seen if pair[0] == detector_identity
    }
    seeds: set[PairPermutation] = set()
    for width in range(1, min(bound, n) + 1):
        lower_seen, _lower_generators, lower_truncated = _joint_image_with_words(
            solution, detector, width, state_limit
        )
        if lower_truncated:
            return RealizedParabolicCrossEffectAudit(
                bound=bound,
                n=n,
                joint_image_size=len(full_seen),
                kernel_image_size=len(kernel_image),
                parabolic_image_size=None,
                quotient_size=None,
                quotient_nontrivial=None,
                seed_count=len(seeds),
                first_witness_word=None,
                first_moved_tuple=None,
                first_moved_tuple_image=None,
                truncated=True,
            )
        lower_detector_identity = tuple(range(len(detector.elements) ** width))
        lower_solution_identity = tuple(range(len(solution.elements) ** width))
        for lower_pair in lower_seen:
            if (
                lower_pair[0] != lower_detector_identity
                or lower_pair[1] == lower_solution_identity
            ):
                continue
            for block_start in range(0, n - width + 1):
                seed = (
                    detector_identity,
                    _block_embed_permutation(
                        lower_pair[1],
                        len(solution.elements),
                        width,
                        n,
                        block_start,
                    ),
                )
                if seed not in full_seen:
                    raise AssertionError("parabolic seed is not in the joint image")
                seeds.add(seed)

    parabolic_image, parabolic_truncated = _normal_closure_in_joint_image(
        identity,
        full_seen.keys(),
        seeds,
        state_limit,
    )
    if parabolic_truncated:
        return RealizedParabolicCrossEffectAudit(
            bound=bound,
            n=n,
            joint_image_size=len(full_seen),
            kernel_image_size=len(kernel_image),
            parabolic_image_size=None,
            quotient_size=None,
            quotient_nontrivial=None,
            seed_count=len(seeds),
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=True,
        )

    if not parabolic_image <= kernel_image:
        raise AssertionError("parabolic normal closure escaped the detector kernel")

    first_witness_pair = None
    first_witness_word = None
    for pair, word in full_seen.items():
        if pair in kernel_image and pair not in parabolic_image:
            first_witness_pair = pair
            first_witness_word = word
            break

    moved, moved_image = (
        (None, None)
        if first_witness_pair is None
        else _first_moved_tuple(solution, n, first_witness_pair[1])
    )
    quotient_size = None
    if parabolic_image:
        if len(kernel_image) % len(parabolic_image) != 0:
            raise AssertionError("parabolic image size does not divide kernel image size")
        quotient_size = len(kernel_image) // len(parabolic_image)
    return RealizedParabolicCrossEffectAudit(
        bound=bound,
        n=n,
        joint_image_size=len(full_seen),
        kernel_image_size=len(kernel_image),
        parabolic_image_size=len(parabolic_image),
        quotient_size=quotient_size,
        quotient_nontrivial=first_witness_pair is not None,
        seed_count=len(seeds),
        first_witness_word=first_witness_word,
        first_moved_tuple=moved,
        first_moved_tuple_image=moved_image,
        truncated=False,
    )


def _rack_size_detector(max_rack_size: int) -> FiniteBraidedSet:
    representatives = small_rack_representatives(max_rack_size)
    prefixes = rack_product_prefixes(representatives)
    if not prefixes:
        raise ValueError("at least one rack representative is required")
    return prefixes[-1]


def two_strand_rack_cutoff_audit(
    solution: FiniteBraidedSet,
    max_rack_size: int,
) -> TwoStrandRackCutoffAudit:
    """Return the least checked rack size whose two-strand detector covers X.

    Since ``B_2`` is infinite cyclic, the product detector formed from all
    rack isomorphism classes of size at most ``s`` dominates the two-strand
    action of ``solution`` exactly when the order of the two-strand crossing
    permutation of ``solution`` divides the lcm of the corresponding rack
    crossing orders.
    """

    if max_rack_size < 1:
        raise ValueError("maximum rack size must be positive")

    solution_order = _permutation_order(action_permutation(solution, 2, (1,)))
    representatives = small_rack_representatives(max_rack_size)
    crossing_lcm = 1
    detector_size = 1
    cutoff = None
    rows = []
    for rack_size in range(1, max_rack_size + 1):
        size_representatives = tuple(
            rack for rack in representatives if len(rack.elements) == rack_size
        )
        for rack in size_representatives:
            crossing_lcm = lcm(
                crossing_lcm,
                _permutation_order(action_permutation(rack, 2, (1,))),
            )
            detector_size *= len(rack.elements)
        detects_solution = crossing_lcm % solution_order == 0
        if detects_solution and cutoff is None:
            cutoff = rack_size
        rows.append(
            TwoStrandRackCutoffRow(
                rack_size=rack_size,
                representative_count=len(size_representatives),
                detector_size=detector_size,
                crossing_lcm=crossing_lcm,
                detects_solution=detects_solution,
            )
        )
    return TwoStrandRackCutoffAudit(
        max_rack_size=max_rack_size,
        solution_crossing_order=solution_order,
        cutoff=cutoff,
        rows=tuple(rows),
    )


def pure_braid_image_audit(
    solution: FiniteBraidedSet,
    n: int,
) -> PureBraidImageAudit:
    """Check exactly whether the standard pure generators move ``X^n``."""

    if n < 1:
        raise ValueError("braid degree must be positive")

    identity = tuple(range(len(solution.elements) ** n))
    generator_count = 0
    for left in range(1, n):
        for right in range(left + 1, n + 1):
            generator_count += 1
            word = _pure_generator_word(left, right)
            permutation = action_permutation(solution, n, word)
            if permutation != identity:
                moved, moved_image = _first_moved_tuple(solution, n, permutation)
                return PureBraidImageAudit(
                    n=n,
                    generator_count=generator_count,
                    image_nontrivial=True,
                    first_witness_word=word,
                    first_moved_tuple=moved,
                    first_moved_tuple_image=moved_image,
                )
    return PureBraidImageAudit(
        n=n,
        generator_count=generator_count,
        image_nontrivial=False,
        first_witness_word=None,
        first_moved_tuple=None,
        first_moved_tuple_image=None,
    )


def bounded_deletion_search_triage(
    solution: FiniteBraidedSet,
    max_rack_size: int,
    max_pure_arity: int,
) -> BoundedDeletionSearchTriage:
    """Run cheap filters before the expensive bounded-deletion closure."""

    if max_pure_arity < 1:
        raise ValueError("maximum pure arity must be positive")
    two_strand_cutoff = two_strand_rack_cutoff_audit(solution, max_rack_size)
    pure_audits = tuple(
        pure_braid_image_audit(solution, n)
        for n in range(1, max_pure_arity + 1)
    )
    return BoundedDeletionSearchTriage(
        max_rack_size=max_rack_size,
        max_pure_arity=max_pure_arity,
        two_strand_cutoff=two_strand_cutoff,
        pure_image_audits=pure_audits,
    )


def bounded_deletion_support_audit(
    solution: FiniteBraidedSet,
    h: int,
    n: int,
    rack_size_bound: int,
    state_limit: int = 100_000,
) -> BoundedDeletionSupportAudit:
    """Compute the finite obstruction group E_{X,h,n} for one cutoff.

    The detector is the product of all rack isomorphism classes of size at
    most ``rack_size_bound``.  To avoid building huge product-rack
    permutation sets, the closure records the action on each small rack
    representative separately; this is equivalent because the product action
    is componentwise.  The remaining components record the full ``X`` action
    and all ``X`` actions after deletion to subsets of size at most ``h``.
    """

    if h < 1:
        raise ValueError("h must be positive")
    if n < 1:
        raise ValueError("braid degree must be positive")
    if rack_size_bound < 2:
        raise ValueError("rack_size_bound must be at least 2 for pure deletion")

    detector_components = small_rack_representatives(rack_size_bound)
    detector_size = 1
    for detector in detector_components:
        detector_size *= len(detector.elements)
    subsets = _deletion_subsets(n, h)
    detector_identities = tuple(
        tuple(range(len(detector.elements) ** n))
        for detector in detector_components
    )
    solution_identity = tuple(range(len(solution.elements) ** n))
    deletion_identities = tuple(
        tuple(range(len(solution.elements) ** len(subset)))
        for subset in subsets
    )
    identity: MultiPermutation = (
        *detector_identities,
        solution_identity,
        *deletion_identities,
    )
    solution_index = len(detector_identities)
    deletion_start_index = solution_index + 1

    if n < 2:
        return BoundedDeletionSupportAudit(
            rack_size_bound=rack_size_bound,
            h=h,
            n=n,
            detector_size=detector_size,
            detector_component_count=len(detector_components),
            subset_count=len(subsets),
            joint_image_size=1,
            obstruction_size=1,
            obstruction_nontrivial=False,
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=False,
        )

    generators: list[Tuple[Word, MultiPermutation]] = []
    for left in range(1, n):
        for right in range(left + 1, n + 1):
            word = _pure_generator_word(left, right)
            components: list[Permutation] = [
                action_permutation(detector, n, word)
                for detector in detector_components
            ]
            components.append(action_permutation(solution, n, word))
            for subset, deletion_identity in zip(subsets, deletion_identities):
                deleted_word = _deleted_pure_generator_word(left, right, subset)
                if deleted_word is None:
                    components.append(deletion_identity)
                else:
                    components.append(
                        action_permutation(solution, len(subset), deleted_word)
                    )
            generator = tuple(components)
            generators.append((word, generator))
            generators.append((_invert_word(word), _invert_multi(generator)))

    seen: dict[MultiPermutation, Word] = {identity: tuple()}
    queue = deque((identity,))
    obstruction_solution = {solution_identity}
    first_witness_state = None
    first_witness_word = None

    while queue:
        state = queue.popleft()
        state_word = seen[state]
        for generator_word, generator in generators:
            next_state = _compose_multi(generator, state)
            if next_state in seen:
                continue
            next_word = state_word + tuple(generator_word)
            seen[next_state] = next_word
            detector_trivial = all(
                next_state[index] == detector_identity
                for index, detector_identity in enumerate(detector_identities)
            )
            deletions_trivial = all(
                next_state[deletion_start_index + index] == deletion_identity
                for index, deletion_identity in enumerate(deletion_identities)
            )
            if detector_trivial and deletions_trivial:
                obstruction_solution.add(next_state[solution_index])
                if (
                    next_state[solution_index] != solution_identity
                    and first_witness_state is None
                ):
                    first_witness_state = next_state
                    first_witness_word = next_word
            if len(seen) > state_limit:
                moved, moved_image = (
                    (None, None)
                    if first_witness_state is None
                    else _first_moved_tuple(
                        solution,
                        n,
                        first_witness_state[solution_index],
                    )
                )
                return BoundedDeletionSupportAudit(
                    rack_size_bound=rack_size_bound,
                    h=h,
                    n=n,
                    detector_size=detector_size,
                    detector_component_count=len(detector_components),
                    subset_count=len(subsets),
                    joint_image_size=None,
                    obstruction_size=None,
                    obstruction_nontrivial=None,
                    first_witness_word=first_witness_word,
                    first_moved_tuple=moved,
                    first_moved_tuple_image=moved_image,
                    truncated=True,
                )
            queue.append(next_state)

    moved, moved_image = (
        (None, None)
        if first_witness_state is None
        else _first_moved_tuple(solution, n, first_witness_state[solution_index])
    )
    return BoundedDeletionSupportAudit(
        rack_size_bound=rack_size_bound,
        h=h,
        n=n,
        detector_size=detector_size,
        detector_component_count=len(detector_components),
        subset_count=len(subsets),
        joint_image_size=len(seen),
        obstruction_size=len(obstruction_solution),
        obstruction_nontrivial=any(
            permutation != solution_identity for permutation in obstruction_solution
        ),
        first_witness_word=first_witness_word,
        first_moved_tuple=moved,
        first_moved_tuple_image=moved_image,
        truncated=False,
    )


def _compose_index_permutations(left: Permutation, right: Permutation) -> Permutation:
    return tuple(left[right[index]] for index in range(len(left)))


def _invert_index_permutation(permutation: Permutation) -> Permutation:
    inverse = [0] * len(permutation)
    for index, image in enumerate(permutation):
        inverse[image] = index
    return tuple(inverse)


def _rack_signature(rack: FiniteBraidedSet) -> Tuple[Tuple[int, ...], ...]:
    index = {element: position for position, element in enumerate(rack.elements)}
    return tuple(
        tuple(index[rack.R[(left, right)][0]] for right in rack.elements)
        for left in rack.elements
    )


def canonical_rack_signature(rack: FiniteBraidedSet) -> Tuple[Tuple[int, ...], ...]:
    """Return the lexicographically least operation table under relabeling."""

    size = len(rack.elements)
    raw = _rack_signature(rack)
    signatures = []
    for relabel in permutations(range(size)):
        inverse = _invert_index_permutation(tuple(relabel))
        signatures.append(
            tuple(
                tuple(
                    relabel[raw[inverse[left]][inverse[right]]]
                    for right in range(size)
                )
                for left in range(size)
            )
        )
    return min(signatures)


def labelled_rack_solutions(size: int) -> Tuple[FiniteBraidedSet, ...]:
    """Enumerate all labelled racks on `range(size)`.

    This is intended for small sizes only.  It enumerates all choices of left
    translations and filters by the rack conjugacy identity.
    """

    if size < 1:
        raise ValueError("rack size must be positive")
    elements = tuple(range(size))
    all_permutations = tuple(permutations(elements))
    racks = []
    for translations in product(all_permutations, repeat=size):
        ok = True
        for left in elements:
            left_inverse = _invert_index_permutation(translations[left])
            for right in elements:
                output = translations[left][right]
                conjugate = _compose_index_permutations(
                    _compose_index_permutations(translations[left], translations[right]),
                    left_inverse,
                )
                if translations[output] != conjugate:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            racks.append(
                rack_solution(
                    elements,
                    lambda left, right, translations=translations: translations[left][right],
                )
            )
    return tuple(racks)


@lru_cache(maxsize=None)
def small_rack_representatives(max_size: int) -> Tuple[FiniteBraidedSet, ...]:
    """Return one labelled representative of each rack isomorphism class."""

    if max_size < 1:
        raise ValueError("maximum rack size must be positive")
    representatives = []
    seen = set()
    for size in range(1, max_size + 1):
        for rack in labelled_rack_solutions(size):
            signature = canonical_rack_signature(rack)
            if (size, signature) in seen:
                continue
            seen.add((size, signature))
            representatives.append(rack)
    return tuple(representatives)


def rack_product_prefixes(
    racks: Iterable[FiniteBraidedSet],
    max_detector_size: Optional[int] = None,
) -> Tuple[FiniteBraidedSet, ...]:
    """Return successive Cartesian product prefixes of the supplied racks."""

    prefixes = []
    current = None
    for rack in racks:
        candidate = rack if current is None else product_solution(current, rack)
        if max_detector_size is not None and len(candidate.elements) > max_detector_size:
            break
        prefixes.append(candidate)
        current = candidate
    return tuple(prefixes)


def small_rack_prefix_obstruction_rows(
    solution: FiniteBraidedSet,
    max_rack_size: int,
    max_arity: int,
    max_detector_size: Optional[int] = None,
    state_limit: int = 100_000,
) -> Tuple[RackPrefixObstructionRow, ...]:
    """Run fixed-width obstruction audits for small rack product prefixes."""

    rows = []
    prefixes = rack_product_prefixes(
        small_rack_representatives(max_rack_size),
        max_detector_size=max_detector_size,
    )
    for prefix_index, detector in enumerate(prefixes, start=1):
        for arity in range(1, max_arity + 1):
            rows.append(
                RackPrefixObstructionRow(
                    detector_prefix_length=prefix_index,
                    detector_size=len(detector.elements),
                    arity=arity,
                    audit=rack_residual_obstruction_audit(
                        solution, detector, arity, state_limit=state_limit
                    ),
                )
            )
    return tuple(rows)
