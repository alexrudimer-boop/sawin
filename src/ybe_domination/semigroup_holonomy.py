from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Sequence, Tuple

from .artin_longitudes import (
    BraidWord,
    artin_longitudes,
    direct_product_longitude_subgroup_audit,
    direct_product_longitude_subgroup_witness,
    evaluate_longitude_expression,
    evaluate_longitude_subgroup_witness,
    evaluate_free_word,
    has_identity_longitude_signature,
    longitude_value_subgroup_elements,
)
from .finite_group import (
    FiniteGroup,
    direct_product_group,
    permutation_group_from_generators,
    subgroup_generated_elements,
)
from .green_branch import (
    Transformation,
    TransformationMonoid,
    compose_transformations,
    identity_transformation,
)

ProductUnitGroupElement = Tuple[Transformation, ...]
ProductLongitudeWitnessLetter = Tuple[Tuple[ProductUnitGroupElement, ...], int, int]
ProductLongitudeWitness = Tuple[ProductLongitudeWitnessLetter, ...]


@dataclass(frozen=True)
class AperiodicPermutationAudit:
    is_aperiodic: bool
    permutation_count: int
    nonidentity_permutation_count: int
    nonidentity_permutations: Tuple[Transformation, ...]


@dataclass(frozen=True)
class UnitLongitudeSubgroupAudit:
    """Check finite-longitude visibility for unit labels in a transition monoid."""

    artin_permutation: Tuple[int, ...]
    unit_group_order: int
    longitude_subgroup_size: int
    label_count: int
    nonunit_labels: Tuple[Transformation, ...]
    labels_outside_longitude_subgroup: Tuple[Transformation, ...]

    @property
    def labels_are_units(self) -> bool:
        return not self.nonunit_labels

    @property
    def labels_lie_in_longitude_subgroup(self) -> bool:
        return not self.nonunit_labels and not self.labels_outside_longitude_subgroup


@dataclass(frozen=True)
class UnitFactorizationAudit:
    """Check whether a transformation product can be a residual permutation."""

    degree: int
    factor_count: int
    composite: Transformation
    composite_is_unit: bool
    all_factors_are_units: bool
    nonunit_factor_indices: Tuple[int, ...]
    nonunit_factors: Tuple[Transformation, ...]

    @property
    def permutation_composite_forces_unit_factors(self) -> bool:
        return not self.composite_is_unit or self.all_factors_are_units


@dataclass(frozen=True)
class UnitSectionDetectionAudit:
    """Audit a proposed unit-section factorization against finite longitudes."""

    monoid_element_count: int
    factors_in_monoid: bool
    factorization: UnitFactorizationAudit
    longitude: UnitLongitudeSubgroupAudit
    monoid_identity: Transformation

    @property
    def is_permutation_branch(self) -> bool:
        return self.factorization.composite_is_unit

    @property
    def factors_are_unit_sections(self) -> bool:
        return (
            self.factors_in_monoid
            and self.factorization.all_factors_are_units
            and self.longitude.labels_are_units
        )

    @property
    def factors_lie_in_longitude_subgroup(self) -> bool:
        return self.factors_are_unit_sections and self.longitude.labels_lie_in_longitude_subgroup

    @property
    def identity_longitude_signature(self) -> bool:
        return (
            self.longitude.artin_permutation
            == tuple(range(len(self.longitude.artin_permutation)))
            and self.longitude.longitude_subgroup_size == 1
        )

    @property
    def composite_is_identity(self) -> bool:
        return self.factorization.composite == self.monoid_identity

    @property
    def identity_longitudes_kill_branch(self) -> bool:
        """Return the fixed-word implication supplied by the criterion."""

        if not self.is_permutation_branch:
            return False
        if not self.factors_lie_in_longitude_subgroup:
            return False
        if not self.identity_longitude_signature:
            return True
        return self.composite_is_identity


@dataclass(frozen=True)
class UnitCompositeDetectionAudit:
    """Audit a residual unit composite against a finite longitude subgroup."""

    monoid_element_count: int
    factors_in_monoid: bool
    factorization: UnitFactorizationAudit
    longitude: UnitLongitudeSubgroupAudit
    monoid_identity: Transformation

    @property
    def is_permutation_branch(self) -> bool:
        return self.factorization.composite_is_unit

    @property
    def composite_lies_in_longitude_subgroup(self) -> bool:
        return (
            self.factors_in_monoid
            and self.factorization.composite_is_unit
            and self.longitude.labels_lie_in_longitude_subgroup
        )

    @property
    def identity_longitude_signature(self) -> bool:
        return (
            self.longitude.artin_permutation
            == tuple(range(len(self.longitude.artin_permutation)))
            and self.longitude.longitude_subgroup_size == 1
        )

    @property
    def composite_is_identity(self) -> bool:
        return self.factorization.composite == self.monoid_identity

    @property
    def identity_longitudes_kill_composite(self) -> bool:
        if not self.composite_lies_in_longitude_subgroup:
            return False
        if not self.identity_longitude_signature:
            return True
        return self.composite_is_identity

    @property
    def is_finite_unit_detector_failure(self) -> bool:
        """Return whether this word defeats this one unit detector."""

        return (
            self.is_permutation_branch
            and self.identity_longitude_signature
            and not self.composite_is_identity
        )


@dataclass(frozen=True)
class UnitCompositeLongitudeRouteAudit:
    """Compare endpoint-unit detection routes for one braid word."""

    monoid_element_count: int
    factors_in_monoid: bool
    factorization: UnitFactorizationAudit
    artin_permutation: Tuple[int, ...]
    unit_group_order: int
    longitude_generator_count: int
    longitude_subgroup_size: int
    composite_lies_in_longitude_subgroup: bool
    has_single_longitude_witness: bool
    witness_longitude_index: int | None
    witness_assignment: Tuple[Transformation, ...] | None
    monoid_identity: Transformation

    @property
    def is_permutation_branch(self) -> bool:
        return self.factorization.composite_is_unit

    @property
    def composite_is_identity(self) -> bool:
        return self.factorization.composite == self.monoid_identity

    @property
    def identity_longitude_signature(self) -> bool:
        return (
            self.artin_permutation == tuple(range(len(self.artin_permutation)))
            and self.longitude_subgroup_size == 1
        )

    @property
    def identity_longitudes_kill_composite(self) -> bool:
        if not self.composite_lies_in_longitude_subgroup:
            return False
        if not self.identity_longitude_signature:
            return True
        return self.composite_is_identity

    @property
    def is_finite_unit_detector_failure(self) -> bool:
        return (
            self.is_permutation_branch
            and self.identity_longitude_signature
            and not self.composite_is_identity
        )


@dataclass(frozen=True)
class UnitCompositeLongitudeExpressionAudit:
    """Explicit expression certificate for one residual endpoint unit."""

    monoid_element_count: int
    factors_in_monoid: bool
    factorization: UnitFactorizationAudit
    artin_permutation: Tuple[int, ...]
    unit_group_order: int
    assignment: Tuple[Transformation, ...]
    assignment_in_unit_group: bool
    expression: Tuple[Tuple[int, int], ...]
    expression_value: Transformation | None
    expression_matches_composite: bool
    identity_longitude_signature: bool
    monoid_identity: Transformation

    @property
    def is_permutation_branch(self) -> bool:
        return self.factorization.composite_is_unit

    @property
    def composite_is_identity(self) -> bool:
        return self.factorization.composite == self.monoid_identity

    @property
    def composite_lies_in_longitude_subgroup_by_expression(self) -> bool:
        return (
            self.factors_in_monoid
            and self.is_permutation_branch
            and self.assignment_in_unit_group
            and self.expression_matches_composite
        )

    @property
    def identity_longitudes_kill_composite_by_expression(self) -> bool:
        if not self.composite_lies_in_longitude_subgroup_by_expression:
            return False
        if not self.identity_longitude_signature:
            return True
        return self.composite_is_identity


@dataclass(frozen=True)
class UnitSectionProductDetectionAudit:
    """Combine several unit-section branches into one product detector."""

    factor_audits: Tuple[UnitSectionDetectionAudit, ...]
    unit_group_orders: Tuple[int, ...]
    product_group_order: int
    truncated: bool
    product_subgroup_size: int | None
    expected_product_subgroup_size: int | None
    product_subgroup_equals_factor_product: bool | None

    @property
    def all_factor_words_in_monoids(self) -> bool:
        return all(audit.factors_in_monoid for audit in self.factor_audits)

    @property
    def all_permutation_branches(self) -> bool:
        return all(audit.is_permutation_branch for audit in self.factor_audits)

    @property
    def all_factors_lie_in_longitude_subgroups(self) -> bool:
        return all(
            audit.factors_lie_in_longitude_subgroup
            for audit in self.factor_audits
        )

    @property
    def all_identity_longitudes_kill_branches(self) -> bool:
        return all(
            audit.identity_longitudes_kill_branch
            for audit in self.factor_audits
        )

    @property
    def proves_single_product_detector_when_enumerated(self) -> bool:
        if self.truncated:
            return False
        return bool(self.product_subgroup_equals_factor_product)


@dataclass(frozen=True)
class UnitCompositeProductDetectionAudit:
    """Combine several endpoint-unit branches into one product detector."""

    factor_audits: Tuple[UnitCompositeDetectionAudit, ...]
    product_endpoint: Tuple[Transformation, ...]
    unit_group_orders: Tuple[int, ...]
    product_group_order: int
    truncated: bool
    product_subgroup_size: int | None
    expected_product_subgroup_size: int | None
    product_subgroup_equals_factor_product: bool | None
    product_endpoint_in_product_subgroup: bool | None

    @property
    def all_factor_words_in_monoids(self) -> bool:
        return all(audit.factors_in_monoid for audit in self.factor_audits)

    @property
    def all_permutation_branches(self) -> bool:
        return all(audit.is_permutation_branch for audit in self.factor_audits)

    @property
    def all_composites_lie_in_longitude_subgroups(self) -> bool:
        return all(
            audit.composite_lies_in_longitude_subgroup
            for audit in self.factor_audits
        )

    @property
    def all_identity_longitudes_kill_composites(self) -> bool:
        return all(
            audit.identity_longitudes_kill_composite
            for audit in self.factor_audits
        )

    @property
    def proves_single_product_detector_when_enumerated(self) -> bool:
        if self.truncated:
            return False
        return bool(
            self.product_subgroup_equals_factor_product
            and self.product_endpoint_in_product_subgroup
        )

    @property
    def identity_product_longitude_signature(self) -> bool:
        """Return whether the fixed product detector sees identity data."""

        return all(
            audit.identity_longitude_signature for audit in self.factor_audits
        )

    @property
    def product_endpoint_lies_in_product_longitude_subgroup(self) -> bool:
        """Return the direct product-endpoint membership check.

        This is the endpoint criterion in the single detector group
        ``prod_i U(M_i)``.  It is intentionally separate from the factorwise
        booleans: the sharp obstruction theorem uses one finite product group,
        and the endpoint tuple itself must lie in that product group's
        longitude-value subgroup.
        """

        return self.product_endpoint_in_product_subgroup is True

    @property
    def identity_longitudes_kill_product_endpoint(self) -> bool:
        """Return the fixed-word implication for the product endpoint."""

        if not self.product_endpoint_lies_in_product_longitude_subgroup:
            return False
        if not self.identity_product_longitude_signature:
            return True
        return self.product_endpoint == tuple(
            audit.monoid_identity for audit in self.factor_audits
        )

    @property
    def proves_product_endpoint_detector_when_enumerated(self) -> bool:
        """Return whether enumeration proves the product endpoint criterion."""

        return (not self.truncated) and self.product_endpoint_lies_in_product_longitude_subgroup

    @property
    def is_finite_product_unit_detector_failure(self) -> bool:
        """Return whether the endpoint defeats the listed product detector."""

        return (
            not self.truncated
            and all(audit.identity_longitude_signature for audit in self.factor_audits)
            and all(audit.is_permutation_branch for audit in self.factor_audits)
            and self.product_endpoint
            != tuple(audit.monoid_identity for audit in self.factor_audits)
        )


@dataclass(frozen=True)
class UnitCompositeProductExpressionAudit:
    """Combine endpoint longitude-expression certificates into one product."""

    factor_audits: Tuple[UnitCompositeLongitudeExpressionAudit, ...]
    product_endpoint: Tuple[Transformation, ...]
    unit_group_orders: Tuple[int, ...]
    product_group_order: int
    product_witness: ProductLongitudeWitness | None
    product_witness_value: ProductUnitGroupElement | None
    product_witness_matches_endpoint: bool

    @property
    def all_factor_words_in_monoids(self) -> bool:
        return all(audit.factors_in_monoid for audit in self.factor_audits)

    @property
    def all_permutation_branches(self) -> bool:
        return all(audit.is_permutation_branch for audit in self.factor_audits)

    @property
    def all_assignments_in_unit_groups(self) -> bool:
        return all(audit.assignment_in_unit_group for audit in self.factor_audits)

    @property
    def all_expressions_match_composites(self) -> bool:
        return all(
            audit.expression_matches_composite for audit in self.factor_audits
        )

    @property
    def product_endpoint_lies_in_product_longitude_subgroup_by_expression(self) -> bool:
        """Return whether expressions certify product-subgroup membership."""

        return (
            self.all_factor_words_in_monoids
            and self.all_permutation_branches
            and self.all_assignments_in_unit_groups
            and self.all_expressions_match_composites
            and self.product_witness_matches_endpoint
        )

    @property
    def identity_product_longitude_signature(self) -> bool:
        return all(
            audit.identity_longitude_signature for audit in self.factor_audits
        )

    @property
    def identity_longitudes_kill_product_endpoint_by_expression(self) -> bool:
        if not self.product_endpoint_lies_in_product_longitude_subgroup_by_expression:
            return False
        if not self.identity_product_longitude_signature:
            return True
        return self.product_endpoint == tuple(
            audit.monoid_identity for audit in self.factor_audits
        )

    @property
    def proves_product_endpoint_detector_by_expression(self) -> bool:
        return self.product_endpoint_lies_in_product_longitude_subgroup_by_expression


def is_permutation_transformation(element: Transformation) -> bool:
    """Return whether a finite transformation is a permutation."""

    return set(element) == set(range(len(element)))


def compose_transformation_word(
    factors: Sequence[Transformation],
    *,
    degree: int | None = None,
) -> Transformation:
    """Compose a finite word of transformations in the listed order."""

    factor_tuple = tuple(factors)
    if factor_tuple:
        degree = len(factor_tuple[0])
    elif degree is None:
        raise ValueError("empty transformation words need an explicit degree")
    out = identity_transformation(degree)
    for factor in factor_tuple:
        if len(factor) != degree:
            raise ValueError("all transformations must have the same degree")
        out = compose_transformations(factor, out)
    return out


def unit_factorization_audit(
    factors: Sequence[Transformation],
    *,
    degree: int | None = None,
) -> UnitFactorizationAudit:
    """Audit the gate: a permutation composite has only permutation factors.

    For total self-maps of a finite set, if ``f_k ... f_1`` is bijective, then
    each factor ``f_i`` is bijective.  Thus a residual branch represented as a
    product containing a nonunit transformation cannot later become a genuine
    residual permutation.
    """

    factor_tuple = tuple(factors)
    composite = compose_transformation_word(factor_tuple, degree=degree)
    if factor_tuple:
        degree = len(factor_tuple[0])
    elif degree is None:
        degree = len(composite)
    nonunit_rows = tuple(
        (index, factor)
        for index, factor in enumerate(factor_tuple)
        if not is_permutation_transformation(factor)
    )
    return UnitFactorizationAudit(
        degree=degree,
        factor_count=len(factor_tuple),
        composite=composite,
        composite_is_unit=is_permutation_transformation(composite),
        all_factors_are_units=not nonunit_rows,
        nonunit_factor_indices=tuple(index for index, _factor in nonunit_rows),
        nonunit_factors=tuple(factor for _index, factor in nonunit_rows),
    )


def transformation_power(element: Transformation, exponent: int) -> Transformation:
    """Return a power of a transformation under composition."""

    if exponent < 0:
        raise ValueError("transformation powers must be nonnegative")
    out = identity_transformation(len(element))
    for _ in range(exponent):
        out = compose_transformations(element, out)
    return out


def is_aperiodic_element(element: Transformation, max_power: int | None = None) -> bool:
    """Return whether the generated monogenic semigroup is aperiodic.

    For a finite transformation of degree `d`, checking `k <= d!` would be
    enough but wasteful.  The orbit of powers has at most `d^d` states, so this
    helper follows powers until either an idempotent step appears or a cycle
    repeats without one.
    """

    if max_power is None:
        max_power = len(element) ** len(element) + 1
    current = identity_transformation(len(element))
    seen = {current}
    for _ in range(max_power):
        next_value = compose_transformations(element, current)
        if next_value == current:
            return True
        if next_value in seen:
            return False
        seen.add(next_value)
        current = next_value
    return False


def is_aperiodic_monoid(monoid: TransformationMonoid) -> bool:
    """Return whether every element has an idempotent power."""

    return all(is_aperiodic_element(element) for element in monoid.elements)


def permutation_elements(elements: Iterable[Transformation]) -> Tuple[Transformation, ...]:
    """Return the elements that are permutations of the underlying set."""

    out = []
    for element in elements:
        if is_permutation_transformation(element):
            out.append(element)
    return tuple(out)


def monoid_permutation_group(monoid: TransformationMonoid) -> FiniteGroup:
    """Return the group of permutation elements in a transformation monoid."""

    return permutation_group_from_generators(
        permutation_elements(monoid.elements),
        degree=len(monoid.identity),
    )


def aperiodic_permutation_audit(monoid: TransformationMonoid) -> AperiodicPermutationAudit:
    """Check the lemma that aperiodic permutation elements are identity."""

    identity = monoid.identity
    permutations = permutation_elements(monoid.elements)
    nonidentity = tuple(element for element in permutations if element != identity)
    return AperiodicPermutationAudit(
        is_aperiodic=is_aperiodic_monoid(monoid),
        permutation_count=len(permutations),
        nonidentity_permutation_count=len(nonidentity),
        nonidentity_permutations=nonidentity,
    )


def unit_longitude_subgroup_audit(
    monoid: TransformationMonoid,
    n: int,
    braid_word: BraidWord,
    labels: Sequence[Transformation],
    *,
    max_assignments: int | None = None,
) -> UnitLongitudeSubgroupAudit:
    """Audit whether monoid unit labels are killed by finite-G longitudes.

    The finite group is the unit/permutation group of the transformation
    monoid.  If every supplied unit label lies in the subgroup generated by
    all values of the recursive Artin longitudes for ``braid_word``, then
    identity longitude data in this unit group forces all of those labels to
    be identity.  Nonunit labels are reported separately, because residual
    braid actions are permutations and must enter the unit group before they
    can represent genuine residual motion.
    """

    unit_group = monoid_permutation_group(monoid)
    unit_elements = set(unit_group.elements)
    subgroup = set(
        longitude_value_subgroup_elements(
            unit_group,
            n,
            braid_word,
            max_assignments=max_assignments,
        )
    )
    label_tuple = tuple(labels)
    nonunit = tuple(label for label in label_tuple if label not in unit_elements)
    outside = tuple(
        label
        for label in label_tuple
        if label in unit_elements and label not in subgroup
    )
    return UnitLongitudeSubgroupAudit(
        artin_permutation=artin_longitudes(n, braid_word).permutation,
        unit_group_order=len(unit_group.elements),
        longitude_subgroup_size=len(subgroup),
        label_count=len(label_tuple),
        nonunit_labels=nonunit,
        labels_outside_longitude_subgroup=outside,
    )


def unit_section_detection_audit(
    monoid: TransformationMonoid,
    n: int,
    braid_word: BraidWord,
    factors: Sequence[Transformation],
    *,
    max_assignments: int | None = None,
) -> UnitSectionDetectionAudit:
    """Audit the finite unit-section detector criterion for one branch word.

    A residual braid action is a permutation.  If the supplied factor word
    represents that residual branch inside a fixed finite transformation
    monoid, then a permutation composite forces every factor into the unit
    group.  If those unit factors all lie in ``V_beta(U(M))``, identity
    longitude data in the fixed finite group ``U(M)`` kills the branch.
    """

    factor_tuple = tuple(factors)
    factorization = unit_factorization_audit(
        factor_tuple,
        degree=len(monoid.identity),
    )
    longitude = unit_longitude_subgroup_audit(
        monoid,
        n,
        braid_word,
        factor_tuple,
        max_assignments=max_assignments,
    )
    monoid_elements = set(monoid.elements)
    return UnitSectionDetectionAudit(
        monoid_element_count=len(monoid.elements),
        factors_in_monoid=all(factor in monoid_elements for factor in factor_tuple),
        factorization=factorization,
        longitude=longitude,
        monoid_identity=monoid.identity,
    )


def unit_composite_detection_audit(
    monoid: TransformationMonoid,
    n: int,
    braid_word: BraidWord,
    factors: Sequence[Transformation],
    *,
    max_assignments: int | None = None,
) -> UnitCompositeDetectionAudit:
    """Audit the weaker endpoint criterion for a residual unit word.

    The section criterion asks each unit factor to lie in ``V_beta(U(M))``.
    For a residual branch it is enough that the final unit composite lies in
    that subgroup; internal unit labels may telescope before the detector
    readout is applied.
    """

    factor_tuple = tuple(factors)
    factorization = unit_factorization_audit(
        factor_tuple,
        degree=len(monoid.identity),
    )
    longitude = unit_longitude_subgroup_audit(
        monoid,
        n,
        braid_word,
        (factorization.composite,),
        max_assignments=max_assignments,
    )
    monoid_elements = set(monoid.elements)
    return UnitCompositeDetectionAudit(
        monoid_element_count=len(monoid.elements),
        factors_in_monoid=all(factor in monoid_elements for factor in factor_tuple),
        factorization=factorization,
        longitude=longitude,
        monoid_identity=monoid.identity,
    )


def unit_composite_longitude_route_audit(
    monoid: TransformationMonoid,
    n: int,
    braid_word: BraidWord,
    factors: Sequence[Transformation],
    *,
    max_assignments: int = 100_000,
) -> UnitCompositeLongitudeRouteAudit:
    """Compare endpoint-unit proof routes for one fixed braid word.

    This is the endpoint-unit analogue of the product closed-label route
    audit.  A single evaluated longitude hitting the endpoint is a convenient
    witness, but the theorem-level condition is only membership in the
    subgroup generated by all longitude values in the fixed unit group.
    """

    factor_tuple = tuple(factors)
    factorization = unit_factorization_audit(
        factor_tuple,
        degree=len(monoid.identity),
    )
    unit_group = monoid_permutation_group(monoid)
    assignment_count = len(unit_group.elements) ** n
    if assignment_count > max_assignments:
        raise ValueError(
            f"assignment search would enumerate {assignment_count} rows; "
            f"raise max_assignments above {max_assignments} explicitly"
        )
    data = artin_longitudes(n, braid_word)
    composite = factorization.composite
    generator_values = set()
    witness_longitude_index = None
    witness_assignment = None
    for assignment in product(unit_group.elements, repeat=n):
        values = tuple(
            evaluate_free_word(unit_group, assignment, longitude)
            for longitude in data.longitudes
        )
        generator_values.update(values)
        if (
            factorization.composite_is_unit
            and witness_assignment is None
            and composite != unit_group.identity
        ):
            for longitude_index, value in enumerate(values):
                if value == composite:
                    witness_longitude_index = longitude_index
                    witness_assignment = assignment
                    break
    subgroup = frozenset(subgroup_generated_elements(unit_group, generator_values))
    monoid_elements = set(monoid.elements)
    return UnitCompositeLongitudeRouteAudit(
        monoid_element_count=len(monoid.elements),
        factors_in_monoid=all(factor in monoid_elements for factor in factor_tuple),
        factorization=factorization,
        artin_permutation=data.permutation,
        unit_group_order=len(unit_group.elements),
        longitude_generator_count=len(generator_values),
        longitude_subgroup_size=len(subgroup),
        composite_lies_in_longitude_subgroup=(
            factorization.composite_is_unit and composite in subgroup
        ),
        has_single_longitude_witness=(
            composite == unit_group.identity or witness_assignment is not None
        ),
        witness_longitude_index=witness_longitude_index,
        witness_assignment=witness_assignment,
        monoid_identity=monoid.identity,
    )


def unit_composite_longitude_expression_audit(
    monoid: TransformationMonoid,
    n: int,
    braid_word: BraidWord,
    factors: Sequence[Transformation],
    assignment: Sequence[Transformation],
    expression: Sequence[Tuple[int, int]],
) -> UnitCompositeLongitudeExpressionAudit:
    """Verify that an endpoint is an explicit product of longitude values.

    The expression is a word in the evaluated recursive longitudes for one
    assignment ``F_n -> U(M)``.  When it matches the endpoint composite, it is
    a symbolic certificate of membership in ``V_beta(U(M))``: no subgroup
    enumeration is needed for the membership step.
    """

    factor_tuple = tuple(factors)
    assignment_tuple = tuple(assignment)
    expression_tuple = tuple(expression)
    factorization = unit_factorization_audit(
        factor_tuple,
        degree=len(monoid.identity),
    )
    unit_group = monoid_permutation_group(monoid)
    unit_elements = set(unit_group.elements)
    assignment_in_unit_group = (
        len(assignment_tuple) == n
        and all(value in unit_elements for value in assignment_tuple)
    )
    expression_value = None
    if assignment_in_unit_group:
        expression_value = evaluate_longitude_expression(
            unit_group,
            assignment_tuple,
            braid_word,
            expression_tuple,
        )
    monoid_elements = set(monoid.elements)
    data = artin_longitudes(n, braid_word)
    return UnitCompositeLongitudeExpressionAudit(
        monoid_element_count=len(monoid.elements),
        factors_in_monoid=all(factor in monoid_elements for factor in factor_tuple),
        factorization=factorization,
        artin_permutation=data.permutation,
        unit_group_order=len(unit_group.elements),
        assignment=assignment_tuple,
        assignment_in_unit_group=assignment_in_unit_group,
        expression=expression_tuple,
        expression_value=expression_value,
        expression_matches_composite=(
            expression_value is not None
            and factorization.composite_is_unit
            and expression_value == factorization.composite
        ),
        identity_longitude_signature=has_identity_longitude_signature(
            unit_group,
            n,
            braid_word,
        ),
        monoid_identity=monoid.identity,
    )


def unit_section_product_detection_audit(
    monoids: Sequence[TransformationMonoid],
    n: int,
    braid_word: BraidWord,
    factor_words: Sequence[Sequence[Transformation]],
    *,
    max_assignments: int | None = None,
    max_product_order: int = 100_000,
) -> UnitSectionProductDetectionAudit:
    """Audit that separate unit-section checks use one product detector.

    Branch proofs often split residual motion into several fixed finite
    transition monoids.  The sharp obstruction theorem needs one finite
    detector group, not a drifting list.  This helper applies
    ``unit_section_detection_audit`` to each factor and, when the direct
    product is small enough, checks the longitude-subgroup product identity
    for the unit groups.
    """

    monoid_tuple = tuple(monoids)
    word_tuple = tuple(tuple(word) for word in factor_words)
    if len(monoid_tuple) != len(word_tuple):
        raise ValueError("need one factor word for each transformation monoid")
    factor_audits = tuple(
        unit_section_detection_audit(
            monoid,
            n,
            braid_word,
            word,
            max_assignments=max_assignments,
        )
        for monoid, word in zip(monoid_tuple, word_tuple)
    )
    unit_groups = tuple(monoid_permutation_group(monoid) for monoid in monoid_tuple)
    unit_group_orders = tuple(len(group.elements) for group in unit_groups)
    product_order = 1
    for order in unit_group_orders:
        product_order *= order
    if product_order > max_product_order:
        return UnitSectionProductDetectionAudit(
            factor_audits=factor_audits,
            unit_group_orders=unit_group_orders,
            product_group_order=product_order,
            truncated=True,
            product_subgroup_size=None,
            expected_product_subgroup_size=None,
            product_subgroup_equals_factor_product=None,
        )
    product_audit = direct_product_longitude_subgroup_audit(
        unit_groups,
        n,
        braid_word,
        max_assignments=max_assignments,
    )
    return UnitSectionProductDetectionAudit(
        factor_audits=factor_audits,
        unit_group_orders=unit_group_orders,
        product_group_order=product_order,
        truncated=False,
        product_subgroup_size=product_audit.product_subgroup_size,
        expected_product_subgroup_size=product_audit.expected_product_subgroup_size,
        product_subgroup_equals_factor_product=product_audit.product_subgroup_equals_factor_product,
    )


def unit_composite_product_detection_audit(
    monoids: Sequence[TransformationMonoid],
    n: int,
    braid_word: BraidWord,
    factor_words: Sequence[Sequence[Transformation]],
    *,
    max_assignments: int | None = None,
    max_product_order: int = 100_000,
) -> UnitCompositeProductDetectionAudit:
    """Audit that endpoint-unit checks use one product detector.

    This is the product version of ``unit_composite_detection_audit``.  It
    accepts telescoping inside each fixed monoid and checks, when feasible,
    that the fixed direct product of the unit groups supplies the same
    longitude-value subgroup as the listed factors.
    """

    monoid_tuple = tuple(monoids)
    word_tuple = tuple(tuple(word) for word in factor_words)
    if len(monoid_tuple) != len(word_tuple):
        raise ValueError("need one factor word for each transformation monoid")
    factor_audits = tuple(
        unit_composite_detection_audit(
            monoid,
            n,
            braid_word,
            word,
            max_assignments=max_assignments,
        )
        for monoid, word in zip(monoid_tuple, word_tuple)
    )
    unit_groups = tuple(monoid_permutation_group(monoid) for monoid in monoid_tuple)
    unit_group_orders = tuple(len(group.elements) for group in unit_groups)
    product_endpoint = tuple(
        audit.factorization.composite
        for audit in factor_audits
    )
    product_order = 1
    for order in unit_group_orders:
        product_order *= order
    if product_order > max_product_order:
        return UnitCompositeProductDetectionAudit(
            factor_audits=factor_audits,
            product_endpoint=product_endpoint,
            unit_group_orders=unit_group_orders,
            product_group_order=product_order,
            truncated=True,
            product_subgroup_size=None,
            expected_product_subgroup_size=None,
            product_subgroup_equals_factor_product=None,
            product_endpoint_in_product_subgroup=None,
        )
    product_group = direct_product_group(unit_groups)
    product_subgroup = set(
        longitude_value_subgroup_elements(
            product_group,
            n,
            braid_word,
            max_assignments=max_assignments,
        )
    )
    product_audit = direct_product_longitude_subgroup_audit(
        unit_groups,
        n,
        braid_word,
        max_assignments=max_assignments,
    )
    return UnitCompositeProductDetectionAudit(
        factor_audits=factor_audits,
        product_endpoint=product_endpoint,
        unit_group_orders=unit_group_orders,
        product_group_order=product_order,
        truncated=False,
        product_subgroup_size=product_audit.product_subgroup_size,
        expected_product_subgroup_size=product_audit.expected_product_subgroup_size,
        product_subgroup_equals_factor_product=product_audit.product_subgroup_equals_factor_product,
        product_endpoint_in_product_subgroup=product_endpoint in product_subgroup,
    )


def unit_composite_product_longitude_expression_audit(
    monoids: Sequence[TransformationMonoid],
    n: int,
    braid_word: BraidWord,
    factor_words: Sequence[Sequence[Transformation]],
    assignments: Sequence[Sequence[Transformation]],
    expressions: Sequence[Sequence[Tuple[int, int]]],
) -> UnitCompositeProductExpressionAudit:
    """Combine endpoint expression certificates for one product detector.

    Each factor certificate displays its endpoint in ``V_beta(U(M_i))``.
    The helper embeds those factor certificates as an explicit word in
    generators of ``V_beta(prod_i U(M_i))``.  This is the non-enumerative
    product analogue of ``unit_composite_product_detection_audit``.
    """

    monoid_tuple = tuple(monoids)
    word_tuple = tuple(tuple(word) for word in factor_words)
    assignment_tuple = tuple(tuple(assignment) for assignment in assignments)
    expression_tuple = tuple(tuple(expression) for expression in expressions)
    if not (
        len(monoid_tuple)
        == len(word_tuple)
        == len(assignment_tuple)
        == len(expression_tuple)
    ):
        raise ValueError(
            "need one factor word, assignment, and expression for each monoid"
        )
    factor_audits = tuple(
        unit_composite_longitude_expression_audit(
            monoid,
            n,
            braid_word,
            word,
            assignment,
            expression,
        )
        for monoid, word, assignment, expression in zip(
            monoid_tuple,
            word_tuple,
            assignment_tuple,
            expression_tuple,
        )
    )
    unit_groups = tuple(monoid_permutation_group(monoid) for monoid in monoid_tuple)
    unit_group_orders = tuple(audit.unit_group_order for audit in factor_audits)
    product_order = 1
    for order in unit_group_orders:
        product_order *= order
    product_endpoint = tuple(
        audit.factorization.composite for audit in factor_audits
    )
    product_witness = None
    product_witness_value = None
    if all(audit.assignment_in_unit_group for audit in factor_audits):
        factor_witnesses = tuple(
            tuple(
                (audit.assignment, longitude_index, exponent)
                for longitude_index, exponent in audit.expression
            )
            for audit in factor_audits
        )
        product_witness = direct_product_longitude_subgroup_witness(
            unit_groups,
            n,
            factor_witnesses,
        )
        product_witness_value = evaluate_longitude_subgroup_witness(
            direct_product_group(unit_groups),
            n,
            braid_word,
            product_witness,
        )
    return UnitCompositeProductExpressionAudit(
        factor_audits=factor_audits,
        product_endpoint=product_endpoint,
        unit_group_orders=unit_group_orders,
        product_group_order=product_order,
        product_witness=product_witness,
        product_witness_value=product_witness_value,
        product_witness_matches_endpoint=product_witness_value == product_endpoint,
    )
