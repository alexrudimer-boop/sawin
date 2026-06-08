"""Audit contextual readout orbit separation for linear F3 skew-over-flip rows."""

from __future__ import annotations

import argparse
import itertools
import json
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(TOOLS))

from run_linear_f3_skew_flip_completion_audit import (  # noqa: E402
    COLORS,
    GL2,
    PAIRS,
    UnionFind,
    close_monoid,
    compose,
    contextual_completion,
    is_involutive_indices,
    is_nondegenerate,
    quadruple_is_ybe,
    table_from_indices,
)

OUT_JSON = ROOT / "proofs" / "linear_f3_skew_flip_orbit_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_skew_flip_orbit_audit.md"


def contextual_readout_builder(table: tuple[tuple[int, int], ...]):
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

    identity = tuple(range(size))

    def readout(word: tuple[int, ...]) -> tuple[int, ...]:
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
                    left_index[left_contexts[index]],
                    word[index],
                    right_index[right_contexts[index]],
                )
            ]
            for index in range(len(word))
        )

    return readout, len(class_index_by_root)


def apply_at(
    word: tuple[int, ...],
    index: int,
    table: tuple[tuple[int, int], ...],
    inverse_table: tuple[tuple[int, int], ...],
    inverse: bool = False,
) -> tuple[int, ...]:
    size = len(COLORS)
    out = list(word)
    x, y = out[index], out[index + 1]
    next_x, next_y = (inverse_table if inverse else table)[size * x + y]
    out[index], out[index + 1] = next_x, next_y
    return tuple(out)


def orbit_readout_collision(
    table: tuple[tuple[int, int], ...],
    readout,
    arity: int,
) -> dict | None:
    size = len(COLORS)
    inverse_dict = {table[size * x + y]: (x, y) for x, y in PAIRS}
    inverse_table = tuple(inverse_dict[(x, y)] for x, y in PAIRS)
    all_words = tuple(itertools.product(COLORS, repeat=arity))
    seen = set()
    orbit_count = 0
    max_orbit_size = 0

    for start in all_words:
        if start in seen:
            continue
        orbit_count += 1
        queue = deque([start])
        seen.add(start)
        readout_owner = {readout(start): start}
        orbit_size = 0
        while queue:
            current = queue.popleft()
            orbit_size += 1
            for generator_index in range(arity - 1):
                for inverse in (False, True):
                    image = apply_at(
                        current,
                        generator_index,
                        table,
                        inverse_table,
                        inverse=inverse,
                    )
                    image_readout = readout(image)
                    owner = readout_owner.get(image_readout)
                    if owner is not None and owner != image:
                        return {
                            "arity": arity,
                            "collision_readout": list(image_readout),
                            "first_word": list(owner),
                            "second_word": list(image),
                        }
                    readout_owner[image_readout] = image
                    if image not in seen:
                        seen.add(image)
                        queue.append(image)
        max_orbit_size = max(max_orbit_size, orbit_size)

    return {
        "arity": arity,
        "orbit_count": orbit_count,
        "max_orbit_size": max_orbit_size,
        "collision": None,
    }


def degenerate_noninvolutive_rows():
    for indices in itertools.product(range(len(GL2)), repeat=4):
        if not quadruple_is_ybe(indices):
            continue
        table = table_from_indices(indices)
        if is_nondegenerate(table) or is_involutive_indices(indices):
            continue
        yield indices, table


def run_audit(all_case_max_arity: int, representative_max_arity: int) -> dict:
    rows = list(degenerate_noninvolutive_rows())
    failures = []
    all_case_summaries = []
    representatives = {}

    for row_index, (indices, table) in enumerate(rows):
        stats = contextual_completion(table)
        key = (
            stats["left_monoid_size"],
            stats["right_monoid_size"],
            stats["quotient_class_count"],
            stats["forced_product_count"],
            tuple(stats["domain_sizes"]),
        )
        representatives.setdefault(key, (row_index, indices, table))
        readout, class_count = contextual_readout_builder(table)
        row_summary = {
            "row_index": row_index,
            "matrix_indices": list(indices),
            "context_key": {
                "left_monoid_size": key[0],
                "right_monoid_size": key[1],
                "quotient_class_count": key[2],
                "forced_product_count": key[3],
                "domain_sizes": list(key[4]),
            },
            "readout_class_count": class_count,
            "arity_checks": [],
        }
        for arity in range(1, all_case_max_arity + 1):
            result = orbit_readout_collision(table, readout, arity)
            row_summary["arity_checks"].append(result)
            if result.get("collision") is not None:
                failures.append(
                    {
                        "scope": "all_cases",
                        "row_index": row_index,
                        "matrix_indices": list(indices),
                        "result": result,
                    }
                )
                break
        all_case_summaries.append(row_summary)

    representative_summaries = []
    for key, (row_index, indices, table) in sorted(representatives.items()):
        readout, class_count = contextual_readout_builder(table)
        rep_summary = {
            "row_index": row_index,
            "matrix_indices": list(indices),
            "context_key": {
                "left_monoid_size": key[0],
                "right_monoid_size": key[1],
                "quotient_class_count": key[2],
                "forced_product_count": key[3],
                "domain_sizes": list(key[4]),
            },
            "readout_class_count": class_count,
            "arity_checks": [],
        }
        for arity in range(all_case_max_arity + 1, representative_max_arity + 1):
            result = orbit_readout_collision(table, readout, arity)
            rep_summary["arity_checks"].append(result)
            if result.get("collision") is not None:
                failures.append(
                    {
                        "scope": "representatives",
                        "row_index": row_index,
                        "matrix_indices": list(indices),
                        "result": result,
                    }
                )
                break
        representative_summaries.append(rep_summary)

    return {
        "family": "linear_f3_skew_over_flip",
        "degenerate_noninvolutive_rows": len(rows),
        "all_case_max_arity": all_case_max_arity,
        "representative_max_arity": representative_max_arity,
        "representative_context_type_count": len(representatives),
        "failure_count": len(failures),
        "failures": failures[:8],
        "all_case_summaries": all_case_summaries,
        "representative_summaries": representative_summaries,
        "all_claimed_checks_passed": len(rows) == 144 and not failures,
    }


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Skew-Over-Flip Orbit Audit",
        "",
        "This generated audit checks contextual readout orbit-injectivity for",
        "the 144 degenerate non-involutive six-point linear skew-over-flip rows.",
        "",
        "## Summary",
        "",
        f"- degenerate non-involutive rows: `{report['degenerate_noninvolutive_rows']}`;",
        f"- all rows checked through arity: `{report['all_case_max_arity']}`;",
        "- representative structural types checked through arity: "
        f"`{report['representative_max_arity']}`;",
        "- representative contextual type count: "
        f"`{report['representative_context_type_count']}`;",
        f"- orbit-injectivity failure count: `{report['failure_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "The check is finite evidence only.  It does not prove all-arity",
        "orbit-injectivity for this family or for arbitrary YBE solutions.",
    ]
    if report["failures"]:
        lines.extend(["", "## Failures", "", "```json"])
        lines.append(json.dumps(report["failures"], indent=2))
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--all-case-max-arity", type=int, default=5)
    parser.add_argument("--representative-max-arity", type=int, default=6)
    args = parser.parse_args()
    report = run_audit(args.all_case_max_arity, args.representative_max_arity)
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    OUT_MD.write_text(write_markdown(report))
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 skew-over-flip orbit audit failed")
    print("OK linear F3 skew-over-flip orbit audit")
    print(f"rows {report['degenerate_noninvolutive_rows']}")
    print(f"all rows through arity {report['all_case_max_arity']}")
    print(f"representatives through arity {report['representative_max_arity']}")


if __name__ == "__main__":
    main()
