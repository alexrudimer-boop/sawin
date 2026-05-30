from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from typing import Iterable, Mapping, Sequence, Tuple

from .artin_longitudes import BraidWord, FreeWord
from .finite_braided_set import FiniteBraidedSet
from .finite_group import FiniteGroup
from .residual import action_permutation, permutation_order

Permutation = Tuple[int, ...]


@dataclass(frozen=True)
class PureGeneratorOrderRow:
    braid_index: int
    tuple_count: int
    generator_orders: Tuple[int, ...]
    max_order: int


@dataclass(frozen=True)
class PureSubgroupGrowthRow:
    braid_index: int
    tuple_count: int
    generator_count: int
    subgroup_size: int | None
    subgroup_exponent: int | None
    truncated: bool


@dataclass(frozen=True)
class LawBraidActionCertificate:
    braid_index: int
    tuple_count: int
    generator_image_subgroup_size: int
    generator_image_subgroup_exponent: int
    word_is_law_on_image_subgroup: bool
    evaluated_word_is_identity: bool
    direct_braid_is_identity: bool
    direct_matches_evaluated: bool


@dataclass(frozen=True)
class AssignedLawSeparation:
    """A law on detector groups that moves a specific permutation assignment."""

    arity: int
    target_degree: int
    separating_word: FreeWord | None
    evaluated_permutation: Permutation | None
    moved_index: int | None


@dataclass(frozen=True)
class PointPushingMarkedQuotientAudit:
    """Exact finite arity check for the derivative-detector quotient criterion."""

    group_order: int
    arity: int
    braid_index: int
    detector_state_count: int
    ybe_tuple_count: int
    pair_subgroup_size: int | None
    detector_image_size: int | None
    action_image_size: int | None
    truncated: bool
    witness_word: FreeWord | None
    witness_action_value: Permutation | None
    moved_index: int | None

    @property
    def found_kernel_mover(self) -> bool:
        return self.witness_word is not None and self.moved_index is not None

    @property
    def marked_quotient_holds(self) -> bool:
        return not self.truncated and not self.found_kernel_mover

    @property
    def vertical_kernel_trivial(self) -> bool:
        """Whether ``<(d_i,h_i)>`` has no nontrivial ``(1,p)`` witness."""

        return self.marked_quotient_holds


@dataclass(frozen=True)
class PointPushingVerticalWitnessCertificate:
    """Checked finite row for a nontrivial paired vertical-kernel witness."""

    group_order: int
    arity: int
    braid_index: int
    detector_state_count: int
    ybe_tuple_count: int
    word: FreeWord
    braid_word: BraidWord
    detector_word_identity: bool
    evaluated_action_identity: bool
    direct_braid_identity: bool
    direct_matches_evaluated: bool
    moved_index: int | None
    moved_tuple: Tuple[object, ...] | None
    moved_tuple_image: Tuple[object, ...] | None

    @property
    def moves_solution(self) -> bool:
        return self.moved_index is not None and not self.direct_braid_identity

    @property
    def valid_vertical_witness(self) -> bool:
        return (
            self.detector_word_identity
            and self.direct_matches_evaluated
            and self.moves_solution
        )


@dataclass(frozen=True)
class PointPushingVarietyEscapeAudit:
    """Bounded finite row for a point-pushing action-image variety escape."""

    symmetric_degree: int
    point_pushing_arity: int
    law_arity: int
    braid_index: int
    tuple_count: int
    action_image_size: int | None
    truncated: bool
    assignment_count_checked: int
    separating_word: FreeWord | None
    assignment_representatives: Tuple[FreeWord, ...]
    substituted_point_pushing_word: FreeWord | None
    evaluated_permutation: Permutation | None
    direct_braid_permutation: Permutation | None
    moved_index: int | None
    substituted_word_is_symmetric_law: bool | None

    @property
    def found_variety_escape(self) -> bool:
        return self.separating_word is not None and self.moved_index is not None

    @property
    def direct_matches_evaluated(self) -> bool:
        return (
            self.evaluated_permutation is not None
            and self.direct_braid_permutation is not None
            and self.evaluated_permutation == self.direct_braid_permutation
        )

    @property
    def substituted_word_gives_point_pushing_mover(self) -> bool:
        return (
            self.found_variety_escape
            and self.substituted_word_is_symmetric_law is True
            and self.direct_matches_evaluated
        )


@dataclass(frozen=True)
class PointPushingVarietyPrefixAudit:
    """Bounded prefix scan for one proposed symmetric variety."""

    symmetric_degree: int
    max_point_pushing_arity: int
    law_arity: int
    max_length: int
    rows: Tuple[PointPushingVarietyEscapeAudit, ...]

    @property
    def row_count(self) -> int:
        return len(self.rows)

    @property
    def arities_are_initial_segment(self) -> bool:
        return tuple(row.point_pushing_arity for row in self.rows) == tuple(
            range(1, self.row_count + 1)
        )

    @property
    def truncated_rows(self) -> Tuple[PointPushingVarietyEscapeAudit, ...]:
        return tuple(row for row in self.rows if row.truncated)

    @property
    def escape_rows(self) -> Tuple[PointPushingVarietyEscapeAudit, ...]:
        return tuple(row for row in self.rows if row.found_variety_escape)

    @property
    def escaped_arities(self) -> Tuple[int, ...]:
        return tuple(row.point_pushing_arity for row in self.escape_rows)

    @property
    def all_escape_rows_give_movers(self) -> bool:
        return all(row.substituted_word_gives_point_pushing_mover for row in self.escape_rows)

    @property
    def no_bounded_escape_found(self) -> bool:
        return not self.escape_rows and not self.truncated_rows


@dataclass(frozen=True)
class PointPushingExponentEscapeAudit:
    """One finite row where a power law moves a point-pushing action image."""

    law_bound: int
    point_pushing_arity: int
    exponent_bound: int
    braid_index: int
    tuple_count: int
    action_image_size: int | None
    truncated: bool
    escaping_element_order: int | None
    escaping_element_word: FreeWord | None
    exponent_law_word: FreeWord | None
    evaluated_permutation: Permutation | None
    direct_braid_permutation: Permutation | None
    symmetric_identity_longitude_signature: bool | None
    moved_index: int | None

    @property
    def found_exponent_escape(self) -> bool:
        return self.escaping_element_word is not None and self.moved_index is not None

    @property
    def direct_matches_evaluated(self) -> bool:
        return (
            self.evaluated_permutation is not None
            and self.direct_braid_permutation is not None
            and self.evaluated_permutation == self.direct_braid_permutation
        )

    @property
    def gives_power_law_mover(self) -> bool:
        return self.found_exponent_escape and self.direct_matches_evaluated

    @property
    def exposes_naive_law_gap(self) -> bool:
        return self.gives_power_law_mover and self.symmetric_identity_longitude_signature is False


def identity_permutation(size: int) -> Permutation:
    return tuple(range(size))


def compose_permutations(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    if len(left) != len(right):
        raise ValueError("permutations must have the same size")
    return tuple(left[right[i]] for i in range(len(left)))


def invert_permutation(permutation: Permutation) -> Permutation:
    out = [0] * len(permutation)
    for i, image in enumerate(permutation):
        out[image] = i
    return tuple(out)


def generated_permutation_subgroup(generators: Iterable[Permutation], max_size: int | None = None):
    gens = tuple(generators)
    if not gens:
        return {tuple()}
    size = len(gens[0])
    identity = identity_permutation(size)
    symmetric_gens = set(gens)
    symmetric_gens.update(invert_permutation(gen) for gen in gens)
    subgroup = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for gen in symmetric_gens:
            candidate = compose_permutations(gen, current)
            if candidate in subgroup:
                continue
            subgroup.add(candidate)
            if max_size is not None and len(subgroup) > max_size:
                raise ValueError("generated subgroup exceeded max_size")
            queue.append(candidate)
    return subgroup


def generated_permutation_subgroup_with_words(
    generators: Mapping[int, Permutation],
    max_size: int | None = None,
) -> dict[Permutation, FreeWord]:
    """Generate a permutation subgroup and remember words in the generators."""

    gens = tuple(sorted(generators.items()))
    if not gens:
        return {tuple(): tuple()}
    size = len(gens[0][1])
    identity = identity_permutation(size)
    moves = []
    for index, generator in gens:
        moves.append((generator, ((index, 1),)))
        moves.append((invert_permutation(generator), ((index, -1),)))
    words: dict[Permutation, FreeWord] = {identity: tuple()}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        current_word = words[current]
        for move, move_word in moves:
            candidate = compose_permutations(move, current)
            if candidate in words:
                continue
            candidate_word = _reduce_free_word(current_word + move_word)
            words[candidate] = candidate_word
            if max_size is not None and len(words) > max_size:
                raise ValueError("generated subgroup exceeded max_size")
            queue.append(candidate)
    return words


def permutation_group_from_subgroup(subgroup: Iterable[Permutation]):
    """View a finite permutation subgroup as a `FiniteGroup`."""

    from .finite_group import FiniteGroup

    elements = tuple(sorted(subgroup))
    if not elements:
        return FiniteGroup((tuple(),), tuple(), {(tuple(), tuple()): tuple()})
    identity = identity_permutation(len(elements[0]))
    table = {
        (left, right): compose_permutations(left, right)
        for left in elements
        for right in elements
    }
    return FiniteGroup(elements, identity, table)


def evaluate_free_word_on_permutations(
    word: FreeWord, generator_images: Mapping[int, Permutation]
) -> Permutation:
    if not generator_images:
        if word:
            raise ValueError("missing generator images")
        return tuple()
    size = len(next(iter(generator_images.values())))
    out = identity_permutation(size)
    for generator, exponent in word:
        image = generator_images[generator]
        if exponent < 0:
            image = invert_permutation(image)
        out = compose_permutations(image, out)
    return out


def _reduce_free_word(word: FreeWord) -> FreeWord:
    from .artin_longitudes import reduce_free_word

    return reduce_free_word(word)


def _invert_free_word(word: FreeWord) -> FreeWord:
    from .artin_longitudes import invert_free_word

    return invert_free_word(word)


def substitute_free_word(word: FreeWord, substitutions: Sequence[FreeWord]) -> FreeWord:
    """Substitute words in ``F_k`` for variables of another free word."""

    out: FreeWord = tuple()
    for generator, exponent in word:
        replacement = substitutions[generator]
        if exponent < 0:
            replacement = _invert_free_word(replacement)
        out = _reduce_free_word(out + replacement)
    return out


def short_law_separating_permutation_assignment(
    law_groups: Sequence[FiniteGroup],
    generator_images: Mapping[int, Permutation],
    *,
    max_length: int,
) -> AssignedLawSeparation:
    """Find a short finite-group law that moves a fixed permutation tuple.

    This is the assigned-generator form needed by normalized-law obstruction
    searches.  It is stronger than merely finding a word that is not a law on
    the subgroup generated by ``generator_images``: the returned word is
    certified to evaluate nontrivially on this particular tuple.
    """

    from .group_laws import is_law_on_group, reduced_free_words

    if not generator_images:
        return AssignedLawSeparation(
            arity=0,
            target_degree=0,
            separating_word=None,
            evaluated_permutation=None,
            moved_index=None,
        )
    arity = 1 + max(generator_images)
    target_degree = len(next(iter(generator_images.values())))
    identity = identity_permutation(target_degree)
    for word in reduced_free_words(arity, max_length):
        if not all(is_law_on_group(group, word, arity=arity) for group in law_groups):
            continue
        evaluated = evaluate_free_word_on_permutations(word, generator_images)
        if evaluated == identity:
            continue
        moved_index = next(
            index
            for index, image in enumerate(evaluated)
            if image != index
        )
        return AssignedLawSeparation(
            arity=arity,
            target_degree=target_degree,
            separating_word=word,
            evaluated_permutation=evaluated,
            moved_index=moved_index,
        )
    return AssignedLawSeparation(
        arity=arity,
        target_degree=target_degree,
        separating_word=None,
        evaluated_permutation=None,
        moved_index=None,
    )


def point_pushing_marked_quotient_audit(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    arity: int,
    *,
    max_detector_states: int | None = None,
    max_pair_subgroup_size: int | None = None,
) -> PointPushingMarkedQuotientAudit:
    """Audit whether the YBE point-pushing image is a marked detector quotient.

    The audit generates the paired subgroup
    ``<(d_i,h_i)> <= D_k(G) x P_k(X)``.  A pair ``(1, nonidentity)`` is exactly
    a point-pushing word lying in ``K_G`` whose action on ``X`` is nontrivial.
    """

    from .braid_laws import (
        point_pushing_derivative_detector_generators,
        pure_braid_generator,
    )

    if arity < 1:
        raise ValueError("arity must be positive")
    n = arity + 1
    detector_images = point_pushing_derivative_detector_generators(
        group,
        arity,
        max_states=max_detector_states,
    )
    action_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(arity)
    }
    action_images = braid_images_for_words(solution, n, action_braids)
    detector_identity = identity_permutation(
        len(next(iter(detector_images.values())))
    )
    action_identity = identity_permutation(
        len(next(iter(action_images.values())))
    )
    moves = []
    for generator in range(arity):
        detector = detector_images[generator]
        action = action_images[generator]
        moves.append((detector, action, ((generator, 1),)))
        moves.append(
            (
                invert_permutation(detector),
                invert_permutation(action),
                ((generator, -1),),
            )
        )
    identity_pair = (detector_identity, action_identity)
    words: dict[Tuple[Permutation, Permutation], FreeWord] = {identity_pair: tuple()}
    queue = deque([identity_pair])
    truncated = False
    witness_word: FreeWord | None = None
    witness_action: Permutation | None = None
    moved_index: int | None = None
    while queue:
        current = queue.popleft()
        current_word = words[current]
        for detector_move, action_move, move_word in moves:
            candidate = (
                compose_permutations(detector_move, current[0]),
                compose_permutations(action_move, current[1]),
            )
            if candidate in words:
                continue
            candidate_word = _reduce_free_word(current_word + move_word)
            if candidate[0] == detector_identity and candidate[1] != action_identity:
                witness_word = candidate_word
                witness_action = candidate[1]
                moved_index = next(
                    index
                    for index, image in enumerate(candidate[1])
                    if image != index
                )
                words[candidate] = candidate_word
                queue.clear()
                break
            words[candidate] = candidate_word
            if (
                max_pair_subgroup_size is not None
                and len(words) > max_pair_subgroup_size
            ):
                truncated = True
                queue.clear()
                break
            queue.append(candidate)
    detector_projection = {pair[0] for pair in words}
    action_projection = {pair[1] for pair in words}
    return PointPushingMarkedQuotientAudit(
        group_order=len(group.elements),
        arity=arity,
        braid_index=n,
        detector_state_count=len(detector_identity),
        ybe_tuple_count=len(action_identity),
        pair_subgroup_size=None if truncated else len(words),
        detector_image_size=None if truncated else len(detector_projection),
        action_image_size=None if truncated else len(action_projection),
        truncated=truncated,
        witness_word=witness_word,
        witness_action_value=witness_action,
        moved_index=moved_index,
    )


def point_pushing_vertical_witness_certificate(
    solution: FiniteBraidedSet,
    group: FiniteGroup,
    word: FreeWord,
    arity: int,
    *,
    max_detector_states: int | None = None,
) -> PointPushingVerticalWitnessCertificate:
    """Check one paired vertical-kernel witness.

    A valid certificate means the point-pushed braid is in ``K_G`` by the
    derivative detector criterion and still acts nontrivially on ``X``.
    """

    from .braid_laws import (
        law_word_on_last_strand,
        point_pushing_derivative_detector_generators,
        pure_braid_generator,
    )

    if arity < 1:
        raise ValueError("arity must be positive")
    for generator, _exponent in word:
        if generator < 0 or generator >= arity:
            raise ValueError(f"free generator {generator} outside arity {arity}")

    n, braid = law_word_on_last_strand(word, arity)
    detector_images = point_pushing_derivative_detector_generators(
        group,
        arity,
        max_states=max_detector_states,
    )
    detector_value = evaluate_free_word_on_permutations(word, detector_images)
    detector_identity = identity_permutation(len(detector_value))

    action_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(arity)
    }
    action_images = braid_images_for_words(solution, n, action_braids)
    evaluated_action = evaluate_free_word_on_permutations(word, action_images)
    direct_action = action_permutation(solution, n, braid)
    action_identity = identity_permutation(len(direct_action))

    moved_index = None
    moved_tuple = None
    moved_tuple_image = None
    if direct_action != action_identity:
        moved_index = next(
            index for index, image in enumerate(direct_action) if image != index
        )
        tuples = tuple(product(solution.elements, repeat=n))
        moved_tuple = tuples[moved_index]
        moved_tuple_image = tuples[direct_action[moved_index]]

    return PointPushingVerticalWitnessCertificate(
        group_order=len(group.elements),
        arity=arity,
        braid_index=n,
        detector_state_count=len(detector_identity),
        ybe_tuple_count=len(action_identity),
        word=tuple(word),
        braid_word=braid,
        detector_word_identity=detector_value == detector_identity,
        evaluated_action_identity=evaluated_action == action_identity,
        direct_braid_identity=direct_action == action_identity,
        direct_matches_evaluated=direct_action == evaluated_action,
        moved_index=moved_index,
        moved_tuple=moved_tuple,
        moved_tuple_image=moved_tuple_image,
    )


def braid_word_permutation_image(
    solution: FiniteBraidedSet, n: int, braid_word: BraidWord
) -> Permutation:
    return action_permutation(solution, n, braid_word)


def braid_images_for_words(
    solution: FiniteBraidedSet, n: int, words: Mapping[int, BraidWord]
) -> dict[int, Permutation]:
    return {generator: braid_word_permutation_image(solution, n, word) for generator, word in words.items()}


def law_braid_action_certificate(
    solution: FiniteBraidedSet,
    word: FreeWord,
    arity: int,
    *,
    max_subgroup_size: int | None = None,
) -> LawBraidActionCertificate:
    """Certify the fixed-image obstruction for an embedded free law.

    The free word is embedded into `B_{arity+1}` using the standard pure
    generators `A_{r+1,n}`.  The certificate compares two computations:
    direct action of the embedded braid on `X^n`, and evaluation of the free
    word in the finite subgroup of `Sym(X^n)` generated by those pure-generator
    images.  If the word is a law on that subgroup, the embedded braid must act
    trivially on this fixed finite YBE action image.
    """

    from .braid_laws import law_word_on_last_strand, pure_braid_generator
    from .group_laws import group_exponent, is_law_on_group

    n, braid = law_word_on_last_strand(word, arity)
    generator_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(arity)
    }
    images = braid_images_for_words(solution, n, generator_braids)
    subgroup = generated_permutation_subgroup(
        images.values(), max_size=max_subgroup_size
    )
    subgroup_as_group = permutation_group_from_subgroup(subgroup)
    evaluated = evaluate_free_word_on_permutations(word, images)
    identity = identity_permutation(len(evaluated))
    direct = braid_word_permutation_image(solution, n, braid)
    return LawBraidActionCertificate(
        braid_index=n,
        tuple_count=len(solution.elements) ** n,
        generator_image_subgroup_size=len(subgroup),
        generator_image_subgroup_exponent=group_exponent(subgroup_as_group),
        word_is_law_on_image_subgroup=is_law_on_group(
            subgroup_as_group, word, arity=arity
        ),
        evaluated_word_is_identity=evaluated == identity,
        direct_braid_is_identity=direct == identity,
        direct_matches_evaluated=direct == evaluated,
    )


def point_pushing_variety_escape_audit(
    solution: FiniteBraidedSet,
    symmetric_degree: int,
    point_pushing_arity: int,
    *,
    law_arity: int,
    max_length: int,
    max_subgroup_size: int | None = None,
    max_assignments: int | None = None,
) -> PointPushingVarietyEscapeAudit:
    """Search one bounded point-pushing action image for a variety escape.

    A returned separating word is a law on ``S_m`` but evaluates nontrivially
    on the computed action image ``P_k(X)``.  The audit also records
    representatives for the chosen assignment in the marked pure generators,
    and verifies that the substituted point-pushing word moves the direct YBE
    braid action.
    """

    from .braid_laws import law_word_on_last_strand, pure_braid_generator
    from .finite_group import symmetric_group
    from .group_laws import is_law_on_group, reduced_free_words

    if symmetric_degree < 1:
        raise ValueError("symmetric_degree must be positive")
    if point_pushing_arity < 1:
        raise ValueError("point_pushing_arity must be positive")
    if law_arity < 1:
        raise ValueError("law_arity must be positive")
    if max_length < 1:
        raise ValueError("max_length must be positive")

    n = point_pushing_arity + 1
    tuple_count = len(solution.elements) ** n
    generator_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(point_pushing_arity)
    }
    images = braid_images_for_words(solution, n, generator_braids)
    try:
        subgroup_words = generated_permutation_subgroup_with_words(
            images,
            max_size=max_subgroup_size,
        )
    except ValueError:
        return PointPushingVarietyEscapeAudit(
            symmetric_degree=symmetric_degree,
            point_pushing_arity=point_pushing_arity,
            law_arity=law_arity,
            braid_index=n,
            tuple_count=tuple_count,
            action_image_size=None,
            truncated=True,
            assignment_count_checked=0,
            separating_word=None,
            assignment_representatives=tuple(),
            substituted_point_pushing_word=None,
            evaluated_permutation=None,
            direct_braid_permutation=None,
            moved_index=None,
            substituted_word_is_symmetric_law=None,
        )

    subgroup = tuple(subgroup_words)
    detector = symmetric_group(symmetric_degree)
    identity = identity_permutation(tuple_count)
    assignment_count = 0
    for word in reduced_free_words(law_arity, max_length):
        if not is_law_on_group(detector, word, arity=law_arity):
            continue
        for assignment in product(subgroup, repeat=law_arity):
            assignment_count += 1
            if max_assignments is not None and assignment_count > max_assignments:
                return PointPushingVarietyEscapeAudit(
                    symmetric_degree=symmetric_degree,
                    point_pushing_arity=point_pushing_arity,
                    law_arity=law_arity,
                    braid_index=n,
                    tuple_count=tuple_count,
                    action_image_size=len(subgroup),
                    truncated=True,
                    assignment_count_checked=assignment_count - 1,
                    separating_word=None,
                    assignment_representatives=tuple(),
                    substituted_point_pushing_word=None,
                    evaluated_permutation=None,
                    direct_braid_permutation=None,
                    moved_index=None,
                    substituted_word_is_symmetric_law=None,
                )
            evaluated = evaluate_free_word_on_permutations(
                word,
                {index: value for index, value in enumerate(assignment)},
            )
            if evaluated == identity:
                continue
            representatives = tuple(subgroup_words[value] for value in assignment)
            substituted = substitute_free_word(word, representatives)
            braid_n, braid = law_word_on_last_strand(
                substituted,
                point_pushing_arity,
            )
            direct = braid_word_permutation_image(solution, braid_n, braid)
            moved_index = next(
                index
                for index, image in enumerate(evaluated)
                if image != index
            )
            return PointPushingVarietyEscapeAudit(
                symmetric_degree=symmetric_degree,
                point_pushing_arity=point_pushing_arity,
                law_arity=law_arity,
                braid_index=n,
                tuple_count=tuple_count,
                action_image_size=len(subgroup),
                truncated=False,
                assignment_count_checked=assignment_count,
                separating_word=word,
                assignment_representatives=representatives,
                substituted_point_pushing_word=substituted,
                evaluated_permutation=evaluated,
                direct_braid_permutation=direct,
                moved_index=moved_index,
                substituted_word_is_symmetric_law=is_law_on_group(
                    detector,
                    substituted,
                    arity=point_pushing_arity,
                ),
            )

    return PointPushingVarietyEscapeAudit(
        symmetric_degree=symmetric_degree,
        point_pushing_arity=point_pushing_arity,
        law_arity=law_arity,
        braid_index=n,
        tuple_count=tuple_count,
        action_image_size=len(subgroup),
        truncated=False,
        assignment_count_checked=assignment_count,
        separating_word=None,
        assignment_representatives=tuple(),
        substituted_point_pushing_word=None,
        evaluated_permutation=None,
        direct_braid_permutation=None,
        moved_index=None,
        substituted_word_is_symmetric_law=None,
    )


def point_pushing_variety_prefix_audit(
    solution: FiniteBraidedSet,
    symmetric_degree: int,
    max_point_pushing_arity: int,
    *,
    law_arity: int,
    max_length: int,
    max_subgroup_size: int | None = None,
    max_assignments_per_row: int | None = None,
) -> PointPushingVarietyPrefixAudit:
    """Run bounded point-pushing variety escape checks for arities ``1..K``."""

    if max_point_pushing_arity < 1:
        raise ValueError("max_point_pushing_arity must be positive")
    rows = tuple(
        point_pushing_variety_escape_audit(
            solution,
            symmetric_degree,
            arity,
            law_arity=law_arity,
            max_length=max_length,
            max_subgroup_size=max_subgroup_size,
            max_assignments=max_assignments_per_row,
        )
        for arity in range(1, max_point_pushing_arity + 1)
    )
    return PointPushingVarietyPrefixAudit(
        symmetric_degree=symmetric_degree,
        max_point_pushing_arity=max_point_pushing_arity,
        law_arity=law_arity,
        max_length=max_length,
        rows=rows,
    )


def _free_word_power_word(word: FreeWord, exponent: int) -> FreeWord:
    if exponent < 0:
        raise ValueError("exponent must be nonnegative")
    from .group_laws import multiply_free_words

    out: FreeWord = tuple()
    for _ in range(exponent):
        out = multiply_free_words(out, word)
    return out


def point_pushing_exponent_escape_audit(
    solution: FiniteBraidedSet,
    law_bound: int,
    point_pushing_arity: int,
    *,
    max_subgroup_size: int | None = None,
) -> PointPushingExponentEscapeAudit:
    """Audit one exponent-law point-pushing action escape.

    If an element of ``P_k(X)`` has order not dividing ``lcm(1,...,j)``, a
    representative word for that element, raised to this lcm, is a law on
    every group of order at most ``j`` but moves the YBE action.  This does
    *not* by itself certify finite-longitude invisibility: the returned row
    also records whether the corresponding braid has identity longitude data
    in ``S_j``.  Rows with ``exposes_naive_law_gap`` true are counterexamples
    to the naive implication "word law => point-pushing braid in K_G".
    """

    from .braid_laws import law_word_on_last_strand, pure_braid_generator
    from .artin_longitudes import has_identity_longitude_signature_streamed
    from .finite_group import symmetric_group
    from .group_laws import lcm_upto

    if law_bound < 1:
        raise ValueError("law_bound must be positive")
    if point_pushing_arity < 1:
        raise ValueError("point_pushing_arity must be positive")

    exponent_bound = lcm_upto(law_bound)
    n = point_pushing_arity + 1
    tuple_count = len(solution.elements) ** n
    generator_braids = {
        generator: pure_braid_generator(generator + 1, n)
        for generator in range(point_pushing_arity)
    }
    images = braid_images_for_words(solution, n, generator_braids)
    try:
        subgroup_words = generated_permutation_subgroup_with_words(
            images,
            max_size=max_subgroup_size,
        )
    except ValueError:
        return PointPushingExponentEscapeAudit(
            law_bound=law_bound,
            point_pushing_arity=point_pushing_arity,
            exponent_bound=exponent_bound,
            braid_index=n,
            tuple_count=tuple_count,
            action_image_size=None,
            truncated=True,
            escaping_element_order=None,
            escaping_element_word=None,
            exponent_law_word=None,
            evaluated_permutation=None,
            direct_braid_permutation=None,
            symmetric_identity_longitude_signature=None,
            moved_index=None,
        )

    identity = identity_permutation(tuple_count)
    for element, representative in subgroup_words.items():
        order = permutation_order(element)
        if exponent_bound % order == 0:
            continue
        exponent_word = _free_word_power_word(representative, exponent_bound)
        evaluated = evaluate_free_word_on_permutations(exponent_word, images)
        if evaluated == identity:
            continue
        braid_n, braid = law_word_on_last_strand(
            exponent_word,
            point_pushing_arity,
        )
        direct = braid_word_permutation_image(solution, braid_n, braid)
        symmetric_identity = has_identity_longitude_signature_streamed(
            symmetric_group(law_bound),
            braid_n,
            braid,
        )
        moved_index = next(
            index for index, image in enumerate(evaluated) if image != index
        )
        return PointPushingExponentEscapeAudit(
            law_bound=law_bound,
            point_pushing_arity=point_pushing_arity,
            exponent_bound=exponent_bound,
            braid_index=n,
            tuple_count=tuple_count,
            action_image_size=len(subgroup_words),
            truncated=False,
            escaping_element_order=order,
            escaping_element_word=representative,
            exponent_law_word=exponent_word,
            evaluated_permutation=evaluated,
            direct_braid_permutation=direct,
            symmetric_identity_longitude_signature=symmetric_identity,
            moved_index=moved_index,
        )

    return PointPushingExponentEscapeAudit(
        law_bound=law_bound,
        point_pushing_arity=point_pushing_arity,
        exponent_bound=exponent_bound,
        braid_index=n,
        tuple_count=tuple_count,
        action_image_size=len(subgroup_words),
        truncated=False,
        escaping_element_order=None,
        escaping_element_word=None,
        exponent_law_word=None,
        evaluated_permutation=None,
        direct_braid_permutation=None,
        symmetric_identity_longitude_signature=None,
        moved_index=None,
    )


def pure_generator_order_profile(
    solution: FiniteBraidedSet, max_q: int
) -> Tuple[PureGeneratorOrderRow, ...]:
    from .braid_laws import pure_braid_generator

    rows = []
    for q in range(2, max_q + 1):
        orders = tuple(
            permutation_order(action_permutation(solution, q, pure_braid_generator(i, q)))
            for i in range(1, q)
        )
        rows.append(
            PureGeneratorOrderRow(
                braid_index=q,
                tuple_count=len(solution.elements) ** q,
                generator_orders=orders,
                max_order=max(orders) if orders else 1,
            )
        )
    return tuple(rows)


def pure_subgroup_growth_profile(
    solution: FiniteBraidedSet,
    max_q: int,
    *,
    max_subgroup_size: int,
    max_tuple_count: int | None = None,
) -> Tuple[PureSubgroupGrowthRow, ...]:
    from .braid_laws import pure_braid_generator

    rows = []
    for q in range(2, max_q + 1):
        tuple_count = len(solution.elements) ** q
        if max_tuple_count is not None and tuple_count > max_tuple_count:
            rows.append(
                PureSubgroupGrowthRow(
                    braid_index=q,
                    tuple_count=tuple_count,
                    generator_count=q - 1,
                    subgroup_size=None,
                    subgroup_exponent=None,
                    truncated=True,
                )
            )
            continue
        pure_generators = {i - 1: pure_braid_generator(i, q) for i in range(1, q)}
        images = braid_images_for_words(solution, q, pure_generators)
        try:
            subgroup = generated_permutation_subgroup(
                images.values(), max_size=max_subgroup_size
            )
            from .group_laws import lcm

            exponent = 1
            for permutation in subgroup:
                exponent = lcm(exponent, permutation_order(permutation))
            rows.append(
                PureSubgroupGrowthRow(
                    braid_index=q,
                    tuple_count=tuple_count,
                    generator_count=len(images),
                    subgroup_size=len(subgroup),
                    subgroup_exponent=exponent,
                    truncated=False,
                )
            )
        except ValueError:
            rows.append(
                PureSubgroupGrowthRow(
                    braid_index=q,
                    tuple_count=tuple_count,
                    generator_count=len(images),
                    subgroup_size=None,
                    subgroup_exponent=None,
                    truncated=True,
                )
            )
    return tuple(rows)
