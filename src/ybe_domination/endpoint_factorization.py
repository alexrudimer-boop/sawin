from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, Tuple

from .artin_longitudes import (
    BraidWord,
    LongitudeExpression,
    LongitudeSubgroupWitness,
    artin_longitudes,
    direct_product_longitude_subgroup_witness,
    evaluate_longitude_expression,
    evaluate_longitude_subgroup_witness,
    has_identity_longitude_signature,
)
from .finite_group import FiniteGroup, GroupElement, direct_product_group


@dataclass(frozen=True)
class EndpointLongitudeExpressionAudit:
    """Expression certificate for one endpoint in a fixed finite group."""

    artin_permutation: Tuple[int, ...]
    group_order: int
    endpoint: GroupElement
    endpoint_in_group: bool
    assignment: Tuple[GroupElement, ...]
    assignment_in_group: bool
    expression: LongitudeExpression
    expression_value: GroupElement | None
    expression_matches_endpoint: bool
    identity_longitude_signature: bool
    group_identity: GroupElement

    @property
    def endpoint_is_identity(self) -> bool:
        return self.endpoint == self.group_identity

    @property
    def endpoint_lies_in_longitude_subgroup_by_expression(self) -> bool:
        return (
            self.endpoint_in_group
            and self.assignment_in_group
            and self.expression_matches_endpoint
        )

    @property
    def identity_longitudes_kill_endpoint_by_expression(self) -> bool:
        if not self.endpoint_lies_in_longitude_subgroup_by_expression:
            return False
        if not self.identity_longitude_signature:
            return True
        return self.endpoint_is_identity


@dataclass(frozen=True)
class EndpointProductExpressionAudit:
    """Assemble endpoint expression certificates into one product detector."""

    factor_audits: Tuple[EndpointLongitudeExpressionAudit, ...]
    product_endpoint: Tuple[GroupElement, ...]
    group_orders: Tuple[int, ...]
    product_group_order: int
    product_witness: LongitudeSubgroupWitness | None
    product_witness_value: GroupElement | None
    product_witness_matches_endpoint: bool

    @property
    def all_endpoints_in_groups(self) -> bool:
        return all(audit.endpoint_in_group for audit in self.factor_audits)

    @property
    def all_assignments_in_groups(self) -> bool:
        return all(audit.assignment_in_group for audit in self.factor_audits)

    @property
    def all_expressions_match_endpoints(self) -> bool:
        return all(audit.expression_matches_endpoint for audit in self.factor_audits)

    @property
    def product_endpoint_lies_in_product_longitude_subgroup_by_expression(self) -> bool:
        return (
            self.all_endpoints_in_groups
            and self.all_assignments_in_groups
            and self.all_expressions_match_endpoints
            and self.product_witness_matches_endpoint
        )

    @property
    def identity_product_longitude_signature_by_factors(self) -> bool:
        return all(audit.identity_longitude_signature for audit in self.factor_audits)

    @property
    def identity_longitudes_kill_product_endpoint_by_expression(self) -> bool:
        if not self.product_endpoint_lies_in_product_longitude_subgroup_by_expression:
            return False
        if not self.identity_product_longitude_signature_by_factors:
            return True
        return self.product_endpoint == tuple(
            audit.group_identity for audit in self.factor_audits
        )

    @property
    def proves_product_endpoint_detector_by_expression(self) -> bool:
        return self.product_endpoint_lies_in_product_longitude_subgroup_by_expression


@dataclass(frozen=True)
class EndpointCoordinateReadoutAudit:
    """One residual coordinate readout controlled by endpoint expressions."""

    endpoint_audit: EndpointProductExpressionAudit
    input_coordinate: object
    output_coordinate: object

    @property
    def endpoint_tuple_is_identity(self) -> bool:
        return self.endpoint_audit.product_endpoint == tuple(
            audit.group_identity for audit in self.endpoint_audit.factor_audits
        )

    @property
    def coordinate_fixed(self) -> bool:
        return self.output_coordinate == self.input_coordinate

    @property
    def identity_endpoints_fix_coordinate(self) -> bool:
        return (not self.endpoint_tuple_is_identity) or self.coordinate_fixed

    @property
    def identity_longitudes_kill_coordinate_by_expression(self) -> bool:
        audit = self.endpoint_audit
        if not audit.product_endpoint_lies_in_product_longitude_subgroup_by_expression:
            return False
        if not audit.identity_product_longitude_signature_by_factors:
            return True
        return self.endpoint_tuple_is_identity and self.coordinate_fixed


@dataclass(frozen=True)
class EndpointResidualReadoutAudit:
    """Bundle coordinate readout rows for one residual tuple."""

    coordinate_audits: Tuple[EndpointCoordinateReadoutAudit, ...]

    @property
    def input_tuple(self) -> Tuple[object, ...]:
        return tuple(audit.input_coordinate for audit in self.coordinate_audits)

    @property
    def output_tuple(self) -> Tuple[object, ...]:
        return tuple(audit.output_coordinate for audit in self.coordinate_audits)

    @property
    def residual_tuple_fixed(self) -> bool:
        return self.output_tuple == self.input_tuple

    @property
    def identity_endpoints_fix_all_coordinates(self) -> bool:
        return all(
            audit.identity_endpoints_fix_coordinate
            for audit in self.coordinate_audits
        )

    @property
    def identity_longitudes_kill_residual_tuple_by_expression(self) -> bool:
        return all(
            audit.identity_longitudes_kill_coordinate_by_expression
            for audit in self.coordinate_audits
        )


def endpoint_longitude_expression_audit(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    endpoint: GroupElement,
    assignment: Sequence[GroupElement],
    expression: Sequence[Tuple[int, int]],
) -> EndpointLongitudeExpressionAudit:
    """Verify that one endpoint is a word in recursive longitude values.

    This is the finite-group version of the endpoint expression certificate in
    ``proofs/bifree_corridor_endpoint_factorization.md``.  A successful audit
    proves endpoint membership in ``V_beta(G)`` without enumerating that
    subgroup.
    """

    assignment_tuple = tuple(assignment)
    expression_tuple = tuple(expression)
    elements = set(group.elements)
    endpoint_in_group = endpoint in elements
    assignment_in_group = (
        len(assignment_tuple) == n
        and all(value in elements for value in assignment_tuple)
    )
    expression_value = None
    if assignment_in_group:
        expression_value = evaluate_longitude_expression(
            group,
            assignment_tuple,
            braid_word,
            expression_tuple,
        )
    data = artin_longitudes(n, braid_word)
    return EndpointLongitudeExpressionAudit(
        artin_permutation=data.permutation,
        group_order=len(group.elements),
        endpoint=endpoint,
        endpoint_in_group=endpoint_in_group,
        assignment=assignment_tuple,
        assignment_in_group=assignment_in_group,
        expression=expression_tuple,
        expression_value=expression_value,
        expression_matches_endpoint=(
            expression_value is not None
            and endpoint_in_group
            and expression_value == endpoint
        ),
        identity_longitude_signature=has_identity_longitude_signature(
            group,
            n,
            braid_word,
        ),
        group_identity=group.identity,
    )


def endpoint_product_longitude_expression_audit(
    groups: Sequence[FiniteGroup],
    n: int,
    braid_word: BraidWord,
    endpoints: Sequence[GroupElement],
    assignments: Sequence[Sequence[GroupElement]],
    expressions: Sequence[Sequence[Tuple[int, int]]],
) -> EndpointProductExpressionAudit:
    """Assemble endpoint expression certificates in one fixed product group."""

    group_tuple = tuple(groups)
    endpoint_tuple = tuple(endpoints)
    assignment_tuple = tuple(tuple(assignment) for assignment in assignments)
    expression_tuple = tuple(tuple(expression) for expression in expressions)
    if not (
        len(group_tuple)
        == len(endpoint_tuple)
        == len(assignment_tuple)
        == len(expression_tuple)
    ):
        raise ValueError(
            "need one endpoint, assignment, and expression for each group"
        )
    factor_audits = tuple(
        endpoint_longitude_expression_audit(
            group,
            n,
            braid_word,
            endpoint,
            assignment,
            expression,
        )
        for group, endpoint, assignment, expression in zip(
            group_tuple,
            endpoint_tuple,
            assignment_tuple,
            expression_tuple,
        )
    )
    product_order = 1
    for group in group_tuple:
        product_order *= len(group.elements)
    product_witness = None
    product_witness_value = None
    if all(audit.assignment_in_group for audit in factor_audits):
        factor_witnesses = tuple(
            tuple(
                (audit.assignment, longitude_index, exponent)
                for longitude_index, exponent in audit.expression
            )
            for audit in factor_audits
        )
        product_witness = direct_product_longitude_subgroup_witness(
            group_tuple,
            n,
            factor_witnesses,
        )
        product_witness_value = evaluate_longitude_subgroup_witness(
            direct_product_group(group_tuple),
            n,
            braid_word,
            product_witness,
        )
    return EndpointProductExpressionAudit(
        factor_audits=factor_audits,
        product_endpoint=endpoint_tuple,
        group_orders=tuple(len(group.elements) for group in group_tuple),
        product_group_order=product_order,
        product_witness=product_witness,
        product_witness_value=product_witness_value,
        product_witness_matches_endpoint=product_witness_value == endpoint_tuple,
    )


def endpoint_coordinate_readout_audit(
    endpoint_audit: EndpointProductExpressionAudit,
    input_coordinate: object,
    output_coordinate: object,
) -> EndpointCoordinateReadoutAudit:
    """Audit the faithful-readout implication for one residual coordinate."""

    return EndpointCoordinateReadoutAudit(
        endpoint_audit=endpoint_audit,
        input_coordinate=input_coordinate,
        output_coordinate=output_coordinate,
    )


def endpoint_residual_readout_audit(
    coordinate_audits: Sequence[EndpointCoordinateReadoutAudit],
) -> EndpointResidualReadoutAudit:
    """Bundle endpoint-controlled coordinates into one residual-tuple audit."""

    return EndpointResidualReadoutAudit(coordinate_audits=tuple(coordinate_audits))
