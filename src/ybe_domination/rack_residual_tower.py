from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import product
from typing import Optional, Tuple

from .finite_braided_set import Element, FiniteBraidedSet, Word
from .residual import action_permutation

Permutation = Tuple[int, ...]


@dataclass(frozen=True)
class RackResidualObstructionAudit:
    """Fixed-width audit for a detector rack versus one YBE solution."""

    n: int
    joint_image_size: Optional[int]
    solution_image_size: Optional[int]
    detector_image_size: Optional[int]
    kernel_size: Optional[int]
    kernel_contains_nonidentity: Optional[bool]
    first_witness_word: Optional[Word]
    first_moved_tuple: Optional[Tuple[Element, ...]]
    first_moved_tuple_image: Optional[Tuple[Element, ...]]
    truncated: bool

    @property
    def proves_fixed_width_domination_failure(self) -> bool:
        return not self.truncated and self.kernel_contains_nonidentity is True


def _compose_permutations(left: Permutation, right: Permutation) -> Permutation:
    if len(left) != len(right):
        raise ValueError("permutations must have the same size")
    return tuple(left[right[i]] for i in range(len(left)))


def _first_moved_tuple(
    solution: FiniteBraidedSet, n: int, permutation: Permutation
) -> Tuple[Optional[Tuple[Element, ...]], Optional[Tuple[Element, ...]]]:
    tuples = tuple(product(solution.elements, repeat=n))
    for index, image_index in enumerate(permutation):
        if index != image_index:
            return tuple(tuples[index]), tuple(tuples[image_index])
    return None, None


def rack_residual_obstruction_audit(
    solution: FiniteBraidedSet,
    detector: FiniteBraidedSet,
    n: int,
    state_limit: int = 100_000,
) -> RackResidualObstructionAudit:
    """Compute the fixed-arity rack-residual obstruction group.

    The audit closes the image of `B_n` on
    `solution^n x detector^n`.  It then checks whether the kernel of the
    projection to the detector coordinate has a nonidentity solution
    projection.  For fixed `solution`, `detector`, and `n` this is a finite
    computation; the Sawin problem is the remaining unbounded quantifier over
    detector racks and braid arities.
    """

    if n < 1:
        raise ValueError("braid degree must be positive")
    solution_identity = tuple(range(len(solution.elements) ** n))
    detector_identity = tuple(range(len(detector.elements) ** n))
    alphabet = tuple(i for generator in range(1, n) for i in (generator, -generator))
    if not alphabet:
        return RackResidualObstructionAudit(
            n=n,
            joint_image_size=1,
            solution_image_size=1,
            detector_image_size=1,
            kernel_size=1,
            kernel_contains_nonidentity=False,
            first_witness_word=None,
            first_moved_tuple=None,
            first_moved_tuple_image=None,
            truncated=False,
        )

    solution_generators = {
        signed: action_permutation(solution, n, (signed,)) for signed in alphabet
    }
    detector_generators = {
        signed: action_permutation(detector, n, (signed,)) for signed in alphabet
    }

    start = (detector_identity, solution_identity, tuple())
    queue = deque((start,))
    seen = {(detector_identity, solution_identity)}
    solution_projection = {solution_identity}
    detector_projection = {detector_identity}
    kernel_solution = {solution_identity}
    first_witness_word = None
    first_witness_permutation = None

    while queue:
        detector_state, solution_state, word = queue.popleft()
        for signed in alphabet:
            next_word = word + (signed,)
            next_detector = _compose_permutations(
                detector_generators[signed], detector_state
            )
            next_solution = _compose_permutations(
                solution_generators[signed], solution_state
            )
            key = (next_detector, next_solution)
            if key in seen:
                continue
            seen.add(key)
            solution_projection.add(next_solution)
            detector_projection.add(next_detector)
            if next_detector == detector_identity:
                kernel_solution.add(next_solution)
                if (
                    next_solution != solution_identity
                    and first_witness_word is None
                ):
                    first_witness_word = next_word
                    first_witness_permutation = next_solution
            if len(seen) > state_limit:
                moved, moved_image = (
                    (None, None)
                    if first_witness_permutation is None
                    else _first_moved_tuple(solution, n, first_witness_permutation)
                )
                return RackResidualObstructionAudit(
                    n=n,
                    joint_image_size=None,
                    solution_image_size=None,
                    detector_image_size=None,
                    kernel_size=None,
                    kernel_contains_nonidentity=None,
                    first_witness_word=first_witness_word,
                    first_moved_tuple=moved,
                    first_moved_tuple_image=moved_image,
                    truncated=True,
                )
            queue.append((next_detector, next_solution, next_word))

    moved, moved_image = (
        (None, None)
        if first_witness_permutation is None
        else _first_moved_tuple(solution, n, first_witness_permutation)
    )
    return RackResidualObstructionAudit(
        n=n,
        joint_image_size=len(seen),
        solution_image_size=len(solution_projection),
        detector_image_size=len(detector_projection),
        kernel_size=len(kernel_solution),
        kernel_contains_nonidentity=any(
            item != solution_identity for item in kernel_solution
        ),
        first_witness_word=first_witness_word,
        first_moved_tuple=moved,
        first_moved_tuple_image=moved_image,
        truncated=False,
    )
