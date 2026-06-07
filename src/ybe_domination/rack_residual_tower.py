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
    flip_disjoint_union_solution,
    identity_solution,
    is_rack_solution,
    product_solution,
    rack_solution,
)
from .residual import action_permutation

Permutation = Tuple[int, ...]
DetectorState = Tuple[Permutation, ...]


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
ComponentwisePairPermutation = Tuple[DetectorState, Permutation]
MultiPermutation = Tuple[Permutation, ...]
MatrixFlat = Tuple[int, ...]
AffineMapFlat = Tuple[MatrixFlat, Tuple[int, ...]]
Q3CompressedState = Tuple[object, ...]


def _compose_pair(left: PairPermutation, right: PairPermutation) -> PairPermutation:
    return (
        _compose_permutations(left[0], right[0]),
        _compose_permutations(left[1], right[1]),
    )


def _invert_pair(pair: PairPermutation) -> PairPermutation:
    return (_invert_permutation(pair[0]), _invert_permutation(pair[1]))


def _compose_componentwise_pair(
    left: ComponentwisePairPermutation,
    right: ComponentwisePairPermutation,
) -> ComponentwisePairPermutation:
    if len(left[0]) != len(right[0]):
        raise ValueError("componentwise detector states have different lengths")
    return (
        tuple(
            _compose_permutations(left_part, right_part)
            for left_part, right_part in zip(left[0], right[0])
        ),
        _compose_permutations(left[1], right[1]),
    )


def _invert_componentwise_pair(
    pair: ComponentwisePairPermutation,
) -> ComponentwisePairPermutation:
    return (
        tuple(_invert_permutation(part) for part in pair[0]),
        _invert_permutation(pair[1]),
    )


def _compose_multi(left: MultiPermutation, right: MultiPermutation) -> MultiPermutation:
    if len(left) != len(right):
        raise ValueError("multi-permutations must have the same arity")
    return tuple(
        _compose_permutations(left_part, right_part)
        for left_part, right_part in zip(left, right)
    )


def _invert_multi(permutation: MultiPermutation) -> MultiPermutation:
    return tuple(_invert_permutation(part) for part in permutation)


def _identity_matrix(size: int) -> MatrixFlat:
    return tuple(
        1 if row == col else 0
        for row in range(size)
        for col in range(size)
    )


def _matrix_multiply_mod(
    left: MatrixFlat,
    right: MatrixFlat,
    size: int,
    modulus: int,
) -> MatrixFlat:
    return tuple(
        sum(
            left[row * size + inner] * right[inner * size + col]
            for inner in range(size)
        )
        % modulus
        for row in range(size)
        for col in range(size)
    )


def _matrix_inverse_mod(
    matrix: MatrixFlat,
    size: int,
    modulus: int,
) -> MatrixFlat:
    rows = [
        [
            matrix[row * size + col] % modulus
            for col in range(size)
        ]
        + [
            1 if row == col else 0
            for col in range(size)
        ]
        for row in range(size)
    ]
    for col in range(size):
        pivot = None
        for row in range(col, size):
            if rows[row][col] % modulus:
                pivot = row
                break
        if pivot is None:
            raise ValueError("matrix is not invertible modulo the supplied modulus")
        rows[col], rows[pivot] = rows[pivot], rows[col]
        pivot_inverse = pow(rows[col][col] % modulus, -1, modulus)
        rows[col] = [(entry * pivot_inverse) % modulus for entry in rows[col]]
        for row in range(size):
            if row == col:
                continue
            factor = rows[row][col] % modulus
            if not factor:
                continue
            rows[row] = [
                (entry - factor * pivot_entry) % modulus
                for entry, pivot_entry in zip(rows[row], rows[col])
            ]
    return tuple(
        rows[row][size + col] % modulus
        for row in range(size)
        for col in range(size)
    )


def _matrix_vector_multiply_mod(
    matrix: MatrixFlat,
    vector: Tuple[int, ...],
    size: int,
    modulus: int,
) -> Tuple[int, ...]:
    return tuple(
        sum(matrix[row * size + col] * vector[col] for col in range(size))
        % modulus
        for row in range(size)
    )


def _normalize_matrix_flat(
    matrix: Iterable[Iterable[int]],
    size: int,
    modulus: int,
) -> MatrixFlat:
    rows = tuple(tuple(entry % modulus for entry in row) for row in matrix)
    if len(rows) != size or any(len(row) != size for row in rows):
        raise ValueError("matrix has the wrong dimensions")
    return tuple(entry for row in rows for entry in row)


def _normalize_vector(
    vector: Iterable[int],
    size: int,
    modulus: int,
) -> Tuple[int, ...]:
    entries = tuple(entry % modulus for entry in vector)
    if len(entries) != size:
        raise ValueError("vector has the wrong dimension")
    return entries


def _identity_affine_map(size: int) -> AffineMapFlat:
    return (_identity_matrix(size), tuple(0 for _ in range(size)))


def _compose_affine_mod2(
    left: AffineMapFlat,
    right: AffineMapFlat,
) -> AffineMapFlat:
    """Return ``left after right`` for affine maps over ``F_2``."""

    left_matrix, left_offset = left
    right_matrix, right_offset = right
    size = len(left_offset)
    if len(right_offset) != size:
        raise ValueError("affine maps must have the same dimension")
    matrix = _matrix_multiply_mod(left_matrix, right_matrix, size, 2)
    translated = _matrix_vector_multiply_mod(left_matrix, right_offset, size, 2)
    offset = tuple(a ^ b for a, b in zip(translated, left_offset))
    return (matrix, offset)


def _invert_affine_mod2(affine_map: AffineMapFlat) -> AffineMapFlat:
    matrix, offset = affine_map
    size = len(offset)
    inverse_matrix = _matrix_inverse_mod(matrix, size, 2)
    inverse_offset = _matrix_vector_multiply_mod(inverse_matrix, offset, size, 2)
    return (inverse_matrix, inverse_offset)


def _affine_generator_map_mod2(
    local_matrix: MatrixFlat,
    local_offset: Tuple[int, ...],
    dimension: int,
    braid_index: int,
    signed_generator: int,
) -> AffineMapFlat:
    if signed_generator == 0:
        raise ValueError("braid generators are nonzero")
    generator = abs(signed_generator)
    if generator < 1 or generator >= braid_index:
        raise ValueError("braid generator is out of range")
    local_size = 2 * dimension
    if signed_generator < 0:
        block_matrix = _matrix_inverse_mod(local_matrix, local_size, 2)
        block_offset = _matrix_vector_multiply_mod(
            block_matrix,
            local_offset,
            local_size,
            2,
        )
    else:
        block_matrix = local_matrix
        block_offset = local_offset

    total_size = dimension * braid_index
    start = dimension * (generator - 1)
    matrix = list(_identity_matrix(total_size))
    offset = [0] * total_size
    for block_row in range(local_size):
        target_row = start + block_row
        for col in range(total_size):
            matrix[target_row * total_size + col] = 0
        for block_col in range(local_size):
            matrix[target_row * total_size + start + block_col] = block_matrix[
                block_row * local_size + block_col
            ]
        offset[target_row] = block_offset[block_row]
    return (tuple(matrix), tuple(offset))


def _affine_word_map_mod2(
    local_matrix: MatrixFlat,
    local_offset: Tuple[int, ...],
    dimension: int,
    braid_index: int,
    word: Word,
) -> AffineMapFlat:
    current = _identity_affine_map(dimension * braid_index)
    for signed_generator in word:
        current = _compose_affine_mod2(
            _affine_generator_map_mod2(
                local_matrix,
                local_offset,
                dimension,
                braid_index,
                signed_generator,
            ),
            current,
        )
    return current


def _compose_q3_affine_compressed_state(
    left: Q3CompressedState,
    right: Q3CompressedState,
    n: int,
) -> Q3CompressedState:
    if len(left) != len(right):
        raise ValueError("compressed states must have the same arity")
    pair = tuple((a + b) % 2 for a, b in zip(left[0], right[0]))
    row = tuple((a + b) % 3 for a, b in zip(left[1], right[1]))
    dihedral = _matrix_multiply_mod(left[2], right[2], n, 3)
    affine_maps = tuple(
        _compose_affine_mod2(left_part, right_part)
        for left_part, right_part in zip(left[3:], right[3:])
    )
    return (pair, row, dihedral, *affine_maps)


def _invert_q3_affine_compressed_state(
    state: Q3CompressedState,
    n: int,
) -> Q3CompressedState:
    pair = state[0]
    row = tuple((-entry) % 3 for entry in state[1])
    dihedral = _matrix_inverse_mod(state[2], n, 3)
    affine_maps = tuple(_invert_affine_mod2(part) for part in state[3:])
    return (pair, row, dihedral, *affine_maps)


def _vector_to_affine_tuple(
    vector: Tuple[int, ...],
    dimension: int,
) -> Tuple[Tuple[int, ...], ...]:
    return tuple(
        tuple(vector[start:start + dimension])
        for start in range(0, len(vector), dimension)
    )


def _first_moved_affine_tuple(
    affine_map: AffineMapFlat,
    dimension: int,
) -> Tuple[Optional[Tuple[Element, ...]], Optional[Tuple[Element, ...]]]:
    matrix, offset = affine_map
    size = len(offset)
    if size % dimension:
        raise ValueError("affine map dimension is not a multiple of element size")
    identity = _identity_matrix(size)
    if offset != tuple(0 for _ in range(size)):
        vector = tuple(0 for _ in range(size))
        image = offset
    elif matrix != identity:
        moved_col = next(
            col
            for col in range(size)
            if tuple(matrix[row * size + col] for row in range(size))
            != tuple(1 if row == col else 0 for row in range(size))
        )
        vector = tuple(1 if col == moved_col else 0 for col in range(size))
        image = tuple(matrix[row * size + moved_col] for row in range(size))
    else:
        return None, None
    return (
        _vector_to_affine_tuple(vector, dimension),
        _vector_to_affine_tuple(image, dimension),
    )


def _dihedral_sigma_matrix(n: int, signed_generator: int) -> MatrixFlat:
    if signed_generator == 0:
        raise ValueError("braid generators are nonzero")
    generator = abs(signed_generator)
    if generator < 1 or generator >= n:
        raise ValueError("braid generator is out of range")
    matrix = list(_identity_matrix(n))
    row = generator - 1
    col = generator - 1
    block = ((2, 2), (1, 0))
    for block_row in range(2):
        for block_col in range(2):
            matrix[(row + block_row) * n + col + block_col] = block[block_row][
                block_col
            ]
    matrix_tuple = tuple(matrix)
    if signed_generator < 0:
        return _matrix_inverse_mod(matrix_tuple, n, 3)
    return matrix_tuple


def _dihedral_word_matrix(n: int, word: Word) -> MatrixFlat:
    state = _identity_matrix(n)
    for signed_generator in word:
        state = _matrix_multiply_mod(
            _dihedral_sigma_matrix(n, signed_generator),
            state,
            n,
            3,
        )
    return state


def _compose_q3_compressed_state(
    left: Q3CompressedState,
    right: Q3CompressedState,
    n: int,
) -> Q3CompressedState:
    if len(left) != len(right):
        raise ValueError("compressed states must have the same arity")
    pair = tuple((a + b) % 2 for a, b in zip(left[0], right[0]))
    row = tuple((a + b) % 3 for a, b in zip(left[1], right[1]))
    dihedral = _matrix_multiply_mod(left[2], right[2], n, 3)
    permutations = tuple(
        _compose_permutations(left_part, right_part)
        for left_part, right_part in zip(left[3:], right[3:])
    )
    return (pair, row, dihedral, *permutations)


def _invert_q3_compressed_state(
    state: Q3CompressedState,
    n: int,
) -> Q3CompressedState:
    pair = state[0]
    row = tuple((-entry) % 3 for entry in state[1])
    dihedral = _matrix_inverse_mod(state[2], n, 3)
    permutations = tuple(_invert_permutation(part) for part in state[3:])
    return (pair, row, dihedral, *permutations)


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


def _componentwise_joint_generators(
    solution: FiniteBraidedSet,
    detectors: Tuple[FiniteBraidedSet, ...],
    n: int,
) -> Tuple[Tuple[int, ComponentwisePairPermutation], ...]:
    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    return tuple(
        (
            signed,
            (
                tuple(
                    action_permutation(detector, n, (signed,))
                    for detector in detectors
                ),
                action_permutation(solution, n, (signed,)),
            ),
        )
        for signed in alphabet
    )


def _componentwise_joint_image_with_words(
    solution: FiniteBraidedSet,
    detectors: Tuple[FiniteBraidedSet, ...],
    n: int,
    state_limit: int,
) -> Tuple[
    dict[ComponentwisePairPermutation, Word],
    Tuple[Tuple[int, ComponentwisePairPermutation], ...],
    bool,
]:
    detector_identity = tuple(
        tuple(range(len(detector.elements) ** n)) for detector in detectors
    )
    solution_identity = tuple(range(len(solution.elements) ** n))
    identity = (detector_identity, solution_identity)
    generators = _componentwise_joint_generators(solution, detectors, n)
    seen: dict[ComponentwisePairPermutation, Word] = {identity: tuple()}
    queue = deque((identity,))
    while queue:
        state = queue.popleft()
        word = seen[state]
        for signed, generator in generators:
            next_state = _compose_componentwise_pair(generator, state)
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


def _subgroup_generated_by_componentwise_pairs(
    identity: ComponentwisePairPermutation,
    generators: Iterable[ComponentwisePairPermutation],
    state_limit: int,
) -> Tuple[set[ComponentwisePairPermutation], bool]:
    generator_tuple = tuple(generator for generator in generators if generator != identity)
    subgroup = {identity}
    queue = deque((identity,))
    while queue:
        state = queue.popleft()
        for generator in generator_tuple:
            next_state = _compose_componentwise_pair(generator, state)
            if next_state in subgroup:
                continue
            subgroup.add(next_state)
            if len(subgroup) > state_limit:
                return subgroup, True
            queue.append(next_state)
    return subgroup, False


def _normal_closure_in_componentwise_joint_image(
    identity: ComponentwisePairPermutation,
    group_elements: Iterable[ComponentwisePairPermutation],
    seeds: Iterable[ComponentwisePairPermutation],
    state_limit: int,
) -> Tuple[set[ComponentwisePairPermutation], bool]:
    seed_tuple = tuple(seed for seed in seeds if seed != identity)
    if not seed_tuple:
        return {identity}, False
    conjugates = []
    for group_element in group_elements:
        inverse = _invert_componentwise_pair(group_element)
        for seed in seed_tuple:
            conjugates.append(
                _compose_componentwise_pair(
                    _compose_componentwise_pair(group_element, seed),
                    inverse,
                )
            )
            if len(conjugates) > state_limit:
                return set((identity,)), True
    return _subgroup_generated_by_componentwise_pairs(
        identity, conjugates, state_limit
    )


def _subgroup_generated_by_permutations(
    identity: Permutation,
    generators: Iterable[Permutation],
    state_limit: int,
) -> Tuple[set[Permutation], bool]:
    generator_tuple = tuple(generator for generator in generators if generator != identity)
    subgroup = {identity}
    queue = deque((identity,))
    while queue:
        state = queue.popleft()
        for generator in generator_tuple:
            next_state = _compose_permutations(generator, state)
            if next_state in subgroup:
                continue
            subgroup.add(next_state)
            if len(subgroup) > state_limit:
                return subgroup, True
            queue.append(next_state)
    return subgroup, False


def _normal_closure_in_permutation_group(
    identity: Permutation,
    group_elements: Iterable[Permutation],
    seeds: Iterable[Permutation],
    state_limit: int,
) -> Tuple[set[Permutation], bool]:
    seed_tuple = tuple(seed for seed in seeds if seed != identity)
    if not seed_tuple:
        return {identity}, False
    conjugates = []
    for group_element in group_elements:
        inverse = _invert_permutation(group_element)
        for seed in seed_tuple:
            conjugates.append(
                _compose_permutations(_compose_permutations(group_element, seed), inverse)
            )
            if len(conjugates) > state_limit:
                return set((identity,)), True
    return _subgroup_generated_by_permutations(identity, conjugates, state_limit)


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


def _componentwise_stabilizer_kernel_generators(
    solution: FiniteBraidedSet,
    detectors: Tuple[FiniteBraidedSet, ...],
    n: int,
) -> Tuple[int, int, Tuple[Permutation, ...]]:
    """Return the X-restrictions of detector-kernel generators.

    The generators are computed as a pointwise stabilizer in the disjoint-union
    permutation action on all detector components and the X component.  Fixing
    every detector point is exactly the kernel of the detector projection, and
    restricting that stabilizer to the X block gives ``rho^X_n(K^Y_n)``.
    """

    try:
        from sympy.combinatorics import Permutation as SympyPermutation
        from sympy.combinatorics import PermutationGroup
    except ImportError as exc:  # pragma: no cover - depends on environment
        raise RuntimeError(
            "componentwise stabilizer cross-effect audit requires sympy"
        ) from exc

    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    detector_degrees = tuple(len(detector.elements) ** n for detector in detectors)
    solution_degree = len(solution.elements) ** n
    component_degrees = detector_degrees + (solution_degree,)
    offsets = []
    total_degree = 0
    for degree in component_degrees:
        offsets.append(total_degree)
        total_degree += degree
    solution_offset = offsets[-1]
    detector_total_degree = solution_offset

    def embed_components(components: Tuple[Permutation, ...]):
        if len(components) != len(component_degrees):
            raise ValueError("component count mismatch")
        array = list(range(total_degree))
        for offset, component in zip(offsets, components):
            for index, image in enumerate(component):
                array[offset + index] = offset + image
        return SympyPermutation(array)

    if not alphabet:
        return 1, 1, tuple()

    generators = []
    for signed in alphabet:
        components = tuple(
            action_permutation(detector, n, (signed,))
            for detector in detectors
        ) + (action_permutation(solution, n, (signed,)),)
        generators.append(embed_components(components))

    group = PermutationGroup(generators)
    fixed_points = list(range(detector_total_degree))
    stabilizer = group.pointwise_stabilizer(fixed_points)
    solution_identity = tuple(range(solution_degree))
    restrictions = []
    for generator in stabilizer.generators:
        array = generator.array_form
        restriction = tuple(
            array[solution_offset + index] - solution_offset
            for index in range(solution_degree)
        )
        if restriction != solution_identity:
            restrictions.append(restriction)
    return int(group.order()), int(stabilizer.order()), tuple(restrictions)


def componentwise_stabilizer_realized_parabolic_cross_effect_audit(
    solution: FiniteBraidedSet,
    detectors: Iterable[FiniteBraidedSet],
    bound: int,
    n: int,
    state_limit: int = 100_000,
) -> RealizedParabolicCrossEffectAudit:
    """Compute the componentwise cross-effect using stabilizer kernels.

    This is an exact alternative to
    ``componentwise_realized_parabolic_cross_effect_audit``.  It replaces BFS
    enumeration of the full joint image by a Schreier-Sims pointwise stabilizer
    calculation on a disjoint-union permutation action.  The finite subgroup
    closures that remain are only in the X-action image, so this is practical
    when the detector image is large but the kernel image in X is small.

    The stabilizer method does not retain braid words for nontrivial witnesses;
    witness words are therefore reported as ``None``.
    """

    detector_tuple = tuple(detectors)
    if not detector_tuple:
        raise ValueError("at least one detector component is required")
    if bound < 1:
        raise ValueError("bound must be positive")
    if n < 1:
        raise ValueError("braid degree must be positive")

    joint_image_size, _kernel_stabilizer_size, kernel_generators = (
        _componentwise_stabilizer_kernel_generators(
            solution,
            detector_tuple,
            n,
        )
    )
    solution_identity = tuple(range(len(solution.elements) ** n))
    kernel_image, kernel_truncated = _subgroup_generated_by_permutations(
        solution_identity,
        kernel_generators,
        state_limit,
    )
    if kernel_truncated:
        return RealizedParabolicCrossEffectAudit(
            bound=bound,
            n=n,
            joint_image_size=joint_image_size,
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
    if len(kernel_image) == 1:
        return RealizedParabolicCrossEffectAudit(
            bound=bound,
            n=n,
            joint_image_size=joint_image_size,
            kernel_image_size=1,
            parabolic_image_size=1,
            quotient_size=1,
            quotient_nontrivial=False,
            seed_count=0,
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=False,
        )

    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    solution_generators = tuple(
        action_permutation(solution, n, (signed,))
        for signed in alphabet
    )
    solution_image, solution_truncated = _subgroup_generated_by_permutations(
        solution_identity,
        solution_generators,
        state_limit,
    )
    if solution_truncated:
        return RealizedParabolicCrossEffectAudit(
            bound=bound,
            n=n,
            joint_image_size=joint_image_size,
            kernel_image_size=len(kernel_image),
            parabolic_image_size=None,
            quotient_size=None,
            quotient_nontrivial=None,
            seed_count=0,
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=True,
        )

    seeds: set[Permutation] = set()
    for width in range(1, min(bound, n) + 1):
        _lower_joint_size, _lower_stabilizer_size, lower_kernel_generators = (
            _componentwise_stabilizer_kernel_generators(
                solution,
                detector_tuple,
                width,
            )
        )
        lower_identity = tuple(range(len(solution.elements) ** width))
        lower_kernel_image, lower_truncated = _subgroup_generated_by_permutations(
            lower_identity,
            lower_kernel_generators,
            state_limit,
        )
        if lower_truncated:
            return RealizedParabolicCrossEffectAudit(
                bound=bound,
                n=n,
                joint_image_size=joint_image_size,
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
        for lower_permutation in lower_kernel_image:
            if lower_permutation == lower_identity:
                continue
            for block_start in range(0, n - width + 1):
                seeds.add(
                    _block_embed_permutation(
                        lower_permutation,
                        len(solution.elements),
                        width,
                        n,
                        block_start,
                    )
                )

    for seed in seeds:
        if seed not in solution_image:
            raise AssertionError("parabolic seed is not in the X-action image")
        if seed not in kernel_image:
            raise AssertionError("parabolic seed is not in the detector-kernel X image")

    parabolic_image, parabolic_truncated = _normal_closure_in_permutation_group(
        solution_identity,
        solution_image,
        seeds,
        state_limit,
    )
    if parabolic_truncated:
        return RealizedParabolicCrossEffectAudit(
            bound=bound,
            n=n,
            joint_image_size=joint_image_size,
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

    first_witness_permutation = None
    for generator in kernel_generators:
        if generator not in parabolic_image:
            first_witness_permutation = generator
            break

    moved, moved_image = (
        (None, None)
        if first_witness_permutation is None
        else _first_moved_tuple(solution, n, first_witness_permutation)
    )
    if len(kernel_image) % len(parabolic_image) != 0:
        raise AssertionError("parabolic image size does not divide kernel image size")
    quotient_size = len(kernel_image) // len(parabolic_image)
    return RealizedParabolicCrossEffectAudit(
        bound=bound,
        n=n,
        joint_image_size=joint_image_size,
        kernel_image_size=len(kernel_image),
        parabolic_image_size=len(parabolic_image),
        quotient_size=quotient_size,
        quotient_nontrivial=first_witness_permutation is not None,
        seed_count=len(seeds),
        first_witness_word=None,
        first_moved_tuple=moved,
        first_moved_tuple_image=moved_image,
        truncated=False,
    )


def componentwise_realized_parabolic_cross_effect_audit(
    solution: FiniteBraidedSet,
    detectors: Iterable[FiniteBraidedSet],
    bound: int,
    n: int,
    state_limit: int = 100_000,
) -> RealizedParabolicCrossEffectAudit:
    """Compute the realized cross-effect for a product detector by components.

    This is equivalent to running ``realized_parabolic_cross_effect_audit`` on
    the Cartesian product rack of all detector components, but the detector
    coordinate is stored as a tuple of component permutation images.  That
    avoids constructing the product rack state set.
    """

    detector_tuple = tuple(detectors)
    if not detector_tuple:
        raise ValueError("at least one detector component is required")
    if bound < 1:
        raise ValueError("bound must be positive")
    if n < 1:
        raise ValueError("braid degree must be positive")

    full_seen, _full_generators, full_truncated = (
        _componentwise_joint_image_with_words(
            solution, detector_tuple, n, state_limit
        )
    )
    detector_identity = tuple(
        tuple(range(len(detector.elements) ** n)) for detector in detector_tuple
    )
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
    seeds: set[ComponentwisePairPermutation] = set()
    for width in range(1, min(bound, n) + 1):
        lower_seen, _lower_generators, lower_truncated = (
            _componentwise_joint_image_with_words(
                solution, detector_tuple, width, state_limit
            )
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
        lower_detector_identity = tuple(
            tuple(range(len(detector.elements) ** width))
            for detector in detector_tuple
        )
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

    parabolic_image, parabolic_truncated = (
        _normal_closure_in_componentwise_joint_image(
            identity,
            full_seen.keys(),
            seeds,
            state_limit,
        )
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


def bounded_deletion_support_q3_compressed_audit(
    solution: FiniteBraidedSet,
    h: int,
    n: int,
    state_limit: int = 100_000,
) -> BoundedDeletionSupportAudit:
    """Compute the ``Q_3`` bounded-deletion obstruction by compressed data.

    The product of all racks of size at most three is detected, on pure
    braids, by pairwise linking mod 2, row-sum linking mod 3, and the
    three-color dihedral rack matrix over ``F_3``.  This helper closes that
    compressed finite image together with the full ``X^n`` action and all
    deletion shadows through ``h``.
    """

    if h < 1:
        raise ValueError("h must be positive")
    if n < 1:
        raise ValueError("braid degree must be positive")

    subsets = _deletion_subsets(n, h)
    pair_indices = {
        pair: index
        for index, pair in enumerate(combinations(range(1, n + 1), 2))
    }
    pair_identity = tuple(0 for _ in pair_indices)
    row_identity = tuple(0 for _ in range(n))
    dihedral_identity = _identity_matrix(n)
    solution_identity = tuple(range(len(solution.elements) ** n))
    deletion_identities = tuple(
        tuple(range(len(solution.elements) ** len(subset)))
        for subset in subsets
    )
    identity: Q3CompressedState = (
        pair_identity,
        row_identity,
        dihedral_identity,
        solution_identity,
        *deletion_identities,
    )
    deletion_start_index = 4

    if n < 2:
        return BoundedDeletionSupportAudit(
            rack_size_bound=3,
            h=h,
            n=n,
            detector_size=2916,
            detector_component_count=3,
            subset_count=len(subsets),
            joint_image_size=1,
            obstruction_size=1,
            obstruction_nontrivial=False,
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=False,
        )

    generators: list[Tuple[Word, Q3CompressedState]] = []
    for left in range(1, n):
        for right in range(left + 1, n + 1):
            word = _pure_generator_word(left, right)
            pair_component = [0] * len(pair_indices)
            pair_component[pair_indices[(left, right)]] = 1
            row_component = [0] * n
            row_component[left - 1] = 1
            row_component[right - 1] = 1
            components: Q3CompressedState = (
                tuple(pair_component),
                tuple(row_component),
                _dihedral_word_matrix(n, word),
                action_permutation(solution, n, word),
                *(
                    deletion_identity
                    if _deleted_pure_generator_word(left, right, subset) is None
                    else action_permutation(
                        solution,
                        len(subset),
                        _deleted_pure_generator_word(left, right, subset),
                    )
                    for subset, deletion_identity in zip(subsets, deletion_identities)
                ),
            )
            generators.append((word, components))
            generators.append(
                (_invert_word(word), _invert_q3_compressed_state(components, n))
            )

    seen: dict[Q3CompressedState, Word] = {identity: tuple()}
    queue = deque((identity,))
    obstruction_solution = {solution_identity}
    first_witness_state = None
    first_witness_word = None

    while queue:
        state = queue.popleft()
        state_word = seen[state]
        for generator_word, generator in generators:
            next_state = _compose_q3_compressed_state(generator, state, n)
            if next_state in seen:
                continue
            next_word = state_word + tuple(generator_word)
            seen[next_state] = next_word
            detector_trivial = (
                next_state[0] == pair_identity
                and next_state[1] == row_identity
                and next_state[2] == dihedral_identity
            )
            deletions_trivial = all(
                next_state[deletion_start_index + index] == deletion_identity
                for index, deletion_identity in enumerate(deletion_identities)
            )
            if detector_trivial and deletions_trivial:
                obstruction_solution.add(next_state[3])
                if next_state[3] != solution_identity and first_witness_state is None:
                    first_witness_state = next_state
                    first_witness_word = next_word
            if len(seen) > state_limit:
                moved, moved_image = (
                    (None, None)
                    if first_witness_state is None
                    else _first_moved_tuple(solution, n, first_witness_state[3])
                )
                return BoundedDeletionSupportAudit(
                    rack_size_bound=3,
                    h=h,
                    n=n,
                    detector_size=2916,
                    detector_component_count=3,
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
        else _first_moved_tuple(solution, n, first_witness_state[3])
    )
    return BoundedDeletionSupportAudit(
        rack_size_bound=3,
        h=h,
        n=n,
        detector_size=2916,
        detector_component_count=3,
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


def bounded_deletion_support_affine_q3_compressed_audit(
    matrix: Iterable[Iterable[int]],
    offset: Iterable[int],
    dimension: int,
    h: int,
    n: int,
    state_limit: int = 100_000,
) -> BoundedDeletionSupportAudit:
    """Compute the ``Q_3`` deletion obstruction for affine ``F_2`` solutions.

    The local crossing is

    ``R(x,y) = M(x,y) + t``

    on ``(F_2^dimension)^2``.  This helper is the affine analogue of
    ``bounded_deletion_support_q3_compressed_audit``: it keeps the small-rack
    detector side as pairwise linking, row-sum linking, and the dihedral
    ``F_3`` matrix, while storing the ``X`` and deleted ``X`` actions as
    augmented affine maps over ``F_2`` instead of permutations of ``X^n``.
    """

    if dimension < 1:
        raise ValueError("dimension must be positive")
    if h < 1:
        raise ValueError("h must be positive")
    if n < 1:
        raise ValueError("braid degree must be positive")

    local_size = 2 * dimension
    local_matrix = _normalize_matrix_flat(matrix, local_size, 2)
    local_offset = _normalize_vector(offset, local_size, 2)
    _matrix_inverse_mod(local_matrix, local_size, 2)

    subsets = _deletion_subsets(n, h)
    pair_indices = {
        pair: index
        for index, pair in enumerate(combinations(range(1, n + 1), 2))
    }
    pair_identity = tuple(0 for _ in pair_indices)
    row_identity = tuple(0 for _ in range(n))
    dihedral_identity = _identity_matrix(n)
    solution_identity = _identity_affine_map(dimension * n)
    deletion_identities = tuple(
        _identity_affine_map(dimension * len(subset))
        for subset in subsets
    )
    identity: Q3CompressedState = (
        pair_identity,
        row_identity,
        dihedral_identity,
        solution_identity,
        *deletion_identities,
    )
    deletion_start_index = 4

    if n < 2:
        return BoundedDeletionSupportAudit(
            rack_size_bound=3,
            h=h,
            n=n,
            detector_size=2916,
            detector_component_count=3,
            subset_count=len(subsets),
            joint_image_size=1,
            obstruction_size=1,
            obstruction_nontrivial=False,
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=False,
        )

    generators: list[Tuple[Word, Q3CompressedState]] = []
    for left in range(1, n):
        for right in range(left + 1, n + 1):
            word = _pure_generator_word(left, right)
            pair_component = [0] * len(pair_indices)
            pair_component[pair_indices[(left, right)]] = 1
            row_component = [0] * n
            row_component[left - 1] = 1
            row_component[right - 1] = 1
            deletion_components = []
            for subset, deletion_identity in zip(subsets, deletion_identities):
                deleted_word = _deleted_pure_generator_word(left, right, subset)
                deletion_components.append(
                    deletion_identity
                    if deleted_word is None
                    else _affine_word_map_mod2(
                        local_matrix,
                        local_offset,
                        dimension,
                        len(subset),
                        deleted_word,
                    )
                )
            components: Q3CompressedState = (
                tuple(pair_component),
                tuple(row_component),
                _dihedral_word_matrix(n, word),
                _affine_word_map_mod2(
                    local_matrix,
                    local_offset,
                    dimension,
                    n,
                    word,
                ),
                *deletion_components,
            )
            generators.append((word, components))
            generators.append(
                (
                    _invert_word(word),
                    _invert_q3_affine_compressed_state(components, n),
                )
            )

    seen: dict[Q3CompressedState, Word] = {identity: tuple()}
    queue = deque((identity,))
    obstruction_solution = {solution_identity}
    first_witness_state = None
    first_witness_word = None

    while queue:
        state = queue.popleft()
        state_word = seen[state]
        for generator_word, generator in generators:
            next_state = _compose_q3_affine_compressed_state(generator, state, n)
            if next_state in seen:
                continue
            next_word = state_word + tuple(generator_word)
            seen[next_state] = next_word
            detector_trivial = (
                next_state[0] == pair_identity
                and next_state[1] == row_identity
                and next_state[2] == dihedral_identity
            )
            deletions_trivial = all(
                next_state[deletion_start_index + index] == deletion_identity
                for index, deletion_identity in enumerate(deletion_identities)
            )
            if detector_trivial and deletions_trivial:
                obstruction_solution.add(next_state[3])
                if next_state[3] != solution_identity and first_witness_state is None:
                    first_witness_state = next_state
                    first_witness_word = next_word
            if len(seen) > state_limit:
                moved, moved_image = (
                    (None, None)
                    if first_witness_state is None
                    else _first_moved_affine_tuple(
                        first_witness_state[3],
                        dimension,
                    )
                )
                return BoundedDeletionSupportAudit(
                    rack_size_bound=3,
                    h=h,
                    n=n,
                    detector_size=2916,
                    detector_component_count=3,
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
        else _first_moved_affine_tuple(first_witness_state[3], dimension)
    )
    return BoundedDeletionSupportAudit(
        rack_size_bound=3,
        h=h,
        n=n,
        detector_size=2916,
        detector_component_count=3,
        subset_count=len(subsets),
        joint_image_size=len(seen),
        obstruction_size=len(obstruction_solution),
        obstruction_nontrivial=any(
            affine_map != solution_identity
            for affine_map in obstruction_solution
        ),
        first_witness_word=first_witness_word,
        first_moved_tuple=moved,
        first_moved_tuple_image=moved_image,
        truncated=False,
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

    detector_components, detector_size = _bounded_deletion_detector_components(
        rack_size_bound
    )
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
            components = _bounded_deletion_generator_components(
                solution,
                detector_components,
                subsets,
                n,
                left,
                right,
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


def _bounded_deletion_detector_components(
    rack_size_bound: int,
) -> Tuple[Tuple[FiniteBraidedSet, ...], int]:
    detector_components = small_rack_representatives(rack_size_bound)
    detector_size = 1
    for detector in detector_components:
        detector_size *= len(detector.elements)
    return detector_components, detector_size


def _bounded_deletion_generator_components(
    solution: FiniteBraidedSet,
    detector_components: Tuple[FiniteBraidedSet, ...],
    subsets: Tuple[Tuple[int, ...], ...],
    n: int,
    left: int,
    right: int,
) -> Tuple[Permutation, ...]:
    word = _pure_generator_word(left, right)
    components: list[Permutation] = [
        action_permutation(detector, n, word)
        for detector in detector_components
    ]
    components.append(action_permutation(solution, n, word))
    for subset in subsets:
        deleted_word = _deleted_pure_generator_word(left, right, subset)
        if deleted_word is None:
            components.append(tuple(range(len(solution.elements) ** len(subset))))
        else:
            components.append(
                action_permutation(solution, len(subset), deleted_word)
            )
    return tuple(components)


def bounded_deletion_support_stabilizer_audit(
    solution: FiniteBraidedSet,
    h: int,
    n: int,
    rack_size_bound: int,
) -> BoundedDeletionSupportAudit:
    """Compute ``E_{X,h,n}`` using permutation-group stabilizers.

    This is an exact alternative to ``bounded_deletion_support_audit``.  It
    embeds the detector components, the full ``X`` action, and all deletion
    shadows into one disjoint-union permutation action.  The obstruction group
    is the image on the ``X^n`` component of the pointwise stabilizer of every
    detector and deletion-shadow component.

    The stabilizer method avoids BFS enumeration of the joint image and can
    close larger arities, but it does not retain braid words for nontrivial
    stabilizer elements.
    """

    if h < 1:
        raise ValueError("h must be positive")
    if n < 1:
        raise ValueError("braid degree must be positive")
    if rack_size_bound < 2:
        raise ValueError("rack_size_bound must be at least 2 for pure deletion")

    try:
        from sympy.combinatorics import Permutation as SympyPermutation
        from sympy.combinatorics import PermutationGroup
    except ImportError as exc:  # pragma: no cover - depends on environment
        raise RuntimeError(
            "bounded_deletion_support_stabilizer_audit requires sympy"
        ) from exc

    detector_components, detector_size = _bounded_deletion_detector_components(
        rack_size_bound
    )
    subsets = _deletion_subsets(n, h)
    solution_degree = len(solution.elements) ** n
    deletion_degrees = tuple(len(solution.elements) ** len(subset) for subset in subsets)
    detector_degrees = tuple(
        len(detector.elements) ** n
        for detector in detector_components
    )
    component_degrees = detector_degrees + (solution_degree,) + deletion_degrees
    solution_component_index = len(detector_degrees)
    offsets = []
    total_degree = 0
    for degree in component_degrees:
        offsets.append(total_degree)
        total_degree += degree
    solution_offset = offsets[solution_component_index]

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

    def embed_components(components: Tuple[Permutation, ...]):
        if len(components) != len(component_degrees):
            raise ValueError("component count mismatch")
        array = list(range(total_degree))
        for offset, component in zip(offsets, components):
            for index, image in enumerate(component):
                array[offset + index] = offset + image
        return SympyPermutation(array)

    generators = []
    for left in range(1, n):
        for right in range(left + 1, n + 1):
            generators.append(
                embed_components(
                    _bounded_deletion_generator_components(
                        solution,
                        detector_components,
                        subsets,
                        n,
                        left,
                        right,
                    )
                )
            )

    group = PermutationGroup(generators)
    fixed_points = []
    for component_index, (offset, degree) in enumerate(
        zip(offsets, component_degrees)
    ):
        if component_index == solution_component_index:
            continue
        fixed_points.extend(range(offset, offset + degree))
    stabilizer = group.pointwise_stabilizer(fixed_points)

    solution_identity = tuple(range(solution_degree))
    nontrivial_restrictions = []
    for generator in stabilizer.generators:
        array = generator.array_form
        restriction = tuple(
            array[solution_offset + index] - solution_offset
            for index in range(solution_degree)
        )
        if restriction != solution_identity:
            nontrivial_restrictions.append(restriction)

    first_restriction = (
        None if not nontrivial_restrictions else nontrivial_restrictions[0]
    )
    if not nontrivial_restrictions:
        obstruction_size = 1
    else:
        obstruction_group = PermutationGroup(
            [
                SympyPermutation(list(restriction))
                for restriction in nontrivial_restrictions
            ]
        )
        obstruction_size = int(obstruction_group.order())

    moved, moved_image = (
        (None, None)
        if first_restriction is None
        else _first_moved_tuple(solution, n, first_restriction)
    )
    return BoundedDeletionSupportAudit(
        rack_size_bound=rack_size_bound,
        h=h,
        n=n,
        detector_size=detector_size,
        detector_component_count=len(detector_components),
        subset_count=len(subsets),
        joint_image_size=int(group.order()),
        obstruction_size=obstruction_size,
        obstruction_nontrivial=obstruction_size != 1,
        first_witness_word=None,
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


def transparent_rack_extension(
    rack: FiniteBraidedSet,
    *,
    rack_tag: Element = "rack",
    transparent_tag: Element = "transparent",
    transparent_value: Element = 0,
) -> FiniteBraidedSet:
    """Adjoin one transparent rack color.

    The added color ``0`` satisfies ``0*y=y`` and ``y*0=0`` in rack notation.
    Equivalently, mixed crossings with the added one-point rack are flips.
    """

    if not is_rack_solution(rack):
        raise ValueError("transparent extension requires a rack-form solution")
    dummy = identity_solution((transparent_value,))
    return flip_disjoint_union_solution(
        rack,
        dummy,
        left_tag=rack_tag,
        right_tag=transparent_tag,
    )


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
