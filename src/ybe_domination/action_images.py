from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, permutations, product
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
class PrefixFiniteBasePullbackGaugeRow:
    """One arity of the finite-base pullback/gauge pressure surface."""

    point_pushing_arity: int
    braid_index: int
    tuple_count: int
    generator_count: int
    label_tuple_count: int
    max_label_fibre_size: int
    label_action_well_defined: bool
    tuple_action_group_size: int | None
    tuple_action_group_exponent: int | None
    label_action_group_size: int | None
    label_action_group_exponent: int | None
    quotient_map_well_defined: bool | None
    vertical_kernel_size: int | None
    vertical_kernel_exponent: int | None
    canonical_section_displacement_count: int | None
    canonical_section_gauge_trivial: bool | None
    truncated: bool

    @property
    def computed_untruncated_pullback_row(self) -> bool:
        return (
            not self.truncated
            and self.label_action_well_defined
            and self.tuple_action_group_size is not None
            and self.tuple_action_group_exponent is not None
            and self.label_action_group_size is not None
            and self.label_action_group_exponent is not None
            and self.quotient_map_well_defined is not None
            and self.vertical_kernel_size is not None
            and self.vertical_kernel_exponent is not None
            and self.canonical_section_displacement_count is not None
            and self.canonical_section_gauge_trivial is not None
        )


@dataclass(frozen=True)
class PrefixFiniteBasePullbackGaugeAudit:
    """Finite translation-pair base ledger for pullback/gauge pressure."""

    element_count: int
    translation_pair_label_count: int
    left_translation_label_count: int
    right_translation_label_count: int
    crossing_descends_to_translation_pair_labels: bool
    crossing_label_ambiguity_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    rows: Tuple[PrefixFiniteBasePullbackGaugeRow, ...]
    vertical_defect_transport_mismatch_count: int
    vertical_defect_order_spectrum: Tuple[int, ...]
    peiffer_square_nontrivial_boundary_count: int
    peiffer_cube_transport_mismatch_count: int
    peiffer_order_pair_spectrum: Tuple[Tuple[int, int], ...]
    observed_deletion_two_cocycle_gauge_trivial: bool
    fixed_translation_pair_base_only: bool
    group_hurwitz_realization_still_required: bool

    @property
    def checked_arities(self) -> Tuple[int, ...]:
        return tuple(row.point_pushing_arity for row in self.rows)

    @property
    def all_rows_untruncated(self) -> bool:
        return all(row.computed_untruncated_pullback_row for row in self.rows)

    @property
    def all_label_actions_well_defined(self) -> bool:
        return all(row.label_action_well_defined for row in self.rows)

    @property
    def all_quotient_maps_well_defined(self) -> bool:
        return all(row.quotient_map_well_defined for row in self.rows)

    @property
    def all_canonical_section_gauges_trivial(self) -> bool:
        return all(row.canonical_section_gauge_trivial for row in self.rows)

    @property
    def vertical_kernel_exponent_spectrum(self) -> Tuple[int, ...]:
        return tuple(
            sorted(
                {
                    row.vertical_kernel_exponent
                    for row in self.rows
                    if row.vertical_kernel_exponent is not None
                }
            )
        )

    @property
    def records_prefix_finite_base_pullback_gauge_surface(self) -> bool:
        return (
            self.checked_arities == (3, 4, 5)
            and self.crossing_descends_to_translation_pair_labels
            and self.all_rows_untruncated
            and self.all_label_actions_well_defined
            and self.all_quotient_maps_well_defined
            and self.observed_deletion_two_cocycle_gauge_trivial
            and self.fixed_translation_pair_base_only
            and self.group_hurwitz_realization_still_required
        )


@dataclass(frozen=True)
class PullbackCoskeletalCriterionCase:
    """One logical branch of the fixed-base pullback/coskeletal route."""

    key: str
    role: str
    finite_data: str
    criterion: str
    consequence: str
    failure_mode: str


@dataclass(frozen=True)
class PullbackCoskeletalCriterionAudit:
    """Theorem-route ledger for finite pullback compactness versus cutoff."""

    fixed_base_inverse_limit_compactness_recorded: bool
    uniform_bounded_arity_cutoff_rejected_without_extra_hypothesis: bool
    pullback_coskeletal_hypothesis_identified: bool
    finite_obstruction_certificate_identified: bool
    missing_pullback_coskeletal_lemma: str
    cases: Tuple[PullbackCoskeletalCriterionCase, ...]

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_pullback_coskeletal_route_boundary(self) -> bool:
        return (
            self.fixed_base_inverse_limit_compactness_recorded
            and self.uniform_bounded_arity_cutoff_rejected_without_extra_hypothesis
            and self.pullback_coskeletal_hypothesis_identified
            and self.finite_obstruction_certificate_identified
            and self.case_keys
            == (
                "fixed_base_inverse_limit",
                "bounded_cutoff_requires_coskeletality",
                "finite_obstruction_certificate",
                "general_uniform_cutoff_failure",
            )
        )


@dataclass(frozen=True)
class YBECoskeletalMechanismCase:
    """One YBE-specific source or failure of pullback coskeletality."""

    key: str
    role: str
    mechanism: str
    finite_ybe_status: str
    theorem_obligation: str
    obstruction_signature: str


@dataclass(frozen=True)
class YBECoskeletalMechanismAudit:
    """YBE-specific ledger for possible bounded-state coskeletality."""

    finite_bijectivity_gives_local_generation: bool
    finite_bijectivity_does_not_give_local_cohomology_detection: bool
    bounded_state_recursion_would_imply_coskeletality: bool
    high_cross_effect_bisections_are_live_obstruction: bool
    w_local_operator_label_descent_is_extra_hypothesis: bool
    coefficient_inverse_limit_condition_recorded: bool
    comparison_commutes_with_inverse_limits_recorded: bool
    bounded_relation_arity_cutoff_recorded: bool
    brunnian_cross_effect_criterion_recorded: bool
    cutoff_formula: str
    conditional_pullback_coskeletal_theorem: str
    brunnian_cross_effect_formula: str
    brunnian_obstruction_criterion: str
    positive_ybe_theorem_obligations: Tuple[str, ...]
    cases: Tuple[YBECoskeletalMechanismCase, ...]

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_ybe_coskeletal_mechanism_boundary(self) -> bool:
        return (
            self.finite_bijectivity_gives_local_generation
            and self.finite_bijectivity_does_not_give_local_cohomology_detection
            and self.bounded_state_recursion_would_imply_coskeletality
            and self.high_cross_effect_bisections_are_live_obstruction
            and self.w_local_operator_label_descent_is_extra_hypothesis
            and self.coefficient_inverse_limit_condition_recorded
            and self.comparison_commutes_with_inverse_limits_recorded
            and self.bounded_relation_arity_cutoff_recorded
            and self.brunnian_cross_effect_criterion_recorded
            and self.cutoff_formula == "N0 = max(r, w + 3)"
            and "Omega" in self.conditional_pullback_coskeletal_theorem
            and "cr_ij^I" in self.brunnian_cross_effect_formula
            and "Br^2_I" in self.brunnian_obstruction_criterion
            and self.positive_ybe_theorem_obligations
            == (
                "prove w-local inverse-limit reconstruction for operator labels",
                (
                    "prove coefficient inverse-limit reconstruction for "
                    "one-, two-, and three-deletion bands"
                ),
                (
                    "prove bounded relation arity for transport, cocycle, "
                    "and gauge equations"
                ),
                (
                    "prove vanishing of Brunnian relative deletion "
                    "2-obstructions above the cutoff"
                ),
            )
            and self.case_keys
            == (
                "formal_w_local_descent_theorem",
                "fadell_neuwirth_recursion",
                "finite_operator_state_recursion",
                "garside_or_automaton_normal_forms",
                "fi_fb_finite_generation",
                "brunnian_cross_effect_obstruction",
            )
        )


@dataclass(frozen=True)
class YBEBrunnianDerivativeGateCase:
    """One row in the Brunnian derivative residual gate."""

    key: str
    role: str
    statement: str
    consequence: str


@dataclass(frozen=True)
class YBEBrunnianDerivativeGateAudit:
    """Ledger separating Brunnian point-push gauge from true H^2 residuals."""

    naive_brunnian_pure_braid_obstruction_rejected: bool
    one_strand_derivatives_are_gauge_coboundaries: bool
    brunnian_point_push_shadow_is_gauge: bool
    nonabelian_derivative_chain_rule_recorded: bool
    residual_double_deletion_quotient_identified: bool
    fadell_neuwirth_decomposition_would_kill_high_brunnian_classes: bool
    derivative_formula: str
    gauge_formula: str
    chain_rule_formula: str
    residual_quotient_formula: str
    decomposition_formula: str
    cases: Tuple[YBEBrunnianDerivativeGateCase, ...]

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_brunnian_derivative_gate(self) -> bool:
        return (
            self.naive_brunnian_pure_braid_obstruction_rejected
            and self.one_strand_derivatives_are_gauge_coboundaries
            and self.brunnian_point_push_shadow_is_gauge
            and self.nonabelian_derivative_chain_rule_recorded
            and self.residual_double_deletion_quotient_identified
            and self.fadell_neuwirth_decomposition_would_kill_high_brunnian_classes
            and self.derivative_formula
            == "nabla_q b = tau_q(b) inf_q(partial_q b)^-1"
            and self.gauge_formula == "(delta u)_{p,q}^I = nabla_q b"
            and "nabla_r(nabla_q b)" in self.chain_rule_formula
            and "R_{p,q}^I" in self.residual_quotient_formula
            and "Pi^sharp(theta)" in self.decomposition_formula
            and self.case_keys
            == (
                "one_strand_derivative_gauge_gate",
                "pure_braid_brunnian_shadow_triviality",
                "nonabelian_derivative_chain_rule",
                "residual_double_deletion_quotient",
                "fadell_neuwirth_decomposition_route",
            )
        )


@dataclass(frozen=True)
class YBECrossedSquareResidualCase:
    """One row in the crossed-square residual quotient criterion."""

    key: str
    role: str
    statement: str
    consequence: str


@dataclass(frozen=True)
class YBECrossedSquareResidualAudit:
    """Crossed-square criterion for the residual double-deletion quotient."""

    crossed_square_model_identified: bool
    edge_degenerate_subgroup_identified: bool
    peiffer_mutual_subgroup_identified: bool
    fixed_base_pullback_subgroup_identified: bool
    residual_exact_sequence_recorded: bool
    boundary_obstruction_identified: bool
    moore_peiffer_obstruction_identified: bool
    peiffer_complete_vanishing_theorem_recorded: bool
    obstruction_invariant_form_recorded: bool
    crossed_square_vertices: Tuple[str, str, str, str]
    residual_quotient_formula: str
    exact_sequence_formula: str
    boundary_obstruction_formula: str
    moore_peiffer_obstruction_formula: str
    compact_vanishing_formula: str
    obstruction_invariant_formula: str
    cases: Tuple[YBECrossedSquareResidualCase, ...]

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_crossed_square_residual_criterion(self) -> bool:
        return (
            self.crossed_square_model_identified
            and self.edge_degenerate_subgroup_identified
            and self.peiffer_mutual_subgroup_identified
            and self.fixed_base_pullback_subgroup_identified
            and self.residual_exact_sequence_recorded
            and self.boundary_obstruction_identified
            and self.moore_peiffer_obstruction_identified
            and self.peiffer_complete_vanishing_theorem_recorded
            and self.obstruction_invariant_form_recorded
            and self.crossed_square_vertices == ("L", "M", "N", "P")
            and "R_{p,q}^I" in self.residual_quotient_formula
            and "K/(K cap D_{p,q})" in self.exact_sequence_formula
            and "H_partial^square" in self.boundary_obstruction_formula
            and "H_2^square" in self.moore_peiffer_obstruction_formula
            and "partial L = partial E_{p,q}" in self.compact_vanishing_formula
            and "chi_I" in self.obstruction_invariant_formula
            and self.case_keys
            == (
                "crossed_square_bisection_model",
                "residual_exact_sequence",
                "boundary_obstruction",
                "moore_peiffer_homology",
                "peiffer_complete_vanishing_theorem",
                "crossed_square_countercertificate",
            )
        )


@dataclass(frozen=True)
class YBEFiniteStateRackCoverCase:
    """One row in the finite-state rack-cover obstruction criterion."""

    key: str
    role: str
    statement: str
    consequence: str


@dataclass(frozen=True)
class YBEFiniteStateRackCoverAudit:
    """Finite-state decoder criterion for marked rack covers of YBE actions."""

    coordinatewise_rack_quotient_obstruction_identified: bool
    fiber_label_first_coordinate_obstruction_identified: bool
    rack_shadow_identity_recorded: bool
    label_cocycle_equation_recorded: bool
    finite_state_decoder_criterion_recorded: bool
    decoder_surjectivity_requirement_recorded: bool
    structure_group_obstruction_recorded: bool
    right_update_defect_identified: bool
    rack_switch_formula: str
    coordinatewise_obstruction_formula: str
    rack_shadow_identity_formula: str
    ybe_twisted_identity_formula: str
    label_cocycle_formula: str
    decoder_equations_formula: str
    right_update_defect_formula: str
    cases: Tuple[YBEFiniteStateRackCoverCase, ...]

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_finite_state_rack_cover_criterion(self) -> bool:
        return (
            self.coordinatewise_rack_quotient_obstruction_identified
            and self.fiber_label_first_coordinate_obstruction_identified
            and self.rack_shadow_identity_recorded
            and self.label_cocycle_equation_recorded
            and self.finite_state_decoder_criterion_recorded
            and self.decoder_surjectivity_requirement_recorded
            and self.structure_group_obstruction_recorded
            and self.right_update_defect_identified
            and "R_Y(a,b)=(a > b,a)" in self.rack_switch_formula
            and "rho_y(x)=x" in self.coordinatewise_obstruction_formula
            and "lambda_x lambda_y" in self.rack_shadow_identity_formula
            and "lambda_{rho_y(x)}" in self.ybe_twisted_identity_formula
            and "alpha_{x,lambda_y(z)}" in self.label_cocycle_formula
            and "d(tau(q,a > b),a)" in self.decoder_equations_formula
            and "Delta(x,y)" in self.right_update_defect_formula
            and self.case_keys
            == (
                "coordinatewise_rack_quotient_obstruction",
                "fiber_label_first_coordinate_obstruction",
                "rack_shadow_identity_gap",
                "label_cocycle_equation",
                "finite_state_decoder_criterion",
                "structure_group_same_copy_obstruction",
            )
        )


@dataclass(frozen=True)
class YBEEquivariantReconstructionClosureCase:
    """One row in the quotient/block detector gluing criterion."""

    key: str
    role: str
    statement: str
    consequence: str


@dataclass(frozen=True)
class YBEEquivariantReconstructionClosureAudit:
    """Closure gate for gluing known detectors by equivariant reconstruction."""

    marked_tower_reconstruction_recorded: bool
    product_kernel_implication_recorded: bool
    total_quotient_corollary_recorded: bool
    partial_domain_totalization_required: bool
    point_separation_insufficient_recorded: bool
    off_diagonal_transition_data_required: bool
    arity3_extension_cocycle_obstruction_recorded: bool
    hidden_fibre_kernel_criterion_recorded: bool
    reconstruction_formula: str
    product_kernel_formula: str
    total_quotient_formula: str
    visible_kernel_formula: str
    hidden_fibre_formula: str
    partial_domain_formula: str
    extension_cocycle_formula: str
    arity3_stress_formula: str
    cases: Tuple[YBEEquivariantReconstructionClosureCase, ...]

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_equivariant_reconstruction_closure_gate(self) -> bool:
        return (
            self.marked_tower_reconstruction_recorded
            and self.product_kernel_implication_recorded
            and self.total_quotient_corollary_recorded
            and self.partial_domain_totalization_required
            and self.point_separation_insufficient_recorded
            and self.off_diagonal_transition_data_required
            and self.arity3_extension_cocycle_obstruction_recorded
            and self.hidden_fibre_kernel_criterion_recorded
            and "R_n:X^n" in self.reconstruction_formula
            and "ker rho_product,n" in self.product_kernel_formula
            and "pi^n" in self.total_quotient_formula
            and "K_vis,n" in self.visible_kernel_formula
            and "H_t=F_n^-1(t)" in self.hidden_fibre_formula
            and "partial" in self.partial_domain_formula
            and "omega_{z,z'}" in self.extension_cocycle_formula
            and "arity 3" in self.arity3_stress_formula
            and self.case_keys
            == (
                "marked_tower_reconstruction",
                "product_kernel_implication",
                "total_quotient_corollary",
                "partial_subquotient_domain_totalization",
                "point_separation_not_enough",
                "off_diagonal_transition_data",
                "arity3_extension_cocycle_obstruction",
                "hidden_fibre_visible_kernel_criterion",
            )
        )


@dataclass(frozen=True)
class YBEGuitarDecoderBoundaryCase:
    """One row in the guitar-map finite-state decoder boundary."""

    key: str
    role: str
    statement: str
    consequence: str


@dataclass(frozen=True)
class YBEGuitarDecoderBoundaryAudit:
    """Boundary between the guitar-derived rack theorem and degenerate repair."""

    right_guitar_hypothesis_recorded: bool
    derived_rack_operation_recorded: bool
    all_arity_kernel_equality_recorded: bool
    finite_state_decoder_realization_recorded: bool
    degenerate_j2_failure_recorded: bool
    monoid_inverse_branch_gate_recorded: bool
    no_automatic_unbounded_memory_obstruction_recorded: bool
    deterministic_decoder_obligation_recorded: bool
    right_guitar_formula: str
    derived_rack_formula: str
    kernel_equality_formula: str
    decoder_state_formula: str
    degenerate_j2_failure_formula: str
    monoid_gate_formula: str
    cases: Tuple[YBEGuitarDecoderBoundaryCase, ...]

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_guitar_decoder_boundary(self) -> bool:
        return (
            self.right_guitar_hypothesis_recorded
            and self.derived_rack_operation_recorded
            and self.all_arity_kernel_equality_recorded
            and self.finite_state_decoder_realization_recorded
            and self.degenerate_j2_failure_recorded
            and self.monoid_inverse_branch_gate_recorded
            and self.no_automatic_unbounded_memory_obstruction_recorded
            and self.deterministic_decoder_obligation_recorded
            and "R_y(x)=rho_y(x)" in self.right_guitar_formula
            and "R_a(lambda_{R_b^-1(a)}(b))" in self.derived_rack_formula
            and "ker rho_Y,n = ker rho_X,n" in self.kernel_equality_formula
            and "Q=G_rho" in self.decoder_state_formula
            and "J_2(x,y)=(R_y(x),y)" in self.degenerate_j2_failure_formula
            and "Q=M_rho" in self.monoid_gate_formula
            and self.case_keys
            == (
                "right_nondegenerate_guitar_theorem",
                "derived_rack_domination",
                "finite_state_decoder_realization",
                "degenerate_j2_failure",
                "monoid_inverse_branch_gate",
                "deterministic_decoder_obligation",
            )
        )


@dataclass(frozen=True)
class YBEInverseBranchDeterminizationCase:
    """One row in the total monoid-guitar determinization obstruction."""

    key: str
    role: str
    statement: str
    consequence: str


@dataclass(frozen=True)
class YBEInverseBranchDeterminizationAudit:
    """Gate for total deterministic inverse-branch monoid decoders.

    The guitar boundary leaves the degenerate case as an inverse-branch
    problem over the finite transformation monoid M_rho.  This ledger records
    the sharper obstruction: a total deterministic decoder of that monoid
    type forces the relevant side actions to be surjective, hence bijective
    for finite X.
    """

    total_decoder_surjectivity_recorded: bool
    local_surjectivity_equation_recorded: bool
    finite_side_bijection_forced: bool
    total_monoid_guitar_negative_recorded: bool
    powerset_relation_failure_recorded: bool
    green_rank_drop_failure_recorded: bool
    restricted_language_cocycle_recorded: bool
    nondeterministic_kernel_gap_recorded: bool
    initial_state_formula: str
    local_surjectivity_equation_formula: str
    forced_bijection_formula: str
    monoid_rank_formula: str
    branch_cocycle_formula: str
    cases: Tuple[YBEInverseBranchDeterminizationCase, ...]

    @property
    def case_keys(self) -> Tuple[str, ...]:
        return tuple(case.key for case in self.cases)

    @property
    def records_inverse_branch_determinization_gate(self) -> bool:
        return (
            self.total_decoder_surjectivity_recorded
            and self.local_surjectivity_equation_recorded
            and self.finite_side_bijection_forced
            and self.total_monoid_guitar_negative_recorded
            and self.powerset_relation_failure_recorded
            and self.green_rank_drop_failure_recorded
            and self.restricted_language_cocycle_recorded
            and self.nondeterministic_kernel_gap_recorded
            and "Phi_1" in self.initial_state_formula
            and "rho" in self.local_surjectivity_equation_formula
            and "R_y(X)=X" in self.forced_bijection_formula
            and "rank(q R_x)" in self.monoid_rank_formula
            and "arity-3" in self.branch_cocycle_formula
            and self.case_keys
            == (
                "total_decoder_surjectivity",
                "local_equation_forces_side_surjectivity",
                "rank_drop_empty_inverse_fibre",
                "powerset_relation_not_rack",
                "green_schutzenberger_no_rank_repair",
                "restricted_language_branch_cocycle",
                "nondeterministic_kernel_gap",
            )
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
class PrefixDeletionSquareRestrictionRow:
    """One marked generator comparison after two stationary-strand deletions."""

    source_point_pushing_arity: int
    source_braid_index: int
    target_point_pushing_arity: int
    target_braid_index: int
    forget_stationary_indices: Tuple[int, int]
    source_generator_index: int
    target_generator_index: int | None
    source_braid_word: BraidWord
    target_braid_word: BraidWord
    tuple_count: int
    expected_identity_after_forgetting: bool
    deletion_orders_commute: bool
    matches_marked_double_restriction: bool
    mismatch_count: int
    first_witness_input: Tuple[object, ...] | None
    first_deleted_after_source: Tuple[object, ...] | None
    first_expected_target: Tuple[object, ...] | None

    @property
    def source_generator_deleted(self) -> bool:
        return self.source_generator_index in self.forget_stationary_indices

    @property
    def vertical_square_cocycle_visible(self) -> bool:
        return self.mismatch_count > 0


@dataclass(frozen=True)
class PrefixDeletionSquareRestrictionAudit:
    """First two-face point-forgetting surface for Peiffer pressure."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    source_point_pushing_arity: int
    target_point_pushing_arity: int
    rows: Tuple[PrefixDeletionSquareRestrictionRow, ...]
    records_first_deletion_square_surface: bool

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def total_mismatch_count(self) -> int:
        return sum(row.mismatch_count for row in self.rows)

    @property
    def deleted_generator_mismatch_count(self) -> int:
        return sum(
            row.mismatch_count
            for row in self.rows
            if row.source_generator_deleted
        )

    @property
    def surviving_generator_all_match(self) -> bool:
        return all(
            row.matches_marked_double_restriction
            for row in self.rows
            if not row.source_generator_deleted
        )

    @property
    def deletion_orders_all_commute(self) -> bool:
        return all(row.deletion_orders_commute for row in self.rows)

    @property
    def all_rows_match(self) -> bool:
        return all(row.matches_marked_double_restriction for row in self.rows)

    @property
    def verifies_first_deletion_square_surface(self) -> bool:
        return (
            self.source_point_pushing_arity == 5
            and self.target_point_pushing_arity == 3
            and self.row_count == 50
            and self.deletion_orders_all_commute
            and self.records_first_deletion_square_surface
        )


@dataclass(frozen=True)
class PrefixDeletionCubeRestrictionRow:
    """One marked generator comparison after three stationary deletions."""

    source_point_pushing_arity: int
    source_braid_index: int
    target_point_pushing_arity: int
    target_braid_index: int
    forget_stationary_indices: Tuple[int, int, int]
    source_generator_index: int
    target_generator_index: int | None
    source_braid_word: BraidWord
    target_braid_word: BraidWord
    tuple_count: int
    deletion_order_count: int
    expected_identity_after_forgetting: bool
    deletion_orders_commute: bool
    matches_marked_triple_restriction: bool
    mismatch_count: int
    first_witness_input: Tuple[object, ...] | None
    first_deleted_after_source: Tuple[object, ...] | None
    first_expected_target: Tuple[object, ...] | None

    @property
    def source_generator_deleted(self) -> bool:
        return self.source_generator_index in self.forget_stationary_indices

    @property
    def vertical_cube_cocycle_visible(self) -> bool:
        return self.mismatch_count > 0


@dataclass(frozen=True)
class PrefixDeletionCubeRestrictionAudit:
    """First three-face point-forgetting ledger for cube pressure."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    source_point_pushing_arity: int
    target_point_pushing_arity: int
    rows: Tuple[PrefixDeletionCubeRestrictionRow, ...]
    records_first_deletion_cube_surface: bool

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def total_mismatch_count(self) -> int:
        return sum(row.mismatch_count for row in self.rows)

    @property
    def deleted_generator_mismatch_count(self) -> int:
        return sum(
            row.mismatch_count
            for row in self.rows
            if row.source_generator_deleted
        )

    @property
    def surviving_generator_all_match(self) -> bool:
        return all(
            row.matches_marked_triple_restriction
            for row in self.rows
            if not row.source_generator_deleted
        )

    @property
    def deletion_orders_all_commute(self) -> bool:
        return all(row.deletion_orders_commute for row in self.rows)

    @property
    def all_rows_match(self) -> bool:
        return all(row.matches_marked_triple_restriction for row in self.rows)

    @property
    def verifies_first_deletion_cube_surface(self) -> bool:
        return (
            self.source_point_pushing_arity == 5
            and self.target_point_pushing_arity == 2
            and self.row_count == 50
            and self.deletion_orders_all_commute
            and self.records_first_deletion_cube_surface
        )


@dataclass(frozen=True)
class PrefixVerticalDefectTransformRow:
    """A deleted-generator point-forgetting defect as a target-tuple map."""

    deletion_level: int
    source_point_pushing_arity: int
    source_braid_index: int
    target_point_pushing_arity: int
    target_braid_index: int
    forget_stationary_indices: Tuple[int, ...]
    source_generator_index: int
    source_braid_word: BraidWord
    source_tuple_count: int
    target_tuple_count: int
    well_defined_on_deleted_tuple: bool
    ambiguous_deleted_tuple_count: int
    max_outputs_per_deleted_tuple: int
    defect_is_permutation: bool
    defect_permutation: Permutation | None
    defect_order: int | None
    identity_defect: bool | None
    first_witness_input: Tuple[object, ...] | None
    first_deleted_input: Tuple[object, ...] | None
    first_deleted_after_source: Tuple[object, ...] | None

    @property
    def nontrivial_defect(self) -> bool:
        return self.identity_defect is False


@dataclass(frozen=True)
class PrefixVerticalDefectTransformAudit:
    """Coefficient-candidate extraction from diagonal deletion defects."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    rows: Tuple[PrefixVerticalDefectTransformRow, ...]
    records_vertical_defect_transform_extraction: bool

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def all_defects_well_defined(self) -> bool:
        return all(row.well_defined_on_deleted_tuple for row in self.rows)

    @property
    def all_defects_are_permutations(self) -> bool:
        return all(row.defect_is_permutation for row in self.rows)

    @property
    def nontrivial_defect_count(self) -> int:
        return sum(1 for row in self.rows if row.nontrivial_defect)

    @property
    def order_spectrum(self) -> Tuple[int, ...]:
        return tuple(sorted({row.defect_order for row in self.rows if row.defect_order}))

    @property
    def verifies_vertical_defect_transform_extraction(self) -> bool:
        return (
            self.row_count == 54
            and self.all_defects_well_defined
            and self.all_defects_are_permutations
            and self.records_vertical_defect_transform_extraction
        )


@dataclass(frozen=True)
class PrefixVerticalDefectTransportRow:
    """Transport of an already-vertical defect across one more deletion."""

    source_point_pushing_arity: int
    source_braid_index: int
    from_deletion_level: int
    to_deletion_level: int
    from_forget_stationary_indices: Tuple[int, ...]
    extra_stationary_index: int
    to_forget_stationary_indices: Tuple[int, ...]
    source_generator_index: int
    from_target_braid_index: int
    to_target_braid_index: int
    from_target_tuple_count: int
    to_target_tuple_count: int
    additional_face_surjective: bool
    from_defect_is_permutation: bool
    to_defect_is_permutation: bool
    from_defect_order: int | None
    to_defect_order: int | None
    from_identity_defect: bool | None
    to_identity_defect: bool | None
    transport_commutes: bool
    mismatch_count: int
    first_witness_target_input: Tuple[object, ...] | None
    first_left_after_defect_then_delete: Tuple[object, ...] | None
    first_right_after_delete_then_defect: Tuple[object, ...] | None

    @property
    def defects_are_transportable(self) -> bool:
        return (
            self.additional_face_surjective
            and self.from_defect_is_permutation
            and self.to_defect_is_permutation
        )


@dataclass(frozen=True)
class PrefixVerticalDefectTransportAudit:
    """First face-transport check for vertical coefficient candidates."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    source_point_pushing_arity: int
    rows: Tuple[PrefixVerticalDefectTransportRow, ...]
    records_first_vertical_defect_face_transport: bool

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def all_additional_faces_surjective(self) -> bool:
        return all(row.additional_face_surjective for row in self.rows)

    @property
    def all_defects_are_transportable(self) -> bool:
        return all(row.defects_are_transportable for row in self.rows)

    @property
    def all_transports_commute(self) -> bool:
        return all(row.transport_commutes for row in self.rows)

    @property
    def total_mismatch_count(self) -> int:
        return sum(row.mismatch_count for row in self.rows)

    @property
    def order_pair_spectrum(self) -> Tuple[Tuple[int, int], ...]:
        return tuple(
            sorted(
                {
                    (row.from_defect_order, row.to_defect_order)
                    for row in self.rows
                    if (
                        row.from_defect_order is not None
                        and row.to_defect_order is not None
                    )
                }
            )
        )

    @property
    def verifies_first_vertical_defect_face_transport(self) -> bool:
        return (
            self.source_point_pushing_arity == 5
            and self.row_count == 80
            and self.all_defects_are_transportable
            and self.all_transports_commute
            and self.records_first_vertical_defect_face_transport
        )


@dataclass(frozen=True)
class PrefixVerticalPeifferSquareRow:
    """Peiffer commutator of two diagonal defects on a deletion square."""

    source_point_pushing_arity: int
    source_braid_index: int
    forget_stationary_indices: Tuple[int, int]
    first_source_generator_index: int
    second_source_generator_index: int
    target_braid_index: int
    target_tuple_count: int
    first_defect_is_permutation: bool
    second_defect_is_permutation: bool
    first_defect_order: int | None
    second_defect_order: int | None
    first_single_transport_commutes: bool
    second_single_transport_commutes: bool
    peiffer_commutator_permutation: Permutation | None
    peiffer_commutator_order: int | None
    peiffer_commutator_is_identity: bool | None
    peiffer_moved_tuple_count: int
    first_witness_target_input: Tuple[object, ...] | None
    first_witness_after_commutator: Tuple[object, ...] | None

    @property
    def defects_are_permutations(self) -> bool:
        return self.first_defect_is_permutation and self.second_defect_is_permutation

    @property
    def single_transports_commute(self) -> bool:
        return self.first_single_transport_commutes and self.second_single_transport_commutes

    @property
    def nontrivial_peiffer_boundary(self) -> bool:
        return self.peiffer_commutator_is_identity is False


@dataclass(frozen=True)
class PrefixVerticalPeifferSquareAudit:
    """First Peiffer square-boundary computation for vertical defects."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    source_point_pushing_arity: int
    rows: Tuple[PrefixVerticalPeifferSquareRow, ...]
    records_first_vertical_peiffer_square_boundary: bool

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def all_defects_are_permutations(self) -> bool:
        return all(row.defects_are_permutations for row in self.rows)

    @property
    def all_single_transports_commute(self) -> bool:
        return all(row.single_transports_commute for row in self.rows)

    @property
    def all_peiffer_boundaries_identity(self) -> bool:
        return all(row.peiffer_commutator_is_identity for row in self.rows)

    @property
    def nontrivial_peiffer_boundary_count(self) -> int:
        return sum(1 for row in self.rows if row.nontrivial_peiffer_boundary)

    @property
    def total_peiffer_moved_tuple_count(self) -> int:
        return sum(row.peiffer_moved_tuple_count for row in self.rows)

    @property
    def defect_order_pair_spectrum(self) -> Tuple[Tuple[int, int], ...]:
        return tuple(
            sorted(
                {
                    (row.first_defect_order, row.second_defect_order)
                    for row in self.rows
                    if (
                        row.first_defect_order is not None
                        and row.second_defect_order is not None
                    )
                }
            )
        )

    @property
    def peiffer_order_spectrum(self) -> Tuple[int, ...]:
        return tuple(
            sorted(
                {
                    row.peiffer_commutator_order
                    for row in self.rows
                    if row.peiffer_commutator_order is not None
                }
            )
        )

    @property
    def verifies_first_vertical_peiffer_square_boundary(self) -> bool:
        return (
            self.source_point_pushing_arity == 5
            and self.row_count == 10
            and self.all_defects_are_permutations
            and self.all_single_transports_commute
            and self.records_first_vertical_peiffer_square_boundary
        )


@dataclass(frozen=True)
class PrefixVerticalPeifferCubeTransportRow:
    """Transport of a Peiffer square boundary across a third deletion."""

    source_point_pushing_arity: int
    source_braid_index: int
    triple_forget_stationary_indices: Tuple[int, int, int]
    pair_forget_stationary_indices: Tuple[int, int]
    extra_stationary_index: int
    first_source_generator_index: int
    second_source_generator_index: int
    pair_target_braid_index: int
    triple_target_braid_index: int
    pair_target_tuple_count: int
    triple_target_tuple_count: int
    pair_defect_order_pair: Tuple[int | None, int | None]
    triple_defect_order_pair: Tuple[int | None, int | None]
    pair_peiffer_is_permutation: bool
    triple_peiffer_is_permutation: bool
    pair_peiffer_order: int | None
    triple_peiffer_order: int | None
    pair_peiffer_identity: bool | None
    triple_peiffer_identity: bool | None
    pair_peiffer_moved_tuple_count: int
    triple_peiffer_moved_tuple_count: int
    additional_face_surjective: bool
    peiffer_transport_commutes: bool
    mismatch_count: int
    first_witness_pair_target_input: Tuple[object, ...] | None
    first_left_after_pair_peiffer_then_delete: Tuple[object, ...] | None
    first_right_after_delete_then_triple_peiffer: Tuple[object, ...] | None

    @property
    def peiffer_boundaries_are_transportable(self) -> bool:
        return (
            self.additional_face_surjective
            and self.pair_peiffer_is_permutation
            and self.triple_peiffer_is_permutation
        )


@dataclass(frozen=True)
class PrefixVerticalPeifferCubeTransportAudit:
    """First cube-transport check for vertical Peiffer square boundaries."""

    element_count: int
    left_prefix_monoid_size: int
    nonunit_prefix_count: int
    source_point_pushing_arity: int
    rows: Tuple[PrefixVerticalPeifferCubeTransportRow, ...]
    records_first_vertical_peiffer_cube_transport: bool

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def all_peiffer_boundaries_transportable(self) -> bool:
        return all(row.peiffer_boundaries_are_transportable for row in self.rows)

    @property
    def all_peiffer_transports_commute(self) -> bool:
        return all(row.peiffer_transport_commutes for row in self.rows)

    @property
    def all_pair_peiffer_boundaries_identity(self) -> bool:
        return all(row.pair_peiffer_identity for row in self.rows)

    @property
    def all_triple_peiffer_boundaries_identity(self) -> bool:
        return all(row.triple_peiffer_identity for row in self.rows)

    @property
    def total_mismatch_count(self) -> int:
        return sum(row.mismatch_count for row in self.rows)

    @property
    def total_pair_peiffer_moved_tuple_count(self) -> int:
        return sum(row.pair_peiffer_moved_tuple_count for row in self.rows)

    @property
    def total_triple_peiffer_moved_tuple_count(self) -> int:
        return sum(row.triple_peiffer_moved_tuple_count for row in self.rows)

    @property
    def peiffer_order_pair_spectrum(self) -> Tuple[Tuple[int, int], ...]:
        return tuple(
            sorted(
                {
                    (row.pair_peiffer_order, row.triple_peiffer_order)
                    for row in self.rows
                    if (
                        row.pair_peiffer_order is not None
                        and row.triple_peiffer_order is not None
                    )
                }
            )
        )

    @property
    def verifies_first_vertical_peiffer_cube_transport(self) -> bool:
        return (
            self.source_point_pushing_arity == 5
            and self.row_count == 30
            and self.all_peiffer_boundaries_transportable
            and self.all_peiffer_transports_commute
            and self.records_first_vertical_peiffer_cube_transport
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


def _transformation_order(transformation: Transformation) -> int | None:
    if not _transformation_is_permutation(transformation):
        return None
    return permutation_order(transformation)


def _translation_pair_labels(
    solution: FiniteBraidedSet,
) -> Mapping[object, Tuple[Transformation, Transformation]]:
    index = {element: position for position, element in enumerate(solution.elements)}
    labels = {}
    for element in solution.elements:
        left_translation = tuple(
            index[solution.R[(element, right)][0]]
            for right in solution.elements
        )
        right_translation = tuple(
            index[solution.R[(left, element)][1]]
            for left in solution.elements
        )
        labels[element] = (left_translation, right_translation)
    return labels


def _translation_pair_crossing_ambiguity_count(
    solution: FiniteBraidedSet,
    labels: Mapping[object, Tuple[Transformation, Transformation]],
) -> int:
    seen: dict[
        Tuple[
            Tuple[Transformation, Transformation],
            Tuple[Transformation, Transformation],
        ],
        Tuple[
            Tuple[Transformation, Transformation],
            Tuple[Transformation, Transformation],
        ],
    ] = {}
    ambiguities = 0
    for left, right in product(solution.elements, repeat=2):
        source = (labels[left], labels[right])
        out_left, out_right = solution.R[(left, right)]
        target = (labels[out_left], labels[out_right])
        previous = seen.get(source)
        if previous is None:
            seen[source] = target
        elif previous != target:
            ambiguities += 1
    return ambiguities


def _label_action_generator_images(
    solution: FiniteBraidedSet,
    arity: int,
    action_images: Mapping[int, Permutation],
    labels: Mapping[object, Tuple[Transformation, Transformation]],
) -> tuple[
    bool,
    int,
    int,
    Tuple[Tuple[Transformation, Transformation], ...],
    Mapping[int, Permutation],
]:
    braid_index = arity + 1
    tuple_values = tuple(product(solution.elements, repeat=braid_index))
    labels_by_tuple_index = tuple(
        tuple(labels[element] for element in tuple_value)
        for tuple_value in tuple_values
    )
    label_tuples = tuple(sorted(set(labels_by_tuple_index), key=repr))
    label_index = {label_tuple: index for index, label_tuple in enumerate(label_tuples)}
    fibre_sizes = {label_tuple: 0 for label_tuple in label_tuples}
    for label_tuple in labels_by_tuple_index:
        fibre_sizes[label_tuple] += 1
    max_fibre_size = max(fibre_sizes.values(), default=0)
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
                return (
                    False,
                    len(label_tuples),
                    max_fibre_size,
                    labels_by_tuple_index,
                    {},
                )
        if any(value is None for value in image_by_label):
            return (
                False,
                len(label_tuples),
                max_fibre_size,
                labels_by_tuple_index,
                {},
            )
        label_images[generator] = tuple(
            value for value in image_by_label if value is not None
        )
    return (
        True,
        len(label_tuples),
        max_fibre_size,
        labels_by_tuple_index,
        label_images,
    )


def _permutation_subgroup_exponent(subgroup: Iterable[Permutation]) -> int:
    from .group_laws import lcm

    exponent = 1
    for permutation in subgroup:
        exponent = lcm(exponent, permutation_order(permutation))
    return exponent


def _canonical_section_displacement_count(
    action_images: Mapping[int, Permutation],
    label_images: Mapping[int, Permutation],
    labels_by_tuple_index: Sequence[Tuple[Tuple[Transformation, Transformation], ...]],
) -> int:
    label_tuples = tuple(sorted(set(labels_by_tuple_index), key=repr))
    label_index = {label_tuple: index for index, label_tuple in enumerate(label_tuples)}
    section_by_label_index: dict[int, int] = {}
    for tuple_index, label_tuple in enumerate(labels_by_tuple_index):
        current = section_by_label_index.get(label_index[label_tuple])
        if current is None or tuple_index < current:
            section_by_label_index[label_index[label_tuple]] = tuple_index

    displacement_count = 0
    for generator, action in action_images.items():
        label_action = label_images[generator]
        for source_label_index, source_tuple_index in section_by_label_index.items():
            target_label_index = label_action[source_label_index]
            expected_tuple_index = section_by_label_index[target_label_index]
            if action[source_tuple_index] != expected_tuple_index:
                displacement_count += 1
    return displacement_count


def _prefix_finite_base_pullback_gauge_row(
    solution: FiniteBraidedSet,
    point_pushing_arity: int,
    labels: Mapping[object, Tuple[Transformation, Transformation]],
    *,
    max_subgroup_size: int | None,
) -> PrefixFiniteBasePullbackGaugeRow:
    braid_index = point_pushing_arity + 1
    tuple_count = len(solution.elements) ** braid_index
    action_images = _point_pushing_action_generator_images(
        solution,
        point_pushing_arity,
    )
    (
        label_well_defined,
        label_tuple_count,
        max_label_fibre_size,
        labels_by_tuple_index,
        label_images,
    ) = _label_action_generator_images(
        solution,
        point_pushing_arity,
        action_images,
        labels,
    )
    if not label_well_defined:
        return PrefixFiniteBasePullbackGaugeRow(
            point_pushing_arity=point_pushing_arity,
            braid_index=braid_index,
            tuple_count=tuple_count,
            generator_count=len(action_images),
            label_tuple_count=label_tuple_count,
            max_label_fibre_size=max_label_fibre_size,
            label_action_well_defined=False,
            tuple_action_group_size=None,
            tuple_action_group_exponent=None,
            label_action_group_size=None,
            label_action_group_exponent=None,
            quotient_map_well_defined=None,
            vertical_kernel_size=None,
            vertical_kernel_exponent=None,
            canonical_section_displacement_count=None,
            canonical_section_gauge_trivial=None,
            truncated=False,
        )

    pair_generators = {
        generator: (action_images[generator], label_images[generator])
        for generator in sorted(action_images)
    }
    try:
        pair_subgroup = _generated_pair_subgroup_with_words(
            pair_generators,
            max_size=max_subgroup_size,
        )
    except ValueError:
        return PrefixFiniteBasePullbackGaugeRow(
            point_pushing_arity=point_pushing_arity,
            braid_index=braid_index,
            tuple_count=tuple_count,
            generator_count=len(action_images),
            label_tuple_count=label_tuple_count,
            max_label_fibre_size=max_label_fibre_size,
            label_action_well_defined=True,
            tuple_action_group_size=None,
            tuple_action_group_exponent=None,
            label_action_group_size=None,
            label_action_group_exponent=None,
            quotient_map_well_defined=None,
            vertical_kernel_size=None,
            vertical_kernel_exponent=None,
            canonical_section_displacement_count=None,
            canonical_section_gauge_trivial=None,
            truncated=True,
        )

    labels_by_tuple_action: dict[Permutation, Permutation] = {}
    quotient_map_well_defined = True
    for tuple_action, label_action in pair_subgroup:
        previous = labels_by_tuple_action.get(tuple_action)
        if previous is None:
            labels_by_tuple_action[tuple_action] = label_action
        elif previous != label_action:
            quotient_map_well_defined = False
            break

    tuple_subgroup = {tuple_action for tuple_action, _label_action in pair_subgroup}
    label_subgroup = {label_action for _tuple_action, label_action in pair_subgroup}
    label_identity = identity_permutation(label_tuple_count)
    vertical_kernel = {
        tuple_action
        for tuple_action, label_action in pair_subgroup
        if label_action == label_identity
    }
    section_displacement_count = _canonical_section_displacement_count(
        action_images,
        label_images,
        labels_by_tuple_index,
    )

    return PrefixFiniteBasePullbackGaugeRow(
        point_pushing_arity=point_pushing_arity,
        braid_index=braid_index,
        tuple_count=tuple_count,
        generator_count=len(action_images),
        label_tuple_count=label_tuple_count,
        max_label_fibre_size=max_label_fibre_size,
        label_action_well_defined=True,
        tuple_action_group_size=len(tuple_subgroup),
        tuple_action_group_exponent=_permutation_subgroup_exponent(tuple_subgroup),
        label_action_group_size=len(label_subgroup),
        label_action_group_exponent=_permutation_subgroup_exponent(label_subgroup),
        quotient_map_well_defined=quotient_map_well_defined,
        vertical_kernel_size=len(vertical_kernel),
        vertical_kernel_exponent=_permutation_subgroup_exponent(vertical_kernel),
        canonical_section_displacement_count=section_displacement_count,
        canonical_section_gauge_trivial=section_displacement_count == 0,
        truncated=False,
    )


def prefix_finite_base_pullback_gauge_audit(
    solution: FiniteBraidedSet,
    *,
    max_subgroup_size: int | None = None,
) -> PrefixFiniteBasePullbackGaugeAudit:
    """Audit the first fixed-base pullback/gauge pressure surface.

    The fixed candidate is the finite translation-pair label of an element:
    its left and right coordinate transformations.  This is a finite
    label-action base; the audit deliberately keeps the separate
    group-Hurwitz realization obligation visible.
    """

    labels = _translation_pair_labels(solution)
    left_labels = {label[0] for label in labels.values()}
    right_labels = {label[1] for label in labels.values()}
    crossing_ambiguities = _translation_pair_crossing_ambiguity_count(
        solution,
        labels,
    )
    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    defect_transport = prefix_vertical_defect_transport_audit(solution)
    peiffer_square = prefix_vertical_peiffer_square_audit(solution)
    peiffer_cube = prefix_vertical_peiffer_cube_transport_audit(solution)
    rows = tuple(
        _prefix_finite_base_pullback_gauge_row(
            solution,
            arity,
            labels,
            max_subgroup_size=max_subgroup_size,
        )
        for arity in (3, 4, 5)
    )
    observed_trivial = (
        defect_transport.total_mismatch_count == 0
        and peiffer_square.nontrivial_peiffer_boundary_count == 0
        and peiffer_cube.total_mismatch_count == 0
        and peiffer_cube.all_peiffer_transports_commute
    )
    return PrefixFiniteBasePullbackGaugeAudit(
        element_count=len(solution.elements),
        translation_pair_label_count=len(set(labels.values())),
        left_translation_label_count=len(left_labels),
        right_translation_label_count=len(right_labels),
        crossing_descends_to_translation_pair_labels=crossing_ambiguities == 0,
        crossing_label_ambiguity_count=crossing_ambiguities,
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        rows=rows,
        vertical_defect_transport_mismatch_count=(
            defect_transport.total_mismatch_count
        ),
        vertical_defect_order_spectrum=defect_transport.order_pair_spectrum[0]
        if len(defect_transport.order_pair_spectrum) == 1
        else tuple(
            sorted(
                {
                    order
                    for pair in defect_transport.order_pair_spectrum
                    for order in pair
                }
            )
        ),
        peiffer_square_nontrivial_boundary_count=(
            peiffer_square.nontrivial_peiffer_boundary_count
        ),
        peiffer_cube_transport_mismatch_count=peiffer_cube.total_mismatch_count,
        peiffer_order_pair_spectrum=peiffer_cube.peiffer_order_pair_spectrum,
        observed_deletion_two_cocycle_gauge_trivial=observed_trivial,
        fixed_translation_pair_base_only=True,
        group_hurwitz_realization_still_required=True,
    )


def pullback_coskeletal_criterion_audit() -> PullbackCoskeletalCriterionAudit:
    """Record the exact boundary of finite pullback/coskeletal reasoning.

    For one fixed proposed finite base, compatible finite truncation solution
    sets form an inverse system of finite sets.  A nonempty solution at every
    finite arity gives an all-arity branch by compactness.  This does not give
    a uniform bounded-arity cutoff; such a cutoff is an additional
    coskeletality/noetherian hypothesis.
    """

    cases = (
        PullbackCoskeletalCriterionCase(
            key="fixed_base_inverse_limit",
            role="valid_compactness_principle",
            finite_data=(
                "for one fixed base B, finite sets S_N(B) of gauge/pullback "
                "solutions through arity N and restriction maps "
                "S_{N+1}(B)->S_N(B)"
            ),
            criterion=(
                "every S_N(B) is nonempty and the restrictions make these "
                "sets an inverse system"
            ),
            consequence=(
                "König/compactness gives one compatible all-arity solution "
                "for that fixed base"
            ),
            failure_mode=(
                "some finite S_N(B) is empty; this is a real obstruction to "
                "that fixed base"
            ),
        ),
        PullbackCoskeletalCriterionCase(
            key="bounded_cutoff_requires_coskeletality",
            role="missing_positive_hypothesis",
            finite_data=(
                "a comparison tower whose cocycles, coefficient transports, "
                "and gauge cochains above arity d are forced by their "
                "d-skeleton"
            ),
            criterion=(
                "the tower is d-pullback-coskeletal and section-gauge "
                "relations are generated in arity at most d"
            ),
            consequence=(
                "checking the finite gauge/pullback system through arity d "
                "is enough for the fixed base"
            ),
            failure_mode=(
                "new independent obstruction coordinates can first appear in "
                "arbitrarily high arity"
            ),
        ),
        PullbackCoskeletalCriterionCase(
            key="finite_obstruction_certificate",
            role="valid_negative_certificate_for_fixed_base",
            finite_data=(
                "the finite system S_N(B) of base comparison maps, vertical "
                "coefficient labels, and section-change cochains"
            ),
            criterion="S_N(B) is empty for a specified finite arity N",
            consequence=(
                "no all-arity pullback to that fixed base exists, because "
                "any all-arity solution restricts to S_N(B)"
            ),
            failure_mode=(
                "nonemptiness of S_N(B) for small N alone does not certify "
                "an all-arity solution unless the inverse-system or "
                "coskeletal hypotheses are supplied"
            ),
        ),
        PullbackCoskeletalCriterionCase(
            key="general_uniform_cutoff_failure",
            role="warning_countermechanism",
            finite_data=(
                "a finite-state-looking tower with an independent new "
                "gauge/pullback constraint introduced at each higher arity"
            ),
            criterion=(
                "for every d there is a tower whose first failed constraint "
                "appears above d"
            ),
            consequence=(
                "there is no universal bounded-arity pullback test without "
                "extra finite-type or coskeletal structure"
            ),
            failure_mode=(
                "a proof that uses only bounded prefix checks silently assumes "
                "the missing pullback-coskeletal lemma"
            ),
        ),
    )
    return PullbackCoskeletalCriterionAudit(
        fixed_base_inverse_limit_compactness_recorded=True,
        uniform_bounded_arity_cutoff_rejected_without_extra_hypothesis=True,
        pullback_coskeletal_hypothesis_identified=True,
        finite_obstruction_certificate_identified=True,
        missing_pullback_coskeletal_lemma=(
            "finite YBE point-pushing deletion towers are d-pullback-coskeletal "
            "over one fixed finite operator-label Hurwitz base, for some d "
            "depending only on the finite solution or on the proposed base"
        ),
        cases=cases,
    )


def ybe_coskeletal_mechanism_audit() -> YBECoskeletalMechanismAudit:
    """Record YBE-specific routes toward or against pullback coskeletality.

    Finite bijective YBE data gives finite local transition rules, but local
    generation of braid/deletion moves is weaker than local detection of the
    nonabelian deletion-cohomology class.  A positive theorem needs a
    finite operator-label enrichment with genuine bounded-width descent for
    the groupoid and the one-, two-, and three-deletion coefficient bands.
    A negative route should build high-arity cross-effects invisible on every
    bounded skeleton.
    """

    cases = (
        YBECoskeletalMechanismCase(
            key="formal_w_local_descent_theorem",
            role="conditional_positive_theorem",
            mechanism=(
                "right Kan descent from arity at most w for the labelled "
                "point-pushing groupoid and from arity at most |D|+w for "
                "the deletion coefficient bands"
            ),
            finite_ybe_status=(
                "finite bijectivity alone does not provide this descent; it "
                "must be proved after adding suitable finite operator labels"
            ),
            theorem_obligation=(
                "prove w-local inverse-limit reconstruction and bounded "
                "relation arity r, then use N0=max(r,w+3)"
            ),
            obstruction_signature=(
                "compatible low-arity gauge/base solutions fail to extend "
                "because a high-arity Brunnian deletion 2-class survives"
            ),
        ),
        YBECoskeletalMechanismCase(
            key="fadell_neuwirth_recursion",
            role="necessary_but_insufficient_structure",
            mechanism=(
                "point-pushing generators and point-forgetting maps are "
                "recursive under the Fadell-Neuwirth tower"
            ),
            finite_ybe_status=(
                "finite YBE tables make each local transition finite and "
                "computable"
            ),
            theorem_obligation=(
                "prove that recursive generator descriptions also generate "
                "all deletion 2-cocycle relations in bounded arity"
            ),
            obstruction_signature=(
                "Brunnian vertical classes restrict trivially to all bounded "
                "faces while remaining nontrivial in higher arity"
            ),
        ),
        YBECoskeletalMechanismCase(
            key="finite_operator_state_recursion",
            role="positive_candidate",
            mechanism=(
                "augment tuples by finite operator labels so every Artin "
                "conjugacy update is read by a fixed finite transducer"
            ),
            finite_ybe_status=(
                "finite labels can make local moves deterministic on a chosen "
                "finite state space"
            ),
            theorem_obligation=(
                "show the transducer state is complete for vertical "
                "fibre-bisection cohomology, not merely for tuple motion"
            ),
            obstruction_signature=(
                "two towers with identical finite operator-state histories "
                "but different high-arity vertical 2-cocycles"
            ),
        ),
        YBECoskeletalMechanismCase(
            key="garside_or_automaton_normal_forms",
            role="possible_finite_type_tool",
            mechanism=(
                "use braid or pure-braid normal forms to recognize Artin "
                "conjugacy words by finite or noetherian rewriting"
            ),
            finite_ybe_status=(
                "normal forms control braid words but not automatically the "
                "deletion-gauge cohomology quotient"
            ),
            theorem_obligation=(
                "prove that normal-form rewriting induces a finite complete "
                "rewriting system on vertical cocycle representatives"
            ),
            obstruction_signature=(
                "normal-form length grows while all bounded deletion shadows "
                "stay gauge-trivial"
            ),
        ),
        YBECoskeletalMechanismCase(
            key="fi_fb_finite_generation",
            role="strong_positive_hypothesis",
            mechanism=(
                "view vertical bisection groups, deletion cochains, and "
                "2-cocycles as an FI/FB-type module or nonabelian analogue"
            ),
            finite_ybe_status=(
                "finite sets supply finite fibres in each arity but not "
                "finite generation as a tower"
            ),
            theorem_obligation=(
                "establish finite generation/noetherianity for the relevant "
                "coefficient and obstruction functors"
            ),
            obstruction_signature=(
                "new orbit types or coefficient generators appear in "
                "unbounded arity"
            ),
        ),
        YBECoskeletalMechanismCase(
            key="brunnian_cross_effect_obstruction",
            role="negative_countermechanism",
            mechanism=(
                "construct vertical bisections supported only on genuinely "
                "multi-point interactions"
            ),
            finite_ybe_status=(
                "finite bijectivity does not by itself forbid high-order "
                "cross-effects"
            ),
            theorem_obligation=(
                "rule out or bound Brunnian cross-effects using YBE-specific "
                "identities"
            ),
            obstruction_signature=(
                "for every bound d, a nontrivial deletion 2-cocycle appears "
                "whose restriction to every d-skeleton is gauge-trivial"
            ),
        ),
    )
    return YBECoskeletalMechanismAudit(
        finite_bijectivity_gives_local_generation=True,
        finite_bijectivity_does_not_give_local_cohomology_detection=True,
        bounded_state_recursion_would_imply_coskeletality=True,
        high_cross_effect_bisections_are_live_obstruction=True,
        w_local_operator_label_descent_is_extra_hypothesis=True,
        coefficient_inverse_limit_condition_recorded=True,
        comparison_commutes_with_inverse_limits_recorded=True,
        bounded_relation_arity_cutoff_recorded=True,
        brunnian_cross_effect_criterion_recorded=True,
        cutoff_formula="N0 = max(r, w + 3)",
        conditional_pullback_coskeletal_theorem=(
            "[Omega] is in im Pi^sharp iff the truncation "
            "[Omega_<=N0] is in im Pi^sharp_<=N0, equivalently all-arity "
            "base cocycle and gauge data exist iff they exist through arity N0"
        ),
        brunnian_cross_effect_formula=(
            "cr_ij^I(A) = intersection over k in I\\{i,j} of "
            "ker(A_ij^I -> A_ij^{I\\{k}})"
        ),
        brunnian_obstruction_criterion=(
            "bounded pullback-coskeletality for a fixed labelled tower "
            "requires Br^2_I(C,A;B)=1 for all sufficiently large I, together "
            "with effective low-arity coefficient descent"
        ),
        positive_ybe_theorem_obligations=(
            "prove w-local inverse-limit reconstruction for operator labels",
            (
                "prove coefficient inverse-limit reconstruction for "
                "one-, two-, and three-deletion bands"
            ),
            (
                "prove bounded relation arity for transport, cocycle, "
                "and gauge equations"
            ),
            (
                "prove vanishing of Brunnian relative deletion "
                "2-obstructions above the cutoff"
            ),
        ),
        cases=cases,
    )


def ybe_brunnian_derivative_gate_audit() -> YBEBrunnianDerivativeGateAudit:
    """Record the derivative gate for Brunnian deletion H^2 obstructions.

    Brunnian point-pushing elements naturally give one-deletion vertical
    bisections.  Their first deletion derivatives are two-deletion bisections,
    but those derivatives are exactly section-gauge coboundaries.  Hence a
    genuine high-arity deletion 2-class must survive the residual quotient by
    one-strand derivatives, bounded two-strand mutual terms, and fixed-base
    pullback.
    """

    cases = (
        YBEBrunnianDerivativeGateCase(
            key="one_strand_derivative_gauge_gate",
            role="gauge_triviality",
            statement=(
                "for b in the one-deletion vertical group V_p^I, the deletion "
                "derivative nabla_q b is the square coboundary of the "
                "1-cochain with u_p^I=b"
            ),
            consequence=(
                "ordinary point-pushing derivatives land in deletion degree 2 "
                "but represent the trivial gauge class"
            ),
        ),
        YBEBrunnianDerivativeGateCase(
            key="pure_braid_brunnian_shadow_triviality",
            role="false_counterexample_removed",
            statement=(
                "if a Brunnian pure braid is killed by deleting p and q, its "
                "transported two-deletion bisection is tau_q(b_beta)=nabla_q b_beta"
            ),
            consequence=(
                "Brunnian pure-braid subgroups can survive as vertical "
                "bisections without producing nonzero Br^2 classes"
            ),
        ),
        YBEBrunnianDerivativeGateCase(
            key="nonabelian_derivative_chain_rule",
            role="coherence_identity",
            statement=(
                "the second derivatives nabla_r(nabla_q b) and "
                "nabla_q(nabla_r b) agree after the Peiffer and cube "
                "transport defects have been killed"
            ),
            consequence=(
                "YBE locality makes point-pushing derivatives satisfy the "
                "cocycle equation precisely because they are coboundaries"
            ),
        ),
        YBEBrunnianDerivativeGateCase(
            key="residual_double_deletion_quotient",
            role="true_obstruction_target",
            statement=(
                "a nonzero high-arity Brunnian deletion 2-class must survive "
                "the quotient by one-strand derivatives, bounded mutual "
                "two-strand data, and fixed-base pullback"
            ),
            consequence=(
                "the counterexample search narrows to residual double-deletion "
                "vertical bisections, not arbitrary Brunnian pure braids"
            ),
        ),
        YBEBrunnianDerivativeGateCase(
            key="fadell_neuwirth_decomposition_route",
            role="positive_route",
            statement=(
                "if every double-deletion vertical bisection decomposes as "
                "one-strand derivatives times a bounded mutual term and a "
                "fixed-base pullback, then the residual quotient is trivial"
            ),
            consequence=(
                "after finite labels for derivative images and bounded mutual "
                "terms, arbitrarily high Brunnian relative deletion 2-classes vanish"
            ),
        ),
    )
    return YBEBrunnianDerivativeGateAudit(
        naive_brunnian_pure_braid_obstruction_rejected=True,
        one_strand_derivatives_are_gauge_coboundaries=True,
        brunnian_point_push_shadow_is_gauge=True,
        nonabelian_derivative_chain_rule_recorded=True,
        residual_double_deletion_quotient_identified=True,
        fadell_neuwirth_decomposition_would_kill_high_brunnian_classes=True,
        derivative_formula="nabla_q b = tau_q(b) inf_q(partial_q b)^-1",
        gauge_formula="(delta u)_{p,q}^I = nabla_q b",
        chain_rule_formula="nabla_r(nabla_q b) = nabla_q(nabla_r b)",
        residual_quotient_formula=(
            "R_{p,q}^I = V_{p,q}^{I,Br} / "
            "<nabla_q V_p^{I,Br}, nabla_p V_q^{I,Br}, "
            "M_{p,q}^I, Pi^sharp V_{p,q,B}^{I,Br}>"
        ),
        decomposition_formula=(
            "a = nabla_q b_p nabla_p b_q m_{p,q} Pi^sharp(theta)"
        ),
        cases=cases,
    )


def ybe_crossed_square_residual_audit() -> YBECrossedSquareResidualAudit:
    """Record the crossed-square criterion for the residual quotient.

    The two stationary deletion maps form a crossed square of finite
    bisection groups.  The residual quotient from the Brunnian derivative gate
    splits into a boundary quotient and a Moore-Peiffer homology quotient.
    This audit records the exact sequence and the vanishing/obstruction
    criteria supplied by that crossed-square algebra.
    """

    cases = (
        YBECrossedSquareResidualCase(
            key="crossed_square_bisection_model",
            role="model",
            statement=(
                "the two deletion maps p and q give a crossed square "
                "L -> M, L -> N, M -> P, N -> P of finite vertical "
                "bisection groups over each survivor object"
            ),
            consequence=(
                "the Peiffer pairing h:M x N -> L is the intrinsic source of "
                "the bounded mutual two-strand subgroup"
            ),
        ),
        YBECrossedSquareResidualCase(
            key="residual_exact_sequence",
            role="exact_sequence",
            statement=(
                "for L=V_{p,q}^{I,Br}, D_{p,q}=<E_{p,q}, M_{p,q}, B_{p,q}>^L, "
                "and K=ker(partial:L -> M x N), there is an exact sequence "
                "1 -> K/(K cap D_{p,q}) -> R_{p,q}^I -> partial L/partial D_{p,q} -> 1"
            ),
            consequence=(
                "the residual quotient vanishes exactly when both the boundary "
                "quotient and the Moore-Peiffer quotient vanish"
            ),
        ),
        YBECrossedSquareResidualCase(
            key="boundary_obstruction",
            role="quotient_obstruction",
            statement=(
                "H_partial^square(I;p,q|B)=partial L/partial D_{p,q}"
            ),
            consequence=(
                "a nonzero boundary class means some Brunnian double-deletion "
                "bisection has one-face boundary not produced by edge, Peiffer, "
                "or base terms"
            ),
        ),
        YBECrossedSquareResidualCase(
            key="moore_peiffer_homology",
            role="cycle_obstruction",
            statement=(
                "H_2^square(I;p,q|B)=K/(K cap D_{p,q})"
            ),
            consequence=(
                "a nonzero Moore-Peiffer class is a square-internal Brunnian "
                "vertical cycle not generated by edge, Peiffer mutual, or base "
                "pullback cycles"
            ),
        ),
        YBECrossedSquareResidualCase(
            key="peiffer_complete_vanishing_theorem",
            role="positive_route",
            statement=(
                "if partial L=partial E_{p,q} and K <= <im kappa, B_{p,q}>^L, "
                "then R_{p,q}^I=1"
            ),
            consequence=(
                "finite operator labels only need to make the crossed square "
                "Peiffer-complete on Brunnian boundaries and Moore cycles"
            ),
        ),
        YBECrossedSquareResidualCase(
            key="crossed_square_countercertificate",
            role="negative_route",
            statement=(
                "a family of invariants chi_I on K killing E_{p,q}, im kappa, "
                "and fixed-base pullback but not a_I certifies nonzero "
                "H_2^square and hence nonzero R_{p,q}^I"
            ),
            consequence=(
                "a counterexample must now exhibit crossed-square homology "
                "surviving every fixed finite operator-label base"
            ),
        ),
    )
    return YBECrossedSquareResidualAudit(
        crossed_square_model_identified=True,
        edge_degenerate_subgroup_identified=True,
        peiffer_mutual_subgroup_identified=True,
        fixed_base_pullback_subgroup_identified=True,
        residual_exact_sequence_recorded=True,
        boundary_obstruction_identified=True,
        moore_peiffer_obstruction_identified=True,
        peiffer_complete_vanishing_theorem_recorded=True,
        obstruction_invariant_form_recorded=True,
        crossed_square_vertices=("L", "M", "N", "P"),
        residual_quotient_formula=(
            "R_{p,q}^I = L / D_{p,q}, where "
            "D_{p,q}=<E_{p,q}, M_{p,q}, B_{p,q}>^L"
        ),
        exact_sequence_formula=(
            "1 -> K/(K cap D_{p,q}) -> R_{p,q}^I -> "
            "partial L/partial D_{p,q} -> 1"
        ),
        boundary_obstruction_formula=(
            "H_partial^square(I;p,q|B) = partial L/partial D_{p,q}"
        ),
        moore_peiffer_obstruction_formula=(
            "H_2^square(I;p,q|B) = K/(K cap D_{p,q})"
        ),
        compact_vanishing_formula=(
            "partial L = partial E_{p,q} and "
            "K <= <im kappa, B_{p,q}>^L imply R_{p,q}^I = 1"
        ),
        obstruction_invariant_formula=(
            "chi_I: K -> Q_I kills E_{p,q}, im kappa, and "
            "Pi^sharp V_{p,q,B}^{I,Br}, but chi_I(a_I) != 1"
        ),
        cases=cases,
    )


def ybe_finite_state_rack_cover_audit() -> YBEFiniteStateRackCoverAudit:
    """Record the finite-state criterion for direct rack-cover attempts.

    A coordinatewise rack quotient cannot model a general bijective YBE
    solution because a rack switch copies one strand while a YBE switch updates
    both strands.  The remaining possible direct route is a marked quotient
    with a finite decoder state; this audit records the local equations such a
    decoder must satisfy.
    """

    cases = (
        YBEFiniteStateRackCoverCase(
            key="coordinatewise_rack_quotient_obstruction",
            role="negative_coordinatewise",
            statement=(
                "if pi:Y -> X is a coordinatewise quotient from a rack switch "
                "R_Y(a,b)=(a > b,a), then pi(a)=rho_{pi(b)}(pi(a)) for all "
                "a,b"
            ),
            consequence=(
                "surjectivity forces rho_y(x)=x for every x,y, so general "
                "YBE solutions cannot be covered coordinatewise by a rack"
            ),
        ),
        YBEFiniteStateRackCoverCase(
            key="fiber_label_first_coordinate_obstruction",
            role="negative_fiber_label",
            statement=(
                "a fibre-labelled operation (x,s)>(y,t) with first coordinate "
                "lambda_x(y) requires the maps lambda_x to be bijective and "
                "cannot repair first-coordinate identities using labels"
            ),
            consequence=(
                "left-degenerate solutions are excluded immediately, and even "
                "nondegenerate solutions face a rack-shadow identity stronger "
                "than the YBE identity"
            ),
        ),
        YBEFiniteStateRackCoverCase(
            key="rack_shadow_identity_gap",
            role="operator_gap",
            statement=(
                "rack self-distributivity forces lambda_x lambda_y = "
                "lambda_{lambda_x(y)} lambda_x, while YBE gives "
                "lambda_x lambda_y = lambda_{lambda_x(y)} lambda_{rho_y(x)}"
            ),
            consequence=(
                "the copied rack strand would need to carry future operator "
                "lambda_{rho_y(x)} even though it remains the old x-strand"
            ),
        ),
        YBEFiniteStateRackCoverCase(
            key="label_cocycle_equation",
            role="remaining_label_problem",
            statement=(
                "if the first-coordinate gap vanishes, the fibre labels must "
                "still solve a nonabelian rack cocycle equation for alpha"
            ),
            consequence=(
                "finite labels are extra data; the YBE equations do not by "
                "themselves supply the required alpha-cocycle"
            ),
        ),
        YBEFiniteStateRackCoverCase(
            key="finite_state_decoder_criterion",
            role="positive_reformulation",
            statement=(
                "a marked quotient can only evade the copy obstruction by "
                "using a finite decoder state q with maps d:Q x Y -> X and "
                "tau:Q x Y -> Q satisfying the local two-symbol equations"
            ),
            consequence=(
                "finite rack domination by a direct cover reduces to a finite "
                "transducer/cocycle problem plus surjectivity of every decoded "
                "map Phi_n"
            ),
        ),
        YBEFiniteStateRackCoverCase(
            key="structure_group_same_copy_obstruction",
            role="group_rack_warning",
            statement=(
                "a finite quotient of the structure group used as a conjugation "
                "rack has the same copied second output g in (g,h)->(ghg^-1,g)"
            ),
            consequence=(
                "without finite decoder context, the group-rack approach also "
                "cannot make the copied x-strand represent rho_y(x)"
            ),
        ),
    )
    return YBEFiniteStateRackCoverAudit(
        coordinatewise_rack_quotient_obstruction_identified=True,
        fiber_label_first_coordinate_obstruction_identified=True,
        rack_shadow_identity_recorded=True,
        label_cocycle_equation_recorded=True,
        finite_state_decoder_criterion_recorded=True,
        decoder_surjectivity_requirement_recorded=True,
        structure_group_obstruction_recorded=True,
        right_update_defect_identified=True,
        rack_switch_formula="R_Y(a,b)=(a > b,a)",
        coordinatewise_obstruction_formula=(
            "pi(a)=rho_{pi(b)}(pi(a)); surjectivity implies rho_y(x)=x"
        ),
        rack_shadow_identity_formula=(
            "lambda_x lambda_y = lambda_{lambda_x(y)} lambda_x"
        ),
        ybe_twisted_identity_formula=(
            "lambda_x lambda_y = lambda_{lambda_x(y)} lambda_{rho_y(x)}"
        ),
        label_cocycle_formula=(
            "alpha_{x,lambda_y(z)}(s,alpha_{y,z}(t,u)) = "
            "alpha_{lambda_x(y),lambda_x(z)}("
            "alpha_{x,y}(s,t),alpha_{x,z}(s,u))"
        ),
        decoder_equations_formula=(
            "d(q,a > b)=lambda_{d(q,a)}(d(tau(q,a),b)); "
            "d(tau(q,a > b),a)=rho_{d(tau(q,a),b)}(d(q,a)); "
            "tau(tau(q,a > b),a)=tau(tau(q,a),b)"
        ),
        right_update_defect_formula=(
            "Delta(x,y)=lambda_{rho_y(x)} lambda_x^-1"
        ),
        cases=cases,
    )


def ybe_equivariant_reconstruction_closure_audit(
) -> YBEEquivariantReconstructionClosureAudit:
    """Record the safe gluing theorem for quotient/block detector products.

    Known quotient, subsolution, and subquotient branches can be multiplied
    only after their marked action towers reconstruct the whole X-tower
    equivariantly and injectively in every arity.  Point separation at arity 1
    or separately dominated components can miss off-diagonal transition and
    extension-fibre data.
    """

    cases = (
        YBEEquivariantReconstructionClosureCase(
            key="marked_tower_reconstruction",
            role="sufficient_data",
            statement=(
                "for every n, the chosen quotient, block, and subquotient "
                "readouts assemble to a B_n-equivariant map "
                "R_n:X^n -> product_j T_{j,n}"
            ),
            consequence=(
                "the product factors describe the same marked braid-action "
                "tower only when R_n is injective on the actual X^n states"
            ),
        ),
        YBEEquivariantReconstructionClosureCase(
            key="product_kernel_implication",
            role="positive_theorem",
            statement=(
                "if each factor T_j is dominated by a finite rack detector "
                "Y_j and R_n is B_n-equivariant and injective for all n, then "
                "the product rack detector prod_j Y_j dominates X"
            ),
            consequence=(
                "a braid acting trivially on every rack factor fixes every "
                "T_{j,n}-coordinate, hence fixes R_n(x), hence fixes x by "
                "injectivity"
            ),
        ),
        YBEEquivariantReconstructionClosureCase(
            key="total_quotient_corollary",
            role="quotient_corollary",
            statement=(
                "if pi_j:X -> Z_j are genuine YBE quotient maps and the "
                "combined map pi=(pi_j)_j is injective on X, then pi^n is "
                "B_n-equivariant and injective on X^n for every n"
            ),
            consequence=(
                "point-separating total quotient maps are enough when they "
                "are genuine YBE quotients and each Z_j is already dominated"
            ),
        ),
        YBEEquivariantReconstructionClosureCase(
            key="partial_subquotient_domain_totalization",
            role="domain_guardrail",
            statement=(
                "partial subquotients and crossing-closed blocks must be "
                "encoded as total marked factors, including their defined "
                "domain, incidence, and exit data"
            ),
            consequence=(
                "a partial map that is injective only on its own domain cannot "
                "be used in a product proof until the product records which "
                "tuples lie in that domain after every braid move"
            ),
        ),
        YBEEquivariantReconstructionClosureCase(
            key="point_separation_not_enough",
            role="negative_warning",
            statement=(
                "coordinatewise point-separating quotients, or separately "
                "dominated crossing-closed components, need not reconstruct "
                "the all-arity marked action tower"
            ),
            consequence=(
                "two tuples can agree in every visible component while a "
                "braid in the visible kernel permutes hidden extension fibres"
            ),
        ),
        YBEEquivariantReconstructionClosureCase(
            key="off_diagonal_transition_data",
            role="missing_data",
            statement=(
                "mixed-block crossings require explicit block incidence "
                "maps, transition groupoids, and fibre actions over the "
                "visible quotient states"
            ),
            consequence=(
                "the gluing theorem needs the off-diagonal transition data, "
                "not just detectors for the diagonal components"
            ),
        ),
        YBEEquivariantReconstructionClosureCase(
            key="arity3_extension_cocycle_obstruction",
            role="arity3_stress",
            statement=(
                "at arity 3, the two YBE paths can agree in all visible "
                "quotients while differing by a coherent extension-fibre "
                "cocycle omega_{z,z'}"
            ),
            consequence=(
                "the YBE equation makes this hidden fibre action coherent, "
                "but it does not force it to be visible to the chosen product "
                "detectors"
            ),
        ),
        YBEEquivariantReconstructionClosureCase(
            key="hidden_fibre_visible_kernel_criterion",
            role="exact_criterion",
            statement=(
                "for any finite family of visible marked factors, the visible "
                "kernel K_vis,n must act trivially on every hidden fibre "
                "H_t=F_n^-1(t)"
            ),
            consequence=(
                "visible product detectors dominate X if and only if this "
                "hidden-fibre action is trivial; injective reconstruction is "
                "the simple sufficient case where all H_t are singletons"
            ),
        ),
    )
    return YBEEquivariantReconstructionClosureAudit(
        marked_tower_reconstruction_recorded=True,
        product_kernel_implication_recorded=True,
        total_quotient_corollary_recorded=True,
        partial_domain_totalization_required=True,
        point_separation_insufficient_recorded=True,
        off_diagonal_transition_data_required=True,
        arity3_extension_cocycle_obstruction_recorded=True,
        hidden_fibre_kernel_criterion_recorded=True,
        reconstruction_formula=(
            "R_n:X^n -> product_j T_{j,n} is B_n-equivariant and injective "
            "for every n"
        ),
        product_kernel_formula=(
            "ker rho_product,n <= ker rho_X,n follows from equivariant "
            "injective reconstruction"
        ),
        total_quotient_formula=(
            "for genuine YBE quotients pi_j, injective pi:X->product_j Z_j "
            "implies injective pi^n:X^n->product_j Z_j^n"
        ),
        visible_kernel_formula=(
            "K_vis,n = intersection_j ker(B_n action on T_{j,n}) may still "
            "act on hidden fibres if R_n is not injective"
        ),
        hidden_fibre_formula=(
            "visible detectors dominate iff K_vis,n acts trivially on every "
            "H_t=F_n^-1(t)"
        ),
        partial_domain_formula=(
            "partial subquotient data must be totalized by recording domain, "
            "incidence, exits, and braid transport of definedness"
        ),
        extension_cocycle_formula=(
            "mixed-block extension fibres can carry a coherent "
            "omega_{z,z'} action invisible to diagonal detectors"
        ),
        arity3_stress_formula=(
            "arity 3 tests whether the two YBE paths agree visibly but differ "
            "by hidden fibre transport"
        ),
        cases=cases,
    )


def ybe_guitar_decoder_boundary_audit() -> YBEGuitarDecoderBoundaryAudit:
    """Record the guitar-map boundary of the finite-state decoder route.

    The one-sided nondegenerate guitar theorem solves the decoder equations
    with a finite group of suffix actions.  Degeneracy replaces that group by
    a finite transformation monoid, where inverse branches are not canonical
    and become the actual finite cocycle obligation.
    """

    cases = (
        YBEGuitarDecoderBoundaryCase(
            key="right_nondegenerate_guitar_theorem",
            role="positive_known_theorem",
            statement=(
                "if every right action R_y(x)=rho_y(x) is bijective, the "
                "right-guitar maps J_n are triangular bijections in every "
                "arity"
            ),
            consequence=(
                "the relevant nondegenerate branch is not a search result; it "
                "is closed by the standard guitar-map conjugacy theorem"
            ),
        ),
        YBEGuitarDecoderBoundaryCase(
            key="derived_rack_domination",
            role="positive_domination",
            statement=(
                "the derived operation a < b = R_a(lambda_{R_b^-1(a)}(b)) "
                "is a finite rack operation and its braid action is conjugate "
                "to the YBE action"
            ),
            consequence=(
                "taking Y to be this derived rack gives kernel equality, hence "
                "finite rack domination, for every braid arity"
            ),
        ),
        YBEGuitarDecoderBoundaryCase(
            key="finite_state_decoder_realization",
            role="decoder_model",
            statement=(
                "the inverse guitar map is a finite-state decoder with "
                "Q=G_rho, d(q,a)=q^-1(a), and tau(q,a)=q R_{q^-1(a)}"
            ),
            consequence=(
                "the finite-state rack-cover equations are solved exactly in "
                "the one-sided nondegenerate case"
            ),
        ),
        YBEGuitarDecoderBoundaryCase(
            key="degenerate_j2_failure",
            role="first_failure",
            statement=(
                "if some R_y is not bijective, then J_2(x,y)=(R_y(x),y) is "
                "not bijective and the derived formula needs a noncanonical "
                "preimage R_b^-1(a)"
            ),
            consequence=(
                "the degenerate obstruction begins at inverse-branch choice, "
                "not at high arity or whole-image exponent growth"
            ),
        ),
        YBEGuitarDecoderBoundaryCase(
            key="monoid_inverse_branch_gate",
            role="finite_repair_gate",
            statement=(
                "the transformation monoid M_rho is finite, but a decoder "
                "using Q=M_rho needs choices d(q,a) in q^-1(a) and updates "
                "tau(q,a)=q R_{d(q,a)}"
            ),
            consequence=(
                "finite memory is available, but braid compatibility becomes "
                "a finite inverse-branch cocycle system"
            ),
        ),
        YBEGuitarDecoderBoundaryCase(
            key="deterministic_decoder_obligation",
            role="remaining_obligation",
            statement=(
                "relation-valued or nondeterministic inverse branches do not "
                "give Sawin kernel inclusion unless they determinize to finite "
                "labels satisfying rack self-distributivity and decoder equations"
            ),
            consequence=(
                "the unresolved degenerate regime is exactly the search for "
                "coherent deterministic finite decoder labels"
            ),
        ),
    )
    return YBEGuitarDecoderBoundaryAudit(
        right_guitar_hypothesis_recorded=True,
        derived_rack_operation_recorded=True,
        all_arity_kernel_equality_recorded=True,
        finite_state_decoder_realization_recorded=True,
        degenerate_j2_failure_recorded=True,
        monoid_inverse_branch_gate_recorded=True,
        no_automatic_unbounded_memory_obstruction_recorded=True,
        deterministic_decoder_obligation_recorded=True,
        right_guitar_formula=(
            "R_y(x)=rho_y(x); if every R_y is bijective, "
            "J_n(x_1,...,x_n)=(R_{x_n}...R_{x_2}(x_1),...,x_n)"
        ),
        derived_rack_formula=(
            "a < b = R_a(lambda_{R_b^-1(a)}(b))"
        ),
        kernel_equality_formula=(
            "J_n rho_X,n(beta)=rho_Y,n(beta) J_n, hence "
            "ker rho_Y,n = ker rho_X,n for every n"
        ),
        decoder_state_formula=(
            "Q=G_rho, d(q,a)=q^-1(a), tau(q,a)=q R_{q^-1(a)}"
        ),
        degenerate_j2_failure_formula=(
            "J_2(x,y)=(R_y(x),y), so nonbijective R_y makes J_2 nonbijective"
        ),
        monoid_gate_formula=(
            "Q=M_rho requires d(q,a) in q^-1(a), "
            "tau(q,a)=q R_{d(q,a)}, and the finite-state cocycle equations"
        ),
        cases=cases,
    )


def ybe_inverse_branch_determinization_audit() -> YBEInverseBranchDeterminizationAudit:
    """Record the obstruction to total monoid-guitar determinization.

    The degenerate guitar repair might try to replace the suffix group
    G_rho by the finite transformation monoid M_rho and then determinize
    inverse branches by powersets, partial sections, or Green data.  A total
    decoder of that form cannot cover a genuinely right-degenerate solution:
    the local decoder equation together with all-arity surjectivity forces
    every relevant right action to be surjective, hence bijective for finite X.
    """

    cases = (
        YBEInverseBranchDeterminizationCase(
            key="total_decoder_surjectivity",
            role="hypothesis",
            statement=(
                "a total finite-state rack decoder must give surjective maps "
                "Phi_n:Y^n -> X^n for all n, so every one-step reachable "
                "decoder state must still realize every next X-symbol"
            ),
            consequence=(
                "the local two-symbol equations may be tested at arbitrary "
                "right outputs, not only at outputs lying in an image of a "
                "rank-dropping suffix transformation"
            ),
        ),
        YBEInverseBranchDeterminizationCase(
            key="local_equation_forces_side_surjectivity",
            role="negative_total_decoder",
            statement=(
                "the decoder equation for the copied rack strand forces every "
                "target value rho_y(x) to appear as a decoded value with fixed "
                "old rack symbol a once x=d(q,a) and y is the decoded neighbor"
            ),
            consequence=(
                "for the right-guitar convention, total deterministic decoding "
                "forces R_y(X)=X for every y; since X is finite, all R_y are "
                "bijections"
            ),
        ),
        YBEInverseBranchDeterminizationCase(
            key="rank_drop_empty_inverse_fibre",
            role="first_failure",
            statement=(
                "if some R_y is not surjective, a monoid state q followed by "
                "R_y has an output a with empty inverse fibre under q R_y"
            ),
            consequence=(
                "the branch value d(q R_y,a) cannot be total; the obstruction "
                "appears before any high-arity rack cocycle"
            ),
        ),
        YBEInverseBranchDeterminizationCase(
            key="powerset_relation_not_rack",
            role="failed_determinization",
            statement=(
                "direct or inverse image operations on subsets are not "
                "bijective when a finite transformation is nonbijective, and "
                "saturated subsets lose singleton separation"
            ),
            consequence=(
                "powerset or relation-valued guitars preserve possible "
                "branches but do not produce a rack action proving pointwise "
                "kernel inclusion on X^n"
            ),
        ),
        YBEInverseBranchDeterminizationCase(
            key="green_schutzenberger_no_rank_repair",
            role="semigroup_warning",
            statement=(
                "Green R-class and Schutzenberger coordinates describe the "
                "regular part of M_rho but do not undo a transition that drops "
                "image rank from the identity state"
            ),
            consequence=(
                "finite semigroup labels are useful diagnostics, but a "
                "rank-dropping generator still creates empty branch fibres for "
                "a total decoder"
            ),
        ),
        YBEInverseBranchDeterminizationCase(
            key="restricted_language_branch_cocycle",
            role="remaining_restricted_problem",
            statement=(
                "if one restricts to a proper invariant language where empty "
                "fibres are avoided, the selected partial inverse branches "
                "must satisfy closure equations and an arity-3 rack "
                "self-distributivity cocycle"
            ),
            consequence=(
                "the obstruction can move from arity 2 to arity 3 only after "
                "abandoning total decoding on all of Y^n"
            ),
        ),
        YBEInverseBranchDeterminizationCase(
            key="nondeterministic_kernel_gap",
            role="kernel_gap",
            statement=(
                "a nondeterministic relation-valued decoder can record that "
                "some inverse branch exists, but it does not give a functional "
                "braid action on a finite rack alphabet"
            ),
            consequence=(
                "Sawin kernel inclusion requires deterministic finite labels "
                "or an equivalent marked quotient, not merely preservation of "
                "a relation of possible decodings"
            ),
        ),
    )
    return YBEInverseBranchDeterminizationAudit(
        total_decoder_surjectivity_recorded=True,
        local_surjectivity_equation_recorded=True,
        finite_side_bijection_forced=True,
        total_monoid_guitar_negative_recorded=True,
        powerset_relation_failure_recorded=True,
        green_rank_drop_failure_recorded=True,
        restricted_language_cocycle_recorded=True,
        nondeterministic_kernel_gap_recorded=True,
        initial_state_formula=(
            "Phi_1(a)=d(q0,a) is surjective, and Phi_2 is surjective through "
            "every one-step reachable state tau(q0,a)"
        ),
        local_surjectivity_equation_formula=(
            "d(tau(q,a > b),a)=rho_{d(tau(q,a),b)}(d(q,a))"
        ),
        forced_bijection_formula=(
            "total decoding implies R_y(X)=X for every y; finite X then "
            "implies every R_y is bijective"
        ),
        monoid_rank_formula=(
            "rank(q R_x) < rank(q) gives outputs a with (q R_x)^-1(a)=empty"
        ),
        branch_cocycle_formula=(
            "on any restricted language, branch selectors must satisfy "
            "closure plus the arity-3 rack self-distributivity cocycle"
        ),
        cases=cases,
    )


def _delete_tuple_index(tuple_value: Sequence[object], delete_index: int) -> Tuple[object, ...]:
    return tuple(
        value
        for index, value in enumerate(tuple_value)
        if index != delete_index
    )


def _delete_tuple_source_positions(
    tuple_value: Sequence[object],
    source_positions: Sequence[int],
    deletion_order: Sequence[int],
) -> Tuple[object, ...]:
    remaining_positions = list(source_positions)
    out = tuple(tuple_value)
    for delete_position in deletion_order:
        delete_index = remaining_positions.index(delete_position)
        out = _delete_tuple_index(out, delete_index)
        del remaining_positions[delete_index]
    return out


def _target_point_pushing_generator_after_forgetting(
    source_generator_index: int,
    forget_stationary_index: int,
) -> int | None:
    if source_generator_index == forget_stationary_index:
        return None
    if source_generator_index < forget_stationary_index:
        return source_generator_index
    return source_generator_index - 1


def _target_point_pushing_generator_after_forgetting_many(
    source_generator_index: int,
    forget_stationary_indices: Sequence[int],
) -> int | None:
    forgets = tuple(sorted(forget_stationary_indices))
    if source_generator_index in forgets:
        return None
    return source_generator_index - sum(
        1 for forget_stationary_index in forgets
        if forget_stationary_index < source_generator_index
    )


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


def _prefix_deletion_square_restriction_row(
    solution: FiniteBraidedSet,
    *,
    source_generator_index: int,
    forget_stationary_indices: Tuple[int, int],
) -> PrefixDeletionSquareRestrictionRow:
    from .braid_laws import pure_braid_generator

    source_point_pushing_arity = 5
    source_braid_index = source_point_pushing_arity + 1
    target_point_pushing_arity = 3
    target_braid_index = target_point_pushing_arity + 1
    source_positions = tuple(range(1, source_braid_index + 1))
    forgets = tuple(sorted(forget_stationary_indices))
    if len(forgets) != 2 or forgets != forget_stationary_indices:
        raise ValueError("forget_stationary_indices must be increasing")
    if forgets[0] < 1 or forgets[-1] > source_point_pushing_arity:
        raise ValueError("can only forget stationary strands")

    source_braid_word = pure_braid_generator(
        source_generator_index,
        source_braid_index,
    )
    target_generator_index = _target_point_pushing_generator_after_forgetting_many(
        source_generator_index,
        forgets,
    )
    target_braid_word: BraidWord = (
        tuple()
        if target_generator_index is None
        else pure_braid_generator(target_generator_index, target_braid_index)
    )
    forward_order = forgets
    reverse_order = tuple(reversed(forgets))
    mismatch_count = 0
    first_witness_input = None
    first_deleted_after_source = None
    first_expected_target = None
    deletion_orders_commute = True
    for tuple_value in product(solution.elements, repeat=source_braid_index):
        source_image = solution.braid_action(source_braid_word, tuple_value)
        deleted_after_source = _delete_tuple_source_positions(
            source_image,
            source_positions,
            reverse_order,
        )
        alternate_deleted_after_source = _delete_tuple_source_positions(
            source_image,
            source_positions,
            forward_order,
        )
        if alternate_deleted_after_source != deleted_after_source:
            deletion_orders_commute = False

        deleted_input = _delete_tuple_source_positions(
            tuple_value,
            source_positions,
            reverse_order,
        )
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
    return PrefixDeletionSquareRestrictionRow(
        source_point_pushing_arity=source_point_pushing_arity,
        source_braid_index=source_braid_index,
        target_point_pushing_arity=target_point_pushing_arity,
        target_braid_index=target_braid_index,
        forget_stationary_indices=forgets,
        source_generator_index=source_generator_index,
        target_generator_index=target_generator_index,
        source_braid_word=source_braid_word,
        target_braid_word=target_braid_word,
        tuple_count=len(solution.elements) ** source_braid_index,
        expected_identity_after_forgetting=target_generator_index is None,
        deletion_orders_commute=deletion_orders_commute,
        matches_marked_double_restriction=mismatch_count == 0,
        mismatch_count=mismatch_count,
        first_witness_input=first_witness_input,
        first_deleted_after_source=first_deleted_after_source,
        first_expected_target=first_expected_target,
    )


def prefix_deletion_square_restriction_audit(
    solution: FiniteBraidedSet,
) -> PrefixDeletionSquareRestrictionAudit:
    """Compare marked `Q_X(5)` generators after two stationary deletions."""

    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    rows = tuple(
        _prefix_deletion_square_restriction_row(
            solution,
            source_generator_index=source_generator_index,
            forget_stationary_indices=forget_stationary_indices,
        )
        for forget_stationary_indices in combinations(range(1, 6), 2)
        for source_generator_index in range(1, 6)
    )
    return PrefixDeletionSquareRestrictionAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        source_point_pushing_arity=5,
        target_point_pushing_arity=3,
        rows=rows,
        records_first_deletion_square_surface=True,
    )


def _prefix_deletion_cube_restriction_row(
    solution: FiniteBraidedSet,
    *,
    source_generator_index: int,
    forget_stationary_indices: Tuple[int, int, int],
) -> PrefixDeletionCubeRestrictionRow:
    from .braid_laws import pure_braid_generator

    source_point_pushing_arity = 5
    source_braid_index = source_point_pushing_arity + 1
    target_point_pushing_arity = 2
    target_braid_index = target_point_pushing_arity + 1
    source_positions = tuple(range(1, source_braid_index + 1))
    forgets = tuple(sorted(forget_stationary_indices))
    if len(forgets) != 3 or forgets != forget_stationary_indices:
        raise ValueError("forget_stationary_indices must be increasing")
    if forgets[0] < 1 or forgets[-1] > source_point_pushing_arity:
        raise ValueError("can only forget stationary strands")

    source_braid_word = pure_braid_generator(
        source_generator_index,
        source_braid_index,
    )
    target_generator_index = _target_point_pushing_generator_after_forgetting_many(
        source_generator_index,
        forgets,
    )
    target_braid_word: BraidWord = (
        tuple()
        if target_generator_index is None
        else pure_braid_generator(target_generator_index, target_braid_index)
    )
    deletion_orders = tuple(permutations(forgets))
    canonical_order = tuple(reversed(forgets))
    mismatch_count = 0
    first_witness_input = None
    first_deleted_after_source = None
    first_expected_target = None
    deletion_orders_commute = True
    for tuple_value in product(solution.elements, repeat=source_braid_index):
        source_image = solution.braid_action(source_braid_word, tuple_value)
        deleted_after_source = _delete_tuple_source_positions(
            source_image,
            source_positions,
            canonical_order,
        )
        for deletion_order in deletion_orders:
            alternate_deleted_after_source = _delete_tuple_source_positions(
                source_image,
                source_positions,
                deletion_order,
            )
            if alternate_deleted_after_source != deleted_after_source:
                deletion_orders_commute = False

        deleted_input = _delete_tuple_source_positions(
            tuple_value,
            source_positions,
            canonical_order,
        )
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
    return PrefixDeletionCubeRestrictionRow(
        source_point_pushing_arity=source_point_pushing_arity,
        source_braid_index=source_braid_index,
        target_point_pushing_arity=target_point_pushing_arity,
        target_braid_index=target_braid_index,
        forget_stationary_indices=forgets,
        source_generator_index=source_generator_index,
        target_generator_index=target_generator_index,
        source_braid_word=source_braid_word,
        target_braid_word=target_braid_word,
        tuple_count=len(solution.elements) ** source_braid_index,
        deletion_order_count=len(deletion_orders),
        expected_identity_after_forgetting=target_generator_index is None,
        deletion_orders_commute=deletion_orders_commute,
        matches_marked_triple_restriction=mismatch_count == 0,
        mismatch_count=mismatch_count,
        first_witness_input=first_witness_input,
        first_deleted_after_source=first_deleted_after_source,
        first_expected_target=first_expected_target,
    )


def prefix_deletion_cube_restriction_audit(
    solution: FiniteBraidedSet,
) -> PrefixDeletionCubeRestrictionAudit:
    """Compare marked `Q_X(5)` generators after three stationary deletions."""

    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    rows = tuple(
        _prefix_deletion_cube_restriction_row(
            solution,
            source_generator_index=source_generator_index,
            forget_stationary_indices=forget_stationary_indices,
        )
        for forget_stationary_indices in combinations(range(1, 6), 3)
        for source_generator_index in range(1, 6)
    )
    return PrefixDeletionCubeRestrictionAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        source_point_pushing_arity=5,
        target_point_pushing_arity=2,
        rows=rows,
        records_first_deletion_cube_surface=True,
    )


def _prefix_vertical_defect_transform_row(
    solution: FiniteBraidedSet,
    *,
    deletion_level: int,
    source_point_pushing_arity: int,
    forget_stationary_indices: Tuple[int, ...],
    source_generator_index: int,
) -> PrefixVerticalDefectTransformRow:
    from .braid_laws import pure_braid_generator

    source_braid_index = source_point_pushing_arity + 1
    target_point_pushing_arity = source_point_pushing_arity - deletion_level
    target_braid_index = target_point_pushing_arity + 1
    source_positions = tuple(range(1, source_braid_index + 1))
    forgets = tuple(sorted(forget_stationary_indices))
    if len(forgets) != deletion_level or forgets != forget_stationary_indices:
        raise ValueError("forget_stationary_indices must be increasing")
    if source_generator_index not in forgets:
        raise ValueError("only deleted-generator defects are vertical rows")
    if target_point_pushing_arity < 1:
        raise ValueError("target point-pushing arity must be positive")

    source_braid_word = pure_braid_generator(
        source_generator_index,
        source_braid_index,
    )
    deletion_order = tuple(reversed(forgets))
    outputs_by_deleted_tuple: dict[Tuple[object, ...], set[Tuple[object, ...]]] = {}
    first_witness_input = None
    first_deleted_input = None
    first_deleted_after_source = None
    for tuple_value in product(solution.elements, repeat=source_braid_index):
        deleted_input = _delete_tuple_source_positions(
            tuple_value,
            source_positions,
            deletion_order,
        )
        deleted_after_source = _delete_tuple_source_positions(
            solution.braid_action(source_braid_word, tuple_value),
            source_positions,
            deletion_order,
        )
        outputs_by_deleted_tuple.setdefault(deleted_input, set()).add(
            deleted_after_source
        )
        if first_witness_input is None and deleted_after_source != deleted_input:
            first_witness_input = tuple(tuple_value)
            first_deleted_input = deleted_input
            first_deleted_after_source = deleted_after_source

    ambiguous_count = sum(
        1
        for outputs in outputs_by_deleted_tuple.values()
        if len(outputs) > 1
    )
    max_outputs = max(
        (len(outputs) for outputs in outputs_by_deleted_tuple.values()),
        default=0,
    )
    well_defined = ambiguous_count == 0
    target_tuples = tuple(product(solution.elements, repeat=target_braid_index))
    target_index = {tuple_value: index for index, tuple_value in enumerate(target_tuples)}
    defect_permutation = None
    defect_is_permutation = False
    defect_order = None
    identity_defect = None
    if well_defined and len(outputs_by_deleted_tuple) == len(target_tuples):
        image_tuples = tuple(
            next(iter(outputs_by_deleted_tuple[tuple_value]))
            for tuple_value in target_tuples
        )
        if all(tuple_value in target_index for tuple_value in image_tuples):
            image_indices = tuple(target_index[tuple_value] for tuple_value in image_tuples)
            defect_is_permutation = set(image_indices) == set(range(len(target_tuples)))
            if defect_is_permutation:
                defect_permutation = image_indices
                defect_order = permutation_order(defect_permutation)
                identity_defect = defect_permutation == identity_permutation(
                    len(target_tuples)
                )

    return PrefixVerticalDefectTransformRow(
        deletion_level=deletion_level,
        source_point_pushing_arity=source_point_pushing_arity,
        source_braid_index=source_braid_index,
        target_point_pushing_arity=target_point_pushing_arity,
        target_braid_index=target_braid_index,
        forget_stationary_indices=forgets,
        source_generator_index=source_generator_index,
        source_braid_word=source_braid_word,
        source_tuple_count=len(solution.elements) ** source_braid_index,
        target_tuple_count=len(target_tuples),
        well_defined_on_deleted_tuple=well_defined,
        ambiguous_deleted_tuple_count=ambiguous_count,
        max_outputs_per_deleted_tuple=max_outputs,
        defect_is_permutation=defect_is_permutation,
        defect_permutation=defect_permutation,
        defect_order=defect_order,
        identity_defect=identity_defect,
        first_witness_input=first_witness_input,
        first_deleted_input=first_deleted_input,
        first_deleted_after_source=first_deleted_after_source,
    )


def prefix_vertical_defect_transform_audit(
    solution: FiniteBraidedSet,
) -> PrefixVerticalDefectTransformAudit:
    """Extract target-tuple transformations from diagonal deletion defects."""

    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    row_specs: list[tuple[int, int, Tuple[int, ...], int]] = []
    for forgets in combinations(range(1, 5), 1):
        for source_generator_index in forgets:
            row_specs.append((1, 4, forgets, source_generator_index))
    for forgets in combinations(range(1, 6), 2):
        for source_generator_index in forgets:
            row_specs.append((2, 5, forgets, source_generator_index))
    for forgets in combinations(range(1, 6), 3):
        for source_generator_index in forgets:
            row_specs.append((3, 5, forgets, source_generator_index))
    rows = tuple(
        _prefix_vertical_defect_transform_row(
            solution,
            deletion_level=deletion_level,
            source_point_pushing_arity=source_point_pushing_arity,
            forget_stationary_indices=forget_stationary_indices,
            source_generator_index=source_generator_index,
        )
        for (
            deletion_level,
            source_point_pushing_arity,
            forget_stationary_indices,
            source_generator_index,
        ) in row_specs
    )
    return PrefixVerticalDefectTransformAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        rows=rows,
        records_vertical_defect_transform_extraction=True,
    )


def _delete_additional_target_stationary_index(
    tuple_value: Sequence[object],
    *,
    source_braid_index: int,
    already_forgetting: Sequence[int],
    extra_stationary_index: int,
) -> Tuple[object, ...]:
    remaining_positions = tuple(
        position
        for position in range(1, source_braid_index + 1)
        if position not in already_forgetting
    )
    return _delete_tuple_source_positions(
        tuple_value,
        remaining_positions,
        (extra_stationary_index,),
    )


def _prefix_vertical_defect_transport_row(
    solution: FiniteBraidedSet,
    *,
    source_point_pushing_arity: int,
    from_forget_stationary_indices: Tuple[int, ...],
    extra_stationary_index: int,
    source_generator_index: int,
) -> PrefixVerticalDefectTransportRow:
    source_braid_index = source_point_pushing_arity + 1
    from_forgets = tuple(sorted(from_forget_stationary_indices))
    if from_forgets != from_forget_stationary_indices:
        raise ValueError("from_forget_stationary_indices must be increasing")
    if source_generator_index not in from_forgets:
        raise ValueError("source generator must already be vertical")
    if extra_stationary_index in from_forgets:
        raise ValueError("extra deletion must be new")
    if extra_stationary_index < 1 or extra_stationary_index > source_point_pushing_arity:
        raise ValueError("can only delete stationary strands")

    to_forgets = tuple(sorted((*from_forgets, extra_stationary_index)))
    from_row = _prefix_vertical_defect_transform_row(
        solution,
        deletion_level=len(from_forgets),
        source_point_pushing_arity=source_point_pushing_arity,
        forget_stationary_indices=from_forgets,
        source_generator_index=source_generator_index,
    )
    to_row = _prefix_vertical_defect_transform_row(
        solution,
        deletion_level=len(to_forgets),
        source_point_pushing_arity=source_point_pushing_arity,
        forget_stationary_indices=to_forgets,
        source_generator_index=source_generator_index,
    )

    from_target_tuples = tuple(
        product(solution.elements, repeat=from_row.target_braid_index)
    )
    to_target_tuples = tuple(
        product(solution.elements, repeat=to_row.target_braid_index)
    )
    to_target_index = {
        tuple_value: index
        for index, tuple_value in enumerate(to_target_tuples)
    }
    additional_face_images = {
        _delete_additional_target_stationary_index(
            tuple_value,
            source_braid_index=source_braid_index,
            already_forgetting=from_forgets,
            extra_stationary_index=extra_stationary_index,
        )
        for tuple_value in from_target_tuples
    }
    additional_face_surjective = additional_face_images == set(to_target_tuples)

    mismatch_count = 0
    first_witness_target_input = None
    first_left_after_defect_then_delete = None
    first_right_after_delete_then_defect = None
    if (
        from_row.defect_permutation is not None
        and to_row.defect_permutation is not None
    ):
        for from_index, tuple_value in enumerate(from_target_tuples):
            left_after_from_defect = from_target_tuples[
                from_row.defect_permutation[from_index]
            ]
            left = _delete_additional_target_stationary_index(
                left_after_from_defect,
                source_braid_index=source_braid_index,
                already_forgetting=from_forgets,
                extra_stationary_index=extra_stationary_index,
            )
            deleted_input = _delete_additional_target_stationary_index(
                tuple_value,
                source_braid_index=source_braid_index,
                already_forgetting=from_forgets,
                extra_stationary_index=extra_stationary_index,
            )
            right = to_target_tuples[
                to_row.defect_permutation[to_target_index[deleted_input]]
            ]
            if left == right:
                continue
            mismatch_count += 1
            if first_witness_target_input is None:
                first_witness_target_input = tuple(tuple_value)
                first_left_after_defect_then_delete = left
                first_right_after_delete_then_defect = right
    else:
        mismatch_count = len(from_target_tuples)
        if from_target_tuples:
            first_witness_target_input = tuple(from_target_tuples[0])

    return PrefixVerticalDefectTransportRow(
        source_point_pushing_arity=source_point_pushing_arity,
        source_braid_index=source_braid_index,
        from_deletion_level=len(from_forgets),
        to_deletion_level=len(to_forgets),
        from_forget_stationary_indices=from_forgets,
        extra_stationary_index=extra_stationary_index,
        to_forget_stationary_indices=to_forgets,
        source_generator_index=source_generator_index,
        from_target_braid_index=from_row.target_braid_index,
        to_target_braid_index=to_row.target_braid_index,
        from_target_tuple_count=len(from_target_tuples),
        to_target_tuple_count=len(to_target_tuples),
        additional_face_surjective=additional_face_surjective,
        from_defect_is_permutation=from_row.defect_is_permutation,
        to_defect_is_permutation=to_row.defect_is_permutation,
        from_defect_order=from_row.defect_order,
        to_defect_order=to_row.defect_order,
        from_identity_defect=from_row.identity_defect,
        to_identity_defect=to_row.identity_defect,
        transport_commutes=mismatch_count == 0,
        mismatch_count=mismatch_count,
        first_witness_target_input=first_witness_target_input,
        first_left_after_defect_then_delete=first_left_after_defect_then_delete,
        first_right_after_delete_then_defect=first_right_after_delete_then_defect,
    )


def prefix_vertical_defect_transport_audit(
    solution: FiniteBraidedSet,
) -> PrefixVerticalDefectTransportAudit:
    """Check face transport for already-vertical deletion defects."""

    source_point_pushing_arity = 5
    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    row_specs: list[tuple[Tuple[int, ...], int, int]] = []
    stationary_indices = range(1, source_point_pushing_arity + 1)
    for deletion_level in (1, 2):
        for from_forgets in combinations(stationary_indices, deletion_level):
            for source_generator_index in from_forgets:
                for extra_stationary_index in stationary_indices:
                    if extra_stationary_index not in from_forgets:
                        row_specs.append(
                            (
                                from_forgets,
                                extra_stationary_index,
                                source_generator_index,
                            )
                        )
    rows = tuple(
        _prefix_vertical_defect_transport_row(
            solution,
            source_point_pushing_arity=source_point_pushing_arity,
            from_forget_stationary_indices=from_forgets,
            extra_stationary_index=extra_stationary_index,
            source_generator_index=source_generator_index,
        )
        for (
            from_forgets,
            extra_stationary_index,
            source_generator_index,
        ) in row_specs
    )
    return PrefixVerticalDefectTransportAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        source_point_pushing_arity=source_point_pushing_arity,
        rows=rows,
        records_first_vertical_defect_face_transport=True,
    )


def _permutation_commutator(first: Permutation, second: Permutation) -> Permutation:
    """Return first second first^-1 second^-1 using left-after-right composition."""

    return compose_permutations(
        first,
        compose_permutations(
            second,
            compose_permutations(
                invert_permutation(first),
                invert_permutation(second),
            ),
        ),
    )


def _prefix_vertical_peiffer_square_row(
    solution: FiniteBraidedSet,
    *,
    source_point_pushing_arity: int,
    forget_stationary_indices: Tuple[int, int],
) -> PrefixVerticalPeifferSquareRow:
    source_braid_index = source_point_pushing_arity + 1
    forgets = tuple(sorted(forget_stationary_indices))
    if len(forgets) != 2 or forgets != forget_stationary_indices:
        raise ValueError("forget_stationary_indices must be increasing")
    if forgets[0] < 1 or forgets[-1] > source_point_pushing_arity:
        raise ValueError("can only delete stationary strands")

    first_index, second_index = forgets
    first_defect = _prefix_vertical_defect_transform_row(
        solution,
        deletion_level=2,
        source_point_pushing_arity=source_point_pushing_arity,
        forget_stationary_indices=forgets,
        source_generator_index=first_index,
    )
    second_defect = _prefix_vertical_defect_transform_row(
        solution,
        deletion_level=2,
        source_point_pushing_arity=source_point_pushing_arity,
        forget_stationary_indices=forgets,
        source_generator_index=second_index,
    )
    first_transport = _prefix_vertical_defect_transport_row(
        solution,
        source_point_pushing_arity=source_point_pushing_arity,
        from_forget_stationary_indices=(first_index,),
        extra_stationary_index=second_index,
        source_generator_index=first_index,
    )
    second_transport = _prefix_vertical_defect_transport_row(
        solution,
        source_point_pushing_arity=source_point_pushing_arity,
        from_forget_stationary_indices=(second_index,),
        extra_stationary_index=first_index,
        source_generator_index=second_index,
    )

    target_tuples = tuple(
        product(solution.elements, repeat=first_defect.target_braid_index)
    )
    peiffer_commutator = None
    peiffer_order = None
    peiffer_is_identity = None
    moved_count = 0
    first_witness_target_input = None
    first_witness_after_commutator = None
    if (
        first_defect.defect_permutation is not None
        and second_defect.defect_permutation is not None
    ):
        peiffer_commutator = _permutation_commutator(
            first_defect.defect_permutation,
            second_defect.defect_permutation,
        )
        peiffer_order = permutation_order(peiffer_commutator)
        identity = identity_permutation(len(peiffer_commutator))
        peiffer_is_identity = peiffer_commutator == identity
        for index, image_index in enumerate(peiffer_commutator):
            if index == image_index:
                continue
            moved_count += 1
            if first_witness_target_input is None:
                first_witness_target_input = tuple(target_tuples[index])
                first_witness_after_commutator = tuple(target_tuples[image_index])

    return PrefixVerticalPeifferSquareRow(
        source_point_pushing_arity=source_point_pushing_arity,
        source_braid_index=source_braid_index,
        forget_stationary_indices=forgets,
        first_source_generator_index=first_index,
        second_source_generator_index=second_index,
        target_braid_index=first_defect.target_braid_index,
        target_tuple_count=len(target_tuples),
        first_defect_is_permutation=first_defect.defect_is_permutation,
        second_defect_is_permutation=second_defect.defect_is_permutation,
        first_defect_order=first_defect.defect_order,
        second_defect_order=second_defect.defect_order,
        first_single_transport_commutes=first_transport.transport_commutes,
        second_single_transport_commutes=second_transport.transport_commutes,
        peiffer_commutator_permutation=peiffer_commutator,
        peiffer_commutator_order=peiffer_order,
        peiffer_commutator_is_identity=peiffer_is_identity,
        peiffer_moved_tuple_count=moved_count,
        first_witness_target_input=first_witness_target_input,
        first_witness_after_commutator=first_witness_after_commutator,
    )


def prefix_vertical_peiffer_square_audit(
    solution: FiniteBraidedSet,
) -> PrefixVerticalPeifferSquareAudit:
    """Compute first Peiffer commutators for diagonal deletion defects."""

    source_point_pushing_arity = 5
    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    rows = tuple(
        _prefix_vertical_peiffer_square_row(
            solution,
            source_point_pushing_arity=source_point_pushing_arity,
            forget_stationary_indices=forget_stationary_indices,
        )
        for forget_stationary_indices in combinations(
            range(1, source_point_pushing_arity + 1),
            2,
        )
    )
    return PrefixVerticalPeifferSquareAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        source_point_pushing_arity=source_point_pushing_arity,
        rows=rows,
        records_first_vertical_peiffer_square_boundary=True,
    )


def _vertical_peiffer_boundary_data(
    solution: FiniteBraidedSet,
    *,
    source_point_pushing_arity: int,
    forget_stationary_indices: Tuple[int, ...],
    first_source_generator_index: int,
    second_source_generator_index: int,
) -> tuple[
    PrefixVerticalDefectTransformRow,
    PrefixVerticalDefectTransformRow,
    Tuple[Tuple[object, ...], ...],
    Permutation | None,
    int | None,
    bool | None,
    int,
]:
    first_defect = _prefix_vertical_defect_transform_row(
        solution,
        deletion_level=len(forget_stationary_indices),
        source_point_pushing_arity=source_point_pushing_arity,
        forget_stationary_indices=forget_stationary_indices,
        source_generator_index=first_source_generator_index,
    )
    second_defect = _prefix_vertical_defect_transform_row(
        solution,
        deletion_level=len(forget_stationary_indices),
        source_point_pushing_arity=source_point_pushing_arity,
        forget_stationary_indices=forget_stationary_indices,
        source_generator_index=second_source_generator_index,
    )
    target_tuples = tuple(
        product(solution.elements, repeat=first_defect.target_braid_index)
    )
    peiffer_commutator = None
    peiffer_order = None
    peiffer_identity = None
    moved_count = 0
    if (
        first_defect.defect_permutation is not None
        and second_defect.defect_permutation is not None
    ):
        peiffer_commutator = _permutation_commutator(
            first_defect.defect_permutation,
            second_defect.defect_permutation,
        )
        peiffer_order = permutation_order(peiffer_commutator)
        peiffer_identity = peiffer_commutator == identity_permutation(
            len(peiffer_commutator)
        )
        moved_count = sum(
            1
            for index, image_index in enumerate(peiffer_commutator)
            if index != image_index
        )
    return (
        first_defect,
        second_defect,
        target_tuples,
        peiffer_commutator,
        peiffer_order,
        peiffer_identity,
        moved_count,
    )


def _prefix_vertical_peiffer_cube_transport_row(
    solution: FiniteBraidedSet,
    *,
    source_point_pushing_arity: int,
    triple_forget_stationary_indices: Tuple[int, int, int],
    pair_forget_stationary_indices: Tuple[int, int],
) -> PrefixVerticalPeifferCubeTransportRow:
    source_braid_index = source_point_pushing_arity + 1
    triple_forgets = tuple(sorted(triple_forget_stationary_indices))
    pair_forgets = tuple(sorted(pair_forget_stationary_indices))
    if (
        len(triple_forgets) != 3
        or triple_forgets != triple_forget_stationary_indices
    ):
        raise ValueError("triple_forget_stationary_indices must be increasing")
    if len(pair_forgets) != 2 or pair_forgets != pair_forget_stationary_indices:
        raise ValueError("pair_forget_stationary_indices must be increasing")
    if not set(pair_forgets).issubset(triple_forgets):
        raise ValueError("pair face must be contained in triple face")
    if triple_forgets[0] < 1 or triple_forgets[-1] > source_point_pushing_arity:
        raise ValueError("can only delete stationary strands")

    extra_stationary_index = next(
        index
        for index in triple_forgets
        if index not in pair_forgets
    )
    first_index, second_index = pair_forgets
    (
        pair_first_defect,
        pair_second_defect,
        pair_target_tuples,
        pair_peiffer,
        pair_peiffer_order,
        pair_peiffer_identity,
        pair_moved_count,
    ) = _vertical_peiffer_boundary_data(
        solution,
        source_point_pushing_arity=source_point_pushing_arity,
        forget_stationary_indices=pair_forgets,
        first_source_generator_index=first_index,
        second_source_generator_index=second_index,
    )
    (
        triple_first_defect,
        triple_second_defect,
        triple_target_tuples,
        triple_peiffer,
        triple_peiffer_order,
        triple_peiffer_identity,
        triple_moved_count,
    ) = _vertical_peiffer_boundary_data(
        solution,
        source_point_pushing_arity=source_point_pushing_arity,
        forget_stationary_indices=triple_forgets,
        first_source_generator_index=first_index,
        second_source_generator_index=second_index,
    )
    triple_target_index = {
        tuple_value: index
        for index, tuple_value in enumerate(triple_target_tuples)
    }
    additional_face_images = {
        _delete_additional_target_stationary_index(
            tuple_value,
            source_braid_index=source_braid_index,
            already_forgetting=pair_forgets,
            extra_stationary_index=extra_stationary_index,
        )
        for tuple_value in pair_target_tuples
    }
    additional_face_surjective = additional_face_images == set(triple_target_tuples)

    mismatch_count = 0
    first_witness_pair_target_input = None
    first_left_after_pair_peiffer_then_delete = None
    first_right_after_delete_then_triple_peiffer = None
    if pair_peiffer is not None and triple_peiffer is not None:
        for pair_index, tuple_value in enumerate(pair_target_tuples):
            left_after_pair_peiffer = pair_target_tuples[pair_peiffer[pair_index]]
            left = _delete_additional_target_stationary_index(
                left_after_pair_peiffer,
                source_braid_index=source_braid_index,
                already_forgetting=pair_forgets,
                extra_stationary_index=extra_stationary_index,
            )
            deleted_input = _delete_additional_target_stationary_index(
                tuple_value,
                source_braid_index=source_braid_index,
                already_forgetting=pair_forgets,
                extra_stationary_index=extra_stationary_index,
            )
            right = triple_target_tuples[
                triple_peiffer[triple_target_index[deleted_input]]
            ]
            if left == right:
                continue
            mismatch_count += 1
            if first_witness_pair_target_input is None:
                first_witness_pair_target_input = tuple(tuple_value)
                first_left_after_pair_peiffer_then_delete = left
                first_right_after_delete_then_triple_peiffer = right
    else:
        mismatch_count = len(pair_target_tuples)
        if pair_target_tuples:
            first_witness_pair_target_input = tuple(pair_target_tuples[0])

    return PrefixVerticalPeifferCubeTransportRow(
        source_point_pushing_arity=source_point_pushing_arity,
        source_braid_index=source_braid_index,
        triple_forget_stationary_indices=triple_forgets,
        pair_forget_stationary_indices=pair_forgets,
        extra_stationary_index=extra_stationary_index,
        first_source_generator_index=first_index,
        second_source_generator_index=second_index,
        pair_target_braid_index=pair_first_defect.target_braid_index,
        triple_target_braid_index=triple_first_defect.target_braid_index,
        pair_target_tuple_count=len(pair_target_tuples),
        triple_target_tuple_count=len(triple_target_tuples),
        pair_defect_order_pair=(
            pair_first_defect.defect_order,
            pair_second_defect.defect_order,
        ),
        triple_defect_order_pair=(
            triple_first_defect.defect_order,
            triple_second_defect.defect_order,
        ),
        pair_peiffer_is_permutation=pair_peiffer is not None,
        triple_peiffer_is_permutation=triple_peiffer is not None,
        pair_peiffer_order=pair_peiffer_order,
        triple_peiffer_order=triple_peiffer_order,
        pair_peiffer_identity=pair_peiffer_identity,
        triple_peiffer_identity=triple_peiffer_identity,
        pair_peiffer_moved_tuple_count=pair_moved_count,
        triple_peiffer_moved_tuple_count=triple_moved_count,
        additional_face_surjective=additional_face_surjective,
        peiffer_transport_commutes=mismatch_count == 0,
        mismatch_count=mismatch_count,
        first_witness_pair_target_input=first_witness_pair_target_input,
        first_left_after_pair_peiffer_then_delete=(
            first_left_after_pair_peiffer_then_delete
        ),
        first_right_after_delete_then_triple_peiffer=(
            first_right_after_delete_then_triple_peiffer
        ),
    )


def prefix_vertical_peiffer_cube_transport_audit(
    solution: FiniteBraidedSet,
) -> PrefixVerticalPeifferCubeTransportAudit:
    """Check cube transport for vertical Peiffer square boundaries."""

    source_point_pushing_arity = 5
    left_translations = _left_prefix_translations(solution)
    monoid = TransformationMonoid.generated(left_translations.values())
    row_specs = tuple(
        (triple_forgets, pair_forgets)
        for triple_forgets in combinations(
            range(1, source_point_pushing_arity + 1),
            3,
        )
        for pair_forgets in combinations(triple_forgets, 2)
    )
    rows = tuple(
        _prefix_vertical_peiffer_cube_transport_row(
            solution,
            source_point_pushing_arity=source_point_pushing_arity,
            triple_forget_stationary_indices=triple_forgets,
            pair_forget_stationary_indices=pair_forgets,
        )
        for triple_forgets, pair_forgets in row_specs
    )
    return PrefixVerticalPeifferCubeTransportAudit(
        element_count=len(solution.elements),
        left_prefix_monoid_size=len(monoid.elements),
        nonunit_prefix_count=sum(
            1
            for element in monoid.elements
            if not _transformation_is_permutation(element)
        ),
        source_point_pushing_arity=source_point_pushing_arity,
        rows=rows,
        records_first_vertical_peiffer_cube_transport=True,
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
