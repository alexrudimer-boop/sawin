"""Audit the gap-corrected hidden-fibre invariant for linear F3 collision rows."""

from __future__ import annotations

import itertools
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(TOOLS))

from run_linear_f3_skew_flip_completion_audit import (  # noqa: E402
    COLORS,
    fibre,
    table_from_indices,
)
from run_linear_f3_skew_flip_monolith_audit import (  # noqa: E402
    meet_partitions,
    solution_from_table,
)
from ybe_domination import (  # noqa: E402
    congruences,
    equality_congruence,
    quotient_solution,
)

SOURCE_JSON = ROOT / "proofs" / "linear_f3_collision_quotient_invariant_audit.json"
OUT_JSON = ROOT / "proofs" / "linear_f3_gap_corrected_invariant_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_gap_corrected_invariant_audit.md"

P = 3
IDENTITY_AFFINE = (1, 0)


def affine_apply(action: tuple[int, int], value: int) -> int:
    alpha, beta = action
    return (alpha * value + beta) % P


def affine_compose(
    left: tuple[int, int],
    right: tuple[int, int],
) -> tuple[int, int]:
    """Return left after right."""

    return (
        (left[0] * right[0]) % P,
        (left[0] * right[1] + left[1]) % P,
    )


def invert_map(mapping: dict[int, int]) -> dict[int, int]:
    return {value: key for key, value in mapping.items()}


def compose_maps(left: dict[int, int], right: dict[int, int]) -> dict[int, int]:
    return {key: left[right[key]] for key in right}


def map_powers(mapping: dict[int, int]) -> list[dict[int, int]]:
    powers = []
    current = {key: key for key in mapping}
    seen = set()
    while True:
        marker = tuple(current[key] for key in sorted(current))
        if marker in seen:
            return powers
        seen.add(marker)
        powers.append(dict(current))
        current = compose_maps(mapping, current)


def choose_color(block, hidden_value: int = 0) -> int:
    if len(block) == 1:
        return next(iter(block))
    for color in block:
        if fibre(color) == hidden_value:
            return color
    raise ValueError(f"no colour with fibre {hidden_value} in {block}")


def row_solution_data(matrix_indices: tuple[int, int, int, int]):
    solution = solution_from_table(table_from_indices(matrix_indices))
    all_congruences = congruences(solution, max_size=7)
    equality = equality_congruence(solution.elements)
    monolith = meet_partitions(
        [partition for partition in all_congruences if partition != equality]
    )
    qmap = quotient_solution(solution, monolith)
    collapsed = next(block for block in monolith if len(block) == 3)
    singleton_blocks = {
        next(iter(block)): block
        for block in monolith
        if len(block) == 1
    }
    return solution, qmap.quotient, qmap.pi, collapsed, singleton_blocks


def local_gap_certificate(row: dict) -> dict:
    cert = row["quotient_invariant_certificate"]
    solution, quotient, _pi, collapsed, singleton_blocks = row_solution_data(
        tuple(row["matrix_indices"])
    )
    singletons = tuple(cert["singleton_colors"])
    singleton_set = set(singletons)
    collapsed_set = set(cert["collapsed_block"])
    s_actions = {int(key): tuple(value) for key, value in cert["singleton_actions"].items()}
    alpha = {
        int(key): value
        for key, value in cert["singleton_after_left_crossing"].items()
    }
    beta = {
        int(key): value["output_singleton"]
        for key, value in cert["right_actions"].items()
    }
    t_actions = {
        int(key): tuple(value["hidden_action"])
        for key, value in cert["right_actions"].items()
    }

    problems = []
    if beta != invert_map(alpha):
        problems.append(
            {
                "kind": "beta_not_alpha_inverse",
                "alpha": alpha,
                "beta": beta,
                "alpha_inverse": invert_map(alpha),
            }
        )

    for left, right in itertools.product(collapsed_set, repeat=2):
        if solution.R[(left, right)] != (left, right):
            problems.append(
                {
                    "kind": "collapsed_self_crossing_not_identity",
                    "input": [left, right],
                    "output": list(solution.R[(left, right)]),
                }
            )
            break

    alpha_powers = map_powers(alpha)
    for z, w in itertools.product(singletons, repeat=2):
        out_left, out_right = quotient.R[(singleton_blocks[z], singleton_blocks[w])]
        u = choose_color(out_left)
        v = choose_color(out_right)
        if u not in singleton_set or v not in singleton_set:
            problems.append(
                {
                    "kind": "visible_crossing_leaves_singleton_layer",
                    "input": [z, w],
                    "output": [u, v],
                }
            )
            continue
        for power in alpha_powers:
            lhs = affine_compose(s_actions[power[z]], s_actions[power[w]])
            rhs = affine_compose(s_actions[power[u]], s_actions[power[v]])
            if lhs != rhs:
                problems.append(
                    {
                        "kind": "alpha_equivariant_visible_visible_failure",
                        "input": [z, w],
                        "output": [u, v],
                        "alpha_power": power,
                        "lhs": lhs,
                        "rhs": rhs,
                    }
                )
                break

    for z in singletons:
        tracked = affine_compose(s_actions[beta[z]], t_actions[z])
        if tracked != IDENTITY_AFFINE:
            problems.append(
                {
                    "kind": "tracked_crossing_failure",
                    "singleton": z,
                    "composition": tracked,
                }
            )

    return {
        "certified": not problems,
        "alpha": alpha,
        "beta": beta,
        "alpha_order": len(alpha_powers),
        "problem_count": len(problems),
        "problems": problems[:8],
    }


def tagged_word(word: tuple[int, ...], collapsed: frozenset[int]) -> tuple[tuple, ...]:
    next_hidden_id = 0
    out = []
    for color in word:
        if color in collapsed:
            out.append(("F", next_hidden_id, fibre(color)))
            next_hidden_id += 1
        else:
            out.append(("V", color))
    return tuple(out)


def tag_to_color(item, collapsed: frozenset[int]) -> int:
    if item[0] == "V":
        return item[1]
    return choose_color(collapsed, item[2])


def color_with_tag(color: int, hidden_ids: list[int], collapsed: frozenset[int]):
    if color in collapsed:
        return ("F", hidden_ids.pop(0), fibre(color))
    return ("V", color)


def apply_tagged_pair(
    solution,
    tagged: tuple[tuple, ...],
    collapsed: frozenset[int],
    index: int,
    *,
    inverse: bool,
) -> tuple[tuple, ...]:
    left, right = tagged[index], tagged[index + 1]
    table = solution.inverse_R if inverse else solution.R
    output_colors = table[(tag_to_color(left, collapsed), tag_to_color(right, collapsed))]
    hidden_ids = [item[1] for item in (left, right) if item[0] == "F"]
    output_items = tuple(
        color_with_tag(color, hidden_ids, collapsed)
        for color in output_colors
    )
    if hidden_ids:
        raise ValueError("not every hidden strand tag was propagated")
    return tagged[:index] + output_items + tagged[index + 2 :]


def gap_corrected_invariants(
    tagged: tuple[tuple, ...],
    s_actions: dict[int, tuple[int, int]],
    alpha: dict[int, int],
) -> dict[int, int]:
    invariants = {}
    for index, item in enumerate(tagged):
        if item[0] != "F":
            continue
        _kind, hidden_id, hidden_value = item
        action = IDENTITY_AFFINE
        for left_index, left_item in enumerate(tagged[:index]):
            if left_item[0] != "V":
                continue
            gap = sum(1 for middle in tagged[left_index + 1:index] if middle[0] == "F")
            effective = left_item[1]
            for _ in range(gap):
                effective = alpha[effective]
            action = affine_compose(action, s_actions[effective])
        invariants[hidden_id] = affine_apply(action, hidden_value)
    return invariants


def direct_invariant_check(row: dict, max_arity: int) -> dict:
    cert = row["quotient_invariant_certificate"]
    solution, _quotient, _pi, collapsed, _singleton_blocks = row_solution_data(
        tuple(row["matrix_indices"])
    )
    collapsed = frozenset(collapsed)
    s_actions = {int(key): tuple(value) for key, value in cert["singleton_actions"].items()}
    alpha = {
        int(key): value
        for key, value in cert["singleton_after_left_crossing"].items()
    }
    checked_moves = 0
    for arity in range(1, max_arity + 1):
        for word in itertools.product(COLORS, repeat=arity):
            tagged = tagged_word(tuple(word), collapsed)
            before = gap_corrected_invariants(tagged, s_actions, alpha)
            for index in range(arity - 1):
                for inverse in (False, True):
                    checked_moves += 1
                    image = apply_tagged_pair(
                        solution,
                        tagged,
                        collapsed,
                        index,
                        inverse=inverse,
                    )
                    after = gap_corrected_invariants(image, s_actions, alpha)
                    if before != after:
                        return {
                            "max_arity": max_arity,
                            "checked_moves": checked_moves,
                            "failure_count": 1,
                            "failure": {
                                "arity": arity,
                                "word": list(word),
                                "index": index,
                                "inverse": inverse,
                                "before": before,
                                "after": after,
                                "image": [repr(item) for item in image],
                            },
                        }
    return {
        "max_arity": max_arity,
        "checked_moves": checked_moves,
        "failure_count": 0,
        "failure": None,
    }


def run_audit(max_direct_arity: int = 5) -> dict:
    source = json.loads(SOURCE_JSON.read_text(encoding="utf-8"))
    collision_rows = [
        row for row in source["rows"]
        if row.get("quotient_invariant_certificate")
    ]
    rows = []
    local_failures = []
    direct_failures = []
    for row in collision_rows:
        local = local_gap_certificate(row)
        direct = direct_invariant_check(row, max_direct_arity)
        if not local["certified"]:
            local_failures.append(row["row_index"])
        if direct["failure_count"]:
            direct_failures.append(row["row_index"])
        rows.append(
            {
                "row_index": row["row_index"],
                "matrix_indices": row["matrix_indices"],
                "previous_passive_certified": row["quotient_invariant_certificate"]["certified"],
                "gap_corrected_local_certificate": local,
                "gap_corrected_direct_invariant_check": direct,
            }
        )
    report = {
        "family": "linear_f3_skew_over_flip_formal_collision_rows",
        "source_artifact": str(SOURCE_JSON.relative_to(ROOT)),
        "collision_row_count": len(collision_rows),
        "max_direct_arity": max_direct_arity,
        "gap_corrected_local_success_count": len(collision_rows) - len(local_failures),
        "gap_corrected_local_failure_count": len(local_failures),
        "gap_corrected_local_failure_rows": local_failures,
        "gap_corrected_direct_failure_count": len(direct_failures),
        "gap_corrected_direct_failure_rows": direct_failures,
        "rows": rows,
    }
    report["all_claimed_checks_passed"] = (
        report["collision_row_count"] == 32
        and report["gap_corrected_local_success_count"] == 32
        and report["gap_corrected_local_failure_count"] == 0
        and report["gap_corrected_direct_failure_count"] == 0
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Gap-Corrected Invariant Audit",
        "",
        "This generated audit verifies the corrected multi-fibre invariant",
        "for all `32` formal monolith-collision rows in the six-point linear",
        "skew-over-flip family.",
        "",
        "## Summary",
        "",
        f"- source artifact: `{report['source_artifact']}`;",
        f"- collision rows: `{report['collision_row_count']}`;",
        "- gap-corrected local certificates: "
        f"`{report['gap_corrected_local_success_count']}`;",
        "- local certificate failures: "
        f"`{report['gap_corrected_local_failure_count']}`;",
        "- direct invariant arity check: "
        f"`1..{report['max_direct_arity']}`;",
        "- direct invariant failures: "
        f"`{report['gap_corrected_direct_failure_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "## Checked Identities",
        "",
        "For each row, let `alpha` be the visible-label transport in",
        "`zF -> F alpha(z)`, and let `beta` be the visible-label transport in",
        "`Fz -> beta(z)F`.  The audit checks:",
        "",
        "```text",
        "beta = alpha^{-1},",
        "S_{alpha^g z} S_{alpha^g w} = S_{alpha^g u} S_{alpha^g v}",
        "  whenever R_Z(z,w)=(u,v),",
        "S_{beta z} T_z = id,",
        "R(F_i,F_j)=(F_i,F_j).",
        "```",
        "",
        "It also directly checks the resulting tagged-strand invariant through",
        f"arity `{report['max_direct_arity']}` for positive and negative local",
        "crossings.",
        "",
        "## Consequence",
        "",
        "The earlier passive-left-list obstruction is repaired by using the",
        "number of collapsed-fibre strands between a visible letter and the",
        "tracked fibre.  If a visible label `z` lies to the left of a tracked",
        "`F`-strand with `g` other `F`-strands between them, the invariant uses",
        "`S_{alpha^g z}` rather than `S_z`.",
    ]
    if report["gap_corrected_local_failure_rows"] or report["gap_corrected_direct_failure_rows"]:
        lines.extend(["", "## Failures", "", "```json"])
        lines.append(
            json.dumps(
                {
                    "local": report["gap_corrected_local_failure_rows"],
                    "direct": report["gap_corrected_direct_failure_rows"],
                },
                indent=2,
            )
        )
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_audit()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 gap-corrected invariant audit failed")
    print("OK linear F3 gap-corrected invariant audit")
    print(f"collision rows {report['collision_row_count']}")
    print(
        "gap-corrected local certificates "
        f"{report['gap_corrected_local_success_count']}"
    )


if __name__ == "__main__":
    main()
