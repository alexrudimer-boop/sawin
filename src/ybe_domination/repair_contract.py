from __future__ import annotations

from dataclasses import dataclass
from math import factorial
from typing import Tuple

from .endpoint_factorization import (
    EndpointArtinDefectResidualActionAudit,
    EndpointResidualActionAudit,
    RoutedLostEdgeEndpointWitnessAudit,
)
from .local_interval import ReadoutDescentSeparationAudit


EndpointActionAudit = EndpointResidualActionAudit | EndpointArtinDefectResidualActionAudit


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
    routed_edge_audit: RoutedLostEdgeEndpointWitnessAudit | None = None

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
    routed_edge_audit: RoutedLostEdgeEndpointWitnessAudit | None = None,
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
