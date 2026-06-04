from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Hashable, Mapping, Optional, Tuple

from .finite_braided_set import Element, FiniteBraidedSet

State = Hashable


@dataclass(frozen=True)
class MealyTransducer:
    """Finite left-to-right transducer with output in a rack alphabet."""

    states: Tuple[State, ...]
    initial: State
    delta: Mapping[Tuple[State, Element], State]
    omega: Mapping[Tuple[State, Element], Element]

    def next_state(self, state: State, letter: Element) -> State:
        return self.delta[(state, letter)]

    def output(self, state: State, letter: Element) -> Element:
        return self.omega[(state, letter)]

    def outputs(self, word: Tuple[Element, ...]) -> Tuple[Element, ...]:
        state = self.initial
        out = []
        for letter in word:
            out.append(self.output(state, letter))
            state = self.next_state(state, letter)
        return tuple(out)


@dataclass(frozen=True)
class InvariantTransducer:
    """Finite left-to-right transducer whose output should be braid-invariant."""

    states: Tuple[State, ...]
    initial: State
    delta: Mapping[Tuple[State, Element], State]
    nu: Mapping[Tuple[State, Element], Element]

    def next_state(self, state: State, letter: Element) -> State:
        return self.delta[(state, letter)]

    def output(self, state: State, letter: Element) -> Element:
        return self.nu[(state, letter)]

    def outputs(self, word: Tuple[Element, ...]) -> Tuple[Element, ...]:
        state = self.initial
        out = []
        for letter in word:
            out.append(self.output(state, letter))
            state = self.next_state(state, letter)
        return tuple(out)


@dataclass(frozen=True)
class QuotientEquivarianceFailure:
    left: Element
    right: Element
    expected: Tuple[Element, Element]
    actual: Tuple[Element, Element]


@dataclass(frozen=True)
class RackTransducerFailure:
    state: State
    left: Element
    right: Element
    reason: str
    expected: Tuple[Element, ...]
    actual: Tuple[Element, ...]


@dataclass(frozen=True)
class InvariantTransducerFailure:
    state: State
    left: Element
    right: Element
    reason: str
    expected: Tuple[Element, ...]
    actual: Tuple[Element, ...]


@dataclass(frozen=True)
class InjectivityWitness:
    left_word: Tuple[Element, ...]
    right_word: Tuple[Element, ...]

    @property
    def length(self) -> int:
        return len(self.left_word)


@dataclass(frozen=True)
class TransducerRackificationAudit:
    quotient_failures: Tuple[QuotientEquivarianceFailure, ...]
    rack_failures: Tuple[RackTransducerFailure, ...]
    invariant_failures: Tuple[InvariantTransducerFailure, ...]
    injectivity_witness: Optional[InjectivityWitness]

    @property
    def finite_conditions_hold(self) -> bool:
        return (
            not self.quotient_failures
            and not self.rack_failures
            and not self.invariant_failures
            and self.injectivity_witness is None
        )


def quotient_equivariance_failures(
    solution: FiniteBraidedSet,
    quotient: FiniteBraidedSet,
    quotient_map: Mapping[Element, Element],
) -> Tuple[QuotientEquivarianceFailure, ...]:
    """Return failures of `quotient_map` to be a YBE quotient map."""

    failures = []
    for left in solution.elements:
        for right in solution.elements:
            out_left, out_right = solution.R[(left, right)]
            expected = quotient.R[(quotient_map[left], quotient_map[right])]
            actual = (quotient_map[out_left], quotient_map[out_right])
            if expected != actual:
                failures.append(
                    QuotientEquivarianceFailure(left, right, expected, actual)
                )
    return tuple(failures)


def rack_transducer_equivariance_failures(
    solution: FiniteBraidedSet,
    rack: FiniteBraidedSet,
    transducer: MealyTransducer,
) -> Tuple[RackTransducerFailure, ...]:
    """Check the two-letter equations making `M:X^* -> S^*` braid-equivariant."""

    failures = []
    for state in transducer.states:
        for left in solution.elements:
            for right in solution.elements:
                out_left, out_right = solution.R[(left, right)]
                original_next = transducer.next_state(
                    transducer.next_state(state, left), right
                )
                crossed_next = transducer.next_state(
                    transducer.next_state(state, out_left), out_right
                )
                if original_next != crossed_next:
                    failures.append(
                        RackTransducerFailure(
                            state,
                            left,
                            right,
                            "state",
                            (original_next,),
                            (crossed_next,),
                        )
                    )
                original_outputs = (
                    transducer.output(state, left),
                    transducer.output(transducer.next_state(state, left), right),
                )
                crossed_outputs = (
                    transducer.output(state, out_left),
                    transducer.output(transducer.next_state(state, out_left), out_right),
                )
                actual = rack.R[original_outputs]
                if actual != crossed_outputs:
                    failures.append(
                        RackTransducerFailure(
                            state,
                            left,
                            right,
                            "output",
                            crossed_outputs,
                            actual,
                        )
                    )
    return tuple(failures)


def invariant_transducer_failures(
    solution: FiniteBraidedSet,
    transducer: InvariantTransducer,
) -> Tuple[InvariantTransducerFailure, ...]:
    """Check the two-letter equations making `N:X^* -> I^*` braid-invariant."""

    failures = []
    for state in transducer.states:
        for left in solution.elements:
            for right in solution.elements:
                out_left, out_right = solution.R[(left, right)]
                original_next = transducer.next_state(
                    transducer.next_state(state, left), right
                )
                crossed_next = transducer.next_state(
                    transducer.next_state(state, out_left), out_right
                )
                if original_next != crossed_next:
                    failures.append(
                        InvariantTransducerFailure(
                            state,
                            left,
                            right,
                            "state",
                            (original_next,),
                            (crossed_next,),
                        )
                    )
                original_outputs = (
                    transducer.output(state, left),
                    transducer.output(transducer.next_state(state, left), right),
                )
                crossed_outputs = (
                    transducer.output(state, out_left),
                    transducer.output(transducer.next_state(state, out_left), out_right),
                )
                if original_outputs != crossed_outputs:
                    failures.append(
                        InvariantTransducerFailure(
                            state,
                            left,
                            right,
                            "output",
                            crossed_outputs,
                            original_outputs,
                        )
                    )
    return tuple(failures)


def combined_transducer_output(
    word: Tuple[Element, ...],
    quotient_map: Mapping[Element, Element],
    rack_transducer: MealyTransducer,
    invariant_transducer: Optional[InvariantTransducer] = None,
) -> Tuple[Tuple[Element, ...], Optional[Tuple[Element, ...]], Tuple[Element, ...]]:
    """Return `(pi^n, N_n, F_n)` for one input word."""

    quotient_word = tuple(quotient_map[letter] for letter in word)
    invariant_word = (
        None
        if invariant_transducer is None
        else invariant_transducer.outputs(word)
    )
    return (quotient_word, invariant_word, rack_transducer.outputs(word))


def all_length_injectivity_witness(
    solution: FiniteBraidedSet,
    quotient_map: Mapping[Element, Element],
    rack_transducer: MealyTransducer,
    invariant_transducer: Optional[InvariantTransducer] = None,
) -> Optional[InjectivityWitness]:
    """Find two different words with identical combined outputs, if any.

    This is the finite pair-automaton test from the certificate theorem.
    """

    if invariant_transducer is None:
        invariant_initial = None
    else:
        invariant_initial = invariant_transducer.initial

    start = (
        rack_transducer.initial,
        invariant_initial,
        rack_transducer.initial,
        invariant_initial,
        False,
    )
    queue = deque([(start, tuple(), tuple())])
    seen = {start}

    while queue:
        state, left_word, right_word = queue.popleft()
        q_left, p_left, q_right, p_right, already_differs = state
        for left in solution.elements:
            left_output = (
                quotient_map[left],
                None
                if invariant_transducer is None
                else invariant_transducer.output(p_left, left),
                rack_transducer.output(q_left, left),
            )
            for right in solution.elements:
                right_output = (
                    quotient_map[right],
                    None
                    if invariant_transducer is None
                    else invariant_transducer.output(p_right, right),
                    rack_transducer.output(q_right, right),
                )
                if left_output != right_output:
                    continue
                next_left_state = rack_transducer.next_state(q_left, left)
                next_right_state = rack_transducer.next_state(q_right, right)
                if invariant_transducer is None:
                    next_left_inv = None
                    next_right_inv = None
                else:
                    next_left_inv = invariant_transducer.next_state(p_left, left)
                    next_right_inv = invariant_transducer.next_state(p_right, right)
                differs = already_differs or left != right
                next_state = (
                    next_left_state,
                    next_left_inv,
                    next_right_state,
                    next_right_inv,
                    differs,
                )
                next_left_word = left_word + (left,)
                next_right_word = right_word + (right,)
                if differs:
                    return InjectivityWitness(next_left_word, next_right_word)
                if next_state not in seen:
                    seen.add(next_state)
                    queue.append((next_state, next_left_word, next_right_word))
    return None


def transducer_rackification_audit(
    solution: FiniteBraidedSet,
    quotient: FiniteBraidedSet,
    quotient_map: Mapping[Element, Element],
    rack: FiniteBraidedSet,
    rack_transducer: MealyTransducer,
    invariant_transducer: Optional[InvariantTransducer] = None,
) -> TransducerRackificationAudit:
    """Audit the finite conditions of a transducer rackification certificate."""

    return TransducerRackificationAudit(
        quotient_failures=quotient_equivariance_failures(
            solution, quotient, quotient_map
        ),
        rack_failures=rack_transducer_equivariance_failures(
            solution, rack, rack_transducer
        ),
        invariant_failures=()
        if invariant_transducer is None
        else invariant_transducer_failures(solution, invariant_transducer),
        injectivity_witness=all_length_injectivity_witness(
            solution, quotient_map, rack_transducer, invariant_transducer
        ),
    )
