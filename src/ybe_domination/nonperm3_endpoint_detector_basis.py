"""Reconstruct non-permutation size-three endpoint detector inputs.

The functions in this module reconstruct the finite endpoint candidates and
monoid quotients used by the non-permutation ``|X|=3`` endpoint-gate
experiments.  They deliberately separate the proved finite data being
reconstructed from the later detector search and all-arity interpretation.
"""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from dataclasses import dataclass
from itertools import product
from typing import Any, Iterable, Sequence

from .finite_braided_set import FiniteBraidedSet
from .finite_rack_sat import (
    ContextPresentation,
    Endpoint,
    MonoidQuotient,
    RackDetector,
    _assignment_for_fixed_rack,
    build_context_presentation,
    enumerate_rack_tables,
    q2_fast_detector,
    verify_detector,
)
from .small_search import all_bijection_solutions, is_permutation_solution_form

FlatYbeTable = tuple[int, ...]
RackTable = tuple[tuple[int, ...], ...]
ENDPOINT_BASIS_KIND = "nonperm3_endpoint_detector_basis_reconstruction_v1"
ENDPOINT_BASIS_BRANCH = "nonpermutation_size3"
REPORTED_Q5_SHA256 = "376e901839c978530ecd32893da56de5ff69b26dd3c407d1cb3eda365c63fc75"


class _DSU:
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, item: int) -> int:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def union(self, left: int, right: int) -> bool:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        if self.rank[left_root] < self.rank[right_root]:
            left_root, right_root = right_root, left_root
        self.parent[right_root] = left_root
        if self.rank[left_root] == self.rank[right_root]:
            self.rank[left_root] += 1
        return True


@dataclass(frozen=True)
class EndpointCandidate:
    """A principal endpoint pair made equal by a rack-admissible quotient."""

    candidate_id: str
    ybe_table: FlatYbeTable
    solution_index: int
    partition: tuple[int, ...]
    partition_index: int
    arity: int
    e_word: tuple[int, ...]
    e_position: int
    eprime_word: tuple[int, ...]
    eprime_position: int

    @property
    def endpoint(self) -> Endpoint:
        return Endpoint(
            prefix=self.e_word[: self.e_position],
            letter=self.e_word[self.e_position],
            suffix=self.e_word[self.e_position + 1 :],
        )

    @property
    def endpoint_prime(self) -> Endpoint:
        return Endpoint(
            prefix=self.eprime_word[: self.eprime_position],
            letter=self.eprime_word[self.eprime_position],
            suffix=self.eprime_word[self.eprime_position + 1 :],
        )


@dataclass(frozen=True)
class DetectorSchema:
    """One contextual finite-rack detector schema covering one or more candidates."""

    schema_id: str
    source_batch: str
    ybe_table: FlatYbeTable
    solution_index: int
    partition: tuple[int, ...]
    partition_index: int
    arity: int
    monoid_family: str
    monoid: MonoidQuotient
    rack_table: RackTable
    assignment_by_class: tuple[int, ...]
    endpoint_class: int
    endpoint_prime_class: int
    endpoint_values: tuple[int, int]
    covered_candidate_ids: tuple[str, ...]
    example_candidate: EndpointCandidate


def flat_table_from_solution(solution: FiniteBraidedSet) -> FlatYbeTable:
    """Return the flat ``d*x+y`` table convention used by certificates."""

    size = len(solution.elements)
    return tuple(
        size * solution.R[(x, y)][0] + solution.R[(x, y)][1]
        for x in solution.elements
        for y in solution.elements
    )


def solution_from_flat_table(table: Iterable[int]) -> FiniteBraidedSet:
    """Build a zero-based finite braided set from a flat pair table."""

    flat = tuple(int(entry) for entry in table)
    size_squared = len(flat)
    size = int(size_squared**0.5)
    if size * size != size_squared:
        raise ValueError("flat YBE table length must be a square")
    elements = tuple(range(size))
    pairs = tuple(product(elements, repeat=2))
    values = tuple(divmod(value, size) for value in flat)
    return FiniteBraidedSet(elements, dict(zip(pairs, values)))


def nonpermutation_size3_solutions() -> tuple[tuple[int, FiniteBraidedSet], ...]:
    """Return ``(global_solution_index, solution)`` for the 55 target tables."""

    return tuple(
        (index, solution)
        for index, solution in enumerate(all_bijection_solutions(3))
        if not is_permutation_solution_form(solution)
    )


def truncated_structure_monoid_length_1() -> MonoidQuotient:
    """Universal truncation retaining the empty word and length-one words."""

    return MonoidQuotient(
        size=5,
        identity=0,
        mul=(
            (0, 1, 2, 3, 4),
            (1, 4, 4, 4, 4),
            (2, 4, 4, 4, 4),
            (3, 4, 4, 4, 4),
            (4, 4, 4, 4, 4),
        ),
        gen=(1, 2, 3),
    )


def truncated_structure_monoid_length_2(
    solution: FiniteBraidedSet,
) -> MonoidQuotient:
    """Solution-dependent truncation retaining structure-monoid words of length 2."""

    if tuple(solution.elements) != (0, 1, 2):
        raise ValueError("length-two truncation is implemented for size-three tables")
    pair_index = {(x, y): 3 * x + y for x in range(3) for y in range(3)}
    pair_dsu = _DSU(9)
    for x in range(3):
        for y in range(3):
            x_prime, y_prime = solution.R[(x, y)]
            pair_dsu.union(pair_index[(x, y)], pair_index[(x_prime, y_prime)])

    roots: dict[int, int] = {}
    for pair, index in pair_index.items():
        root = pair_dsu.find(index)
        if root not in roots:
            roots[root] = 4 + len(roots)
    absorbing = 4 + len(roots)
    size = absorbing + 1
    mul = [[absorbing for _ in range(size)] for _ in range(size)]
    for value in range(size):
        mul[0][value] = value
        mul[value][0] = value
    for x in range(3):
        for y in range(3):
            mul[1 + x][1 + y] = roots[pair_dsu.find(pair_index[(x, y)])]
    return MonoidQuotient(
        size=size,
        identity=0,
        mul=tuple(tuple(row) for row in mul),
        gen=(1, 2, 3),
    )


def canonical_partitions_3() -> tuple[tuple[int, int, int], ...]:
    """Return canonical set partitions of ``{0,1,2}`` in restricted-growth order."""

    return (
        (0, 0, 0),
        (0, 0, 1),
        (0, 1, 0),
        (0, 1, 1),
        (0, 1, 2),
    )


def quotient_solution_by_partition(
    solution: FiniteBraidedSet,
    partition: Sequence[int],
) -> FiniteBraidedSet | None:
    """Return the quotient braided set induced by ``partition``, if well-defined."""

    partition = tuple(int(value) for value in partition)
    if len(partition) != len(solution.elements):
        raise ValueError("partition length must match solution size")
    classes = tuple(sorted(set(partition)))
    table = {}
    for left_class in classes:
        for right_class in classes:
            values = set()
            for x in solution.elements:
                for y in solution.elements:
                    if partition[x] == left_class and partition[y] == right_class:
                        x_prime, y_prime = solution.R[(x, y)]
                        values.add((partition[x_prime], partition[y_prime]))
            if len(values) != 1:
                return None
            table[(left_class, right_class)] = values.pop()
    try:
        quotient = FiniteBraidedSet(classes, table)
    except ValueError:
        return None
    if not quotient.is_ybe():
        return None
    return quotient


def endpoint_t_classes(
    solution: FiniteBraidedSet,
    arity: int,
) -> tuple[_DSU, object, tuple[tuple[int, ...], ...]]:
    """Return endpoint T-classes for all positions in all ``X^arity`` tuples."""

    elements = tuple(solution.elements)
    words = tuple(tuple(word) for word in product(elements, repeat=arity))
    index = {word: position for position, word in enumerate(words)}
    dsu = _DSU(len(words) * arity)

    def node(word: Sequence[int], position: int) -> int:
        return index[tuple(word)] * arity + position

    for word in words:
        for crossing in range(arity - 1):
            left, right = solution.R[(word[crossing], word[crossing + 1])]
            word2 = word[:crossing] + (left, right) + word[crossing + 2 :]
            for position in range(arity):
                if position < crossing or position > crossing + 1:
                    dsu.union(node(word, position), node(word2, position))
                elif position == crossing:
                    dsu.union(node(word, crossing), node(word2, crossing + 1))
    return dsu, node, words


def tuple_orbits(
    solution: FiniteBraidedSet,
    arity: int,
) -> tuple[_DSU, dict[tuple[int, ...], int], tuple[tuple[int, ...], ...]]:
    """Return tuple braid-orbit components using the forward generators."""

    words = tuple(
        tuple(word)
        for word in product(tuple(solution.elements), repeat=arity)
    )
    index = {word: position for position, word in enumerate(words)}
    dsu = _DSU(len(words))
    for word in words:
        for crossing in range(arity - 1):
            word2 = solution.apply_R_at(word, crossing)
            dsu.union(index[word], index[word2])
    return dsu, index, words


def principal_bad_endpoint_candidates(
    solution: FiniteBraidedSet,
    *,
    solution_index: int,
    arity: int,
) -> tuple[EndpointCandidate, ...]:
    """Enumerate compact principal bad endpoint pairs for one size-three table."""

    if tuple(solution.elements) != (0, 1, 2):
        raise ValueError("principal nonperm3 candidates require elements 0,1,2")
    if arity < 1:
        raise ValueError("arity must be positive")

    ybe_table = flat_table_from_solution(solution)
    x_t_dsu, x_t_node, words = endpoint_t_classes(solution, arity)
    orbit_dsu, orbit_index, _ = tuple_orbits(solution, arity)
    all_endpoints = tuple((word, position) for word in words for position in range(arity))
    out: list[EndpointCandidate] = []
    local_index = 0

    for partition_index, partition in enumerate(canonical_partitions_3()):
        quotient = quotient_solution_by_partition(solution, partition)
        if quotient is None:
            continue
        quotient_t_dsu, quotient_t_node, _ = endpoint_t_classes(quotient, arity)
        for left_index, (word, position) in enumerate(all_endpoints):
            for right_index, (word2, position2) in enumerate(all_endpoints):
                if right_index <= left_index:
                    continue
                if orbit_dsu.find(orbit_index[word]) != orbit_dsu.find(orbit_index[word2]):
                    continue
                quotient_word = tuple(partition[x] for x in word)
                quotient_word2 = tuple(partition[x] for x in word2)
                quotient_equal = (
                    quotient_t_dsu.find(quotient_t_node(quotient_word, position))
                    == quotient_t_dsu.find(quotient_t_node(quotient_word2, position2))
                )
                x_equal = (
                    x_t_dsu.find(x_t_node(word, position))
                    == x_t_dsu.find(x_t_node(word2, position2))
                )
                if quotient_equal and not x_equal:
                    out.append(
                        EndpointCandidate(
                            candidate_id=(
                                f"a{arity}:X{solution_index:03d}:"
                                f"P{partition_index}:E{local_index:06d}"
                            ),
                            ybe_table=ybe_table,
                            solution_index=solution_index,
                            partition=tuple(partition),
                            partition_index=partition_index,
                            arity=arity,
                            e_word=tuple(word),
                            e_position=position,
                            eprime_word=tuple(word2),
                            eprime_position=position2,
                        )
                    )
                    local_index += 1
    return tuple(out)


def principal_bad_endpoint_candidates_for_nonperm3(
    *,
    arity: int,
) -> tuple[EndpointCandidate, ...]:
    """Enumerate principal bad endpoint candidates over all 55 target tables."""

    out: list[EndpointCandidate] = []
    for solution_index, solution in nonpermutation_size3_solutions():
        out.extend(
            principal_bad_endpoint_candidates(
                solution,
                solution_index=solution_index,
                arity=arity,
            )
        )
    return tuple(out)


def is_associative_monoid(monoid: MonoidQuotient) -> bool:
    """Check monoid associativity and identity laws."""

    for value in range(monoid.size):
        if monoid.mul[monoid.identity][value] != value:
            return False
        if monoid.mul[value][monoid.identity] != value:
            return False
    for a in range(monoid.size):
        for b in range(monoid.size):
            for c in range(monoid.size):
                if monoid.mul[monoid.mul[a][b]][c] != monoid.mul[a][monoid.mul[b][c]]:
                    return False
    return True


def monoids_for_solution(
    solution: FiniteBraidedSet,
    requested: tuple[str, ...],
) -> tuple[tuple[str, MonoidQuotient], ...]:
    """Return requested monoid families in deterministic order."""

    out: list[tuple[str, MonoidQuotient]] = []
    for name in requested:
        if name == "truncated_structure_monoid_length_1":
            out.append((name, truncated_structure_monoid_length_1()))
        elif name == "truncated_structure_monoid_length_2":
            out.append((name, truncated_structure_monoid_length_2(solution)))
        else:
            raise ValueError(f"unknown monoid family: {name}")
    return tuple(out)


def _monoid_to_dict(monoid: MonoidQuotient, *, construction: str) -> dict[str, Any]:
    return {
        "construction": construction,
        "size": monoid.size,
        "identity": monoid.identity,
        "generator_images": list(monoid.gen),
        "mul": [list(row) for row in monoid.mul],
    }


def _monoid_from_dict(value: dict[str, Any]) -> MonoidQuotient:
    size = int(value["size"])
    identity = int(value.get("identity", 0))
    generator_images = tuple(int(entry) for entry in value["generator_images"])
    mul = tuple(tuple(int(entry) for entry in row) for row in value["mul"])
    if len(mul) != size or any(len(row) != size for row in mul):
        raise ValueError("monoid multiplication table shape does not match size")
    return MonoidQuotient(
        size=size,
        identity=identity,
        mul=mul,
        gen=generator_images,
    )


def _endpoint_dict(word: tuple[int, ...], position: int) -> dict[str, Any]:
    return {
        "word": list(word),
        "position": position,
        "prefix": list(word[:position]),
        "letter": word[position],
        "suffix": list(word[position + 1 :]),
    }


def _endpoint_pair_dict(candidate: EndpointCandidate) -> dict[str, Any]:
    return {
        "e": _endpoint_dict(candidate.e_word, candidate.e_position),
        "eprime": _endpoint_dict(
            candidate.eprime_word,
            candidate.eprime_position,
        ),
    }


def _raw_alpha_from_assignment_by_class(
    raw_to_class: tuple[int, ...],
    assignment_by_class: tuple[int, ...],
) -> tuple[int, ...]:
    return tuple(assignment_by_class[class_id] for class_id in raw_to_class)


def schema_from_detector(
    candidate: EndpointCandidate,
    *,
    source_batch: str,
    monoid_family: str,
    monoid: MonoidQuotient,
    presentation: ContextPresentation,
    detector: RackDetector,
) -> DetectorSchema:
    """Build a schema object from a verified detector for one candidate."""

    endpoint_values = (
        detector.assignment[presentation.endpoint_class],
        detector.assignment[presentation.endpoint_prime_class],
    )
    return DetectorSchema(
        schema_id="",
        source_batch=source_batch,
        ybe_table=candidate.ybe_table,
        solution_index=candidate.solution_index,
        partition=candidate.partition,
        partition_index=candidate.partition_index,
        arity=candidate.arity,
        monoid_family=monoid_family,
        monoid=monoid,
        rack_table=detector.table,
        assignment_by_class=detector.assignment,
        endpoint_class=presentation.endpoint_class,
        endpoint_prime_class=presentation.endpoint_prime_class,
        endpoint_values=endpoint_values,
        covered_candidate_ids=(candidate.candidate_id,),
        example_candidate=candidate,
    )


def _schema_with_id_and_covered_candidates(
    schema: DetectorSchema,
    *,
    schema_id: str,
    covered_candidate_ids: tuple[str, ...],
) -> DetectorSchema:
    return DetectorSchema(
        schema_id=schema_id,
        source_batch=schema.source_batch,
        ybe_table=schema.ybe_table,
        solution_index=schema.solution_index,
        partition=schema.partition,
        partition_index=schema.partition_index,
        arity=schema.arity,
        monoid_family=schema.monoid_family,
        monoid=schema.monoid,
        rack_table=schema.rack_table,
        assignment_by_class=schema.assignment_by_class,
        endpoint_class=schema.endpoint_class,
        endpoint_prime_class=schema.endpoint_prime_class,
        endpoint_values=schema.endpoint_values,
        covered_candidate_ids=covered_candidate_ids,
        example_candidate=schema.example_candidate,
    )


def schema_key(schema: DetectorSchema) -> tuple[Any, ...]:
    """Return the deduplication key for contextual detector schemas."""

    return (
        tuple(schema.ybe_table),
        schema.arity,
        tuple(schema.partition),
        schema.monoid_family,
        tuple(tuple(row) for row in schema.monoid.mul),
        tuple(tuple(row) for row in schema.rack_table),
        tuple(schema.assignment_by_class),
        schema.endpoint_class,
        schema.endpoint_prime_class,
    )


def detector_schema_to_record(schema: DetectorSchema) -> dict[str, Any]:
    """Return a JSON-friendly full detector schema record."""

    presentation = build_context_presentation(
        solution_from_flat_table(schema.ybe_table),
        schema.monoid,
        schema.example_candidate.endpoint,
        schema.example_candidate.endpoint_prime,
    )
    alpha = _raw_alpha_from_assignment_by_class(
        presentation.raw_to_class,
        schema.assignment_by_class,
    )
    endpoint_pair = _endpoint_pair_dict(schema.example_candidate)
    return {
        "schema_id": schema.schema_id,
        "id": schema.schema_id,
        "type": "finite_rack_detector_schema",
        "source_batch": schema.source_batch,
        "ybe_table": list(schema.ybe_table),
        "solution_index": schema.solution_index,
        "partition": list(schema.partition),
        "partition_index": schema.partition_index,
        "arity": schema.arity,
        "monoid_family": schema.monoid_family,
        "monoid_quotient": _monoid_to_dict(
            schema.monoid,
            construction=schema.monoid_family,
        ),
        "rack": {
            "size": len(schema.rack_table),
            "table": [list(row) for row in schema.rack_table],
        },
        "rack_table": [list(row) for row in schema.rack_table],
        "assignment_by_class": list(schema.assignment_by_class),
        "alpha": list(alpha),
        "endpoint_class": schema.endpoint_class,
        "endpoint_prime_class": schema.endpoint_prime_class,
        "endpoint_values": list(schema.endpoint_values),
        "covered_candidate_ids": list(schema.covered_candidate_ids),
        "endpoint_pair": endpoint_pair,
        "example_endpoint_pair": endpoint_pair,
    }


def _source_batch_name(
    *,
    arity: int,
    qmax: int,
    emit_new_q5_only: bool,
) -> str:
    if arity == 2:
        return "nonperm3_arity2_endpoint_gate_full_schema"
    if arity == 3 and emit_new_q5_only:
        return "nonperm3_arity3_q5_resolution"
    if arity == 3 and qmax <= 4:
        return "nonperm3_arity3_endpoint_gate_q4_full_schema"
    return f"nonperm3_arity{arity}_q{qmax}_endpoint_schema"


def _schema_id_prefix(
    *,
    arity: int,
    qmax: int,
    emit_new_q5_only: bool,
) -> str:
    if emit_new_q5_only:
        return f"a{arity}-q5"
    return f"a{arity}-q{qmax}"


def _presentation_cache_key(
    candidate: EndpointCandidate,
    monoid_family: str,
    monoid: MonoidQuotient,
) -> tuple[Any, ...]:
    return (
        candidate.ybe_table,
        monoid_family,
        monoid.mul,
        monoid.gen,
        candidate.e_word,
        candidate.e_position,
        candidate.eprime_word,
        candidate.eprime_position,
    )


def first_detector_for_candidate(
    solution: FiniteBraidedSet,
    candidate: EndpointCandidate,
    *,
    monoid_family_names: tuple[str, ...],
    qmax: int,
    source_batch: str = "nonperm3_endpoint_detector_basis_reconstruction",
    presentation_cache: dict[tuple[Any, ...], Any] | None = None,
    fixed_rack_failure_cache: set[tuple[Any, ...]] | None = None,
) -> DetectorSchema | None:
    """Return the first deterministic detector schema for ``candidate``."""

    if presentation_cache is None:
        presentation_cache = {}
    if fixed_rack_failure_cache is None:
        fixed_rack_failure_cache = set()

    monoids = monoids_for_solution(solution, monoid_family_names)
    for q in range(2, qmax + 1):
        for monoid_name, monoid in monoids:
            cache_key = _presentation_cache_key(candidate, monoid_name, monoid)
            presentation = presentation_cache.get(cache_key)
            if presentation is None:
                presentation = build_context_presentation(
                    solution,
                    monoid,
                    candidate.endpoint,
                    candidate.endpoint_prime,
                )
                presentation_cache[cache_key] = presentation
            if presentation.endpoint_class == presentation.endpoint_prime_class:
                continue
            if q == 2:
                detector = q2_fast_detector(presentation)
                if detector is None:
                    continue
                return schema_from_detector(
                    candidate,
                    source_batch=source_batch,
                    monoid_family=monoid_name,
                    monoid=monoid,
                    presentation=presentation,
                    detector=detector,
                )
            for rack_table in enumerate_rack_tables(q):
                failure_key = (
                    presentation.class_count,
                    presentation.equations,
                    presentation.endpoint_class,
                    presentation.endpoint_prime_class,
                    rack_table,
                )
                if failure_key in fixed_rack_failure_cache:
                    continue
                assignment = _assignment_for_fixed_rack(presentation, rack_table)
                if assignment is None:
                    fixed_rack_failure_cache.add(failure_key)
                    continue
                detector = RackDetector(q=q, table=rack_table, assignment=assignment)
                if verify_detector(presentation, detector):
                    return schema_from_detector(
                        candidate,
                        source_batch=source_batch,
                        monoid_family=monoid_name,
                        monoid=monoid,
                        presentation=presentation,
                        detector=detector,
                    )
                fixed_rack_failure_cache.add(failure_key)
    return None


def _covered_candidate_ids_from_payload(payload: Any) -> set[str]:
    covered: set[str] = set()

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            candidate_ids = value.get("covered_candidate_ids")
            if isinstance(candidate_ids, (list, tuple)):
                covered.update(str(item) for item in candidate_ids)
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    if payload is not None:
        visit(payload)
    return covered


def _deduplicate_schemas(
    schemas: Iterable[DetectorSchema],
    *,
    id_prefix: str,
) -> tuple[DetectorSchema, ...]:
    grouped: dict[tuple[Any, ...], tuple[DetectorSchema, list[str]]] = {}
    for schema in schemas:
        key = schema_key(schema)
        if key not in grouped:
            grouped[key] = (schema, [])
        covered = grouped[key][1]
        for candidate_id in schema.covered_candidate_ids:
            if candidate_id not in covered:
                covered.append(candidate_id)

    out = []
    for index, (_key, (schema, covered)) in enumerate(grouped.items(), start=1):
        out.append(
            _schema_with_id_and_covered_candidates(
                schema,
                schema_id=f"{id_prefix}-s{index:06d}",
                covered_candidate_ids=tuple(covered),
            )
        )
    return tuple(out)


def _expected_checkpoint_failures(payload: dict[str, Any]) -> tuple[str, ...]:
    if not payload.get("enforce_checkpoint_counts", False):
        return tuple()
    failures = []
    arity = payload.get("arity")
    qmax = payload.get("qmax")
    emit_new_q5_only = payload.get("emit_new_q5_only", False)
    expected: dict[str, Any] | None = None
    if arity == 2 and qmax == 3:
        expected = {
            "nonpermutation_ybe_tables": 55,
            "bad_endpoint_pairs": 2064,
            "positive_detector_coverages": 2064,
            "unresolved_obstruction_candidates": 0,
            "by_rack_size": {"q2": 1200, "q3": 864},
        }
    elif arity == 3 and qmax == 4 and not emit_new_q5_only:
        expected = {
            "nonpermutation_ybe_tables": 55,
            "bad_endpoint_pairs": 37692,
            "positive_detector_coverages": 37476,
            "positive_detector_schemas": 320,
            "unresolved_obstruction_candidates": 216,
            "by_rack_size": {"q2": 16416, "q3": 20736, "q4": 324},
            "by_monoid": {
                "truncated_structure_monoid_length_1": 15309,
                "truncated_structure_monoid_length_2": 22167,
            },
        }
    elif arity == 3 and qmax == 5 and emit_new_q5_only:
        expected = {
            "new_positive_detector_coverages": 216,
            "new_positive_detector_schemas": 22,
            "combined_positive_detector_coverages": 37692,
            "remaining_unresolved_candidates": 0,
        }
    if expected is None:
        return tuple()
    for key, expected_value in expected.items():
        if payload.get(key) != expected_value:
            failures.append(
                f"{key} expected {expected_value!r}, got {payload.get(key)!r}"
            )
    return tuple(failures)


def reconstruct_detector_basis_payload(
    *,
    arity: int,
    qmax: int,
    monoid_family_names: tuple[str, ...],
    baseline_payload: Any | None = None,
    emit_new_q5_only: bool = False,
    enforce_checkpoint_counts: bool = True,
) -> dict[str, Any]:
    """Reconstruct and export a full deterministic detector-basis payload."""

    source_batch = _source_batch_name(
        arity=arity,
        qmax=qmax,
        emit_new_q5_only=emit_new_q5_only,
    )
    id_prefix = _schema_id_prefix(
        arity=arity,
        qmax=qmax,
        emit_new_q5_only=emit_new_q5_only,
    )
    baseline_covered = _covered_candidate_ids_from_payload(baseline_payload)
    presentation_cache: dict[tuple[Any, ...], Any] = {}
    fixed_rack_failure_cache: set[tuple[Any, ...]] = set()
    found: list[DetectorSchema] = []
    unresolved: list[str] = []
    all_candidate_count = 0
    skipped_baseline_count = 0

    for solution_index, solution in nonpermutation_size3_solutions():
        candidates = principal_bad_endpoint_candidates(
            solution,
            solution_index=solution_index,
            arity=arity,
        )
        all_candidate_count += len(candidates)
        for candidate in candidates:
            if emit_new_q5_only and candidate.candidate_id in baseline_covered:
                skipped_baseline_count += 1
                continue
            schema = first_detector_for_candidate(
                solution,
                candidate,
                monoid_family_names=monoid_family_names,
                qmax=qmax,
                source_batch=source_batch,
                presentation_cache=presentation_cache,
                fixed_rack_failure_cache=fixed_rack_failure_cache,
            )
            if schema is None:
                unresolved.append(candidate.candidate_id)
            else:
                found.append(schema)

    deduped = _deduplicate_schemas(found, id_prefix=id_prefix)
    records = [detector_schema_to_record(schema) for schema in deduped]
    coverage_by_q: Counter[str] = Counter()
    coverage_by_monoid: Counter[str] = Counter()
    for schema in deduped:
        coverage = len(schema.covered_candidate_ids)
        coverage_by_q[f"q{len(schema.rack_table)}"] += coverage
        coverage_by_monoid[schema.monoid_family] += coverage

    searched_candidate_count = all_candidate_count - skipped_baseline_count
    positive_coverages = sum(len(schema.covered_candidate_ids) for schema in deduped)
    payload: dict[str, Any] = {
        "kind": ENDPOINT_BASIS_KIND,
        "branch": ENDPOINT_BASIS_BRANCH,
        "source_batch": source_batch,
        "arity": arity,
        "qmax": qmax,
        "monoid_families": list(monoid_family_names),
        "emit_new_q5_only": emit_new_q5_only,
        "enforce_checkpoint_counts": enforce_checkpoint_counts,
        "nonpermutation_ybe_tables": 55,
        "bad_endpoint_pairs": all_candidate_count,
        "baseline_covered_candidate_count": skipped_baseline_count,
        "searched_candidate_count": searched_candidate_count,
        "positive_detector_coverages": positive_coverages,
        "positive_detector_schemas": len(deduped),
        "unresolved_obstruction_candidates": len(unresolved),
        "unresolved_candidate_ids": unresolved,
        "by_rack_size": dict(sorted(coverage_by_q.items())),
        "by_monoid": dict(sorted(coverage_by_monoid.items())),
        "positive_detector_schemas_records": records,
    }
    if emit_new_q5_only:
        payload["reported_sha256"] = REPORTED_Q5_SHA256
        payload["new_positive_detector_coverages"] = positive_coverages
        payload["new_positive_detector_schemas"] = len(deduped)
        payload["combined_positive_detector_coverages"] = (
            skipped_baseline_count + positive_coverages
        )
        payload["remaining_unresolved_candidates"] = len(unresolved)
    return payload


def _payload_without_reconstructed_sha(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            key: _payload_without_reconstructed_sha(child)
            for key, child in value.items()
            if key not in {"reconstructed_sha256", "sha256_matches_reported"}
        }
    if isinstance(value, list):
        return [_payload_without_reconstructed_sha(child) for child in value]
    return value


def canonical_payload_sha256(payload: dict[str, Any]) -> str:
    """Return a deterministic SHA256 over the JSON payload minus computed SHA fields."""

    canonical = json.dumps(
        _payload_without_reconstructed_sha(payload),
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()


def _int_tuple(value: Any) -> tuple[int, ...]:
    if isinstance(value, str):
        return tuple(int(part) for part in value.replace(",", " ").split())
    if isinstance(value, (list, tuple)):
        return tuple(int(part) for part in value)
    raise TypeError(f"expected integer sequence, got {value!r}")


def _rack_table_from_record(record: dict[str, Any]) -> RackTable:
    value = record.get("rack_table")
    if value is None:
        rack = record.get("rack")
        if isinstance(rack, dict):
            value = rack.get("table")
        else:
            value = rack
    if not isinstance(value, (list, tuple)):
        raise ValueError("record has no rack table")
    return tuple(tuple(int(entry) for entry in row) for row in value)


def _endpoint_from_endpoint_record(value: dict[str, Any]) -> Endpoint:
    return Endpoint(
        prefix=_int_tuple(value.get("prefix", tuple())),
        letter=int(value["letter"]),
        suffix=_int_tuple(value.get("suffix", tuple())),
    )


def verify_detector_schema_record(record: dict[str, Any]) -> tuple[str, ...]:
    """Verify one exported detector schema without trusting stored classes."""

    failures = []
    try:
        solution = solution_from_flat_table(record["ybe_table"])
        monoid = _monoid_from_dict(record["monoid_quotient"])
        rack_table = _rack_table_from_record(record)
        endpoint_pair = record.get("endpoint_pair", record.get("example_endpoint_pair"))
        if not isinstance(endpoint_pair, dict):
            raise ValueError("missing endpoint_pair")
        endpoint = _endpoint_from_endpoint_record(endpoint_pair["e"])
        endpoint_prime = _endpoint_from_endpoint_record(endpoint_pair["eprime"])
        assignment_by_class = _int_tuple(record["assignment_by_class"])
        presentation = build_context_presentation(
            solution,
            monoid,
            endpoint,
            endpoint_prime,
        )
        detector = RackDetector(
            q=len(rack_table),
            table=rack_table,
            assignment=assignment_by_class,
        )
        if not verify_detector(presentation, detector):
            failures.append("assignment_by_class is not a valid detector")
        if record.get("endpoint_class") != presentation.endpoint_class:
            failures.append("endpoint_class does not match recomputed presentation")
        if record.get("endpoint_prime_class") != presentation.endpoint_prime_class:
            failures.append(
                "endpoint_prime_class does not match recomputed presentation"
            )
        endpoint_values = (
            detector.assignment[presentation.endpoint_class],
            detector.assignment[presentation.endpoint_prime_class],
        )
        if tuple(record.get("endpoint_values", ())) != endpoint_values:
            failures.append("endpoint_values do not match recomputed assignment")
        alpha = _int_tuple(record.get("alpha", tuple()))
        expected_alpha = _raw_alpha_from_assignment_by_class(
            presentation.raw_to_class,
            assignment_by_class,
        )
        if alpha != expected_alpha:
            failures.append("alpha does not match assignment_by_class on raw classes")
    except (KeyError, TypeError, ValueError, IndexError) as exc:
        failures.append(f"invalid detector schema record: {exc}")
    return tuple(failures)


def _schema_records_from_payload(payload: Any) -> tuple[dict[str, Any], ...]:
    records: list[dict[str, Any]] = []

    def visit(value: Any) -> None:
        if isinstance(value, dict):
            if (
                value.get("type") == "finite_rack_detector_schema"
                and "assignment_by_class" in value
            ):
                records.append(value)
            for child in value.values():
                visit(child)
        elif isinstance(value, list):
            for child in value:
                visit(child)

    visit(payload)
    return tuple(records)


def verify_detector_basis_payload(payload: dict[str, Any]) -> tuple[str, ...]:
    """Verify exported detector schemas and checkpoint counts."""

    failures: list[str] = []
    if not isinstance(payload, dict):
        return ("payload must be a JSON object",)
    if payload.get("kind") != ENDPOINT_BASIS_KIND:
        failures.append(f"kind must be {ENDPOINT_BASIS_KIND!r}")
    if payload.get("branch") != ENDPOINT_BASIS_BRANCH:
        failures.append(f"branch must be {ENDPOINT_BASIS_BRANCH!r}")
    records = _schema_records_from_payload(payload)
    if payload.get("positive_detector_schemas") != len(records):
        failures.append("positive_detector_schemas does not match record count")
    covered: list[str] = []
    for index, record in enumerate(records):
        for failure in verify_detector_schema_record(record):
            schema_id = record.get("schema_id", f"schema[{index}]")
            failures.append(f"{schema_id}: {failure}")
        candidate_ids = record.get("covered_candidate_ids", [])
        if not isinstance(candidate_ids, list):
            failures.append(f"schema[{index}]: covered_candidate_ids must be a list")
        else:
            covered.extend(str(item) for item in candidate_ids)
    if payload.get("positive_detector_coverages") != len(covered):
        failures.append("positive_detector_coverages does not match covered IDs")
    if len(covered) != len(set(covered)):
        failures.append("covered_candidate_ids contain duplicates")
    failures.extend(_expected_checkpoint_failures(payload))
    return tuple(failures)
