"""Audit the quotient closure of one displayed linear F3 residual row."""

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
    GL2,
    COLORS,
    is_involutive_indices,
    is_nondegenerate,
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
)

OUT_JSON = ROOT / "proofs" / "linear_f3_residual_representative_closure_audit.json"
OUT_MD = ROOT / "proofs" / "linear_f3_residual_representative_closure_audit.md"

P = 3
DISPLAYED_MATRICES = (
    (0, 1, 2, 2),
    (1, 2, 1, 0),
    (0, 1, 2, 1),
    (1, 0, 0, 1),
)


def e(a: int) -> int:
    return a % P


def f(i: int) -> int:
    return P + (i % P)


def is_e(color: int) -> bool:
    return color < P


def fibre(color: int) -> int:
    return color % P


def tagged_word(word: tuple[int, ...]) -> tuple[tuple, ...]:
    next_f_id = 0
    out = []
    for color in word:
        if is_e(color):
            out.append(("e", fibre(color)))
        else:
            out.append(("f", next_f_id, fibre(color)))
            next_f_id += 1
    return tuple(out)


def tag_to_color(tagged) -> int:
    if tagged[0] == "e":
        return e(tagged[1])
    return f(tagged[2])


def color_with_tag(color: int, f_tags: list[int]):
    if is_e(color):
        return ("e", fibre(color))
    return ("f", f_tags.pop(0), fibre(color))


def apply_tagged_pair(solution, word: tuple[tuple, ...], index: int, *, inverse: bool) -> tuple[tuple, ...]:
    left, right = word[index], word[index + 1]
    input_colors = (tag_to_color(left), tag_to_color(right))
    output_colors = (solution.inverse_R if inverse else solution.R)[input_colors]
    f_tags = [item[1] for item in (left, right) if item[0] == "f"]
    tagged_outputs = tuple(color_with_tag(color, f_tags) for color in output_colors)
    if f_tags:
        raise ValueError("not every tagged f-strand was propagated")
    return word[:index] + tagged_outputs + word[index + 2 :]


def h_invariants(word: tuple[tuple, ...]) -> dict[int, int]:
    left_e_values: list[int] = []
    invariants: dict[int, int] = {}
    for item in word:
        if item[0] == "e":
            left_e_values.append(item[1] % P)
            continue
        _, f_id, i = item
        k = len(left_e_values)
        value = ((-1) ** k) * i
        for position, a in enumerate(left_e_values, start=1):
            value += ((-1) ** (position - 1)) * a
        invariants[f_id] = value % P
    return invariants


def displayed_row_index(indices: tuple[int, int, int, int]) -> int | None:
    row_index = 0
    for candidate in itertools.product(range(len(GL2)), repeat=4):
        if not quadruple_is_ybe(candidate):
            continue
        table = table_from_indices(candidate)
        if is_nondegenerate(table) or is_involutive_indices(candidate):
            continue
        if candidate == indices:
            return row_index
        row_index += 1
    return None


def local_rule_checks(solution) -> dict[str, bool]:
    checks = {}
    for a, b in itertools.product(range(P), repeat=2):
        checks[f"e{a}_e{b}"] = solution.R[(e(a), e(b))] == (e(b), e(-a - b))
        checks[f"e{a}_f{b}"] = solution.R[(e(a), f(b))] == (f(a - b), e(a))
        checks[f"f{a}_e{b}"] = solution.R[(f(a), e(b))] == (e(b), f(b - a))
        checks[f"f{a}_f{b}"] = solution.R[(f(a), f(b))] == (f(a), f(b))
    return checks


def invariant_check(solution, max_arity: int) -> dict:
    failures = []
    checked_moves = 0
    for arity in range(1, max_arity + 1):
        for word in itertools.product(COLORS, repeat=arity):
            tagged = tagged_word(tuple(word))
            before = h_invariants(tagged)
            for index in range(arity - 1):
                for inverse in (False, True):
                    checked_moves += 1
                    image = apply_tagged_pair(solution, tagged, index, inverse=inverse)
                    after = h_invariants(image)
                    if before != after:
                        failures.append(
                            {
                                "arity": arity,
                                "word": list(word),
                                "index": index,
                                "inverse": inverse,
                                "before": before,
                                "after": after,
                                "image": [repr(item) for item in image],
                            }
                        )
                        return {
                            "max_arity": max_arity,
                            "checked_moves": checked_moves,
                            "failure_count": len(failures),
                            "failures": failures,
                        }
    return {
        "max_arity": max_arity,
        "checked_moves": checked_moves,
        "failure_count": 0,
        "failures": [],
    }


def run_audit(max_invariant_arity: int = 6) -> dict:
    indices = tuple(GL2.index(matrix) for matrix in DISPLAYED_MATRICES)
    table = table_from_indices(indices)
    solution = solution_from_table(table)
    all_congruences = congruences(solution, max_size=7)
    equality = equality_congruence(solution.elements)
    nontrivial = [
        partition
        for partition in all_congruences
        if partition != equality
    ]
    monolith = meet_partitions(nontrivial)
    quotient = quotient_solution(solution, monolith).quotient
    quotient_left_nondegenerate = all(
        {quotient.R[(x, y)][0] for y in quotient.elements} == set(quotient.elements)
        for x in quotient.elements
    )
    quotient_right_nondegenerate = all(
        {quotient.R[(x, y)][1] for x in quotient.elements} == set(quotient.elements)
        for y in quotient.elements
    )
    rules = local_rule_checks(solution)
    invariant = invariant_check(solution, max_invariant_arity)
    report = {
        "family": "linear_f3_skew_over_flip_degenerate_noninvolutive",
        "row_index": displayed_row_index(indices),
        "matrix_indices": list(indices),
        "matrices": [list(matrix) for matrix in DISPLAYED_MATRICES],
        "is_ybe": solution.is_ybe(),
        "is_nondegenerate": is_nondegenerate(table),
        "is_involutive": is_involutive_indices(indices),
        "congruence_count": len(all_congruences),
        "monolith_blocks": [sorted(block) for block in monolith],
        "monolith_block_sizes": sorted(len(block) for block in monolith),
        "quotient_size": len(quotient.elements),
        "quotient_left_nondegenerate": quotient_left_nondegenerate,
        "quotient_right_nondegenerate": quotient_right_nondegenerate,
        "local_rule_failure_count": sum(1 for value in rules.values() if not value),
        "local_rule_checks": rules,
        "invariant_check": invariant,
    }
    report["all_claimed_checks_passed"] = (
        report["row_index"] == 20
        and report["matrix_indices"] == [5, 26, 4, 12]
        and report["is_ybe"]
        and not report["is_nondegenerate"]
        and not report["is_involutive"]
        and report["monolith_block_sizes"] == [1, 1, 1, 3]
        and report["quotient_size"] == 4
        and report["quotient_left_nondegenerate"]
        and report["local_rule_failure_count"] == 0
        and report["invariant_check"]["failure_count"] == 0
    )
    return report


def write_markdown(report: dict) -> str:
    lines = [
        "# Linear F3 Residual Representative Closure Audit",
        "",
        "This generated audit checks the displayed six-point residual",
        "representative closed by the quotient-and-alternating-sum invariant.",
        "",
        "## Summary",
        "",
        f"- degenerate non-involutive row index: `{report['row_index']}`;",
        f"- matrix indices: `{report['matrix_indices']}`;",
        f"- YBE: `{report['is_ybe']}`;",
        f"- nondegenerate: `{report['is_nondegenerate']}`;",
        f"- involutive: `{report['is_involutive']}`;",
        f"- monolith blocks: `{report['monolith_blocks']}`;",
        f"- quotient size: `{report['quotient_size']}`;",
        f"- quotient left-nondegenerate: `{report['quotient_left_nondegenerate']}`;",
        f"- local rule failures: `{report['local_rule_failure_count']}`;",
        "- invariant checked moves through arity "
        f"`{report['invariant_check']['max_arity']}`: "
        f"`{report['invariant_check']['checked_moves']}`;",
        "- invariant failure count: "
        f"`{report['invariant_check']['failure_count']}`;",
        f"- all claimed checks passed: `{report['all_claimed_checks_passed']}`.",
        "",
        "## Consequence",
        "",
        "The executable audit verifies the finite bookkeeping behind the",
        "all-arity proof note: the monolith collapses the three `f_i` points,",
        "the four-point quotient is left-nondegenerate, and the stated",
        "alternating-sum quantity is preserved by positive and negative local",
        "crossings in all tested arities.  The symbolic proof gives the",
        "all-arity kernel inclusion.",
    ]
    if report["invariant_check"]["failures"]:
        lines.extend(["", "## Invariant Failures", "", "```json"])
        lines.append(json.dumps(report["invariant_check"]["failures"], indent=2))
        lines.append("```")
    return "\n".join(lines) + "\n"


def main() -> None:
    report = run_audit()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(write_markdown(report), encoding="utf-8")
    if not report["all_claimed_checks_passed"]:
        raise SystemExit("linear F3 residual representative closure audit failed")
    print("OK linear F3 residual representative closure audit")
    print(f"row {report['row_index']}")
    print(f"invariant checked moves {report['invariant_check']['checked_moves']}")


if __name__ == "__main__":
    main()
