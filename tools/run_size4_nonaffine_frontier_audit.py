from __future__ import annotations

import json
import sys
from itertools import permutations, product
from pathlib import Path
from typing import Iterable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    flip_disjoint_union_solution,
    identity_solution,
    is_involutive_solution,
    rack_solution,
    terminal_branch_triage_audit,
)
from ybe_domination.transducer_certificate import (  # noqa: E402
    MealyTransducer,
    multi_active_factor_certificate_audit,
)

OUT_JSON = ROOT / "proofs" / "size4_nonaffine_frontier_audit.json"
OUT_MD = ROOT / "proofs" / "size4_nonaffine_frontier_audit.md"


F2_SQUARE = tuple(product((0, 1), repeat=2))


def affine_f2_type_a_solution() -> FiniteBraidedSet:
    elements = tuple(product((0, 1), repeat=2))
    table = {}
    for a, b in elements:
        for c, d in elements:
            table[((a, b), (c, d))] = (
                (d, (a + b + d) % 2),
                ((a + c + d + 1) % 2, (a + 1) % 2),
            )
    return FiniteBraidedSet(elements, table)


def permutation_solution_with_toggle() -> FiniteBraidedSet:
    elements = (0, 1)
    return FiniteBraidedSet(
        elements,
        {
            (left, right): (right, 1 - left)
            for left in elements
            for right in elements
        },
    )


def type_b_flip_across_solution() -> FiniteBraidedSet:
    return flip_disjoint_union_solution(
        identity_solution((0, 1)),
        permutation_solution_with_toggle(),
        "T",
        "P",
    )


def _xor(left: Sequence[int], right: Sequence[int]) -> tuple[int, ...]:
    return tuple((a + b) % 2 for a, b in zip(left, right))


def _unit_vector(size: int, index: int) -> tuple[int, ...]:
    return tuple(1 if cursor == index else 0 for cursor in range(size))


def affine_f2_square_model(solution: FiniteBraidedSet) -> dict[str, object]:
    """Test whether a four-point solution is affine over F_2^2 up to relabeling."""

    if len(solution.elements) != 4:
        raise ValueError("affine F_2^2 test only applies to four-point solutions")

    zero = (0, 0, 0, 0)
    basis = tuple(_unit_vector(4, index) for index in range(4))
    elements = solution.elements

    for coordinates in permutations(F2_SQUARE):
        label = dict(zip(elements, coordinates))
        table = {}
        for left, right in product(elements, repeat=2):
            out_left, out_right = solution.R[(left, right)]
            table[label[left] + label[right]] = label[out_left] + label[out_right]

        translation = table[zero]
        columns = tuple(_xor(table[basis_vector], translation) for basis_vector in basis)
        affine = True
        for input_vector, output_vector in table.items():
            predicted = translation
            for bit, column in zip(input_vector, columns):
                if bit:
                    predicted = _xor(predicted, column)
            if predicted != output_vector:
                affine = False
                break
        if affine:
            return {
                "is_affine_over_f2_square_up_to_relabeling": True,
                "label": {repr(element): label[element] for element in elements},
                "translation": translation,
                "linear_columns": columns,
            }

    return {
        "is_affine_over_f2_square_up_to_relabeling": False,
        "label": None,
        "translation": None,
        "linear_columns": None,
    }


def coordinate_degeneracy(solution: FiniteBraidedSet) -> dict[str, object]:
    left_bijective = []
    right_bijective = []
    for left in solution.elements:
        images = [solution.R[(left, right)][0] for right in solution.elements]
        if len(set(images)) == len(solution.elements):
            left_bijective.append(repr(left))
    for right in solution.elements:
        images = [solution.R[(left, right)][1] for left in solution.elements]
        if len(set(images)) == len(solution.elements):
            right_bijective.append(repr(right))
    return {
        "left_degenerate": len(left_bijective) < len(solution.elements),
        "right_degenerate": len(right_bijective) < len(solution.elements),
        "left_bijective_elements": left_bijective,
        "right_bijective_elements": right_bijective,
        "everywhere_left_singular": not left_bijective,
        "everywhere_right_singular": not right_bijective,
    }


def one_state_transducer(
    solution: FiniteBraidedSet,
    output_map: Mapping[object, object],
) -> MealyTransducer:
    state = "q"
    delta = {}
    omega = {}
    for letter in solution.elements:
        delta[(state, letter)] = state
        omega[(state, letter)] = output_map[letter]
    return MealyTransducer((state,), state, delta, omega)


def type_b_active_factor_certificate() -> dict[str, object]:
    trivial = identity_solution((0, 1))
    toggle = permutation_solution_with_toggle()
    target = flip_disjoint_union_solution(trivial, toggle, "T", "P")
    dummy = identity_solution(("dummy",))
    trivial_factor = flip_disjoint_union_solution(trivial, dummy, "T", "D")
    toggle_factor = flip_disjoint_union_solution(dummy, toggle, "D", "P")

    trivial_map = {}
    toggle_map = {}
    for tag, value in target.elements:
        if tag == "T":
            trivial_map[(tag, value)] = ("T", value)
            toggle_map[(tag, value)] = ("D", "dummy")
        else:
            trivial_map[(tag, value)] = ("D", "dummy")
            toggle_map[(tag, value)] = ("P", value)

    audit = multi_active_factor_certificate_audit(
        target,
        (
            (trivial_factor, one_state_transducer(target, trivial_map)),
            (toggle_factor, one_state_transducer(target, toggle_map)),
        ),
    )
    return {
        "proper_factor_sizes": (len(trivial_factor.elements), len(toggle_factor.elements)),
        "finite_conditions_hold": audit.finite_conditions_hold,
        "injectivity_witness": None
        if audit.injectivity_witness is None
        else repr(audit.injectivity_witness),
    }


def model_row(
    name: str,
    solution: FiniteBraidedSet,
    mechanism: str,
    active_certificate: dict[str, object] | None = None,
) -> dict[str, object]:
    triage = terminal_branch_triage_audit(solution)
    return {
        "name": name,
        "element_count": len(solution.elements),
        "is_ybe": solution.is_ybe(),
        "is_involutive": is_involutive_solution(solution),
        "coordinate_degeneracy": coordinate_degeneracy(solution),
        "affine_f2_square_model": affine_f2_square_model(solution),
        "has_flip_across_decomposition": triage.has_flip_across_decomposition,
        "has_point_separating_proper_quotients": (
            triage.has_point_separating_proper_quotients
        ),
        "has_proper_subsolution": triage.has_proper_subsolution,
        "mechanism": mechanism,
        "active_certificate": active_certificate,
    }


def build_report() -> dict[str, object]:
    type_a = affine_f2_type_a_solution()
    type_b = type_b_flip_across_solution()
    return {
        "title": "Size-four non-affine frontier audit",
        "rows": [
            model_row(
                "size4_type_a_affine_f2",
                type_a,
                "all-arity parity/fibre gauge to the two-element cyclic rack",
            ),
            model_row(
                "size4_type_b_flip_across_nonaffine",
                type_b,
                "flip-across union of the two-point identity solution and the two-point toggle permutation solution",
                type_b_active_factor_certificate(),
            ),
        ],
        "remaining_gap": (
            "The repo now contains an explicit non-affine size-four degenerate "
            "non-involutive solution, but it is not a rigid-core candidate: it "
            "is a flip-across union with proper active quotient factors.  The "
            "remaining size-four question is whether any degenerate "
            "non-involutive solution lies outside the Type A affine gauge and "
            "Type B flip-across mechanisms."
        ),
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md"
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Size-Four Non-Affine Frontier Audit",
        "",
        "This generated audit records a finite correction to the size-four",
        "frontier.  The committed Type B representative is genuinely",
        "non-affine over `F_2^2` under every relabeling, but it is already",
        "closed by the flip-across/product-rack mechanism.",
        "",
    ]
    for row in report["rows"]:
        degeneracy = row["coordinate_degeneracy"]
        affine = row["affine_f2_square_model"]
        lines.extend(
            [
                f"## {row['name']}",
                "",
                f"- YBE: `{row['is_ybe']}`;",
                f"- involutive: `{row['is_involutive']}`;",
                f"- left-degenerate: `{degeneracy['left_degenerate']}`;",
                f"- right-degenerate: `{degeneracy['right_degenerate']}`;",
                "- everywhere left singular: "
                f"`{degeneracy['everywhere_left_singular']}`;",
                "- everywhere right singular: "
                f"`{degeneracy['everywhere_right_singular']}`;",
                "- affine over `F_2^2` up to relabeling: "
                f"`{affine['is_affine_over_f2_square_up_to_relabeling']}`;",
                "- flip-across decomposition: "
                f"`{row['has_flip_across_decomposition']}`;",
                "- point-separating proper quotients: "
                f"`{row['has_point_separating_proper_quotients']}`;",
                f"- mechanism: `{row['mechanism']}`.",
                "",
            ]
        )
        if affine["is_affine_over_f2_square_up_to_relabeling"]:
            lines.extend(
                [
                    "Affine witness:",
                    "",
                    f"- label: `{affine['label']}`;",
                    f"- translation: `{affine['translation']}`;",
                    f"- linear columns: `{affine['linear_columns']}`.",
                    "",
                ]
            )
        certificate = row["active_certificate"]
        if certificate is not None:
            lines.extend(
                [
                    "Active-factor certificate:",
                    "",
                    f"- proper factor sizes: `{certificate['proper_factor_sizes']}`;",
                    "- finite conditions hold: "
                    f"`{certificate['finite_conditions_hold']}`;",
                    "- injectivity witness: "
                    f"`{certificate['injectivity_witness']}`.",
                    "",
                ]
            )
    lines.extend(
        [
            "## Remaining Gap",
            "",
            report["remaining_gap"],
            "",
            "## Next Prompt",
            "",
            f"`{report['next_prompt']}`.",
        ]
    )
    return "\n".join(lines) + "\n"


def main(argv: Sequence[str] | None = None) -> int:
    if argv not in (None, ()):
        raise SystemExit("no arguments are supported")
    report = build_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")
    print(OUT_JSON)
    print(OUT_MD)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(tuple(sys.argv[1:])))
