from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Dict, Iterable, List, Mapping, Sequence, Tuple

from .finite_braided_set import (
    FiniteBraidedSet,
    is_rack_solution,
    opposite_solution,
    product_solution,
    rack_solution,
)
from .finite_group import (
    FiniteGroup,
    FiniteGroupHomomorphism,
    GroupElement,
    commutator_subgroup_elements,
    direct_product_group,
    is_abelian_group,
    left_regular_representation,
    permutation_group_from_generators,
    subgroup_generated_elements,
    symmetric_group_inclusion,
    symmetric_group,
)

FreeLetter = Tuple[int, int]
FreeWord = Tuple[FreeLetter, ...]
BraidWord = Sequence[int]
LongitudeExpressionLetter = Tuple[int, int]
LongitudeExpression = Tuple[LongitudeExpressionLetter, ...]
LongitudeSubgroupWitnessLetter = Tuple[Tuple[GroupElement, ...], int, int]
LongitudeSubgroupWitness = Tuple[LongitudeSubgroupWitnessLetter, ...]
AbelianLongitudeMatrixWitnessLetter = Tuple[GroupElement, int, int, int]
AbelianLongitudeMatrixWitness = Tuple[AbelianLongitudeMatrixWitnessLetter, ...]
ArtinDetectorLiftLabel = Tuple[GroupElement, GroupElement]


def reduce_free_word(word: Iterable[FreeLetter]) -> FreeWord:
    out: List[FreeLetter] = []
    for generator, exponent in word:
        if exponent == 0:
            continue
        if exponent not in (-1, 1):
            raise ValueError("free words use unit exponents")
        if out and out[-1][0] == generator and out[-1][1] == -exponent:
            out.pop()
        else:
            out.append((generator, exponent))
    return tuple(out)


def invert_free_word(word: FreeWord) -> FreeWord:
    return tuple((generator, -exponent) for generator, exponent in reversed(word))


def substitute_free_word(word: FreeWord, images: Sequence[FreeWord]) -> FreeWord:
    expanded: List[FreeLetter] = []
    for generator, exponent in word:
        image = images[generator]
        if exponent < 0:
            image = invert_free_word(image)
        expanded.extend(image)
    return reduce_free_word(expanded)


def artin_generator_images(n: int, generator: int, inverse: bool = False) -> Tuple[FreeWord, ...]:
    """Return images for one Artin generator.

    The generator argument is zero-based.  Positive sigma_i uses

        x_i     -> x_i x_{i+1} x_i^{-1}
        x_{i+1} -> x_i

    and the negative generator uses the inverse automorphism.
    """

    if generator < 0 or generator + 1 >= n:
        raise IndexError(generator)
    images: List[FreeWord] = [((i, 1),) for i in range(n)]
    i = generator
    if inverse:
        images[i] = ((i + 1, 1),)
        images[i + 1] = ((i + 1, -1), (i, 1), (i + 1, 1))
    else:
        images[i] = ((i, 1), (i + 1, 1), (i, -1))
        images[i + 1] = ((i, 1),)
    return tuple(images)


def artin_images(n: int, braid_word: BraidWord) -> Tuple[FreeWord, ...]:
    """Return Artin images of free generators for a braid word.

    Braid generators are one-based: `i` means sigma_i, `-i` means
    sigma_i^{-1}.  Words are read left to right, matching the braid-action
    convention used by `FiniteBraidedSet.braid_action`.
    """

    images: Tuple[FreeWord, ...] = tuple(((i, 1),) for i in range(n))
    for signed_generator in braid_word:
        if signed_generator == 0:
            raise ValueError("braid generators are nonzero")
        generator = abs(signed_generator) - 1
        step = artin_generator_images(n, generator, inverse=signed_generator < 0)
        images = tuple(substitute_free_word(step_image, images) for step_image in step)
    return images


def _artin_images_and_longitudes(n: int, braid_word: BraidWord) -> Tuple[Tuple[FreeWord, ...], Tuple[FreeWord, ...]]:
    images: List[FreeWord] = [((i, 1),) for i in range(n)]
    longitudes: List[FreeWord] = [tuple() for _ in range(n)]
    for signed_generator in braid_word:
        if signed_generator == 0:
            raise ValueError("braid generators are nonzero")
        i = abs(signed_generator) - 1
        if i < 0 or i + 1 >= n:
            raise IndexError(i)
        image_i, image_j = images[i], images[i + 1]
        longitude_i, longitude_j = longitudes[i], longitudes[i + 1]
        if signed_generator > 0:
            images[i] = reduce_free_word(image_i + image_j + invert_free_word(image_i))
            images[i + 1] = image_i
            longitudes[i] = reduce_free_word(image_i + longitude_j)
            longitudes[i + 1] = longitude_i
        else:
            images[i] = image_j
            images[i + 1] = reduce_free_word(invert_free_word(image_j) + image_i + image_j)
            longitudes[i] = longitude_j
            longitudes[i + 1] = reduce_free_word(invert_free_word(image_j) + longitude_i)
    return tuple(images), tuple(longitudes)


def braid_permutation(n: int, braid_word: BraidWord) -> Tuple[int, ...]:
    perm = list(range(n))
    for signed_generator in braid_word:
        if signed_generator == 0:
            raise ValueError("braid generators are nonzero")
        i = abs(signed_generator) - 1
        if i < 0 or i + 1 >= n:
            raise IndexError(i)
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    return tuple(perm)


def conjugator_and_target(word: FreeWord) -> Tuple[FreeWord, int]:
    """Extract l and j from a reduced conjugate l x_j l^{-1}."""

    reduced = list(reduce_free_word(word))
    prefix: List[FreeLetter] = []
    while len(reduced) > 1 and reduced[0][0] == reduced[-1][0] and reduced[0][1] == -reduced[-1][1]:
        prefix.append(reduced.pop(0))
        reduced.pop()
    if len(reduced) != 1 or reduced[0][1] != 1:
        raise ValueError(f"word is not a positive conjugate of a generator: {word!r}")
    return tuple(prefix), reduced[0][0]


@dataclass(frozen=True)
class ArtinLongitudeData:
    permutation: Tuple[int, ...]
    longitudes: Tuple[FreeWord, ...]


@dataclass(frozen=True)
class ArtinPermutationDefectWitnessAudit:
    """Witness that one Artin permutation defect lies in ``V_beta(G)``."""

    n: int
    braid_word: Tuple[int, ...]
    word: FreeWord
    assignment: Tuple[GroupElement, ...]
    defect_word: FreeWord
    defect_value: GroupElement
    longitude_witness: LongitudeSubgroupWitness
    longitude_witness_value: GroupElement
    witness_matches_defect: bool


@dataclass(frozen=True)
class ArtinDefectAbelianizationBarrierAudit:
    """Necessary abelianization test for an Artin-defect-only display."""

    group_order: int
    commutator_subgroup: Tuple[GroupElement, ...]
    endpoints: Tuple[GroupElement, ...]
    endpoints_outside_commutator: Tuple[GroupElement, ...]

    @property
    def commutator_subgroup_size(self) -> int:
        return len(self.commutator_subgroup)

    @property
    def group_has_nontrivial_abelianization(self) -> bool:
        return self.commutator_subgroup_size < self.group_order

    @property
    def all_endpoints_have_trivial_abelianization(self) -> bool:
        return not self.endpoints_outside_commutator

    @property
    def artin_defect_only_display_not_obstructed(self) -> bool:
        return self.all_endpoints_have_trivial_abelianization


@dataclass(frozen=True)
class ArtinDetectorLiftTransitionAudit:
    """One local row check for the active ``G x G`` Artin detector update."""

    signed_generator: int
    input_left: ArtinDetectorLiftLabel
    input_right: ArtinDetectorLiftLabel
    supplied_left: ArtinDetectorLiftLabel
    supplied_right: ArtinDetectorLiftLabel
    expected_left: ArtinDetectorLiftLabel
    expected_right: ArtinDetectorLiftLabel
    row_matches_artin_detector: bool


@dataclass(frozen=True)
class ArtinDetectorLiftBraidAudit:
    """Global induction check for a supplied detector-lift endpoint expression."""

    n: int
    braid_word: Tuple[int, ...]
    group_order: int
    initial_meridians: Tuple[GroupElement, ...]
    terminal_meridians: Tuple[GroupElement, ...]
    terminal_longitude_labels: Tuple[GroupElement, ...]
    expected_meridians: Tuple[GroupElement, ...]
    expected_longitudes: Tuple[GroupElement, ...]
    meridians_match_artin_images: bool
    longitudes_match_artin_longitudes: bool
    endpoint_expression: LongitudeExpression
    endpoint_value: GroupElement
    expected_endpoint_value: GroupElement
    endpoint_matches_longitude_expression: bool

    @property
    def proves_detector_lift_recursion(self) -> bool:
        return (
            self.meridians_match_artin_images
            and self.longitudes_match_artin_longitudes
            and self.endpoint_matches_longitude_expression
        )


@dataclass(frozen=True)
class ArtinDetectorLiftInverseRowAudit:
    """Check that the negative detector row is the inverse positive row."""

    input_left: ArtinDetectorLiftLabel
    input_right: ArtinDetectorLiftLabel
    positive_left: ArtinDetectorLiftLabel
    positive_right: ArtinDetectorLiftLabel
    positive_then_negative_left: ArtinDetectorLiftLabel
    positive_then_negative_right: ArtinDetectorLiftLabel
    negative_left: ArtinDetectorLiftLabel
    negative_right: ArtinDetectorLiftLabel
    negative_then_positive_left: ArtinDetectorLiftLabel
    negative_then_positive_right: ArtinDetectorLiftLabel

    @property
    def positive_then_negative_recovers_input(self) -> bool:
        return (
            self.positive_then_negative_left == self.input_left
            and self.positive_then_negative_right == self.input_right
        )

    @property
    def negative_then_positive_recovers_input(self) -> bool:
        return (
            self.negative_then_positive_left == self.input_left
            and self.negative_then_positive_right == self.input_right
        )

    @property
    def negative_row_is_positive_inverse(self) -> bool:
        return (
            self.positive_then_negative_recovers_input
            and self.negative_then_positive_recovers_input
        )


@dataclass(frozen=True)
class RackInnerDetectorLiftRowAudit:
    """One rack-inner positive row checked against the Artin detector lift."""

    input_left_atom: object
    input_right_atom: object
    output_left_atom: object
    output_right_atom: object
    endpoint_left: GroupElement
    endpoint_right: GroupElement
    input_left: ArtinDetectorLiftLabel
    input_right: ArtinDetectorLiftLabel
    supplied_left: ArtinDetectorLiftLabel
    supplied_right: ArtinDetectorLiftLabel
    transition_audit: ArtinDetectorLiftTransitionAudit
    left_translation_conjugacy_matches: bool
    right_output_translation_matches: bool
    left_base_atom: object
    right_base_atom: object
    left_endpoint_image: object
    right_endpoint_image: object
    endpoint_transport_matches_crossing: bool
    negative_row_is_positive_inverse: bool

    @property
    def positive_row_matches_artin_detector(self) -> bool:
        return self.transition_audit.row_matches_artin_detector

    @property
    def proves_rack_inner_detector_lift_row(self) -> bool:
        return (
            self.positive_row_matches_artin_detector
            and self.left_translation_conjugacy_matches
            and self.right_output_translation_matches
            and self.endpoint_transport_matches_crossing
            and self.negative_row_is_positive_inverse
        )


@dataclass(frozen=True)
class RackInnerDetectorLiftAudit:
    """Finite row audit for a rack inner-group detector factor."""

    rack_size: int
    inner_group_order: int
    endpoint_label_count: int
    row_audits: Tuple[RackInnerDetectorLiftRowAudit, ...]

    @property
    def row_count(self) -> int:
        return len(self.row_audits)

    @property
    def all_positive_rows_match_artin_detector(self) -> bool:
        return all(
            row.positive_row_matches_artin_detector
            for row in self.row_audits
        )

    @property
    def all_translation_conjugacies_match(self) -> bool:
        return all(
            row.left_translation_conjugacy_matches
            and row.right_output_translation_matches
            for row in self.row_audits
        )

    @property
    def all_endpoint_transports_match_crossing(self) -> bool:
        return all(
            row.endpoint_transport_matches_crossing
            for row in self.row_audits
        )

    @property
    def all_negative_rows_follow_by_inverse(self) -> bool:
        return all(
            row.negative_row_is_positive_inverse
            for row in self.row_audits
        )

    @property
    def proves_rack_inner_detector_lift_rows(self) -> bool:
        return (
            self.all_positive_rows_match_artin_detector
            and self.all_translation_conjugacies_match
            and self.all_endpoint_transports_match_crossing
            and self.all_negative_rows_follow_by_inverse
        )


@dataclass(frozen=True)
class PrincipalGaugeCocycleFailure:
    """One failed nonabelian rack-cocycle identity."""

    left_atom: object
    middle_atom: object
    right_atom: object
    left_value: GroupElement
    right_value: GroupElement


@dataclass(frozen=True)
class PrincipalGaugeExtensionDetectorAudit:
    """Audit a principal finite rack-extension detector for unit holonomy."""

    base_rack_size: int
    unit_group_order: int
    extension_size: int
    cocycle_failures: Tuple[PrincipalGaugeCocycleFailure, ...]
    extension_is_rack_form: bool
    extension_is_ybe: bool
    inner_group_order: int | None
    detector_lift_audit: RackInnerDetectorLiftAudit | None

    @property
    def cocycle_identity_holds(self) -> bool:
        return not self.cocycle_failures

    @property
    def principal_extension_is_finite_rack(self) -> bool:
        return (
            self.cocycle_identity_holds
            and self.extension_is_rack_form
            and self.extension_is_ybe
        )

    @property
    def proves_principal_gauge_detector(self) -> bool:
        return (
            self.principal_extension_is_finite_rack
            and self.detector_lift_audit is not None
            and self.detector_lift_audit.proves_rack_inner_detector_lift_rows
        )


@dataclass(frozen=True)
class RackExtensionProjectionFailure:
    """One failed projection-homomorphism identity for a rack extension."""

    left_extension_element: object
    right_extension_element: object
    projected_output: object
    expected_base_output: object


@dataclass(frozen=True)
class RackExtensionDetectorAudit:
    """Audit that a finite rack extension is closed by its inner group."""

    base_rack_size: int
    extension_size: int
    projection_image_size: int
    projection_surjective: bool
    extension_is_rack_form: bool
    extension_is_ybe: bool
    projection_failures: Tuple[RackExtensionProjectionFailure, ...]
    inner_group_order: int | None
    detector_lift_audit: RackInnerDetectorLiftAudit | None

    @property
    def projection_is_rack_homomorphism(self) -> bool:
        return self.projection_surjective and not self.projection_failures

    @property
    def extension_is_finite_rack_over_base(self) -> bool:
        return (
            self.extension_is_rack_form
            and self.extension_is_ybe
            and self.projection_is_rack_homomorphism
        )

    @property
    def proves_rack_extension_detector(self) -> bool:
        return (
            self.extension_is_finite_rack_over_base
            and self.detector_lift_audit is not None
            and self.detector_lift_audit.proves_rack_inner_detector_lift_rows
        )


@dataclass(frozen=True)
class TransportStateLeftTranslationFailure:
    """One non-bijective left translation in a transport-state row."""

    left_atom: object
    left_state: object
    image_size: int
    expected_size: int


@dataclass(frozen=True)
class TransportStateRackificationAudit:
    """Audit rackification of a strand-continuing finite gauge row."""

    atom_rack_size: int
    state_count: int
    transport_size: int
    left_translation_failures: Tuple[TransportStateLeftTranslationFailure, ...]
    transport_rack_built: bool
    extension_detector_audit: RackExtensionDetectorAudit | None

    @property
    def all_left_translations_bijective(self) -> bool:
        return not self.left_translation_failures

    @property
    def transport_state_is_finite_rack_extension(self) -> bool:
        return (
            self.transport_rack_built
            and self.extension_detector_audit is not None
            and self.extension_detector_audit.extension_is_finite_rack_over_base
        )

    @property
    def proves_transport_state_detector(self) -> bool:
        return (
            self.transport_state_is_finite_rack_extension
            and self.extension_detector_audit is not None
            and self.extension_detector_audit.proves_rack_extension_detector
        )


@dataclass(frozen=True)
class RackLongitudeFactorization:
    """Input-dependent finite-group longitude factorization for a rack action."""

    assignment: Tuple[GroupElement, ...]
    permutation: Tuple[int, ...]
    longitude_values: Tuple[GroupElement, ...]
    output: Tuple[GroupElement, ...]


@dataclass(frozen=True)
class LongitudeSubgroupProfileRow:
    """Compact finite-group visibility row for one braid word."""

    name: str
    group_order: int
    permutation: Tuple[int, ...]
    generator_count: int
    subgroup_size: int

    @property
    def identity_longitude_signature(self) -> bool:
        return self.permutation == tuple(range(len(self.permutation))) and self.subgroup_size == 1


@dataclass(frozen=True)
class HomomorphicLongitudeSubgroupAudit:
    """Functoriality check for longitude-value subgroups under a homomorphism."""

    source_subgroup_size: int
    image_subgroup_size: int
    target_subgroup_size: int
    homomorphism_surjective: bool
    image_contained_in_target_subgroup: bool
    target_subgroup_equals_image: bool


@dataclass(frozen=True)
class AbelianLongitudeImageAudit:
    """Exact matrix computation of ``V_beta(A)`` for a finite abelian group."""

    n: int
    braid_word: Tuple[int, ...]
    group_order: int
    permutation: Tuple[int, ...]
    exponent_matrix: Tuple[Tuple[int, ...], ...]
    coefficient_entries: Tuple[int, ...]
    matrix_generators: Tuple[GroupElement, ...]
    matrix_subgroup: Tuple[GroupElement, ...]
    enumerated_subgroup: Tuple[GroupElement, ...] | None

    @property
    def matrix_generator_count(self) -> int:
        return len(self.matrix_generators)

    @property
    def matrix_subgroup_size(self) -> int:
        return len(self.matrix_subgroup)

    @property
    def enumerated_subgroup_size(self) -> int | None:
        if self.enumerated_subgroup is None:
            return None
        return len(self.enumerated_subgroup)

    @property
    def enumeration_matches_matrix_formula(self) -> bool:
        return (
            self.enumerated_subgroup is None
            or set(self.enumerated_subgroup) == set(self.matrix_subgroup)
        )

    @property
    def identity_signature_by_matrix(self) -> bool:
        return (
            self.permutation == tuple(range(self.n))
            and len(self.matrix_subgroup) == 1
        )


@dataclass(frozen=True)
class AbelianLongitudeMatrixWitnessAudit:
    """Certificate that an abelian endpoint lies in the matrix form of ``V_beta``."""

    n: int
    braid_word: Tuple[int, ...]
    endpoint: GroupElement
    matrix_witness: AbelianLongitudeMatrixWitness
    matrix_witness_value: GroupElement
    longitude_subgroup_witness: LongitudeSubgroupWitness
    longitude_subgroup_witness_value: GroupElement
    endpoint_matches_matrix_witness: bool
    matrix_witness_matches_longitude_witness: bool

    @property
    def proves_endpoint_in_abelian_longitude_subgroup(self) -> bool:
        return (
            self.endpoint_matches_matrix_witness
            and self.matrix_witness_matches_longitude_witness
        )


@dataclass(frozen=True)
class PushforwardLongitudeSubgroupWitnessAudit:
    """Certificate-level functoriality for one longitude subgroup witness."""

    source_value: GroupElement
    target_image_value: GroupElement
    pushed_witness: LongitudeSubgroupWitness
    pushed_witness_value: GroupElement
    pushforward_matches_image: bool


@dataclass(frozen=True)
class NormalQuotientLongitudeLiftAudit:
    """Lift a quotient longitude witness plus kernel correction to ``G``."""

    n: int
    braid_word: Tuple[int, ...]
    endpoint: GroupElement
    quotient_endpoint: GroupElement
    quotient_witness: LongitudeSubgroupWitness
    quotient_witness_value: GroupElement
    lifted_witness: LongitudeSubgroupWitness
    lifted_witness_value: GroupElement
    lifted_witness_projection_value: GroupElement
    kernel_size: int
    kernel_correction: GroupElement
    kernel_correction_in_kernel: bool
    kernel_witness: LongitudeSubgroupWitness
    kernel_witness_assignments_in_kernel: bool
    kernel_witness_value: GroupElement
    combined_witness: LongitudeSubgroupWitness
    combined_witness_value: GroupElement

    @property
    def quotient_witness_matches_endpoint(self) -> bool:
        return self.quotient_witness_value == self.quotient_endpoint

    @property
    def lifted_witness_projects_to_quotient_witness(self) -> bool:
        return self.lifted_witness_projection_value == self.quotient_witness_value

    @property
    def kernel_witness_matches_correction(self) -> bool:
        return self.kernel_witness_value == self.kernel_correction

    @property
    def combined_witness_matches_endpoint(self) -> bool:
        return self.combined_witness_value == self.endpoint

    @property
    def proves_endpoint_in_longitude_subgroup_by_normal_lift(self) -> bool:
        return (
            self.quotient_witness_matches_endpoint
            and self.lifted_witness_projects_to_quotient_witness
            and self.kernel_correction_in_kernel
            and self.kernel_witness_assignments_in_kernel
            and self.kernel_witness_matches_correction
            and self.combined_witness_matches_endpoint
        )


@dataclass(frozen=True)
class ConjugateLongitudeSubgroupWitnessAudit:
    """Certificate-level normality for one longitude subgroup witness."""

    original_value: GroupElement
    conjugator: GroupElement
    conjugated_witness: LongitudeSubgroupWitness
    conjugated_witness_value: GroupElement
    expected_conjugate_value: GroupElement
    conjugated_witness_matches: bool


@dataclass(frozen=True)
class DirectProductLongitudeSubgroupAudit:
    """Compare ``V_beta(product_i G_i)`` with ``product_i V_beta(G_i)``."""

    factor_orders: Tuple[int, ...]
    factor_subgroup_sizes: Tuple[int, ...]
    product_group_order: int
    product_subgroup_size: int
    expected_product_subgroup_size: int
    product_subgroup_equals_factor_product: bool


@dataclass(frozen=True)
class DirectProductLongitudeSubgroupWitnessAudit:
    """Certificate-level assembly of factor witnesses in a product group."""

    factor_values: Tuple[GroupElement, ...]
    product_witness: LongitudeSubgroupWitness
    product_witness_value: GroupElement
    expected_product_value: GroupElement
    product_witness_matches_factors: bool


@dataclass(frozen=True)
class DirectProductDetectorActionAudit:
    """Projection check for the active coordinates of product detector racks."""

    factor_orders: Tuple[int, ...]
    product_image_values: Tuple[GroupElement, ...]
    product_longitude_values: Tuple[GroupElement, ...]
    factor_image_values: Tuple[Tuple[GroupElement, ...], ...]
    factor_longitude_values: Tuple[Tuple[GroupElement, ...], ...]
    projected_image_values: Tuple[Tuple[GroupElement, ...], ...]
    projected_longitude_values: Tuple[Tuple[GroupElement, ...], ...]
    image_projections_match: bool
    longitude_projections_match: bool

    @property
    def detector_projections_match(self) -> bool:
        return self.image_projections_match and self.longitude_projections_match


@dataclass(frozen=True)
class DiagonalProductInvisibilityAudit:
    """Audit product-group invisibility used in diagonal B constructions."""

    group_orders: Tuple[int, ...]
    product_group_order: int
    factor_identity_signatures: Tuple[bool, ...]
    product_identity_signature: bool

    @property
    def product_identity_implies_factor_identities(self) -> bool:
        return not self.product_identity_signature or all(self.factor_identity_signatures)

    @property
    def factor_identities_imply_product_identity(self) -> bool:
        return not all(self.factor_identity_signatures) or self.product_identity_signature

    @property
    def product_signature_equivalent_to_factors(self) -> bool:
        return (
            self.product_identity_implies_factor_identities
            and self.factor_identities_imply_product_identity
        )


@dataclass(frozen=True)
class RightStabilizationLongitudeAudit:
    """Audit Artin-longitude stability after adding unused right strands."""

    old_n: int
    new_n: int
    braid_word: Tuple[int, ...]
    old_permutation: Tuple[int, ...]
    new_permutation: Tuple[int, ...]
    old_longitudes: Tuple[FreeWord, ...]
    new_restricted_longitudes: Tuple[FreeWord, ...]
    added_longitudes: Tuple[FreeWord, ...]

    @property
    def old_data_preserved(self) -> bool:
        return (
            self.new_permutation[: self.old_n] == self.old_permutation
            and self.old_longitudes == self.new_restricted_longitudes
        )

    @property
    def added_strands_trivial(self) -> bool:
        return (
            self.new_permutation[self.old_n :] == tuple(range(self.old_n, self.new_n))
            and all(longitude == tuple() for longitude in self.added_longitudes)
        )

    @property
    def stabilization_valid(self) -> bool:
        return self.old_data_preserved and self.added_strands_trivial


@dataclass(frozen=True)
class NormalizedLawPrefixWitnessAudit:
    """Finite-prefix check for a constructive normalized-law obstruction.

    Passing one record verifies one explicit diagonal witness against one
    finite product group.  A B proof still needs an all-`j` construction of
    such records for the product of the first `j` finite groups.
    """

    source_n: int
    target_n: int
    braid_word: Tuple[int, ...]
    group_orders: Tuple[int, ...]
    product_group_order: int
    source_product_identity_signature: bool
    target_product_identity_signature: bool
    source_factor_identity_signatures: Tuple[bool, ...]
    target_factor_identity_signatures: Tuple[bool, ...]
    right_stabilization: RightStabilizationLongitudeAudit
    moved_tuple: Tuple[object, ...]
    source_image: Tuple[object, ...] | None
    source_tuple_moved: bool
    stabilized_tuple: Tuple[object, ...]
    stabilized_image: Tuple[object, ...] | None
    stabilized_tuple_moved: bool

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
    def movement_survives_stabilization(self) -> bool:
        return self.source_tuple_moved and self.stabilized_tuple_moved

    @property
    def proves_one_prefix_normalized_law_witness(self) -> bool:
        return (
            self.product_invisibility_survives_stabilization
            and self.movement_survives_stabilization
        )


@dataclass(frozen=True)
class SymmetricDetectorReductionAudit:
    """Check the Cayley-embedding reduction to symmetric detector groups."""

    group_order: int
    symmetric_degree: int
    symmetric_group_order: int
    embedding_injective: bool
    source_identity_signature: bool
    symmetric_identity_signature: bool

    @property
    def symmetric_identity_implies_source_identity(self) -> bool:
        return not self.symmetric_identity_signature or self.source_identity_signature

    @property
    def proves_symmetric_detector_reduction(self) -> bool:
        return self.embedding_injective and self.symmetric_identity_implies_source_identity


@dataclass(frozen=True)
class SymmetricTowerMonotonicityAudit:
    """Check the kernel containment ``K_{S_M} <= K_{S_m}`` for ``M>=m``."""

    source_degree: int
    target_degree: int
    inclusion_injective: bool
    smaller_identity_signature: bool
    larger_identity_signature: bool

    @property
    def larger_identity_implies_smaller_identity(self) -> bool:
        return not self.larger_identity_signature or self.smaller_identity_signature

    @property
    def proves_symmetric_tower_monotonicity(self) -> bool:
        return self.inclusion_injective and self.larger_identity_implies_smaller_identity


def artin_longitudes(n: int, braid_word: BraidWord) -> ArtinLongitudeData:
    images, longitudes = _artin_images_and_longitudes(n, braid_word)
    targets: List[int] = []
    for image in images:
        _canonical_longitude, target = conjugator_and_target(image)
        targets.append(target)
    return ArtinLongitudeData(tuple(targets), longitudes)


def evaluate_free_word(group: FiniteGroup, assignment: Sequence[GroupElement], word: FreeWord) -> GroupElement:
    out = group.identity
    for generator, exponent in word:
        value = assignment[generator]
        if exponent < 0:
            value = group.inv(value)
        out = group.mul(out, value)
    return out


def _check_group_assignment(
    group: FiniteGroup,
    assignment: Sequence[GroupElement],
) -> Tuple[GroupElement, ...]:
    assignment_tuple = tuple(assignment)
    elements = set(group.elements)
    if any(value not in elements for value in assignment_tuple):
        raise ValueError("assignment contains a value outside the group")
    return assignment_tuple


def _check_detector_lift_label(
    group: FiniteGroup,
    label: ArtinDetectorLiftLabel,
) -> ArtinDetectorLiftLabel:
    pair = tuple(label)
    if len(pair) != 2:
        raise ValueError("detector-lift labels are pairs (meridian, endpoint)")
    elements = set(group.elements)
    if pair[0] not in elements or pair[1] not in elements:
        raise ValueError("detector-lift label contains a value outside the group")
    return pair  # type: ignore[return-value]


def artin_detector_lift_positive_update(
    group: FiniteGroup,
    left: ArtinDetectorLiftLabel,
    right: ArtinDetectorLiftLabel,
) -> Tuple[ArtinDetectorLiftLabel, ArtinDetectorLiftLabel]:
    """Return the active ``G x G`` detector update for ``sigma_i``."""

    m_left, u_left = _check_detector_lift_label(group, left)
    m_right, u_right = _check_detector_lift_label(group, right)
    return (
        (
            group.mul(group.mul(m_left, m_right), group.inv(m_left)),
            group.mul(m_left, u_right),
        ),
        (m_left, u_left),
    )


def artin_detector_lift_negative_update(
    group: FiniteGroup,
    left: ArtinDetectorLiftLabel,
    right: ArtinDetectorLiftLabel,
) -> Tuple[ArtinDetectorLiftLabel, ArtinDetectorLiftLabel]:
    """Return the active ``G x G`` detector update for ``sigma_i^-1``."""

    m_left, u_left = _check_detector_lift_label(group, left)
    m_right, u_right = _check_detector_lift_label(group, right)
    return (
        (m_right, u_right),
        (
            group.mul(group.mul(group.inv(m_right), m_left), m_right),
            group.mul(group.inv(m_right), u_left),
        ),
    )


def artin_detector_lift_inverse_row_audit(
    group: FiniteGroup,
    left: ArtinDetectorLiftLabel,
    right: ArtinDetectorLiftLabel,
) -> ArtinDetectorLiftInverseRowAudit:
    """Audit the formal identity ``P^{-1}`` = negative Artin detector row."""

    input_left = _check_detector_lift_label(group, left)
    input_right = _check_detector_lift_label(group, right)
    positive_left, positive_right = artin_detector_lift_positive_update(
        group,
        input_left,
        input_right,
    )
    positive_then_negative_left, positive_then_negative_right = (
        artin_detector_lift_negative_update(
            group,
            positive_left,
            positive_right,
        )
    )
    negative_left, negative_right = artin_detector_lift_negative_update(
        group,
        input_left,
        input_right,
    )
    negative_then_positive_left, negative_then_positive_right = (
        artin_detector_lift_positive_update(
            group,
            negative_left,
            negative_right,
        )
    )
    return ArtinDetectorLiftInverseRowAudit(
        input_left=input_left,
        input_right=input_right,
        positive_left=positive_left,
        positive_right=positive_right,
        positive_then_negative_left=positive_then_negative_left,
        positive_then_negative_right=positive_then_negative_right,
        negative_left=negative_left,
        negative_right=negative_right,
        negative_then_positive_left=negative_then_positive_left,
        negative_then_positive_right=negative_then_positive_right,
    )


def artin_detector_lift_transition_audit(
    group: FiniteGroup,
    signed_generator: int,
    input_left: ArtinDetectorLiftLabel,
    input_right: ArtinDetectorLiftLabel,
    supplied_left: ArtinDetectorLiftLabel,
    supplied_right: ArtinDetectorLiftLabel,
) -> ArtinDetectorLiftTransitionAudit:
    """Audit one supplied finite row against the Artin detector-lift rules."""

    if signed_generator == 0:
        raise ValueError("signed generator must be nonzero")
    if signed_generator > 0:
        expected_left, expected_right = artin_detector_lift_positive_update(
            group,
            input_left,
            input_right,
        )
    else:
        expected_left, expected_right = artin_detector_lift_negative_update(
            group,
            input_left,
            input_right,
        )
    supplied_left = _check_detector_lift_label(group, supplied_left)
    supplied_right = _check_detector_lift_label(group, supplied_right)
    return ArtinDetectorLiftTransitionAudit(
        signed_generator=1 if signed_generator > 0 else -1,
        input_left=_check_detector_lift_label(group, input_left),
        input_right=_check_detector_lift_label(group, input_right),
        supplied_left=supplied_left,
        supplied_right=supplied_right,
        expected_left=expected_left,
        expected_right=expected_right,
        row_matches_artin_detector=(
            supplied_left == expected_left and supplied_right == expected_right
        ),
    )


def artin_detector_lift_state(
    group: FiniteGroup,
    initial_meridians: Sequence[GroupElement],
    braid_word: BraidWord,
) -> Tuple[ArtinDetectorLiftLabel, ...]:
    """Sweep a braid with active ``G x G`` Artin detector labels."""

    meridians = _check_group_assignment(group, initial_meridians)
    initial_state: list[ArtinDetectorLiftLabel] = [
        (meridian, group.identity) for meridian in meridians
    ]
    return artin_detector_lift_general_state(group, initial_state, braid_word)


def artin_detector_lift_general_state(
    group: FiniteGroup,
    initial_state: Sequence[ArtinDetectorLiftLabel],
    braid_word: BraidWord,
) -> Tuple[ArtinDetectorLiftLabel, ...]:
    """Sweep a braid from arbitrary active ``G x G`` detector labels."""

    state: list[ArtinDetectorLiftLabel] = [
        _check_detector_lift_label(group, label) for label in initial_state
    ]
    n = len(state)
    for signed_generator in braid_word:
        if signed_generator == 0:
            raise ValueError("braid generators are nonzero")
        index = abs(signed_generator) - 1
        if index < 0 or index + 1 >= n:
            raise IndexError(index)
        if signed_generator > 0:
            left, right = artin_detector_lift_positive_update(
                group,
                state[index],
                state[index + 1],
            )
        else:
            left, right = artin_detector_lift_negative_update(
                group,
                state[index],
                state[index + 1],
            )
        state[index], state[index + 1] = left, right
    return tuple(state)


def evaluate_terminal_label_expression(
    group: FiniteGroup,
    labels: Sequence[GroupElement],
    expression: LongitudeExpression,
) -> GroupElement:
    """Evaluate a signed word in terminal detector-lift endpoint labels."""

    label_tuple = _check_group_assignment(group, labels)
    out = group.identity
    for index, exponent in tuple(expression):
        if index < 0 or index >= len(label_tuple):
            raise IndexError(index)
        if exponent not in (-1, 1):
            raise ValueError("terminal label expression exponents must be +/-1")
        value = label_tuple[index]
        if exponent < 0:
            value = group.inv(value)
        out = group.mul(out, value)
    return out


def artin_detector_lift_braid_audit(
    group: FiniteGroup,
    initial_meridians: Sequence[GroupElement],
    braid_word: BraidWord,
    endpoint_expression: Sequence[LongitudeExpressionLetter] = (),
) -> ArtinDetectorLiftBraidAudit:
    """Audit the detector-lift induction for a full braid word.

    Passing this audit says that the terminal endpoint labels produced by the
    finite local ``G x G`` update rules are exactly the recursive Artin
    longitude values under the initial meridian assignment.
    """

    meridians = _check_group_assignment(group, initial_meridians)
    n = len(meridians)
    state = artin_detector_lift_state(group, meridians, braid_word)
    terminal_meridians = tuple(label[0] for label in state)
    terminal_longitudes = tuple(label[1] for label in state)
    expected_meridians = evaluate_artin_images(group, meridians, braid_word)
    expected_longitudes = evaluate_artin_longitudes(group, meridians, braid_word)
    expression = tuple(endpoint_expression)
    endpoint_value = evaluate_terminal_label_expression(
        group,
        terminal_longitudes,
        expression,
    )
    expected_endpoint_value = evaluate_longitude_expression(
        group,
        meridians,
        braid_word,
        expression,
    )
    return ArtinDetectorLiftBraidAudit(
        n=n,
        braid_word=tuple(braid_word),
        group_order=len(group.elements),
        initial_meridians=meridians,
        terminal_meridians=terminal_meridians,
        terminal_longitude_labels=terminal_longitudes,
        expected_meridians=expected_meridians,
        expected_longitudes=expected_longitudes,
        meridians_match_artin_images=terminal_meridians == expected_meridians,
        longitudes_match_artin_longitudes=terminal_longitudes == expected_longitudes,
        endpoint_expression=expression,
        endpoint_value=endpoint_value,
        expected_endpoint_value=expected_endpoint_value,
        endpoint_matches_longitude_expression=(
            endpoint_value == expected_endpoint_value
        ),
    )


def _check_free_word_indices(n: int, word: FreeWord) -> None:
    for generator, exponent in word:
        if generator < 0 or generator >= n:
            raise IndexError(generator)
        if exponent not in (-1, 1):
            raise ValueError("free words use unit exponents")


def apply_permutation_to_free_word(
    permutation: Sequence[int],
    word: FreeWord,
) -> FreeWord:
    """Apply a generator permutation to a free word."""

    perm = tuple(permutation)
    if sorted(perm) != list(range(len(perm))):
        raise ValueError("permutation must contain each generator index once")
    _check_free_word_indices(len(perm), tuple(word))
    return reduce_free_word((perm[generator], exponent) for generator, exponent in word)


def artin_permutation_defect_word(
    n: int,
    braid_word: BraidWord,
    word: FreeWord,
) -> FreeWord:
    """Return ``beta(word) * p_beta(word)^-1`` as a free word.

    Here ``p_beta`` is the Artin strand permutation acting on free generators.
    The word is reduced before evaluation, but no finite-group assignments are
    enumerated.
    """

    word_tuple = reduce_free_word(word)
    _check_free_word_indices(n, word_tuple)
    beta_word = substitute_free_word(word_tuple, artin_images(n, braid_word))
    permuted_word = apply_permutation_to_free_word(
        braid_permutation(n, braid_word),
        word_tuple,
    )
    return reduce_free_word(beta_word + invert_free_word(permuted_word))


def conjugated_assignment(
    group: FiniteGroup,
    assignment: Sequence[GroupElement],
    conjugator: FreeWord,
) -> Tuple[GroupElement, ...]:
    """Return the assignment ``x_j |-> phi(u x_j u^-1)``."""

    assignment_tuple = tuple(assignment)
    elements = set(group.elements)
    if any(value not in elements for value in assignment_tuple):
        raise ValueError("assignment contains a value outside the group")
    _check_free_word_indices(len(assignment_tuple), tuple(conjugator))
    conjugator_value = evaluate_free_word(group, assignment_tuple, tuple(conjugator))
    inverse = group.inv(conjugator_value)
    return tuple(
        group.mul(group.mul(conjugator_value, value), inverse)
        for value in assignment_tuple
    )


def invert_longitude_subgroup_witness(
    witness: Sequence[LongitudeSubgroupWitnessLetter],
) -> LongitudeSubgroupWitness:
    """Return a witness for the inverse subgroup element."""

    return tuple(
        (tuple(assignment), longitude_index, -exponent)
        for assignment, longitude_index, exponent in reversed(tuple(witness))
    )


def artin_permutation_defect_longitude_witness(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    assignment: Sequence[GroupElement],
    word: FreeWord,
) -> LongitudeSubgroupWitness:
    """Convert an Artin permutation defect value into a ``V_beta(G)`` witness.

    For a generator, the identity

    ``beta(x_i) x_{p(i)}^-1 = L_i (x_{p(i)} L_i^-1 x_{p(i)}^-1)``

    writes the defect as two normal conjugates of the longitude ``L_i``.  For a
    word, defects multiply with the usual prefix conjugation
    ``d(uv)=d(u) p(u) d(v) p(u)^-1``.  The returned witness records these
    conjugations by changing the finite-group assignment, not by enumerating
    any subgroup.
    """

    assignment_tuple = tuple(assignment)
    if len(assignment_tuple) != n:
        raise ValueError("assignment must have length n")
    elements = set(group.elements)
    if any(value not in elements for value in assignment_tuple):
        raise ValueError("assignment contains a value outside the group")
    word_tuple = reduce_free_word(word)
    _check_free_word_indices(n, word_tuple)
    data = artin_longitudes(n, braid_word)
    p_prefix: FreeWord = tuple()
    rows: List[LongitudeSubgroupWitnessLetter] = []
    for generator, exponent in word_tuple:
        target = data.permutation[generator]
        prefix_assignment = conjugated_assignment(group, assignment_tuple, p_prefix)
        rows.append((prefix_assignment, generator, 1))
        target_conjugator = ((target, exponent),)
        rows.append(
            (
                conjugated_assignment(group, prefix_assignment, target_conjugator),
                generator,
                -1,
            )
        )
        p_prefix = reduce_free_word(p_prefix + ((target, exponent),))
    return tuple(rows)


def evaluate_artin_permutation_defect(
    group: FiniteGroup,
    assignment: Sequence[GroupElement],
    n: int,
    braid_word: BraidWord,
    word: FreeWord,
) -> GroupElement:
    """Evaluate ``beta(word) * p_beta(word)^-1`` under one assignment."""

    assignment_tuple = tuple(assignment)
    if len(assignment_tuple) != n:
        raise ValueError("assignment must have length n")
    return evaluate_free_word(
        group,
        assignment_tuple,
        artin_permutation_defect_word(n, braid_word, word),
    )


def artin_permutation_defect_witness_audit(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    assignment: Sequence[GroupElement],
    word: FreeWord,
) -> ArtinPermutationDefectWitnessAudit:
    """Audit the Artin-defect normal-closure witness for one word."""

    assignment_tuple = tuple(assignment)
    word_tuple = reduce_free_word(word)
    defect_word = artin_permutation_defect_word(n, braid_word, word_tuple)
    defect_value = evaluate_free_word(group, assignment_tuple, defect_word)
    longitude_witness = artin_permutation_defect_longitude_witness(
        group,
        n,
        braid_word,
        assignment_tuple,
        word_tuple,
    )
    longitude_witness_value = evaluate_longitude_subgroup_witness(
        group,
        n,
        braid_word,
        longitude_witness,
    )
    return ArtinPermutationDefectWitnessAudit(
        n=n,
        braid_word=tuple(braid_word),
        word=word_tuple,
        assignment=assignment_tuple,
        defect_word=defect_word,
        defect_value=defect_value,
        longitude_witness=longitude_witness,
        longitude_witness_value=longitude_witness_value,
        witness_matches_defect=longitude_witness_value == defect_value,
    )


def artin_defect_abelianization_barrier_audit(
    group: FiniteGroup,
    endpoints: Sequence[GroupElement],
) -> ArtinDefectAbelianizationBarrierAudit:
    """Check the abelianization obstruction to pure Artin-defect displays.

    Every value of an Artin permutation defect
    ``beta(w) p_beta(w)^-1`` lies in the commutator subgroup of the target
    finite group.  Hence an endpoint outside ``[G,G]`` cannot be certified by
    a product of such defect values, although it may still lie in ``V_beta(G)``
    by an ordinary recursive-longitude or abelian matrix witness.
    """

    endpoint_tuple = tuple(endpoints)
    element_set = set(group.elements)
    if any(endpoint not in element_set for endpoint in endpoint_tuple):
        raise ValueError("endpoint outside group")
    commutator = commutator_subgroup_elements(group)
    commutator_set = set(commutator)
    outside = tuple(
        endpoint
        for endpoint in endpoint_tuple
        if endpoint not in commutator_set
    )
    return ArtinDefectAbelianizationBarrierAudit(
        group_order=len(group.elements),
        commutator_subgroup=commutator,
        endpoints=endpoint_tuple,
        endpoints_outside_commutator=outside,
    )


def free_word_exponent_vector(n: int, word: FreeWord) -> Tuple[int, ...]:
    """Return the abelianized exponent vector of a free word."""

    exponents = [0] * n
    for generator, exponent in word:
        if generator < 0 or generator >= n:
            raise IndexError(generator)
        exponents[generator] += exponent
    return tuple(exponents)


def artin_longitude_exponent_matrix(n: int, braid_word: BraidWord) -> Tuple[Tuple[int, ...], ...]:
    """Return the abelianized exponent vectors of all Artin longitudes."""

    data = artin_longitudes(n, braid_word)
    return tuple(
        free_word_exponent_vector(n, longitude)
        for longitude in data.longitudes
    )


def artin_longitude_row_column_sums(
    n: int, braid_word: BraidWord
) -> Tuple[Tuple[int, int], ...]:
    """Return row and column sums of the abelianized longitude matrix."""

    matrix = artin_longitude_exponent_matrix(n, braid_word)
    return tuple(
        (
            sum(matrix[index]),
            sum(row[index] for row in matrix),
        )
        for index in range(n)
    )


def has_trivial_abelian_longitudes_mod(
    modulus: int, n: int, braid_word: BraidWord
) -> bool:
    """Return whether all abelian longitude exponents vanish modulo modulus."""

    if modulus <= 0:
        raise ValueError("modulus must be positive")
    data = artin_longitudes(n, braid_word)
    if data.permutation != tuple(range(n)):
        return False
    return all(
        exponent % modulus == 0
        for row in artin_longitude_exponent_matrix(n, braid_word)
        for exponent in row
    )


def _require_abelian_group(group: FiniteGroup) -> None:
    if not is_abelian_group(group):
        raise ValueError("abelian longitude matrix formula requires an abelian group")


def abelian_longitude_value_generators(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
) -> Tuple[GroupElement, ...]:
    """Return the matrix-generated longitude values for an abelian group.

    If ``A`` is abelian and the exponent of ``x_j`` in ``L_i(beta)`` is
    ``m_ij``, then the values of all recursive longitudes under all
    assignments ``F_n -> A`` generate exactly the subgroup generated by
    ``a ** m_ij`` for every ``a in A`` and every matrix entry ``m_ij``.
    """

    if n < 0:
        raise ValueError("braid degree must be nonnegative")
    _require_abelian_group(group)
    matrix = artin_longitude_exponent_matrix(n, braid_word)
    coefficients = tuple(coefficient for row in matrix for coefficient in row)
    values = {
        group.pow(element, coefficient)
        for element in group.elements
        for coefficient in coefficients
    }
    return tuple(sorted(values, key=repr))


def abelian_longitude_value_subgroup_elements(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
) -> Tuple[GroupElement, ...]:
    """Return ``V_beta(A)`` from the abelian longitude exponent matrix."""

    return subgroup_generated_elements(
        group,
        abelian_longitude_value_generators(group, n, braid_word),
    )


def has_identity_abelian_longitude_signature(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
) -> bool:
    """Return whether finite-abelian longitude data equals the identity data."""

    _require_abelian_group(group)
    data = artin_longitudes(n, braid_word)
    if data.permutation != tuple(range(n)):
        return False
    return len(abelian_longitude_value_subgroup_elements(group, n, braid_word)) == 1


def abelian_longitude_image_audit(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    *,
    compare_by_enumeration: bool = False,
    max_assignments: int | None = None,
) -> AbelianLongitudeImageAudit:
    """Audit the exact abelian matrix formula for ``V_beta(A)``.

    The default avoids enumerating ``A^n``.  Set ``compare_by_enumeration`` to
    additionally compare the matrix subgroup with the general finite-group
    longitude enumeration on small examples.
    """

    if n < 0:
        raise ValueError("braid degree must be nonnegative")
    _require_abelian_group(group)
    data = artin_longitudes(n, braid_word)
    matrix = artin_longitude_exponent_matrix(n, braid_word)
    coefficient_entries = tuple(
        sorted({coefficient for row in matrix for coefficient in row})
    )
    matrix_generators = abelian_longitude_value_generators(group, n, braid_word)
    matrix_subgroup = abelian_longitude_value_subgroup_elements(
        group,
        n,
        braid_word,
    )
    enumerated_subgroup = (
        longitude_value_subgroup_elements(
            group,
            n,
            braid_word,
            max_assignments=max_assignments,
        )
        if compare_by_enumeration
        else None
    )
    return AbelianLongitudeImageAudit(
        n=n,
        braid_word=tuple(braid_word),
        group_order=len(group.elements),
        permutation=data.permutation,
        exponent_matrix=matrix,
        coefficient_entries=coefficient_entries,
        matrix_generators=matrix_generators,
        matrix_subgroup=matrix_subgroup,
        enumerated_subgroup=enumerated_subgroup,
    )


def _check_abelian_matrix_witness(
    group: FiniteGroup,
    n: int,
    witness: Sequence[AbelianLongitudeMatrixWitnessLetter],
) -> AbelianLongitudeMatrixWitness:
    elements = set(group.elements)
    rows = []
    for element, longitude_index, generator_index, exponent in witness:
        if element not in elements:
            raise ValueError("matrix witness element outside group")
        if longitude_index < 0 or longitude_index >= n:
            raise IndexError(longitude_index)
        if generator_index < 0 or generator_index >= n:
            raise IndexError(generator_index)
        if exponent not in (-1, 1):
            raise ValueError("matrix witness exponents must be +/-1")
        rows.append((element, longitude_index, generator_index, exponent))
    return tuple(rows)


def evaluate_abelian_longitude_matrix_witness(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    witness: Sequence[AbelianLongitudeMatrixWitnessLetter],
) -> GroupElement:
    """Evaluate a word in the matrix generators ``a^{m_ij}`` of ``V_beta(A)``."""

    if n < 0:
        raise ValueError("braid degree must be nonnegative")
    _require_abelian_group(group)
    witness_tuple = _check_abelian_matrix_witness(group, n, witness)
    matrix = artin_longitude_exponent_matrix(n, braid_word)
    out = group.identity
    for element, longitude_index, generator_index, exponent in witness_tuple:
        value = group.pow(element, matrix[longitude_index][generator_index])
        if exponent < 0:
            value = group.inv(value)
        out = group.mul(out, value)
    return out


def abelian_longitude_matrix_witness_to_subgroup_witness(
    group: FiniteGroup,
    n: int,
    witness: Sequence[AbelianLongitudeMatrixWitnessLetter],
) -> LongitudeSubgroupWitness:
    """Turn matrix letters into literal recursive-longitude subgroup letters."""

    if n < 0:
        raise ValueError("braid degree must be nonnegative")
    _require_abelian_group(group)
    witness_tuple = _check_abelian_matrix_witness(group, n, witness)
    rows: List[LongitudeSubgroupWitnessLetter] = []
    for element, longitude_index, generator_index, exponent in witness_tuple:
        assignment = [group.identity] * n
        assignment[generator_index] = element
        rows.append((tuple(assignment), longitude_index, exponent))
    return tuple(rows)


def abelian_longitude_matrix_witness_audit(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    endpoint: GroupElement,
    witness: Sequence[AbelianLongitudeMatrixWitnessLetter],
) -> AbelianLongitudeMatrixWitnessAudit:
    """Audit a displayed abelian matrix-subgroup certificate for an endpoint."""

    if endpoint not in group.elements:
        raise ValueError("endpoint outside group")
    matrix_witness = _check_abelian_matrix_witness(group, n, witness)
    matrix_value = evaluate_abelian_longitude_matrix_witness(
        group,
        n,
        braid_word,
        matrix_witness,
    )
    subgroup_witness = abelian_longitude_matrix_witness_to_subgroup_witness(
        group,
        n,
        matrix_witness,
    )
    subgroup_value = evaluate_longitude_subgroup_witness(
        group,
        n,
        braid_word,
        subgroup_witness,
    )
    return AbelianLongitudeMatrixWitnessAudit(
        n=n,
        braid_word=tuple(braid_word),
        endpoint=endpoint,
        matrix_witness=matrix_witness,
        matrix_witness_value=matrix_value,
        longitude_subgroup_witness=subgroup_witness,
        longitude_subgroup_witness_value=subgroup_value,
        endpoint_matches_matrix_witness=(endpoint == matrix_value),
        matrix_witness_matches_longitude_witness=(matrix_value == subgroup_value),
    )


def evaluate_artin_images(
    group: FiniteGroup, assignment: Sequence[GroupElement], braid_word: BraidWord
) -> Tuple[GroupElement, ...]:
    images = artin_images(len(assignment), braid_word)
    return tuple(evaluate_free_word(group, assignment, image) for image in images)


def evaluate_artin_longitudes(
    group: FiniteGroup, assignment: Sequence[GroupElement], braid_word: BraidWord
) -> Tuple[GroupElement, ...]:
    data = artin_longitudes(len(assignment), braid_word)
    return tuple(evaluate_free_word(group, assignment, longitude) for longitude in data.longitudes)


def evaluate_artin_longitudes_streamed(
    group: FiniteGroup, assignment: Sequence[GroupElement], braid_word: BraidWord
) -> Tuple[GroupElement, ...]:
    """Evaluate recursive Artin longitudes without expanding free words."""

    images = list(_check_group_assignment(group, assignment))
    longitudes = [group.identity for _ in images]
    n = len(images)
    for signed_generator in braid_word:
        if signed_generator == 0:
            raise ValueError("braid generators are nonzero")
        i = abs(signed_generator) - 1
        if i < 0 or i + 1 >= n:
            raise IndexError(i)
        image_i, image_j = images[i], images[i + 1]
        longitude_i, longitude_j = longitudes[i], longitudes[i + 1]
        if signed_generator > 0:
            images[i] = group.mul(group.mul(image_i, image_j), group.inv(image_i))
            images[i + 1] = image_i
            longitudes[i] = group.mul(image_i, longitude_j)
            longitudes[i + 1] = longitude_i
        else:
            images[i] = image_j
            images[i + 1] = group.mul(group.mul(group.inv(image_j), image_i), image_j)
            longitudes[i] = longitude_j
            longitudes[i + 1] = group.mul(group.inv(image_j), longitude_i)
    return tuple(longitudes)


def has_identity_longitude_signature_streamed(
    group: FiniteGroup, n: int, braid_word: BraidWord
) -> bool:
    """Streaming version of ``has_identity_longitude_signature``."""

    if braid_permutation(n, braid_word) != tuple(range(n)):
        return False
    identity_row = tuple(group.identity for _ in range(n))
    return all(
        evaluate_artin_longitudes_streamed(group, assignment, braid_word)
        == identity_row
        for assignment in product(group.elements, repeat=n)
    )


def evaluate_longitude_expression(
    group: FiniteGroup,
    assignment: Sequence[GroupElement],
    braid_word: BraidWord,
    expression: LongitudeExpression,
) -> GroupElement:
    """Evaluate a word in the Artin-longitude values for one assignment.

    The expression letters are ``(longitude_index, exponent)`` with
    zero-based longitude indices and exponent ``+1`` or ``-1``.  A matching
    expression is a compact certificate that the resulting element lies in
    ``V_beta(G)`` without enumerating every assignment into ``G``.
    """

    values = evaluate_artin_longitudes(group, assignment, braid_word)
    out = group.identity
    for longitude_index, exponent in expression:
        if longitude_index < 0 or longitude_index >= len(values):
            raise IndexError(longitude_index)
        if exponent not in (-1, 1):
            raise ValueError("longitude expression exponents must be +/-1")
        value = values[longitude_index]
        if exponent < 0:
            value = group.inv(value)
        out = group.mul(out, value)
    return out


def evaluate_longitude_subgroup_witness(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    witness: Sequence[LongitudeSubgroupWitnessLetter],
) -> GroupElement:
    """Evaluate a literal word in generators of ``V_beta(G)``.

    Each witness letter is ``(assignment, longitude_index, exponent)``.  Unlike
    ``evaluate_longitude_expression``, consecutive letters may use different
    assignments ``F_n -> G``.  Thus a successful equality with this value is a
    direct certificate of membership in the subgroup generated by all recursive
    longitude values.
    """

    if n < 0:
        raise ValueError("braid degree must be nonnegative")
    data = artin_longitudes(n, braid_word)
    elements = set(group.elements)
    out = group.identity
    for assignment, longitude_index, exponent in witness:
        assignment_tuple = tuple(assignment)
        if len(assignment_tuple) != n:
            raise ValueError("witness assignments must have length n")
        if any(value not in elements for value in assignment_tuple):
            raise ValueError("witness assignment contains a value outside the group")
        if longitude_index < 0 or longitude_index >= len(data.longitudes):
            raise IndexError(longitude_index)
        if exponent not in (-1, 1):
            raise ValueError("longitude witness exponents must be +/-1")
        value = evaluate_free_word(
            group,
            assignment_tuple,
            data.longitudes[longitude_index],
        )
        if exponent < 0:
            value = group.inv(value)
        out = group.mul(out, value)
    return out


def pushforward_longitude_subgroup_witness(
    homomorphism: FiniteGroupHomomorphism,
    witness: Sequence[LongitudeSubgroupWitnessLetter],
) -> LongitudeSubgroupWitness:
    """Push a ``V_beta(G)`` witness through a fixed homomorphism ``G -> H``."""

    source_elements = set(homomorphism.source.elements)
    pushed = []
    for assignment, longitude_index, exponent in witness:
        assignment_tuple = tuple(assignment)
        if any(value not in source_elements for value in assignment_tuple):
            raise ValueError("witness assignment contains a value outside the source group")
        pushed.append(
            (
                tuple(homomorphism.apply(value) for value in assignment_tuple),
                longitude_index,
                exponent,
            )
        )
    return tuple(pushed)


def pushforward_longitude_subgroup_witness_audit(
    homomorphism: FiniteGroupHomomorphism,
    n: int,
    braid_word: BraidWord,
    witness: Sequence[LongitudeSubgroupWitnessLetter],
) -> PushforwardLongitudeSubgroupWitnessAudit:
    """Audit that witness pushforward evaluates to the homomorphic image."""

    source_value = evaluate_longitude_subgroup_witness(
        homomorphism.source,
        n,
        braid_word,
        witness,
    )
    pushed_witness = pushforward_longitude_subgroup_witness(
        homomorphism,
        witness,
    )
    pushed_witness_value = evaluate_longitude_subgroup_witness(
        homomorphism.target,
        n,
        braid_word,
        pushed_witness,
    )
    target_image_value = homomorphism.apply(source_value)
    return PushforwardLongitudeSubgroupWitnessAudit(
        source_value=source_value,
        target_image_value=target_image_value,
        pushed_witness=pushed_witness,
        pushed_witness_value=pushed_witness_value,
        pushforward_matches_image=pushed_witness_value == target_image_value,
    )


def normal_quotient_longitude_lift_audit(
    quotient: FiniteGroupHomomorphism,
    n: int,
    braid_word: BraidWord,
    endpoint: GroupElement,
    quotient_witness: Sequence[LongitudeSubgroupWitnessLetter],
    lifted_witness: Sequence[LongitudeSubgroupWitnessLetter],
    kernel_witness: Sequence[LongitudeSubgroupWitnessLetter],
) -> NormalQuotientLongitudeLiftAudit:
    """Audit the quotient-plus-kernel certificate for ``endpoint in V_beta(G)``.

    Let ``q:G -> H`` be a surjective quotient map.  If ``q(endpoint)`` has a
    longitude witness in ``H``, choose any lifted witness in ``G`` that projects
    to that quotient value.  The correction

    ``endpoint * lifted_value^-1``

    lies in ``ker(q)``.  A witness for this correction using only assignments
    into ``ker(q)`` completes a literal witness for ``endpoint`` in ``G``.
    This is the certificate-level form of the abelianization-plus-commutator
    split used for the final unit-continuation endpoint.
    """

    source = quotient.source
    if endpoint not in set(source.elements):
        raise ValueError("endpoint must be an element of the source group")
    kernel = frozenset(
        element
        for element in source.elements
        if quotient.apply(element) == quotient.target.identity
    )
    quotient_witness_tuple = tuple(quotient_witness)
    lifted_witness_tuple = tuple(lifted_witness)
    kernel_witness_tuple = tuple(kernel_witness)
    quotient_endpoint = quotient.apply(endpoint)
    quotient_witness_value = evaluate_longitude_subgroup_witness(
        quotient.target,
        n,
        braid_word,
        quotient_witness_tuple,
    )
    lifted_witness_value = evaluate_longitude_subgroup_witness(
        source,
        n,
        braid_word,
        lifted_witness_tuple,
    )
    lifted_witness_projection_value = quotient.apply(lifted_witness_value)
    kernel_correction = source.mul(endpoint, source.inv(lifted_witness_value))
    kernel_witness_assignments_in_kernel = all(
        all(value in kernel for value in assignment)
        for assignment, _longitude_index, _exponent in kernel_witness_tuple
    )
    kernel_witness_value = evaluate_longitude_subgroup_witness(
        source,
        n,
        braid_word,
        kernel_witness_tuple,
    )
    combined_witness = kernel_witness_tuple + lifted_witness_tuple
    combined_witness_value = evaluate_longitude_subgroup_witness(
        source,
        n,
        braid_word,
        combined_witness,
    )
    return NormalQuotientLongitudeLiftAudit(
        n=n,
        braid_word=tuple(braid_word),
        endpoint=endpoint,
        quotient_endpoint=quotient_endpoint,
        quotient_witness=quotient_witness_tuple,
        quotient_witness_value=quotient_witness_value,
        lifted_witness=lifted_witness_tuple,
        lifted_witness_value=lifted_witness_value,
        lifted_witness_projection_value=lifted_witness_projection_value,
        kernel_size=len(kernel),
        kernel_correction=kernel_correction,
        kernel_correction_in_kernel=kernel_correction in kernel,
        kernel_witness=kernel_witness_tuple,
        kernel_witness_assignments_in_kernel=kernel_witness_assignments_in_kernel,
        kernel_witness_value=kernel_witness_value,
        combined_witness=combined_witness,
        combined_witness_value=combined_witness_value,
    )


def conjugate_longitude_subgroup_witness(
    group: FiniteGroup,
    conjugator: GroupElement,
    witness: Sequence[LongitudeSubgroupWitnessLetter],
) -> LongitudeSubgroupWitness:
    """Return a witness for ``conjugator * value * conjugator^-1``.

    Each witness letter evaluates a recursive longitude under some assignment
    ``phi:F_n -> G``.  Replacing that assignment by
    ``x_j |-> c phi(x_j) c^-1`` conjugates the corresponding longitude value.
    Letterwise conjugation therefore witnesses the conjugate of the whole
    product, which is the certificate-level normality of ``V_beta(G)``.
    """

    elements = set(group.elements)
    if conjugator not in elements:
        raise ValueError("conjugator must be an element of the group")
    inverse = group.inv(conjugator)
    conjugated = []
    for assignment, longitude_index, exponent in witness:
        assignment_tuple = tuple(assignment)
        if any(value not in elements for value in assignment_tuple):
            raise ValueError("witness assignment contains a value outside the group")
        conjugated.append(
            (
                tuple(
                    group.mul(group.mul(conjugator, value), inverse)
                    for value in assignment_tuple
                ),
                longitude_index,
                exponent,
            )
        )
    return tuple(conjugated)


def conjugate_longitude_subgroup_witness_audit(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    conjugator: GroupElement,
    witness: Sequence[LongitudeSubgroupWitnessLetter],
) -> ConjugateLongitudeSubgroupWitnessAudit:
    """Audit that conjugating assignments conjugates the witness value."""

    original_value = evaluate_longitude_subgroup_witness(
        group,
        n,
        braid_word,
        witness,
    )
    conjugated_witness = conjugate_longitude_subgroup_witness(
        group,
        conjugator,
        witness,
    )
    conjugated_witness_value = evaluate_longitude_subgroup_witness(
        group,
        n,
        braid_word,
        conjugated_witness,
    )
    expected_conjugate_value = group.mul(
        group.mul(conjugator, original_value),
        group.inv(conjugator),
    )
    return ConjugateLongitudeSubgroupWitnessAudit(
        original_value=original_value,
        conjugator=conjugator,
        conjugated_witness=conjugated_witness,
        conjugated_witness_value=conjugated_witness_value,
        expected_conjugate_value=expected_conjugate_value,
        conjugated_witness_matches=(
            conjugated_witness_value == expected_conjugate_value
        ),
    )


def direct_product_longitude_subgroup_witness(
    groups: Sequence[FiniteGroup],
    n: int,
    factor_witnesses: Sequence[Sequence[LongitudeSubgroupWitnessLetter]],
) -> LongitudeSubgroupWitness:
    """Assemble factor witnesses into a witness in the direct product group."""

    factors = tuple(groups)
    witnesses = tuple(tuple(witness) for witness in factor_witnesses)
    if len(factors) != len(witnesses):
        raise ValueError("need one longitude witness for each product factor")
    rows = []
    for factor_index, (group, witness) in enumerate(zip(factors, witnesses)):
        elements = set(group.elements)
        for assignment, longitude_index, exponent in witness:
            assignment_tuple = tuple(assignment)
            if len(assignment_tuple) != n:
                raise ValueError("factor witness assignments must have length n")
            if any(value not in elements for value in assignment_tuple):
                raise ValueError("factor witness assignment contains a value outside its group")
            product_assignment = tuple(
                tuple(
                    assignment_tuple[strand]
                    if coordinate == factor_index
                    else factor.identity
                    for coordinate, factor in enumerate(factors)
                )
                for strand in range(n)
            )
            rows.append((product_assignment, longitude_index, exponent))
    return tuple(rows)


def direct_product_longitude_subgroup_witness_audit(
    groups: Sequence[FiniteGroup],
    n: int,
    braid_word: BraidWord,
    factor_witnesses: Sequence[Sequence[LongitudeSubgroupWitnessLetter]],
) -> DirectProductLongitudeSubgroupWitnessAudit:
    """Audit that assembled product witnesses evaluate coordinatewise."""

    factors = tuple(groups)
    witnesses = tuple(tuple(witness) for witness in factor_witnesses)
    if len(factors) != len(witnesses):
        raise ValueError("need one longitude witness for each product factor")
    factor_values = tuple(
        evaluate_longitude_subgroup_witness(
            group,
            n,
            braid_word,
            witness,
        )
        for group, witness in zip(factors, witnesses)
    )
    product_group = direct_product_group(factors)
    product_witness = direct_product_longitude_subgroup_witness(
        factors,
        n,
        witnesses,
    )
    product_witness_value = evaluate_longitude_subgroup_witness(
        product_group,
        n,
        braid_word,
        product_witness,
    )
    expected_product_value = tuple(factor_values)
    return DirectProductLongitudeSubgroupWitnessAudit(
        factor_values=factor_values,
        product_witness=product_witness,
        product_witness_value=product_witness_value,
        expected_product_value=expected_product_value,
        product_witness_matches_factors=product_witness_value == expected_product_value,
    )


def longitude_value_generators(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    *,
    max_assignments: int | None = None,
) -> Tuple[GroupElement, ...]:
    """Return all finite-group values of all recursive Artin longitudes."""

    if max_assignments is not None and len(group.elements) ** n > max_assignments:
        raise ValueError(
            f"assignment search would enumerate {len(group.elements) ** n} rows; "
            f"raise max_assignments above {max_assignments} explicitly"
        )
    data = artin_longitudes(n, braid_word)
    values = {
        evaluate_free_word(group, assignment, longitude)
        for assignment in product(group.elements, repeat=n)
        for longitude in data.longitudes
    }
    return tuple(sorted(values, key=repr))


def longitude_value_subgroup_elements(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    *,
    max_assignments: int | None = None,
) -> Tuple[GroupElement, ...]:
    """Return the subgroup generated by all finite-group longitude values."""

    return subgroup_generated_elements(
        group,
        longitude_value_generators(
            group,
            n,
            braid_word,
            max_assignments=max_assignments,
        ),
    )


def longitude_subgroup_profile(
    groups: Mapping[str, FiniteGroup],
    n: int,
    braid_word: BraidWord,
    *,
    max_assignments: int | None = None,
) -> Tuple[LongitudeSubgroupProfileRow, ...]:
    """Return compact longitude-value subgroup visibility rows.

    For a finite group ``G``, identity finite-``G`` longitude data is
    equivalent to trivial Artin permutation and ``V_beta(G)={1}``, where
    ``V_beta(G)`` is the subgroup generated by all values of all recursive
    longitudes under all assignments ``F_n -> G``.
    """

    data = artin_longitudes(n, braid_word)
    rows = []
    for name, group in groups.items():
        generators = longitude_value_generators(
            group,
            n,
            braid_word,
            max_assignments=max_assignments,
        )
        subgroup = longitude_value_subgroup_elements(
            group,
            n,
            braid_word,
            max_assignments=max_assignments,
        )
        rows.append(
            LongitudeSubgroupProfileRow(
                name=name,
                group_order=len(group.elements),
                permutation=data.permutation,
                generator_count=len(generators),
                subgroup_size=len(subgroup),
            )
        )
    return tuple(rows)


def homomorphic_longitude_subgroup_audit(
    homomorphism: FiniteGroupHomomorphism,
    n: int,
    braid_word: BraidWord,
    *,
    max_assignments: int | None = None,
) -> HomomorphicLongitudeSubgroupAudit:
    """Return the image comparison for ``V_beta(G)`` under a homomorphism.

    For any group homomorphism ``f:G -> H``, the image of the longitude-value
    subgroup ``V_beta(G)`` is contained in ``V_beta(H)``.  If ``f`` is
    surjective, the two subgroups are equal, because every assignment
    ``F_n -> H`` lifts generator-by-generator to an assignment ``F_n -> G``.
    """

    source_subgroup = longitude_value_subgroup_elements(
        homomorphism.source,
        n,
        braid_word,
        max_assignments=max_assignments,
    )
    image_subgroup = {
        homomorphism.apply(element)
        for element in source_subgroup
    }
    target_subgroup = set(
        longitude_value_subgroup_elements(
            homomorphism.target,
            n,
            braid_word,
            max_assignments=max_assignments,
        )
    )
    return HomomorphicLongitudeSubgroupAudit(
        source_subgroup_size=len(source_subgroup),
        image_subgroup_size=len(image_subgroup),
        target_subgroup_size=len(target_subgroup),
        homomorphism_surjective=homomorphism.is_surjective,
        image_contained_in_target_subgroup=image_subgroup.issubset(target_subgroup),
        target_subgroup_equals_image=image_subgroup == target_subgroup,
    )


def direct_product_longitude_subgroup_audit(
    groups: Sequence[FiniteGroup],
    n: int,
    braid_word: BraidWord,
    *,
    max_assignments: int | None = None,
) -> DirectProductLongitudeSubgroupAudit:
    """Audit ``V_beta(product_i G_i) = product_i V_beta(G_i)``.

    Assignments ``F_n -> product_i G_i`` are tuples of assignments into the
    factors.  Because the all-identity assignment is available in every other
    factor, each factor longitude value embeds into the product subgroup with
    identity coordinates elsewhere.  Thus the product subgroup is exactly the
    Cartesian product of the factor subgroups.
    """

    factors = tuple(groups)
    product_group = direct_product_group(factors)
    product_subgroup = set(
        longitude_value_subgroup_elements(
            product_group,
            n,
            braid_word,
            max_assignments=max_assignments,
        )
    )
    factor_subgroups = tuple(
        tuple(
            longitude_value_subgroup_elements(
                group,
                n,
                braid_word,
                max_assignments=max_assignments,
            )
        )
        for group in factors
    )
    expected = set(product(*(subgroup for subgroup in factor_subgroups)))
    if not factors:
        expected = {tuple()}
    expected_size = 1
    for subgroup in factor_subgroups:
        expected_size *= len(subgroup)
    return DirectProductLongitudeSubgroupAudit(
        factor_orders=tuple(len(group.elements) for group in factors),
        factor_subgroup_sizes=tuple(len(subgroup) for subgroup in factor_subgroups),
        product_group_order=len(product_group.elements),
        product_subgroup_size=len(product_subgroup),
        expected_product_subgroup_size=expected_size,
        product_subgroup_equals_factor_product=product_subgroup == expected,
    )


def finite_group_longitude_signature(
    group: FiniteGroup, n: int, braid_word: BraidWord
) -> Tuple[Tuple[int, ...], Tuple[Tuple[GroupElement, ...], ...]]:
    """Evaluate all Artin longitudes over all assignments in a finite group."""

    data = artin_longitudes(n, braid_word)
    rows = []
    for assignment in product(group.elements, repeat=n):
        rows.append(
            tuple(evaluate_free_word(group, assignment, longitude) for longitude in data.longitudes)
        )
    return data.permutation, tuple(rows)


def has_identity_longitude_signature(group: FiniteGroup, n: int, braid_word: BraidWord) -> bool:
    permutation, rows = finite_group_longitude_signature(group, n, braid_word)
    if permutation != tuple(range(n)):
        return False
    identity_row = tuple(group.identity for _ in range(n))
    return all(row == identity_row for row in rows)


def symmetric_detector_reduction_audit(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    *,
    degree: int | None = None,
) -> SymmetricDetectorReductionAudit:
    """Audit that identity data in a symmetric group implies identity in ``G``.

    The group is embedded in ``S_degree`` by the left regular representation,
    fixing any extra points.  If the braid has identity finite-longitude data in
    that symmetric group, then restricting assignments to the embedded copy of
    ``G`` gives identity data in ``G``.
    """

    embedding = left_regular_representation(group, degree)
    target = embedding.target
    return SymmetricDetectorReductionAudit(
        group_order=len(group.elements),
        symmetric_degree=len(target.identity),
        symmetric_group_order=len(target.elements),
        embedding_injective=len(set(embedding.mapping.values())) == len(group.elements),
        source_identity_signature=has_identity_longitude_signature(
            group,
            n,
            braid_word,
        ),
        symmetric_identity_signature=has_identity_longitude_signature(
            target,
            n,
            braid_word,
        ),
    )


def symmetric_tower_monotonicity_audit(
    smaller_degree: int,
    larger_degree: int,
    n: int,
    braid_word: BraidWord,
) -> SymmetricTowerMonotonicityAudit:
    """Audit the inclusion ``K_{S_larger} <= K_{S_smaller}``.

    The group inclusion fixes the extra points.  If every assignment into
    ``S_larger`` kills the recursive longitudes of a braid, then in particular
    every assignment whose image lies in the embedded ``S_smaller`` kills them.
    """

    inclusion = symmetric_group_inclusion(smaller_degree, larger_degree)
    smaller = inclusion.source
    larger = inclusion.target
    return SymmetricTowerMonotonicityAudit(
        source_degree=smaller_degree,
        target_degree=larger_degree,
        inclusion_injective=len(set(inclusion.mapping.values())) == len(smaller.elements),
        smaller_identity_signature=has_identity_longitude_signature(
            smaller,
            n,
            braid_word,
        ),
        larger_identity_signature=has_identity_longitude_signature(
            larger,
            n,
            braid_word,
        ),
    )


def artin_detector_rack(group: FiniteGroup, include_trivial_two: bool = True) -> FiniteBraidedSet:
    """Build the finite rack A_G used by the sharp obstruction theorem.

    The active coordinates are `(a,u) in G x G` with
    `(a,u) rack (b,v) = (a b a^{-1}, a v)`.  When `include_trivial_two` is
    true, a two-element trivial rack factor is included as the first coordinate.
    """

    labels = (0, 1) if include_trivial_two else (None,)
    elements = tuple((label, a, u) for label in labels for a in group.elements for u in group.elements)

    def op(left, right):
        _left_label, a, _u = left
        right_label, b, v = right
        return (right_label, group.conjugate(a, b), group.mul(a, v))

    return rack_solution(elements, op)


def sharp_obstruction_rack(quotient_rack: FiniteBraidedSet, group: FiniteGroup) -> FiniteBraidedSet:
    """Return the finite rack ``Q x A_G`` used in the sharp domination step."""

    if not is_rack_solution(quotient_rack):
        raise ValueError("quotient detector must be a finite rack")
    return product_solution(quotient_rack, artin_detector_rack(group))


def detector_rack_state(
    group: FiniteGroup, assignment: Sequence[GroupElement], braid_word: BraidWord
) -> Tuple[Tuple[GroupElement, ...], Tuple[GroupElement, ...]]:
    """Apply A_G to `(g_i,e)` and return active coordinates.

    The first returned tuple is the evaluated Artin image tuple.  The second is
    the evaluated Artin-longitude tuple, with the convention used in this file.
    """

    rack = artin_detector_rack(group, include_trivial_two=True)
    start = tuple((0, value, group.identity) for value in assignment)
    image = rack.braid_action(braid_word, start)
    return tuple(cell[1] for cell in image), tuple(cell[2] for cell in image)


def direct_product_detector_action_audit(
    groups: Sequence[FiniteGroup],
    factor_assignments: Sequence[Sequence[GroupElement]],
    braid_word: BraidWord,
) -> DirectProductDetectorActionAudit:
    """Check that ``A_{product_i G_i}`` projects to the factor detector actions."""

    factors = tuple(groups)
    assignments = tuple(tuple(assignment) for assignment in factor_assignments)
    if not factors:
        raise ValueError("at least one detector factor is required")
    if len(factors) != len(assignments):
        raise ValueError("need one assignment tuple for each detector factor")
    n = len(assignments[0])
    if any(len(assignment) != n for assignment in assignments):
        raise ValueError("all factor assignments must have the same braid degree")
    for group, assignment in zip(factors, assignments):
        if any(value not in group.elements for value in assignment):
            raise ValueError("factor assignment contains a value outside its group")

    product_group = direct_product_group(factors)
    product_assignment = tuple(
        tuple(assignment[strand] for assignment in assignments)
        for strand in range(n)
    )
    product_image_values, product_longitude_values = detector_rack_state(
        product_group,
        product_assignment,
        braid_word,
    )
    factor_states = tuple(
        detector_rack_state(group, assignment, braid_word)
        for group, assignment in zip(factors, assignments)
    )
    factor_image_values = tuple(state[0] for state in factor_states)
    factor_longitude_values = tuple(state[1] for state in factor_states)
    projected_image_values = tuple(
        tuple(product_image_values[strand][factor_index] for strand in range(n))
        for factor_index in range(len(factors))
    )
    projected_longitude_values = tuple(
        tuple(product_longitude_values[strand][factor_index] for strand in range(n))
        for factor_index in range(len(factors))
    )
    return DirectProductDetectorActionAudit(
        factor_orders=tuple(len(group.elements) for group in factors),
        product_image_values=product_image_values,
        product_longitude_values=product_longitude_values,
        factor_image_values=factor_image_values,
        factor_longitude_values=factor_longitude_values,
        projected_image_values=projected_image_values,
        projected_longitude_values=projected_longitude_values,
        image_projections_match=projected_image_values == factor_image_values,
        longitude_projections_match=projected_longitude_values == factor_longitude_values,
    )


def diagonal_product_invisibility_audit(
    groups: Sequence[FiniteGroup],
    n: int,
    braid_word: BraidWord,
) -> DiagonalProductInvisibilityAudit:
    """Check product/factor finite-longitude invisibility equivalence.

    The diagonal normalized-obstruction lemma enumerates finite groups and
    uses products ``G_1 x ... x G_j``.  Identity finite-longitude data in the
    product is equivalent to identity data in every listed factor.
    """

    factors = tuple(groups)
    product_group = direct_product_group(factors)
    factor_signatures = tuple(
        has_identity_longitude_signature(group, n, braid_word)
        for group in factors
    )
    return DiagonalProductInvisibilityAudit(
        group_orders=tuple(len(group.elements) for group in factors),
        product_group_order=len(product_group.elements),
        factor_identity_signatures=factor_signatures,
        product_identity_signature=has_identity_longitude_signature(
            product_group,
            n,
            braid_word,
        ),
    )


def right_stabilization_longitude_audit(
    n: int,
    braid_word: BraidWord,
    extra_strands: int,
) -> RightStabilizationLongitudeAudit:
    """Check Artin data under the inclusion ``B_n -> B_{n+extra}``."""

    if extra_strands < 0:
        raise ValueError("extra_strands must be nonnegative")
    old_data = artin_longitudes(n, braid_word)
    new_n = n + extra_strands
    new_data = artin_longitudes(new_n, braid_word)
    return RightStabilizationLongitudeAudit(
        old_n=n,
        new_n=new_n,
        braid_word=tuple(braid_word),
        old_permutation=old_data.permutation,
        new_permutation=new_data.permutation,
        old_longitudes=old_data.longitudes,
        new_restricted_longitudes=new_data.longitudes[:n],
        added_longitudes=new_data.longitudes[n:],
    )


def normalized_law_prefix_witness_audit(
    solution: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    n: int,
    braid_word: BraidWord,
    moved_tuple: Sequence[object],
    extra_strands: int,
    fill_value: object,
) -> NormalizedLawPrefixWitnessAudit:
    """Check one explicit prefix record for a normalized-law B sequence.

    The listed groups represent the finite prefix ``G_1,...,G_j``; the helper
    checks invisibility in their product, right-stabilization of the Artin
    data, and survival of one moved tuple after adding unused right strands.
    It is a certificate-shape check for supplied data, not an all-`j` proof.
    """

    if not groups:
        raise ValueError("at least one finite group is required")
    if extra_strands < 0:
        raise ValueError("extra_strands must be nonnegative")
    tuple_value = tuple(moved_tuple)
    if len(tuple_value) != n:
        raise ValueError("moved_tuple length must equal n")
    if any(value not in solution.elements for value in tuple_value):
        raise ValueError("moved_tuple entries must lie in the solution")
    if fill_value not in solution.elements:
        raise ValueError("fill_value must lie in the solution")

    group_tuple = tuple(groups)
    product_group = direct_product_group(group_tuple)
    stabilization = right_stabilization_longitude_audit(
        n,
        braid_word,
        extra_strands,
    )
    target_n = n + extra_strands
    source_image = solution.braid_action(braid_word, tuple_value)
    stabilized_tuple = tuple_value + tuple(fill_value for _ in range(extra_strands))
    stabilized_image = solution.braid_action(braid_word, stabilized_tuple)
    return NormalizedLawPrefixWitnessAudit(
        source_n=n,
        target_n=target_n,
        braid_word=tuple(braid_word),
        group_orders=tuple(len(group.elements) for group in group_tuple),
        product_group_order=len(product_group.elements),
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
        moved_tuple=tuple_value,
        source_image=source_image,
        source_tuple_moved=source_image != tuple_value,
        stabilized_tuple=stabilized_tuple,
        stabilized_image=stabilized_image,
        stabilized_tuple_moved=stabilized_image != stabilized_tuple,
    )


def symmetric_normalized_law_prefix_witness_audit(
    solution: FiniteBraidedSet,
    symmetric_degree: int,
    n: int,
    braid_word: BraidWord,
    moved_tuple: Sequence[object],
    extra_strands: int,
    fill_value: object,
) -> NormalizedLawPrefixWitnessAudit:
    """Check one global normalized-law prefix using only ``S_j``.

    By the symmetric detector reduction, a final B construction may give
    witnesses against the symmetric tower instead of product prefixes of all
    finite groups.  This helper checks one supplied row for ``S_j``.
    """

    return normalized_law_prefix_witness_audit(
        solution,
        (symmetric_group(symmetric_degree),),
        n,
        braid_word,
        moved_tuple,
        extra_strands,
        fill_value,
    )


def rack_inner_group(rack: FiniteBraidedSet) -> FiniteGroup:
    """Return the finite inner permutation group of a rack-type solution."""

    index = {element: i for i, element in enumerate(rack.elements)}
    generators = []
    for left in rack.elements:
        images = []
        for right in rack.elements:
            first, second = rack.R[(left, right)]
            if second != left:
                raise ValueError("solution is not in rack form R(a,b)=(a▷b,a)")
            images.append(index[first])
        permutation = tuple(images)
        if set(permutation) != set(range(len(rack.elements))):
            raise ValueError("left rack translation is not bijective")
        generators.append(permutation)
    return permutation_group_from_generators(generators, degree=len(rack.elements))


def _rack_left_translation(
    rack: FiniteBraidedSet,
    index: Mapping[object, int],
    left: object,
) -> Tuple[int, ...]:
    images = []
    for right in rack.elements:
        first, second = rack.R[(left, right)]
        if second != left:
            raise ValueError("solution is not in rack form R(a,b)=(a*b,a)")
        images.append(index[first])
    permutation = tuple(images)
    if set(permutation) != set(range(len(rack.elements))):
        raise ValueError("left rack translation is not bijective")
    return permutation


def _apply_indexed_permutation(
    index: Mapping[object, int],
    elements_by_index: Mapping[int, object],
    permutation: GroupElement,
    element: object,
) -> object:
    perm = tuple(permutation)  # type: ignore[arg-type]
    return elements_by_index[perm[index[element]]]


def rack_inner_detector_lift_row_audit(
    rack: FiniteBraidedSet,
    left: object,
    right: object,
    endpoint_left: GroupElement | None = None,
    endpoint_right: GroupElement | None = None,
) -> RackInnerDetectorLiftRowAudit:
    """Audit one positive row for the rack inner-group detector factor.

    The rack is in the left convention ``R(a,b)=(a*b,a)``.  The meridian
    labels are left translations, and endpoint labels are arbitrary elements
    of the same inner group.
    """

    if left not in rack.elements or right not in rack.elements:
        raise ValueError("row atoms must be rack elements")
    group = rack_inner_group(rack)
    endpoint_left = group.identity if endpoint_left is None else endpoint_left
    endpoint_right = group.identity if endpoint_right is None else endpoint_right
    endpoint_left = _check_group_assignment(group, (endpoint_left,))[0]
    endpoint_right = _check_group_assignment(group, (endpoint_right,))[0]
    index = {element: i for i, element in enumerate(rack.elements)}
    elements_by_index = {i: element for element, i in index.items()}

    left_translation = _rack_left_translation(rack, index, left)
    right_translation = _rack_left_translation(rack, index, right)
    output_left, output_right = rack.R[(left, right)]
    output_left_translation = _rack_left_translation(rack, index, output_left)
    output_right_translation = _rack_left_translation(rack, index, output_right)
    supplied_left = (
        output_left_translation,
        group.mul(left_translation, endpoint_right),
    )
    supplied_right = (output_right_translation, endpoint_left)
    input_left = (left_translation, endpoint_left)
    input_right = (right_translation, endpoint_right)
    transition = artin_detector_lift_transition_audit(
        group,
        1,
        input_left,
        input_right,
        supplied_left,
        supplied_right,
    )
    left_translation_conjugacy_matches = output_left_translation == group.mul(
        group.mul(left_translation, right_translation),
        group.inv(left_translation),
    )
    right_output_translation_matches = output_right_translation == left_translation
    left_base = _apply_indexed_permutation(
        index,
        elements_by_index,
        group.inv(endpoint_left),
        left,
    )
    right_base = _apply_indexed_permutation(
        index,
        elements_by_index,
        group.inv(endpoint_right),
        right,
    )
    left_endpoint_image = _apply_indexed_permutation(
        index,
        elements_by_index,
        supplied_left[1],
        right_base,
    )
    right_endpoint_image = _apply_indexed_permutation(
        index,
        elements_by_index,
        supplied_right[1],
        left_base,
    )
    inverse_audit = artin_detector_lift_inverse_row_audit(
        group,
        input_left,
        input_right,
    )
    return RackInnerDetectorLiftRowAudit(
        input_left_atom=left,
        input_right_atom=right,
        output_left_atom=output_left,
        output_right_atom=output_right,
        endpoint_left=endpoint_left,
        endpoint_right=endpoint_right,
        input_left=input_left,
        input_right=input_right,
        supplied_left=supplied_left,
        supplied_right=supplied_right,
        transition_audit=transition,
        left_translation_conjugacy_matches=left_translation_conjugacy_matches,
        right_output_translation_matches=right_output_translation_matches,
        left_base_atom=left_base,
        right_base_atom=right_base,
        left_endpoint_image=left_endpoint_image,
        right_endpoint_image=right_endpoint_image,
        endpoint_transport_matches_crossing=(
            left_endpoint_image == output_left
            and right_endpoint_image == output_right
        ),
        negative_row_is_positive_inverse=(
            inverse_audit.negative_row_is_positive_inverse
        ),
    )


def rack_inner_detector_lift_audit(
    rack: FiniteBraidedSet,
    endpoint_labels: Sequence[GroupElement] | None = None,
) -> RackInnerDetectorLiftAudit:
    """Audit all positive rack rows for an inner-group detector factor.

    By default the endpoint label set is the identity singleton; callers may
    pass the whole inner group to check every finite endpoint state explicitly.
    The symbolic rack proof uses the same multiplication formula for arbitrary
    endpoint labels.
    """

    if not is_rack_solution(rack):
        raise ValueError("solution is not a rack in left convention")
    group = rack_inner_group(rack)
    labels = (
        (group.identity,)
        if endpoint_labels is None
        else _check_group_assignment(group, endpoint_labels)
    )
    row_audits = tuple(
        rack_inner_detector_lift_row_audit(
            rack,
            left,
            right,
            endpoint_left,
            endpoint_right,
        )
        for left in rack.elements
        for right in rack.elements
        for endpoint_left in labels
        for endpoint_right in labels
    )
    return RackInnerDetectorLiftAudit(
        rack_size=len(rack.elements),
        inner_group_order=len(group.elements),
        endpoint_label_count=len(labels),
        row_audits=row_audits,
    )


def right_rack_inner_detector_lift_audit(
    solution: FiniteBraidedSet,
    endpoint_labels: Sequence[GroupElement] | None = None,
) -> RackInnerDetectorLiftAudit:
    """Audit a right-rack-like layer via its side-opposite left rack."""

    return rack_inner_detector_lift_audit(
        opposite_solution(solution),
        endpoint_labels=endpoint_labels,
    )


def rack_extension_projection_failures(
    extension_rack: FiniteBraidedSet,
    base_rack: FiniteBraidedSet,
    projection: Mapping[object, object] | Callable[[object], object],
) -> Tuple[RackExtensionProjectionFailure, ...]:
    """Return failed identities ``p(e*f)=p(e)*p(f)`` for a rack extension."""

    if not is_rack_solution(base_rack) or not base_rack.is_ybe():
        raise ValueError("base solution must be a finite rack")
    if callable(projection):
        projection_map = {
            element: projection(element)
            for element in extension_rack.elements
        }
    else:
        if set(projection.keys()) != set(extension_rack.elements):
            raise ValueError("projection must be defined on every extension element")
        projection_map = dict(projection)
    if any(value not in base_rack.elements for value in projection_map.values()):
        raise ValueError("projection values must lie in the base rack")
    failures: List[RackExtensionProjectionFailure] = []
    for left, right in product(extension_rack.elements, repeat=2):
        extension_output, _extension_second = extension_rack.R[(left, right)]
        base_left = projection_map[left]
        base_right = projection_map[right]
        expected = _rack_operation_value(base_rack, base_left, base_right)
        actual = projection_map[extension_output]
        if actual != expected:
            failures.append(
                RackExtensionProjectionFailure(
                    left_extension_element=left,
                    right_extension_element=right,
                    projected_output=actual,
                    expected_base_output=expected,
                )
            )
    return tuple(failures)


def rack_extension_detector_audit(
    extension_rack: FiniteBraidedSet,
    base_rack: FiniteBraidedSet,
    projection: Mapping[object, object] | Callable[[object], object],
    endpoint_labels: Sequence[GroupElement] | None = None,
) -> RackExtensionDetectorAudit:
    """Audit the detector for a finite rack extension over a finite base rack."""

    if callable(projection):
        projection_map = {
            element: projection(element)
            for element in extension_rack.elements
        }
    else:
        if set(projection.keys()) != set(extension_rack.elements):
            raise ValueError("projection must be defined on every extension element")
        projection_map = dict(projection)
    if any(value not in base_rack.elements for value in projection_map.values()):
        raise ValueError("projection values must lie in the base rack")
    projection_failures = rack_extension_projection_failures(
        extension_rack,
        base_rack,
        projection_map,
    )
    extension_is_rack_form = is_rack_solution(extension_rack)
    extension_is_ybe = extension_rack.is_ybe()
    detector_lift_audit = (
        rack_inner_detector_lift_audit(
            extension_rack,
            endpoint_labels=endpoint_labels,
        )
        if extension_is_rack_form and extension_is_ybe
        else None
    )
    return RackExtensionDetectorAudit(
        base_rack_size=len(base_rack.elements),
        extension_size=len(extension_rack.elements),
        projection_image_size=len(set(projection_map.values())),
        projection_surjective=set(projection_map.values()) == set(base_rack.elements),
        extension_is_rack_form=extension_is_rack_form,
        extension_is_ybe=extension_is_ybe,
        projection_failures=projection_failures,
        inner_group_order=(
            detector_lift_audit.inner_group_order
            if detector_lift_audit is not None
            else None
        ),
        detector_lift_audit=detector_lift_audit,
    )


TransportStateTransition = (
    Mapping[Tuple[object, object, object, object], object]
    | Callable[[object, object, object, object], object]
)


def _transport_state_transition_value(
    states: Tuple[object, ...],
    transition: TransportStateTransition,
    left_atom: object,
    right_atom: object,
    left_state: object,
    right_state: object,
) -> object:
    value = (
        transition(left_atom, right_atom, left_state, right_state)
        if callable(transition)
        else transition[(left_atom, right_atom, left_state, right_state)]
    )
    if value not in states:
        raise ValueError("transport-state transition value outside state set")
    return value


def transport_state_left_translation_failures(
    atom_rack: FiniteBraidedSet,
    states: Iterable[object],
    transition: TransportStateTransition,
) -> Tuple[TransportStateLeftTranslationFailure, ...]:
    """Return non-bijective left translations for ``A x E`` transport rows."""

    if not is_rack_solution(atom_rack) or not atom_rack.is_ybe():
        raise ValueError("atom solution must be a finite rack")
    state_tuple = tuple(states)
    if not state_tuple:
        raise ValueError("transport-state set must be nonempty")
    elements = tuple(
        (atom, state)
        for atom in atom_rack.elements
        for state in state_tuple
    )
    expected_size = len(elements)
    failures: List[TransportStateLeftTranslationFailure] = []
    for left_atom, left_state in elements:
        images = set()
        for right_atom, right_state in elements:
            images.add(
                (
                    _rack_operation_value(atom_rack, left_atom, right_atom),
                    _transport_state_transition_value(
                        state_tuple,
                        transition,
                        left_atom,
                        right_atom,
                        left_state,
                        right_state,
                    ),
                )
            )
        if len(images) != expected_size:
            failures.append(
                TransportStateLeftTranslationFailure(
                    left_atom=left_atom,
                    left_state=left_state,
                    image_size=len(images),
                    expected_size=expected_size,
                )
            )
    return tuple(failures)


def transport_state_rack(
    atom_rack: FiniteBraidedSet,
    states: Iterable[object],
    transition: TransportStateTransition,
) -> FiniteBraidedSet:
    """Build the rack-type transport-state row on ``A x E``."""

    state_tuple = tuple(states)
    failures = transport_state_left_translation_failures(
        atom_rack,
        state_tuple,
        transition,
    )
    if failures:
        raise ValueError("transport-state left translations are not bijective")
    elements = tuple(
        (atom, state)
        for atom in atom_rack.elements
        for state in state_tuple
    )

    def op(left: Tuple[object, object], right: Tuple[object, object]):
        left_atom, left_state = left
        right_atom, right_state = right
        return (
            _rack_operation_value(atom_rack, left_atom, right_atom),
            _transport_state_transition_value(
                state_tuple,
                transition,
                left_atom,
                right_atom,
                left_state,
                right_state,
            ),
        )

    return rack_solution(elements, op)


def transport_state_rackification_audit(
    atom_rack: FiniteBraidedSet,
    states: Iterable[object],
    transition: TransportStateTransition,
    endpoint_labels: Sequence[GroupElement] | None = None,
) -> TransportStateRackificationAudit:
    """Audit the finite detector for a strand-continuing transport-state row."""

    state_tuple = tuple(states)
    failures = transport_state_left_translation_failures(
        atom_rack,
        state_tuple,
        transition,
    )
    extension_audit = None
    transport_built = False
    if not failures:
        transport = transport_state_rack(atom_rack, state_tuple, transition)
        transport_built = True
        projection = {
            element: element[0]
            for element in transport.elements
        }
        extension_audit = rack_extension_detector_audit(
            transport,
            atom_rack,
            projection,
            endpoint_labels=endpoint_labels,
        )
    return TransportStateRackificationAudit(
        atom_rack_size=len(atom_rack.elements),
        state_count=len(state_tuple),
        transport_size=len(atom_rack.elements) * len(state_tuple),
        left_translation_failures=failures,
        transport_rack_built=transport_built,
        extension_detector_audit=extension_audit,
    )


PrincipalGaugeCocycle = (
    Mapping[Tuple[object, object], GroupElement]
    | Callable[[object, object], GroupElement]
)


def _rack_operation_value(
    rack: FiniteBraidedSet,
    left: object,
    right: object,
) -> object:
    first, second = rack.R[(left, right)]
    if second != left:
        raise ValueError("base solution is not in left rack form R(a,b)=(a*b,a)")
    return first


def _principal_gauge_cocycle_value(
    unit_group: FiniteGroup,
    cocycle: PrincipalGaugeCocycle,
    left: object,
    right: object,
) -> GroupElement:
    value = (
        cocycle(left, right)
        if callable(cocycle)
        else cocycle[(left, right)]
    )
    if value not in unit_group.elements:
        raise ValueError("principal gauge cocycle value outside unit group")
    return value


def principal_gauge_cocycle_failures(
    base_rack: FiniteBraidedSet,
    unit_group: FiniteGroup,
    cocycle: PrincipalGaugeCocycle,
) -> Tuple[PrincipalGaugeCocycleFailure, ...]:
    """Return failed identities ``c(a,b*d)c(b,d)=c(a*b,a*d)c(a,d)``."""

    if not is_rack_solution(base_rack) or not base_rack.is_ybe():
        raise ValueError("base solution must be a finite rack")
    failures: List[PrincipalGaugeCocycleFailure] = []
    for left, middle, right in product(base_rack.elements, repeat=3):
        middle_under_right = _rack_operation_value(base_rack, middle, right)
        left_under_middle = _rack_operation_value(base_rack, left, middle)
        left_under_right = _rack_operation_value(base_rack, left, right)
        left_value = unit_group.mul(
            _principal_gauge_cocycle_value(
                unit_group,
                cocycle,
                left,
                middle_under_right,
            ),
            _principal_gauge_cocycle_value(unit_group, cocycle, middle, right),
        )
        right_value = unit_group.mul(
            _principal_gauge_cocycle_value(
                unit_group,
                cocycle,
                left_under_middle,
                left_under_right,
            ),
            _principal_gauge_cocycle_value(unit_group, cocycle, left, right),
        )
        if left_value != right_value:
            failures.append(
                PrincipalGaugeCocycleFailure(
                    left_atom=left,
                    middle_atom=middle,
                    right_atom=right,
                    left_value=left_value,
                    right_value=right_value,
                )
            )
    return tuple(failures)


def principal_gauge_extension_rack(
    base_rack: FiniteBraidedSet,
    unit_group: FiniteGroup,
    cocycle: PrincipalGaugeCocycle,
) -> FiniteBraidedSet:
    """Build the principal gauge extension ``(a,r)*(b,s)=(a*b,c(a,b)s)``."""

    if not is_rack_solution(base_rack) or not base_rack.is_ybe():
        raise ValueError("base solution must be a finite rack")
    elements = tuple(
        (atom, unit)
        for atom in base_rack.elements
        for unit in unit_group.elements
    )

    def op(left: Tuple[object, GroupElement], right: Tuple[object, GroupElement]):
        left_atom, _left_unit = left
        right_atom, right_unit = right
        return (
            _rack_operation_value(base_rack, left_atom, right_atom),
            unit_group.mul(
                _principal_gauge_cocycle_value(
                    unit_group,
                    cocycle,
                    left_atom,
                    right_atom,
                ),
                right_unit,
            ),
        )

    return rack_solution(elements, op)


def principal_gauge_extension_detector_audit(
    base_rack: FiniteBraidedSet,
    unit_group: FiniteGroup,
    cocycle: PrincipalGaugeCocycle,
    endpoint_labels: Sequence[GroupElement] | None = None,
) -> PrincipalGaugeExtensionDetectorAudit:
    """Audit that a principal gauge cocycle is closed by a rack inner detector."""

    failures = principal_gauge_cocycle_failures(base_rack, unit_group, cocycle)
    extension = principal_gauge_extension_rack(base_rack, unit_group, cocycle)
    extension_is_rack_form = is_rack_solution(extension)
    extension_is_ybe = extension.is_ybe()
    detector_lift_audit = rack_inner_detector_lift_audit(
        extension,
        endpoint_labels=endpoint_labels,
    )
    return PrincipalGaugeExtensionDetectorAudit(
        base_rack_size=len(base_rack.elements),
        unit_group_order=len(unit_group.elements),
        extension_size=len(extension.elements),
        cocycle_failures=failures,
        extension_is_rack_form=extension_is_rack_form,
        extension_is_ybe=extension_is_ybe,
        inner_group_order=detector_lift_audit.inner_group_order,
        detector_lift_audit=detector_lift_audit,
    )


def rack_longitude_action(
    rack: FiniteBraidedSet, braid_word: BraidWord, tup: Sequence[GroupElement]
) -> Tuple[GroupElement, ...]:
    """Compute rack braid action from Artin longitudes in the inner group."""

    return rack_longitude_factorization(rack, braid_word, tup).output


def rack_longitude_factorization(
    rack: FiniteBraidedSet, braid_word: BraidWord, tup: Sequence[GroupElement]
) -> RackLongitudeFactorization:
    """Return the finite-group longitude data computing a rack action."""

    group = rack_inner_group(rack)
    index = {element: i for i, element in enumerate(rack.elements)}
    elements_by_index = {i: element for element, i in index.items()}
    translations = {}
    for left in rack.elements:
        translations[left] = tuple(
            index[rack.R[(left, right)][0]]
            for right in rack.elements
        )
    assignment = tuple(translations[element] for element in tup)
    data = artin_longitudes(len(tup), braid_word)
    longitude_values = tuple(
        evaluate_free_word(group, assignment, longitude)
        for longitude in data.longitudes
    )
    out = []
    for permutation, target in zip(longitude_values, data.permutation):
        out.append(elements_by_index[permutation[index[tup[target]]]])
    return RackLongitudeFactorization(
        assignment=assignment,
        permutation=data.permutation,
        longitude_values=longitude_values,
        output=tuple(out),
    )



def longitude_blind_movers(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    n: int,
    braid_words: Iterable[BraidWord],
) -> Dict[Tuple[int, ...], Tuple[Tuple[object, ...], Tuple[object, ...]]]:
    """Find bounded evidence for words invisible to G-longitudes but moving X^n."""

    movers = {}
    for word in braid_words:
        key = tuple(word)
        if not has_identity_longitude_signature(group, n, key):
            continue
        for tup in product(solution.elements, repeat=n):
            image = solution.braid_action(key, tup)
            if image != tup:
                movers[key] = (tuple(tup), image)
                break
    return movers
