from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING, Sequence, Tuple

from .artin_longitudes import (
    ArtinDetectorLiftBraidAudit,
    ArtinDetectorLiftLabel,
    ArtinDetectorLiftTransitionAudit,
    BraidWord,
    LongitudeExpressionLetter,
    LongitudeSubgroupWitness,
    artin_detector_lift_braid_audit,
    artin_detector_lift_transition_audit,
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
        MixedUnitContextEndpointWitnessAudit,
        UniversalContinuationIdentityEndpointWitnessAudit,
    )
    from .repair_contract import DescentEndpointRepairContractAudit
    from .residual import LocalNormalizedLawPrefixWitnessAudit


NONLINEAR_OVERLAP_TARGET_VERDICT = "bi_free_universal_corridor_bottleneck"
TriangularRecoveryState = Tuple[Color, Color, FibrePoint, FibrePoint]
TriangularRecoveryEndpointKey = Tuple[Color, Color, str]


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
    universal_continuation_endpoint_witness: (
        "UniversalContinuationIdentityEndpointWitnessAudit | None"
    ) = None
    mixed_unit_context_endpoint_witness: (
        "MixedUnitContextEndpointWitnessAudit | None"
    ) = None

    @property
    def closed_by_recorded_branch(self) -> bool:
        return self.refinement.status in {
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
        }

    @property
    def raw_system_k(self) -> bool:
        return self.refinement.status == "triangular_recovery_kink_completion_deficit"

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
        if routing is None:
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
        if self.missing_triangular_coordinate_unit_routing is None:
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
                ): row
                for row in self.missing_triangular_partial_constant_continuation_route.rows
            }
        for row in closure_rows:
            if row.closure_is_proper:
                continue
            route = route_by_key.get(
                (
                    row.side,
                    row.left_color,
                    row.right_color,
                    row.fixed_input,
                    row.domain_color,
                    row.collapsed_inputs,
                )
            )
            if route is None or not route.routes_to_continuation_seed_closure:
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
            ): row
            for row in self.missing_triangular_partial_constant_continuation_route.rows
        }
        for row in closure_rows:
            if row.closure_is_proper:
                continue
            route = route_by_key.get(
                (
                    row.side,
                    row.left_color,
                    row.right_color,
                    row.fixed_input,
                    row.domain_color,
                    row.collapsed_inputs,
                )
            )
            if route is not None and route.routes_to_continuation_seed_closure:
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
        return self._live_missing_latin_row_defects(
            self.refinement.active_missing_left_latin_row_defects
            + self.refinement.active_missing_right_latin_row_defects,
        )

    @property
    def recovery_routed_k_missing_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        return self._recovery_routed_missing_latin_row_defects(
            self.refinement.active_missing_left_latin_row_defects
            + self.refinement.active_missing_right_latin_row_defects,
        )

    @property
    def continuation_routed_k_missing_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        return self._continuation_routed_missing_latin_row_defects(
            self.refinement.active_missing_left_latin_row_defects
            + self.refinement.active_missing_right_latin_row_defects,
        )

    @property
    def mixed_context_routed_k_missing_latin_row_defects(
        self,
    ) -> Tuple[Tuple[Tuple[Color, Color], str], ...]:
        return self._mixed_context_routed_missing_latin_row_defects(
            self.refinement.active_missing_left_latin_row_defects
            + self.refinement.active_missing_right_latin_row_defects,
        )

    @property
    def k_deficits_routed_to_recovery_endpoint(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and bool(self.recovery_routed_k_missing_latin_row_defects)
            and not self.live_k_missing_latin_row_defects
        )

    @property
    def k_deficits_routed_to_continuation_endpoint(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and bool(self.continuation_routed_k_missing_latin_row_defects)
            and not self.live_k_missing_latin_row_defects
        )

    @property
    def k_deficits_routed_to_mixed_context_endpoint(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
            and bool(self.mixed_context_routed_k_missing_latin_row_defects)
            and not self.live_k_missing_latin_row_defects
        )

    @property
    def k_deficits_closed_by_recorded_routing(self) -> bool:
        return (
            self.raw_system_k
            and not self.kink_completion_deficits_routed
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
            and bool(self.live_k_missing_latin_row_defects)
        )

    @property
    def routed_system_k_to_u(self) -> bool:
        return (
            (
                self.raw_system_k
                and self.kink_completion_deficits_routed
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
        if self.system_u_active and not self.system_u_closed_by_endpoint_witness:
            systems.append("U")
        if self.system_c_active and not self.system_c_closed_by_endpoint_witness:
            systems.append("C")
        if self.system_m_active and not self.system_m_closed_by_endpoint_witness:
            systems.append("M")
        return tuple(systems)

    @property
    def all_active_routed_endpoint_systems_closed(self) -> bool:
        return bool(self.active_routed_endpoint_systems) and not self.unclosed_routed_endpoint_systems

    @property
    def system_name(self) -> str:
        if self.closed_by_recorded_branch:
            return "closed_by_recorded_branch"
        if self.all_active_routed_endpoint_systems_closed:
            if self.active_routed_endpoint_systems == ("U",):
                return "closed_by_triangular_recovery_endpoint_witness"
            if self.active_routed_endpoint_systems == ("C",):
                return "closed_by_universal_continuation_endpoint_witness"
            if self.active_routed_endpoint_systems == ("M",):
                return "closed_by_mixed_unit_context_endpoint_witness"
            return "closed_by_routed_endpoint_witnesses"
        if len(self.unclosed_routed_endpoint_systems) > 1:
            joined = "".join(system.lower() for system in self.unclosed_routed_endpoint_systems)
            return f"system_{joined}_routed_endpoint_product"
        if self.k_deficits_closed_by_recorded_routing:
            return "closed_by_recorded_k_deficit_routing"
        if self.system_k_active:
            return "system_k_kink_completion_deficit"
        if self.system_u_active and not self.system_u_closed_by_endpoint_witness:
            return "system_u_triangular_recovery_unit_endpoint"
        if self.system_c_active and not self.system_c_closed_by_endpoint_witness:
            return "system_c_universal_continuation_endpoint"
        if self.system_m_active and not self.system_m_closed_by_endpoint_witness:
            return "system_m_mixed_unit_context_endpoint"
        return f"earlier_unrouted_status:{self.refinement.status}"

    @property
    def is_current_remaining_finite_system(self) -> bool:
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
        data.extend(self._universal_continuation_endpoint_witness_data)
        data.extend(self._coordinate_unit_routing_data)
        data.extend(self._mixed_unit_endpoint_witness_data)
        return tuple(data)

    @property
    def finite_obstruction_data(self) -> Tuple[Tuple[str, object], ...]:
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
                                if not row.routes_to_continuation_seed_closure
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
        if self.k_deficits_closed_by_recorded_routing:
            return ()
        if self.all_active_routed_endpoint_systems_closed:
            return ()
        endpoint_obligations = []
        if (
            self.system_u_active
            and not self.system_u_closed_by_endpoint_witness
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
        if self.system_c_active and not self.system_c_closed_by_endpoint_witness:
            endpoint_obligations.extend(
                (
                    "construct fixed endpoint witnesses for the routed universal-continuation seed closures",
                    "or upgrade one routed universal-continuation endpoint miss to a normalized-law sequence",
                )
            )
        if self.system_m_active and not self.system_m_closed_by_endpoint_witness:
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
    universal_continuation_endpoint_witness: (
        "UniversalContinuationIdentityEndpointWitnessAudit | None"
    ) = None,
    mixed_unit_context_endpoint_witness: (
        "MixedUnitContextEndpointWitnessAudit | None"
    ) = None,
) -> PostLinearRemainingFiniteSystemAudit:
    """Return the K/U finite-system classifier after finite-linear closure."""

    return PostLinearRemainingFiniteSystemAudit(
        refinement=nonlinear_overlap_refinement_audit(
            interval,
            repair_contract_audit=repair_contract_audit,
            normalized_prefix=normalized_prefix,
            max_kernel_degree=max_kernel_degree,
        ),
        kink_completion_deficits_routed=kink_completion_deficits_routed,
        triangular_latin_defect_closure=triangular_latin_defect_closure_audit(
            interval
        ),
        triangular_constant_kernel_recovery_route=triangular_constant_kernel_recovery_route_audit(
            interval
        ),
        missing_triangular_row_profile=missing_triangular_row_profile_audit(interval),
        missing_triangular_left_rack_cardinality=missing_triangular_left_rack_cardinality_audit(
            interval
        ),
        missing_triangular_coordinate_unit_routing=missing_triangular_coordinate_unit_routing_audit(
            interval
        ),
        missing_triangular_partial_constant_closure=missing_triangular_partial_constant_closure_audit(
            interval
        ),
        missing_triangular_partial_constant_continuation_route=missing_triangular_partial_constant_continuation_route_audit(
            interval
        ),
        universal_continuation_identity_routing=universal_continuation_identity_routing_audit(
            interval
        ),
        triangular_recovery_endpoint_witness=triangular_recovery_endpoint_witness,
        universal_continuation_endpoint_witness=universal_continuation_endpoint_witness,
        mixed_unit_context_endpoint_witness=mixed_unit_context_endpoint_witness,
    )
