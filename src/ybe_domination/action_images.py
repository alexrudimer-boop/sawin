from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product
from typing import Iterable, Mapping, Sequence, Tuple

from .artin_longitudes import BraidWord, FreeWord, NormalizedLawPrefixWitnessAudit
from .finite_braided_set import FiniteBraidedSet
from .finite_group import (
    FiniteGroup,
    commutator_subgroup_elements,
    is_abelian_group,
    subgroup_generated_elements,
)
from .residual import action_permutation, permutation_order

Permutation = Tuple[int, ...]


@dataclass(frozen=True)
class PureGeneratorOrderRow:
    braid_index: int
    tuple_count: int
    generator_orders: Tuple[int, ...]
    max_order: int


@dataclass(frozen=True)
class PureSubgroupGrowthRow:
    braid_index: int
    tuple_count: int
    generator_count: int
    subgroup_size: int | None
    subgroup_exponent: int | None
    truncated: bool


@dataclass(frozen=True)
class LawBraidActionCertificate:
    braid_index: int
    tuple_count: int
    generator_image_subgroup_size: int
    generator_image_subgroup_exponent: int
    word_is_law_on_image_subgroup: bool
    evaluated_word_is_identity: bool
    direct_braid_is_identity: bool
    direct_matches_evaluated: bool


@dataclass(frozen=True)
class AssignedLawSeparation:
    """A law on detector groups that moves a specific permutation assignment."""

    arity: int
    target_degree: int
    separating_word: FreeWord | None
    evaluated_permutation: Permutation | None
    moved_index: int | None


@dataclass(frozen=True)
class PointPushingMarkedQuotientAudit:
    """Exact finite arity check for the derivative-detector quotient criterion."""

    group_order: int
    arity: int
    braid_index: int
    detector_state_count: int
    ybe_tuple_count: int
    pair_subgroup_size: int | None
    detector_image_size: int | None
    action_image_size: int | None
    truncated: bool
    witness_word: FreeWord | None
    witness_action_value: Permutation | None
    moved_index: int | None

    @property
    def found_kernel_mover(self) -> bool:
        return self.witness_word is not None and self.moved_index is not None

    @property
    def marked_quotient_holds(self) -> bool:
        return not self.truncated and not self.found_kernel_mover

    @property
    def vertical_kernel_trivial(self) -> bool:
        """Whether ``<(d_i,h_i)>`` has no nontrivial ``(1,p)`` witness."""

        return self.marked_quotient_holds


@dataclass(frozen=True)
class PointPushingVerticalWitnessCertificate:
    """Checked finite row for a nontrivial paired vertical-kernel witness."""

    group_order: int
    arity: int
    braid_index: int
    detector_state_count: int
    ybe_tuple_count: int
    word: FreeWord
    braid_word: BraidWord
    detector_word_identity: bool
    evaluated_action_identity: bool
    direct_braid_identity: bool
    direct_matches_evaluated: bool
    moved_index: int | None
    moved_tuple: Tuple[object, ...] | None
    moved_tuple_image: Tuple[object, ...] | None

    @property
    def moves_solution(self) -> bool:
        return self.moved_index is not None and not self.direct_braid_identity

    @property
    def valid_vertical_witness(self) -> bool:
        return (
            self.detector_word_identity
            and self.direct_matches_evaluated
            and self.moves_solution
        )


@dataclass(frozen=True)
class PointPushingBrunnianWitnessCertificate:
    """Right-based one-new-strand Brunnian vertical witness certificate."""

    arity: int
    right_based_word: FreeWord
    left_based_word: FreeWord
    deletion_word: FreeWord
    deletion_trivial: bool
    vertical: PointPushingVerticalWitnessCertificate

    @property
    def valid_brunnian_witness(self) -> bool:
        return self.deletion_trivial and self.vertical.valid_vertical_witness


@dataclass(frozen=True)
class PointPushingBrunnianOrbitAudit:
    """Finite normal-closure check for one Brunnian extension step."""

    group_order: int
    arity: int
    braid_index: int
    detector_state_count: int
    ybe_tuple_count: int
    old_pair_subgroup_size: int | None
    conjugate_generator_count: int | None
    detector_stabilizer_size: int | None
    stabilizer_centralizes_new_action: bool | None
    detector_orbit_size: int | None
    action_orbit_size: int | None
    orbit_map_well_defined: bool | None
    relative_detector_projection_size: int | None
    relative_action_projection_size: int | None
    relative_subgroup_size: int | None
    failure_kind: str
    truncated: bool
    witness_right_word: FreeWord | None
    witness_left_word: FreeWord | None
    witness_action_value: Permutation | None
    moved_index: int | None

    @property
    def found_brunnian_vertical_witness(self) -> bool:
        return self.witness_right_word is not None and self.moved_index is not None

    @property
    def relative_vertical_kernel_trivial(self) -> bool:
        return (
            not self.truncated
            and self.failure_kind == "none"
            and self.orbit_map_well_defined is not False
            and not self.found_brunnian_vertical_witness
        )


@dataclass(frozen=True)
class PointPushingBrunnianGatePrefixAudit:
    """Sequential finite-prefix check for the Brunnian extension induction."""

    group_order: int
    max_arity: int
    base_audit: PointPushingMarkedQuotientAudit
    extension_rows: Tuple[PointPushingBrunnianOrbitAudit, ...]
    first_failure_arity: int | None
    first_failure_kind: str | None

    @property
    def prefix_detected(self) -> bool:
        return self.first_failure_arity is None

    @property
    def checked_arities(self) -> Tuple[int, ...]:
        return (1,) + tuple(row.arity for row in self.extension_rows)


@dataclass(frozen=True)
class PointPushingBaseArityCertificate:
    """Closed-form certificate for the arity-1 point-pushing base gate."""

    tuple_count: int
    pure_generator_order: int
    symmetric_degree_bound: int
    symmetric_exponent: int
    symmetric_marked_quotient_holds: bool

    @property
    def proves_base_arity_detected(self) -> bool:
        return self.symmetric_marked_quotient_holds


@dataclass(frozen=True)
class PointPushingCyclicTailBoundAudit:
    """Uniform generator-order bound for cyclic point-pushing quotients."""

    tuple_count: int
    cyclic_quotient_order_bound: int
    max_braid_index_checked: int
    rows: Tuple[PureGeneratorOrderRow, ...]
    checked_generator_orders_divide_bound: bool

    @property
    def closes_cyclic_tails_symbolically(self) -> bool:
        return self.cyclic_quotient_order_bound >= 1


@dataclass(frozen=True)
class PointPushingBoundedNormalGeneratorAudit:
    """Uniform bound for first-failure monolith normal generators."""

    tuple_count: int
    normal_generator_order_bound: int
    max_braid_index_checked: int
    rows: Tuple[PureGeneratorOrderRow, ...]
    checked_generator_orders_divide_bound: bool

    @property
    def supports_bounded_normal_generator_reduction(self) -> bool:
        return self.normal_generator_order_bound >= 1


@dataclass(frozen=True)
class PointPushingBrunnianFailureCertificate:
    """Braid-action certificate for one nontrivial Brunnian gate failure."""

    group_order: int
    arity: int
    failure_kind: str
    orbit_audit: PointPushingBrunnianOrbitAudit
    witness: PointPushingBrunnianWitnessCertificate | None

    @property
    def has_real_failure_kind(self) -> bool:
        return self.failure_kind in ("stabilizer", "orbit_label", "orbit_relation")

    @property
    def valid_failure_certificate(self) -> bool:
        return (
            self.has_real_failure_kind
            and self.witness is not None
            and self.witness.valid_brunnian_witness
        )


@dataclass(frozen=True)
class PointPushingBrunnianTailRow:
    """One symmetric degree in a finite first-failure tail diagnostic."""

    symmetric_degree: int
    max_arity: int
    prefix_detected: bool
    first_failure_arity: int | None
    first_failure_kind: str | None


@dataclass(frozen=True)
class PointPushingBrunnianTailPrefixAudit:
    """Finite prefix of the symmetric first-failure tail."""

    max_symmetric_degree: int
    max_arity: int
    rows: Tuple[PointPushingBrunnianTailRow, ...]

    @property
    def unresolved_degrees(self) -> Tuple[int, ...]:
        return tuple(row.symmetric_degree for row in self.rows if not row.prefix_detected)

    @property
    def detected_degrees(self) -> Tuple[int, ...]:
        return tuple(row.symmetric_degree for row in self.rows if row.prefix_detected)

    @property
    def failure_kinds(self) -> Tuple[str, ...]:
        return tuple(
            row.first_failure_kind
            for row in self.rows
            if row.first_failure_kind is not None
        )


@dataclass(frozen=True)
class PointPushingBrunnianTailCertificateRow:
    """One symmetric degree with its first-failure certificate when available."""

    symmetric_degree: int
    max_arity: int
    prefix_detected: bool
    first_failure_arity: int | None
    first_failure_kind: str | None
    certificate: PointPushingBrunnianFailureCertificate | None

    @property
    def has_valid_nonbase_certificate(self) -> bool:
        return (
            self.certificate is not None
            and self.certificate.valid_failure_certificate
        )


@dataclass(frozen=True)
class PointPushingBrunnianTailCertificatePrefix:
    """Finite symmetric-tail prefix with braid-action certificates."""

    max_symmetric_degree: int
    max_arity: int
    rows: Tuple[PointPushingBrunnianTailCertificateRow, ...]

    @property
    def detected_degrees(self) -> Tuple[int, ...]:
        return tuple(row.symmetric_degree for row in self.rows if row.prefix_detected)

    @property
    def certified_nonbase_degrees(self) -> Tuple[int, ...]:
        return tuple(
            row.symmetric_degree for row in self.rows if row.has_valid_nonbase_certificate
        )

    @property
    def uncertified_failure_degrees(self) -> Tuple[int, ...]:
        return tuple(
            row.symmetric_degree
            for row in self.rows
            if not row.prefix_detected and not row.has_valid_nonbase_certificate
        )

    @property
    def certified_failure_kinds(self) -> Tuple[str, ...]:
        return tuple(
            row.first_failure_kind
            for row in self.rows
            if row.has_valid_nonbase_certificate and row.first_failure_kind is not None
        )


@dataclass(frozen=True)
class PointPushingProductPrefixFirstFailureRow:
    """One product-prefix detector row in the first-failure profile."""

    prefix_index: int
    product_group_order: int
    max_arity: int
    prefix_detected: bool
    first_failure_arity: int | None
    first_failure_kind: str | None

    @property
    def has_nonbase_failure(self) -> bool:
        return self.first_failure_kind in ("stabilizer", "orbit_label", "orbit_relation")


@dataclass(frozen=True)
class PointPushingProductPrefixFirstFailureAudit:
    """Finite product-prefix first-failure stratification diagnostic."""

    prefix_count: int
    max_arity: int
    rows: Tuple[PointPushingProductPrefixFirstFailureRow, ...]

    @property
    def detected_prefix_indices(self) -> Tuple[int, ...]:
        return tuple(row.prefix_index for row in self.rows if row.prefix_detected)

    @property
    def unresolved_prefix_indices(self) -> Tuple[int, ...]:
        return tuple(row.prefix_index for row in self.rows if not row.prefix_detected)

    @property
    def nonbase_failure_prefix_indices(self) -> Tuple[int, ...]:
        return tuple(row.prefix_index for row in self.rows if row.has_nonbase_failure)

    @property
    def failure_kinds(self) -> Tuple[str, ...]:
        return tuple(
            row.first_failure_kind
            for row in self.rows
            if row.first_failure_kind is not None
        )

    @property
    def first_failure_arities_weakly_increase(self) -> bool:
        previous = 0
        for row in self.rows:
            value = row.first_failure_arity
            if value is None:
                value = self.max_arity + 1
            if value < previous:
                return False
            previous = value
        return True


@dataclass(frozen=True)
class PointPushingActionQuotientSeparationRow:
    """Finite residual-depth diagnostic for one action image ``P_k(X)``."""

    arity: int
    action_group_order: int | None
    nonidentity_count: int | None
    max_separating_quotient_size: int | None
    deepest_element: Permutation | None
    truncated: bool

    @property
    def computed_all_separators(self) -> bool:
        return not self.truncated and self.max_separating_quotient_size is not None


@dataclass(frozen=True)
class PointPushingActionQuotientSeparationAudit:
    """Finite-prefix audit for quotient-separating depth of action images."""

    max_arity: int
    max_action_group_order: int | None
    rows: Tuple[PointPushingActionQuotientSeparationRow, ...]

    @property
    def truncated_arities(self) -> Tuple[int, ...]:
        return tuple(row.arity for row in self.rows if row.truncated)

    @property
    def computed_arities(self) -> Tuple[int, ...]:
        return tuple(row.arity for row in self.rows if row.computed_all_separators)

    @property
    def prefix_separation_bound(self) -> int | None:
        values = [
            row.max_separating_quotient_size
            for row in self.rows
            if row.max_separating_quotient_size is not None
        ]
        if len(values) != len(self.rows):
            return None
        return max(values, default=1)


@dataclass(frozen=True)
class PointPushingMonolithicCompressionAudit:
    """Compress one moving point-pushing action value to a minimal quotient."""

    arity: int
    word: FreeWord
    action_group_order: int | None
    action_value: object | None
    action_value_nontrivial: bool
    quotient_order: int | None
    quotient_kernel_size: int | None
    monolith_order: int | None
    monolith_type: str | None
    monolith_prime: int | None
    monolith_element_orders: Tuple[int, ...] | None
    monolith_centralizer_order: int | None
    monolith_action_quotient_order: int | None
    monolith_commutator_order: int | None
    monolith_is_central: bool | None
    quotient_commutator_order: int | None
    monolith_in_quotient_commutator: bool | None
    projected_value_in_quotient_commutator: bool | None
    central_abelian_depth_regime: str | None
    central_cyclic_prime: int | None
    central_cyclic_exponent: int | None
    central_cyclic_prefix_regime: str | None
    noncentral_module_dimension: int | None
    noncentral_centralizer_layer_order: int | None
    noncentral_size_product_matches_quotient: bool | None
    noncentral_parameter_regime: str | None
    nonabelian_centralizer_trivial: bool | None
    nonabelian_over_monolith_order: int | None
    nonabelian_prefix_regime: str | None
    quotient_is_monolithic: bool | None
    projected_value_in_monolith: bool | None
    prefix_order_bound: int | None
    quotient_escapes_prefix_bound: bool | None
    truncated: bool

    @property
    def proves_monolithic_compression(self) -> bool:
        return (
            not self.truncated
            and self.action_value_nontrivial
            and self.quotient_is_monolithic is True
            and self.projected_value_in_monolith is True
        )


@dataclass(frozen=True)
class PointPushingAbelianChiefRelationModuleAudit:
    """Bookkeeping for abelian-chief relation-module compression."""

    group_order: int
    monolith_order: int
    relation_image_order: int
    monolith_is_normal: bool
    relation_image_is_normal: bool
    monolith_is_unique_minimal_normal: bool
    monolith_is_abelian: bool
    relation_image_nontrivial: bool
    relation_image_inside_monolith: bool
    relation_image_equals_monolith: bool

    @property
    def proves_abelian_chief_relation_module_quotient(self) -> bool:
        return (
            self.monolith_is_normal
            and self.relation_image_is_normal
            and self.monolith_is_unique_minimal_normal
            and self.monolith_is_abelian
            and self.relation_image_nontrivial
            and self.relation_image_inside_monolith
            and self.relation_image_equals_monolith
        )


@dataclass(frozen=True)
class PointPushingAbelianRelationActionSplitAudit:
    """Split abelian-chief relation quotients by trivial/nontrivial action."""

    group_order: int
    monolith_order: int
    monolith_prime: int | None
    relation_image_order: int
    monolith_is_abelian: bool
    monolith_is_central: bool
    monolith_is_unique_minimal_normal: bool
    relation_image_equals_monolith: bool
    split_regime: str

    @property
    def proves_abelian_relation_action_split(self) -> bool:
        return self.split_regime in (
            "central_trivial_coinvariant",
            "noncentral_irreducible_module",
        )


@dataclass(frozen=True)
class PointPushingModulePrimeCharacteristicAudit:
    """Split module-prime tails by the fixed point-pushing order bound."""

    normal_generator_order_bound: int
    module_prime: int
    prime_divides_bound: bool
    cross_characteristic: bool
    tail_regime: str

    @property
    def proves_prime_tail_characteristic_split(self) -> bool:
        return self.tail_regime in (
            "bounded_prime_divides_generator_bound",
            "cross_characteristic_prime_escape",
        )


@dataclass(frozen=True)
class PointPushingActiveModuleGeneratorAudit:
    """Split module rows by whether the bounded generator acts on the module."""

    normal_generator_order_bound: int
    generator_action_order: int
    action_order_divides_bound: bool
    active_on_module: bool
    tail_regime: str

    @property
    def proves_active_module_generator_split(self) -> bool:
        return self.tail_regime in (
            "centralizer_layer_generator",
            "active_bounded_order_linear_generator",
        )


@dataclass(frozen=True)
class PointPushingCentralizerLayerCommutatorAudit:
    """Split centralizer-layer generator rows by the commutator of <<t>>."""

    group_order: int
    monolith_order: int
    normal_closure_order: int
    normal_closure_commutator_order: int
    generator_order: int
    generator_centralizes_monolith: bool
    normal_closure_centralizes_monolith: bool
    monolith_in_normal_closure: bool
    monolith_in_normal_closure_commutator: bool
    layer_regime: str

    @property
    def proves_centralizer_layer_commutator_split(self) -> bool:
        return self.layer_regime in (
            "abelian_centralizer_layer",
            "centralizer_stem_layer",
        )


@dataclass(frozen=True)
class PointPushingAbelianCentralizerLayerPrimeAudit:
    """Constrain abelian centralizer-layer rows to bounded p-primary layers."""

    normal_generator_order_bound: int
    group_order: int
    monolith_order: int
    monolith_prime: int | None
    normal_closure_order: int
    normal_closure_exponent: int
    generator_order: int
    generator_order_divides_bound: bool
    normal_closure_exponent_divides_generator_order: bool
    normal_closure_exponent_divides_bound: bool
    normal_closure_abelian: bool
    normal_closure_prime_set: Tuple[int, ...]
    monolith_in_normal_closure: bool
    same_prime_as_monolith: bool
    prime_divides_generator_order: bool
    prime_divides_bound: bool
    tail_regime: str

    @property
    def proves_abelian_centralizer_layer_prime_bound(self) -> bool:
        return self.tail_regime == "bounded_p_primary_abelian_centralizer_layer"


@dataclass(frozen=True)
class PointPushingCentralizerStemMultiplierAudit:
    """Audit centralizer-stem rows as stem extensions of N/M."""

    normal_generator_order_bound: int
    group_order: int
    monolith_order: int
    monolith_prime: int | None
    normal_closure_order: int
    normal_closure_commutator_order: int
    quotient_order: int
    quotient_exponent: int
    quotient_is_cyclic: bool
    quotient_generator_internal_normal_closure_order: int
    quotient_generator_internally_normally_generates: bool
    generator_order: int
    generator_image_order: int
    generator_order_divides_bound: bool
    monolith_central_in_normal_closure: bool
    monolith_in_normal_closure_commutator: bool
    monolith_is_elementary_abelian: bool
    quotient_is_stem_target: bool
    quotient_is_noncyclic_stem_target: bool
    quotient_generation_regime: str
    tail_regime: str

    @property
    def proves_centralizer_stem_multiplier_tail(self) -> bool:
        return self.tail_regime == "centralizer_stem_multiplier_tail"


@dataclass(frozen=True)
class PointPushingCentralStemRelationAudit:
    """Bookkeeping for central trivial relation tails as stem extensions."""

    group_order: int
    monolith_order: int
    monolith_prime: int | None
    relation_image_order: int
    quotient_commutator_order: int
    monolith_is_central: bool
    monolith_in_commutator: bool
    relation_image_equals_monolith: bool
    quotient_is_stem: bool

    @property
    def proves_central_stem_relation_tail(self) -> bool:
        return (
            self.monolith_is_central
            and self.monolith_in_commutator
            and self.relation_image_equals_monolith
            and self.quotient_is_stem
        )


@dataclass(frozen=True)
class PointPushingNonabelianChiefRelationQuotientAudit:
    """Bookkeeping for nonabelian-chief relation-group compression."""

    group_order: int
    monolith_order: int
    relation_image_order: int
    monolith_is_normal: bool
    monolith_is_nonabelian: bool
    monolith_is_unique_minimal_normal: bool
    relation_image_is_normal: bool
    relation_image_nontrivial: bool
    relation_image_inside_monolith: bool
    relation_image_equals_monolith: bool

    @property
    def proves_nonabelian_chief_relation_quotient(self) -> bool:
        return (
            self.monolith_is_normal
            and self.monolith_is_nonabelian
            and self.monolith_is_unique_minimal_normal
            and self.relation_image_is_normal
            and self.relation_image_nontrivial
            and self.relation_image_inside_monolith
            and self.relation_image_equals_monolith
        )


@dataclass(frozen=True)
class PointPushingNonabelianWreathCoordinateAudit:
    """Bookkeeping for simple-wreath coordinate relation-lift rows."""

    group_order: int
    monolith_order: int
    simple_factor_order: int
    multiplicity: int
    relation_image_order: int
    centralizer_order: int
    monolith_order_matches_simple_power: bool
    monolith_is_nonabelian: bool
    relation_image_equals_monolith: bool
    centralizer_trivial: bool
    factor_action_transitive: bool
    coordinate_value_nontrivial: bool

    @property
    def proves_simple_wreath_coordinate_shape(self) -> bool:
        return (
            self.monolith_order_matches_simple_power
            and self.monolith_is_nonabelian
            and self.relation_image_equals_monolith
            and self.centralizer_trivial
            and self.factor_action_transitive
            and self.coordinate_value_nontrivial
        )


@dataclass(frozen=True)
class PointPushingBaseFreeBrunnianTailPrefix:
    """Finite symmetric-tail prefix after the explicit base-arity cutoff."""

    base_certificate: PointPushingBaseArityCertificate
    max_symmetric_degree: int
    max_arity: int
    rows: Tuple[PointPushingBrunnianTailCertificateRow, ...]

    @property
    def base_cutoff(self) -> int:
        return self.base_certificate.symmetric_degree_bound

    @property
    def checked_degrees(self) -> Tuple[int, ...]:
        return tuple(row.symmetric_degree for row in self.rows)

    @property
    def detected_degrees(self) -> Tuple[int, ...]:
        return tuple(row.symmetric_degree for row in self.rows if row.prefix_detected)

    @property
    def certified_nonbase_degrees(self) -> Tuple[int, ...]:
        return tuple(
            row.symmetric_degree for row in self.rows if row.has_valid_nonbase_certificate
        )

    @property
    def uncertified_failure_degrees(self) -> Tuple[int, ...]:
        return tuple(
            row.symmetric_degree
            for row in self.rows
            if not row.prefix_detected and not row.has_valid_nonbase_certificate
        )

    @property
    def base_failures_after_cutoff(self) -> Tuple[int, ...]:
        return tuple(
            row.symmetric_degree
            for row in self.rows
            if row.first_failure_kind in ("base_marked_quotient", "truncated_base")
        )

    @property
    def base_cutoff_respected(self) -> bool:
        return not self.base_failures_after_cutoff


@dataclass(frozen=True)
class PointPushingBaseFreeThresholdAudit:
    """Finite-prefix threshold audit after removing the base gate."""

    base_free_prefix: PointPushingBaseFreeBrunnianTailPrefix
    minimal_detecting_degree: int | None

    @property
    def base_cutoff(self) -> int:
        return self.base_free_prefix.base_cutoff

    @property
    def max_symmetric_degree(self) -> int:
        return self.base_free_prefix.max_symmetric_degree

    @property
    def max_arity(self) -> int:
        return self.base_free_prefix.max_arity

    @property
    def checked_degrees(self) -> Tuple[int, ...]:
        return self.base_free_prefix.checked_degrees

    @property
    def detected_within_bound(self) -> bool:
        return self.minimal_detecting_degree is not None

    @property
    def bound_below_base_cutoff(self) -> bool:
        return self.max_symmetric_degree < self.base_cutoff

    @property
    def unresolved_degrees(self) -> Tuple[int, ...]:
        return tuple(
            row.symmetric_degree
            for row in self.base_free_prefix.rows
            if not row.prefix_detected
        )


@dataclass(frozen=True)
class PointPushingBaseFreeThresholdPrefixAudit:
    """Finite prefix of the base-free threshold sequence."""

    max_symmetric_degree: int
    max_arity: int
    rows: Tuple[PointPushingBaseFreeThresholdAudit, ...]

    @property
    def base_cutoff(self) -> int:
        return self.rows[0].base_cutoff if self.rows else 0

    @property
    def threshold_sequence(self) -> Tuple[int | None, ...]:
        return tuple(row.minimal_detecting_degree for row in self.rows)

    @property
    def detected_arities(self) -> Tuple[int, ...]:
        return tuple(
            index + 1
            for index, row in enumerate(self.rows)
            if row.detected_within_bound
        )

    @property
    def unresolved_arities(self) -> Tuple[int, ...]:
        return tuple(
            index + 1
            for index, row in enumerate(self.rows)
            if not row.detected_within_bound
        )

    @property
    def detected_thresholds_weakly_increase(self) -> bool:
        values = [
            value for value in self.threshold_sequence if value is not None
        ]
        return all(left <= right for left, right in zip(values, values[1:]))


@dataclass(frozen=True)
class PointPushingBrunnianNormalizedPrefixAudit:
    """One Brunnian row checked as a symmetric normalized-law prefix."""

    symmetric_degree: int
    arity: int
    extra_strands: int
    certificate: PointPushingBrunnianFailureCertificate
    normalized_prefix: NormalizedLawPrefixWitnessAudit | None

    @property
    def has_valid_brunnian_row(self) -> bool:
        return self.certificate.valid_failure_certificate

    @property
    def proves_one_symmetric_normalized_prefix(self) -> bool:
        return (
            self.has_valid_brunnian_row
            and self.normalized_prefix is not None
            and self.normalized_prefix.proves_one_prefix_normalized_law_witness
        )


@dataclass(frozen=True)
class PointPushingMuPrefixRow:
    """One finite row in a bounded search for ``mu_X(k)``."""

    arity: int
    max_symmetric_degree: int
    minimal_symmetric_degree: int | None
    checked_degrees: Tuple[int, ...]
    truncated_degrees: Tuple[int, ...]
    first_witness_degree: int | None
    witness_word: FreeWord | None
    witness_moved_index: int | None

    @property
    def detected_within_bound(self) -> bool:
        return self.minimal_symmetric_degree is not None

    @property
    def has_vertical_witness_within_bound(self) -> bool:
        return self.first_witness_degree is not None and self.witness_word is not None


@dataclass(frozen=True)
class PointPushingMuPrefixAudit:
    """Bounded finite-prefix audit for the symmetric detector degree ``mu_X``."""

    max_arity: int
    max_symmetric_degree: int
    rows: Tuple[PointPushingMuPrefixRow, ...]

    @property
    def detected_prefix_within_bound(self) -> bool:
        return all(row.detected_within_bound for row in self.rows)

    @property
    def detected_arities(self) -> Tuple[int, ...]:
        return tuple(row.arity for row in self.rows if row.detected_within_bound)

    @property
    def unresolved_arities(self) -> Tuple[int, ...]:
        return tuple(row.arity for row in self.rows if not row.detected_within_bound)


@dataclass(frozen=True)
class PointPushingSuffixShuttleAudit:
    """Check the two-pass suffix shuttle formula for one point-pushing generator."""

    braid_index: int
    generator: int
    tuple_count: int
    matches_direct_action: bool
    first_failure_input: Tuple[object, ...] | None
    first_failure_direct: Tuple[object, ...] | None
    first_failure_shuttle: Tuple[object, ...] | None


@dataclass(frozen=True)
class PointPushingRecursiveConjugacyAudit:
    """Check recursive conjugacy and suffix-shift formulas for point pushing."""

    braid_index: int
    tuple_count: int
    first_generator_recursion_matches: bool
    all_suffix_shift_generators_match: bool
    first_failure_generator: int | None
    first_failure_input: Tuple[object, ...] | None
    first_failure_direct: Tuple[object, ...] | None
    first_failure_recursive: Tuple[object, ...] | None

    @property
    def point_pushing_recursion_verified(self) -> bool:
        return (
            self.first_generator_recursion_matches
            and self.all_suffix_shift_generators_match
        )


@dataclass(frozen=True)
class PointPushingVarietyEscapeAudit:
    """Bounded finite row for a point-pushing action-image variety escape."""

    symmetric_degree: int
    point_pushing_arity: int
    law_arity: int
    braid_index: int
    tuple_count: int
    action_image_size: int | None
    truncated: bool
    assignment_count_checked: int
    separating_word: FreeWord | None
    assignment_representatives: Tuple[FreeWord, ...]
    substituted_point_pushing_word: FreeWord | None
    evaluated_permutation: Permutation | None
    direct_braid_permutation: Permutation | None
    moved_index: int | None
    substituted_word_is_symmetric_law: bool | None

    @property
    def found_variety_escape(self) -> bool:
        return self.separating_word is not None and self.moved_index is not None

    @property
    def direct_matches_evaluated(self) -> bool:
        return (
            self.evaluated_permutation is not None
            and self.direct_braid_permutation is not None
            and self.evaluated_permutation == self.direct_braid_permutation
        )

    @property
    def substituted_word_gives_point_pushing_mover(self) -> bool:
        return (
            self.found_variety_escape
            and self.substituted_word_is_symmetric_law is True
            and self.direct_matches_evaluated
        )


@dataclass(frozen=True)
class PointPushingVarietyPrefixAudit:
    """Bounded prefix scan for one proposed symmetric variety."""

    symmetric_degree: int
    max_point_pushing_arity: int
    law_arity: int
    max_length: int
    rows: Tuple[PointPushingVarietyEscapeAudit, ...]

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def arities_are_initial_segment(self) -> bool:
        return tuple(row.point_pushing_arity for row in self.rows) == tuple(
            range(1, self.row_count + 1)
        )

    @property
    def truncated_rows(self) -> Tuple[PointPushingVarietyEscapeAudit, ...]:
        return tuple(row for row in self.rows if row.truncated)

    @property
    def escape_rows(self) -> Tuple[PointPushingVarietyEscapeAudit, ...]:
        return tuple(row for row in self.rows if row.found_variety_escape)

    @property
    def escaped_arities(self) -> Tuple[int, ...]:
        return tuple(row.point_pushing_arity for row in self.escape_rows)

    @property
    def all_escape_rows_give_movers(self) -> bool:
        return all(row.substituted_word_gives_point_pushing_mover for row in self.escape_rows)

    @property
    def no_bounded_escape_found(self) -> bool:
        return not self.escape_rows and not self.truncated_rows


@dataclass(frozen=True)
class PointPushingExponentEscapeAudit:
    """One finite row where a power law moves a point-pushing action image."""

    law_bound: int
    point_pushing_arity: int
    exponent_bound: int
    braid_index: int
    tuple_count: int
    action_image_size: int | None
    truncated: bool
    escaping_element_order: int | None
    escaping_element_word: FreeWord | None
    exponent_law_word: FreeWord | None
    evaluated_permutation: Permutation | None
    direct_braid_permutation: Permutation | None
    symmetric_identity_longitude_signature: bool | None
    moved_index: int | None

    @property
    def found_exponent_escape(self) -> bool:
        return self.escaping_element_word is not None and self.moved_index is not None

    @property
    def direct_matches_evaluated(self) -> bool:
        return (
            self.evaluated_permutation is not None
            and self.direct_braid_permutation is not None
            and self.evaluated_permutation == self.direct_braid_permutation
        )

    @property
    def gives_power_law_mover(self) -> bool:
        return self.found_exponent_escape and self.direct_matches_evaluated

    @property
    def exposes_naive_law_gap(self) -> bool:
        return self.gives_power_law_mover and self.symmetric_identity_longitude_signature is False


def identity_permutation(size: int) -> Permutation:
    return tuple(range(size))


def compose_permutations(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    if len(left) != len(right):
        raise ValueError("permutations must have the same size")
    return tuple(left[right[i]] for i in range(len(left)))


def invert_permutation(permutation: Permutation) -> Permutation:
    out = [0] * len(permutation)
    for i, image in enumerate(permutation):
        out[image] = i
    return tuple(out)


def generated_permutation_subgroup(generators: Iterable[Permutation], max_size: int | None = None):
    gens = tuple(generators)
    if not gens:
        return {tuple()}
    size = len(gens[0])
    identity = identity_permutation(size)
    symmetric_gens = set(gens)
    symmetric_gens.update(invert_permutation(gen) for gen in gens)
    subgroup = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for gen in symmetric_gens:
            candidate = compose_permutations(gen, current)
            if candidate in subgroup:
                continue
            subgroup.add(candidate)
            if max_size is not None and len(subgroup) > max_size:
                raise ValueError("generated subgroup exceeded max_size")
            queue.append(candidate)
    return subgroup


def generated_permutation_subgroup_with_words(
    generators: Mapping[int, Permutation],
    max_size: int | None = None,
) -> dict[Permutation, FreeWord]:
    """Generate a permutation subgroup and remember words in the generators."""

    gens = tuple(sorted(generators.items()))
    if not gens:
        return {tuple(): tuple()}
    size = len(gens[0][1])
    identity = identity_permutation(size)
    moves = []
    for index, generator in gens:
        moves.append((generator, ((index, 1),)))
        moves.append((invert_permutation(generator), ((index, -1),)))
    words: dict[Permutation, FreeWord] = {identity: tuple()}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        current_word = words[current]
        for move, move_word in moves:
            candidate = compose_permutations(move, current)
            if candidate in words:
                continue
            candidate_word = _reduce_free_word(current_word + move_word)
            words[candidate] = candidate_word
            if max_size is not None and len(words) > max_size:
                raise ValueError("generated subgroup exceeded max_size")
            queue.append(candidate)
    return words


def _generated_pair_subgroup_with_words(
    generators: Mapping[int, Tuple[Permutation, Permutation]],
    max_size: int | None = None,
) -> dict[Tuple[Permutation, Permutation], FreeWord]:
    """Generate a subgroup of a direct product and remember generator words."""

    gens = tuple(sorted(generators.items()))
    if not gens:
        return {(tuple(), tuple()): tuple()}
    detector_size = len(gens[0][1][0])
    action_size = len(gens[0][1][1])
    identity_pair = (
        identity_permutation(detector_size),
        identity_permutation(action_size),
    )
    moves = []
    for index, (detector, action) in gens:
        moves.append((detector, action, ((index, 1),)))
        moves.append(
            (
                invert_permutation(detector),
                invert_permutation(action),
                ((index, -1),),
            )
        )
    words: dict[Tuple[Permutation, Permutation], FreeWord] = {identity_pair: tuple()}
    queue = deque([identity_pair])
    while queue:
        current = queue.popleft()
        current_word = words[current]
        for detector_move, action_move, move_word in moves:
            candidate = (
                compose_permutations(detector_move, current[0]),
                compose_permutations(action_move, current[1]),
            )
            if candidate in words:
                continue
            candidate_word = _reduce_free_word(current_word + move_word)
            words[candidate] = candidate_word
            if max_size is not None and len(words) > max_size:
                raise ValueError("generated pair subgroup exceeded max_size")
            queue.append(candidate)
    return words


def permutation_group_from_subgroup(subgroup: Iterable[Permutation]):
    """View a finite permutation subgroup as a `FiniteGroup`."""

    from .finite_group import FiniteGroup

    elements = tuple(sorted(subgroup))
    if not elements:
        return FiniteGroup((tuple(),), tuple(), {(tuple(), tuple()): tuple()})
    identity = identity_permutation(len(elements[0]))
    table = {
        (left, right): compose_permutations(left, right)
        for left in elements
        for right in elements
    }
    return FiniteGroup(elements, identity, table)


def point_pushing_action_group(
    solution: FiniteBraidedSet,
    arity: int,
    *,
    max_size: int | None = None,
) -> FiniteGroup:
    """Return the finite marked action image ``P_k(X)`` as a group."""

    if arity < 1:
        raise ValueError("arity must be positive")
    action_images = _point_pushing_action_generator_images(solution, arity)
    subgroup = generated_permutation_subgroup(
        action_images.values(),
        max_size=max_size,
    )
    return permutation_group_from_subgroup(subgroup)


def _point_pushing_action_generator_images(
    solution: FiniteBraidedSet,
    arity: int,
) -> Mapping[int, Permutation]:
    """Return marked generator images for ``P_k(X)``."""

    from .braid_laws import pure_braid_generator

    if arity < 1:
        raise ValueError("arity must be positive")
    braid_index = arity + 1
    action_braids = {
        generator: pure_braid_generator(generator + 1, braid_index)
        for generator in range(arity)
    }
    return braid_images_for_words(solution, braid_index, action_braids)


def evaluate_free_word_on_permutations(
    word: FreeWord, generator_images: Mapping[int, Permutation]
) -> Permutation:
    if not generator_images:
        if word:
            raise ValueError("missing generator images")
        return tuple()
    size = len(next(iter(generator_images.values())))
    out = identity_permutation(size)
    for generator, exponent in word:
        image = generator_images[generator]
        if exponent < 0:
            image = invert_permutation(image)
        out = compose_permutations(image, out)
    return out


def _reduce_free_word(word: FreeWord) -> FreeWord:
    from .artin_longitudes import reduce_free_word

    return reduce_free_word(word)


def _invert_free_word(word: FreeWord) -> FreeWord:
    from .artin_longitudes import invert_free_word

    return invert_free_word(word)


def substitute_free_word(word: FreeWord, substitutions: Sequence[FreeWord]) -> FreeWord:
    """Substitute words in ``F_k`` for variables of another free word."""

    out: FreeWord = tuple()
    for generator, exponent in word:
        replacement = substitutions[generator]
        if exponent < 0:
            replacement = _invert_free_word(replacement)
        out = _reduce_free_word(out + replacement)
    return out


def short_law_separating_permutation_assignment(
    law_groups: Sequence[FiniteGroup],
    generator_images: Mapping[int, Permutation],
    *,
    max_length: int,
) -> AssignedLawSeparation:
    """Find a short finite-group law that moves a fixed permutation tuple.

    This is the assigned-generator form needed by normalized-law obstruction
    searches.  It is stronger than merely finding a word that is not a law on
    the subgroup generated by ``generator_images``: the returned word is
    certified to evaluate nontrivially on this particular tuple.
    """

    from .group_laws import is_law_on_group, reduced_free_words

    if not generator_images:
        return AssignedLawSeparation(
            arity=0,
            target_degree=0,
            separating_word=None,
            evaluated_permutation=None,
            moved_index=None,
        )
    arity = 1 + max(generator_images)
    target_degree = len(next(iter(generator_images.values())))
    identity = identity_permutation(target_degree)
    for word in reduced_free_words(arity, max_length):
        if not all(is_law_on_group(group, word, arity=arity) for group in law_groups):
            continue
        evaluated = evaluate_free_word_on_permutations(word, generator_images)
        if evaluated == identity:
            continue
        moved_index = next(
            index
            for index, image in enumerate(evaluated)
            if image != index
        )
        return AssignedLawSeparation(
            arity=arity,
            target_degree=target_degree,
            separating_word=word,
            evaluated_permutation=evaluated,
            moved_index=moved_index,
        )
    return AssignedLawSeparation(
        arity=arity,
        target_degree=target_degree,
        separating_word=None,
        evaluated_permutation=None,
        moved_index=None,
    )


def point_pushing_marked_quotient_audit(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingMarkedQuotientAudit:
    """Audit whether the YBE point-pushing image is a marked detector quotient.

    The audit generates the paired subgroup
    ``<(d_i,h_i)> <= D_k(G) x P_k(X)``.  A pair ``(1, nonidentity)`` is exactly
    a point-pushing word lying in ``K_G`` whose action on ``X`` is nontrivial.
    """

    from .braid_laws import (
        point_pushing_derivative_detector_generators,
        pure_braid_generator,
    )

    if arity < 1:
        raise ValueError("arity must be positive")
    n = arity + 1
    detector_images = point_pushing_derivative_detector_generators(
        group,
        arity,
        max_states=max_detector_states,
    )
    action_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(arity)
    }
    action_images = braid_images_for_words(solution, n, action_braids)
    detector_identity = identity_permutation(
        len(next(iter(detector_images.values())))
    )
    action_identity = identity_permutation(
        len(next(iter(action_images.values())))
    )
    moves = []
    for generator in range(arity):
        detector = detector_images[generator]
        action = action_images[generator]
        moves.append((detector, action, ((generator, 1),)))
        moves.append(
            (
                invert_permutation(detector),
                invert_permutation(action),
                ((generator, -1),),
            )
        )
    identity_pair = (detector_identity, action_identity)
    words: dict[Tuple[Permutation, Permutation], FreeWord] = {identity_pair: tuple()}
    queue = deque([identity_pair])
    truncated = False
    witness_word: FreeWord | None = None
    witness_action: Permutation | None = None
    moved_index: int | None = None
    while queue:
        current = queue.popleft()
        current_word = words[current]
        for detector_move, action_move, move_word in moves:
            candidate = (
                compose_permutations(detector_move, current[0]),
                compose_permutations(action_move, current[1]),
            )
            if candidate in words:
                continue
            candidate_word = _reduce_free_word(current_word + move_word)
            if candidate[0] == detector_identity and candidate[1] != action_identity:
                witness_word = candidate_word
                witness_action = candidate[1]
                moved_index = next(
                    index
                    for index, image in enumerate(candidate[1])
                    if image != index
                )
                words[candidate] = candidate_word
                queue.clear()
                break
            words[candidate] = candidate_word
            if (
                max_pair_subgroup_size is not None
                and len(words) > max_pair_subgroup_size
            ):
                truncated = True
                queue.clear()
                break
            queue.append(candidate)
    detector_projection = {pair[0] for pair in words}
    action_projection = {pair[1] for pair in words}
    return PointPushingMarkedQuotientAudit(
        group_order=len(group.elements),
        arity=arity,
        braid_index=n,
        detector_state_count=len(detector_identity),
        ybe_tuple_count=len(action_identity),
        pair_subgroup_size=None if truncated else len(words),
        detector_image_size=None if truncated else len(detector_projection),
        action_image_size=None if truncated else len(action_projection),
        truncated=truncated,
        witness_word=witness_word,
        witness_action_value=witness_action,
        moved_index=moved_index,
    )


def point_pushing_vertical_witness_certificate(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    word: FreeWord,
    arity: int,
    *,
    max_detector_states: int | None = None,
) -> PointPushingVerticalWitnessCertificate:
    """Check one paired vertical-kernel witness.

    A valid certificate means the point-pushed braid is in ``K_G`` by the
    derivative detector criterion and still acts nontrivially on ``X``.
    """

    from .braid_laws import (
        law_word_on_last_strand,
        point_pushing_derivative_detector_generators,
        pure_braid_generator,
    )

    if arity < 1:
        raise ValueError("arity must be positive")
    for generator, _exponent in word:
        if generator < 0 or generator >= arity:
            raise ValueError(f"free generator {generator} outside arity {arity}")

    n, braid = law_word_on_last_strand(word, arity)
    detector_images = point_pushing_derivative_detector_generators(
        group,
        arity,
        max_states=max_detector_states,
    )
    detector_value = evaluate_free_word_on_permutations(word, detector_images)
    detector_identity = identity_permutation(len(detector_value))

    action_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(arity)
    }
    action_images = braid_images_for_words(solution, n, action_braids)
    evaluated_action = evaluate_free_word_on_permutations(word, action_images)
    direct_action = action_permutation(solution, n, braid)
    action_identity = identity_permutation(len(direct_action))

    moved_index = None
    moved_tuple = None
    moved_tuple_image = None
    if direct_action != action_identity:
        moved_index = next(
            index for index, image in enumerate(direct_action) if image != index
        )
        tuples = tuple(product(solution.elements, repeat=n))
        moved_tuple = tuples[moved_index]
        moved_tuple_image = tuples[direct_action[moved_index]]

    return PointPushingVerticalWitnessCertificate(
        group_order=len(group.elements),
        arity=arity,
        braid_index=n,
        detector_state_count=len(detector_identity),
        ybe_tuple_count=len(action_identity),
        word=tuple(word),
        braid_word=braid,
        detector_word_identity=detector_value == detector_identity,
        evaluated_action_identity=evaluated_action == action_identity,
        direct_braid_identity=direct_action == action_identity,
        direct_matches_evaluated=direct_action == evaluated_action,
        moved_index=moved_index,
        moved_tuple=moved_tuple,
        moved_tuple_image=moved_tuple_image,
    )


def right_based_point_pushing_word_to_left(word: FreeWord, arity: int) -> FreeWord:
    """Convert right-based point-pushing coordinates to left-based coordinates.

    In right-based arity ``k``, generator ``a_1`` is nearest the moving last
    strand and ``a_k`` is farthest.  The existing point-pushing helpers use
    left-based coordinates, where generator ``0`` is ``A_{1,k+1}``.
    """

    if arity < 1:
        raise ValueError("arity must be positive")
    converted = []
    for generator, exponent in word:
        if generator < 0 or generator >= arity:
            raise ValueError(f"free generator {generator} outside arity {arity}")
        converted.append((arity - 1 - generator, exponent))
    return _reduce_free_word(tuple(converted))


def delete_right_based_new_strand_word(word: FreeWord, arity: int) -> FreeWord:
    """Delete the newly added far-left stationary strand in right-based form.

    Passing from arity ``k-1`` to arity ``k`` adds the farthest generator
    ``a_k``.  The deletion retraction kills that generator and fixes the old
    suffix generators ``a_1,...,a_{k-1}``.
    """

    if arity < 1:
        raise ValueError("arity must be positive")
    kept = []
    for generator, exponent in word:
        if generator < 0 or generator >= arity:
            raise ValueError(f"free generator {generator} outside arity {arity}")
        if generator == arity - 1:
            continue
        kept.append((generator, exponent))
    return _reduce_free_word(tuple(kept))


def point_pushing_brunnian_witness_certificate(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    right_based_word: FreeWord,
    arity: int,
    *,
    max_detector_states: int | None = None,
) -> PointPushingBrunnianWitnessCertificate:
    """Check a right-based one-new-strand Brunnian vertical witness.

    A valid certificate means the word is killed by deleting the newly added
    far-left stationary strand, is invisible to the derivative detector for
    ``group``, and still moves the YBE action.
    """

    left_word = right_based_point_pushing_word_to_left(right_based_word, arity)
    deletion_word = delete_right_based_new_strand_word(right_based_word, arity)
    vertical = point_pushing_vertical_witness_certificate(
        solution,
        group,
        left_word,
        arity,
        max_detector_states=max_detector_states,
    )
    return PointPushingBrunnianWitnessCertificate(
        arity=arity,
        right_based_word=tuple(right_based_word),
        left_based_word=left_word,
        deletion_word=deletion_word,
        deletion_trivial=deletion_word == tuple(),
        vertical=vertical,
    )


def _evaluate_free_word_on_pair_images(
    word: FreeWord,
    pair_images: Mapping[int, Tuple[Permutation, Permutation]],
) -> Tuple[Permutation, Permutation]:
    detector_images = {index: pair[0] for index, pair in pair_images.items()}
    action_images = {index: pair[1] for index, pair in pair_images.items()}
    return (
        evaluate_free_word_on_permutations(word, detector_images),
        evaluate_free_word_on_permutations(word, action_images),
    )


def point_pushing_brunnian_orbit_audit(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    arity: int,
    *,
    max_detector_states: int | None = None,
    max_old_pair_subgroup_size: int | None = None,
    max_relative_subgroup_size: int | None = None,
) -> PointPushingBrunnianOrbitAudit:
    """Audit the relative Brunnian normal closure at one point-pushing arity.

    Coordinates are right-based: the old suffix generators are
    ``a_1,...,a_{k-1}`` and the newly added far-left generator is ``a_k``.
    """

    from .braid_laws import (
        point_pushing_derivative_detector_generators,
        pure_braid_generator,
    )

    if arity < 1:
        raise ValueError("arity must be positive")

    n = arity + 1
    detector_left = point_pushing_derivative_detector_generators(
        group,
        arity,
        max_states=max_detector_states,
    )
    action_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(arity)
    }
    action_left = braid_images_for_words(solution, n, action_braids)
    detector_identity = identity_permutation(
        len(next(iter(detector_left.values())))
    )
    action_identity = identity_permutation(len(next(iter(action_left.values()))))

    pair_right = {
        right_generator: (
            detector_left[arity - 1 - right_generator],
            action_left[arity - 1 - right_generator],
        )
        for right_generator in range(arity)
    }
    new_generator = arity - 1
    old_pair_generators = {
        generator: pair_right[generator] for generator in range(arity - 1)
    }
    try:
        old_words = _generated_pair_subgroup_with_words(
            old_pair_generators,
            max_size=max_old_pair_subgroup_size,
        )
    except ValueError as exc:
        if "exceeded max_size" not in str(exc):
            raise
        return PointPushingBrunnianOrbitAudit(
            group_order=len(group.elements),
            arity=arity,
            braid_index=n,
            detector_state_count=len(detector_identity),
            ybe_tuple_count=len(action_identity),
            old_pair_subgroup_size=None,
            conjugate_generator_count=None,
            detector_stabilizer_size=None,
            stabilizer_centralizes_new_action=None,
            detector_orbit_size=None,
            action_orbit_size=None,
            orbit_map_well_defined=None,
            relative_detector_projection_size=None,
            relative_action_projection_size=None,
            relative_subgroup_size=None,
            failure_kind="truncated_old_suffix",
            truncated=True,
            witness_right_word=None,
            witness_left_word=None,
            witness_action_value=None,
            moved_index=None,
        )

    conjugate_pairs: dict[FreeWord, Tuple[Permutation, Permutation]] = {}
    detector_orbit_words: dict[Permutation, FreeWord] = {}
    detector_orbit_actions: dict[Permutation, Permutation] = {}
    action_orbit: set[Permutation] = set()
    new_detector, new_action = pair_right[new_generator]
    detector_stabilizer_size = 0
    for old_word in old_words.values():
        old_detector, old_action = _evaluate_free_word_on_pair_images(
            old_word,
            pair_right,
        )
        old_detector_inverse = invert_permutation(old_detector)
        old_action_inverse = invert_permutation(old_action)
        old_detector_conjugate = compose_permutations(
            compose_permutations(old_detector, new_detector),
            old_detector_inverse,
        )
        if old_detector_conjugate == new_detector:
            detector_stabilizer_size += 1
            old_action_conjugate = compose_permutations(
                compose_permutations(old_action, new_action),
                old_action_inverse,
            )
            if old_action_conjugate != new_action:
                witness_right_word = _reduce_free_word(
                    old_word
                    + ((new_generator, 1),)
                    + _invert_free_word(old_word)
                    + ((new_generator, -1),)
                )
                witness_pair = _evaluate_free_word_on_pair_images(
                    witness_right_word,
                    pair_right,
                )
                moved_index = next(
                    index
                    for index, image in enumerate(witness_pair[1])
                    if image != index
                )
                return PointPushingBrunnianOrbitAudit(
                    group_order=len(group.elements),
                    arity=arity,
                    braid_index=n,
                    detector_state_count=len(detector_identity),
                    ybe_tuple_count=len(action_identity),
                    old_pair_subgroup_size=len(old_words),
                    conjugate_generator_count=len(conjugate_pairs),
                    detector_stabilizer_size=detector_stabilizer_size,
                    stabilizer_centralizes_new_action=False,
                    detector_orbit_size=len(detector_orbit_actions),
                    action_orbit_size=len(action_orbit),
                    orbit_map_well_defined=False,
                    relative_detector_projection_size=None,
                    relative_action_projection_size=None,
                    relative_subgroup_size=None,
                    failure_kind="stabilizer",
                    truncated=False,
                    witness_right_word=witness_right_word,
                    witness_left_word=right_based_point_pushing_word_to_left(
                        witness_right_word,
                        arity,
                    ),
                    witness_action_value=witness_pair[1],
                    moved_index=moved_index,
                )
        conjugate_word = _reduce_free_word(
            old_word + ((new_generator, 1),) + _invert_free_word(old_word)
        )
        conjugate_pair = _evaluate_free_word_on_pair_images(
            conjugate_word,
            pair_right,
        )
        detector_conjugate, action_conjugate = conjugate_pair
        action_orbit.add(action_conjugate)
        previous_action = detector_orbit_actions.get(detector_conjugate)
        if previous_action is not None and previous_action != action_conjugate:
            previous_word = detector_orbit_words[detector_conjugate]
            witness_right_word = _reduce_free_word(
                conjugate_word + _invert_free_word(previous_word)
            )
            witness_pair = _evaluate_free_word_on_pair_images(
                witness_right_word,
                pair_right,
            )
            moved_index = next(
                index
                for index, image in enumerate(witness_pair[1])
                if image != index
            )
            return PointPushingBrunnianOrbitAudit(
                group_order=len(group.elements),
                arity=arity,
                braid_index=n,
                detector_state_count=len(detector_identity),
                ybe_tuple_count=len(action_identity),
                old_pair_subgroup_size=len(old_words),
                conjugate_generator_count=len(conjugate_pairs),
                detector_stabilizer_size=detector_stabilizer_size,
                stabilizer_centralizes_new_action=True,
                detector_orbit_size=len(detector_orbit_actions),
                action_orbit_size=len(action_orbit),
                orbit_map_well_defined=False,
                relative_detector_projection_size=None,
                relative_action_projection_size=None,
                relative_subgroup_size=None,
                failure_kind="orbit_label",
                truncated=False,
                witness_right_word=witness_right_word,
                witness_left_word=right_based_point_pushing_word_to_left(
                    witness_right_word,
                    arity,
                ),
                witness_action_value=witness_pair[1],
                moved_index=moved_index,
            )
        if previous_action is None:
            detector_orbit_words[detector_conjugate] = conjugate_word
            detector_orbit_actions[detector_conjugate] = action_conjugate
        conjugate_pairs[conjugate_word] = conjugate_pair

    moves = []
    for conjugate_word, (detector, action) in conjugate_pairs.items():
        moves.append((detector, action, conjugate_word))
        moves.append(
            (
                invert_permutation(detector),
                invert_permutation(action),
                _invert_free_word(conjugate_word),
            )
        )

    identity_pair = (detector_identity, action_identity)
    words: dict[Tuple[Permutation, Permutation], FreeWord] = {identity_pair: tuple()}
    queue = deque([identity_pair])
    truncated = False
    witness_right_word: FreeWord | None = None
    witness_action: Permutation | None = None
    moved_index: int | None = None
    while queue:
        current = queue.popleft()
        current_word = words[current]
        for detector_move, action_move, move_word in moves:
            candidate = (
                compose_permutations(detector_move, current[0]),
                compose_permutations(action_move, current[1]),
            )
            if candidate in words:
                continue
            candidate_word = _reduce_free_word(current_word + move_word)
            if candidate[0] == detector_identity and candidate[1] != action_identity:
                witness_right_word = candidate_word
                witness_action = candidate[1]
                moved_index = next(
                    index
                    for index, image in enumerate(candidate[1])
                    if image != index
                )
                words[candidate] = candidate_word
                queue.clear()
                break
            words[candidate] = candidate_word
            if (
                max_relative_subgroup_size is not None
                and len(words) > max_relative_subgroup_size
            ):
                truncated = True
                queue.clear()
                break
            queue.append(candidate)

    witness_left_word = (
        None
        if witness_right_word is None
        else right_based_point_pushing_word_to_left(witness_right_word, arity)
    )
    relative_detector_projection = {pair[0] for pair in words}
    relative_action_projection = {pair[1] for pair in words}
    failure_kind = "none"
    if truncated:
        failure_kind = "truncated_relative"
    elif witness_right_word is not None:
        failure_kind = "orbit_relation"
    return PointPushingBrunnianOrbitAudit(
        group_order=len(group.elements),
        arity=arity,
        braid_index=n,
        detector_state_count=len(detector_identity),
        ybe_tuple_count=len(action_identity),
        old_pair_subgroup_size=len(old_words),
        conjugate_generator_count=len(conjugate_pairs),
        detector_stabilizer_size=detector_stabilizer_size,
        stabilizer_centralizes_new_action=True,
        detector_orbit_size=len(detector_orbit_actions),
        action_orbit_size=len(action_orbit),
        orbit_map_well_defined=True,
        relative_detector_projection_size=(
            None if truncated else len(relative_detector_projection)
        ),
        relative_action_projection_size=(
            None if truncated else len(relative_action_projection)
        ),
        relative_subgroup_size=None if truncated else len(words),
        failure_kind=failure_kind,
        truncated=truncated,
        witness_right_word=witness_right_word,
        witness_left_word=witness_left_word,
        witness_action_value=witness_action,
        moved_index=moved_index,
    )


def point_pushing_mu_prefix_audit(
    solution: FiniteBraidedSet,
    max_arity: int,
    max_symmetric_degree: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingMuPrefixAudit:
    """Bounded finite-prefix audit for the growth sequence ``mu_X(k)``.

    This is a finite diagnostic only.  A positive proof needs a symbolic bound
    independent of ``k``; a negative proof needs an infinite tail of witnesses.
    """

    from .finite_group import symmetric_group

    if max_arity < 1:
        raise ValueError("max_arity must be positive")
    if max_symmetric_degree < 1:
        raise ValueError("max_symmetric_degree must be positive")

    rows = []
    for arity in range(1, max_arity + 1):
        checked = []
        truncated = []
        minimal_degree = None
        first_witness_degree = None
        witness_word = None
        witness_moved_index = None
        for degree in range(1, max_symmetric_degree + 1):
            try:
                row = point_pushing_marked_quotient_audit(
                    solution,
                    symmetric_group(degree),
                    arity,
                    max_detector_states=max_detector_states,
                    max_pair_subgroup_size=max_pair_subgroup_size,
                )
            except ValueError as exc:
                if "exceeded max_states" not in str(exc):
                    raise
                truncated.append(degree)
                continue
            checked.append(degree)
            if row.truncated:
                truncated.append(degree)
                continue
            if row.marked_quotient_holds:
                minimal_degree = degree
                break
            if first_witness_degree is None and row.found_kernel_mover:
                first_witness_degree = degree
                witness_word = row.witness_word
                witness_moved_index = row.moved_index
        rows.append(
            PointPushingMuPrefixRow(
                arity=arity,
                max_symmetric_degree=max_symmetric_degree,
                minimal_symmetric_degree=minimal_degree,
                checked_degrees=tuple(checked),
                truncated_degrees=tuple(truncated),
                first_witness_degree=first_witness_degree,
                witness_word=witness_word,
                witness_moved_index=witness_moved_index,
            )
        )
    return PointPushingMuPrefixAudit(
        max_arity=max_arity,
        max_symmetric_degree=max_symmetric_degree,
        rows=tuple(rows),
    )


def point_pushing_brunnian_gate_prefix_audit(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    max_arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingBrunnianGatePrefixAudit:
    """Sequential finite-prefix audit for the Brunnian gate induction.

    A successful row means arity ``1`` satisfies the marked quotient criterion
    and each extension arity has ``failure_kind == "none"``.
    """

    if max_arity < 1:
        raise ValueError("max_arity must be positive")

    base_audit = point_pushing_marked_quotient_audit(
        solution,
        group,
        arity=1,
        max_detector_states=max_detector_states,
        max_pair_subgroup_size=max_pair_subgroup_size,
    )
    if base_audit.truncated:
        return PointPushingBrunnianGatePrefixAudit(
            group_order=len(group.elements),
            max_arity=max_arity,
            base_audit=base_audit,
            extension_rows=tuple(),
            first_failure_arity=1,
            first_failure_kind="truncated_base",
        )
    if not base_audit.marked_quotient_holds:
        return PointPushingBrunnianGatePrefixAudit(
            group_order=len(group.elements),
            max_arity=max_arity,
            base_audit=base_audit,
            extension_rows=tuple(),
            first_failure_arity=1,
            first_failure_kind="base_marked_quotient",
        )

    rows = []
    for arity in range(2, max_arity + 1):
        row = point_pushing_brunnian_orbit_audit(
            solution,
            group,
            arity=arity,
            max_detector_states=max_detector_states,
            max_old_pair_subgroup_size=max_pair_subgroup_size,
            max_relative_subgroup_size=max_pair_subgroup_size,
        )
        rows.append(row)
        if row.truncated:
            return PointPushingBrunnianGatePrefixAudit(
                group_order=len(group.elements),
                max_arity=max_arity,
                base_audit=base_audit,
                extension_rows=tuple(rows),
                first_failure_arity=arity,
                first_failure_kind=row.failure_kind,
            )
        if row.failure_kind != "none":
            return PointPushingBrunnianGatePrefixAudit(
                group_order=len(group.elements),
                max_arity=max_arity,
                base_audit=base_audit,
                extension_rows=tuple(rows),
                first_failure_arity=arity,
                first_failure_kind=row.failure_kind,
            )

    return PointPushingBrunnianGatePrefixAudit(
        group_order=len(group.elements),
        max_arity=max_arity,
        base_audit=base_audit,
        extension_rows=tuple(rows),
        first_failure_arity=None,
        first_failure_kind=None,
    )


def point_pushing_brunnian_tail_prefix_audit(
    solution: FiniteBraidedSet,
    max_symmetric_degree: int,
    max_arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingBrunnianTailPrefixAudit:
    """Finite diagnostic for symmetric first-failure gate rows."""

    from .finite_group import symmetric_group

    if max_symmetric_degree < 1:
        raise ValueError("max_symmetric_degree must be positive")
    if max_arity < 1:
        raise ValueError("max_arity must be positive")

    rows = []
    for degree in range(1, max_symmetric_degree + 1):
        audit = point_pushing_brunnian_gate_prefix_audit(
            solution,
            symmetric_group(degree),
            max_arity=max_arity,
            max_detector_states=max_detector_states,
            max_pair_subgroup_size=max_pair_subgroup_size,
        )
        rows.append(
            PointPushingBrunnianTailRow(
                symmetric_degree=degree,
                max_arity=max_arity,
                prefix_detected=audit.prefix_detected,
                first_failure_arity=audit.first_failure_arity,
                first_failure_kind=audit.first_failure_kind,
            )
        )
    return PointPushingBrunnianTailPrefixAudit(
        max_symmetric_degree=max_symmetric_degree,
        max_arity=max_arity,
        rows=tuple(rows),
    )


def point_pushing_base_arity_certificate(
    solution: FiniteBraidedSet,
) -> PointPushingBaseArityCertificate:
    """Return an explicit symmetric detector bound for arity ``1``."""

    from .group_laws import lcm_upto

    pure_action = action_permutation(solution, 2, (1, 1))
    pure_order = permutation_order(pure_action)
    symmetric_degree = 1
    while lcm_upto(symmetric_degree) % pure_order != 0:
        symmetric_degree += 1
    symmetric_exponent = lcm_upto(symmetric_degree)
    return PointPushingBaseArityCertificate(
        tuple_count=len(pure_action),
        pure_generator_order=pure_order,
        symmetric_degree_bound=symmetric_degree,
        symmetric_exponent=symmetric_exponent,
        symmetric_marked_quotient_holds=symmetric_exponent % pure_order == 0,
    )


def point_pushing_cyclic_tail_bound_audit(
    solution: FiniteBraidedSet,
    *,
    max_braid_index: int = 5,
) -> PointPushingCyclicTailBoundAudit:
    """Record the uniform order bound for cyclic point-pushing quotients."""

    if max_braid_index < 2:
        raise ValueError("max_braid_index must be at least 2")
    pure_action = action_permutation(solution, 2, (1, 1))
    bound = permutation_order(pure_action)
    rows = pure_generator_order_profile(solution, max_braid_index)
    divides = all(
        bound % order == 0
        for row in rows
        for order in row.generator_orders
    )
    return PointPushingCyclicTailBoundAudit(
        tuple_count=len(pure_action),
        cyclic_quotient_order_bound=bound,
        max_braid_index_checked=max_braid_index,
        rows=rows,
        checked_generator_orders_divide_bound=divides,
    )


def point_pushing_bounded_normal_generator_audit(
    solution: FiniteBraidedSet,
    *,
    max_braid_index: int = 5,
) -> PointPushingBoundedNormalGeneratorAudit:
    """Record the bounded-order normal-generator constraint."""

    if max_braid_index < 2:
        raise ValueError("max_braid_index must be at least 2")
    pure_action = action_permutation(solution, 2, (1, 1))
    bound = permutation_order(pure_action)
    rows = pure_generator_order_profile(solution, max_braid_index)
    divides = all(
        bound % order == 0
        for row in rows
        for order in row.generator_orders
    )
    return PointPushingBoundedNormalGeneratorAudit(
        tuple_count=len(pure_action),
        normal_generator_order_bound=bound,
        max_braid_index_checked=max_braid_index,
        rows=rows,
        checked_generator_orders_divide_bound=divides,
    )


def point_pushing_brunnian_failure_certificate(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingBrunnianFailureCertificate:
    """Return a braid-level certificate for one Brunnian gate failure."""

    audit = point_pushing_brunnian_orbit_audit(
        solution,
        group,
        arity=arity,
        max_detector_states=max_detector_states,
        max_old_pair_subgroup_size=max_pair_subgroup_size,
        max_relative_subgroup_size=max_pair_subgroup_size,
    )
    witness = None
    if audit.witness_right_word is not None:
        witness = point_pushing_brunnian_witness_certificate(
            solution,
            group,
            audit.witness_right_word,
            arity,
            max_detector_states=max_detector_states,
        )
    return PointPushingBrunnianFailureCertificate(
        group_order=len(group.elements),
        arity=arity,
        failure_kind=audit.failure_kind,
        orbit_audit=audit,
        witness=witness,
    )


def point_pushing_brunnian_tail_certificate_prefix(
    solution: FiniteBraidedSet,
    max_symmetric_degree: int,
    max_arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingBrunnianTailCertificatePrefix:
    """Check a finite symmetric-tail prefix and certify real non-base failures."""

    from .finite_group import symmetric_group

    if max_symmetric_degree < 1:
        raise ValueError("max_symmetric_degree must be positive")
    if max_arity < 1:
        raise ValueError("max_arity must be positive")

    rows = []
    for degree in range(1, max_symmetric_degree + 1):
        group = symmetric_group(degree)
        audit = point_pushing_brunnian_gate_prefix_audit(
            solution,
            group,
            max_arity=max_arity,
            max_detector_states=max_detector_states,
            max_pair_subgroup_size=max_pair_subgroup_size,
        )
        certificate = None
        if audit.first_failure_kind in ("stabilizer", "orbit_label", "orbit_relation"):
            if audit.first_failure_arity is None:
                raise AssertionError("non-base failure kind without failure arity")
            certificate = point_pushing_brunnian_failure_certificate(
                solution,
                group,
                audit.first_failure_arity,
                max_detector_states=max_detector_states,
                max_pair_subgroup_size=max_pair_subgroup_size,
            )
        rows.append(
            PointPushingBrunnianTailCertificateRow(
                symmetric_degree=degree,
                max_arity=max_arity,
                prefix_detected=audit.prefix_detected,
                first_failure_arity=audit.first_failure_arity,
                first_failure_kind=audit.first_failure_kind,
                certificate=certificate,
            )
        )
    return PointPushingBrunnianTailCertificatePrefix(
        max_symmetric_degree=max_symmetric_degree,
        max_arity=max_arity,
        rows=tuple(rows),
    )


def point_pushing_product_prefix_first_failure_audit(
    solution: FiniteBraidedSet,
    groups: Sequence[FiniteGroup],
    max_arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingProductPrefixFirstFailureAudit:
    """Check finite product-prefix first failures for supplied group factors."""

    from .finite_group import direct_product_group

    if max_arity < 1:
        raise ValueError("max_arity must be positive")
    factors = tuple(groups)
    if not factors:
        raise ValueError("at least one group is required")

    rows = []
    for index in range(1, len(factors) + 1):
        product_group = direct_product_group(factors[:index])
        audit = point_pushing_brunnian_gate_prefix_audit(
            solution,
            product_group,
            max_arity=max_arity,
            max_detector_states=max_detector_states,
            max_pair_subgroup_size=max_pair_subgroup_size,
        )
        rows.append(
            PointPushingProductPrefixFirstFailureRow(
                prefix_index=index,
                product_group_order=len(product_group.elements),
                max_arity=max_arity,
                prefix_detected=audit.prefix_detected,
                first_failure_arity=audit.first_failure_arity,
                first_failure_kind=audit.first_failure_kind,
            )
        )
    return PointPushingProductPrefixFirstFailureAudit(
        prefix_count=len(factors),
        max_arity=max_arity,
        rows=tuple(rows),
    )


def _normal_subgroups_bruteforce(
    group: FiniteGroup,
    *,
    max_group_order: int | None = None,
) -> Tuple[frozenset[object], ...] | None:
    """Enumerate normal subgroups for small explicit groups."""

    from .finite_group import is_normal_subgroup

    group_order = len(group.elements)
    if max_group_order is not None and group_order > max_group_order:
        return None
    identity = group.identity
    rest = tuple(element for element in group.elements if element != identity)
    normal_subgroups = []
    for size in range(1, group_order + 1):
        for chosen in combinations(rest, size - 1):
            subset = frozenset((identity,) + chosen)
            if is_normal_subgroup(group, subset):
                normal_subgroups.append(subset)
    return tuple(normal_subgroups)


def _separating_quotient_size(
    group: FiniteGroup,
    element: object,
    normal_subgroups: Sequence[frozenset[object]],
) -> int:
    """Return the smallest quotient order separating ``element`` from identity."""

    candidates = [
        len(group.elements) // len(normal)
        for normal in normal_subgroups
        if element not in normal
    ]
    if not candidates:
        raise ValueError("no quotient separates the supplied nonidentity element")
    return min(candidates)


def _minimal_separating_quotient_data(
    group: FiniteGroup,
    element: object,
    normal_subgroups: Sequence[frozenset[object]],
):
    """Return quotient data for a smallest quotient separating ``element``."""

    from .finite_group import quotient_group_by_normal_subgroup

    separating_normals = [
        normal for normal in normal_subgroups if element not in normal
    ]
    if not separating_normals:
        raise ValueError("no quotient separates the supplied nonidentity element")
    kernel = max(separating_normals, key=len)
    quotient, projection = quotient_group_by_normal_subgroup(group, kernel)
    return kernel, quotient, projection


def _minimal_normal_subgroups(
    group: FiniteGroup,
    normal_subgroups: Sequence[frozenset[object]],
) -> Tuple[frozenset[object], ...]:
    """Return minimal nontrivial normal subgroups of a finite group."""

    identity_subgroup = frozenset((group.identity,))
    nontrivial = [
        normal for normal in normal_subgroups if normal != identity_subgroup
    ]
    minimal = []
    for candidate in nontrivial:
        if any(other < candidate for other in nontrivial):
            continue
        minimal.append(candidate)
    return tuple(minimal)


def _is_prime_integer(value: int) -> bool:
    if value < 2:
        return False
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            return False
        divisor += 1
    return True


def _prime_divisors_integer(value: int) -> Tuple[int, ...]:
    if value < 1:
        raise ValueError("value must be positive")
    primes = []
    divisor = 2
    remaining = value
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            primes.append(divisor)
            while remaining % divisor == 0:
                remaining //= divisor
        divisor += 1
    if remaining > 1:
        primes.append(remaining)
    return tuple(primes)


def _monolith_type_data(
    group: FiniteGroup,
    monolith: frozenset[object],
) -> Tuple[str, int | None, Tuple[int, ...]]:
    """Classify a finite monolith as abelian elementary or nonabelian."""

    from .finite_group import subgroup_as_group
    from .group_laws import element_order

    monolith_group = subgroup_as_group(group, monolith)
    orders = tuple(
        sorted(
            {
                element_order(monolith_group, element)
                for element in monolith_group.elements
                if element != monolith_group.identity
            }
        )
    )
    if is_abelian_group(monolith_group):
        prime = orders[0] if len(orders) == 1 and _is_prime_integer(orders[0]) else None
        monolith_type = "elementary_abelian" if prime is not None else "abelian"
        return monolith_type, prime, orders
    return "nonabelian_characteristically_simple", None, orders


def point_pushing_abelian_chief_relation_module_audit(
    group: FiniteGroup,
    monolith: Iterable[object],
    relation_image_generators: Iterable[object],
) -> PointPushingAbelianChiefRelationModuleAudit:
    """Audit the finite-group side of an abelian-chief relation module row."""

    from .finite_group import is_normal_subgroup, subgroup_as_group

    monolith_set = frozenset(monolith)
    relation_image = frozenset(
        subgroup_generated_elements(group, relation_image_generators)
    )
    normal_subgroups = _normal_subgroups_bruteforce(group)
    minimal_normals = _minimal_normal_subgroups(group, normal_subgroups)
    monolith_is_normal = is_normal_subgroup(group, monolith_set)
    relation_image_is_normal = is_normal_subgroup(group, relation_image)
    monolith_is_unique_minimal_normal = (
        len(minimal_normals) == 1 and minimal_normals[0] == monolith_set
    )
    monolith_is_abelian = (
        monolith_is_normal and is_abelian_group(subgroup_as_group(group, monolith_set))
    )
    relation_image_nontrivial = relation_image != frozenset((group.identity,))
    relation_image_inside_monolith = relation_image <= monolith_set
    relation_image_equals_monolith = relation_image == monolith_set
    return PointPushingAbelianChiefRelationModuleAudit(
        group_order=len(group.elements),
        monolith_order=len(monolith_set),
        relation_image_order=len(relation_image),
        monolith_is_normal=monolith_is_normal,
        relation_image_is_normal=relation_image_is_normal,
        monolith_is_unique_minimal_normal=monolith_is_unique_minimal_normal,
        monolith_is_abelian=monolith_is_abelian,
        relation_image_nontrivial=relation_image_nontrivial,
        relation_image_inside_monolith=relation_image_inside_monolith,
        relation_image_equals_monolith=relation_image_equals_monolith,
    )


def point_pushing_abelian_relation_action_split_audit(
    group: FiniteGroup,
    monolith: Iterable[object],
    relation_image_generators: Iterable[object],
) -> PointPushingAbelianRelationActionSplitAudit:
    """Audit the central/noncentral split for an abelian-chief relation row."""

    from .finite_group import is_normal_subgroup, subgroup_as_group

    monolith_set = frozenset(monolith)
    relation_image = frozenset(
        subgroup_generated_elements(group, relation_image_generators)
    )
    normal_subgroups = _normal_subgroups_bruteforce(group)
    minimal_normals = _minimal_normal_subgroups(group, normal_subgroups)
    monolith_is_normal = is_normal_subgroup(group, monolith_set)
    monolith_group = subgroup_as_group(group, monolith_set)
    monolith_is_abelian = monolith_is_normal and is_abelian_group(monolith_group)
    monolith_type, monolith_prime, _orders = _monolith_type_data(group, monolith_set)
    monolith_is_central = monolith_is_normal and all(
        group.conjugate(element, monolith_element) == monolith_element
        for element in group.elements
        for monolith_element in monolith_set
    )
    monolith_is_unique_minimal_normal = (
        len(minimal_normals) == 1 and minimal_normals[0] == monolith_set
    )
    relation_image_equals_monolith = relation_image == monolith_set
    if not (
        monolith_is_abelian
        and monolith_type == "elementary_abelian"
        and monolith_is_unique_minimal_normal
        and relation_image_equals_monolith
    ):
        split_regime = "invalid_abelian_relation_action_data"
    elif monolith_is_central and len(monolith_set) == monolith_prime:
        split_regime = "central_trivial_coinvariant"
    elif monolith_is_central:
        split_regime = "invalid_central_monolith_dimension"
    else:
        split_regime = "noncentral_irreducible_module"
    return PointPushingAbelianRelationActionSplitAudit(
        group_order=len(group.elements),
        monolith_order=len(monolith_set),
        monolith_prime=monolith_prime,
        relation_image_order=len(relation_image),
        monolith_is_abelian=monolith_is_abelian,
        monolith_is_central=monolith_is_central,
        monolith_is_unique_minimal_normal=monolith_is_unique_minimal_normal,
        relation_image_equals_monolith=relation_image_equals_monolith,
        split_regime=split_regime,
    )


def point_pushing_module_prime_characteristic_audit(
    normal_generator_order_bound: int,
    module_prime: int,
) -> PointPushingModulePrimeCharacteristicAudit:
    """Record whether a module-prime row is same- or cross-characteristic."""

    if normal_generator_order_bound <= 0:
        raise ValueError("normal_generator_order_bound must be positive")
    if not _is_prime_integer(module_prime):
        raise ValueError("module_prime must be prime")
    prime_divides_bound = normal_generator_order_bound % module_prime == 0
    cross_characteristic = not prime_divides_bound
    tail_regime = (
        "bounded_prime_divides_generator_bound"
        if prime_divides_bound
        else "cross_characteristic_prime_escape"
    )
    return PointPushingModulePrimeCharacteristicAudit(
        normal_generator_order_bound=normal_generator_order_bound,
        module_prime=module_prime,
        prime_divides_bound=prime_divides_bound,
        cross_characteristic=cross_characteristic,
        tail_regime=tail_regime,
    )


def point_pushing_active_module_generator_audit(
    normal_generator_order_bound: int,
    generator_action_order: int,
) -> PointPushingActiveModuleGeneratorAudit:
    """Record whether the bounded generator acts nontrivially on the module."""

    if normal_generator_order_bound <= 0:
        raise ValueError("normal_generator_order_bound must be positive")
    if generator_action_order <= 0:
        raise ValueError("generator_action_order must be positive")
    action_order_divides_bound = normal_generator_order_bound % generator_action_order == 0
    active_on_module = generator_action_order > 1
    tail_regime = (
        "active_bounded_order_linear_generator"
        if active_on_module
        else "centralizer_layer_generator"
    )
    return PointPushingActiveModuleGeneratorAudit(
        normal_generator_order_bound=normal_generator_order_bound,
        generator_action_order=generator_action_order,
        action_order_divides_bound=action_order_divides_bound,
        active_on_module=active_on_module,
        tail_regime=tail_regime,
    )


def point_pushing_centralizer_layer_commutator_audit(
    group: FiniteGroup,
    monolith: Iterable[object],
    generator: object,
) -> PointPushingCentralizerLayerCommutatorAudit:
    """Audit the abelian/stem split inside a centralizer-layer row."""

    from .finite_group import normal_closure_elements
    from .group_laws import element_order

    if generator not in group.elements:
        raise ValueError("generator must be a group element")
    monolith_set = frozenset(monolith)
    normal_closure = frozenset(normal_closure_elements(group, [generator]))
    commutator = frozenset(commutator_subgroup_elements(group, normal_closure))
    generator_centralizes_monolith = all(
        group.conjugate(generator, monolith_element) == monolith_element
        for monolith_element in monolith_set
    )
    normal_closure_centralizes_monolith = all(
        group.conjugate(element, monolith_element) == monolith_element
        for element in normal_closure
        for monolith_element in monolith_set
    )
    monolith_in_normal_closure = monolith_set <= normal_closure
    monolith_in_commutator = monolith_set <= commutator
    if not (
        generator_centralizes_monolith
        and normal_closure_centralizes_monolith
        and monolith_in_normal_closure
    ):
        layer_regime = "invalid_centralizer_layer_data"
    elif len(commutator) == 1:
        layer_regime = "abelian_centralizer_layer"
    elif monolith_in_commutator:
        layer_regime = "centralizer_stem_layer"
    else:
        layer_regime = "abelianization_visible_centralizer_layer"
    return PointPushingCentralizerLayerCommutatorAudit(
        group_order=len(group.elements),
        monolith_order=len(monolith_set),
        normal_closure_order=len(normal_closure),
        normal_closure_commutator_order=len(commutator),
        generator_order=element_order(group, generator),
        generator_centralizes_monolith=generator_centralizes_monolith,
        normal_closure_centralizes_monolith=normal_closure_centralizes_monolith,
        monolith_in_normal_closure=monolith_in_normal_closure,
        monolith_in_normal_closure_commutator=monolith_in_commutator,
        layer_regime=layer_regime,
    )


def point_pushing_abelian_centralizer_layer_prime_audit(
    group: FiniteGroup,
    monolith: Iterable[object],
    generator: object,
    normal_generator_order_bound: int,
) -> PointPushingAbelianCentralizerLayerPrimeAudit:
    """Audit the p-primary constraint on an abelian centralizer layer."""

    from .finite_group import normal_closure_elements
    from .group_laws import element_order, lcm

    if normal_generator_order_bound <= 0:
        raise ValueError("normal_generator_order_bound must be positive")
    if generator not in group.elements:
        raise ValueError("generator must be a group element")
    monolith_set = frozenset(monolith)
    monolith_type, monolith_prime, _orders = _monolith_type_data(group, monolith_set)
    normal_closure = frozenset(normal_closure_elements(group, [generator]))
    commutator = frozenset(commutator_subgroup_elements(group, normal_closure))
    element_orders = tuple(
        element_order(group, element)
        for element in normal_closure
        if element != group.identity
    )
    normal_closure_exponent = 1
    for order in element_orders:
        normal_closure_exponent = lcm(normal_closure_exponent, order)
    normal_closure_prime_set = _prime_divisors_integer(normal_closure_exponent)
    generator_order = element_order(group, generator)
    generator_order_divides_bound = normal_generator_order_bound % generator_order == 0
    exponent_divides_generator_order = generator_order % normal_closure_exponent == 0
    exponent_divides_bound = normal_generator_order_bound % normal_closure_exponent == 0
    normal_closure_abelian = len(commutator) == 1
    monolith_in_normal_closure = monolith_set <= normal_closure
    same_prime_as_monolith = (
        monolith_prime is not None
        and normal_closure_prime_set == (monolith_prime,)
    )
    prime_divides_generator_order = (
        monolith_prime is not None and generator_order % monolith_prime == 0
    )
    prime_divides_bound = (
        monolith_prime is not None
        and normal_generator_order_bound % monolith_prime == 0
    )
    if not (
        monolith_type == "elementary_abelian"
        and normal_closure_abelian
        and monolith_in_normal_closure
    ):
        tail_regime = "invalid_abelian_centralizer_layer_data"
    elif (
        same_prime_as_monolith
        and generator_order_divides_bound
        and exponent_divides_generator_order
    ):
        tail_regime = "bounded_p_primary_abelian_centralizer_layer"
    else:
        tail_regime = "mixed_prime_or_unbounded_generator_layer"
    return PointPushingAbelianCentralizerLayerPrimeAudit(
        normal_generator_order_bound=normal_generator_order_bound,
        group_order=len(group.elements),
        monolith_order=len(monolith_set),
        monolith_prime=monolith_prime,
        normal_closure_order=len(normal_closure),
        normal_closure_exponent=normal_closure_exponent,
        generator_order=generator_order,
        generator_order_divides_bound=generator_order_divides_bound,
        normal_closure_exponent_divides_generator_order=exponent_divides_generator_order,
        normal_closure_exponent_divides_bound=exponent_divides_bound,
        normal_closure_abelian=normal_closure_abelian,
        normal_closure_prime_set=normal_closure_prime_set,
        monolith_in_normal_closure=monolith_in_normal_closure,
        same_prime_as_monolith=same_prime_as_monolith,
        prime_divides_generator_order=prime_divides_generator_order,
        prime_divides_bound=prime_divides_bound,
        tail_regime=tail_regime,
    )


def point_pushing_centralizer_stem_multiplier_audit(
    group: FiniteGroup,
    monolith: Iterable[object],
    generator: object,
    normal_generator_order_bound: int,
) -> PointPushingCentralizerStemMultiplierAudit:
    """Audit a centralizer-stem layer as a stem extension of N/M."""

    from .finite_group import (
        normal_closure_elements,
        quotient_group_by_normal_subgroup,
        subgroup_as_group,
    )
    from .group_laws import element_order, group_exponent

    if normal_generator_order_bound <= 0:
        raise ValueError("normal_generator_order_bound must be positive")
    if generator not in group.elements:
        raise ValueError("generator must be a group element")
    monolith_set = frozenset(monolith)
    monolith_type, monolith_prime, _orders = _monolith_type_data(group, monolith_set)
    normal_closure = frozenset(normal_closure_elements(group, [generator]))
    normal_closure_group = subgroup_as_group(group, normal_closure)
    commutator = frozenset(commutator_subgroup_elements(group, normal_closure))
    monolith_central_in_normal_closure = all(
        group.conjugate(element, monolith_element) == monolith_element
        for element in normal_closure
        for monolith_element in monolith_set
    )
    monolith_in_commutator = monolith_set <= commutator
    monolith_is_elementary_abelian = monolith_type == "elementary_abelian"
    quotient_is_stem_target = (
        monolith_is_elementary_abelian
        and monolith_central_in_normal_closure
        and monolith_in_commutator
    )
    quotient_order = 0
    quotient_exponent = 0
    quotient_is_cyclic = False
    quotient_generator_internal_normal_closure_order = 0
    quotient_generator_internally_normally_generates = False
    generator_image_order = 0
    if (
        monolith_is_elementary_abelian
        and monolith_central_in_normal_closure
        and monolith_set <= normal_closure
    ):
        quotient, projection = quotient_group_by_normal_subgroup(
            normal_closure_group,
            monolith_set,
        )
        quotient_order = len(quotient.elements)
        quotient_exponent = group_exponent(quotient)
        quotient_is_cyclic = any(
            element_order(quotient, element) == quotient_order
            for element in quotient.elements
        )
        generator_image = projection.apply(generator)
        generator_image_order = element_order(quotient, generator_image)
        internal_closure = frozenset(
            normal_closure_elements(quotient, [generator_image])
        )
        quotient_generator_internal_normal_closure_order = len(internal_closure)
        quotient_generator_internally_normally_generates = (
            quotient_generator_internal_normal_closure_order == quotient_order
        )
    generator_order = element_order(group, generator)
    generator_order_divides_bound = normal_generator_order_bound % generator_order == 0
    quotient_is_noncyclic_stem_target = quotient_is_stem_target and not quotient_is_cyclic
    tail_regime = (
        "centralizer_stem_multiplier_tail"
        if quotient_is_noncyclic_stem_target and generator_order_divides_bound
        else "invalid_centralizer_stem_multiplier_data"
    )
    if tail_regime != "centralizer_stem_multiplier_tail":
        quotient_generation_regime = "invalid_centralizer_stem_generation_data"
    elif quotient_generator_internally_normally_generates:
        quotient_generation_regime = "internal_bounded_normal_generator_quotient"
    else:
        quotient_generation_regime = "transport_orbit_generated_quotient"
    return PointPushingCentralizerStemMultiplierAudit(
        normal_generator_order_bound=normal_generator_order_bound,
        group_order=len(group.elements),
        monolith_order=len(monolith_set),
        monolith_prime=monolith_prime,
        normal_closure_order=len(normal_closure),
        normal_closure_commutator_order=len(commutator),
        quotient_order=quotient_order,
        quotient_exponent=quotient_exponent,
        quotient_is_cyclic=quotient_is_cyclic,
        quotient_generator_internal_normal_closure_order=(
            quotient_generator_internal_normal_closure_order
        ),
        quotient_generator_internally_normally_generates=(
            quotient_generator_internally_normally_generates
        ),
        generator_order=generator_order,
        generator_image_order=generator_image_order,
        generator_order_divides_bound=generator_order_divides_bound,
        monolith_central_in_normal_closure=monolith_central_in_normal_closure,
        monolith_in_normal_closure_commutator=monolith_in_commutator,
        monolith_is_elementary_abelian=monolith_is_elementary_abelian,
        quotient_is_stem_target=quotient_is_stem_target,
        quotient_is_noncyclic_stem_target=quotient_is_noncyclic_stem_target,
        quotient_generation_regime=quotient_generation_regime,
        tail_regime=tail_regime,
    )


def point_pushing_central_stem_relation_audit(
    group: FiniteGroup,
    monolith: Iterable[object],
    relation_image_generators: Iterable[object],
) -> PointPushingCentralStemRelationAudit:
    """Audit a central trivial relation row as a stem central extension."""

    monolith_set = frozenset(monolith)
    relation_image = frozenset(
        subgroup_generated_elements(group, relation_image_generators)
    )
    monolith_type, monolith_prime, _orders = _monolith_type_data(group, monolith_set)
    commutator = frozenset(commutator_subgroup_elements(group))
    monolith_is_central = all(
        group.conjugate(element, monolith_element) == monolith_element
        for element in group.elements
        for monolith_element in monolith_set
    )
    monolith_in_commutator = monolith_set <= commutator
    relation_image_equals_monolith = relation_image == monolith_set
    quotient_is_stem = (
        monolith_type == "elementary_abelian"
        and monolith_is_central
        and monolith_in_commutator
    )
    return PointPushingCentralStemRelationAudit(
        group_order=len(group.elements),
        monolith_order=len(monolith_set),
        monolith_prime=monolith_prime,
        relation_image_order=len(relation_image),
        quotient_commutator_order=len(commutator),
        monolith_is_central=monolith_is_central,
        monolith_in_commutator=monolith_in_commutator,
        relation_image_equals_monolith=relation_image_equals_monolith,
        quotient_is_stem=quotient_is_stem,
    )


def point_pushing_nonabelian_chief_relation_quotient_audit(
    group: FiniteGroup,
    monolith: Iterable[object],
    relation_image_generators: Iterable[object],
    *,
    monolith_is_unique_minimal_normal: bool,
) -> PointPushingNonabelianChiefRelationQuotientAudit:
    """Audit the finite-group side of a nonabelian-chief relation row."""

    from .finite_group import is_normal_subgroup, subgroup_as_group

    monolith_set = frozenset(monolith)
    relation_image = frozenset(
        subgroup_generated_elements(group, relation_image_generators)
    )
    monolith_is_normal = is_normal_subgroup(group, monolith_set)
    relation_image_is_normal = is_normal_subgroup(group, relation_image)
    monolith_is_nonabelian = (
        monolith_is_normal
        and not is_abelian_group(subgroup_as_group(group, monolith_set))
    )
    relation_image_nontrivial = relation_image != frozenset((group.identity,))
    relation_image_inside_monolith = relation_image <= monolith_set
    relation_image_equals_monolith = relation_image == monolith_set
    return PointPushingNonabelianChiefRelationQuotientAudit(
        group_order=len(group.elements),
        monolith_order=len(monolith_set),
        relation_image_order=len(relation_image),
        monolith_is_normal=monolith_is_normal,
        monolith_is_nonabelian=monolith_is_nonabelian,
        monolith_is_unique_minimal_normal=monolith_is_unique_minimal_normal,
        relation_image_is_normal=relation_image_is_normal,
        relation_image_nontrivial=relation_image_nontrivial,
        relation_image_inside_monolith=relation_image_inside_monolith,
        relation_image_equals_monolith=relation_image_equals_monolith,
    )


def point_pushing_nonabelian_wreath_coordinate_audit(
    group: FiniteGroup,
    monolith: Iterable[object],
    relation_image_generators: Iterable[object],
    *,
    simple_factor_order: int,
    multiplicity: int,
    factor_action_transitive: bool,
    coordinate_value_nontrivial: bool,
) -> PointPushingNonabelianWreathCoordinateAudit:
    """Audit the finite shape of a simple-wreath coordinate relation row."""

    from .finite_group import subgroup_as_group

    if simple_factor_order <= 1:
        raise ValueError("simple_factor_order must be greater than 1")
    if multiplicity <= 0:
        raise ValueError("multiplicity must be positive")
    monolith_set = frozenset(monolith)
    monolith_group = subgroup_as_group(group, monolith_set)
    relation_image = frozenset(
        subgroup_generated_elements(group, relation_image_generators)
    )
    centralizer = frozenset(
        element
        for element in group.elements
        if all(
            group.conjugate(element, monolith_element) == monolith_element
            for monolith_element in monolith_set
        )
    )
    monolith_order_matches_simple_power = (
        len(monolith_set) == simple_factor_order ** multiplicity
    )
    monolith_is_nonabelian = not is_abelian_group(monolith_group)
    relation_image_equals_monolith = relation_image == monolith_set
    centralizer_trivial = centralizer == frozenset((group.identity,))
    return PointPushingNonabelianWreathCoordinateAudit(
        group_order=len(group.elements),
        monolith_order=len(monolith_set),
        simple_factor_order=simple_factor_order,
        multiplicity=multiplicity,
        relation_image_order=len(relation_image),
        centralizer_order=len(centralizer),
        monolith_order_matches_simple_power=monolith_order_matches_simple_power,
        monolith_is_nonabelian=monolith_is_nonabelian,
        relation_image_equals_monolith=relation_image_equals_monolith,
        centralizer_trivial=centralizer_trivial,
        factor_action_transitive=factor_action_transitive,
        coordinate_value_nontrivial=coordinate_value_nontrivial,
    )


def _monolith_conjugation_data(
    group: FiniteGroup,
    monolith: frozenset[object],
) -> Tuple[int, int, int, bool]:
    """Return centralizer, action quotient, and ``[G,M]`` sizes."""

    centralizer = frozenset(
        element
        for element in group.elements
        if all(
            group.conjugate(element, monolith_element) == monolith_element
            for monolith_element in monolith
        )
    )
    commutators = [
        group.mul(
            group.conjugate(element, monolith_element),
            group.inv(monolith_element),
        )
        for element in group.elements
        for monolith_element in monolith
    ]
    commutator_subgroup = subgroup_generated_elements(group, commutators)
    return (
        len(centralizer),
        len(group.elements) // len(centralizer),
        len(commutator_subgroup),
        len(commutator_subgroup) == 1,
    )


def _central_abelian_monolith_depth_data(
    group: FiniteGroup,
    monolith: frozenset[object],
    projected_value: object,
    *,
    monolith_type: str | None,
    monolith_is_central: bool | None,
) -> Tuple[int, bool, bool, str | None]:
    """Return derived-subgroup data and the central abelian depth regime."""

    derived = frozenset(commutator_subgroup_elements(group))
    monolith_in_derived = monolith.issubset(derived)
    projected_value_in_derived = projected_value in derived
    regime = None
    if monolith_type == "elementary_abelian" and monolith_is_central is True:
        if monolith_in_derived:
            regime = "central_stem"
        elif is_abelian_group(group):
            regime = "cyclic_p_power_depth"
        else:
            regime = "abelianization_visible"
    return (
        len(derived),
        monolith_in_derived,
        projected_value_in_derived,
        regime,
    )


def _cyclic_p_power_tail_data(
    quotient_order: int,
    monolith_prime: int | None,
    prefix_order_bound: int | None,
    *,
    central_abelian_depth_regime: str | None,
) -> Tuple[int | None, int | None, str | None]:
    """Return prime/exponent and product-prefix escape type for cyclic depth."""

    if central_abelian_depth_regime != "cyclic_p_power_depth":
        return None, None, None
    if monolith_prime is None:
        return None, None, "invalid_cyclic_p_power_data"
    exponent = 0
    remaining = quotient_order
    while remaining % monolith_prime == 0:
        exponent += 1
        remaining //= monolith_prime
    if remaining != 1 or exponent == 0:
        return monolith_prime, None, "invalid_cyclic_p_power_data"
    if prefix_order_bound is None:
        return monolith_prime, exponent, "cyclic_p_power"
    if quotient_order <= prefix_order_bound:
        return monolith_prime, exponent, "prefix_covers_cyclic_p_power"
    if monolith_prime > prefix_order_bound:
        return monolith_prime, exponent, "prime_escape"
    return monolith_prime, exponent, "p_power_depth_escape"


def _noncentral_abelian_module_tail_data(
    quotient_order: int,
    monolith_order: int | None,
    monolith_prime: int | None,
    monolith_type: str | None,
    monolith_is_central: bool | None,
    action_quotient_order: int | None,
    centralizer_order: int | None,
    prefix_order_bound: int | None,
) -> Tuple[int | None, int | None, bool | None, str | None]:
    """Return module dimension, centralizer layer, and escape regime."""

    if monolith_type != "elementary_abelian" or monolith_is_central is not False:
        return None, None, None, None
    if (
        monolith_order is None
        or monolith_prime is None
        or action_quotient_order is None
        or centralizer_order is None
    ):
        return None, None, None, "invalid_noncentral_module_data"

    dimension = 0
    remaining = monolith_order
    while remaining % monolith_prime == 0:
        dimension += 1
        remaining //= monolith_prime
    if remaining != 1 or dimension == 0:
        return None, None, None, "invalid_noncentral_module_data"
    if centralizer_order % monolith_order != 0:
        return dimension, None, False, "invalid_noncentral_module_data"

    centralizer_layer_order = centralizer_order // monolith_order
    product_matches = (
        monolith_order * action_quotient_order * centralizer_layer_order
        == quotient_order
    )
    if not product_matches:
        return (
            dimension,
            centralizer_layer_order,
            False,
            "invalid_noncentral_module_data",
        )
    if prefix_order_bound is None:
        return (
            dimension,
            centralizer_layer_order,
            True,
            "noncentral_irreducible_module",
        )
    if quotient_order <= prefix_order_bound:
        return (
            dimension,
            centralizer_layer_order,
            True,
            "prefix_covers_noncentral_quotient",
        )
    if monolith_prime > prefix_order_bound:
        return dimension, centralizer_layer_order, True, "module_prime_escape"
    if monolith_order > prefix_order_bound:
        return dimension, centralizer_layer_order, True, "module_dimension_escape"
    if action_quotient_order > prefix_order_bound:
        return dimension, centralizer_layer_order, True, "action_shadow_escape"
    if centralizer_layer_order > prefix_order_bound:
        return dimension, centralizer_layer_order, True, "centralizer_layer_escape"
    return dimension, centralizer_layer_order, True, "mixed_parameter_escape"


def _nonabelian_monolith_tail_data(
    quotient_order: int,
    monolith_order: int | None,
    monolith_type: str | None,
    centralizer_order: int | None,
    prefix_order_bound: int | None,
) -> Tuple[bool | None, int | None, str | None]:
    """Return centralizer and prefix data for nonabelian monolith tails."""

    if monolith_type != "nonabelian_characteristically_simple":
        return None, None, None
    if monolith_order is None or centralizer_order is None:
        return None, None, "invalid_nonabelian_monolith_data"
    centralizer_trivial = centralizer_order == 1
    if quotient_order % monolith_order != 0:
        return centralizer_trivial, None, "invalid_nonabelian_monolith_data"
    over_monolith_order = quotient_order // monolith_order
    if not centralizer_trivial:
        return (
            centralizer_trivial,
            over_monolith_order,
            "invalid_nonabelian_monolith_data",
        )
    if prefix_order_bound is None:
        return centralizer_trivial, over_monolith_order, "nonabelian_simple_product"
    if quotient_order <= prefix_order_bound:
        return (
            centralizer_trivial,
            over_monolith_order,
            "prefix_covers_nonabelian_quotient",
        )
    if monolith_order > prefix_order_bound:
        return (
            centralizer_trivial,
            over_monolith_order,
            "nonabelian_monolith_order_escape",
        )
    if over_monolith_order > prefix_order_bound:
        return (
            centralizer_trivial,
            over_monolith_order,
            "over_monolith_action_escape",
        )
    return (
        centralizer_trivial,
        over_monolith_order,
        "mixed_nonabelian_parameter_escape",
    )


def point_pushing_monolithic_compression_audit(
    solution: FiniteBraidedSet,
    word: FreeWord,
    arity: int,
    *,
    prefix_order_bound: int | None = None,
    max_action_group_order: int | None = None,
) -> PointPushingMonolithicCompressionAudit:
    """Compress one nontrivial point-pushing action value to a monolith."""

    if arity < 1:
        raise ValueError("arity must be positive")
    for generator, _exponent in word:
        if generator < 0 or generator >= arity:
            raise ValueError(f"free generator {generator} outside arity {arity}")

    try:
        action_group = point_pushing_action_group(
            solution,
            arity,
            max_size=max_action_group_order,
        )
    except ValueError as exc:
        if "exceeded max_size" not in str(exc):
            raise
        return PointPushingMonolithicCompressionAudit(
            arity=arity,
            word=tuple(word),
            action_group_order=None,
            action_value=None,
            action_value_nontrivial=False,
            quotient_order=None,
            quotient_kernel_size=None,
            monolith_order=None,
            monolith_type=None,
            monolith_prime=None,
            monolith_element_orders=None,
            monolith_centralizer_order=None,
            monolith_action_quotient_order=None,
            monolith_commutator_order=None,
            monolith_is_central=None,
            quotient_commutator_order=None,
            monolith_in_quotient_commutator=None,
            projected_value_in_quotient_commutator=None,
            central_abelian_depth_regime=None,
            central_cyclic_prime=None,
            central_cyclic_exponent=None,
            central_cyclic_prefix_regime=None,
            noncentral_module_dimension=None,
            noncentral_centralizer_layer_order=None,
            noncentral_size_product_matches_quotient=None,
            noncentral_parameter_regime=None,
            nonabelian_centralizer_trivial=None,
            nonabelian_over_monolith_order=None,
            nonabelian_prefix_regime=None,
            quotient_is_monolithic=None,
            projected_value_in_monolith=None,
            prefix_order_bound=prefix_order_bound,
            quotient_escapes_prefix_bound=None,
            truncated=True,
        )

    action_images = _point_pushing_action_generator_images(solution, arity)
    action_value = evaluate_free_word_on_permutations(word, action_images)
    if action_value == action_group.identity:
        return PointPushingMonolithicCompressionAudit(
            arity=arity,
            word=tuple(word),
            action_group_order=len(action_group.elements),
            action_value=action_value,
            action_value_nontrivial=False,
            quotient_order=None,
            quotient_kernel_size=None,
            monolith_order=None,
            monolith_type=None,
            monolith_prime=None,
            monolith_element_orders=None,
            monolith_centralizer_order=None,
            monolith_action_quotient_order=None,
            monolith_commutator_order=None,
            monolith_is_central=None,
            quotient_commutator_order=None,
            monolith_in_quotient_commutator=None,
            projected_value_in_quotient_commutator=None,
            central_abelian_depth_regime=None,
            central_cyclic_prime=None,
            central_cyclic_exponent=None,
            central_cyclic_prefix_regime=None,
            noncentral_module_dimension=None,
            noncentral_centralizer_layer_order=None,
            noncentral_size_product_matches_quotient=None,
            noncentral_parameter_regime=None,
            nonabelian_centralizer_trivial=None,
            nonabelian_over_monolith_order=None,
            nonabelian_prefix_regime=None,
            quotient_is_monolithic=None,
            projected_value_in_monolith=None,
            prefix_order_bound=prefix_order_bound,
            quotient_escapes_prefix_bound=None,
            truncated=False,
        )

    normal_subgroups = _normal_subgroups_bruteforce(
        action_group,
        max_group_order=max_action_group_order,
    )
    if normal_subgroups is None:
        return PointPushingMonolithicCompressionAudit(
            arity=arity,
            word=tuple(word),
            action_group_order=len(action_group.elements),
            action_value=action_value,
            action_value_nontrivial=True,
            quotient_order=None,
            quotient_kernel_size=None,
            monolith_order=None,
            monolith_type=None,
            monolith_prime=None,
            monolith_element_orders=None,
            monolith_centralizer_order=None,
            monolith_action_quotient_order=None,
            monolith_commutator_order=None,
            monolith_is_central=None,
            quotient_commutator_order=None,
            monolith_in_quotient_commutator=None,
            projected_value_in_quotient_commutator=None,
            central_abelian_depth_regime=None,
            central_cyclic_prime=None,
            central_cyclic_exponent=None,
            central_cyclic_prefix_regime=None,
            noncentral_module_dimension=None,
            noncentral_centralizer_layer_order=None,
            noncentral_size_product_matches_quotient=None,
            noncentral_parameter_regime=None,
            nonabelian_centralizer_trivial=None,
            nonabelian_over_monolith_order=None,
            nonabelian_prefix_regime=None,
            quotient_is_monolithic=None,
            projected_value_in_monolith=None,
            prefix_order_bound=prefix_order_bound,
            quotient_escapes_prefix_bound=None,
            truncated=True,
        )

    kernel, quotient, projection = _minimal_separating_quotient_data(
        action_group,
        action_value,
        normal_subgroups,
    )
    quotient_normals = _normal_subgroups_bruteforce(
        quotient,
        max_group_order=max_action_group_order,
    )
    if quotient_normals is None:
        return PointPushingMonolithicCompressionAudit(
            arity=arity,
            word=tuple(word),
            action_group_order=len(action_group.elements),
            action_value=action_value,
            action_value_nontrivial=True,
            quotient_order=len(quotient.elements),
            quotient_kernel_size=len(kernel),
            monolith_order=None,
            monolith_type=None,
            monolith_prime=None,
            monolith_element_orders=None,
            monolith_centralizer_order=None,
            monolith_action_quotient_order=None,
            monolith_commutator_order=None,
            monolith_is_central=None,
            quotient_commutator_order=None,
            monolith_in_quotient_commutator=None,
            projected_value_in_quotient_commutator=None,
            central_abelian_depth_regime=None,
            central_cyclic_prime=None,
            central_cyclic_exponent=None,
            central_cyclic_prefix_regime=None,
            noncentral_module_dimension=None,
            noncentral_centralizer_layer_order=None,
            noncentral_size_product_matches_quotient=None,
            noncentral_parameter_regime=None,
            nonabelian_centralizer_trivial=None,
            nonabelian_over_monolith_order=None,
            nonabelian_prefix_regime=None,
            quotient_is_monolithic=None,
            projected_value_in_monolith=None,
            prefix_order_bound=prefix_order_bound,
            quotient_escapes_prefix_bound=(
                None
                if prefix_order_bound is None
                else len(quotient.elements) > prefix_order_bound
            ),
            truncated=True,
        )

    minimal_normals = _minimal_normal_subgroups(quotient, quotient_normals)
    monolith = minimal_normals[0] if len(minimal_normals) == 1 else None
    projected_value = projection.apply(action_value)
    quotient_order = len(quotient.elements)
    monolith_type = None
    monolith_prime = None
    monolith_element_orders = None
    monolith_centralizer_order = None
    monolith_action_quotient_order = None
    monolith_commutator_order = None
    monolith_is_central = None
    quotient_commutator_order = None
    monolith_in_quotient_commutator = None
    projected_value_in_quotient_commutator = None
    central_abelian_depth_regime = None
    central_cyclic_prime = None
    central_cyclic_exponent = None
    central_cyclic_prefix_regime = None
    noncentral_module_dimension = None
    noncentral_centralizer_layer_order = None
    noncentral_size_product_matches_quotient = None
    noncentral_parameter_regime = None
    nonabelian_centralizer_trivial = None
    nonabelian_over_monolith_order = None
    nonabelian_prefix_regime = None
    if monolith is not None:
        monolith_type, monolith_prime, monolith_element_orders = _monolith_type_data(
            quotient,
            monolith,
        )
        (
            monolith_centralizer_order,
            monolith_action_quotient_order,
            monolith_commutator_order,
            monolith_is_central,
        ) = _monolith_conjugation_data(quotient, monolith)
        (
            quotient_commutator_order,
            monolith_in_quotient_commutator,
            projected_value_in_quotient_commutator,
            central_abelian_depth_regime,
        ) = _central_abelian_monolith_depth_data(
            quotient,
            monolith,
            projected_value,
            monolith_type=monolith_type,
            monolith_is_central=monolith_is_central,
        )
        (
            central_cyclic_prime,
            central_cyclic_exponent,
            central_cyclic_prefix_regime,
        ) = _cyclic_p_power_tail_data(
            quotient_order,
            monolith_prime,
            prefix_order_bound,
            central_abelian_depth_regime=central_abelian_depth_regime,
        )
        (
            noncentral_module_dimension,
            noncentral_centralizer_layer_order,
            noncentral_size_product_matches_quotient,
            noncentral_parameter_regime,
        ) = _noncentral_abelian_module_tail_data(
            quotient_order,
            len(monolith),
            monolith_prime,
            monolith_type,
            monolith_is_central,
            monolith_action_quotient_order,
            monolith_centralizer_order,
            prefix_order_bound,
        )
        (
            nonabelian_centralizer_trivial,
            nonabelian_over_monolith_order,
            nonabelian_prefix_regime,
        ) = _nonabelian_monolith_tail_data(
            quotient_order,
            len(monolith),
            monolith_type,
            monolith_centralizer_order,
            prefix_order_bound,
        )
    return PointPushingMonolithicCompressionAudit(
        arity=arity,
        word=tuple(word),
        action_group_order=len(action_group.elements),
        action_value=action_value,
        action_value_nontrivial=True,
        quotient_order=quotient_order,
        quotient_kernel_size=len(kernel),
        monolith_order=None if monolith is None else len(monolith),
        monolith_type=monolith_type,
        monolith_prime=monolith_prime,
        monolith_element_orders=monolith_element_orders,
        monolith_centralizer_order=monolith_centralizer_order,
        monolith_action_quotient_order=monolith_action_quotient_order,
        monolith_commutator_order=monolith_commutator_order,
        monolith_is_central=monolith_is_central,
        quotient_commutator_order=quotient_commutator_order,
        monolith_in_quotient_commutator=monolith_in_quotient_commutator,
        projected_value_in_quotient_commutator=projected_value_in_quotient_commutator,
        central_abelian_depth_regime=central_abelian_depth_regime,
        central_cyclic_prime=central_cyclic_prime,
        central_cyclic_exponent=central_cyclic_exponent,
        central_cyclic_prefix_regime=central_cyclic_prefix_regime,
        noncentral_module_dimension=noncentral_module_dimension,
        noncentral_centralizer_layer_order=noncentral_centralizer_layer_order,
        noncentral_size_product_matches_quotient=noncentral_size_product_matches_quotient,
        noncentral_parameter_regime=noncentral_parameter_regime,
        nonabelian_centralizer_trivial=nonabelian_centralizer_trivial,
        nonabelian_over_monolith_order=nonabelian_over_monolith_order,
        nonabelian_prefix_regime=nonabelian_prefix_regime,
        quotient_is_monolithic=monolith is not None,
        projected_value_in_monolith=(
            None if monolith is None else projected_value in monolith
        ),
        prefix_order_bound=prefix_order_bound,
        quotient_escapes_prefix_bound=(
            None if prefix_order_bound is None else quotient_order > prefix_order_bound
        ),
        truncated=False,
    )


def point_pushing_action_quotient_separation_audit(
    solution: FiniteBraidedSet,
    max_arity: int,
    *,
    max_action_group_order: int | None = None,
) -> PointPushingActionQuotientSeparationAudit:
    """Audit finite quotient-separating depths of ``P_k(X)`` for small rows."""

    if max_arity < 1:
        raise ValueError("max_arity must be positive")

    rows = []
    for arity in range(1, max_arity + 1):
        try:
            action_group = point_pushing_action_group(
                solution,
                arity,
                max_size=max_action_group_order,
            )
        except ValueError as exc:
            if "exceeded max_size" not in str(exc):
                raise
            rows.append(
                PointPushingActionQuotientSeparationRow(
                    arity=arity,
                    action_group_order=None,
                    nonidentity_count=None,
                    max_separating_quotient_size=None,
                    deepest_element=None,
                    truncated=True,
                )
            )
            continue

        normal_subgroups = _normal_subgroups_bruteforce(
            action_group,
            max_group_order=max_action_group_order,
        )
        if normal_subgroups is None:
            rows.append(
                PointPushingActionQuotientSeparationRow(
                    arity=arity,
                    action_group_order=len(action_group.elements),
                    nonidentity_count=len(action_group.elements) - 1,
                    max_separating_quotient_size=None,
                    deepest_element=None,
                    truncated=True,
                )
            )
            continue

        deepest_element = None
        max_separator = 1
        for element in action_group.elements:
            if element == action_group.identity:
                continue
            separator = _separating_quotient_size(
                action_group,
                element,
                normal_subgroups,
            )
            if separator > max_separator:
                max_separator = separator
                deepest_element = element
        rows.append(
            PointPushingActionQuotientSeparationRow(
                arity=arity,
                action_group_order=len(action_group.elements),
                nonidentity_count=len(action_group.elements) - 1,
                max_separating_quotient_size=max_separator,
                deepest_element=deepest_element,
                truncated=False,
            )
        )
    return PointPushingActionQuotientSeparationAudit(
        max_arity=max_arity,
        max_action_group_order=max_action_group_order,
        rows=tuple(rows),
    )


def point_pushing_base_free_brunnian_tail_prefix(
    solution: FiniteBraidedSet,
    max_symmetric_degree: int,
    max_arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingBaseFreeBrunnianTailPrefix:
    """Check a finite symmetric-tail prefix after the base gate cutoff."""

    from .finite_group import symmetric_group

    if max_symmetric_degree < 1:
        raise ValueError("max_symmetric_degree must be positive")
    if max_arity < 1:
        raise ValueError("max_arity must be positive")

    base_certificate = point_pushing_base_arity_certificate(solution)
    rows = []
    for degree in range(base_certificate.symmetric_degree_bound, max_symmetric_degree + 1):
        group = symmetric_group(degree)
        audit = point_pushing_brunnian_gate_prefix_audit(
            solution,
            group,
            max_arity=max_arity,
            max_detector_states=max_detector_states,
            max_pair_subgroup_size=max_pair_subgroup_size,
        )
        certificate = None
        if audit.first_failure_kind in ("stabilizer", "orbit_label", "orbit_relation"):
            if audit.first_failure_arity is None:
                raise AssertionError("non-base failure kind without failure arity")
            certificate = point_pushing_brunnian_failure_certificate(
                solution,
                group,
                audit.first_failure_arity,
                max_detector_states=max_detector_states,
                max_pair_subgroup_size=max_pair_subgroup_size,
            )
        rows.append(
            PointPushingBrunnianTailCertificateRow(
                symmetric_degree=degree,
                max_arity=max_arity,
                prefix_detected=audit.prefix_detected,
                first_failure_arity=audit.first_failure_arity,
                first_failure_kind=audit.first_failure_kind,
                certificate=certificate,
            )
        )
    return PointPushingBaseFreeBrunnianTailPrefix(
        base_certificate=base_certificate,
        max_symmetric_degree=max_symmetric_degree,
        max_arity=max_arity,
        rows=tuple(rows),
    )


def point_pushing_base_free_threshold_audit(
    solution: FiniteBraidedSet,
    max_symmetric_degree: int,
    max_arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingBaseFreeThresholdAudit:
    """Find the first checked symmetric degree passing a base-free prefix."""

    prefix = point_pushing_base_free_brunnian_tail_prefix(
        solution,
        max_symmetric_degree=max_symmetric_degree,
        max_arity=max_arity,
        max_detector_states=max_detector_states,
        max_pair_subgroup_size=max_pair_subgroup_size,
    )
    minimal_detecting_degree = None
    for row in prefix.rows:
        if row.prefix_detected:
            minimal_detecting_degree = row.symmetric_degree
            break
    return PointPushingBaseFreeThresholdAudit(
        base_free_prefix=prefix,
        minimal_detecting_degree=minimal_detecting_degree,
    )


def point_pushing_base_free_threshold_prefix_audit(
    solution: FiniteBraidedSet,
    max_symmetric_degree: int,
    max_arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingBaseFreeThresholdPrefixAudit:
    """Audit ``epsilon_X(K)`` for ``1 <= K <= max_arity`` within a degree bound."""

    if max_arity < 1:
        raise ValueError("max_arity must be positive")
    rows = []
    for arity in range(1, max_arity + 1):
        rows.append(
            point_pushing_base_free_threshold_audit(
                solution,
                max_symmetric_degree=max_symmetric_degree,
                max_arity=arity,
                max_detector_states=max_detector_states,
                max_pair_subgroup_size=max_pair_subgroup_size,
            )
        )
    return PointPushingBaseFreeThresholdPrefixAudit(
        max_symmetric_degree=max_symmetric_degree,
        max_arity=max_arity,
        rows=tuple(rows),
    )


def point_pushing_brunnian_normalized_prefix_audit(
    solution: FiniteBraidedSet,
    symmetric_degree: int,
    arity: int,
    fill_value: object,
    *,
    extra_strands: int | None = None,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingBrunnianNormalizedPrefixAudit:
    """Turn one Brunnian failure row into a symmetric normalized-law row."""

    from .finite_group import symmetric_group
    from .artin_longitudes import symmetric_normalized_law_prefix_witness_audit

    if symmetric_degree < 1:
        raise ValueError("symmetric_degree must be positive")
    if arity < 1:
        raise ValueError("arity must be positive")
    if extra_strands is None:
        extra_strands = symmetric_degree
    if extra_strands < 0:
        raise ValueError("extra_strands must be nonnegative")

    group = symmetric_group(symmetric_degree)
    certificate = point_pushing_brunnian_failure_certificate(
        solution,
        group,
        arity,
        max_detector_states=max_detector_states,
        max_pair_subgroup_size=max_pair_subgroup_size,
    )
    normalized_prefix = None
    if certificate.valid_failure_certificate:
        witness = certificate.witness
        if witness is None or witness.vertical.moved_tuple is None:
            raise AssertionError("valid Brunnian failure certificate lacks moved tuple")
        normalized_prefix = symmetric_normalized_law_prefix_witness_audit(
            solution,
            symmetric_degree,
            arity + 1,
            witness.vertical.braid_word,
            witness.vertical.moved_tuple,
            extra_strands,
            fill_value,
        )
    return PointPushingBrunnianNormalizedPrefixAudit(
        symmetric_degree=symmetric_degree,
        arity=arity,
        extra_strands=extra_strands,
        certificate=certificate,
        normalized_prefix=normalized_prefix,
    )


def point_pushing_suffix_shuttle_action(
    solution: FiniteBraidedSet,
    braid_index: int,
    generator: int,
    tuple_value: Sequence[object],
) -> Tuple[object, ...]:
    """Apply ``A_{generator,braid_index}`` by the suffix-shuttle normal form.

    Indices are one-based.  The formula expands
    ``A_{i,n}=sigma_{n-1}...sigma_{i+1} sigma_i^2
    sigma_{i+1}^{-1}...sigma_{n-1}^{-1}``.
    """

    if braid_index < 2:
        raise ValueError("braid_index must be at least two")
    if generator < 1 or generator >= braid_index:
        raise ValueError("require 1 <= generator < braid_index")
    if len(tuple_value) != braid_index:
        raise ValueError("tuple length must equal braid_index")

    out = list(tuple_value)
    for crossing in range(braid_index - 1, generator, -1):
        index = crossing - 1
        out[index], out[index + 1] = solution.R[(out[index], out[index + 1])]
    core_index = generator - 1
    out[core_index], out[core_index + 1] = solution.R[
        (out[core_index], out[core_index + 1])
    ]
    out[core_index], out[core_index + 1] = solution.R[
        (out[core_index], out[core_index + 1])
    ]
    inverse = solution.inverse_R
    for crossing in range(generator + 1, braid_index):
        index = crossing - 1
        out[index], out[index + 1] = inverse[(out[index], out[index + 1])]
    return tuple(out)


def point_pushing_suffix_shuttle_audit(
    solution: FiniteBraidedSet,
    braid_index: int,
    generator: int,
) -> PointPushingSuffixShuttleAudit:
    """Check the suffix-shuttle normal form against direct braid action."""

    from .braid_laws import pure_braid_generator

    if braid_index < 2:
        raise ValueError("braid_index must be at least two")
    if generator < 1 or generator >= braid_index:
        raise ValueError("require 1 <= generator < braid_index")

    braid = pure_braid_generator(generator, braid_index)
    tuple_count = 0
    for tuple_value in product(solution.elements, repeat=braid_index):
        tuple_count += 1
        direct = solution.braid_action(braid, tuple_value)
        shuttle = point_pushing_suffix_shuttle_action(
            solution,
            braid_index,
            generator,
            tuple_value,
        )
        if direct != shuttle:
            return PointPushingSuffixShuttleAudit(
                braid_index=braid_index,
                generator=generator,
                tuple_count=tuple_count,
                matches_direct_action=False,
                first_failure_input=tuple_value,
                first_failure_direct=direct,
                first_failure_shuttle=shuttle,
            )
    return PointPushingSuffixShuttleAudit(
        braid_index=braid_index,
        generator=generator,
        tuple_count=tuple_count,
        matches_direct_action=True,
        first_failure_input=None,
        first_failure_direct=None,
        first_failure_shuttle=None,
    )


def _apply_word_to_slice(
    solution: FiniteBraidedSet,
    tuple_value: Sequence[object],
    start: int,
    braid_word: BraidWord,
) -> Tuple[object, ...]:
    out = list(tuple_value)
    suffix = tuple(out[start:])
    image = solution.braid_action(braid_word, suffix)
    out[start:] = image
    return tuple(out)


def point_pushing_recursive_conjugacy_audit(
    solution: FiniteBraidedSet,
    braid_index: int,
) -> PointPushingRecursiveConjugacyAudit:
    """Check the recursive ``A_{1,n}`` and suffix-shift point-pushing forms."""

    from .braid_laws import invert_braid_word, pure_braid_generator

    if braid_index < 2:
        raise ValueError("braid_index must be at least two")

    tuple_count = 0
    for tuple_value in product(solution.elements, repeat=braid_index):
        tuple_count += 1
        direct = solution.braid_action(
            pure_braid_generator(1, braid_index),
            tuple_value,
        )
        if braid_index == 2:
            recursive = solution.braid_action((1, 1), tuple_value)
        else:
            crossing = (braid_index - 1,)
            inverse_crossing = invert_braid_word(crossing)
            recursive = solution.braid_action(crossing, tuple_value)
            recursive = _apply_word_to_slice(
                solution,
                recursive,
                0,
                pure_braid_generator(1, braid_index - 1),
            )
            recursive = solution.braid_action(inverse_crossing, recursive)
        if direct != recursive:
            return PointPushingRecursiveConjugacyAudit(
                braid_index=braid_index,
                tuple_count=tuple_count,
                first_generator_recursion_matches=False,
                all_suffix_shift_generators_match=False,
                first_failure_generator=1,
                first_failure_input=tuple_value,
                first_failure_direct=direct,
                first_failure_recursive=recursive,
            )

    for generator in range(1, braid_index):
        suffix_length = braid_index - generator + 1
        suffix_braid = pure_braid_generator(1, suffix_length)
        direct_braid = pure_braid_generator(generator, braid_index)
        for tuple_value in product(solution.elements, repeat=braid_index):
            direct = solution.braid_action(direct_braid, tuple_value)
            recursive = _apply_word_to_slice(
                solution,
                tuple_value,
                generator - 1,
                suffix_braid,
            )
            if direct != recursive:
                return PointPushingRecursiveConjugacyAudit(
                    braid_index=braid_index,
                    tuple_count=tuple_count,
                    first_generator_recursion_matches=True,
                    all_suffix_shift_generators_match=False,
                    first_failure_generator=generator,
                    first_failure_input=tuple_value,
                    first_failure_direct=direct,
                    first_failure_recursive=recursive,
                )
    return PointPushingRecursiveConjugacyAudit(
        braid_index=braid_index,
        tuple_count=tuple_count,
        first_generator_recursion_matches=True,
        all_suffix_shift_generators_match=True,
        first_failure_generator=None,
        first_failure_input=None,
        first_failure_direct=None,
        first_failure_recursive=None,
    )


def braid_word_permutation_image(
    solution: FiniteBraidedSet, n: int, braid_word: BraidWord
) -> Permutation:
    return action_permutation(solution, n, braid_word)


def braid_images_for_words(
    solution: FiniteBraidedSet, n: int, words: Mapping[int, BraidWord]
) -> dict[int, Permutation]:
    return {generator: braid_word_permutation_image(solution, n, word) for generator, word in words.items()}


def law_braid_action_certificate(
    solution: FiniteBraidedSet,
    word: FreeWord,
    arity: int,
    *,
    max_subgroup_size: int | None = None,
) -> LawBraidActionCertificate:
    """Certify the fixed-image obstruction for an embedded free law.

    The free word is embedded into `B_{arity+1}` using the standard pure
    generators `A_{r+1,n}`.  The certificate compares two computations:
    direct action of the embedded braid on `X^n`, and evaluation of the free
    word in the finite subgroup of `Sym(X^n)` generated by those pure-generator
    images.  If the word is a law on that subgroup, the embedded braid must act
    trivially on this fixed finite YBE action image.
    """

    from .braid_laws import law_word_on_last_strand, pure_braid_generator
    from .group_laws import group_exponent, is_law_on_group

    n, braid = law_word_on_last_strand(word, arity)
    generator_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(arity)
    }
    images = braid_images_for_words(solution, n, generator_braids)
    subgroup = generated_permutation_subgroup(
        images.values(), max_size=max_subgroup_size
    )
    subgroup_as_group = permutation_group_from_subgroup(subgroup)
    evaluated = evaluate_free_word_on_permutations(word, images)
    identity = identity_permutation(len(evaluated))
    direct = braid_word_permutation_image(solution, n, braid)
    return LawBraidActionCertificate(
        braid_index=n,
        tuple_count=len(solution.elements) ** n,
        generator_image_subgroup_size=len(subgroup),
        generator_image_subgroup_exponent=group_exponent(subgroup_as_group),
        word_is_law_on_image_subgroup=is_law_on_group(
            subgroup_as_group, word, arity=arity
        ),
        evaluated_word_is_identity=evaluated == identity,
        direct_braid_is_identity=direct == identity,
        direct_matches_evaluated=direct == evaluated,
    )


def point_pushing_variety_escape_audit(
    solution: FiniteBraidedSet,
    symmetric_degree: int,
    point_pushing_arity: int,
    *,
    law_arity: int,
    max_length: int,
    max_subgroup_size: int | None = None,
    max_assignments: int | None = None,
) -> PointPushingVarietyEscapeAudit:
    """Search one bounded point-pushing action image for a variety escape.

    A returned separating word is a law on ``S_m`` but evaluates nontrivially
    on the computed action image ``P_k(X)``.  The audit also records
    representatives for the chosen assignment in the marked pure generators,
    and verifies that the substituted point-pushing word moves the direct YBE
    braid action.
    """

    from .braid_laws import law_word_on_last_strand, pure_braid_generator
    from .finite_group import symmetric_group
    from .group_laws import is_law_on_group, reduced_free_words

    if symmetric_degree < 1:
        raise ValueError("symmetric_degree must be positive")
    if point_pushing_arity < 1:
        raise ValueError("point_pushing_arity must be positive")
    if law_arity < 1:
        raise ValueError("law_arity must be positive")
    if max_length < 1:
        raise ValueError("max_length must be positive")

    n = point_pushing_arity + 1
    tuple_count = len(solution.elements) ** n
    generator_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(point_pushing_arity)
    }
    images = braid_images_for_words(solution, n, generator_braids)
    try:
        subgroup_words = generated_permutation_subgroup_with_words(
            images,
            max_size=max_subgroup_size,
        )
    except ValueError:
        return PointPushingVarietyEscapeAudit(
            symmetric_degree=symmetric_degree,
            point_pushing_arity=point_pushing_arity,
            law_arity=law_arity,
            braid_index=n,
            tuple_count=tuple_count,
            action_image_size=None,
            truncated=True,
            assignment_count_checked=0,
            separating_word=None,
            assignment_representatives=tuple(),
            substituted_point_pushing_word=None,
            evaluated_permutation=None,
            direct_braid_permutation=None,
            moved_index=None,
            substituted_word_is_symmetric_law=None,
        )

    subgroup = tuple(subgroup_words)
    detector = symmetric_group(symmetric_degree)
    identity = identity_permutation(tuple_count)
    assignment_count = 0
    for word in reduced_free_words(law_arity, max_length):
        if not is_law_on_group(detector, word, arity=law_arity):
            continue
        for assignment in product(subgroup, repeat=law_arity):
            assignment_count += 1
            if max_assignments is not None and assignment_count > max_assignments:
                return PointPushingVarietyEscapeAudit(
                    symmetric_degree=symmetric_degree,
                    point_pushing_arity=point_pushing_arity,
                    law_arity=law_arity,
                    braid_index=n,
                    tuple_count=tuple_count,
                    action_image_size=len(subgroup),
                    truncated=True,
                    assignment_count_checked=assignment_count - 1,
                    separating_word=None,
                    assignment_representatives=tuple(),
                    substituted_point_pushing_word=None,
                    evaluated_permutation=None,
                    direct_braid_permutation=None,
                    moved_index=None,
                    substituted_word_is_symmetric_law=None,
                )
            evaluated = evaluate_free_word_on_permutations(
                word,
                {index: value for index, value in enumerate(assignment)},
            )
            if evaluated == identity:
                continue
            representatives = tuple(subgroup_words[value] for value in assignment)
            substituted = substitute_free_word(word, representatives)
            braid_n, braid = law_word_on_last_strand(
                substituted,
                point_pushing_arity,
            )
            direct = braid_word_permutation_image(solution, braid_n, braid)
            moved_index = next(
                index
                for index, image in enumerate(evaluated)
                if image != index
            )
            return PointPushingVarietyEscapeAudit(
                symmetric_degree=symmetric_degree,
                point_pushing_arity=point_pushing_arity,
                law_arity=law_arity,
                braid_index=n,
                tuple_count=tuple_count,
                action_image_size=len(subgroup),
                truncated=False,
                assignment_count_checked=assignment_count,
                separating_word=word,
                assignment_representatives=representatives,
                substituted_point_pushing_word=substituted,
                evaluated_permutation=evaluated,
                direct_braid_permutation=direct,
                moved_index=moved_index,
                substituted_word_is_symmetric_law=is_law_on_group(
                    detector,
                    substituted,
                    arity=point_pushing_arity,
                ),
            )

    return PointPushingVarietyEscapeAudit(
        symmetric_degree=symmetric_degree,
        point_pushing_arity=point_pushing_arity,
        law_arity=law_arity,
        braid_index=n,
        tuple_count=tuple_count,
        action_image_size=len(subgroup),
        truncated=False,
        assignment_count_checked=assignment_count,
        separating_word=None,
        assignment_representatives=tuple(),
        substituted_point_pushing_word=None,
        evaluated_permutation=None,
        direct_braid_permutation=None,
        moved_index=None,
        substituted_word_is_symmetric_law=None,
    )


def point_pushing_variety_prefix_audit(
    solution: FiniteBraidedSet,
    symmetric_degree: int,
    max_point_pushing_arity: int,
    *,
    law_arity: int,
    max_length: int,
    max_subgroup_size: int | None = None,
    max_assignments_per_row: int | None = None,
) -> PointPushingVarietyPrefixAudit:
    """Run bounded point-pushing variety escape checks for arities ``1..K``."""

    if max_point_pushing_arity < 1:
        raise ValueError("max_point_pushing_arity must be positive")
    rows = tuple(
        point_pushing_variety_escape_audit(
            solution,
            symmetric_degree,
            arity,
            law_arity=law_arity,
            max_length=max_length,
            max_subgroup_size=max_subgroup_size,
            max_assignments=max_assignments_per_row,
        )
        for arity in range(1, max_point_pushing_arity + 1)
    )
    return PointPushingVarietyPrefixAudit(
        symmetric_degree=symmetric_degree,
        max_point_pushing_arity=max_point_pushing_arity,
        law_arity=law_arity,
        max_length=max_length,
        rows=rows,
    )


def _free_word_power_word(word: FreeWord, exponent: int) -> FreeWord:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    from .group_laws import multiply_free_words

    out: FreeWord = tuple()
    for _ in range(exponent):
        out = multiply_free_words(out, word)
    return out


def point_pushing_exponent_escape_audit(
    solution: FiniteBraidedSet,
    law_bound: int,
    point_pushing_arity: int,
    *,
    max_subgroup_size: int | None = None,
) -> PointPushingExponentEscapeAudit:
    """Audit one exponent-law point-pushing action escape.

    If an element of ``P_k(X)`` has order not dividing ``lcm(1,...,j)``, a
    representative word for that element, raised to this lcm, is a law on
    every group of order at most ``j`` but moves the YBE action.  This does
    *not* by itself certify finite-longitude invisibility: the returned row
    also records whether the corresponding braid has identity longitude data
    in ``S_j``.  Rows with ``exposes_naive_law_gap`` true are counterexamples
    to the naive implication "word law => point-pushing braid in K_G".
    """

    from .braid_laws import law_word_on_last_strand, pure_braid_generator
    from .artin_longitudes import has_identity_longitude_signature_streamed
    from .finite_group import symmetric_group
    from .group_laws import lcm_upto

    if law_bound < 1:
        raise ValueError("law_bound must be positive")
    if point_pushing_arity < 1:
        raise ValueError("point_pushing_arity must be positive")

    exponent_bound = lcm_upto(law_bound)
    n = point_pushing_arity + 1
    tuple_count = len(solution.elements) ** n
    generator_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(point_pushing_arity)
    }
    images = braid_images_for_words(solution, n, generator_braids)
    try:
        subgroup_words = generated_permutation_subgroup_with_words(
            images,
            max_size=max_subgroup_size,
        )
    except ValueError:
        return PointPushingExponentEscapeAudit(
            law_bound=law_bound,
            point_pushing_arity=point_pushing_arity,
            exponent_bound=exponent_bound,
            braid_index=n,
            tuple_count=tuple_count,
            action_image_size=None,
            truncated=True,
            escaping_element_order=None,
            escaping_element_word=None,
            exponent_law_word=None,
            evaluated_permutation=None,
            direct_braid_permutation=None,
            symmetric_identity_longitude_signature=None,
            moved_index=None,
        )

    identity = identity_permutation(tuple_count)
    for element, representative in subgroup_words.items():
        order = permutation_order(element)
        if exponent_bound % order == 0:
            continue
        exponent_word = _free_word_power_word(representative, exponent_bound)
        evaluated = evaluate_free_word_on_permutations(exponent_word, images)
        if evaluated == identity:
            continue
        braid_n, braid = law_word_on_last_strand(
            exponent_word,
            point_pushing_arity,
        )
        direct = braid_word_permutation_image(solution, braid_n, braid)
        symmetric_identity = has_identity_longitude_signature_streamed(
            symmetric_group(law_bound),
            braid_n,
            braid,
        )
        moved_index = next(
            index for index, image in enumerate(evaluated) if image != index
        )
        return PointPushingExponentEscapeAudit(
            law_bound=law_bound,
            point_pushing_arity=point_pushing_arity,
            exponent_bound=exponent_bound,
            braid_index=n,
            tuple_count=tuple_count,
            action_image_size=len(subgroup_words),
            truncated=False,
            escaping_element_order=order,
            escaping_element_word=representative,
            exponent_law_word=exponent_word,
            evaluated_permutation=evaluated,
            direct_braid_permutation=direct,
            symmetric_identity_longitude_signature=symmetric_identity,
            moved_index=moved_index,
        )

    return PointPushingExponentEscapeAudit(
        law_bound=law_bound,
        point_pushing_arity=point_pushing_arity,
        exponent_bound=exponent_bound,
        braid_index=n,
        tuple_count=tuple_count,
        action_image_size=len(subgroup_words),
        truncated=False,
        escaping_element_order=None,
        escaping_element_word=None,
        exponent_law_word=None,
        evaluated_permutation=None,
        direct_braid_permutation=None,
        symmetric_identity_longitude_signature=None,
        moved_index=None,
    )


def pure_generator_order_profile(
    solution: FiniteBraidedSet, max_q: int
) -> Tuple[PureGeneratorOrderRow, ...]:
    from .braid_laws import pure_braid_generator

    rows = []
    for q in range(2, max_q + 1):
        orders = tuple(
            permutation_order(action_permutation(solution, q, pure_braid_generator(i, q)))
            for i in range(1, q)
        )
        rows.append(
            PureGeneratorOrderRow(
                braid_index=q,
                tuple_count=len(solution.elements) ** q,
                generator_orders=orders,
                max_order=max(orders) if orders else 1,
            )
        )
    return tuple(rows)


def pure_subgroup_growth_profile(
    solution: FiniteBraidedSet,
    max_q: int,
    *,
    max_subgroup_size: int,
    max_tuple_count: int | None = None,
) -> Tuple[PureSubgroupGrowthRow, ...]:
    from .braid_laws import pure_braid_generator

    rows = []
    for q in range(2, max_q + 1):
        tuple_count = len(solution.elements) ** q
        if max_tuple_count is not None and tuple_count > max_tuple_count:
            rows.append(
                PureSubgroupGrowthRow(
                    braid_index=q,
                    tuple_count=tuple_count,
                    generator_count=q - 1,
                    subgroup_size=None,
                    subgroup_exponent=None,
                    truncated=True,
                )
            )
            continue
        pure_generators = {i - 1: pure_braid_generator(i, q) for i in range(1, q)}
        images = braid_images_for_words(solution, q, pure_generators)
        try:
            subgroup = generated_permutation_subgroup(
                images.values(), max_size=max_subgroup_size
            )
            from .group_laws import lcm

            exponent = 1
            for permutation in subgroup:
                exponent = lcm(exponent, permutation_order(permutation))
            rows.append(
                PureSubgroupGrowthRow(
                    braid_index=q,
                    tuple_count=tuple_count,
                    generator_count=len(images),
                    subgroup_size=len(subgroup),
                    subgroup_exponent=exponent,
                    truncated=False,
                )
            )
        except ValueError:
            rows.append(
                PureSubgroupGrowthRow(
                    braid_index=q,
                    tuple_count=tuple_count,
                    generator_count=len(images),
                    subgroup_size=None,
                    subgroup_exponent=None,
                    truncated=True,
                )
            )
    return tuple(rows)
