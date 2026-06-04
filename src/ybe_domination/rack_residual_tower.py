from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import permutations, product
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


def _compose_pair(left: PairPermutation, right: PairPermutation) -> PairPermutation:
    return (
        _compose_permutations(left[0], right[0]),
        _compose_permutations(left[1], right[1]),
    )


def _invert_pair(pair: PairPermutation) -> PairPermutation:
    return (_invert_permutation(pair[0]), _invert_permutation(pair[1]))


def _first_moved_tuple(
    solution: FiniteBraidedSet, n: int, permutation: Permutation
) -> Tuple[Optional[Tuple[Element, ...]], Optional[Tuple[Element, ...]]]:
    tuples = tuple(product(solution.elements, repeat=n))
    for index, image_index in enumerate(permutation):
        if index != image_index:
            return tuple(tuples[index]), tuple(tuples[image_index])
    return None, None


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
