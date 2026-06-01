from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import TYPE_CHECKING, Mapping, Sequence, Tuple

from .artin_longitudes import (
    ArtinDetectorLiftBraidAudit,
    ArtinDetectorLiftLabel,
    ArtinDetectorLiftTransitionAudit,
    BraidWord,
    LongitudeExpressionLetter,
    LongitudeSubgroupWitness,
    artin_generator_images,
    artin_detector_lift_braid_audit,
    artin_detector_lift_transition_audit,
    evaluate_free_word,
    evaluate_longitude_subgroup_witness,
)
from .finite_group import FiniteGroup, GroupElement
from .green_branch import (
    Transformation,
    TransformationMonoid,
    identity_transformation,
)
from .local_bottleneck import LocalMasterBottleneckSummary, local_master_bottleneck_summary
from .local_interval import (
    ContinuationCongruenceAudit,
    Color,
    FibrePoint,
    LocalInterval,
    LatinTriangularYBEAudit,
    MissingTriangularCoordinateUnitRoutingAudit,
    MissingTriangularLeftRackCardinalityAudit,
    MissingTriangularPartialConstantClosureAudit,
    MissingTriangularPartialConstantContinuationRouteAudit,
    MissingTriangularRowProfileAudit,
    RackKinkLatinTriangularCollapseAudit,
    RightRackKinkLatinTriangularCollapseAudit,
    SectionRankProfileCollapseAudit,
    TriangularBundleAudit,
    TriangularColumnCollapseAudit,
    TriangularConstantKernelRecoveryRouteAudit,
    TriangularLatinDefectClosureAudit,
    TriangularRecoveryAudit,
    TwoSidedUnitCollapseAudit,
    UniversalContinuationIdentityRoutingAudit,
    continuation_congruence_audit,
    latin_triangular_ybe_audit,
    missing_triangular_coordinate_unit_routing_audit,
    missing_triangular_left_rack_cardinality_audit,
    missing_triangular_partial_constant_closure_audit,
    missing_triangular_partial_constant_continuation_route_audit,
    missing_triangular_row_profile_audit,
    rack_kink_latin_triangular_collapse_audit,
    right_rack_kink_latin_triangular_collapse_audit,
    section_rank_profile_collapse_audit,
    side_opposite_local_interval,
    triangular_bundle_audit,
    triangular_column_collapse_audit,
    triangular_constant_kernel_recovery_route_audit,
    triangular_latin_defect_closure_audit,
    triangular_recovery_audit,
    two_sided_unit_collapse_audit,
    universal_continuation_identity_routing_audit,
)
from .semigroup_holonomy import (
    UnitCompositeDerivedSeriesLiftAudit,
    UnitCompositeLongitudeExpressionAudit,
    UnitCompositeLongitudeRouteAudit,
    UnitPerfectResidualLongitudeAudit,
    monoid_permutation_group,
    unit_composite_derived_series_lift_audit,
    unit_composite_longitude_expression_audit,
    unit_composite_longitude_route_audit,
    unit_perfect_residual_longitude_audit,
)

if TYPE_CHECKING:  # pragma: no cover - typing only
    from .endpoint_factorization import (
        EndpointResidualActionAudit,
        MixedUnitContextEndpointWitnessAudit,
        MixedUnitContextSymmetricEndpointForkAudit,
        UniversalContinuationIdentityEndpointWitnessAudit,
        UniversalContinuationIdentitySymmetricEndpointForkAudit,
    )
    from .repair_contract import (
        DescentEndpointRepairContractAudit,
        EndpointFamilySymmetricForkAudit,
    )
    from .residual import LocalNormalizedLawPrefixWitnessAudit


NONLINEAR_OVERLAP_TARGET_VERDICT = "bi_free_universal_corridor_bottleneck"
UNIVERSAL_K_ENDPOINT_FAMILIES = frozenset(("U", "C", "M"))
_UNIVERSAL_K_CUTOFF_READOUT_FAMILIES = frozenset(("C", "M"))
TriangularRecoveryState = Tuple[Color, Color, FibrePoint, FibrePoint]
TriangularRecoveryEndpointKey = Tuple[Color, Color, str]
UniversalKRowDescriptor = Tuple[object, ...]
UniversalKSeedState = Tuple[object, ...]
UniversalKSeedClassifierEntry = Tuple[
    UniversalKRowDescriptor,
    Tuple[str, UniversalKSeedState],
]
UnsupportedCompanionBlockImageRowKey = Tuple[str, Color, Color]
UniversalKDetectorTrackKey = Tuple[str, int]
UniversalKDetectorTrackInitializationFailure = Tuple[
    UniversalKDetectorTrackKey,
    str,
    object,
]
UniversalKSignedEndpointEntryKey = Tuple[
    str,
    UniversalKSeedState,
    int,
    Color,
    Color,
    FibrePoint,
    FibrePoint,
]
UniversalKSignedEndpointCoordinateFailure = Tuple[
    UniversalKSignedEndpointEntryKey,
    str,
    object,
]
UniversalKSignedEndpointInverseFailure = Tuple[
    UniversalKSignedEndpointEntryKey,
    str,
    object,
]
UniversalKSignedEndpointPositiveYBEFailure = Tuple[
    Tuple[object, ...],
    str,
    object,
]
UniversalKSignedEndpointLabelFailure = Tuple[
    Tuple[object, ...],
    str,
    object,
]
UniversalKEndpointMonodromyFailure = Tuple[
    Tuple[object, ...],
    str,
    object,
]
UniversalKEndpointMonodromyContext = Tuple[
    str,
    Color,
    Color,
    FibrePoint,
    FibrePoint,
]
UniversalKEndpointMonodromyWord = Tuple[UniversalKEndpointMonodromyContext, ...]
UniversalKEndpointMonodromyRelation = Tuple[
    UniversalKEndpointMonodromyWord,
    UniversalKEndpointMonodromyWord,
]
UniversalKWordPotentialVariable = Tuple[str, int, int]
UniversalKWordPotentialLetter = Tuple[UniversalKWordPotentialVariable, int]
UniversalKWordPotentialWord = Tuple[UniversalKWordPotentialLetter, ...]
UniversalKWordPotentialSubstitution = Tuple[
    Tuple[UniversalKWordPotentialVariable, UniversalKWordPotentialWord],
    ...,
]
UniversalKWordPotentialFailure = Tuple[object, str, object]


_UNIVERSAL_K_DETECTOR_TRACK_ALLOWED_DEPENDENCIES = frozenset(
    (
        "interval_data",
        "endpoint_family",
        "routed_seed_state",
        "initial_colour_tuple",
        "initial_fibre_tuple",
        "strand_index",
        "strand_colour",
        "local_input",
        "local_output",
    )
)
_UNIVERSAL_K_DETECTOR_TRACK_FORBIDDEN_DEPENDENCIES = frozenset(
    (
        "braid_word",
        "braid_prefix",
        "braid_index",
        "failed_detector",
        "finite_search_result",
        "normalized_law_sequence",
        "timeout",
    )
)
_UNIVERSAL_K_DETECTOR_DOMAIN_SOUNDNESS_WITNESSES = frozenset(
    (
        "reachable_detector_values_enumerated",
        "symbolic_detector_domain_invariant",
    )
)


def _universal_k_nonnegative_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _universal_k_positive_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _universal_k_detector_track_key_well_formed(key: object) -> bool:
    return (
        isinstance(key, tuple)
        and len(key) == 2
        and key[0] in UNIVERSAL_K_ENDPOINT_FAMILIES
        and _universal_k_nonnegative_int(key[1])
    )


def _universal_k_detector_track_count_row_parts(
    row: object,
) -> Tuple[object, object] | None:
    if not isinstance(row, tuple) or len(row) != 2:
        return None
    return row[0], row[1]


def _universal_k_two_field_row_parts(
    row: object,
) -> Tuple[object, object] | None:
    if not isinstance(row, tuple) or len(row) != 2:
        return None
    return row[0], row[1]


def _universal_k_permutation_tuple(value: object, degree: object) -> bool:
    return (
        isinstance(value, tuple)
        and _universal_k_positive_int(degree)
        and len(value) == degree
        and all(
            _universal_k_nonnegative_int(entry) and entry < degree
            for entry in value
        )
        and set(value) == set(range(degree))
    )


@dataclass(frozen=True)
class UniversalKDetectorTrackInitializationRow:
    """Finite rule descriptor for one fixed endpoint detector track."""

    endpoint_family: str
    track_index: int
    assignment_rule: str
    dependencies: Tuple[str, ...] = ()
    local_assignment_template: Tuple[Tuple[object, object], ...] = ()

    @property
    def key(self) -> UniversalKDetectorTrackKey:
        return (self.endpoint_family, self.track_index)

    @property
    def key_valid(self) -> bool:
        return _universal_k_detector_track_key_well_formed(self.key)

    @property
    def assignment_rule_present(self) -> bool:
        return bool(self.assignment_rule)

    @property
    def duplicate_dependencies(self) -> Tuple[str, ...]:
        return _duplicate_values(self.dependencies)

    @property
    def forbidden_dependencies(self) -> Tuple[str, ...]:
        forbidden = _UNIVERSAL_K_DETECTOR_TRACK_FORBIDDEN_DEPENDENCIES
        return tuple(dependency for dependency in self.dependencies if dependency in forbidden)

    @property
    def unknown_dependencies(self) -> Tuple[str, ...]:
        allowed = _UNIVERSAL_K_DETECTOR_TRACK_ALLOWED_DEPENDENCIES
        return tuple(dependency for dependency in self.dependencies if dependency not in allowed)

    @property
    def fixed_before_braid(self) -> bool:
        return (
            self.key_valid
            and self.assignment_rule_present
            and not self.duplicate_dependencies
            and not self.forbidden_dependencies
            and not self.unknown_dependencies
        )

    @property
    def initialization_rule_finite(self) -> bool:
        return self.fixed_before_braid and bool(self.local_assignment_template)


_NONCIRCULAR_CLOSED_BRANCH_STATUSES = frozenset(
    (
        "closed_by_repair_contract",
        "closed_by_transport_state_rackification",
        "closed_by_locally_nondegenerate_branch",
        "section_kernel_visible_to_existing_readouts",
        "closed_by_product_triangular_collapse",
        "rack_base_consistency_inconsistent",
        "latin_triangular_kink_contradiction",
        "latin_triangular_kink_impossible",
        "latin_triangular_ybe_projection_inconsistent",
        "latin_triangular_kink_cancellation_inconsistent",
        "side_dual_latin_triangular_kink_contradiction",
        "side_dual_latin_triangular_kink_impossible",
        "side_dual_latin_triangular_ybe_projection_inconsistent",
        "side_dual_latin_triangular_diagonal_cancellation_inconsistent",
    )
)


@dataclass(frozen=True)
class UnsupportedCompanionStructuralContradictionRow:
    """Finite witness excluding one unsupported companion block-image row."""

    side: str
    left_color: Color
    right_color: Color
    witness_kind: str
    ybe_triple: Tuple[Color, Color, Color] = ()
    coordinate: str = ""
    left_value: object = None
    right_value: object = None
    closed_branch: str = ""

    @property
    def key(self) -> UnsupportedCompanionBlockImageRowKey:
        return (self.side, self.left_color, self.right_color)

    @property
    def proves_coordinate_ybe_contradiction(self) -> bool:
        return (
            self.witness_kind == "colored_ybe_coordinate_contradiction"
            and len(self.ybe_triple) == 3
            and self.coordinate in {"left", "right", "pair", "fibre", "state"}
            and self.left_value != self.right_value
        )

    @property
    def proves_already_closed_branch(self) -> bool:
        return (
            self.witness_kind == "already_closed_branch"
            and self.closed_branch in _NONCIRCULAR_CLOSED_BRANCH_STATUSES
        )

    @property
    def proves_structural_contradiction(self) -> bool:
        return (
            self.proves_coordinate_ybe_contradiction
            or self.proves_already_closed_branch
        )


@dataclass(frozen=True)
class UnsupportedCompanionStructuralContradictionAudit:
    """Exact finite certificate for unsupported companion block-image exclusions."""

    expected_rows: Tuple[UnsupportedCompanionBlockImageRowKey, ...]
    covered_rows: Tuple[UnsupportedCompanionBlockImageRowKey, ...]
    contradiction_rows: Tuple[
        UnsupportedCompanionStructuralContradictionRow,
        ...,
    ] = ()

    @property
    def expected_rows_exact(self) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        return tuple(sorted(set(self.expected_rows), key=repr))

    @property
    def covered_rows_exact(self) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        return tuple(sorted(set(self.covered_rows), key=repr))

    @property
    def duplicate_expected_rows(
        self,
    ) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        seen = set()
        duplicates = []
        for row in self.expected_rows:
            if row in seen and row not in duplicates:
                duplicates.append(row)
            seen.add(row)
        return tuple(duplicates)

    @property
    def duplicate_covered_rows(
        self,
    ) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        seen = set()
        duplicates = []
        for row in self.covered_rows:
            if row in seen and row not in duplicates:
                duplicates.append(row)
            seen.add(row)
        return tuple(duplicates)

    @property
    def missing_covered_rows(
        self,
    ) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        covered = set(self.covered_rows_exact)
        return tuple(row for row in self.expected_rows_exact if row not in covered)

    @property
    def extra_covered_rows(
        self,
    ) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        expected = set(self.expected_rows_exact)
        return tuple(row for row in self.covered_rows_exact if row not in expected)

    @property
    def invalid_contradiction_rows(
        self,
    ) -> Tuple[UnsupportedCompanionStructuralContradictionRow, ...]:
        return tuple(
            row
            for row in self.contradiction_rows
            if not row.proves_structural_contradiction
        )

    @property
    def contradiction_row_keys(
        self,
    ) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        return tuple(
            sorted(
                {
                    row.key
                    for row in self.contradiction_rows
                    if row.proves_structural_contradiction
                },
                key=repr,
            )
        )

    @property
    def missing_contradiction_rows(
        self,
    ) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        contradiction_keys = set(self.contradiction_row_keys)
        return tuple(
            row for row in self.expected_rows_exact if row not in contradiction_keys
        )

    @property
    def extra_contradiction_rows(
        self,
    ) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        expected = set(self.expected_rows_exact)
        return tuple(row for row in self.contradiction_row_keys if row not in expected)

    @property
    def proves_unsupported_companion_structural_contradiction(self) -> bool:
        return (
            bool(self.expected_rows_exact)
            and not self.duplicate_expected_rows
            and not self.duplicate_covered_rows
            and not self.missing_covered_rows
            and not self.extra_covered_rows
            and not self.invalid_contradiction_rows
            and not self.missing_contradiction_rows
            and not self.extra_contradiction_rows
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.expected_rows_exact:
            reasons.append("unsupported_companion_expected_rows_empty")
        if self.duplicate_expected_rows:
            reasons.append("unsupported_companion_duplicate_expected_rows")
        if self.duplicate_covered_rows:
            reasons.append("unsupported_companion_duplicate_covered_rows")
        if self.missing_covered_rows:
            reasons.append("unsupported_companion_missing_covered_rows")
        if self.extra_covered_rows:
            reasons.append("unsupported_companion_extra_covered_rows")
        if self.invalid_contradiction_rows:
            reasons.append("unsupported_companion_invalid_contradiction_rows")
        if self.missing_contradiction_rows:
            reasons.append("unsupported_companion_missing_contradiction_rows")
        if self.extra_contradiction_rows:
            reasons.append("unsupported_companion_extra_contradiction_rows")
        return tuple(reasons)


def _is_permutation_transformation(transformation: Transformation) -> bool:
    return set(transformation) == set(range(len(transformation)))


def _extend_partial_bijection_to_transformation(
    universe: Tuple[TriangularRecoveryState, ...],
    partial: Tuple[Tuple[TriangularRecoveryState, TriangularRecoveryState], ...],
) -> Transformation:
    index = {state: position for position, state in enumerate(universe)}
    mapping = {source: target for source, target in partial}
    domain = set(mapping)
    image = set(mapping.values())
    if len(mapping) != len(partial) or len(image) != len(partial):
        raise ValueError("triangular recovery row did not define a partial bijection")
    remaining_domain = tuple(state for state in universe if state not in domain)
    remaining_image = tuple(state for state in universe if state not in image)
    if len(remaining_domain) != len(remaining_image):
        raise ValueError("partial recovery bijection cannot be extended")
    mapping.update(zip(remaining_domain, remaining_image))
    return tuple(index[mapping[state]] for state in universe)


@dataclass(frozen=True)
class NonlinearOverlapObstructionAudit:
    """Audit the exact nonlinear survivor after the linear overlap closure.

    The audit joins the master local bottleneck ledger with the continuation
    congruence gate.  Optional supplied certificates record the two exits that
    remain after the finite-linear obstruction is ruled out:

    - a positive descent-endpoint repair certificate, closing the row on the
      A side;
    - a finite normalized-law prefix witness, which is only one B-shaped row
      and not by itself a counterexample.
    """

    summary: LocalMasterBottleneckSummary
    continuation: ContinuationCongruenceAudit
    repair_contract_audit: "DescentEndpointRepairContractAudit | None" = None
    normalized_prefix: "LocalNormalizedLawPrefixWitnessAudit | None" = None

    @property
    def is_corridor_verdict(self) -> bool:
        return self.summary.verdict == NONLINEAR_OVERLAP_TARGET_VERDICT

    @property
    def is_valid_local_minimal_corridor(self) -> bool:
        return (
            self.is_corridor_verdict
            and self.summary.colored_ybe
            and self.summary.semisplit_count == 0
            and self.summary.local_minimal is True
        )

    @property
    def continuation_base_ready(self) -> bool:
        return self.continuation.base_rows_are_left_rack_form

    @property
    def strand_continuing_closed(self) -> bool:
        return (
            self.is_valid_local_minimal_corridor
            and self.continuation.is_strand_continuing_on_the_nose
        )

    @property
    def universal_continuation_shape(self) -> bool:
        return (
            self.is_valid_local_minimal_corridor
            and self.continuation_base_ready
            and self.continuation.nontrivial_seed_count > 0
            and self.continuation.continuation_closure_is_universal
        )

    @property
    def exact_remaining_nonlinear_shape(self) -> bool:
        return self.universal_continuation_shape

    @property
    def repair_contract_closes(self) -> bool:
        return (
            self.is_valid_local_minimal_corridor
            and self.repair_contract_audit is not None
            and self.repair_contract_audit.proves_repair_contract_for_supplied_data
        )

    @property
    def normalized_prefix_certifies_b_row(self) -> bool:
        return (
            self.exact_remaining_nonlinear_shape
            and self.normalized_prefix is not None
            and self.normalized_prefix.proves_one_local_prefix_normalized_law_witness
        )

    @property
    def status(self) -> str:
        if not self.is_corridor_verdict:
            return "not_corridor_target"
        if not self.is_valid_local_minimal_corridor:
            return "invalid_local_corridor_data"
        if self.repair_contract_closes:
            return "closed_by_repair_contract"
        if self.normalized_prefix_certifies_b_row:
            return "one_normalized_b_prefix_certified"
        if self.strand_continuing_closed:
            return "closed_by_transport_state_rackification"
        if not self.continuation_base_ready:
            return "base_not_left_rack_form"
        if self.exact_remaining_nonlinear_shape:
            return "exact_remaining_nonlinear_obstruction"
        return "continuation_not_universal"

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.is_corridor_verdict:
            reasons.append(f"verdict:{self.summary.verdict}")
            return tuple(reasons)
        if not self.summary.colored_ybe:
            reasons.append("colored_ybe_false")
        if self.summary.semisplit_count != 0:
            reasons.append("semisplit_family_survives")
        if self.summary.local_minimal is not True:
            reasons.append("not_local_minimal")
        if not self.continuation_base_ready:
            reasons.append("non_left_rack_base_rows")
        if self.continuation_base_ready and self.continuation.nontrivial_seed_count == 0:
            reasons.append("no_continuation_seed")
        if (
            self.continuation_base_ready
            and self.continuation.nontrivial_seed_count > 0
            and not self.continuation.continuation_closure_is_universal
        ):
            reasons.append(f"continuation_closure:{self.continuation.generated.kind}")
        if (
            self.repair_contract_audit is not None
            and not self.repair_contract_audit.proves_repair_contract_for_supplied_data
        ):
            reasons.extend(
                f"repair_contract:{reason}"
                for reason in self.repair_contract_audit.failure_reasons
            )
        if (
            self.normalized_prefix is not None
            and not self.normalized_prefix.proves_one_local_prefix_normalized_law_witness
        ):
            reasons.append("normalized_prefix_not_certified")
        return tuple(reasons)


def nonlinear_overlap_obstruction_audit(
    interval: LocalInterval,
    *,
    repair_contract_audit: "DescentEndpointRepairContractAudit | None" = None,
    normalized_prefix: "LocalNormalizedLawPrefixWitnessAudit | None" = None,
    max_kernel_degree: int | None = None,
) -> NonlinearOverlapObstructionAudit:
    """Return the exact post-linear nonlinear-overlap obstruction audit."""

    return NonlinearOverlapObstructionAudit(
        summary=local_master_bottleneck_summary(
            interval,
            max_kernel_degree=max_kernel_degree,
        ),
        continuation=continuation_congruence_audit(interval),
        repair_contract_audit=repair_contract_audit,
        normalized_prefix=normalized_prefix,
    )


@dataclass(frozen=True)
class TriangularRecoveryUnitGeneratorAudit:
    """One triangular recovery row as a permutation of a fixed tagged universe."""

    row_index: int
    side: str
    left_color: Color
    right_color: Color
    output_left_color: Color
    output_right_color: Color
    source_states: Tuple[TriangularRecoveryState, ...]
    output_states: Tuple[TriangularRecoveryState, ...]
    transformation: Transformation

    @property
    def partial_is_bijection(self) -> bool:
        return (
            len(set(self.source_states)) == len(self.source_states)
            and len(set(self.output_states)) == len(self.output_states)
            and len(self.source_states) == len(self.output_states)
        )

    @property
    def transformation_is_unit(self) -> bool:
        return _is_permutation_transformation(self.transformation)


@dataclass(frozen=True)
class TriangularRecoveryUnitObserverAudit:
    """Fixed finite unit observer for triangular recovery endpoint labels."""

    recovery: TriangularRecoveryAudit
    universe: Tuple[TriangularRecoveryState, ...]
    generator_rows: Tuple[TriangularRecoveryUnitGeneratorAudit, ...]
    monoid: TransformationMonoid
    unit_group_order: int

    @property
    def row_count(self) -> int:
        return len(self.generator_rows)

    @property
    def all_recovery_formulas_bijective(self) -> bool:
        return self.recovery.every_recovery_formula_bijective

    @property
    def all_generators_are_units(self) -> bool:
        return all(row.transformation_is_unit for row in self.generator_rows)

    @property
    def proves_fixed_unit_observer(self) -> bool:
        return self.all_recovery_formulas_bijective and self.all_generators_are_units

    @property
    def generator_transformations(self) -> Tuple[Transformation, ...]:
        return tuple(row.transformation for row in self.generator_rows)


@dataclass(frozen=True)
class TriangularRecoveryLongitudeRouteAudit:
    """Route one supplied triangular recovery endpoint through its unit group."""

    observer: TriangularRecoveryUnitObserverAudit
    factor_row_indices: Tuple[int, ...]
    factors: Tuple[Transformation, ...]
    unit_route: UnitCompositeLongitudeRouteAudit

    @property
    def factors_are_triangular_recovery_generators(self) -> bool:
        return len(self.factors) == len(self.factor_row_indices)

    @property
    def endpoint_lies_in_recovery_unit_longitude_subgroup(self) -> bool:
        return self.unit_route.composite_lies_in_longitude_subgroup

    @property
    def identity_longitudes_kill_recovery_endpoint(self) -> bool:
        return self.unit_route.identity_longitudes_kill_composite

    @property
    def proves_recovery_endpoint_by_longitude_route(self) -> bool:
        return (
            self.factors_are_triangular_recovery_generators
            and self.endpoint_lies_in_recovery_unit_longitude_subgroup
        )

    @property
    def is_finite_recovery_unit_detector_failure(self) -> bool:
        return self.unit_route.is_finite_unit_detector_failure


@dataclass(frozen=True)
class TriangularRecoveryLongitudeExpressionAudit:
    """Explicit longitude-expression certificate for one recovery endpoint."""

    observer: TriangularRecoveryUnitObserverAudit
    factor_row_indices: Tuple[int, ...]
    factors: Tuple[Transformation, ...]
    unit_expression: UnitCompositeLongitudeExpressionAudit

    @property
    def factors_are_triangular_recovery_generators(self) -> bool:
        return len(self.factors) == len(self.factor_row_indices)

    @property
    def endpoint_lies_in_recovery_unit_longitude_subgroup_by_expression(self) -> bool:
        return self.unit_expression.composite_lies_in_longitude_subgroup_by_expression

    @property
    def identity_longitudes_kill_recovery_endpoint_by_expression(self) -> bool:
        return self.unit_expression.identity_longitudes_kill_composite_by_expression

    @property
    def proves_recovery_endpoint_by_longitude_expression(self) -> bool:
        return (
            self.factors_are_triangular_recovery_generators
            and self.endpoint_lies_in_recovery_unit_longitude_subgroup_by_expression
        )


@dataclass(frozen=True)
class TriangularRecoveryDerivedSeriesLiftAudit:
    """Derived-series lift route for one triangular recovery endpoint."""

    observer: TriangularRecoveryUnitObserverAudit
    factor_row_indices: Tuple[int, ...]
    factors: Tuple[Transformation, ...]
    derived_lift: UnitCompositeDerivedSeriesLiftAudit

    @property
    def factors_are_triangular_recovery_generators(self) -> bool:
        return len(self.factors) == len(self.factor_row_indices)

    @property
    def residual_endpoint(self) -> GroupElement | None:
        return self.derived_lift.final_residual

    @property
    def perfect_residual_size(self) -> int:
        return self.derived_lift.perfect_residual_size

    @property
    def proves_recovery_endpoint_by_derived_lift(self) -> bool:
        return (
            self.factors_are_triangular_recovery_generators
            and self.derived_lift.proves_endpoint_in_longitude_subgroup_by_derived_lift
        )

    @property
    def solvable_unit_group_closed_by_supplied_lifts(self) -> bool:
        return (
            self.proves_recovery_endpoint_by_derived_lift
            and self.derived_lift.perfect_residual_is_trivial
        )


@dataclass(frozen=True)
class TriangularRecoveryPerfectResidualAudit:
    """Perfect-residual route for the terminal triangular recovery endpoint."""

    observer: TriangularRecoveryUnitObserverAudit
    residual_endpoint: Transformation
    perfect_residual: UnitPerfectResidualLongitudeAudit

    @property
    def residual_endpoint_is_recovery_unit(self) -> bool:
        return self.perfect_residual.residual_endpoint_in_unit_group

    @property
    def residual_endpoint_is_in_perfect_residual(self) -> bool:
        return self.perfect_residual.residual_endpoint_in_perfect_residual

    @property
    def proves_recovery_residual_endpoint_by_perfect_route(self) -> bool:
        return self.perfect_residual.proves_perfect_residual_endpoint_in_longitude_subgroup

    @property
    def identity_longitudes_kill_recovery_residual_endpoint(self) -> bool:
        return self.perfect_residual.identity_longitudes_kill_perfect_residual_endpoint

    @property
    def is_finite_recovery_perfect_residual_detector_failure(self) -> bool:
        return self.perfect_residual.is_finite_perfect_residual_detector_failure


def _triangular_recovery_endpoint_audit_proves(endpoint_audit: object) -> bool:
    """Return whether a supplied recovery endpoint audit proves V_beta membership."""

    for attribute in (
        "proves_recovery_endpoint_by_longitude_route",
        "proves_recovery_endpoint_by_longitude_expression",
        "proves_recovery_endpoint_by_derived_lift",
        "proves_recovery_residual_endpoint_by_perfect_route",
    ):
        value = getattr(endpoint_audit, attribute, None)
        if value is True:
            return True
    return False


def _triangular_recovery_endpoint_key(
    defect: Tuple[Tuple[Color, Color], str],
) -> TriangularRecoveryEndpointKey:
    pair, reason = defect
    return (pair[0], pair[1], reason)


def _sorted_triangular_recovery_endpoint_keys(
    keys: Sequence[TriangularRecoveryEndpointKey],
) -> Tuple[TriangularRecoveryEndpointKey, ...]:
    return tuple(sorted(set(keys), key=repr))


def _side_symbol(side: str) -> str:
    if side == "left":
        return "L"
    if side == "right":
        return "R"
    return side


def _side_from_reason(reason: str) -> str | None:
    if reason.startswith("left_") or reason == "no_left_triangular_row":
        return "left"
    if reason.startswith("right_") or reason == "no_right_triangular_row":
        return "right"
    return None


def _constant_map_kernel_kind_from_reason(reason: str) -> str:
    if "_proper_kernel" in reason:
        return "proper"
    if "_universal_kernel" in reason:
        return "universal"
    return "supported"


def _duplicate_values(values: Sequence[object]) -> Tuple[object, ...]:
    def marker(value: object) -> object:
        try:
            hash(value)
        except TypeError:
            return ("unhashable", repr(value))
        return ("hashable", value)

    seen = set()
    duplicates = {}
    for value in values:
        key = marker(value)
        if key in seen:
            duplicates.setdefault(key, value)
        else:
            seen.add(key)
    return tuple(sorted(duplicates.values(), key=repr))


def _value_marker(value: object) -> object:
    try:
        hash(value)
    except TypeError:
        return ("unhashable", repr(value))
    return ("hashable", value)


def _is_hashable(value: object) -> bool:
    try:
        hash(value)
    except TypeError:
        return False
    return True


def _unique_values(values: Sequence[object]) -> Tuple[object, ...]:
    unique = {}
    for value in values:
        unique.setdefault(_value_marker(value), value)
    return tuple(sorted(unique.values(), key=repr))


@dataclass(frozen=True)
class UniversalKSignedEndpointGeneratorRow:
    """One finite signed endpoint-generator entry on a routed K seed state."""

    endpoint_family: str
    seed_state: UniversalKSeedState
    sign: int
    left_color: Color
    right_color: Color
    input_left: FibrePoint
    input_right: FibrePoint
    output_left: FibrePoint
    output_right: FibrePoint
    next_seed_state: UniversalKSeedState
    endpoint_value: object | None

    @property
    def seed_key(self) -> Tuple[str, UniversalKSeedState, int]:
        return (self.endpoint_family, self.seed_state, self.sign)

    @property
    def entry_key(self) -> Tuple[
        str, UniversalKSeedState, int, Color, Color, FibrePoint, FibrePoint
    ]:
        return (
            self.endpoint_family,
            self.seed_state,
            self.sign,
            self.left_color,
            self.right_color,
            self.input_left,
            self.input_right,
        )

    @property
    def endpoint_family_known(self) -> bool:
        return self.endpoint_family in UNIVERSAL_K_ENDPOINT_FAMILIES

    @property
    def sign_known(self) -> bool:
        return self.sign in {-1, 1}

    @property
    def endpoint_value_supplied(self) -> bool:
        return self.endpoint_value is not None

    @property
    def row_is_defined(self) -> bool:
        return (
            self.endpoint_family_known
            and self.sign_known
            and self.endpoint_value_supplied
        )


@dataclass(frozen=True)
class UniversalKWordPotentialIdentityRow:
    """One finite word-potential identity attached to a signed endpoint row."""

    entry_key: UniversalKSignedEndpointEntryKey
    next_seed_state: UniversalKSeedState
    endpoint_value: object
    artin_substitution: UniversalKWordPotentialSubstitution = ()
    detector_domain_assignments: (
        Tuple[Tuple[Tuple[UniversalKWordPotentialVariable, GroupElement], ...], ...]
        | None
    ) = None
    detector_domain_sound: bool = False
    detector_domain_soundness_witness: Tuple[str, ...] = ()


def _universal_k_word_potential_variables(
    word: UniversalKWordPotentialWord,
) -> Tuple[UniversalKWordPotentialVariable, ...]:
    variables = []
    for letter in word:
        parts = _universal_k_word_potential_letter_parts(letter)
        if parts is None:
            continue
        variable, _exponent = parts
        variables.append(variable)
    return _unique_values(tuple(variables))


def _universal_k_word_potential_letter_parts(
    letter: object,
) -> Tuple[object, object] | None:
    if not isinstance(letter, tuple) or len(letter) != 2:
        return None
    return letter[0], letter[1]


def _universal_k_word_potential_substitution_parts(
    substitution_row: object,
) -> Tuple[object, object] | None:
    if not isinstance(substitution_row, tuple) or len(substitution_row) != 2:
        return None
    return substitution_row[0], substitution_row[1]


def _universal_k_word_potential_variable_valid(
    variable: object,
) -> bool:
    return (
        isinstance(variable, tuple)
        and len(variable) == 3
        and variable[0] in {"U", "A"}
        and _universal_k_nonnegative_int(variable[1])
        and _universal_k_nonnegative_int(variable[2])
    )


def _universal_k_word_potential_word_failures(
    word: UniversalKWordPotentialWord,
) -> Tuple[UniversalKWordPotentialFailure, ...]:
    failures = []
    for index, letter in enumerate(word):
        parts = _universal_k_word_potential_letter_parts(letter)
        if parts is None:
            failures.append((index, "invalid_word_potential_letter", letter))
            continue
        variable, exponent = parts
        if not _universal_k_word_potential_variable_valid(variable):
            failures.append((index, "invalid_word_potential_variable", variable))
        if exponent not in {-1, 1}:
            failures.append((index, "invalid_word_potential_exponent", exponent))
    return tuple(failures)


def _universal_k_word_potential_invert(
    word: UniversalKWordPotentialWord,
) -> UniversalKWordPotentialWord:
    inverted = []
    for letter in reversed(word):
        parts = _universal_k_word_potential_letter_parts(letter)
        if parts is None:
            inverted.append(letter)
            continue
        variable, exponent = parts
        inverted.append((variable, -exponent))
    return tuple(inverted)


def _universal_k_word_potential_substitute(
    word: UniversalKWordPotentialWord,
    substitution: UniversalKWordPotentialSubstitution,
) -> UniversalKWordPotentialWord:
    substitution_map = {}
    for substitution_row in substitution:
        parts = _universal_k_word_potential_substitution_parts(substitution_row)
        if parts is None:
            continue
        variable, image = parts
        substitution_map[_value_marker(variable)] = image
    expanded = []
    for letter in word:
        parts = _universal_k_word_potential_letter_parts(letter)
        if parts is None:
            expanded.append(letter)
            continue
        variable, exponent = parts
        image = substitution_map.get(_value_marker(variable), ((variable, 1),))
        if exponent < 0:
            image = _universal_k_word_potential_invert(image)
        expanded.extend(image)
    return tuple(expanded)


def universal_k_evaluate_word_potential(
    endpoint_group: FiniteGroup,
    assignment: Mapping[UniversalKWordPotentialVariable, GroupElement],
    word: UniversalKWordPotentialWord,
) -> GroupElement:
    """Evaluate a finite word-potential template in an explicit endpoint group."""

    out = endpoint_group.identity
    group_elements = set(endpoint_group.elements)
    for letter in word:
        parts = _universal_k_word_potential_letter_parts(letter)
        if parts is None:
            raise ValueError(f"invalid word-potential letter {letter!r}")
        variable, exponent = parts
        if not _universal_k_word_potential_variable_valid(variable):
            raise ValueError(f"invalid word-potential variable {variable!r}")
        if exponent not in {-1, 1}:
            raise ValueError(f"invalid word-potential exponent {exponent!r}")
        if variable not in assignment:
            raise ValueError(f"missing word-potential assignment for {variable!r}")
        value = assignment[variable]
        if value not in group_elements:
            raise ValueError("word-potential assignment contains value outside group")
        out = endpoint_group.mul(out, endpoint_group.pow(value, exponent))
    return out


def _universal_k_expected_artin_substitution(
    variable: UniversalKWordPotentialVariable,
    sign: int,
) -> UniversalKWordPotentialWord:
    kind, track, position = variable
    if kind != "U" or position not in {0, 1}:
        return ((variable, 1),)
    u_left = ("U", track, 0)
    u_right = ("U", track, 1)
    a_left = ("A", track, 0)
    a_right = ("A", track, 1)
    if sign == 1 and position == 0:
        return ((u_left, 1), (a_left, 1), (u_left, -1), (u_right, 1))
    if sign == 1 and position == 1:
        return ((u_left, 1),)
    if sign == -1 and position == 0:
        return ((u_right, 1),)
    if sign == -1 and position == 1:
        return ((u_right, 1), (a_right, -1), (u_right, -1), (u_left, 1))
    return ((variable, 1),)


def _universal_k_is_positive_entry_key(
    key: UniversalKSignedEndpointEntryKey,
) -> bool:
    return _universal_k_signed_entry_key_well_formed(key) and key[2] == 1


def _universal_k_signed_entry_key_well_formed(
    key: UniversalKSignedEndpointEntryKey,
) -> bool:
    return (
        isinstance(key, tuple)
        and len(key) == 7
        and _is_hashable(key)
        and key[0] in UNIVERSAL_K_ENDPOINT_FAMILIES
        and isinstance(key[1], tuple)
        and key[2] in {-1, 1}
    )


def _universal_k_entry_key_sign(key: object) -> object:
    if not isinstance(key, tuple) or len(key) <= 2:
        return None
    return key[2]


def _universal_k_endpoint_seed_state_well_formed(state: object) -> bool:
    return (
        isinstance(state, tuple)
        and len(state) == 2
        and _is_hashable(state)
        and state[0] in UNIVERSAL_K_ENDPOINT_FAMILIES
        and isinstance(state[1], tuple)
    )


def _universal_k_cutoff_seed_state_well_formed(state: object) -> bool:
    return (
        _universal_k_endpoint_seed_state_well_formed(state)
        and state[0] in _UNIVERSAL_K_CUTOFF_READOUT_FAMILIES
    )


def _universal_k_residual_endpoint_channel_key_well_formed(key: object) -> bool:
    if not isinstance(key, tuple) or len(key) < 3:
        return False
    family, seed_state, channel_name = key[:3]
    try:
        hash(key)
    except TypeError:
        return False
    return (
        family in UNIVERSAL_K_ENDPOINT_FAMILIES
        and isinstance(seed_state, tuple)
        and _universal_k_endpoint_seed_state_well_formed((family, seed_state))
        and isinstance(channel_name, str)
        and bool(channel_name)
    )


@dataclass(frozen=True)
class UniversalKWordPotentialCertificate:
    """Concrete finite word-potential detector-lift certificate.

    Templates are indexed by endpoint family and reachable seed state.  Each
    positive table row supplies the Artin substitution for the next-state
    template and the emitted endpoint label.  Negative rows are checked as
    inverse-derived signed endpoint rows by the surrounding generator audit.
    The checker exhausts all assignments of the finitely many formal variables
    to the finite endpoint group, so the certificate is mathematical data
    rather than a boolean assertion.
    """

    endpoint_group: FiniteGroup
    templates: Tuple[
        Tuple[Tuple[str, UniversalKSeedState], UniversalKWordPotentialWord],
        ...,
    ]
    identity_rows: Tuple[UniversalKWordPotentialIdentityRow, ...]
    normalized_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...] = ()

    @property
    def template_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(tuple(state for state, _word in self.templates))

    @property
    def duplicate_template_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(tuple(state for state, _word in self.templates))

    @property
    def malformed_template_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(
            tuple(
                state
                for state, _word in self.templates
                if not _universal_k_endpoint_seed_state_well_formed(state)
            )
        )

    @property
    def identity_entry_keys_exact(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _unique_values(tuple(row.entry_key for row in self.identity_rows))

    @property
    def positive_identity_entry_keys_exact(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return tuple(
            key
            for key in self.identity_entry_keys_exact
            if _universal_k_is_positive_entry_key(key)
        )

    @property
    def duplicate_identity_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _duplicate_values(tuple(row.entry_key for row in self.identity_rows))

    @property
    def duplicate_positive_identity_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _duplicate_values(
            tuple(
                row.entry_key
                for row in self.identity_rows
                if _universal_k_is_positive_entry_key(row.entry_key)
            )
        )

    @property
    def malformed_identity_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _unique_values(
            tuple(
                row.entry_key
                for row in self.identity_rows
                if not _universal_k_signed_entry_key_well_formed(row.entry_key)
            )
        )

    @property
    def malformed_identity_next_seed_states(
        self,
    ) -> Tuple[Tuple[UniversalKSignedEndpointEntryKey, object], ...]:
        return _unique_values(
            tuple(
                (row.entry_key, row.next_seed_state)
                for row in self.identity_rows
                if _universal_k_signed_entry_key_well_formed(row.entry_key)
                if _universal_k_is_positive_entry_key(row.entry_key)
                if not _universal_k_endpoint_seed_state_well_formed(
                    (row.entry_key[0], row.next_seed_state)
                )
            )
        )

    @property
    def normalized_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(self.normalized_seed_states)

    @property
    def duplicate_normalized_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.normalized_seed_states)

    @property
    def malformed_normalized_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(
            tuple(
                state
                for state in self.normalized_seed_states
                if not _universal_k_endpoint_seed_state_well_formed(state)
            )
        )

    @property
    def template_map(
        self,
    ) -> Mapping[Tuple[str, UniversalKSeedState], UniversalKWordPotentialWord]:
        return {
            state: word
            for state, word in self.templates
            if _universal_k_endpoint_seed_state_well_formed(state)
        }

    @property
    def identity_row_map(
        self,
    ) -> Mapping[UniversalKSignedEndpointEntryKey, UniversalKWordPotentialIdentityRow]:
        return {
            row.entry_key: row
            for row in self.identity_rows
            if _universal_k_signed_entry_key_well_formed(row.entry_key)
        }

    @property
    def template_word_failures(self) -> Tuple[UniversalKWordPotentialFailure, ...]:
        failures = []
        for state, word in self.templates:
            for failure in _universal_k_word_potential_word_failures(word):
                failures.append((state, failure[1], failure[2]))
        return tuple(failures)

    @property
    def substitution_failures(self) -> Tuple[UniversalKWordPotentialFailure, ...]:
        failures = []
        template_map = self.template_map
        for row in self.identity_rows:
            sign = _universal_k_entry_key_sign(row.entry_key)
            if not _universal_k_signed_entry_key_well_formed(row.entry_key):
                failures.append((row.entry_key, "malformed_signed_entry_key", sign))
                continue
            entry_family, _state, sign, *_rest = row.entry_key
            if sign != 1:
                continue
            if not _universal_k_endpoint_seed_state_well_formed(
                (entry_family, row.next_seed_state)
            ):
                failures.append(
                    (
                        row.entry_key,
                        "malformed_next_seed_state",
                        row.next_seed_state,
                    )
                )
                continue
            next_key = (entry_family, row.next_seed_state)
            next_template = template_map.get(next_key)
            if next_template is None:
                failures.append((row.entry_key, "missing_next_state_template", next_key))
                continue
            next_template_failures = _universal_k_word_potential_word_failures(
                next_template
            )
            if next_template_failures:
                for failure in next_template_failures:
                    failures.append((row.entry_key, failure[1], failure[2]))
                continue
            expected_variables = set(_universal_k_word_potential_variables(next_template))
            substitution_variables = []
            malformed_substitution_rows = []
            for substitution_row in row.artin_substitution:
                parts = _universal_k_word_potential_substitution_parts(
                    substitution_row
                )
                if parts is None:
                    malformed_substitution_rows.append(substitution_row)
                    continue
                variable, _image = parts
                substitution_variables.append(variable)
            for substitution_row in malformed_substitution_rows:
                failures.append(
                    (
                        row.entry_key,
                        "malformed_artin_substitution_row",
                        substitution_row,
                    )
                )
            substitution_variables = tuple(substitution_variables)
            duplicate_variables = _duplicate_values(substitution_variables)
            for variable in duplicate_variables:
                failures.append(
                    (row.entry_key, "duplicate_artin_substitution_variable", variable)
                )
            supplied_variables = set(substitution_variables)
            for variable in sorted(expected_variables - supplied_variables, key=repr):
                failures.append(
                    (row.entry_key, "missing_artin_substitution_variable", variable)
                )
            for variable in sorted(supplied_variables - expected_variables, key=repr):
                failures.append(
                    (row.entry_key, "extra_artin_substitution_variable", variable)
                )
            for substitution_row in row.artin_substitution:
                parts = _universal_k_word_potential_substitution_parts(
                    substitution_row
                )
                if parts is None:
                    continue
                variable, image = parts
                if not _universal_k_word_potential_variable_valid(variable):
                    failures.append(
                        (row.entry_key, "invalid_artin_substitution_variable", variable)
                    )
                    continue
                for failure in _universal_k_word_potential_word_failures(image):
                    failures.append((row.entry_key, failure[1], failure[2]))
                expected_image = _universal_k_expected_artin_substitution(
                    variable,
                    sign,
                )
                if tuple(image) != expected_image:
                    failures.append(
                        (
                            row.entry_key,
                            "artin_substitution_image_mismatch",
                            (variable, image, expected_image),
                        )
                    )
        return tuple(failures)

    @property
    def templates_use_only_current_longitudes(self) -> bool:
        for _state, word in self.templates:
            for letter in word:
                parts = _universal_k_word_potential_letter_parts(letter)
                if parts is None:
                    continue
                variable, _exponent = parts
                if (
                    _universal_k_word_potential_variable_valid(variable)
                    and variable[0] != "U"
                ):
                    return False
        return True

    @property
    def invalid_template_variable_failures(
        self,
    ) -> Tuple[UniversalKWordPotentialFailure, ...]:
        return tuple(
            failure
            for failure in self.template_word_failures
            if failure[1] == "invalid_word_potential_variable"
        )

    @property
    def raw_assignment_template_variables(
        self,
    ) -> Tuple[UniversalKWordPotentialVariable, ...]:
        raw_variables = []
        for _state, word in self.templates:
            for letter in word:
                parts = _universal_k_word_potential_letter_parts(letter)
                if parts is None:
                    continue
                variable, _exponent = parts
                if (
                    _universal_k_word_potential_variable_valid(variable)
                    and variable[0] != "U"
                ):
                    raw_variables.append(variable)
        return _unique_values(tuple(raw_variables))

    def _identity_row_variable_support(
        self,
        row: UniversalKWordPotentialIdentityRow,
    ) -> Tuple[UniversalKWordPotentialVariable, ...] | None:
        if not _universal_k_signed_entry_key_well_formed(row.entry_key):
            return None
        entry_family, source_state, sign, *_rest = row.entry_key
        if sign != 1:
            return None
        if not _universal_k_endpoint_seed_state_well_formed(
            (entry_family, row.next_seed_state)
        ):
            return None
        template_map = self.template_map
        source_template = template_map.get((entry_family, source_state))
        next_template = template_map.get((entry_family, row.next_seed_state))
        if source_template is None or next_template is None:
            return None
        substituted_next = _universal_k_word_potential_substitute(
            next_template,
            row.artin_substitution,
        )
        word_failures = (
            _universal_k_word_potential_word_failures(source_template)
            + _universal_k_word_potential_word_failures(substituted_next)
        )
        if word_failures:
            return None
        return tuple(
            sorted(
                set(_universal_k_word_potential_variables(source_template))
                | set(_universal_k_word_potential_variables(substituted_next)),
                key=repr,
            )
        )

    @property
    def detector_domain_failures(self) -> Tuple[UniversalKWordPotentialFailure, ...]:
        failures = []
        group_elements = set(self.endpoint_group.elements)
        for row in self.identity_rows:
            if not _universal_k_signed_entry_key_well_formed(row.entry_key):
                continue
            if not _universal_k_is_positive_entry_key(row.entry_key):
                continue
            assignments = row.detector_domain_assignments
            if assignments is None:
                continue
            variables = self._identity_row_variable_support(row)
            if variables is None:
                continue
            variable_by_marker = {
                _value_marker(variable): variable for variable in variables
            }
            variable_markers = set(variable_by_marker)
            if not row.detector_domain_sound:
                failures.append(
                    (
                        row.entry_key,
                        "detector_domain_subset_not_proved_sound",
                        None,
                    )
                )
            if not row.detector_domain_soundness_witness:
                failures.append(
                    (
                        row.entry_key,
                        "detector_domain_soundness_witness_missing",
                        None,
                    )
                )
            duplicate_witnesses = _duplicate_values(
                row.detector_domain_soundness_witness
            )
            for witness in duplicate_witnesses:
                failures.append(
                    (
                        row.entry_key,
                        "detector_domain_duplicate_soundness_witness",
                        witness,
                    )
                )
            for witness in row.detector_domain_soundness_witness:
                if witness not in _UNIVERSAL_K_DETECTOR_DOMAIN_SOUNDNESS_WITNESSES:
                    failures.append(
                        (
                            row.entry_key,
                            "detector_domain_unknown_soundness_witness",
                            witness,
                        )
                    )
            if not assignments:
                failures.append((row.entry_key, "detector_domain_subset_empty", None))
                continue
            duplicate_assignments = _duplicate_values(
                tuple(tuple(sorted(assignment, key=repr)) for assignment in assignments)
            )
            for duplicate in duplicate_assignments:
                failures.append(
                    (row.entry_key, "duplicate_detector_domain_assignment", duplicate)
                )
            for index, assignment in enumerate(assignments):
                assignment_variables = []
                malformed_assignment_entries = []
                for assignment_entry in assignment:
                    parts = _universal_k_word_potential_substitution_parts(
                        assignment_entry
                    )
                    if parts is None:
                        malformed_assignment_entries.append(assignment_entry)
                        continue
                    variable, _value = parts
                    assignment_variables.append(variable)
                for assignment_entry in malformed_assignment_entries:
                    failures.append(
                        (
                            row.entry_key,
                            "detector_domain_assignment_malformed_entry",
                            (index, assignment_entry),
                        )
                    )
                assignment_variables = tuple(assignment_variables)
                duplicate_variables = _duplicate_values(assignment_variables)
                for variable in duplicate_variables:
                    failures.append(
                        (
                            row.entry_key,
                            "detector_domain_assignment_duplicate_variable",
                            (index, variable),
                        )
                    )
                assignment_variable_by_marker = {
                    _value_marker(variable): variable
                    for variable in assignment_variables
                }
                assignment_variable_markers = set(assignment_variable_by_marker)
                missing_variables = tuple(
                    sorted(
                        (
                            variable_by_marker[marker]
                            for marker in (
                                variable_markers - assignment_variable_markers
                            )
                        ),
                        key=repr,
                    )
                )
                if missing_variables:
                    failures.append(
                        (
                            row.entry_key,
                            "detector_domain_assignment_missing_variables",
                            (index, missing_variables),
                        )
                    )
                extra_variables = tuple(
                    sorted(
                        (
                            assignment_variable_by_marker[marker]
                            for marker in (
                                assignment_variable_markers - variable_markers
                            )
                        ),
                        key=repr,
                    )
                )
                if extra_variables:
                    failures.append(
                        (
                            row.entry_key,
                            "detector_domain_assignment_extra_variables",
                            (index, extra_variables),
                        )
                    )
                for assignment_entry in assignment:
                    parts = _universal_k_word_potential_substitution_parts(
                        assignment_entry
                    )
                    if parts is None:
                        continue
                    variable, value = parts
                    if not _universal_k_word_potential_variable_valid(variable):
                        failures.append(
                            (
                                row.entry_key,
                                "detector_domain_assignment_invalid_variable",
                                (index, variable),
                            )
                        )
                    if value not in group_elements:
                        failures.append(
                            (
                                row.entry_key,
                                "detector_domain_assignment_value_outside_group",
                                (index, value),
                            )
                        )
        return tuple(failures)

    @property
    def detector_domains_sound(self) -> bool:
        return not self.detector_domain_failures

    @property
    def identity_failures(self) -> Tuple[UniversalKWordPotentialFailure, ...]:
        failures = []
        template_map = self.template_map
        group_elements = set(self.endpoint_group.elements)
        domain_failure_keys = {failure[0] for failure in self.detector_domain_failures}
        for row in self.identity_rows:
            if not _universal_k_signed_entry_key_well_formed(row.entry_key):
                continue
            entry_family, source_state, _sign, *_rest = row.entry_key
            if _sign != 1:
                continue
            source_key = (entry_family, source_state)
            if not _universal_k_endpoint_seed_state_well_formed(
                (entry_family, row.next_seed_state)
            ):
                failures.append(
                    (
                        row.entry_key,
                        "malformed_next_seed_state",
                        row.next_seed_state,
                    )
                )
                continue
            next_key = (entry_family, row.next_seed_state)
            source_template = template_map.get(source_key)
            next_template = template_map.get(next_key)
            if source_template is None:
                failures.append((row.entry_key, "missing_source_state_template", source_key))
                continue
            if next_template is None:
                failures.append((row.entry_key, "missing_next_state_template", next_key))
                continue
            if row.endpoint_value not in group_elements:
                failures.append(
                    (
                        row.entry_key,
                        "endpoint_value_outside_group",
                        row.endpoint_value,
                    )
                )
                continue
            substituted_next = _universal_k_word_potential_substitute(
                next_template,
                row.artin_substitution,
            )
            word_failures = (
                _universal_k_word_potential_word_failures(source_template)
                + _universal_k_word_potential_word_failures(substituted_next)
            )
            if word_failures:
                for failure in word_failures:
                    failures.append((row.entry_key, failure[1], failure[2]))
                continue
            variables = tuple(
                sorted(
                    set(_universal_k_word_potential_variables(source_template))
                    | set(_universal_k_word_potential_variables(substituted_next)),
                    key=repr,
                )
            )
            if row.entry_key in domain_failure_keys:
                continue
            if row.detector_domain_assignments is None:
                assignment_iter = (
                    tuple(zip(variables, values))
                    for values in product(
                        self.endpoint_group.elements,
                        repeat=len(variables),
                    )
                )
            else:
                assignment_iter = iter(row.detector_domain_assignments)
            for assignment_row in assignment_iter:
                assignment = dict(assignment_row)
                left = universal_k_evaluate_word_potential(
                    self.endpoint_group,
                    assignment,
                    substituted_next,
                )
                source_value = universal_k_evaluate_word_potential(
                    self.endpoint_group,
                    assignment,
                    source_template,
                )
                right = self.endpoint_group.mul(source_value, row.endpoint_value)
                if left != right:
                    failures.append(
                        (
                            row.entry_key,
                            "word_potential_identity_mismatch",
                            (tuple(assignment_row), left, right),
                        )
                    )
                    break
        return tuple(failures)

    @property
    def coboundary_defect_failures(self) -> Tuple[UniversalKWordPotentialFailure, ...]:
        return self.detector_domain_failures + self.identity_failures

    @property
    def coboundary_defects_constant(self) -> bool:
        return not self.coboundary_defect_failures

    @property
    def normalization_failures(self) -> Tuple[UniversalKWordPotentialFailure, ...]:
        failures = []
        template_map = self.template_map
        for state in self.normalized_seed_states_exact:
            template = template_map.get(state)
            if template is None:
                failures.append((state, "missing_normalized_state_template", None))
                continue
            variables = _universal_k_word_potential_variables(template)
            invalid_variables = tuple(
                variable
                for variable in variables
                if not _universal_k_word_potential_variable_valid(variable)
            )
            if invalid_variables:
                failures.append(
                    (
                        state,
                        "word_potential_normalization_invalid_template",
                        invalid_variables,
                    )
                )
                continue
            assignment = {variable: self.endpoint_group.identity for variable in variables}
            try:
                value = universal_k_evaluate_word_potential(
                    self.endpoint_group,
                    assignment,
                    template,
                )
            except ValueError as error:
                failures.append(
                    (
                        state,
                        "word_potential_normalization_invalid_template",
                        repr(error),
                    )
                )
                continue
            if value != self.endpoint_group.identity:
                failures.append((state, "word_potential_initial_value_mismatch", value))
        return tuple(failures)

    @property
    def word_potential_templates_verified(self) -> bool:
        return (
            not self.duplicate_template_seed_states
            and not self.malformed_template_seed_states
            and not self.template_word_failures
            and self.templates_use_only_current_longitudes
        )

    @property
    def artin_substitutions_verified(self) -> bool:
        return (
            not self.malformed_identity_entry_keys
            and not self.malformed_identity_next_seed_states
            and not self.duplicate_positive_identity_entry_keys
            and not self.substitution_failures
        )

    @property
    def identities_verified(self) -> bool:
        return (
            not self.malformed_identity_entry_keys
            and not self.malformed_identity_next_seed_states
            and not self.duplicate_positive_identity_entry_keys
            and not self.detector_domain_failures
            and not self.identity_failures
        )

    @property
    def initial_readouts_normalized(self) -> bool:
        return (
            bool(self.normalized_seed_states_exact)
            and not self.duplicate_normalized_seed_states
            and not self.malformed_normalized_seed_states
            and not self.normalization_failures
        )


_UNIVERSAL_K_RESIDUAL_ALLOWED_DEPENDENCIES = frozenset(
    (
        "interval_data",
        "endpoint_family",
        "routed_seed_state",
        "residual_input_tuple",
        "endpoint_channel",
        "local_fibre_coordinate",
        "local_row_table",
    )
)
_UNIVERSAL_K_RESIDUAL_FORBIDDEN_DEPENDENCIES = frozenset(
    (
        "braid_word",
        "braid_prefix",
        "braid_index",
        "failed_detector",
        "finite_search_result",
        "normalized_law_sequence",
        "timeout",
    )
)


@dataclass(frozen=True)
class UniversalKResidualFaithfulnessRow:
    """One symbolic residual row controlled by killed endpoint channels."""

    input_tuple: Tuple[object, ...]
    output_tuple: Tuple[object, ...]
    identity_endpoint_output_tuple: Tuple[object, ...]
    endpoint_families: Tuple[str, ...]
    endpoint_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...]
    endpoint_channel_keys: Tuple[object, ...] = ()
    dependencies: Tuple[str, ...] = ()

    @property
    def duplicate_endpoint_families(self) -> Tuple[str, ...]:
        return _duplicate_values(self.endpoint_families)

    @property
    def duplicate_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.endpoint_seed_states)

    @property
    def malformed_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    state
                    for state in self.endpoint_seed_states
                    if not _universal_k_endpoint_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def duplicate_endpoint_channel_keys(self) -> Tuple[object, ...]:
        hashable_keys = []
        for key in self.endpoint_channel_keys:
            try:
                hash(key)
            except TypeError:
                continue
            hashable_keys.append(key)
        return _duplicate_values(tuple(hashable_keys))

    @property
    def malformed_endpoint_channel_keys(self) -> Tuple[object, ...]:
        malformed = []
        seen = set()
        for key in self.endpoint_channel_keys:
            if _universal_k_residual_endpoint_channel_key_well_formed(key):
                continue
            marker = repr(key)
            if marker in seen:
                continue
            seen.add(marker)
            malformed.append(key)
        return tuple(sorted(malformed, key=repr))

    @property
    def endpoint_channel_key_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    (key[0], key[1])
                    for key in self.endpoint_channel_keys
                    if _universal_k_residual_endpoint_channel_key_well_formed(key)
                },
                key=repr,
            )
        )

    @property
    def endpoint_channel_keys_match_seed_states(self) -> bool:
        return (
            not self.malformed_endpoint_channel_keys
            and set(self.endpoint_channel_key_seed_states)
            == set(self.endpoint_seed_states)
        )

    @property
    def duplicate_dependencies(self) -> Tuple[str, ...]:
        return _duplicate_values(self.dependencies)

    @property
    def invalid_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.endpoint_families
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def seed_state_families_match_row(self) -> bool:
        return not self.malformed_endpoint_seed_states and {
            family for family, _seed_state in self.endpoint_seed_states
        } == set(self.endpoint_families)

    @property
    def forbidden_dependencies(self) -> Tuple[str, ...]:
        forbidden = _UNIVERSAL_K_RESIDUAL_FORBIDDEN_DEPENDENCIES
        return tuple(dependency for dependency in self.dependencies if dependency in forbidden)

    @property
    def unknown_dependencies(self) -> Tuple[str, ...]:
        allowed = _UNIVERSAL_K_RESIDUAL_ALLOWED_DEPENDENCIES
        return tuple(dependency for dependency in self.dependencies if dependency not in allowed)

    @property
    def identity_endpoint_data_fixes_row(self) -> bool:
        return self.identity_endpoint_output_tuple == self.input_tuple

    @property
    def tuple_arity_consistent(self) -> bool:
        return (
            bool(self.input_tuple)
            and len(self.input_tuple)
            == len(self.output_tuple)
            == len(self.identity_endpoint_output_tuple)
        )

    @property
    def row_scope_valid(self) -> bool:
        return (
            self.tuple_arity_consistent
            and bool(self.endpoint_families)
            and bool(self.endpoint_seed_states)
            and bool(self.endpoint_channel_keys)
            and not self.duplicate_endpoint_channel_keys
            and not self.malformed_endpoint_channel_keys
            and self.endpoint_channel_keys_match_seed_states
            and not self.duplicate_endpoint_families
            and not self.duplicate_endpoint_seed_states
            and not self.malformed_endpoint_seed_states
            and not self.invalid_endpoint_families
            and self.seed_state_families_match_row
            and not self.duplicate_dependencies
            and not self.forbidden_dependencies
            and not self.unknown_dependencies
        )


@dataclass(frozen=True)
class UniversalKResidualFaithfulnessAudit:
    """Scoped theorem audit connecting endpoint collapse to residual action."""

    active_endpoint_families: Tuple[str, ...]
    covered_endpoint_families: Tuple[str, ...]
    expected_residual_row_count: int | None
    covered_residual_row_count: int
    expected_residual_rows_by_family: Tuple[Tuple[str, int], ...] = ()
    covered_residual_rows_by_family: Tuple[Tuple[str, int], ...] = ()
    expected_residual_input_tuples: Tuple[Tuple[object, ...], ...] = ()
    covered_residual_input_tuples: Tuple[Tuple[object, ...], ...] = ()
    endpoint_channels_exact: bool = False
    identity_endpoint_data_forces_residual_identity: bool = False
    braid_index_independent: bool = False
    product_families_separated: bool = False
    expected_endpoint_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...] = ()
    covered_endpoint_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...] = ()
    residual_rows: Tuple[UniversalKResidualFaithfulnessRow, ...] = ()

    @property
    def family_coverage_exact(self) -> bool:
        return self.family_ledgers_known and set(
            self.active_endpoint_families
        ) == set(self.covered_endpoint_families)

    @property
    def duplicate_active_endpoint_families(self) -> Tuple[str, ...]:
        return _duplicate_values(self.active_endpoint_families)

    @property
    def duplicate_covered_endpoint_families(self) -> Tuple[str, ...]:
        return _duplicate_values(self.covered_endpoint_families)

    @property
    def invalid_active_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.active_endpoint_families
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def invalid_covered_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.covered_endpoint_families
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def family_ledgers_known(self) -> bool:
        return (
            not self.invalid_active_endpoint_families
            and not self.invalid_covered_endpoint_families
        )

    @property
    def family_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_active_endpoint_families
            and not self.duplicate_covered_endpoint_families
        )

    @property
    def expected_endpoint_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(sorted(set(self.expected_endpoint_seed_states), key=repr))

    @property
    def covered_endpoint_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(sorted(set(self.covered_endpoint_seed_states), key=repr))

    @property
    def seed_state_coverage_exact(self) -> bool:
        return self.seed_state_ledgers_well_formed and set(
            self.expected_endpoint_seed_states_exact
        ) == set(self.covered_endpoint_seed_states_exact)

    @property
    def duplicate_expected_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.expected_endpoint_seed_states)

    @property
    def duplicate_covered_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.covered_endpoint_seed_states)

    @property
    def malformed_expected_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    state
                    for state in self.expected_endpoint_seed_states
                    if not _universal_k_endpoint_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def malformed_covered_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    state
                    for state in self.covered_endpoint_seed_states
                    if not _universal_k_endpoint_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def seed_state_ledgers_well_formed(self) -> bool:
        return (
            not self.malformed_expected_endpoint_seed_states
            and not self.malformed_covered_endpoint_seed_states
        )

    @property
    def seed_state_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_endpoint_seed_states
            and not self.duplicate_covered_endpoint_seed_states
        )

    @property
    def seed_state_families_match_active(self) -> bool:
        return self.seed_state_ledgers_well_formed and set(
            self.active_endpoint_families
        ) == {
            state[0]
            for state in self.expected_endpoint_seed_states_exact
            if _universal_k_endpoint_seed_state_well_formed(state)
        }

    @property
    def residual_row_count_supplied(self) -> bool:
        return self.expected_residual_row_count is not None

    @property
    def residual_row_counts_well_formed(self) -> bool:
        return (
            _universal_k_nonnegative_int(self.expected_residual_row_count)
            and _universal_k_nonnegative_int(self.covered_residual_row_count)
        )

    @property
    def malformed_residual_row_counts(self) -> Tuple[Tuple[str, object], ...]:
        malformed = []
        if (
            self.expected_residual_row_count is not None
            and not _universal_k_nonnegative_int(self.expected_residual_row_count)
        ):
            malformed.append(
                ("expected_residual_row_count", self.expected_residual_row_count)
            )
        if not _universal_k_nonnegative_int(self.covered_residual_row_count):
            malformed.append(
                ("covered_residual_row_count", self.covered_residual_row_count)
            )
        return tuple(malformed)

    @property
    def residual_row_coverage_exact(self) -> bool:
        return (
            self.residual_row_counts_well_formed
            and self.covered_residual_row_count == self.expected_residual_row_count
        )

    @property
    def residual_input_tuple_domain_supplied(self) -> bool:
        return bool(self.expected_residual_input_tuples)

    @property
    def duplicate_expected_residual_input_tuples(
        self,
    ) -> Tuple[Tuple[object, ...], ...]:
        return _duplicate_values(self.expected_residual_input_tuples)

    @property
    def duplicate_covered_residual_input_tuples(
        self,
    ) -> Tuple[Tuple[object, ...], ...]:
        return _duplicate_values(self.covered_residual_input_tuples)

    @property
    def missing_residual_input_tuples(self) -> Tuple[Tuple[object, ...], ...]:
        covered = set(self.covered_residual_input_tuples)
        return tuple(
            input_tuple
            for input_tuple in self.expected_residual_input_tuples
            if input_tuple not in covered
        )

    @property
    def extra_residual_input_tuples(self) -> Tuple[Tuple[object, ...], ...]:
        expected = set(self.expected_residual_input_tuples)
        return tuple(
            input_tuple
            for input_tuple in self.covered_residual_input_tuples
            if input_tuple not in expected
        )

    @property
    def residual_input_tuple_domain_exact(self) -> bool:
        return (
            self.residual_input_tuple_domain_supplied
            and not self.duplicate_expected_residual_input_tuples
            and not self.duplicate_covered_residual_input_tuples
            and not self.missing_residual_input_tuples
            and not self.extra_residual_input_tuples
        )

    @property
    def residual_row_input_tuples(self) -> Tuple[Tuple[object, ...], ...]:
        return tuple(row.input_tuple for row in self.residual_rows)

    @property
    def duplicate_residual_row_input_tuples(self) -> Tuple[Tuple[object, ...], ...]:
        return _duplicate_values(self.residual_row_input_tuples)

    @property
    def missing_residual_rows_for_input_tuples(
        self,
    ) -> Tuple[Tuple[object, ...], ...]:
        row_inputs = set(self.residual_row_input_tuples)
        return tuple(
            input_tuple
            for input_tuple in self.expected_residual_input_tuples
            if input_tuple not in row_inputs
        )

    @property
    def extra_residual_rows_for_input_tuples(
        self,
    ) -> Tuple[Tuple[object, ...], ...]:
        expected = set(self.expected_residual_input_tuples)
        return tuple(
            input_tuple
            for input_tuple in self.residual_row_input_tuples
            if input_tuple not in expected
        )

    @property
    def invalid_residual_rows(
        self,
    ) -> Tuple[UniversalKResidualFaithfulnessRow, ...]:
        active = set(self.active_endpoint_families)
        seeds = set(self.expected_endpoint_seed_states_exact)
        return tuple(
            row
            for row in self.residual_rows
            if (
                not row.row_scope_valid
                or not set(row.endpoint_families) <= active
                or not set(row.endpoint_seed_states) <= seeds
            )
        )

    @property
    def malformed_residual_row_endpoint_channel_keys(
        self,
    ) -> Tuple[Tuple[Tuple[object, ...], Tuple[object, ...]], ...]:
        return tuple(
            (row.input_tuple, row.malformed_endpoint_channel_keys)
            for row in self.residual_rows
            if row.malformed_endpoint_channel_keys
        )

    @property
    def residual_row_endpoint_channel_seed_mismatches(
        self,
    ) -> Tuple[
        Tuple[
            Tuple[object, ...],
            Tuple[Tuple[str, UniversalKSeedState], ...],
            Tuple[Tuple[str, UniversalKSeedState], ...],
        ],
        ...,
    ]:
        return tuple(
            (
                row.input_tuple,
                row.endpoint_channel_key_seed_states,
                row.endpoint_seed_states,
            )
            for row in self.residual_rows
            if (
                not row.malformed_endpoint_channel_keys
                and not row.endpoint_channel_keys_match_seed_states
            )
        )

    @property
    def residual_rows_cover_input_domain(self) -> bool:
        return (
            bool(self.residual_rows)
            and not self.duplicate_residual_row_input_tuples
            and not self.missing_residual_rows_for_input_tuples
            and not self.extra_residual_rows_for_input_tuples
        )

    @property
    def residual_rows_have_valid_scope(self) -> bool:
        return not self.invalid_residual_rows

    @property
    def residual_rows_cover_endpoint_seed_states(self) -> bool:
        row_seed_states = {
            seed_state
            for row in self.residual_rows
            for seed_state in row.endpoint_seed_states
        }
        return row_seed_states == set(self.expected_endpoint_seed_states_exact)

    @property
    def residual_rows_cover_endpoint_families(self) -> bool:
        row_families = {
            family for row in self.residual_rows for family in row.endpoint_families
        }
        return row_families == set(self.active_endpoint_families)

    @property
    def residual_rows_identity_endpoint_data_fixes_all(self) -> bool:
        return bool(self.residual_rows) and all(
            row.identity_endpoint_data_fixes_row for row in self.residual_rows
        )

    @property
    def endpoint_channels_exact_proved(self) -> bool:
        return (
            self.family_coverage_exact
            and self.seed_state_coverage_exact
            and self.residual_rows_cover_endpoint_families
            and self.residual_rows_cover_endpoint_seed_states
        )

    @property
    def identity_endpoint_data_forces_residual_identity_proved(self) -> bool:
        return (
            self.residual_rows_cover_input_domain
            and self.residual_rows_have_valid_scope
            and self.residual_rows_identity_endpoint_data_fixes_all
        )

    @property
    def braid_index_independence_proved(self) -> bool:
        return self.residual_rows_have_valid_scope

    @property
    def product_families_separated_proved(self) -> bool:
        return (
            self.residual_family_row_coverage_exact
            and (
                len(set(self.active_endpoint_families)) <= 1
                or bool(self.expected_residual_rows_by_family)
            )
        )

    @property
    def residual_family_row_counts_required(self) -> bool:
        return len(set(self.active_endpoint_families)) > 1

    @property
    def expected_residual_family_row_count_rows(
        self,
    ) -> Tuple[Tuple[object, object], ...]:
        return tuple(
            parts
            for row in self.expected_residual_rows_by_family
            for parts in (_universal_k_two_field_row_parts(row),)
            if parts is not None
        )

    @property
    def covered_residual_family_row_count_rows(
        self,
    ) -> Tuple[Tuple[object, object], ...]:
        return tuple(
            parts
            for row in self.covered_residual_rows_by_family
            for parts in (_universal_k_two_field_row_parts(row),)
            if parts is not None
        )

    @property
    def malformed_residual_family_row_count_rows(
        self,
    ) -> Tuple[Tuple[str, object], ...]:
        malformed = []
        seen = set()
        for ledger_name, rows in (
            ("expected", self.expected_residual_rows_by_family),
            ("covered", self.covered_residual_rows_by_family),
        ):
            for row in rows:
                if _universal_k_two_field_row_parts(row) is not None:
                    continue
                value = (ledger_name, row)
                marker = repr(value)
                if marker in seen:
                    continue
                seen.add(marker)
                malformed.append(value)
        return tuple(sorted(malformed, key=repr))

    @property
    def residual_family_row_count_rows_well_formed(self) -> bool:
        return not self.malformed_residual_family_row_count_rows

    @property
    def duplicate_expected_residual_row_families(self) -> Tuple[str, ...]:
        return _duplicate_values(
            tuple(family for family, _count in self.expected_residual_family_row_count_rows)
        )

    @property
    def duplicate_covered_residual_row_families(self) -> Tuple[str, ...]:
        return _duplicate_values(
            tuple(family for family, _count in self.covered_residual_family_row_count_rows)
        )

    @property
    def residual_family_row_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_residual_row_families
            and not self.duplicate_covered_residual_row_families
        )

    @property
    def residual_family_row_families_exact(self) -> bool:
        if (
            not self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
            and not self.covered_residual_rows_by_family
        ):
            return True
        return (
            {family for family, _count in self.expected_residual_family_row_count_rows}
            == set(self.active_endpoint_families)
            and {family for family, _count in self.covered_residual_family_row_count_rows}
            == set(self.covered_endpoint_families)
        )

    @property
    def residual_family_row_counts_nonnegative(self) -> bool:
        return all(
            _universal_k_nonnegative_int(count)
            for _family, count in (
                self.expected_residual_family_row_count_rows
                + self.covered_residual_family_row_count_rows
            )
        )

    @property
    def malformed_residual_family_row_counts(
        self,
    ) -> Tuple[Tuple[str, str, object], ...]:
        malformed = []
        seen = set()
        for ledger_name, rows in (
            ("expected", self.expected_residual_family_row_count_rows),
            ("covered", self.covered_residual_family_row_count_rows),
        ):
            for family, count in rows:
                if _universal_k_nonnegative_int(count):
                    continue
                value = (ledger_name, family, count)
                marker = repr(value)
                if marker in seen:
                    continue
                seen.add(marker)
                malformed.append(value)
        return tuple(sorted(malformed, key=repr))

    @property
    def residual_family_row_counts_match(self) -> bool:
        if (
            not self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
            and not self.covered_residual_rows_by_family
        ):
            return True
        return dict(self.expected_residual_family_row_count_rows) == dict(
            self.covered_residual_family_row_count_rows
        )

    @property
    def residual_family_row_count_sums_match(self) -> bool:
        if (
            not self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
            and not self.covered_residual_rows_by_family
        ):
            return True
        if self.expected_residual_row_count is None:
            return False
        if (
            not self.residual_row_counts_well_formed
            or not self.residual_family_row_counts_nonnegative
        ):
            return False
        return (
            sum(
                count
                for _family, count in self.expected_residual_family_row_count_rows
            )
            == self.expected_residual_row_count
            and sum(
                count
                for _family, count in self.covered_residual_family_row_count_rows
            )
            == self.covered_residual_row_count
        )

    @property
    def actual_residual_rows_by_family(self) -> Tuple[Tuple[str, int], ...]:
        return tuple(
            sorted(
                (
                    family,
                    sum(
                        1
                        for row in self.residual_rows
                        if family in set(row.endpoint_families)
                    ),
                )
                for family in set(self.active_endpoint_families)
            )
        )

    @property
    def residual_family_row_counts_match_rows(self) -> bool:
        if (
            not self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
            and not self.covered_residual_rows_by_family
        ):
            return True
        if not self.residual_family_row_counts_nonnegative:
            return False
        return (
            dict(self.expected_residual_family_row_count_rows)
            == dict(self.actual_residual_rows_by_family)
            and dict(self.covered_residual_family_row_count_rows)
            == dict(self.actual_residual_rows_by_family)
        )

    @property
    def residual_family_row_coverage_exact(self) -> bool:
        return (
            self.residual_family_row_ledgers_have_no_duplicates
            and self.residual_family_row_count_rows_well_formed
            and self.residual_family_row_families_exact
            and self.residual_family_row_counts_nonnegative
            and self.residual_family_row_counts_match
            and self.residual_family_row_count_sums_match
            and self.residual_family_row_counts_match_rows
        )

    @property
    def proves_residual_faithfulness(self) -> bool:
        return (
            self.family_coverage_exact
            and self.family_ledgers_known
            and self.family_ledgers_have_no_duplicates
            and self.seed_state_ledgers_well_formed
            and self.seed_state_coverage_exact
            and self.seed_state_ledgers_have_no_duplicates
            and self.seed_state_families_match_active
            and self.residual_row_coverage_exact
            and self.residual_input_tuple_domain_exact
            and self.residual_rows_cover_input_domain
            and self.residual_rows_have_valid_scope
            and self.residual_family_row_coverage_exact
            and self.endpoint_channels_exact_proved
            and self.identity_endpoint_data_forces_residual_identity_proved
            and self.braid_index_independence_proved
            and self.product_families_separated_proved
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.family_coverage_exact:
            reasons.append("residual_faithfulness_family_coverage_not_exact")
        if not self.family_ledgers_known:
            reasons.append("residual_faithfulness_unknown_endpoint_families")
        if not self.family_ledgers_have_no_duplicates:
            reasons.append("residual_faithfulness_duplicate_families")
        if not self.seed_state_coverage_exact:
            reasons.append("residual_faithfulness_seed_state_coverage_not_exact")
        if not self.seed_state_ledgers_well_formed:
            reasons.append("residual_faithfulness_malformed_seed_states")
        if not self.seed_state_ledgers_have_no_duplicates:
            reasons.append("residual_faithfulness_duplicate_seed_states")
        if not self.seed_state_families_match_active:
            reasons.append("residual_faithfulness_seed_state_families_mismatch")
        if not self.residual_row_count_supplied:
            reasons.append("residual_faithfulness_expected_row_count_missing")
        elif not self.residual_row_counts_well_formed:
            reasons.append("residual_faithfulness_row_count_malformed")
        elif not self.residual_row_coverage_exact:
            reasons.append("residual_faithfulness_row_coverage_not_exact")
        if not self.residual_input_tuple_domain_supplied:
            reasons.append("residual_faithfulness_input_tuple_domain_missing")
        elif not self.residual_input_tuple_domain_exact:
            reasons.append("residual_faithfulness_input_tuple_domain_not_exact")
        if not self.residual_rows:
            reasons.append("residual_faithfulness_rows_missing")
        if not self.residual_rows_cover_input_domain:
            reasons.append("residual_faithfulness_rows_do_not_cover_input_domain")
        if self.duplicate_residual_row_input_tuples:
            reasons.append("residual_faithfulness_duplicate_row_input_tuples")
        if self.missing_residual_rows_for_input_tuples:
            reasons.append("residual_faithfulness_missing_rows_for_input_tuples")
        if self.extra_residual_rows_for_input_tuples:
            reasons.append("residual_faithfulness_extra_rows_for_input_tuples")
        if not self.residual_rows_have_valid_scope:
            reasons.append("residual_faithfulness_invalid_rows")
        if self.malformed_residual_row_endpoint_channel_keys:
            reasons.append("residual_faithfulness_malformed_endpoint_channel_keys")
        if self.residual_row_endpoint_channel_seed_mismatches:
            reasons.append("residual_faithfulness_endpoint_channel_seed_mismatch")
        if not self.residual_rows_cover_endpoint_families:
            reasons.append("residual_faithfulness_rows_do_not_cover_families")
        if not self.residual_rows_cover_endpoint_seed_states:
            reasons.append("residual_faithfulness_rows_do_not_cover_seed_states")
        if (
            self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
        ):
            reasons.append("residual_faithfulness_family_row_counts_missing")
        if self.malformed_residual_family_row_count_rows:
            reasons.append("residual_faithfulness_family_row_count_malformed_rows")
        if not self.residual_family_row_ledgers_have_no_duplicates:
            reasons.append("residual_faithfulness_duplicate_family_row_counts")
        if not self.residual_family_row_families_exact:
            reasons.append("residual_faithfulness_family_row_count_scope_mismatch")
        if not self.residual_family_row_counts_nonnegative:
            reasons.append("residual_faithfulness_family_row_count_negative")
        if self.malformed_residual_family_row_counts:
            reasons.append("residual_faithfulness_family_row_count_malformed")
        if not self.residual_family_row_counts_match:
            reasons.append("residual_faithfulness_family_row_counts_mismatch")
        if not self.residual_family_row_count_sums_match:
            reasons.append("residual_faithfulness_family_row_count_sum_mismatch")
        if not self.residual_family_row_counts_match_rows:
            reasons.append(
                "residual_faithfulness_family_row_counts_do_not_match_rows"
            )
        if not self.endpoint_channels_exact_proved:
            reasons.append("residual_faithfulness_endpoint_channels_not_exact")
        if not self.identity_endpoint_data_forces_residual_identity_proved:
            reasons.append("residual_faithfulness_implication_not_proved")
        if not self.braid_index_independence_proved:
            reasons.append("residual_faithfulness_not_braid_index_independent")
        if not self.product_families_separated_proved:
            reasons.append("residual_faithfulness_product_families_not_separated")
        return tuple(reasons)


@dataclass(frozen=True)
class UniversalKResidualActionScopeAudit:
    """Scope data for explicit residual-action row certificates."""

    active_endpoint_families: Tuple[str, ...]
    covered_endpoint_families: Tuple[str, ...]
    expected_residual_row_count: int | None
    covered_residual_row_count: int
    expected_residual_rows_by_family: Tuple[Tuple[str, int], ...] = ()
    covered_residual_rows_by_family: Tuple[Tuple[str, int], ...] = ()
    endpoint_channels_exact: bool = False
    braid_index_independent: bool = False
    product_families_separated: bool = False
    expected_endpoint_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...] = ()
    covered_endpoint_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...] = ()
    scope_dependencies: Tuple[str, ...] = ()

    @property
    def family_coverage_exact(self) -> bool:
        return self.family_ledgers_known and set(
            self.active_endpoint_families
        ) == set(self.covered_endpoint_families)

    @property
    def duplicate_active_endpoint_families(self) -> Tuple[str, ...]:
        return _duplicate_values(self.active_endpoint_families)

    @property
    def duplicate_covered_endpoint_families(self) -> Tuple[str, ...]:
        return _duplicate_values(self.covered_endpoint_families)

    @property
    def invalid_active_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.active_endpoint_families
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def invalid_covered_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.covered_endpoint_families
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def family_ledgers_known(self) -> bool:
        return (
            not self.invalid_active_endpoint_families
            and not self.invalid_covered_endpoint_families
        )

    @property
    def family_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_active_endpoint_families
            and not self.duplicate_covered_endpoint_families
        )

    @property
    def expected_endpoint_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(sorted(set(self.expected_endpoint_seed_states), key=repr))

    @property
    def covered_endpoint_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(sorted(set(self.covered_endpoint_seed_states), key=repr))

    @property
    def seed_state_coverage_exact(self) -> bool:
        return self.seed_state_ledgers_well_formed and set(
            self.expected_endpoint_seed_states_exact
        ) == set(self.covered_endpoint_seed_states_exact)

    @property
    def duplicate_expected_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.expected_endpoint_seed_states)

    @property
    def duplicate_covered_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.covered_endpoint_seed_states)

    @property
    def malformed_expected_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    state
                    for state in self.expected_endpoint_seed_states
                    if not _universal_k_endpoint_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def malformed_covered_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    state
                    for state in self.covered_endpoint_seed_states
                    if not _universal_k_endpoint_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def seed_state_ledgers_well_formed(self) -> bool:
        return (
            not self.malformed_expected_endpoint_seed_states
            and not self.malformed_covered_endpoint_seed_states
        )

    @property
    def seed_state_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_endpoint_seed_states
            and not self.duplicate_covered_endpoint_seed_states
        )

    @property
    def seed_state_families_match_active(self) -> bool:
        return self.seed_state_ledgers_well_formed and set(
            self.active_endpoint_families
        ) == {
            state[0]
            for state in self.expected_endpoint_seed_states_exact
            if _universal_k_endpoint_seed_state_well_formed(state)
        }

    @property
    def residual_row_count_supplied(self) -> bool:
        return self.expected_residual_row_count is not None

    @property
    def residual_row_counts_well_formed(self) -> bool:
        return (
            _universal_k_nonnegative_int(self.expected_residual_row_count)
            and _universal_k_nonnegative_int(self.covered_residual_row_count)
        )

    @property
    def malformed_residual_row_counts(self) -> Tuple[Tuple[str, object], ...]:
        malformed = []
        if (
            self.expected_residual_row_count is not None
            and not _universal_k_nonnegative_int(self.expected_residual_row_count)
        ):
            malformed.append(
                ("expected_residual_row_count", self.expected_residual_row_count)
            )
        if not _universal_k_nonnegative_int(self.covered_residual_row_count):
            malformed.append(
                ("covered_residual_row_count", self.covered_residual_row_count)
            )
        return tuple(malformed)

    @property
    def residual_row_coverage_exact(self) -> bool:
        return (
            self.residual_row_counts_well_formed
            and self.covered_residual_row_count == self.expected_residual_row_count
        )

    @property
    def residual_family_row_counts_required(self) -> bool:
        return len(set(self.active_endpoint_families)) > 1

    @property
    def expected_residual_family_row_count_rows(
        self,
    ) -> Tuple[Tuple[object, object], ...]:
        return tuple(
            parts
            for row in self.expected_residual_rows_by_family
            for parts in (_universal_k_two_field_row_parts(row),)
            if parts is not None
        )

    @property
    def covered_residual_family_row_count_rows(
        self,
    ) -> Tuple[Tuple[object, object], ...]:
        return tuple(
            parts
            for row in self.covered_residual_rows_by_family
            for parts in (_universal_k_two_field_row_parts(row),)
            if parts is not None
        )

    @property
    def malformed_residual_family_row_count_rows(
        self,
    ) -> Tuple[Tuple[str, object], ...]:
        malformed = []
        seen = set()
        for ledger_name, rows in (
            ("expected", self.expected_residual_rows_by_family),
            ("covered", self.covered_residual_rows_by_family),
        ):
            for row in rows:
                if _universal_k_two_field_row_parts(row) is not None:
                    continue
                value = (ledger_name, row)
                marker = repr(value)
                if marker in seen:
                    continue
                seen.add(marker)
                malformed.append(value)
        return tuple(sorted(malformed, key=repr))

    @property
    def residual_family_row_count_rows_well_formed(self) -> bool:
        return not self.malformed_residual_family_row_count_rows

    @property
    def duplicate_expected_residual_row_families(self) -> Tuple[str, ...]:
        return _duplicate_values(
            tuple(family for family, _count in self.expected_residual_family_row_count_rows)
        )

    @property
    def duplicate_covered_residual_row_families(self) -> Tuple[str, ...]:
        return _duplicate_values(
            tuple(family for family, _count in self.covered_residual_family_row_count_rows)
        )

    @property
    def residual_family_row_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_residual_row_families
            and not self.duplicate_covered_residual_row_families
        )

    @property
    def residual_family_row_families_exact(self) -> bool:
        if (
            not self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
            and not self.covered_residual_rows_by_family
        ):
            return True
        return (
            {family for family, _count in self.expected_residual_family_row_count_rows}
            == set(self.active_endpoint_families)
            and {family for family, _count in self.covered_residual_family_row_count_rows}
            == set(self.covered_endpoint_families)
        )

    @property
    def residual_family_row_counts_nonnegative(self) -> bool:
        return all(
            _universal_k_nonnegative_int(count)
            for _family, count in (
                self.expected_residual_family_row_count_rows
                + self.covered_residual_family_row_count_rows
            )
        )

    @property
    def malformed_residual_family_row_counts(
        self,
    ) -> Tuple[Tuple[str, str, object], ...]:
        malformed = []
        seen = set()
        for ledger_name, rows in (
            ("expected", self.expected_residual_family_row_count_rows),
            ("covered", self.covered_residual_family_row_count_rows),
        ):
            for family, count in rows:
                if _universal_k_nonnegative_int(count):
                    continue
                value = (ledger_name, family, count)
                marker = repr(value)
                if marker in seen:
                    continue
                seen.add(marker)
                malformed.append(value)
        return tuple(sorted(malformed, key=repr))

    @property
    def residual_family_row_counts_cover_active_families(self) -> bool:
        if (
            not self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
            and not self.covered_residual_rows_by_family
        ):
            return True
        if not self.residual_family_row_counts_nonnegative:
            return False
        expected_counts = dict(self.expected_residual_family_row_count_rows)
        covered_counts = dict(self.covered_residual_family_row_count_rows)
        return all(
            expected_counts.get(family, 0) > 0
            for family in self.active_endpoint_families
        ) and all(
            covered_counts.get(family, 0) > 0
            for family in self.covered_endpoint_families
        )

    @property
    def residual_family_row_counts_match(self) -> bool:
        if (
            not self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
            and not self.covered_residual_rows_by_family
        ):
            return True
        return dict(self.expected_residual_family_row_count_rows) == dict(
            self.covered_residual_family_row_count_rows
        )

    @property
    def residual_family_row_count_sums_match(self) -> bool:
        if (
            not self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
            and not self.covered_residual_rows_by_family
        ):
            return True
        if self.expected_residual_row_count is None:
            return False
        if (
            not self.residual_row_counts_well_formed
            or not self.residual_family_row_counts_nonnegative
        ):
            return False
        return (
            sum(
                count
                for _family, count in self.expected_residual_family_row_count_rows
            )
            == self.expected_residual_row_count
            and sum(
                count
                for _family, count in self.covered_residual_family_row_count_rows
            )
            == self.covered_residual_row_count
        )

    @property
    def residual_family_row_coverage_exact(self) -> bool:
        return (
            self.residual_family_row_ledgers_have_no_duplicates
            and self.residual_family_row_count_rows_well_formed
            and self.residual_family_row_families_exact
            and self.residual_family_row_counts_nonnegative
            and self.residual_family_row_counts_cover_active_families
            and self.residual_family_row_counts_match
            and self.residual_family_row_count_sums_match
        )

    @property
    def duplicate_scope_dependencies(self) -> Tuple[str, ...]:
        return _duplicate_values(self.scope_dependencies)

    @property
    def forbidden_scope_dependencies(self) -> Tuple[str, ...]:
        forbidden = _UNIVERSAL_K_RESIDUAL_FORBIDDEN_DEPENDENCIES
        return tuple(dependency for dependency in self.scope_dependencies if dependency in forbidden)

    @property
    def unknown_scope_dependencies(self) -> Tuple[str, ...]:
        allowed = _UNIVERSAL_K_RESIDUAL_ALLOWED_DEPENDENCIES
        return tuple(dependency for dependency in self.scope_dependencies if dependency not in allowed)

    @property
    def scope_dependencies_valid(self) -> bool:
        return (
            bool(self.scope_dependencies)
            and not self.duplicate_scope_dependencies
            and not self.forbidden_scope_dependencies
            and not self.unknown_scope_dependencies
        )

    @property
    def endpoint_channels_exact_proved(self) -> bool:
        return (
            self.family_coverage_exact
            and self.seed_state_coverage_exact
            and self.seed_state_families_match_active
        )

    @property
    def braid_index_independence_proved(self) -> bool:
        return self.scope_dependencies_valid

    @property
    def product_families_separated_proved(self) -> bool:
        return (
            self.residual_family_row_coverage_exact
            and (
                len(set(self.active_endpoint_families)) <= 1
                or bool(self.expected_residual_rows_by_family)
            )
        )

    @property
    def proves_residual_action_scope(self) -> bool:
        return (
            self.family_coverage_exact
            and self.family_ledgers_known
            and self.family_ledgers_have_no_duplicates
            and self.seed_state_ledgers_well_formed
            and self.seed_state_coverage_exact
            and self.seed_state_ledgers_have_no_duplicates
            and self.seed_state_families_match_active
            and self.residual_row_coverage_exact
            and self.residual_family_row_coverage_exact
            and self.endpoint_channels_exact_proved
            and self.braid_index_independence_proved
            and self.product_families_separated_proved
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.family_coverage_exact:
            reasons.append("residual_action_scope_family_coverage_not_exact")
        if not self.family_ledgers_known:
            reasons.append("residual_action_scope_unknown_endpoint_families")
        if not self.family_ledgers_have_no_duplicates:
            reasons.append("residual_action_scope_duplicate_families")
        if not self.seed_state_coverage_exact:
            reasons.append("residual_action_scope_seed_state_coverage_not_exact")
        if not self.seed_state_ledgers_well_formed:
            reasons.append("residual_action_scope_malformed_seed_states")
        if not self.seed_state_ledgers_have_no_duplicates:
            reasons.append("residual_action_scope_duplicate_seed_states")
        if not self.seed_state_families_match_active:
            reasons.append("residual_action_scope_seed_state_families_mismatch")
        if not self.residual_row_count_supplied:
            reasons.append("residual_action_scope_expected_row_count_missing")
        elif not self.residual_row_counts_well_formed:
            reasons.append("residual_action_scope_row_count_malformed")
        elif not self.residual_row_coverage_exact:
            reasons.append("residual_action_scope_row_coverage_not_exact")
        if (
            self.residual_family_row_counts_required
            and not self.expected_residual_rows_by_family
        ):
            reasons.append("residual_action_scope_family_row_counts_missing")
        if self.malformed_residual_family_row_count_rows:
            reasons.append("residual_action_scope_family_row_count_malformed_rows")
        if not self.residual_family_row_ledgers_have_no_duplicates:
            reasons.append("residual_action_scope_duplicate_family_row_counts")
        if not self.residual_family_row_families_exact:
            reasons.append("residual_action_scope_family_row_count_scope_mismatch")
        if not self.residual_family_row_counts_nonnegative:
            reasons.append("residual_action_scope_family_row_count_negative")
        if self.malformed_residual_family_row_counts:
            reasons.append("residual_action_scope_family_row_count_malformed")
        if not self.residual_family_row_counts_cover_active_families:
            reasons.append(
                "residual_action_scope_family_row_counts_do_not_cover_active_families"
            )
        if not self.residual_family_row_counts_match:
            reasons.append("residual_action_scope_family_row_counts_mismatch")
        if not self.residual_family_row_count_sums_match:
            reasons.append("residual_action_scope_family_row_count_sum_mismatch")
        if not self.endpoint_channels_exact_proved:
            reasons.append("residual_action_scope_endpoint_channels_not_exact")
        if not self.scope_dependencies_valid:
            reasons.append("residual_action_scope_invalid_dependencies")
        if self.duplicate_scope_dependencies:
            reasons.append("residual_action_scope_duplicate_dependencies")
        if self.forbidden_scope_dependencies:
            reasons.append("residual_action_scope_forbidden_dependencies")
        if self.unknown_scope_dependencies:
            reasons.append("residual_action_scope_unknown_dependencies")
        if not self.braid_index_independence_proved:
            reasons.append("residual_action_scope_not_braid_index_independent")
        if not self.product_families_separated_proved:
            reasons.append("residual_action_scope_product_families_not_separated")
        return tuple(reasons)


@dataclass(frozen=True)
class UniversalKCutoffReadoutRow:
    """One finite symmetric cutoff readout for a routed C/M seed state."""

    cutoff_seed_state: Tuple[str, UniversalKSeedState]
    readout_permutation: Tuple[int, ...]
    killed_readout_permutation: Tuple[int, ...]

    def readout_is_permutation(self, degree: int) -> bool:
        return _universal_k_permutation_tuple(self.readout_permutation, degree)

    def killed_readout_is_permutation(self, degree: int) -> bool:
        return (
            _universal_k_permutation_tuple(
                self.killed_readout_permutation,
                degree,
            )
        )

    def identity_data_kills_channel(self, degree: int) -> bool:
        return self.killed_readout_is_permutation(
            degree
        ) and self.killed_readout_permutation == tuple(range(degree))


@dataclass(frozen=True)
class UniversalKCutoffReadoutAudit:
    """Exact C/M symmetric-cutoff readout coverage for routed K seeds."""

    expected_cutoff_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...]
    covered_cutoff_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...]
    cutoff_degree: int | None = None
    readout_rows: Tuple[UniversalKCutoffReadoutRow, ...] = ()
    readouts_faithful: bool = False
    identity_cutoff_data_kills_channels: bool = False
    braid_index_independent: bool = False

    @property
    def expected_cutoff_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(sorted(set(self.expected_cutoff_seed_states), key=repr))

    @property
    def covered_cutoff_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(sorted(set(self.covered_cutoff_seed_states), key=repr))

    @property
    def duplicate_expected_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.expected_cutoff_seed_states)

    @property
    def duplicate_covered_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.covered_cutoff_seed_states)

    @property
    def malformed_expected_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    state
                    for state in self.expected_cutoff_seed_states
                    if not _universal_k_cutoff_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def malformed_covered_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    state
                    for state in self.covered_cutoff_seed_states
                    if not _universal_k_cutoff_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def cutoff_seed_ledgers_well_formed(self) -> bool:
        return (
            not self.malformed_expected_cutoff_seed_states
            and not self.malformed_covered_cutoff_seed_states
        )

    @property
    def cutoff_seed_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_cutoff_seed_states
            and not self.duplicate_covered_cutoff_seed_states
        )

    @property
    def missing_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        covered = set(self.covered_cutoff_seed_states_exact)
        return tuple(
            state
            for state in self.expected_cutoff_seed_states_exact
            if state not in covered
        )

    @property
    def extra_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        expected = set(self.expected_cutoff_seed_states_exact)
        return tuple(
            state
            for state in self.covered_cutoff_seed_states_exact
            if state not in expected
        )

    @property
    def cutoff_seed_coverage_exact(self) -> bool:
        return (
            bool(self.expected_cutoff_seed_states_exact)
            and self.cutoff_seed_ledgers_well_formed
            and not self.missing_cutoff_seed_states
            and not self.extra_cutoff_seed_states
        )

    @property
    def expected_cutoff_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    state[0]
                    for state in self.expected_cutoff_seed_states
                    if _universal_k_cutoff_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def covered_cutoff_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    state[0]
                    for state in self.covered_cutoff_seed_states
                    if _universal_k_cutoff_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def row_cutoff_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    state[0]
                    for state in self.row_cutoff_seed_states
                    if _universal_k_cutoff_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def missing_cutoff_families(self) -> Tuple[str, ...]:
        covered = set(self.covered_cutoff_families)
        return tuple(
            family for family in self.expected_cutoff_families if family not in covered
        )

    @property
    def extra_cutoff_families(self) -> Tuple[str, ...]:
        expected = set(self.expected_cutoff_families)
        return tuple(
            family for family in self.covered_cutoff_families if family not in expected
        )

    @property
    def missing_readout_row_families(self) -> Tuple[str, ...]:
        row_families = set(self.row_cutoff_families)
        return tuple(
            family for family in self.expected_cutoff_families if family not in row_families
        )

    @property
    def extra_readout_row_families(self) -> Tuple[str, ...]:
        expected = set(self.expected_cutoff_families)
        return tuple(
            family for family in self.row_cutoff_families if family not in expected
        )

    @property
    def cutoff_family_scope_exact(self) -> bool:
        return (
            bool(self.expected_cutoff_families)
            and not self.missing_cutoff_families
            and not self.extra_cutoff_families
            and not self.missing_readout_row_families
            and not self.extra_readout_row_families
        )

    @property
    def cutoff_degree_supplied(self) -> bool:
        return _universal_k_positive_int(self.cutoff_degree)

    @property
    def row_cutoff_seed_states(self) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(row.cutoff_seed_state for row in self.readout_rows)

    @property
    def row_cutoff_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(sorted(set(self.row_cutoff_seed_states), key=repr))

    @property
    def duplicate_row_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.row_cutoff_seed_states)

    @property
    def malformed_row_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {
                    state
                    for state in self.row_cutoff_seed_states
                    if not _universal_k_cutoff_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def missing_readout_row_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        row_states = set(self.row_cutoff_seed_states_exact)
        return tuple(
            state
            for state in self.expected_cutoff_seed_states_exact
            if state not in row_states
        )

    @property
    def extra_readout_row_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        expected = set(self.expected_cutoff_seed_states_exact)
        return tuple(
            state for state in self.row_cutoff_seed_states_exact if state not in expected
        )

    @property
    def readout_rows_cover_expected_states(self) -> bool:
        return (
            bool(self.readout_rows)
            and not self.duplicate_row_cutoff_seed_states
            and not self.malformed_row_cutoff_seed_states
            and not self.missing_readout_row_seed_states
            and not self.extra_readout_row_seed_states
        )

    @property
    def invalid_readout_permutation_rows(
        self,
    ) -> Tuple[Tuple[Tuple[str, UniversalKSeedState], str, object], ...]:
        if not self.cutoff_degree_supplied:
            return tuple(
                (
                    row.cutoff_seed_state,
                    "cutoff_degree_not_supplied",
                    self.cutoff_degree,
                )
                for row in self.readout_rows
            )
        failures = []
        for row in self.readout_rows:
            if not row.readout_is_permutation(self.cutoff_degree):
                failures.append(
                    (
                        row.cutoff_seed_state,
                        "readout_not_permutation",
                        row.readout_permutation,
                    )
                )
            if not row.killed_readout_is_permutation(self.cutoff_degree):
                failures.append(
                    (
                        row.cutoff_seed_state,
                        "killed_readout_not_permutation",
                        row.killed_readout_permutation,
                    )
                )
        return tuple(failures)

    @property
    def readout_permutations_valid(self) -> bool:
        return self.cutoff_degree_supplied and not self.invalid_readout_permutation_rows

    @property
    def duplicate_readout_permutations(
        self,
    ) -> Tuple[Tuple[int, ...], ...]:
        return _duplicate_values(
            tuple(row.readout_permutation for row in self.readout_rows)
        )

    @property
    def readout_rows_faithful(self) -> bool:
        return self.readout_permutations_valid and not self.duplicate_readout_permutations

    @property
    def unkilled_readout_rows(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        if not self.cutoff_degree_supplied:
            return tuple(row.cutoff_seed_state for row in self.readout_rows)
        return tuple(
            row.cutoff_seed_state
            for row in self.readout_rows
            if not row.identity_data_kills_channel(self.cutoff_degree)
        )

    @property
    def identity_cutoff_rows_kill_channels(self) -> bool:
        return self.readout_permutations_valid and not self.unkilled_readout_rows

    @property
    def finite_readout_rows_verified(self) -> bool:
        return (
            self.readout_rows_cover_expected_states
            and self.readout_rows_faithful
            and self.identity_cutoff_rows_kill_channels
        )

    @property
    def braid_index_independence_proved(self) -> bool:
        return self.cutoff_degree_supplied and self.readout_rows_cover_expected_states

    @property
    def proves_exact_cutoff_readouts(self) -> bool:
        return (
            self.cutoff_seed_coverage_exact
            and self.cutoff_family_scope_exact
            and self.cutoff_seed_ledgers_well_formed
            and self.cutoff_seed_ledgers_have_no_duplicates
            and self.finite_readout_rows_verified
            and self.braid_index_independence_proved
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.expected_cutoff_seed_states_exact:
            reasons.append("cutoff_readout_expected_states_empty")
        if self.missing_cutoff_seed_states:
            reasons.append("cutoff_readout_missing_seed_states")
        if self.extra_cutoff_seed_states:
            reasons.append("cutoff_readout_extra_seed_states")
        if not self.cutoff_seed_ledgers_well_formed:
            reasons.append("cutoff_readout_malformed_seed_states")
        if not self.cutoff_seed_ledgers_have_no_duplicates:
            reasons.append("cutoff_readout_duplicate_seed_states")
        if not self.cutoff_family_scope_exact:
            reasons.append("cutoff_readout_family_scope_mismatch")
        if self.missing_cutoff_families:
            reasons.append("cutoff_readout_missing_families")
        if self.extra_cutoff_families:
            reasons.append("cutoff_readout_extra_families")
        if self.missing_readout_row_families:
            reasons.append("cutoff_readout_missing_row_families")
        if self.extra_readout_row_families:
            reasons.append("cutoff_readout_extra_row_families")
        if not self.cutoff_degree_supplied:
            reasons.append("cutoff_degree_not_supplied")
        if not self.readout_rows_cover_expected_states:
            reasons.append("cutoff_readout_rows_do_not_cover_expected_states")
        if self.duplicate_row_cutoff_seed_states:
            reasons.append("cutoff_readout_duplicate_row_states")
        if self.missing_readout_row_seed_states:
            reasons.append("cutoff_readout_missing_row_states")
        if self.extra_readout_row_seed_states:
            reasons.append("cutoff_readout_extra_row_states")
        if self.malformed_row_cutoff_seed_states:
            reasons.append("cutoff_readout_malformed_row_states")
        if not self.readout_permutations_valid:
            reasons.append("cutoff_readout_permutations_invalid")
        if not self.readout_rows_faithful:
            reasons.append("cutoff_readouts_not_faithful")
        if self.duplicate_readout_permutations:
            reasons.append("cutoff_readout_duplicate_permutations")
        if not self.identity_cutoff_rows_kill_channels:
            reasons.append("cutoff_identity_data_does_not_kill_channels")
        if self.unkilled_readout_rows:
            reasons.append("cutoff_readout_rows_not_killed_by_identity_data")
        if not self.braid_index_independence_proved:
            reasons.append("cutoff_readouts_not_braid_index_independent")
        return tuple(reasons)


@dataclass(frozen=True)
class UniversalKEndpointTargetAudit:
    """Family-scoped finite endpoint targets for signed U/C/M tables."""

    expected_endpoint_families: Tuple[str, ...]
    covered_endpoint_families: Tuple[str, ...]
    endpoint_group_orders: Tuple[Tuple[str, int], ...] = ()
    cutoff_degrees: Tuple[Tuple[str, int], ...] = ()
    braid_index_independent: bool = False
    product_families_separated: bool = False

    @property
    def expected_endpoint_families_exact(self) -> Tuple[str, ...]:
        return tuple(sorted(set(self.expected_endpoint_families), key=repr))

    @property
    def covered_endpoint_families_exact(self) -> Tuple[str, ...]:
        return tuple(sorted(set(self.covered_endpoint_families), key=repr))

    @property
    def duplicate_expected_endpoint_families(self) -> Tuple[str, ...]:
        return _duplicate_values(self.expected_endpoint_families)

    @property
    def duplicate_covered_endpoint_families(self) -> Tuple[str, ...]:
        return _duplicate_values(self.covered_endpoint_families)

    @property
    def invalid_expected_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.expected_endpoint_families
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def invalid_covered_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.covered_endpoint_families
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def invalid_target_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.target_endpoint_families
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def family_ledgers_known(self) -> bool:
        return (
            not self.invalid_expected_endpoint_families
            and not self.invalid_covered_endpoint_families
            and not self.invalid_target_endpoint_families
        )

    @property
    def family_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_endpoint_families
            and not self.duplicate_covered_endpoint_families
        )

    @property
    def endpoint_group_order_rows(self) -> Tuple[Tuple[object, object], ...]:
        return tuple(
            parts
            for row in self.endpoint_group_orders
            for parts in (_universal_k_two_field_row_parts(row),)
            if parts is not None
        )

    @property
    def cutoff_degree_rows(self) -> Tuple[Tuple[object, object], ...]:
        return tuple(
            parts
            for row in self.cutoff_degrees
            for parts in (_universal_k_two_field_row_parts(row),)
            if parts is not None
        )

    @property
    def malformed_endpoint_group_order_rows(self) -> Tuple[object, ...]:
        return _unique_values(
            tuple(
                row
                for row in self.endpoint_group_orders
                if _universal_k_two_field_row_parts(row) is None
            )
        )

    @property
    def malformed_cutoff_degree_rows(self) -> Tuple[object, ...]:
        return _unique_values(
            tuple(
                row
                for row in self.cutoff_degrees
                if _universal_k_two_field_row_parts(row) is None
            )
        )

    @property
    def target_size_rows_well_formed(self) -> bool:
        return (
            not self.malformed_endpoint_group_order_rows
            and not self.malformed_cutoff_degree_rows
        )

    @property
    def endpoint_group_order_rows_well_formed(self) -> bool:
        return not self.malformed_endpoint_group_order_rows

    @property
    def cutoff_degree_rows_well_formed(self) -> bool:
        return not self.malformed_cutoff_degree_rows

    @property
    def target_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {family for family, _order in self.endpoint_group_order_rows}
                | {family for family, _degree in self.cutoff_degree_rows},
                key=repr,
            )
        )

    @property
    def family_coverage_exact(self) -> bool:
        return set(self.expected_endpoint_families_exact) == set(
            self.covered_endpoint_families_exact
        )

    @property
    def duplicate_target_endpoint_families(self) -> Tuple[str, ...]:
        families = tuple(
            family for family, _target_size in self.endpoint_group_order_rows + self.cutoff_degree_rows
        )
        return _duplicate_values(families)

    @property
    def missing_target_families(self) -> Tuple[str, ...]:
        targets = set(self.target_endpoint_families)
        return tuple(
            family
            for family in self.covered_endpoint_families_exact
            if family not in targets
        )

    @property
    def extra_target_families(self) -> Tuple[str, ...]:
        covered = set(self.covered_endpoint_families_exact)
        return tuple(
            family
            for family in self.target_endpoint_families
            if family not in covered
        )

    @property
    def target_orders_positive(self) -> bool:
        return self.endpoint_group_order_rows_well_formed and all(
            _universal_k_positive_int(order)
            for _family, order in self.endpoint_group_order_rows
        )

    @property
    def cutoff_degrees_positive(self) -> bool:
        return self.cutoff_degree_rows_well_formed and all(
            _universal_k_positive_int(degree)
            for _family, degree in self.cutoff_degree_rows
        )

    @property
    def malformed_endpoint_group_orders(self) -> Tuple[Tuple[object, object], ...]:
        malformed = []
        seen = set()
        for family, order in self.endpoint_group_order_rows:
            if _universal_k_positive_int(order):
                continue
            value = (family, order)
            marker = repr(value)
            if marker in seen:
                continue
            seen.add(marker)
            malformed.append(value)
        return tuple(sorted(malformed, key=repr))

    @property
    def malformed_cutoff_degrees(self) -> Tuple[Tuple[object, object], ...]:
        malformed = []
        seen = set()
        for family, degree in self.cutoff_degree_rows:
            if _universal_k_positive_int(degree):
                continue
            value = (family, degree)
            marker = repr(value)
            if marker in seen:
                continue
            seen.add(marker)
            malformed.append(value)
        return tuple(sorted(malformed, key=repr))

    @property
    def target_families_exact(self) -> bool:
        return not self.missing_target_families and not self.extra_target_families

    @property
    def target_ledgers_have_no_duplicates(self) -> bool:
        return not self.duplicate_target_endpoint_families

    @property
    def braid_index_independence_proved(self) -> bool:
        return (
            self.target_families_exact
            and self.target_orders_positive
            and self.cutoff_degrees_positive
        )

    @property
    def product_families_separated_proved(self) -> bool:
        return self.target_families_exact and self.target_ledgers_have_no_duplicates

    @property
    def proves_endpoint_targets(self) -> bool:
        return (
            self.family_coverage_exact
            and self.family_ledgers_known
            and self.family_ledgers_have_no_duplicates
            and self.target_size_rows_well_formed
            and self.target_families_exact
            and self.target_ledgers_have_no_duplicates
            and self.target_orders_positive
            and self.cutoff_degrees_positive
            and self.braid_index_independence_proved
            and self.product_families_separated_proved
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.family_coverage_exact:
            reasons.append("endpoint_target_family_coverage_not_exact")
        if not self.family_ledgers_known:
            reasons.append("endpoint_target_unknown_families")
        if not self.family_ledgers_have_no_duplicates:
            reasons.append("endpoint_target_duplicate_families")
        if self.missing_target_families:
            reasons.append("endpoint_target_missing_families")
        if self.extra_target_families:
            reasons.append("endpoint_target_extra_families")
        if not self.target_ledgers_have_no_duplicates:
            reasons.append("endpoint_target_duplicate_target_families")
        if self.malformed_endpoint_group_order_rows:
            reasons.append("endpoint_target_malformed_group_order_rows")
        if not self.target_orders_positive:
            reasons.append("endpoint_target_nonpositive_group_order")
        if self.malformed_endpoint_group_orders:
            reasons.append("endpoint_target_malformed_group_order")
        if self.malformed_cutoff_degree_rows:
            reasons.append("endpoint_target_malformed_cutoff_degree_rows")
        if not self.cutoff_degrees_positive:
            reasons.append("endpoint_target_nonpositive_cutoff_degree")
        if self.malformed_cutoff_degrees:
            reasons.append("endpoint_target_malformed_cutoff_degree")
        if not self.braid_index_independence_proved:
            reasons.append("endpoint_target_not_braid_index_independent")
        if not self.product_families_separated_proved:
            reasons.append("endpoint_target_product_families_not_separated")
        return tuple(reasons)


def universal_k_signed_endpoint_seed_states(
    seed_classifier_entries: Sequence[UniversalKSeedClassifierEntry],
) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
    """Return the initial endpoint states hit by the current kappa table."""

    return _unique_values(tuple(entry[1] for entry in seed_classifier_entries))


def universal_k_signed_endpoint_transition_closure(
    seed_classifier_entries: Sequence[UniversalKSeedClassifierEntry],
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
    """Least signed endpoint state closure generated from kappa seeds."""

    closure = list(universal_k_signed_endpoint_seed_states(seed_classifier_entries))
    closure_markers = {_value_marker(state) for state in closure}
    changed = True
    while changed:
        changed = False
        for row in rows:
            current = (row.endpoint_family, row.seed_state)
            if _value_marker(current) not in closure_markers:
                continue
            next_state = (row.endpoint_family, row.next_seed_state)
            next_marker = _value_marker(next_state)
            if next_marker not in closure_markers:
                closure.append(next_state)
                closure_markers.add(next_marker)
                changed = True
    return tuple(sorted(closure, key=repr))


@dataclass(frozen=True)
class UniversalKEndpointMonodromyPresentation:
    """Finite positive local-context presentation for a U/C/M observer.

    Contexts are the positive local crossings `(E,a,b,x,y)`.  Relations are
    stored in application order: `((r1,r2,r3),(r1',r2',r3'))` records the two
    positive adjacent paths, and `((r,r'),(r',r))` records a far-commuting
    disjoint-context pair.  A finite permutation representation of this
    presentation is exactly the endpoint-state part of a positive observer.
    """

    expected_endpoint_families: Tuple[str, ...]
    contexts: Tuple[UniversalKEndpointMonodromyContext, ...]
    adjacent_relations: Tuple[UniversalKEndpointMonodromyRelation, ...] = ()
    far_commutativity_relations: Tuple[
        UniversalKEndpointMonodromyRelation,
        ...,
    ] = ()

    @property
    def expected_endpoint_families_exact(self) -> Tuple[str, ...]:
        return _unique_values(self.expected_endpoint_families)

    @property
    def duplicate_expected_endpoint_families(self) -> Tuple[str, ...]:
        return _duplicate_values(self.expected_endpoint_families)

    @property
    def invalid_expected_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            family
            for family in self.expected_endpoint_families_exact
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @property
    def contexts_exact(self) -> Tuple[UniversalKEndpointMonodromyContext, ...]:
        return _unique_values(self.contexts)

    @property
    def duplicate_contexts(self) -> Tuple[UniversalKEndpointMonodromyContext, ...]:
        return _duplicate_values(self.contexts)

    @property
    def malformed_contexts(self) -> Tuple[UniversalKEndpointMonodromyContext, ...]:
        return _unique_values(
            tuple(context for context in self.contexts if not self._context_valid(context))
        )

    @staticmethod
    def _context_valid(context: object) -> bool:
        return (
            isinstance(context, tuple)
            and len(context) == 5
            and context[0] in UNIVERSAL_K_ENDPOINT_FAMILIES
        )

    @classmethod
    def _word_valid(cls, word: object, length: int) -> bool:
        return (
            isinstance(word, tuple)
            and len(word) == length
            and all(cls._context_valid(context) for context in word)
        )

    @property
    def context_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    context[0]
                    for context in self.contexts_exact
                    if self._context_valid(context)
                },
                key=repr,
            )
        )

    @property
    def family_scope_exact(self) -> bool:
        return set(self.context_families) == set(self.expected_endpoint_families_exact)

    @property
    def adjacent_relations_exact(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyRelation, ...]:
        return _unique_values(self.adjacent_relations)

    @property
    def far_commutativity_relations_exact(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyRelation, ...]:
        return _unique_values(self.far_commutativity_relations)

    @property
    def duplicate_adjacent_relations(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyRelation, ...]:
        return _duplicate_values(self.adjacent_relations)

    @property
    def duplicate_far_commutativity_relations(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyRelation, ...]:
        return _duplicate_values(self.far_commutativity_relations)

    @staticmethod
    def _relation_contexts(
        relation: UniversalKEndpointMonodromyRelation,
    ) -> Tuple[UniversalKEndpointMonodromyContext, ...]:
        left_word, right_word = relation
        return tuple(left_word) + tuple(right_word)

    @property
    def malformed_adjacent_relations(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyRelation, ...]:
        return _unique_values(
            tuple(
                relation
                for relation in self.adjacent_relations
                if (
                    not isinstance(relation, tuple)
                    or len(relation) != 2
                    or not self._word_valid(relation[0], 3)
                    or not self._word_valid(relation[1], 3)
                )
            )
        )

    @property
    def malformed_far_commutativity_relations(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyRelation, ...]:
        return _unique_values(
            tuple(
                relation
                for relation in self.far_commutativity_relations
                if (
                    not isinstance(relation, tuple)
                    or len(relation) != 2
                    or not self._word_valid(relation[0], 2)
                    or not self._word_valid(relation[1], 2)
                )
            )
        )

    @property
    def relation_contexts_outside_domain(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyContext, ...]:
        context_markers = {_value_marker(context) for context in self.contexts_exact}
        outside = []
        for relation in self.adjacent_relations + self.far_commutativity_relations:
            if (
                not isinstance(relation, tuple)
                or len(relation) != 2
                or not isinstance(relation[0], tuple)
                or not isinstance(relation[1], tuple)
            ):
                continue
            for context in tuple(relation[0]) + tuple(relation[1]):
                if (
                    self._context_valid(context)
                    and _value_marker(context) not in context_markers
                ):
                    outside.append(context)
        return _unique_values(tuple(outside))

    @property
    def relations_well_formed(self) -> bool:
        return (
            not self.malformed_adjacent_relations
            and not self.malformed_far_commutativity_relations
            and not self.relation_contexts_outside_domain
        )

    @property
    def presentation_is_finite(self) -> bool:
        return (
            bool(self.contexts_exact)
            and not self.duplicate_expected_endpoint_families
            and not self.invalid_expected_endpoint_families
            and not self.duplicate_contexts
            and not self.malformed_contexts
            and self.family_scope_exact
            and not self.duplicate_adjacent_relations
            and not self.duplicate_far_commutativity_relations
            and self.relations_well_formed
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.contexts_exact:
            reasons.append("endpoint_monodromy_contexts_missing")
        if self.duplicate_expected_endpoint_families:
            reasons.append("endpoint_monodromy_duplicate_families")
        if self.invalid_expected_endpoint_families:
            reasons.append("endpoint_monodromy_unknown_families")
        if self.duplicate_contexts:
            reasons.append("endpoint_monodromy_duplicate_contexts")
        if self.malformed_contexts:
            reasons.append("endpoint_monodromy_malformed_contexts")
        if not self.family_scope_exact:
            reasons.append("endpoint_monodromy_family_scope_mismatch")
        if self.duplicate_adjacent_relations:
            reasons.append("endpoint_monodromy_duplicate_adjacent_relations")
        if self.duplicate_far_commutativity_relations:
            reasons.append("endpoint_monodromy_duplicate_far_relations")
        if self.malformed_adjacent_relations:
            reasons.append("endpoint_monodromy_malformed_adjacent_relations")
        if self.malformed_far_commutativity_relations:
            reasons.append("endpoint_monodromy_malformed_far_relations")
        if self.relation_contexts_outside_domain:
            reasons.append("endpoint_monodromy_relation_context_outside_domain")
        return tuple(reasons)


@dataclass(frozen=True)
class UniversalKEndpointMonodromyRepresentationAudit:
    """Finite permutation representation of the endpoint monodromy presentation."""

    presentation: UniversalKEndpointMonodromyPresentation
    reachable_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...]
    rows: Tuple[UniversalKSignedEndpointGeneratorRow, ...]

    @property
    def reachable_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(self.reachable_seed_states)

    @property
    def malformed_reachable_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(
            tuple(
                state
                for state in self.reachable_seed_states
                if not _universal_k_endpoint_seed_state_well_formed(state)
            )
        )

    @property
    def duplicate_reachable_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.reachable_seed_states)

    @property
    def reachable_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    family
                    for family, _state in self.reachable_seed_states_exact
                    if family in UNIVERSAL_K_ENDPOINT_FAMILIES
                },
                key=repr,
            )
        )

    @property
    def family_scope_exact(self) -> bool:
        return set(self.reachable_families) == set(
            self.presentation.expected_endpoint_families_exact
        )

    @property
    def states_by_family(self) -> Mapping[str, Tuple[UniversalKSeedState, ...]]:
        states: dict[str, list[UniversalKSeedState]] = {}
        seen: dict[str, set[object]] = {}
        for family, seed_state in self.reachable_seed_states_exact:
            if family not in UNIVERSAL_K_ENDPOINT_FAMILIES:
                continue
            marker = _value_marker(seed_state)
            family_seen = seen.setdefault(family, set())
            if marker in family_seen:
                continue
            family_seen.add(marker)
            states.setdefault(family, []).append(seed_state)
        return {
            family: tuple(sorted(family_states, key=repr))
            for family, family_states in states.items()
        }

    @property
    def positive_rows_by_context(
        self,
    ) -> Mapping[
        UniversalKEndpointMonodromyContext,
        Mapping[UniversalKSeedState, UniversalKSeedState],
    ]:
        rows_by_context: dict[
            UniversalKEndpointMonodromyContext,
            dict[UniversalKSeedState, UniversalKSeedState],
        ] = {}
        for row in self.rows:
            if row.sign != 1:
                continue
            context = (
                row.endpoint_family,
                row.left_color,
                row.right_color,
                row.input_left,
                row.input_right,
            )
            if not UniversalKEndpointMonodromyPresentation._context_valid(context):
                continue
            if not _is_hashable(row.seed_state):
                continue
            rows_by_context.setdefault(context, {}).setdefault(
                row.seed_state,
                row.next_seed_state,
            )
        return rows_by_context

    @property
    def duplicate_context_state_rows(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyFailure, ...]:
        seen = set()
        duplicates = []
        for row in self.rows:
            if row.sign != 1:
                continue
            context = (
                row.endpoint_family,
                row.left_color,
                row.right_color,
                row.input_left,
                row.input_right,
            )
            key = (_value_marker(context), _value_marker(row.seed_state))
            if key in seen:
                duplicates.append((context, "monodromy_duplicate_state_row", row.seed_state))
            seen.add(key)
        return tuple(sorted(duplicates, key=repr))

    @property
    def extra_context_rows(self) -> Tuple[UniversalKEndpointMonodromyContext, ...]:
        expected = {_value_marker(context) for context in self.presentation.contexts_exact}
        return _unique_values(
            tuple(
                (
                    row.endpoint_family,
                    row.left_color,
                    row.right_color,
                    row.input_left,
                    row.input_right,
                )
                for row in self.rows
                if row.sign == 1
                and _value_marker(
                    (
                        row.endpoint_family,
                        row.left_color,
                        row.right_color,
                        row.input_left,
                        row.input_right,
                    )
                )
                not in expected
            )
        )

    @property
    def context_map_failures(self) -> Tuple[UniversalKEndpointMonodromyFailure, ...]:
        failures = list(self.duplicate_context_state_rows)
        rows_by_context = self.positive_rows_by_context
        for context in self.presentation.contexts_exact:
            if not UniversalKEndpointMonodromyPresentation._context_valid(context):
                continue
            family = context[0]
            states = self.states_by_family.get(family, ())
            state_markers = {_value_marker(state) for state in states}
            state_map = rows_by_context.get(context, {})
            missing_states = tuple(
                state
                for state in states
                if _value_marker(state) not in {_value_marker(key) for key in state_map}
            )
            if missing_states:
                failures.append(
                    (context, "monodromy_representation_missing_state_rows", missing_states)
                )
            extra_states = tuple(
                sorted(
                    (
                        state
                        for state in state_map
                        if _value_marker(state) not in state_markers
                    ),
                    key=repr,
                )
            )
            if extra_states:
                failures.append(
                    (context, "monodromy_representation_extra_state_rows", extra_states)
                )
            outside_next_states = tuple(
                sorted(
                    {
                        next_state
                        for next_state in state_map.values()
                        if _value_marker(next_state) not in state_markers
                    },
                    key=repr,
                )
            )
            if outside_next_states:
                failures.append(
                    (
                        context,
                        "monodromy_representation_next_state_outside_family",
                        outside_next_states,
                    )
                )
            if not states:
                failures.append(
                    (context, "monodromy_representation_family_has_no_states", family)
                )
                continue
            if missing_states or extra_states or outside_next_states:
                continue
            image_markers = tuple(_value_marker(state) for state in state_map.values())
            if set(image_markers) != state_markers or len(image_markers) != len(
                set(image_markers)
            ):
                failures.append(
                    (
                        context,
                        "monodromy_representation_context_not_permutation",
                        tuple(sorted(state_map.items(), key=repr)),
                    )
                )
        if self.extra_context_rows:
            failures.append(
                (
                    ("positive_monodromy_contexts",),
                    "monodromy_representation_extra_context_rows",
                    self.extra_context_rows,
                )
            )
        return tuple(sorted(failures, key=repr))

    def _apply_word(
        self,
        seed_state: UniversalKSeedState,
        word: UniversalKEndpointMonodromyWord,
    ) -> Tuple[UniversalKSeedState | None, UniversalKEndpointMonodromyFailure | None]:
        state = seed_state
        rows_by_context = self.positive_rows_by_context
        for context in word:
            state_map = rows_by_context.get(context)
            if state_map is None:
                return None, (context, "monodromy_relation_missing_context_map", None)
            next_state = state_map.get(state)
            if next_state is None:
                return None, (
                    context,
                    "monodromy_relation_missing_state_map",
                    state,
                )
            state = next_state
        return state, None

    @property
    def relation_failures(self) -> Tuple[UniversalKEndpointMonodromyFailure, ...]:
        if self.context_map_failures:
            return ()
        failures = []
        relations = (
            tuple((relation, "adjacent") for relation in self.presentation.adjacent_relations_exact)
            + tuple(
                (relation, "far")
                for relation in self.presentation.far_commutativity_relations_exact
            )
        )
        for relation, relation_kind in relations:
            left_word, right_word = relation
            families = {
                context[0]
                for context in tuple(left_word) + tuple(right_word)
                if UniversalKEndpointMonodromyPresentation._context_valid(context)
            }
            if len(families) != 1:
                failures.append(
                    (relation, "monodromy_relation_family_mismatch", tuple(sorted(families)))
                )
                continue
            family = next(iter(families))
            for seed_state in self.states_by_family.get(family, ()):
                left_state, left_failure = self._apply_word(seed_state, left_word)
                right_state, right_failure = self._apply_word(seed_state, right_word)
                if left_failure is not None:
                    failures.append(left_failure)
                if right_failure is not None:
                    failures.append(right_failure)
                if left_failure is None and right_failure is None and left_state != right_state:
                    failures.append(
                        (
                            relation,
                            f"monodromy_{relation_kind}_relation_mismatch",
                            (seed_state, left_state, right_state),
                        )
                    )
        return tuple(sorted(_unique_values(tuple(failures)), key=repr))

    @property
    def proves_monodromy_representation(self) -> bool:
        return (
            self.presentation.presentation_is_finite
            and self.family_scope_exact
            and not self.malformed_reachable_seed_states
            and not self.duplicate_reachable_seed_states
            and not self.context_map_failures
            and not self.relation_failures
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.presentation.presentation_is_finite:
            reasons.append("endpoint_monodromy_presentation_not_finite")
            reasons.extend(self.presentation.failure_reasons)
        if not self.family_scope_exact:
            reasons.append("endpoint_monodromy_representation_family_scope_mismatch")
        if self.malformed_reachable_seed_states:
            reasons.append("endpoint_monodromy_representation_malformed_seed_states")
        if self.duplicate_reachable_seed_states:
            reasons.append("endpoint_monodromy_representation_duplicate_seed_states")
        if self.context_map_failures:
            reasons.append("endpoint_monodromy_representation_context_map_failures")
        if self.relation_failures:
            reasons.append("endpoint_monodromy_representation_relation_failures")
        return tuple(_unique_values(tuple(reasons)))


def universal_k_endpoint_monodromy_representation_audit(
    presentation: UniversalKEndpointMonodromyPresentation,
    reachable_seed_states: Sequence[Tuple[str, UniversalKSeedState]],
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> UniversalKEndpointMonodromyRepresentationAudit:
    """Audit the positive endpoint state maps as a representation of Pi_E."""

    return UniversalKEndpointMonodromyRepresentationAudit(
        presentation=presentation,
        reachable_seed_states=tuple(reachable_seed_states),
        rows=tuple(rows),
    )


def _universal_k_positive_context_path(
    interval: LocalInterval,
    endpoint_family: str,
    start_colors: Tuple[Color, ...],
    start_fibres: Tuple[FibrePoint, ...],
    indices: Tuple[int, ...],
) -> UniversalKEndpointMonodromyWord | None:
    contexts = []
    colors = tuple(start_colors)
    fibres = tuple(start_fibres)
    for index in indices:
        left_color = colors[index]
        right_color = colors[index + 1]
        input_left = fibres[index]
        input_right = fibres[index + 1]
        output = interval.T.get((left_color, right_color, input_left, input_right))
        target_colors = interval.base_R.get((left_color, right_color))
        if output is None or target_colors is None:
            return None
        contexts.append(
            (endpoint_family, left_color, right_color, input_left, input_right)
        )
        next_colors = list(colors)
        next_fibres = list(fibres)
        next_colors[index], next_colors[index + 1] = target_colors
        next_fibres[index], next_fibres[index + 1] = output
        colors = tuple(next_colors)
        fibres = tuple(next_fibres)
    return tuple(contexts)


def universal_k_endpoint_monodromy_presentation(
    interval: LocalInterval,
    endpoint_families: Sequence[str],
) -> UniversalKEndpointMonodromyPresentation:
    """Build the finite positive local-context presentation for U/C/M observers."""

    families = _unique_values(tuple(endpoint_families))
    valid_families = tuple(
        family for family in families if family in UNIVERSAL_K_ENDPOINT_FAMILIES
    )
    contexts = tuple(
        sorted(
            (
                (family, left_color, right_color, input_left, input_right)
                for family in valid_families
                for left_color, right_color in product(interval.colors, repeat=2)
                for input_left in interval.fibres[left_color]
                for input_right in interval.fibres[right_color]
            ),
            key=repr,
        )
    )
    adjacent_relations = []
    for family in valid_families:
        for a, b, c in product(interval.colors, repeat=3):
            for x, y, z in product(
                interval.fibres[a],
                interval.fibres[b],
                interval.fibres[c],
            ):
                left_word = _universal_k_positive_context_path(
                    interval,
                    family,
                    (a, b, c),
                    (x, y, z),
                    (0, 1, 0),
                )
                right_word = _universal_k_positive_context_path(
                    interval,
                    family,
                    (a, b, c),
                    (x, y, z),
                    (1, 0, 1),
                )
                if left_word is not None and right_word is not None:
                    adjacent_relations.append((left_word, right_word))

    far_relations = []
    contexts_by_family = {
        family: tuple(context for context in contexts if context[0] == family)
        for family in valid_families
    }
    for family in valid_families:
        family_contexts = contexts_by_family.get(family, ())
        for index, left_context in enumerate(family_contexts):
            for right_context in family_contexts[index:]:
                far_relations.append(
                    ((left_context, right_context), (right_context, left_context))
                )

    return UniversalKEndpointMonodromyPresentation(
        expected_endpoint_families=families,
        contexts=contexts,
        adjacent_relations=_unique_values(tuple(adjacent_relations)),
        far_commutativity_relations=_unique_values(tuple(far_relations)),
    )


@dataclass(frozen=True)
class UniversalKTelescopingDetectorAudit:
    """Fixed-assignment detector-lift proving endpoint labels telescope.

    Rowwise two-strand longitude witnesses only show that an individual
    emission has the shape of a generator longitude value.  This audit records
    the stronger all-word certificate: fixed detector tracks are initialized
    before reading the braid word, updated by the Artin detector recurrence,
    and tied to state-indexed word templates in current longitude variables
    whose local row identities telescope to the endpoint.
    """

    expected_entry_keys: Tuple[UniversalKSignedEndpointEntryKey, ...]
    covered_entry_keys: Tuple[UniversalKSignedEndpointEntryKey, ...]
    expected_endpoint_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...] = ()
    covered_endpoint_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...] = ()
    detector_track_counts_by_family: Tuple[Tuple[str, int], ...] = ()
    detector_track_initialization_rows: Tuple[
        UniversalKDetectorTrackInitializationRow,
        ...,
    ] = ()
    expected_word_potential_seed_states: Tuple[
        Tuple[str, UniversalKSeedState], ...
    ] = ()
    covered_word_potential_seed_states: Tuple[
        Tuple[str, UniversalKSeedState], ...
    ] = ()
    detector_track_count: int | None = None
    detector_tracks_fixed_before_braid: bool = False
    detector_track_initialization_verified: bool = False
    artin_detector_recurrence_verified: bool = False
    word_potential_templates_use_only_current_longitudes: bool = False
    word_potential_artin_substitution_verified: bool = False
    word_potential_identity_verified: bool = False
    word_potential_certificate: UniversalKWordPotentialCertificate | None = None
    telescoping_identity_verified: bool = False
    terminal_readout_longitudes_verified: bool = False
    initial_readout_normalized: bool = False
    braid_index_independent: bool = False

    @property
    def expected_entry_keys_exact(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _unique_values(self.expected_entry_keys)

    @property
    def covered_entry_keys_exact(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _unique_values(self.covered_entry_keys)

    @property
    def expected_positive_entry_keys_exact(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return tuple(
            key
            for key in self.expected_entry_keys_exact
            if _universal_k_is_positive_entry_key(key)
        )

    @property
    def covered_positive_entry_keys_exact(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return tuple(
            key
            for key in self.covered_entry_keys_exact
            if _universal_k_is_positive_entry_key(key)
        )

    @property
    def duplicate_expected_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _duplicate_values(self.expected_entry_keys)

    @property
    def duplicate_covered_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _duplicate_values(self.covered_entry_keys)

    @property
    def duplicate_expected_positive_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _duplicate_values(
            tuple(
                key
                for key in self.expected_entry_keys
                if _universal_k_is_positive_entry_key(key)
            )
        )

    @property
    def duplicate_covered_positive_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _duplicate_values(
            tuple(
                key
                for key in self.covered_entry_keys
                if _universal_k_is_positive_entry_key(key)
            )
        )

    @property
    def malformed_expected_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _unique_values(
            tuple(
                key
                for key in self.expected_entry_keys
                if not _universal_k_signed_entry_key_well_formed(key)
            )
        )

    @property
    def malformed_covered_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _unique_values(
            tuple(
                key
                for key in self.covered_entry_keys
                if not _universal_k_signed_entry_key_well_formed(key)
            )
        )

    @property
    def entry_ledgers_well_formed(self) -> bool:
        return (
            not self.malformed_expected_entry_keys
            and not self.malformed_covered_entry_keys
        )

    @property
    def entry_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_positive_entry_keys
            and not self.duplicate_covered_positive_entry_keys
        )

    @property
    def missing_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        covered = set(self.covered_positive_entry_keys_exact)
        return tuple(
            key for key in self.expected_positive_entry_keys_exact if key not in covered
        )

    @property
    def extra_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        expected = set(self.expected_positive_entry_keys_exact)
        return tuple(
            key for key in self.covered_positive_entry_keys_exact if key not in expected
        )

    @property
    def entry_coverage_exact(self) -> bool:
        return (
            bool(self.expected_positive_entry_keys_exact)
            and not self.missing_entry_keys
            and not self.extra_entry_keys
        )

    @property
    def entry_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            sorted(
                {(key[0], key[1]) for key in self.expected_positive_entry_keys_exact},
                key=repr,
            )
        )

    @property
    def expected_endpoint_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(self.expected_endpoint_seed_states)

    @property
    def covered_endpoint_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(self.covered_endpoint_seed_states)

    @property
    def duplicate_expected_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.expected_endpoint_seed_states)

    @property
    def duplicate_covered_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.covered_endpoint_seed_states)

    @property
    def malformed_expected_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(
            tuple(
                state
                for state in self.expected_endpoint_seed_states
                if not _universal_k_endpoint_seed_state_well_formed(state)
            )
        )

    @property
    def malformed_covered_endpoint_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(
            tuple(
                state
                for state in self.covered_endpoint_seed_states
                if not _universal_k_endpoint_seed_state_well_formed(state)
            )
        )

    @property
    def endpoint_seed_state_ledgers_well_formed(self) -> bool:
        return (
            not self.malformed_expected_endpoint_seed_states
            and not self.malformed_covered_endpoint_seed_states
        )

    @property
    def seed_state_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_endpoint_seed_states
            and not self.duplicate_covered_endpoint_seed_states
        )

    @property
    def seed_state_scope_matches_entries(self) -> bool:
        return set(self.expected_endpoint_seed_states_exact) == set(
            self.entry_endpoint_seed_states
        )

    @property
    def seed_state_coverage_exact(self) -> bool:
        return (
            bool(self.expected_endpoint_seed_states_exact)
            and set(self.expected_endpoint_seed_states_exact)
            == set(self.covered_endpoint_seed_states_exact)
        )

    @property
    def expected_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    state[0]
                    for state in self.expected_endpoint_seed_states_exact
                    if _universal_k_endpoint_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def detector_track_count_rows(
        self,
    ) -> Tuple[Tuple[object, object], ...]:
        return tuple(
            parts
            for row in self.detector_track_counts_by_family
            for parts in (_universal_k_detector_track_count_row_parts(row),)
            if parts is not None
        )

    @property
    def detector_track_count_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    family
                    for family, count in self.detector_track_count_rows
                    if (
                        family in UNIVERSAL_K_ENDPOINT_FAMILIES
                        and _universal_k_positive_int(count)
                    )
                },
                key=repr,
            )
        )

    @property
    def detector_track_count_by_family(self) -> Mapping[str, int]:
        return {
            family: count
            for family, count in self.detector_track_count_rows
            if (
                family in UNIVERSAL_K_ENDPOINT_FAMILIES
                and _universal_k_positive_int(count)
            )
        }

    @property
    def malformed_detector_track_count_rows(self) -> Tuple[object, ...]:
        return _unique_values(
            tuple(
                row
                for row in self.detector_track_counts_by_family
                if _universal_k_detector_track_count_row_parts(row) is None
            )
        )

    @property
    def invalid_detector_track_count_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    family
                    for family, _count in self.detector_track_count_rows
                    if family not in UNIVERSAL_K_ENDPOINT_FAMILIES
                },
                key=repr,
            )
        )

    @property
    def malformed_detector_track_count_values(
        self,
    ) -> Tuple[Tuple[str, object], ...]:
        malformed = []
        seen = set()
        for family, count in self.detector_track_count_rows:
            if _universal_k_positive_int(count):
                continue
            value = (family, count)
            marker = repr(value)
            if marker in seen:
                continue
            seen.add(marker)
            malformed.append(value)
        return tuple(sorted(malformed, key=repr))

    @property
    def detector_track_count_rows_well_formed(self) -> bool:
        return (
            not self.malformed_detector_track_count_rows
            and not self.invalid_detector_track_count_families
            and not self.malformed_detector_track_count_values
        )

    @property
    def duplicate_detector_track_count_families(self) -> Tuple[str, ...]:
        return _duplicate_values(
            tuple(
                family
                for family, _count in self.detector_track_count_rows
            )
        )

    @property
    def detector_track_count_ledgers_have_no_duplicates(self) -> bool:
        return not self.duplicate_detector_track_count_families

    @property
    def detector_track_count_family_scope_exact(self) -> bool:
        return set(self.detector_track_count_families) == set(
            self.expected_endpoint_families
        )

    @property
    def detector_track_counts_positive(self) -> bool:
        return (
            bool(self.detector_track_counts_by_family)
            and self.detector_track_count_rows_well_formed
        )

    @property
    def detector_track_count_matches_family_sum(self) -> bool:
        return (
            _universal_k_positive_int(self.detector_track_count)
            and self.detector_track_count_rows_well_formed
            and self.detector_track_count
            == sum(
                count
                for _family, count in self.detector_track_count_rows
            )
        )

    @property
    def expected_detector_track_keys(self) -> Tuple[UniversalKDetectorTrackKey, ...]:
        keys = []
        for family, count in self.detector_track_count_rows:
            if (
                family not in UNIVERSAL_K_ENDPOINT_FAMILIES
                or not _universal_k_positive_int(count)
            ):
                continue
            keys.extend((family, index) for index in range(count))
        return tuple(sorted(keys, key=repr))

    @property
    def covered_detector_track_keys(self) -> Tuple[UniversalKDetectorTrackKey, ...]:
        return tuple(
            sorted(
                {
                    row.key
                    for row in self.detector_track_initialization_rows
                    if _universal_k_detector_track_key_well_formed(row.key)
                },
                key=repr,
            )
        )

    @property
    def duplicate_detector_track_initialization_keys(
        self,
    ) -> Tuple[UniversalKDetectorTrackKey, ...]:
        return _duplicate_values(
            tuple(
                row.key
                for row in self.detector_track_initialization_rows
                if _universal_k_detector_track_key_well_formed(row.key)
            )
        )

    @property
    def missing_detector_track_initialization_keys(
        self,
    ) -> Tuple[UniversalKDetectorTrackKey, ...]:
        covered = set(self.covered_detector_track_keys)
        return tuple(key for key in self.expected_detector_track_keys if key not in covered)

    @property
    def extra_detector_track_initialization_keys(
        self,
    ) -> Tuple[UniversalKDetectorTrackKey, ...]:
        expected = set(self.expected_detector_track_keys)
        return tuple(key for key in self.covered_detector_track_keys if key not in expected)

    @property
    def invalid_detector_track_initialization_rows(
        self,
    ) -> Tuple[UniversalKDetectorTrackInitializationRow, ...]:
        return tuple(
            row
            for row in self.detector_track_initialization_rows
            if not row.initialization_rule_finite
        )

    @property
    def detector_track_initialization_rows_not_fixed_before_braid(
        self,
    ) -> Tuple[UniversalKDetectorTrackInitializationRow, ...]:
        return tuple(
            row
            for row in self.detector_track_initialization_rows
            if not row.fixed_before_braid
        )

    @property
    def detector_track_initializations_fixed_before_braid(self) -> bool:
        return (
            self.detector_track_initialization_rows_exact
            and not self.detector_track_initialization_rows_not_fixed_before_braid
        )

    @property
    def detector_track_initialization_template_failures(
        self,
    ) -> Tuple[UniversalKDetectorTrackInitializationFailure, ...]:
        failures = []
        group_elements = None
        if self.word_potential_certificate is not None:
            group_elements = set(self.word_potential_certificate.endpoint_group.elements)
        for row in self.detector_track_initialization_rows:
            seen_variables = set()
            for assignment_entry in row.local_assignment_template:
                parts = _universal_k_word_potential_substitution_parts(
                    assignment_entry
                )
                if parts is None:
                    failures.append(
                        (
                            row.key,
                            "malformed_detector_track_assignment",
                            assignment_entry,
                        )
                    )
                    continue
                variable, value = parts
                variable_marker = _value_marker(variable)
                if variable_marker in seen_variables:
                    failures.append(
                        (row.key, "duplicate_detector_track_assignment", variable)
                    )
                seen_variables.add(variable_marker)
                if not _universal_k_word_potential_variable_valid(variable):
                    failures.append(
                        (row.key, "invalid_detector_track_assignment_variable", variable)
                    )
                    continue
                kind, track_index, _position = variable
                if kind != "A":
                    failures.append(
                        (row.key, "detector_track_assignment_not_raw_variable", variable)
                    )
                if track_index != row.track_index:
                    failures.append(
                        (row.key, "detector_track_assignment_track_mismatch", variable)
                    )
                if group_elements is not None and value not in group_elements:
                    failures.append(
                        (row.key, "detector_track_assignment_value_outside_group", value)
                    )
        return tuple(failures)

    @property
    def detector_track_initialization_rows_exact(self) -> bool:
        return (
            bool(self.expected_detector_track_keys)
            and not self.duplicate_detector_track_initialization_keys
            and not self.missing_detector_track_initialization_keys
            and not self.extra_detector_track_initialization_keys
        )

    @property
    def detector_track_initializations_verified(self) -> bool:
        return (
            self.detector_track_initialization_rows_exact
            and not self.invalid_detector_track_initialization_rows
            and not self.detector_track_initialization_template_failures
        )

    @property
    def initialized_raw_assignment_variables_by_family(
        self,
    ) -> Mapping[str, Tuple[UniversalKWordPotentialVariable, ...]]:
        initialized: dict[str, set[UniversalKWordPotentialVariable]] = {}
        for row in self.detector_track_initialization_rows:
            family_initialized = initialized.setdefault(row.endpoint_family, set())
            for assignment_entry in row.local_assignment_template:
                parts = _universal_k_word_potential_substitution_parts(
                    assignment_entry
                )
                if parts is None:
                    continue
                variable, _value = parts
                if (
                    _universal_k_word_potential_variable_valid(variable)
                    and variable[0] == "A"
                    and variable[1] == row.track_index
                ):
                    family_initialized.add(variable)
        return {
            family: tuple(sorted(variables, key=repr))
            for family, variables in initialized.items()
        }

    @property
    def expected_word_potential_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(self.expected_word_potential_seed_states)

    @property
    def covered_word_potential_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(self.covered_word_potential_seed_states)

    @property
    def duplicate_expected_word_potential_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.expected_word_potential_seed_states)

    @property
    def duplicate_covered_word_potential_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.covered_word_potential_seed_states)

    @property
    def malformed_expected_word_potential_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(
            tuple(
                state
                for state in self.expected_word_potential_seed_states
                if not _universal_k_endpoint_seed_state_well_formed(state)
            )
        )

    @property
    def malformed_covered_word_potential_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(
            tuple(
                state
                for state in self.covered_word_potential_seed_states
                if not _universal_k_endpoint_seed_state_well_formed(state)
            )
        )

    @property
    def word_potential_seed_state_ledgers_well_formed(self) -> bool:
        return (
            not self.malformed_expected_word_potential_seed_states
            and not self.malformed_covered_word_potential_seed_states
        )

    @property
    def word_potential_seed_ledgers_have_no_duplicates(self) -> bool:
        return (
            not self.duplicate_expected_word_potential_seed_states
            and not self.duplicate_covered_word_potential_seed_states
        )

    @property
    def word_potential_seed_state_scope_matches_expected(self) -> bool:
        return set(self.expected_word_potential_seed_states_exact) == set(
            self.expected_endpoint_seed_states_exact
        )

    @property
    def word_potential_seed_state_coverage_exact(self) -> bool:
        return (
            bool(self.expected_word_potential_seed_states_exact)
            and set(self.expected_word_potential_seed_states_exact)
            == set(self.covered_word_potential_seed_states_exact)
        )

    @property
    def word_potential_templates_supplied(self) -> bool:
        return (
            self.word_potential_certificate is not None
            and self.word_potential_seed_state_scope_matches_expected
            and self.word_potential_seed_state_coverage_exact
            and self.word_potential_seed_state_ledgers_well_formed
            and self.word_potential_seed_ledgers_have_no_duplicates
            and self.word_potential_certificate_template_scope_exact
            and self.word_potential_certificate_entry_scope_exact
            and self.word_potential_certificate_ledgers_have_no_duplicates
        )

    @property
    def word_potential_certificate_template_scope_exact(self) -> bool:
        return (
            self.word_potential_certificate is not None
            and set(self.word_potential_certificate.template_seed_states_exact)
            == set(self.expected_word_potential_seed_states_exact)
        )

    @property
    def word_potential_certificate_entry_scope_exact(self) -> bool:
        return (
            self.word_potential_certificate is not None
            and set(self.word_potential_certificate.positive_identity_entry_keys_exact)
            == set(self.expected_positive_entry_keys_exact)
        )

    @property
    def word_potential_certificate_ledgers_have_no_duplicates(self) -> bool:
        return self.word_potential_certificate is not None and (
            not self.word_potential_certificate.duplicate_template_seed_states
            and not self.word_potential_certificate.malformed_template_seed_states
            and not self.word_potential_certificate.malformed_identity_entry_keys
            and not self.word_potential_certificate.malformed_identity_next_seed_states
            and not self.word_potential_certificate.duplicate_positive_identity_entry_keys
            and not self.word_potential_certificate.malformed_normalized_seed_states
            and not self.word_potential_certificate.duplicate_normalized_seed_states
        )

    @property
    def word_potential_templates_use_only_current_longitudes_verified(self) -> bool:
        return (
            self.word_potential_certificate is not None
            and self.word_potential_certificate.templates_use_only_current_longitudes
        )

    @property
    def word_potential_track_scope_failures(
        self,
    ) -> Tuple[UniversalKWordPotentialFailure, ...]:
        if self.word_potential_certificate is None:
            return ()
        failures = []
        counts_by_family = self.detector_track_count_by_family
        for state, word in self.word_potential_certificate.templates:
            if not _universal_k_endpoint_seed_state_well_formed(state):
                continue
            family, _seed_state = state
            count = counts_by_family.get(family)
            if count is None:
                failures.append(
                    (state, "word_potential_family_has_no_track_count", family)
                )
                continue
            for letter in word:
                parts = _universal_k_word_potential_letter_parts(letter)
                if parts is None:
                    continue
                variable, _exponent = parts
                if (
                    _universal_k_word_potential_variable_valid(variable)
                    and variable[1] >= count
                ):
                    failures.append(
                        (state, "word_potential_track_index_out_of_scope", variable)
                    )
        for row in self.word_potential_certificate.identity_rows:
            if not _universal_k_signed_entry_key_well_formed(row.entry_key):
                continue
            family = row.entry_key[0]
            if not _universal_k_is_positive_entry_key(row.entry_key):
                continue
            count = counts_by_family.get(family)
            if count is None:
                failures.append(
                    (
                        row.entry_key,
                        "word_potential_row_family_has_no_track_count",
                        family,
                    )
                )
                continue
            row_variables = []
            for substitution_row in row.artin_substitution:
                parts = _universal_k_word_potential_substitution_parts(
                    substitution_row
                )
                if parts is None:
                    continue
                variable, image = parts
                row_variables.append(variable)
                for image_letter in image:
                    image_parts = _universal_k_word_potential_letter_parts(
                        image_letter
                    )
                    if image_parts is None:
                        continue
                    image_variable, _exponent = image_parts
                    row_variables.append(image_variable)
            for variable in row_variables:
                if (
                    _universal_k_word_potential_variable_valid(variable)
                    and variable[1] >= count
                ):
                    failures.append(
                        (
                            row.entry_key,
                            "word_potential_substitution_track_index_out_of_scope",
                            variable,
                        )
                    )
        return tuple(failures)

    @property
    def word_potential_track_scope_verified(self) -> bool:
        return not self.word_potential_track_scope_failures

    @property
    def word_potential_raw_assignment_scope_failures(
        self,
    ) -> Tuple[UniversalKWordPotentialFailure, ...]:
        if self.word_potential_certificate is None:
            return ()
        failures = []
        initialized_by_family = self.initialized_raw_assignment_variables_by_family
        for row in self.word_potential_certificate.identity_rows:
            if not _universal_k_signed_entry_key_well_formed(row.entry_key):
                continue
            family = row.entry_key[0]
            if not _universal_k_is_positive_entry_key(row.entry_key):
                continue
            initialized = set(initialized_by_family.get(family, ()))
            row_raw_variables = []
            for substitution_row in row.artin_substitution:
                parts = _universal_k_word_potential_substitution_parts(
                    substitution_row
                )
                if parts is None:
                    continue
                variable, image = parts
                row_raw_variables.append(variable)
                for image_letter in image:
                    image_parts = _universal_k_word_potential_letter_parts(
                        image_letter
                    )
                    if image_parts is None:
                        continue
                    image_variable, _exponent = image_parts
                    row_raw_variables.append(image_variable)
            for variable in sorted(set(row_raw_variables), key=repr):
                if (
                    _universal_k_word_potential_variable_valid(variable)
                    and variable[0] == "A"
                    and variable not in initialized
                ):
                    failures.append(
                        (
                            row.entry_key,
                            "word_potential_raw_assignment_not_initialized",
                            variable,
                        )
                    )
        return tuple(failures)

    @property
    def word_potential_raw_assignment_scope_verified(self) -> bool:
        return not self.word_potential_raw_assignment_scope_failures

    @property
    def word_potential_artin_substitution_proved(self) -> bool:
        return (
            self.word_potential_certificate is not None
            and self.word_potential_certificate.artin_substitutions_verified
        )

    @property
    def word_potential_identity_proved(self) -> bool:
        return (
            self.word_potential_certificate is not None
            and self.word_potential_certificate.identities_verified
        )

    @property
    def initial_readout_normalized_proved(self) -> bool:
        return (
            self.word_potential_certificate is not None
            and self.word_potential_certificate.initial_readouts_normalized
        )

    @property
    def word_potential_templates_verified(self) -> bool:
        return (
            self.word_potential_templates_supplied
            and self.word_potential_templates_use_only_current_longitudes_verified
            and self.word_potential_track_scope_verified
            and self.word_potential_raw_assignment_scope_verified
            and self.word_potential_artin_substitution_proved
            and self.word_potential_identity_proved
        )

    @property
    def artin_detector_recurrence_proved(self) -> bool:
        return self.word_potential_artin_substitution_proved

    @property
    def terminal_readout_longitudes_proved(self) -> bool:
        return (
            self.word_potential_templates_supplied
            and self.word_potential_templates_use_only_current_longitudes_verified
            and self.word_potential_track_scope_verified
            and self.word_potential_raw_assignment_scope_verified
        )

    @property
    def braid_index_independence_proved(self) -> bool:
        return (
            self.detector_track_initializations_verified
            and self.word_potential_templates_supplied
            and self.word_potential_track_scope_verified
            and self.word_potential_raw_assignment_scope_verified
        )

    @property
    def detector_tracks_supplied(self) -> bool:
        return (
            self.detector_track_count is not None
            and _universal_k_positive_int(self.detector_track_count)
            and self.detector_track_count_rows_well_formed
            and self.detector_track_count_matches_family_sum
            and self.detector_track_count_ledgers_have_no_duplicates
            and self.detector_track_count_family_scope_exact
            and self.detector_track_counts_positive
        )

    @property
    def proves_telescoping_detector_lift(self) -> bool:
        return (
            self.entry_coverage_exact
            and self.entry_ledgers_well_formed
            and self.entry_ledgers_have_no_duplicates
            and self.endpoint_seed_state_ledgers_well_formed
            and self.seed_state_scope_matches_entries
            and self.seed_state_coverage_exact
            and self.seed_state_ledgers_have_no_duplicates
            and self.detector_tracks_supplied
            and self.detector_track_initializations_verified
            and self.artin_detector_recurrence_proved
            and self.word_potential_templates_verified
            and self.terminal_readout_longitudes_proved
            and self.initial_readout_normalized_proved
            and self.braid_index_independence_proved
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.expected_positive_entry_keys_exact:
            reasons.append("telescoping_detector_expected_positive_entry_keys_empty")
        if self.missing_entry_keys:
            reasons.append("telescoping_detector_missing_entry_keys")
        if self.extra_entry_keys:
            reasons.append("telescoping_detector_extra_entry_keys")
        if not self.entry_ledgers_well_formed:
            reasons.append("telescoping_detector_malformed_entry_keys")
        if not self.entry_ledgers_have_no_duplicates:
            reasons.append("telescoping_detector_duplicate_entry_keys")
        if not self.seed_state_scope_matches_entries:
            reasons.append("telescoping_detector_seed_state_scope_mismatch")
        if not self.seed_state_coverage_exact:
            reasons.append("telescoping_detector_seed_state_coverage_not_exact")
        if not self.endpoint_seed_state_ledgers_well_formed:
            reasons.append("telescoping_detector_malformed_seed_states")
        if not self.seed_state_ledgers_have_no_duplicates:
            reasons.append("telescoping_detector_duplicate_seed_states")
        if not self.detector_tracks_supplied:
            reasons.append("fixed_detector_tracks_not_supplied")
        if not self.detector_track_count_matches_family_sum:
            reasons.append("detector_track_count_family_sum_mismatch")
        if not self.detector_track_count_rows_well_formed:
            reasons.append("detector_track_count_rows_malformed")
        if self.malformed_detector_track_count_rows:
            reasons.append("detector_track_count_malformed_rows")
        if self.invalid_detector_track_count_families:
            reasons.append("detector_track_count_unknown_families")
        if self.malformed_detector_track_count_values:
            reasons.append("detector_track_count_nonpositive_or_noninteger")
        if not self.detector_track_count_ledgers_have_no_duplicates:
            reasons.append("detector_track_count_duplicate_families")
        if not self.detector_track_count_family_scope_exact:
            reasons.append("detector_track_count_family_scope_mismatch")
        if not self.detector_track_counts_positive:
            reasons.append("detector_track_count_nonpositive_family_count")
        if not self.detector_track_initialization_rows_exact:
            reasons.append("detector_track_initialization_rows_not_exact")
        if self.missing_detector_track_initialization_keys:
            reasons.append("detector_track_initialization_missing_keys")
        if self.extra_detector_track_initialization_keys:
            reasons.append("detector_track_initialization_extra_keys")
        if self.duplicate_detector_track_initialization_keys:
            reasons.append("detector_track_initialization_duplicate_keys")
        if self.invalid_detector_track_initialization_rows:
            reasons.append("detector_track_initialization_invalid_rows")
        if self.detector_track_initialization_rows_not_fixed_before_braid:
            reasons.append("detector_track_initialization_depends_on_braid")
        if self.detector_track_initialization_template_failures:
            reasons.append("detector_track_initialization_invalid_templates")
        if not self.detector_track_initializations_fixed_before_braid:
            reasons.append("detector_tracks_not_fixed_before_braid")
        if not self.detector_track_initializations_verified:
            reasons.append("detector_track_initialization_not_verified")
        if not self.artin_detector_recurrence_proved:
            reasons.append("artin_detector_recurrence_not_verified")
        if not self.word_potential_templates_supplied:
            reasons.append("word_potential_templates_not_supplied")
        if self.word_potential_certificate is None:
            reasons.append("word_potential_certificate_missing")
        if not self.word_potential_seed_state_scope_matches_expected:
            reasons.append("word_potential_seed_state_scope_mismatch")
        if not self.word_potential_seed_state_coverage_exact:
            reasons.append("word_potential_seed_state_coverage_not_exact")
        if not self.word_potential_seed_state_ledgers_well_formed:
            reasons.append("word_potential_malformed_seed_states")
        if not self.word_potential_seed_ledgers_have_no_duplicates:
            reasons.append("word_potential_duplicate_seed_states")
        if not self.word_potential_certificate_template_scope_exact:
            reasons.append("word_potential_certificate_template_scope_mismatch")
        if not self.word_potential_certificate_entry_scope_exact:
            reasons.append("word_potential_certificate_entry_scope_mismatch")
        if not self.word_potential_certificate_ledgers_have_no_duplicates:
            reasons.append("word_potential_certificate_duplicate_ledgers")
        if not self.word_potential_templates_use_only_current_longitudes_verified:
            reasons.append("word_potential_uses_raw_assignment_variables")
        if not self.word_potential_track_scope_verified:
            reasons.append("word_potential_track_variables_out_of_scope")
        if not self.word_potential_raw_assignment_scope_verified:
            reasons.append("word_potential_raw_assignments_not_initialized")
        if not self.word_potential_artin_substitution_proved:
            reasons.append("word_potential_artin_substitution_not_verified")
        if not self.word_potential_identity_proved:
            reasons.append("word_potential_identity_not_verified")
        if self.word_potential_certificate is not None:
            if self.word_potential_certificate.malformed_template_seed_states:
                reasons.append("word_potential_certificate_malformed_template_states")
            if self.word_potential_certificate.malformed_identity_entry_keys:
                reasons.append("word_potential_certificate_malformed_identity_rows")
            if self.word_potential_certificate.malformed_identity_next_seed_states:
                reasons.append(
                    "word_potential_certificate_malformed_next_seed_states"
                )
            if self.word_potential_certificate.malformed_normalized_seed_states:
                reasons.append("word_potential_certificate_malformed_normalized_states")
            if self.word_potential_certificate.raw_assignment_template_variables:
                reasons.append("word_potential_template_contains_raw_assignments")
            if self.word_potential_certificate.substitution_failures:
                reasons.append("word_potential_artin_substitution_failures")
            if self.word_potential_certificate.detector_domain_failures:
                reasons.append("word_potential_detector_domain_failures")
            if self.word_potential_certificate.identity_failures:
                reasons.append("word_potential_identity_failures")
            if self.word_potential_certificate.coboundary_defect_failures:
                reasons.append("word_potential_coboundary_defect_not_constant")
            if self.word_potential_certificate.normalization_failures:
                reasons.append("word_potential_normalization_failures")
        if not self.terminal_readout_longitudes_proved:
            reasons.append("terminal_readout_longitudes_not_verified")
        if not self.initial_readout_normalized_proved:
            reasons.append("word_potential_initial_value_not_normalized")
        if not self.braid_index_independence_proved:
            reasons.append("telescoping_detector_not_braid_index_independent")
        return tuple(reasons)


@dataclass(frozen=True)
class UniversalKSignedEndpointGeneratorAudit:
    """Certificate-shape audit for signed endpoint tables on K_nabla seeds."""

    seed_classifier_entries: Tuple[UniversalKSeedClassifierEntry, ...]
    reachable_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...]
    required_entry_keys: Tuple[UniversalKSignedEndpointEntryKey, ...]
    rows: Tuple[UniversalKSignedEndpointGeneratorRow, ...]
    entry_domain_derived_from_interval: bool = False
    finite_row_checks_derived_from_tables: bool = False
    endpoint_targets_fixed: bool = False
    coordinate_components_verified: bool = False
    inverse_pairing_verified: bool = False
    inverse_cancellation_verified: bool = False
    positive_ybe_path_verified: bool = False
    positive_ybe_cocycle_verified: bool = False
    far_commutativity_verified: bool = False
    signed_two_strand_base_verified: bool = False
    artin_homomorphism_update_verified: bool = False
    coordinate_component_failures: Tuple[
        UniversalKSignedEndpointCoordinateFailure, ...
    ] = ()
    inverse_pairing_failures: Tuple[UniversalKSignedEndpointInverseFailure, ...] = ()
    inverse_cancellation_failures: Tuple[UniversalKSignedEndpointLabelFailure, ...] = ()
    positive_ybe_path_failures: Tuple[
        UniversalKSignedEndpointPositiveYBEFailure, ...
    ] = ()
    positive_ybe_cocycle_failures: Tuple[UniversalKSignedEndpointLabelFailure, ...] = ()
    far_commutativity_failures: Tuple[UniversalKSignedEndpointLabelFailure, ...] = ()
    two_strand_witness_domain_failures: Tuple[
        UniversalKSignedEndpointLabelFailure, ...
    ] = ()
    two_strand_base_failures: Tuple[UniversalKSignedEndpointLabelFailure, ...] = ()
    artin_update_failures: Tuple[UniversalKSignedEndpointLabelFailure, ...] = ()
    cutoff_readouts_exact: bool = False
    residual_faithfulness_verified: bool = False
    endpoint_target_audit: UniversalKEndpointTargetAudit | None = None
    cutoff_readout_audit: UniversalKCutoffReadoutAudit | None = None
    residual_action_scope: UniversalKResidualActionScopeAudit | None = None
    residual_faithfulness_theorem: UniversalKResidualFaithfulnessAudit | None = None
    residual_action_audit: "EndpointResidualActionAudit | None" = None
    telescoping_detector_audit: UniversalKTelescopingDetectorAudit | None = None
    monodromy_representation_audit: (
        UniversalKEndpointMonodromyRepresentationAudit | None
    ) = None
    endpoint_group: FiniteGroup | None = None

    @property
    def required_seed_states(self) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return universal_k_signed_endpoint_seed_states(self.seed_classifier_entries)

    @property
    def duplicate_seed_classifier_entries(
        self,
    ) -> Tuple[UniversalKSeedClassifierEntry, ...]:
        return _duplicate_values(self.seed_classifier_entries)

    @property
    def duplicate_seed_classifier_descriptors(
        self,
    ) -> Tuple[UniversalKRowDescriptor, ...]:
        return _duplicate_values(tuple(entry[0] for entry in self.seed_classifier_entries))

    @property
    def conflicting_seed_classifier_descriptors(
        self,
    ) -> Tuple[UniversalKRowDescriptor, ...]:
        targets_by_descriptor = {}
        for descriptor, target in self.seed_classifier_entries:
            targets_by_descriptor.setdefault(descriptor, set()).add(target)
        return tuple(
            sorted(
                (
                    descriptor
                    for descriptor, targets in targets_by_descriptor.items()
                    if len(targets) > 1
                ),
                key=repr,
            )
        )

    @property
    def seed_classifier_is_functional(self) -> bool:
        return (
            not self.duplicate_seed_classifier_entries
            and not self.duplicate_seed_classifier_descriptors
            and not self.conflicting_seed_classifier_descriptors
        )

    @property
    def invalid_seed_classifier_targets(
        self,
    ) -> Tuple[UniversalKSeedClassifierEntry, ...]:
        return tuple(
            entry
            for entry in self.seed_classifier_entries
            if not _universal_k_endpoint_seed_state_well_formed(entry[1])
        )

    @property
    def seed_classifier_targets_known(self) -> bool:
        return not self.invalid_seed_classifier_targets

    @property
    def reachable_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _unique_values(self.reachable_seed_states)

    @property
    def duplicate_reachable_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return _duplicate_values(self.reachable_seed_states)

    @property
    def invalid_reachable_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            state
            for state in self.reachable_seed_states_exact
            if not _universal_k_endpoint_seed_state_well_formed(state)
        )

    @property
    def reachable_seed_families_known(self) -> bool:
        return not self.invalid_reachable_seed_states

    @property
    def missing_initial_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        reachable = {_value_marker(state) for state in self.reachable_seed_states_exact}
        return tuple(
            state
            for state in self.required_seed_states
            if _value_marker(state) not in reachable
        )

    @property
    def transition_reachable_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return universal_k_signed_endpoint_transition_closure(
            self.seed_classifier_entries,
            self.rows,
        )

    @property
    def missing_transition_reachable_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        declared = {_value_marker(state) for state in self.reachable_seed_states_exact}
        return tuple(
            state
            for state in self.transition_reachable_seed_states
            if _value_marker(state) not in declared
        )

    @property
    def unreachable_declared_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        transition_reachable = {
            _value_marker(state) for state in self.transition_reachable_seed_states
        }
        return tuple(
            state
            for state in self.reachable_seed_states_exact
            if _value_marker(state) not in transition_reachable
        )

    @property
    def reachable_seed_state_closure_exact(self) -> bool:
        return {
            _value_marker(state) for state in self.reachable_seed_states_exact
        } == {_value_marker(state) for state in self.transition_reachable_seed_states}

    @property
    def row_states_outside_reachable_set(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        reachable = {_value_marker(state) for state in self.reachable_seed_states_exact}
        outside = []
        for row in self.rows:
            current = (row.endpoint_family, row.seed_state)
            next_state = (row.endpoint_family, row.next_seed_state)
            if _value_marker(current) not in reachable:
                outside.append(current)
            if _value_marker(next_state) not in reachable:
                outside.append(next_state)
        return _unique_values(tuple(outside))

    @property
    def required_signed_seed_keys(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState, int], ...]:
        return tuple(
            sorted(
                (
                    (state[0], state[1], sign)
                    for state in self.reachable_seed_states_exact
                    if _universal_k_endpoint_seed_state_well_formed(state)
                    for sign in (-1, 1)
                ),
                key=repr,
            )
        )

    @property
    def supplied_signed_seed_keys(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState, int], ...]:
        return _unique_values(tuple(row.seed_key for row in self.rows))

    @property
    def required_entry_keys_exact(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _unique_values(self.required_entry_keys)

    @property
    def required_positive_entry_keys_exact(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return tuple(
            key
            for key in self.required_entry_keys_exact
            if _universal_k_is_positive_entry_key(key)
        )

    @property
    def required_entry_signed_seed_keys(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState, int], ...]:
        return tuple(sorted({key[:3] for key in self.required_entry_keys_exact}, key=repr))

    @property
    def supplied_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _unique_values(tuple(row.entry_key for row in self.rows))

    @property
    def missing_required_entry_seed_keys(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState, int], ...]:
        required_by_entries = set(self.required_entry_signed_seed_keys)
        return tuple(
            key
            for key in self.required_signed_seed_keys
            if key not in required_by_entries
        )

    @property
    def extra_required_entry_seed_keys(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState, int], ...]:
        required_by_kappa = set(self.required_signed_seed_keys)
        return tuple(
            key
            for key in self.required_entry_signed_seed_keys
            if key not in required_by_kappa
        )

    @property
    def missing_signed_seed_keys(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState, int], ...]:
        supplied = set(self.supplied_signed_seed_keys)
        return tuple(key for key in self.required_signed_seed_keys if key not in supplied)

    @property
    def extra_signed_seed_keys(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState, int], ...]:
        required = set(self.required_signed_seed_keys)
        return tuple(key for key in self.supplied_signed_seed_keys if key not in required)

    @property
    def missing_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        supplied = set(self.supplied_entry_keys)
        return tuple(
            key for key in self.required_entry_keys_exact if key not in supplied
        )

    @property
    def extra_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        required = set(self.required_entry_keys_exact)
        return tuple(key for key in self.supplied_entry_keys if key not in required)

    @property
    def duplicate_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        return _duplicate_values(tuple(row.entry_key for row in self.rows))

    @property
    def undefined_rows(self) -> Tuple[UniversalKSignedEndpointGeneratorRow, ...]:
        return tuple(row for row in self.rows if not row.row_is_defined)

    @property
    def reachable_states_by_family(
        self,
    ) -> Mapping[str, Tuple[UniversalKSeedState, ...]]:
        states_by_family: dict[str, set[UniversalKSeedState]] = {}
        for state in self.reachable_seed_states_exact:
            if not _universal_k_endpoint_seed_state_well_formed(state):
                continue
            family, seed_state = state
            states_by_family.setdefault(family, set()).add(seed_state)
        return {
            family: tuple(sorted(states, key=repr))
            for family, states in states_by_family.items()
        }

    @property
    def positive_monodromy_contexts(
        self,
    ) -> Tuple[Tuple[str, Color, Color, FibrePoint, FibrePoint], ...]:
        return tuple(
            sorted(
                {
                    (key[0], key[3], key[4], key[5], key[6])
                    for key in self.required_positive_entry_keys_exact
                    if _universal_k_signed_entry_key_well_formed(key)
                },
                key=repr,
            )
        )

    @property
    def positive_monodromy_permutation_failures(
        self,
    ) -> Tuple[UniversalKEndpointMonodromyFailure, ...]:
        states_by_family = self.reachable_states_by_family
        rows_by_context: dict[
            Tuple[str, Color, Color, FibrePoint, FibrePoint],
            dict[UniversalKSeedState, UniversalKSeedState],
        ] = {}
        duplicate_state_rows: list[UniversalKEndpointMonodromyFailure] = []
        for row in self.rows:
            if row.sign != 1:
                continue
            context = (
                row.endpoint_family,
                row.left_color,
                row.right_color,
                row.input_left,
                row.input_right,
            )
            state_map = rows_by_context.setdefault(context, {})
            if row.seed_state in state_map:
                duplicate_state_rows.append(
                    (
                        context,
                        "monodromy_context_duplicate_state_row",
                        row.seed_state,
                    )
                )
                continue
            state_map[row.seed_state] = row.next_seed_state

        failures = list(duplicate_state_rows)
        expected_contexts = set(self.positive_monodromy_contexts)
        for context in self.positive_monodromy_contexts:
            family = context[0]
            states = states_by_family.get(family, ())
            state_set = set(states)
            state_map = rows_by_context.get(context, {})
            missing_states = tuple(
                sorted((state for state in states if state not in state_map), key=repr)
            )
            if missing_states:
                failures.append(
                    (context, "monodromy_context_missing_state_rows", missing_states)
                )
            extra_states = tuple(
                sorted(
                    (state for state in state_map if state not in state_set),
                    key=repr,
                )
            )
            if extra_states:
                failures.append(
                    (context, "monodromy_context_extra_state_rows", extra_states)
                )
            outside_next_states = tuple(
                sorted(
                    {
                        next_state
                        for next_state in state_map.values()
                        if next_state not in state_set
                    },
                    key=repr,
                )
            )
            if outside_next_states:
                failures.append(
                    (
                        context,
                        "monodromy_context_next_state_outside_reachable",
                        outside_next_states,
                    )
                )
            if not states:
                failures.append(
                    (context, "monodromy_context_family_has_no_states", family)
                )
                continue
            if missing_states or extra_states or outside_next_states:
                continue
            image_states = set(state_map.values())
            if (
                image_states != state_set
                or len(state_map.values()) != len(image_states)
            ):
                failures.append(
                    (
                        context,
                        "monodromy_context_not_permutation",
                        tuple(
                            sorted(
                                (
                                    (source_state, target_state)
                                    for source_state, target_state in state_map.items()
                                ),
                                key=repr,
                            )
                        ),
                    )
                )

        extra_contexts = tuple(
            sorted(
                (
                    context
                    for context in rows_by_context
                    if context not in expected_contexts
                ),
                key=repr,
            )
        )
        if extra_contexts:
            failures.append(
                (
                    ("positive_monodromy_contexts",),
                    "monodromy_extra_context_rows",
                    extra_contexts,
                )
            )
        return tuple(failures)

    @property
    def positive_monodromy_representation_verified(self) -> bool:
        return (
            not self.positive_monodromy_permutation_failures
            and self.positive_ybe_path_verified
            and self.far_commutativity_verified
            and self.explicit_monodromy_representation_verified
        )

    @property
    def explicit_monodromy_representation_verified(self) -> bool:
        return (
            self.monodromy_representation_audit is None
            or self.monodromy_representation_audit.proves_monodromy_representation
        )

    @property
    def signed_generator_domain_exact(self) -> bool:
        return (
            bool(self.required_entry_keys_exact)
            and self.seed_classifier_is_functional
            and self.seed_classifier_targets_known
            and self.entry_domain_derived_from_interval
            and bool(self.reachable_seed_states_exact)
            and not self.duplicate_reachable_seed_states
            and self.reachable_seed_families_known
            and not self.missing_initial_seed_states
            and self.reachable_seed_state_closure_exact
            and not self.row_states_outside_reachable_set
            and not self.missing_required_entry_seed_keys
            and not self.extra_required_entry_seed_keys
            and not self.missing_signed_seed_keys
            and not self.extra_signed_seed_keys
            and not self.missing_entry_keys
            and not self.extra_entry_keys
            and not self.duplicate_entry_keys
        )

    @property
    def all_rows_defined(self) -> bool:
        return bool(self.rows) and not self.undefined_rows

    @property
    def signed_finite_row_checks_proved(self) -> bool:
        return (
            self.finite_row_checks_derived_from_tables
            and self.endpoint_group is not None
            and self.coordinate_components_verified
            == (not self.coordinate_component_failures)
            and self.inverse_pairing_verified == (not self.inverse_pairing_failures)
            and self.inverse_cancellation_verified
            == (not self.inverse_cancellation_failures)
            and self.positive_ybe_path_verified == (not self.positive_ybe_path_failures)
            and self.far_commutativity_verified
            == (not self.far_commutativity_path_failures)
            and self.positive_monodromy_representation_verified
        )

    @property
    def far_commutativity_path_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
        return tuple(
            failure
            for failure in self.far_commutativity_failures
            if failure[1] != "far_commutativity_label_mismatch"
        )

    @property
    def positive_ybe_label_diagnostic_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
        return tuple(
            failure
            for failure in self.positive_ybe_cocycle_failures
            if failure[1] == "positive_ybe_label_mismatch"
        )

    @property
    def far_commutativity_label_diagnostic_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
        return tuple(
            failure
            for failure in self.far_commutativity_failures
            if failure[1] == "far_commutativity_label_mismatch"
        )

    @property
    def cutoff_readouts_required(self) -> bool:
        return any(
            state[0] in {"C", "M"}
            for state in self.required_seed_states
            if _universal_k_endpoint_seed_state_well_formed(state)
        )

    @property
    def required_cutoff_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        return tuple(
            state
            for state in self.required_seed_states
            if _universal_k_endpoint_seed_state_well_formed(state)
            if state[0] in {"C", "M"}
        )

    @property
    def required_cutoff_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {endpoint_family for endpoint_family, _state in self.required_cutoff_seed_states},
                key=repr,
            )
        )

    @property
    def cutoff_readout_scope_matches_required(self) -> bool:
        return (
            self.cutoff_readout_audit is not None
            and set(self.cutoff_readout_audit.expected_cutoff_seed_states_exact)
            == set(self.required_cutoff_seed_states)
        )

    @property
    def endpoint_target_cutoff_degree_by_family(self) -> Mapping[str, int]:
        if self.endpoint_target_audit is None:
            return {}
        return dict(self.endpoint_target_audit.cutoff_degree_rows)

    @property
    def cutoff_target_degree_mismatches(
        self,
    ) -> Tuple[Tuple[str, int | None, int | None], ...]:
        if not self.cutoff_readouts_required:
            return ()
        target_degrees = self.endpoint_target_cutoff_degree_by_family
        readout_degree = (
            self.cutoff_readout_audit.cutoff_degree
            if self.cutoff_readout_audit is not None
            else None
        )
        return tuple(
            (family, target_degrees.get(family), readout_degree)
            for family in self.required_cutoff_families
            if target_degrees.get(family) != readout_degree
        )

    @property
    def cutoff_target_degrees_match_readout(self) -> bool:
        return not self.cutoff_readouts_required or (
            self.endpoint_target_audit is not None
            and self.cutoff_readout_audit is not None
            and not self.cutoff_target_degree_mismatches
        )

    @property
    def exact_cutoff_readouts_proved(self) -> bool:
        return not self.cutoff_readouts_required or (
            self.cutoff_readout_audit is not None
            and self.cutoff_readout_scope_matches_required
            and self.cutoff_target_degrees_match_readout
            and self.cutoff_readout_audit.proves_exact_cutoff_readouts
        )

    @property
    def required_endpoint_families(self) -> Tuple[str, ...]:
        return tuple(
            sorted(
                {
                    state[0]
                    for state in self.required_seed_states
                    if _universal_k_endpoint_seed_state_well_formed(state)
                },
                key=repr,
            )
        )

    @property
    def endpoint_target_scope_matches_required(self) -> bool:
        return (
            self.endpoint_target_audit is not None
            and set(self.endpoint_target_audit.expected_endpoint_families_exact)
            == set(self.required_endpoint_families)
        )

    @property
    def endpoint_targets_proved(self) -> bool:
        return not self.required_seed_states or (
            self.endpoint_target_audit is not None
            and self.endpoint_target_scope_matches_required
            and self.endpoint_target_audit.proves_endpoint_targets
            and self.endpoint_group_order_matches_target_audit
            and self.endpoint_group_family_support_proved
        )

    @property
    def endpoint_group_order_matches_target_audit(self) -> bool:
        if self.endpoint_group is None or self.endpoint_target_audit is None:
            return False
        group_orders = self.endpoint_target_audit.endpoint_group_order_rows
        if not group_orders:
            return True
        target_order = 1
        for _family, order in group_orders:
            if not _universal_k_positive_int(order):
                return False
            target_order *= order
        return len(self.endpoint_group.elements) == target_order

    @property
    def endpoint_group_target_families(self) -> Tuple[str, ...]:
        if self.endpoint_target_audit is None:
            return ()
        return tuple(
            family
            for family, order in self.endpoint_target_audit.endpoint_group_order_rows
            if family in UNIVERSAL_K_ENDPOINT_FAMILIES
            and _universal_k_positive_int(order)
        )

    @property
    def endpoint_group_family_support_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
        """Rows in a product endpoint group must emit only in their family factor."""

        if self.endpoint_group is None or self.endpoint_target_audit is None:
            return ()
        group_families = self.endpoint_group_target_families
        if len(group_families) <= 1:
            return ()
        identity = self.endpoint_group.identity
        if not isinstance(identity, tuple) or len(identity) != len(group_families):
            return tuple(
                (
                    row.entry_key,
                    "endpoint_group_identity_not_product_tuple",
                    identity,
                )
                for row in self.rows
                if row.endpoint_family in set(group_families)
            )
        failures = []
        family_position = {
            family: position for position, family in enumerate(group_families)
        }
        for row in self.rows:
            if row.endpoint_family not in family_position:
                continue
            value = row.endpoint_value
            if not isinstance(value, tuple) or len(value) != len(group_families):
                failures.append(
                    (
                        row.entry_key,
                        "endpoint_value_not_product_tuple",
                        value,
                    )
                )
                continue
            off_family_values = tuple(
                (family, value[position])
                for position, family in enumerate(group_families)
                if family != row.endpoint_family and value[position] != identity[position]
            )
            if off_family_values:
                failures.append(
                    (
                        row.entry_key,
                        "endpoint_value_has_off_family_components",
                        off_family_values,
                    )
                )
        return tuple(sorted(failures, key=repr))

    @property
    def endpoint_group_family_support_proved(self) -> bool:
        return not self.endpoint_group_family_support_failures

    @property
    def residual_action_scope_matches_required(self) -> bool:
        return (
            self.residual_action_scope is not None
            and set(self.residual_action_scope.active_endpoint_families)
            == set(self.required_endpoint_families)
        )

    @property
    def residual_action_scope_matches_seed_states(self) -> bool:
        return (
            self.residual_action_scope is not None
            and set(self.residual_action_scope.expected_endpoint_seed_states_exact)
            == set(self.required_seed_states)
        )

    @property
    def residual_action_scope_matches_action_rows(self) -> bool:
        return (
            self.residual_action_scope is not None
            and self.residual_action_audit is not None
            and self.residual_action_scope.expected_residual_row_count
            == self.residual_action_audit.expected_row_count
            and self.residual_action_scope.covered_residual_row_count
            == self.residual_action_audit.row_count
        )

    @property
    def residual_action_input_tuple_domain_exact(self) -> bool:
        return (
            self.residual_action_audit is not None
            and self.residual_action_audit.expected_input_tuple_domain_supplied
            and self.residual_action_audit.input_tuple_domain_exact
        )

    @property
    def residual_theorem_scope_matches_required(self) -> bool:
        return (
            self.residual_faithfulness_theorem is not None
            and set(self.residual_faithfulness_theorem.active_endpoint_families)
            == set(self.required_endpoint_families)
        )

    @property
    def residual_theorem_scope_matches_seed_states(self) -> bool:
        return (
            self.residual_faithfulness_theorem is not None
            and set(
                self.residual_faithfulness_theorem.expected_endpoint_seed_states_exact
            )
            == set(self.required_seed_states)
        )

    @property
    def residual_action_faithfulness_proved(self) -> bool:
        return (
            self.residual_action_audit is not None
            and self.residual_action_audit.expected_row_count is not None
            and self.residual_action_audit.proves_complete_residual_action_implication
            and self.residual_action_scope is not None
            and self.residual_action_scope_matches_required
            and self.residual_action_scope_matches_seed_states
            and self.residual_action_scope_matches_action_rows
            and self.residual_action_scope.proves_residual_action_scope
            and self.residual_action_input_tuple_domain_exact
        )

    @property
    def residual_theorem_faithfulness_proved(self) -> bool:
        return (
            self.residual_faithfulness_theorem is not None
            and self.residual_theorem_scope_matches_required
            and self.residual_theorem_scope_matches_seed_states
            and self.residual_faithfulness_theorem.proves_residual_faithfulness
        )

    @property
    def residual_faithfulness_proved(self) -> bool:
        return (
            self.residual_action_faithfulness_proved
            or self.residual_theorem_faithfulness_proved
        )

    @property
    def two_strand_witness_domain_exact(self) -> bool:
        return not self.two_strand_witness_domain_failures

    @property
    def telescoping_detector_scope_matches_required(self) -> bool:
        return (
            self.telescoping_detector_audit is not None
            and set(self.telescoping_detector_audit.expected_positive_entry_keys_exact)
            == set(self.required_positive_entry_keys_exact)
            and set(self.telescoping_detector_audit.expected_endpoint_seed_states_exact)
            == set(self.reachable_seed_states_exact)
        )

    @property
    def telescoping_detector_endpoint_group_matches(self) -> bool:
        return (
            self.endpoint_group is None
            or self.telescoping_detector_audit is None
            or self.telescoping_detector_audit.word_potential_certificate is None
            or self.telescoping_detector_audit.word_potential_certificate.endpoint_group
            == self.endpoint_group
        )

    @property
    def telescoping_detector_extra_diagnostic_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        if self.telescoping_detector_audit is None:
            return ()
        required = set(self.required_entry_keys_exact)
        candidate_keys = (
            set(self.telescoping_detector_audit.expected_entry_keys_exact)
            | set(self.telescoping_detector_audit.covered_entry_keys_exact)
        )
        if self.telescoping_detector_audit.word_potential_certificate is not None:
            candidate_keys |= set(
                self.telescoping_detector_audit
                .word_potential_certificate.identity_entry_keys_exact
            )
        return tuple(sorted(candidate_keys - required, key=repr))

    @property
    def telescoping_detector_diagnostic_entries_in_signed_domain(self) -> bool:
        return not self.telescoping_detector_extra_diagnostic_entry_keys

    @property
    def word_potential_initial_seed_states_normalized(self) -> bool:
        if (
            self.telescoping_detector_audit is None
            or self.telescoping_detector_audit.word_potential_certificate is None
        ):
            return False
        certificate = self.telescoping_detector_audit.word_potential_certificate
        normalized = set(certificate.normalized_seed_states_exact)
        return (
            bool(self.required_seed_states)
            and set(self.required_seed_states).issubset(normalized)
        )

    @property
    def normalized_word_potential_seed_states_exact(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        if (
            self.telescoping_detector_audit is None
            or self.telescoping_detector_audit.word_potential_certificate is None
        ):
            return ()
        return (
            self.telescoping_detector_audit.word_potential_certificate
            .normalized_seed_states_exact
        )

    @property
    def missing_initial_normalized_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        normalized = set(self.normalized_word_potential_seed_states_exact)
        return tuple(
            state for state in self.required_seed_states if state not in normalized
        )

    @property
    def extra_initial_normalized_seed_states(
        self,
    ) -> Tuple[Tuple[str, UniversalKSeedState], ...]:
        required = set(self.required_seed_states)
        return tuple(
            state
            for state in self.normalized_word_potential_seed_states_exact
            if state not in required
        )

    @property
    def word_potential_initial_seed_state_scope_exact(self) -> bool:
        return (
            bool(self.required_seed_states)
            and not self.missing_initial_normalized_seed_states
            and not self.extra_initial_normalized_seed_states
        )

    @property
    def telescoping_detector_signed_row_mismatches(
        self,
    ) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
        if (
            self.telescoping_detector_audit is None
            or self.telescoping_detector_audit.word_potential_certificate is None
        ):
            return ()
        identity_rows = (
            self.telescoping_detector_audit.word_potential_certificate.identity_row_map
        )
        failures = []
        for row in self.rows:
            if row.sign != 1:
                continue
            identity_row = identity_rows.get(row.entry_key)
            if identity_row is None:
                continue
            if (
                identity_row.next_seed_state != row.next_seed_state
                or identity_row.endpoint_value != row.endpoint_value
            ):
                failures.append(
                    (
                        row.entry_key,
                        "word_potential_row_mismatch",
                        (
                            (row.next_seed_state, row.endpoint_value),
                            (
                                identity_row.next_seed_state,
                                identity_row.endpoint_value,
                            ),
                        ),
                    )
                )
        return tuple(failures)

    @property
    def telescoping_detector_proved(self) -> bool:
        return (
            self.telescoping_detector_audit is not None
            and self.telescoping_detector_scope_matches_required
            and self.telescoping_detector_endpoint_group_matches
            and self.telescoping_detector_diagnostic_entries_in_signed_domain
            and self.word_potential_initial_seed_states_normalized
            and self.word_potential_initial_seed_state_scope_exact
            and not self.telescoping_detector_signed_row_mismatches
            and self.telescoping_detector_audit.proves_telescoping_detector_lift
        )

    @property
    def proves_signed_endpoint_generator_tables(self) -> bool:
        return (
            self.signed_generator_domain_exact
            and self.all_rows_defined
            and self.signed_finite_row_checks_proved
            and self.endpoint_targets_proved
            and self.coordinate_components_verified
            and self.inverse_pairing_verified
            and self.inverse_cancellation_verified
            and self.positive_ybe_path_verified
            and self.far_commutativity_verified
            and self.telescoping_detector_proved
            and self.exact_cutoff_readouts_proved
            and self.residual_faithfulness_proved
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.required_seed_states:
            reasons.append("no_routed_k_seed_states")
        if self.duplicate_seed_classifier_entries:
            reasons.append("seed_classifier_duplicate_entries")
        if self.duplicate_seed_classifier_descriptors:
            reasons.append("seed_classifier_duplicate_descriptors")
        if self.conflicting_seed_classifier_descriptors:
            reasons.append("seed_classifier_conflicting_descriptors")
        if self.invalid_seed_classifier_targets:
            reasons.append("seed_classifier_targets_unknown_endpoint_family")
        if not self.reachable_seed_states_exact:
            reasons.append("reachable_seed_states_not_supplied")
        if self.duplicate_reachable_seed_states:
            reasons.append("reachable_seed_states_duplicate_entries")
        if self.invalid_reachable_seed_states:
            reasons.append("reachable_seed_states_unknown_endpoint_family")
        if self.missing_initial_seed_states:
            reasons.append("reachable_seed_states_missing_initial_seeds")
        if self.missing_transition_reachable_seed_states:
            reasons.append("reachable_seed_states_missing_transition_closure")
        if self.unreachable_declared_seed_states:
            reasons.append("reachable_seed_states_have_unreachable_extras")
        if self.row_states_outside_reachable_set:
            reasons.append("signed_generator_row_state_outside_reachable_set")
        if not self.required_entry_keys_exact:
            reasons.append("signed_entry_domain_not_supplied")
        if self.required_entry_keys_exact and not self.entry_domain_derived_from_interval:
            reasons.append("signed_entry_domain_not_derived_from_interval")
        if self.missing_required_entry_seed_keys:
            reasons.append("signed_entry_domain_missing_seed_keys")
        if self.extra_required_entry_seed_keys:
            reasons.append("signed_entry_domain_has_extra_seed_keys")
        if self.missing_signed_seed_keys:
            reasons.append("signed_seed_keys_missing")
        if self.extra_signed_seed_keys:
            reasons.append("extra_signed_seed_keys")
        if self.missing_entry_keys:
            reasons.append("signed_generator_entries_missing")
        if self.extra_entry_keys:
            reasons.append("extra_signed_generator_entries")
        if self.duplicate_entry_keys:
            reasons.append("duplicate_signed_generator_entries")
        if self.undefined_rows:
            reasons.append("undefined_signed_generator_rows")
        if not self.finite_row_checks_derived_from_tables:
            reasons.append("finite_signed_row_checks_not_derived_from_tables")
        if self.finite_row_checks_derived_from_tables and self.endpoint_group is None:
            reasons.append("finite_signed_row_checks_missing_endpoint_group")
        if self.finite_row_checks_derived_from_tables and not self.signed_finite_row_checks_proved:
            reasons.append("finite_signed_row_checks_inconsistent")
        if (
            self.monodromy_representation_audit is not None
            and not self.monodromy_representation_audit.proves_monodromy_representation
        ):
            reasons.append("explicit_endpoint_monodromy_representation_not_verified")
            reasons.extend(self.monodromy_representation_audit.failure_reasons)
        if self.positive_monodromy_permutation_failures:
            reasons.append("endpoint_monodromy_not_permutation_representation")
        if not self.endpoint_targets_proved:
            reasons.append("endpoint_targets_not_fixed")
            if self.required_seed_states and self.endpoint_target_audit is None:
                reasons.append("endpoint_target_audit_missing")
            if (
                self.endpoint_target_audit is not None
                and not self.endpoint_target_scope_matches_required
            ):
                reasons.append("endpoint_target_scope_mismatch")
            if (
                self.endpoint_target_audit is not None
                and not self.endpoint_group_order_matches_target_audit
            ):
                reasons.append("endpoint_target_group_order_mismatch")
            if not self.endpoint_group_family_support_proved:
                reasons.append("endpoint_group_family_support_mismatch")
            if self.endpoint_target_audit is not None:
                reasons.extend(self.endpoint_target_audit.failure_reasons)
        if not self.coordinate_components_verified:
            reasons.append("coordinate_components_not_verified")
        if not self.inverse_pairing_verified:
            reasons.append("inverse_pairing_not_verified")
        if not self.inverse_cancellation_verified:
            reasons.append("inverse_cancellation_not_verified")
        if not self.positive_ybe_path_verified:
            reasons.append("positive_ybe_path_not_verified")
        if not self.far_commutativity_verified:
            reasons.append("far_commutativity_not_verified")
        if not self.telescoping_detector_proved:
            reasons.append("detector_lift_telescoping_not_verified")
            if self.required_seed_states and self.telescoping_detector_audit is None:
                reasons.append("telescoping_detector_audit_missing")
            if self.telescoping_detector_audit is not None:
                if not self.telescoping_detector_scope_matches_required:
                    reasons.append("telescoping_detector_scope_mismatch")
                if not self.telescoping_detector_endpoint_group_matches:
                    reasons.append("telescoping_detector_endpoint_group_mismatch")
                if not self.telescoping_detector_diagnostic_entries_in_signed_domain:
                    reasons.append(
                        "telescoping_detector_diagnostic_rows_outside_signed_domain"
                    )
                if not self.word_potential_initial_seed_states_normalized:
                    reasons.append("word_potential_initial_seed_states_not_normalized")
                if not self.word_potential_initial_seed_state_scope_exact:
                    reasons.append("word_potential_initial_seed_state_scope_not_exact")
                if self.missing_initial_normalized_seed_states:
                    reasons.append("word_potential_initial_seed_states_missing")
                if self.extra_initial_normalized_seed_states:
                    reasons.append("word_potential_initial_seed_states_extra")
                if self.telescoping_detector_signed_row_mismatches:
                    reasons.append("telescoping_detector_signed_row_mismatch")
                reasons.extend(self.telescoping_detector_audit.failure_reasons)
        if not self.exact_cutoff_readouts_proved:
            reasons.append("cutoff_readouts_not_exact")
            if self.cutoff_readouts_required and self.cutoff_readout_audit is None:
                reasons.append("cutoff_readout_audit_missing")
            if (
                self.cutoff_readout_audit is not None
                and not self.cutoff_readout_scope_matches_required
            ):
                reasons.append("cutoff_readout_scope_mismatch")
            if (
                self.endpoint_target_audit is not None
                and self.cutoff_readout_audit is not None
                and not self.cutoff_target_degrees_match_readout
            ):
                reasons.append("cutoff_readout_target_degree_mismatch")
            if self.cutoff_readout_audit is not None:
                reasons.extend(self.cutoff_readout_audit.failure_reasons)
        if not self.residual_faithfulness_proved:
            reasons.append("residual_faithfulness_not_verified")
            if self.residual_action_audit is not None:
                if self.residual_action_scope is None:
                    reasons.append("residual_action_scope_missing")
                else:
                    if not self.residual_action_scope_matches_required:
                        reasons.append("residual_action_scope_mismatch")
                    if not self.residual_action_scope_matches_seed_states:
                        reasons.append("residual_action_scope_seed_state_mismatch")
                    if not self.residual_action_scope_matches_action_rows:
                        reasons.append("residual_action_scope_row_count_mismatch")
                    if not self.residual_action_input_tuple_domain_exact:
                        reasons.append("residual_action_input_tuple_domain_not_exact")
                    reasons.extend(self.residual_action_scope.failure_reasons)
            if self.residual_faithfulness_theorem is not None:
                if not self.residual_theorem_scope_matches_required:
                    reasons.append("residual_theorem_scope_mismatch")
                if not self.residual_theorem_scope_matches_seed_states:
                    reasons.append("residual_theorem_seed_state_mismatch")
                reasons.extend(self.residual_faithfulness_theorem.failure_reasons)
        return tuple(reasons)


def universal_k_signed_endpoint_required_entry_keys(
    interval: LocalInterval,
    reachable_seed_states: Sequence[Tuple[str, UniversalKSeedState]],
) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
    """Derive the full D_Gamma row domain from interval fibres and states."""

    keys = []
    for endpoint_family, seed_state in reachable_seed_states:
        for sign in (-1, 1):
            for left_color, right_color in product(interval.colors, repeat=2):
                for input_left in interval.fibres[left_color]:
                    for input_right in interval.fibres[right_color]:
                        keys.append(
                            (
                                endpoint_family,
                                seed_state,
                                sign,
                                left_color,
                                right_color,
                                input_left,
                                input_right,
                            )
                        )
    return tuple(sorted(set(keys), key=repr))


def universal_k_signed_endpoint_coordinate_failures(
    interval: LocalInterval,
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> Tuple[UniversalKSignedEndpointCoordinateFailure, ...]:
    """Return signed table rows whose fibre component is not T or T inverse."""

    inverse_base = {target: source for source, target in interval.base_R.items()}
    failures = []
    for row in rows:
        output_pair = (row.output_left, row.output_right)
        input_pair = (row.input_left, row.input_right)
        if row.sign == 1:
            expected = interval.T.get(
                (
                    row.left_color,
                    row.right_color,
                    row.input_left,
                    row.input_right,
                )
            )
            if expected is None:
                failures.append((row.entry_key, "positive_input_outside_domain", None))
            elif output_pair != expected:
                failures.append((row.entry_key, "positive_coordinate_mismatch", expected))
            continue
        if row.sign == -1:
            source_colors = inverse_base.get((row.left_color, row.right_color))
            if source_colors is None:
                failures.append((row.entry_key, "negative_color_pair_not_in_image", None))
                continue
            source_left, source_right = source_colors
            if (
                row.output_left not in interval.fibres[source_left]
                or row.output_right not in interval.fibres[source_right]
            ):
                failures.append(
                    (
                        row.entry_key,
                        "negative_output_outside_inverse_domain",
                        source_colors,
                    )
                )
                continue
            forward = interval.T[
                (source_left, source_right, row.output_left, row.output_right)
            ]
            if forward != input_pair:
                failures.append((row.entry_key, "negative_coordinate_mismatch", forward))
            continue
        failures.append((row.entry_key, "unknown_sign", row.sign))
    return tuple(failures)


def universal_k_signed_endpoint_inverse_failures(
    interval: LocalInterval,
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> Tuple[UniversalKSignedEndpointInverseFailure, ...]:
    """Return signed rows whose opposite-sign inverse row is absent or wrong."""

    inverse_base = {target: source for source, target in interval.base_R.items()}
    row_by_key = {}
    duplicate_keys = set()
    for row in rows:
        if row.entry_key in row_by_key:
            duplicate_keys.add(row.entry_key)
            continue
        row_by_key[row.entry_key] = row

    failures = [
        (key, "duplicate_entry_key", None)
        for key in sorted(duplicate_keys, key=repr)
    ]
    for row in rows:
        input_pair = (row.input_left, row.input_right)
        if row.sign == 1:
            target_colors = interval.base_R.get((row.left_color, row.right_color))
            if target_colors is None:
                failures.append((row.entry_key, "positive_color_pair_outside_base", None))
                continue
            expected_key = (
                row.endpoint_family,
                row.next_seed_state,
                -1,
                target_colors[0],
                target_colors[1],
                row.output_left,
                row.output_right,
            )
            inverse_row = row_by_key.get(expected_key)
            if inverse_row is None:
                failures.append(
                    (row.entry_key, "missing_negative_inverse_row", expected_key)
                )
                continue
            if (
                inverse_row.next_seed_state != row.seed_state
                or (inverse_row.output_left, inverse_row.output_right) != input_pair
            ):
                failures.append(
                    (
                        row.entry_key,
                        "negative_inverse_does_not_return",
                        (
                            inverse_row.next_seed_state,
                            inverse_row.output_left,
                            inverse_row.output_right,
                        ),
                    )
                )
            continue
        if row.sign == -1:
            source_colors = inverse_base.get((row.left_color, row.right_color))
            if source_colors is None:
                failures.append((row.entry_key, "negative_color_pair_not_in_image", None))
                continue
            expected_key = (
                row.endpoint_family,
                row.next_seed_state,
                1,
                source_colors[0],
                source_colors[1],
                row.output_left,
                row.output_right,
            )
            inverse_row = row_by_key.get(expected_key)
            if inverse_row is None:
                failures.append(
                    (row.entry_key, "missing_positive_inverse_row", expected_key)
                )
                continue
            if (
                inverse_row.next_seed_state != row.seed_state
                or (inverse_row.output_left, inverse_row.output_right) != input_pair
            ):
                failures.append(
                    (
                        row.entry_key,
                        "positive_inverse_does_not_return",
                        (
                            inverse_row.next_seed_state,
                            inverse_row.output_left,
                            inverse_row.output_right,
                        ),
                    )
                )
            continue
        failures.append((row.entry_key, "unknown_sign", row.sign))
    return tuple(failures)


def universal_k_signed_endpoint_inverse_cancellation_failures(
    endpoint_group: FiniteGroup,
    interval: LocalInterval,
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
    """Return signed inverse pairs whose endpoint labels do not cancel."""

    inverse_base = {target: source for source, target in interval.base_R.items()}
    row_by_key = {}
    duplicate_keys = set()
    group_elements = set(endpoint_group.elements)
    failures = []
    for row in rows:
        if row.entry_key in row_by_key:
            duplicate_keys.add(row.entry_key)
            continue
        row_by_key[row.entry_key] = row
        if row.endpoint_value not in group_elements:
            failures.append(
                (row.entry_key, "endpoint_value_outside_group", row.endpoint_value)
            )

    failures.extend(
        (key, "duplicate_entry_key", None)
        for key in sorted(duplicate_keys, key=repr)
    )
    for row in rows:
        if row.endpoint_value not in group_elements:
            continue
        if row.sign == 1:
            target_colors = interval.base_R.get((row.left_color, row.right_color))
            if target_colors is None:
                failures.append((row.entry_key, "positive_color_pair_outside_base", None))
                continue
            expected_key = (
                row.endpoint_family,
                row.next_seed_state,
                -1,
                target_colors[0],
                target_colors[1],
                row.output_left,
                row.output_right,
            )
            inverse_row = row_by_key.get(expected_key)
            if inverse_row is None:
                failures.append(
                    (row.entry_key, "missing_negative_inverse_row", expected_key)
                )
                continue
            if inverse_row.endpoint_value not in group_elements:
                continue
            label_product = endpoint_group.mul(
                row.endpoint_value,
                inverse_row.endpoint_value,
            )
            if label_product != endpoint_group.identity:
                failures.append(
                    (
                        row.entry_key,
                        "negative_inverse_label_mismatch",
                        label_product,
                    )
                )
            continue
        if row.sign == -1:
            source_colors = inverse_base.get((row.left_color, row.right_color))
            if source_colors is None:
                failures.append((row.entry_key, "negative_color_pair_not_in_image", None))
                continue
            expected_key = (
                row.endpoint_family,
                row.next_seed_state,
                1,
                source_colors[0],
                source_colors[1],
                row.output_left,
                row.output_right,
            )
            inverse_row = row_by_key.get(expected_key)
            if inverse_row is None:
                failures.append(
                    (row.entry_key, "missing_positive_inverse_row", expected_key)
                )
                continue
            if inverse_row.endpoint_value not in group_elements:
                continue
            label_product = endpoint_group.mul(
                row.endpoint_value,
                inverse_row.endpoint_value,
            )
            if label_product != endpoint_group.identity:
                failures.append(
                    (
                        row.entry_key,
                        "positive_inverse_label_mismatch",
                        label_product,
                    )
                )
            continue
        failures.append((row.entry_key, "unknown_sign", row.sign))
    return tuple(failures)


def universal_k_signed_endpoint_positive_ybe_failures(
    interval: LocalInterval,
    reachable_seed_states: Sequence[Tuple[str, UniversalKSeedState]],
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> Tuple[UniversalKSignedEndpointPositiveYBEFailure, ...]:
    """Return positive 121/212 endpoint-table path mismatches."""

    row_by_key = {}
    duplicate_keys = set()
    for row in rows:
        if row.sign != 1:
            continue
        if row.entry_key in row_by_key:
            duplicate_keys.add(row.entry_key)
            continue
        row_by_key[row.entry_key] = row

    failures = [
        (key, "duplicate_positive_entry_key", None)
        for key in sorted(duplicate_keys, key=repr)
    ]

    def run_path(
        endpoint_family: str,
        seed_state: UniversalKSeedState,
        start_colors: Tuple[Color, Color, Color],
        start_fibres: Tuple[FibrePoint, FibrePoint, FibrePoint],
        indices: Tuple[int, int, int],
    ) -> Tuple[
        Tuple[UniversalKSeedState, Tuple[Color, ...], Tuple[FibrePoint, ...]] | None,
        UniversalKSignedEndpointPositiveYBEFailure | None,
    ]:
        state = seed_state
        colors = tuple(start_colors)
        fibres = tuple(start_fibres)
        for step, index in enumerate(indices):
            key = (
                endpoint_family,
                state,
                1,
                colors[index],
                colors[index + 1],
                fibres[index],
                fibres[index + 1],
            )
            row = row_by_key.get(key)
            if row is None:
                return None, (
                    key,
                    "missing_positive_ybe_row",
                    (indices, step, colors, fibres),
                )
            target_colors = interval.base_R.get((row.left_color, row.right_color))
            if target_colors is None:
                return None, (
                    key,
                    "positive_color_pair_outside_base",
                    (indices, step),
                )
            next_colors = list(colors)
            next_fibres = list(fibres)
            next_colors[index], next_colors[index + 1] = target_colors
            next_fibres[index], next_fibres[index + 1] = (
                row.output_left,
                row.output_right,
            )
            state = row.next_seed_state
            colors = tuple(next_colors)
            fibres = tuple(next_fibres)
        return (state, colors, fibres), None

    for endpoint_family, seed_state in sorted(set(reachable_seed_states), key=repr):
        for a, b, c in product(interval.colors, repeat=3):
            for x, y, z in product(
                interval.fibres[a],
                interval.fibres[b],
                interval.fibres[c],
            ):
                start_colors = (a, b, c)
                start_fibres = (x, y, z)
                left_result, left_failure = run_path(
                    endpoint_family,
                    seed_state,
                    start_colors,
                    start_fibres,
                    (0, 1, 0),
                )
                right_result, right_failure = run_path(
                    endpoint_family,
                    seed_state,
                    start_colors,
                    start_fibres,
                    (1, 0, 1),
                )
                if left_failure is not None:
                    failures.append(left_failure)
                if right_failure is not None:
                    failures.append(right_failure)
                if (
                    left_failure is None
                    and right_failure is None
                    and left_result != right_result
                ):
                    failures.append(
                        (
                            (
                                endpoint_family,
                                seed_state,
                                a,
                                b,
                                c,
                                x,
                                y,
                                z,
                            ),
                            "positive_ybe_terminal_mismatch",
                            (left_result, right_result),
                        )
                    )
    return tuple(failures)


def universal_k_signed_endpoint_positive_ybe_cocycle_failures(
    endpoint_group: FiniteGroup,
    interval: LocalInterval,
    reachable_seed_states: Sequence[Tuple[str, UniversalKSeedState]],
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
    """Return positive 121/212 endpoint label cocycle mismatches."""

    row_by_key = {}
    duplicate_keys = set()
    group_elements = set(endpoint_group.elements)
    failures = []
    for row in rows:
        if row.sign != 1:
            continue
        if row.entry_key in row_by_key:
            duplicate_keys.add(row.entry_key)
            continue
        row_by_key[row.entry_key] = row
        if row.endpoint_value not in group_elements:
            failures.append(
                (row.entry_key, "endpoint_value_outside_group", row.endpoint_value)
            )

    failures.extend(
        (key, "duplicate_positive_entry_key", None)
        for key in sorted(duplicate_keys, key=repr)
    )

    def run_path(
        endpoint_family: str,
        seed_state: UniversalKSeedState,
        start_colors: Tuple[Color, Color, Color],
        start_fibres: Tuple[FibrePoint, FibrePoint, FibrePoint],
        indices: Tuple[int, int, int],
    ) -> Tuple[
        Tuple[
            UniversalKSeedState,
            Tuple[Color, ...],
            Tuple[FibrePoint, ...],
            GroupElement,
        ]
        | None,
        UniversalKSignedEndpointLabelFailure | None,
    ]:
        state = seed_state
        colors = tuple(start_colors)
        fibres = tuple(start_fibres)
        label_product = endpoint_group.identity
        for step, index in enumerate(indices):
            key = (
                endpoint_family,
                state,
                1,
                colors[index],
                colors[index + 1],
                fibres[index],
                fibres[index + 1],
            )
            row = row_by_key.get(key)
            if row is None:
                return None, (
                    key,
                    "missing_positive_ybe_row",
                    (indices, step, colors, fibres),
                )
            if row.endpoint_value not in group_elements:
                return None, (
                    key,
                    "endpoint_value_outside_group",
                    row.endpoint_value,
                )
            target_colors = interval.base_R.get((row.left_color, row.right_color))
            if target_colors is None:
                return None, (
                    key,
                    "positive_color_pair_outside_base",
                    (indices, step),
                )
            label_product = endpoint_group.mul(label_product, row.endpoint_value)
            next_colors = list(colors)
            next_fibres = list(fibres)
            next_colors[index], next_colors[index + 1] = target_colors
            next_fibres[index], next_fibres[index + 1] = (
                row.output_left,
                row.output_right,
            )
            state = row.next_seed_state
            colors = tuple(next_colors)
            fibres = tuple(next_fibres)
        return (state, colors, fibres, label_product), None

    for endpoint_family, seed_state in sorted(set(reachable_seed_states), key=repr):
        for a, b, c in product(interval.colors, repeat=3):
            for x, y, z in product(
                interval.fibres[a],
                interval.fibres[b],
                interval.fibres[c],
            ):
                start_colors = (a, b, c)
                start_fibres = (x, y, z)
                left_result, left_failure = run_path(
                    endpoint_family,
                    seed_state,
                    start_colors,
                    start_fibres,
                    (0, 1, 0),
                )
                right_result, right_failure = run_path(
                    endpoint_family,
                    seed_state,
                    start_colors,
                    start_fibres,
                    (1, 0, 1),
                )
                if left_failure is not None:
                    failures.append(left_failure)
                if right_failure is not None:
                    failures.append(right_failure)
                if left_failure is not None or right_failure is not None:
                    continue
                assert left_result is not None
                assert right_result is not None
                if left_result[:3] != right_result[:3]:
                    failures.append(
                        (
                            (
                                endpoint_family,
                                seed_state,
                                a,
                                b,
                                c,
                                x,
                                y,
                                z,
                            ),
                            "positive_ybe_terminal_mismatch",
                            (left_result[:3], right_result[:3]),
                        )
                    )
                    continue
                if left_result[3] != right_result[3]:
                    failures.append(
                        (
                            (
                                endpoint_family,
                                seed_state,
                                a,
                                b,
                                c,
                                x,
                                y,
                                z,
                            ),
                            "positive_ybe_label_mismatch",
                            (left_result[3], right_result[3]),
                        )
                    )
    return tuple(failures)


def universal_k_signed_endpoint_far_commutativity_failures(
    endpoint_group: FiniteGroup,
    interval: LocalInterval,
    reachable_seed_states: Sequence[Tuple[str, UniversalKSeedState]],
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
    """Return disjoint-crossing endpoint path or label mismatches."""

    inverse_base = {target: source for source, target in interval.base_R.items()}
    row_by_key = {}
    duplicate_keys = set()
    for row in rows:
        if row.entry_key in row_by_key:
            duplicate_keys.add(row.entry_key)
            continue
        row_by_key[row.entry_key] = row

    failures: list[UniversalKSignedEndpointLabelFailure] = [
        (key, "duplicate_far_commutativity_entry_key", None)
        for key in sorted(duplicate_keys, key=repr)
    ]
    group_elements = set(endpoint_group.elements)

    def run_step(
        endpoint_family: str,
        state: UniversalKSeedState,
        colors: Tuple[Color, Color, Color, Color],
        fibres: Tuple[FibrePoint, FibrePoint, FibrePoint, FibrePoint],
        position: int,
        sign: int,
    ) -> Tuple[
        Tuple[
            UniversalKSeedState,
            Tuple[Color, Color, Color, Color],
            Tuple[FibrePoint, FibrePoint, FibrePoint, FibrePoint],
            GroupElement,
        ]
        | None,
        UniversalKSignedEndpointLabelFailure | None,
    ]:
        key = (
            endpoint_family,
            state,
            sign,
            colors[position],
            colors[position + 1],
            fibres[position],
            fibres[position + 1],
        )
        row = row_by_key.get(key)
        if row is None:
            return None, (
                key,
                "missing_far_commutativity_row",
                (position, colors, fibres),
            )
        if row.endpoint_value not in group_elements:
            return None, (
                key,
                "endpoint_value_outside_group",
                row.endpoint_value,
            )
        if sign == 1:
            target_colors = interval.base_R.get((row.left_color, row.right_color))
            if target_colors is None:
                return None, (key, "positive_color_pair_outside_base", None)
        elif sign == -1:
            target_colors = inverse_base.get((row.left_color, row.right_color))
            if target_colors is None:
                return None, (key, "negative_color_pair_not_in_image", None)
        else:
            return None, (key, "unknown_sign", sign)

        next_colors = list(colors)
        next_fibres = list(fibres)
        next_colors[position], next_colors[position + 1] = target_colors
        next_fibres[position], next_fibres[position + 1] = (
            row.output_left,
            row.output_right,
        )
        next_color_tuple = tuple(next_colors)
        next_fibre_tuple = tuple(next_fibres)
        return (
            row.next_seed_state,
            next_color_tuple,
            next_fibre_tuple,
            row.endpoint_value,
        ), None

    def run_path(
        endpoint_family: str,
        seed_state: UniversalKSeedState,
        start_colors: Tuple[Color, Color, Color, Color],
        start_fibres: Tuple[FibrePoint, FibrePoint, FibrePoint, FibrePoint],
        steps: Tuple[Tuple[int, int], Tuple[int, int]],
    ) -> Tuple[
        Tuple[
            UniversalKSeedState,
            Tuple[Color, Color, Color, Color],
            Tuple[FibrePoint, FibrePoint, FibrePoint, FibrePoint],
            GroupElement,
        ]
        | None,
        UniversalKSignedEndpointLabelFailure | None,
    ]:
        state = seed_state
        colors = start_colors
        fibres = start_fibres
        label_product = endpoint_group.identity
        for position, sign in steps:
            result, failure = run_step(
                endpoint_family,
                state,
                colors,
                fibres,
                position,
                sign,
            )
            if failure is not None:
                return None, failure
            assert result is not None
            state, colors, fibres, label = result
            label_product = endpoint_group.mul(label_product, label)
        return (state, colors, fibres, label_product), None

    for endpoint_family, seed_state in sorted(set(reachable_seed_states), key=repr):
        for colors in product(interval.colors, repeat=4):
            fibre_ranges = tuple(interval.fibres[color] for color in colors)
            for fibres in product(*fibre_ranges):
                start_colors = tuple(colors)
                start_fibres = tuple(fibres)
                for left_sign, right_sign in product((-1, 1), repeat=2):
                    left_result, left_failure = run_path(
                        endpoint_family,
                        seed_state,
                        start_colors,
                        start_fibres,
                        ((0, left_sign), (2, right_sign)),
                    )
                    right_result, right_failure = run_path(
                        endpoint_family,
                        seed_state,
                        start_colors,
                        start_fibres,
                        ((2, right_sign), (0, left_sign)),
                    )
                    if left_failure is not None:
                        failures.append(left_failure)
                    if right_failure is not None:
                        failures.append(right_failure)
                    if left_failure is not None or right_failure is not None:
                        continue
                    assert left_result is not None
                    assert right_result is not None
                    context = (
                        endpoint_family,
                        seed_state,
                        left_sign,
                        right_sign,
                        *start_colors,
                        *start_fibres,
                    )
                    if left_result[:3] != right_result[:3]:
                        failures.append(
                            (
                                context,
                                "far_commutativity_terminal_mismatch",
                                (left_result[:3], right_result[:3]),
                            )
                        )
                        continue
                    if left_result[3] != right_result[3]:
                        failures.append(
                            (
                                context,
                                "far_commutativity_label_mismatch",
                                (left_result[3], right_result[3]),
                            )
                        )
    return tuple(failures)


def universal_k_signed_endpoint_two_strand_base_failures(
    endpoint_group: FiniteGroup,
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
    witnesses: Mapping[
        UniversalKSignedEndpointEntryKey,
        LongitudeSubgroupWitness,
    ],
) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
    """Return rows whose signed two-strand longitude witness is missing or wrong."""

    duplicate_keys = set()
    seen_keys = set()
    group_elements = set(endpoint_group.elements)
    failures = []
    for row in rows:
        if row.entry_key in seen_keys:
            duplicate_keys.add(row.entry_key)
            continue
        seen_keys.add(row.entry_key)
        if row.endpoint_value not in group_elements:
            failures.append(
                (row.entry_key, "endpoint_value_outside_group", row.endpoint_value)
            )
            continue
        if row.sign not in {-1, 1}:
            failures.append((row.entry_key, "unknown_sign", row.sign))
            continue
        if row.entry_key not in witnesses:
            failures.append((row.entry_key, "missing_two_strand_base_witness", None))
            continue
        braid_word = (1,) if row.sign == 1 else (-1,)
        try:
            witness_value = evaluate_longitude_subgroup_witness(
                endpoint_group,
                2,
                braid_word,
                witnesses[row.entry_key],
            )
        except (IndexError, ValueError) as error:
            failures.append(
                (row.entry_key, "invalid_two_strand_base_witness", repr(error))
            )
            continue
        if witness_value != row.endpoint_value:
            failures.append(
                (
                    row.entry_key,
                    "two_strand_base_value_mismatch",
                    (row.endpoint_value, witness_value),
                )
            )

    failures.extend(
        (key, "duplicate_entry_key", None)
        for key in sorted(duplicate_keys, key=repr)
    )
    extra_keys = tuple(sorted(set(witnesses) - seen_keys, key=repr))
    failures.extend(
        (key, "extra_two_strand_base_witness", None)
        for key in extra_keys
    )
    return tuple(failures)


def universal_k_signed_endpoint_two_strand_witness_domain_failures(
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
    witnesses: Mapping[
        UniversalKSignedEndpointEntryKey,
        LongitudeSubgroupWitness,
    ],
) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
    """Return missing or extra longitude witness keys for the signed row domain."""

    row_keys = {row.entry_key for row in rows}
    witness_keys = set(witnesses)
    failures = [
        (key, "missing_two_strand_witness_domain_entry", None)
        for key in sorted(row_keys - witness_keys, key=repr)
    ]
    failures.extend(
        (key, "extra_two_strand_witness_domain_entry", None)
        for key in sorted(witness_keys - row_keys, key=repr)
    )
    return tuple(failures)


def _precompose_two_strand_assignment(
    endpoint_group: FiniteGroup,
    assignment: Sequence[GroupElement],
    signed_generator: int,
) -> Tuple[GroupElement, GroupElement]:
    assignment_tuple = tuple(assignment)
    if len(assignment_tuple) != 2:
        raise ValueError("two-strand assignments must have length 2")
    if any(value not in endpoint_group.elements for value in assignment_tuple):
        raise ValueError("assignment contains a value outside the group")
    images = artin_generator_images(
        2,
        0,
        inverse=signed_generator < 0,
    )
    return tuple(
        evaluate_free_word(endpoint_group, assignment_tuple, image)
        for image in images
    )


def universal_k_signed_endpoint_artin_update_failures(
    endpoint_group: FiniteGroup,
    interval: LocalInterval,
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
    witnesses: Mapping[
        UniversalKSignedEndpointEntryKey,
        LongitudeSubgroupWitness,
    ],
) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
    """Return rows whose literal witnesses do not satisfy Artin precomposition."""

    inverse_base = {target: source for source, target in interval.base_R.items()}
    row_keys = {row.entry_key for row in rows}
    failures = []
    for row in rows:
        if row.sign == 1:
            target_colors = interval.base_R.get((row.left_color, row.right_color))
            if target_colors is None:
                failures.append((row.entry_key, "positive_color_pair_outside_base", None))
                continue
            target_key = (
                row.endpoint_family,
                row.next_seed_state,
                1,
                target_colors[0],
                target_colors[1],
                row.output_left,
                row.output_right,
            )
            precompose_sign = -1
        elif row.sign == -1:
            source_colors = inverse_base.get((row.left_color, row.right_color))
            if source_colors is None:
                failures.append((row.entry_key, "negative_color_pair_not_in_image", None))
                continue
            target_key = (
                row.endpoint_family,
                row.next_seed_state,
                -1,
                source_colors[0],
                source_colors[1],
                row.output_left,
                row.output_right,
            )
            precompose_sign = 1
        else:
            failures.append((row.entry_key, "unknown_sign", row.sign))
            continue

        source_witness = witnesses.get(row.entry_key)
        if source_witness is None:
            failures.append((row.entry_key, "missing_artin_update_source_witness", None))
            continue
        if target_key not in row_keys:
            failures.append((row.entry_key, "missing_artin_update_target_row", target_key))
            continue
        target_witness = witnesses.get(target_key)
        if target_witness is None:
            failures.append((row.entry_key, "missing_artin_update_target_witness", target_key))
            continue
        if len(source_witness) != len(target_witness):
            failures.append(
                (
                    row.entry_key,
                    "artin_update_witness_length_mismatch",
                    (len(source_witness), len(target_witness)),
                )
            )
            continue
        for index, (source_letter, target_letter) in enumerate(
            zip(source_witness, target_witness)
        ):
            source_assignment, source_longitude_index, source_exponent = source_letter
            target_assignment, target_longitude_index, target_exponent = target_letter
            try:
                expected_assignment = _precompose_two_strand_assignment(
                    endpoint_group,
                    source_assignment,
                    precompose_sign,
                )
            except ValueError as error:
                failures.append(
                    (
                        row.entry_key,
                        "invalid_artin_update_source_assignment",
                        (index, repr(error)),
                    )
                )
                continue
            target_assignment_tuple = tuple(target_assignment)
            if any(value not in endpoint_group.elements for value in target_assignment_tuple):
                failures.append(
                    (
                        row.entry_key,
                        "invalid_artin_update_target_assignment",
                        (index, target_assignment_tuple),
                    )
                )
                continue
            if (
                target_assignment_tuple != expected_assignment
                or target_longitude_index != source_longitude_index
                or target_exponent != source_exponent
            ):
                failures.append(
                    (
                        row.entry_key,
                        "artin_update_witness_letter_mismatch",
                        (index, target_letter, (expected_assignment, source_longitude_index, source_exponent)),
                    )
                )
    return tuple(failures)


def universal_k_signed_endpoint_generator_audit(
    interval: LocalInterval,
    seed_classifier_entries: Sequence[UniversalKSeedClassifierEntry],
    reachable_seed_states: Sequence[Tuple[str, UniversalKSeedState]],
    rows: Sequence[UniversalKSignedEndpointGeneratorRow],
    *,
    endpoint_group: FiniteGroup | None = None,
    witnesses: (
        Mapping[
            UniversalKSignedEndpointEntryKey,
            LongitudeSubgroupWitness,
        ]
        | None
    ) = None,
    endpoint_target_audit: UniversalKEndpointTargetAudit | None = None,
    cutoff_readouts_exact: bool = False,
    cutoff_readout_audit: UniversalKCutoffReadoutAudit | None = None,
    residual_faithfulness_verified: bool = False,
    residual_action_scope: UniversalKResidualActionScopeAudit | None = None,
    residual_faithfulness_theorem: UniversalKResidualFaithfulnessAudit | None = None,
    residual_action_audit: "EndpointResidualActionAudit | None" = None,
    telescoping_detector_audit: UniversalKTelescopingDetectorAudit | None = None,
    monodromy_representation_audit: (
        UniversalKEndpointMonodromyRepresentationAudit | None
    ) = None,
) -> UniversalKSignedEndpointGeneratorAudit:
    """Build a signed endpoint audit by deriving all finite row checks.

    This keeps the certificate tied to the actual interval table: the required
    entry domain is computed from the reachable states and fibres, while the
    finite coordinate, inverse, YBE, row-diagnostic longitude, and supplied
    fixed-track telescoping gates remain visibly separated.
    """

    reachable_tuple = tuple(reachable_seed_states)
    row_tuple = tuple(rows)
    witness_map = dict(witnesses or {})
    expected_endpoint_families = tuple(
        sorted({entry[1][0] for entry in seed_classifier_entries}, key=repr)
    )
    if (
        endpoint_target_audit is None
        and len(expected_endpoint_families) == 1
    ):
        endpoint_family = expected_endpoint_families[0]
        cutoff_target_degrees = ()
        endpoint_group_orders = ()
        if (
            endpoint_family in {"C", "M"}
            and cutoff_readout_audit is not None
            and cutoff_readout_audit.cutoff_degree is not None
        ):
            cutoff_target_degrees = (
                (endpoint_family, cutoff_readout_audit.cutoff_degree),
            )
        elif endpoint_group is not None:
            endpoint_group_orders = ((endpoint_family, len(endpoint_group.elements)),)
        endpoint_target_audit = UniversalKEndpointTargetAudit(
            expected_endpoint_families=expected_endpoint_families,
            covered_endpoint_families=expected_endpoint_families,
            endpoint_group_orders=endpoint_group_orders,
            cutoff_degrees=cutoff_target_degrees,
            braid_index_independent=True,
            product_families_separated=True,
        )
    required_entry_keys = universal_k_signed_endpoint_required_entry_keys(
        interval,
        reachable_tuple,
    )
    if monodromy_representation_audit is None:
        endpoint_families = tuple(
            sorted(
                {
                    family
                    for family, _seed_state in reachable_tuple
                    if family in UNIVERSAL_K_ENDPOINT_FAMILIES
                },
                key=repr,
            )
        )
        monodromy_representation_audit = universal_k_endpoint_monodromy_representation_audit(
            universal_k_endpoint_monodromy_presentation(interval, endpoint_families),
            reachable_tuple,
            row_tuple,
        )
    coordinate_failures = universal_k_signed_endpoint_coordinate_failures(
        interval,
        row_tuple,
    )
    inverse_failures = universal_k_signed_endpoint_inverse_failures(
        interval,
        row_tuple,
    )
    positive_ybe_failures = universal_k_signed_endpoint_positive_ybe_failures(
        interval,
        reachable_tuple,
        row_tuple,
    )
    if endpoint_group is None:
        inverse_cancellation_failures = ()
        positive_ybe_cocycle_failures = ()
        far_commutativity_failures = ()
        two_strand_witness_domain_failures = ()
        two_strand_base_failures = ()
        artin_update_failures = ()
    else:
        inverse_cancellation_failures = universal_k_signed_endpoint_inverse_cancellation_failures(
            endpoint_group,
            interval,
            row_tuple,
        )
        positive_ybe_cocycle_failures = universal_k_signed_endpoint_positive_ybe_cocycle_failures(
            endpoint_group,
            interval,
            reachable_tuple,
            row_tuple,
        )
        far_commutativity_failures = universal_k_signed_endpoint_far_commutativity_failures(
            endpoint_group,
            interval,
            reachable_tuple,
            row_tuple,
        )
        two_strand_witness_domain_failures = (
            universal_k_signed_endpoint_two_strand_witness_domain_failures(
                row_tuple,
                witness_map,
            )
        )
        two_strand_base_failures = universal_k_signed_endpoint_two_strand_base_failures(
            endpoint_group,
            row_tuple,
            witness_map,
        )
        artin_update_failures = universal_k_signed_endpoint_artin_update_failures(
            endpoint_group,
            interval,
            row_tuple,
            witness_map,
        )

    return UniversalKSignedEndpointGeneratorAudit(
        seed_classifier_entries=tuple(seed_classifier_entries),
        reachable_seed_states=reachable_tuple,
        required_entry_keys=required_entry_keys,
        rows=row_tuple,
        entry_domain_derived_from_interval=True,
        finite_row_checks_derived_from_tables=True,
        endpoint_targets_fixed=endpoint_group is not None,
        coordinate_components_verified=not coordinate_failures,
        inverse_pairing_verified=not inverse_failures,
        inverse_cancellation_verified=(
            endpoint_group is not None and not inverse_cancellation_failures
        ),
        positive_ybe_path_verified=not positive_ybe_failures,
        positive_ybe_cocycle_verified=(
            endpoint_group is not None and not positive_ybe_failures
        ),
        far_commutativity_verified=(
            endpoint_group is not None
            and not tuple(
                failure
                for failure in far_commutativity_failures
                if failure[1] != "far_commutativity_label_mismatch"
            )
        ),
        signed_two_strand_base_verified=(
            endpoint_group is not None and not two_strand_base_failures
        ),
        artin_homomorphism_update_verified=(
            endpoint_group is not None and not artin_update_failures
        ),
        coordinate_component_failures=coordinate_failures,
        inverse_pairing_failures=inverse_failures,
        inverse_cancellation_failures=inverse_cancellation_failures,
        positive_ybe_path_failures=positive_ybe_failures,
        positive_ybe_cocycle_failures=positive_ybe_cocycle_failures,
        far_commutativity_failures=far_commutativity_failures,
        two_strand_witness_domain_failures=two_strand_witness_domain_failures,
        two_strand_base_failures=two_strand_base_failures,
        artin_update_failures=artin_update_failures,
        cutoff_readouts_exact=cutoff_readouts_exact,
        residual_faithfulness_verified=residual_faithfulness_verified,
        endpoint_target_audit=endpoint_target_audit,
        cutoff_readout_audit=cutoff_readout_audit,
        residual_action_scope=residual_action_scope,
        residual_faithfulness_theorem=residual_faithfulness_theorem,
        residual_action_audit=residual_action_audit,
        telescoping_detector_audit=telescoping_detector_audit,
        monodromy_representation_audit=monodromy_representation_audit,
        endpoint_group=endpoint_group,
    )


@dataclass(frozen=True)
class UniversalKEndpointObserverBuild:
    """Constructed U/C/M endpoint observer plus its derived audit.

    The build record is the executable version of the monodromy-coboundary
    certificate: positive rows are read from the word-potential identity rows,
    negative rows are forced by inversion, and the signed endpoint audit then
    checks the full D_Gamma domain, braid-presentation coherence, telescoping,
    cutoff readouts, and residual faithfulness.
    """

    reachable_seed_states: Tuple[Tuple[str, UniversalKSeedState], ...]
    monodromy_presentation: UniversalKEndpointMonodromyPresentation
    monodromy_representation_audit: UniversalKEndpointMonodromyRepresentationAudit
    positive_rows: Tuple[UniversalKSignedEndpointGeneratorRow, ...]
    rows: Tuple[UniversalKSignedEndpointGeneratorRow, ...]
    telescoping_detector_audit: UniversalKTelescopingDetectorAudit
    audit: UniversalKSignedEndpointGeneratorAudit

    @property
    def proves_endpoint_observer(self) -> bool:
        return (
            self.monodromy_representation_audit.proves_monodromy_representation
            and self.audit.proves_signed_endpoint_generator_tables
        )


def universal_k_endpoint_observer_positive_rows_from_word_potential(
    interval: LocalInterval,
    word_potential_certificate: UniversalKWordPotentialCertificate,
) -> Tuple[UniversalKSignedEndpointGeneratorRow, ...]:
    """Build positive endpoint rows from word-potential coboundary data."""

    rows = []
    for identity_row in word_potential_certificate.identity_rows:
        key = identity_row.entry_key
        if not _universal_k_is_positive_entry_key(key):
            continue
        endpoint_family, seed_state, _sign, left_color, right_color, x, y = key
        output = interval.T.get((left_color, right_color, x, y))
        if output is None:
            continue
        rows.append(
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family=endpoint_family,
                seed_state=seed_state,
                sign=1,
                left_color=left_color,
                right_color=right_color,
                input_left=x,
                input_right=y,
                output_left=output[0],
                output_right=output[1],
                next_seed_state=identity_row.next_seed_state,
                endpoint_value=identity_row.endpoint_value,
            )
        )
    return tuple(rows)


def universal_k_endpoint_observer_signed_rows_from_positive(
    interval: LocalInterval,
    endpoint_group: FiniteGroup,
    positive_rows: Sequence[UniversalKSignedEndpointGeneratorRow],
) -> Tuple[UniversalKSignedEndpointGeneratorRow, ...]:
    """Force the signed observer table by adjoining inverse negative rows."""

    group_elements = set(endpoint_group.elements)
    rows = list(positive_rows)
    for row in positive_rows:
        if row.sign != 1 or row.endpoint_value not in group_elements:
            continue
        target_colors = interval.base_R.get((row.left_color, row.right_color))
        if target_colors is None:
            continue
        rows.append(
            UniversalKSignedEndpointGeneratorRow(
                endpoint_family=row.endpoint_family,
                seed_state=row.next_seed_state,
                sign=-1,
                left_color=target_colors[0],
                right_color=target_colors[1],
                input_left=row.output_left,
                input_right=row.output_right,
                output_left=row.input_left,
                output_right=row.input_right,
                next_seed_state=row.seed_state,
                endpoint_value=endpoint_group.inv(row.endpoint_value),
            )
        )
    return tuple(rows)


def _universal_k_detector_track_counts_from_initialization_rows(
    rows: Sequence[UniversalKDetectorTrackInitializationRow],
) -> Tuple[Tuple[str, int], ...]:
    counts: dict[str, int] = {}
    for row in rows:
        if (
            row.endpoint_family not in UNIVERSAL_K_ENDPOINT_FAMILIES
            or not _universal_k_nonnegative_int(row.track_index)
        ):
            continue
        counts[row.endpoint_family] = max(
            counts.get(row.endpoint_family, 0),
            row.track_index + 1,
        )
    return tuple(sorted(counts.items(), key=repr))


def universal_k_endpoint_observer_build(
    interval: LocalInterval,
    seed_classifier_entries: Sequence[UniversalKSeedClassifierEntry],
    word_potential_certificate: UniversalKWordPotentialCertificate,
    *,
    detector_track_counts_by_family: Tuple[Tuple[str, int], ...] = (),
    detector_track_initialization_rows: Tuple[
        UniversalKDetectorTrackInitializationRow,
        ...,
    ] = (),
    endpoint_target_audit: UniversalKEndpointTargetAudit | None = None,
    cutoff_readout_audit: UniversalKCutoffReadoutAudit | None = None,
    residual_faithfulness_theorem: UniversalKResidualFaithfulnessAudit | None = None,
    residual_action_scope: UniversalKResidualActionScopeAudit | None = None,
    residual_action_audit: "EndpointResidualActionAudit | None" = None,
    witnesses: (
        Mapping[
            UniversalKSignedEndpointEntryKey,
            LongitudeSubgroupWitness,
        ]
        | None
    ) = None,
) -> UniversalKEndpointObserverBuild:
    """Construct the finite U/C/M observer determined by a word-potential certificate.

    This is intentionally not a theorem by itself.  It builds the observer rows
    forced by the supplied monodromy-coboundary data and then returns the same
    signed endpoint audit used elsewhere.  If the certificate omits a reachable
    context, uses a non-constant coboundary defect, lacks exact C/M readouts, or
    does not include residual faithfulness, the returned audit stays open.
    """

    endpoint_group = word_potential_certificate.endpoint_group
    positive_rows = universal_k_endpoint_observer_positive_rows_from_word_potential(
        interval,
        word_potential_certificate,
    )
    rows = universal_k_endpoint_observer_signed_rows_from_positive(
        interval,
        endpoint_group,
        positive_rows,
    )
    reachable_seed_states = universal_k_signed_endpoint_transition_closure(
        seed_classifier_entries,
        rows,
    )
    monodromy_presentation = universal_k_endpoint_monodromy_presentation(
        interval,
        tuple(
            sorted(
                {
                    family
                    for family, _seed_state in reachable_seed_states
                    if family in UNIVERSAL_K_ENDPOINT_FAMILIES
                },
                key=repr,
            )
        ),
    )
    monodromy_representation_audit = universal_k_endpoint_monodromy_representation_audit(
        monodromy_presentation,
        reachable_seed_states,
        rows,
    )
    required_entry_keys = universal_k_signed_endpoint_required_entry_keys(
        interval,
        reachable_seed_states,
    )
    if not detector_track_counts_by_family:
        detector_track_counts_by_family = (
            _universal_k_detector_track_counts_from_initialization_rows(
                detector_track_initialization_rows
            )
        )
    detector_track_count = sum(
        count
        for _family, count in detector_track_counts_by_family
        if _universal_k_positive_int(count)
    )
    telescoping_detector_audit = UniversalKTelescopingDetectorAudit(
        expected_entry_keys=required_entry_keys,
        covered_entry_keys=tuple(row.entry_key for row in rows),
        expected_endpoint_seed_states=reachable_seed_states,
        covered_endpoint_seed_states=reachable_seed_states,
        detector_track_counts_by_family=tuple(detector_track_counts_by_family),
        detector_track_initialization_rows=tuple(detector_track_initialization_rows),
        expected_word_potential_seed_states=reachable_seed_states,
        covered_word_potential_seed_states=reachable_seed_states,
        detector_track_count=detector_track_count or None,
        detector_tracks_fixed_before_braid=True,
        detector_track_initialization_verified=True,
        artin_detector_recurrence_verified=True,
        word_potential_templates_use_only_current_longitudes=True,
        word_potential_artin_substitution_verified=True,
        word_potential_identity_verified=True,
        word_potential_certificate=word_potential_certificate,
        telescoping_identity_verified=True,
        terminal_readout_longitudes_verified=True,
        initial_readout_normalized=True,
        braid_index_independent=True,
    )
    audit = universal_k_signed_endpoint_generator_audit(
        interval,
        seed_classifier_entries,
        reachable_seed_states,
        rows,
        endpoint_group=endpoint_group,
        witnesses=witnesses,
        endpoint_target_audit=endpoint_target_audit,
        cutoff_readout_audit=cutoff_readout_audit,
        cutoff_readouts_exact=(
            cutoff_readout_audit is not None
            and cutoff_readout_audit.proves_exact_cutoff_readouts
        ),
        residual_faithfulness_theorem=residual_faithfulness_theorem,
        residual_action_scope=residual_action_scope,
        residual_action_audit=residual_action_audit,
        telescoping_detector_audit=telescoping_detector_audit,
        monodromy_representation_audit=monodromy_representation_audit,
    )
    return UniversalKEndpointObserverBuild(
        reachable_seed_states=reachable_seed_states,
        monodromy_presentation=monodromy_presentation,
        monodromy_representation_audit=monodromy_representation_audit,
        positive_rows=positive_rows,
        rows=rows,
        telescoping_detector_audit=telescoping_detector_audit,
        audit=audit,
    )


@dataclass(frozen=True)
class TriangularRecoveryEndpointWitnessAudit:
    """Endpoint witnesses for K rows routed to the triangular recovery unit."""

    observer: TriangularRecoveryUnitObserverAudit
    routed_defects: Tuple[Tuple[Tuple[Color, Color], str], ...]
    endpoint_audits: Tuple[Tuple[TriangularRecoveryEndpointKey, object], ...]

    @property
    def routed_keys(self) -> Tuple[TriangularRecoveryEndpointKey, ...]:
        return _sorted_triangular_recovery_endpoint_keys(
            tuple(
                _triangular_recovery_endpoint_key(defect)
                for defect in self.routed_defects
            )
        )

    @property
    def witnessed_keys(self) -> Tuple[TriangularRecoveryEndpointKey, ...]:
        return _sorted_triangular_recovery_endpoint_keys(
            tuple(
                key
                for key, audit in self.endpoint_audits
                if _triangular_recovery_endpoint_audit_proves(audit)
            )
        )

    @property
    def missing_routed_keys(self) -> Tuple[TriangularRecoveryEndpointKey, ...]:
        witnessed = set(self.witnessed_keys)
        return _sorted_triangular_recovery_endpoint_keys(
            tuple(key for key in self.routed_keys if key not in witnessed)
        )

    @property
    def extra_witness_keys(self) -> Tuple[TriangularRecoveryEndpointKey, ...]:
        routed = set(self.routed_keys)
        return _sorted_triangular_recovery_endpoint_keys(
            tuple(key for key, _audit in self.endpoint_audits if key not in routed)
        )

    @property
    def all_endpoint_witnesses_match_observer(self) -> bool:
        return all(
            getattr(audit, "observer", None) == self.observer
            for _key, audit in self.endpoint_audits
        )

    @property
    def all_endpoint_witnesses_visible(self) -> bool:
        return all(
            _triangular_recovery_endpoint_audit_proves(audit)
            for _key, audit in self.endpoint_audits
        )

    @property
    def all_routed_keys_have_endpoint_witnesses(self) -> bool:
        return bool(self.routed_keys) and not self.missing_routed_keys

    @property
    def proves_triangular_recovery_endpoint_witnesses(self) -> bool:
        return (
            self.observer.proves_fixed_unit_observer
            and self.all_endpoint_witnesses_match_observer
            and self.all_endpoint_witnesses_visible
            and self.all_routed_keys_have_endpoint_witnesses
            and not self.extra_witness_keys
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.observer.proves_fixed_unit_observer:
            reasons.append("triangular_recovery_observer_not_proved")
        if not self.all_endpoint_witnesses_match_observer:
            reasons.append("endpoint_witness_observer_mismatch")
        if not self.all_endpoint_witnesses_visible:
            reasons.append("endpoint_witnesses_not_proved")
        if not self.all_routed_keys_have_endpoint_witnesses:
            reasons.append("routed_recovery_keys_not_covered")
        if self.extra_witness_keys:
            reasons.append("extra_recovery_witness_keys")
        return tuple(reasons)


def triangular_recovery_endpoint_witness_audit(
    observer: TriangularRecoveryUnitObserverAudit,
    routed_defects: Sequence[Tuple[Tuple[Color, Color], str]],
    endpoint_audits: Sequence[Tuple[TriangularRecoveryEndpointKey, object]],
) -> TriangularRecoveryEndpointWitnessAudit:
    """Bundle endpoint-longitude witnesses for System U routed K defects."""

    return TriangularRecoveryEndpointWitnessAudit(
        observer=observer,
        routed_defects=tuple(routed_defects),
        endpoint_audits=tuple(endpoint_audits),
    )


@dataclass(frozen=True)
class TriangularRecoverySymmetricEndpointForkAudit:
    """Symmetric cutoff certificate for routed triangular recovery endpoints.

    This is the System U specialization of the finite endpoint-family fork.  It
    does not construct endpoint witnesses.  It checks that a supplied symmetric
    endpoint-family certificate is attached to exactly the routed U keys and to
    the fixed triangular recovery unit group ``U_tri``.
    """

    observer: TriangularRecoveryUnitObserverAudit
    routed_defects: Tuple[Tuple[Tuple[Color, Color], str], ...]
    endpoint_family: "EndpointFamilySymmetricForkAudit"
    covered_keys: Tuple[TriangularRecoveryEndpointKey, ...]

    @property
    def routed_keys(self) -> Tuple[TriangularRecoveryEndpointKey, ...]:
        return _sorted_triangular_recovery_endpoint_keys(
            tuple(
                _triangular_recovery_endpoint_key(defect)
                for defect in self.routed_defects
            )
        )

    @property
    def supplied_covered_keys(self) -> Tuple[TriangularRecoveryEndpointKey, ...]:
        return _sorted_triangular_recovery_endpoint_keys(self.covered_keys)

    @property
    def missing_routed_keys(self) -> Tuple[TriangularRecoveryEndpointKey, ...]:
        covered = set(self.supplied_covered_keys)
        return _sorted_triangular_recovery_endpoint_keys(
            tuple(key for key in self.routed_keys if key not in covered)
        )

    @property
    def extra_covered_keys(self) -> Tuple[TriangularRecoveryEndpointKey, ...]:
        routed = set(self.routed_keys)
        return _sorted_triangular_recovery_endpoint_keys(
            tuple(key for key in self.covered_keys if key not in routed)
        )

    @property
    def endpoint_family_uses_recovery_unit_group(self) -> bool:
        return self.endpoint_family.endpoint_group_orders == (
            self.observer.unit_group_order,
        )

    @property
    def all_routed_keys_covered(self) -> bool:
        return bool(self.routed_keys) and not self.missing_routed_keys

    @property
    def proves_triangular_recovery_symmetric_endpoint_cutoff(self) -> bool:
        return (
            self.observer.proves_fixed_unit_observer
            and self.endpoint_family_uses_recovery_unit_group
            and self.all_routed_keys_covered
            and not self.extra_covered_keys
            and self.endpoint_family.faithful_endpoint_cutoff_proved
        )

    @property
    def proves_triangular_recovery_symmetric_tail_seed_prefix(self) -> bool:
        return (
            self.observer.proves_fixed_unit_observer
            and self.endpoint_family_uses_recovery_unit_group
            and self.endpoint_family.proves_supplied_symmetric_tail_endpoint_seed_prefix
            and bool(set(self.supplied_covered_keys).intersection(self.routed_keys))
            and not self.extra_covered_keys
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.observer.proves_fixed_unit_observer:
            reasons.append("triangular_recovery_observer_not_proved")
        if not self.endpoint_family_uses_recovery_unit_group:
            reasons.append("endpoint_family_group_mismatch")
        if not self.all_routed_keys_covered:
            reasons.append("routed_recovery_keys_not_covered")
        if self.extra_covered_keys:
            reasons.append("extra_recovery_symmetric_keys")
        if not self.endpoint_family.faithful_endpoint_cutoff_proved:
            reasons.extend(self.endpoint_family.failure_reasons)
        return tuple(reasons)


def triangular_recovery_symmetric_endpoint_fork_audit(
    observer: TriangularRecoveryUnitObserverAudit,
    routed_defects: Sequence[Tuple[Tuple[Color, Color], str]],
    endpoint_family: "EndpointFamilySymmetricForkAudit",
    covered_keys: Sequence[TriangularRecoveryEndpointKey],
) -> TriangularRecoverySymmetricEndpointForkAudit:
    """Attach a finite symmetric endpoint-family certificate to System U keys."""

    return TriangularRecoverySymmetricEndpointForkAudit(
        observer=observer,
        routed_defects=tuple(routed_defects),
        endpoint_family=endpoint_family,
        covered_keys=tuple(covered_keys),
    )


@dataclass(frozen=True)
class PostLinearRemainingFiniteSystemAudit:
    """Classify the exact finite system left after finite-linear closure."""

    refinement: "NonlinearOverlapRefinementAudit"
    kink_completion_deficits_routed: bool = False
    triangular_latin_defect_closure: TriangularLatinDefectClosureAudit | None = None
    triangular_constant_kernel_recovery_route: (
        TriangularConstantKernelRecoveryRouteAudit | None
    ) = None
    missing_triangular_row_profile: MissingTriangularRowProfileAudit | None = None
    missing_triangular_left_rack_cardinality: (
        MissingTriangularLeftRackCardinalityAudit | None
    ) = None
    missing_triangular_coordinate_unit_routing: (
        MissingTriangularCoordinateUnitRoutingAudit | None
    ) = None
    missing_triangular_partial_constant_closure: (
        MissingTriangularPartialConstantClosureAudit | None
    ) = None
    missing_triangular_partial_constant_continuation_route: (
        MissingTriangularPartialConstantContinuationRouteAudit | None
    ) = None
    universal_continuation_identity_routing: (
        UniversalContinuationIdentityRoutingAudit | None
    ) = None
    triangular_recovery_endpoint_witness: (
        TriangularRecoveryEndpointWitnessAudit | None
    ) = None
    triangular_recovery_symmetric_endpoint_fork: (
        TriangularRecoverySymmetricEndpointForkAudit | None
    ) = None
    universal_continuation_endpoint_witness: (
        "UniversalContinuationIdentityEndpointWitnessAudit | None"
    ) = None
    universal_continuation_symmetric_endpoint_fork: (
        "UniversalContinuationIdentitySymmetricEndpointForkAudit | None"
    ) = None
    mixed_unit_context_endpoint_witness: (
        "MixedUnitContextEndpointWitnessAudit | None"
    ) = None
    mixed_unit_context_symmetric_endpoint_fork: (
        "MixedUnitContextSymmetricEndpointForkAudit | None"
    ) = None
    universal_k_signed_endpoint_generator: (
        UniversalKSignedEndpointGeneratorAudit | None
    ) = None
    universal_k_signed_endpoint_interval: LocalInterval | None = None
    unsupported_companion_structural_contradiction: (
        UnsupportedCompanionStructuralContradictionAudit | None
    ) = None

    @property
    def unsupported_companion_block_image_rows(
        self,
    ) -> Tuple[UnsupportedCompanionBlockImageRowKey, ...]:
        return tuple(
            sorted(
                {
                    (row.side, row.left_color, row.right_color)
                    for row in self.refinement.triangular_column.companion_nonbijective_without_constant_kernel_rows
                },
                key=repr,
            )
        )

    @property
    def unsupported_companion_structural_contradiction_expected_exact(self) -> bool:
        if self.unsupported_companion_structural_contradiction is None:
            return not self.unsupported_companion_block_image_rows
        return (
            self.unsupported_companion_structural_contradiction.expected_rows_exact
            == self.unsupported_companion_block_image_rows
        )

    @property
    def unsupported_companion_structural_contradiction_proved(self) -> bool:
        if not self.unsupported_companion_block_image_rows:
            return True
        return (
            self.unsupported_companion_structural_contradiction is not None
            and self.unsupported_companion_structural_contradiction_expected_exact
            and self.unsupported_companion_structural_contradiction.proves_unsupported_companion_structural_contradiction
        )

    @property
    def unsupported_companion_structural_obligation_active(self) -> bool:
        return (
            self.refinement.status == "triangular_structural_inconsistency"
            and bool(self.unsupported_companion_block_image_rows)
            and not self.unsupported_companion_structural_contradiction_proved
        )

    @property
    def closed_by_recorded_branch(self) -> bool:
        if self.refinement.status == "triangular_structural_inconsistency":
            return not self.unsupported_companion_structural_obligation_active
        return self.refinement.status in {
            "closed_by_repair_contract",
            "closed_by_transport_state_rackification",
            "closed_by_locally_nondegenerate_branch",
            "section_kernel_visible_to_existing_readouts",
            "closed_by_product_triangular_collapse",
            "rack_base_consistency_inconsistent",
            "latin_triangular_kink_contradiction",
            "latin_triangular_kink_impossible",
            "latin_triangular_ybe_projection_inconsistent",
            "latin_triangular_kink_cancellation_inconsistent",
            "side_dual_latin_triangular_kink_contradiction",
            "side_dual_latin_triangular_kink_impossible",
            "side_dual_latin_triangular_ybe_projection_inconsistent",
            "side_dual_latin_triangular_diagonal_cancellation_inconsistent",
        }

    @property
    def raw_system_k(self) -> bool:
        return self.refinement.status == "triangular_recovery_kink_completion_deficit"

    @property
    def system_k_closed_by_proper_defect_closure(self) -> bool:
        return (
            self.raw_system_k
            and self.triangular_latin_defect_closure is not None
            and self.triangular_latin_defect_closure.has_proper_closure
        )

    @property
    def system_k_closed_by_partial_constant_proper_closure(self) -> bool:
        return (
            self.raw_system_k
            and self.missing_triangular_partial_constant_closure is not None
            and bool(
                self.missing_triangular_partial_constant_closure.proper_closure_rows
            )
        )

    @property
    def system_k_closed_by_proper_generated_closure(self) -> bool:
        return (
            self.system_k_closed_by_proper_defect_closure
            or self.system_k_closed_by_partial_constant_proper_closure
        )

    def _missing_profile_row(
        self,
        side: str,
        pair: Tuple[Color, Color],
    ):
        if self.missing_triangular_row_profile is None:
            return None
        for row in self.missing_triangular_row_profile.rows:
            if row.side == side and (row.left_color, row.right_color) == pair:
                return row
        return None

    def _coordinate_unit_profile_routes(self, side: str, pair: Tuple[Color, Color]) -> bool:
        routing = self.missing_triangular_coordinate_unit_routing
        if routing is None or not routing.colored_ybe:
            return False
        for row in routing.rows:
            if (
                (row.left_color, row.right_color) == pair
                and side in row.coordinate_unit_sides
            ):
                if row.status == "mixed_unit_context":
                    return True
                if row.status == "two_sided_unit_pair":
                    return routing.locally_nondegenerate_closed_branch
                return False
        return False

    def _coordinate_unit_profile_routes_to_mixed_context(
        self, side: str, pair: Tuple[Color, Color]
    ) -> bool:
        if (
            self.missing_triangular_coordinate_unit_routing is None
            or not self.missing_triangular_coordinate_unit_routing.colored_ybe
        ):
            return False
        for row in self.missing_triangular_coordinate_unit_routing.rows:
            if (
                (row.left_color, row.right_color) == pair
                and side in row.coordinate_unit_sides
            ):
                return row.status == "mixed_unit_context"
        return False

    def _partial_constant_profile_routes(self, side: str, pair: Tuple[Color, Color]) -> bool:
        if self.missing_triangular_partial_constant_closure is None:
            return False
        closure_rows = tuple(
            row
            for row in self.missing_triangular_partial_constant_closure.rows
            if row.side == side and (row.left_color, row.right_color) == pair
        )
        if not closure_rows:
            return False
        route_by_key = {}
        if self.missing_triangular_partial_constant_continuation_route is not None:
            route_by_key = {
                (
                    row.side,
                    row.left_color,
                    row.right_color,
                    row.fixed_input,
                    row.domain_color,
                    row.collapsed_inputs,
                    row.closure_kind,
                ): row
                for row in self.missing_triangular_partial_constant_continuation_route.rows
            }
        for row in closure_rows:
            if row.closure_is_proper:
                continue
            if not row.closure_is_universal:
                return False
            route = route_by_key.get(
                (
                    row.side,
                    row.left_color,
                    row.right_color,
                    row.fixed_input,
                    row.domain_color,
                    row.collapsed_inputs,
                    row.closure_kind,
                )
            )
            if route is None or not route.routes_to_universal_continuation_seed:
                return False
        return True

    def _partial_constant_profile_routes_to_continuation(
        self, side: str, pair: Tuple[Color, Color]
    ) -> bool:
        if (
            self.missing_triangular_partial_constant_closure is None
            or self.missing_triangular_partial_constant_continuation_route is None
        ):
            return False
        closure_rows = tuple(
            row
            for row in self.missing_triangular_partial_constant_closure.rows
            if row.side == side and (row.left_color, row.right_color) == pair
        )
        if not closure_rows:
            return False
        route_by_key = {
            (
                row.side,
                row.left_color,
                row.right_color,
                row.fixed_input,
                row.domain_color,
                row.collapsed_inputs,
                row.closure_kind,
            ): row
            for row in self.missing_triangular_partial_constant_continuation_route.rows
        }
        for row in closure_rows:
            if row.closure_is_proper:
                continue
            if not row.closure_is_universal:
                return False
            route = route_by_key.get(
                (
                    row.side,
                    row.left_color,
                    row.right_color,
                    row.fixed_input,
                    row.domain_color,
                    row.collapsed_inputs,
                    row.closure_kind,
                )
            )
            if route is not None and route.routes_to_universal_continuation_seed:
                return True
        return False

    def _no_triangular_row_routes_by_profile(
        self,
        side: str,
        pair: Tuple[Color, Color],
    ) -> bool:
        row = self._missing_profile_row(side, pair)
        if row is None:
            return False
        if row.explanation == "proper_section_kernel_visible":
            return True
        if row.explanation == "coordinate_side_unit_not_triangular":
            return self._coordinate_unit_profile_routes(side, pair)
        if row.explanation == "partial_constant_hidden_rank_loss":
            return self._partial_constant_profile_routes(side, pair)
        if row.explanation in (
            "injective_non_surjective_section",
            "nonconstant_hidden_rank_loss",
            "unclassified_missing_triangular_profile",
        ):
            return (
                self.missing_triangular_left_rack_cardinality is not None
                and self.missing_triangular_left_rack_cardinality.proves_left_rack_missing_triangular_cardinality_closure
            )
        return False

    def _no_triangular_row_routes_to_continuation(
        self,
        side: str,
        pair: Tuple[Color, Color],
    ) -> bool:
        row = self._missing_profile_row(side, pair)
        return (
            row is not None
            and row.explanation == "partial_constant_hidden_rank_loss"
            and self._partial_constant_profile_routes_to_continuation(side, pair)
        )

    def _no_triangular_row_routes_to_mixed_context(
        self,
        side: str,
        pair: Tuple[Color, Color],
    ) -> bool:
        row = self._missing_profile_row(side, pair)
        return (
            row is not None
            and row.explanation == "coordinate_side_unit_not_triangular"
            and self._coordinate_unit_profile_routes_to_mixed_context(side, pair)
        )

    def _constant_map_kernel_routes_by_recovery(
        self,
        side: str,
        pair: Tuple[Color, Color],
    ) -> bool:
        if (
            self.triangular_latin_defect_closure is None
            or self.triangular_constant_kernel_recovery_route is None
        ):
            return False
        closure_rows = tuple(
            row
            for row in self.triangular_latin_defect_closure.rows
            if row.side == side
            and row.defect == "constant_map_kernel"
            and (row.left_color, row.right_color) == pair
        )
        if not closure_rows:
            return False
        route_by_key = {
            (
                row.side,
                row.left_color,
                row.right_color,
                row.domain_color,
                row.collapsed_inputs,
                row.closure_kind,
            ): row
            for row in self.triangular_constant_kernel_recovery_route.rows
        }
        for row in closure_rows:
            if row.closure_is_proper:
                continue
            route = route_by_key.get(
                (
                    row.side,
                    row.left_color,
                    row.right_color,
                    row.domain_color,
                    row.collapsed_inputs,
                    row.closure_kind,
                )
            )
            if route is None or not route.routes_universal_kernel_edge_to_recovery:
                return False
        return True

    def _live_missing_latin_row_defects(
        self,
        defects: Tuple[Tuple[Tuple[Color, Color], str], ...],
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        live = []
        for pair, reason in defects:
            if reason == "no_left_triangular_row" and self._no_triangular_row_routes_by_profile(
                "left",
                pair,
            ):
                continue
            if reason == "no_right_triangular_row" and self._no_triangular_row_routes_by_profile(
                "right",
                pair,
            ):
                continue
            if reason in (
                "left_constant_map_proper_kernel",
                "left_constant_map_universal_kernel",
            ) and self._constant_map_kernel_routes_by_recovery("left", pair):
                continue
            if reason in (
                "right_constant_map_proper_kernel",
                "right_constant_map_universal_kernel",
            ) and self._constant_map_kernel_routes_by_recovery("right", pair):
                continue
            if (
                reason == "left_companion_sections_injective_non_surjective"
                and self._constant_map_kernel_routes_by_recovery("left", pair)
            ):
                continue
            if (
                reason == "right_companion_sections_injective_non_surjective"
                and self._constant_map_kernel_routes_by_recovery("right", pair)
            ):
                continue
            live.append((pair, reason))
        return tuple(live)

    def _recovery_routed_missing_latin_row_defects(
        self,
        defects: Tuple[Tuple[Tuple[Color, Color], str], ...],
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        routed = []
        for pair, reason in defects:
            if reason in (
                "left_constant_map_proper_kernel",
                "left_constant_map_universal_kernel",
                "left_companion_sections_injective_non_surjective",
            ) and self._constant_map_kernel_routes_by_recovery("left", pair):
                routed.append((pair, reason))
            if reason in (
                "right_constant_map_proper_kernel",
                "right_constant_map_universal_kernel",
                "right_companion_sections_injective_non_surjective",
            ) and self._constant_map_kernel_routes_by_recovery("right", pair):
                routed.append((pair, reason))
        return tuple(routed)

    def _continuation_routed_missing_latin_row_defects(
        self,
        defects: Tuple[Tuple[Tuple[Color, Color], str], ...],
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        routed = []
        for pair, reason in defects:
            if reason == "no_left_triangular_row" and self._no_triangular_row_routes_to_continuation(
                "left",
                pair,
            ):
                routed.append((pair, reason))
            if reason == "no_right_triangular_row" and self._no_triangular_row_routes_to_continuation(
                "right",
                pair,
            ):
                routed.append((pair, reason))
        return tuple(routed)

    def _mixed_context_routed_missing_latin_row_defects(
        self,
        defects: Tuple[Tuple[Tuple[Color, Color], str], ...],
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        routed = []
        for pair, reason in defects:
            if reason == "no_left_triangular_row" and self._no_triangular_row_routes_to_mixed_context(
                "left",
                pair,
            ):
                routed.append((pair, reason))
            if reason == "no_right_triangular_row" and self._no_triangular_row_routes_to_mixed_context(
                "right",
                pair,
            ):
                routed.append((pair, reason))
        return tuple(routed)

    @property
    def live_k_missing_latin_row_defects(self) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        if self.system_k_closed_by_proper_generated_closure:
            return ()
        return self._live_missing_latin_row_defects(
            self.refinement.active_missing_left_latin_row_defects
            + self.refinement.active_missing_right_latin_row_defects,
        )

    @property
    def recovery_routed_k_missing_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        if self.system_k_closed_by_proper_generated_closure:
            return ()
        return self._recovery_routed_missing_latin_row_defects(
            self.refinement.active_missing_left_latin_row_defects
            + self.refinement.active_missing_right_latin_row_defects,
        )

    @property
    def continuation_routed_k_missing_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        if self.system_k_closed_by_proper_generated_closure:
            return ()
        return self._continuation_routed_missing_latin_row_defects(
            self.refinement.active_missing_left_latin_row_defects
            + self.refinement.active_missing_right_latin_row_defects,
        )

    @property
    def mixed_context_routed_k_missing_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        if self.system_k_closed_by_proper_generated_closure:
            return ()
        return self._mixed_context_routed_missing_latin_row_defects(
            self.refinement.active_missing_left_latin_row_defects
            + self.refinement.active_missing_right_latin_row_defects,
        )

    @property
    def k_deficits_routed_to_recovery_endpoint(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and not self.system_k_closed_by_proper_generated_closure
            and bool(self.recovery_routed_k_missing_latin_row_defects)
            and not self.live_k_missing_latin_row_defects
        )

    @property
    def k_deficits_routed_to_continuation_endpoint(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and not self.system_k_closed_by_proper_generated_closure
            and bool(self.continuation_routed_k_missing_latin_row_defects)
            and not self.live_k_missing_latin_row_defects
        )

    @property
    def k_deficits_routed_to_mixed_context_endpoint(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and not self.system_k_closed_by_proper_generated_closure
            and bool(self.mixed_context_routed_k_missing_latin_row_defects)
            and not self.live_k_missing_latin_row_defects
        )

    @property
    def k_deficits_closed_by_recorded_routing(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and not self.system_k_closed_by_proper_generated_closure
            and not self.k_deficits_routed_to_recovery_endpoint
            and not self.k_deficits_routed_to_continuation_endpoint
            and not self.k_deficits_routed_to_mixed_context_endpoint
            and not self.live_k_missing_latin_row_defects
        )

    @property
    def system_k_active(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and not self.system_k_closed_by_proper_generated_closure
            and bool(self.live_k_missing_latin_row_defects)
        )

    @property
    def routed_system_k_to_u(self) -> bool:
        return (
            (
                self.raw_system_k
                and self.kink_completion_deficits_routed
                and not self.system_k_closed_by_proper_generated_closure
                and bool(self.live_k_missing_latin_row_defects)
            )
            or self.k_deficits_routed_to_recovery_endpoint
        )

    @property
    def system_u_active(self) -> bool:
        return (
            self.refinement.status == "triangular_recovery_unit_longitude_obstruction"
            or self.routed_system_k_to_u
        )

    @property
    def system_u_endpoint_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        if (
            self.raw_system_k
            and self.kink_completion_deficits_routed
            and self.live_k_missing_latin_row_defects
        ):
            return self.live_k_missing_latin_row_defects
        if self.k_deficits_routed_to_recovery_endpoint:
            return self.recovery_routed_k_missing_latin_row_defects
        return ()

    @property
    def system_c_active(self) -> bool:
        return self.k_deficits_routed_to_continuation_endpoint

    @property
    def system_m_active(self) -> bool:
        return self.k_deficits_routed_to_mixed_context_endpoint

    @property
    def system_u_closed_by_endpoint_witness(self) -> bool:
        witness = self.triangular_recovery_endpoint_witness
        return (
            self.system_u_active
            and witness is not None
            and witness.observer == self.refinement.triangular_recovery_unit_observer
            and witness.routed_keys
            == _sorted_triangular_recovery_endpoint_keys(
                tuple(
                    _triangular_recovery_endpoint_key(defect)
                    for defect in self.system_u_endpoint_defects
                )
            )
            and witness.proves_triangular_recovery_endpoint_witnesses
        )

    @property
    def system_u_closed_by_symmetric_endpoint_fork(self) -> bool:
        fork = self.triangular_recovery_symmetric_endpoint_fork
        return (
            self.system_u_active
            and fork is not None
            and fork.observer == self.refinement.triangular_recovery_unit_observer
            and fork.routed_keys
            == _sorted_triangular_recovery_endpoint_keys(
                tuple(
                    _triangular_recovery_endpoint_key(defect)
                    for defect in self.system_u_endpoint_defects
                )
            )
            and fork.proves_triangular_recovery_symmetric_endpoint_cutoff
        )

    @property
    def system_u_closed_by_routed_certificate(self) -> bool:
        return (
            self.system_u_closed_by_endpoint_witness
            or self.system_u_closed_by_symmetric_endpoint_fork
            or self.system_u_closed_by_signed_endpoint_generator
        )

    @property
    def system_c_closed_by_endpoint_witness(self) -> bool:
        witness = self.universal_continuation_endpoint_witness
        return (
            self.k_deficits_routed_to_continuation_endpoint
            and self.universal_continuation_identity_routing is not None
            and witness is not None
            and witness.identity_routing == self.universal_continuation_identity_routing
            and witness.proves_universal_continuation_identity_endpoint_witnesses
        )

    @property
    def system_c_closed_by_symmetric_endpoint_fork(self) -> bool:
        fork = self.universal_continuation_symmetric_endpoint_fork
        return (
            self.k_deficits_routed_to_continuation_endpoint
            and self.universal_continuation_identity_routing is not None
            and fork is not None
            and fork.identity_routing == self.universal_continuation_identity_routing
            and fork.proves_universal_continuation_identity_symmetric_endpoint_cutoff
        )

    @property
    def system_c_closed_by_routed_certificate(self) -> bool:
        return (
            self.system_c_closed_by_endpoint_witness
            or self.system_c_closed_by_symmetric_endpoint_fork
            or self.system_c_closed_by_signed_endpoint_generator
        )

    @property
    def system_m_closed_by_endpoint_witness(self) -> bool:
        witness = self.mixed_unit_context_endpoint_witness
        return (
            self.k_deficits_routed_to_mixed_context_endpoint
            and self.missing_triangular_coordinate_unit_routing is not None
            and witness is not None
            and witness.coordinate_routing == self.missing_triangular_coordinate_unit_routing
            and witness.proves_mixed_unit_context_endpoint_witnesses
        )

    @property
    def system_m_closed_by_symmetric_endpoint_fork(self) -> bool:
        fork = self.mixed_unit_context_symmetric_endpoint_fork
        return (
            self.k_deficits_routed_to_mixed_context_endpoint
            and self.missing_triangular_coordinate_unit_routing is not None
            and fork is not None
            and fork.coordinate_routing == self.missing_triangular_coordinate_unit_routing
            and fork.proves_mixed_unit_context_symmetric_endpoint_cutoff
        )

    @property
    def signed_endpoint_generator_matches_current_kappa(self) -> bool:
        audit = self.universal_k_signed_endpoint_generator
        return (
            audit is not None
            and audit.seed_classifier_entries == self.universal_k_seed_classifier_entries
        )

    @property
    def signed_endpoint_generator_interval_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        audit = self.universal_k_signed_endpoint_generator
        if audit is None or self.universal_k_signed_endpoint_interval is None:
            return ()
        return universal_k_signed_endpoint_required_entry_keys(
            self.universal_k_signed_endpoint_interval,
            audit.reachable_seed_states_exact,
        )

    @property
    def signed_endpoint_generator_missing_interval_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        audit = self.universal_k_signed_endpoint_generator
        if audit is None:
            return ()
        interval_keys = set(self.signed_endpoint_generator_interval_entry_keys)
        supplied = set(audit.required_entry_keys_exact)
        return tuple(key for key in sorted(interval_keys - supplied, key=repr))

    @property
    def signed_endpoint_generator_extra_interval_entry_keys(
        self,
    ) -> Tuple[UniversalKSignedEndpointEntryKey, ...]:
        audit = self.universal_k_signed_endpoint_generator
        if audit is None:
            return ()
        interval_keys = set(self.signed_endpoint_generator_interval_entry_keys)
        supplied = set(audit.required_entry_keys_exact)
        return tuple(key for key in sorted(supplied - interval_keys, key=repr))

    @property
    def signed_endpoint_generator_entry_domain_matches_current_interval(self) -> bool:
        return (
            self.universal_k_signed_endpoint_generator is not None
            and self.universal_k_signed_endpoint_interval is not None
            and not self.signed_endpoint_generator_missing_interval_entry_keys
            and not self.signed_endpoint_generator_extra_interval_entry_keys
        )

    @property
    def signed_endpoint_generator_current_coordinate_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointCoordinateFailure, ...]:
        audit = self.universal_k_signed_endpoint_generator
        interval = self.universal_k_signed_endpoint_interval
        if audit is None or interval is None:
            return ()
        return universal_k_signed_endpoint_coordinate_failures(interval, audit.rows)

    @property
    def signed_endpoint_generator_current_inverse_pairing_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointInverseFailure, ...]:
        audit = self.universal_k_signed_endpoint_generator
        interval = self.universal_k_signed_endpoint_interval
        if audit is None or interval is None:
            return ()
        return universal_k_signed_endpoint_inverse_failures(interval, audit.rows)

    @property
    def signed_endpoint_generator_current_inverse_cancellation_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
        audit = self.universal_k_signed_endpoint_generator
        interval = self.universal_k_signed_endpoint_interval
        if audit is None or interval is None or audit.endpoint_group is None:
            return ()
        return universal_k_signed_endpoint_inverse_cancellation_failures(
            audit.endpoint_group,
            interval,
            audit.rows,
        )

    @property
    def signed_endpoint_generator_current_positive_ybe_path_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointPositiveYBEFailure, ...]:
        audit = self.universal_k_signed_endpoint_generator
        interval = self.universal_k_signed_endpoint_interval
        if audit is None or interval is None:
            return ()
        return universal_k_signed_endpoint_positive_ybe_failures(
            interval,
            audit.reachable_seed_states_exact,
            audit.rows,
        )

    @property
    def signed_endpoint_generator_current_far_commutativity_path_failures(
        self,
    ) -> Tuple[UniversalKSignedEndpointLabelFailure, ...]:
        audit = self.universal_k_signed_endpoint_generator
        interval = self.universal_k_signed_endpoint_interval
        if audit is None or interval is None or audit.endpoint_group is None:
            return ()
        failures = universal_k_signed_endpoint_far_commutativity_failures(
            audit.endpoint_group,
            interval,
            audit.reachable_seed_states_exact,
            audit.rows,
        )
        return tuple(
            failure
            for failure in failures
            if failure[1] != "far_commutativity_label_mismatch"
        )

    @property
    def signed_endpoint_generator_rows_match_current_interval(self) -> bool:
        audit = self.universal_k_signed_endpoint_generator
        return (
            audit is not None
            and self.universal_k_signed_endpoint_interval is not None
            and audit.endpoint_group is not None
            and not self.signed_endpoint_generator_current_coordinate_failures
            and not self.signed_endpoint_generator_current_inverse_pairing_failures
            and not self.signed_endpoint_generator_current_inverse_cancellation_failures
            and not self.signed_endpoint_generator_current_positive_ybe_path_failures
            and not self.signed_endpoint_generator_current_far_commutativity_path_failures
        )

    @property
    def signed_endpoint_generator_closes_current_kappa(self) -> bool:
        audit = self.universal_k_signed_endpoint_generator
        return (
            audit is not None
            and self.signed_endpoint_generator_matches_current_kappa
            and self.signed_endpoint_generator_entry_domain_matches_current_interval
            and self.signed_endpoint_generator_rows_match_current_interval
            and audit.proves_signed_endpoint_generator_tables
        )

    @property
    def signed_endpoint_generator_closed_families(self) -> Tuple[str, ...]:
        audit = self.universal_k_signed_endpoint_generator
        if not self.signed_endpoint_generator_closes_current_kappa or audit is None:
            return ()
        active = set(self.active_routed_endpoint_systems)
        return tuple(
            family for family in audit.required_endpoint_families if family in active
        )

    @property
    def system_u_closed_by_signed_endpoint_generator(self) -> bool:
        return (
            self.system_u_active
            and "U" in self.signed_endpoint_generator_closed_families
        )

    @property
    def system_m_closed_by_routed_certificate(self) -> bool:
        return (
            self.system_m_closed_by_endpoint_witness
            or self.system_m_closed_by_symmetric_endpoint_fork
            or self.system_m_closed_by_signed_endpoint_generator
        )

    @property
    def system_c_closed_by_signed_endpoint_generator(self) -> bool:
        return (
            self.system_c_active
            and "C" in self.signed_endpoint_generator_closed_families
        )

    @property
    def system_m_closed_by_signed_endpoint_generator(self) -> bool:
        return (
            self.system_m_active
            and "M" in self.signed_endpoint_generator_closed_families
        )

    @property
    def active_routed_endpoint_systems(self) -> Tuple[str, ...]:
        systems = []
        if self.system_u_active:
            systems.append("U")
        if self.system_c_active:
            systems.append("C")
        if self.system_m_active:
            systems.append("M")
        return tuple(systems)

    @property
    def unclosed_routed_endpoint_systems(self) -> Tuple[str, ...]:
        systems = []
        if self.system_u_active and not self.system_u_closed_by_routed_certificate:
            systems.append("U")
        if self.system_c_active and not self.system_c_closed_by_routed_certificate:
            systems.append("C")
        if self.system_m_active and not self.system_m_closed_by_routed_certificate:
            systems.append("M")
        return tuple(systems)

    @property
    def all_active_routed_endpoint_systems_closed(self) -> bool:
        return bool(self.active_routed_endpoint_systems) and not self.unclosed_routed_endpoint_systems

    @property
    def universal_k_seed_classifier_entries(
        self,
    ) -> Tuple[UniversalKSeedClassifierEntry, ...]:
        """Finite K_nabla descriptors together with their kappa values."""

        entries = []

        if self.triangular_constant_kernel_recovery_route is not None:
            for pair, reason in self.recovery_routed_k_missing_latin_row_defects:
                side = _side_from_reason(reason)
                if side is None:
                    continue
                descriptor_reason = (
                    "supported_companion_block_image"
                    if "companion_sections_injective_non_surjective" in reason
                    else "constant_map_kernel"
                )
                for row in self.triangular_constant_kernel_recovery_route.rows:
                    if (
                        row.side == side
                        and (row.left_color, row.right_color) == pair
                        and row.routes_universal_kernel_edge_to_recovery
                    ):
                        kernel_kind = _constant_map_kernel_kind_from_reason(reason)
                        witness = (
                            row.domain_color,
                            row.collapsed_inputs,
                            kernel_kind,
                            row.closure_kind,
                        )
                        if descriptor_reason == "supported_companion_block_image":
                            witness = (
                                "support_constant_map_kernel",
                                row.domain_color,
                                row.collapsed_inputs,
                                row.closure_kind,
                            )
                        descriptor = (
                            pair[0],
                            pair[1],
                            _side_symbol(side),
                            descriptor_reason,
                            witness,
                        )
                        entries.append(
                            (
                                descriptor,
                                ("U", _triangular_recovery_endpoint_key((pair, reason))),
                            )
                        )

        if self.missing_triangular_partial_constant_continuation_route is not None:
            continuation_pairs = {
                (_side_from_reason(reason), pair)
                for pair, reason in self.continuation_routed_k_missing_latin_row_defects
            }
            for row in (
                self.missing_triangular_partial_constant_continuation_route
                .universal_continuation_rows
            ):
                if (row.side, (row.left_color, row.right_color)) not in continuation_pairs:
                    continue
                witness = (
                    row.fixed_input,
                    row.domain_color,
                    row.collapsed_inputs,
                    row.companion_output_color,
                    row.companion_outputs,
                    row.closure_kind,
                    row.continuation_seed_closure_kinds,
                    row.partial_edge_contained_in_seed_closure,
                )
                descriptor = (
                    row.left_color,
                    row.right_color,
                    _side_symbol(row.side),
                    "partial_constant_hidden_rank_loss",
                    witness,
                )
                seed_state = (
                    row.left_color,
                    row.right_color,
                    row.side,
                    row.fixed_input,
                    row.domain_color,
                    row.collapsed_inputs,
                    row.companion_output_color,
                    row.companion_outputs,
                )
                entries.append((descriptor, ("C", seed_state)))

        if self.missing_triangular_coordinate_unit_routing is not None:
            mixed_pairs = {
                (_side_from_reason(reason), pair)
                for pair, reason in self.mixed_context_routed_k_missing_latin_row_defects
            }
            for row in self.missing_triangular_coordinate_unit_routing.mixed_unit_context_rows:
                for side in row.coordinate_unit_sides:
                    if (side, (row.left_color, row.right_color)) not in mixed_pairs:
                        continue
                    witness = (
                        row.coordinate_unit_sides,
                        row.left_explanation,
                        row.right_explanation,
                        row.left_unit_inputs,
                        row.left_nonunit_inputs,
                        row.right_unit_inputs,
                        row.right_nonunit_inputs,
                    )
                    descriptor = (
                        row.left_color,
                        row.right_color,
                        _side_symbol(side),
                        "coordinate_side_unit_not_triangular",
                        witness,
                    )
                    seed_state = (row.left_color, row.right_color, side)
                    entries.append((descriptor, ("M", seed_state)))

        return tuple(sorted(entries, key=repr))

    @property
    def universal_k_row_normal_form_domain(
        self,
    ) -> Tuple[UniversalKRowDescriptor, ...]:
        return tuple(entry[0] for entry in self.universal_k_seed_classifier_entries)

    @property
    def system_name(self) -> str:
        if self.closed_by_recorded_branch:
            return "closed_by_recorded_branch"
        if self.unsupported_companion_structural_obligation_active:
            return "unsupported_companion_structural_contradiction_obligation"
        if self.system_k_closed_by_proper_defect_closure:
            return "closed_by_triangular_latin_proper_closure"
        if self.system_k_closed_by_partial_constant_proper_closure:
            return "closed_by_missing_triangular_partial_constant_proper_closure"
        if self.all_active_routed_endpoint_systems_closed:
            if self.active_routed_endpoint_systems == ("U",):
                if self.system_u_closed_by_endpoint_witness:
                    return "closed_by_triangular_recovery_endpoint_witness"
                return "closed_by_triangular_recovery_symmetric_endpoint_fork"
            if self.active_routed_endpoint_systems == ("C",):
                if self.system_c_closed_by_endpoint_witness:
                    return "closed_by_universal_continuation_endpoint_witness"
                return "closed_by_universal_continuation_symmetric_endpoint_fork"
            if self.active_routed_endpoint_systems == ("M",):
                if self.system_m_closed_by_endpoint_witness:
                    return "closed_by_mixed_unit_context_endpoint_witness"
                return "closed_by_mixed_unit_symmetric_endpoint_fork"
            if (
                self.triangular_recovery_symmetric_endpoint_fork is not None
                or self.universal_continuation_symmetric_endpoint_fork is not None
                or self.mixed_unit_context_symmetric_endpoint_fork is not None
            ):
                return "closed_by_routed_endpoint_certificates"
            return "closed_by_routed_endpoint_witnesses"
        if len(self.unclosed_routed_endpoint_systems) > 1:
            joined = "".join(system.lower() for system in self.unclosed_routed_endpoint_systems)
            return f"system_{joined}_routed_endpoint_product"
        if self.k_deficits_closed_by_recorded_routing:
            return "closed_by_recorded_k_deficit_routing"
        if self.system_k_active:
            return "system_k_kink_completion_deficit"
        if self.system_u_active and not self.system_u_closed_by_routed_certificate:
            return "system_u_triangular_recovery_unit_endpoint"
        if self.system_c_active and not self.system_c_closed_by_routed_certificate:
            return "system_c_universal_continuation_endpoint"
        if self.system_m_active and not self.system_m_closed_by_routed_certificate:
            return "system_m_mixed_unit_context_endpoint"
        return f"earlier_unrouted_status:{self.refinement.status}"

    @property
    def is_current_remaining_finite_system(self) -> bool:
        if self.unsupported_companion_structural_obligation_active:
            return True
        if self.system_k_closed_by_proper_generated_closure:
            return False
        return (
            self.system_k_active
            or bool(self.unclosed_routed_endpoint_systems)
        )

    @property
    def k_left_side_dual_replacement_rows(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str, Tuple[str, ...], Tuple[str, ...]], ...]:
        right_latin_pairs = set(self.refinement.right_latin_row_pairs)
        right_triangular_pairs = set(self.refinement.right_triangular_row_pairs)
        right_defects = {}
        for pair, reason in self.refinement.missing_right_latin_row_defects:
            right_defects.setdefault(pair, []).append(reason)
        right_profiles = {}
        if self.missing_triangular_row_profile is not None:
            for row in self.missing_triangular_row_profile.rows:
                if row.side != "right":
                    continue
                right_profiles.setdefault((row.left_color, row.right_color), []).append(
                    row.explanation
                )

        rows = []
        for pair in self.refinement.missing_left_latin_row_pairs:
            if pair in right_latin_pairs:
                status = "side_dual_right_latin_available"
            elif pair in right_triangular_pairs:
                status = "side_dual_right_triangular_nonlatin"
            else:
                status = "no_side_dual_right_triangular_replacement"
            rows.append(
                (
                    pair,
                    status,
                    tuple(right_defects.get(pair, ())),
                    tuple(right_profiles.get(pair, ())),
                )
            )
        return tuple(rows)

    @property
    def _universal_continuation_identity_routing_data(self) -> Tuple[Tuple[str, object], ...]:
        if self.universal_continuation_identity_routing is None:
            return ()
        routing = self.universal_continuation_identity_routing
        return (
            (
                "universal_continuation_identity_lost_edges",
                routing.routing.lost_edges,
            ),
            (
                "universal_continuation_identity_unrouted_edges",
                routing.routing.unrouted_edges,
            ),
            (
                "universal_continuation_identity_routing_proved",
                routing.proves_identity_routed_universal_continuation,
            ),
        )

    @property
    def _triangular_recovery_endpoint_witness_data(self) -> Tuple[Tuple[str, object], ...]:
        if self.triangular_recovery_endpoint_witness is None:
            return ()
        witness = self.triangular_recovery_endpoint_witness
        return (
            (
                "triangular_recovery_endpoint_witness_matches_system",
                witness.observer == self.refinement.triangular_recovery_unit_observer
                and witness.routed_keys
                == _sorted_triangular_recovery_endpoint_keys(
                    tuple(
                        _triangular_recovery_endpoint_key(defect)
                        for defect in self.system_u_endpoint_defects
                    )
                ),
            ),
            (
                "triangular_recovery_endpoint_witness_proved",
                witness.proves_triangular_recovery_endpoint_witnesses,
            ),
            (
                "triangular_recovery_endpoint_missing_keys",
                witness.missing_routed_keys,
            ),
            (
                "triangular_recovery_endpoint_extra_keys",
                witness.extra_witness_keys,
            ),
        )

    @property
    def _triangular_recovery_symmetric_endpoint_fork_data(
        self,
    ) -> Tuple[Tuple[str, object], ...]:
        if self.triangular_recovery_symmetric_endpoint_fork is None:
            return ()
        fork = self.triangular_recovery_symmetric_endpoint_fork
        return (
            (
                "triangular_recovery_symmetric_fork_matches_system",
                fork.observer == self.refinement.triangular_recovery_unit_observer
                and fork.routed_keys
                == _sorted_triangular_recovery_endpoint_keys(
                    tuple(
                        _triangular_recovery_endpoint_key(defect)
                        for defect in self.system_u_endpoint_defects
                    )
                ),
            ),
            (
                "triangular_recovery_symmetric_fork_group_orders",
                fork.endpoint_family.endpoint_group_orders,
            ),
            (
                "triangular_recovery_symmetric_fork_minimum_degree",
                fork.endpoint_family.minimum_symmetric_degree,
            ),
            (
                "triangular_recovery_symmetric_fork_degree",
                fork.endpoint_family.symmetric_degree,
            ),
            (
                "triangular_recovery_symmetric_fork_cutoff_proved",
                fork.proves_triangular_recovery_symmetric_endpoint_cutoff,
            ),
            (
                "triangular_recovery_symmetric_fork_tail_seed_prefix_proved",
                fork.proves_triangular_recovery_symmetric_tail_seed_prefix,
            ),
            (
                "triangular_recovery_symmetric_fork_missing_keys",
                fork.missing_routed_keys,
            ),
            (
                "triangular_recovery_symmetric_fork_extra_keys",
                fork.extra_covered_keys,
            ),
        )

    @property
    def _universal_continuation_endpoint_witness_data(
        self,
    ) -> Tuple[Tuple[str, object], ...]:
        if self.universal_continuation_endpoint_witness is None:
            return ()
        witness = self.universal_continuation_endpoint_witness
        return (
            (
                "universal_continuation_endpoint_witness_matches_routing",
                self.universal_continuation_identity_routing is not None
                and witness.identity_routing == self.universal_continuation_identity_routing,
            ),
            (
                "universal_continuation_endpoint_witness_proved",
                witness.proves_universal_continuation_identity_endpoint_witnesses,
            ),
            (
                "universal_continuation_endpoint_missing_edges",
                witness.missing_identity_routed_edges,
            ),
            (
                "universal_continuation_endpoint_extra_edges",
                witness.extra_witness_edges,
            ),
        )

    @property
    def _universal_continuation_symmetric_endpoint_fork_data(
        self,
    ) -> Tuple[Tuple[str, object], ...]:
        if self.universal_continuation_symmetric_endpoint_fork is None:
            return ()
        fork = self.universal_continuation_symmetric_endpoint_fork
        return (
            (
                "universal_continuation_symmetric_fork_matches_routing",
                self.universal_continuation_identity_routing is not None
                and fork.identity_routing == self.universal_continuation_identity_routing,
            ),
            (
                "universal_continuation_symmetric_fork_group_orders",
                fork.endpoint_family.endpoint_group_orders,
            ),
            (
                "universal_continuation_symmetric_fork_minimum_degree",
                fork.endpoint_family.minimum_symmetric_degree,
            ),
            (
                "universal_continuation_symmetric_fork_degree",
                fork.endpoint_family.symmetric_degree,
            ),
            (
                "universal_continuation_symmetric_fork_cutoff_proved",
                fork.proves_universal_continuation_identity_symmetric_endpoint_cutoff,
            ),
            (
                "universal_continuation_symmetric_fork_tail_seed_prefix_proved",
                fork.proves_universal_continuation_identity_symmetric_tail_seed_prefix,
            ),
            (
                "universal_continuation_symmetric_fork_missing_edges",
                fork.missing_identity_routed_edges,
            ),
            (
                "universal_continuation_symmetric_fork_extra_edges",
                fork.extra_covered_edges,
            ),
        )

    @property
    def _coordinate_unit_routing_data(self) -> Tuple[Tuple[str, object], ...]:
        if self.missing_triangular_coordinate_unit_routing is None:
            return ()
        routing = self.missing_triangular_coordinate_unit_routing
        return (
            (
                "missing_triangular_coordinate_unit_mixed_rows",
                tuple(
                    (
                        row.left_color,
                        row.right_color,
                        row.coordinate_unit_sides,
                        row.left_explanation,
                        row.right_explanation,
                    )
                    for row in routing.mixed_unit_context_rows
                ),
            ),
            (
                "missing_triangular_coordinate_unit_unrouted_rows",
                tuple(
                    (
                        row.left_color,
                        row.right_color,
                        row.coordinate_unit_sides,
                        row.left_explanation,
                        row.right_explanation,
                    )
                    for row in routing.unrouted_rows
                ),
            ),
            (
                "missing_triangular_coordinate_unit_unclosed_two_sided_rows",
                tuple(
                    (
                        row.left_color,
                        row.right_color,
                        row.coordinate_unit_sides,
                        row.left_explanation,
                        row.right_explanation,
                    )
                    for row in routing.unclosed_two_sided_unit_pair_rows
                ),
            ),
            (
                "missing_triangular_coordinate_unit_routing_proved",
                routing.proves_coordinate_unit_routing_ledger,
            ),
        )

    @property
    def _mixed_unit_endpoint_witness_data(self) -> Tuple[Tuple[str, object], ...]:
        if self.mixed_unit_context_endpoint_witness is None:
            return ()
        witness = self.mixed_unit_context_endpoint_witness
        return (
            (
                "mixed_unit_endpoint_witness_matches_routing",
                self.missing_triangular_coordinate_unit_routing is not None
                and witness.coordinate_routing
                == self.missing_triangular_coordinate_unit_routing,
            ),
            (
                "mixed_unit_endpoint_witness_proved",
                witness.proves_mixed_unit_context_endpoint_witnesses,
            ),
            (
                "mixed_unit_endpoint_missing_context_keys",
                witness.missing_mixed_context_keys,
            ),
            (
                "mixed_unit_endpoint_extra_context_keys",
                witness.extra_witness_keys,
            ),
        )

    @property
    def _mixed_unit_symmetric_endpoint_fork_data(
        self,
    ) -> Tuple[Tuple[str, object], ...]:
        if self.mixed_unit_context_symmetric_endpoint_fork is None:
            return ()
        fork = self.mixed_unit_context_symmetric_endpoint_fork
        return (
            (
                "mixed_unit_symmetric_fork_matches_routing",
                self.missing_triangular_coordinate_unit_routing is not None
                and fork.coordinate_routing
                == self.missing_triangular_coordinate_unit_routing,
            ),
            (
                "mixed_unit_symmetric_fork_group_orders",
                fork.endpoint_family.endpoint_group_orders,
            ),
            (
                "mixed_unit_symmetric_fork_minimum_degree",
                fork.endpoint_family.minimum_symmetric_degree,
            ),
            (
                "mixed_unit_symmetric_fork_degree",
                fork.endpoint_family.symmetric_degree,
            ),
            (
                "mixed_unit_symmetric_fork_cutoff_proved",
                fork.proves_mixed_unit_context_symmetric_endpoint_cutoff,
            ),
            (
                "mixed_unit_symmetric_fork_tail_seed_prefix_proved",
                fork.proves_mixed_unit_context_symmetric_tail_seed_prefix,
            ),
            (
                "mixed_unit_symmetric_fork_missing_context_keys",
                fork.missing_mixed_context_keys,
            ),
            (
                "mixed_unit_symmetric_fork_extra_context_keys",
                fork.extra_covered_keys,
            ),
        )

    @property
    def _universal_k_signed_endpoint_generator_data(
        self,
    ) -> Tuple[Tuple[str, object], ...]:
        audit = self.universal_k_signed_endpoint_generator
        if audit is None:
            return (
                (
                    "signed_endpoint_generator_required_seed_states",
                    tuple(
                        sorted(
                            {
                                classifier_entry[1]
                                for classifier_entry in (
                                    self.universal_k_seed_classifier_entries
                                )
                            },
                            key=repr,
                        )
                    ),
                ),
                ("signed_endpoint_generator_duplicate_seed_classifier_entries", ()),
                ("signed_endpoint_generator_duplicate_seed_classifier_descriptors", ()),
                ("signed_endpoint_generator_conflicting_seed_classifier_descriptors", ()),
                ("signed_endpoint_generator_invalid_seed_classifier_targets", ()),
                ("signed_endpoint_generator_matches_current_kappa", False),
                (
                    "signed_endpoint_generator_entry_domain_matches_current_interval",
                    False,
                ),
                ("signed_endpoint_generator_missing_current_interval_entry_keys", ()),
                ("signed_endpoint_generator_extra_current_interval_entry_keys", ()),
                (
                    "signed_endpoint_generator_rows_match_current_interval",
                    False,
                ),
                (
                    "signed_endpoint_generator_current_coordinate_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_current_inverse_pairing_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_current_inverse_cancellation_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_current_positive_ybe_path_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_current_far_commutativity_path_failures",
                    (),
                ),
                ("signed_endpoint_generator_closes_current_kappa", False),
                ("signed_endpoint_generator_closed_families", ()),
                ("signed_endpoint_generator_reachable_seed_states", ()),
                ("signed_endpoint_generator_duplicate_reachable_seed_states", ()),
                ("signed_endpoint_generator_invalid_reachable_seed_states", ()),
                ("signed_endpoint_generator_transition_reachable_seed_states", ()),
                ("signed_endpoint_generator_unreachable_declared_seed_states", ()),
                ("signed_endpoint_generator_missing_transition_reachable_seed_states", ()),
                ("signed_endpoint_generator_reachable_closure_exact", False),
                ("signed_endpoint_generator_required_entry_keys", ()),
                ("signed_endpoint_generator_entry_domain_derived_from_interval", False),
                ("signed_endpoint_generator_finite_checks_derived_from_tables", False),
                ("signed_endpoint_generator_missing_entry_keys", ()),
                ("signed_endpoint_generator_endpoint_targets_fixed", False),
                ("signed_endpoint_generator_endpoint_targets_flag_supplied", False),
                (
                    "signed_endpoint_generator_endpoint_target_scope_matches_required",
                    False,
                ),
                ("signed_endpoint_generator_endpoint_target_expected_families", ()),
                ("signed_endpoint_generator_endpoint_target_covered_families", ()),
                ("signed_endpoint_generator_endpoint_target_families", ()),
                ("signed_endpoint_generator_endpoint_target_group_orders", ()),
                (
                    "signed_endpoint_generator_endpoint_target_malformed_group_orders",
                    (),
                ),
                (
                    "signed_endpoint_generator_endpoint_target_malformed_group_order_rows",
                    (),
                ),
                ("signed_endpoint_generator_endpoint_group_order", None),
                (
                    "signed_endpoint_generator_endpoint_group_order_matches_target",
                    False,
                ),
                ("signed_endpoint_generator_endpoint_group_target_families", ()),
                (
                    "signed_endpoint_generator_endpoint_group_family_support_verified",
                    False,
                ),
                (
                    "signed_endpoint_generator_endpoint_group_family_support_failures",
                    (),
                ),
                ("signed_endpoint_generator_endpoint_target_cutoff_degrees", ()),
                (
                    "signed_endpoint_generator_endpoint_target_malformed_cutoff_degrees",
                    (),
                ),
                (
                    "signed_endpoint_generator_endpoint_target_malformed_cutoff_degree_rows",
                    (),
                ),
                ("signed_endpoint_generator_endpoint_target_duplicate_families", ()),
                ("signed_endpoint_generator_endpoint_target_unknown_families", ()),
                (
                    "signed_endpoint_generator_endpoint_target_duplicate_target_families",
                    (),
                ),
                ("signed_endpoint_generator_endpoint_target_audit_proved", False),
                ("signed_endpoint_generator_coordinate_components_verified", False),
                ("signed_endpoint_generator_coordinate_failures", ()),
                ("signed_endpoint_generator_inverse_pairing_verified", False),
                ("signed_endpoint_generator_inverse_pairing_failures", ()),
                ("signed_endpoint_generator_inverse_cancellation_verified", False),
                ("signed_endpoint_generator_inverse_cancellation_failures", ()),
                ("signed_endpoint_generator_positive_ybe_path_verified", False),
                ("signed_endpoint_generator_positive_ybe_path_failures", ()),
                ("signed_endpoint_generator_positive_ybe_cocycle_verified", False),
                ("signed_endpoint_generator_positive_ybe_cocycle_failures", ()),
                (
                    "signed_endpoint_generator_positive_ybe_label_diagnostics",
                    (),
                ),
                ("signed_endpoint_generator_far_commutativity_verified", False),
                ("signed_endpoint_generator_far_commutativity_failures", ()),
                ("signed_endpoint_generator_far_commutativity_path_failures", ()),
                (
                    "signed_endpoint_generator_far_commutativity_label_diagnostics",
                    (),
                ),
                (
                    "signed_endpoint_generator_explicit_monodromy_representation_verified",
                    False,
                ),
                (
                    "signed_endpoint_generator_explicit_monodromy_representation_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_positive_monodromy_permutation_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_positive_monodromy_representation_verified",
                    False,
                ),
                ("signed_endpoint_generator_two_strand_witness_domain_exact", False),
                ("signed_endpoint_generator_two_strand_witness_domain_failures", ()),
                ("signed_endpoint_generator_two_strand_base_verified", False),
                ("signed_endpoint_generator_two_strand_base_failures", ()),
                ("signed_endpoint_generator_artin_update_verified", False),
                ("signed_endpoint_generator_artin_update_failures", ()),
                ("signed_endpoint_generator_telescoping_detector_verified", False),
                (
                    "signed_endpoint_generator_telescoping_detector_scope_matches_required",
                    False,
                ),
                (
                    "signed_endpoint_generator_telescoping_endpoint_group_matches",
                    False,
                ),
                (
                    "signed_endpoint_generator_telescoping_signed_row_mismatches",
                    (),
                ),
                (
                    "signed_endpoint_generator_telescoping_extra_diagnostic_entry_keys",
                    (),
                ),
                ("signed_endpoint_generator_telescoping_expected_entry_keys", ()),
                ("signed_endpoint_generator_telescoping_covered_entry_keys", ()),
                (
                    "signed_endpoint_generator_telescoping_expected_positive_entry_keys",
                    (),
                ),
                (
                    "signed_endpoint_generator_telescoping_covered_positive_entry_keys",
                    (),
                ),
                ("signed_endpoint_generator_telescoping_missing_entry_keys", ()),
                ("signed_endpoint_generator_telescoping_extra_entry_keys", ()),
                ("signed_endpoint_generator_telescoping_duplicate_entry_keys", ()),
                (
                    "signed_endpoint_generator_telescoping_duplicate_positive_entry_keys",
                    (),
                ),
                (
                    "signed_endpoint_generator_telescoping_malformed_entry_keys",
                    (),
                ),
                ("signed_endpoint_generator_telescoping_expected_seed_states", ()),
                ("signed_endpoint_generator_telescoping_covered_seed_states", ()),
                ("signed_endpoint_generator_telescoping_duplicate_seed_states", ()),
                ("signed_endpoint_generator_telescoping_malformed_seed_states", ()),
                ("signed_endpoint_generator_detector_track_counts_by_family", ()),
                ("signed_endpoint_generator_detector_track_count_malformed_rows", ()),
                (
                    "signed_endpoint_generator_detector_track_count_unknown_families",
                    (),
                ),
                (
                    "signed_endpoint_generator_detector_track_count_malformed_values",
                    (),
                ),
                ("signed_endpoint_generator_detector_track_count_duplicate_families", ()),
                (
                    "signed_endpoint_generator_detector_track_count_family_scope_exact",
                    False,
                ),
                (
                    "signed_endpoint_generator_detector_track_count_matches_family_sum",
                    False,
                ),
                ("signed_endpoint_generator_fixed_detector_track_count", None),
                ("signed_endpoint_generator_detector_track_initialization_rows", ()),
                (
                    "signed_endpoint_generator_detector_track_initialization_missing_keys",
                    (),
                ),
                (
                    "signed_endpoint_generator_detector_track_initialization_extra_keys",
                    (),
                ),
                (
                    "signed_endpoint_generator_detector_track_initialization_duplicate_keys",
                    (),
                ),
                (
                    "signed_endpoint_generator_detector_track_initialization_invalid_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_detector_track_initialization_unfixed_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_detector_track_initialization_template_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_detector_track_initialization_rows_exact",
                    False,
                ),
                (
                    "signed_endpoint_generator_detector_tracks_fixed_before_braid",
                    False,
                ),
                (
                    "signed_endpoint_generator_detector_track_initialization_verified",
                    False,
                ),
                (
                    "signed_endpoint_generator_artin_detector_recurrence_verified",
                    False,
                ),
                ("signed_endpoint_generator_word_potential_expected_seed_states", ()),
                ("signed_endpoint_generator_word_potential_covered_seed_states", ()),
                ("signed_endpoint_generator_word_potential_duplicate_seed_states", ()),
                ("signed_endpoint_generator_word_potential_malformed_seed_states", ()),
                (
                    "signed_endpoint_generator_word_potential_seed_state_scope_matches_expected",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_templates_use_only_current_longitudes",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_track_scope_verified",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_track_scope_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_initialized_raw_assignment_variables",
                    {},
                ),
                (
                    "signed_endpoint_generator_word_potential_raw_assignment_scope_verified",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_raw_assignment_scope_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_word_potential_artin_substitution_verified",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_identity_verified",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_detector_domains_sound",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_detector_domain_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_word_potential_coboundary_defects_constant",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_coboundary_defect_failures",
                    (),
                ),
                (
                    "signed_endpoint_generator_word_potential_malformed_identity_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_word_potential_certificate_malformed_next_seed_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_word_potential_certificate_malformed_template_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_word_potential_certificate_malformed_normalized_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_terminal_readout_longitudes_verified",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_initial_normalized",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_initial_seed_states_normalized",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_normalized_seed_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_word_potential_initial_seed_state_scope_exact",
                    False,
                ),
                (
                    "signed_endpoint_generator_word_potential_missing_initial_normalized_seed_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_word_potential_extra_initial_normalized_seed_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_telescoping_braid_index_independent",
                    False,
                ),
                ("signed_endpoint_generator_cutoff_readouts_exact", False),
                ("signed_endpoint_generator_cutoff_readouts_flag_supplied", False),
                ("signed_endpoint_generator_cutoff_readout_scope_matches_required", False),
                ("signed_endpoint_generator_required_cutoff_families", ()),
                (
                    "signed_endpoint_generator_cutoff_target_degrees_match_readout",
                    False,
                ),
                (
                    "signed_endpoint_generator_cutoff_target_degree_mismatches",
                    (),
                ),
                ("signed_endpoint_generator_cutoff_readout_expected_states", ()),
                ("signed_endpoint_generator_cutoff_readout_covered_states", ()),
                ("signed_endpoint_generator_cutoff_readout_expected_families", ()),
                ("signed_endpoint_generator_cutoff_readout_covered_families", ()),
                ("signed_endpoint_generator_cutoff_readout_row_families", ()),
                ("signed_endpoint_generator_cutoff_readout_missing_families", ()),
                ("signed_endpoint_generator_cutoff_readout_extra_families", ()),
                (
                    "signed_endpoint_generator_cutoff_readout_missing_row_families",
                    (),
                ),
                (
                    "signed_endpoint_generator_cutoff_readout_extra_row_families",
                    (),
                ),
                ("signed_endpoint_generator_cutoff_readout_family_scope_exact", False),
                ("signed_endpoint_generator_cutoff_readout_missing_states", ()),
                ("signed_endpoint_generator_cutoff_readout_extra_states", ()),
                ("signed_endpoint_generator_cutoff_readout_duplicate_states", ()),
                ("signed_endpoint_generator_cutoff_readout_malformed_states", ()),
                ("signed_endpoint_generator_cutoff_readout_degree", None),
                ("signed_endpoint_generator_cutoff_readout_rows", ()),
                ("signed_endpoint_generator_cutoff_readout_malformed_row_states", ()),
                (
                    "signed_endpoint_generator_cutoff_readout_invalid_permutation_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_cutoff_readout_duplicate_permutations",
                    (),
                ),
                (
                    "signed_endpoint_generator_cutoff_readout_unkilled_rows",
                    (),
                ),
                ("signed_endpoint_generator_cutoff_readout_audit_proved", False),
                ("signed_endpoint_generator_residual_faithfulness_verified", False),
                ("signed_endpoint_generator_residual_faithfulness_flag_supplied", False),
                ("signed_endpoint_generator_residual_action_scope_matches_required", False),
                ("signed_endpoint_generator_residual_action_scope_matches_seed_states", False),
                ("signed_endpoint_generator_residual_action_scope_matches_rows", False),
                ("signed_endpoint_generator_residual_action_scope_expected_states", ()),
                ("signed_endpoint_generator_residual_action_scope_covered_states", ()),
                (
                    "signed_endpoint_generator_residual_action_scope_malformed_row_counts",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_scope_duplicate_seed_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_scope_malformed_seed_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_scope_unknown_families",
                    (),
                ),
                ("signed_endpoint_generator_residual_action_scope_family_rows", ()),
                (
                    "signed_endpoint_generator_residual_action_scope_family_rows_covered",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_scope_duplicate_family_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_scope_malformed_family_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_scope_malformed_family_row_count_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_scope_family_rows_cover_active",
                    False,
                ),
                ("signed_endpoint_generator_residual_action_scope_dependencies", ()),
                (
                    "signed_endpoint_generator_residual_action_scope_invalid_dependencies",
                    (),
                ),
                ("signed_endpoint_generator_residual_action_scope_proved", False),
                ("signed_endpoint_generator_residual_theorem_proved", False),
                ("signed_endpoint_generator_residual_theorem_scope_matches_required", False),
                ("signed_endpoint_generator_residual_theorem_scope_matches_seed_states", False),
                ("signed_endpoint_generator_residual_theorem_expected_states", ()),
                ("signed_endpoint_generator_residual_theorem_covered_states", ()),
                (
                    "signed_endpoint_generator_residual_theorem_malformed_row_counts",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_duplicate_seed_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_malformed_seed_states",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_unknown_families",
                    (),
                ),
                ("signed_endpoint_generator_residual_theorem_family_rows", ()),
                (
                    "signed_endpoint_generator_residual_theorem_family_rows_covered",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_duplicate_family_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_malformed_family_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_malformed_family_row_count_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_actual_family_rows",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_family_rows_match_actual",
                    False,
                ),
                (
                    "signed_endpoint_generator_residual_theorem_expected_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_covered_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_missing_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_extra_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_duplicate_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_input_tuple_domain_exact",
                    False,
                ),
                ("signed_endpoint_generator_residual_theorem_rows", ()),
                ("signed_endpoint_generator_residual_theorem_invalid_rows", ()),
                (
                    "signed_endpoint_generator_residual_theorem_malformed_channel_keys",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_channel_key_seed_mismatches",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_theorem_rows_cover_input_domain",
                    False,
                ),
                (
                    "signed_endpoint_generator_residual_theorem_rows_cover_families",
                    False,
                ),
                (
                    "signed_endpoint_generator_residual_theorem_rows_cover_seed_states",
                    False,
                ),
                ("signed_endpoint_generator_residual_action_rows", 0),
                ("signed_endpoint_generator_residual_action_rows_expected", None),
                (
                    "signed_endpoint_generator_residual_action_expected_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_supplied_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_missing_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_extra_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_duplicate_input_tuples",
                    (),
                ),
                (
                    "signed_endpoint_generator_residual_action_input_tuple_domain_exact",
                    False,
                ),
                ("signed_endpoint_generator_residual_action_complete", False),
                ("signed_endpoint_generator_tables_proved", False),
            )
        matches_current_kappa = (
            audit.seed_classifier_entries == self.universal_k_seed_classifier_entries
        )
        endpoint_target_audit = audit.endpoint_target_audit
        telescoping_audit = audit.telescoping_detector_audit
        failure_reasons = audit.failure_reasons
        if not matches_current_kappa:
            failure_reasons = failure_reasons + ("seed_classifier_entries_mismatch",)
        if not self.signed_endpoint_generator_entry_domain_matches_current_interval:
            failure_reasons = failure_reasons + (
                "signed_entry_domain_mismatch_current_interval",
            )
        if not self.signed_endpoint_generator_rows_match_current_interval:
            failure_reasons = failure_reasons + (
                "signed_row_checks_mismatch_current_interval",
            )
        return (
            (
                "signed_endpoint_generator_matches_current_kappa",
                matches_current_kappa,
            ),
            (
                "signed_endpoint_generator_entry_domain_matches_current_interval",
                self.signed_endpoint_generator_entry_domain_matches_current_interval,
            ),
            (
                "signed_endpoint_generator_missing_current_interval_entry_keys",
                self.signed_endpoint_generator_missing_interval_entry_keys,
            ),
            (
                "signed_endpoint_generator_extra_current_interval_entry_keys",
                self.signed_endpoint_generator_extra_interval_entry_keys,
            ),
            (
                "signed_endpoint_generator_rows_match_current_interval",
                self.signed_endpoint_generator_rows_match_current_interval,
            ),
            (
                "signed_endpoint_generator_current_coordinate_failures",
                self.signed_endpoint_generator_current_coordinate_failures,
            ),
            (
                "signed_endpoint_generator_current_inverse_pairing_failures",
                self.signed_endpoint_generator_current_inverse_pairing_failures,
            ),
            (
                "signed_endpoint_generator_current_inverse_cancellation_failures",
                self.signed_endpoint_generator_current_inverse_cancellation_failures,
            ),
            (
                "signed_endpoint_generator_current_positive_ybe_path_failures",
                self.signed_endpoint_generator_current_positive_ybe_path_failures,
            ),
            (
                "signed_endpoint_generator_current_far_commutativity_path_failures",
                self.signed_endpoint_generator_current_far_commutativity_path_failures,
            ),
            (
                "signed_endpoint_generator_closes_current_kappa",
                self.signed_endpoint_generator_closes_current_kappa,
            ),
            (
                "signed_endpoint_generator_closed_families",
                self.signed_endpoint_generator_closed_families,
            ),
            (
                "signed_endpoint_generator_required_seed_states",
                audit.required_seed_states,
            ),
            (
                "signed_endpoint_generator_duplicate_seed_classifier_entries",
                audit.duplicate_seed_classifier_entries,
            ),
            (
                "signed_endpoint_generator_duplicate_seed_classifier_descriptors",
                audit.duplicate_seed_classifier_descriptors,
            ),
            (
                "signed_endpoint_generator_conflicting_seed_classifier_descriptors",
                audit.conflicting_seed_classifier_descriptors,
            ),
            (
                "signed_endpoint_generator_invalid_seed_classifier_targets",
                audit.invalid_seed_classifier_targets,
            ),
            (
                "signed_endpoint_generator_reachable_seed_states",
                audit.reachable_seed_states_exact,
            ),
            (
                "signed_endpoint_generator_duplicate_reachable_seed_states",
                audit.duplicate_reachable_seed_states,
            ),
            (
                "signed_endpoint_generator_invalid_reachable_seed_states",
                audit.invalid_reachable_seed_states,
            ),
            (
                "signed_endpoint_generator_transition_reachable_seed_states",
                audit.transition_reachable_seed_states,
            ),
            (
                "signed_endpoint_generator_unreachable_declared_seed_states",
                audit.unreachable_declared_seed_states,
            ),
            (
                "signed_endpoint_generator_missing_transition_reachable_seed_states",
                audit.missing_transition_reachable_seed_states,
            ),
            (
                "signed_endpoint_generator_reachable_closure_exact",
                audit.reachable_seed_state_closure_exact,
            ),
            (
                "signed_endpoint_generator_missing_initial_seed_states",
                audit.missing_initial_seed_states,
            ),
            (
                "signed_endpoint_generator_required_signed_seed_keys",
                audit.required_signed_seed_keys,
            ),
            (
                "signed_endpoint_generator_required_entry_keys",
                audit.required_entry_keys_exact,
            ),
            (
                "signed_endpoint_generator_entry_domain_derived_from_interval",
                audit.entry_domain_derived_from_interval,
            ),
            (
                "signed_endpoint_generator_finite_checks_derived_from_tables",
                audit.finite_row_checks_derived_from_tables,
            ),
            (
                "signed_endpoint_generator_supplied_entry_keys",
                audit.supplied_entry_keys,
            ),
            (
                "signed_endpoint_generator_missing_entry_keys",
                audit.missing_entry_keys,
            ),
            (
                "signed_endpoint_generator_extra_entry_keys",
                audit.extra_entry_keys,
            ),
            (
                "signed_endpoint_generator_supplied_signed_seed_keys",
                audit.supplied_signed_seed_keys,
            ),
            (
                "signed_endpoint_generator_missing_signed_seed_keys",
                audit.missing_signed_seed_keys,
            ),
            (
                "signed_endpoint_generator_extra_signed_seed_keys",
                audit.extra_signed_seed_keys,
            ),
            (
                "signed_endpoint_generator_duplicate_entries",
                audit.duplicate_entry_keys,
            ),
            (
                "signed_endpoint_generator_endpoint_targets_fixed",
                audit.endpoint_targets_proved,
            ),
            (
                "signed_endpoint_generator_endpoint_targets_flag_supplied",
                audit.endpoint_targets_fixed,
            ),
            (
                "signed_endpoint_generator_endpoint_target_scope_matches_required",
                audit.endpoint_target_scope_matches_required,
            ),
            (
                "signed_endpoint_generator_endpoint_target_expected_families",
                (
                    endpoint_target_audit.expected_endpoint_families_exact
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_covered_families",
                (
                    endpoint_target_audit.covered_endpoint_families_exact
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_families",
                (
                    endpoint_target_audit.target_endpoint_families
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_group_orders",
                (
                    endpoint_target_audit.endpoint_group_orders
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_malformed_group_orders",
                (
                    endpoint_target_audit.malformed_endpoint_group_orders
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_malformed_group_order_rows",
                (
                    endpoint_target_audit.malformed_endpoint_group_order_rows
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_group_order",
                (
                    len(audit.endpoint_group.elements)
                    if audit.endpoint_group is not None
                    else None
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_group_order_matches_target",
                audit.endpoint_group_order_matches_target_audit,
            ),
            (
                "signed_endpoint_generator_endpoint_group_target_families",
                audit.endpoint_group_target_families,
            ),
            (
                "signed_endpoint_generator_endpoint_group_family_support_verified",
                audit.endpoint_group_family_support_proved,
            ),
            (
                "signed_endpoint_generator_endpoint_group_family_support_failures",
                audit.endpoint_group_family_support_failures,
            ),
            (
                "signed_endpoint_generator_endpoint_target_cutoff_degrees",
                (
                    endpoint_target_audit.cutoff_degrees
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_malformed_cutoff_degrees",
                (
                    endpoint_target_audit.malformed_cutoff_degrees
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_malformed_cutoff_degree_rows",
                (
                    endpoint_target_audit.malformed_cutoff_degree_rows
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_duplicate_families",
                (
                    endpoint_target_audit.duplicate_expected_endpoint_families
                    + endpoint_target_audit.duplicate_covered_endpoint_families
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_unknown_families",
                (
                    endpoint_target_audit.invalid_expected_endpoint_families
                    + endpoint_target_audit.invalid_covered_endpoint_families
                    + endpoint_target_audit.invalid_target_endpoint_families
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_duplicate_target_families",
                (
                    endpoint_target_audit.duplicate_target_endpoint_families
                    if endpoint_target_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_endpoint_target_audit_proved",
                (
                    endpoint_target_audit.proves_endpoint_targets
                    if endpoint_target_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_coordinate_components_verified",
                audit.coordinate_components_verified,
            ),
            (
                "signed_endpoint_generator_coordinate_failures",
                audit.coordinate_component_failures,
            ),
            (
                "signed_endpoint_generator_inverse_pairing_verified",
                audit.inverse_pairing_verified,
            ),
            (
                "signed_endpoint_generator_inverse_pairing_failures",
                audit.inverse_pairing_failures,
            ),
            (
                "signed_endpoint_generator_inverse_cancellation_verified",
                audit.inverse_cancellation_verified,
            ),
            (
                "signed_endpoint_generator_inverse_cancellation_failures",
                audit.inverse_cancellation_failures,
            ),
            (
                "signed_endpoint_generator_positive_ybe_path_verified",
                audit.positive_ybe_path_verified,
            ),
            (
                "signed_endpoint_generator_positive_ybe_path_failures",
                audit.positive_ybe_path_failures,
            ),
            (
                "signed_endpoint_generator_positive_ybe_cocycle_verified",
                audit.positive_ybe_cocycle_verified,
            ),
            (
                "signed_endpoint_generator_positive_ybe_cocycle_failures",
                audit.positive_ybe_cocycle_failures,
            ),
            (
                "signed_endpoint_generator_positive_ybe_label_diagnostics",
                audit.positive_ybe_label_diagnostic_failures,
            ),
            (
                "signed_endpoint_generator_far_commutativity_verified",
                audit.far_commutativity_verified,
            ),
            (
                "signed_endpoint_generator_far_commutativity_failures",
                audit.far_commutativity_failures,
            ),
            (
                "signed_endpoint_generator_far_commutativity_path_failures",
                audit.far_commutativity_path_failures,
            ),
            (
                "signed_endpoint_generator_far_commutativity_label_diagnostics",
                audit.far_commutativity_label_diagnostic_failures,
            ),
            (
                "signed_endpoint_generator_explicit_monodromy_representation_verified",
                audit.explicit_monodromy_representation_verified,
            ),
            (
                "signed_endpoint_generator_explicit_monodromy_representation_failures",
                (
                    audit.monodromy_representation_audit.context_map_failures
                    + audit.monodromy_representation_audit.relation_failures
                    if audit.monodromy_representation_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_positive_monodromy_permutation_failures",
                audit.positive_monodromy_permutation_failures,
            ),
            (
                "signed_endpoint_generator_positive_monodromy_representation_verified",
                audit.positive_monodromy_representation_verified,
            ),
            (
                "signed_endpoint_generator_two_strand_witness_domain_exact",
                audit.two_strand_witness_domain_exact,
            ),
            (
                "signed_endpoint_generator_two_strand_witness_domain_failures",
                audit.two_strand_witness_domain_failures,
            ),
            (
                "signed_endpoint_generator_two_strand_base_verified",
                audit.signed_two_strand_base_verified,
            ),
            (
                "signed_endpoint_generator_two_strand_base_failures",
                audit.two_strand_base_failures,
            ),
            (
                "signed_endpoint_generator_artin_update_verified",
                audit.artin_homomorphism_update_verified,
            ),
            (
                "signed_endpoint_generator_artin_update_failures",
                audit.artin_update_failures,
            ),
            (
                "signed_endpoint_generator_telescoping_detector_verified",
                audit.telescoping_detector_proved,
            ),
            (
                "signed_endpoint_generator_telescoping_detector_scope_matches_required",
                audit.telescoping_detector_scope_matches_required,
            ),
            (
                "signed_endpoint_generator_telescoping_endpoint_group_matches",
                audit.telescoping_detector_endpoint_group_matches,
            ),
            (
                "signed_endpoint_generator_telescoping_signed_row_mismatches",
                audit.telescoping_detector_signed_row_mismatches,
            ),
            (
                "signed_endpoint_generator_telescoping_extra_diagnostic_entry_keys",
                audit.telescoping_detector_extra_diagnostic_entry_keys,
            ),
            (
                "signed_endpoint_generator_telescoping_expected_entry_keys",
                (
                    telescoping_audit.expected_entry_keys_exact
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_covered_entry_keys",
                (
                    telescoping_audit.covered_entry_keys_exact
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_expected_positive_entry_keys",
                (
                    telescoping_audit.expected_positive_entry_keys_exact
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_covered_positive_entry_keys",
                (
                    telescoping_audit.covered_positive_entry_keys_exact
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_missing_entry_keys",
                (
                    telescoping_audit.missing_entry_keys
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_extra_entry_keys",
                (
                    telescoping_audit.extra_entry_keys
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_duplicate_entry_keys",
                (
                    telescoping_audit.duplicate_expected_entry_keys
                    + telescoping_audit.duplicate_covered_entry_keys
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_duplicate_positive_entry_keys",
                (
                    telescoping_audit.duplicate_expected_positive_entry_keys
                    + telescoping_audit.duplicate_covered_positive_entry_keys
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_malformed_entry_keys",
                (
                    telescoping_audit.malformed_expected_entry_keys
                    + telescoping_audit.malformed_covered_entry_keys
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_expected_seed_states",
                (
                    telescoping_audit.expected_endpoint_seed_states_exact
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_covered_seed_states",
                (
                    telescoping_audit.covered_endpoint_seed_states_exact
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_duplicate_seed_states",
                (
                    telescoping_audit.duplicate_expected_endpoint_seed_states
                    + telescoping_audit.duplicate_covered_endpoint_seed_states
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_telescoping_malformed_seed_states",
                (
                    telescoping_audit.malformed_expected_endpoint_seed_states
                    + telescoping_audit.malformed_covered_endpoint_seed_states
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_counts_by_family",
                (
                    telescoping_audit.detector_track_counts_by_family
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_count_unknown_families",
                (
                    telescoping_audit.invalid_detector_track_count_families
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_count_malformed_rows",
                (
                    telescoping_audit.malformed_detector_track_count_rows
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_count_malformed_values",
                (
                    telescoping_audit.malformed_detector_track_count_values
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_count_duplicate_families",
                (
                    telescoping_audit.duplicate_detector_track_count_families
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_count_family_scope_exact",
                (
                    telescoping_audit.detector_track_count_family_scope_exact
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_count_matches_family_sum",
                (
                    telescoping_audit.detector_track_count_matches_family_sum
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_fixed_detector_track_count",
                (
                    telescoping_audit.detector_track_count
                    if telescoping_audit is not None
                    else None
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_rows",
                (
                    tuple(
                        (
                            row.endpoint_family,
                            row.track_index,
                            row.assignment_rule,
                            row.dependencies,
                            row.local_assignment_template,
                        )
                        for row in telescoping_audit.detector_track_initialization_rows
                    )
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_missing_keys",
                (
                    telescoping_audit.missing_detector_track_initialization_keys
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_extra_keys",
                (
                    telescoping_audit.extra_detector_track_initialization_keys
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_duplicate_keys",
                (
                    telescoping_audit.duplicate_detector_track_initialization_keys
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_invalid_rows",
                (
                    tuple(row.key for row in telescoping_audit.invalid_detector_track_initialization_rows)
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_unfixed_rows",
                (
                    tuple(
                        row.key
                        for row in (
                            telescoping_audit
                            .detector_track_initialization_rows_not_fixed_before_braid
                        )
                    )
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_template_failures",
                (
                    telescoping_audit.detector_track_initialization_template_failures
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_rows_exact",
                (
                    telescoping_audit.detector_track_initialization_rows_exact
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_detector_tracks_fixed_before_braid",
                (
                    telescoping_audit.detector_track_initializations_fixed_before_braid
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_detector_track_initialization_verified",
                (
                    telescoping_audit.detector_track_initializations_verified
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_artin_detector_recurrence_verified",
                (
                    telescoping_audit.artin_detector_recurrence_proved
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_expected_seed_states",
                (
                    telescoping_audit.expected_word_potential_seed_states_exact
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_covered_seed_states",
                (
                    telescoping_audit.covered_word_potential_seed_states_exact
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_duplicate_seed_states",
                (
                    telescoping_audit.duplicate_expected_word_potential_seed_states
                    + telescoping_audit.duplicate_covered_word_potential_seed_states
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_malformed_seed_states",
                (
                    telescoping_audit.malformed_expected_word_potential_seed_states
                    + telescoping_audit.malformed_covered_word_potential_seed_states
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_seed_state_scope_matches_expected",
                (
                    telescoping_audit.word_potential_seed_state_scope_matches_expected
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_templates_use_only_current_longitudes",
                (
                    telescoping_audit.word_potential_templates_use_only_current_longitudes_verified
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_track_scope_verified",
                (
                    telescoping_audit.word_potential_track_scope_verified
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_track_scope_failures",
                (
                    telescoping_audit.word_potential_track_scope_failures
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_initialized_raw_assignment_variables",
                (
                    telescoping_audit.initialized_raw_assignment_variables_by_family
                    if telescoping_audit is not None
                    else {}
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_raw_assignment_scope_verified",
                (
                    telescoping_audit.word_potential_raw_assignment_scope_verified
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_raw_assignment_scope_failures",
                (
                    telescoping_audit.word_potential_raw_assignment_scope_failures
                    if telescoping_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_artin_substitution_verified",
                (
                    telescoping_audit.word_potential_artin_substitution_proved
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_identity_verified",
                (
                    telescoping_audit.word_potential_identity_proved
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_detector_domains_sound",
                (
                    telescoping_audit.word_potential_certificate.detector_domains_sound
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_detector_domain_failures",
                (
                    telescoping_audit.word_potential_certificate.detector_domain_failures
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_coboundary_defects_constant",
                (
                    telescoping_audit.word_potential_certificate.coboundary_defects_constant
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_malformed_identity_rows",
                (
                    telescoping_audit.word_potential_certificate.malformed_identity_entry_keys
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_certificate_malformed_next_seed_states",
                (
                    telescoping_audit.word_potential_certificate.malformed_identity_next_seed_states
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_certificate_malformed_template_states",
                (
                    telescoping_audit.word_potential_certificate.malformed_template_seed_states
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_certificate_malformed_normalized_states",
                (
                    telescoping_audit.word_potential_certificate.malformed_normalized_seed_states
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_certificate_template_states",
                (
                    telescoping_audit.word_potential_certificate.template_seed_states_exact
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_certificate_identity_rows",
                (
                    telescoping_audit.word_potential_certificate.identity_entry_keys_exact
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_certificate_positive_identity_rows",
                (
                    telescoping_audit.word_potential_certificate.positive_identity_entry_keys_exact
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_artin_substitution_failures",
                (
                    telescoping_audit.word_potential_certificate.substitution_failures
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_identity_failures",
                (
                    telescoping_audit.word_potential_certificate.identity_failures
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_coboundary_defect_failures",
                (
                    telescoping_audit.word_potential_certificate.coboundary_defect_failures
                    if telescoping_audit is not None
                    and telescoping_audit.word_potential_certificate is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_terminal_readout_longitudes_verified",
                (
                    telescoping_audit.terminal_readout_longitudes_proved
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_initial_normalized",
                (
                    telescoping_audit.initial_readout_normalized_proved
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_word_potential_initial_seed_states_normalized",
                audit.word_potential_initial_seed_states_normalized,
            ),
            (
                "signed_endpoint_generator_word_potential_normalized_seed_states",
                audit.normalized_word_potential_seed_states_exact,
            ),
            (
                "signed_endpoint_generator_word_potential_initial_seed_state_scope_exact",
                audit.word_potential_initial_seed_state_scope_exact,
            ),
            (
                "signed_endpoint_generator_word_potential_missing_initial_normalized_seed_states",
                audit.missing_initial_normalized_seed_states,
            ),
            (
                "signed_endpoint_generator_word_potential_extra_initial_normalized_seed_states",
                audit.extra_initial_normalized_seed_states,
            ),
            (
                "signed_endpoint_generator_telescoping_braid_index_independent",
                (
                    telescoping_audit.braid_index_independence_proved
                    if telescoping_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readouts_required",
                audit.cutoff_readouts_required,
            ),
            (
                "signed_endpoint_generator_cutoff_readouts_exact",
                audit.exact_cutoff_readouts_proved,
            ),
            (
                "signed_endpoint_generator_cutoff_readouts_flag_supplied",
                audit.cutoff_readouts_exact,
            ),
            (
                "signed_endpoint_generator_cutoff_readout_scope_matches_required",
                audit.cutoff_readout_scope_matches_required,
            ),
            (
                "signed_endpoint_generator_required_cutoff_families",
                audit.required_cutoff_families,
            ),
            (
                "signed_endpoint_generator_cutoff_target_degrees_match_readout",
                audit.cutoff_target_degrees_match_readout,
            ),
            (
                "signed_endpoint_generator_cutoff_target_degree_mismatches",
                audit.cutoff_target_degree_mismatches,
            ),
            (
                "signed_endpoint_generator_cutoff_readout_expected_states",
                (
                    audit.cutoff_readout_audit.expected_cutoff_seed_states_exact
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_covered_states",
                (
                    audit.cutoff_readout_audit.covered_cutoff_seed_states_exact
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_expected_families",
                (
                    audit.cutoff_readout_audit.expected_cutoff_families
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_covered_families",
                (
                    audit.cutoff_readout_audit.covered_cutoff_families
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_row_families",
                (
                    audit.cutoff_readout_audit.row_cutoff_families
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_missing_families",
                (
                    audit.cutoff_readout_audit.missing_cutoff_families
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_extra_families",
                (
                    audit.cutoff_readout_audit.extra_cutoff_families
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_missing_row_families",
                (
                    audit.cutoff_readout_audit.missing_readout_row_families
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_extra_row_families",
                (
                    audit.cutoff_readout_audit.extra_readout_row_families
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_family_scope_exact",
                (
                    audit.cutoff_readout_audit.cutoff_family_scope_exact
                    if audit.cutoff_readout_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_missing_states",
                (
                    audit.cutoff_readout_audit.missing_cutoff_seed_states
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_extra_states",
                (
                    audit.cutoff_readout_audit.extra_cutoff_seed_states
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_duplicate_states",
                (
                    audit.cutoff_readout_audit.duplicate_expected_cutoff_seed_states
                    + audit.cutoff_readout_audit.duplicate_covered_cutoff_seed_states
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_malformed_states",
                (
                    audit.cutoff_readout_audit.malformed_expected_cutoff_seed_states
                    + audit.cutoff_readout_audit.malformed_covered_cutoff_seed_states
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_degree",
                (
                    audit.cutoff_readout_audit.cutoff_degree
                    if audit.cutoff_readout_audit is not None
                    else None
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_rows",
                (
                    tuple(
                        (
                            row.cutoff_seed_state,
                            row.readout_permutation,
                            row.killed_readout_permutation,
                        )
                        for row in audit.cutoff_readout_audit.readout_rows
                    )
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_malformed_row_states",
                (
                    audit.cutoff_readout_audit.malformed_row_cutoff_seed_states
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_invalid_permutation_rows",
                (
                    audit.cutoff_readout_audit.invalid_readout_permutation_rows
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_duplicate_permutations",
                (
                    audit.cutoff_readout_audit.duplicate_readout_permutations
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_unkilled_rows",
                (
                    audit.cutoff_readout_audit.unkilled_readout_rows
                    if audit.cutoff_readout_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_cutoff_readout_audit_proved",
                (
                    audit.cutoff_readout_audit.proves_exact_cutoff_readouts
                    if audit.cutoff_readout_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_residual_faithfulness_verified",
                audit.residual_faithfulness_proved,
            ),
            (
                "signed_endpoint_generator_residual_faithfulness_flag_supplied",
                audit.residual_faithfulness_verified,
            ),
            (
                "signed_endpoint_generator_residual_action_scope_matches_required",
                audit.residual_action_scope_matches_required,
            ),
            (
                "signed_endpoint_generator_residual_action_scope_matches_seed_states",
                audit.residual_action_scope_matches_seed_states,
            ),
            (
                "signed_endpoint_generator_residual_action_scope_matches_rows",
                audit.residual_action_scope_matches_action_rows,
            ),
            (
                "signed_endpoint_generator_residual_action_scope_expected_states",
                (
                    audit.residual_action_scope.expected_endpoint_seed_states_exact
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_covered_states",
                (
                    audit.residual_action_scope.covered_endpoint_seed_states_exact
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_malformed_row_counts",
                (
                    audit.residual_action_scope.malformed_residual_row_counts
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_duplicate_seed_states",
                (
                    audit.residual_action_scope.duplicate_expected_endpoint_seed_states
                    + audit.residual_action_scope.duplicate_covered_endpoint_seed_states
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_malformed_seed_states",
                (
                    audit.residual_action_scope.malformed_expected_endpoint_seed_states
                    + audit.residual_action_scope.malformed_covered_endpoint_seed_states
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_unknown_families",
                (
                    audit.residual_action_scope.invalid_active_endpoint_families
                    + audit.residual_action_scope.invalid_covered_endpoint_families
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_family_rows",
                (
                    audit.residual_action_scope.expected_residual_rows_by_family
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_family_rows_covered",
                (
                    audit.residual_action_scope.covered_residual_rows_by_family
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_duplicate_family_rows",
                (
                    audit.residual_action_scope.duplicate_expected_residual_row_families
                    + audit.residual_action_scope.duplicate_covered_residual_row_families
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_malformed_family_rows",
                (
                    audit.residual_action_scope.malformed_residual_family_row_counts
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_malformed_family_row_count_rows",
                (
                    audit.residual_action_scope.malformed_residual_family_row_count_rows
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_family_rows_cover_active",
                (
                    audit.residual_action_scope.residual_family_row_counts_cover_active_families
                    if audit.residual_action_scope is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_dependencies",
                (
                    audit.residual_action_scope.scope_dependencies
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_invalid_dependencies",
                (
                    audit.residual_action_scope.duplicate_scope_dependencies
                    + audit.residual_action_scope.forbidden_scope_dependencies
                    + audit.residual_action_scope.unknown_scope_dependencies
                    if audit.residual_action_scope is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_scope_proved",
                (
                    audit.residual_action_scope.proves_residual_action_scope
                    if audit.residual_action_scope is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_proved",
                audit.residual_theorem_faithfulness_proved,
            ),
            (
                "signed_endpoint_generator_residual_theorem_scope_matches_required",
                audit.residual_theorem_scope_matches_required,
            ),
            (
                "signed_endpoint_generator_residual_theorem_scope_matches_seed_states",
                audit.residual_theorem_scope_matches_seed_states,
            ),
            (
                "signed_endpoint_generator_residual_theorem_expected_states",
                (
                    audit.residual_faithfulness_theorem.expected_endpoint_seed_states_exact
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_covered_states",
                (
                    audit.residual_faithfulness_theorem.covered_endpoint_seed_states_exact
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_malformed_row_counts",
                (
                    audit.residual_faithfulness_theorem.malformed_residual_row_counts
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_duplicate_seed_states",
                (
                    audit.residual_faithfulness_theorem.duplicate_expected_endpoint_seed_states
                    + audit.residual_faithfulness_theorem.duplicate_covered_endpoint_seed_states
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_malformed_seed_states",
                (
                    audit.residual_faithfulness_theorem.malformed_expected_endpoint_seed_states
                    + audit.residual_faithfulness_theorem.malformed_covered_endpoint_seed_states
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_unknown_families",
                (
                    audit.residual_faithfulness_theorem.invalid_active_endpoint_families
                    + audit.residual_faithfulness_theorem.invalid_covered_endpoint_families
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_family_rows",
                (
                    audit.residual_faithfulness_theorem.expected_residual_rows_by_family
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_family_rows_covered",
                (
                    audit.residual_faithfulness_theorem.covered_residual_rows_by_family
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_duplicate_family_rows",
                (
                    audit.residual_faithfulness_theorem.duplicate_expected_residual_row_families
                    + audit.residual_faithfulness_theorem.duplicate_covered_residual_row_families
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_malformed_family_rows",
                (
                    audit.residual_faithfulness_theorem.malformed_residual_family_row_counts
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_malformed_family_row_count_rows",
                (
                    audit.residual_faithfulness_theorem.malformed_residual_family_row_count_rows
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_actual_family_rows",
                (
                    audit.residual_faithfulness_theorem.actual_residual_rows_by_family
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_family_rows_match_actual",
                (
                    audit.residual_faithfulness_theorem.residual_family_row_counts_match_rows
                    if audit.residual_faithfulness_theorem is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_expected_input_tuples",
                (
                    audit.residual_faithfulness_theorem.expected_residual_input_tuples
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_covered_input_tuples",
                (
                    audit.residual_faithfulness_theorem.covered_residual_input_tuples
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_missing_input_tuples",
                (
                    audit.residual_faithfulness_theorem.missing_residual_input_tuples
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_extra_input_tuples",
                (
                    audit.residual_faithfulness_theorem.extra_residual_input_tuples
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_duplicate_input_tuples",
                (
                    audit.residual_faithfulness_theorem.duplicate_expected_residual_input_tuples
                    + audit.residual_faithfulness_theorem.duplicate_covered_residual_input_tuples
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_input_tuple_domain_exact",
                (
                    audit.residual_faithfulness_theorem.residual_input_tuple_domain_exact
                    if audit.residual_faithfulness_theorem is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_rows",
                (
                    tuple(
                        (
                            row.input_tuple,
                            row.output_tuple,
                            row.identity_endpoint_output_tuple,
                            row.endpoint_families,
                            row.endpoint_seed_states,
                            row.endpoint_channel_keys,
                            row.dependencies,
                        )
                        for row in audit.residual_faithfulness_theorem.residual_rows
                    )
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_invalid_rows",
                (
                    tuple(row.input_tuple for row in audit.residual_faithfulness_theorem.invalid_residual_rows)
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_malformed_channel_keys",
                (
                    audit.residual_faithfulness_theorem.malformed_residual_row_endpoint_channel_keys
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_channel_key_seed_mismatches",
                (
                    audit.residual_faithfulness_theorem.residual_row_endpoint_channel_seed_mismatches
                    if audit.residual_faithfulness_theorem is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_rows_cover_input_domain",
                (
                    audit.residual_faithfulness_theorem.residual_rows_cover_input_domain
                    if audit.residual_faithfulness_theorem is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_rows_cover_families",
                (
                    audit.residual_faithfulness_theorem.residual_rows_cover_endpoint_families
                    if audit.residual_faithfulness_theorem is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_residual_theorem_rows_cover_seed_states",
                (
                    audit.residual_faithfulness_theorem.residual_rows_cover_endpoint_seed_states
                    if audit.residual_faithfulness_theorem is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_rows",
                (
                    audit.residual_action_audit.row_count
                    if audit.residual_action_audit is not None
                    else 0
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_rows_expected",
                (
                    audit.residual_action_audit.expected_row_count
                    if audit.residual_action_audit is not None
                    else None
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_expected_input_tuples",
                (
                    audit.residual_action_audit.expected_input_tuples
                    if audit.residual_action_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_supplied_input_tuples",
                (
                    audit.residual_action_audit.supplied_input_tuples
                    if audit.residual_action_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_missing_input_tuples",
                (
                    audit.residual_action_audit.missing_input_tuples
                    if audit.residual_action_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_extra_input_tuples",
                (
                    audit.residual_action_audit.extra_input_tuples
                    if audit.residual_action_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_duplicate_input_tuples",
                (
                    audit.residual_action_audit.duplicate_expected_input_tuples
                    + audit.residual_action_audit.duplicate_supplied_input_tuples
                    if audit.residual_action_audit is not None
                    else ()
                ),
            ),
            (
                "signed_endpoint_generator_residual_action_input_tuple_domain_exact",
                audit.residual_action_input_tuple_domain_exact,
            ),
            (
                "signed_endpoint_generator_residual_action_complete",
                (
                    audit.residual_action_audit.proves_complete_residual_action_implication
                    if audit.residual_action_audit is not None
                    else False
                ),
            ),
            (
                "signed_endpoint_generator_tables_proved",
                self.signed_endpoint_generator_closes_current_kappa,
            ),
            (
                "signed_endpoint_generator_failure_reasons",
                failure_reasons,
            ),
        )

    @property
    def routed_endpoint_obstruction_data(self) -> Tuple[Tuple[str, object], ...]:
        data = []
        if self.system_u_active:
            observer = self.refinement.triangular_recovery_unit_observer
            data.extend(
                (
                    ("unit_group_order", observer.unit_group_order),
                    ("recovery_row_count", observer.row_count),
                    ("left_latin_row_pairs", self.refinement.left_latin_row_pairs),
                    ("right_latin_row_pairs", self.refinement.right_latin_row_pairs),
                )
            )
        data.extend(
            (
                (
                    "live_k_missing_latin_row_defects",
                    self.live_k_missing_latin_row_defects,
                ),
                (
                    "recovery_routed_k_missing_latin_row_defects",
                    self.recovery_routed_k_missing_latin_row_defects,
                ),
                (
                    "system_u_endpoint_defects",
                    self.system_u_endpoint_defects,
                ),
                (
                    "continuation_routed_k_missing_latin_row_defects",
                    self.continuation_routed_k_missing_latin_row_defects,
                ),
                (
                    "mixed_context_routed_k_missing_latin_row_defects",
                    self.mixed_context_routed_k_missing_latin_row_defects,
                ),
                (
                    "universal_k_row_normal_form_domain",
                    self.universal_k_row_normal_form_domain,
                ),
                (
                    "universal_k_seed_classifier_entries",
                    self.universal_k_seed_classifier_entries,
                ),
                (
                    "active_routed_endpoint_systems",
                    self.active_routed_endpoint_systems,
                ),
                (
                    "unclosed_routed_endpoint_systems",
                    self.unclosed_routed_endpoint_systems,
                ),
            )
        )
        data.extend(self._universal_continuation_identity_routing_data)
        data.extend(self._triangular_recovery_endpoint_witness_data)
        data.extend(self._triangular_recovery_symmetric_endpoint_fork_data)
        data.extend(self._universal_continuation_endpoint_witness_data)
        data.extend(self._universal_continuation_symmetric_endpoint_fork_data)
        data.extend(self._coordinate_unit_routing_data)
        data.extend(self._mixed_unit_endpoint_witness_data)
        data.extend(self._mixed_unit_symmetric_endpoint_fork_data)
        data.extend(self._universal_k_signed_endpoint_generator_data)
        return tuple(data)

    @property
    def finite_obstruction_data(self) -> Tuple[Tuple[str, object], ...]:
        if self.unsupported_companion_structural_obligation_active:
            data = [
                (
                    "unsupported_companion_block_image_rows",
                    self.unsupported_companion_block_image_rows,
                ),
                (
                    "unsupported_companion_structural_contradiction_proved",
                    self.unsupported_companion_structural_contradiction_proved,
                ),
            ]
            audit = self.unsupported_companion_structural_contradiction
            if audit is not None:
                data.extend(
                    (
                        (
                            "unsupported_companion_expected_rows",
                            audit.expected_rows_exact,
                        ),
                        (
                            "unsupported_companion_covered_rows",
                            audit.covered_rows_exact,
                        ),
                        (
                            "unsupported_companion_contradiction_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.witness_kind,
                                    row.ybe_triple,
                                    row.coordinate,
                                    row.left_value,
                                    row.right_value,
                                    row.closed_branch,
                                )
                                for row in audit.contradiction_rows
                            ),
                        ),
                        (
                            "unsupported_companion_contradiction_failures",
                            audit.failure_reasons,
                        ),
                    )
                )
            return tuple(data)
        if (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and not self.k_deficits_routed_to_recovery_endpoint
            and not self.k_deficits_routed_to_continuation_endpoint
            and not self.k_deficits_routed_to_mixed_context_endpoint
        ):
            data = [
                ("deficits", self.refinement.rack_kink_completion_deficits),
                (
                    "live_kink_completion_deficits",
                    self.refinement.live_kink_completion_deficits,
                ),
                (
                    "nonlive_kink_completion_deficits",
                    self.refinement.nonlive_kink_completion_deficits,
                ),
                ("left_triangular_row_pairs", self.refinement.left_triangular_row_pairs),
                ("right_triangular_row_pairs", self.refinement.right_triangular_row_pairs),
                ("missing_left_latin_row_pairs", self.refinement.missing_left_latin_row_pairs),
                ("missing_right_latin_row_pairs", self.refinement.missing_right_latin_row_pairs),
                (
                    "missing_left_latin_row_defects",
                    self.refinement.missing_left_latin_row_defects,
                ),
                (
                    "missing_right_latin_row_defects",
                    self.refinement.missing_right_latin_row_defects,
                ),
                (
                    "active_missing_left_latin_row_defects",
                    self.refinement.active_missing_left_latin_row_defects,
                ),
                (
                    "active_missing_right_latin_row_defects",
                    self.refinement.active_missing_right_latin_row_defects,
                ),
                (
                    "live_k_missing_latin_row_defects",
                    self.live_k_missing_latin_row_defects,
                ),
                (
                    "recovery_routed_k_missing_latin_row_defects",
                    self.recovery_routed_k_missing_latin_row_defects,
                ),
                (
                    "system_u_endpoint_defects",
                    self.system_u_endpoint_defects,
                ),
                (
                    "continuation_routed_k_missing_latin_row_defects",
                    self.continuation_routed_k_missing_latin_row_defects,
                ),
                (
                    "mixed_context_routed_k_missing_latin_row_defects",
                    self.mixed_context_routed_k_missing_latin_row_defects,
                ),
                (
                    "universal_k_row_normal_form_domain",
                    self.universal_k_row_normal_form_domain,
                ),
                (
                    "universal_k_seed_classifier_entries",
                    self.universal_k_seed_classifier_entries,
                ),
                (
                    "active_routed_endpoint_systems",
                    self.active_routed_endpoint_systems,
                ),
                (
                    "unclosed_routed_endpoint_systems",
                    self.unclosed_routed_endpoint_systems,
                ),
                (
                    "active_companion_block_image_support_rows",
                    self.refinement.active_companion_block_image_support_rows,
                ),
                (
                    "active_companion_block_images_have_constant_kernel_support",
                    self.refinement.active_companion_block_images_have_constant_kernel_support,
                ),
                (
                    "k_left_side_dual_replacement_rows",
                    self.k_left_side_dual_replacement_rows,
                ),
                (
                    "triangular_constant_map_non_surjective_rows",
                    tuple(
                        (row.side, row.left_color, row.right_color)
                        for row in self.refinement.triangular_column.constant_map_non_surjective_rows
                    ),
                ),
                (
                    "triangular_companion_kernel_rows",
                    tuple(
                        (row.side, row.left_color, row.right_color)
                        for row in self.refinement.triangular_column.companion_kernel_rows
                    ),
                ),
                (
                    "triangular_companion_nonbijective_without_constant_kernel_rows",
                    tuple(
                        (row.side, row.left_color, row.right_color)
                        for row in self.refinement.triangular_column.companion_nonbijective_without_constant_kernel_rows
                    ),
                ),
                (
                    "triangular_hidden_nonunit_opposite_without_product_rows",
                    tuple(
                        (row.side, row.left_color, row.right_color)
                        for row in self.refinement.triangular_column.hidden_nonunit_opposite_without_product_rows
                    ),
                ),
                (
                    "side_dual_latin_completion_available",
                    self.refinement.side_dual_latin_completion_available,
                ),
                ("latin_ybe_failure_triples", self.refinement.latin_ybe_failure_triples),
                (
                    "side_dual_latin_ybe_failure_triples",
                    self.refinement.side_dual_latin_ybe_failure_triples,
                ),
                (
                    "direct_unit_longitude_status_preempted_by_kink_dichotomy",
                    self.refinement.direct_unit_longitude_status_preempted_by_kink_dichotomy,
                ),
            ]
            data.extend(self._universal_k_signed_endpoint_generator_data)
            if self.triangular_latin_defect_closure is not None:
                closure = self.triangular_latin_defect_closure
                data.extend(
                    (
                        (
                            "triangular_latin_defect_closure_rows",
                            tuple(
                                (
                                    row.side,
                                    row.defect,
                                    row.left_color,
                                    row.right_color,
                                    row.domain_color,
                                    row.fixed_input,
                                    row.collapsed_inputs,
                                    row.closure_kind,
                                )
                                for row in closure.rows
                            ),
                        ),
                        (
                            "triangular_latin_defect_proper_closure_rows",
                            tuple(
                                (
                                    row.side,
                                    row.defect,
                                    row.left_color,
                                    row.right_color,
                                    row.domain_color,
                                    row.fixed_input,
                                    row.collapsed_inputs,
                                    row.closure_kind,
                                )
                                for row in closure.proper_closure_rows
                            ),
                        ),
                        (
                            "triangular_latin_defect_universal_closure_rows",
                            tuple(
                                (
                                    row.side,
                                    row.defect,
                                    row.left_color,
                                    row.right_color,
                                    row.domain_color,
                                    row.fixed_input,
                                    row.collapsed_inputs,
                                    row.closure_kind,
                                )
                                for row in closure.universal_closure_rows
                            ),
                        ),
                    )
                )
            if self.triangular_constant_kernel_recovery_route is not None:
                route = self.triangular_constant_kernel_recovery_route
                data.extend(
                    (
                        (
                            "triangular_constant_kernel_recovery_route_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.domain_color,
                                    row.collapsed_inputs,
                                    row.closure_kind,
                                    row.recovery_separates_kernel_edge,
                                )
                                for row in route.rows
                            ),
                        ),
                        (
                            "triangular_constant_kernel_unrouted_universal_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.domain_color,
                                    row.collapsed_inputs,
                                    row.closure_kind,
                                )
                                for row in route.unrouted_universal_rows
                            ),
                        ),
                    )
                )
            if self.missing_triangular_row_profile is not None:
                profile = self.missing_triangular_row_profile
                missing_left_pairs = set(self.refinement.missing_left_latin_row_pairs)
                missing_right_pairs = set(self.refinement.missing_right_latin_row_pairs)
                relevant_rows = tuple(
                    row
                    for row in profile.rows
                    if (
                        row.side == "left"
                        and (row.left_color, row.right_color) in missing_left_pairs
                    )
                    or (
                        row.side == "right"
                        and (row.left_color, row.right_color) in missing_right_pairs
                    )
                )
                data.extend(
                    (
                        (
                            "missing_triangular_row_profiles",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.explanation,
                                    row.constant_section_inputs,
                                    row.nonconstant_section_inputs,
                                )
                                for row in relevant_rows
                            ),
                        ),
                        (
                            "missing_triangular_partial_constant_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.unit_section_inputs,
                                    row.constant_section_inputs,
                                )
                                for row in relevant_rows
                                if row.partial_constant_hidden_rank_loss
                            ),
                        ),
                        (
                            "missing_triangular_partial_constant_mixed_unit_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.unit_section_inputs,
                                    row.constant_section_inputs,
                                )
                                for row in relevant_rows
                                if row.partial_constant_mixed_unit_context
                            ),
                        ),
                        (
                            "missing_triangular_nonconstant_hidden_rows",
                            tuple(
                                (row.side, row.left_color, row.right_color)
                                for row in relevant_rows
                                if row.explanation == "nonconstant_hidden_rank_loss"
                            ),
                        ),
                    )
                )
            if self.missing_triangular_left_rack_cardinality is not None:
                cardinality = self.missing_triangular_left_rack_cardinality
                data.extend(
                    (
                        (
                            "missing_triangular_left_rack_section_cardinality_failures",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.fixed_input,
                                    row.domain_size,
                                    row.codomain_size,
                                )
                                for row in cardinality.unequal_section_rows
                            ),
                        ),
                        (
                            "missing_triangular_injective_non_surjective_rows",
                            tuple(
                                (row.side, row.left_color, row.right_color)
                                for row in cardinality.injective_non_surjective_rows
                            ),
                        ),
                        (
                            "missing_triangular_profile_unclassified_rows",
                            tuple(
                                (row.side, row.left_color, row.right_color)
                                for row in cardinality.unclassified_rows
                            ),
                        ),
                        (
                            "missing_triangular_left_rack_cardinality_proved",
                            cardinality.proves_left_rack_missing_triangular_cardinality_closure,
                        ),
                    )
                )
            if self.missing_triangular_coordinate_unit_routing is not None:
                routing = self.missing_triangular_coordinate_unit_routing
                missing_left_pairs = set(self.refinement.missing_left_latin_row_pairs)
                missing_right_pairs = set(self.refinement.missing_right_latin_row_pairs)
                relevant_route_rows = tuple(
                    row
                    for row in routing.rows
                    if (
                        "left" in row.coordinate_unit_sides
                        and (row.left_color, row.right_color) in missing_left_pairs
                    )
                    or (
                        "right" in row.coordinate_unit_sides
                        and (row.left_color, row.right_color) in missing_right_pairs
                    )
                )
                data.extend(
                    (
                        (
                            "missing_triangular_coordinate_unit_routes",
                            tuple(
                                (
                                    row.left_color,
                                    row.right_color,
                                    row.coordinate_unit_sides,
                                    row.left_explanation,
                                    row.right_explanation,
                                    row.status,
                                )
                                for row in relevant_route_rows
                            ),
                        ),
                        (
                            "missing_triangular_coordinate_unit_mixed_rows",
                            tuple(
                                (
                                    row.left_color,
                                    row.right_color,
                                    row.coordinate_unit_sides,
                                    row.left_explanation,
                                    row.right_explanation,
                                )
                                for row in relevant_route_rows
                                if row.status == "mixed_unit_context"
                            ),
                        ),
                        (
                            "missing_triangular_coordinate_unit_unrouted_rows",
                            tuple(
                                (
                                    row.left_color,
                                    row.right_color,
                                    row.coordinate_unit_sides,
                                    row.left_explanation,
                                    row.right_explanation,
                                )
                                for row in relevant_route_rows
                                if row.status == "unrouted_coordinate_unit_row"
                            ),
                        ),
                        (
                            "missing_triangular_coordinate_unit_unclosed_two_sided_rows",
                            tuple(
                                (
                                    row.left_color,
                                    row.right_color,
                                    row.coordinate_unit_sides,
                                    row.left_explanation,
                                    row.right_explanation,
                                )
                                for row in routing.unclosed_two_sided_unit_pair_rows
                            ),
                        ),
                        (
                            "missing_triangular_locally_nondegenerate_closed_branch",
                            routing.locally_nondegenerate_closed_branch,
                        ),
                    )
                )
            if self.missing_triangular_partial_constant_closure is not None:
                closure = self.missing_triangular_partial_constant_closure
                missing_left_pairs = set(self.refinement.missing_left_latin_row_pairs)
                missing_right_pairs = set(self.refinement.missing_right_latin_row_pairs)
                relevant_closure_rows = tuple(
                    row
                    for row in closure.rows
                    if (
                        row.side == "left"
                        and (row.left_color, row.right_color) in missing_left_pairs
                    )
                    or (
                        row.side == "right"
                        and (row.left_color, row.right_color) in missing_right_pairs
                    )
                )
                data.extend(
                    (
                        (
                            "missing_triangular_partial_constant_closure_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.fixed_input,
                                    row.domain_color,
                                    row.collapsed_inputs,
                                    row.closure_kind,
                                )
                                for row in relevant_closure_rows
                            ),
                        ),
                        (
                            "missing_triangular_partial_constant_proper_closure_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.fixed_input,
                                    row.domain_color,
                                    row.collapsed_inputs,
                                    row.closure_kind,
                                )
                                for row in relevant_closure_rows
                                if row.closure_is_proper
                            ),
                        ),
                        (
                            "missing_triangular_partial_constant_universal_closure_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.fixed_input,
                                    row.domain_color,
                                    row.collapsed_inputs,
                                    row.closure_kind,
                                )
                                for row in relevant_closure_rows
                                if row.closure_is_universal
                            ),
                        ),
                    )
                )
            if self.missing_triangular_partial_constant_continuation_route is not None:
                route = self.missing_triangular_partial_constant_continuation_route
                missing_left_pairs = set(self.refinement.missing_left_latin_row_pairs)
                missing_right_pairs = set(self.refinement.missing_right_latin_row_pairs)
                relevant_route_rows = tuple(
                    row
                    for row in route.rows
                    if (
                        row.side == "left"
                        and (row.left_color, row.right_color) in missing_left_pairs
                    )
                    or (
                        row.side == "right"
                        and (row.left_color, row.right_color) in missing_right_pairs
                    )
                )
                data.extend(
                    (
                        (
                            "missing_triangular_partial_constant_continuation_routes",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.fixed_input,
                                    row.domain_color,
                                    row.collapsed_inputs,
                                    row.companion_output_color,
                                    row.companion_outputs,
                                    row.continuation_seed_closure_kinds,
                                    row.status,
                                )
                                for row in relevant_route_rows
                            ),
                        ),
                        (
                            "missing_triangular_partial_constant_unrouted_continuation_rows",
                            tuple(
                                (
                                    row.side,
                                    row.left_color,
                                    row.right_color,
                                    row.fixed_input,
                                    row.domain_color,
                                    row.collapsed_inputs,
                                    row.status,
                                )
                                for row in relevant_route_rows
                                if not row.routes_to_universal_continuation_seed
                            ),
                        ),
                    )
                )
            if self.universal_continuation_identity_routing is not None:
                routing = self.universal_continuation_identity_routing
                data.extend(
                    (
                        (
                            "universal_continuation_identity_lost_edges",
                            routing.routing.lost_edges,
                        ),
                        (
                            "universal_continuation_identity_unrouted_edges",
                            routing.routing.unrouted_edges,
                        ),
                        (
                            "universal_continuation_identity_routing_proved",
                            routing.proves_identity_routed_universal_continuation,
                        ),
                    )
                )
            if self.triangular_recovery_endpoint_witness is not None:
                witness = self.triangular_recovery_endpoint_witness
                data.extend(
                    (
                        (
                            "triangular_recovery_endpoint_witness_matches_system",
                            witness.observer
                            == self.refinement.triangular_recovery_unit_observer
                            and witness.routed_keys
                            == _sorted_triangular_recovery_endpoint_keys(
                                tuple(
                                    _triangular_recovery_endpoint_key(defect)
                                    for defect in self.system_u_endpoint_defects
                                )
                            ),
                        ),
                        (
                            "triangular_recovery_endpoint_witness_proved",
                            witness.proves_triangular_recovery_endpoint_witnesses,
                        ),
                        (
                            "triangular_recovery_endpoint_missing_keys",
                            witness.missing_routed_keys,
                        ),
                        (
                            "triangular_recovery_endpoint_extra_keys",
                            witness.extra_witness_keys,
                        ),
                    )
                )
            if self.universal_continuation_endpoint_witness is not None:
                witness = self.universal_continuation_endpoint_witness
                data.extend(
                    (
                        (
                            "universal_continuation_endpoint_witness_matches_routing",
                            self.universal_continuation_identity_routing is not None
                            and witness.identity_routing
                            == self.universal_continuation_identity_routing,
                        ),
                        (
                            "universal_continuation_endpoint_witness_proved",
                            witness.proves_universal_continuation_identity_endpoint_witnesses,
                        ),
                        (
                            "universal_continuation_endpoint_missing_edges",
                            witness.missing_identity_routed_edges,
                        ),
                        (
                            "universal_continuation_endpoint_extra_edges",
                            witness.extra_witness_edges,
                        ),
                    )
                )
            if self.missing_triangular_coordinate_unit_routing is not None:
                routing = self.missing_triangular_coordinate_unit_routing
                data.extend(
                    (
                        (
                            "missing_triangular_coordinate_unit_mixed_rows",
                            tuple(
                                (
                                    row.left_color,
                                    row.right_color,
                                    row.coordinate_unit_sides,
                                    row.left_explanation,
                                    row.right_explanation,
                                )
                                for row in routing.mixed_unit_context_rows
                            ),
                        ),
                        (
                            "missing_triangular_coordinate_unit_unrouted_rows",
                            tuple(
                                (
                                    row.left_color,
                                    row.right_color,
                                    row.coordinate_unit_sides,
                                    row.left_explanation,
                                    row.right_explanation,
                                )
                                for row in routing.unrouted_rows
                            ),
                        ),
                        (
                            "missing_triangular_coordinate_unit_unclosed_two_sided_rows",
                            tuple(
                                (
                                    row.left_color,
                                    row.right_color,
                                    row.coordinate_unit_sides,
                                    row.left_explanation,
                                    row.right_explanation,
                                )
                                for row in routing.unclosed_two_sided_unit_pair_rows
                            ),
                        ),
                        (
                            "missing_triangular_coordinate_unit_routing_proved",
                            routing.proves_coordinate_unit_routing_ledger,
                        ),
                    )
                )
            if self.mixed_unit_context_endpoint_witness is not None:
                witness = self.mixed_unit_context_endpoint_witness
                data.extend(
                    (
                        (
                            "mixed_unit_endpoint_witness_matches_routing",
                            self.missing_triangular_coordinate_unit_routing is not None
                            and witness.coordinate_routing
                            == self.missing_triangular_coordinate_unit_routing,
                        ),
                        (
                            "mixed_unit_endpoint_witness_proved",
                            witness.proves_mixed_unit_context_endpoint_witnesses,
                        ),
                        (
                            "mixed_unit_endpoint_missing_context_keys",
                            witness.missing_mixed_context_keys,
                        ),
                        (
                            "mixed_unit_endpoint_extra_context_keys",
                            witness.extra_witness_keys,
                        ),
                    )
                )
            return tuple(data)
        if self.system_u_active or self.system_c_active or self.system_m_active:
            return self.routed_endpoint_obstruction_data
        return (("status", self.refinement.status),)

    @property
    def remaining_obligations(self) -> Tuple[str, ...]:
        if self.unsupported_companion_structural_obligation_active:
            return (
                "prove unsupported companion block-image rows contradict the coloured YBE equations or an already closed branch",
                "or upgrade one unsupported companion row to a normalized-law counterexample",
            )
        if self.system_k_closed_by_proper_generated_closure:
            return ()
        if self.k_deficits_closed_by_recorded_routing:
            return ()
        if self.all_active_routed_endpoint_systems_closed:
            return ()
        endpoint_obligations = []
        if (
            self.system_u_active
            and not self.system_u_closed_by_routed_certificate
            and (
                self.refinement.status == "triangular_recovery_unit_longitude_obstruction"
                or (
                    self.raw_system_k
                    and (
                        self.kink_completion_deficits_routed
                        or self.k_deficits_routed_to_recovery_endpoint
                    )
                )
            )
        ):
            endpoint_obligations.extend(
                (
                    "prove each routed triangular recovery endpoint composite lies in V_beta(U_tri)",
                    "or upgrade one routed U_tri endpoint miss to a normalized-law sequence",
                )
            )
        if self.system_c_active and not self.system_c_closed_by_routed_certificate:
            endpoint_obligations.extend(
                (
                    "construct fixed endpoint witnesses for the routed universal-continuation seed closures",
                    "or upgrade one routed universal-continuation endpoint miss to a normalized-law sequence",
                )
            )
        if self.system_m_active and not self.system_m_closed_by_routed_certificate:
            endpoint_obligations.extend(
                (
                    "prove each routed mixed-unit context endpoint factors through fixed detector/readout data",
                    "or upgrade one routed mixed-unit endpoint miss to a normalized-law sequence",
                )
            )
        if endpoint_obligations:
            return tuple(endpoint_obligations)
        return self.refinement.remaining_obligations


def triangular_recovery_unit_observer_from_audit(
    recovery: TriangularRecoveryAudit,
) -> TriangularRecoveryUnitObserverAudit:
    """Turn triangular recovery rows into one fixed finite permutation observer."""

    raw_states = []
    row_partials = []
    for row in recovery.row_audits:
        partial = []
        for entry in row.entries:
            output_state = (
                row.output_left_color,
                row.output_right_color,
                entry.output_left,
                entry.output_right,
            )
            source_state = (
                row.left_color,
                row.right_color,
                entry.recovered_left_input,
                entry.recovered_right_input,
            )
            raw_states.extend((output_state, source_state))
            partial.append((output_state, source_state))
        row_partials.append(tuple(partial))

    universe = tuple(sorted(set(raw_states), key=repr))
    generators = []
    for index, (row, partial) in enumerate(zip(recovery.row_audits, row_partials)):
        transformation = _extend_partial_bijection_to_transformation(universe, partial)
        generators.append(
            TriangularRecoveryUnitGeneratorAudit(
                row_index=index,
                side=row.side,
                left_color=row.left_color,
                right_color=row.right_color,
                output_left_color=row.output_left_color,
                output_right_color=row.output_right_color,
                source_states=tuple(target for _source, target in partial),
                output_states=tuple(source for source, _target in partial),
                transformation=transformation,
            )
        )

    generator_transformations = tuple(row.transformation for row in generators)
    if generator_transformations:
        monoid = TransformationMonoid.generated(generator_transformations)
    else:
        identity = identity_transformation(len(universe))
        monoid = TransformationMonoid((identity,), identity)
    unit_group = monoid_permutation_group(monoid)
    return TriangularRecoveryUnitObserverAudit(
        recovery=recovery,
        universe=universe,
        generator_rows=tuple(generators),
        monoid=monoid,
        unit_group_order=len(unit_group.elements),
    )


def triangular_recovery_unit_observer_audit(
    interval: LocalInterval,
) -> TriangularRecoveryUnitObserverAudit:
    """Return the fixed unit observer generated by triangular recovery rows."""

    return triangular_recovery_unit_observer_from_audit(
        triangular_recovery_audit(interval),
    )


def triangular_recovery_unit_group(interval: LocalInterval) -> FiniteGroup:
    """Return the unit group generated by triangular recovery permutations."""

    return monoid_permutation_group(triangular_recovery_unit_observer_audit(interval).monoid)


def triangular_recovery_longitude_route_audit(
    interval: LocalInterval,
    n: int,
    braid_word: BraidWord,
    factor_row_indices: Tuple[int, ...],
    *,
    max_assignments: int = 100_000,
) -> TriangularRecoveryLongitudeRouteAudit:
    """Check one supplied triangular recovery endpoint against ``V_beta``."""

    observer = triangular_recovery_unit_observer_audit(interval)
    generators = observer.generator_transformations
    factors = tuple(generators[index] for index in factor_row_indices)
    unit_route = unit_composite_longitude_route_audit(
        observer.monoid,
        n,
        braid_word,
        factors,
        max_assignments=max_assignments,
    )
    return TriangularRecoveryLongitudeRouteAudit(
        observer=observer,
        factor_row_indices=tuple(factor_row_indices),
        factors=factors,
        unit_route=unit_route,
    )


def triangular_recovery_longitude_expression_audit(
    interval: LocalInterval,
    n: int,
    braid_word: BraidWord,
    factor_row_indices: Tuple[int, ...],
    assignment: Sequence[Transformation],
    expression: Sequence[LongitudeExpressionLetter],
) -> TriangularRecoveryLongitudeExpressionAudit:
    """Check an explicit ``U_tri`` longitude expression for one endpoint."""

    observer = triangular_recovery_unit_observer_audit(interval)
    generators = observer.generator_transformations
    factors = tuple(generators[index] for index in factor_row_indices)
    unit_expression = unit_composite_longitude_expression_audit(
        observer.monoid,
        n,
        braid_word,
        factors,
        assignment,
        expression,
    )
    return TriangularRecoveryLongitudeExpressionAudit(
        observer=observer,
        factor_row_indices=tuple(factor_row_indices),
        factors=factors,
        unit_expression=unit_expression,
    )


def triangular_recovery_derived_series_lift_audit(
    interval: LocalInterval,
    n: int,
    braid_word: BraidWord,
    factor_row_indices: Tuple[int, ...],
    stage_lifted_witnesses: Sequence[LongitudeSubgroupWitness],
    final_witness: LongitudeSubgroupWitness = (),
) -> TriangularRecoveryDerivedSeriesLiftAudit:
    """Check a supplied derived-series lift inside ``U_tri``."""

    observer = triangular_recovery_unit_observer_audit(interval)
    generators = observer.generator_transformations
    factors = tuple(generators[index] for index in factor_row_indices)
    derived_lift = unit_composite_derived_series_lift_audit(
        observer.monoid,
        n,
        braid_word,
        factors,
        stage_lifted_witnesses,
        final_witness,
    )
    return TriangularRecoveryDerivedSeriesLiftAudit(
        observer=observer,
        factor_row_indices=tuple(factor_row_indices),
        factors=factors,
        derived_lift=derived_lift,
    )


def triangular_recovery_perfect_residual_audit(
    interval: LocalInterval,
    n: int,
    braid_word: BraidWord,
    residual_endpoint: Transformation,
    *,
    max_assignments: int | None = None,
) -> TriangularRecoveryPerfectResidualAudit:
    """Check a terminal triangular recovery endpoint in the stable residual."""

    observer = triangular_recovery_unit_observer_audit(interval)
    perfect_residual = unit_perfect_residual_longitude_audit(
        observer.monoid,
        n,
        braid_word,
        residual_endpoint,
        max_assignments=max_assignments,
    )
    return TriangularRecoveryPerfectResidualAudit(
        observer=observer,
        residual_endpoint=residual_endpoint,
        perfect_residual=perfect_residual,
    )


def triangular_recovery_detector_lift_transition_audit(
    interval: LocalInterval,
    signed_generator: int,
    input_left: ArtinDetectorLiftLabel,
    input_right: ArtinDetectorLiftLabel,
    supplied_left: ArtinDetectorLiftLabel,
    supplied_right: ArtinDetectorLiftLabel,
) -> ArtinDetectorLiftTransitionAudit:
    """Check one supplied triangular-recovery row against Artin lift rules."""

    return artin_detector_lift_transition_audit(
        triangular_recovery_unit_group(interval),
        signed_generator,
        input_left,
        input_right,
        supplied_left,
        supplied_right,
    )


def triangular_recovery_detector_lift_braid_audit(
    interval: LocalInterval,
    initial_meridians: Sequence[GroupElement],
    braid_word: BraidWord,
    endpoint_expression: Sequence[LongitudeExpressionLetter] = (),
) -> ArtinDetectorLiftBraidAudit:
    """Run the Artin detector-lift induction in the triangular recovery group."""

    return artin_detector_lift_braid_audit(
        triangular_recovery_unit_group(interval),
        initial_meridians,
        braid_word,
        endpoint_expression,
    )


@dataclass(frozen=True)
class NonlinearOverlapRefinementAudit:
    """Refine the exact survivor through the mixed-unit triangular reductions."""

    obstruction: NonlinearOverlapObstructionAudit
    unit_collapse: TwoSidedUnitCollapseAudit
    rank_profile: SectionRankProfileCollapseAudit
    triangular_bundle: TriangularBundleAudit
    triangular_recovery: TriangularRecoveryAudit
    triangular_column: TriangularColumnCollapseAudit
    latin_triangular: LatinTriangularYBEAudit
    side_dual_latin_triangular: LatinTriangularYBEAudit
    rack_kink: RackKinkLatinTriangularCollapseAudit
    side_dual_rack_kink: RightRackKinkLatinTriangularCollapseAudit

    @property
    def target_ready(self) -> bool:
        return self.obstruction.exact_remaining_nonlinear_shape

    @property
    def closed_by_repair_contract(self) -> bool:
        return self.obstruction.repair_contract_closes

    @property
    def closed_by_strand_continuing_transport(self) -> bool:
        return self.target_ready and self.unit_collapse.strand_continuing_case

    @property
    def closed_by_locally_nondegenerate_branch(self) -> bool:
        return self.target_ready and self.unit_collapse.locally_nondegenerate_closed_branch

    @property
    def proper_section_kernel_visible(self) -> bool:
        return self.target_ready and bool(self.rank_profile.proper_kernel_rows)

    @property
    def mixed_unit_context_recovery(self) -> bool:
        return self.target_ready and self.unit_collapse.mixed_unit_context_recovery_remaining

    @property
    def nonunit_endpoint_obstruction(self) -> bool:
        return (
            self.target_ready
            and self.unit_collapse.colored_ybe
            and not self.unit_collapse.strand_continuing_case
            and not self.unit_collapse.all_rows_two_sided_unit
            and not self.unit_collapse.mixed_unit_rows
        )

    @property
    def hidden_rank_loss_is_constant(self) -> bool:
        return (
            self.target_ready
            and bool(self.rank_profile.hidden_kernel_rows_after_proper_profiles_removed)
            and self.rank_profile.hidden_kernel_rows_are_constant
        )

    @property
    def triangular_rows_present(self) -> bool:
        return bool(self.triangular_bundle.row_audits)

    @property
    def triangular_bundle_partition_verified(self) -> bool:
        return (
            self.target_ready
            and self.triangular_rows_present
            and self.triangular_bundle.every_bundle_partition_identity_holds
        )

    @property
    def triangular_recovery_verified(self) -> bool:
        return (
            self.triangular_bundle_partition_verified
            and self.triangular_recovery.every_recovery_formula_bijective
        )

    @property
    def all_triangular_rows_close_by_product(self) -> bool:
        return (
            self.triangular_recovery_verified
            and bool(self.triangular_column.row_audits)
            and len(self.triangular_column.product_collapse_rows)
            == len(self.triangular_column.row_audits)
        )

    @property
    def triangular_structural_inconsistency(self) -> bool:
        return (
            self.target_ready
            and (
                bool(self.triangular_column.constant_map_non_surjective_rows)
                or bool(self.triangular_column.companion_kernel_rows)
                or bool(
                    self.triangular_column.companion_nonbijective_without_constant_kernel_rows
                )
                or bool(
                    self.triangular_column.hidden_nonunit_opposite_without_product_rows
                )
            )
        )

    @property
    def rack_base_consistency_inconsistent(self) -> bool:
        return self.target_ready and not self.rack_kink.base_is_finite_rack

    @property
    def latin_triangular_kink_impossible(self) -> bool:
        return self.target_ready and self.rack_kink.all_latin_fibres_forced_singleton

    @property
    def latin_triangular_kink_contradiction(self) -> bool:
        return (
            self.target_ready
            and self.rack_kink.theorem_hypotheses_hold
            and self.rack_kink.kink_cancellation_verified
            and bool(self.rack_kink.non_singleton_latin_colors)
        )

    @property
    def latin_triangular_kink_cancellation_inconsistent(self) -> bool:
        return (
            self.target_ready
            and self.rack_kink.theorem_hypotheses_hold
            and not self.rack_kink.kink_cancellation_verified
        )

    @property
    def side_dual_latin_triangular_kink_impossible(self) -> bool:
        return (
            self.target_ready
            and self.side_dual_rack_kink.all_latin_fibres_forced_singleton
        )

    @property
    def side_dual_latin_triangular_kink_contradiction(self) -> bool:
        return (
            self.target_ready
            and self.side_dual_rack_kink.theorem_hypotheses_hold
            and self.side_dual_rack_kink.diagonal_cancellation_verified
            and bool(self.side_dual_rack_kink.non_singleton_latin_colors)
        )

    @property
    def side_dual_latin_triangular_diagonal_cancellation_inconsistent(self) -> bool:
        return (
            self.target_ready
            and self.side_dual_rack_kink.theorem_hypotheses_hold
            and not self.side_dual_rack_kink.diagonal_cancellation_verified
        )

    @property
    def latin_triangular_ybe_projection_inconsistent(self) -> bool:
        return (
            self.target_ready
            and self.unit_collapse.colored_ybe
            and self.rack_kink.latin_rows_present_for_all_pairs
            and bool(self.latin_ybe_failure_triples)
        )

    @property
    def side_dual_latin_triangular_ybe_projection_inconsistent(self) -> bool:
        return (
            self.target_ready
            and self.unit_collapse.colored_ybe
            and self.side_dual_latin_completion_available
            and bool(self.side_dual_latin_ybe_failure_triples)
        )

    @property
    def expected_latin_color_pairs(self) -> Tuple[Tuple[Color, Color], ...]:
        return tuple(
            sorted(
                {
                    (row.left_color, row.right_color)
                    for row in self.unit_collapse.row_audits
                },
                key=repr,
            )
        )

    @property
    def left_latin_row_pairs(self) -> Tuple[Tuple[Color, Color], ...]:
        return tuple(
            sorted(
                {
                    (row.left_color, row.right_color)
                    for row in self.triangular_column.latin_unit_rows
                    if row.side == "left"
                },
                key=repr,
            )
        )

    @property
    def right_latin_row_pairs(self) -> Tuple[Tuple[Color, Color], ...]:
        return tuple(
            sorted(
                {
                    (row.left_color, row.right_color)
                    for row in self.triangular_column.latin_unit_rows
                    if row.side == "right"
                },
                key=repr,
            )
        )

    @property
    def left_triangular_row_pairs(self) -> Tuple[Tuple[Color, Color], ...]:
        return tuple(
            sorted(
                {
                    (row.left_color, row.right_color)
                    for row in self.triangular_column.row_audits
                    if row.side == "left"
                },
                key=repr,
            )
        )

    @property
    def right_triangular_row_pairs(self) -> Tuple[Tuple[Color, Color], ...]:
        return tuple(
            sorted(
                {
                    (row.left_color, row.right_color)
                    for row in self.triangular_column.row_audits
                    if row.side == "right"
                },
                key=repr,
            )
        )

    def _missing_latin_row_reasons(
        self,
        side: str,
        pair: Tuple[Color, Color],
    ) -> Tuple[str, ...]:
        rows = tuple(
            row
            for row in self.triangular_column.row_audits
            if row.side == side and (row.left_color, row.right_color) == pair
        )
        reasons = []

        def add(reason: str) -> None:
            if reason not in reasons:
                reasons.append(reason)

        if not rows:
            add(f"no_{side}_triangular_row")
        for row in rows:
            if row.product_collapse_for_hidden_nonunit:
                add(f"{side}_row_product_collapse")
            if not row.constant_map_is_bijective:
                add(f"{side}_constant_map_not_bijective")
                if not row.constant_map_surjective:
                    add(f"{side}_constant_map_not_surjective")
                if row.constant_map_has_proper_kernel:
                    add(f"{side}_constant_map_proper_kernel")
                elif row.constant_kernel_kind == "universal":
                    add(f"{side}_constant_map_universal_kernel")
            if not row.companion_sections_bijective:
                add(f"{side}_companion_sections_not_bijective")
                if any(
                    section.has_proper_nontrivial_kernel
                    for section in row.companion_sections
                ):
                    add(f"{side}_companion_sections_proper_kernel")
                if any(
                    section.kernel_kind == "universal"
                    for section in row.companion_sections
                ):
                    add(f"{side}_companion_sections_constant")
                if all(
                    section.is_injective_non_surjective
                    for section in row.companion_sections
                ):
                    add(f"{side}_companion_sections_injective_non_surjective")
            if not row.opposite_sections_all_bijective:
                add(f"{side}_opposite_sections_not_bijective")
            if row.has_proper_opposite_kernel:
                add(f"{side}_opposite_proper_kernel_visible")
            if row.has_injective_non_surjective_opposite_section:
                add(f"{side}_opposite_injective_non_surjective")
            if (
                row.constant_map_is_bijective
                and row.companion_sections_bijective
                and not row.product_collapse_for_hidden_nonunit
                and row.has_nonbijective_opposite_section
                and not row.has_proper_opposite_kernel
                and not row.has_injective_non_surjective_opposite_section
            ):
                add(f"{side}_opposite_hidden_nonunit_unclassified")

        opposite_side = "right" if side == "left" else "left"
        opposite_latin_pairs = (
            set(self.right_latin_row_pairs)
            if side == "left"
            else set(self.left_latin_row_pairs)
        )
        opposite_triangular_pairs = (
            set(self.right_triangular_row_pairs)
            if side == "left"
            else set(self.left_triangular_row_pairs)
        )
        if pair in opposite_latin_pairs:
            add(f"side_dual_{opposite_side}_latin_available")
        elif pair in opposite_triangular_pairs:
            add(f"side_dual_{opposite_side}_triangular_nonlatin")
        else:
            add(f"no_side_dual_{opposite_side}_latin_replacement")

        return tuple(reasons)

    @property
    def missing_left_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        return tuple(
            (pair, reason)
            for pair in self.missing_left_latin_row_pairs
            for reason in self._missing_latin_row_reasons("left", pair)
        )

    @property
    def missing_right_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        return tuple(
            (pair, reason)
            for pair in self.missing_right_latin_row_pairs
            for reason in self._missing_latin_row_reasons("right", pair)
        )

    @property
    def active_missing_left_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        if self.status != "triangular_recovery_kink_completion_deficit":
            return ()
        routed_pair_reasons = {
            "left_row_product_collapse",
            "left_opposite_proper_kernel_visible",
            "left_opposite_injective_non_surjective",
            "side_dual_right_latin_available",
        }
        active_reasons = {
            "no_left_triangular_row",
            "left_constant_map_proper_kernel",
            "left_constant_map_universal_kernel",
            "left_companion_sections_injective_non_surjective",
        }
        active = []
        for pair in self.missing_left_latin_row_pairs:
            reasons = self._missing_latin_row_reasons("left", pair)
            if any(reason in routed_pair_reasons for reason in reasons):
                continue
            has_constant_kernel_support = any(
                reason
                in {
                    "left_constant_map_proper_kernel",
                    "left_constant_map_universal_kernel",
                }
                for reason in reasons
            )
            for reason in reasons:
                if reason not in active_reasons:
                    continue
                if (
                    reason == "left_companion_sections_injective_non_surjective"
                    and not has_constant_kernel_support
                ):
                    continue
                active.append((pair, reason))
        return tuple(active)

    @property
    def active_missing_right_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        if self.status != "triangular_recovery_kink_completion_deficit":
            return ()
        routed_pair_reasons = {
            "right_row_product_collapse",
            "right_opposite_proper_kernel_visible",
            "right_opposite_injective_non_surjective",
            "side_dual_left_latin_available",
        }
        active_reasons = {
            "no_right_triangular_row",
            "right_constant_map_proper_kernel",
            "right_constant_map_universal_kernel",
            "right_companion_sections_injective_non_surjective",
        }
        active = []
        for pair in self.missing_right_latin_row_pairs:
            reasons = self._missing_latin_row_reasons("right", pair)
            if any(reason in routed_pair_reasons for reason in reasons):
                continue
            has_constant_kernel_support = any(
                reason
                in {
                    "right_constant_map_proper_kernel",
                    "right_constant_map_universal_kernel",
                }
                for reason in reasons
            )
            for reason in reasons:
                if reason not in active_reasons:
                    continue
                if (
                    reason == "right_companion_sections_injective_non_surjective"
                    and not has_constant_kernel_support
                ):
                    continue
                active.append((pair, reason))
        return tuple(active)

    @property
    def active_companion_block_image_support_rows(
        self,
    ) -> Tuple[Tuple[str, Tuple[Color, Color], Tuple[str, ...]], ...]:
        rows = []
        for side, defects in (
            ("left", self.active_missing_left_latin_row_defects),
            ("right", self.active_missing_right_latin_row_defects),
        ):
            companion_reason = f"{side}_companion_sections_injective_non_surjective"
            support_reasons = {
                f"{side}_constant_map_proper_kernel",
                f"{side}_constant_map_universal_kernel",
            }
            for pair, reason in defects:
                if reason != companion_reason:
                    continue
                raw_reasons = self._missing_latin_row_reasons(side, pair)
                rows.append(
                    (
                        side,
                        pair,
                        tuple(
                            support
                            for support in raw_reasons
                            if support in support_reasons
                        ),
                    )
                )
        return tuple(rows)

    @property
    def active_companion_block_images_have_constant_kernel_support(self) -> bool:
        return all(
            bool(support_reasons)
            for _side, _pair, support_reasons in self.active_companion_block_image_support_rows
        )

    @property
    def missing_left_latin_row_pairs(self) -> Tuple[Tuple[Color, Color], ...]:
        left_pairs = set(self.left_latin_row_pairs)
        return tuple(
            pair
            for pair in self.expected_latin_color_pairs
            if pair not in left_pairs
        )

    @property
    def missing_right_latin_row_pairs(self) -> Tuple[Tuple[Color, Color], ...]:
        right_pairs = set(self.right_latin_row_pairs)
        return tuple(
            pair
            for pair in self.expected_latin_color_pairs
            if pair not in right_pairs
        )

    @property
    def left_latin_rows_present_for_all_pairs(self) -> bool:
        return not self.missing_left_latin_row_pairs

    @property
    def right_latin_rows_present_for_all_pairs(self) -> bool:
        return not self.missing_right_latin_row_pairs

    @property
    def side_dual_latin_completion_available(self) -> bool:
        return (
            bool(self.missing_left_latin_row_pairs)
            and self.right_latin_rows_present_for_all_pairs
        )

    @property
    def latin_ybe_failure_triples(self) -> Tuple[Tuple[Color, Color, Color, str], ...]:
        return self._latin_ybe_failure_triples(self.latin_triangular)

    @property
    def side_dual_latin_ybe_failure_triples(
        self,
    ) -> Tuple[Tuple[Color, Color, Color, str], ...]:
        return self._latin_ybe_failure_triples(self.side_dual_latin_triangular)

    @staticmethod
    def _latin_ybe_failure_triples(
        audit: LatinTriangularYBEAudit,
    ) -> Tuple[Tuple[Color, Color, Color, str], ...]:
        failures = []
        for triple in audit.triple_audits:
            prefix = (
                triple.left_color,
                triple.middle_color,
                triple.right_color,
            )
            if triple.alpha_failures:
                failures.append((*prefix, "alpha"))
            if triple.middle_failures:
                failures.append((*prefix, "middle"))
            if triple.endpoint_failures:
                failures.append((*prefix, "endpoint"))
        return tuple(failures)

    @property
    def rack_kink_completion_deficits(self) -> Tuple[str, ...]:
        deficits = []
        if not self.rack_kink.base_is_finite_rack:
            deficits.append("base_not_finite_rack")
        if not self.rack_kink.latin_rows_present_for_all_pairs:
            deficits.append("latin_rows_not_present_for_all_pairs")
            if self.side_dual_latin_completion_available:
                deficits.append("side_dual_latin_rows_present_for_all_pairs")
        if (
            self.rack_kink.latin_rows_present_for_all_pairs
            and not self.rack_kink.latin_ybe_equations_hold
        ):
            deficits.append("latin_ybe_equations_not_verified")
        if self.rack_kink.theorem_hypotheses_hold and not self.rack_kink.kink_cancellation_verified:
            deficits.append("kink_cancellation_not_verified")
        return tuple(deficits)

    @property
    def live_kink_completion_deficits(self) -> Tuple[str, ...]:
        if not self.triangular_recovery_needs_kink_completion:
            return ()
        return tuple(
            deficit
            for deficit in self.rack_kink_completion_deficits
            if deficit == "latin_rows_not_present_for_all_pairs"
        )

    @property
    def nonlive_kink_completion_deficits(self) -> Tuple[str, ...]:
        live = set(self.live_kink_completion_deficits)
        return tuple(
            deficit
            for deficit in self.rack_kink_completion_deficits
            if deficit not in live
        )

    @property
    def triangular_recovery_needs_kink_completion(self) -> bool:
        return (
            self.triangular_endpoint_recovery_obstruction
            and bool(self.rack_kink_completion_deficits)
        )

    @property
    def triangular_endpoint_recovery_obstruction(self) -> bool:
        return (
            self.triangular_recovery_verified
            and not self.all_triangular_rows_close_by_product
            and not self.latin_triangular_kink_impossible
            and not self.side_dual_latin_triangular_kink_impossible
        )

    @property
    def triangular_recovery_unit_observer(self) -> TriangularRecoveryUnitObserverAudit:
        return triangular_recovery_unit_observer_from_audit(self.triangular_recovery)

    @property
    def triangular_recovery_unit_observer_ready(self) -> bool:
        return (
            self.triangular_endpoint_recovery_obstruction
            and self.triangular_recovery_unit_observer.proves_fixed_unit_observer
        )

    @property
    def direct_unit_longitude_status_preempted_by_kink_dichotomy(self) -> bool:
        return (
            self.triangular_recovery_unit_observer_ready
            and not self.rack_kink_completion_deficits
            and (
                self.latin_triangular_kink_contradiction
                or self.latin_triangular_kink_impossible
            )
        )

    @property
    def status(self) -> str:
        if self.closed_by_repair_contract:
            return "closed_by_repair_contract"
        if not self.target_ready:
            return self.obstruction.status
        if self.closed_by_strand_continuing_transport:
            return "closed_by_transport_state_rackification"
        if self.closed_by_locally_nondegenerate_branch:
            return "closed_by_locally_nondegenerate_branch"
        if self.proper_section_kernel_visible:
            return "section_kernel_visible_to_existing_readouts"
        if self.all_triangular_rows_close_by_product:
            return "closed_by_product_triangular_collapse"
        if self.triangular_structural_inconsistency:
            return "triangular_structural_inconsistency"
        if self.rack_base_consistency_inconsistent:
            return "rack_base_consistency_inconsistent"
        if self.latin_triangular_ybe_projection_inconsistent:
            return "latin_triangular_ybe_projection_inconsistent"
        if self.latin_triangular_kink_cancellation_inconsistent:
            return "latin_triangular_kink_cancellation_inconsistent"
        if self.latin_triangular_kink_contradiction:
            return "latin_triangular_kink_contradiction"
        if self.latin_triangular_kink_impossible:
            return "latin_triangular_kink_impossible"
        if self.side_dual_latin_triangular_ybe_projection_inconsistent:
            return "side_dual_latin_triangular_ybe_projection_inconsistent"
        if self.side_dual_latin_triangular_diagonal_cancellation_inconsistent:
            return "side_dual_latin_triangular_diagonal_cancellation_inconsistent"
        if self.side_dual_latin_triangular_kink_contradiction:
            return "side_dual_latin_triangular_kink_contradiction"
        if self.side_dual_latin_triangular_kink_impossible:
            return "side_dual_latin_triangular_kink_impossible"
        if self.triangular_recovery_needs_kink_completion:
            return "triangular_recovery_kink_completion_deficit"
        if self.triangular_recovery_unit_observer_ready:
            return "triangular_recovery_unit_longitude_obstruction"
        if self.triangular_endpoint_recovery_obstruction:
            return "triangular_endpoint_recovery_obstruction"
        if self.hidden_rank_loss_is_constant:
            return "constant_section_triangular_obstruction"
        if self.mixed_unit_context_recovery:
            return "mixed_unit_context_recovery_obstruction"
        if self.nonunit_endpoint_obstruction:
            return "nonunit_endpoint_obstruction"
        return "unclassified_nonlinear_obstruction"

    @property
    def remaining_obligations(self) -> Tuple[str, ...]:
        if self.status in {
            "closed_by_repair_contract",
            "closed_by_transport_state_rackification",
            "closed_by_locally_nondegenerate_branch",
            "section_kernel_visible_to_existing_readouts",
            "closed_by_product_triangular_collapse",
            "triangular_structural_inconsistency",
            "rack_base_consistency_inconsistent",
            "latin_triangular_kink_contradiction",
            "latin_triangular_kink_impossible",
            "latin_triangular_ybe_projection_inconsistent",
            "latin_triangular_kink_cancellation_inconsistent",
            "side_dual_latin_triangular_kink_contradiction",
            "side_dual_latin_triangular_kink_impossible",
            "side_dual_latin_triangular_ybe_projection_inconsistent",
            "side_dual_latin_triangular_diagonal_cancellation_inconsistent",
        }:
            return ()
        if self.status == "triangular_recovery_kink_completion_deficit":
            return (
                "prove the triangular recovery corridor satisfies the rack-kink all-pairs Latin hypotheses",
                "or route the failed kink-completion hypothesis to a fixed detector or normalized-law seed",
                "then prove the remaining recovery endpoint lies in V_beta(U_tri)",
            )
        if self.status == "triangular_recovery_unit_longitude_obstruction":
            return (
                "prove each triangular recovery endpoint composite lies in V_beta(U_tri)",
                "or upgrade one U_tri endpoint miss to a normalized-law sequence",
            )
        if self.status == "triangular_endpoint_recovery_obstruction":
            return (
                "construct the fixed triangular recovery unit observer",
                "or upgrade one recovery endpoint to a normalized-law sequence",
            )
        if self.status == "constant_section_triangular_obstruction":
            return (
                "prove triangular bundle recovery visibility",
                "or construct a normalized-law obstruction from a constant section",
            )
        if self.status == "mixed_unit_context_recovery_obstruction":
            return (
                "route mixed-unit context recovery to constant-section triangular form",
                "or construct a normalized-law obstruction from the mixed row",
            )
        if self.status == "nonunit_endpoint_obstruction":
            return (
                "apply the unit-factorization gate to show nonunit rows are not final movers",
                "or exhibit a unit endpoint surviving all finite detectors",
            )
        return self.obstruction.failure_reasons


def nonlinear_overlap_refinement_audit(
    interval: LocalInterval,
    *,
    repair_contract_audit: "DescentEndpointRepairContractAudit | None" = None,
    normalized_prefix: "LocalNormalizedLawPrefixWitnessAudit | None" = None,
    max_kernel_degree: int | None = None,
) -> NonlinearOverlapRefinementAudit:
    """Return the post-linear nonlinear-overlap audit plus row-level refinements."""

    return NonlinearOverlapRefinementAudit(
        obstruction=nonlinear_overlap_obstruction_audit(
            interval,
            repair_contract_audit=repair_contract_audit,
            normalized_prefix=normalized_prefix,
            max_kernel_degree=max_kernel_degree,
        ),
        unit_collapse=two_sided_unit_collapse_audit(interval),
        rank_profile=section_rank_profile_collapse_audit(interval),
        triangular_bundle=triangular_bundle_audit(interval),
        triangular_recovery=triangular_recovery_audit(interval),
        triangular_column=triangular_column_collapse_audit(interval),
        latin_triangular=latin_triangular_ybe_audit(interval),
        side_dual_latin_triangular=latin_triangular_ybe_audit(
            side_opposite_local_interval(interval),
        ),
        rack_kink=rack_kink_latin_triangular_collapse_audit(interval),
        side_dual_rack_kink=right_rack_kink_latin_triangular_collapse_audit(
            side_opposite_local_interval(interval),
        ),
    )


def post_linear_remaining_finite_system_audit(
    interval: LocalInterval,
    *,
    repair_contract_audit: "DescentEndpointRepairContractAudit | None" = None,
    normalized_prefix: "LocalNormalizedLawPrefixWitnessAudit | None" = None,
    max_kernel_degree: int | None = None,
    kink_completion_deficits_routed: bool = False,
    triangular_recovery_endpoint_witness: (
        TriangularRecoveryEndpointWitnessAudit | None
    ) = None,
    triangular_recovery_symmetric_endpoint_fork: (
        TriangularRecoverySymmetricEndpointForkAudit | None
    ) = None,
    universal_continuation_endpoint_witness: (
        "UniversalContinuationIdentityEndpointWitnessAudit | None"
    ) = None,
    universal_continuation_symmetric_endpoint_fork: (
        "UniversalContinuationIdentitySymmetricEndpointForkAudit | None"
    ) = None,
    mixed_unit_context_endpoint_witness: (
        "MixedUnitContextEndpointWitnessAudit | None"
    ) = None,
    mixed_unit_context_symmetric_endpoint_fork: (
        "MixedUnitContextSymmetricEndpointForkAudit | None"
    ) = None,
    universal_k_signed_endpoint_reachable_seed_states: (
        Sequence[Tuple[str, UniversalKSeedState]] | None
    ) = None,
    universal_k_signed_endpoint_rows: (
        Sequence[UniversalKSignedEndpointGeneratorRow] | None
    ) = None,
    universal_k_signed_endpoint_group: FiniteGroup | None = None,
    universal_k_signed_endpoint_witnesses: (
        Mapping[UniversalKSignedEndpointEntryKey, LongitudeSubgroupWitness] | None
    ) = None,
    universal_k_word_potential_certificate: (
        UniversalKWordPotentialCertificate | None
    ) = None,
    universal_k_detector_track_counts_by_family: Tuple[Tuple[str, int], ...] = (),
    universal_k_detector_track_initialization_rows: Tuple[
        UniversalKDetectorTrackInitializationRow,
        ...,
    ] = (),
    universal_k_endpoint_target_audit: UniversalKEndpointTargetAudit | None = None,
    universal_k_cutoff_readouts_exact: bool = False,
    universal_k_cutoff_readout_audit: UniversalKCutoffReadoutAudit | None = None,
    universal_k_residual_faithfulness_verified: bool = False,
    universal_k_residual_action_scope: (
        UniversalKResidualActionScopeAudit | None
    ) = None,
    universal_k_residual_faithfulness_theorem: (
        UniversalKResidualFaithfulnessAudit | None
    ) = None,
    universal_k_residual_action_audit: "EndpointResidualActionAudit | None" = None,
    universal_k_telescoping_detector_audit: (
        UniversalKTelescopingDetectorAudit | None
    ) = None,
    universal_k_signed_endpoint_generator: (
        UniversalKSignedEndpointGeneratorAudit | None
    ) = None,
    unsupported_companion_structural_contradiction: (
        UnsupportedCompanionStructuralContradictionAudit | None
    ) = None,
) -> PostLinearRemainingFiniteSystemAudit:
    """Return the K/U finite-system classifier after finite-linear closure."""

    refinement = nonlinear_overlap_refinement_audit(
        interval,
        repair_contract_audit=repair_contract_audit,
        normalized_prefix=normalized_prefix,
        max_kernel_degree=max_kernel_degree,
    )
    triangular_latin_defect_closure = triangular_latin_defect_closure_audit(interval)
    triangular_constant_kernel_recovery_route = (
        triangular_constant_kernel_recovery_route_audit(interval)
    )
    missing_triangular_row_profile = missing_triangular_row_profile_audit(interval)
    missing_triangular_left_rack_cardinality = (
        missing_triangular_left_rack_cardinality_audit(interval)
    )
    missing_triangular_coordinate_unit_routing = (
        missing_triangular_coordinate_unit_routing_audit(interval)
    )
    missing_triangular_partial_constant_closure = (
        missing_triangular_partial_constant_closure_audit(interval)
    )
    missing_triangular_partial_constant_continuation_route = (
        missing_triangular_partial_constant_continuation_route_audit(interval)
    )
    universal_continuation_identity_routing = (
        universal_continuation_identity_routing_audit(interval)
    )
    signed_endpoint_generator = universal_k_signed_endpoint_generator
    derive_signed_endpoint_generator = (
        signed_endpoint_generator is None
        and (
            universal_k_signed_endpoint_reachable_seed_states is not None
            or universal_k_signed_endpoint_rows is not None
            or universal_k_signed_endpoint_group is not None
            or universal_k_signed_endpoint_witnesses is not None
            or universal_k_word_potential_certificate is not None
            or bool(universal_k_detector_track_counts_by_family)
            or bool(universal_k_detector_track_initialization_rows)
            or universal_k_endpoint_target_audit is not None
            or universal_k_cutoff_readout_audit is not None
            or universal_k_residual_action_scope is not None
            or universal_k_residual_faithfulness_theorem is not None
            or universal_k_residual_action_audit is not None
            or universal_k_telescoping_detector_audit is not None
        )
    )
    if derive_signed_endpoint_generator:
        unsigned = PostLinearRemainingFiniteSystemAudit(
            refinement=refinement,
            kink_completion_deficits_routed=kink_completion_deficits_routed,
            triangular_latin_defect_closure=triangular_latin_defect_closure,
            triangular_constant_kernel_recovery_route=triangular_constant_kernel_recovery_route,
            missing_triangular_row_profile=missing_triangular_row_profile,
            missing_triangular_left_rack_cardinality=missing_triangular_left_rack_cardinality,
            missing_triangular_coordinate_unit_routing=missing_triangular_coordinate_unit_routing,
            missing_triangular_partial_constant_closure=missing_triangular_partial_constant_closure,
            missing_triangular_partial_constant_continuation_route=missing_triangular_partial_constant_continuation_route,
            universal_continuation_identity_routing=universal_continuation_identity_routing,
            triangular_recovery_endpoint_witness=triangular_recovery_endpoint_witness,
            triangular_recovery_symmetric_endpoint_fork=triangular_recovery_symmetric_endpoint_fork,
            universal_continuation_endpoint_witness=universal_continuation_endpoint_witness,
            universal_continuation_symmetric_endpoint_fork=universal_continuation_symmetric_endpoint_fork,
            mixed_unit_context_endpoint_witness=mixed_unit_context_endpoint_witness,
            mixed_unit_context_symmetric_endpoint_fork=mixed_unit_context_symmetric_endpoint_fork,
            universal_k_signed_endpoint_interval=interval,
            unsupported_companion_structural_contradiction=unsupported_companion_structural_contradiction,
        )
        reachable_states = universal_k_signed_endpoint_reachable_seed_states
        if reachable_states is None:
            reachable_states = universal_k_signed_endpoint_transition_closure(
                unsigned.universal_k_seed_classifier_entries,
                universal_k_signed_endpoint_rows or (),
            )
        if universal_k_word_potential_certificate is not None:
            signed_endpoint_generator = universal_k_endpoint_observer_build(
                interval,
                unsigned.universal_k_seed_classifier_entries,
                universal_k_word_potential_certificate,
                detector_track_counts_by_family=(
                    universal_k_detector_track_counts_by_family
                ),
                detector_track_initialization_rows=(
                    universal_k_detector_track_initialization_rows
                ),
                endpoint_target_audit=universal_k_endpoint_target_audit,
                cutoff_readout_audit=universal_k_cutoff_readout_audit,
                residual_faithfulness_theorem=universal_k_residual_faithfulness_theorem,
                residual_action_scope=universal_k_residual_action_scope,
                residual_action_audit=universal_k_residual_action_audit,
                witnesses=universal_k_signed_endpoint_witnesses,
            ).audit
        else:
            signed_endpoint_generator = universal_k_signed_endpoint_generator_audit(
                interval,
                unsigned.universal_k_seed_classifier_entries,
                reachable_states or (),
                universal_k_signed_endpoint_rows or (),
                endpoint_group=universal_k_signed_endpoint_group,
                witnesses=universal_k_signed_endpoint_witnesses,
                endpoint_target_audit=universal_k_endpoint_target_audit,
                cutoff_readouts_exact=universal_k_cutoff_readouts_exact,
                cutoff_readout_audit=universal_k_cutoff_readout_audit,
                residual_faithfulness_verified=universal_k_residual_faithfulness_verified,
                residual_action_scope=universal_k_residual_action_scope,
                residual_faithfulness_theorem=universal_k_residual_faithfulness_theorem,
                residual_action_audit=universal_k_residual_action_audit,
                telescoping_detector_audit=universal_k_telescoping_detector_audit,
            )

    return PostLinearRemainingFiniteSystemAudit(
        refinement=refinement,
        kink_completion_deficits_routed=kink_completion_deficits_routed,
        triangular_latin_defect_closure=triangular_latin_defect_closure,
        triangular_constant_kernel_recovery_route=triangular_constant_kernel_recovery_route,
        missing_triangular_row_profile=missing_triangular_row_profile,
        missing_triangular_left_rack_cardinality=missing_triangular_left_rack_cardinality,
        missing_triangular_coordinate_unit_routing=missing_triangular_coordinate_unit_routing,
        missing_triangular_partial_constant_closure=missing_triangular_partial_constant_closure,
        missing_triangular_partial_constant_continuation_route=missing_triangular_partial_constant_continuation_route,
        universal_continuation_identity_routing=universal_continuation_identity_routing,
        triangular_recovery_endpoint_witness=triangular_recovery_endpoint_witness,
        triangular_recovery_symmetric_endpoint_fork=triangular_recovery_symmetric_endpoint_fork,
        universal_continuation_endpoint_witness=universal_continuation_endpoint_witness,
        universal_continuation_symmetric_endpoint_fork=universal_continuation_symmetric_endpoint_fork,
        mixed_unit_context_endpoint_witness=mixed_unit_context_endpoint_witness,
        mixed_unit_context_symmetric_endpoint_fork=mixed_unit_context_symmetric_endpoint_fork,
        universal_k_signed_endpoint_generator=signed_endpoint_generator,
        universal_k_signed_endpoint_interval=interval,
        unsupported_companion_structural_contradiction=unsupported_companion_structural_contradiction,
    )
