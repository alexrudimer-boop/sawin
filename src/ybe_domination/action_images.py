from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, product
from typing import Iterable, Mapping, Sequence, Tuple

from .artin_longitudes import BraidWord, FreeWord, NormalizedLawPrefixWitnessAudit
from .finite_braided_set import FiniteBraidedSet, rack_solution
from .finite_group import (
    FiniteGroup,
    commutator_subgroup_elements,
    is_abelian_group,
    subgroup_generated_elements,
)
from .green_branch import (
    Transformation,
    TransformationMonoid,
    compose_transformations,
    coordinate_action_maps,
    identity_transformation,
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
class RackPointPushingOperatorLabelAudit:
    """Checked rack point-pushing operator-label extension in one arity."""

    arity: int
    braid_index: int
    tuple_count: int
    operator_label_tuple_count: int
    inner_group_order: int
    inner_group_exponent: int
    point_pushing_group_order: int | None
    point_pushing_group_exponent: int | None
    hurwitz_quotient_order: int | None
    vertical_kernel_size: int | None
    vertical_kernel_exponent: int | None
    operator_label_action_well_defined: bool
    quotient_map_well_defined: bool | None
    vertical_exponent_divides_inner_exponent: bool | None
    truncated: bool

    @property
    def verifies_rack_operator_label_extension(self) -> bool:
        return (
            not self.truncated
            and self.operator_label_action_well_defined
            and self.quotient_map_well_defined is True
            and self.vertical_exponent_divides_inner_exponent is True
        )


@dataclass(frozen=True)
class PointPushingGeneratorRow:
    """One standard last-strand point-pushing generator."""

    point_pushing_arity: int
    braid_index: int
    generator_index: int
    braid_word: BraidWord


@dataclass(frozen=True)
class FiniteAugmentedArtinEnvelopeRouteAudit:
    """Symbolic route ledger for the point-pushing theorem strategy.

    The rack-side operator-label extension is proved separately by the
    rack note and finite-prefix audit.  This ledger records the exact
    theorem route left after that correction: prove a finite augmented
    Artin envelope for arbitrary finite bijective YBE solutions, then
    realize compatible envelopes by finite racks.
    """

    rack_operator_label_exact_sequence_recorded: bool
    rack_vertical_kernel_bound_recorded: bool
    whole_point_pushing_exponent_bound_rejected: bool
    domination_transfers_marked_point_pushing_quotients: bool
    missing_augmented_envelope_lemma: str
    missing_realization_lemma: str
    obstruction_arities: Tuple[int, ...]
    generator_rows: Tuple[PointPushingGeneratorRow, ...]
    obstruction_requires_all_fixed_group_hurwitz_bases: bool
    bounded_vertical_extension_is_live_invariant: bool

    @property
    def rack_side_invariant_is_ready(self) -> bool:
        return (
            self.rack_operator_label_exact_sequence_recorded
            and self.rack_vertical_kernel_bound_recorded
            and self.whole_point_pushing_exponent_bound_rejected
            and self.domination_transfers_marked_point_pushing_quotients
        )

    @property
    def remaining_theorem_lemmas(self) -> Tuple[str, str]:
        return (self.missing_augmented_envelope_lemma, self.missing_realization_lemma)

    @property
    def has_first_obstruction_prefix(self) -> bool:
        expected_count = sum(self.obstruction_arities)
        return (
            self.obstruction_arities == (3, 4)
            and len(self.generator_rows) == expected_count
            and all(row.braid_index == row.point_pushing_arity + 1 for row in self.generator_rows)
        )

    @property
    def records_route_one_pressure_test(self) -> bool:
        return (
            self.rack_side_invariant_is_ready
            and self.has_first_obstruction_prefix
            and self.obstruction_requires_all_fixed_group_hurwitz_bases
            and self.bounded_vertical_extension_is_live_invariant
        )


@dataclass(frozen=True)
class FiniteAugmentedArtinEnvelopePressureCase:
    """One positive obligation or negative failure mode for the envelope lemma."""

    key: str
    role: str
    label_object: str
    required_identity_or_failure: str
    first_probe: str

    @property
    def is_positive_obligation(self) -> bool:
        return self.role in {"proved_baseline", "positive_candidate"}

    @property
    def is_failure_mechanism(self) -> bool:
        return self.role == "negative_mechanism"


@dataclass(frozen=True)
class FiniteAugmentedArtinEnvelopePressureAudit:
    """Pressure-test ledger for the augmented Artin-envelope lemma."""

    route: FiniteAugmentedArtinEnvelopeRouteAudit
    cases: Tuple[FiniteAugmentedArtinEnvelopePressureCase, ...]

    @property
    def case_count(self) -> int:
        return len(self.cases)

    @property
    def positive_obligation_count(self) -> int:
        return sum(1 for case in self.cases if case.is_positive_obligation)

    @property
    def failure_mechanism_count(self) -> int:
        return sum(1 for case in self.cases if case.is_failure_mechanism)

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_true_or_false_mechanisms(self) -> bool:
        return (
            self.route.records_route_one_pressure_test
            and self.positive_obligation_count >= 2
            and self.failure_mechanism_count >= 3
            and "whole_exponent_growth" not in self.case_keys
        )


@dataclass(frozen=True)
class DerivedEnvelopePreimageFailure:
    """One obstruction to the derived Hurwitz operation being total."""

    derived_left_label: object
    original_left_label: object
    kind: str
    preimages: Tuple[object, ...]
    candidate_outputs: Tuple[Tuple[object, object], ...]


@dataclass(frozen=True)
class DerivedHurwitzEnvelopeAudit:
    """Audit the guitar-derived Hurwitz envelope for one finite solution."""

    element_count: int
    left_nondegenerate: bool
    right_nondegenerate: bool
    nondegenerate: bool
    derived_operation_total: bool
    derived_rack_ybe: bool
    two_strand_guitar_conjugacy: bool
    three_strand_guitar_conjugacy: bool
    interior_forgetting_unaugmented_matches: bool | None
    prefix_left_group_order: int | None
    recorded_preimage_failures: Tuple[DerivedEnvelopePreimageFailure, ...]

    @property
    def preimage_failure_count(self) -> int:
        return len(self.recorded_preimage_failures)

    @property
    def proves_nondegenerate_derived_hurwitz_envelope_prefix(self) -> bool:
        return (
            self.nondegenerate
            and self.derived_operation_total
            and self.derived_rack_ybe
            and self.two_strand_guitar_conjugacy
            and self.three_strand_guitar_conjugacy
            and self.prefix_left_group_order is not None
        )

    @property
    def detects_degenerate_derived_operation_failure(self) -> bool:
        return not self.derived_operation_total and self.preimage_failure_count > 0


@dataclass(frozen=True)
class PreimageMemoryFibre:
    """One fibre of the degenerate derived-operation preimage relation."""

    derived_left_label: object
    original_left_label: object
    preimages: Tuple[object, ...]
    candidate_outputs: Tuple[Tuple[object, object], ...]
    status: str


@dataclass(frozen=True)
class DegeneratePreimageMemoryAudit:
    """Audit the finite edge-memory repair for preimage ambiguity."""

    element_count: int
    visible_pair_count: int
    edge_memory_state_count: int
    singleton_fibre_count: int
    missing_fibre_count: int
    multiple_same_candidate_count: int
    ambiguous_candidate_count: int
    visible_derived_operation_total: bool
    finite_edge_memory_repairs_two_strand: bool
    tower_consistency_status: str
    recorded_fibres: Tuple[PreimageMemoryFibre, ...]

    @property
    def hidden_preimage_memory_needed(self) -> bool:
        return (
            self.missing_fibre_count
            + self.multiple_same_candidate_count
            + self.ambiguous_candidate_count
            > 0
        )

    @property
    def visible_compression_is_safe(self) -> bool:
        return (
            self.visible_derived_operation_total
            and self.missing_fibre_count == 0
            and self.ambiguous_candidate_count == 0
        )

    @property
    def records_degenerate_memory_gate(self) -> bool:
        return (
            self.edge_memory_state_count == self.element_count * self.element_count
            and self.finite_edge_memory_repairs_two_strand
            and self.tower_consistency_status == "requires_triple_quadruple_check"
        )


@dataclass(frozen=True)
class EdgeMemoryTowerAudit:
    """Audit braid and forgetting consistency for adjacent edge memory."""

    element_count: int
    edge_label_count: int
    arity3_tuple_count: int
    arity4_tuple_count: int
    arity3_encoding_injective: bool
    arity4_encoding_injective: bool
    braid_relation_on_edge_memory: bool
    generator_updates_well_defined: Tuple[Tuple[int, bool], ...]
    point_forgetting_well_defined: Tuple[Tuple[int, bool], ...]
    records_finite_edge_memory_tower_prefix: bool

    @property
    def all_generator_updates_well_defined(self) -> bool:
        return all(value for _index, value in self.generator_updates_well_defined)

    @property
    def all_point_forgetting_maps_well_defined(self) -> bool:
        return all(value for _index, value in self.point_forgetting_well_defined)

    @property
    def verifies_edge_memory_triple_quadruple_prefix(self) -> bool:
        return (
            self.arity3_encoding_injective
            and self.arity4_encoding_injective
            and self.braid_relation_on_edge_memory
            and self.all_generator_updates_well_defined
            and self.all_point_forgetting_maps_well_defined
            and self.records_finite_edge_memory_tower_prefix
        )


@dataclass(frozen=True)
class PrefixEdgeTransducerAudit:
    """Audit the finite left-prefix edge transducer for degenerate rows."""

    element_count: int
    left_prefix_monoid_size: int
    edge_state_count: int
    arity3_path_count: int
    arity4_path_count: int
    arity3_encoding_injective: bool
    arity4_encoding_injective: bool
    left_prefix_identity_holds: bool
    generator_updates_bijective: Tuple[Tuple[int, bool], ...]
    braid_relation_on_prefix_paths: bool
    point_forgetting_well_defined: Tuple[Tuple[int, bool], ...]
    point_forgetting_max_fibre_sizes: Tuple[Tuple[int, int], ...]
    forgetting_fibres_bounded_by_element_count: bool
    records_prefix_edge_transducer_tower: bool

    @property
    def all_generator_updates_bijective(self) -> bool:
        return all(value for _index, value in self.generator_updates_bijective)

    @property
    def all_point_forgetting_maps_well_defined(self) -> bool:
        return all(value for _index, value in self.point_forgetting_well_defined)

    @property
    def verifies_prefix_edge_transducer_prefix(self) -> bool:
        return (
            self.arity3_encoding_injective
            and self.arity4_encoding_injective
            and self.left_prefix_identity_holds
            and self.all_generator_updates_bijective
            and self.braid_relation_on_prefix_paths
            and self.all_point_forgetting_maps_well_defined
            and self.forgetting_fibres_bounded_by_element_count
            and self.records_prefix_edge_transducer_tower
        )


@dataclass(frozen=True)
class PrefixGroupHurwitzCompressionPressureAudit:
    """Finite ledger for compressing prefix memory to group-Hurwitz labels."""

    element_count: int
    left_prefix_monoid_size: int
    edge_state_count: int
    nonunit_prefix_count: int
    faithful_prefix_monoid_group_embedding_obstructed: bool
    local_hurwitz_label_equation_count: int
    product_invariance_equation_count: int
    forgetting_rescan_lumpability_equation_count: int
    first_obstruction_arities: Tuple[int, int]
    requires_group_label_map: bool
    requires_conjugation_stable_image: bool
    requires_local_hurwitz_descend: bool
    requires_total_product_invariance: bool
    requires_forgetting_rescan_lumpability: bool
    bounded_vertical_kernel_still_unproved: bool
    finite_transducer_alone_is_not_group_hurwitz: bool

    @property
    def records_group_hurwitz_compression_pressure(self) -> bool:
        return (
            self.requires_group_label_map
            and self.requires_conjugation_stable_image
            and self.requires_local_hurwitz_descend
            and self.requires_total_product_invariance
            and self.requires_forgetting_rescan_lumpability
            and self.bounded_vertical_kernel_still_unproved
            and self.finite_transducer_alone_is_not_group_hurwitz
            and self.first_obstruction_arities == (3, 4)
        )


@dataclass(frozen=True)
class PrefixPointPushingSurfaceRow:
    """One concrete ``Q_X(n)`` prefix-transducer obstruction surface row."""

    point_pushing_arity: int
    braid_index: int
    tuple_count: int
    prefix_path_count: int
    prefix_encoding_injective: bool
    generator_count: int
    generator_braid_words: Tuple[BraidWord, ...]
    generator_orders: Tuple[int, ...]
    point_pushing_group_size: int | None
    point_pushing_group_exponent: int | None
    prefix_action_matches_tuple_action: bool
    truncated: bool

    @property
    def computed_untruncated_surface(self) -> bool:
        return (
            not self.truncated
            and self.prefix_encoding_injective
            and self.prefix_action_matches_tuple_action
            and self.point_pushing_group_size is not None
            and self.point_pushing_group_exponent is not None
        )


@dataclass(frozen=True)
class PrefixPointPushingSurfaceAudit:
    """Concrete ``Q_X(3),Q_X(4)`` surface for prefix transducer compression."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    rows: Tuple[PrefixPointPushingSurfaceRow, ...]
    records_first_group_hurwitz_obstruction_surface: bool

    @property
    def checked_arities(self) -> Tuple[int, ...]:
        return tuple(row.point_pushing_arity for row in self.rows)

    @property
    def all_rows_untruncated(self) -> bool:
        return all(row.computed_untruncated_surface for row in self.rows)

    @property
    def verifies_prefix_point_pushing_surface(self) -> bool:
        return (
            self.checked_arities == (3, 4)
            and self.all_rows_untruncated
            and self.records_first_group_hurwitz_obstruction_surface
        )


@dataclass(frozen=True)
class PrefixArtinEnvelopeCohomologyRow:
    """One action-groupoid row for finite Artin-envelope cohomology pressure."""

    point_pushing_arity: int
    braid_index: int
    tuple_count: int
    generator_count: int
    point_pushing_group_size: int | None
    point_pushing_group_exponent: int | None
    orbit_count: int | None
    max_orbit_size: int | None
    action_groupoid_arrow_count: int | None
    stabilizer_loop_arrow_count: int | None
    generator_cocycle_value_count: int
    restriction_to_previous_required: bool
    forgetting_naturality_square_count: int
    truncated: bool

    @property
    def computed_untruncated_cohomology_row(self) -> bool:
        return (
            not self.truncated
            and self.point_pushing_group_size is not None
            and self.point_pushing_group_exponent is not None
            and self.orbit_count is not None
            and self.max_orbit_size is not None
            and self.action_groupoid_arrow_count is not None
            and self.stabilizer_loop_arrow_count is not None
        )


@dataclass(frozen=True)
class PrefixArtinEnvelopeCohomologyAudit:
    """Finite ledger for the missing Artin-envelope cohomology lemma."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    operator_label_variable_count: int
    rows: Tuple[PrefixArtinEnvelopeCohomologyRow, ...]
    fixed_finite_hurwitz_base_required: bool
    vertical_cocycle_bounded_exponent_required: bool
    quotient_groupoid_functor_required: bool
    tower_restriction_compatibility_required: bool
    finite_surface_only: bool

    @property
    def checked_arities(self) -> Tuple[int, ...]:
        return tuple(row.point_pushing_arity for row in self.rows)

    @property
    def all_rows_untruncated(self) -> bool:
        return all(row.computed_untruncated_cohomology_row for row in self.rows)

    @property
    def records_artin_envelope_cohomology_pressure(self) -> bool:
        return (
            self.checked_arities == (3, 4)
            and self.fixed_finite_hurwitz_base_required
            and self.vertical_cocycle_bounded_exponent_required
            and self.quotient_groupoid_functor_required
            and self.tower_restriction_compatibility_required
            and self.finite_surface_only
        )


@dataclass(frozen=True)
class PrefixPointForgettingRestrictionRow:
    """One marked generator comparison under stationary-strand deletion."""

    source_point_pushing_arity: int
    source_braid_index: int
    target_point_pushing_arity: int
    target_braid_index: int
    forget_stationary_index: int
    source_generator_index: int
    target_generator_index: int | None
    source_braid_word: BraidWord
    target_braid_word: BraidWord
    tuple_count: int
    expected_identity_after_forgetting: bool
    matches_marked_restriction: bool
    mismatch_count: int
    first_witness_input: Tuple[object, ...] | None
    first_deleted_after_source: Tuple[object, ...] | None
    first_expected_target: Tuple[object, ...] | None

    @property
    def vertical_cocycle_visible(self) -> bool:
        return self.mismatch_count > 0

    @property
    def diagonal_forgetting_row(self) -> bool:
        return self.forget_stationary_index == self.source_generator_index


@dataclass(frozen=True)
class PrefixPointForgettingRestrictionAudit:
    """First marked point-forgetting surface for vertical cocycle pressure."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    source_point_pushing_arity: int
    target_point_pushing_arity: int
    rows: Tuple[PrefixPointForgettingRestrictionRow, ...]
    records_first_point_forgetting_restriction_surface: bool

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def total_mismatch_count(self) -> int:
        return sum(row.mismatch_count for row in self.rows)

    @property
    def diagonal_mismatch_count(self) -> int:
        return sum(
            row.mismatch_count
            for row in self.rows
            if row.diagonal_forgetting_row
        )

    @property
    def off_diagonal_all_match(self) -> bool:
        return all(
            row.matches_marked_restriction
            for row in self.rows
            if not row.diagonal_forgetting_row
        )

    @property
    def all_rows_match(self) -> bool:
        return all(row.matches_marked_restriction for row in self.rows)

    @property
    def verifies_first_point_forgetting_restriction_surface(self) -> bool:
        return (
            self.source_point_pushing_arity == 4
            and self.target_point_pushing_arity == 3
            and self.row_count == 16
            and self.records_first_point_forgetting_restriction_surface
        )


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

    @property
    def checked_arity_prefix_complete(self) -> bool:
        return self.checked_arities == tuple(range(1, self.max_arity + 1))

    @property
    def proves_all_arity_marked_quotients(self) -> bool:
        """Finite prefix data never proves the all-arity quotient tower."""

        return False

    @property
    def remaining_all_arity_obligation(self) -> str:
        if self.first_failure_kind is not None:
            return self.first_failure_kind
        return "symbolic_all_arity_argument"


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
    transport_residual_quotient_order: int
    transport_residual_abelianization_order: int
    transport_residual_abelianization_exponent: int
    transport_residual_abelianization_prime_set: Tuple[int, ...]
    transport_residual_abelianization_exponent_divides_bound: bool
    transport_residual_prime_support_bounded: bool
    transport_residual_is_perfect: bool
    transport_residual_regime: str
    quotient_abelianization_order: int
    quotient_abelianization_exponent: int
    quotient_abelianization_is_cyclic: bool
    generator_abelianization_order: int
    generator_generates_quotient_abelianization: bool
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


def _rack_left_translation_permutations(
    rack: FiniteBraidedSet,
) -> Mapping[object, Permutation]:
    index = {element: position for position, element in enumerate(rack.elements)}
    translations = {}
    for left in rack.elements:
        images = []
        for right in rack.elements:
            first, second = rack.R[(left, right)]
            if second != left:
                raise ValueError("solution is not in rack form R(a,b)=(a*b,a)")
            images.append(index[first])
        permutation = tuple(images)
        if set(permutation) != set(range(len(rack.elements))):
            raise ValueError("left rack translation is not bijective")
        translations[left] = permutation
    return translations


def _rack_operator_label_generator_images(
    rack: FiniteBraidedSet,
    arity: int,
    action_images: Mapping[int, Permutation],
) -> tuple[bool, int, Mapping[int, Permutation]]:
    braid_index = arity + 1
    translations = _rack_left_translation_permutations(rack)
    tuple_values = tuple(product(rack.elements, repeat=braid_index))
    labels_by_tuple_index = tuple(
        tuple(translations[element] for element in tuple_value)
        for tuple_value in tuple_values
    )
    label_tuples = tuple(sorted(set(labels_by_tuple_index), key=repr))
    label_index = {label: position for position, label in enumerate(label_tuples)}
    label_images = {}

    for generator, action in action_images.items():
        image_by_label: list[int | None] = [None] * len(label_tuples)
        for tuple_index, source_label in enumerate(labels_by_tuple_index):
            target_label = labels_by_tuple_index[action[tuple_index]]
            source_index = label_index[source_label]
            target_index = label_index[target_label]
            previous = image_by_label[source_index]
            if previous is None:
                image_by_label[source_index] = target_index
            elif previous != target_index:
                return False, len(label_tuples), {}
        if any(value is None for value in image_by_label):
            return False, len(label_tuples), {}
        label_images[generator] = tuple(value for value in image_by_label if value is not None)
    return True, len(label_tuples), label_images


def rack_point_pushing_operator_label_audit(
    rack: FiniteBraidedSet,
    arity: int,
    *,
    max_size: int | None = None,
) -> RackPointPushingOperatorLabelAudit:
    """Check the rack operator-label quotient for one point-pushing arity.

    The rack convention is ``R(a,b)=(a*b,a)``.  The checked group is generated
    by the standard last-strand pure braids ``A_{i,n+1}``, ``1<=i<=n``.  The
    quotient is the induced action on tuples of left translations
    ``(L_{y_1},...,L_{y_{n+1}})``; the vertical kernel consists of elements
    acting trivially on those operator labels.
    """

    if arity < 1:
        raise ValueError("arity must be positive")

    from .artin_longitudes import rack_inner_group
    from .group_laws import group_exponent, lcm

    braid_index = arity + 1
    tuple_count = len(rack.elements) ** braid_index
    inner_group = rack_inner_group(rack)
    inner_exponent = group_exponent(inner_group)
    action_images = _point_pushing_action_generator_images(rack, arity)
    label_well_defined, label_tuple_count, label_images = (
        _rack_operator_label_generator_images(rack, arity, action_images)
    )
    if not label_well_defined:
        return RackPointPushingOperatorLabelAudit(
            arity=arity,
            braid_index=braid_index,
            tuple_count=tuple_count,
            operator_label_tuple_count=label_tuple_count,
            inner_group_order=len(inner_group.elements),
            inner_group_exponent=inner_exponent,
            point_pushing_group_order=None,
            point_pushing_group_exponent=None,
            hurwitz_quotient_order=None,
            vertical_kernel_size=None,
            vertical_kernel_exponent=None,
            operator_label_action_well_defined=False,
            quotient_map_well_defined=None,
            vertical_exponent_divides_inner_exponent=None,
            truncated=False,
        )

    pair_generators = {
        generator: (action_images[generator], label_images[generator])
        for generator in sorted(action_images)
    }
    try:
        pair_subgroup = _generated_pair_subgroup_with_words(
            pair_generators,
            max_size=max_size,
        )
    except ValueError:
        return RackPointPushingOperatorLabelAudit(
            arity=arity,
            braid_index=braid_index,
            tuple_count=tuple_count,
            operator_label_tuple_count=label_tuple_count,
            inner_group_order=len(inner_group.elements),
            inner_group_exponent=inner_exponent,
            point_pushing_group_order=None,
            point_pushing_group_exponent=None,
            hurwitz_quotient_order=None,
            vertical_kernel_size=None,
            vertical_kernel_exponent=None,
            operator_label_action_well_defined=True,
            quotient_map_well_defined=None,
            vertical_exponent_divides_inner_exponent=None,
            truncated=True,
        )

    action_to_label: dict[Permutation, Permutation] = {}
    quotient_map_well_defined = True
    for action, label in pair_subgroup:
        previous = action_to_label.get(action)
        if previous is None:
            action_to_label[action] = label
        elif previous != label:
            quotient_map_well_defined = False

    actions = tuple(action_to_label)
    labels = tuple(sorted(set(action_to_label.values())))
    point_exponent = 1
    for action in actions:
        point_exponent = lcm(point_exponent, permutation_order(action))

    vertical_kernel = None
    vertical_exponent = None
    vertical_divides = None
    if quotient_map_well_defined:
        label_identity = identity_permutation(label_tuple_count)
        vertical_kernel = tuple(
            action for action, label in action_to_label.items() if label == label_identity
        )
        vertical_exponent = 1
        for action in vertical_kernel:
            vertical_exponent = lcm(vertical_exponent, permutation_order(action))
        vertical_divides = inner_exponent % vertical_exponent == 0

    return RackPointPushingOperatorLabelAudit(
        arity=arity,
        braid_index=braid_index,
        tuple_count=tuple_count,
        operator_label_tuple_count=label_tuple_count,
        inner_group_order=len(inner_group.elements),
        inner_group_exponent=inner_exponent,
        point_pushing_group_order=len(actions),
        point_pushing_group_exponent=point_exponent,
        hurwitz_quotient_order=len(labels),
        vertical_kernel_size=None if vertical_kernel is None else len(vertical_kernel),
        vertical_kernel_exponent=vertical_exponent,
        operator_label_action_well_defined=True,
        quotient_map_well_defined=quotient_map_well_defined,
        vertical_exponent_divides_inner_exponent=vertical_divides,
        truncated=False,
    )


def finite_augmented_artin_envelope_route_audit(
    obstruction_arities: Sequence[int] = (3, 4),
) -> FiniteAugmentedArtinEnvelopeRouteAudit:
    """Record the corrected point-pushing route and its first finite tests.

    The live invariant is not a uniform exponent bound for the whole
    point-pushing image.  It is a fixed finite group-Hurwitz base with
    bounded-exponent vertical noise.  The returned rows spell out the
    standard generators ``alpha_{i,n+1}`` for the first obstruction arities
    so finite computations use the same Fadell-Neuwirth convention.
    """

    from .braid_laws import pure_braid_generator

    rows = []
    arities = tuple(obstruction_arities)
    for arity in arities:
        if arity < 1:
            raise ValueError("obstruction arities must be positive")
        braid_index = arity + 1
        rows.extend(
            PointPushingGeneratorRow(
                point_pushing_arity=arity,
                braid_index=braid_index,
                generator_index=generator,
                braid_word=pure_braid_generator(generator, braid_index),
            )
            for generator in range(1, arity + 1)
        )
    return FiniteAugmentedArtinEnvelopeRouteAudit(
        rack_operator_label_exact_sequence_recorded=True,
        rack_vertical_kernel_bound_recorded=True,
        whole_point_pushing_exponent_bound_rejected=True,
        domination_transfers_marked_point_pushing_quotients=True,
        missing_augmented_envelope_lemma="finite augmented Artin-envelope lemma",
        missing_realization_lemma="finite rack realization of compatible augmented Artin-envelope towers",
        obstruction_arities=arities,
        generator_rows=tuple(rows),
        obstruction_requires_all_fixed_group_hurwitz_bases=True,
        bounded_vertical_extension_is_live_invariant=True,
    )


def finite_augmented_artin_envelope_pressure_audit(
) -> FiniteAugmentedArtinEnvelopePressureAudit:
    """List the exact mechanisms that can prove or refute the route.

    This is a theorem-route ledger.  It deliberately omits whole-image
    exponent growth, because finite racks already allow that in the
    group-Hurwitz quotient.  The live checks are well-defined finite labels,
    coordinatewise vertical action in one fixed finite group, compatibility
    under point-forgetting, and bounded vertical exponent.
    """

    route = finite_augmented_artin_envelope_route_audit()
    cases = (
        FiniteAugmentedArtinEnvelopePressureCase(
            key="rack_operator_conjugation_baseline",
            role="proved_baseline",
            label_object="C={L_y:y in Y} inside H=Inn(Y)",
            required_identity_or_failure=(
                "L_{y*z}=L_y L_z L_y^{-1}; pure Artin conjugacy words "
                "evaluate coordinatewise in H over each fixed label fibre"
            ),
            first_probe=(
                "rack_point_pushing_operator_label_audit at arities 3 and 4; "
                "check vertical exponent divides exp Inn(Y)"
            ),
        ),
        FiniteAugmentedArtinEnvelopePressureCase(
            key="translation_pair_label_candidate",
            role="positive_candidate",
            label_object=(
                "labels generated by (lambda_x,rho_x) in Sym(X) x Sym(X)"
            ),
            required_identity_or_failure=(
                "the labels of lambda_x(y) and rho_y(x) must be functions "
                "of the two incoming labels, and pure braid coordinate "
                "maps must evaluate in one fixed finite permutation group"
            ),
            first_probe=(
                "on X^4 and X^5, quotient point-pushing generator actions "
                "by translation-pair labels and test well-definedness of "
                "the induced marked quotient"
            ),
        ),
        FiniteAugmentedArtinEnvelopePressureCase(
            key="finite_structure_action_candidate",
            role="positive_candidate",
            label_object=(
                "a finite quotient of the structure-group or derived-action "
                "image acting on X"
            ),
            required_identity_or_failure=(
                "Artin words x_j -> u_j x_j u_j^{-1} must have a finite "
                "evaluation rule for each coordinate that is independent "
                "of braid index except through Hurwitz label motion"
            ),
            first_probe=(
                "compare the labels induced by alpha_{i,4} and alpha_{i,5}; "
                "the arity-5 labels must forget to the arity-4 labels"
            ),
        ),
        FiniteAugmentedArtinEnvelopePressureCase(
            key="nonconjugation_stable_label_failure",
            role="negative_mechanism",
            label_object="any proposed finite operator label quotient",
            required_identity_or_failure=(
                "two pairs with the same incoming labels produce different "
                "outgoing labels after one YBE crossing"
            ),
            first_probe=(
                "find x,y,x',y' with equal candidate labels but unequal "
                "labels of lambda_x(y) or rho_y(x)"
            ),
        ),
        FiniteAugmentedArtinEnvelopePressureCase(
            key="ordered_neighbor_memory_failure",
            role="negative_mechanism",
            label_object="candidate label tuples on X^m",
            required_identity_or_failure=(
                "a point-pushing word acts trivially on candidate labels but "
                "its coordinate action depends on ordered pass history not "
                "recoverable from a coordinatewise element of one fixed group"
            ),
            first_probe=(
                "inside Q_X(3), search the kernel of the label action for "
                "two equal label-fibre states with different vertical maps"
            ),
        ),
        FiniteAugmentedArtinEnvelopePressureCase(
            key="point_forgetting_incompatibility",
            role="negative_mechanism",
            label_object="normal vertical kernels V_X(n)",
            required_identity_or_failure=(
                "the normal vertical subgroups can be chosen in each arity "
                "separately but cannot be made compatible with P_{n+1}->P_n"
            ),
            first_probe=(
                "compare the marked images of alpha_{i,5} after forgetting "
                "one strand with the marked generators alpha_{i,4}"
            ),
        ),
        FiniteAugmentedArtinEnvelopePressureCase(
            key="unbounded_vertical_kernel_failure",
            role="negative_mechanism",
            label_object="kernel of every fixed finite label-Hurwitz quotient",
            required_identity_or_failure=(
                "elements acting trivially on every fixed label model have "
                "orders or nilpotent layers escaping every fixed exponent e"
            ),
            first_probe=(
                "compute candidate vertical kernels at Q_X(3) and Q_X(4); "
                "a real obstruction must continue as an all-n compatible "
                "escape, not just a large whole-image order"
            ),
        ),
    )
    return FiniteAugmentedArtinEnvelopePressureAudit(route=route, cases=cases)


def _left_translation_permutations(
    solution: FiniteBraidedSet,
) -> Mapping[object, Permutation] | None:
    index = {element: position for position, element in enumerate(solution.elements)}
    elements = set(solution.elements)
    translations = {}
    for left in solution.elements:
        images = tuple(solution.R[(left, right)][0] for right in solution.elements)
        if set(images) != elements:
            return None
        translations[left] = tuple(index[image] for image in images)
    return translations


def _is_right_nondegenerate(solution: FiniteBraidedSet) -> bool:
    elements = set(solution.elements)
    return all(
        {solution.R[(left, right)][1] for left in solution.elements} == elements
        for right in solution.elements
    )


def _left_translate(solution: FiniteBraidedSet, left: object, value: object) -> object:
    return solution.R[(left, value)][0]


def _guitar_label_tuple(
    solution: FiniteBraidedSet,
    tuple_value: Sequence[object],
) -> Tuple[object, ...]:
    prefix_labels = []
    for index, value in enumerate(tuple_value):
        label = value
        for left in tuple_value[:index]:
            label = _left_translate(solution, left, label)
        prefix_labels.append(label)
    return tuple(reversed(prefix_labels))


def derived_hurwitz_envelope_audit(
    solution: FiniteBraidedSet,
    *,
    max_left_group_size: int | None = None,
    max_recorded_failures: int = 8,
) -> DerivedHurwitzEnvelopeAudit:
    """Audit the guitar-derived Hurwitz envelope suggested by route (1).

    In the repository convention, the two-strand guitar map is
    ``J_2(x,y)=(lambda_x(y),x)``.  The derived rack operation is therefore
    defined by
    ``a*b=lambda_a(rho_y(b))`` where ``lambda_b(y)=a``.  The operation is
    total exactly when each such left preimage is unique.
    """

    elements = tuple(solution.elements)
    left_translations = _left_translation_permutations(solution)
    left_nondegenerate = left_translations is not None
    right_nondegenerate = _is_right_nondegenerate(solution)
    failures = []
    operation = {}
    for derived_left, original_left in product(elements, repeat=2):
        preimages = tuple(
            value
            for value in elements
            if solution.R[(original_left, value)][0] == derived_left
        )
        candidates = tuple(
            (
                preimage,
                _left_translate(
                    solution,
                    derived_left,
                    solution.R[(original_left, preimage)][1],
                ),
            )
            for preimage in preimages
        )
        if len(preimages) == 1:
            operation[(derived_left, original_left)] = candidates[0][1]
            continue
        if not preimages:
            kind = "missing_preimage"
        elif len({candidate for _preimage, candidate in candidates}) == 1:
            kind = "multiple_preimages_same_candidate"
        else:
            kind = "ambiguous_preimage_candidates"
        if len(failures) < max_recorded_failures:
            failures.append(
                DerivedEnvelopePreimageFailure(
                    derived_left_label=derived_left,
                    original_left_label=original_left,
                    kind=kind,
                    preimages=preimages,
                    candidate_outputs=candidates,
                )
            )

    derived = None
    derived_rack_ybe = False
    two_strand = False
    three_strand = False
    interior_forgetting = None
    prefix_group_order = None
    if not failures:
        try:
            derived = rack_solution(
                elements,
                lambda left, right: operation[(left, right)],
            )
        except ValueError:
            derived = None
        if derived is not None:
            derived_rack_ybe = derived.is_ybe()
            guitar_2 = {
                (left, right): _guitar_label_tuple(solution, (left, right))
                for left, right in product(elements, repeat=2)
            }
            two_strand = (
                set(guitar_2.values()) == set(guitar_2.keys())
                and all(
                    guitar_2[solution.R[(left, right)]]
                    == derived.R[guitar_2[(left, right)]]
                    for left, right in product(elements, repeat=2)
                )
            )
            if derived_rack_ybe:
                three_strand = True
                for tuple_value in product(elements, repeat=3):
                    for index in (0, 1):
                        derived_index = 1 - index
                        if (
                            _guitar_label_tuple(
                                solution,
                                solution.apply_R_at(tuple_value, index),
                            )
                            != derived.apply_R_at(
                                _guitar_label_tuple(solution, tuple_value),
                                derived_index,
                            )
                        ):
                            three_strand = False
                            break
                    if not three_strand:
                        break
                interior_forgetting = all(
                    (
                        _guitar_label_tuple(solution, (left, right))[0],
                        _guitar_label_tuple(solution, (left, right))[1],
                    )
                    == (
                        _guitar_label_tuple(solution, (left, middle, right))[0],
                        _guitar_label_tuple(solution, (left, middle, right))[2],
                    )
                    for left, middle, right in product(elements, repeat=3)
                )
            if left_translations is not None:
                prefix_group_order = len(
                    generated_permutation_subgroup(
                        left_translations.values(),
                        max_size=max_left_group_size,
                    )
                )

    return DerivedHurwitzEnvelopeAudit(
        element_count=len(elements),
        left_nondegenerate=left_nondegenerate,
        right_nondegenerate=right_nondegenerate,
        nondegenerate=left_nondegenerate and right_nondegenerate,
        derived_operation_total=not failures,
        derived_rack_ybe=derived_rack_ybe,
        two_strand_guitar_conjugacy=two_strand,
        three_strand_guitar_conjugacy=three_strand,
        interior_forgetting_unaugmented_matches=interior_forgetting,
        prefix_left_group_order=prefix_group_order,
        recorded_preimage_failures=tuple(failures),
    )


def degenerate_preimage_memory_audit(
    solution: FiniteBraidedSet,
    *,
    max_recorded_fibres: int = 12,
) -> DegeneratePreimageMemoryAudit:
    """Audit the canonical finite edge memory for degenerate preimages.

    A visible derived pair ``(a,b)`` asks for preimages ``y`` with
    ``lambda_b(y)=a``.  The nondegenerate derived rack route works exactly
    when every visible pair has one such ``y``.  The finite local repair is
    to retain the edge-memory state ``(a,b,y)`` for each actual pair
    ``(b,y)``.  This always has ``|X|^2`` states, but it is only a two-strand
    repair; a tower proof still needs triple/quadruple compatibility.
    """

    elements = tuple(solution.elements)
    fibres = []
    singleton = 0
    missing = 0
    multiple_same = 0
    ambiguous = 0
    for derived_left, original_left in product(elements, repeat=2):
        preimages = tuple(
            value
            for value in elements
            if solution.R[(original_left, value)][0] == derived_left
        )
        candidates = tuple(
            (
                preimage,
                _left_translate(
                    solution,
                    derived_left,
                    solution.R[(original_left, preimage)][1],
                ),
            )
            for preimage in preimages
        )
        if len(preimages) == 1:
            status = "singleton"
            singleton += 1
        elif not preimages:
            status = "missing"
            missing += 1
        elif len({candidate for _preimage, candidate in candidates}) == 1:
            status = "multiple_same_candidate"
            multiple_same += 1
        else:
            status = "ambiguous_candidates"
            ambiguous += 1
        if status != "singleton" and len(fibres) < max_recorded_fibres:
            fibres.append(
                PreimageMemoryFibre(
                    derived_left_label=derived_left,
                    original_left_label=original_left,
                    preimages=preimages,
                    candidate_outputs=candidates,
                    status=status,
                )
            )
    visible_total = missing == 0 and ambiguous == 0
    return DegeneratePreimageMemoryAudit(
        element_count=len(elements),
        visible_pair_count=len(elements) * len(elements),
        edge_memory_state_count=len(elements) * len(elements),
        singleton_fibre_count=singleton,
        missing_fibre_count=missing,
        multiple_same_candidate_count=multiple_same,
        ambiguous_candidate_count=ambiguous,
        visible_derived_operation_total=visible_total,
        finite_edge_memory_repairs_two_strand=True,
        tower_consistency_status="requires_triple_quadruple_check",
        recorded_fibres=tuple(fibres),
    )


def _edge_memory_label(solution: FiniteBraidedSet, left: object, right: object):
    return (solution.R[(left, right)][0], left, right)


def _edge_memory_tuple(
    solution: FiniteBraidedSet,
    tuple_value: Sequence[object],
) -> Tuple[Tuple[object, object, object], ...]:
    return tuple(
        _edge_memory_label(solution, tuple_value[index], tuple_value[index + 1])
        for index in range(len(tuple_value) - 1)
    )


def _edge_update_well_defined(
    solution: FiniteBraidedSet,
    arity: int,
    generator_index: int,
) -> bool:
    seen = {}
    for tuple_value in product(solution.elements, repeat=arity):
        source = _edge_memory_tuple(solution, tuple_value)
        target = _edge_memory_tuple(
            solution,
            solution.apply_R_at(tuple_value, generator_index),
        )
        previous = seen.get(source)
        if previous is None:
            seen[source] = target
        elif previous != target:
            return False
    return True


def _edge_forgetting_well_defined(
    solution: FiniteBraidedSet,
    arity: int,
    forget_index: int,
) -> bool:
    seen = {}
    for tuple_value in product(solution.elements, repeat=arity):
        source = _edge_memory_tuple(solution, tuple_value)
        forgotten = tuple(
            value
            for index, value in enumerate(tuple_value)
            if index != forget_index
        )
        target = _edge_memory_tuple(solution, forgotten)
        previous = seen.get(source)
        if previous is None:
            seen[source] = target
        elif previous != target:
            return False
    return True


def edge_memory_tower_audit(solution: FiniteBraidedSet) -> EdgeMemoryTowerAudit:
    """Check the finite adjacent-edge memory through the first tower gates."""

    elements = tuple(solution.elements)
    edge_labels = {
        _edge_memory_label(solution, left, right)
        for left, right in product(elements, repeat=2)
    }
    arity3_encodings = {
        _edge_memory_tuple(solution, tuple_value)
        for tuple_value in product(elements, repeat=3)
    }
    arity4_encodings = {
        _edge_memory_tuple(solution, tuple_value)
        for tuple_value in product(elements, repeat=4)
    }
    braid_relation = True
    for tuple_value in product(elements, repeat=3):
        left = solution.apply_R_at(
            solution.apply_R_at(solution.apply_R_at(tuple_value, 0), 1),
            0,
        )
        right = solution.apply_R_at(
            solution.apply_R_at(solution.apply_R_at(tuple_value, 1), 0),
            1,
        )
        if _edge_memory_tuple(solution, left) != _edge_memory_tuple(solution, right):
            braid_relation = False
            break
    generator_updates = tuple(
        (index, _edge_update_well_defined(solution, 4, index))
        for index in range(3)
    )
    forgetting = tuple(
        (index, _edge_forgetting_well_defined(solution, 4, index))
        for index in range(4)
    )
    tuple3_count = len(elements) ** 3
    tuple4_count = len(elements) ** 4
    return EdgeMemoryTowerAudit(
        element_count=len(elements),
        edge_label_count=len(edge_labels),
        arity3_tuple_count=tuple3_count,
        arity4_tuple_count=tuple4_count,
        arity3_encoding_injective=len(arity3_encodings) == tuple3_count,
        arity4_encoding_injective=len(arity4_encodings) == tuple4_count,
        braid_relation_on_edge_memory=braid_relation,
        generator_updates_well_defined=generator_updates,
        point_forgetting_well_defined=forgetting,
        records_finite_edge_memory_tower_prefix=True,
    )


def _left_prefix_translations(
    solution: FiniteBraidedSet,
) -> Mapping[object, Transformation]:
    return coordinate_action_maps(solution)


def _left_prefix_path_tuple(
    solution: FiniteBraidedSet,
    tuple_value: Sequence[object],
    left_translations: Mapping[object, Transformation] | None = None,
) -> Tuple[Tuple[Transformation, object, Transformation], ...]:
    """Encode a tuple by the finite path of left-prefix transformations."""

    if left_translations is None:
        left_translations = _left_prefix_translations(solution)
    prefix = identity_transformation(len(solution.elements))
    edges = []
    for value in tuple_value:
        next_prefix = compose_transformations(left_translations[value], prefix)
        edges.append((prefix, value, next_prefix))
        prefix = next_prefix
    return tuple(edges)


def _prefix_path_forgetting_well_defined_and_max_fibre(
    solution: FiniteBraidedSet,
    arity: int,
    forget_index: int,
    left_translations: Mapping[object, Transformation],
) -> Tuple[bool, int]:
    seen = {}
    fibres: dict[Tuple[Tuple[Transformation, object, Transformation], ...], int] = {}
    for tuple_value in product(solution.elements, repeat=arity):
        source = _left_prefix_path_tuple(solution, tuple_value, left_translations)
        forgotten = tuple(
            value
            for index, value in enumerate(tuple_value)
            if index != forget_index
        )
        target = _left_prefix_path_tuple(solution, forgotten, left_translations)
        previous = seen.get(source)
        if previous is None:
            seen[source] = target
        elif previous != target:
            return False, 0
        fibres[target] = fibres.get(target, 0) + 1
    return True, max(fibres.values(), default=0)


def _prefix_path_generator_update_bijective(
    solution: FiniteBraidedSet,
    arity: int,
    generator_index: int,
    left_translations: Mapping[object, Transformation],
) -> bool:
    source_paths = set()
    target_paths = set()
    for tuple_value in product(solution.elements, repeat=arity):
        source_paths.add(_left_prefix_path_tuple(solution, tuple_value, left_translations))
        target_paths.add(
            _left_prefix_path_tuple(
                solution,
                solution.apply_R_at(tuple_value, generator_index),
                left_translations,
            )
        )
    return len(source_paths) == len(target_paths) == len(solution.elements) ** arity


def _left_prefix_identity_holds(
    solution: FiniteBraidedSet,
    left_translations: Mapping[object, Transformation],
) -> bool:
    for left, right in product(solution.elements, repeat=2):
        out_left, out_right = solution.R[(left, right)]
        before = compose_transformations(
            left_translations[left],
            left_translations[right],
        )
        after = compose_transformations(
            left_translations[out_left],
            left_translations[out_right],
        )
        if before != after:
            return False
    return True


def prefix_edge_transducer_audit(
    solution: FiniteBraidedSet,
) -> PrefixEdgeTransducerAudit:
    """Check the finite left-prefix path transducer through first tower gates."""

    elements = tuple(solution.elements)
    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    edge_states = {
        (prefix, value, compose_transformations(left_translations[value], prefix))
        for prefix, value in product(monoid.elements, elements)
    }
    arity3_paths = {
        _left_prefix_path_tuple(solution, tuple_value, left_translations)
        for tuple_value in product(elements, repeat=3)
    }
    arity4_paths = {
        _left_prefix_path_tuple(solution, tuple_value, left_translations)
        for tuple_value in product(elements, repeat=4)
    }
    braid_relation = True
    for tuple_value in product(elements, repeat=3):
        left = solution.apply_R_at(
            solution.apply_R_at(solution.apply_R_at(tuple_value, 0), 1),
            0,
        )
        right = solution.apply_R_at(
            solution.apply_R_at(solution.apply_R_at(tuple_value, 1), 0),
            1,
        )
        if (
            _left_prefix_path_tuple(solution, left, left_translations)
            != _left_prefix_path_tuple(solution, right, left_translations)
        ):
            braid_relation = False
            break
    generator_updates = tuple(
        (
            index,
            _prefix_path_generator_update_bijective(
                solution,
                4,
                index,
                left_translations,
            ),
        )
        for index in range(3)
    )
    forgetting_rows = tuple(
        (
            index,
            _prefix_path_forgetting_well_defined_and_max_fibre(
                solution,
                4,
                index,
                left_translations,
            ),
        )
        for index in range(4)
    )
    point_forgetting = tuple((index, row[0]) for index, row in forgetting_rows)
    max_fibres = tuple((index, row[1]) for index, row in forgetting_rows)
    tuple3_count = len(elements) ** 3
    tuple4_count = len(elements) ** 4
    return PrefixEdgeTransducerAudit(
        element_count=len(elements),
        left_prefix_monoid_size=len(monoid.elements),
        edge_state_count=len(edge_states),
        arity3_path_count=tuple3_count,
        arity4_path_count=tuple4_count,
        arity3_encoding_injective=len(arity3_paths) == tuple3_count,
        arity4_encoding_injective=len(arity4_paths) == tuple4_count,
        left_prefix_identity_holds=_left_prefix_identity_holds(
            solution,
            left_translations,
        ),
        generator_updates_bijective=generator_updates,
        braid_relation_on_prefix_paths=braid_relation,
        point_forgetting_well_defined=point_forgetting,
        point_forgetting_max_fibre_sizes=max_fibres,
        forgetting_fibres_bounded_by_element_count=all(
            size <= len(elements) for _index, size in max_fibres
        ),
        records_prefix_edge_transducer_tower=True,
    )


def _transformation_is_permutation(transformation: Transformation) -> bool:
    return set(transformation) == set(range(len(transformation)))


def prefix_group_hurwitz_compression_pressure_audit(
    solution: FiniteBraidedSet,
) -> PrefixGroupHurwitzCompressionPressureAudit:
    """Record finite equations for group-completing prefix-edge memory.

    A group-Hurwitz compression would be a map from prefix edges
    ``(P,x,P lambda_x)`` to a conjugation-stable subset of one finite group
    such that every local prefix-edge move descends to the ordinary Hurwitz
    rule ``(h,k) -> (hkh^-1,h)``.  This helper does not search all finite
    groups.  It records the exact finite equation family and the first
    ``Q_X(3),Q_X(4)`` obstruction arities where such a compression must be
    tested.
    """

    elements = tuple(solution.elements)
    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    edge_state_count = len(monoid.elements) * len(elements)
    nonunit_count = sum(
        1 for element in monoid.elements if not _transformation_is_permutation(element)
    )
    local_equations = len(monoid.elements) * len(elements) * len(elements)
    forgetting_equations = (
        len(monoid.elements)
        * len(monoid.elements)
        * len(elements)
        * len(elements)
    )
    return PrefixGroupHurwitzCompressionPressureAudit(
        element_count=len(elements),
        left_prefix_monoid_size=len(monoid.elements),
        edge_state_count=edge_state_count,
        nonunit_prefix_count=nonunit_count,
        faithful_prefix_monoid_group_embedding_obstructed=nonunit_count > 0,
        local_hurwitz_label_equation_count=local_equations,
        product_invariance_equation_count=local_equations,
        forgetting_rescan_lumpability_equation_count=forgetting_equations,
        first_obstruction_arities=(3, 4),
        requires_group_label_map=True,
        requires_conjugation_stable_image=True,
        requires_local_hurwitz_descend=True,
        requires_total_product_invariance=True,
        requires_forgetting_rescan_lumpability=True,
        bounded_vertical_kernel_still_unproved=True,
        finite_transducer_alone_is_not_group_hurwitz=True,
    )


def _prefix_action_matches_tuple_action(
    solution: FiniteBraidedSet,
    braid_word: BraidWord,
    braid_index: int,
    left_translations: Mapping[object, Transformation],
) -> tuple[bool, int]:
    tuple_values = tuple(product(solution.elements, repeat=braid_index))
    path_values = tuple(
        _left_prefix_path_tuple(solution, tuple_value, left_translations)
        for tuple_value in tuple_values
    )
    path_to_index = {path: index for index, path in enumerate(path_values)}
    if len(path_to_index) != len(tuple_values):
        return False, len(path_to_index)
    tuple_permutation = braid_word_permutation_image(
        solution,
        braid_index,
        braid_word,
    )
    path_permutation = []
    for tuple_value in tuple_values:
        image = solution.braid_action(braid_word, tuple_value)
        image_path = _left_prefix_path_tuple(solution, image, left_translations)
        path_permutation.append(path_to_index[image_path])
    return tuple(path_permutation) == tuple_permutation, len(path_to_index)


def _prefix_point_pushing_surface_row(
    solution: FiniteBraidedSet,
    point_pushing_arity: int,
    left_translations: Mapping[object, Transformation],
    *,
    max_subgroup_size: int | None,
) -> PrefixPointPushingSurfaceRow:
    from .braid_laws import pure_braid_generator
    from .group_laws import lcm

    braid_index = point_pushing_arity + 1
    generator_braids = tuple(
        pure_braid_generator(generator, braid_index)
        for generator in range(1, point_pushing_arity + 1)
    )
    generator_images = tuple(
        braid_word_permutation_image(solution, braid_index, braid_word)
        for braid_word in generator_braids
    )
    generator_orders = tuple(permutation_order(image) for image in generator_images)
    prefix_checks = tuple(
        _prefix_action_matches_tuple_action(
            solution,
            braid_word,
            braid_index,
            left_translations,
        )
        for braid_word in generator_braids
    )
    prefix_path_count = min((count for _matches, count in prefix_checks), default=0)
    tuple_count = len(solution.elements) ** braid_index
    try:
        subgroup = generated_permutation_subgroup(
            generator_images,
            max_size=max_subgroup_size,
        )
    except ValueError:
        return PrefixPointPushingSurfaceRow(
            point_pushing_arity=point_pushing_arity,
            braid_index=braid_index,
            tuple_count=tuple_count,
            prefix_path_count=prefix_path_count,
            prefix_encoding_injective=prefix_path_count == tuple_count,
            generator_count=len(generator_braids),
            generator_braid_words=generator_braids,
            generator_orders=generator_orders,
            point_pushing_group_size=None,
            point_pushing_group_exponent=None,
            prefix_action_matches_tuple_action=all(
                matches for matches, _count in prefix_checks
            ),
            truncated=True,
        )
    exponent = 1
    for permutation in subgroup:
        exponent = lcm(exponent, permutation_order(permutation))
    return PrefixPointPushingSurfaceRow(
        point_pushing_arity=point_pushing_arity,
        braid_index=braid_index,
        tuple_count=tuple_count,
        prefix_path_count=prefix_path_count,
        prefix_encoding_injective=prefix_path_count == tuple_count,
        generator_count=len(generator_braids),
        generator_braid_words=generator_braids,
        generator_orders=generator_orders,
        point_pushing_group_size=len(subgroup),
        point_pushing_group_exponent=exponent,
        prefix_action_matches_tuple_action=all(
            matches for matches, _count in prefix_checks
        ),
        truncated=False,
    )


def prefix_point_pushing_surface_audit(
    solution: FiniteBraidedSet,
    *,
    max_subgroup_size: int | None = None,
) -> PrefixPointPushingSurfaceAudit:
    """Compute the first concrete ``Q_X(3),Q_X(4)`` prefix surfaces."""

    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    rows = tuple(
        _prefix_point_pushing_surface_row(
            solution,
            arity,
            left_translations,
            max_subgroup_size=max_subgroup_size,
        )
        for arity in (3, 4)
    )
    return PrefixPointPushingSurfaceAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        rows=rows,
        records_first_group_hurwitz_obstruction_surface=True,
    )


def _permutation_orbit_sizes(
    size: int,
    generators: Iterable[Permutation],
) -> Tuple[int, ...]:
    symmetric_generators = set(generators)
    symmetric_generators.update(
        invert_permutation(generator)
        for generator in tuple(symmetric_generators)
    )
    seen = set()
    orbit_sizes = []
    for start in range(size):
        if start in seen:
            continue
        orbit = {start}
        queue = deque([start])
        seen.add(start)
        while queue:
            current = queue.popleft()
            for generator in symmetric_generators:
                candidate = generator[current]
                if candidate in seen:
                    continue
                seen.add(candidate)
                orbit.add(candidate)
                queue.append(candidate)
        orbit_sizes.append(len(orbit))
    return tuple(sorted(orbit_sizes, reverse=True))


def _prefix_artin_envelope_cohomology_row(
    solution: FiniteBraidedSet,
    point_pushing_arity: int,
    *,
    max_subgroup_size: int | None,
) -> PrefixArtinEnvelopeCohomologyRow:
    from .braid_laws import pure_braid_generator
    from .group_laws import lcm

    braid_index = point_pushing_arity + 1
    generator_braids = tuple(
        pure_braid_generator(generator, braid_index)
        for generator in range(1, point_pushing_arity + 1)
    )
    generator_images = tuple(
        braid_word_permutation_image(solution, braid_index, braid_word)
        for braid_word in generator_braids
    )
    tuple_count = len(solution.elements) ** braid_index
    generator_count = len(generator_images)
    generator_cocycle_value_count = generator_count * tuple_count
    restriction_to_previous_required = point_pushing_arity > 3
    forgetting_naturality_square_count = (
        point_pushing_arity * generator_cocycle_value_count
        if restriction_to_previous_required
        else 0
    )
    try:
        subgroup = generated_permutation_subgroup(
            generator_images,
            max_size=max_subgroup_size,
        )
    except ValueError:
        return PrefixArtinEnvelopeCohomologyRow(
            point_pushing_arity=point_pushing_arity,
            braid_index=braid_index,
            tuple_count=tuple_count,
            generator_count=generator_count,
            point_pushing_group_size=None,
            point_pushing_group_exponent=None,
            orbit_count=None,
            max_orbit_size=None,
            action_groupoid_arrow_count=None,
            stabilizer_loop_arrow_count=None,
            generator_cocycle_value_count=generator_cocycle_value_count,
            restriction_to_previous_required=restriction_to_previous_required,
            forgetting_naturality_square_count=forgetting_naturality_square_count,
            truncated=True,
        )
    exponent = 1
    for permutation in subgroup:
        exponent = lcm(exponent, permutation_order(permutation))
    orbit_sizes = _permutation_orbit_sizes(tuple_count, generator_images)
    stabilizer_loop_arrow_count = sum(
        1
        for permutation in subgroup
        for index in range(tuple_count)
        if permutation[index] == index
    )
    return PrefixArtinEnvelopeCohomologyRow(
        point_pushing_arity=point_pushing_arity,
        braid_index=braid_index,
        tuple_count=tuple_count,
        generator_count=generator_count,
        point_pushing_group_size=len(subgroup),
        point_pushing_group_exponent=exponent,
        orbit_count=len(orbit_sizes),
        max_orbit_size=max(orbit_sizes, default=0),
        action_groupoid_arrow_count=len(subgroup) * tuple_count,
        stabilizer_loop_arrow_count=stabilizer_loop_arrow_count,
        generator_cocycle_value_count=generator_cocycle_value_count,
        restriction_to_previous_required=restriction_to_previous_required,
        forgetting_naturality_square_count=forgetting_naturality_square_count,
        truncated=False,
    )


def prefix_artin_envelope_cohomology_audit(
    solution: FiniteBraidedSet,
    *,
    max_subgroup_size: int | None = None,
) -> PrefixArtinEnvelopeCohomologyAudit:
    """Record the first finite cohomology obligations for an Artin envelope.

    This does not compute group cohomology.  It records the finite
    action-groupoid surface on which a fixed operator-label Hurwitz quotient
    and a uniformly bounded vertical cocycle would have to live.
    """

    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    nonunit_count = sum(
        1
        for element in monoid.elements
        if not _transformation_is_permutation(element)
    )
    rows = tuple(
        _prefix_artin_envelope_cohomology_row(
            solution,
            arity,
            max_subgroup_size=max_subgroup_size,
        )
        for arity in (3, 4)
    )
    return PrefixArtinEnvelopeCohomologyAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=nonunit_count,
        operator_label_variable_count=len(monoid.elements) * len(solution.elements),
        rows=rows,
        fixed_finite_hurwitz_base_required=True,
        vertical_cocycle_bounded_exponent_required=True,
        quotient_groupoid_functor_required=True,
        tower_restriction_compatibility_required=True,
        finite_surface_only=True,
    )


def _delete_tuple_index(tuple_value: Sequence[object], delete_index: int) -> Tuple[object, ...]:
    return tuple(
        value
        for index, value in enumerate(tuple_value)
        if index != delete_index
    )


def _target_point_pushing_generator_after_forgetting(
    source_generator_index: int,
    forget_stationary_index: int,
) -> int | None:
    if source_generator_index == forget_stationary_index:
        return None
    if source_generator_index < forget_stationary_index:
        return source_generator_index
    return source_generator_index - 1


def _prefix_point_forgetting_restriction_row(
    solution: FiniteBraidedSet,
    *,
    source_generator_index: int,
    forget_stationary_index: int,
) -> PrefixPointForgettingRestrictionRow:
    from .braid_laws import pure_braid_generator

    source_point_pushing_arity = 4
    source_braid_index = source_point_pushing_arity + 1
    target_point_pushing_arity = 3
    target_braid_index = target_point_pushing_arity + 1
    delete_index = forget_stationary_index - 1
    source_braid_word = pure_braid_generator(
        source_generator_index,
        source_braid_index,
    )
    target_generator_index = _target_point_pushing_generator_after_forgetting(
        source_generator_index,
        forget_stationary_index,
    )
    target_braid_word: BraidWord = (
        tuple()
        if target_generator_index is None
        else pure_braid_generator(target_generator_index, target_braid_index)
    )
    mismatch_count = 0
    first_witness_input = None
    first_deleted_after_source = None
    first_expected_target = None
    for tuple_value in product(solution.elements, repeat=source_braid_index):
        source_image = solution.braid_action(source_braid_word, tuple_value)
        deleted_after_source = _delete_tuple_index(source_image, delete_index)
        deleted_input = _delete_tuple_index(tuple_value, delete_index)
        expected_target = (
            deleted_input
            if target_generator_index is None
            else solution.braid_action(target_braid_word, deleted_input)
        )
        if deleted_after_source == expected_target:
            continue
        mismatch_count += 1
        if first_witness_input is None:
            first_witness_input = tuple(tuple_value)
            first_deleted_after_source = deleted_after_source
            first_expected_target = expected_target
    return PrefixPointForgettingRestrictionRow(
        source_point_pushing_arity=source_point_pushing_arity,
        source_braid_index=source_braid_index,
        target_point_pushing_arity=target_point_pushing_arity,
        target_braid_index=target_braid_index,
        forget_stationary_index=forget_stationary_index,
        source_generator_index=source_generator_index,
        target_generator_index=target_generator_index,
        source_braid_word=source_braid_word,
        target_braid_word=target_braid_word,
        tuple_count=len(solution.elements) ** source_braid_index,
        expected_identity_after_forgetting=target_generator_index is None,
        matches_marked_restriction=mismatch_count == 0,
        mismatch_count=mismatch_count,
        first_witness_input=first_witness_input,
        first_deleted_after_source=first_deleted_after_source,
        first_expected_target=first_expected_target,
    )


def prefix_point_forgetting_restriction_audit(
    solution: FiniteBraidedSet,
) -> PrefixPointForgettingRestrictionAudit:
    """Compare marked `Q_X(4)` generators after deleting one stationary strand."""

    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    rows = tuple(
        _prefix_point_forgetting_restriction_row(
            solution,
            source_generator_index=source_generator_index,
            forget_stationary_index=forget_stationary_index,
        )
        for forget_stationary_index in range(1, 5)
        for source_generator_index in range(1, 5)
    )
    return PrefixPointForgettingRestrictionAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        source_point_pushing_arity=4,
        target_point_pushing_arity=3,
        rows=rows,
        records_first_point_forgetting_restriction_surface=True,
    )


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
    transport_residual_quotient_order = 0
    transport_residual_abelianization_order = 0
    transport_residual_abelianization_exponent = 0
    transport_residual_abelianization_prime_set: Tuple[int, ...] = ()
    transport_residual_abelianization_exponent_divides_bound = False
    transport_residual_prime_support_bounded = False
    transport_residual_is_perfect = False
    transport_residual_regime = "invalid_transport_residual_data"
    quotient_abelianization_order = 0
    quotient_abelianization_exponent = 0
    quotient_abelianization_is_cyclic = False
    generator_abelianization_order = 0
    generator_generates_quotient_abelianization = False
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
        transport_residual, _residual_projection = quotient_group_by_normal_subgroup(
            quotient,
            internal_closure,
        )
        transport_residual_quotient_order = len(transport_residual.elements)
        residual_commutator = frozenset(
            commutator_subgroup_elements(transport_residual)
        )
        residual_abelianization, _residual_ab_projection = (
            quotient_group_by_normal_subgroup(
                transport_residual,
                residual_commutator,
            )
        )
        transport_residual_abelianization_order = len(
            residual_abelianization.elements
        )
        transport_residual_abelianization_exponent = group_exponent(
            residual_abelianization
        )
        transport_residual_abelianization_prime_set = _prime_divisors_integer(
            transport_residual_abelianization_exponent
        )
        transport_residual_abelianization_exponent_divides_bound = (
            normal_generator_order_bound
            % transport_residual_abelianization_exponent
            == 0
        )
        bound_prime_set = set(_prime_divisors_integer(normal_generator_order_bound))
        transport_residual_prime_support_bounded = set(
            transport_residual_abelianization_prime_set
        ) <= bound_prime_set
        transport_residual_is_perfect = (
            transport_residual_abelianization_order == 1
        )
        quotient_commutator = frozenset(commutator_subgroup_elements(quotient))
        quotient_abelianization, ab_projection = quotient_group_by_normal_subgroup(
            quotient,
            quotient_commutator,
        )
        quotient_abelianization_order = len(quotient_abelianization.elements)
        quotient_abelianization_exponent = group_exponent(quotient_abelianization)
        quotient_abelianization_is_cyclic = any(
            element_order(quotient_abelianization, element)
            == quotient_abelianization_order
            for element in quotient_abelianization.elements
        )
        generator_abelianization = ab_projection.apply(generator_image)
        generator_abelianization_order = element_order(
            quotient_abelianization,
            generator_abelianization,
        )
        generator_generates_quotient_abelianization = (
            generator_abelianization_order == quotient_abelianization_order
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
    if quotient_generation_regime == "internal_bounded_normal_generator_quotient":
        transport_residual_regime = "no_transport_residual"
    elif quotient_generation_regime == "transport_orbit_generated_quotient":
        transport_residual_regime = (
            "perfect_transport_residual"
            if transport_residual_is_perfect
            else "abelian_visible_transport_residual"
        )
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
        transport_residual_quotient_order=transport_residual_quotient_order,
        transport_residual_abelianization_order=(
            transport_residual_abelianization_order
        ),
        transport_residual_abelianization_exponent=(
            transport_residual_abelianization_exponent
        ),
        transport_residual_abelianization_prime_set=(
            transport_residual_abelianization_prime_set
        ),
        transport_residual_abelianization_exponent_divides_bound=(
            transport_residual_abelianization_exponent_divides_bound
        ),
        transport_residual_prime_support_bounded=(
            transport_residual_prime_support_bounded
        ),
        transport_residual_is_perfect=transport_residual_is_perfect,
        transport_residual_regime=transport_residual_regime,
        quotient_abelianization_order=quotient_abelianization_order,
        quotient_abelianization_exponent=quotient_abelianization_exponent,
        quotient_abelianization_is_cyclic=quotient_abelianization_is_cyclic,
        generator_abelianization_order=generator_abelianization_order,
        generator_generates_quotient_abelianization=(
            generator_generates_quotient_abelianization
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
