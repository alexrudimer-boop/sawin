"""Audit identity-extension completion for linear F3 skew-over-flip solutions."""

from __future__ import annotations

import itertools
import json
import sys
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

P = 3
BASES = (0, 1)
FIBRES = tuple(range(P))
COLORS = tuple(range(2 * P))
PAIRS = tuple(itertools.product(COLORS, repeat=2))

OUT_JSON = ROOT / "proofs" / "linear_f3_skew_flip_completion_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_skew_flip_completion_audit.md"


def base(color: int) -> int:
    return color // P


def fibre(color: int) -> int:
    return color % P


def color(base_value: int, fibre_value: int) -> int:
    return P * base_value + fibre_value


def det2(matrix: tuple[int, int, int, int]) -> int:
    a, b, c, d = matrix
    return (a * d - b * c) % P


def mat2_apply(matrix: tuple[int, int, int, int], i: int, j: int) -> tuple[int, int]:
    a, b, c, d = matrix
    return (a * i + b * j) % P, (c * i + d * j) % P


def mat2_mul(
    left: tuple[int, int, int, int],
    right: tuple[int, int, int, int],
) -> tuple[int, int, int, int]:
    a, b, c, d = left
    e, f, g, h = right
    return (
        (a * e + b * g) % P,
        (a * f + b * h) % P,
        (c * e + d * g) % P,
        (c * f + d * h) % P,
    )


def mat3_mul(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(
        sum(left[3 * row + inner] * right[3 * inner + col] for inner in range(3)) % P
        for row in range(3)
        for col in range(3)
    )


def embed12(matrix: tuple[int, int, int, int]) -> tuple[int, ...]:
    a, b, c, d = matrix
    return (a, b, 0, c, d, 0, 0, 0, 1)


def embed23(matrix: tuple[int, int, int, int]) -> tuple[int, ...]:
    a, b, c, d = matrix
    return (1, 0, 0, 0, a, b, 0, c, d)


def compose(left: tuple[int, ...], right: tuple[int, ...]) -> tuple[int, ...]:
    """Return left after right."""

    return tuple(left[right[index]] for index in range(len(left)))


def inverse_perm(perm: tuple[int, ...]) -> tuple[int, ...]:
    inverse = [0] * len(perm)
    for index, image in enumerate(perm):
        inverse[image] = index
    return tuple(inverse)


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


def gl2_f3() -> tuple[tuple[int, int, int, int], ...]:
    return tuple(
        matrix
        for matrix in itertools.product(range(P), repeat=4)
        if det2(matrix) != 0
    )


GL2 = gl2_f3()
IDENTITY2 = (1, 0, 0, 1)


def precompute_ybe_relation() -> set[tuple[int, int, int]]:
    e12 = tuple(embed12(matrix) for matrix in GL2)
    e23 = tuple(embed23(matrix) for matrix in GL2)
    relation = set()
    for left_index in range(len(GL2)):
        for middle_index in range(len(GL2)):
            left_prefix = mat3_mul(e12[left_index], e23[middle_index])
            right_suffix = mat3_mul(e12[middle_index], e23[left_index])
            for right_index in range(len(GL2)):
                left_side = mat3_mul(left_prefix, e12[right_index])
                right_side = mat3_mul(e23[right_index], right_suffix)
                if left_side == right_side:
                    relation.add((left_index, middle_index, right_index))
    return relation


YBE_RELATION = precompute_ybe_relation()


def quadruple_is_ybe(indices: tuple[int, int, int, int]) -> bool:
    m00, m01, m10, m11 = indices
    required = (
        (m00, m00, m00),
        (m01, m01, m00),
        (m10, m00, m01),
        (m11, m01, m01),
        (m00, m10, m10),
        (m01, m11, m10),
        (m10, m10, m11),
        (m11, m11, m11),
    )
    return all(triple in YBE_RELATION for triple in required)


def table_from_indices(indices: tuple[int, int, int, int]) -> tuple[tuple[int, int], ...]:
    matrices = tuple(GL2[index] for index in indices)
    table = []
    for x, y in PAIRS:
        a, i = base(x), fibre(x)
        b, j = base(y), fibre(y)
        out_i, out_j = mat2_apply(matrices[2 * a + b], i, j)
        table.append((color(b, out_i), color(a, out_j)))
    return tuple(table)


def is_nondegenerate(table: tuple[tuple[int, int], ...]) -> bool:
    size = len(COLORS)
    for x in COLORS:
        if len({table[size * x + y][0] for y in COLORS}) != size:
            return False
    for y in COLORS:
        if len({table[size * x + y][1] for x in COLORS}) != size:
            return False
    return True


def is_involutive_indices(indices: tuple[int, int, int, int]) -> bool:
    m00, m01, m10, m11 = (GL2[index] for index in indices)
    return (
        mat2_mul(m00, m00) == IDENTITY2
        and mat2_mul(m11, m11) == IDENTITY2
        and mat2_mul(m10, m01) == IDENTITY2
        and mat2_mul(m01, m10) == IDENTITY2
    )


def contextual_completion(table: tuple[tuple[int, int], ...]) -> dict:
    size = len(COLORS)
    inverse_table = {table[size * x + y]: (x, y) for x, y in PAIRS}
    r_maps = {
        y: tuple(table[size * x + y][1] for x in COLORS)
        for y in COLORS
    }
    m_maps = {
        u: tuple(inverse_table[(u, v)][0] for v in COLORS)
        for u in COLORS
    }
    left_monoid = close_monoid(set(m_maps.values()))
    right_monoid = close_monoid(set(r_maps.values()))
    left_index = {mapping: index for index, mapping in enumerate(left_monoid)}
    right_index = {mapping: index for index, mapping in enumerate(right_monoid)}

    triples = tuple(
        (left, x, right)
        for left in range(len(left_monoid))
        for x in COLORS
        for right in range(len(right_monoid))
    )
    triple_index = {triple: index for index, triple in enumerate(triples)}
    uf = UnionFind(len(triples))

    for left_id, left_map in enumerate(left_monoid):
        for right_id, right_map in enumerate(right_monoid):
            for x, y in PAIRS:
                u, v = table[size * x + y]
                first = (
                    left_id,
                    x,
                    right_index[compose(right_map, r_maps[y])],
                )
                second = (
                    left_index[compose(left_map, m_maps[u])],
                    v,
                    right_id,
                )
                uf.union(triple_index[first], triple_index[second])

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
    for left_id, left_map in enumerate(left_monoid):
        for right_id, right_map in enumerate(right_monoid):
            for x, y in PAIRS:
                u, v = table[size * x + y]
                p = class_of_triple[
                    (
                        left_id,
                        x,
                        right_index[compose(right_map, r_maps[y])],
                    )
                ]
                q = class_of_triple[
                    (
                        left_index[compose(left_map, m_maps[x])],
                        y,
                        right_id,
                    )
                ]
                out = class_of_triple[
                    (
                        left_id,
                        u,
                        right_index[compose(right_map, r_maps[v])],
                    )
                ]
                previous = partial[p].get(q)
                if previous is not None and previous != out:
                    conflicts.append((p, q, previous, out))
                partial[p][q] = out

    identity = tuple(range(class_count))
    left_translations = []
    domain_equals_image = True
    partial_injective = True
    for p in range(class_count):
        domain = set(partial[p])
        image = set(partial[p].values())
        if domain != image:
            domain_equals_image = False
        if len(image) != len(partial[p]):
            partial_injective = False
        row = list(identity)
        for source, target in partial[p].items():
            row[source] = target
        left_translations.append(tuple(row))

    total_permutations = all(len(set(row)) == class_count for row in left_translations)
    involutions = all(compose(row, row) == identity for row in left_translations)
    commuting = all(
        compose(left_translations[p], left_translations[q])
        == compose(left_translations[q], left_translations[p])
        for p in range(class_count)
        for q in range(class_count)
    )
    covariance = False
    if total_permutations:
        inverses = tuple(inverse_perm(row) for row in left_translations)
        covariance = True
        for p in range(class_count):
            for q in range(class_count):
                conjugate = compose(
                    compose(left_translations[p], left_translations[q]),
                    inverses[p],
                )
                if left_translations[left_translations[p][q]] != conjugate:
                    covariance = False
                    break
            if not covariance:
                break

    forced_product_count = sum(len(row) for row in partial.values())
    return {
        "left_monoid_size": len(left_monoid),
        "right_monoid_size": len(right_monoid),
        "left_right_monoids_equal": set(left_monoid) == set(right_monoid),
        "quotient_class_count": class_count,
        "forced_product_count": forced_product_count,
        "domain_sizes": tuple(sorted({len(row) for row in partial.values()})),
        "conflict_count": len(conflicts),
        "partial_translations_injective": partial_injective,
        "balanced_domains": domain_equals_image,
        "identity_extension_total_permutations": total_permutations,
        "identity_extension_involutions": involutions,
        "identity_extension_commuting": commuting,
        "identity_extension_conjugacy_covariance": covariance,
        "nontrivial_left_translation_count": sum(
            1 for row in left_translations if row != identity
        ),
    }


def run_audit() -> dict:
    classification_counts = Counter()
    contextual_counts = Counter()
    contextual_failures = []
    left_right_monoids_unequal = 0
    total_checked = 0
    first_noninvolutive_translation = None

    for indices in itertools.product(range(len(GL2)), repeat=4):
        total_checked += 1
        if not quadruple_is_ybe(indices):
            continue

        table = table_from_indices(indices)
        nondegenerate = is_nondegenerate(table)
        involutive = is_involutive_indices(indices)
        if nondegenerate and involutive:
            classification = "nondegenerate_involutive"
        elif nondegenerate:
            classification = "nondegenerate_noninvolutive"
        elif involutive:
            classification = "degenerate_involutive"
        else:
            classification = "degenerate_noninvolutive"
        classification_counts[classification] += 1

        if classification == "nondegenerate_noninvolutive" and first_noninvolutive_translation is None:
            stats = contextual_completion(table)
            if not stats["identity_extension_involutions"]:
                first_noninvolutive_translation = {
                    "matrix_indices": list(indices),
                    "matrices": [list(GL2[index]) for index in indices],
                    "contextual_stats": stats,
                }

        if classification != "degenerate_noninvolutive":
            continue

        stats = contextual_completion(table)
        if not stats["left_right_monoids_equal"]:
            left_right_monoids_unequal += 1
        key = (
            stats["left_monoid_size"],
            stats["right_monoid_size"],
            stats["quotient_class_count"],
            stats["forced_product_count"],
            stats["domain_sizes"],
        )
        contextual_counts[key] += 1
        if not (
            stats["conflict_count"] == 0
            and stats["partial_translations_injective"]
            and stats["balanced_domains"]
            and stats["identity_extension_total_permutations"]
            and stats["identity_extension_conjugacy_covariance"]
        ):
            contextual_failures.append(
                {
                    "matrix_indices": list(indices),
                    "matrices": [list(GL2[index]) for index in indices],
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
        for key, count in sorted(contextual_counts.items(), key=lambda item: (-item[1], item[0]))
    ]
    report = {
        "family": "linear_f3_skew_over_flip",
        "gl2_f3_count": len(GL2),
        "total_tables_checked": total_checked,
        "expected_total_tables": len(GL2) ** 4,
        "ybe_solution_count": sum(classification_counts.values()),
        "classification_counts": dict(sorted(classification_counts.items())),
        "degenerate_noninvolutive_contextual_summary": contextual_rows,
        "left_right_monoids_unequal_count": left_right_monoids_unequal,
        "contextual_failure_count": len(contextual_failures),
        "contextual_failures": contextual_failures[:8],
        "first_noninvolutive_contextual_translation_example": first_noninvolutive_translation,
    }
    report["all_claimed_checks_passed"] = (
        len(GL2) == 48
        and total_checked == 48**4
        and report["ybe_solution_count"] == 1088
        and classification_counts["nondegenerate_noninvolutive"] == 816
        and classification_counts["degenerate_noninvolutive"] == 144
        and classification_counts["degenerate_involutive"] == 96
        and classification_counts["nondegenerate_involutive"] == 32
        and not contextual_failures
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Skew-Over-Flip Completion Audit",
        "",
        "This generated audit enumerates six-point linear skew-over-flip",
        "solutions",
        "",
        "```text",
        "X={0,1} x F_3",
        "R((a,i),(b,j))=((b,I),(a,J))",
        "(I,J)^T = M_ab (i,j)^T,  M_ab in GL_2(F_3).",
        "```",
        "",
        "The audit focuses on the finite hypotheses of the identity-extension",
        "completion lemma: balanced domains and conjugacy covariance.",
        "",
        "## Classification",
        "",
        f"- `GL_2(F_3)` size: `{report['gl2_f3_count']}`;",
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
            "For every one of the 144 degenerate non-involutive rows, the audit",
            "checks:",
            "",
            "```text",
            "forced products have no representative-independence conflicts;",
            "forced partial translations are injective;",
            "lambda_p(D_p)=D_p for every p;",
            "identity-outside L_p are total permutations;",
            "L_{L_p(q)}=L_p L_q L_p^{-1} for every p,q.",
            "```",
            "",
            "- degenerate non-involutive rows where `M_L` and `M_R` differ as",
            f"  sets of maps: `{report['left_right_monoids_unequal_count']}`;",
            f"- contextual failure count: `{report['contextual_failure_count']}`.",
            "",
            "## Consequence",
            "",
            "The finite totalization obstruction still does not occur in this",
            "six-point ternary-fibre linear family.  This audit does not check",
            "all-arity orbit separation.  It verifies only the finite rack",
            "completion hypotheses from the identity-extension lemma.",
        ]
    )
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_audit()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report))
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 skew-over-flip completion audit failed")
    print("OK linear F3 skew-over-flip completion audit")
    print(f"tables checked {report['total_tables_checked']}")
    print(f"YBE solutions {report['ybe_solution_count']}")
    print(f"classification {report['classification_counts']}")


if __name__ == "__main__":
    main()
