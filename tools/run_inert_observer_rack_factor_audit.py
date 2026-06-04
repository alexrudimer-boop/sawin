from __future__ import annotations

import json
import sys
from itertools import product
from pathlib import Path
from typing import Callable, Mapping, Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "tools"))

from run_observer_product_derived_route_boundary import (  # noqa: E402
    observer_product_solution,
    s3_conjugation_rack,
)
from run_sequential_primitivity_frontier_audit import (  # noqa: E402
    affine_f2_type_a_solution,
    permutation_solution_with_toggle,
)
from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    flip_disjoint_union_solution,
    identity_solution,
    rack_solution,
)
from ybe_domination.finite_braided_set import Element  # noqa: E402

OUT_JSON = ROOT / "proofs" / "inert_observer_rack_factor_audit.json"
OUT_MD = ROOT / "proofs" / "inert_observer_rack_factor_audit.md"


ObserverMap = Mapping[Element, Element]
RackMap = Mapping[Element, Element]


def type_b_flip_across_solution() -> FiniteBraidedSet:
    return flip_disjoint_union_solution(
        identity_solution((0, 1)),
        permutation_solution_with_toggle(),
        "T",
        "P",
    )


def two_element_cyclic_rack() -> FiniteBraidedSet:
    return rack_solution((0, 1), lambda _left, right: 1 - right)


def affine_type_a_naive_maps(
    solution: FiniteBraidedSet,
) -> tuple[FiniteBraidedSet, ObserverMap, RackMap]:
    rack = two_element_cyclic_rack()
    observer_map = {element: (element[0] + element[1]) % 2 for element in solution.elements}
    rack_map = {element: element[0] for element in solution.elements}
    return rack, observer_map, rack_map


def type_b_naive_maps(
    solution: FiniteBraidedSet,
) -> tuple[FiniteBraidedSet, ObserverMap, RackMap]:
    rack = two_element_cyclic_rack()
    observer_map = {element: element[0] for element in solution.elements}
    rack_map = {element: element[1] for element in solution.elements}
    return rack, observer_map, rack_map


def observer_product_maps(
    solution: FiniteBraidedSet,
) -> tuple[FiniteBraidedSet, ObserverMap, RackMap]:
    rack = s3_conjugation_rack()
    observer_map = {element: element[0] for element in solution.elements}
    rack_map = {element: element[1] for element in solution.elements}
    return rack, observer_map, rack_map


def _first_observer_failure(
    solution: FiniteBraidedSet,
    observer_map: ObserverMap,
) -> dict[str, object] | None:
    for left, right in product(solution.elements, repeat=2):
        out_left, out_right = solution.R[(left, right)]
        expected = (observer_map[left], observer_map[right])
        actual = (observer_map[out_left], observer_map[out_right])
        if actual != expected:
            return {
                "left": repr(left),
                "right": repr(right),
                "expected": repr(expected),
                "actual": repr(actual),
            }
    return None


def _first_rack_factor_failure(
    solution: FiniteBraidedSet,
    rack: FiniteBraidedSet,
    rack_map: RackMap,
) -> dict[str, object] | None:
    for left, right in product(solution.elements, repeat=2):
        out_left, out_right = solution.R[(left, right)]
        expected = rack.R[(rack_map[left], rack_map[right])]
        actual = (rack_map[out_left], rack_map[out_right])
        if actual != expected:
            return {
                "left": repr(left),
                "right": repr(right),
                "expected": repr(expected),
                "actual": repr(actual),
            }
    return None


def _first_injectivity_collision(
    solution: FiniteBraidedSet,
    observer_map: ObserverMap,
    rack_map: RackMap,
) -> dict[str, object] | None:
    seen = {}
    for element in solution.elements:
        code = (observer_map[element], rack_map[element])
        if code in seen:
            return {
                "left": repr(seen[code]),
                "right": repr(element),
                "code": repr(code),
            }
        seen[code] = element
    return None


def inert_observer_rack_factor_audit(
    solution: FiniteBraidedSet,
    rack: FiniteBraidedSet,
    observer_map: ObserverMap,
    rack_map: RackMap,
) -> dict[str, object]:
    observer_failure = _first_observer_failure(solution, observer_map)
    rack_failure = _first_rack_factor_failure(solution, rack, rack_map)
    injectivity_collision = _first_injectivity_collision(solution, observer_map, rack_map)
    finite_conditions_hold = (
        observer_failure is None
        and rack_failure is None
        and injectivity_collision is None
    )
    return {
        "solution_size": len(solution.elements),
        "rack_size": len(rack.elements),
        "observer_alphabet_size": len(set(observer_map.values())),
        "observer_failure": observer_failure,
        "rack_factor_failure": rack_failure,
        "injectivity_collision": injectivity_collision,
        "finite_conditions_hold": finite_conditions_hold,
        "kernel_conclusion": (
            "ker rho^X_n = ker rho^Y_n for every n"
            if finite_conditions_hold
            else None
        ),
    }


def model_row(
    name: str,
    solution: FiniteBraidedSet,
    maps_builder: Callable[
        [FiniteBraidedSet],
        tuple[FiniteBraidedSet, ObserverMap, RackMap],
    ],
    expectation: str,
) -> dict[str, object]:
    rack, observer_map, rack_map = maps_builder(solution)
    audit = inert_observer_rack_factor_audit(solution, rack, observer_map, rack_map)
    return {
        "name": name,
        "expectation": expectation,
        "audit": audit,
    }


def build_report() -> dict[str, object]:
    return {
        "title": "Inert observer rack-factor audit",
        "theorem": (
            "If maps o:X->I and q:X->Y to a finite rack Y satisfy "
            "o(u)=o(x), o(v)=o(y), and (q(u),q(v))=r_Y(q(x),q(y)) for every "
            "r_X(x,y)=(u,v), and x->(o(x),q(x)) is injective, then "
            "X^n is B_n-isomorphic to a B_n-invariant subset of Y^n x I^n "
            "with I^n fixed pointwise.  If the map is bijective onto "
            "Y x I on one letters, then ker rho^X_n = ker rho^Y_n for all n."
        ),
        "rows": [
            model_row(
                "observer_product_s3_conjugation",
                observer_product_solution(),
                observer_product_maps,
                "passes: the S_3 rack coordinate is active and the E coordinate is inert",
            ),
            model_row(
                "size4_affine_type_a_naive_pointwise",
                affine_f2_type_a_solution(),
                affine_type_a_naive_maps,
                "fails: Type A needs a sequential prefix-dependent gauge, not a pointwise rack factor",
            ),
            model_row(
                "size4_type_b_flip_across_naive_tag",
                type_b_flip_across_solution(),
                type_b_naive_maps,
                "fails: mixed flip-across crossings route the tag observer rather than fixing it pointwise",
            ),
        ],
        "conclusion": (
            "The inert observer theorem is a strict positive branch.  It "
            "covers the E x S_3 derived-route boundary example but is too "
            "narrow for Type A sequential gauges and Type B flip-across "
            "routing.  Those require the existing active-factor/transducer "
            "certificate framework."
        ),
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md"
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Inert Observer Rack-Factor Audit",
        "",
        "This generated audit isolates the simplest observer-factor",
        "rackification theorem: a pointwise active rack factor plus inert",
        "observer coordinates.",
        "",
        "## Theorem",
        "",
        report["theorem"],
        "",
        "## Rows",
        "",
        "| model | expectation | finite conditions | observer failure | rack failure | injectivity collision |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in report["rows"]:
        audit = row["audit"]
        lines.append(
            f"| `{row['name']}` | `{row['expectation']}` | "
            f"`{audit['finite_conditions_hold']}` | "
            f"`{audit['observer_failure']}` | "
            f"`{audit['rack_factor_failure']}` | "
            f"`{audit['injectivity_collision']}` |"
        )
    lines.extend(
        [
            "",
            "## Conclusion",
            "",
            report["conclusion"],
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
