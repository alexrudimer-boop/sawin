from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from math import prod as math_prod
from typing import Iterable, Mapping, Sequence, Tuple

from .artin_longitudes import (
    BraidWord,
    LongitudeSubgroupProfileRow,
    finite_group_longitude_signature,
    has_identity_longitude_signature,
    longitude_subgroup_profile,
)
from .finite_braided_set import FiniteBraidedSet, identity_solution, opposite_solution
from .finite_group import (
    FiniteGroup,
    cyclic_group,
    direct_product_group,
    permutation_group_from_generators,
    symmetric_group,
)
from .green_branch import (
    atom_quotient_inner_group,
    atom_quotient_rack_audit,
    green_branch_audits,
    kernel_action_summary,
    schutzenberger_action_groups,
)
from .group_laws import two_strand_longitude_period, two_strand_symmetric_longitude_period
from .residual import QuotientMap, is_identity_action
from .residual import ResidualDependencySummary, residual_coordinate_dependency_summary
from .residual import action_permutation, permutation_order

Permutation = Tuple[int, ...]
DetectorRow = Tuple[Tuple[object, ...], Tuple[object, ...]]
DetectorState = Tuple[DetectorRow, ...]
IntDetectorState = Tuple[int, ...]


def kernel_action_groups(solution: FiniteBraidedSet) -> Tuple[FiniteGroup, ...]:
    """Return the actual kernel-block permutation groups from retained labels."""

    groups = []
    seen = set()
    for summary in kernel_action_summary(solution):
        degree = len(summary.kernel_partition)
        if degree < 2:
            continue
        generators = tuple(permutation for _label, permutation in summary.induced_permutations)
        group = permutation_group_from_generators(generators, degree=degree)
        key = group.elements
        if key not in seen:
            seen.add(key)
            groups.append(group)
    return tuple(groups)


def kernel_symmetric_groups(
    solution: FiniteBraidedSet, max_degree: int | None = None
) -> Tuple[FiniteGroup, ...]:
    """Return full symmetric groups on kernel-block quotients.

    These are candidate detector factors stronger than the actual
    Schutzenberger/kernel action image: a word invisible to `Sym(d)` is a law
    for every possible `d`-block kernel action.
    """

    degrees = sorted(
        {
            len(summary.kernel_partition)
            for summary in kernel_action_summary(solution)
            if len(summary.kernel_partition) >= 2
            and (max_degree is None or len(summary.kernel_partition) <= max_degree)
        }
    )
    return tuple(symmetric_group(degree) for degree in degrees)


def two_sided_kernel_symmetric_groups(
    solution: FiniteBraidedSet, max_degree: int | None = None
) -> Tuple[FiniteGroup, ...]:
    """Return full symmetric kernel-block groups for left and right actions."""

    groups = (
        *kernel_symmetric_groups(solution, max_degree=max_degree),
        *kernel_symmetric_groups(opposite_solution(solution), max_degree=max_degree),
    )
    unique = []
    seen = set()
    for group in groups:
        key = (
            group.elements,
            tuple(sorted(group.multiply_table.items(), key=repr)),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(group)
    return tuple(unique)


def _deduplicate_groups(groups: Iterable[FiniteGroup]) -> Tuple[FiniteGroup, ...]:
    unique = []
    seen = set()
    for group in groups:
        key = (
            group.elements,
            tuple(sorted(group.multiply_table.items(), key=repr)),
        )
        if key in seen:
            continue
        seen.add(key)
        unique.append(group)
    return tuple(unique)


def schutzenberger_groups(solution: FiniteBraidedSet) -> Tuple[FiniteGroup, ...]:
    """Return finite Schutzenberger action groups from left Green classes."""

    return _deduplicate_groups(summary.group for summary in schutzenberger_action_groups(solution))


def two_sided_schutzenberger_groups(solution: FiniteBraidedSet) -> Tuple[FiniteGroup, ...]:
    """Return finite Schutzenberger action groups from left and right Green data."""

    return _deduplicate_groups(
        (
            *schutzenberger_groups(solution),
            *schutzenberger_groups(opposite_solution(solution)),
        )
    )


def atom_quotient_inner_groups(solution: FiniteBraidedSet) -> Tuple[FiniteGroup, ...]:
    """Return inner groups of proved Green atom-rack quotient layers."""

    groups = []
    for audit in green_branch_audits(solution):
        rack_audit = atom_quotient_rack_audit(audit)
        if not rack_audit.proves_right_rack_ybe_layer:
            continue
        group = atom_quotient_inner_group(audit)
        if len(group.elements) <= 1:
            continue
        groups.append(group)
    return _deduplicate_groups(groups)


def two_sided_atom_quotient_inner_groups(
    solution: FiniteBraidedSet,
) -> Tuple[FiniteGroup, ...]:
    """Return atom-rack inner groups from left and right Green data."""

    return _deduplicate_groups(
        (
            *atom_quotient_inner_groups(solution),
            *atom_quotient_inner_groups(opposite_solution(solution)),
        )
    )


def two_sided_green_detector_groups(
    solution: FiniteBraidedSet,
    max_kernel_degree: int | None = None,
) -> Tuple[FiniteGroup, ...]:
    """Return the explicit finite Green detector factors currently proposed."""

    return _deduplicate_groups(
        (
            *two_sided_kernel_symmetric_groups(solution, max_degree=max_kernel_degree),
            *two_sided_schutzenberger_groups(solution),
            *two_sided_atom_quotient_inner_groups(solution),
        )
    )


def two_sided_green_detector_product(
    solution: FiniteBraidedSet,
    max_kernel_degree: int | None = None,
) -> FiniteGroup:
    """Return one finite product group for the proposed two-sided Green detector."""

    return direct_product_group(
        two_sided_green_detector_groups(
            solution,
            max_kernel_degree=max_kernel_degree,
        )
    )


def two_strand_crossing_order(solution: FiniteBraidedSet) -> int:
    """Return the order of the two-strand crossing action of a finite solution."""

    return permutation_order(action_permutation(solution, 2, (1,)))


def two_strand_group_detector_covers_solution(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
) -> bool:
    """Return the exact B_2 kernel-containment test for one detector group."""

    return two_strand_longitude_period(group) % two_strand_crossing_order(solution) == 0


def two_strand_group_detector_failure_certificate(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
) -> "TwoStrandDetectorFailureCertificate | None":
    """Return the explicit ``B_2`` obstruction when one group is too small.

    For a finite group ``G``, the exact finite-``G`` longitude kernel on
    ``B_2`` is generated by ``sigma_1^(2*exp(G))``.  If the crossing order of
    ``X`` does not divide this period, that braid is invisible to ``G`` but
    still moves an explicit tuple of ``X^2``.
    """

    period = two_strand_longitude_period(group)
    crossing_order = two_strand_crossing_order(solution)
    if period % crossing_order == 0:
        return None
    braid_word = (1,) * period
    moved = first_moved_tuple(solution, 2, braid_word)
    if moved is None:
        raise RuntimeError("crossing-order gate failed but no moved tuple was found")
    return TwoStrandDetectorFailureCertificate(
        group_order=len(group.elements),
        longitude_period=period,
        crossing_order=crossing_order,
        braid_word=braid_word,
        moved=moved,
    )


def two_strand_cyclic_detector_certificate(
    solution: FiniteBraidedSet,
) -> TwoStrandCyclicDetectorCertificate:
    """Return a cyclic finite-group detector for the two-strand action.

    Taking ``G=C_r`` for ``r=ord(R_X)`` gives finite-G longitude period
    ``2r`` on ``B_2``.  Hence every braid invisible to this cyclic detector is
    a multiple of ``2r`` and acts trivially on the crossing action.  This
    proves that no counterexample can be purely two-strand; B must use
    unbounded braid degree and normalized laws.
    """

    crossing_order = two_strand_crossing_order(solution)
    group = cyclic_group(crossing_order)
    period = two_strand_longitude_period(group)
    return TwoStrandCyclicDetectorCertificate(
        crossing_order=crossing_order,
        group_order=crossing_order,
        longitude_period=period,
        kernel_containment_holds=period % crossing_order == 0,
    )


def two_strand_symmetric_detector_covers_solution(solution: FiniteBraidedSet) -> bool:
    """Return the exact B_2 test for the direct ``Sym(X)`` detector."""

    return (
        two_strand_symmetric_longitude_period(len(solution.elements))
        % two_strand_crossing_order(solution)
        == 0
    )


def two_strand_symmetric_detector_failure_certificate(
    solution: FiniteBraidedSet,
) -> "TwoStrandDetectorFailureCertificate | None":
    """Return the explicit two-strand obstruction to the direct Sym detector."""

    return two_strand_group_detector_failure_certificate(
        solution,
        symmetric_group(len(solution.elements)),
    )


def invisible_to_all_groups(
    groups: Iterable[FiniteGroup], n: int, braid_word: BraidWord
) -> bool:
    return all(has_identity_longitude_signature(group, n, braid_word) for group in groups)


def first_moved_tuple(
    solution: FiniteBraidedSet, n: int, braid_word: BraidWord
) -> Tuple[Tuple[object, ...], Tuple[object, ...]] | None:
    for tup in product(solution.elements, repeat=n):
        image = solution.braid_action(braid_word, tup)
        if image != tup:
            return tuple(tup), image
    return None


def detector_blind_movers(
    solution: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    braid_words: Iterable[BraidWord],
):
    """Return bounded words invisible to all groups but moving the solution."""

    out = {}
    for word in braid_words:
        key = tuple(word)
        if not invisible_to_all_groups(groups, n, key):
            continue
        moved = first_moved_tuple(solution, n, key)
        if moved is not None:
            out[key] = moved
    return out


def residual_detector_blind_movers(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    braid_words: Iterable[BraidWord],
):
    """Return bounded residual movers invisible to all groups.

    This is the bounded version of the sharp-kernel implication: words must
    lie in the chosen base detector kernel, must have identity finite-group
    longitude data for every listed group, and must still move a fibre tuple
    of the quotient map.
    """

    out = {}
    for word in braid_words:
        key = tuple(word)
        if not is_identity_action(base_detector, n, key):
            continue
        if not invisible_to_all_groups(groups, n, key):
            continue
        moved = quotient_map.moved_residual_tuple(n, key)
        if moved is not None:
            out[key] = moved
    return out


def group_detector_signature(
    groups: Sequence[FiniteGroup], n: int, braid_word: BraidWord
):
    """Return finite-group longitude signatures for all listed groups."""

    return tuple(
        finite_group_longitude_signature(group, n, braid_word)
        for group in groups
    )


def residual_action_signature(
    quotient_map: QuotientMap, n: int, braid_word: BraidWord
):
    """Return a deterministic residual-action signature, or None if not base-fixed."""

    try:
        action = quotient_map.residual_action(n, braid_word)
    except ValueError:
        return None
    return tuple(
        sorted(
            (
                repr(base),
                tuple(sorted((repr(start), repr(image)) for start, image in fibre.items())),
            )
            for base, fibre in action.items()
        )
    )


def detector_collision_failures(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    braid_words: Iterable[BraidWord],
    max_failures: int = 5,
):
    """Find bounded failures of detector-signature => residual-action equality."""

    seen = {}
    failures = []
    for word in braid_words:
        key = tuple(word)
        if not is_identity_action(base_detector, n, key):
            continue
        detector = group_detector_signature(groups, n, key)
        residual = residual_action_signature(quotient_map, n, key)
        if residual is None:
            continue
        if detector in seen and seen[detector][1] != residual:
            failures.append(
                {
                    "first_word": seen[detector][0],
                    "second_word": key,
                    "first_residual": seen[detector][1],
                    "second_residual": residual,
                }
            )
            if len(failures) >= max_failures:
                break
        else:
            seen[detector] = (key, residual)
    return tuple(failures)


@dataclass(frozen=True)
class ExactImageAudit:
    n: int
    visited_state_count: int
    detector_state_count: int
    residual_state_count: int
    base_kernel_detector_state_count: int
    base_kernel_residual_state_count: int
    truncated: bool
    kernel_failure: Tuple[int, ...] | None
    collision_failure: Tuple[Tuple[int, ...], Tuple[int, ...]] | None

    @property
    def proves_fixed_n_implication(self) -> bool:
        return (
            not self.truncated
            and self.kernel_failure is None
            and self.collision_failure is None
        )


@dataclass(frozen=True)
class DetectorReadoutRow:
    """One row of a fixed-index detector-state readout table."""

    representative_braid_word: Tuple[int, ...]
    residual_permutation: Permutation
    preserves_quotient_fibres: bool
    moved_base_tuple_count: int
    moved_total_tuple_count: int


@dataclass(frozen=True)
class ExactDetectorReadoutAudit:
    """Materialize the fixed-index residual readout when it is well-defined."""

    n: int
    visited_state_count: int
    detector_state_count: int
    residual_state_count: int
    base_kernel_detector_state_count: int
    base_kernel_residual_state_count: int
    truncated: bool
    kernel_failure: Tuple[int, ...] | None
    collision_failure: Tuple[Tuple[int, ...], Tuple[int, ...]] | None
    readout_rows: Tuple[DetectorReadoutRow, ...]

    @property
    def readout_state_count(self) -> int:
        return len(self.readout_rows)

    @property
    def proves_fixed_n_readout(self) -> bool:
        return (
            not self.truncated
            and self.kernel_failure is None
            and self.collision_failure is None
            and self.readout_state_count == self.base_kernel_detector_state_count
            and all(row.preserves_quotient_fibres for row in self.readout_rows)
        )


@dataclass(frozen=True)
class ExactDetectorProductReadoutAudit:
    """Compare factor-list readouts with the single product detector readout."""

    n: int
    factor_orders: Tuple[int, ...]
    product_group_order: int
    product_skipped: bool
    factor_audit: ExactDetectorReadoutAudit
    product_audit: ExactDetectorReadoutAudit | None
    factor_residual_readouts: Tuple[Permutation, ...]
    product_residual_readouts: Tuple[Permutation, ...] | None
    readout_state_counts_match: bool | None
    proof_status_matches: bool | None
    residual_readouts_match: bool | None

    @property
    def product_readout_equivalent_when_enumerated(self) -> bool | None:
        if self.product_skipped:
            return None
        return (
            self.readout_state_counts_match is True
            and self.proof_status_matches is True
            and self.residual_readouts_match is True
        )


@dataclass(frozen=True)
class TwoStrandDetectorFailureCertificate:
    """Explicit two-strand finite-group detector failure."""

    group_order: int
    longitude_period: int
    crossing_order: int
    braid_word: Tuple[int, ...]
    moved: Tuple[Tuple[object, ...], Tuple[object, ...]]

    @property
    def braid_is_group_longitude_invisible(self) -> bool:
        """Return the exact B_2 finite-group invisibility check."""

        return len(self.braid_word) == self.longitude_period

    @property
    def braid_moves_solution(self) -> bool:
        return self.moved[0] != self.moved[1]

    @property
    def proves_group_detector_failure(self) -> bool:
        return (
            self.longitude_period % self.crossing_order != 0
            and self.braid_is_group_longitude_invisible
            and self.braid_moves_solution
        )


@dataclass(frozen=True)
class TwoStrandCyclicDetectorCertificate:
    """A cyclic finite-group detector for one two-strand crossing action."""

    crossing_order: int
    group_order: int
    longitude_period: int
    kernel_containment_holds: bool

    @property
    def detector_group(self) -> FiniteGroup:
        return cyclic_group(self.group_order)


@dataclass(frozen=True)
class DetectorBlindDependencyFailure:
    """A bounded residual mover, together with fibre-coordinate dependencies."""

    braid_word: Tuple[int, ...]
    moved: Tuple[Tuple[object, ...], Tuple[object, ...], Tuple[object, ...]]
    dependency_summaries: Tuple[ResidualDependencySummary, ...]

    @property
    def max_arity(self) -> int:
        return max(
            (summary.max_arity for summary in self.dependency_summaries),
            default=0,
        )

    @property
    def has_multi_input_support(self) -> bool:
        return self.max_arity > 1


@dataclass(frozen=True)
class LongitudeSubgroupMoverProfile:
    """A moving braid word together with compact finite-group visibility rows."""

    braid_word: Tuple[int, ...]
    moved: Tuple[Tuple[object, ...], Tuple[object, ...]]
    subgroup_profile: Tuple[LongitudeSubgroupProfileRow, ...]

    @property
    def all_groups_invisible(self) -> bool:
        return all(row.identity_longitude_signature for row in self.subgroup_profile)

    @property
    def visible_group_names(self) -> Tuple[str, ...]:
        return tuple(
            row.name
            for row in self.subgroup_profile
            if not row.identity_longitude_signature
        )


@dataclass(frozen=True)
class ResidualLongitudeSubgroupMoverProfile:
    """A residual mover with compact finite-group longitude-subgroup rows."""

    braid_word: Tuple[int, ...]
    moved: Tuple[Tuple[object, ...], Tuple[object, ...], Tuple[object, ...]]
    subgroup_profile: Tuple[LongitudeSubgroupProfileRow, ...]

    @property
    def all_groups_invisible(self) -> bool:
        return all(row.identity_longitude_signature for row in self.subgroup_profile)

    @property
    def visible_group_names(self) -> Tuple[str, ...]:
        return tuple(
            row.name
            for row in self.subgroup_profile
            if not row.identity_longitude_signature
        )


def _compose_permutation(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    if len(left) != len(right):
        raise ValueError("permutations must have same size")
    return tuple(left[right[i]] for i in range(len(left)))


def residual_detector_dependency_failures(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    braid_words: Iterable[BraidWord],
    max_failures: int = 5,
) -> Tuple[DetectorBlindDependencyFailure, ...]:
    """Return bounded detector-blind residual movers with dependency support.

    This refines ``residual_detector_blind_movers`` by recording, for every
    quotient base tuple fixed by the word, which input fibre coordinates each
    residual output coordinate depends on.  It is a finite diagnostic for
    classifying proposed failures as coordinatewise/product-like or
    multi-input/Green-corridor-like.
    """

    failures = []
    for word in braid_words:
        key = tuple(word)
        if not is_identity_action(base_detector, n, key):
            continue
        if not invisible_to_all_groups(groups, n, key):
            continue
        moved = quotient_map.moved_residual_tuple(n, key)
        if moved is None:
            continue
        summaries = []
        for base in product(quotient_map.quotient.elements, repeat=n):
            if quotient_map.quotient.braid_action(key, base) != tuple(base):
                continue
            summaries.append(
                residual_coordinate_dependency_summary(quotient_map, base, key)
            )
        failures.append(
            DetectorBlindDependencyFailure(
                braid_word=key,
                moved=moved,
                dependency_summaries=tuple(summaries),
            )
        )
        if len(failures) >= max_failures:
            break
    return tuple(failures)


def longitude_subgroup_mover_profiles(
    solution: FiniteBraidedSet,
    groups: Mapping[str, FiniteGroup],
    n: int,
    braid_words: Iterable[BraidWord],
    *,
    require_invisible: bool = False,
    max_profiles: int = 5,
    max_assignments: int | None = None,
) -> Tuple[LongitudeSubgroupMoverProfile, ...]:
    """Return moving words annotated by compact longitude-subgroup profiles.

    This is a bounded diagnostic for B-candidate words.  With
    ``require_invisible=True`` it keeps only words whose profile is identity
    for every listed finite group.
    """

    profiles = []
    for word in braid_words:
        key = tuple(word)
        moved = first_moved_tuple(solution, n, key)
        if moved is None:
            continue
        subgroup_rows = longitude_subgroup_profile(
            groups,
            n,
            key,
            max_assignments=max_assignments,
        )
        profile = LongitudeSubgroupMoverProfile(
            braid_word=key,
            moved=moved,
            subgroup_profile=subgroup_rows,
        )
        if require_invisible and not profile.all_groups_invisible:
            continue
        profiles.append(profile)
        if len(profiles) >= max_profiles:
            break
    return tuple(profiles)


def residual_longitude_subgroup_mover_profiles(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    groups: Mapping[str, FiniteGroup],
    n: int,
    braid_words: Iterable[BraidWord],
    *,
    require_invisible: bool = False,
    max_profiles: int = 5,
    max_assignments: int | None = None,
) -> Tuple[ResidualLongitudeSubgroupMoverProfile, ...]:
    """Return residual movers annotated by compact subgroup visibility rows."""

    profiles = []
    for word in braid_words:
        key = tuple(word)
        if not is_identity_action(base_detector, n, key):
            continue
        moved = quotient_map.moved_residual_tuple(n, key)
        if moved is None:
            continue
        subgroup_rows = longitude_subgroup_profile(
            groups,
            n,
            key,
            max_assignments=max_assignments,
        )
        profile = ResidualLongitudeSubgroupMoverProfile(
            braid_word=key,
            moved=moved,
            subgroup_profile=subgroup_rows,
        )
        if require_invisible and not profile.all_groups_invisible:
            continue
        profiles.append(profile)
        if len(profiles) >= max_profiles:
            break
    return tuple(profiles)


def _solution_generator_permutation(
    solution: FiniteBraidedSet, n: int, signed_generator: int
) -> Permutation:
    tuples = tuple(product(solution.elements, repeat=n))
    index = {tup: i for i, tup in enumerate(tuples)}
    generator = abs(signed_generator) - 1
    inverse = signed_generator < 0
    return tuple(
        index[solution.apply_R_at(tup, generator, inverse=inverse)]
        for tup in tuples
    )


def _group_detector_initial_state(group: FiniteGroup, n: int) -> DetectorState:
    identity_tuple = tuple(group.identity for _ in range(n))
    return tuple((tuple(assignment), identity_tuple) for assignment in product(group.elements, repeat=n))


def _group_int_tables(group: FiniteGroup):
    index = {element: i for i, element in enumerate(group.elements)}
    mul = tuple(
        tuple(index[group.mul(a, b)] for b in group.elements)
        for a in group.elements
    )
    inv = tuple(index[group.inv(a)] for a in group.elements)
    identity = index[group.identity]
    return len(group.elements), identity, mul, inv


def _conjugate_int(mul, inv, left: int, right: int) -> int:
    return mul[mul[left][right]][inv[left]]


def _group_detector_initial_int_state(group: FiniteGroup, n: int) -> IntDetectorState:
    size, identity, _mul, _inv = _group_int_tables(group)
    out = []
    for assignment in product(range(size), repeat=n):
        out.extend(assignment)
        out.extend([identity] * n)
    return tuple(out)


def _apply_group_detector_generator_int(
    group: FiniteGroup,
    state: IntDetectorState,
    signed_generator: int,
    n: int,
    tables=None,
) -> IntDetectorState:
    if tables is None:
        tables = _group_int_tables(group)
    _size, _identity, mul, inv = tables
    i = abs(signed_generator) - 1
    row_width = 2 * n
    out = list(state)
    for offset in range(0, len(state), row_width):
        image_offset = offset
        longitude_offset = offset + n
        left_image = state[image_offset + i]
        right_image = state[image_offset + i + 1]
        left_longitude = state[longitude_offset + i]
        right_longitude = state[longitude_offset + i + 1]
        if signed_generator > 0:
            out[image_offset + i] = _conjugate_int(mul, inv, left_image, right_image)
            out[longitude_offset + i] = mul[left_image][right_longitude]
            out[image_offset + i + 1] = left_image
            out[longitude_offset + i + 1] = left_longitude
        else:
            out[image_offset + i] = right_image
            out[longitude_offset + i] = right_longitude
            out[image_offset + i + 1] = _conjugate_int(
                mul, inv, inv[right_image], left_image
            )
            out[longitude_offset + i + 1] = mul[inv[right_image]][left_longitude]
    return tuple(out)


def _apply_group_detector_generator(
    group: FiniteGroup, state: DetectorState, signed_generator: int
) -> DetectorState:
    i = abs(signed_generator) - 1
    out = []
    for images, longitudes in state:
        images_list = list(images)
        longitudes_list = list(longitudes)
        left_image, right_image = images_list[i], images_list[i + 1]
        left_longitude, right_longitude = longitudes_list[i], longitudes_list[i + 1]
        if signed_generator > 0:
            images_list[i] = group.conjugate(left_image, right_image)
            longitudes_list[i] = group.mul(left_image, right_longitude)
            images_list[i + 1] = left_image
            longitudes_list[i + 1] = left_longitude
        else:
            images_list[i] = right_image
            longitudes_list[i] = right_longitude
            images_list[i + 1] = group.conjugate(group.inv(right_image), left_image)
            longitudes_list[i + 1] = group.mul(group.inv(right_image), left_longitude)
        out.append((tuple(images_list), tuple(longitudes_list)))
    return tuple(out)


def exact_detector_image_audit(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    state_limit: int = 10000,
) -> ExactImageAudit:
    """Explore the exact finite joint image for one braid index.

    The detector state is `(base action, finite-group Artin-longitude data)`.
    The residual state is represented by the total action permutation.  A
    collision failure is a pair of braid words with equal detector state,
    base action identity, and different residual action.
    """

    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    base_identity = tuple(range(len(base_detector.elements) ** n))
    total_identity = tuple(range(len(quotient_map.total.elements) ** n))
    group_initial = tuple(_group_detector_initial_int_state(group, n) for group in groups)
    group_tables = tuple(_group_int_tables(group) for group in groups)

    base_generators = {
        signed: _solution_generator_permutation(base_detector, n, signed)
        for signed in alphabet
    }
    total_generators = {
        signed: _solution_generator_permutation(quotient_map.total, n, signed)
        for signed in alphabet
    }

    initial = (base_identity, total_identity, group_initial, tuple())
    queue = deque([initial])
    visited = {(base_identity, total_identity, group_initial)}
    detector_states = {(base_identity, group_initial)}
    residual_states = {total_identity}
    base_kernel_detector_states = {(base_identity, group_initial)}
    base_kernel_residual_states = {total_identity}
    residual_by_detector = {(base_identity, group_initial): (total_identity, tuple())}
    truncated = False

    while queue:
        base_state, total_state, group_state, word = queue.popleft()
        for signed in alphabet:
            next_word = word + (signed,)
            next_base = _compose_permutation(base_generators[signed], base_state)
            next_total = _compose_permutation(total_generators[signed], total_state)
            next_groups = tuple(
                _apply_group_detector_generator_int(group, state, signed, n, tables)
                for group, state, tables in zip(groups, group_state, group_tables)
            )
            key = (next_base, next_total, next_groups)
            if key in visited:
                continue
            visited.add(key)
            detector_states.add((next_base, next_groups))
            residual_states.add(next_total)
            if next_base == base_identity:
                base_kernel_detector_states.add((next_base, next_groups))
                base_kernel_residual_states.add(next_total)
            if len(visited) > state_limit:
                truncated = True
                return ExactImageAudit(
                    n=n,
                    visited_state_count=len(visited),
                    detector_state_count=len(detector_states),
                    residual_state_count=len(residual_states),
                    base_kernel_detector_state_count=len(base_kernel_detector_states),
                    base_kernel_residual_state_count=len(base_kernel_residual_states),
                    truncated=truncated,
                    kernel_failure=None,
                    collision_failure=None,
                )
            detector_key = (next_base, next_groups)
            if next_base == base_identity:
                previous = residual_by_detector.get(detector_key)
                if previous is not None and previous[0] != next_total:
                    return ExactImageAudit(
                        n=n,
                        visited_state_count=len(visited),
                        detector_state_count=len(detector_states),
                        residual_state_count=len(residual_states),
                        base_kernel_detector_state_count=len(base_kernel_detector_states),
                        base_kernel_residual_state_count=len(base_kernel_residual_states),
                        truncated=False,
                        kernel_failure=(
                            next_word
                            if detector_key == (base_identity, group_initial)
                            else None
                        ),
                        collision_failure=(previous[1], next_word),
                    )
                residual_by_detector[detector_key] = (next_total, next_word)
                if detector_key == (base_identity, group_initial) and next_total != total_identity:
                    return ExactImageAudit(
                        n=n,
                        visited_state_count=len(visited),
                        detector_state_count=len(detector_states),
                        residual_state_count=len(residual_states),
                        base_kernel_detector_state_count=len(base_kernel_detector_states),
                        base_kernel_residual_state_count=len(base_kernel_residual_states),
                        truncated=False,
                        kernel_failure=next_word,
                        collision_failure=(tuple(), next_word),
                    )
            queue.append((next_base, next_total, next_groups, next_word))

    return ExactImageAudit(
        n=n,
        visited_state_count=len(visited),
        detector_state_count=len(detector_states),
        residual_state_count=len(residual_states),
        base_kernel_detector_state_count=len(base_kernel_detector_states),
        base_kernel_residual_state_count=len(base_kernel_residual_states),
        truncated=False,
        kernel_failure=None,
        collision_failure=None,
    )


def _readout_rows(
    quotient_map: QuotientMap,
    n: int,
    residual_by_detector: Mapping[object, Tuple[Permutation, Tuple[int, ...]]]
) -> Tuple[DetectorReadoutRow, ...]:
    total_tuples = tuple(product(quotient_map.total.elements, repeat=n))
    base_by_index = tuple(quotient_map.base_tuple(tup) for tup in total_tuples)
    values = sorted(
        residual_by_detector.values(),
        key=lambda item: (len(item[1]), item[1], item[0]),
    )
    rows = []
    for residual, word in values:
        moved_base_tuples = {
            base_by_index[index]
            for index, image in enumerate(residual)
            if image != index
        }
        rows.append(
            DetectorReadoutRow(
                representative_braid_word=word,
                residual_permutation=residual,
                preserves_quotient_fibres=all(
                    base_by_index[index] == base_by_index[image]
                    for index, image in enumerate(residual)
                ),
                moved_base_tuple_count=len(moved_base_tuples),
                moved_total_tuple_count=sum(
                    1 for index, image in enumerate(residual) if image != index
                ),
            )
        )
    return tuple(rows)


def exact_detector_readout_audit(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    state_limit: int = 10000,
) -> ExactDetectorReadoutAudit:
    """Build the fixed-index detector-to-residual readout table.

    The table is indexed by reachable detector states for braids in the base
    kernel.  Each row stores a shortest representative braid word reaching
    that detector state and the corresponding residual permutation.  A
    nontruncated audit with no kernel or collision failure proves the same
    fixed-``n`` implication as ``exact_detector_image_audit``, but in readout
    form: residual motion is a function of the fixed detector state.
    """

    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    base_identity = tuple(range(len(base_detector.elements) ** n))
    total_identity = tuple(range(len(quotient_map.total.elements) ** n))
    group_initial = tuple(_group_detector_initial_int_state(group, n) for group in groups)
    group_tables = tuple(_group_int_tables(group) for group in groups)

    base_generators = {
        signed: _solution_generator_permutation(base_detector, n, signed)
        for signed in alphabet
    }
    total_generators = {
        signed: _solution_generator_permutation(quotient_map.total, n, signed)
        for signed in alphabet
    }

    initial = (base_identity, total_identity, group_initial, tuple())
    queue = deque([initial])
    visited = {(base_identity, total_identity, group_initial)}
    detector_states = {(base_identity, group_initial)}
    residual_states = {total_identity}
    base_kernel_detector_states = {(base_identity, group_initial)}
    base_kernel_residual_states = {total_identity}
    residual_by_detector = {(base_identity, group_initial): (total_identity, tuple())}

    while queue:
        base_state, total_state, group_state, word = queue.popleft()
        for signed in alphabet:
            next_word = word + (signed,)
            next_base = _compose_permutation(base_generators[signed], base_state)
            next_total = _compose_permutation(total_generators[signed], total_state)
            next_groups = tuple(
                _apply_group_detector_generator_int(group, state, signed, n, tables)
                for group, state, tables in zip(groups, group_state, group_tables)
            )
            key = (next_base, next_total, next_groups)
            if key in visited:
                continue
            visited.add(key)
            detector_states.add((next_base, next_groups))
            residual_states.add(next_total)
            if next_base == base_identity:
                base_kernel_detector_states.add((next_base, next_groups))
                base_kernel_residual_states.add(next_total)
            if len(visited) > state_limit:
                return ExactDetectorReadoutAudit(
                    n=n,
                    visited_state_count=len(visited),
                    detector_state_count=len(detector_states),
                    residual_state_count=len(residual_states),
                    base_kernel_detector_state_count=len(base_kernel_detector_states),
                    base_kernel_residual_state_count=len(base_kernel_residual_states),
                    truncated=True,
                    kernel_failure=None,
                    collision_failure=None,
                    readout_rows=_readout_rows(quotient_map, n, residual_by_detector),
                )
            detector_key = (next_base, next_groups)
            if next_base == base_identity:
                previous = residual_by_detector.get(detector_key)
                if previous is not None and previous[0] != next_total:
                    return ExactDetectorReadoutAudit(
                        n=n,
                        visited_state_count=len(visited),
                        detector_state_count=len(detector_states),
                        residual_state_count=len(residual_states),
                        base_kernel_detector_state_count=len(base_kernel_detector_states),
                        base_kernel_residual_state_count=len(base_kernel_residual_states),
                        truncated=False,
                        kernel_failure=(
                            next_word
                            if detector_key == (base_identity, group_initial)
                            else None
                        ),
                        collision_failure=(previous[1], next_word),
                        readout_rows=_readout_rows(quotient_map, n, residual_by_detector),
                    )
                residual_by_detector[detector_key] = (next_total, next_word)
                if detector_key == (base_identity, group_initial) and next_total != total_identity:
                    return ExactDetectorReadoutAudit(
                        n=n,
                        visited_state_count=len(visited),
                        detector_state_count=len(detector_states),
                        residual_state_count=len(residual_states),
                        base_kernel_detector_state_count=len(base_kernel_detector_states),
                        base_kernel_residual_state_count=len(base_kernel_residual_states),
                        truncated=False,
                        kernel_failure=next_word,
                        collision_failure=(tuple(), next_word),
                        readout_rows=_readout_rows(quotient_map, n, residual_by_detector),
                    )
            queue.append((next_base, next_total, next_groups, next_word))

    return ExactDetectorReadoutAudit(
        n=n,
        visited_state_count=len(visited),
        detector_state_count=len(detector_states),
        residual_state_count=len(residual_states),
        base_kernel_detector_state_count=len(base_kernel_detector_states),
        base_kernel_residual_state_count=len(base_kernel_residual_states),
        truncated=False,
        kernel_failure=None,
        collision_failure=None,
        readout_rows=_readout_rows(quotient_map, n, residual_by_detector),
    )


def _residual_readout_permutations(
    audit: ExactDetectorReadoutAudit,
) -> Tuple[Permutation, ...]:
    return tuple(sorted({row.residual_permutation for row in audit.readout_rows}))


def exact_detector_product_readout_audit(
    quotient_map: QuotientMap,
    base_detector: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    *,
    state_limit: int = 10000,
    max_product_order: int = 100_000,
) -> ExactDetectorProductReadoutAudit:
    """Compare listed detector factors with their single product detector.

    The sharp obstruction theorem uses one finite group.  This helper checks,
    in a fixed degree and when the product is small enough to enumerate, that
    the exact residual-fibre readout obtained from a list of factor detectors
    agrees with the readout obtained from the one direct-product group.
    """

    factors = tuple(groups)
    factor_orders = tuple(len(group.elements) for group in factors)
    product_order = math_prod(factor_orders, start=1)
    factor_audit = exact_detector_readout_audit(
        quotient_map,
        base_detector,
        factors,
        n,
        state_limit=state_limit,
    )
    factor_residuals = _residual_readout_permutations(factor_audit)
    if product_order > max_product_order:
        return ExactDetectorProductReadoutAudit(
            n=n,
            factor_orders=factor_orders,
            product_group_order=product_order,
            product_skipped=True,
            factor_audit=factor_audit,
            product_audit=None,
            factor_residual_readouts=factor_residuals,
            product_residual_readouts=None,
            readout_state_counts_match=None,
            proof_status_matches=None,
            residual_readouts_match=None,
        )
    product_group = direct_product_group(factors)
    product_audit = exact_detector_readout_audit(
        quotient_map,
        base_detector,
        (product_group,),
        n,
        state_limit=state_limit,
    )
    product_residuals = _residual_readout_permutations(product_audit)
    return ExactDetectorProductReadoutAudit(
        n=n,
        factor_orders=factor_orders,
        product_group_order=product_order,
        product_skipped=False,
        factor_audit=factor_audit,
        product_audit=product_audit,
        factor_residual_readouts=factor_residuals,
        product_residual_readouts=product_residuals,
        readout_state_counts_match=(
            factor_audit.readout_state_count == product_audit.readout_state_count
        ),
        proof_status_matches=(
            factor_audit.proves_fixed_n_readout
            == product_audit.proves_fixed_n_readout
        ),
        residual_readouts_match=factor_residuals == product_residuals,
    )


def symmetric_detector_readout_audit(
    solution: FiniteBraidedSet,
    n: int,
    *,
    state_limit: int = 10000,
) -> ExactDetectorReadoutAudit:
    """Audit the direct ``G_X = Sym(X)`` readout over the one-point quotient.

    This is a fixed-index diagnostic for the stronger direct route: if it is
    nontruncated and has no kernel/collision failure, then every braid whose
    ``Sym(X)`` Artin-longitude detector state is identity acts trivially on
    ``X^n``.  It does not by itself prove the all-``n`` theorem.
    """

    quotient = identity_solution(("*",))
    quotient_map = QuotientMap(
        solution,
        quotient,
        {element: "*" for element in solution.elements},
    )
    return exact_detector_readout_audit(
        quotient_map,
        quotient,
        (symmetric_group(len(solution.elements)),),
        n,
        state_limit=state_limit,
    )
