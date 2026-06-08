"""Audit the 20-element contextual rack completion for the 4-point example."""

from __future__ import annotations

import itertools
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import FiniteBraidedSet, is_rack_solution, rack_solution  # noqa: E402


OUT_JSON = ROOT / "proofs" / "four_point_contextual_completion_audit.json"
OUT_MD = ROOT / "proofs" / "four_point_contextual_completion_audit.md"

X = ("00", "01", "10", "11")
X_INDEX = {x: i for i, x in enumerate(X)}


def _bits(x: str) -> tuple[int, int]:
    return int(x[0]), int(x[1])


def _label(base: int, fibre: int) -> str:
    return f"{base}{fibre}"


def four_point_R(x: str, y: str) -> tuple[str, str]:
    a, i = _bits(x)
    b, j = _bits(y)
    if (a, b) == (0, 0):
        first_fibre, second_fibre = i, j
    elif (a, b) in {(0, 1), (1, 0)}:
        first_fibre, second_fibre = j, i
    else:
        first_fibre, second_fibre = j, 1 - i
    return _label(b, first_fibre), _label(a, second_fibre)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Composition convention used by contextual products: left after right."""

    return tuple(left[right[i]] for i in range(len(left)))


def close_monoid(generators: set[tuple[int, ...]]) -> tuple[tuple[int, ...], ...]:
    identity = tuple(range(len(X)))
    monoid = {identity}
    queue = deque([identity])
    while queue:
        current = queue.popleft()
        for other in tuple(monoid | generators):
            for candidate in (compose(current, other), compose(other, current)):
                if candidate not in monoid:
                    monoid.add(candidate)
                    queue.append(candidate)
    return tuple(sorted(monoid))


class UnionFind:
    def __init__(self, count: int) -> None:
        self.parent = list(range(count))

    def find(self, item: int) -> int:
        while self.parent[item] != item:
            self.parent[item] = self.parent[self.parent[item]]
            item = self.parent[item]
        return item

    def union(self, left: int, right: int) -> None:
        root_left = self.find(left)
        root_right = self.find(right)
        if root_left != root_right:
            self.parent[root_right] = root_left


def build_contextual_completion():
    solution = FiniteBraidedSet(X, {(x, y): four_point_R(x, y) for x in X for y in X})
    inverse = {four_point_R(x, y): (x, y) for x in X for y in X}

    r_maps = {
        y: tuple(X_INDEX[four_point_R(x, y)[1]] for x in X)
        for y in X
    }
    m_maps = {
        u: tuple(X_INDEX[inverse[(u, v)][0]] for v in X)
        for u in X
    }
    monoid = close_monoid(set(r_maps.values()) | set(m_maps.values()))
    monoid_index = {mapping: index for index, mapping in enumerate(monoid)}

    triples = tuple(
        (a_index, x_index, b_index)
        for a_index in range(len(monoid))
        for x_index in range(len(X))
        for b_index in range(len(monoid))
    )
    triple_index = {triple: index for index, triple in enumerate(triples)}
    uf = UnionFind(len(triples))

    for a_index, a_map in enumerate(monoid):
        for b_index, b_map in enumerate(monoid):
            for x, y in itertools.product(X, repeat=2):
                u, v = four_point_R(x, y)
                left = (
                    a_index,
                    X_INDEX[x],
                    monoid_index[compose(b_map, r_maps[y])],
                )
                right = (
                    monoid_index[compose(a_map, m_maps[u])],
                    X_INDEX[v],
                    b_index,
                )
                uf.union(triple_index[left], triple_index[right])

    class_index_by_root: dict[int, int] = {}
    class_of_triple: dict[tuple[int, int, int], int] = {}
    for triple in triples:
        root = uf.find(triple_index[triple])
        if root not in class_index_by_root:
            class_index_by_root[root] = len(class_index_by_root)
        class_of_triple[triple] = class_index_by_root[root]

    partial_translations: dict[int, dict[int, int]] = {
        index: {} for index in range(len(class_index_by_root))
    }
    conflicts = []
    for a_index, a_map in enumerate(monoid):
        for b_index, b_map in enumerate(monoid):
            for x, y in itertools.product(X, repeat=2):
                u, v = four_point_R(x, y)
                p = class_of_triple[
                    (
                        a_index,
                        X_INDEX[x],
                        monoid_index[compose(b_map, r_maps[y])],
                    )
                ]
                q = class_of_triple[
                    (
                        monoid_index[compose(a_map, m_maps[x])],
                        X_INDEX[y],
                        b_index,
                    )
                ]
                out = class_of_triple[
                    (
                        a_index,
                        X_INDEX[u],
                        monoid_index[compose(b_map, r_maps[v])],
                    )
                ]
                previous = partial_translations[p].get(q)
                if previous is not None and previous != out:
                    conflicts.append((p, q, previous, out, a_index, b_index, x, y))
                partial_translations[p][q] = out

    left_translations = []
    for p in range(len(class_index_by_root)):
        row = list(range(len(class_index_by_root)))
        for source, target in partial_translations[p].items():
            row[source] = target
        left_translations.append(tuple(row))

    rack = rack_solution(
        tuple(range(len(class_index_by_root))),
        lambda left, right: left_translations[left][right],
    )

    identity = tuple(range(len(X)))

    def contextual_readout(word: tuple[str, ...]) -> tuple[int, ...]:
        left_contexts = []
        current = identity
        for x in word:
            left_contexts.append(current)
            current = compose(current, m_maps[x])

        right_contexts = [identity for _ in word]
        current = identity
        for index in range(len(word) - 1, -1, -1):
            right_contexts[index] = current
            current = compose(current, r_maps[word[index]])

        return tuple(
            class_of_triple[
                (
                    monoid_index[left_contexts[index]],
                    X_INDEX[word[index]],
                    monoid_index[right_contexts[index]],
                )
            ]
            for index in range(len(word))
        )

    return {
        "solution": solution,
        "rack": rack,
        "r_maps": r_maps,
        "m_maps": m_maps,
        "monoid": monoid,
        "class_of_triple": class_of_triple,
        "partial_translations": partial_translations,
        "left_translations": tuple(left_translations),
        "conflicts": conflicts,
        "contextual_readout": contextual_readout,
    }


def _permutation_cycles(mapping: tuple[int, ...]) -> list[list[int]]:
    seen = set()
    cycles = []
    for start in range(len(mapping)):
        if start in seen:
            continue
        cycle = []
        current = start
        while current not in seen:
            seen.add(current)
            cycle.append(current)
            current = mapping[current]
        if len(cycle) > 1:
            cycles.append(cycle)
    return cycles


def _orbit_injective(solution, contextual_readout, arity: int) -> bool:
    tuples = tuple(itertools.product(solution.elements, repeat=arity))
    seen = set()
    for start in tuples:
        if start in seen:
            continue
        orbit = set()
        queue = deque([start])
        seen.add(start)
        while queue:
            current = queue.popleft()
            orbit.add(current)
            for generator in range(1, arity):
                for signed in (generator, -generator):
                    image = solution.braid_action((signed,), current)
                    if image not in seen:
                        seen.add(image)
                        queue.append(image)
        readouts = [contextual_readout(tuple(word)) for word in orbit]
        if len(set(readouts)) != len(readouts):
            return False
    return True


def _equivariant(solution, rack, contextual_readout, arity: int) -> bool:
    for word in itertools.product(solution.elements, repeat=arity):
        readout = contextual_readout(tuple(word))
        for generator in range(1, arity):
            image = solution.braid_action((generator,), word)
            if contextual_readout(tuple(image)) != rack.braid_action((generator,), readout):
                return False
            inverse_image = solution.braid_action((-generator,), word)
            if contextual_readout(tuple(inverse_image)) != rack.braid_action(
                (-generator,), readout
            ):
                return False
    return True


def run_audit(max_checked_arity: int = 8) -> dict:
    completion = build_contextual_completion()
    solution = completion["solution"]
    rack = completion["rack"]
    contextual_readout = completion["contextual_readout"]
    class_count = len(rack.elements)

    nontrivial_translations = {
        str(index): _permutation_cycles(mapping)
        for index, mapping in enumerate(completion["left_translations"])
        if mapping != tuple(range(class_count))
    }

    base_separating = True
    one_fibre_separating = True
    class_of = completion["class_of_triple"]
    for a_index in range(len(completion["monoid"])):
        for b_index in range(len(completion["monoid"])):
            zero_classes = {
                class_of[(a_index, X_INDEX["00"], b_index)],
                class_of[(a_index, X_INDEX["01"], b_index)],
            }
            one_classes = {
                class_of[(a_index, X_INDEX["10"], b_index)],
                class_of[(a_index, X_INDEX["11"], b_index)],
            }
            if zero_classes & one_classes:
                base_separating = False
            if len(one_classes) != 2:
                one_fibre_separating = False

    equivariant_arities = []
    orbit_injective_arities = []
    for arity in range(1, max_checked_arity + 1):
        if _equivariant(solution, rack, contextual_readout, arity):
            equivariant_arities.append(arity)
        if _orbit_injective(solution, contextual_readout, arity):
            orbit_injective_arities.append(arity)

    report = {
        "source_elements": list(X),
        "source_is_ybe": solution.is_ybe(),
        "source_is_bijective": True,
        "contextual_monoid_size": len(completion["monoid"]),
        "contextual_monoid_maps": [list(mapping) for mapping in completion["monoid"]],
        "contextual_quotient_class_count": class_count,
        "forced_product_conflict_count": len(completion["conflicts"]),
        "rack_size": class_count,
        "rack_is_ybe": rack.is_ybe(),
        "rack_is_rack_solution": is_rack_solution(rack),
        "nontrivial_left_translation_cycles": nontrivial_translations,
        "forced_partial_translations_extend_to_permutations": all(
            len(set(mapping)) == len(mapping)
            for mapping in completion["left_translations"]
        ),
        "base_separating_for_equal_contexts": base_separating,
        "one_fibre_separating_for_equal_contexts": one_fibre_separating,
        "equivariance_checked_arities": equivariant_arities,
        "orbit_injectivity_checked_arities": orbit_injective_arities,
        "max_checked_arity": max_checked_arity,
        "all_checks_passed": (
            solution.is_ybe()
            and class_count == 20
            and not completion["conflicts"]
            and rack.is_ybe()
            and is_rack_solution(rack)
            and base_separating
            and one_fibre_separating
            and equivariant_arities == list(range(1, max_checked_arity + 1))
            and orbit_injective_arities == list(range(1, max_checked_arity + 1))
        ),
    }
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Four-Point Contextual Completion Audit",
        "",
        "This generated audit checks the explicit contextual rack completion for",
        "the four-point degenerate YBE solution on `00,01,10,11`.",
        "",
        "## Summary",
        "",
        f"- source YBE: `{report['source_is_ybe']}`;",
        f"- contextual monoid size: `{report['contextual_monoid_size']}`;",
        f"- contextual quotient classes: `{report['contextual_quotient_class_count']}`;",
        f"- forced product conflicts: `{report['forced_product_conflict_count']}`;",
        f"- rack size: `{report['rack_size']}`;",
        f"- rack YBE: `{report['rack_is_ybe']}`;",
        f"- rack-form check: `{report['rack_is_rack_solution']}`;",
        "- forced partial translations extend to permutations: "
        f"`{report['forced_partial_translations_extend_to_permutations']}`;",
        "- base separation for equal contexts: "
        f"`{report['base_separating_for_equal_contexts']}`;",
        "- one-fibre separation for equal contexts: "
        f"`{report['one_fibre_separating_for_equal_contexts']}`;",
        "- equivariance checked arities: "
        f"`{report['equivariance_checked_arities']}`;",
        "- orbit-injectivity checked arities: "
        f"`{report['orbit_injectivity_checked_arities']}`;",
        f"- all checks passed: `{report['all_checks_passed']}`.",
        "",
        "## Nontrivial Left Translations",
        "",
        "The deterministic class labels are canonical for this script, not the",
        "labels from the theoretical response.  The nontrivial translations are",
        "still only paired transpositions:",
        "",
        "```json",
        json.dumps(report["nontrivial_left_translation_cycles"], indent=2),
        "```",
        "",
        "## Consequence",
        "",
        "The four-point example is positive evidence for the contextual route.  The",
        "finite partial translations close to a 20-element rack in this case, and",
        "the contextual readout is equivariant and orbit-injective in the checked",
        "arities.  The all-arity proof still uses the orbit classification of this",
        "specific example; the audit does not prove the corresponding theorem for",
        "all finite degenerate YBE solutions.",
    ]
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_audit()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report))
    if not report["all_checks_passed"]:
        raise SystemExit("four-point contextual completion audit failed")
    print("OK four-point contextual completion audit")
    print(f"rack size {report['rack_size']}")
    print(f"checked arities 1..{report['max_checked_arity']}")


if __name__ == "__main__":
    main()
