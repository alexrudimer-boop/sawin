from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from itertools import product
from typing import Dict, Hashable, Iterable, Mapping, Tuple

from .finite_braided_set import FiniteBraidedSet, opposite_solution
from .finite_group import FiniteGroup, permutation_group_from_generators
from .local_interval import canonical_partition

Transformation = Tuple[int, ...]
EdgeGerm = Tuple[Transformation, Hashable]
ContextWord = Tuple[EdgeGerm, ...]
Permutation = Tuple[int, ...]


def identity_transformation(size: int) -> Transformation:
    return tuple(range(size))


def compose_transformations(left: Transformation, right: Transformation) -> Transformation:
    """Return left after right."""

    if len(left) != len(right):
        raise ValueError("transformations must have the same domain size")
    return tuple(left[right[i]] for i in range(len(left)))


def coordinate_action_maps(solution: FiniteBraidedSet) -> Dict[Hashable, Transformation]:
    """Return first-coordinate action maps tau_x(y)=pr_1 R(x,y)."""

    index = {element: i for i, element in enumerate(solution.elements)}
    return {
        x: tuple(index[solution.R[(x, y)][0]] for y in solution.elements)
        for x in solution.elements
    }


def right_coordinate_action_maps(solution: FiniteBraidedSet) -> Dict[Hashable, Transformation]:
    """Return right-coordinate action maps rho_x(y)=pr_2 R(y,x)."""

    return coordinate_action_maps(opposite_solution(solution))


def coordinate_action_relation_failures(solution: FiniteBraidedSet):
    """Return failures of tau_x tau_y = tau_u tau_v for R(x,y)=(u,v)."""

    tau = coordinate_action_maps(solution)
    failures = []
    for x, y in product(solution.elements, repeat=2):
        u, v = solution.R[(x, y)]
        left = compose_transformations(tau[x], tau[y])
        right = compose_transformations(tau[u], tau[v])
        if left != right:
            failures.append((x, y, u, v, left, right))
    return failures


def right_coordinate_action_relation_failures(solution: FiniteBraidedSet):
    """Return failures of rho_y rho_x = rho_v rho_u for R(x,y)=(u,v)."""

    rho = right_coordinate_action_maps(solution)
    failures = []
    for x, y in product(solution.elements, repeat=2):
        u, v = solution.R[(x, y)]
        left = compose_transformations(rho[y], rho[x])
        right = compose_transformations(rho[v], rho[u])
        if left != right:
            failures.append((x, y, u, v, left, right))
    return failures


def opposite_green_branch_audits(solution: FiniteBraidedSet) -> Tuple[GreenBranchAudit, ...]:
    """Run the Green branch audit on the side-opposite solution."""

    return green_branch_audits(opposite_solution(solution))


@dataclass(frozen=True)
class TransformationMonoid:
    elements: Tuple[Transformation, ...]
    identity: Transformation

    @classmethod
    def generated(cls, generators: Iterable[Transformation]) -> "TransformationMonoid":
        gens = tuple(generators)
        if not gens:
            return cls((tuple(),), tuple())
        size = len(gens[0])
        identity = identity_transformation(size)
        seen = {identity}
        queue = deque([identity])
        while queue:
            current = queue.popleft()
            for gen in gens:
                for candidate in (
                    compose_transformations(current, gen),
                    compose_transformations(gen, current),
                ):
                    if candidate not in seen:
                        seen.add(candidate)
                        queue.append(candidate)
        return cls(tuple(sorted(seen)), identity)

    def mul(self, left: Transformation, right: Transformation) -> Transformation:
        return compose_transformations(left, right)

    def right_ideal(self, element: Transformation) -> frozenset[Transformation]:
        return frozenset(self.mul(element, other) for other in self.elements)

    def left_ideal(self, element: Transformation) -> frozenset[Transformation]:
        return frozenset(self.mul(other, element) for other in self.elements)

    def two_sided_ideal(self, element: Transformation) -> frozenset[Transformation]:
        return frozenset(
            self.mul(left, self.mul(element, right))
            for left in self.elements
            for right in self.elements
        )

    def r_classes(self) -> Tuple[Tuple[Transformation, ...], ...]:
        classes: Dict[frozenset[Transformation], list[Transformation]] = defaultdict(list)
        for element in self.elements:
            classes[self.right_ideal(element)].append(element)
        return tuple(tuple(sorted(values)) for values in classes.values())

    def j_classes(self) -> Tuple[Tuple[Transformation, ...], ...]:
        classes: Dict[frozenset[Transformation], list[Transformation]] = defaultdict(list)
        for element in self.elements:
            classes[self.two_sided_ideal(element)].append(element)
        return tuple(tuple(sorted(values)) for values in classes.values())

    def is_idempotent(self, element: Transformation) -> bool:
        return self.mul(element, element) == element

    def regular_j_classes(self) -> Tuple[Tuple[Transformation, ...], ...]:
        return tuple(
            j_class
            for j_class in self.j_classes()
            if any(self.is_idempotent(element) for element in j_class)
        )


class UnionFind:
    def __init__(self, items: Iterable[EdgeGerm]) -> None:
        self.parent = {item: item for item in items}

    def find(self, item: EdgeGerm) -> EdgeGerm:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, a: EdgeGerm, b: EdgeGerm) -> None:
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a

    def partition(self):
        blocks: Dict[EdgeGerm, list[EdgeGerm]] = defaultdict(list)
        for item in self.parent:
            blocks[self.find(item)].append(item)
        return canonical_partition(blocks.values())


@dataclass(frozen=True)
class BranchRow:
    a: EdgeGerm
    q: EdgeGerm
    q_under_a: EdgeGerm
    a_under_q: EdgeGerm


@dataclass(frozen=True)
class GreenBranchAudit:
    r_class: Tuple[Transformation, ...]
    edge_germs: Tuple[EdgeGerm, ...]
    edge_targets: Tuple[Tuple[EdgeGerm, Transformation], ...]
    rows: Tuple[BranchRow, ...]
    atom_partition: Tuple[frozenset[EdgeGerm], ...]
    branch_choice_failures: Tuple[Tuple[EdgeGerm, EdgeGerm, EdgeGerm, EdgeGerm, EdgeGerm], ...]


@dataclass(frozen=True)
class AtomActionFailure:
    """A conflict in the atom-level completed-row action."""

    operation: str
    left_atom: int
    right_atom: int
    previous_output_atom: int
    output_atom: int


@dataclass(frozen=True)
class AtomActionSummary:
    """Whether completed Green rows descend to saturated atoms.

    The completed-row formula gives a partial operation
    ``p(a) triangleright p(q) = p(a^q)`` on supported atom pairs.  The inverse
    bookkeeping operation is ``p(a^q) triangleleft p(q) = p(a)``.  Conflicts
    here mean that the saturated atom quotient still remembers section data
    not carried by the pair of input atoms.
    """

    atom_count: int
    row_count: int
    supported_pair_count: int
    undefined_pair_count: int
    triangleright_failure_count: int
    triangleleft_failure_count: int
    triangleright_failures: Tuple[AtomActionFailure, ...]
    triangleleft_failures: Tuple[AtomActionFailure, ...]

    @property
    def well_defined(self) -> bool:
        return (
            self.triangleright_failure_count == 0
            and self.triangleleft_failure_count == 0
        )


@dataclass(frozen=True)
class AtomDescentClosureSummary:
    """Least coarsening that makes completed rows act on atoms.

    The atom partition is generated by the Green relations ``q^a ~ q``.  The
    rack layer needs one more property: the completed-row output ``a^q`` must
    depend only on the two input atoms, and the inverse bookkeeping output
    must also depend only on atoms.  This audit closes the atom relation under
    those two implications and records whether any new identifications were
    forced.
    """

    initial_atom_count: int
    closed_atom_count: int
    stable_depth: int
    initial_related_pair_count: int
    closed_related_pair_count: int
    closure_partition: Tuple[frozenset[EdgeGerm], ...]
    well_defined_after_closure: bool
    undefined_pair_count_after_closure: int

    @property
    def added_related_pair_count(self) -> int:
        return self.closed_related_pair_count - self.initial_related_pair_count

    @property
    def closes_without_coarsening(self) -> bool:
        return self.initial_atom_count == self.closed_atom_count

    @property
    def proves_stable_atom_action(self) -> bool:
        return (
            self.closes_without_coarsening
            and self.well_defined_after_closure
            and self.undefined_pair_count_after_closure == 0
        )


@dataclass(frozen=True)
class AtomQuotientRackAudit:
    """Right-rack law audit for the Green atom quotient."""

    atom_count: int
    constructed: bool
    construction_error: str | None
    right_rack_like: bool | None
    right_translations_bijective: bool | None
    right_self_distributive: bool | None
    is_ybe: bool | None

    @property
    def proves_right_rack_ybe_layer(self) -> bool:
        return (
            self.constructed
            and self.right_rack_like is True
            and self.right_translations_bijective is True
            and self.right_self_distributive is True
            and self.is_ybe is True
        )


@dataclass(frozen=True)
class SourceAtomProjection:
    source: Transformation
    retained_labels: Tuple[Hashable, ...]
    label_partition: Tuple[frozenset[Hashable], ...]
    kind: str


@dataclass(frozen=True)
class AtomProjectionSummary:
    r_class: Tuple[Transformation, ...]
    source_count: int
    equality_source_count: int
    universal_source_count: int
    mixed_source_count: int
    empty_source_count: int
    source_projections: Tuple[SourceAtomProjection, ...]


@dataclass(frozen=True)
class SchutzenbergerSummary:
    r_class: Tuple[Transformation, ...]
    right_stabilizer_size: int
    permutation_count: int
    nonpermutation_stabilizer_count: int
    permutation_group_closed: bool
    globally_stabilizing_labels: Tuple[Hashable, ...]
    global_edge_germ_count: int
    local_only_edge_germ_count: int


@dataclass(frozen=True)
class SchutzenbergerActionGroup:
    r_class: Tuple[Transformation, ...]
    actions: Tuple[Permutation, ...]
    group: FiniteGroup


@dataclass(frozen=True)
class KernelActionSummary:
    r_class: Tuple[Transformation, ...]
    kernel_partition: Tuple[frozenset[int], ...]
    retained_labels: Tuple[Hashable, ...]
    induced_permutations: Tuple[Tuple[Hashable, Permutation], ...]
    induced_group_size: int
    nonpermutation_label_count: int


def _block_index(partition: Tuple[frozenset[EdgeGerm], ...], item: EdgeGerm) -> int:
    for index, block in enumerate(partition):
        if item in block:
            return index
    raise ValueError("item not present in partition")


def edge_source(edge: EdgeGerm) -> Transformation:
    return edge[0]


def edge_target_map(audit: GreenBranchAudit) -> Dict[EdgeGerm, Transformation]:
    return dict(audit.edge_targets)


def completed_row_map(audit: GreenBranchAudit) -> Dict[Tuple[EdgeGerm, EdgeGerm], BranchRow]:
    return {(row.q, row.a): row for row in audit.rows}


def atom_index(audit: GreenBranchAudit, edge: EdgeGerm) -> int:
    return _block_index(audit.atom_partition, edge)


def atom_word(audit: GreenBranchAudit, word: ContextWord) -> Tuple[int, ...]:
    return tuple(atom_index(audit, edge) for edge in word)


def _record_atom_action(
    table: Dict[Tuple[int, int], int],
    failures: list[AtomActionFailure],
    *,
    operation: str,
    left_atom: int,
    right_atom: int,
    output_atom: int,
) -> None:
    key = (left_atom, right_atom)
    previous = table.get(key)
    if previous is None:
        table[key] = output_atom
        return
    if previous != output_atom:
        failures.append(
            AtomActionFailure(
                operation=operation,
                left_atom=left_atom,
                right_atom=right_atom,
                previous_output_atom=previous,
                output_atom=output_atom,
            )
        )


def atom_action_summary(audit: GreenBranchAudit) -> AtomActionSummary:
    """Summarize whether Green completed rows act on saturated atoms.

    Existing ``branch_choice_failures`` check whether a fixed edge ``a`` and
    atom ``p(q)`` determine ``p(a^q)``.  This stronger summary asks whether
    the output depends only on the two input atoms ``p(a),p(q)``.  It also
    checks the inverse bookkeeping operation from ``p(a^q),p(q)`` back to
    ``p(a)``.
    """

    triangleright: Dict[Tuple[int, int], int] = {}
    triangleleft: Dict[Tuple[int, int], int] = {}
    triangleright_failures: list[AtomActionFailure] = []
    triangleleft_failures: list[AtomActionFailure] = []
    supported_pairs = set()
    for row in audit.rows:
        a_atom = atom_index(audit, row.a)
        q_atom = atom_index(audit, row.q)
        aq_atom = atom_index(audit, row.a_under_q)
        supported_pairs.add((a_atom, q_atom))
        _record_atom_action(
            triangleright,
            triangleright_failures,
            operation="triangleright",
            left_atom=a_atom,
            right_atom=q_atom,
            output_atom=aq_atom,
        )
        _record_atom_action(
            triangleleft,
            triangleleft_failures,
            operation="triangleleft",
            left_atom=aq_atom,
            right_atom=q_atom,
            output_atom=a_atom,
        )
    atom_count = len(audit.atom_partition)
    return AtomActionSummary(
        atom_count=atom_count,
        row_count=len(audit.rows),
        supported_pair_count=len(supported_pairs),
        undefined_pair_count=atom_count * atom_count - len(supported_pairs),
        triangleright_failure_count=len(triangleright_failures),
        triangleleft_failure_count=len(triangleleft_failures),
        triangleright_failures=tuple(triangleright_failures),
        triangleleft_failures=tuple(triangleleft_failures),
    )


def _partition_related_pair_count(partition: Tuple[frozenset[EdgeGerm], ...]) -> int:
    return sum(len(block) * len(block) for block in partition)


def _atom_action_summary_for_partition(
    audit: GreenBranchAudit,
    partition: Tuple[frozenset[EdgeGerm], ...],
) -> AtomActionSummary:
    triangleright: Dict[Tuple[int, int], int] = {}
    triangleleft: Dict[Tuple[int, int], int] = {}
    triangleright_failures: list[AtomActionFailure] = []
    triangleleft_failures: list[AtomActionFailure] = []
    supported_pairs = set()
    for row in audit.rows:
        a_atom = _block_index(partition, row.a)
        q_atom = _block_index(partition, row.q)
        aq_atom = _block_index(partition, row.a_under_q)
        supported_pairs.add((a_atom, q_atom))
        _record_atom_action(
            triangleright,
            triangleright_failures,
            operation="triangleright",
            left_atom=a_atom,
            right_atom=q_atom,
            output_atom=aq_atom,
        )
        _record_atom_action(
            triangleleft,
            triangleleft_failures,
            operation="triangleleft",
            left_atom=aq_atom,
            right_atom=q_atom,
            output_atom=a_atom,
        )
    atom_count = len(partition)
    return AtomActionSummary(
        atom_count=atom_count,
        row_count=len(audit.rows),
        supported_pair_count=len(supported_pairs),
        undefined_pair_count=atom_count * atom_count - len(supported_pairs),
        triangleright_failure_count=len(triangleright_failures),
        triangleleft_failure_count=len(triangleleft_failures),
        triangleright_failures=tuple(triangleright_failures),
        triangleleft_failures=tuple(triangleleft_failures),
    )


def atom_descent_closure_summary(audit: GreenBranchAudit) -> AtomDescentClosureSummary:
    """Close Green atoms under completed-row action and inverse bookkeeping.

    A forward conflict says two rows have the same pair of input atoms
    ``p(a),p(q)`` but different output atoms ``p(a^q)``.  An inverse conflict
    says the pair ``p(a^q),p(q)`` does not determine ``p(a)``.  This helper
    repeatedly identifies the conflicting outputs until both operations are
    well-defined on the coarsened partition.  If the coarsening is trivial and
    no atom pair is unsupported, the original atom partition already supplies
    the desired total rack-like action.
    """

    uf = UnionFind(audit.edge_germs)
    for block in audit.atom_partition:
        block_tuple = tuple(block)
        for edge in block_tuple[1:]:
            uf.union(block_tuple[0], edge)

    depth = 0
    while True:
        before = tuple(sorted((edge, uf.find(edge)) for edge in audit.edge_germs))
        rows = tuple(audit.rows)
        for left in rows:
            for right in rows:
                if (
                    uf.find(left.a) == uf.find(right.a)
                    and uf.find(left.q) == uf.find(right.q)
                ):
                    uf.union(left.a_under_q, right.a_under_q)
                if (
                    uf.find(left.a_under_q) == uf.find(right.a_under_q)
                    and uf.find(left.q) == uf.find(right.q)
                ):
                    uf.union(left.a, right.a)
        after = tuple(sorted((edge, uf.find(edge)) for edge in audit.edge_germs))
        if after == before:
            closure = uf.partition()
            closed_action = _atom_action_summary_for_partition(audit, closure)
            return AtomDescentClosureSummary(
                initial_atom_count=len(audit.atom_partition),
                closed_atom_count=len(closure),
                stable_depth=depth,
                initial_related_pair_count=_partition_related_pair_count(
                    audit.atom_partition
                ),
                closed_related_pair_count=_partition_related_pair_count(closure),
                closure_partition=closure,
                well_defined_after_closure=closed_action.well_defined,
                undefined_pair_count_after_closure=(
                    closed_action.undefined_pair_count
                ),
            )
        depth += 1


def atom_quotient_solution(audit: GreenBranchAudit) -> FiniteBraidedSet:
    """Return the rack-like atom quotient of a Green completed-row audit.

    When the completed-row action descends to atoms and is defined on every
    atom pair, the quotient crossing is

    ``R_atom(A,Q) = (Q, A triangleright Q)``.

    This is the atom-level branch action isolated by the Green audit.  It is
    finite and depends only on the coordinate-action monoid data for the
    chosen Green class.  Failures here are structural: the saturated atom
    layer is not yet a well-defined total finite braided set.
    """

    summary = atom_action_summary(audit)
    if not summary.well_defined:
        raise ValueError("atom action does not descend to saturated atoms")
    if summary.undefined_pair_count:
        raise ValueError("atom action is not defined on every atom pair")
    return _atom_quotient_solution_for_partition(audit, audit.atom_partition)


def _atom_quotient_solution_for_partition(
    audit: GreenBranchAudit,
    partition: Tuple[frozenset[EdgeGerm], ...],
) -> FiniteBraidedSet:
    summary = _atom_action_summary_for_partition(audit, partition)
    if not summary.well_defined:
        raise ValueError("atom action does not descend to the chosen partition")
    if summary.undefined_pair_count:
        raise ValueError("atom action is not defined on every chosen atom pair")
    elements = tuple(range(summary.atom_count))
    table: Dict[Tuple[int, int], Tuple[int, int]] = {}
    for row in audit.rows:
        a_atom = _block_index(partition, row.a)
        q_atom = _block_index(partition, row.q)
        aq_atom = _block_index(partition, row.a_under_q)
        table[(a_atom, q_atom)] = (q_atom, aq_atom)
    return FiniteBraidedSet(elements, table)


def atom_descent_quotient_solution(audit: GreenBranchAudit) -> FiniteBraidedSet:
    """Return the rack-like quotient after descent-closure coarsening.

    This constructs the atom crossing on the least coarsening that makes the
    completed-row action and inverse bookkeeping action well-defined.  It is
    useful for distinguishing controlled atom coarsening from a genuine
    obstruction.  It still raises if the closed action is not total.
    """

    closure = atom_descent_closure_summary(audit)
    if not closure.well_defined_after_closure:
        raise ValueError("descent closure did not make atom action well-defined")
    if closure.undefined_pair_count_after_closure:
        raise ValueError("descent-closed atom action is not defined on every atom pair")
    return _atom_quotient_solution_for_partition(audit, closure.closure_partition)


def atom_quotient_rack_audit(audit: GreenBranchAudit) -> AtomQuotientRackAudit:
    """Check the explicit right-rack laws for the Green atom quotient."""

    atom_count = len(audit.atom_partition)
    try:
        quotient = atom_quotient_solution(audit)
    except ValueError as exc:
        return AtomQuotientRackAudit(
            atom_count=atom_count,
            constructed=False,
            construction_error=str(exc),
            right_rack_like=None,
            right_translations_bijective=None,
            right_self_distributive=None,
            is_ybe=None,
        )
    elements = quotient.elements
    right_rack_like = all(
        quotient.R[(left, right)][0] == right
        for left in elements
        for right in elements
    )

    def op(left: int, right: int) -> int:
        return quotient.R[(left, right)][1]

    right_translations_bijective = all(
        {op(left, right) for left in elements} == set(elements)
        for right in elements
    )
    right_self_distributive = all(
        op(op(left, middle), right)
        == op(op(left, right), op(middle, right))
        for left in elements
        for middle in elements
        for right in elements
    )
    return AtomQuotientRackAudit(
        atom_count=atom_count,
        constructed=True,
        construction_error=None,
        right_rack_like=right_rack_like,
        right_translations_bijective=right_translations_bijective,
        right_self_distributive=right_self_distributive,
        is_ybe=quotient.is_ybe(),
    )


def atom_descent_quotient_rack_audit(audit: GreenBranchAudit) -> AtomQuotientRackAudit:
    """Check rack laws after atom descent-closure coarsening."""

    closure = atom_descent_closure_summary(audit)
    atom_count = closure.closed_atom_count
    try:
        quotient = atom_descent_quotient_solution(audit)
    except ValueError as exc:
        return AtomQuotientRackAudit(
            atom_count=atom_count,
            constructed=False,
            construction_error=str(exc),
            right_rack_like=None,
            right_translations_bijective=None,
            right_self_distributive=None,
            is_ybe=None,
        )
    elements = quotient.elements
    right_rack_like = all(
        quotient.R[(left, right)][0] == right
        for left in elements
        for right in elements
    )

    def op(left: int, right: int) -> int:
        return quotient.R[(left, right)][1]

    right_translations_bijective = all(
        {op(left, right) for left in elements} == set(elements)
        for right in elements
    )
    right_self_distributive = all(
        op(op(left, middle), right)
        == op(op(left, right), op(middle, right))
        for left in elements
        for middle in elements
        for right in elements
    )
    return AtomQuotientRackAudit(
        atom_count=atom_count,
        constructed=True,
        construction_error=None,
        right_rack_like=right_rack_like,
        right_translations_bijective=right_translations_bijective,
        right_self_distributive=right_self_distributive,
        is_ybe=quotient.is_ybe(),
    )


def atom_quotient_inner_group(audit: GreenBranchAudit) -> FiniteGroup:
    """Return the finite group generated by atom right translations."""

    rack_audit = atom_quotient_rack_audit(audit)
    if not rack_audit.proves_right_rack_ybe_layer:
        raise ValueError("atom quotient is not a proved right-rack layer")
    quotient = atom_quotient_solution(audit)
    generators = tuple(
        tuple(quotient.R[(left, right)][1] for left in quotient.elements)
        for right in quotient.elements
    )
    return permutation_group_from_generators(
        generators,
        degree=len(quotient.elements),
    )


def source_atom_projection(
    audit: GreenBranchAudit, source: Transformation
) -> SourceAtomProjection:
    """Project the atom partition to labels retained at one R-class source."""

    labels_by_atom: Dict[int, list[Hashable]] = defaultdict(list)
    for edge in audit.edge_germs:
        if edge_source(edge) == source:
            labels_by_atom[atom_index(audit, edge)].append(edge[1])
    blocks = canonical_partition(labels_by_atom.values())
    retained = tuple(sorted((label for block in blocks for label in block), key=repr))
    if not blocks:
        kind = "empty"
    elif len(blocks) == len(retained):
        kind = "equality"
    elif len(blocks) == 1:
        kind = "universal"
    else:
        kind = "mixed"
    return SourceAtomProjection(
        source=source,
        retained_labels=retained,
        label_partition=blocks,
        kind=kind,
    )


def atom_projection_summary(audit: GreenBranchAudit) -> AtomProjectionSummary:
    projections = tuple(
        source_atom_projection(audit, source) for source in audit.r_class
    )
    return AtomProjectionSummary(
        r_class=audit.r_class,
        source_count=len(projections),
        equality_source_count=sum(1 for item in projections if item.kind == "equality"),
        universal_source_count=sum(1 for item in projections if item.kind == "universal"),
        mixed_source_count=sum(1 for item in projections if item.kind == "mixed"),
        empty_source_count=sum(1 for item in projections if item.kind == "empty"),
        source_projections=projections,
    )


def _permutation_action_on_r_class(
    monoid: TransformationMonoid, r_class: Tuple[Transformation, ...], element: Transformation
) -> Permutation | None:
    index = {value: i for i, value in enumerate(r_class)}
    images = []
    for source in r_class:
        target = monoid.mul(source, element)
        if target not in index:
            return None
        images.append(index[target])
    candidate = tuple(images)
    if set(candidate) != set(range(len(r_class))):
        return None
    return candidate


def _compose_index_permutations(left: Permutation, right: Permutation) -> Permutation:
    if len(left) != len(right):
        raise ValueError("permutations must have same size")
    return tuple(left[right[i]] for i in range(len(left)))


def _generated_index_permutation_group(generators: Iterable[Permutation]) -> frozenset[Permutation]:
    gens = tuple(generators)
    if not gens:
        return frozenset({tuple()})
    identity = tuple(range(len(gens[0])))
    seen = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for gen in gens:
            candidate = _compose_index_permutations(gen, current)
            if candidate not in seen:
                seen.add(candidate)
                queue.append(candidate)
    return frozenset(seen)


def transformation_kernel(transform: Transformation) -> Tuple[frozenset[int], ...]:
    blocks: Dict[int, list[int]] = defaultdict(list)
    for index, value in enumerate(transform):
        blocks[value].append(index)
    return canonical_partition(blocks.values())


def _kernel_block_lookup(partition: Tuple[frozenset[int], ...]) -> Dict[int, int]:
    lookup = {}
    for block_index, block in enumerate(partition):
        for item in block:
            lookup[item] = block_index
    return lookup


def induced_kernel_permutation(
    kernel_partition: Tuple[frozenset[int], ...], transform: Transformation
) -> Permutation | None:
    """Return the induced permutation on kernel blocks, if it exists."""

    lookup = _kernel_block_lookup(kernel_partition)
    images = []
    for block in kernel_partition:
        target_blocks = {lookup[transform[item]] for item in block}
        if len(target_blocks) != 1:
            return None
        images.append(next(iter(target_blocks)))
    candidate = tuple(images)
    if set(candidate) != set(range(len(kernel_partition))):
        return None
    return candidate


def kernel_action_summary(solution: FiniteBraidedSet) -> Tuple[KernelActionSummary, ...]:
    """Summarize finite kernel-block actions for retained Green labels.

    Every element of one Green R-class has the same transformation kernel.
    If a retained edge `(s,x)` stays in the class, then `tau_x` preserves that
    kernel and induces a permutation on the quotient by the kernel.  This
    summary records the finite permutation group generated by those induced
    actions; unlike the Schutzenberger action, it is insensitive to possible
    splitting of one full-transformation R-class into several submonoid
    R-classes.
    """

    failures = coordinate_action_relation_failures(solution)
    if failures:
        raise ValueError("coordinate actions do not satisfy structure relation")

    tau = coordinate_action_maps(solution)
    summaries = []
    for audit in green_branch_audits(solution):
        if not audit.r_class:
            continue
        kernel = transformation_kernel(audit.r_class[0])
        retained_labels = tuple(sorted({label for _source, label in audit.edge_germs}, key=repr))
        induced = []
        nonpermutation = 0
        for label in retained_labels:
            permutation = induced_kernel_permutation(kernel, tau[label])
            if permutation is None:
                nonpermutation += 1
            else:
                induced.append((label, permutation))
        group = _generated_index_permutation_group(permutation for _label, permutation in induced)
        summaries.append(
            KernelActionSummary(
                r_class=audit.r_class,
                kernel_partition=kernel,
                retained_labels=retained_labels,
                induced_permutations=tuple(induced),
                induced_group_size=len(group),
                nonpermutation_label_count=nonpermutation,
            )
        )
    return tuple(sorted(summaries, key=repr))


def schutzenberger_summaries(solution: FiniteBraidedSet) -> Tuple[SchutzenbergerSummary, ...]:
    """Summarize finite permutation actions attached to regular Green R-classes.

    The right stabilizer of an R-class acts on that class by right
    multiplication.  In a regular R-class this is the Schutzenberger group
    action; local-only retained edge germs identify branch transitions that do
    not come from a global stabilizer element and therefore remain outside this
    finite group-action candidate.
    """

    failures = coordinate_action_relation_failures(solution)
    if failures:
        raise ValueError("coordinate actions do not satisfy structure relation")

    tau = coordinate_action_maps(solution)
    monoid = TransformationMonoid.generated(tau.values())
    audit_by_class = {audit.r_class: audit for audit in green_branch_audits(solution)}
    summaries = []
    for r_class, audit in audit_by_class.items():
        stabilizer = tuple(
            element
            for element in monoid.elements
            if all(monoid.mul(source, element) in set(r_class) for source in r_class)
        )
        actions = tuple(
            action
            for action in (
                _permutation_action_on_r_class(monoid, r_class, element)
                for element in stabilizer
            )
            if action is not None
        )
        action_set = set(actions)
        closed = all(
            _compose_index_permutations(left, right) in action_set
            for left in action_set
            for right in action_set
        )
        global_labels = tuple(
            sorted(
                (
                    label
                    for label, action in tau.items()
                    if _permutation_action_on_r_class(monoid, r_class, action)
                    is not None
                ),
                key=repr,
            )
        )
        global_label_set = set(global_labels)
        global_edges = sum(1 for _source, label in audit.edge_germs if label in global_label_set)
        summaries.append(
            SchutzenbergerSummary(
                r_class=r_class,
                right_stabilizer_size=len(stabilizer),
                permutation_count=len(action_set),
                nonpermutation_stabilizer_count=len(stabilizer) - len(actions),
                permutation_group_closed=closed,
                globally_stabilizing_labels=global_labels,
                global_edge_germ_count=global_edges,
                local_only_edge_germ_count=len(audit.edge_germs) - global_edges,
            )
        )
    return tuple(sorted(summaries, key=repr))


def schutzenberger_action_groups(
    solution: FiniteBraidedSet,
) -> Tuple[SchutzenbergerActionGroup, ...]:
    """Return finite Schutzenberger permutation groups for regular R-classes."""

    failures = coordinate_action_relation_failures(solution)
    if failures:
        raise ValueError("coordinate actions do not satisfy structure relation")

    tau = coordinate_action_maps(solution)
    monoid = TransformationMonoid.generated(tau.values())
    groups = []
    for audit in green_branch_audits(solution):
        r_class = audit.r_class
        if len(r_class) < 2:
            continue
        stabilizer = tuple(
            element
            for element in monoid.elements
            if all(monoid.mul(source, element) in set(r_class) for source in r_class)
        )
        actions = tuple(
            sorted(
                {
                    action
                    for action in (
                        _permutation_action_on_r_class(monoid, r_class, element)
                        for element in stabilizer
                    )
                    if action is not None
                }
            )
        )
        if len(actions) <= 1:
            continue
        group = permutation_group_from_generators(actions, degree=len(r_class))
        groups.append(
            SchutzenbergerActionGroup(
                r_class=r_class,
                actions=actions,
                group=group,
            )
        )
    return tuple(sorted(groups, key=repr))


def context_words_by_target(
    audit: GreenBranchAudit, max_depth: int
) -> Dict[Transformation, Tuple[ContextWord, ...]]:
    """Return retained nearest-first context words of length at most max_depth."""

    if max_depth < 0:
        raise ValueError("max_depth must be nonnegative")
    targets = edge_target_map(audit)
    by_target = {target: {tuple()} for target in audit.r_class}
    exact_previous = {target: {tuple()} for target in audit.r_class}
    incoming: Dict[Transformation, list[EdgeGerm]] = defaultdict(list)
    for edge, target in targets.items():
        incoming[target].append(edge)
    for _depth in range(1, max_depth + 1):
        exact_current = {target: set() for target in audit.r_class}
        for target in audit.r_class:
            for edge in incoming[target]:
                for tail in exact_previous[edge_source(edge)]:
                    word = (edge,) + tail
                    exact_current[target].add(word)
                    by_target[target].add(word)
        exact_previous = exact_current
    return {
        target: tuple(sorted(words, key=repr))
        for target, words in by_target.items()
    }


def apply_completed_profile(
    audit: GreenBranchAudit, q: EdgeGerm, word: ContextWord
) -> ContextWord | None:
    """Apply the partial recursive profile R_q to one finite context word."""

    if not word:
        return tuple()
    row = completed_row_map(audit).get((q, word[0]))
    if row is None:
        return None
    tail = apply_completed_profile(audit, row.q_under_a, word[1:])
    if tail is None:
        return None
    return (row.a_under_q,) + tail


def _sort_key(value) -> str:
    return repr(value)


def completed_profile_signature(
    audit: GreenBranchAudit,
    q: EdgeGerm,
    max_depth: int,
    *,
    atoms: bool = False,
):
    """Return a deterministic finite-depth profile signature for R_q.

    With ``atoms=True``, the profile is aggregated by atom words.  Multiple
    outputs for the same atom input are retained, so atom-level nondeterminism
    remains visible to the caller.
    """

    targets = edge_target_map(audit)
    words = context_words_by_target(audit, max_depth)[edge_source(q)]
    rows = []
    for word in words:
        image = apply_completed_profile(audit, q, word)
        if atoms:
            source_key = atom_word(audit, word)
            image_key = None if image is None else atom_word(audit, image)
        else:
            source_key = word
            image_key = image
        rows.append((source_key, image_key))
    if not atoms:
        return tuple(sorted(rows, key=_sort_key))
    grouped: Dict[Tuple[int, ...], set[Tuple[int, ...] | None]] = defaultdict(set)
    for source_key, image_key in rows:
        grouped[source_key].add(image_key)
    return tuple(
        sorted(
            (
                source_key,
                tuple(sorted(grouped[source_key], key=_sort_key)),
            )
            for source_key in grouped
        )
    )


@dataclass(frozen=True)
class DepthObserverSummary:
    max_depth: int
    context_word_counts: Tuple[Tuple[str, int], ...]
    undefined_profile_count: int
    atom_profile_conflict_count: int
    hidden_profile_split_count: int


@dataclass(frozen=True)
class BoundedMorphism:
    source: Transformation
    target: Transformation
    images: Tuple[ContextWord | None, ...]


@dataclass(frozen=True)
class BoundedCategorySummary:
    max_depth: int
    morphism_count: int
    truncated: bool
    hidden_atom_trivial_loop_count: int
    hidden_bijective_loop_count: int
    undefined_image_count: int


@dataclass(frozen=True)
class BoundedAtomTrivialLoopGroupSummary:
    """Finite-depth group part of atom-trivial completed-context loops."""

    source: Transformation
    max_depth: int
    word_count: int
    atom_trivial_bijective_loop_count: int
    nonidentity_loop_count: int
    truncated: bool
    group: FiniteGroup

    @property
    def group_order(self) -> int:
        return len(self.group.elements)


def depth_observer_summary(audit: GreenBranchAudit, max_depth: int) -> DepthObserverSummary:
    """Summarize finite-depth completed-context observers for one R-class."""

    targets = edge_target_map(audit)
    words_by_target = context_words_by_target(audit, max_depth)
    undefined = 0
    atom_conflicts = 0
    profile_groups: Dict[
        Tuple[Transformation, Transformation, int, object], set[object]
    ] = defaultdict(set)
    for q in audit.edge_germs:
        for word in words_by_target[edge_source(q)]:
            if apply_completed_profile(audit, q, word) is None:
                undefined += 1
        atom_profile = completed_profile_signature(audit, q, max_depth, atoms=True)
        atom_conflicts += sum(
            1
            for _source_key, image_keys in atom_profile
            if len(image_keys) > 1
        )
        key = (edge_source(q), targets[q], atom_index(audit, q), atom_profile)
        profile_groups[key].add(
            completed_profile_signature(audit, q, max_depth, atoms=False)
        )
    hidden_splits = sum(1 for values in profile_groups.values() if len(values) > 1)
    return DepthObserverSummary(
        max_depth=max_depth,
        context_word_counts=tuple(
            sorted((repr(target), len(words)) for target, words in words_by_target.items())
        ),
        undefined_profile_count=undefined,
        atom_profile_conflict_count=atom_conflicts,
        hidden_profile_split_count=hidden_splits,
    )


def _morphism_map(
    words_by_target: Mapping[Transformation, Tuple[ContextWord, ...]],
    morphism: BoundedMorphism,
) -> Dict[ContextWord, ContextWord | None]:
    return dict(zip(words_by_target[morphism.source], morphism.images))


def _compose_morphisms(
    words_by_target: Mapping[Transformation, Tuple[ContextWord, ...]],
    left: BoundedMorphism,
    right: BoundedMorphism,
) -> BoundedMorphism:
    """Return right after left."""

    if left.target != right.source:
        raise ValueError("morphism targets do not match")
    right_map = _morphism_map(words_by_target, right)
    images = []
    for image in left.images:
        if image is None:
            images.append(None)
        else:
            images.append(right_map.get(image))
    return BoundedMorphism(left.source, right.target, tuple(images))


def _identity_morphism(
    words_by_target: Mapping[Transformation, Tuple[ContextWord, ...]],
    target: Transformation,
) -> BoundedMorphism:
    return BoundedMorphism(target, target, words_by_target[target])


def _generator_morphism(
    audit: GreenBranchAudit,
    words_by_target: Mapping[Transformation, Tuple[ContextWord, ...]],
    q: EdgeGerm,
) -> BoundedMorphism:
    targets = edge_target_map(audit)
    source = edge_source(q)
    target = targets[q]
    target_words = set(words_by_target[target])
    images = []
    for word in words_by_target[source]:
        image = apply_completed_profile(audit, q, word)
        images.append(image if image in target_words else None)
    return BoundedMorphism(source, target, tuple(images))


def bounded_completed_category(
    audit: GreenBranchAudit, max_depth: int, morphism_limit: int = 10000
) -> Tuple[Tuple[BoundedMorphism, ...], bool]:
    """Generate the bounded deterministic completed-context category."""

    words_by_target = context_words_by_target(audit, max_depth)
    morphisms = {
        _identity_morphism(words_by_target, target)
        for target in audit.r_class
    }
    morphisms.update(
        _generator_morphism(audit, words_by_target, q)
        for q in audit.edge_germs
    )
    queue = deque(morphisms)
    truncated = False
    while queue:
        current = queue.popleft()
        snapshot = tuple(morphisms)
        for other in snapshot:
            candidates = []
            if current.target == other.source:
                candidates.append(_compose_morphisms(words_by_target, current, other))
            if other.target == current.source:
                candidates.append(_compose_morphisms(words_by_target, other, current))
            for candidate in candidates:
                if candidate in morphisms:
                    continue
                morphisms.add(candidate)
                if len(morphisms) > morphism_limit:
                    truncated = True
                    return tuple(sorted(morphisms, key=repr)), truncated
                queue.append(candidate)
    return tuple(sorted(morphisms, key=repr)), truncated


def _is_atom_identity_morphism(
    audit: GreenBranchAudit,
    words_by_target: Mapping[Transformation, Tuple[ContextWord, ...]],
    morphism: BoundedMorphism,
) -> bool:
    if morphism.source != morphism.target:
        return False
    for word, image in zip(words_by_target[morphism.source], morphism.images):
        if image is None or atom_word(audit, image) != atom_word(audit, word):
            return False
    return True


def _is_full_identity_morphism(
    words_by_target: Mapping[Transformation, Tuple[ContextWord, ...]],
    morphism: BoundedMorphism,
) -> bool:
    return morphism.source == morphism.target and morphism.images == words_by_target[morphism.source]


def _is_total_bijective_loop(
    words_by_target: Mapping[Transformation, Tuple[ContextWord, ...]],
    morphism: BoundedMorphism,
) -> bool:
    if morphism.source != morphism.target or any(image is None for image in morphism.images):
        return False
    return set(morphism.images) == set(words_by_target[morphism.source])


def bounded_category_summary(
    audit: GreenBranchAudit, max_depth: int, morphism_limit: int = 10000
) -> BoundedCategorySummary:
    words_by_target = context_words_by_target(audit, max_depth)
    morphisms, truncated = bounded_completed_category(
        audit, max_depth, morphism_limit=morphism_limit
    )
    hidden_atom_trivial = 0
    hidden_bijective = 0
    undefined = 0
    for morphism in morphisms:
        undefined += sum(1 for image in morphism.images if image is None)
        if not _is_atom_identity_morphism(audit, words_by_target, morphism):
            continue
        if _is_full_identity_morphism(words_by_target, morphism):
            continue
        hidden_atom_trivial += 1
        if _is_total_bijective_loop(words_by_target, morphism):
            hidden_bijective += 1
    return BoundedCategorySummary(
        max_depth=max_depth,
        morphism_count=len(morphisms),
        truncated=truncated,
        hidden_atom_trivial_loop_count=hidden_atom_trivial,
        hidden_bijective_loop_count=hidden_bijective,
        undefined_image_count=undefined,
    )


def _morphism_permutation(
    words_by_target: Mapping[Transformation, Tuple[ContextWord, ...]],
    morphism: BoundedMorphism,
) -> Permutation:
    words = words_by_target[morphism.source]
    index = {word: i for i, word in enumerate(words)}
    return tuple(index[image] for image in morphism.images if image is not None)


def bounded_atom_trivial_loop_group_summaries(
    audit: GreenBranchAudit, max_depth: int, morphism_limit: int = 10000
) -> Tuple[BoundedAtomTrivialLoopGroupSummary, ...]:
    """Return finite permutation groups from atom-trivial context loops.

    Raw atom-trivial loops may collapse finite context sets rather than act by
    permutations.  Such reset-like loops are useful diagnostics, but they are
    not residual braid motions: residual actions are permutations.  This helper
    extracts only the total bijective atom-trivial loops at the chosen finite
    depth and records the finite group they generate on each context fibre.
    """

    words_by_target = context_words_by_target(audit, max_depth)
    morphisms, truncated = bounded_completed_category(
        audit, max_depth, morphism_limit=morphism_limit
    )
    generators_by_source: Dict[Transformation, set[Permutation]] = {
        source: set() for source in audit.r_class
    }
    for morphism in morphisms:
        if not _is_atom_identity_morphism(audit, words_by_target, morphism):
            continue
        if not _is_total_bijective_loop(words_by_target, morphism):
            continue
        generators_by_source[morphism.source].add(
            _morphism_permutation(words_by_target, morphism)
        )
    summaries = []
    for source in audit.r_class:
        words = words_by_target[source]
        degree = len(words)
        group = permutation_group_from_generators(
            generators_by_source[source],
            degree=degree,
        )
        identity = tuple(range(degree))
        summaries.append(
            BoundedAtomTrivialLoopGroupSummary(
                source=source,
                max_depth=max_depth,
                word_count=degree,
                atom_trivial_bijective_loop_count=len(generators_by_source[source]),
                nonidentity_loop_count=sum(
                    1
                    for permutation in generators_by_source[source]
                    if permutation != identity
                ),
                truncated=truncated,
                group=group,
            )
        )
    return tuple(sorted(summaries, key=repr))


def green_branch_audits(solution: FiniteBraidedSet) -> Tuple[GreenBranchAudit, ...]:
    """Audit retained edge-germs in regular Green R-classes of tau(X).

    For an R-class C, retained edge-germs are pairs ``(s,x)`` with ``s in C``
    and ``s tau_x in C``. Completed YBE rows impose the atom relation
    ``p(q^a)=p(q)``. The failure list records direct branch-choice
    non-determinism: same edge ``a`` and same atom of ``q``, but different
    atoms for ``a^q``.
    """

    failures = coordinate_action_relation_failures(solution)
    if failures:
        raise ValueError("coordinate actions do not satisfy structure relation")

    tau = coordinate_action_maps(solution)
    monoid = TransformationMonoid.generated(tau.values())
    regular = {element for j_class in monoid.regular_j_classes() for element in j_class}
    audits = []
    for r_class in monoid.r_classes():
        if not any(element in regular for element in r_class):
            continue
        class_set = frozenset(r_class)
        edge_germs = tuple(
            sorted(
                (
                    (s, x)
                    for s in r_class
                    for x in solution.elements
                    if monoid.mul(s, tau[x]) in class_set
                ),
                key=repr,
            )
        )
        edge_targets = tuple(
            sorted(
                (
                    (edge, monoid.mul(edge[0], tau[edge[1]]))
                    for edge in edge_germs
                ),
                key=repr,
            )
        )
        edge_set = frozenset(edge_germs)
        rows = []
        uf = UnionFind(edge_germs)
        for s, x in edge_germs:
            sx = monoid.mul(s, tau[x])
            for y in solution.elements:
                q = (sx, y)
                if q not in edge_set:
                    continue
                u, v = solution.R[(x, y)]
                q_under_a = (s, u)
                a_under_q = (monoid.mul(s, tau[u]), v)
                if q_under_a not in edge_set or a_under_q not in edge_set:
                    continue
                row = BranchRow((s, x), q, q_under_a, a_under_q)
                rows.append(row)
                uf.union(q_under_a, q)
        partition = uf.partition()
        row_by_a_and_q_atom: Dict[Tuple[EdgeGerm, int], Tuple[EdgeGerm, EdgeGerm]] = {}
        branch_failures = []
        for row in rows:
            q_atom = _block_index(partition, row.q)
            aq_atom = _block_index(partition, row.a_under_q)
            key = (row.a, q_atom)
            if key in row_by_a_and_q_atom:
                previous_q, previous_aq = row_by_a_and_q_atom[key]
                if _block_index(partition, previous_aq) != aq_atom:
                    branch_failures.append(
                        (row.a, previous_q, row.q, previous_aq, row.a_under_q)
                    )
            else:
                row_by_a_and_q_atom[key] = (row.q, row.a_under_q)
        audits.append(
            GreenBranchAudit(
                r_class=tuple(r_class),
                edge_germs=edge_germs,
                edge_targets=edge_targets,
                rows=tuple(rows),
                atom_partition=partition,
                branch_choice_failures=tuple(branch_failures),
            )
        )
    return tuple(audits)
