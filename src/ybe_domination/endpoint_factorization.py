from __future__ import annotations

from dataclasses import dataclass
from typing import Sequence, Tuple

from .artin_longitudes import (
    BraidWord,
    FreeWord,
    LongitudeExpression,
    LongitudeSubgroupWitness,
    artin_permutation_defect_longitude_witness,
    artin_longitudes,
    direct_product_longitude_subgroup_witness,
    evaluate_artin_permutation_defect,
    evaluate_longitude_expression,
    evaluate_longitude_subgroup_witness,
    has_identity_longitude_signature,
    invert_longitude_subgroup_witness,
)
from .finite_group import FiniteGroup, GroupElement, direct_product_group

ArtinDefectEndpointTerm = Tuple[Tuple[GroupElement, ...], FreeWord, int]


@dataclass(frozen=True)
class EndpointLongitudeExpressionAudit:
    """Expression certificate for one endpoint in a fixed finite group."""

    n: int
    braid_word: Tuple[int, ...]
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

    n: int
    braid_word: Tuple[int, ...]
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
class EndpointArtinDefectAudit:
    """Endpoint certificate using Artin permutation defect values."""

    n: int
    braid_word: Tuple[int, ...]
    artin_permutation: Tuple[int, ...]
    group_order: int
    endpoint: GroupElement
    endpoint_in_group: bool
    terms: Tuple[ArtinDefectEndpointTerm, ...]
    assignments_in_group: bool
    defect_values: Tuple[GroupElement, ...]
    defect_product_value: GroupElement | None
    defect_product_matches_endpoint: bool
    longitude_witness: LongitudeSubgroupWitness | None
    longitude_witness_value: GroupElement | None
    longitude_witness_matches_defect_product: bool
    identity_longitude_signature: bool
    group_identity: GroupElement

    @property
    def endpoint_is_identity(self) -> bool:
        return self.endpoint == self.group_identity

    @property
    def endpoint_lies_in_longitude_subgroup_by_artin_defects(self) -> bool:
        return (
            self.endpoint_in_group
            and self.assignments_in_group
            and self.defect_product_matches_endpoint
            and self.longitude_witness_matches_defect_product
        )

    @property
    def identity_longitudes_kill_endpoint_by_artin_defects(self) -> bool:
        if not self.endpoint_lies_in_longitude_subgroup_by_artin_defects:
            return False
        if not self.identity_longitude_signature:
            return True
        return self.endpoint_is_identity


@dataclass(frozen=True)
class EndpointProductArtinDefectAudit:
    """Assemble Artin-defect endpoint certificates into one product detector."""

    n: int
    braid_word: Tuple[int, ...]
    factor_audits: Tuple[EndpointArtinDefectAudit, ...]
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
        return all(audit.assignments_in_group for audit in self.factor_audits)

    @property
    def all_defect_products_match_endpoints(self) -> bool:
        return all(audit.defect_product_matches_endpoint for audit in self.factor_audits)

    @property
    def product_endpoint_lies_in_product_longitude_subgroup_by_artin_defects(self) -> bool:
        return (
            self.all_endpoints_in_groups
            and self.all_assignments_in_groups
            and self.all_defect_products_match_endpoints
            and self.product_witness_matches_endpoint
        )

    @property
    def identity_product_longitude_signature_by_factors(self) -> bool:
        return all(audit.identity_longitude_signature for audit in self.factor_audits)

    @property
    def identity_longitudes_kill_product_endpoint_by_artin_defects(self) -> bool:
        if not self.product_endpoint_lies_in_product_longitude_subgroup_by_artin_defects:
            return False
        if not self.identity_product_longitude_signature_by_factors:
            return True
        return self.product_endpoint == tuple(
            audit.group_identity for audit in self.factor_audits
        )

    @property
    def proves_product_endpoint_detector_by_artin_defects(self) -> bool:
        return self.product_endpoint_lies_in_product_longitude_subgroup_by_artin_defects


@dataclass(frozen=True)
class EndpointArtinDefectCoordinateReadoutAudit:
    """One residual coordinate readout controlled by Artin-defect endpoints."""

    endpoint_audit: EndpointProductArtinDefectAudit
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
    def identity_longitudes_kill_coordinate_by_artin_defects(self) -> bool:
        audit = self.endpoint_audit
        if not audit.product_endpoint_lies_in_product_longitude_subgroup_by_artin_defects:
            return False
        if not audit.identity_product_longitude_signature_by_factors:
            return True
        return self.endpoint_tuple_is_identity and self.coordinate_fixed


@dataclass(frozen=True)
class EndpointArtinDefectResidualReadoutAudit:
    """Bundle Artin-defect coordinate readout rows for one residual tuple."""

    coordinate_audits: Tuple[EndpointArtinDefectCoordinateReadoutAudit, ...]

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
    def identity_longitudes_kill_residual_tuple_by_artin_defects(self) -> bool:
        return all(
            audit.identity_longitudes_kill_coordinate_by_artin_defects
            for audit in self.coordinate_audits
        )


@dataclass(frozen=True)
class EndpointArtinDefectResidualActionAudit:
    """Supplied-row residual action audit controlled by Artin defects."""

    n: int
    braid_word: Tuple[int, ...]
    residual_readouts: Tuple[EndpointArtinDefectResidualReadoutAudit, ...]
    expected_row_count: int | None = None

    @property
    def row_count(self) -> int:
        return len(self.residual_readouts)

    @property
    def covers_expected_rows(self) -> bool:
        return self.expected_row_count is None or self.row_count == self.expected_row_count

    @property
    def braid_data_consistent(self) -> bool:
        for readout in self.residual_readouts:
            for coordinate in readout.coordinate_audits:
                endpoint = coordinate.endpoint_audit
                if endpoint.n != self.n or endpoint.braid_word != self.braid_word:
                    return False
        return True

    @property
    def all_identity_endpoints_fix_rows(self) -> bool:
        return all(
            readout.identity_endpoints_fix_all_coordinates
            for readout in self.residual_readouts
        )

    @property
    def all_identity_longitudes_kill_rows_by_artin_defects(self) -> bool:
        return all(
            readout.identity_longitudes_kill_residual_tuple_by_artin_defects
            for readout in self.residual_readouts
        )

    @property
    def residual_action_identity_on_supplied_rows(self) -> bool:
        return all(readout.residual_tuple_fixed for readout in self.residual_readouts)

    @property
    def proves_supplied_rows_detector_implication(self) -> bool:
        return (
            self.braid_data_consistent
            and self.all_identity_longitudes_kill_rows_by_artin_defects
        )

    @property
    def proves_complete_residual_action_implication(self) -> bool:
        return self.proves_supplied_rows_detector_implication and self.covers_expected_rows


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


@dataclass(frozen=True)
class EndpointResidualActionAudit:
    """Supplied-row audit for a residual action controlled by endpoints."""

    n: int
    braid_word: Tuple[int, ...]
    residual_readouts: Tuple[EndpointResidualReadoutAudit, ...]
    expected_row_count: int | None = None

    @property
    def row_count(self) -> int:
        return len(self.residual_readouts)

    @property
    def covers_expected_rows(self) -> bool:
        return self.expected_row_count is None or self.row_count == self.expected_row_count

    @property
    def braid_data_consistent(self) -> bool:
        for readout in self.residual_readouts:
            for coordinate in readout.coordinate_audits:
                endpoint = coordinate.endpoint_audit
                if endpoint.n != self.n or endpoint.braid_word != self.braid_word:
                    return False
        return True

    @property
    def all_identity_endpoints_fix_rows(self) -> bool:
        return all(
            readout.identity_endpoints_fix_all_coordinates
            for readout in self.residual_readouts
        )

    @property
    def all_identity_longitudes_kill_rows_by_expression(self) -> bool:
        return all(
            readout.identity_longitudes_kill_residual_tuple_by_expression
            for readout in self.residual_readouts
        )

    @property
    def residual_action_identity_on_supplied_rows(self) -> bool:
        return all(readout.residual_tuple_fixed for readout in self.residual_readouts)

    @property
    def proves_supplied_rows_detector_implication(self) -> bool:
        return (
            self.braid_data_consistent
            and self.all_identity_longitudes_kill_rows_by_expression
        )

    @property
    def proves_complete_residual_action_implication(self) -> bool:
        return self.proves_supplied_rows_detector_implication and self.covers_expected_rows


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
        n=n,
        braid_word=tuple(braid_word),
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
        n=n,
        braid_word=tuple(braid_word),
        factor_audits=factor_audits,
        product_endpoint=endpoint_tuple,
        group_orders=tuple(len(group.elements) for group in group_tuple),
        product_group_order=product_order,
        product_witness=product_witness,
        product_witness_value=product_witness_value,
        product_witness_matches_endpoint=product_witness_value == endpoint_tuple,
    )


def endpoint_artin_defect_audit(
    group: FiniteGroup,
    n: int,
    braid_word: BraidWord,
    endpoint: GroupElement,
    terms: Sequence[Tuple[Sequence[GroupElement], FreeWord, int]],
) -> EndpointArtinDefectAudit:
    """Verify that an endpoint is a product of Artin permutation defects.

    Each term is ``(assignment, word, exponent)`` and represents
    ``phi(beta(word) * p_beta(word)^-1)^exponent``.  The audit also converts
    the supplied defect display into a literal ``V_beta(G)`` witness using the
    Artin-defect normal-closure criterion.
    """

    term_tuple: Tuple[ArtinDefectEndpointTerm, ...] = tuple(
        (tuple(assignment), tuple(word), exponent)
        for assignment, word, exponent in terms
    )
    for _assignment, _word, exponent in term_tuple:
        if exponent not in (-1, 1):
            raise ValueError("Artin-defect endpoint exponents must be +/-1")
    elements = set(group.elements)
    endpoint_in_group = endpoint in elements
    assignments_in_group = all(
        len(assignment) == n and all(value in elements for value in assignment)
        for assignment, _word, _exponent in term_tuple
    )
    defect_values: Tuple[GroupElement, ...] = tuple()
    defect_product_value = None
    longitude_witness = None
    longitude_witness_value = None
    longitude_witness_matches_defect_product = False
    if assignments_in_group:
        values = []
        witness_rows = []
        product_value = group.identity
        for assignment, word, exponent in term_tuple:
            value = evaluate_artin_permutation_defect(
                group,
                assignment,
                n,
                braid_word,
                word,
            )
            witness = artin_permutation_defect_longitude_witness(
                group,
                n,
                braid_word,
                assignment,
                word,
            )
            if exponent < 0:
                value = group.inv(value)
                witness = invert_longitude_subgroup_witness(witness)
            values.append(value)
            witness_rows.extend(witness)
            product_value = group.mul(product_value, value)
        defect_values = tuple(values)
        defect_product_value = product_value
        longitude_witness = tuple(witness_rows)
        longitude_witness_value = evaluate_longitude_subgroup_witness(
            group,
            n,
            braid_word,
            longitude_witness,
        )
        longitude_witness_matches_defect_product = (
            longitude_witness_value == defect_product_value
        )
    data = artin_longitudes(n, braid_word)
    return EndpointArtinDefectAudit(
        n=n,
        braid_word=tuple(braid_word),
        artin_permutation=data.permutation,
        group_order=len(group.elements),
        endpoint=endpoint,
        endpoint_in_group=endpoint_in_group,
        terms=term_tuple,
        assignments_in_group=assignments_in_group,
        defect_values=defect_values,
        defect_product_value=defect_product_value,
        defect_product_matches_endpoint=(
            endpoint_in_group
            and defect_product_value is not None
            and defect_product_value == endpoint
        ),
        longitude_witness=longitude_witness,
        longitude_witness_value=longitude_witness_value,
        longitude_witness_matches_defect_product=longitude_witness_matches_defect_product,
        identity_longitude_signature=has_identity_longitude_signature(
            group,
            n,
            braid_word,
        ),
        group_identity=group.identity,
    )


def endpoint_product_artin_defect_audit(
    groups: Sequence[FiniteGroup],
    n: int,
    braid_word: BraidWord,
    endpoints: Sequence[GroupElement],
    terms_by_factor: Sequence[Sequence[Tuple[Sequence[GroupElement], FreeWord, int]]],
) -> EndpointProductArtinDefectAudit:
    """Assemble Artin-defect endpoint certificates in one product group."""

    group_tuple = tuple(groups)
    endpoint_tuple = tuple(endpoints)
    terms_tuple = tuple(tuple(terms) for terms in terms_by_factor)
    if not (len(group_tuple) == len(endpoint_tuple) == len(terms_tuple)):
        raise ValueError("need one endpoint and Artin-defect term list for each group")
    factor_audits = tuple(
        endpoint_artin_defect_audit(
            group,
            n,
            braid_word,
            endpoint,
            terms,
        )
        for group, endpoint, terms in zip(group_tuple, endpoint_tuple, terms_tuple)
    )
    product_order = 1
    for group in group_tuple:
        product_order *= len(group.elements)
    product_witness = None
    product_witness_value = None
    if all(audit.longitude_witness is not None for audit in factor_audits):
        product_witness = direct_product_longitude_subgroup_witness(
            group_tuple,
            n,
            tuple(audit.longitude_witness or tuple() for audit in factor_audits),
        )
        product_witness_value = evaluate_longitude_subgroup_witness(
            direct_product_group(group_tuple),
            n,
            braid_word,
            product_witness,
        )
    return EndpointProductArtinDefectAudit(
        n=n,
        braid_word=tuple(braid_word),
        factor_audits=factor_audits,
        product_endpoint=endpoint_tuple,
        group_orders=tuple(len(group.elements) for group in group_tuple),
        product_group_order=product_order,
        product_witness=product_witness,
        product_witness_value=product_witness_value,
        product_witness_matches_endpoint=product_witness_value == endpoint_tuple,
    )


def endpoint_artin_defect_coordinate_readout_audit(
    endpoint_audit: EndpointProductArtinDefectAudit,
    input_coordinate: object,
    output_coordinate: object,
) -> EndpointArtinDefectCoordinateReadoutAudit:
    """Audit the faithful-readout implication for one Artin-defect row."""

    return EndpointArtinDefectCoordinateReadoutAudit(
        endpoint_audit=endpoint_audit,
        input_coordinate=input_coordinate,
        output_coordinate=output_coordinate,
    )


def endpoint_artin_defect_residual_readout_audit(
    coordinate_audits: Sequence[EndpointArtinDefectCoordinateReadoutAudit],
) -> EndpointArtinDefectResidualReadoutAudit:
    """Bundle Artin-defect coordinates into one residual-tuple audit."""

    return EndpointArtinDefectResidualReadoutAudit(
        coordinate_audits=tuple(coordinate_audits)
    )


def endpoint_artin_defect_residual_action_audit(
    n: int,
    braid_word: BraidWord,
    residual_readouts: Sequence[EndpointArtinDefectResidualReadoutAudit],
    *,
    expected_row_count: int | None = None,
) -> EndpointArtinDefectResidualActionAudit:
    """Bundle supplied residual rows for the Artin-defect implication."""

    if expected_row_count is not None and expected_row_count < 0:
        raise ValueError("expected row count must be nonnegative")
    return EndpointArtinDefectResidualActionAudit(
        n=n,
        braid_word=tuple(braid_word),
        residual_readouts=tuple(residual_readouts),
        expected_row_count=expected_row_count,
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


def endpoint_residual_action_audit(
    n: int,
    braid_word: BraidWord,
    residual_readouts: Sequence[EndpointResidualReadoutAudit],
    *,
    expected_row_count: int | None = None,
) -> EndpointResidualActionAudit:
    """Bundle supplied residual rows for the endpoint detector implication."""

    if expected_row_count is not None and expected_row_count < 0:
        raise ValueError("expected row count must be nonnegative")
    return EndpointResidualActionAudit(
        n=n,
        braid_word=tuple(braid_word),
        residual_readouts=tuple(residual_readouts),
        expected_row_count=expected_row_count,
    )
