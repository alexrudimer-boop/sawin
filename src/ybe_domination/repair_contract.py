from __future__ import annotations

from dataclasses import dataclass
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
    def proves_repair_contract_for_supplied_data(self) -> bool:
        return (
            self.descent_separation_proved
            and self.endpoint_action_detector_proved
            and self.routed_edges_visible
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
