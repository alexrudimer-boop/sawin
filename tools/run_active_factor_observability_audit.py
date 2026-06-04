from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    InvariantTransducer,
    MealyTransducer,
    active_factor_certificate_audit,
    identity_solution,
    is_left_nondegenerate,
    multi_active_factor_certificate_audit,
    product_solution,
    rack_solution,
)

OUT_JSON = ROOT / "proofs" / "active_factor_observability_audit.json"
OUT_MD = ROOT / "proofs" / "active_factor_observability_audit.md"


def flip_solution(elements: Sequence[int]) -> FiniteBraidedSet:
    elems = tuple(elements)
    return FiniteBraidedSet(elems, {(left, right): (right, left) for left in elems for right in elems})


def one_state_mealy(solution: FiniteBraidedSet, output_map) -> MealyTransducer:
    state = "q"
    delta = {}
    omega = {}
    for letter in solution.elements:
        delta[(state, letter)] = state
        omega[(state, letter)] = output_map(letter)
    return MealyTransducer((state,), state, delta, omega)


def one_state_invariant(solution: FiniteBraidedSet, output_map) -> InvariantTransducer:
    state = "p"
    delta = {}
    nu = {}
    for letter in solution.elements:
        delta[(state, letter)] = state
        nu[(state, letter)] = output_map(letter)
    return InvariantTransducer((state,), state, delta, nu)


def counter_state_mealy(
    solution: FiniteBraidedSet,
    modulus: int,
    output_map,
) -> MealyTransducer:
    states = tuple(range(modulus))
    delta = {}
    omega = {}
    for state in states:
        for letter in solution.elements:
            delta[(state, letter)] = (state + 1) % modulus
            omega[(state, letter)] = output_map(state, letter)
    return MealyTransducer(states, 0, delta, omega)


def identity_base_cyclic_transport_solution() -> FiniteBraidedSet:
    colors = (0, 1)
    points = (0, 1, 2)
    elements = tuple(product(colors, points))
    table = {}
    for left_color, left_point in elements:
        for right_color, right_point in elements:
            table[((left_color, left_point), (right_color, right_point))] = (
                (left_color, right_point),
                (right_color, (left_point + 1) % 3),
            )
    return FiniteBraidedSet(elements, table)


def flip_base_cyclic_transport_solution() -> tuple[FiniteBraidedSet, FiniteBraidedSet, FiniteBraidedSet]:
    colors = (0, 1)
    points = (0, 1, 2)
    quotient = flip_solution(colors)
    fibre = FiniteBraidedSet(
        points,
        {
            (left, right): ((right + 1) % 3, (left + 1) % 3)
            for left in points
            for right in points
        },
    )
    return product_solution(quotient, fibre), quotient, fibre


def dihedral_quotient_inert_fibre_solution() -> tuple[FiniteBraidedSet, FiniteBraidedSet]:
    quotient = rack_solution((0, 1, 2), lambda left, right: (2 * left - right) % 3)
    fibre = identity_solution((0, 1))
    return product_solution(quotient, fibre), quotient


def quotient_colour_path(
    quotient: FiniteBraidedSet,
    word: Sequence[int],
    base_tuple: Sequence[int],
) -> tuple[tuple[int, ...], ...]:
    path = [tuple(base_tuple)]
    current = tuple(base_tuple)
    for generator in word:
        current = quotient.braid_action((generator,), current)
        path.append(current)
    return tuple(path)


def identity_base_cyclic_active_factor_report() -> dict:
    solution = identity_base_cyclic_transport_solution()
    cyclic = rack_solution((0, 1, 2), lambda _left, right: (right + 1) % 3)
    transducer = counter_state_mealy(
        solution,
        3,
        lambda state, letter: (letter[1] - state - 1) % 3,
    )
    invariant = one_state_invariant(solution, lambda letter: letter[0])
    audit = active_factor_certificate_audit(
        solution,
        cyclic,
        transducer,
        invariant,
    )
    return {
        "name": "identity_base_cyclic_transport",
        "description": "r((a,x),(b,y))=((a,y),(b,x+1))",
        "solution_size": len(solution.elements),
        "factor_size": len(cyclic.elements),
        "state_count": len(transducer.states),
        "invariant_state_count": len(invariant.states),
        "factor_is_rack": True,
        "finite_conditions_hold": audit.finite_conditions_hold,
        "factor_failure_count": len(audit.factor_failures),
        "invariant_failure_count": len(audit.invariant_failures),
        "injectivity_witness": None
        if audit.injectivity_witness is None
        else {
            "left": repr(audit.injectivity_witness.left_word),
            "right": repr(audit.injectivity_witness.right_word),
            "length": audit.injectivity_witness.length,
        },
        "position_gauge": "u_i = x_i - i mod 3",
        "observer": "colour a",
    }


def flip_base_cyclic_active_factor_report() -> dict:
    solution, quotient, fibre = flip_base_cyclic_transport_solution()
    quotient_map = {element: element[0] for element in solution.elements}
    transducer = one_state_mealy(solution, lambda letter: letter[1])
    audit = active_factor_certificate_audit(
        solution,
        fibre,
        transducer,
        quotient=quotient,
        quotient_map=quotient_map,
    )
    return {
        "name": "flip_base_cyclic_transport",
        "description": "r((a,i),(b,j))=((b,j+1),(a,i+1))",
        "solution_size": len(solution.elements),
        "quotient_size": len(quotient.elements),
        "factor_size": len(fibre.elements),
        "factor_left_nondegenerate": is_left_nondegenerate(fibre),
        "proper_factor": len(fibre.elements) < len(solution.elements),
        "finite_conditions_hold": audit.finite_conditions_hold,
        "quotient_failure_count": len(audit.quotient_failures),
        "factor_failure_count": len(audit.factor_failures),
        "injectivity_witness": None
        if audit.injectivity_witness is None
        else {
            "left": repr(audit.injectivity_witness.left_word),
            "right": repr(audit.injectivity_witness.right_word),
            "length": audit.injectivity_witness.length,
        },
        "monodromy_witness": "sigma_1^2 sends ((0,0),(1,0)) to ((0,2),(1,2))",
    }


def dihedral_quotient_inert_active_factor_report() -> dict:
    solution, quotient = dihedral_quotient_inert_fibre_solution()
    quotient_map = {element: element[0] for element in solution.elements}
    invariant = one_state_invariant(solution, lambda letter: letter[1])
    audit = multi_active_factor_certificate_audit(
        solution,
        (),
        invariant_transducer=invariant,
        quotient=quotient,
        quotient_map=quotient_map,
    )
    routing_word = (1, 1, 1)
    routing_base = (0, 1)
    routing_path = quotient_colour_path(quotient, routing_word, routing_base)
    return {
        "name": "dihedral_quotient_inert_fibre",
        "description": "r((a,i),(b,j))=((a*b,i),(a,j)), a*b=2a-b mod 3",
        "solution_size": len(solution.elements),
        "quotient_size": len(quotient.elements),
        "active_factor_count": 0,
        "observer": "inert fibre coordinate i",
        "finite_conditions_hold": audit.finite_conditions_hold,
        "quotient_failure_count": len(audit.quotient_failures),
        "invariant_failure_count": len(audit.invariant_failures),
        "injectivity_witness": None
        if audit.injectivity_witness is None
        else {
            "left": repr(audit.injectivity_witness.left_word),
            "right": repr(audit.injectivity_witness.right_word),
            "length": audit.injectivity_witness.length,
        },
        "returning_quotient_word": routing_word,
        "returning_quotient_path": routing_path,
        "changes_colours_midword": any(
            state != routing_path[0] for state in routing_path[1:-1]
        ),
    }


def build_report() -> dict:
    examples = (
        identity_base_cyclic_active_factor_report(),
        flip_base_cyclic_active_factor_report(),
        dihedral_quotient_inert_active_factor_report(),
    )
    return {
        "title": "Active-factor observability audit",
        "examples": examples,
        "all_examples_closed_by_certificate": all(
            example["finite_conditions_hold"] for example in examples
        ),
        "consequence": (
            "The finite monodromy and quotient-routing proof gaps are not "
            "negative evidence by themselves: both are absorbed by proper "
            "active-factor or quotient+observer certificates in these "
            "witnesses. The unresolved theorem is universal existence of "
            "such certificates, or a cofinal rack-prefix obstruction."
        ),
    }


def _render_witness(value) -> str:
    return "`None`" if value is None else f"`{value}`"


def render_markdown(report: dict) -> str:
    lines = [
        "# Active-Factor Observability Audit",
        "",
        "This generated audit checks the active-factor repair on the finite",
        "transport-gluing proof-gap examples.  It is not a proof of Sawin's",
        "question.  It shows that the known monodromy and quotient-routing",
        "gaps are absorbed by finite certificates in these witnesses, so the",
        "remaining issue is the universal existence theorem.",
        "",
        f"- all examples closed by certificate: `{report['all_examples_closed_by_certificate']}`.",
    ]
    for example in report["examples"]:
        lines.extend(
            [
                "",
                f"## {example['name']}",
                "",
                f"- description: `{example['description']}`;",
                f"- solution size: `{example['solution_size']}`;",
                f"- finite conditions hold: `{example['finite_conditions_hold']}`;",
            ]
        )
        for key in (
            "quotient_size",
            "factor_size",
            "state_count",
            "invariant_state_count",
            "active_factor_count",
            "proper_factor",
            "factor_left_nondegenerate",
            "factor_is_rack",
            "observer",
            "position_gauge",
            "monodromy_witness",
            "returning_quotient_word",
            "returning_quotient_path",
            "changes_colours_midword",
        ):
            if key in example:
                lines.append(f"- {key}: `{example[key]}`;")
        for key in (
            "quotient_failure_count",
            "factor_failure_count",
            "invariant_failure_count",
        ):
            if key in example:
                lines.append(f"- {key}: `{example[key]}`;")
        lines.append(
            f"- injectivity witness: {_render_witness(example['injectivity_witness'])}."
        )
    lines.extend(
        [
            "",
            "## Consequence",
            "",
            report["consequence"],
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
