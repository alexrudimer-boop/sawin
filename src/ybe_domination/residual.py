from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from math import factorial, gcd
from typing import Dict, Hashable, Iterable, List, Mapping, Sequence, Tuple

from .artin_longitudes import (
    BraidWord,
    RightStabilizationLongitudeAudit,
    has_identity_longitude_signature,
    right_stabilization_longitude_audit,
)
from .finite_braided_set import Element, FiniteBraidedSet, product_solution
from .finite_group import FiniteGroup, direct_product_group, symmetric_group

BaseTuple = Tuple[Hashable, ...]
FibreTuple = Tuple[Element, ...]
ResidualAction = Dict[BaseTuple, Dict[FibreTuple, FibreTuple]]


def all_tuples(elements: Sequence[Hashable], n: int) -> List[Tuple[Hashable, ...]]:
    return list(product(elements, repeat=n))


def action_permutation(solution: FiniteBraidedSet, n: int, braid_word: BraidWord) -> Tuple[int, ...]:
    tuples = all_tuples(solution.elements, n)
    index = {tup: i for i, tup in enumerate(tuples)}
    return tuple(index[solution.braid_action(braid_word, tup)] for tup in tuples)


def _lcm(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)


def permutation_order(permutation: Sequence[int]) -> int:
    seen = [False] * len(permutation)
    order = 1
    for start in range(len(permutation)):
        if seen[start]:
            continue
        current = start
        cycle_length = 0
        while not seen[current]:
            seen[current] = True
            cycle_length += 1
            current = permutation[current]
        if cycle_length:
            order = _lcm(order, cycle_length)
    return order


def braid_action_order(solution: FiniteBraidedSet, n: int, braid_word: BraidWord) -> int:
    return permutation_order(action_permutation(solution, n, braid_word))


def is_identity_action(solution: FiniteBraidedSet, n: int, braid_word: BraidWord) -> bool:
    for tup in product(solution.elements, repeat=n):
        if solution.braid_action(braid_word, tup) != tuple(tup):
            return False
    return True


@dataclass(frozen=True)
class QuotientMap:
    """A finite braided-set quotient/congruence map pi: X -> Z."""

    total: FiniteBraidedSet
    quotient: FiniteBraidedSet
    pi: Mapping[Element, Hashable]

    def __post_init__(self) -> None:
        if set(self.pi.keys()) != set(self.total.elements):
            raise ValueError("pi must be defined on every total element")
        if any(value not in self.quotient.elements for value in self.pi.values()):
            raise ValueError("pi values must lie in quotient elements")
        if set(self.pi.values()) != set(self.quotient.elements):
            raise ValueError("pi must be onto the quotient")
        self.validate_homomorphism()

    def validate_homomorphism(self) -> None:
        for x, y in product(self.total.elements, repeat=2):
            u, v = self.total.R[(x, y)]
            base_u, base_v = self.quotient.R[(self.pi[x], self.pi[y])]
            if (self.pi[u], self.pi[v]) != (base_u, base_v):
                raise ValueError("pi is not a braided-set homomorphism")

    def base_tuple(self, tup: Sequence[Element]) -> BaseTuple:
        return tuple(self.pi[x] for x in tup)

    def fibre(self, base_tuple: Sequence[Hashable]) -> Tuple[FibreTuple, ...]:
        return tuple(
            tuple(tup)
            for tup in product(self.total.elements, repeat=len(base_tuple))
            if self.base_tuple(tup) == tuple(base_tuple)
        )

    def residual_action(self, n: int, braid_word: BraidWord) -> ResidualAction:
        """Return Delta_n(beta), requiring beta to fix the quotient base."""

        action: ResidualAction = {}
        for base in product(self.quotient.elements, repeat=n):
            base_image = self.quotient.braid_action(braid_word, base)
            if base_image != tuple(base):
                raise ValueError(f"braid word does not fix quotient base {base!r}")
            fibre_action = {}
            for tup in self.fibre(base):
                image = self.total.braid_action(braid_word, tup)
                if self.base_tuple(image) != tuple(base):
                    raise ValueError("total action left the fixed fibre unexpectedly")
                fibre_action[tup] = image
            action[tuple(base)] = fibre_action
        return action

    def residual_is_identity(self, n: int, braid_word: BraidWord) -> bool:
        for base in product(self.quotient.elements, repeat=n):
            if self.quotient.braid_action(braid_word, base) != tuple(base):
                return False
            for tup in self.fibre(base):
                if self.total.braid_action(braid_word, tup) != tup:
                    return False
        return True

    def moved_residual_tuple(
        self, n: int, braid_word: BraidWord
    ) -> Tuple[BaseTuple, FibreTuple, FibreTuple] | None:
        for base in product(self.quotient.elements, repeat=n):
            if self.quotient.braid_action(braid_word, base) != tuple(base):
                continue
            for tup in self.fibre(base):
                image = self.total.braid_action(braid_word, tup)
                if image != tup:
                    return tuple(base), tup, image
        return None


@dataclass(frozen=True)
class QuotientImageKernelSummary:
    """Exact fixed-degree image/kernel data for a quotient action."""

    n: int
    joint_image_size: int | None
    total_image_size: int | None
    base_image_size: int | None
    kernel_size: int | None
    projection_surjective: bool | None
    kernel_contains_nonidentity: bool | None
    first_nonidentity_kernel_word: Tuple[int, ...] | None
    truncated: bool

    @property
    def proves_fixed_n_exact_sequence(self) -> bool:
        return not self.truncated and self.projection_surjective is True


@dataclass(frozen=True)
class ResidualDependencySummary:
    """Coordinate dependency data for one base-fixed residual action."""

    base_tuple: BaseTuple
    braid_word: Tuple[int, ...]
    supports: Tuple[Tuple[int, ...], ...]

    @property
    def max_arity(self) -> int:
        return max((len(support) for support in self.supports), default=0)

    @property
    def is_coordinatewise(self) -> bool:
        return all(len(support) <= 1 for support in self.supports)


@dataclass(frozen=True)
class LocalNormalizedLawPrefixWitnessAudit:
    """One finite-prefix check for a local normalized-law obstruction.

    This is the relative version of a constructive B certificate.  It verifies
    a supplied braid against one finite product group and one quotient/kernel
    detector.  A final B proof still needs such data for every product prefix
    of an enumeration of finite groups.
    """

    source_n: int
    target_n: int
    braid_word: Tuple[int, ...]
    group_orders: Tuple[int, ...]
    product_group_order: int
    source_base_detector_identity_action: bool
    target_base_detector_identity_action: bool
    source_product_identity_signature: bool
    target_product_identity_signature: bool
    source_factor_identity_signatures: Tuple[bool, ...]
    target_factor_identity_signatures: Tuple[bool, ...]
    right_stabilization: RightStabilizationLongitudeAudit
    base_tuple: BaseTuple
    source_base_image: BaseTuple
    source_quotient_base_fixed: bool
    fibre_tuple: FibreTuple
    source_image: FibreTuple
    source_image_base: BaseTuple
    source_stays_over_base: bool
    source_residual_tuple_moved: bool
    stabilized_base_tuple: BaseTuple
    target_base_image: BaseTuple
    target_quotient_base_fixed: bool
    stabilized_fibre_tuple: FibreTuple
    stabilized_image: FibreTuple
    stabilized_image_base: BaseTuple
    target_stays_over_base: bool
    target_residual_tuple_moved: bool
    finite_checks_derived_from_tables: bool = False

    @property
    def source_in_residual_kernel(self) -> bool:
        return (
            self.source_base_detector_identity_action
            and self.source_quotient_base_fixed_derived
            and self.source_stays_over_base_derived
        )

    @property
    def target_in_residual_kernel(self) -> bool:
        return (
            self.target_base_detector_identity_action
            and self.target_quotient_base_fixed_derived
            and self.target_stays_over_base_derived
        )

    @property
    def product_invisibility_survives_stabilization(self) -> bool:
        return (
            self.source_product_identity_signature
            and self.target_product_identity_signature
            and all(self.source_factor_identity_signatures)
            and all(self.target_factor_identity_signatures)
            and self.right_stabilization.stabilization_valid
        )

    @property
    def residual_movement_survives_stabilization(self) -> bool:
        return (
            self.source_residual_tuple_moved_derived
            and self.target_residual_tuple_moved_derived
        )

    @property
    def source_quotient_base_fixed_derived(self) -> bool:
        return self.source_base_image == self.base_tuple

    @property
    def source_stays_over_base_derived(self) -> bool:
        return self.source_image_base == self.base_tuple

    @property
    def source_residual_tuple_moved_derived(self) -> bool:
        return self.source_image != self.fibre_tuple

    @property
    def target_quotient_base_fixed_derived(self) -> bool:
        return self.target_base_image == self.stabilized_base_tuple

    @property
    def target_stays_over_base_derived(self) -> bool:
        return self.stabilized_image_base == self.stabilized_base_tuple

    @property
    def target_residual_tuple_moved_derived(self) -> bool:
        return self.stabilized_image != self.stabilized_fibre_tuple

    @property
    def tuple_checks_match_supplied_flags(self) -> bool:
        return (
            self.source_quotient_base_fixed == self.source_quotient_base_fixed_derived
            and self.source_stays_over_base == self.source_stays_over_base_derived
            and self.source_residual_tuple_moved
            == self.source_residual_tuple_moved_derived
            and self.target_quotient_base_fixed == self.target_quotient_base_fixed_derived
            and self.target_stays_over_base == self.target_stays_over_base_derived
            and self.target_residual_tuple_moved
            == self.target_residual_tuple_moved_derived
        )

    @property
    def proves_one_local_prefix_normalized_law_witness(self) -> bool:
        return (
            self.finite_checks_derived_from_tables
            and self.tuple_checks_match_supplied_flags
            and self.source_in_residual_kernel
            and self.target_in_residual_kernel
            and self.product_invisibility_survives_stabilization
            and self.residual_movement_survives_stabilization
        )


@dataclass(frozen=True)
class LocalSymmetricTowerPrefixSequenceAudit:
    """Finite-prefix check for local witnesses against ``S_1,...,S_k``."""

    degrees: Tuple[int, ...]
    rows: Tuple[LocalNormalizedLawPrefixWitnessAudit, ...]

    @property
    def degrees_are_initial_segment(self) -> bool:
        return self.degrees == tuple(range(1, len(self.degrees) + 1))

    @property
    def row_count_matches_degrees(self) -> bool:
        return len(self.rows) == len(self.degrees)

    @property
    def rows_use_expected_symmetric_orders(self) -> bool:
        if not self.row_count_matches_degrees:
            return False
        return all(
            row.group_orders == (factorial(degree),)
            and row.product_group_order == factorial(degree)
            for degree, row in zip(self.degrees, self.rows)
        )

    @property
    def stabilization_lengths_match_degrees(self) -> bool:
        if not self.row_count_matches_degrees:
            return False
        return all(
            row.target_n - row.source_n == degree
            for degree, row in zip(self.degrees, self.rows)
        )

    @property
    def all_rows_pass(self) -> bool:
        return all(row.proves_one_local_prefix_normalized_law_witness for row in self.rows)

    @property
    def proves_supplied_local_symmetric_tower_prefix(self) -> bool:
        return (
            self.degrees_are_initial_segment
            and self.row_count_matches_degrees
            and self.rows_use_expected_symmetric_orders
            and self.stabilization_lengths_match_degrees
            and self.all_rows_pass
        )


def residual_coordinate_dependency_summary(
    quotient_map: QuotientMap,
    base_tuple: Sequence[Hashable],
    braid_word: BraidWord,
) -> ResidualDependencySummary:
    """Return essential input fibre coordinates for each residual output.

    The braid must fix the supplied quotient base tuple.  The output support
    for coordinate ``j`` contains an input coordinate ``k`` exactly when two
    points in the fixed fibre that differ only at ``k`` can have different
    ``j``-th output coordinates.

    This is an exact finite diagnostic for one base tuple and braid word.  It
    is not a symbolic all-degree proof.
    """

    base = tuple(base_tuple)
    if quotient_map.quotient.braid_action(braid_word, base) != base:
        raise ValueError("braid word does not fix quotient base tuple")
    fibre = quotient_map.fibre(base)
    n = len(base)
    supports = [set() for _ in range(n)]
    images = {
        tup: quotient_map.total.braid_action(braid_word, tup)
        for tup in fibre
    }
    for left in fibre:
        for right in fibre:
            differing = [
                index
                for index, (a, b) in enumerate(zip(left, right))
                if a != b
            ]
            if len(differing) != 1:
                continue
            changed_index = differing[0]
            left_image = images[left]
            right_image = images[right]
            for output_index, (a, b) in enumerate(zip(left_image, right_image)):
                if a != b:
                    supports[output_index].add(changed_index)
    return ResidualDependencySummary(
        base_tuple=base,
        braid_word=tuple(braid_word),
        supports=tuple(tuple(sorted(support)) for support in supports),
    )


def local_normalized_law_prefix_witness_audit(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    braid_word: BraidWord,
    base_tuple: Sequence[Hashable],
    fibre_tuple: Sequence[Element],
    extra_strands: int,
    fill_value: Element,
) -> LocalNormalizedLawPrefixWitnessAudit:
    """Check one supplied local prefix witness for the normalized-law B route.

    The braid is tested against a fixed quotient/base detector, a finite
    product of group-longitude detectors, and one moved residual tuple.  Right
    stabilization is checked by adding unused strands filled with
    ``fill_value``.  This is a finite row of a constructive diagonal
    certificate, not an all-prefix construction by itself.
    """

    if not groups:
        raise ValueError("at least one finite group is required")
    if extra_strands < 0:
        raise ValueError("extra_strands must be nonnegative")
    base = tuple(base_tuple)
    fibre = tuple(fibre_tuple)
    if len(base) != n:
        raise ValueError("base_tuple length must equal n")
    if len(fibre) != n:
        raise ValueError("fibre_tuple length must equal n")
    if any(value not in quotient_map.total.elements for value in fibre):
        raise ValueError("fibre_tuple entries must lie in the total solution")
    if quotient_map.base_tuple(fibre) != base:
        raise ValueError("fibre_tuple must lie over base_tuple")
    if fill_value not in quotient_map.total.elements:
        raise ValueError("fill_value must lie in the total solution")

    group_tuple = tuple(groups)
    product_group = direct_product_group(group_tuple)
    target_n = n + extra_strands
    fill_base = quotient_map.pi[fill_value]
    stabilization = right_stabilization_longitude_audit(
        n,
        braid_word,
        extra_strands,
    )

    source_base_image = quotient_map.quotient.braid_action(braid_word, base)
    source_image = quotient_map.total.braid_action(braid_word, fibre)
    source_image_base = quotient_map.base_tuple(source_image)
    stabilized_base = base + tuple(fill_base for _ in range(extra_strands))
    stabilized_fibre = fibre + tuple(fill_value for _ in range(extra_strands))
    target_base_image = quotient_map.quotient.braid_action(
        braid_word,
        stabilized_base,
    )
    stabilized_image = quotient_map.total.braid_action(
        braid_word,
        stabilized_fibre,
    )
    stabilized_image_base = quotient_map.base_tuple(stabilized_image)

    return LocalNormalizedLawPrefixWitnessAudit(
        source_n=n,
        target_n=target_n,
        braid_word=tuple(braid_word),
        group_orders=tuple(len(group.elements) for group in group_tuple),
        product_group_order=len(product_group.elements),
        source_base_detector_identity_action=is_identity_action(
            base_detector,
            n,
            braid_word,
        ),
        target_base_detector_identity_action=is_identity_action(
            base_detector,
            target_n,
            braid_word,
        ),
        source_product_identity_signature=has_identity_longitude_signature(
            product_group,
            n,
            braid_word,
        ),
        target_product_identity_signature=has_identity_longitude_signature(
            product_group,
            target_n,
            braid_word,
        ),
        source_factor_identity_signatures=tuple(
            has_identity_longitude_signature(group, n, braid_word)
            for group in group_tuple
        ),
        target_factor_identity_signatures=tuple(
            has_identity_longitude_signature(group, target_n, braid_word)
            for group in group_tuple
        ),
        right_stabilization=stabilization,
        base_tuple=base,
        source_base_image=source_base_image,
        source_quotient_base_fixed=source_base_image == base,
        fibre_tuple=fibre,
        source_image=source_image,
        source_image_base=source_image_base,
        source_stays_over_base=source_image_base == base,
        source_residual_tuple_moved=source_image != fibre,
        stabilized_base_tuple=stabilized_base,
        target_base_image=target_base_image,
        target_quotient_base_fixed=target_base_image == stabilized_base,
        stabilized_fibre_tuple=stabilized_fibre,
        stabilized_image=stabilized_image,
        stabilized_image_base=stabilized_image_base,
        target_stays_over_base=stabilized_image_base == stabilized_base,
        target_residual_tuple_moved=stabilized_image != stabilized_fibre,
        finite_checks_derived_from_tables=True,
    )


def local_symmetric_normalized_law_prefix_witness_audit(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    symmetric_degree: int,
    n: int,
    braid_word: BraidWord,
    base_tuple: Sequence[Hashable],
    fibre_tuple: Sequence[Element],
    extra_strands: int,
    fill_value: Element,
) -> LocalNormalizedLawPrefixWitnessAudit:
    """Check one local normalized-law prefix using only the detector ``S_j``."""

    return local_normalized_law_prefix_witness_audit(
        quotient_map,
        base_detector,
        (symmetric_group(symmetric_degree),),
        n,
        braid_word,
        base_tuple,
        fibre_tuple,
        extra_strands,
        fill_value,
    )


def local_symmetric_tower_prefix_sequence_audit(
    degrees: Sequence[int],
    rows: Sequence[LocalNormalizedLawPrefixWitnessAudit],
) -> LocalSymmetricTowerPrefixSequenceAudit:
    """Bundle supplied local symmetric-tower rows into one finite-prefix audit."""

    degree_tuple = tuple(degrees)
    if any(degree <= 0 for degree in degree_tuple):
        raise ValueError("symmetric degrees must be positive")
    return LocalSymmetricTowerPrefixSequenceAudit(
        degrees=degree_tuple,
        rows=tuple(rows),
    )


def _compose_permutations(left: Tuple[int, ...], right: Tuple[int, ...]) -> Tuple[int, ...]:
    """Return left after right."""

    if len(left) != len(right):
        raise ValueError("permutations must have the same size")
    return tuple(left[right[i]] for i in range(len(left)))


def quotient_image_kernel_summary(
    quotient_map: QuotientMap,
    n: int,
    state_limit: int = 100_000,
) -> QuotientImageKernelSummary:
    """Return the exact finite image/kernel sequence for one braid degree.

    The braid action on ``total^n`` projects to the braid action on
    ``quotient^n``.  For fixed ``n`` this helper closes the finite joint image
    generated by the corresponding braid generators and reports the kernel of
    the projection to the quotient image.  The kernel is exactly the fixed-
    degree residual image of base-fixing braids.

    This is a finite-degree structural certificate, not an all-``n`` proof.
    """

    if n < 1:
        raise ValueError("braid degree must be positive")
    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    total_identity = tuple(range(len(quotient_map.total.elements) ** n))
    base_identity = tuple(range(len(quotient_map.quotient.elements) ** n))
    if not alphabet:
        return QuotientImageKernelSummary(
            n=n,
            joint_image_size=1,
            total_image_size=1,
            base_image_size=1,
            kernel_size=1,
            projection_surjective=True,
            kernel_contains_nonidentity=False,
            first_nonidentity_kernel_word=None,
            truncated=False,
        )

    total_generators = {
        signed: action_permutation(quotient_map.total, n, (signed,))
        for signed in alphabet
    }
    base_generators = {
        signed: action_permutation(quotient_map.quotient, n, (signed,))
        for signed in alphabet
    }

    initial = (base_identity, total_identity, tuple())
    queue = [initial]
    seen = {(base_identity, total_identity)}
    total_image = {total_identity}
    base_projection = {base_identity}
    kernel_total = {total_identity}
    first_nonidentity_kernel_word = None
    cursor = 0
    truncated = False
    while cursor < len(queue):
        base_state, total_state, word = queue[cursor]
        cursor += 1
        for signed in alphabet:
            next_word = word + (signed,)
            next_base = _compose_permutations(base_generators[signed], base_state)
            next_total = _compose_permutations(total_generators[signed], total_state)
            key = (next_base, next_total)
            if key in seen:
                continue
            seen.add(key)
            total_image.add(next_total)
            base_projection.add(next_base)
            if next_base == base_identity:
                kernel_total.add(next_total)
                if next_total != total_identity and first_nonidentity_kernel_word is None:
                    first_nonidentity_kernel_word = next_word
            if len(seen) > state_limit:
                truncated = True
                return QuotientImageKernelSummary(
                    n=n,
                    joint_image_size=None,
                    total_image_size=None,
                    base_image_size=None,
                    kernel_size=None,
                    projection_surjective=None,
                    kernel_contains_nonidentity=None,
                    first_nonidentity_kernel_word=first_nonidentity_kernel_word,
                    truncated=True,
                )
            queue.append((next_base, next_total, next_word))

    base_image = set()
    base_queue = [base_identity]
    base_image.add(base_identity)
    cursor = 0
    while cursor < len(base_queue):
        base_state = base_queue[cursor]
        cursor += 1
        for signed in alphabet:
            next_base = _compose_permutations(base_generators[signed], base_state)
            if next_base in base_image:
                continue
            base_image.add(next_base)
            if len(base_image) > state_limit:
                return QuotientImageKernelSummary(
                    n=n,
                    joint_image_size=None,
                    total_image_size=None,
                    base_image_size=None,
                    kernel_size=None,
                    projection_surjective=None,
                    kernel_contains_nonidentity=None,
                    first_nonidentity_kernel_word=first_nonidentity_kernel_word,
                    truncated=True,
                )
            base_queue.append(next_base)

    return QuotientImageKernelSummary(
        n=n,
        joint_image_size=len(seen),
        total_image_size=len(total_image),
        base_image_size=len(base_image),
        kernel_size=len(kernel_total),
        projection_surjective=base_projection == base_image,
        kernel_contains_nonidentity=any(item != total_identity for item in kernel_total),
        first_nonidentity_kernel_word=first_nonidentity_kernel_word,
        truncated=truncated,
    )


def sharp_kernel_implication_failures(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    group: FiniteGroup,
    n: int,
    braid_words: Iterable[BraidWord],
) -> Dict[Tuple[int, ...], Tuple[BaseTuple, FibreTuple, FibreTuple]]:
    """Bounded failures of the sharp kernel implication.

    This checks words in the supplied iterable.  It is useful for auditing
    examples but cannot prove the universal theorem by itself.
    """

    failures = {}
    for word in braid_words:
        key = tuple(word)
        if not is_identity_action(base_detector, n, key):
            continue
        if not has_identity_longitude_signature(group, n, key):
            continue
        moved = quotient_map.moved_residual_tuple(n, key)
        if moved is not None:
            failures[key] = moved
    return failures


def bounded_words(n: int, max_length: int) -> List[Tuple[int, ...]]:
    """Enumerate braid words over sigma_i^{+-1} up to a length bound."""

    if n < 2:
        return [tuple()]
    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    words = [tuple()]
    frontier = [tuple()]
    for _ in range(max_length):
        next_frontier = []
        for word in frontier:
            for letter in alphabet:
                if word and word[-1] == -letter:
                    continue
                new_word = word + (letter,)
                words.append(new_word)
                next_frontier.append(new_word)
        frontier = next_frontier
    return words
