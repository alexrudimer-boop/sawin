from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from collections import deque
from typing import Callable, Dict, Hashable, Iterable, Mapping, Sequence, Tuple

GroupElement = Hashable
Permutation = Tuple[int, ...]


@dataclass(frozen=True)
class FiniteGroup:
    """A small finite group with an explicit multiplication table."""

    elements: Tuple[GroupElement, ...]
    identity: GroupElement
    multiply_table: Mapping[Tuple[GroupElement, GroupElement], GroupElement]

    def __post_init__(self) -> None:
        object.__setattr__(self, "elements", tuple(self.elements))
        if self.identity not in self.elements:
            raise ValueError("identity must be a group element")
        domain = {(a, b) for a in self.elements for b in self.elements}
        if set(self.multiply_table.keys()) != domain:
            raise ValueError("multiplication table must be defined on G x G")
        if any(value not in self.elements for value in self.multiply_table.values()):
            raise ValueError("multiplication table must be closed in G")
        self._validate_group_axioms()

    def _validate_group_axioms(self) -> None:
        e = self.identity
        for a in self.elements:
            if self.mul(e, a) != a or self.mul(a, e) != a:
                raise ValueError("identity axiom failed")
            if not any(self.mul(a, b) == e and self.mul(b, a) == e for b in self.elements):
                raise ValueError(f"missing inverse for {a!r}")
        for a, b, c in product(self.elements, repeat=3):
            if self.mul(self.mul(a, b), c) != self.mul(a, self.mul(b, c)):
                raise ValueError("associativity failed")

    @property
    def inverse_table(self) -> Dict[GroupElement, GroupElement]:
        e = self.identity
        return {
            a: next(b for b in self.elements if self.mul(a, b) == e and self.mul(b, a) == e)
            for a in self.elements
        }

    def mul(self, a: GroupElement, b: GroupElement) -> GroupElement:
        return self.multiply_table[(a, b)]

    def inv(self, a: GroupElement) -> GroupElement:
        return self.inverse_table[a]

    def pow(self, a: GroupElement, exponent: int) -> GroupElement:
        if exponent < 0:
            return self.pow(self.inv(a), -exponent)
        out = self.identity
        for _ in range(exponent):
            out = self.mul(out, a)
        return out

    def conjugate(self, a: GroupElement, b: GroupElement) -> GroupElement:
        """Return a b a^{-1}."""

        return self.mul(self.mul(a, b), self.inv(a))


@dataclass(frozen=True)
class FiniteGroupHomomorphism:
    """A checked homomorphism between explicit finite groups."""

    source: FiniteGroup
    target: FiniteGroup
    mapping: Mapping[GroupElement, GroupElement]

    def __post_init__(self) -> None:
        if set(self.mapping.keys()) != set(self.source.elements):
            raise ValueError("homomorphism mapping must be defined on the source")
        if any(value not in self.target.elements for value in self.mapping.values()):
            raise ValueError("homomorphism values must lie in the target")
        if self.mapping[self.source.identity] != self.target.identity:
            raise ValueError("homomorphism must preserve identity")
        for left, right in product(self.source.elements, repeat=2):
            if self.apply(self.source.mul(left, right)) != self.target.mul(
                self.apply(left),
                self.apply(right),
            ):
                raise ValueError("mapping is not a group homomorphism")

    def apply(self, element: GroupElement) -> GroupElement:
        return self.mapping[element]

    @property
    def image(self) -> Tuple[GroupElement, ...]:
        return tuple(sorted(set(self.mapping.values()), key=repr))

    @property
    def is_surjective(self) -> bool:
        return set(self.image) == set(self.target.elements)


@dataclass(frozen=True)
class DerivedSeriesAudit:
    """Derived-series summary for a finite group."""

    subgroup_orders: Tuple[int, ...]
    perfect_residual: Tuple[GroupElement, ...]
    perfect_residual_order: int
    terminates_at_identity: bool

    @property
    def is_solvable(self) -> bool:
        return self.terminates_at_identity

    @property
    def derived_length(self) -> int:
        return max(0, len(self.subgroup_orders) - 1)


def build_group(
    elements: Iterable[GroupElement],
    identity: GroupElement,
    multiply: Callable[[GroupElement, GroupElement], GroupElement],
) -> FiniteGroup:
    elems = tuple(elements)
    table = {(a, b): multiply(a, b) for a in elems for b in elems}
    return FiniteGroup(elems, identity, table)


def cyclic_group(order: int) -> FiniteGroup:
    if order <= 0:
        raise ValueError("order must be positive")
    return build_group(range(order), 0, lambda a, b: (a + b) % order)


def direct_product_group(groups: Sequence[FiniteGroup]) -> FiniteGroup:
    """Return the finite direct product of the supplied groups."""

    factors = tuple(groups)
    if not factors:
        return build_group((tuple(),), tuple(), lambda _a, _b: tuple())
    elements = tuple(product(*(group.elements for group in factors)))
    identity = tuple(group.identity for group in factors)

    def multiply(left: Tuple[GroupElement, ...], right: Tuple[GroupElement, ...]) -> Tuple[GroupElement, ...]:
        return tuple(
            group.mul(a, b)
            for group, a, b in zip(factors, left, right)
        )

    return build_group(elements, identity, multiply)


def subgroup_generated_elements(
    group: FiniteGroup,
    generators: Iterable[GroupElement],
) -> Tuple[GroupElement, ...]:
    """Return the elements of the subgroup generated inside a finite group."""

    symmetric_gens = set(generators)
    symmetric_gens.update(group.inv(generator) for generator in tuple(symmetric_gens))
    seen = {group.identity}
    queue = deque([group.identity])
    while queue:
        current = queue.popleft()
        for generator in symmetric_gens:
            for candidate in (
                group.mul(generator, current),
                group.mul(current, generator),
            ):
                if candidate not in seen:
                    seen.add(candidate)
                    queue.append(candidate)
    return tuple(sorted(seen, key=repr))


def is_abelian_group(group: FiniteGroup) -> bool:
    """Return whether the finite group is abelian."""

    return all(
        group.mul(left, right) == group.mul(right, left)
        for left in group.elements
        for right in group.elements
    )


def subgroup_as_group(
    group: FiniteGroup,
    subgroup: Iterable[GroupElement],
) -> FiniteGroup:
    """Return a finite group obtained by restricting multiplication."""

    subset = tuple(sorted(set(subgroup), key=repr))
    if not subset:
        raise ValueError("subgroup must be nonempty")
    elements = set(group.elements)
    if any(element not in elements for element in subset):
        raise ValueError("subgroup element outside group")
    subset_set = set(subset)
    if group.identity not in subset_set:
        raise ValueError("subgroup must contain identity")
    if any(group.inv(element) not in subset_set for element in subset):
        raise ValueError("subgroup must contain inverses")
    if any(group.mul(left, right) not in subset_set for left in subset for right in subset):
        raise ValueError("subgroup must be closed under multiplication")
    return build_group(subset, group.identity, lambda left, right: group.mul(left, right))


def normal_closure_elements(
    group: FiniteGroup,
    generators: Iterable[GroupElement],
) -> Tuple[GroupElement, ...]:
    """Return the normal closure of generators inside a finite group."""

    gens = tuple(generators)
    elements = set(group.elements)
    if any(generator not in elements for generator in gens):
        raise ValueError("normal-closure generator outside group")
    conjugates = [
        group.conjugate(element, generator)
        for element in group.elements
        for generator in gens
    ]
    return subgroup_generated_elements(group, conjugates)


def commutator_subgroup_elements(
    group: FiniteGroup,
    subgroup: Iterable[GroupElement] | None = None,
) -> Tuple[GroupElement, ...]:
    """Return the commutator subgroup of ``group`` or a supplied subgroup."""

    subset = tuple(group.elements if subgroup is None else subgroup)
    elements = set(group.elements)
    if any(element not in elements for element in subset):
        raise ValueError("commutator subgroup element outside group")
    commutators = [
        group.mul(group.mul(group.mul(left, right), group.inv(left)), group.inv(right))
        for left in subset
        for right in subset
    ]
    return subgroup_generated_elements(group, commutators)


def derived_series_subgroups(group: FiniteGroup) -> Tuple[Tuple[GroupElement, ...], ...]:
    """Return the derived series ending at its stable perfect residual."""

    series = [tuple(sorted(group.elements, key=repr))]
    while True:
        current = series[-1]
        next_subgroup = commutator_subgroup_elements(group, current)
        if set(next_subgroup) == set(current):
            return tuple(series)
        series.append(next_subgroup)


def derived_series_audit(group: FiniteGroup) -> DerivedSeriesAudit:
    """Audit the finite derived series of ``group``."""

    series = derived_series_subgroups(group)
    residual = series[-1]
    return DerivedSeriesAudit(
        subgroup_orders=tuple(len(subgroup) for subgroup in series),
        perfect_residual=residual,
        perfect_residual_order=len(residual),
        terminates_at_identity=set(residual) == {group.identity},
    )


def is_normal_subgroup(
    group: FiniteGroup,
    subgroup: Iterable[GroupElement],
) -> bool:
    """Return whether the supplied elements form a normal subgroup."""

    subset = frozenset(subgroup)
    elements = set(group.elements)
    if not subset or not subset.issubset(elements):
        return False
    if group.identity not in subset:
        return False
    if any(group.inv(element) not in subset for element in subset):
        return False
    if any(group.mul(left, right) not in subset for left in subset for right in subset):
        return False
    return all(
        group.conjugate(element, normal_element) in subset
        for element in group.elements
        for normal_element in subset
    )


def quotient_group_by_normal_subgroup(
    group: FiniteGroup,
    normal_subgroup: Iterable[GroupElement],
) -> Tuple[FiniteGroup, FiniteGroupHomomorphism]:
    """Return ``G/N`` and the quotient homomorphism for a normal subgroup."""

    normal = frozenset(normal_subgroup)
    if not is_normal_subgroup(group, normal):
        raise ValueError("quotient requires a normal subgroup")

    element_to_coset: Dict[GroupElement, frozenset[GroupElement]] = {}
    cosets = []
    for element in group.elements:
        if element in element_to_coset:
            continue
        coset = frozenset(group.mul(element, normal_element) for normal_element in normal)
        cosets.append(coset)
        for coset_element in coset:
            element_to_coset[coset_element] = coset

    coset_tuple = tuple(sorted(cosets, key=repr))
    identity_coset = element_to_coset[group.identity]

    def multiply(
        left: frozenset[GroupElement],
        right: frozenset[GroupElement],
    ) -> frozenset[GroupElement]:
        left_rep = next(iter(left))
        right_rep = next(iter(right))
        return element_to_coset[group.mul(left_rep, right_rep)]

    quotient = build_group(coset_tuple, identity_coset, multiply)
    projection = FiniteGroupHomomorphism(group, quotient, element_to_coset)
    return quotient, projection


def symmetric_group(degree: int) -> FiniteGroup:
    if degree <= 0:
        raise ValueError("degree must be positive")
    elems = tuple(permutations(range(degree)))
    identity = tuple(range(degree))

    def compose(a: Tuple[int, ...], b: Tuple[int, ...]) -> Tuple[int, ...]:
        return tuple(a[b[i]] for i in range(degree))

    return build_group(elems, identity, compose)


def left_regular_representation(
    group: FiniteGroup,
    degree: int | None = None,
) -> FiniteGroupHomomorphism:
    """Embed a finite group into a symmetric group by left multiplication.

    If ``degree`` is larger than ``|G|``, the extra points are fixed.  This is
    the Cayley embedding used to replace arbitrary finite detector groups by
    symmetric detector groups.
    """

    group_order = len(group.elements)
    target_degree = group_order if degree is None else degree
    if target_degree < group_order:
        raise ValueError("degree must be at least the group order")
    elements = tuple(group.elements)
    index = {element: position for position, element in enumerate(elements)}
    target = symmetric_group(target_degree)
    mapping = {}
    for left in elements:
        images = list(range(target_degree))
        for position, right in enumerate(elements):
            images[position] = index[group.mul(left, right)]
        mapping[left] = tuple(images)
    return FiniteGroupHomomorphism(group, target, mapping)


def symmetric_group_inclusion(
    source_degree: int,
    target_degree: int,
) -> FiniteGroupHomomorphism:
    """Embed ``S_source_degree`` in ``S_target_degree`` by fixing extra points."""

    if source_degree <= 0 or target_degree <= 0:
        raise ValueError("degrees must be positive")
    if target_degree < source_degree:
        raise ValueError("target degree must be at least the source degree")
    source = symmetric_group(source_degree)
    target = symmetric_group(target_degree)
    mapping = {}
    fixed_tail = tuple(range(source_degree, target_degree))
    for permutation in source.elements:
        mapping[permutation] = tuple(permutation) + fixed_tail
    return FiniteGroupHomomorphism(source, target, mapping)


def compose_permutations(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    if len(left) != len(right):
        raise ValueError("permutations must have the same degree")
    return tuple(left[right[i]] for i in range(len(left)))


def invert_permutation(permutation: Permutation) -> Permutation:
    inverse = [0] * len(permutation)
    for index, image in enumerate(permutation):
        inverse[image] = index
    return tuple(inverse)


def permutation_group_from_generators(
    generators: Iterable[Permutation], degree: int | None = None
) -> FiniteGroup:
    """Build the finite permutation group generated by the given permutations."""

    gens = tuple(generators)
    if degree is None:
        if not gens:
            degree = 0
        else:
            degree = len(gens[0])
    if any(len(gen) != degree for gen in gens):
        raise ValueError("all generators must have the requested degree")
    identity = tuple(range(degree))
    symmetric_gens = set(gens)
    symmetric_gens.update(invert_permutation(gen) for gen in gens)
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for gen in symmetric_gens:
            candidate = compose_permutations(gen, current)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return build_group(
        tuple(sorted(seen)),
        identity,
        compose_permutations,
    )
