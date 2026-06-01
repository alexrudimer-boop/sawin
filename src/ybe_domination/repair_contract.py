from __future__ import annotations

from dataclasses import dataclass
from math import factorial
from typing import TYPE_CHECKING, Tuple

from .endpoint_factorization import (
    EndpointArtinDefectResidualActionAudit,
    EndpointResidualActionAudit,
    RoutedLostEdgeEndpointWitnessAudit,
    UniversalContinuationIdentityEndpointWitnessAudit,
)
from .local_interval import ReadoutDescentSeparationAudit


if TYPE_CHECKING:  # pragma: no cover - typing only
    from .residual import LocalNormalizedLawPrefixWitnessAudit


EndpointActionAudit = EndpointResidualActionAudit | EndpointArtinDefectResidualActionAudit
RoutedEndpointWitnessAudit = (
    RoutedLostEdgeEndpointWitnessAudit | UniversalContinuationIdentityEndpointWitnessAudit
)


@dataclass(frozen=True)
class DescentEndpointRepairContractAudit:
    """Integrated audit for the descent-endpoint repair contract.

    This audit does not discover the missing readouts or endpoint witnesses.
    It records whether supplied certificates have the exact shape required by
    the repair theorem: descent separation, faithful endpoint detection on the
    supplied residual rows, and optional routed lost-edge endpoint visibility.
    """

    descent_audit: ReadoutDescentSeparationAudit
    endpoint_action_audit: EndpointActionAudit
    routed_edge_audit: RoutedEndpointWitnessAudit | None = None

    @property
    def descent_separation_proved(self) -> bool:
        return self.descent_audit.proves_descent_separation_readout

    @property
    def endpoint_action_detector_proved(self) -> bool:
        return self.endpoint_action_audit.proves_complete_residual_action_implication

    @property
    def routed_edges_visible(self) -> bool:
        return (
            self.routed_edge_audit is None
            or self.routed_edge_audit.proves_routed_lost_edge_endpoint_visibility
        )

    @property
    def routed_edge_descent_matches_supplied_descent(self) -> bool:
        if self.routed_edge_audit is None:
            return True
        saturated_descent = (
            self.routed_edge_audit.routing_audit.dichotomy.seed_saturation.saturated_descent
        )
        return saturated_descent == self.descent_audit

    @property
    def proves_repair_contract_for_supplied_data(self) -> bool:
        return (
            self.descent_separation_proved
            and self.endpoint_action_detector_proved
            and self.routed_edges_visible
            and self.routed_edge_descent_matches_supplied_descent
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.descent_separation_proved:
            reasons.append("descent_separation_not_proved")
        if not self.endpoint_action_detector_proved:
            reasons.append("endpoint_action_detector_not_proved")
        if not self.routed_edges_visible:
            reasons.append("routed_edges_not_visible")
        if not self.routed_edge_descent_matches_supplied_descent:
            reasons.append("routed_edge_descent_mismatch")
        return tuple(reasons)


def descent_endpoint_repair_contract_audit(
    descent_audit: ReadoutDescentSeparationAudit,
    endpoint_action_audit: EndpointActionAudit,
    routed_edge_audit: RoutedEndpointWitnessAudit | None = None,
) -> DescentEndpointRepairContractAudit:
    """Bundle supplied repair-contract certificates into one audit."""

    return DescentEndpointRepairContractAudit(
        descent_audit=descent_audit,
        endpoint_action_audit=endpoint_action_audit,
        routed_edge_audit=routed_edge_audit,
    )


@dataclass(frozen=True)
class SymmetricRepairContractBridgeAudit:
    """Bridge a supplied finite repair detector to a symmetric detector.

    The repair contract proves a local implication using some fixed finite
    product detector ``H``.  Once that supplied implication is valid, the left
    regular embedding ``H -> S_|H|`` shows that identity ``S_m`` longitude data
    with ``m >= |H|`` implies identity ``H`` longitude data.  This audit records
    that certificate-level bridge; it does not construct the missing repair
    contract witnesses.
    """

    repair_contract_audit: DescentEndpointRepairContractAudit
    detector_group_order: int
    symmetric_degree: int

    @property
    def detector_group_order_valid(self) -> bool:
        return self.detector_group_order > 0

    @property
    def symmetric_degree_valid(self) -> bool:
        return self.symmetric_degree > 0

    @property
    def left_regular_embedding_available(self) -> bool:
        return (
            self.detector_group_order_valid
            and self.symmetric_degree_valid
            and self.symmetric_degree >= self.detector_group_order
        )

    @property
    def symmetric_group_order(self) -> int | None:
        if not self.symmetric_degree_valid:
            return None
        return factorial(self.symmetric_degree)

    @property
    def symmetric_detector_rack_size(self) -> int | None:
        group_order = self.symmetric_group_order
        if group_order is None:
            return None
        return 2 * group_order * group_order

    @property
    def repair_contract_proved(self) -> bool:
        return self.repair_contract_audit.proves_repair_contract_for_supplied_data

    @property
    def proves_symmetric_detector_from_repair_contract(self) -> bool:
        return self.repair_contract_proved and self.left_regular_embedding_available

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.repair_contract_proved:
            reasons.append("repair_contract_not_proved")
        if not self.detector_group_order_valid:
            reasons.append("invalid_detector_group_order")
        if not self.symmetric_degree_valid:
            reasons.append("invalid_symmetric_degree")
        elif (
            self.detector_group_order_valid
            and self.symmetric_degree < self.detector_group_order
        ):
            reasons.append("symmetric_degree_too_small")
        return tuple(reasons)


def symmetric_repair_contract_bridge_audit(
    repair_contract_audit: DescentEndpointRepairContractAudit,
    detector_group_order: int,
    symmetric_degree: int | None = None,
) -> SymmetricRepairContractBridgeAudit:
    """Record that a supplied finite repair detector may be replaced by ``S_m``.

    When ``symmetric_degree`` is omitted, the minimal left-regular degree
    ``m=|H|`` is used.  Larger degrees are also valid by symmetric tower
    monotonicity, but this helper only records the direct left-regular bridge.
    """

    if symmetric_degree is None:
        symmetric_degree = detector_group_order
    return SymmetricRepairContractBridgeAudit(
        repair_contract_audit=repair_contract_audit,
        detector_group_order=detector_group_order,
        symmetric_degree=symmetric_degree,
    )


@dataclass(frozen=True)
class EndpointFamilySymmetricForkRow:
    """One finite endpoint factor row for a symmetric cutoff family."""

    factor_index: int
    endpoint_group_order: int
    endpoint_witness_supplied: bool
    faithful_readout: bool

    @property
    def factor_index_valid(self) -> bool:
        return self.factor_index >= 0

    @property
    def endpoint_group_order_valid(self) -> bool:
        return self.endpoint_group_order > 0

    @property
    def row_valid(self) -> bool:
        return self.factor_index_valid and self.endpoint_group_order_valid


@dataclass(frozen=True)
class EndpointFamilySymmetricForkAudit:
    """Audit the symmetric cutoff fork for a finite endpoint family.

    This is a certificate-shape audit for the endpoint-family theorem.  It
    does not construct the missing all-``n`` endpoint witnesses.  It records
    when a supplied finite family of fixed endpoint factors is killed by one
    symmetric detector degree, and when supplied failed degrees form a finite
    prefix of the symmetric-tail B-seed shape.
    """

    endpoint_group_orders: Tuple[int, ...]
    all_endpoint_witnesses_supplied: bool
    endpoint_family_faithful: bool
    symmetric_degree: int
    failed_symmetric_degrees: Tuple[int, ...] = ()
    endpoint_rows: Tuple[EndpointFamilySymmetricForkRow, ...] = ()

    @property
    def endpoint_family_empty(self) -> bool:
        return not self.endpoint_group_orders

    @property
    def endpoint_group_orders_valid(self) -> bool:
        return all(order > 0 for order in self.endpoint_group_orders)

    @property
    def expected_endpoint_row_keys(self) -> Tuple[int, ...]:
        return tuple(range(len(self.endpoint_group_orders)))

    @property
    def endpoint_row_keys(self) -> Tuple[int, ...]:
        return tuple(row.factor_index for row in self.endpoint_rows)

    @property
    def duplicate_endpoint_row_keys(self) -> Tuple[int, ...]:
        seen = set()
        duplicates = []
        for key in self.endpoint_row_keys:
            if key in seen and key not in duplicates:
                duplicates.append(key)
            seen.add(key)
        return tuple(duplicates)

    @property
    def missing_endpoint_row_keys(self) -> Tuple[int, ...]:
        row_keys = set(self.endpoint_row_keys)
        return tuple(key for key in self.expected_endpoint_row_keys if key not in row_keys)

    @property
    def extra_endpoint_row_keys(self) -> Tuple[int, ...]:
        expected = set(self.expected_endpoint_row_keys)
        return tuple(key for key in self.endpoint_row_keys if key not in expected)

    @property
    def endpoint_row_order_mismatches(self) -> Tuple[Tuple[int, int, int], ...]:
        expected = dict(enumerate(self.endpoint_group_orders))
        return tuple(
            (row.factor_index, expected[row.factor_index], row.endpoint_group_order)
            for row in self.endpoint_rows
            if row.factor_index in expected
            and row.endpoint_group_order != expected[row.factor_index]
        )

    @property
    def invalid_endpoint_rows(self) -> Tuple[EndpointFamilySymmetricForkRow, ...]:
        return tuple(row for row in self.endpoint_rows if not row.row_valid)

    @property
    def endpoint_rows_cover_factors(self) -> bool:
        return (
            not self.endpoint_family_empty
            and not self.duplicate_endpoint_row_keys
            and not self.missing_endpoint_row_keys
            and not self.extra_endpoint_row_keys
            and not self.endpoint_row_order_mismatches
            and not self.invalid_endpoint_rows
        )

    @property
    def endpoint_rows_supply_witnesses(self) -> bool:
        return self.endpoint_rows_cover_factors and all(
            row.endpoint_witness_supplied for row in self.endpoint_rows
        )

    @property
    def endpoint_rows_are_faithful(self) -> bool:
        return self.endpoint_rows_cover_factors and all(
            row.faithful_readout for row in self.endpoint_rows
        )

    @property
    def endpoint_family_faithfulness_proved(self) -> bool:
        if self.endpoint_family_empty:
            return self.endpoint_family_faithful
        return self.endpoint_rows_are_faithful

    @property
    def minimum_symmetric_degree(self) -> int:
        if self.endpoint_family_empty:
            return 1
        return max(self.endpoint_group_orders)

    @property
    def symmetric_degree_valid(self) -> bool:
        return self.symmetric_degree > 0

    @property
    def symmetric_degree_covers_endpoint_groups(self) -> bool:
        return (
            self.endpoint_group_orders_valid
            and self.symmetric_degree_valid
            and self.symmetric_degree >= self.minimum_symmetric_degree
        )

    @property
    def endpoint_cutoff_proved(self) -> bool:
        return self.endpoint_family_empty or (
            self.endpoint_rows_supply_witnesses
            and self.symmetric_degree_covers_endpoint_groups
        )

    @property
    def faithful_endpoint_cutoff_proved(self) -> bool:
        return self.endpoint_cutoff_proved and self.endpoint_family_faithfulness_proved

    @property
    def failed_degrees_are_tail_prefix(self) -> bool:
        if not self.failed_symmetric_degrees:
            return False
        start = self.minimum_symmetric_degree
        expected = tuple(range(start, start + len(self.failed_symmetric_degrees)))
        return self.failed_symmetric_degrees == expected

    @property
    def proves_supplied_symmetric_tail_endpoint_seed_prefix(self) -> bool:
        return (
            self.endpoint_group_orders_valid
            and self.endpoint_family_faithfulness_proved
            and self.failed_degrees_are_tail_prefix
        )

    @property
    def failure_reasons(self) -> Tuple[str, ...]:
        reasons = []
        if not self.endpoint_group_orders_valid:
            reasons.append("invalid_endpoint_group_order")
        if not self.endpoint_family_empty and not self.endpoint_rows_cover_factors:
            reasons.append("endpoint_family_rows_not_exact")
        if self.duplicate_endpoint_row_keys:
            reasons.append("endpoint_family_duplicate_rows")
        if self.missing_endpoint_row_keys:
            reasons.append("endpoint_family_missing_rows")
        if self.extra_endpoint_row_keys:
            reasons.append("endpoint_family_extra_rows")
        if self.endpoint_row_order_mismatches:
            reasons.append("endpoint_family_row_order_mismatch")
        if self.invalid_endpoint_rows:
            reasons.append("endpoint_family_invalid_rows")
        if not self.endpoint_family_empty and not self.endpoint_rows_supply_witnesses:
            reasons.append("endpoint_witnesses_not_supplied")
        if not self.symmetric_degree_valid:
            reasons.append("invalid_symmetric_degree")
        elif (
            self.endpoint_group_orders_valid
            and self.symmetric_degree < self.minimum_symmetric_degree
        ):
            reasons.append("symmetric_degree_too_small")
        if not self.endpoint_family_faithfulness_proved:
            reasons.append("endpoint_family_not_faithful")
        return tuple(reasons)


def endpoint_family_symmetric_fork_audit(
    endpoint_group_orders: Tuple[int, ...],
    *,
    all_endpoint_witnesses_supplied: bool,
    endpoint_family_faithful: bool,
    symmetric_degree: int | None = None,
    failed_symmetric_degrees: Tuple[int, ...] = (),
    endpoint_rows: Tuple[EndpointFamilySymmetricForkRow, ...] | None = None,
) -> EndpointFamilySymmetricForkAudit:
    """Record the symmetric cutoff/tail fork for fixed endpoint factors."""

    orders = tuple(endpoint_group_orders)
    if symmetric_degree is None:
        symmetric_degree = max(orders) if orders else 1
    if endpoint_rows is None:
        endpoint_rows = tuple(
            EndpointFamilySymmetricForkRow(
                factor_index=index,
                endpoint_group_order=order,
                endpoint_witness_supplied=all_endpoint_witnesses_supplied,
                faithful_readout=endpoint_family_faithful,
            )
            for index, order in enumerate(orders)
        )
    return EndpointFamilySymmetricForkAudit(
        endpoint_group_orders=orders,
        all_endpoint_witnesses_supplied=all_endpoint_witnesses_supplied,
        endpoint_family_faithful=endpoint_family_faithful,
        symmetric_degree=symmetric_degree,
        failed_symmetric_degrees=tuple(failed_symmetric_degrees),
        endpoint_rows=tuple(endpoint_rows),
    )


@dataclass(frozen=True)
class EndpointFamilySymmetricSeedAudit:
    """Attach one endpoint-family symmetric failure to a local residual mover."""

    endpoint_family: EndpointFamilySymmetricForkAudit
    local_prefix: "LocalNormalizedLawPrefixWitnessAudit"
    symmetric_degree: int
    endpoint_channel_nonidentity: bool
    endpoint_miss_matches_residual_motion: bool
    endpoint_channel_value: object | None = None
    endpoint_channel_identity: object | None = None
    residual_input_tuple: Tuple[object, ...] = ()
    residual_output_tuple: Tuple[object, ...] = ()

    @property
    def uses_declared_symmetric_row(self) -> bool:
        if self.symmetric_degree <= 0:
            return False
        expected_order = factorial(self.symmetric_degree)
        return (
            self.local_prefix.group_orders == (expected_order,)
            and self.local_prefix.product_group_order == expected_order
        )

    @property
    def right_stabilized_by_symmetric_degree(self) -> bool:
        return self.local_prefix.target_n - self.local_prefix.source_n == self.symmetric_degree

    @property
    def symmetric_degree_covers_endpoint_family(self) -> bool:
        return (
            self.endpoint_family.endpoint_group_orders_valid
            and self.symmetric_degree >= self.endpoint_family.minimum_symmetric_degree
        )

    @property
    def degree_is_declared_endpoint_failure(self) -> bool:
        failed_degrees = self.endpoint_family.failed_symmetric_degrees
        return not failed_degrees or self.symmetric_degree in failed_degrees

    @property
    def local_prefix_is_symmetric_normalized_law_row(self) -> bool:
        return (
            self.local_prefix.proves_one_local_prefix_normalized_law_witness
            and self.uses_declared_symmetric_row
            and self.right_stabilized_by_symmetric_degree
        )

    @property
    def endpoint_miss_is_attached_to_prefix(self) -> bool:
        return (
            self.endpoint_family.endpoint_family_faithfulness_proved
            and self.endpoint_channel_miss_is_nonidentity
            and self.endpoint_miss_matches_prefix_motion
            and self.symmetric_degree_covers_endpoint_family
            and self.degree_is_declared_endpoint_failure
        )

    @property
    def endpoint_channel_miss_is_nonidentity(self) -> bool:
        return (
            self.endpoint_channel_value is not None
            and self.endpoint_channel_identity is not None
            and self.endpoint_channel_value != self.endpoint_channel_identity
        )

    @property
    def residual_motion_row_supplied(self) -> bool:
        return bool(self.residual_input_tuple) and bool(self.residual_output_tuple)

    @property
    def residual_motion_row_is_moved(self) -> bool:
        return (
            self.residual_motion_row_supplied
            and self.residual_input_tuple != self.residual_output_tuple
        )

    @property
    def endpoint_miss_matches_prefix_motion(self) -> bool:
        return (
            self.residual_motion_row_is_moved
            and self.residual_input_tuple == tuple(self.local_prefix.stabilized_fibre_tuple)
            and self.residual_output_tuple == tuple(self.local_prefix.stabilized_image)
        )

    @property
    def proves_one_endpoint_family_symmetric_seed(self) -> bool:
        return (
            self.local_prefix_is_symmetric_normalized_law_row
            and self.endpoint_miss_is_attached_to_prefix
        )


def endpoint_family_symmetric_seed_audit(
    endpoint_family: EndpointFamilySymmetricForkAudit,
    local_prefix: "LocalNormalizedLawPrefixWitnessAudit",
    symmetric_degree: int,
    *,
    endpoint_channel_nonidentity: bool,
    endpoint_miss_matches_residual_motion: bool,
    endpoint_channel_value: object | None = None,
    endpoint_channel_identity: object | None = None,
    residual_input_tuple: Tuple[object, ...] = (),
    residual_output_tuple: Tuple[object, ...] = (),
) -> EndpointFamilySymmetricSeedAudit:
    """Pair one endpoint-family miss with one local symmetric prefix row."""

    if endpoint_channel_value is None and endpoint_channel_nonidentity:
        endpoint_channel_value = "endpoint_nonidentity"
    if endpoint_channel_identity is None:
        endpoint_channel_identity = "endpoint_identity"
    if not residual_input_tuple and endpoint_miss_matches_residual_motion:
        residual_input_tuple = tuple(local_prefix.stabilized_fibre_tuple)
    if not residual_output_tuple and endpoint_miss_matches_residual_motion:
        residual_output_tuple = tuple(local_prefix.stabilized_image)
    return EndpointFamilySymmetricSeedAudit(
        endpoint_family=endpoint_family,
        local_prefix=local_prefix,
        symmetric_degree=symmetric_degree,
        endpoint_channel_nonidentity=endpoint_channel_nonidentity,
        endpoint_miss_matches_residual_motion=endpoint_miss_matches_residual_motion,
        endpoint_channel_value=endpoint_channel_value,
        endpoint_channel_identity=endpoint_channel_identity,
        residual_input_tuple=tuple(residual_input_tuple),
        residual_output_tuple=tuple(residual_output_tuple),
    )
