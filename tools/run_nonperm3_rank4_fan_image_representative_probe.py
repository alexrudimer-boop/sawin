from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "src"))

from tools.run_nonperm3_rank2_brunnian_law_escape_audit import (  # noqa: E402
    _pure_generator_word,
)
from ybe_domination import (  # noqa: E402
    action_permutation_from_generators,
    generator_action_permutations,
)
from ybe_domination.nonperm3_endpoint_detector_basis import (  # noqa: E402
    nonpermutation_size3_solutions,
)
from ybe_domination.semigroup_shadows import (  # noqa: E402
    compose_permutations,
    generated_permutation_group,
    permutation_group_exponent,
    permutation_order,
)


OUT_JSON = ROOT / "proofs" / "nonperm3_rank4_fan_image_representative_probe.json"
OUT_MD = ROOT / "proofs" / "nonperm3_rank4_fan_image_representative_probe.md"

RANK = 4
ARITY = RANK + 1
MAX_GROUP_SIZE = 200_000
REPRESENTATIVE_ROWS = {
    "trivial_representative": 0,
    "abelian_representative": 6,
    "hard_representative": 15,
}


def _rank4_fan_generator_permutations(solution) -> tuple[tuple[int, ...], ...]:
    signed_artin_generators = generator_action_permutations(solution, ARITY)
    state_count = len(solution.elements) ** ARITY
    return tuple(
        action_permutation_from_generators(
            signed_artin_generators,
            state_count,
            _pure_generator_word(anchor, ARITY),
        )
        for anchor in range(1, ARITY)
    )


def _generators_commute(generators: tuple[tuple[int, ...], ...]) -> bool:
    return all(
        compose_permutations(left, right) == compose_permutations(right, left)
        for left_index, left in enumerate(generators)
        for right in generators[left_index + 1 :]
    )


def _profile_for_row(solution_index: int, solution) -> dict[str, Any]:
    generators = _rank4_fan_generator_permutations(solution)
    elements = generated_permutation_group(
        generators,
        max_size=MAX_GROUP_SIZE,
    )
    return {
        "solution_index": solution_index,
        "order": len(elements),
        "exponent": permutation_group_exponent(elements),
        "generator_orders": [
            permutation_order(generator) for generator in generators
        ],
        "generator_pair_product_orders": [
            permutation_order(compose_permutations(generators[i], generators[j]))
            for i in range(len(generators))
            for j in range(i + 1, len(generators))
        ],
        "is_abelian": _generators_commute(generators),
    }


def build_report() -> dict[str, Any]:
    solutions = dict(nonpermutation_size3_solutions())
    rows = {
        name: _profile_for_row(index, solutions[index])
        for name, index in REPRESENTATIVE_ROWS.items()
    }
    return {
        "title": "Nonpermutation size-3 rank-4 fan-image representative probe",
        "solution_family": "55 nonpermutation size-3 bijective YBE solutions",
        "rank": RANK,
        "arity": ARITY,
        "state_count": 3**ARITY,
        "max_group_size": MAX_GROUP_SIZE,
        "representative_rows": REPRESENTATIVE_ROWS,
        "rows": rows,
        "conclusion": (
            "The first rank-4 representative probe closes the row-15 hard "
            "fan image at order 51840.  The sampled easy representatives "
            "remain trivial or elementary abelian.  This is not a full "
            "rank-4 corpus classification; it identifies the first concrete "
            "higher-rank hard fan-image group that a uniform marked-variety "
            "proof must control."
        ),
    }


def render_markdown(report: dict[str, Any]) -> str:
    lines = [
        f"# {report['title']}",
        "",
        report["conclusion"],
        "",
        f"- solution family: `{report['solution_family']}`;",
        f"- rank: `{report['rank']}`;",
        f"- arity: `{report['arity']}`;",
        f"- state count: `{report['state_count']}`;",
        f"- max group size: `{report['max_group_size']}`;",
        f"- representative rows: `{report['representative_rows']}`;",
        "",
        "## Representative profiles",
        "",
        "| label | row | order | exponent | generator orders | pair-product orders | abelian |",
        "| --- | ---: | ---: | ---: | --- | --- | --- |",
    ]
    for label, row in report["rows"].items():
        lines.append(
            "| {label} | {solution_index} | {order} | {exponent} | "
            "`{generator_orders}` | `{generator_pair_product_orders}` | "
            "{is_abelian} |".format(label=label, **row)
        )
    lines.extend(
        [
            "",
            "## Scope",
            "",
            "This probe deliberately checks representatives only.  It does not "
            "prove that every hard rank-4 row is marked-isomorphic to the "
            "row-15 image, and it does not prove the uniform Brunnian "
            "fan-evaluation lemma.  It supplies the next finite pressure "
            "point after the rank-2 H24 and rank-3 F648 audits.",
            "",
        ]
    )
    return "\n".join(lines)


def main() -> None:
    report = build_report()
    OUT_JSON.write_text(json.dumps(report, indent=2, sort_keys=True), encoding="utf-8")
    OUT_MD.write_text(render_markdown(report), encoding="utf-8")


if __name__ == "__main__":
    main()

