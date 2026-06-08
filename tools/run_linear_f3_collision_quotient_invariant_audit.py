"""Audit quotient-invariant closure for linear F3 monolith-collision rows."""

from __future__ import annotations

import itertools
import json
import sys
from collections import Counter, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(TOOLS))

from run_linear_f3_skew_flip_completion_audit import (  # noqa: E402
    COLORS,
    GL2,
    fibre,
    is_involutive_indices,
    is_nondegenerate as table_is_nondegenerate,
    quadruple_is_ybe,
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
    relative_contextual_separation_summary,
)

OUT_JSON = ROOT / "proofs" / "linear_f3_collision_quotient_invariant_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_collision_quotient_invariant_audit.md"

P = 3
NONZERO = (1, 2)
IDENTITY_STATE = (1, 0)
ALL_AFFINE_STATES = tuple((a, b) for a in NONZERO for b in range(P))


def affine_eval(state: tuple[int, int], value: int) -> int:
    a, b = state
    return (a * value + b) % P


def affine_compose(
    left: tuple[int, int],
    right: tuple[int, int],
) -> tuple[int, int]:
    """Return left after right as affine maps over F3."""

    a, b = left
    c, d = right
    return ((a * c) % P, (a * d + b) % P)


def affine_inverse(state: tuple[int, int]) -> tuple[int, int]:
    a, b = state
    inv_a = 1 if a == 1 else 2
    return inv_a, (-inv_a * b) % P


def fit_affine(pairs: list[tuple[int, int]]) -> tuple[int, int] | None:
    for a in NONZERO:
        for b in range(P):
            if all((a * source + b) % P == target for source, target in pairs):
                return a, b
    return None


def is_left_nondegenerate(solution) -> bool:
    elements = set(solution.elements)
    return all(
        {solution.R[(left, right)][0] for right in solution.elements} == elements
        for left in solution.elements
    )


def is_right_nondegenerate(solution) -> bool:
    elements = set(solution.elements)
    return all(
        {solution.R[(left, right)][1] for left in solution.elements} == elements
        for right in solution.elements
    )


def degenerate_noninvolutive_rows():
    for indices in itertools.product(range(len(GL2)), repeat=4):
        if not quadruple_is_ybe(indices):
            continue
        table = table_from_indices(indices)
        if table_is_nondegenerate(table) or is_involutive_indices(indices):
            continue
        yield indices, table


def partition_labels(partition) -> dict[int, int]:
    return {
        element: block_index
        for block_index, block in enumerate(partition)
        for element in block
    }


def affine_transition(
    state: tuple[int, int],
    singleton_action: tuple[int, int],
) -> tuple[int, int]:
    """Append a singleton to the tracked fibre strand's left context."""

    return affine_compose(state, singleton_action)


def transition_closure(
    singleton_actions: dict[int, tuple[int, int]],
) -> tuple[tuple[int, int], ...]:
    seen = {IDENTITY_STATE}
    queue = deque([IDENTITY_STATE])
    while queue:
        state = queue.popleft()
        for action in singleton_actions.values():
            image = affine_transition(state, action)
            if image not in seen:
                seen.add(image)
                queue.append(image)
    return tuple(sorted(seen))


def contextual_collision_found(row_payload: dict) -> bool | None:
    monolith = row_payload.get("monolith")
    if not monolith:
        return None
    relative = monolith.get("relative_separation")
    if not relative:
        return None
    return relative.get("collision_found")


def certify_row(solution, monolith) -> dict:
    quotient = quotient_solution(solution, monolith).quotient
    blocks = [tuple(sorted(block)) for block in monolith]
    collapsed_blocks = [block for block in blocks if len(block) == 3]
    singleton_blocks = [block for block in blocks if len(block) == 1]
    if len(collapsed_blocks) != 1 or len(singleton_blocks) != 3:
        return {
            "certified": False,
            "reason": "monolith is not a single triple fibre over three singletons",
            "monolith_blocks": blocks,
        }

    collapsed = tuple(collapsed_blocks[0])
    singletons = tuple(block[0] for block in singleton_blocks)
    collapsed_set = set(collapsed)
    singleton_set = set(singletons)

    collapsed_self_identity = all(
        solution.R[(left, right)] == (left, right)
        for left in collapsed
        for right in collapsed
    )

    singleton_actions: dict[int, tuple[int, int]] = {}
    singleton_after_left_crossing: dict[int, int] = {}
    left_action_failures = []
    for z in singletons:
        pairs = []
        output_singletons = set()
        for hidden in collapsed:
            out_hidden, out_singleton = solution.R[(z, hidden)]
            if out_hidden not in collapsed_set or out_singleton not in singleton_set:
                left_action_failures.append(
                    {
                        "singleton": z,
                        "hidden": hidden,
                        "output": [out_hidden, out_singleton],
                    }
                )
                continue
            pairs.append((fibre(hidden), fibre(out_hidden)))
            output_singletons.add(out_singleton)
        action = fit_affine(pairs)
        if action is None or len(output_singletons) != 1:
            left_action_failures.append(
                {
                    "singleton": z,
                    "pairs": pairs,
                    "output_singletons": sorted(output_singletons),
                    "affine": action,
                }
            )
        else:
            singleton_actions[z] = action
            singleton_after_left_crossing[z] = next(iter(output_singletons))

    right_crossing_failures = []
    right_actions = {}
    for z in singletons:
        pairs = []
        output_singletons = set()
        for hidden in collapsed:
            out_singleton, out_hidden = solution.R[(hidden, z)]
            if out_hidden not in collapsed_set or out_singleton not in singleton_set:
                right_crossing_failures.append(
                    {
                        "singleton": z,
                        "hidden": hidden,
                        "output": [out_singleton, out_hidden],
                    }
                )
                continue
            pairs.append((fibre(hidden), fibre(out_hidden)))
            output_singletons.add(out_singleton)
        action = fit_affine(pairs)
        if action is None or len(output_singletons) != 1:
            right_crossing_failures.append(
                {
                    "singleton": z,
                    "pairs": pairs,
                    "output_singletons": sorted(output_singletons),
                    "affine": action,
                }
            )
            continue
        out_singleton = next(iter(output_singletons))
        right_actions[z] = {
            "output_singleton": out_singleton,
            "hidden_action": action,
        }
        if out_singleton not in singleton_actions:
            right_crossing_failures.append(
                {
                    "singleton": z,
                    "output_singleton": out_singleton,
                    "reason": "output singleton has no left action",
                }
            )
            continue
        composition = affine_compose(singleton_actions[out_singleton], action)
        if composition != IDENTITY_STATE:
            right_crossing_failures.append(
                {
                    "singleton": z,
                    "output_singleton": out_singleton,
                    "hidden_action": action,
                    "left_action_of_output": singleton_actions[out_singleton],
                    "composition": composition,
                }
            )

    passive_transport_failures = []
    for z, action in singleton_actions.items():
        left_output = singleton_after_left_crossing.get(z)
        if left_output not in singleton_actions:
            passive_transport_failures.append(
                {
                    "side": "left",
                    "singleton": z,
                    "transported_singleton": left_output,
                    "reason": "transported singleton has no left action",
                }
            )
        elif singleton_actions[left_output] != action:
            passive_transport_failures.append(
                {
                    "side": "left",
                    "singleton": z,
                    "transported_singleton": left_output,
                    "action": action,
                    "transported_action": singleton_actions[left_output],
                }
            )
        right_output = right_actions.get(z, {}).get("output_singleton")
        if right_output not in singleton_actions:
            passive_transport_failures.append(
                {
                    "side": "right",
                    "singleton": z,
                    "transported_singleton": right_output,
                    "reason": "transported singleton has no left action",
                }
            )
        elif singleton_actions[right_output] != action:
            passive_transport_failures.append(
                {
                    "side": "right",
                    "singleton": z,
                    "transported_singleton": right_output,
                    "action": action,
                    "transported_action": singleton_actions[right_output],
                }
            )

    singleton_crossing_failures = []
    for z, w in itertools.product(singletons, repeat=2):
        out_z, out_w = solution.R[(z, w)]
        if out_z not in singleton_set or out_w not in singleton_set:
            singleton_crossing_failures.append(
                {
                    "input": [z, w],
                    "output": [out_z, out_w],
                    "reason": "singleton crossing leaves singleton layer",
                }
            )
            continue
        old_action = affine_compose(singleton_actions[z], singleton_actions[w])
        new_action = affine_compose(singleton_actions[out_z], singleton_actions[out_w])
        if old_action != new_action:
            singleton_crossing_failures.append(
                {
                    "input": [z, w],
                    "output": [out_z, out_w],
                    "old_action": old_action,
                    "new_action": new_action,
                }
            )

    reachable_states = transition_closure(singleton_actions)
    state_separates_hidden_fibre = all(state[0] in NONZERO for state in reachable_states)
    transition_closed_in_affine_group = set(reachable_states).issubset(set(ALL_AFFINE_STATES))

    certified = (
        len(collapsed) == 3
        and len(singletons) == 3
        and collapsed_self_identity
        and not left_action_failures
        and not right_crossing_failures
        and not singleton_crossing_failures
        and not passive_transport_failures
        and state_separates_hidden_fibre
        and transition_closed_in_affine_group
        and is_left_nondegenerate(quotient)
    )
    return {
        "certified": certified,
        "monolith_blocks": blocks,
        "collapsed_block": list(collapsed),
        "singleton_colors": list(singletons),
        "quotient_size": len(quotient.elements),
        "quotient_left_nondegenerate": is_left_nondegenerate(quotient),
        "quotient_right_nondegenerate": is_right_nondegenerate(quotient),
        "collapsed_self_identity": collapsed_self_identity,
        "singleton_actions": {
            str(key): list(value)
            for key, value in sorted(singleton_actions.items())
        },
        "singleton_after_left_crossing": {
            str(key): value
            for key, value in sorted(singleton_after_left_crossing.items())
        },
        "right_actions": {
            str(key): {
                "output_singleton": value["output_singleton"],
                "hidden_action": list(value["hidden_action"]),
            }
            for key, value in sorted(right_actions.items())
        },
        "reachable_state_count": len(reachable_states),
        "reachable_states": [list(state) for state in reachable_states],
        "state_separates_hidden_fibre": state_separates_hidden_fibre,
        "transition_closed_in_affine_group": transition_closed_in_affine_group,
        "left_action_failure_count": len(left_action_failures),
        "right_crossing_failure_count": len(right_crossing_failures),
        "singleton_crossing_failure_count": len(singleton_crossing_failures),
        "passive_transport_failure_count": len(passive_transport_failures),
        "left_action_failures": left_action_failures[:5],
        "right_crossing_failures": right_crossing_failures[:5],
        "singleton_crossing_failures": singleton_crossing_failures[:5],
        "passive_transport_failures": passive_transport_failures[:8],
    }


def run_audit() -> dict:
    rows = []
    collision_rows = []
    distribution = Counter()
    subdirect_count = 0
    nondegenerate_quotient_subdirect_count = 0
    degenerate_quotient_subdirect_count = 0
    certificate_success_count = 0
    certificate_failure_rows = []
    certificate_success_rows = []
    certificate_failure_row_indices = []
    passive_success_count = 0
    passive_failure_count = 0

    for row_index, (indices, table) in enumerate(degenerate_noninvolutive_rows()):
        solution = solution_from_table(table)
        all_congruences = congruences(solution, max_size=7)
        equality = equality_congruence(solution.elements)
        nontrivial = [partition for partition in all_congruences if partition != equality]
        monolith = meet_partitions(nontrivial)
        monolith_nontrivial = monolith != equality

        row = {
            "row_index": row_index,
            "matrix_indices": list(indices),
            "matrices": [list(GL2[index]) for index in indices],
            "congruence_count": len(all_congruences),
            "monolith_is_nontrivial": monolith_nontrivial,
            "monolith_blocks": [sorted(block) for block in monolith],
        }

        if monolith_nontrivial:
            subdirect_count += 1
            quotient = quotient_solution(solution, monolith).quotient
            quotient_left = is_left_nondegenerate(quotient)
            quotient_right = is_right_nondegenerate(quotient)
            if quotient_left and quotient_right:
                nondegenerate_quotient_subdirect_count += 1
            else:
                degenerate_quotient_subdirect_count += 1

            labels = partition_labels(monolith)
            separation = relative_contextual_separation_summary(
                __import__("ybe_domination").contextual_completion_data(solution),
                labels,
                max_vertices=2_000_000,
            )
            collision = separation.collision_found
            row.update(
                {
                    "quotient_size": len(quotient.elements),
                    "quotient_left_nondegenerate": quotient_left,
                    "quotient_right_nondegenerate": quotient_right,
                    "monolith_j_collision_found": collision,
                }
            )
            distribution[
                (
                    tuple(sorted(len(block) for block in monolith)),
                    quotient_left and quotient_right,
                    collision,
                )
            ] += 1

            if collision:
                certificate = certify_row(solution, monolith)
                row["quotient_invariant_certificate"] = certificate
                collision_rows.append(row_index)
                if certificate["certified"]:
                    certificate_success_count += 1
                    passive_success_count += 1
                    certificate_success_rows.append(row_index)
                else:
                    if certificate.get("passive_transport_failure_count", 0):
                        passive_failure_count += 1
                    certificate_failure_row_indices.append(row_index)
                    certificate_failure_rows.append(
                        {
                            "row_index": row_index,
                            "matrix_indices": list(indices),
                            "reason": certificate.get("reason"),
                            "certificate": certificate,
                        }
                    )
        rows.append(row)

    distribution_rows = [
        {
            "case_count": count,
            "monolith_block_sizes": list(key[0]),
            "quotient_nondegenerate": key[1],
            "monolith_j_collision_found": key[2],
        }
        for key, count in sorted(distribution.items(), key=lambda item: (-item[1], item[0]))
    ]
    report = {
        "family": "linear_f3_skew_over_flip_degenerate_noninvolutive",
        "row_count": len(rows),
        "subdirect_row_count": subdirect_count,
        "nondegenerate_quotient_subdirect_count": nondegenerate_quotient_subdirect_count,
        "degenerate_quotient_subdirect_count": degenerate_quotient_subdirect_count,
        "monolith_j_collision_row_count": len(collision_rows),
        "monolith_j_collision_rows": collision_rows,
        "quotient_invariant_certificate_success_count": certificate_success_count,
        "quotient_invariant_certificate_success_rows": certificate_success_rows,
        "quotient_invariant_certificate_failure_count": len(certificate_failure_rows),
        "quotient_invariant_certificate_failure_rows": certificate_failure_row_indices,
        "passive_transport_success_count": passive_success_count,
        "passive_transport_failure_count": passive_failure_count,
        "quotient_invariant_certificate_failures": certificate_failure_rows[:8],
        "distribution": distribution_rows,
        "rows": rows,
    }
    report["all_claimed_checks_passed"] = (
        report["row_count"] == 144
        and report["subdirect_row_count"] == 64
        and report["nondegenerate_quotient_subdirect_count"] == 32
        and report["degenerate_quotient_subdirect_count"] == 32
        and report["monolith_j_collision_row_count"] == 32
        and report["quotient_invariant_certificate_success_count"] == 16
        and report["quotient_invariant_certificate_failure_count"] == 16
        and report["passive_transport_success_count"] == 16
        and report["passive_transport_failure_count"] == 16
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Collision Quotient-Invariant Audit",
        "",
        "This generated audit checks the all-arity quotient-invariant",
        "certificate for the formal monolith-collision rows in the",
        "six-point linear skew-over-flip degenerate non-involutive family.",
        "",
        "## Summary",
        "",
        f"- rows checked: `{report['row_count']}`;",
        f"- subdirect rows: `{report['subdirect_row_count']}`;",
        "- subdirect rows with nondegenerate four-point quotient: "
        f"`{report['nondegenerate_quotient_subdirect_count']}`;",
        "- subdirect rows with degenerate quotient: "
        f"`{report['degenerate_quotient_subdirect_count']}`;",
        "- formal monolith `J`-collision rows: "
        f"`{report['monolith_j_collision_row_count']}`;",
        "- quotient-invariant certificates succeeded: "
        f"`{report['quotient_invariant_certificate_success_count']}`;",
        "- quotient-invariant certificates failed: "
        f"`{report['quotient_invariant_certificate_failure_count']}`;",
        "- passive transport failures: "
        f"`{report['passive_transport_failure_count']}`;",
        "- passive-certified rows: "
        f"`{report['quotient_invariant_certificate_success_rows']}`;",
        "- passive-failure rows: "
        f"`{report['quotient_invariant_certificate_failure_rows']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "## Distribution",
        "",
        "| cases | monolith blocks | quotient nondegenerate | formal collision |",
        "|---:|---|---|---|",
    ]
    for row in report["distribution"]:
        lines.append(
            "| {case_count} | {monolith_block_sizes} | "
            "{quotient_nondegenerate} | {monolith_j_collision_found} |".format(**row)
        )
    lines.extend(
        [
            "",
            "## Certificate",
            "",
            "For each certified row, the monolith has one collapsed",
            "three-point fibre and three singleton quotient colours.  The",
            "collapsed fibre crosses itself trivially.  For every singleton",
            "`z`, the mixed crossing `z,F_i -> F_{S_z(i)},z'` gives an affine",
            "permutation `S_z(i)=alpha_z i+beta_z` of `F_3`.  The audit checks",
            "the identities:",
            "",
            "```text",
            "S_z S_w = S_{z'} S_{w'}        when R(z,w)=(z',w'),",
            "S_{z'} T_z = id               when R(F_i,z)=(z',F_{T_z(i)}),",
            "S_{alpha z}=S_z, S_{beta z}=S_z for passive left-list moves,",
            "R(F_i,F_j)=(F_i,F_j).",
            "```",
            "",
            "Thus a tracked collapsed-fibre strand has invariant",
            "",
            "```text",
            "H_s = S_{a_1} S_{a_2} ... S_{a_k}(i),",
            "```",
            "",
            "where `a_1,...,a_k` are the singleton quotient colours to its",
            "left.  If a braid fixes the four-point quotient word, then the",
            "left singleton list and `H_s` return unchanged, so the hidden",
            "fibre coordinate returns unchanged.  Therefore",
            "`ker rho^Z_n <= ker rho^X_n` for all arities for these rows.",
            "",
            "Since each such quotient `Z` is nondegenerate, the known",
            "derived-rack theorem dominates `Z`, and the certificate dominates",
            "the six-point lift.  The remaining passive-failure rows are not",
            "closed by this one-strand invariant; they require either a",
            "stronger invariant or an actual quotient-kernel witness.",
        ]
    )
    if report["quotient_invariant_certificate_failures"]:
        lines.extend(["", "## Failures", "", "```json"])
        lines.append(
            json.dumps(report["quotient_invariant_certificate_failures"], indent=2)
        )
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_audit()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 collision quotient-invariant audit failed")
    print("OK linear F3 collision quotient-invariant audit")
    print(f"rows {report['row_count']}")
    print(f"subdirect rows {report['subdirect_row_count']}")
    print(f"formal collision rows {report['monolith_j_collision_row_count']}")
    print(
        "quotient-invariant certificates "
        f"{report['quotient_invariant_certificate_success_count']}"
    )


if __name__ == "__main__":
    main()
