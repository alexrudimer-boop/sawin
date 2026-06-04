from __future__ import annotations

import json
import sys
from itertools import permutations, product
from pathlib import Path
from typing import Sequence

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from ybe_domination import (  # noqa: E402
    FiniteBraidedSet,
    identity_solution,
    is_involutive_solution,
    product_solution,
    rack_solution,
)

OUT_JSON = ROOT / "proofs" / "observer_product_derived_route_boundary.json"
OUT_MD = ROOT / "proofs" / "observer_product_derived_route_boundary.md"

Permutation = tuple[int, ...]
Element = tuple[int, Permutation]


def compose(left: Permutation, right: Permutation) -> Permutation:
    """Return left after right."""

    return tuple(left[right[index]] for index in range(len(left)))


def invert(permutation: Permutation) -> Permutation:
    inverse = [0] * len(permutation)
    for index, image in enumerate(permutation):
        inverse[image] = index
    return tuple(inverse)


def conjugate(left: Permutation, right: Permutation) -> Permutation:
    return compose(compose(left, right), invert(left))


def s3_elements() -> tuple[Permutation, ...]:
    return tuple(permutations((0, 1, 2)))


def permutation_name(permutation: Permutation) -> str:
    names = {
        (0, 1, 2): "1",
        (1, 2, 0): "a",
        (2, 0, 1): "a^2",
        (1, 0, 2): "s",
        (0, 2, 1): "t",
        (2, 1, 0): "u",
    }
    return names.get(permutation, repr(permutation))


def s3_conjugation_rack() -> FiniteBraidedSet:
    elements = s3_elements()
    return rack_solution(elements, conjugate)


def observer_product_solution() -> FiniteBraidedSet:
    return product_solution(identity_solution((0, 1)), s3_conjugation_rack())


def lambda_image_sizes(solution: FiniteBraidedSet) -> tuple[int, ...]:
    sizes = []
    for left in solution.elements:
        images = {solution.R[(left, right)][0] for right in solution.elements}
        sizes.append(len(images))
    return tuple(sizes)


def rho_image_sizes(solution: FiniteBraidedSet) -> tuple[int, ...]:
    sizes = []
    for right in solution.elements:
        images = {solution.R[(left, right)][1] for left in solution.elements}
        sizes.append(len(images))
    return tuple(sizes)


def fixed_point_counts_for_lambdas(solution: FiniteBraidedSet) -> dict[str, int]:
    counts = {}
    for left in solution.elements:
        count = 0
        for right in solution.elements:
            if solution.R[(left, right)][0] == right:
                count += 1
        observer, permutation = left
        counts[f"({observer},{permutation_name(permutation)})"] = count
    return counts


def quasi_left_failure_witness() -> dict[str, object]:
    identity = (0, 1, 2)
    x = (0, identity)
    y = (1, identity)
    z = (0, identity)

    def lam(left: Element, value: Element) -> Element:
        left_observer, left_group = left
        _value_observer, value_group = value
        return (left_observer, conjugate(left_group, value_group))

    def lam_zero(left: Element, value: Element) -> Element:
        left_observer, _left_group = left
        _value_observer, value_group = value
        return (left_observer, value_group)

    left_side = lam_zero(x, lam(y, z))
    right_side = lam(y, lam_zero(x, z))
    return {
        "x": repr((x[0], permutation_name(x[1]))),
        "y": repr((y[0], permutation_name(y[1]))),
        "z": repr((z[0], permutation_name(z[1]))),
        "lambda_x0_lambda_y_z": repr((left_side[0], permutation_name(left_side[1]))),
        "lambda_y_lambda_x0_z": repr((right_side[0], permutation_name(right_side[1]))),
        "commutes": left_side == right_side,
    }


def split_equivariance_check(max_arity: int = 4) -> dict[str, object]:
    solution = observer_product_solution()
    rack = s3_conjugation_rack()
    failures = []
    for arity in range(2, max_arity + 1):
        for generator in range(1, arity):
            for word in product(solution.elements, repeat=arity):
                image = solution.braid_action((generator,), word)
                observer_before = tuple(entry[0] for entry in word)
                observer_after = tuple(entry[0] for entry in image)
                group_before = tuple(entry[1] for entry in word)
                group_after = tuple(entry[1] for entry in image)
                expected_group_after = rack.braid_action((generator,), group_before)
                if observer_after != observer_before or group_after != expected_group_after:
                    failures.append(
                        {
                            "arity": arity,
                            "generator": generator,
                            "word": repr(word),
                            "image": repr(image),
                        }
                    )
                    return {
                        "max_arity": max_arity,
                        "checked": False,
                        "first_failure": failures[0],
                    }
    return {"max_arity": max_arity, "checked": True, "first_failure": None}


def conjugation_table() -> list[list[str]]:
    elements = s3_elements()
    return [
        [permutation_name(conjugate(left, right)) for right in elements]
        for left in elements
    ]


def build_report() -> dict[str, object]:
    solution = observer_product_solution()
    lambda_sizes = lambda_image_sizes(solution)
    rho_sizes = rho_image_sizes(solution)
    fixed_counts = fixed_point_counts_for_lambdas(solution)
    return {
        "title": "Observer-product derived-route boundary",
        "solution": (
            "X={0,1} x S_3 with r((e,g),(f,h))=((e,ghg^{-1}),(f,g))"
        ),
        "s3_order": [permutation_name(element) for element in s3_elements()],
        "s3_conjugation_table": conjugation_table(),
        "is_ybe": solution.is_ybe(),
        "is_involutive": is_involutive_solution(solution),
        "lambda_image_sizes": lambda_sizes,
        "rho_image_sizes": rho_sizes,
        "everywhere_left_singular": all(size < len(solution.elements) for size in lambda_sizes),
        "everywhere_right_singular": all(size < len(solution.elements) for size in rho_sizes),
        "lambda_fixed_point_counts": fixed_counts,
        "nonaffine_reason": (
            "For any affine model over an abelian group, every nonempty fixed "
            "set of lambda_x has cardinality |ker(1-B)|.  Here all lambda_x "
            "have fixed points, but the counts vary with S_3 centralizer "
            "sizes."
        ),
        "classical_derived_status": (
            "undefined: no lambda_x is surjective, so lambda_y^{-1}(x) is "
            "empty for half of the possible observer fibers"
        ),
        "quasi_left_failure_witness": quasi_left_failure_witness(),
        "split_equivariance_check": split_equivariance_check(),
        "all_arity_kernel_statement": (
            "Projection to S_3^n is the conjugation-rack action and projection "
            "to {0,1}^n is fixed pointwise.  Hence rho^X_n is rho^{S_3-conj}_n "
            "times a trivial observer factor, so the kernels are equal for "
            "all n."
        ),
        "conclusion": (
            "The example is finite, bijective, everywhere degenerate, "
            "non-involutive, and non-affine.  Classical and quasi-derived "
            "routes fail, but the solution is still rack-kernel equivalent to "
            "the S_3 conjugation rack via an inert observer product."
        ),
        "next_prompt": (
            "prompts/gpt55_pro/"
            "2026-06-04-size5-6-everywhere-singular-core-search_ask_now.md"
        ),
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Observer-Product Derived-Route Boundary",
        "",
        "This generated audit records a concrete finite degenerate example",
        "where the classical derived solution and quasi-rack derived route",
        "do not apply, while rack domination is still immediate from an",
        "active rack factor plus inert observer coordinates.",
        "",
        "## Solution",
        "",
        f"`{report['solution']}`.",
        "",
        "The `S_3` order used in the table is:",
        "",
        f"`{report['s3_order']}`.",
        "",
        "The conjugation table is:",
        "",
    ]
    for row in report["s3_conjugation_table"]:
        lines.append(f"- `{row}`;")
    lines.extend(
        [
            "",
            "## Finite Checks",
            "",
            f"- YBE: `{report['is_ybe']}`;",
            f"- involutive: `{report['is_involutive']}`;",
            f"- lambda image sizes: `{report['lambda_image_sizes']}`;",
            f"- rho image sizes: `{report['rho_image_sizes']}`;",
            f"- everywhere left singular: `{report['everywhere_left_singular']}`;",
            f"- everywhere right singular: `{report['everywhere_right_singular']}`;",
            "- lambda fixed-point counts: "
            f"`{report['lambda_fixed_point_counts']}`.",
            "",
            "## Non-Affine Reason",
            "",
            report["nonaffine_reason"],
            "",
            "## Derived Route Failure",
            "",
            f"- classical derived status: `{report['classical_derived_status']}`;",
            "- quasi-left failure witness: "
            f"`{report['quasi_left_failure_witness']}`.",
            "",
            "## Rack Domination",
            "",
            f"- split equivariance check: `{report['split_equivariance_check']}`;",
            "",
            report["all_arity_kernel_statement"],
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
