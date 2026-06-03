from __future__ import annotations

from itertools import islice, permutations, product
from math import gcd
from dataclasses import dataclass
from typing import Dict, Iterable, Iterator, List, Sequence, Tuple

from .action_images import braid_word_permutation_image
from .artin_longitudes import BraidWord, artin_longitudes, free_word_exponent_vector
from .braid_laws import law_word_on_last_strand
from .finite_braided_set import FiniteBraidedSet, rack_solution
from .finite_group import FiniteGroup, cyclic_group, symmetric_group
from .group_laws import (
    commutator,
    free_word_power,
    two_strand_symmetric_longitude_period,
)
from .residual import action_permutation, permutation_order, product_solution
from .residual import (
    braid_action_order,
    full_twist_braid_word,
    rack_full_twist_order_bound_audit,
)


def all_bijection_solutions(size: int, max_checked: int | None = None) -> Iterator[FiniteBraidedSet]:
    """Enumerate bijective YBE tables on {0,...,size-1}.

    This is intended for tiny audit searches only.  It is not a proof method
    for the global theorem.
    """

    elements = tuple(range(size))
    pairs = tuple(product(elements, repeat=2))
    images = permutations(pairs)
    if max_checked is not None:
        images = islice(images, max_checked)
    for image in images:
        solution = FiniteBraidedSet(elements, dict(zip(pairs, image)))
        if solution.is_ybe():
            yield solution


def is_rack_type(solution: FiniteBraidedSet) -> bool:
    """Return whether R(x,y) has rack form (x rack y, x)."""

    op = {}
    for x, y in product(solution.elements, repeat=2):
        first, second = solution.R[(x, y)]
        if second != x:
            return False
        op[(x, y)] = first
    for x in solution.elements:
        if {op[(x, y)] for y in solution.elements} != set(solution.elements):
            return False
    return True


def dependency_profile(solution: FiniteBraidedSet) -> Dict[str, bool]:
    """Detect one-coordinate dependencies of the output coordinates."""

    elements = solution.elements
    return {
        "first_depends_only_on_x": all(
            len({solution.R[(x, y)][0] for y in elements}) == 1
            for x in elements
        ),
        "first_depends_only_on_y": all(
            len({solution.R[(x, y)][0] for x in elements}) == 1
            for y in elements
        ),
        "second_depends_only_on_x": all(
            len({solution.R[(x, y)][1] for y in elements}) == 1
            for x in elements
        ),
        "second_depends_only_on_y": all(
            len({solution.R[(x, y)][1] for x in elements}) == 1
            for y in elements
        ),
    }


def is_identity_table(solution: FiniteBraidedSet) -> bool:
    return all(
        solution.R[(x, y)] == (x, y)
        for x, y in product(solution.elements, repeat=2)
    )


def is_permutation_solution_form(solution: FiniteBraidedSet) -> bool:
    """Return whether R(x,y)=(sigma(y),tau(x)) for permutations sigma,tau."""

    return permutation_solution_maps(solution) is not None


def permutation_solution_maps(solution: FiniteBraidedSet) -> Tuple[Dict[object, object], Dict[object, object]] | None:
    """Return ``(sigma,tau)`` for the form ``R(x,y)=(sigma(y),tau(x))``.

    This checks that both coordinate maps are permutations of the finite set.
    It does not itself prove the Yang-Baxter equation.  For a YBE table in
    this form, the equation forces ``sigma`` and ``tau`` to commute.
    """

    if not solution.elements:
        return None
    profile = dependency_profile(solution)
    if not (
        profile["first_depends_only_on_y"]
        and profile["second_depends_only_on_x"]
    ):
        return None
    base = solution.elements[0]
    sigma = {
        y: solution.R[(base, y)][0]
        for y in solution.elements
    }
    tau = {
        x: solution.R[(x, base)][1]
        for x in solution.elements
    }
    element_set = set(solution.elements)
    if set(sigma.values()) != element_set or set(tau.values()) != element_set:
        return None
    if any(
        solution.R[(x, y)] != (sigma[y], tau[x])
        for x, y in product(solution.elements, repeat=2)
    ):
        return None
    return sigma, tau


def _permutation_mapping_order(mapping: Dict[object, object]) -> int:
    seen = set()
    order = 1
    for start in mapping:
        if start in seen:
            continue
        current = start
        cycle_length = 0
        while current not in seen:
            seen.add(current)
            cycle_length += 1
            current = mapping[current]
        if cycle_length:
            order = abs(order * cycle_length) // gcd(order, cycle_length)
    return order


def permutation_solution_twist_order(solution: FiniteBraidedSet) -> int | None:
    """Return the order of ``sigma tau`` for a permutation-form solution."""

    maps = permutation_solution_maps(solution)
    if maps is None:
        return None
    sigma, tau = maps
    twist = {
        x: sigma[tau[x]]
        for x in solution.elements
    }
    return _permutation_mapping_order(twist)


def permutation_solution_crossing_order_formula(solution: FiniteBraidedSet) -> int | None:
    """Return the two-strand crossing order for a permutation-form solution.

    For ``R(x,y)=(sigma(y),tau(x))`` with commuting ``sigma`` and ``tau``,
    ``R^2`` acts as ``h x, h y`` where ``h=sigma tau``.  Hence the crossing
    order is ``2*ord(h)`` unless the underlying set has one point.
    """

    twist_order = permutation_solution_twist_order(solution)
    if twist_order is None:
        return None
    if len(solution.elements) <= 1:
        return 1
    return 2 * twist_order


@dataclass(frozen=True)
class TwoStrandSymmetricGateSummary:
    point_count: int
    symmetric_longitude_period: int
    crossing_order: int
    passes: bool
    explanation: str
    branch_tags: Tuple[str, ...]


@dataclass(frozen=True)
class TwoStrandProductGateSummary:
    left_size: int
    right_size: int
    product_size: int
    left_crossing_order: int
    right_crossing_order: int
    product_crossing_order: int
    product_symmetric_longitude_period: int
    passes: bool


def derived_rack_operation_table(
    solution: FiniteBraidedSet,
) -> Dict[Tuple[object, object], object] | None:
    """Return the derived rack operation for a left-nondegenerate solution.

    For ``R(x,y)=(sigma_x(y), rho_y(x))`` the operation is

    ``a op b = sigma_a(rho_{sigma_b^{-1}(a)}(b))``.

    This is the two-strand shadow of the guitar-map construction for
    left-nondegenerate set-theoretic YBE solutions.
    """

    if not is_left_nondegenerate(solution):
        return None
    inverse_left_actions: Dict[object, Dict[object, object]] = {}
    for left in solution.elements:
        mapping = {
            solution.R[(left, right)][0]: right
            for right in solution.elements
        }
        if len(mapping) != len(solution.elements):
            return None
        inverse_left_actions[left] = mapping

    operation = {}
    for a, b in product(solution.elements, repeat=2):
        preimage = inverse_left_actions[b][a]
        rho_preimage_of_b = solution.R[(b, preimage)][1]
        operation[(a, b)] = solution.R[(a, rho_preimage_of_b)][0]
    return operation


def derived_rack_solution(solution: FiniteBraidedSet) -> FiniteBraidedSet | None:
    """Build the derived rack solution when the operation is rack-valid."""

    operation = derived_rack_operation_table(solution)
    if operation is None:
        return None
    try:
        derived = rack_solution(
            solution.elements,
            lambda left, right: operation[(left, right)],
        )
    except ValueError:
        return None
    if not derived.is_ybe():
        return None
    return derived


def two_strand_guitar_map(
    solution: FiniteBraidedSet,
) -> Dict[Tuple[object, object], Tuple[object, object]] | None:
    """Return the two-strand guitar bijection ``J_2(x,y)=(sigma_x(y),x)``."""

    if not is_left_nondegenerate(solution):
        return None
    guitar = {
        (x, y): (solution.R[(x, y)][0], x)
        for x, y in product(solution.elements, repeat=2)
    }
    if set(guitar.values()) != set(guitar.keys()):
        return None
    return guitar


def two_strand_guitar_conjugacy_holds(solution: FiniteBraidedSet) -> bool:
    """Check ``J_2 R_X = R_derived J_2`` for the derived rack branch."""

    derived = derived_rack_solution(solution)
    guitar = two_strand_guitar_map(solution)
    if derived is None or guitar is None:
        return False
    return all(
        guitar[solution.R[(x, y)]] == derived.R[guitar[(x, y)]]
        for x, y in product(solution.elements, repeat=2)
    )


def two_strand_symmetric_gate_summary(
    solution: FiniteBraidedSet,
) -> TwoStrandSymmetricGateSummary:
    """Summarize the exact direct-Sym two-strand gate for one solution.

    The summary distinguishes currently proved branch explanations from rows
    that merely pass the divisibility check.  A row marked
    ``passes_unclassified`` is not a counterexample; it means this helper has
    not assigned the divisibility to one of the in-workspace symbolic
    two-strand branch formulas.
    """

    point_count = len(solution.elements)
    period = two_strand_symmetric_longitude_period(point_count)
    crossing_order = permutation_order(action_permutation(solution, 2, (1,)))
    passes = period % crossing_order == 0
    tags = branch_tags(solution)
    if not passes:
        explanation = "direct_symmetric_gate_failure_candidate"
    elif crossing_order == 1:
        explanation = "trivial_crossing_action"
    elif is_involutive_solution(solution):
        explanation = "involutive_order_two"
    elif is_rack_type(solution):
        explanation = "rack_inner_group_branch"
    elif is_permutation_solution_form(solution):
        twist_order = permutation_solution_twist_order(solution)
        explanation = f"permutation_form_twist_order_{twist_order}"
    elif is_left_nondegenerate(solution) and two_strand_guitar_conjugacy_holds(solution):
        explanation = "left_nondegenerate_derived_rack_branch"
    else:
        explanation = "passes_unclassified"
    return TwoStrandSymmetricGateSummary(
        point_count=point_count,
        symmetric_longitude_period=period,
        crossing_order=crossing_order,
        passes=passes,
        explanation=explanation,
        branch_tags=tags,
    )


def two_strand_product_gate_summary(
    left: FiniteBraidedSet,
    right: FiniteBraidedSet,
) -> TwoStrandProductGateSummary:
    """Summarize the direct-Sym two-strand gate for a product solution.

    If the two factors pass the direct symmetric two-strand gate, then their
    Cartesian product passes too.  Indeed, the product crossing order is the
    lcm of the two factor crossing orders, while
    ``lcm(1,...,|left|)`` and ``lcm(1,...,|right|)`` both divide
    ``lcm(1,...,|left|*|right|)``.
    """

    product = product_solution(left, right)
    product_size = len(product.elements)
    product_period = two_strand_symmetric_longitude_period(product_size)
    product_order = permutation_order(action_permutation(product, 2, (1,)))
    return TwoStrandProductGateSummary(
        left_size=len(left.elements),
        right_size=len(right.elements),
        product_size=product_size,
        left_crossing_order=permutation_order(action_permutation(left, 2, (1,))),
        right_crossing_order=permutation_order(action_permutation(right, 2, (1,))),
        product_crossing_order=product_order,
        product_symmetric_longitude_period=product_period,
        passes=product_period % product_order == 0,
    )


@dataclass(frozen=True)
class PermutationSolutionLongitudeFactorization:
    twist_order: int
    longitude_total_exponents: Tuple[int, ...]
    output: Tuple[object, ...]


@dataclass(frozen=True)
class KnownBranchDetectorCertificate:
    """Explicit finite detector group for a closed whole-solution branch.

    The certificate assumes the supplied table is a finite bijective YBE
    solution and records a group that is fixed at the solution/interval level,
    not chosen from the braid index.
    """

    reason: str
    detector_group: FiniteGroup
    detector_group_order: int
    sharp_rack_factor_size: int
    branch_tags: Tuple[str, ...]
    twist_order: int | None
    proof_reference: str
    detector_kind: str
    braid_index_independent: bool


@dataclass(frozen=True)
class FullTwistKnownBranchBoundAudit:
    """Central full-twist order data for one known symbolic branch."""

    solution_size: int
    max_n: int
    action_orders: Tuple[int, ...]
    reason: str | None
    uniform_bound: int | None
    finite_checks_derived_from_tables: bool

    @property
    def symbolic_bound_available(self) -> bool:
        return self.uniform_bound is not None

    @property
    def checked_orders_divide_bound(self) -> bool:
        if self.uniform_bound is None:
            return False
        return all(self.uniform_bound % order == 0 for order in self.action_orders)

    @property
    def proves_checked_known_branch_full_twist_bound(self) -> bool:
        return (
            self.finite_checks_derived_from_tables
            and self.symbolic_bound_available
            and self.checked_orders_divide_bound
        )


@dataclass(frozen=True)
class CoordinateDependencyBranchAudit:
    """Known-branch routing for YBE tables with one-coordinate outputs.

    The same-side cases mean ``pr_1 R(x,y)`` depends only on ``x`` or
    ``pr_2 R(x,y)`` depends only on ``y``.  For a finite bijective YBE table
    either condition forces the identity table.  The opposite-side cases mean
    ``pr_1 R(x,y)`` depends only on ``y`` or ``pr_2 R(x,y)`` depends only on
    ``x``; bijectivity then forces nondegeneracy, so the existing
    left-nondegenerate/guitar branch applies.
    """

    solution_size: int
    max_n: int
    active_dependencies: Tuple[str, ...]
    same_side_dependencies: Tuple[str, ...]
    opposite_side_dependencies: Tuple[str, ...]
    identity_table: bool
    left_nondegenerate: bool
    right_nondegenerate: bool
    nondegenerate: bool
    known_full_twist_reason: str | None
    known_full_twist_bound: int | None
    action_orders: Tuple[int, ...]
    reason: str | None
    finite_checks_derived_from_tables: bool

    @property
    def has_coordinate_dependency(self) -> bool:
        return bool(self.active_dependencies)

    @property
    def has_same_side_dependency(self) -> bool:
        return bool(self.same_side_dependencies)

    @property
    def has_opposite_side_dependency(self) -> bool:
        return bool(self.opposite_side_dependencies)

    @property
    def proves_coordinate_dependency_closed_branch(self) -> bool:
        if not (
            self.finite_checks_derived_from_tables
            and self.has_coordinate_dependency
            and self.reason is not None
        ):
            return False
        if self.has_same_side_dependency:
            return (
                self.reason == "same_side_dependency_identity_collapse"
                and self.identity_table
                and self.known_full_twist_reason is not None
            )
        return (
            self.reason == "opposite_side_dependency_nondegenerate_branch"
            and self.nondegenerate
            and self.known_full_twist_reason is not None
        )


def _known_branch_certificate(
    *,
    solution: FiniteBraidedSet,
    reason: str,
    detector_group: FiniteGroup,
    twist_order: int | None,
    proof_reference: str,
    detector_kind: str,
) -> KnownBranchDetectorCertificate:
    order = len(detector_group.elements)
    return KnownBranchDetectorCertificate(
        reason=reason,
        detector_group=detector_group,
        detector_group_order=order,
        sharp_rack_factor_size=2 * order * order,
        branch_tags=branch_tags(solution),
        twist_order=twist_order,
        proof_reference=proof_reference,
        detector_kind=detector_kind,
        braid_index_independent=True,
    )


def permutation_form_detector_group(solution: FiniteBraidedSet) -> FiniteGroup:
    """Return the fixed cyclic detector ``C_ord(sigma tau)``.

    Raises ``ValueError`` when the solution is not in permutation form.
    """

    twist_order = permutation_solution_twist_order(solution)
    if twist_order is None:
        raise ValueError("solution is not in permutation form")
    return cyclic_group(twist_order)


def known_branch_detector_certificate(
    solution: FiniteBraidedSet,
) -> KnownBranchDetectorCertificate | None:
    """Return an explicit finite-G certificate for closed total branches.

    The involutive and permutation-form branches use the minimal detector
    groups from ``proofs/involutive_permutation_detector.md``.  Rack-type and
    left-nondegenerate/guitar branches use the all-degree direct-symmetric
    implication from ``proofs/direct_symmetric_known_branches.md``.
    """

    if is_involutive_solution(solution):
        return _known_branch_certificate(
            solution=solution,
            reason="involutive_artin_permutation",
            detector_group=cyclic_group(1),
            twist_order=None,
            proof_reference="proofs/involutive_permutation_detector.md",
            detector_kind="trivial_group",
        )
    twist_order = permutation_solution_twist_order(solution)
    if twist_order is not None:
        return _known_branch_certificate(
            solution=solution,
            reason="permutation_twist_subgroup",
            detector_group=cyclic_group(twist_order),
            twist_order=twist_order,
            proof_reference="proofs/involutive_permutation_detector.md",
            detector_kind="cyclic_twist_group",
        )
    reason = direct_symmetric_known_branch_reason(solution)
    if reason is None:
        return None
    return _known_branch_certificate(
        solution=solution,
        reason=reason,
        detector_group=symmetric_group(len(solution.elements)),
        twist_order=None,
        proof_reference="proofs/direct_symmetric_known_branches.md",
        detector_kind="direct_symmetric_group",
    )


def known_branch_full_twist_order_bound_audit(
    solution: FiniteBraidedSet,
    max_n: int,
) -> FullTwistKnownBranchBoundAudit:
    """Audit central full-twist orders against known symbolic branch bounds.

    This is not a classifier for every finite YBE solution.  It records the
    current theorem-level branches where a fixed finite bound is known:
    involutive, permutation-form, rack-type, and left-nondegenerate via the
    derived rack.  The ``action_orders`` field is still a finite prefix check.
    """

    if max_n < 1:
        raise ValueError("max_n must be positive")
    if not solution.is_ybe():
        raise ValueError("solution must satisfy the Yang-Baxter equation")
    action_orders = tuple(
        braid_action_order(solution, n, full_twist_braid_word(n))
        for n in range(1, max_n + 1)
    )
    reason = None
    uniform_bound = None
    if is_involutive_solution(solution):
        reason = "involutive_artin_permutation"
        uniform_bound = 1
    else:
        twist_order = permutation_solution_twist_order(solution)
        if twist_order is not None:
            reason = "permutation_form_twist_order"
            uniform_bound = twist_order
        elif is_rack_type(solution):
            reason = "rack_inner_group_exponent"
            uniform_bound = rack_full_twist_order_bound_audit(
                solution,
                1,
            ).inner_group_exponent
        else:
            derived = derived_rack_solution(solution)
            if is_left_nondegenerate(solution) and derived is not None:
                reason = "left_nondegenerate_derived_rack_exponent"
                uniform_bound = rack_full_twist_order_bound_audit(
                    derived,
                    1,
                ).inner_group_exponent
    return FullTwistKnownBranchBoundAudit(
        solution_size=len(solution.elements),
        max_n=max_n,
        action_orders=action_orders,
        reason=reason,
        uniform_bound=uniform_bound,
        finite_checks_derived_from_tables=True,
    )


def coordinate_dependency_branch_audit(
    solution: FiniteBraidedSet,
    max_n: int,
) -> CoordinateDependencyBranchAudit:
    """Route one-coordinate dependency profiles to closed symbolic branches.

    This helper is deliberately narrow.  It does not classify arbitrary
    degenerate bijective YBE solutions; it only records the elementary
    dependency profiles that cannot supply an unbounded full-twist obstruction.
    """

    if not solution.is_ybe():
        raise ValueError("solution must satisfy the Yang-Baxter equation")
    profile = dependency_profile(solution)
    active = tuple(key for key, value in profile.items() if value)
    same_side = tuple(
        key
        for key in ("first_depends_only_on_x", "second_depends_only_on_y")
        if profile[key]
    )
    opposite_side = tuple(
        key
        for key in ("first_depends_only_on_y", "second_depends_only_on_x")
        if profile[key]
    )
    full_twist = known_branch_full_twist_order_bound_audit(solution, max_n)
    reason = None
    if same_side:
        if is_identity_table(solution):
            reason = "same_side_dependency_identity_collapse"
    elif opposite_side:
        if is_nondegenerate(solution) and full_twist.reason is not None:
            reason = "opposite_side_dependency_nondegenerate_branch"
    return CoordinateDependencyBranchAudit(
        solution_size=len(solution.elements),
        max_n=max_n,
        active_dependencies=active,
        same_side_dependencies=same_side,
        opposite_side_dependencies=opposite_side,
        identity_table=is_identity_table(solution),
        left_nondegenerate=is_left_nondegenerate(solution),
        right_nondegenerate=is_right_nondegenerate(solution),
        nondegenerate=is_nondegenerate(solution),
        known_full_twist_reason=full_twist.reason,
        known_full_twist_bound=full_twist.uniform_bound,
        action_orders=full_twist.action_orders,
        reason=reason,
        finite_checks_derived_from_tables=True,
    )


def _invert_mapping(mapping: Dict[object, object]) -> Dict[object, object]:
    return {value: key for key, value in mapping.items()}


def _apply_mapping_power(mapping: Dict[object, object], value: object, exponent: int) -> object:
    active = mapping
    steps = exponent
    if exponent < 0:
        active = _invert_mapping(mapping)
        steps = -exponent
    out = value
    for _ in range(steps):
        out = active[out]
    return out


def permutation_solution_pure_longitude_factorization(
    solution: FiniteBraidedSet,
    braid_word: BraidWord,
    tup: Sequence[object],
) -> PermutationSolutionLongitudeFactorization:
    """Compute a pure permutation-form action from longitude exponents.

    For ``R(x,y)=(sigma(y),tau(x))`` and pure ``beta``, the action is
    ``h^epsilon(L_j(beta))`` on coordinate ``j``, where ``h=sigma tau``.
    """

    maps = permutation_solution_maps(solution)
    if maps is None:
        raise ValueError("solution is not in permutation form")
    n = len(tup)
    data = artin_longitudes(n, braid_word)
    if data.permutation != tuple(range(n)):
        raise ValueError("braid word is not pure in the Artin permutation")
    sigma, tau = maps
    twist = {
        x: sigma[tau[x]]
        for x in solution.elements
    }
    exponents = tuple(
        sum(free_word_exponent_vector(n, longitude))
        for longitude in data.longitudes
    )
    output = tuple(
        _apply_mapping_power(twist, value, exponent)
        for value, exponent in zip(tup, exponents)
    )
    return PermutationSolutionLongitudeFactorization(
        twist_order=_permutation_mapping_order(twist),
        longitude_total_exponents=exponents,
        output=output,
    )


def is_left_nondegenerate(solution: FiniteBraidedSet) -> bool:
    """Return whether every left coordinate map y -> pr_1 R(x,y) is bijective."""

    elements = set(solution.elements)
    return all(
        {solution.R[(x, y)][0] for y in solution.elements} == elements
        for x in solution.elements
    )


def is_right_nondegenerate(solution: FiniteBraidedSet) -> bool:
    """Return whether every right coordinate map x -> pr_2 R(x,y) is bijective."""

    elements = set(solution.elements)
    return all(
        {solution.R[(x, y)][1] for x in solution.elements} == elements
        for y in solution.elements
    )


def is_nondegenerate(solution: FiniteBraidedSet) -> bool:
    """Return whether the solution is both left and right nondegenerate."""

    return is_left_nondegenerate(solution) and is_right_nondegenerate(solution)


def solution_table_signature(solution: FiniteBraidedSet) -> Tuple[Tuple[object, object], ...]:
    return tuple(solution.R[(x, y)] for x in solution.elements for y in solution.elements)


def affine_cyclic_form(solution: FiniteBraidedSet) -> Dict[str, object] | None:
    """Detect tiny affine formulas over the cyclic set {0,...,m-1}.

    This is a bounded audit helper, not a classification routine.  It searches
    for constants a,b,c,d,e,f modulo m such that
    R(x,y) = (a*x + b*y + c, d*x + e*y + f).
    """

    modulus = len(solution.elements)
    if tuple(solution.elements) != tuple(range(modulus)):
        return None
    for a, b, c, d, e, f in product(range(modulus), repeat=6):
        if all(
            solution.R[(x, y)]
            == ((a * x + b * y + c) % modulus, (d * x + e * y + f) % modulus)
            for x, y in product(solution.elements, repeat=2)
        ):
            return {
                "modulus": modulus,
                "matrix": [[a, b], [d, e]],
                "offset": [c, f],
            }
    return None


def is_involutive_solution(solution: FiniteBraidedSet) -> bool:
    """Return whether R^2 is the identity on X x X."""

    return all(
        solution.R[solution.R[(x, y)]] == (x, y)
        for x, y in product(solution.elements, repeat=2)
    )


def branch_tags(solution: FiniteBraidedSet) -> Tuple[str, ...]:
    """Return conservative known-branch tags used by audit reports."""

    tags = []
    if is_rack_type(solution):
        tags.append("rack_type")
    if is_involutive_solution(solution):
        tags.append("involutive")
    if is_identity_table(solution):
        tags.append("identity_table")
    if is_permutation_solution_form(solution):
        tags.append("permutation_form")
    if is_left_nondegenerate(solution):
        tags.append("left_nondegenerate")
    if is_right_nondegenerate(solution):
        tags.append("right_nondegenerate")
    if is_nondegenerate(solution):
        tags.append("nondegenerate")
    if affine_cyclic_form(solution) is not None:
        tags.append("affine_cyclic")
    return tuple(tags)


def direct_symmetric_known_branch_reason(solution: FiniteBraidedSet) -> str | None:
    """Return a symbolic branch proving direct ``Sym(X)`` detection, if known.

    The returned reason is theorem-level branch bookkeeping, not finite search
    evidence.  Each reason has a finite branch detector that embeds in
    ``Sym(X)`` or is killed by the Artin permutation, so identity
    ``Sym(X)``-longitude data implies the branch detector's identity data.
    """

    if is_rack_type(solution):
        return "rack_inner_group_subgroup"
    if is_involutive_solution(solution):
        return "involutive_artin_permutation"
    if is_permutation_solution_form(solution):
        return "permutation_twist_subgroup"
    if is_left_nondegenerate(solution) and derived_rack_solution(solution) is not None:
        return "left_nondegenerate_guitar_derived_rack"
    return None


def commutator_law_braid_moves(solution: FiniteBraidedSet) -> bool:
    word = commutator(free_word_power(0, 1), free_word_power(1, 1))
    n, braid = law_word_on_last_strand(word, arity=2)
    image = braid_word_permutation_image(solution, n, braid)
    return image != tuple(range(len(image)))


def small_solution_summary(size: int, max_checked: int | None = None) -> Dict[str, object]:
    checked = 0
    ybe_count = 0
    rack_type_count = 0
    nonrack_count = 0
    commutator_movers: List[Tuple[Tuple[object, object], ...]] = []
    elements = tuple(range(size))
    pairs = tuple(product(elements, repeat=2))
    images = permutations(pairs)
    if max_checked is not None:
        images = islice(images, max_checked)
    for image in images:
        checked += 1
        solution = FiniteBraidedSet(elements, dict(zip(pairs, image)))
        if not solution.is_ybe():
            continue
        ybe_count += 1
        if is_rack_type(solution):
            rack_type_count += 1
        else:
            nonrack_count += 1
            if commutator_law_braid_moves(solution):
                commutator_movers.append(solution_table_signature(solution))
    return {
        "size": size,
        "max_checked": max_checked,
        "checked": checked,
        "exhaustive": max_checked is None,
        "ybe_count": ybe_count,
        "rack_type_count": rack_type_count,
        "nonrack_count": nonrack_count,
        "nonrack_commutator_law_mover_count": len(commutator_movers),
        "nonrack_commutator_law_movers": [
            [list(pair) for pair in signature] for signature in commutator_movers[:5]
        ],
    }
