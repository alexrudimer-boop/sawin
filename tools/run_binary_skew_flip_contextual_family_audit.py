"""Audit binary skew-over-flip four-point YBE contextual completions."""

from __future__ import annotations

import itertools
import json
import sys
from collections import Counter, defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import FiniteBraidedSet, is_rack_solution, rack_solution  # noqa: E402


OUT_JSON = ROOT / "proofs" / "binary_skew_flip_contextual_family_audit.json"
OUT_MD = ROOT / "proofs" / "binary_skew_flip_contextual_family_audit.md"

COLORS = tuple(range(4))
LABELS = ("00", "01", "10", "11")
FIBRE_PERMS = tuple(itertools.permutations(range(4)))
TRIPLES = tuple(itertools.product(COLORS, repeat=3))
PAIRS = tuple(itertools.product(COLORS, repeat=2))


def base(color: int) -> int:
    return color >> 1


def fibre(color: int) -> int:
    return color & 1


def color(label_base: int, label_fibre: int) -> int:
    return 2 * label_base + label_fibre


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Composition convention used by contextual products: left after right."""

    return tuple(left[right[i]] for i in range(len(left)))


def table_from_fibre_perms(perms: tuple[tuple[int, ...], ...]) -> tuple[tuple[int, int], ...]:
    table = []
    for x, y in PAIRS:
        a, i = base(x), fibre(x)
        b, j = base(y), fibre(y)
        output_fibres = perms[2 * a + b][2 * i + j]
        out_i = output_fibres >> 1
        out_j = output_fibres & 1
        table.append((color(b, out_i), color(a, out_j)))
    return tuple(table)


def apply_at(
    triple: tuple[int, int, int],
    index: int,
    table: tuple[tuple[int, int], ...],
) -> tuple[int, int, int]:
    out = list(triple)
    x, y = out[index], out[index + 1]
    out[index], out[index + 1] = table[4 * x + y]
    return tuple(out)


def is_ybe_table(table: tuple[tuple[int, int], ...]) -> bool:
    for triple in TRIPLES:
        left = apply_at(apply_at(apply_at(triple, 0, table), 1, table), 0, table)
        right = apply_at(apply_at(apply_at(triple, 1, table), 0, table), 1, table)
        if left != right:
            return False
    return True


def is_involutive(table: tuple[tuple[int, int], ...]) -> bool:
    return all(table[4 * table[4 * x + y][0] + table[4 * x + y][1]] == (x, y) for x, y in PAIRS)


def is_nondegenerate(table: tuple[tuple[int, int], ...]) -> bool:
    for x in COLORS:
        if len({table[4 * x + y][0] for y in COLORS}) != len(COLORS):
            return False
    for y in COLORS:
        if len({table[4 * x + y][1] for x in COLORS}) != len(COLORS):
            return False
    return True


def close_monoid(generators: set[tuple[int, ...]]) -> tuple[tuple[int, ...], ...]:
    identity = tuple(range(len(COLORS)))
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


def contextual_completion_stats(table: tuple[tuple[int, int], ...]) -> dict:
    inverse = {table[4 * x + y]: (x, y) for x, y in PAIRS}
    r_maps = {
        y: tuple(table[4 * x + y][1] for x in COLORS)
        for y in COLORS
    }
    m_maps = {
        u: tuple(inverse[(u, v)][0] for v in COLORS)
        for u in COLORS
    }

    left_monoid = close_monoid(set(m_maps.values()))
    right_monoid = close_monoid(set(r_maps.values()))
    left_index = {mapping: index for index, mapping in enumerate(left_monoid)}
    right_index = {mapping: index for index, mapping in enumerate(right_monoid)}

    triples = tuple(
        (a_index, x, b_index)
        for a_index in range(len(left_monoid))
        for x in COLORS
        for b_index in range(len(right_monoid))
    )
    triple_index = {triple: index for index, triple in enumerate(triples)}
    uf = UnionFind(len(triples))

    for a_index, a_map in enumerate(left_monoid):
        for b_index, b_map in enumerate(right_monoid):
            for x, y in PAIRS:
                u, v = table[4 * x + y]
                left = (
                    a_index,
                    x,
                    right_index[compose(b_map, r_maps[y])],
                )
                right = (
                    left_index[compose(a_map, m_maps[u])],
                    v,
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

    class_count = len(class_index_by_root)
    partial: dict[int, dict[int, int]] = {index: {} for index in range(class_count)}
    conflicts = []
    for a_index, a_map in enumerate(left_monoid):
        for b_index, b_map in enumerate(right_monoid):
            for x, y in PAIRS:
                u, v = table[4 * x + y]
                p = class_of_triple[
                    (
                        a_index,
                        x,
                        right_index[compose(b_map, r_maps[y])],
                    )
                ]
                q = class_of_triple[
                    (
                        left_index[compose(a_map, m_maps[x])],
                        y,
                        b_index,
                    )
                ]
                out = class_of_triple[
                    (
                        a_index,
                        u,
                        right_index[compose(b_map, r_maps[v])],
                    )
                ]
                previous = partial[p].get(q)
                if previous is not None and previous != out:
                    conflicts.append((p, q, previous, out, a_index, b_index, x, y))
                partial[p][q] = out

    left_translations = []
    for p in range(class_count):
        row = list(range(class_count))
        for source, target in partial[p].items():
            row[source] = target
        left_translations.append(tuple(row))

    identity = tuple(range(class_count))
    permutations = all(len(set(row)) == class_count for row in left_translations)
    involutions = all(compose(row, row) == identity for row in left_translations)
    commuting = all(
        compose(left_translations[p], left_translations[q])
        == compose(left_translations[q], left_translations[p])
        for p in range(class_count)
        for q in range(class_count)
    )
    index_stability = all(
        left_translations[left_translations[p][q]] == left_translations[q]
        for p in range(class_count)
        for q in range(class_count)
    )
    rack_ybe = False
    rack_form = False
    if permutations:
        rack = rack_solution(tuple(range(class_count)), lambda left, right: left_translations[left][right])
        rack_ybe = rack.is_ybe()
        rack_form = is_rack_solution(rack)

    forced_product_count = sum(len(row) for row in partial.values())
    domain_sizes = tuple(sorted({len(row) for row in partial.values()}))
    nontrivial_count = sum(1 for row in left_translations if row != identity)

    return {
        "left_monoid_size": len(left_monoid),
        "right_monoid_size": len(right_monoid),
        "left_right_monoids_equal": set(left_monoid) == set(right_monoid),
        "quotient_class_count": class_count,
        "forced_product_count": forced_product_count,
        "domain_sizes": domain_sizes,
        "conflict_count": len(conflicts),
        "partial_translations_injective": all(
            len(set(row.values())) == len(row)
            for row in partial.values()
        ),
        "identity_fill_is_permutation": permutations,
        "identity_fill_involutions": involutions,
        "identity_fill_commuting": commuting,
        "identity_fill_index_stability": index_stability,
        "identity_fill_rack_ybe": rack_ybe,
        "identity_fill_rack_form": rack_form,
        "nontrivial_left_translation_count": nontrivial_count,
    }


def run_audit() -> dict:
    classification_counts = Counter()
    contextual_counts = Counter()
    contextual_failures = []
    sample_cases = []
    total_checked = 0

    for perms in itertools.product(FIBRE_PERMS, repeat=4):
        total_checked += 1
        table = table_from_fibre_perms(perms)
        if not is_ybe_table(table):
            continue

        nondegenerate = is_nondegenerate(table)
        involutive = is_involutive(table)
        if nondegenerate:
            classification = "nondegenerate"
        elif involutive:
            classification = "degenerate_involutive"
        else:
            classification = "degenerate_noninvolutive"
        classification_counts[classification] += 1

        if classification != "degenerate_noninvolutive":
            continue

        stats = contextual_completion_stats(table)
        key = (
            stats["left_monoid_size"],
            stats["right_monoid_size"],
            stats["quotient_class_count"],
            stats["forced_product_count"],
            stats["domain_sizes"],
        )
        contextual_counts[key] += 1
        if len(sample_cases) < 8:
            sample_cases.append(
                {
                    "fibre_perms": [list(perm) for perm in perms],
                    "contextual_stats": stats,
                }
            )
        if not (
            stats["left_right_monoids_equal"]
            and stats["conflict_count"] == 0
            and stats["partial_translations_injective"]
            and stats["identity_fill_is_permutation"]
            and stats["identity_fill_involutions"]
            and stats["identity_fill_commuting"]
            and stats["identity_fill_index_stability"]
            and stats["identity_fill_rack_ybe"]
            and stats["identity_fill_rack_form"]
        ):
            contextual_failures.append(
                {
                    "fibre_perms": [list(perm) for perm in perms],
                    "contextual_stats": stats,
                }
            )

    contextual_rows = [
        {
            "case_count": count,
            "left_monoid_size": key[0],
            "right_monoid_size": key[1],
            "quotient_class_count": key[2],
            "forced_product_count": key[3],
            "domain_sizes": list(key[4]),
        }
        for key, count in sorted(
            contextual_counts.items(),
            key=lambda item: (-item[1], item[0]),
        )
    ]

    report = {
        "family": "binary_skew_over_flip",
        "total_tables_checked": total_checked,
        "expected_total_tables": 24**4,
        "ybe_solution_count": sum(classification_counts.values()),
        "classification_counts": dict(sorted(classification_counts.items())),
        "degenerate_noninvolutive_contextual_summary": contextual_rows,
        "contextual_failure_count": len(contextual_failures),
        "contextual_failures": contextual_failures[:8],
        "sample_degenerate_noninvolutive_cases": sample_cases,
        "all_claimed_checks_passed": (
            total_checked == 24**4
            and sum(classification_counts.values()) == 520
            and classification_counts["nondegenerate"] == 384
            and classification_counts["degenerate_involutive"] == 64
            and classification_counts["degenerate_noninvolutive"] == 72
            and not contextual_failures
        ),
    }
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Binary Skew-Over-Flip Contextual Family Audit",
        "",
        "This generated audit enumerates all binary skew-over-flip four-point",
        "solutions",
        "",
        "```text",
        "R((a,i),(b,j)) = ((b,I_ab(i,j)), (a,J_ab(i,j)))",
        "```",
        "",
        "where each fibre map on `{0,1}^2` is an arbitrary permutation.",
        "",
        "## Classification",
        "",
        f"- tables checked: `{report['total_tables_checked']}`;",
        f"- YBE solutions: `{report['ybe_solution_count']}`;",
        f"- classification counts: `{report['classification_counts']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "## Degenerate Non-Involutive Contextual Summary",
        "",
        "| cases | M_L size | M_R size | P size | forced products | domain sizes |",
        "|---:|---:|---:|---:|---:|---|",
    ]
    for row in report["degenerate_noninvolutive_contextual_summary"]:
        lines.append(
            "| {case_count} | {left_monoid_size} | {right_monoid_size} | "
            "{quotient_class_count} | {forced_product_count} | {domain_sizes} |".format(
                **row
            )
        )
    lines.extend(
        [
            "",
            "For every degenerate non-involutive row, the audit checks that",
            "`M_L` and `M_R` have the same underlying maps, the contextual quotient",
            "has no forced-product conflicts, every forced partial left translation",
            "is injective, and the identity fill is a rack made from commuting",
            "involutions satisfying `L_{L_p(q)}=L_q`.",
            "",
            f"- contextual failure count: `{report['contextual_failure_count']}`.",
            "",
            "## Consequence",
            "",
            "The contextual totalization obstruction does not occur in this full",
            "nearest four-point family.  The remaining search target is either a",
            "larger finite YBE-origin contextual partial rack whose forced",
            "translations cannot be completed by this commuting-involution fill, or",
            "a proof that YBE-origin contextual partial translations always admit a",
            "finite completion of this kind.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_audit()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report))
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("binary skew-over-flip contextual family audit failed")
    print("OK binary skew-over-flip contextual family audit")
    print(f"tables checked {report['total_tables_checked']}")
    print(f"YBE solutions {report['ybe_solution_count']}")
    print(f"classification {report['classification_counts']}")


if __name__ == "__main__":
    main()
